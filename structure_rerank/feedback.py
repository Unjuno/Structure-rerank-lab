from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Tuple

from .evaluate import DEFAULT_JUDGMENTS, evaluate, load_judgments
from .rerank import DEFAULT_OUTPUT, run as run_rerank
from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FEEDBACK_MD = ROOT / "results" / "feedback.md"
DEFAULT_FEEDBACK_JSON = ROOT / "results" / "feedback.json"
DEFAULT_KS = [3, 5, 10]
PRIMARY_K = 3


def _query_level_avg_rel(rows: List[Mapping[str, Any]], judgments: Dict[Tuple[str, str], int], k: int) -> float:
    observed = rows[:k]
    if not observed:
        return 0.0
    rels = [judgments.get((str(row["query_id"]), str(row["post_id"])), 0) for row in observed]
    return sum(rels) / len(rels)


def _group_by_mode_query(rows: List[Mapping[str, Any]]) -> Dict[str, Dict[str, List[Mapping[str, Any]]]]:
    grouped: Dict[str, Dict[str, List[Mapping[str, Any]]]] = {}
    for row in rows:
        mode = str(row["mode"])
        query_id = str(row["query_id"])
        grouped.setdefault(mode, {}).setdefault(query_id, []).append(row)
    for mode_rows in grouped.values():
        for query_rows in mode_rows.values():
            query_rows.sort(key=lambda item: int(item["rank"]))
    return grouped


def judge(metrics_by_k: Dict[int, Dict[str, Dict[str, float]]], primary_k: int = PRIMARY_K) -> str:
    metrics = metrics_by_k.get(primary_k, {})
    baseline = metrics.get("baseline", {})
    rerank = metrics.get("structure_rerank", {})
    ndcg_key = f"nDCG@{primary_k}"
    avg_key = f"AvgRel@{primary_k}"
    ndcg_delta = float(rerank.get(ndcg_key, 0.0)) - float(baseline.get(ndcg_key, 0.0))
    avg_delta = float(rerank.get(avg_key, 0.0)) - float(baseline.get(avg_key, 0.0))

    if ndcg_delta >= 0.01 and avg_delta >= 0.0:
        return "PASS"
    if ndcg_delta <= -0.01 or avg_delta < 0.0:
        return "FAIL"
    return "UNCERTAIN"


def build_feedback(results_path: Path, judgments_path: Path, ks: List[int]) -> Dict[str, Any]:
    rows = load_jsonl(results_path)
    judgments = load_judgments(judgments_path)
    metrics_by_k = {k: evaluate(results_path, judgments_path, k=k) for k in ks}
    grouped = _group_by_mode_query(rows)
    query_ids = sorted(set(grouped.get("baseline", {})) | set(grouped.get("structure_rerank", {})))

    query_deltas_by_k: Dict[int, List[Dict[str, Any]]] = {}
    for k in ks:
        query_deltas: List[Dict[str, Any]] = []
        for query_id in query_ids:
            base_rows = grouped.get("baseline", {}).get(query_id, [])
            rerank_rows = grouped.get("structure_rerank", {}).get(query_id, [])
            base_avg = _query_level_avg_rel(base_rows, judgments, k)
            rerank_avg = _query_level_avg_rel(rerank_rows, judgments, k)
            query_deltas.append(
                {
                    "query_id": query_id,
                    "baseline_avg_rel": round(base_avg, 6),
                    "structure_rerank_avg_rel": round(rerank_avg, 6),
                    "delta": round(rerank_avg - base_avg, 6),
                    "baseline_top": base_rows[0]["post_id"] if base_rows else None,
                    "structure_top": rerank_rows[0]["post_id"] if rerank_rows else None,
                }
            )
        query_deltas_by_k[k] = query_deltas

    primary_deltas = query_deltas_by_k[PRIMARY_K]
    improved = [item for item in primary_deltas if item["delta"] > 0]
    worsened = [item for item in primary_deltas if item["delta"] < 0]
    unchanged = [item for item in primary_deltas if item["delta"] == 0]

    verdict = judge(metrics_by_k, primary_k=PRIMARY_K)
    if verdict == "PASS":
        next_actions = [
            "Add a small real exported dataset without production secrets.",
            "Keep top-3/top-5/top-10 metrics and compare again before changing the scoring formula.",
            "Inspect improved queries to identify which structure types carried the gain.",
        ]
    elif verdict == "FAIL":
        next_actions = [
            "Inspect worsened top-3 queries before adding features.",
            "Reduce beta or disable low-confidence structure matches.",
            "Check whether structure labels are too coarse or query intent labels are wrong.",
        ]
    else:
        next_actions = [
            "Add harder negative examples where lexical overlap is high but structure is wrong.",
            "Add per-structure ablation: conclusion-only, causal-only, contrast-only.",
            "Do not claim success until the real exported dataset improves.",
        ]

    return {
        "verdict": verdict,
        "primary_k": PRIMARY_K,
        "metrics_by_k": {str(k): metrics for k, metrics in metrics_by_k.items()},
        "query_deltas_by_k": {str(k): items for k, items in query_deltas_by_k.items()},
        "improved_queries": improved,
        "worsened_queries": worsened,
        "unchanged_queries": unchanged,
        "next_actions": next_actions,
    }


