# Structure rerank experiment report

## Status

Initial scaffold. This report records the first controlled test of structure-aware reranking.

## Hypothesis

Adding explicit reasoning structures to baseline retrieval improves search quality for question and discussion logs.

## Dataset

- `examples/sample_posts.jsonl`
- `examples/sample_queries.jsonl`
- `examples/sample_structures.jsonl`
- `examples/sample_judgments.jsonl`

The current dataset is synthetic and intentionally small. It exists to verify the pipeline, not to prove the method.

## Method

Baseline:

- dependency-free lexical token overlap

Structure rerank:

- extract or read structure labels
- score candidate structures against query intent
- combine baseline and structure scores

Initial formula:

```text
final_score = 0.8 * baseline_score + 0.2 * structure_score
```

## Current metrics

Run locally or in CI:

```bash
python -m structure_rerank.evaluate
```

Expected output format:

```text
| mode | nDCG@10 | MRR | AvgRel@10 |
|---|---:|---:|---:|
| baseline | ... | ... | ... |
| structure_rerank | ... | ... | ... |
```

## Failure cases to inspect

- structure label matches but meaning does not.
- lexical baseline misses relevant posts before rerank.
- structure score overweights low-confidence structures.
- definition / contrast / causal structures are too coarse.

## Judgment

Current judgment: UNCERTAIN.

Reason: the first dataset is too small and synthetic. The next useful step is to add a small real exported dataset and compare against the same baseline.
