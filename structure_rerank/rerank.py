from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from .structure_score import (
    build_structure_index,
    combine_scores,
    lexical_score,
    load_jsonl,
    normalize_scores,
    structure_score,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POSTS = ROOT / "examples" / "sample_posts.jsonl"
DEFAULT_QUERIES = ROOT / "examples" / "sample_queries.jsonl"
DEFAULT_STRUCTURES = ROOT / "examples" / "sample_structures.jsonl"
DEFAULT_OUTPUT = ROOT / "results" / "sample_results.jsonl"


def rank_for_query(
    query: Dict[str, Any],
    posts: List[Dict[str, Any]],
    structure_index: Dict[str, List[Dict[str, Any]]],
    top_k: int = 10,
    alpha: float = 0.8,
    beta: float = 0.2,
) -> List[Dict[str, Any]]:
    raw_base = []
    raw_struct = []
    for post in posts:
        post_id = str(post["id"])
        base = lexical_score(str(query["query"]), str(post["text"]))
        struct = structure_score(query, structure_index.get(post_id, []))
        raw_base.append((post_id, base))
        raw_struct.append((post_id, struct))

    base_norm = normalize_scores(raw_base)
    struct_norm = normalize_scores(raw_struct)

    rows: List[Dict[str, Any]] = []
    for post in posts:
        post_id = str(post["id"])
        base = base_norm.get(post_id, 0.0)
        struct = struct_norm.get(post_id, 0.0)
        final = combine_scores(base, struct, alpha=alpha, beta=beta)
        rows.append(
            {
                "query_id": query["id"],
                "post_id": post_id,
                "baseline_score": round(base, 6),
                "structure_score": round(struct, 6),
                "rerank_score": round(final, 6),
            }
        )

    rows.sort(key=lambda row: (row["rerank_score"], row["baseline_score"]), reverse=True)
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows[:top_k]


def baseline_for_query(query: Dict[str, Any], posts: List[Dict[str, Any]], top_k: int = 10) -> List[Dict[str, Any]]:
    raw_base = [(str(post["id"]), lexical_score(str(query["query"]), str(post["text"]))) for post in posts]
    base_norm = normalize_scores(raw_base)
    rows: List[Dict[str, Any]] = []
    for post in posts:
        post_id = str(post["id"])
        rows.append(
            {
                "query_id": query["id"],
                "post_id": post_id,
                "baseline_score": round(base_norm.get(post_id, 0.0), 6),
                "structure_score": 0.0,
                "rerank_score": round(base_norm.get(post_id, 0.0), 6),
            }
        )
    rows.sort(key=lambda row: row["baseline_score"], reverse=True)
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows[:top_k]


def run(
    posts_path: Path = DEFAULT_POSTS,
    queries_path: Path = DEFAULT_QUERIES,
    structures_path: Path = DEFAULT_STRUCTURES,
    output_path: Path = DEFAULT_OUTPUT,
    top_k: int = 10,
) -> None:
    posts = load_jsonl(posts_path)
    queries = load_jsonl(queries_path)
    structures = load_jsonl(structures_path)
    structure_index = build_structure_index(structures)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for query in queries:
            for row in baseline_for_query(query, posts, top_k=top_k):
                handle.write(json.dumps({"mode": "baseline", **row}, ensure_ascii=False) + "\n")
            for row in rank_for_query(query, posts, structure_index, top_k=top_k):
                handle.write(json.dumps({"mode": "structure_rerank", **row}, ensure_ascii=False) + "\n")

    print(f"wrote {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run structure-aware reranking over sample data.")
    parser.add_argument("--posts", type=Path, default=DEFAULT_POSTS)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--structures", type=Path, default=DEFAULT_STRUCTURES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()
    run(args.posts, args.queries, args.structures, args.output, args.top_k)


if __name__ == "__main__":
    main()
