from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, Iterable, List, Mapping, Sequence

from .vector_score import SparseVector, cosine, vectorize


def add_scaled(target: Dict[str, float], source: Mapping[str, float], scale: float = 1.0) -> None:
    for key, value in source.items():
        target[key] = target.get(key, 0.0) + value * scale


def scale_vector(vector: Mapping[str, float], scale: float) -> SparseVector:
    if scale == 0:
        return {}
    return {key: value * scale for key, value in vector.items()}


def build_structure_axes(
    structure_rows: Iterable[Mapping[str, Any]],
    idf: Mapping[str, float],
) -> Dict[str, SparseVector]:
    """Build vertical structure-axis vectors.

    Each structure type becomes a corpus-level prototype vector. This is the
    vertical side: instead of trusting a query label directly, the query is
    compared with type-level structure vectors estimated from the corpus.
    """

    sums: Dict[str, Dict[str, float]] = defaultdict(dict)
    counts: Dict[str, float] = defaultdict(float)
    for row in structure_rows:
        structures = row.get("structures", [])
        if not isinstance(structures, list):
            continue
        for item in structures:
            stype = str(item.get("type", "")).strip().lower()
            text = str(item.get("text", ""))
            confidence = float(item.get("confidence", 0.0) or 0.0)
            if not stype or not text:
                continue
            vec = vectorize(text, idf)
            add_scaled(sums[stype], vec, confidence)
            counts[stype] += max(confidence, 1e-9)
    axes: Dict[str, SparseVector] = {}
    for stype, vec in sums.items():
        denom = counts.get(stype, 1.0)
        axes[stype] = scale_vector(vec, 1.0 / denom)
    return axes


def build_post_structure_vectors(
    structure_rows: Iterable[Mapping[str, Any]],
    idf: Mapping[str, float],
) -> Dict[str, List[Dict[str, Any]]]:
    index: Dict[str, List[Dict[str, Any]]] = {}
    for row in structure_rows:
        post_id = str(row["post_id"])
        entries: List[Dict[str, Any]] = []
        for item in row.get("structures", []):
            stype = str(item.get("type", "")).strip().lower()
            text = str(item.get("text", ""))
            confidence = float(item.get("confidence", 0.0) or 0.0)
            entries.append(
                {
                    "type": stype,
                    "confidence": confidence,
                    "vector": vectorize(text, idf),
                }
            )
        index[post_id] = entries
    return index


def query_axis_weights(query_text: str, axes: Mapping[str, SparseVector], idf: Mapping[str, float]) -> Dict[str, float]:
    query_vec = vectorize(query_text, idf)
    raw = {stype: cosine(query_vec, axis_vec) for stype, axis_vec in axes.items()}
    total = sum(value for value in raw.values() if value > 0)
    if total <= 0:
        return {stype: 0.0 for stype in raw}
    return {stype: max(value, 0.0) / total for stype, value in raw.items()}


def vertical_vector_scores(
    query_text: str,
    post_structure_vectors: Mapping[str, Sequence[Mapping[str, Any]]],
    axes: Mapping[str, SparseVector],
    idf: Mapping[str, float],
) -> Dict[str, float]:
    query_vec = vectorize(query_text, idf)
    axis_weights = query_axis_weights(query_text, axes, idf)
    scores: Dict[str, float] = {}
    for post_id, entries in post_structure_vectors.items():
        best = 0.0
        for item in entries:
            stype = str(item.get("type", ""))
            confidence = float(item.get("confidence", 0.0) or 0.0)
            item_vec = item.get("vector", {})
            if not isinstance(item_vec, dict):
                continue
            local = cosine(query_vec, item_vec)
            axis = axis_weights.get(stype, 0.0)
            score = confidence * local * axis
            if score > best:
                best = score
        scores[post_id] = best
    return scores
