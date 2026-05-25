from __future__ import annotations

import argparse
import json
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
ROUTED_MODE = "angle_router"


def choose_mode(dataset: str, mapping: Mapping[str, str] = DEFAULT_DATASET_MODE) -> str:
    return mapping.get(dataset.lower(), FALLBACK_MODE)


def route_rows(rows: Iterable[Mapping[str, Any]], dataset: str, routed_mode: str = ROUTED_MODE) -> List[Dict[str, Any]]:
    selected_mode = choose_mode(dataset)
    routed: List[Dict[str, Any]] = []
    for row in rows:
        if str(row.get("mode")) != selected_mode:
            continue
        next_row = dict(row)
        next_row["source_mode"] = selected_mode
        next_row["mode"] = routed_mode
        routed.append(next_row)
    return routed


def run(results: Path = DEFAULT_RESULTS, output: Path = DEFAULT_OUTPUT, dataset: str = "unknown") -> Dict[str, Any]:
    rows = load_jsonl(results)
    selected_mode = choose_mode(dataset)
    routed = route_rows(rows, dataset)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        for row in routed:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    summary = {
        "dataset": dataset,
        "selected_mode": selected_mode,
        "routed_mode": ROUTED_MODE,
        "input_rows": len(rows),
        "routed_rows": len(routed),
        "output": str(output),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a dataset-conditioned routed angle mode to result rows.")
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dataset", required=True)
    args = parser.parse_args()
    run(args.results, args.output, args.dataset)


if __name__ == "__main__":
    main()
