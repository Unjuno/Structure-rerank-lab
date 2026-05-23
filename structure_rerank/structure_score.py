from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple

_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def load_jsonl(path: str | Path) -> List[Dict[str, Any]]:
    """Load a JSONL file.

    Empty lines are ignored. The function is intentionally dependency-free so the
    initial experiment can run in GitHub Actions without installing packages.
    """

    rows: List[Dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_no}: {exc}") from exc
    return rows


def tokenize(text: str) -> List[str]:
    return [token.lower() for token in _TOKEN_RE.findall(text)]


def lexical_score(query: str, text: str) -> float:
    """Small baseline lexical score.

    This is deliberately simple. It is not intended to be a strong retrieval
    model; it is a reproducible baseline for measuring whether structure signals
    move relevant items upward.
    """

    query_terms = set(tokenize(query))
    if not query_terms:
        return 0.0
    text_terms = set(tokenize(text))
    if not text_terms:
        return 0.0
    overlap = query_terms & text_terms
    return len(overlap) / len(query_terms)


def normalize_scores(items: Sequence[Tuple[str, float]]) -> Dict[str, float]:
    if not items:
        return {}
    values = [score for _, score in items]
    lo = min(values)
    hi = max(values)
    if math.isclose(lo, hi):
        return {item_id: 1.0 if score > 0 else 0.0 for item_id, score in items}
    return {item_id: (score - lo) / (hi - lo) for item_id, score in items}


def build_structure_index(structure_rows: Iterable[Mapping[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    index: Dict[str, List[Dict[str, Any]]] = {}
    for row in structure_rows:
        post_id = str(row["post_id"])
        structures = row.get("structures", [])
        if not isinstance(structures, list):
            raise ValueError(f"structures for post {post_id} must be a list")
        index[post_id] = [dict(item) for item in structures]
    return index


def structure_score(query: Mapping[str, Any], structures: Sequence[Mapping[str, Any]]) -> float:
    """Score how well a post's structures match the query intent.

    The initial score combines:
    - type match: does the post contain the requested structure type?
    - text match: does extracted structure text overlap with the query?
    """

    intent = str(query.get("intent_structure", "")).strip().lower()
    query_text = str(query.get("query", ""))
    best = 0.0
    for item in structures:
        stype = str(item.get("type", "")).strip().lower()
        text = str(item.get("text", ""))
        confidence = float(item.get("confidence", 0.0) or 0.0)
        type_score = confidence if intent and stype == intent else 0.0
        text_score = lexical_score(query_text, text)
        score = 0.7 * type_score + 0.3 * text_score
        if score > best:
            best = score
    return best


def combine_scores(base_score: float, struct_score: float, alpha: float = 0.8, beta: float = 0.2) -> float:
    if alpha < 0 or beta < 0:
        raise ValueError("alpha and beta must be non-negative")
    return alpha * base_score + beta * struct_score
