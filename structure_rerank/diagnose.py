from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Tuple

from .evaluate import DEFAULT_JUDGMENTS, load_judgments
from .rerank import DEFAULT_OUTPUT, DEFAULT_QUERIES, run as run_rerank
from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIAGNOSTICS_MD = ROOT / "results" / "diagnostics.md"
DEFAULT_DIAGNOSTICS_JSON = ROOT / "results" / "diagnostics.json"


def group_results(rows: List[Mapping[str, Any]]) -> Dict[str, Dict[str, List[Mapping[str, Any]]]]:
    grouped: Dict[str, Dict[str, List[Mapping[str, Any]]]] = {}
    for row in rows:
        grouped.setdefault(str(row["mode"]), {}).setdefault(str(row["query_id"]), []).append(row)
    for mode_rows in grouped.values():
        for query_rows in mode_rows.values():
            query_rows.sort(key=lambda item: int(item["rank"]))
    return grouped


def load_query_intents(path: Path) -> Dict[str, str]:
    intents: Dict[str, str] = {}
    for row in load_jsonl(path):
        intents[str(row["id"])] = str(row.get("intent_structure", ""))
    return intents


def mode_structure_type(mode: str) -> str | None:
    prefix = "structure_"
    suffix = "_only"
    if mode.startswith(prefix) and mode.endswith(suffix):
        return mode[len(prefix) : -len(suffix)]
    return None


def avg_rel(rows: List[Mapping[str, Any]], judgments: Dict[Tuple[str, str], int], k: int) -> float:
    observed = rows[:k]
    if not observed:
        return 0.0
    return sum(judgments.get((str(row["query_id"]), str(row["post_id"])), 0) for row in observed) / len(observed)


def diagnose(results_path: Path, judgments_path: Path, queries_path: Path, k: int) -> Dict[str, Any]:
    rows = load_jsonl(results_path)
    judgments = load_judgments(judgments_path)
    query_intents = load_query_intents(queries_path)
    grouped = group_results(rows)
    modes = sorted(grouped)
    query_ids = sorted({query_id for mode_rows in grouped.values() for query_id in mode_rows})

    per_query: List[Dict[str, Any]] = []
    for query_id in query_ids:
        intent = query_intents.get(query_id, "")
        baseline_rows = grouped.get("baseline", {}).get(query_id, [])
        baseline_score = avg_rel(baseline_rows, judgments, k)
        mode_scores = []
        for mode in modes:
            rows_for_mode = grouped.get(mode, {}).get(query_id, [])
            score = avg_rel(rows_for_mode, judgments, k)
            mtype = mode_structure_type(mode)
            top_post = rows_for_mode[0]["post_id"] if rows_for_mode else None
            mode_scores.append(
                {
                    "mode": mode,
                    "structure_type": mtype,
                    "intent_matched": bool(mtype and mtype == intent),
                    "avg_rel": round(score, 6),
                    "delta_vs_baseline": round(score - baseline_score, 6),
                    "top_post": top_post,
                }
            )
        mode_scores.sort(key=lambda item: (item["avg_rel"], item["delta_vs_baseline"]), reverse=True)
        per_query.append(
            {
                "query_id": query_id,
                "intent_structure": intent,
                "baseline_avg_rel": round(baseline_score, 6),
                "best_mode": mode_scores[0] if mode_scores else None,
                "worst_mode": mode_scores[-1] if mode_scores else None,
                "mode_scores": mode_scores,
            }
        )

    harmful_modes: Dict[str, int] = {}
    harmful_intent_matched_modes: Dict[str, int] = {}
    harmful_off_intent_modes: Dict[str, int] = {}
    helpful_modes: Dict[str, int] = {}
    helpful_intent_matched_modes: Dict[str, int] = {}

    for item in per_query:
        baseline = item["baseline_avg_rel"]
        for score in item["mode_scores"]:
            mode = score["mode"]
            if mode == "baseline":
                continue
            delta = score["avg_rel"] - baseline
            if delta < 0:
                harmful_modes[mode] = harmful_modes.get(mode, 0) + 1
                if score["intent_matched"]:
                    harmful_intent_matched_modes[mode] = harmful_intent_matched_modes.get(mode, 0) + 1
                else:
                    harmful_off_intent_modes[mode] = harmful_off_intent_modes.get(mode, 0) + 1
            elif delta > 0:
                helpful_modes[mode] = helpful_modes.get(mode, 0) + 1
                if score["intent_matched"]:
                    helpful_intent_matched_modes[mode] = helpful_intent_matched_modes.get(mode, 0) + 1

    return {
        "k": k,
        "query_count": len(query_ids),
        "helpful_modes": dict(sorted(helpful_modes.items(), key=lambda pair: pair[1], reverse=True)),
        "helpful_intent_matched_modes": dict(sorted(helpful_intent_matched_modes.items(), key=lambda pair: pair[1], reverse=True)),
        "harmful_modes": dict(sorted(harmful_modes.items(), key=lambda pair: pair[1], reverse=True)),
        "harmful_intent_matched_modes": dict(sorted(harmful_intent_matched_modes.items(), key=lambda pair: pair[1], reverse=True)),
        "harmful_off_intent_modes": dict(sorted(harmful_off_intent_modes.items(), key=lambda pair: pair[1], reverse=True)),
        "per_query": per_query,
    }


