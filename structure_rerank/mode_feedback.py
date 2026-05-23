from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Tuple

from .evaluate import DEFAULT_JUDGMENTS, evaluate, load_judgments
from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results" / "sample_results.jsonl"
DEFAULT_OUTPUT_MD = ROOT / "results" / "mode_feedback.md"
DEFAULT_OUTPUT_JSON = ROOT / "results" / "mode_feedback.json"
DEFAULT_KS = [3, 5, 10]


def group_by_mode_query(rows: List[Mapping[str, Any]]) -> Dict[str, Dict[str, List[Mapping[str, Any]]]]:
    grouped: Dict[str, Dict[str, List[Mapping[str, Any]]]] = {}
    for row in rows:
        grouped.setdefault(str(row["mode"]), {}).setdefault(str(row["query_id"]), []).append(row)
    for mode_rows in grouped.values():
        for query_rows in mode_rows.values():
            query_rows.sort(key=lambda item: int(item["rank"]))
    return grouped


def avg_rel(rows: List[Mapping[str, Any]], judgments: Dict[Tuple[str, str], int], k: int) -> float:
    observed = rows[:k]
    if not observed:
        return 0.0
    return sum(judgments.get((str(row["query_id"]), str(row["post_id"])), 0) for row in observed) / len(observed)


def judge(metrics_by_k: Dict[str, Dict[str, Dict[str, float]]], baseline_mode: str, candidate_mode: str, primary_k: int) -> str:
    metrics = metrics_by_k[str(primary_k)]
    baseline = metrics.get(baseline_mode, {})
    candidate = metrics.get(candidate_mode, {})
    ndcg_delta = float(candidate.get(f"nDCG@{primary_k}", 0.0)) - float(baseline.get(f"nDCG@{primary_k}", 0.0))
    avg_delta = float(candidate.get(f"AvgRel@{primary_k}", 0.0)) - float(baseline.get(f"AvgRel@{primary_k}", 0.0))
    if ndcg_delta >= 0.01 and avg_delta >= 0.0:
        return "PASS"
    if ndcg_delta <= -0.01 or avg_delta < 0.0:
        return "FAIL"
    return "UNCERTAIN"


def build_report(
    results_path: Path,
    judgments_path: Path,
    baseline_mode: str,
    candidate_mode: str,
    ks: List[int],
    primary_k: int,
) -> Dict[str, Any]:
    rows = load_jsonl(results_path)
    judgments = load_judgments(judgments_path)
    grouped = group_by_mode_query(rows)
    metrics_by_k = {str(k): evaluate(results_path, judgments_path, k=k) for k in ks}

    query_ids = sorted(set(grouped.get(baseline_mode, {})) | set(grouped.get(candidate_mode, {})))
    deltas: Dict[str, List[Dict[str, Any]]] = {}
    for k in ks:
        items: List[Dict[str, Any]] = []
        for query_id in query_ids:
            base_rows = grouped.get(baseline_mode, {}).get(query_id, [])
            cand_rows = grouped.get(candidate_mode, {}).get(query_id, [])
            base_avg = avg_rel(base_rows, judgments, k)
            cand_avg = avg_rel(cand_rows, judgments, k)
            items.append(
                {
                    "query_id": query_id,
                    "baseline_avg_rel": round(base_avg, 6),
                    "candidate_avg_rel": round(cand_avg, 6),
                    "delta": round(cand_avg - base_avg, 6),
                    "baseline_top": base_rows[0]["post_id"] if base_rows else None,
                    "candidate_top": cand_rows[0]["post_id"] if cand_rows else None,
                }
            )
        deltas[str(k)] = items

    verdict = judge(metrics_by_k, baseline_mode, candidate_mode, primary_k)
    primary_deltas = deltas[str(primary_k)]
    improved = [item for item in primary_deltas if item["delta"] > 0]
    worsened = [item for item in primary_deltas if item["delta"] < 0]

    if verdict == "PASS":
        next_actions = [
            "Keep the candidate mode for the next dataset expansion.",
            "Add harder negative examples before tuning weights.",
            "Compare against an optional neural embedding backend later.",
        ]
    elif verdict == "FAIL":
        next_actions = [
            "Inspect worsened queries before changing the dataset.",
            "Lower structure beta or tighten query-intent gating.",
            "Check whether vector similarity already captures the structure signal.",
        ]
    else:
        next_actions = [
            "Increase query count and add harder cases.",
            "Do not claim improvement from this mode yet.",
            "Inspect rank movement explanations for near misses.",
        ]

    return {
        "verdict": verdict,
        "baseline_mode": baseline_mode,
        "candidate_mode": candidate_mode,
        "primary_k": primary_k,
        "metrics_by_k": metrics_by_k,
        "query_deltas_by_k": deltas,
        "improved_queries": improved,
        "worsened_queries": worsened,
        "next_actions": next_actions,
    }


