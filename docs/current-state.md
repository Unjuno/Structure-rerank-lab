# Current state

## Hypothesis

Retrieval should use two vector directions and angle mixtures:

1. horizontal vector search over documents/posts
2. vertical vector estimation over structure axes/features
3. diagonal mixtures of horizontal and vertical signals

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

`diagonal_vertical_50` is the best mode on expanded real-like data.

`vertical_vector_rerank` remains the safer cross-dataset candidate because it has BEIR support on ArguAna and non-negative evidence on SciFact/NFCorpus.

`corpus_vertical_rerank` is weak: it is only uncertain on expanded real-like and fails on BEIR ArguAna.

This does not prove superiority over dense neural embeddings.

## Active work

- Test diagonal vertical modes on BEIR.
- Keep corpus-derived axes experimental, not primary.
- Prepare a final experiment report after BEIR diagonal checks.

## Next work

1. Run diagonal modes on BEIR ArguAna, SciFact, and NFCorpus.
2. Compare diagonal modes against `vertical_vector_rerank`.
3. Write an experiment report.
4. Clean up temporary workflows and branches.