def _write_count_table(lines: List[str], title: str, data: Mapping[str, int], value_label: str) -> None:
    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"| mode | {value_label} |")
    lines.append("|---|---:|")
    if data:
        for mode, count in data.items():
            lines.append(f"| {mode} | {count} |")
    else:
        lines.append("| none | 0 |")
    lines.append("")


def write_md(report: Mapping[str, Any], output_path: Path) -> None:
    lines: List[str] = ["# Diagnostics report", ""]
    lines.append(f"Primary diagnostic cutoff: **top-{report['k']}**")
    lines.append(f"Query count: **{report['query_count']}**")
    lines.append("")
    _write_count_table(lines, "Helpful modes", report["helpful_modes"], "improved query count")
    _write_count_table(lines, "Helpful intent-matched modes", report["helpful_intent_matched_modes"], "improved query count")
    _write_count_table(lines, "Harmful modes", report["harmful_modes"], "worsened query count")
    _write_count_table(lines, "Harmful intent-matched modes", report["harmful_intent_matched_modes"], "worsened query count")
    _write_count_table(lines, "Harmful off-intent modes", report["harmful_off_intent_modes"], "worsened query count")

    lines.append("## Per-query best/worst modes")
    lines.append("")
    lines.append("| query_id | intent | baseline AvgRel | best mode | best AvgRel | worst mode | worst AvgRel |")
    lines.append("|---|---|---:|---|---:|---|---:|")
    for item in report["per_query"]:
        best = item["best_mode"] or {}
        worst = item["worst_mode"] or {}
        lines.append(
            f"| {item['query_id']} | {item['intent_structure']} | {item['baseline_avg_rel']:.6f} | {best.get('mode')} | {best.get('avg_rel', 0.0):.6f} | {worst.get('mode')} | {worst.get('avg_rel', 0.0):.6f} |"
        )
    lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run(
    results_path: Path = DEFAULT_OUTPUT,
    judgments_path: Path = DEFAULT_JUDGMENTS,
    queries_path: Path = DEFAULT_QUERIES,
    diagnostics_md_path: Path = DEFAULT_DIAGNOSTICS_MD,
    diagnostics_json_path: Path = DEFAULT_DIAGNOSTICS_JSON,
    k: int = 3,
    skip_rerank: bool = False,
) -> Dict[str, Any]:
    if not skip_rerank:
        run_rerank(output_path=results_path, top_k=max(k, 10))
    report = diagnose(results_path, judgments_path, queries_path, k=k)
    diagnostics_md_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_json_path.parent.mkdir(parents=True, exist_ok=True)
    write_md(report, diagnostics_md_path)
    diagnostics_json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {diagnostics_md_path}")
    print(f"wrote {diagnostics_json_path}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Diagnose per-query structure rerank behavior.")
    parser.add_argument("--results", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--diagnostics-md", type=Path, default=DEFAULT_DIAGNOSTICS_MD)
    parser.add_argument("--diagnostics-json", type=Path, default=DEFAULT_DIAGNOSTICS_JSON)
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--skip-rerank", action="store_true")
    args = parser.parse_args()
    run(
        results_path=args.results,
        judgments_path=args.judgments,
        queries_path=args.queries,
        diagnostics_md_path=args.diagnostics_md,
        diagnostics_json_path=args.diagnostics_json,
        k=args.k,
        skip_rerank=args.skip_rerank,
    )


if __name__ == "__main__":
    main()