def write_md(report: Mapping[str, Any], output_path: Path) -> None:
    lines: List[str] = ["# Mode feedback report", ""]
    lines.append(f"Judgment: **{report['verdict']}**")
    lines.append(f"Baseline mode: **{report['baseline_mode']}**")
    lines.append(f"Candidate mode: **{report['candidate_mode']}**")
    lines.append(f"Primary cutoff: **top-{report['primary_k']}**")
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    lines.append("| k | mode | nDCG | MRR | AvgRel |")
    lines.append("|---:|---|---:|---:|---:|")
    for k_text in sorted(report["metrics_by_k"], key=lambda value: int(value)):
        metrics = report["metrics_by_k"][k_text]
        for mode in [report["baseline_mode"], report["candidate_mode"]]:
            row = metrics.get(mode, {})
            lines.append(
                f"| {k_text} | {mode} | {row.get(f'nDCG@{k_text}', 0.0):.6f} | {row.get('MRR', 0.0):.6f} | {row.get(f'AvgRel@{k_text}', 0.0):.6f} |"
            )
    lines.append("")
    lines.append("## Primary query deltas")
    lines.append("")
    lines.append("| query_id | baseline AvgRel | candidate AvgRel | delta | baseline top | candidate top |")
    lines.append("|---|---:|---:|---:|---|---|")
    primary_key = str(report["primary_k"])
    for item in report["query_deltas_by_k"][primary_key]:
        lines.append(
            f"| {item['query_id']} | {item['baseline_avg_rel']:.6f} | {item['candidate_avg_rel']:.6f} | {item['delta']:.6f} | {item['baseline_top']} | {item['candidate_top']} |"
        )
    lines.append("")
    lines.append("## Next actions")
    lines.append("")
    for action in report["next_actions"]:
        lines.append(f"- {action}")
    lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def _parse_ks(raw: str) -> List[int]:
    values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    if not values:
        raise argparse.ArgumentTypeError("at least one k value is required")
    return sorted(set(values))


def run(
    results_path: Path = DEFAULT_RESULTS,
    judgments_path: Path = DEFAULT_JUDGMENTS,
    output_md_path: Path = DEFAULT_OUTPUT_MD,
    output_json_path: Path = DEFAULT_OUTPUT_JSON,
    baseline_mode: str = "baseline",
    candidate_mode: str = "structure_rerank",
    ks: List[int] | None = None,
    primary_k: int = 3,
) -> Dict[str, Any]:
    ks = ks or DEFAULT_KS
    report = build_report(results_path, judgments_path, baseline_mode, candidate_mode, ks, primary_k)
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    write_md(report, output_md_path)
    output_json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"judgment: {report['verdict']}")
    print(f"wrote {output_md_path}")
    print(f"wrote {output_json_path}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two ranking modes and generate feedback.")
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--baseline-mode", default="baseline")
    parser.add_argument("--candidate-mode", default="structure_rerank")
    parser.add_argument("--ks", type=_parse_ks, default=DEFAULT_KS)
    parser.add_argument("--primary-k", type=int, default=3)
    args = parser.parse_args()
    run(
        results_path=args.results,
        judgments_path=args.judgments,
        output_md_path=args.output_md,
        output_json_path=args.output_json,
        baseline_mode=args.baseline_mode,
        candidate_mode=args.candidate_mode,
        ks=args.ks,
        primary_k=args.primary_k,
    )


if __name__ == "__main__":
    main()
