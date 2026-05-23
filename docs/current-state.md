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

## Current results

### Expanded real-like dataset

Dataset: 30 posts / 20 queries

| mode | nDCG@3 | AvgRel@3 |
|---|---:|---:|
| vector_baseline | 0.859447 | 1.100000 |
| vector_structure_rerank | 0.870507 | 1.150000 |
| vertical_vector_rerank | 0.875672 | 1.166667 |

### BEIR ArguAna

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.174341 | 0.098333 | - |
| vector_structure_rerank | 0.174341 | 0.098333 | UNCERTAIN |
| vertical_vector_rerank | 0.198268 | 0.111667 | PASS |

### BEIR SciFact

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.552231 | 0.220000 | - |
| vector_structure_rerank | 0.558092 | 0.215000 | FAIL |
| vertical_vector_rerank | 0.558624 | 0.225000 | UNCERTAIN |

### BEIR NFCorpus

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.391228 | 0.393333 | - |
| vector_structure_rerank | 0.398333 | 0.396667 | UNCERTAIN |
| vertical_vector_rerank | 0.399580 | 0.401667 | UNCERTAIN |

## Current conclusion

`vertical_vector_rerank` is consistently better than `vector_structure_rerank` in the current small tests.

This does not prove superiority over dense neural embeddings.

## Active work

- Generate BEIR summary from CI outputs.
- Generate BEIR vertical rank movement reports.
- Generate BEIR vertical rank movement summaries.
- Use rank movements to inspect why SciFact and NFCorpus gains are small.

## Next work

1. Improve vertical axis estimation beyond fixed structure types.
2. Add optional dense embedding backend later.
