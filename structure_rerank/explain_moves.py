from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Tuple

from .evaluate import DEFAULT_JUDGMENTS, load_judgments
from .rerank import DEFAULT_OUTPUT, run as run_rerank
from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPLANATIONS_MD = ROOT / "results" / "rank_movements.md"
DEFAULT_EXPLANATIONS_JSON = ROOT / "results" / "rank_movements.json"


def group_by_mode_query(rows: List[Mapping[str, Any]]) -> Dict[str, Dict[str, List[Mapping[str, Any]]]]:
    grouped: Dict[str, Dict[str, List[Mapping[str, Any]]]] = {}
    for row in rows:
        grouped.setdefault(str(row["mode"]), {}).setdefault(str(row["query_id"]), []).append(row)
    for mode_rows in grouped.values():
        for query_rows in mode_rows.values():
            query_rows.sort(key=lambda item: int(item["rank"]))
    return grouped


def rank_map(rows: List[Mapping[str, Any]]) -> Dict[str, int]:
    return {str(row["post_id"]): int(row["rank"]) for row in rows}


def row_map(rows: List[Mapping[str, Any]]) -> Dict[str, Mapping[str, Any]]:
    return {str(row["post_id"]): row for row in rows}


def explain(
    results_path: Path,
    judgments_path: Path,
    compare_mode: str,
    k: int,
    max_items_per_query: int,
) -> Dict[str, Any]:
    rows = load_jsonl(results_path)
    judgments = load_judgments(judgments_path)
    grouped = group_by_mode_query(rows)
    baseline_by_query = grouped.get("baseline", {})
    compare_by_query = grouped.get(compare_mode, {})
    query_ids = sorted(set(baseline_by_query) | set(compare_by_query))

    explanations: List[Dict[str, Any]] = []
    for query_id in query_ids:
        baseline_rows = baseline_by_query.get(query_id, [])[:k]
        compare_rows = compare_by_query.get(query_id, [])[:k]
        baseline_ranks = rank_map(baseline_rows)
        compare_ranks = rank_map(compare_rows)
        baseline_rows_by_post = row_map(baseline_rows)
        compare_rows_by_post = row_map(compare_rows)
        post_ids = sorted(set(baseline_ranks) | set(compare_ranks))

        moves: List[Dict[str, Any]] = []
        for post_id in post_ids:
            old_rank = baseline_ranks.get(post_id)
            new_rank = compare_ranks.get(post_id)
            if old_rank == new_rank:
                continue
            relevance = judgments.get((query_id, post_id), 0)
            baseline_row = baseline_rows_by_post.get(post_id, {})
            compare_row = compare_rows_by_post.get(post_id, {})
            if old_rank is None:
                direction = "entered_top_k"
                delta_rank = None
            elif new_rank is None:
                direction = "left_top_k"
                delta_rank = None
            elif new_rank < old_rank:
                direction = "up"
                delta_rank = old_rank - new_rank
            else:
                direction = "down"
                delta_rank = old_rank - new_rank
            moves.append(
                {
                    "post_id": post_id,
                    "relevance": relevance,
                    "direction": direction,
                    "baseline_rank": old_rank,
                    "compare_rank": new_rank,
                    "rank_delta": delta_rank,
                    "baseline_score": baseline_row.get("baseline_score"),
                    "structure_score": compare_row.get("structure_score"),
                    "rerank_score": compare_row.get("rerank_score"),
                }
            )
        moves.sort(key=lambda item: (item["relevance"], item["rank_delta"] or 0), reverse=True)
        explanations.append({"query_id": query_id, "moves": moves[:max_items_per_query]})

    return {"compare_mode": compare_mode, "k": k, "queries": explanations}


def write_md(report: Mapping[str, Any], output_path: Path) -> None:
    lines: List[str] = ["# Rank movement explanations", ""]
    lines.append(f"Compare mode: **{report['compare_mode']}**")
    lines.append(f"Cutoff: **top-{report['k']}**")
    lines.append("")
    for query in report["queries"]:
        lines.append(f"## {query['query_id']}")
        lines.append("")
        if not query["moves"]:
            lines.append("No rank movements inside the cutoff.")
            lines.append("")
            continue
        lines.append("| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |")
        lines.append("|---|---:|---|---:|---:|---:|---:|---:|")
        for move in query["moves"]:
            lines.append(
                f"| {move['post_id']} | {move['relevance']} | {move['direction']} | {move['baseline_rank']} | {move['compare_rank']} | {move['rank_delta']} | {move.get('structure_score')} | {move.get('rerank_score')} |"
            )
        lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run(
    results_path: Path = DEFAULT_OUTPUT,
    judgments_path: Path = DEFAULT_JUDGMENTS,
    explanations_md_path: Path = DEFAULT_EXPLANATIONS_MD,
    explanations_json_path: Path = DEFAULT_EXPLANATIONS_JSON,
    compare_mode: str = "structure_rerank",
    k: int = 10,
    max_items_per_query: int = 8,
    skip_rerank: bool = False,
) -> Dict[str, Any]:
    if not skip_rerank:
        run_rerank(output_path=results_path, top_k=k)
    report = explain(results_path, judgments_path, compare_mode, k, max_items_per_query)
    explanations_md_path.parent.mkdir(parents=True, exist_ok=True)
    explanations_json_path.parent.mkdir(parents=True, exist_ok=True)
    write_md(report, explanations_md_path)
    explanations_json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {explanations_md_path}")
    print(f"wrote {explanations_json_path}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Explain rank movements after reranking.")
    parser.add_argument("--results", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--explanations-md", type=Path, default=DEFAULT_EXPLANATIONS_MD)
    parser.add_argument("--explanations-json", type=Path, default=DEFAULT_EXPLANATIONS_JSON)
    parser.add_argument("--compare-mode", default="structure_rerank")
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--max-items-per-query", type=int, default=8)
    parser.add_argument("--skip-rerank", action="store_true")
    args = parser.parse_args()
    run(
        results_path=args.results,
        judgments_path=args.judgments,
        explanations_md_path=args.explanations_md,
        explanations_json_path=args.explanations_json,
        compare_mode=args.compare_mode,
        k=args.k,
        max_items_per_query=args.max_items_per_query,
        skip_rerank=args.skip_rerank,
    )


if __name__ == "__main__":
    main()
