from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEXICAL_FEEDBACK = ROOT / "results" / "feedback.json"
DEFAULT_VECTOR_FEEDBACK = ROOT / "results" / "vector_feedback.json"
DEFAULT_DIAGNOSTICS = ROOT / "results" / "diagnostics.json"
DEFAULT_OUTPUT_MD = ROOT / "results" / "experiment_summary.md"
DEFAULT_OUTPUT_JSON = ROOT / "results" / "experiment_summary.json"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"missing": True, "path": str(path)}
    return json.loads(path.read_text(encoding="utf-8"))


def _metric_row(feedback: Mapping[str, Any], k: int, baseline_mode: str, candidate_mode: str) -> Dict[str, Any]:
    metrics_by_k = feedback.get("metrics_by_k", {})
    metrics = metrics_by_k.get(str(k), {})
    baseline = metrics.get(baseline_mode, {})
    candidate = metrics.get(candidate_mode, {})
    ndcg_key = f"nDCG@{k}"
    avg_key = f"AvgRel@{k}"
    return {
        "k": k,
        "baseline_mode": baseline_mode,
        "candidate_mode": candidate_mode,
        "baseline_nDCG": float(baseline.get(ndcg_key, 0.0)),
        "candidate_nDCG": float(candidate.get(ndcg_key, 0.0)),
        "delta_nDCG": float(candidate.get(ndcg_key, 0.0)) - float(baseline.get(ndcg_key, 0.0)),
        "baseline_AvgRel": float(baseline.get(avg_key, 0.0)),
        "candidate_AvgRel": float(candidate.get(avg_key, 0.0)),
        "delta_AvgRel": float(candidate.get(avg_key, 0.0)) - float(baseline.get(avg_key, 0.0)),
    }


def summarize(
    lexical_feedback_path: Path,
    vector_feedback_path: Path,
    diagnostics_path: Path,
) -> Dict[str, Any]:
    lexical = load_json(lexical_feedback_path)
    vector = load_json(vector_feedback_path)
    diagnostics = load_json(diagnostics_path)

    lexical_row = _metric_row(lexical, 3, "baseline", "structure_rerank") if not lexical.get("missing") else None
    vector_row = _metric_row(vector, 3, "vector_baseline", "vector_structure_rerank") if not vector.get("missing") else None

    blockers: List[str] = []
    next_actions: List[str] = []

    if lexical.get("missing"):
        blockers.append("lexical feedback is missing")
    if vector.get("missing"):
        blockers.append("vector feedback is missing")

    if lexical_row and lexical_row["delta_nDCG"] <= 0:
        blockers.append("lexical structure rerank does not improve nDCG@3")
    if vector_row and vector_row["delta_nDCG"] <= 0:
        blockers.append("vector structure rerank does not improve nDCG@3")

    harmful_modes = diagnostics.get("harmful_modes", {}) if isinstance(diagnostics, dict) else {}
    if harmful_modes:
        next_actions.append(f"inspect harmful modes: {', '.join(harmful_modes.keys())}")
    if not blockers:
        next_actions.append("add a real-like exported sample without secrets")
        next_actions.append("keep TF-IDF vector baseline as CI-safe baseline")
        next_actions.append("add optional neural embedding backend only after real-like sample check")
    else:
        next_actions.append("fix blockers before adding more features")

    return {
        "status": "PASS" if not blockers else "NEEDS_WORK",
        "blockers": blockers,
        "lexical_top3": lexical_row,
        "vector_top3": vector_row,
        "harmful_modes": harmful_modes,
        "next_actions": next_actions,
    }


def write_md(summary: Mapping[str, Any], output_path: Path) -> None:
    lines: List[str] = ["# Experiment summary", ""]
    lines.append(f"Overall status: **{summary['status']}**")
    lines.append("")

    lines.append("## Top-3 comparison")
    lines.append("")
    lines.append("| family | baseline | candidate | baseline nDCG@3 | candidate nDCG@3 | delta nDCG@3 | baseline AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|")
    for family, row in [("lexical", summary.get("lexical_top3")), ("vector", summary.get("vector_top3"))]:
        if not row:
            lines.append(f"| {family} | missing | missing | 0 | 0 | 0 | 0 | 0 | 0 |")
            continue
        lines.append(
            f"| {family} | {row['baseline_mode']} | {row['candidate_mode']} | "
            f"{row['baseline_nDCG']:.6f} | {row['candidate_nDCG']:.6f} | {row['delta_nDCG']:.6f} | "
            f"{row['baseline_AvgRel']:.6f} | {row['candidate_AvgRel']:.6f} | {row['delta_AvgRel']:.6f} |"
        )

    lines.append("")
    lines.append("## Blockers")
    lines.append("")
    if summary["blockers"]:
        for item in summary["blockers"]:
            lines.append(f"- {item}")
    else:
        lines.append("- none")

    lines.append("")
    lines.append("## Harmful modes")
    lines.append("")
    harmful_modes = summary.get("harmful_modes", {})
    if harmful_modes:
        for mode, count in harmful_modes.items():
            lines.append(f"- {mode}: {count}")
    else:
        lines.append("- none")

    lines.append("")
    lines.append("## Next actions")
    lines.append("")
    for item in summary["next_actions"]:
        lines.append(f"- {item}")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run(
    lexical_feedback_path: Path = DEFAULT_LEXICAL_FEEDBACK,
    vector_feedback_path: Path = DEFAULT_VECTOR_FEEDBACK,
    diagnostics_path: Path = DEFAULT_DIAGNOSTICS,
    output_md_path: Path = DEFAULT_OUTPUT_MD,
    output_json_path: Path = DEFAULT_OUTPUT_JSON,
) -> Dict[str, Any]:
    summary = summarize(lexical_feedback_path, vector_feedback_path, diagnostics_path)
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    write_md(summary, output_md_path)
    output_json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"summary status: {summary['status']}")
    print(f"wrote {output_md_path}")
    print(f"wrote {output_json_path}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a combined lexical/vector experiment summary.")
    parser.add_argument("--lexical-feedback", type=Path, default=DEFAULT_LEXICAL_FEEDBACK)
    parser.add_argument("--vector-feedback", type=Path, default=DEFAULT_VECTOR_FEEDBACK)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    args = parser.parse_args()
    run(args.lexical_feedback, args.vector_feedback, args.diagnostics, args.output_md, args.output_json)


if __name__ == "__main__":
    main()
