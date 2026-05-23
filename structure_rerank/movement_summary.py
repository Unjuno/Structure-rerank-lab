from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results" / "beir" / "arguana" / "vertical_rank_movements.json"
DEFAULT_MD = ROOT / "results" / "movement_summary.md"
DEFAULT_JSON = ROOT / "results" / "movement_summary.json"


def load(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(report: Mapping[str, Any]) -> Dict[str, Any]:
    improved = 0
    harmed = 0
    neutral = 0
    entered_relevant = 0
    left_relevant = 0
    queries_with_relevant_up = []
    queries_with_relevant_down = []

    for query in report.get("queries", []):
        qid = str(query.get("query_id"))
        q_up = 0
        q_down = 0
        for move in query.get("moves", []):
            rel = int(move.get("relevance", 0) or 0)
            direction = str(move.get("direction"))
            if rel <= 0:
                neutral += 1
                continue
            if direction in {"up", "entered_top_k"}:
                improved += 1
                q_up += 1
                if direction == "entered_top_k":
                    entered_relevant += 1
            elif direction in {"down", "left_top_k"}:
                harmed += 1
                q_down += 1
                if direction == "left_top_k":
                    left_relevant += 1
            else:
                neutral += 1
        if q_up:
            queries_with_relevant_up.append({"query_id": qid, "count": q_up})
        if q_down:
            queries_with_relevant_down.append({"query_id": qid, "count": q_down})

    return {
        "baseline_mode": report.get("baseline_mode"),
        "compare_mode": report.get("compare_mode"),
        "k": report.get("k"),
        "improved_relevant_moves": improved,
        "harmed_relevant_moves": harmed,
        "neutral_or_irrelevant_moves": neutral,
        "entered_relevant": entered_relevant,
        "left_relevant": left_relevant,
        "queries_with_relevant_up": queries_with_relevant_up[:20],
        "queries_with_relevant_down": queries_with_relevant_down[:20],
    }


def write_md(summary: Mapping[str, Any], output: Path) -> None:
    lines = ["# Rank movement summary", ""]
    lines.append(f"Baseline mode: **{summary.get('baseline_mode')}**")
    lines.append(f"Compare mode: **{summary.get('compare_mode')}**")
    lines.append(f"Cutoff: **top-{summary.get('k')}**")
    lines.append("")
    lines.append("| metric | value |")
    lines.append("|---|---:|")
    for key in ["improved_relevant_moves", "harmed_relevant_moves", "neutral_or_irrelevant_moves", "entered_relevant", "left_relevant"]:
        lines.append(f"| {key} | {summary.get(key, 0)} |")
    lines.append("")
    lines.append("## Queries with relevant items moved up")
    lines.append("")
    if summary.get("queries_with_relevant_up"):
        for item in summary["queries_with_relevant_up"]:
            lines.append(f"- {item['query_id']}: {item['count']}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Queries with relevant items moved down")
    lines.append("")
    if summary.get("queries_with_relevant_down"):
        for item in summary["queries_with_relevant_down"]:
            lines.append(f"- {item['query_id']}: {item['count']}")
    else:
        lines.append("- none")
    lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def run(input_path: Path = DEFAULT_INPUT, output_md: Path = DEFAULT_MD, output_json: Path = DEFAULT_JSON) -> Dict[str, Any]:
    summary = summarize(load(input_path))
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    write_md(summary, output_md)
    output_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_md}")
    print(f"wrote {output_json}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    run(args.input, args.output_md, args.output_json)


if __name__ == "__main__":
    main()
