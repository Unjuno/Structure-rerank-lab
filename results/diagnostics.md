# Diagnostics report

Primary diagnostic cutoff: **top-3**
Query count: **10**

## Helpful modes

| mode | improved query count |
|---|---:|
| structure_conclusion_only | 1 |
| structure_contrast_only | 1 |
| structure_rerank | 1 |

## Helpful intent-matched modes

| mode | improved query count |
|---|---:|
| structure_conclusion_only | 1 |

## Harmful modes

| mode | worsened query count |
|---|---:|
| none | 0 |

## Harmful intent-matched modes

| mode | worsened query count |
|---|---:|
| none | 0 |

## Harmful off-intent modes

| mode | worsened query count |
|---|---:|
| none | 0 |

## Per-query best/worst modes

| query_id | intent | baseline AvgRel | best mode | best AvgRel | worst mode | worst AvgRel |
|---|---|---:|---|---:|---|---:|
| q1 | conclusion | 1.000000 | baseline | 1.000000 | structure_rerank | 1.000000 |
| q10 | definition | 1.666667 | baseline | 1.666667 | structure_rerank | 1.666667 |
| q2 | causal | 2.000000 | baseline | 2.000000 | structure_rerank | 2.000000 |
| q3 | definition | 1.000000 | baseline | 1.000000 | structure_rerank | 1.000000 |
| q4 | contrast | 2.333333 | baseline | 2.333333 | structure_rerank | 2.333333 |
| q5 | conclusion | 1.000000 | structure_conclusion_only | 2.000000 | structure_premise_only | 1.000000 |
| q6 | definition | 1.000000 | baseline | 1.000000 | structure_rerank | 1.000000 |
| q7 | contrast | 2.000000 | baseline | 2.000000 | structure_rerank | 2.000000 |
| q8 | contrast | 2.000000 | baseline | 2.000000 | structure_rerank | 2.000000 |
| q9 | contrast | 2.333333 | baseline | 2.333333 | structure_rerank | 2.333333 |
