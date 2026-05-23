from __future__ import annotations

import argparse
import json
import urllib.request
import zipfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

BASE_URL = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets"


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def download(dataset: str, cache_dir: Path) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    zip_path = cache_dir / f"{dataset}.zip"
    if not zip_path.exists():
        urllib.request.urlretrieve(f"{BASE_URL}/{dataset}.zip", zip_path)
    out_dir = cache_dir / dataset
    if not out_dir.exists():
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(cache_dir)
    return out_dir


def pick_qrels(dataset_dir: Path, split: str) -> Path:
    path = dataset_dir / "qrels" / f"{split}.tsv"
    if path.exists():
        return path
    candidates = sorted((dataset_dir / "qrels").glob("*.tsv"))
    if not candidates:
        raise FileNotFoundError(f"no qrels found in {dataset_dir}")
    return candidates[0]


def read_qrels(path: Path, max_queries: int | None) -> tuple[List[Dict[str, Any]], Set[str], Set[str]]:
    rows: List[Dict[str, Any]] = []
    query_ids: Set[str] = set()
    doc_ids: Set[str] = set()
    with path.open("r", encoding="utf-8") as f:
        header = next(f, "")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            qid, did, score = parts[0], parts[1], parts[2]
            if max_queries is not None and qid not in query_ids and len(query_ids) >= max_queries:
                continue
            query_ids.add(qid)
            doc_ids.add(did)
            rows.append({"query_id": qid, "post_id": did, "relevance": int(float(score))})
    return rows, query_ids, doc_ids


def text_of(row: Dict[str, Any]) -> str:
    title = str(row.get("title", "") or "")
    text = str(row.get("text", "") or "")
    return (title + " " + text).strip()


def weak_structures(doc_id: str, text: str) -> Dict[str, Any]:
    low = text.lower()
    structs: List[Dict[str, Any]] = []
    first = text[:500]
    if any(k in low for k in ["because", "due to", "therefore", "thus", "caused", "cause"]):
        structs.append({"type": "causal", "text": first, "confidence": 0.55})
    if any(k in low for k in ["however", "but", "whereas", "while", "unlike", "difference"]):
        structs.append({"type": "contrast", "text": first, "confidence": 0.55})
    if any(k in low for k in [" is ", " are ", " means ", " refers to ", " defined as "]):
        structs.append({"type": "definition", "text": first, "confidence": 0.45})
    structs.append({"type": "conclusion", "text": first, "confidence": 0.40})
    return {"post_id": doc_id, "structures": structs[:3]}


def convert(dataset: str, out: Path, cache: Path, split: str, max_queries: int | None, max_corpus: int | None) -> None:
    ddir = download(dataset, cache)
    qrels, qids, dids = read_qrels(pick_qrels(ddir, split), max_queries)
    corpus = read_jsonl(ddir / "corpus.jsonl")
    queries = read_jsonl(ddir / "queries.jsonl")

    selected_docs = []
    for row in corpus:
        doc_id = str(row.get("_id"))
        if doc_id in dids or max_corpus is None or len(selected_docs) < max_corpus:
            selected_docs.append({"id": doc_id, "text": text_of(row)})
    selected_ids = {row["id"] for row in selected_docs}
    selected_qrels = [row for row in qrels if row["post_id"] in selected_ids]
    selected_queries = [{"id": str(row.get("_id")), "query": str(row.get("text", "")), "intent_structure": "conclusion"} for row in queries if str(row.get("_id")) in qids]

    out.mkdir(parents=True, exist_ok=True)
    (out / "posts.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in selected_docs) + "\n", encoding="utf-8")
    (out / "queries.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in selected_queries) + "\n", encoding="utf-8")
    (out / "judgments.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in selected_qrels) + "\n", encoding="utf-8")
    (out / "structures.jsonl").write_text("\n".join(json.dumps(weak_structures(x["id"], x["text"]), ensure_ascii=False) for x in selected_docs) + "\n", encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dataset", required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--cache", type=Path, default=Path(".cache/beir"))
    p.add_argument("--split", default="test")
    p.add_argument("--max-queries", type=int, default=200)
    p.add_argument("--max-corpus", type=int, default=8000)
    a = p.parse_args()
    convert(a.dataset, a.out, a.cache, a.split, a.max_queries, a.max_corpus)


if __name__ == "__main__":
    main()
