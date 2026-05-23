from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Mapping

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEXICAL = ROOT / "results" / "real_like_feedback.json"
DEFAULT_VECTOR = ROOT / "results" / "real_like_vector_feedback.json"
DEFAULT_MD = ROOT / "results" / "real_like_summary.md"
DEFAULT_JSON = ROOT / "results" / "real_like_summary.json"


def load(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"missing": True}
    return json.loads(path.read_text(encoding="utf-8"))


def row(data: Mapping[str, Any], k: int, base: str, cand: str) -> Dict[str, Any]:
    metrics = data.get("metrics_by_k", {}).get(str(k), {})
    b = metrics.get(base, {})
    c = metrics.get(cand, {})
    nk = f"nDCG@{k}"
    ak = f"AvgRel@{k}"
    return {
        "base": base,
        "candidate": cand,
        "base_nDCG": float(b.get(nk, 0.0)),
        "candidate_nDCG": float(c.get(nk, 0.0)),
        "delta_nDCG": float(c.get(nk, 0.0)) - float(b.get(nk, 0.0)),
        "base_AvgRel": float(b.get(ak, 0.0)),
        "candidate_AvgRel": float(c.get(ak, 0.0)),
        "delta_AvgRel": float(c.get(ak, 0.0)) - float(b.get(ak, 0.0)),
    }


def verdict(r: Mapping[str, Any]) -> str:
    if r["delta_nDCG"] >= 0.01 and r["delta_AvgRel"] >= 0:
        return "PASS"
    if r["delta_nDCG"] <= -0.01 or r["delta_AvgRel"] < 0:
        return "FAIL"
    return "UNCERTAIN"


def build(lexical_path: Path, vector_path: Path) -> Dict[str, Any]:
    lexical = load(lexical_path)
    vector = load(vector_path)
    lrow = row(lexical, 3, "baseline", "structure_rerank") if not lexical.get("missing") else None
    vrow = row(vector, 3, "vector_baseline", "vector_structure_rerank") if not vector.get("missing") else None
    lv = verdict(lrow) if lrow else "MISSING"
    vv = verdict(vrow) if vrow else "MISSING"
    status = "PASS" if lv == "PASS" and vv == "PASS" else "VECTOR_ONLY_PASS" if vv == "PASS" else "NEEDS_WORK"
    return {
        "status": status,
        "lexical_verdict": lv,
        "vector_verdict": vv,
        "lexical_top3": lrow,
        "vector_top3": vrow,
    }


def write_md(summary: Mapping[str, Any], path: Path) -> None:
    lines = ["# Real-like experiment summary", "", f"Overall status: **{summary['status']}**", ""]
    lines.append("| family | verdict | base | candidate | base nDCG@3 | candidate nDCG@3 | delta nDCG@3 | base AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |")
    lines.append("|---|---|---|---|---:|---:|---:|---:|---:|---:|")
    for family, verdict_text, item in [("lexical", summary["lexical_verdict"], summary.get("lexical_top3")), ("vector", summary["vector_verdict"], summary.get("vector_top3"))]:
        if not item:
            lines.append(f"| {family} | MISSING | - | - | 0 | 0 | 0 | 0 | 0 | 0 |")
            continue
        lines.append(f"| {family} | {verdict_text} | {item['base']} | {item['candidate']} | {item['base_nDCG']:.6f} | {item['candidate_nDCG']:.6f} | {item['delta_nDCG']:.6f} | {item['base_AvgRel']:.6f} | {item['candidate_AvgRel']:.6f} | {item['delta_AvgRel']:.6f} |")
    lines.append("")
    lines.append("## Decision")
    lines.append("")
    if summary["status"] == "VECTOR_ONLY_PASS":
        lines.append("- Use vector_structure_rerank as the main real-like candidate.")
        lines.append("- Treat lexical structure rerank as unstable on real-like data.")
    elif summary["status"] == "PASS":
        lines.append("- Expand the real-like dataset.")
    else:
        lines.append("- Inspect rank movements before adding features.")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def run(lexical: Path = DEFAULT_LEXICAL, vector: Path = DEFAULT_VECTOR, output_md: Path = DEFAULT_MD, output_json: Path = DEFAULT_JSON) -> Dict[str, Any]:
    summary = build(lexical, vector)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    write_md(summary, output_md)
    output_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"real-like status: {summary['status']}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lexical", type=Path, default=DEFAULT_LEXICAL)
    parser.add_argument("--vector", type=Path, default=DEFAULT_VECTOR)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    run(args.lexical, args.vector, args.output_md, args.output_json)


if __name__ == "__main__":
    main()
