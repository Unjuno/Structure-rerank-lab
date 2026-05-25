# Current state

## Hypothesis

Retrieval should use two vector directions and angle mixtures:

1. horizontal vector search over documents/posts
2. vertical vector estimation over structure axes/features
3. diagonal mixtures of horizontal and vertical signals

## Phase status

Discovery phase is closed.

The next phase is failure-case analysis. Do not keep adding angle rules until changed-query diagnostics are inspected.

## Implemented modes

- `vector_baseline`
- `vector_structure_rerank`
- `vertical_vector_rerank`
- `corpus_vertical_rerank`
- `diagonal_vertical_05`
- `diagonal_vertical_20`
- `diagonal_vertical_35`
- `diagonal_vertical_50`
- `diagonal_corpus_20`
- `angle_router` as an oracle-style dataset-conditioned summary
- `query_angle_router` as a first non-oracle query-only heuristic

## Current results

### Expanded real-like dataset

Dataset: 30 posts / 20 queries

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 | verdict |
|---|---:|---:|---:|---:|---|
| vector_baseline | 0.859447 | - | 1.100000 | - | - |
| diagonal_vertical_50 | 0.878747 | 0.019300 | 1.183333 | 0.083333 | PASS |
| diagonal_vertical_35 | 0.876477 | 0.017030 | 1.166667 | 0.066667 | PASS |
| vertical_vector_rerank | 0.875672 | 0.016225 | 1.166667 | 0.066667 | PASS |
| diagonal_vertical_20 | 0.875672 | 0.016225 | 1.166667 | 0.066667 | PASS |
| vector_structure_rerank | 0.870507 | 0.011060 | 1.150000 | 0.050000 | PASS |
| corpus_vertical_rerank | 0.861717 | 0.002270 | 1.116667 | 0.016667 | UNCERTAIN |
| diagonal_corpus_20 | 0.861717 | 0.002270 | 1.116667 | 0.016667 | UNCERTAIN |
| diagonal_vertical_05 | 0.859447 | 0.000000 | 1.100000 | 0.000000 | UNCERTAIN |

### BEIR ArguAna diagonal sweep

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 | verdict |
|---|---:|---:|---:|---:|---|
| diagonal_vertical_35 | 0.208268 | 0.033927 | 0.118333 | 0.020000 | BEST |
| diagonal_vertical_50 | 0.208150 | 0.033809 | 0.120000 | 0.021667 | STRONG |
| vertical_vector_rerank | 0.198268 | 0.023927 | 0.111667 | 0.013334 | PASS |
| diagonal_vertical_20 | 0.198268 | 0.023927 | 0.111667 | 0.013334 | PASS |
| corpus_vertical_rerank | 0.159877 | -0.014464 | 0.090000 | -0.008333 | FAIL |

### BEIR SciFact diagonal sweep

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 | verdict |
|---|---:|---:|---:|---:|---|
| vertical_vector_rerank | 0.558624 | 0.006393 | 0.225000 | 0.005000 | BEST |
| diagonal_vertical_20 | 0.558624 | 0.006393 | 0.225000 | 0.005000 | BEST |
| vector_structure_rerank | 0.558092 | 0.005861 | 0.215000 | -0.005000 | MIXED |
| diagonal_vertical_35 | 0.543967 | -0.008264 | 0.216667 | -0.003333 | FAIL |
| diagonal_vertical_50 | 0.519224 | -0.033007 | 0.203333 | -0.016667 | FAIL |

### BEIR NFCorpus diagonal sweep

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 | verdict |
|---|---:|---:|---:|---:|---|
| diagonal_vertical_35 | 0.402485 | 0.011257 | 0.410000 | 0.016667 | BEST |
| vertical_vector_rerank | 0.399580 | 0.008352 | 0.401667 | 0.008334 | PASS |
| diagonal_vertical_20 | 0.399580 | 0.008352 | 0.401667 | 0.008334 | PASS |
| vector_structure_rerank | 0.398333 | 0.007105 | 0.396667 | 0.003334 | PASS |
| diagonal_vertical_50 | 0.392086 | 0.000858 | 0.403333 | 0.010000 | WEAK |

### Oracle-style dataset router

| dataset | safe nDCG@3 | routed nDCG@3 | delta nDCG@3 | safe AvgRel@3 | routed AvgRel@3 | delta AvgRel@3 | selected mode |
|---|---:|---:|---:|---:|---:|---:|---|
| expanded real-like | 0.875672 | 0.878747 | 0.003075 | 1.166667 | 1.183333 | 0.016666 | `diagonal_vertical_50` |
| ArguAna | 0.198268 | 0.208268 | 0.010000 | 0.111667 | 0.118333 | 0.006666 | `diagonal_vertical_35` |
| SciFact | 0.558624 | 0.558624 | 0.000000 | 0.225000 | 0.225000 | 0.000000 | `diagonal_vertical_20` |
| NFCorpus | 0.399580 | 0.402485 | 0.002905 | 0.401667 | 0.410000 | 0.008333 | `diagonal_vertical_35` |

### First query-only router

Expanded real-like:

| mode | nDCG@3 | AvgRel@3 | MRR |
|---|---:|---:|---:|
| vertical_vector_rerank | 0.875672 | 1.166667 | 1.000000 |
| query_angle_router | 0.876477 | 1.166667 | 1.000000 |

Delta nDCG@3: 0.000805

Delta AvgRel@3: 0.000000

## Current conclusion

The vertical-vector idea is supported.

A single fixed strong diagonal is not supported:

- `diagonal_vertical_50` is best on expanded real-like.
- `diagonal_vertical_35` is best on ArguAna and NFCorpus.
- `vertical_vector_rerank` / `diagonal_vertical_20` is best on SciFact.

Therefore, the current safe default is `vertical_vector_rerank` / `diagonal_vertical_20`.

The first query-only router keeps the router hypothesis alive, but the improvement is tiny.

`corpus_vertical_rerank` is weak in the current implementation and should not be promoted without a different axis construction method.

This does not prove superiority over dense neural embeddings.

## Next phase

Failure-case analysis:

1. list selected angle per query
2. compare changed ranks against `vertical_vector_rerank`
3. identify queries where the router helped, did nothing, or hurt
4. only then change query router rules

## Hold policy

Stop active experimentation here. Resume only when comments, reviews, or a deliberate next-session plan require changes.
