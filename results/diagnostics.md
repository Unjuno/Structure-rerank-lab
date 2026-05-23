# Diagnostics report

Primary diagnostic cutoff: **top-3**
Query count: **10**

## Helpful modes

| mode | improved query count |
|---|---:|
| structure_premise_only | 1 |
| structure_rerank | 1 |
| structure_conclusion_only | 1 |
| structure_contrast_only | 1 |
| structure_definition_only | 1 |

## Harmful modes

| mode | worsened query count |
|---|---:|
| structure_causal_only | 1 |

## Per-query best/worst modes

| query_id | baseline AvgRel | best mode | best AvgRel | worst mode | worst AvgRel |
|---|---:|---|---:|---|---:|
| q1 | 1.000000 | baseline | 1.000000 | structure_definition_only | 1.000000 |
| q2 | 2.000000 | structure_premise_only | 2.333333 | structure_definition_only | 2.000000 |
| q3 | 1.000000 | baseline | 1.000000 | structure_definition_only | 1.000000 |
| q4 | 2.333333 | baseline | 2.333333 | structure_causal_only | 2.000000 |
| q5 | 1.000000 | structure_rerank | 2.000000 | structure_definition_only | 1.000000 |
| q6 | 1.000000 | baseline | 1.000000 | structure_definition_only | 1.000000 |
| q7 | 2.000000 | baseline | 2.000000 | structure_definition_only | 2.000000 |
| q8 | 2.000000 | structure_definition_only | 2.333333 | structure_contrast_only | 2.000000 |
| q9 | 2.333333 | baseline | 2.333333 | structure_definition_only | 2.333333 |
| q10 | 1.666667 | baseline | 1.666667 | structure_definition_only | 1.666667 |

## Interpretation

- The full structure rerank helps q5, which is the intended formatting-vs-reasoning hard negative case.
- `structure_causal_only` hurts q4, so causal structure should not be boosted globally yet.
- Single-type modes help only isolated queries. Full rerank is still the default candidate.

## Next diagnostic target

Add query-level explanations that show which posts moved up or down after reranking.
