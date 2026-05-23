from __future__ import annotations

import argparse
import math
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Tuple

from .rerank import DEFAULT_OUTPUT, run as run_rerank
from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JUDGMENTS = ROOT / "examples" / "sample_judgments.jsonl"


def load_judgments(path: Path) -> Dict[Tuple[str, str], int]:
    judgments: Dict[Tuple[str, str], int] = {}
    for row in load_jsonl(path):
        judgments[(str(row["query_id"]), str(row["post_id"]))] = int(row["relevance"])
    return judgments


def group_results(rows: Iterable[Mapping[str, object]]) -> Dict[str, Dict[str, List[Mapping[str, object]]]]:
    grouped: Dict[str, Dict[str, List[Mapping[str, object]]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        grouped[str(row["mode"])][str(row["query_id"])].append(row)
    for mode_rows in grouped.values():
        for query_rows in mode_rows.values():
            query_rows.sort(key=lambda item: int(item["rank"]))
    return grouped


def dcg(relevances: List[int]) -> float:
    total = 0.0
    for index, rel in enumerate(relevances, start=1):
        total += (2**rel - 1) / math.log2(index + 1)
    return total


def ndcg_at_k(relevances: List[int], ideal_relevances: List[int], k: int) -> float:
    observed = relevances[:k]
    ideal = sorted(ideal_relevances, reverse=True)[:k]
    ideal_dcg = dcg(ideal)
    if ideal_dcg == 0:
        return 0.0
    return dcg(observed) / ideal_dcg


def reciprocal_rank(relevances: List[int]) -> float:
    for index, rel in enumerate(relevances, start=1):
        if rel > 0:
            return 1.0 / index
    return 0.0


def avg_rel_at_k(relevances: List[int], k: int) -> float:
    observed = relevances[:k]
    if not observed:
        return 0.0
    return sum(observed) / len(observed)


def evaluate(results_path: Path, judgments_path: Path, k: int = 10) -> Dict[str, Dict[str, float]]:
    rows = load_jsonl(results_path)
    judgments = load_judgments(judgments_path)
    grouped = group_results(rows)

    all_query_ids = sorted({query_id for _, query_id_map in grouped.items() for query_id in query_id_map})
    ideal_by_query: Dict[str, List[int]] = defaultdict(list)
    for (query_id, _post_id), relevance in judgments.items():
        ideal_by_query[query_id].append(relevance)

    metrics: Dict[str, Dict[str, float]] = {}
    for mode, query_map in grouped.items():
        ndcgs: List[float] = []
        mrrs: List[float] = []
        avg_rels: List[float] = []
        for query_id in all_query_ids:
            result_rows = query_map.get(query_id, [])
            rels = [judgments.get((query_id, str(row["post_id"])), 0) for row in result_rows]
            ndcgs.append(ndcg_at_k(rels, ideal_by_query.get(query_id, []), k))
            mrrs.append(reciprocal_rank(rels))
            avg_rels.append(avg_rel_at_k(rels, k))
        metrics[mode] = {
            f"nDCG@{k}": round(sum(ndcgs) / len(ndcgs), 6) if ndcgs else 0.0,
            "MRR": round(sum(mrrs) / len(mrrs), 6) if mrrs else 0.0,
            f"AvgRel@{k}": round(sum(avg_rels) / len(avg_rels), 6) if avg_rels else 0.0,
        }
    return metrics


def print_metrics(metrics: Dict[str, Dict[str, float]]) -> None:
    modes = sorted(metrics)
    print("| mode | nDCG@10 | MRR | AvgRel@10 |")
    print("|---|---:|---:|---:|")
    for mode in modes:
        row = metrics[mode]
        print(f"| {mode} | {row.get('nDCG@10', 0.0):.6f} | {row.get('MRR', 0.0):.6f} | {row.get('AvgRel@10', 0.0):.6f} |")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate baseline and structure rerank outputs.")
    parser.add_argument("--results", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--skip-rerank", action="store_true", help="Do not regenerate results before evaluating.")
    args = parser.parse_args()

    if not args.skip_rerank:
        run_rerank(output_path=args.results, top_k=args.k)
    metrics = evaluate(args.results, args.judgments, k=args.k)
    print_metrics(metrics)


if __name__ == "__main__":
    main()
