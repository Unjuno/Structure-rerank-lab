from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping

from .evaluate import evaluate
from .structure_score import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results" / "real_like_expanded_vector_results.jsonl"
DEFAULT_JUDGMENTS = ROOT / "results" / "real_like_judgments_20.jsonl"
DEFAULT_MD = ROOT / "results" / "angle_sweep.md"
DEFAULT_JSON = ROOT / "results" / "angle_sweep.json"
DEFAULT_MODES = [
    "vector_structure_rerank",
    "vertical_vector_rerank",
    "corpus_vertical_rerank",
    "diagonal_vertical_05",
    "diagonal_vertical_20",
    "diagonal_vertical_35",
    "diagonal_vertical_50",
    "diagonal_corpus_20",
]


def build(results: Path, judgments: Path, modes: List[str], k: int) -> Dict[str, Any]:
    rows = load_jsonl(results)
    observed_modes = {str(row["mode"]) for row in rows}
    metrics = evaluate(results, judgments, k=k)
    baseline = metrics.get("vector_baseline", {})
    b_ndcg = float(baseline.get(f"nDCG@{k}", 0.0))
    b_avg = float(baseline.get(f"AvgRel@{k}", 0.0))
    items = []
    for mode in modes:
        if mode not in observed_modes:
            continue
        row = metrics.get(mode, {})
        ndcg = float(row.get(f"nDCG@{k}", 0.0))
        avg = float(row.get(f"AvgRel@{k}", 0.0))
        items.append(
            {
                "mode": mode,
                "nDCG": ndcg,
                "delta_nDCG": ndcg - b_ndcg,
                "AvgRel": avg,
                "delta_AvgRel": avg - b_avg,
                "MRR": float(row.get("MRR", 0.0)),
            }
        )
    items.sort(key=lambda item: (item["delta_nDCG"], item["delta_AvgRel"]), reverse=True)
    return {"k": k, "baseline": {"nDCG": b_ndcg, "AvgRel": b_avg}, "items": items}


def write_md(report: Mapping[str, Any], output: Path) -> None:
    lines = ["# Angle sweep", ""]
    lines.append(f"Primary cutoff: top-{report['k']}")
    lines.append("")
    lines.append("| mode | nDCG | delta nDCG | AvgRel | delta AvgRel | MRR |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for item in report["items"]:
        lines.append(
            f"| {item['mode']} | {item['nDCG']:.6f} | {item['delta_nDCG']:.6f} | {item['AvgRel']:.6f} | {item['delta_AvgRel']:.6f} | {item['MRR']:.6f} |"
        )
    lines.append("")
    if report["items"]:
        best = report["items"][0]
        lines.append(f"Best mode: **{best['mode']}**")
        lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def run(results: Path = DEFAULT_RESULTS, judgments: Path = DEFAULT_JUDGMENTS, output_md: Path = DEFAULT_MD, output_json: Path = DEFAULT_JSON, k: int = 3) -> Dict[str, Any]:
    report = build(results, judgments, DEFAULT_MODES, k)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    write_md(report, output_md)
    output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_md}")
    print(f"wrote {output_json}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--judgments", type=Path, default=DEFAULT_JUDGMENTS)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()
    run(args.results, args.judgments, args.output_md, args.output_json, args.k)


if __name__ == "__main__":
    main()
