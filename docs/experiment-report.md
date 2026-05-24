# Structure rerank experiment report

## Goal

Test whether retrieval improves when horizontal vector search is combined with vertical or diagonal structure-derived signals.

## Tested modes

- `vector_baseline`
- `vector_structure_rerank`
- `vertical_vector_rerank`
- `corpus_vertical_rerank`
- `diagonal_vertical_05`
- `diagonal_vertical_20`
- `diagonal_vertical_35`
- `diagonal_vertical_50`
- `diagonal_corpus_20`

## Current findings

### Expanded real-like dataset

Dataset size: 30 posts / 20 queries.

Best current mode: `diagonal_vertical_50`.

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 |
|---|---:|---:|---:|---:|
| diagonal_vertical_50 | 0.878747 | 0.019300 | 1.183333 | 0.083333 |
| diagonal_vertical_35 | 0.876477 | 0.017030 | 1.166667 | 0.066667 |
| vertical_vector_rerank | 0.875672 | 0.016225 | 1.166667 | 0.066667 |
| diagonal_vertical_20 | 0.875672 | 0.016225 | 1.166667 | 0.066667 |
| vector_structure_rerank | 0.870507 | 0.011060 | 1.150000 | 0.050000 |
| corpus_vertical_rerank | 0.861717 | 0.002270 | 1.116667 | 0.016667 |
| diagonal_corpus_20 | 0.861717 | 0.002270 | 1.116667 | 0.016667 |
| diagonal_vertical_05 | 0.859447 | 0.000000 | 1.100000 | 0.000000 |

### BEIR ArguAna

`vertical_vector_rerank` improved over `vector_baseline`; `corpus_vertical_rerank` failed.

| mode | nDCG@3 | AvgRel@3 | verdict |
|---|---:|---:|---|
| vector_baseline | 0.174341 | 0.098333 | - |
| vertical_vector_rerank | 0.198268 | 0.111667 | PASS |
| corpus_vertical_rerank | 0.159877 | 0.090000 | FAIL |

## Pending

- BEIR diagonal sweep for ArguAna, SciFact, and NFCorpus.
- Final decision after diagonal BEIR checks.

## Current interpretation

The vertical-vector idea is useful. The expanded real-like angle sweep suggests that stronger diagonal vertical mixing can outperform the default 0.8/0.2 vertical mixture.

However, diagonal modes are not yet validated on BEIR. Until then, `vertical_vector_rerank` remains the safer cross-dataset candidate.

## Repository operation note

Heavy result-generation workflows are archived and should not run on every push. Future experiments should run on temporary experiment branches, record results, update this report, and then re-archive workflows before merging.
