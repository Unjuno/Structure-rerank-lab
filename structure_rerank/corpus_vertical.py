from __future__ import annotations

import math
from typing import Dict, List, Mapping

from .vector_score import SparseVector, cosine, vectorize


def l2_norm(vector: Mapping[str, float]) -> float:
    return math.sqrt(sum(value * value for value in vector.values()))


def add_scaled(target: Dict[str, float], source: Mapping[str, float], scale: float = 1.0) -> None:
    for key, value in source.items():
        target[key] = target.get(key, 0.0) + value * scale


def scale_vector(vector: Mapping[str, float], scale: float) -> SparseVector:
    return {key: value * scale for key, value in vector.items() if value != 0.0}


def average_vectors(vectors: List[Mapping[str, float]]) -> SparseVector:
    if not vectors:
        return {}
    total: Dict[str, float] = {}
    for vector in vectors:
        add_scaled(total, vector, 1.0)
    return scale_vector(total, 1.0 / len(vectors))


def choose_seeds(post_vectors: Mapping[str, SparseVector], axis_count: int) -> List[str]:
    candidates = [post_id for post_id, vec in post_vectors.items() if vec]
    if not candidates:
        return []
    first = max(candidates, key=lambda post_id: (l2_norm(post_vectors[post_id]), post_id))
    seeds = [first]
    while len(seeds) < axis_count and len(seeds) < len(candidates):
        def distance_to_seeds(post_id: str) -> tuple[float, str]:
            best_sim = max(cosine(post_vectors[post_id], post_vectors[seed]) for seed in seeds)
            return (1.0 - best_sim, post_id)
        seeds.append(max((post_id for post_id in candidates if post_id not in seeds), key=distance_to_seeds))
    return seeds


def build_corpus_axes(post_vectors: Mapping[str, SparseVector], axis_count: int = 8, iterations: int = 3) -> Dict[str, SparseVector]:
    seeds = choose_seeds(post_vectors, axis_count)
    if not seeds:
        return {}
    axes = {f"axis_{i}": dict(post_vectors[seed]) for i, seed in enumerate(seeds)}
    for _ in range(iterations):
        buckets: Dict[str, List[Mapping[str, float]]] = {axis_id: [] for axis_id in axes}
        for vector in post_vectors.values():
            if not vector:
                continue
            axis_id = max(axes, key=lambda key: cosine(vector, axes[key]))
            buckets[axis_id].append(vector)
        next_axes = {axis_id: average_vectors(items) for axis_id, items in buckets.items() if items}
        if next_axes:
            axes = next_axes
    return axes


def query_axis_weights(query_text: str, axes: Mapping[str, SparseVector], idf: Mapping[str, float]) -> Dict[str, float]:
    query_vec = vectorize(query_text, idf)
    raw = {axis_id: max(cosine(query_vec, axis_vec), 0.0) for axis_id, axis_vec in axes.items()}
    total = sum(raw.values())
    if total <= 0.0:
        return {axis_id: 0.0 for axis_id in raw}
    return {axis_id: value / total for axis_id, value in raw.items()}


def corpus_vertical_scores(
    query_text: str,
    post_vectors: Mapping[str, SparseVector],
    idf: Mapping[str, float],
    axis_count: int = 8,
) -> Dict[str, float]:
    axes = build_corpus_axes(post_vectors, axis_count=axis_count)
    query_weights = query_axis_weights(query_text, axes, idf)
    query_vec = vectorize(query_text, idf)
    scores: Dict[str, float] = {}
    for post_id, post_vec in post_vectors.items():
        base = cosine(query_vec, post_vec)
        axis_alignment = sum(weight * cosine(post_vec, axes[axis_id]) for axis_id, weight in query_weights.items())
        scores[post_id] = base * max(axis_alignment, 0.0)
    return scores
