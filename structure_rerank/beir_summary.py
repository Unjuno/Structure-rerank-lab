from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Mapping

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = ROOT / "results" / "beir"
DEFAULT_MD = DEFAULT_ROOT / "summary.md"
DEFAULT_JSON = DEFAULT_ROOT / "summary.json"
DATASETS = ["arguana", "scifact", "nfcorpus"]


def load(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"missing": True}
    return json.loads(path.read_text(encoding="utf-8"))


def top3(feedback: Mapping[str, Any], base: str, cand: str) -> Dict[str, Any]:
    metrics = feedback.get("metrics_by_k", {}).get("3", {})
    b = metrics.get(base, {})
    c = metrics.get(cand, {})
    return {
        "base": base,
        "candidate": cand,
        "base_nDCG": float(b.get("nDCG@3", 0.0)),
        "candidate_nDCG": float(c.get("nDCG@3", 0.0)),
        "delta_nDCG": float(c.get("nDCG@3", 0.0)) - float(b.get("nDCG@3", 0.0)),
        "base_AvgRel": float(b.get("AvgRel@3", 0.0)),
        "candidate_AvgRel": float(c.get("AvgRel@3", 0.0)),
        "delta_AvgRel": float(c.get("AvgRel@3", 0.0)) - float(b.get("AvgRel@3", 0.0)),
        "verdict": str(feedback.get("verdict", "MISSING")),
    }


def build(root: Path) -> Dict[str, Any]:
    rows = []
    for dataset in DATASETS:
        droot = root / dataset
        structure = load(droot / "vector_feedback.json")
        vertical = load(droot / "vertical_vector_feedback.json")
        if not structure.get("missing"):
            rows.append({"dataset": dataset, "mode": "vector_structure_rerank", **top3(structure, "vector_baseline", "vector_structure_rerank")})
        if not vertical.get("missing"):
            rows.append({"dataset": dataset, "mode": "vertical_vector_rerank", **top3(vertical, "vector_baseline", "vertical_vector_rerank")})
    return {"datasets": DATASETS, "rows": rows}


def write_md(summary: Mapping[str, Any], output: Path) -> None:
    lines = ["# BEIR summary", ""]
    lines.append("| dataset | mode | verdict | base nDCG@3 | candidate nDCG@3 | delta nDCG@3 | base AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|")
    for row in summary["rows"]:
        lines.append(
            f"| {row['dataset']} | {row['mode']} | {row['verdict']} | {row['base_nDCG']:.6f} | {row['candidate_nDCG']:.6f} | {row['delta_nDCG']:.6f} | {row['base_AvgRel']:.6f} | {row['candidate_AvgRel']:.6f} | {row['delta_AvgRel']:.6f} |"
        )
    lines.append("")
    lines.append("## Current read")
    lines.append("")
    lines.append("- Compare each dataset separately.")
    lines.append("- Do not average these datasets yet.")
    lines.append("- `vertical_vector_rerank` is the current main candidate.")
    lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def run(root: Path = DEFAULT_ROOT, output_md: Path = DEFAULT_MD, output_json: Path = DEFAULT_JSON) -> Dict[str, Any]:
    summary = build(root)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    write_md(summary, output_md)
    output_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_md}")
    print(f"wrote {output_json}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    run(args.root, args.output_md, args.output_json)


if __name__ == "__main__":
    main()
