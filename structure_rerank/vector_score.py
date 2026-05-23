from __future__ import annotations

import math
from collections import Counter
from typing import Dict, Iterable, List, Mapping, Tuple

from .structure_score import tokenize

SparseVector = Dict[str, float]


def build_idf(texts: Iterable[str]) -> Dict[str, float]:
    docs = [set(tokenize(text)) for text in texts]
    n_docs = len(docs)
    df: Counter[str] = Counter()
    for terms in docs:
        df.update(terms)
    return {term: math.log((n_docs + 1) / (count + 1)) + 1.0 for term, count in df.items()}


def vectorize(text: str, idf: Mapping[str, float]) -> SparseVector:
    tf = Counter(tokenize(text))
    if not tf:
        return {}
    max_tf = max(tf.values())
    vector: SparseVector = {}
    for term, count in tf.items():
        if term not in idf:
            continue
        vector[term] = (count / max_tf) * float(idf[term])
    return vector


def cosine(left: Mapping[str, float], right: Mapping[str, float]) -> float:
    if not left or not right:
        return 0.0
    if len(left) > len(right):
        left, right = right, left
    dot = sum(value * right.get(term, 0.0) for term, value in left.items())
    if dot == 0.0:
        return 0.0
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return dot / (left_norm * right_norm)


def build_post_vectors(posts: List[Mapping[str, object]]) -> Tuple[Dict[str, SparseVector], Dict[str, float]]:
    idf = build_idf(str(post["text"]) for post in posts)
    vectors = {str(post["id"]): vectorize(str(post["text"]), idf) for post in posts}
    return vectors, idf


def vector_scores(query_text: str, post_vectors: Mapping[str, SparseVector], idf: Mapping[str, float]) -> Dict[str, float]:
    query_vector = vectorize(query_text, idf)
    return {post_id: cosine(query_vector, post_vector) for post_id, post_vector in post_vectors.items()}
