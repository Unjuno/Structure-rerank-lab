# Feedback report

Judgment: **PASS**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | baseline | 0.799869 | 0.933333 | 1.633333 |
| 3 | structure_rerank | 0.871324 | 1.000000 | 1.733333 |
| 5 | baseline | 0.825725 | 0.933333 | 1.080000 |
| 5 | structure_rerank | 0.919919 | 1.000000 | 1.220000 |
| 10 | baseline | 0.876868 | 0.933333 | 0.660000 |
| 10 | structure_rerank | 0.950782 | 1.000000 | 0.700000 |

## Interpretation

- The expanded sample now includes 20 posts and lexical hard negatives.
- Structure rerank improves nDCG and AvgRel at top-3, top-5, and top-10.
- The strongest visible top-3 gain is q5, where the reranker promotes the Markdown/reasoning-structure result over lexical traps.
- This is still synthetic. It demonstrates the feedback mechanism, not production validity.

## Primary query deltas

| query_id | baseline AvgRel | structure AvgRel | delta | baseline top | structure top |
|---|---:|---:|---:|---|---|
| q1 | 1.000000 | 1.000000 | 0.000000 | p1 | p1 |
| q2 | 2.000000 | 2.000000 | 0.000000 | p8 | p8 |
| q3 | 1.000000 | 1.000000 | 0.000000 | p3 | p3 |
| q4 | 2.333333 | 2.333333 | 0.000000 | p4 | p10 |
| q5 | 1.000000 | 2.000000 | 1.000000 | p6 | p6 |
| q6 | 1.000000 | 1.000000 | 0.000000 | p3 | p13 |
| q7 | 2.000000 | 2.000000 | 0.000000 | p5 | p11 |
| q8 | 2.000000 | 2.000000 | 0.000000 | p14 | p14 |
| q9 | 2.333333 | 2.333333 | 0.000000 | p19 | p19 |
| q10 | 1.666667 | 1.666667 | 0.000000 | p20 | p20 |

## Next actions

- Add a small real exported dataset without production secrets.
- Keep top-3/top-5/top-10 metrics and compare again before changing the scoring formula.
- Inspect improved queries to identify which structure types carried the gain.
