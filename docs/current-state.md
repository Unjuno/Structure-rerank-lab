# Current state

## Hypothesis

Retrieval should use two vector directions:

1. horizontal vector search over documents/posts
2. vertical vector estimation over structure axes/features

The current main candidate is `vertical_vector_rerank`.

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

## Current results

### Expanded real-like dataset

Dataset: 30 posts / 20 queries

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.859447 | 1.100000 | - |
| vector_structure_rerank | 0.870507 | 1.150000 | PASS |
| vertical_vector_rerank | 0.875672 | 1.166667 | PASS |
| corpus_vertical_rerank | 0.861717 | 1.116667 | UNCERTAIN |

### BEIR ArguAna

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.174341 | 0.098333 | - |
| vector_structure_rerank | 0.174341 | 0.098333 | UNCERTAIN |
| vertical_vector_rerank | 0.198268 | 0.111667 | PASS |
| corpus_vertical_rerank | 0.159877 | 0.090000 | FAIL |

### BEIR SciFact

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.552231 | 0.220000 | - |
| vector_structure_rerank | 0.558092 | 0.215000 | FAIL |
| vertical_vector_rerank | 0.558624 | 0.225000 | UNCERTAIN |
| corpus_vertical_rerank | not collected | not collected | MISSING |

### BEIR NFCorpus

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.391228 | 0.393333 | - |
| vector_structure_rerank | 0.398333 | 0.396667 | UNCERTAIN |
| vertical_vector_rerank | 0.399580 | 0.401667 | UNCERTAIN |
| corpus_vertical_rerank | not collected | not collected | MISSING |

## Current conclusion

`vertical_vector_rerank` remains the current main candidate.

`corpus_vertical_rerank` is implemented, but it is weaker than `vertical_vector_rerank` on expanded real-like and fails on BEIR ArguAna.

`diagonal_*` modes are implemented but still need an angle sweep result.

This does not prove superiority over dense neural embeddings.

## Active work

- Run angle sweep on `experiment/angle-sweep`.
- Compare diagonal variants against `vector_baseline` and `vertical_vector_rerank`.
- Keep `vertical_vector_rerank` as the main candidate unless angle sweep produces a stronger result.

## Next work

1. Collect `results/angle_sweep.md/json`.
2. If a diagonal mode wins, record it in `docs/current-state.md`.
3. Write an experiment report.
4. Clean up temporary workflows and branches.
