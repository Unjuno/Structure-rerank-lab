# Mode feedback report

Judgment: **PASS**
Baseline mode: **baseline**
Candidate mode: **structure_rerank**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | baseline | 0.878088 | 1.000000 | 1.166667 |
| 3 | structure_rerank | 0.892222 | 1.000000 | 1.233333 |
| 5 | baseline | 0.895290 | 1.000000 | 0.760000 |
| 5 | structure_rerank | 0.906506 | 1.000000 | 0.790000 |
| 10 | baseline | 0.915524 | 1.000000 | 0.425000 |
| 10 | structure_rerank | 0.919227 | 1.000000 | 0.425000 |

## Primary query deltas

| query_id | baseline AvgRel | candidate AvgRel | delta | baseline top | candidate top |
|---|---:|---:|---:|---|---|
| rq1 | 1.333333 | 1.666667 | 0.333333 | r1 | r1 |
| rq10 | 1.333333 | 1.333333 | 0.000000 | r14 | r14 |
| rq11 | 1.000000 | 1.000000 | 0.000000 | r17 | r17 |
| rq12 | 1.333333 | 1.333333 | 0.000000 | r18 | r18 |
| rq13 | 1.000000 | 1.666667 | 0.666667 | r19 | r19 |
| rq14 | 1.666667 | 1.666667 | 0.000000 | r20 | r20 |
| rq15 | 1.000000 | 1.333333 | 0.333333 | r21 | r21 |
| rq16 | 1.000000 | 1.000000 | 0.000000 | r22 | r22 |
| rq17 | 1.000000 | 1.000000 | 0.000000 | r23 | r23 |
| rq18 | 1.333333 | 1.333333 | 0.000000 | r24 | r24 |
| rq19 | 1.333333 | 1.333333 | 0.000000 | r25 | r25 |
| rq2 | 1.000000 | 1.000000 | 0.000000 | r2 | r2 |
| rq20 | 1.333333 | 1.333333 | 0.000000 | r30 | r30 |
| rq3 | 1.333333 | 1.333333 | 0.000000 | r3 | r3 |
| rq4 | 1.000000 | 1.000000 | 0.000000 | r4 | r4 |
| rq5 | 1.000000 | 1.000000 | 0.000000 | r5 | r5 |
| rq6 | 1.333333 | 1.333333 | 0.000000 | r6 | r6 |
| rq7 | 1.000000 | 1.000000 | 0.000000 | r7 | r7 |
| rq8 | 1.000000 | 1.000000 | 0.000000 | r8 | r8 |
| rq9 | 1.000000 | 1.000000 | 0.000000 | r9 | r9 |

## Next actions

- Keep the candidate mode for the next dataset expansion.
- Add harder negative examples before tuning weights.
- Compare against an optional neural embedding backend later.
