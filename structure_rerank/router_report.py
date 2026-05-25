from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Mapping

from .angle_router import DATASET_ROUTED_MODE, QUERY_ROUTED_MODE, choose_dataset_mode
from .evaluate import evaluate

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "results" / "angle_router_results.jsonl"
DEFAULT_JUDGMENTS = ROOT / "examples" / "sample_judgments.jsonl"
DEFAULT_MD = ROOT / "results" / "angle_router_report.md"
DEFAULT_JSON = ROOT / "results" / "angle_router_report.json"
BASELINE_MODE = "vertical_vector_rerank"


def build(results: Path, judgments: Path, dataset: str, routed_mode: str, k: int = 3) -> Dict[str, Any]:
    metrics = evaluate(results, judgments, k=k)
    baseline = metrics.get(BASELINE_MODE, {})
    routed = metrics.get(routed_mode, {})
    b_ndcg = float(baseline.get(f"nDCG@{k}", 0.0))
    r_ndcg = float(routed.get(f"nDCG@{k}", 0.0))
    b_avg = float(baseline.get(f"AvgRel@{k}", 0.0))
    r_avg = float(routed.get(f"AvgRel@{k}", 0.0))
    return {
        "dataset": dataset,
        "k": k,
        "selected_mode": choose_dataset_mode(dataset) if routed_mode == DATASET_ROUTED_MODE else "query_conditioned",
        "baseline_mode": BASELINE_MODE,
        "routed_mode": routed_mode,
        "baseline": baseline,
        "routed": routed,
        "delta_nDCG": r_ndcg - b_ndcg,
        "delta_AvgRel": r_avg - b_avg,
    }


def write_md(report: Mapping[str, Any], output: Path) -> None:
    k = report["k"]
    baseline = report["baseline"]
    routed = report["routed"]
    lines = ["# Angle router report", ""]
    lines.append(f"Dataset: `{report['dataset']}`")
    lines.append(f"Router: `{report['routed_mode']}`")
    lines.append(f"Selected mode: `{report['selected_mode']}`")
    lines.append("")
    lines.append(f"| mode | nDCG@{k} | AvgRel@{k} | MRR |")
    lines.append("|---|---:|---:|---:|")
    lines.append(
        f"| {report['baseline_mode']} | {float(baseline.get(f'nDCG@{k}', 0.0)):.6f} | {float(baseline.get(f'AvgRel@{k}', 0.0)):.6f} | {float(baseline.get('MRR', 0.0)):.6f} |"
    )
    lines.append(
        f"| {report['routed_mode']} | {float(routed.get(f'nDCG@{k}', 0.0)):.6f} | {float(routed.get(f'AvgRel@{k}', 0.0)):.6f} | {float(routed.get('MRR', 0.0)):.6f} |"
    )
    lines.append("")
    lines.append(f"Delta nDCG@{k}: {float(report['delta_nDCG']):.6f}")
    lines.append(f"Delta AvgRel@{k}: {float(report['delta_AvgRel']):.6f}")
    lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def run(
    results: Path = DEFAULT_RESULTS,
    judgments: Path = DEFAULT_JUDGMENTS,
    output_md: Path = DEFAULT_MD,
    output_json: Path = DEFAULT_JSON,
    dataset: str = "unknown",
    routed_mode: str = DATASET_ROUTED_MODE,
    k: int = 3,
) -> Dict[str, Any]:
    report = build(results, judgments, dataset, routed_mode, k)
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
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--routed-mode", choices=[DATASET_ROUTED_MODE, QUERY_ROUTED_MODE], default=DATASET_ROUTED_MODE)
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()
    run(args.results, args.judgments, args.output_md, args.output_json, args.dataset, args.routed_mode, args.k)


if __name__ == "__main__":
    main()