def write_feedback_md(feedback: Mapping[str, Any], output_path: Path) -> None:
    lines: List[str] = []
    lines.append("# Feedback report")
    lines.append("")
    lines.append(f"Judgment: **{feedback['verdict']}**")
    lines.append(f"Primary cutoff: **top-{feedback['primary_k']}**")
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    lines.append("| k | mode | nDCG | MRR | AvgRel |")
    lines.append("|---:|---|---:|---:|---:|")
    for k_text in sorted(feedback["metrics_by_k"], key=lambda value: int(value)):
        metrics = feedback["metrics_by_k"][k_text]
        for mode in sorted(metrics):
            row = metrics[mode]
            lines.append(
                f"| {k_text} | {mode} | {row.get(f'nDCG@{k_text}', 0.0):.6f} | {row.get('MRR', 0.0):.6f} | {row.get(f'AvgRel@{k_text}', 0.0):.6f} |"
            )
    lines.append("")
    lines.append("## Primary query deltas")
    lines.append("")
    lines.append("| query_id | baseline AvgRel | structure AvgRel | delta | baseline top | structure top |")
    lines.append("|---|---:|---:|---:|---|---|")
    primary_key = str(feedback["primary_k"])
    for item in feedback["query_deltas_by_k"][primary_key]:
        lines.append(
            f"| {item['query_id']} | {item['baseline_avg_rel']:.6f} | {item['structure_rerank_avg_rel']:.6f} | {item['delta']:.6f} | {item['baseline_top']} | {item['structure_top']} |"
        )
    lines.append("")
    lines.append("## Next actions")
    lines.append("")
    for action in feedback["next_actions"]:
        lines.append(f"- {action}")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run(
    results_path: Path = DEFAULT_OUTPUT,
    judgments_path: Path = DEFAULT_JUDGMENTS,
    feedback_md_path: Path = DEFAULT_FEEDBACK_MD,
    feedback_json_path: Path = DEFAULT_FEEDBACK_JSON,
    ks: List[int] | None = None,
    skip_rerank: bool = False,
) -> Dict[str, Any]:
    ks = ks or DEFAULT_KS
    max_k = max(ks)
    if not skip_rerank:
        run_rerank(output_path=results_path, top_k=max_k)
    feedback = build_feedback(results_path, judgments_path, ks=ks)
    feedback_md_path.parent.mkdir(parents=True, exist_ok=True)
    feedback_json_path.parent.mkdir(parents=True, exist_ok=True)
    write_feedback_md(feedback, feedback_md_path)
    feedback_json_path.write_text(json.dumps(feedback, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"judgment: {feedback['verdict']}")
    print(f"wrote {feedback_md_path}")
    print(f"wrote {feedback_json_path}")
    return feedback


def _parse_ks(raw: str) -> List[int]:
    values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    if not values:
        raise argparse.ArgumentTypeError("at least one k value is required")
    if any(value <= 0 for value in values):
        raise argparse.ArgumentTypeError("k values must be positive")
    return sorted(set(values))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate closed-loop feedback for the structure rerank experiment.")
    parser.add_argument("--results", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--feedback-md", type=Path, default=DEFAULT_FEEDBACK_MD)
    parser.add_argument("--feedback-json", type=Path, default=DEFAULT_FEEDBACK_JSON)
    parser.add_argument("--ks", type=_parse_ks, default=DEFAULT_KS, help="Comma-separated cutoffs, e.g. 3,5,10")
    parser.add_argument("--skip-rerank", action="store_true")
    args = parser.parse_args()
    run(
        results_path=args.results,
        judgments_path=args.judgments,
        feedback_md_path=args.feedback_md,
        feedback_json_path=args.feedback_json,
        ks=args.ks,
        skip_rerank=args.skip_rerank,
    )


if __name__ == "__main__":
    main()
