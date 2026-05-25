# Structure rerank experiment report

## Goal

Test whether retrieval improves when horizontal sparse-vector search is combined with vertical or diagonal structure-derived signals.

## Scope

This report covers the CI-safe sparse TF-IDF version of the idea. It does not claim results for neural dense embeddings.

This report closes the current discovery phase. Further work should focus on failure-case analysis rather than adding more ad hoc angle rules.

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
- `angle_router` as an oracle-style dataset-conditioned summary
- `query_angle_router` as a first non-oracle query-only heuristic

## Summary

The vertical-vector signal is useful. Diagonal vertical mixtures can improve further, but the best fixed angle depends on the dataset.

Current practical conclusion:

- safest fixed mode: `vertical_vector_rerank` / `diagonal_vertical_20`
- best real-like mode: `diagonal_vertical_50`
- best ArguAna mode: `diagonal_vertical_35`
- best SciFact mode: `vertical_vector_rerank` / `diagonal_vertical_20`
- best NFCorpus mode: `diagonal_vertical_35`
- weak family: `corpus_vertical_rerank` and `diagonal_corpus_20`
- oracle router shows angle-selection headroom
- first query-only router only gives a tiny real-like improvement

## Expanded real-like dataset

Dataset size: 30 posts / 20 queries.

Best fixed mode: `diagonal_vertical_50`.

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

## Oracle-style dataset router

The minimal dataset router selects the empirically best angle per dataset. This is not deployable by itself because it uses dataset identity. It is a headroom check.

| dataset | safe nDCG@3 | routed nDCG@3 | delta nDCG@3 | safe AvgRel@3 | routed AvgRel@3 | delta AvgRel@3 | selected mode |
|---|---:|---:|---:|---:|---:|---:|---|
| expanded real-like | 0.875672 | 0.878747 | 0.003075 | 1.166667 | 1.183333 | 0.016666 | `diagonal_vertical_50` |
| ArguAna | 0.198268 | 0.208268 | 0.010000 | 0.111667 | 0.118333 | 0.006666 | `diagonal_vertical_35` |
| SciFact | 0.558624 | 0.558624 | 0.000000 | 0.225000 | 0.225000 | 0.000000 | `diagonal_vertical_20` |
| NFCorpus | 0.399580 | 0.402485 | 0.002905 | 0.401667 | 0.410000 | 0.008333 | `diagonal_vertical_35` |

## First query-only router

The first non-oracle router uses cheap query text features only. It is intentionally small and heuristic.

Expanded real-like result:

| mode | nDCG@3 | AvgRel@3 | MRR |
|---|---:|---:|---:|
| vertical_vector_rerank | 0.875672 | 1.166667 | 1.000000 |
| query_angle_router | 0.876477 | 1.166667 | 1.000000 |

Delta nDCG@3: 0.000805.

Delta AvgRel@3: 0.000000.

This is a very small improvement. It is enough to keep the router hypothesis alive, but not enough to claim that the query-only heuristic is strong.

## Interpretation

The results reject a single fixed strong-diagonal rule.

- `diagonal_vertical_50` is strong on the small expanded real-like set, but it fails on SciFact and is weak on NFCorpus.
- `diagonal_vertical_35` is strong on ArguAna and NFCorpus, but it hurts SciFact.
- `vertical_vector_rerank` / `diagonal_vertical_20` is not always the best, but it is the most stable fixed choice across tested datasets.
- `corpus_vertical_rerank` is not a main candidate in the current implementation.
- the oracle-style dataset router shows positive headroom, but it is not yet a deployable router.
- the first query-only router gives only a tiny real-like gain.

The next useful work is not to keep adding angle rules immediately. The next useful work is failure-case analysis: inspect which queries changed angle, which rankings changed, and where the heuristic failed.

## Decision

Discovery phase is closed.

Keep `vertical_vector_rerank` / `diagonal_vertical_20` as the safe default.

Promote `diagonal_vertical_35` and `diagonal_vertical_50` to task-conditioned candidates, not fixed global defaults.

Do not promote `corpus_vertical_rerank` without a different axis construction method.

Do not promote `query_angle_router` yet. Treat it as a first weak non-oracle baseline.

## Next phase

Failure-case analysis phase:

- list selected angle per query
- compare changed ranks against `vertical_vector_rerank`
- identify queries where the router helped, did nothing, or hurt
- only then change the query router rules

## Repository operation note

Heavy result-generation workflows should not run on every push. Future experiments should run on temporary experiment branches, record results, update this report, and then re-archive workflows before merging.
