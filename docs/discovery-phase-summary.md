# Discovery phase summary

## Status

Discovery phase is closed.

Active experimentation should stop here until comments, reviews, or a deliberate next-session plan justify more changes.

## What was tested

This repository tested whether sparse-vector retrieval improves when horizontal TF-IDF vector search is combined with vertical or diagonal structure-derived signals.

Tested mode families:

- baseline sparse vector search: `vector_baseline`
- structure rerank: `vector_structure_rerank`
- vertical vector rerank: `vertical_vector_rerank`
- diagonal vertical mixtures: `diagonal_vertical_05`, `diagonal_vertical_20`, `diagonal_vertical_35`, `diagonal_vertical_50`
- corpus-derived vertical modes: `corpus_vertical_rerank`, `diagonal_corpus_20`
- oracle-style dataset router: `angle_router`
- first query-only heuristic router: `query_angle_router`

## Main finding

The vertical-vector signal is useful.

A single fixed strong diagonal is not supported.

The best angle depends on the dataset or task:

| dataset | best observed mode |
|---|---|
| expanded real-like | `diagonal_vertical_50` |
| ArguAna | `diagonal_vertical_35` |
| SciFact | `vertical_vector_rerank` / `diagonal_vertical_20` |
| NFCorpus | `diagonal_vertical_35` |

## Safe default

Use this as the safe fixed default:

```text
vertical_vector_rerank / diagonal_vertical_20
```

Reason: it is not always the best, but it is the most stable fixed choice across the tested datasets.

## Modes not promoted

Do not promote these as main candidates in the current implementation:

- `corpus_vertical_rerank`
- `diagonal_corpus_20`
- `query_angle_router`

`corpus_vertical_rerank` and `diagonal_corpus_20` are weak in the current axis construction.

`query_angle_router` produced only a tiny real-like improvement:

| mode | nDCG@3 | AvgRel@3 | MRR |
|---|---:|---:|---:|
| `vertical_vector_rerank` | 0.875672 | 1.166667 | 1.000000 |
| `query_angle_router` | 0.876477 | 1.166667 | 1.000000 |

Delta nDCG@3: `0.000805`.

Delta AvgRel@3: `0.000000`.

This keeps the router hypothesis alive, but it is not enough to claim a strong query-only router.

## Correct next phase

The next phase is failure-case analysis, not more ad hoc router rules.

Next phase checklist:

1. List selected angle per query.
2. Compare changed ranks against `vertical_vector_rerank`.
3. Classify each query as helped, unchanged, or hurt.
4. Only then change query router rules.

## Feedback and ideas

Ideas, criticism, reproducibility concerns, and alternative experiment designs should be opened as GitHub Issues.

Useful issues are specific and testable. Good examples:

- a concrete failure case or counterexample
- a better way to construct vertical or diagonal axes
- a proposal for non-oracle query/task angle routing
- a reproducibility issue in the current reports
- a small public dataset that can be safely added
- a claim that the current interpretation is too strong or too weak

A good issue should include:

1. the claim
2. the evidence or intuition
3. the smallest check that would confirm or reject it

## Stop rule

Stop active experimentation here.

Resume only if:

- comments or reviews identify a concrete issue,
- a next-session plan starts the failure-case analysis phase,
- or a reproducibility problem is found in the existing report.

## Scope warning

These results are for the dependency-free sparse TF-IDF implementation. They do not prove superiority over neural dense embeddings.
