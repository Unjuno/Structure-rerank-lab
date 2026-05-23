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


def judge(metrics: Dict[str, Dict[str, float]], k: int) -> str:
    baseline = metrics.get("baseline", {})
    rerank = metrics.get("structure_rerank", {})
    ndcg_key = f"nDCG@{k}"
    avg_key = f"AvgRel@{k}"
    ndcg_delta = float(rerank.get(ndcg_key, 0.0)) - float(baseline.get(ndcg_key, 0.0))
    avg_delta = float(rerank.get(avg_key, 0.0)) - float(baseline.get(avg_key, 0.0))

    if ndcg_delta >= 0.01 and avg_delta >= 0.0:
        return "PASS"
    if ndcg_delta <= -0.01 or avg_delta < 0.0:
        return "FAIL"
    return "UNCERTAIN"


def build_feedback(results_path: Path, judgments_path: Path, k: int) -> Dict[str, Any]:
    rows = load_jsonl(results_path)
    judgments = load_judgments(judgments_path)
    metrics = evaluate(results_path, judgments_path, k=k)
    grouped = _group_by_mode_query(rows)
    query_ids = sorted(set(grouped.get("baseline", {})) | set(grouped.get("structure_rerank", {})))

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

    improved = [item for item in query_deltas if item["delta"] > 0]
    worsened = [item for item in query_deltas if item["delta"] < 0]
    unchanged = [item for item in query_deltas if item["delta"] == 0]

    verdict = judge(metrics, k)
    next_actions: List[str]
    if verdict == "PASS":
        next_actions = [
            "Add a small real exported dataset without production secrets.",
            "Keep the same metrics and compare again before changing the scoring formula.",
            "Inspect improved queries to identify which structure types carried the gain.",
        ]
    elif verdict == "FAIL":
        next_actions = [
            "Inspect worsened queries before adding features.",
            "Reduce beta or disable low-confidence structure matches.",
            "Check whether structure labels are too coarse or query intent labels are wrong.",
        ]
    else:
        next_actions = [
            "Increase sample query count and add harder negative examples.",
            "Add per-structure ablation: conclusion-only, causal-only, contrast-only.",
            "Do not claim success until the real exported dataset improves.",
        ]

    return {
        "verdict": verdict,
        "metrics": metrics,
        "query_deltas": query_deltas,
        "improved_queries": improved,
        "worsened_queries": worsened,
        "unchanged_queries": unchanged,
        "next_actions": next_actions,
    }


def write_feedback_md(feedback: Mapping[str, Any], output_path: Path, k: int) -> None:
    metrics = feedback["metrics"]
    lines: List[str] = []
    lines.append("# Feedback report")
    lines.append("")
    lines.append(f"Judgment: **{feedback['verdict']}**")
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    lines.append(f"| mode | nDCG@{k} | MRR | AvgRel@{k} |")
    lines.append("|---|---:|---:|---:|")
    for mode in sorted(metrics):
        row = metrics[mode]
        lines.append(
            f"| {mode} | {row.get(f'nDCG@{k}', 0.0):.6f} | {row.get('MRR', 0.0):.6f} | {row.get(f'AvgRel@{k}', 0.0):.6f} |"
        )
    lines.append("")
    lines.append("## Query deltas")
    lines.append("")
    lines.append("| query_id | baseline AvgRel | structure AvgRel | delta | baseline top | structure top |")
    lines.append("|---|---:|---:|---:|---|---|")
    for item in feedback["query_deltas"]:
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
    k: int = 10,
    skip_rerank: bool = False,
) -> Dict[str, Any]:
    if not skip_rerank:
        run_rerank(output_path=results_path, top_k=k)
    feedback = build_feedback(results_path, judgments_path, k=k)
    feedback_md_path.parent.mkdir(parents=True, exist_ok=True)
    feedback_json_path.parent.mkdir(parents=True, exist_ok=True)
    write_feedback_md(feedback, feedback_md_path, k=k)
    feedback_json_path.write_text(json.dumps(feedback, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"judgment: {feedback['verdict']}")
    print(f"wrote {feedback_md_path}")
    print(f"wrote {feedback_json_path}")
    return feedback


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate closed-loop feedback for the structure rerank experiment.")
    parser.add_argument("--results", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--feedback-md", type=Path, default=DEFAULT_FEEDBACK_MD)
    parser.add_argument("--feedback-json", type=Path, default=DEFAULT_FEEDBACK_JSON)
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--skip-rerank", action="store_true")
    args = parser.parse_args()
    run(
        results_path=args.results,
        judgments_path=args.judgments,
        feedback_md_path=args.feedback_md,
        feedback_json_path=args.feedback_json,
        k=args.k,
        skip_rerank=args.skip_rerank,
    )


if __name__ == "__main__":
    main()
