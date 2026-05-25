# Angle router summary

## Router rule

The minimal dataset-conditioned router selects one fixed mode per dataset:

| dataset | selected mode | reason |
|---|---|---|
| expanded real-like | `diagonal_vertical_50` | best nDCG@3 on expanded real-like |
| ArguAna | `diagonal_vertical_35` | best nDCG@3 on ArguAna |
| SciFact | `diagonal_vertical_20` / `vertical_vector_rerank` | best nDCG@3 and AvgRel@3 on SciFact |
| NFCorpus | `diagonal_vertical_35` | best nDCG@3 and AvgRel@3 on NFCorpus |

## Comparison against safe fixed mode

Safe fixed mode: `vertical_vector_rerank` / `diagonal_vertical_20`.

| dataset | safe nDCG@3 | routed nDCG@3 | delta nDCG@3 | safe AvgRel@3 | routed AvgRel@3 | delta AvgRel@3 | selected mode |
|---|---:|---:|---:|---:|---:|---:|---|
| expanded real-like | 0.875672 | 0.878747 | 0.003075 | 1.166667 | 1.183333 | 0.016666 | `diagonal_vertical_50` |
| ArguAna | 0.198268 | 0.208268 | 0.010000 | 0.111667 | 0.118333 | 0.006666 | `diagonal_vertical_35` |
| SciFact | 0.558624 | 0.558624 | 0.000000 | 0.225000 | 0.225000 | 0.000000 | `diagonal_vertical_20` |
| NFCorpus | 0.399580 | 0.402485 | 0.002905 | 0.401667 | 0.410000 | 0.008333 | `diagonal_vertical_35` |

## Interpretation

The minimal router never underperforms the safe fixed mode on the currently evaluated datasets, because it selects the empirically best angle per dataset.

This is an oracle-style dataset router, not yet a query-feature router. It proves that angle selection has useful headroom, but it does not prove that a deployable router can infer the right angle without dataset labels.

## Next validation

Implement and evaluate a non-oracle router that predicts the angle from query or corpus features.
