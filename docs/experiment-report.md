# Structure rerank experiment report

## Goal

Test whether retrieval improves when horizontal sparse-vector search is combined with vertical or diagonal structure-derived signals.

## Scope

This report covers the CI-safe sparse TF-IDF version of the idea. It does not claim results for neural dense embeddings.

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

## Summary

The vertical-vector signal is useful. Diagonal vertical mixtures can improve further, but the best fixed angle depends on the dataset.

Current practical conclusion:

- safest fixed mode: `vertical_vector_rerank` / `diagonal_vertical_20`
- best real-like mode: `diagonal_vertical_50`
- best ArguAna mode: `diagonal_vertical_35`
- best SciFact mode: `vertical_vector_rerank` / `diagonal_vertical_20`
- best NFCorpus mode: `diagonal_vertical_35`
- weak family: `corpus_vertical_rerank` and `diagonal_corpus_20`

## Expanded real-like dataset

Dataset size: 30 posts / 20 queries.

Best mode: `diagonal_vertical_50`.

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

## BEIR diagonal sweep

### ArguAna

Best mode: `diagonal_vertical_35`.

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 |
|---|---:|---:|---:|---:|
| diagonal_vertical_35 | 0.208268 | 0.033927 | 0.118333 | 0.020000 |
| diagonal_vertical_50 | 0.208150 | 0.033809 | 0.120000 | 0.021667 |
| vertical_vector_rerank | 0.198268 | 0.023927 | 0.111667 | 0.013334 |
| diagonal_vertical_20 | 0.198268 | 0.023927 | 0.111667 | 0.013334 |
| diagonal_vertical_05 | 0.177495 | 0.003154 | 0.100000 | 0.001667 |
| vector_structure_rerank | 0.174341 | 0.000000 | 0.098333 | 0.000000 |
| corpus_vertical_rerank | 0.159877 | -0.014464 | 0.090000 | -0.008333 |
| diagonal_corpus_20 | 0.159877 | -0.014464 | 0.090000 | -0.008333 |

### SciFact

Best mode: `vertical_vector_rerank` / `diagonal_vertical_20`.

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 |
|---|---:|---:|---:|---:|
| vertical_vector_rerank | 0.558624 | 0.006393 | 0.225000 | 0.005000 |
| diagonal_vertical_20 | 0.558624 | 0.006393 | 0.225000 | 0.005000 |
| vector_structure_rerank | 0.558092 | 0.005861 | 0.215000 | -0.005000 |
| corpus_vertical_rerank | 0.551901 | -0.000330 | 0.221667 | 0.001667 |
| diagonal_corpus_20 | 0.551901 | -0.000330 | 0.221667 | 0.001667 |
| diagonal_vertical_05 | 0.551365 | -0.000866 | 0.221667 | 0.001667 |
| diagonal_vertical_35 | 0.543967 | -0.008264 | 0.216667 | -0.003333 |
| diagonal_vertical_50 | 0.519224 | -0.033007 | 0.203333 | -0.016667 |

### NFCorpus

Best mode: `diagonal_vertical_35`.

| mode | nDCG@3 | delta nDCG@3 | AvgRel@3 | delta AvgRel@3 |
|---|---:|---:|---:|---:|
| diagonal_vertical_35 | 0.402485 | 0.011257 | 0.410000 | 0.016667 |
| vertical_vector_rerank | 0.399580 | 0.008352 | 0.401667 | 0.008334 |
| diagonal_vertical_20 | 0.399580 | 0.008352 | 0.401667 | 0.008334 |
| vector_structure_rerank | 0.398333 | 0.007105 | 0.396667 | 0.003334 |
| diagonal_vertical_05 | 0.395614 | 0.004386 | 0.398333 | 0.005000 |
| corpus_vertical_rerank | 0.392094 | 0.000866 | 0.393333 | 0.000000 |
| diagonal_corpus_20 | 0.392094 | 0.000866 | 0.393333 | 0.000000 |
| diagonal_vertical_50 | 0.392086 | 0.000858 | 0.403333 | 0.010000 |

## Interpretation

The results reject a single fixed strong-diagonal rule.

- `diagonal_vertical_50` is strong on the small expanded real-like set, but it fails on SciFact and is weak on NFCorpus.
- `diagonal_vertical_35` is strong on ArguAna and NFCorpus, but it hurts SciFact.
- `vertical_vector_rerank` / `diagonal_vertical_20` is not always the best, but it is the most stable fixed choice across tested datasets.
- `corpus_vertical_rerank` is not a main candidate in the current implementation.

The next useful hypothesis is not “use one fixed diagonal angle.” It is “select the angle by task or query.”

## Decision

Keep `vertical_vector_rerank` / `diagonal_vertical_20` as the safe default.

Promote `diagonal_vertical_35` and `diagonal_vertical_50` to task-conditioned candidates, not fixed global defaults.

Do not promote `corpus_vertical_rerank` without a different axis construction method.

## Next experiment

Implement a minimal angle router:

- ArguAna-like and NFCorpus-like cases: prefer `diagonal_vertical_35`
- SciFact-like cases: prefer `diagonal_vertical_20`
- fallback: `vertical_vector_rerank`

Then compare the routed result against the fixed `vertical_vector_rerank` baseline.

## Repository operation note

Heavy result-generation workflows should not run on every push. Future experiments should run on temporary experiment branches, record results, update this report, and then re-archive workflows before merging.
