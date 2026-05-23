from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from .rerank import DEFAULT_POSTS, DEFAULT_QUERIES, DEFAULT_STRUCTURES
from .structure_score import build_structure_index, combine_scores, load_jsonl, normalize_scores, structure_score
from .vector_score import build_post_vectors, vector_scores

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results" / "vector_results.jsonl"


def rows_for_query(
    mode: str,
    query: Dict[str, Any],
    posts: List[Dict[str, Any]],
    base_scores: Dict[str, float],
    structure_index: Dict[str, List[Dict[str, Any]]],
    top_k: int,
    use_structure: bool,
    alpha: float = 0.8,
    beta: float = 0.2,
) -> List[Dict[str, Any]]:
    raw_base = [(str(post["id"]), base_scores.get(str(post["id"]), 0.0)) for post in posts]
    raw_struct = []
    for post in posts:
        post_id = str(post["id"])
        score = structure_score(query, structure_index.get(post_id, [])) if use_structure else 0.0
        raw_struct.append((post_id, score))

    base_norm = normalize_scores(raw_base)
    struct_norm = normalize_scores(raw_struct)
    rows: List[Dict[str, Any]] = []
    for post in posts:
        post_id = str(post["id"])
        base = base_norm.get(post_id, 0.0)
        struct = struct_norm.get(post_id, 0.0)
        final = combine_scores(base, struct, alpha=alpha, beta=beta) if use_structure else base
        rows.append(
            {
                "mode": mode,
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
    post_vectors, idf = build_post_vectors(posts)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for query in queries:
            base_scores = vector_scores(str(query["query"]), post_vectors, idf)
            for row in rows_for_query("vector_baseline", query, posts, base_scores, structure_index, top_k, False):
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            for row in rows_for_query("vector_structure_rerank", query, posts, base_scores, structure_index, top_k, True):
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run dependency-free TF-IDF vector baseline experiment.")
    parser.add_argument("--posts", type=Path, default=DEFAULT_POSTS)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--structures", type=Path, default=DEFAULT_STRUCTURES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()
    run(args.posts, args.queries, args.structures, args.output, args.top_k)


if __name__ == "__main__":
    main()
