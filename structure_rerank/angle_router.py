from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping

from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results" / "vector_results.jsonl"
DEFAULT_OUTPUT = ROOT / "results" / "angle_router_results.jsonl"

DEFAULT_DATASET_MODE = {
    "expanded_real_like": "diagonal_vertical_50",
    "real_like": "diagonal_vertical_50",
    "arguana": "diagonal_vertical_35",
    "nfcorpus": "diagonal_vertical_35",
    "scifact": "diagonal_vertical_20",
}

FALLBACK_MODE = "vertical_vector_rerank"
DATASET_ROUTED_MODE = "angle_router"
QUERY_ROUTED_MODE = "query_angle_router"

SCIENTIFIC_TERMS = {
    "study",
    "studies",
    "evidence",
    "trial",
    "trials",
    "effect",
    "effects",
    "protein",
    "gene",
    "genes",
    "cell",
    "cells",
    "cancer",
    "disease",
    "patients",
    "treatment",
    "risk",
    "associated",
    "causes",
    "increase",
    "decrease",
}

ARGUMENT_TERMS = {
    "argue",
    "argument",
    "claim",
    "claims",
    "counter",
    "against",
    "support",
    "oppose",
    "reason",
    "reasons",
    "position",
    "premise",
    "conclusion",
}

PRACTICAL_TERMS = {
    "how",
    "what",
    "why",
    "design",
    "build",
    "implement",
    "improve",
    "compare",
    "evaluate",
    "method",
    "system",
    "workflow",
}


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())


def choose_dataset_mode(dataset: str, mapping: Mapping[str, str] = DEFAULT_DATASET_MODE) -> str:
    return mapping.get(dataset.lower(), FALLBACK_MODE)


def choose_query_mode(query_text: str) -> str:
    """Pick an angle from cheap query-only features.

    This deliberately avoids dataset labels. It is a small heuristic router, not a learned model.
    """
    tokens = tokenize(query_text)
    token_set = set(tokens)
    scientific_hits = len(token_set & SCIENTIFIC_TERMS)
    argument_hits = len(token_set & ARGUMENT_TERMS)
    practical_hits = len(token_set & PRACTICAL_TERMS)
    length = len(tokens)

    if scientific_hits >= 1 and argument_hits == 0:
        return "diagonal_vertical_20"
    if argument_hits >= 1:
        return "diagonal_vertical_35"
    if practical_hits >= 1 and length <= 8:
        return "diagonal_vertical_50"
    if length >= 12:
        return "diagonal_vertical_20"
    return "diagonal_vertical_35"


def load_query_texts(path: Path) -> Dict[str, str]:
    texts: Dict[str, str] = {}
    for row in load_jsonl(path):
        query_id = str(row["id"])
        texts[query_id] = str(row.get("query", ""))
    return texts


def route_dataset_rows(rows: Iterable[Mapping[str, Any]], dataset: str, routed_mode: str = DATASET_ROUTED_MODE) -> List[Dict[str, Any]]:
    selected_mode = choose_dataset_mode(dataset)
    routed: List[Dict[str, Any]] = []
    for row in rows:
        if str(row.get("mode")) != selected_mode:
            continue
        next_row = dict(row)
        next_row["source_mode"] = selected_mode
        next_row["mode"] = routed_mode
        routed.append(next_row)
    return routed


def route_query_rows(rows: Iterable[Mapping[str, Any]], query_texts: Mapping[str, str], routed_mode: str = QUERY_ROUTED_MODE) -> List[Dict[str, Any]]:
    routed: List[Dict[str, Any]] = []
    for row in rows:
        query_id = str(row.get("query_id"))
        selected_mode = choose_query_mode(query_texts.get(query_id, ""))
        if str(row.get("mode")) != selected_mode:
            continue
        next_row = dict(row)
        next_row["source_mode"] = selected_mode
        next_row["mode"] = routed_mode
        routed.append(next_row)
    return routed


def run(
    results: Path = DEFAULT_RESULTS,
    output: Path = DEFAULT_OUTPUT,
    dataset: str = "unknown",
    queries: Path | None = None,
    router: str = "dataset",
) -> Dict[str, Any]:
    rows = load_jsonl(results)
    if router == "query":
        if queries is None:
            raise ValueError("--queries is required when --router=query")
        query_texts = load_query_texts(queries)
        routed = route_query_rows(rows, query_texts)
        selected_mode = "query_conditioned"
        routed_mode = QUERY_ROUTED_MODE
    else:
        selected_mode = choose_dataset_mode(dataset)
        routed = route_dataset_rows(rows, dataset)
        routed_mode = DATASET_ROUTED_MODE

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        for row in routed:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    summary = {
        "dataset": dataset,
        "router": router,
        "selected_mode": selected_mode,
        "routed_mode": routed_mode,
        "input_rows": len(rows),
        "routed_rows": len(routed),
        "output": str(output),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Append routed angle modes to result rows.")
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dataset", default="unknown")
    parser.add_argument("--queries", type=Path)
    parser.add_argument("--router", choices=["dataset", "query"], default="dataset")
    args = parser.parse_args()
    run(args.results, args.output, args.dataset, args.queries, args.router)


if __name__ == "__main__":
    main()
