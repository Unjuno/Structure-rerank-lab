# Mode feedback report

Judgment: **UNCERTAIN**
Baseline mode: **vector_baseline**
Candidate mode: **corpus_vertical_rerank**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | vector_baseline | 0.859447 | 1.000000 | 1.100000 |
| 3 | corpus_vertical_rerank | 0.861717 | 1.000000 | 1.116667 |
| 5 | vector_baseline | 0.883786 | 1.000000 | 0.750000 |
| 5 | corpus_vertical_rerank | 0.883407 | 1.000000 | 0.750000 |
| 10 | vector_baseline | 0.899367 | 1.000000 | 0.410000 |
| 10 | corpus_vertical_rerank | 0.899129 | 1.000000 | 0.410000 |

## Primary query deltas

| query_id | baseline AvgRel | candidate AvgRel | delta | baseline top | candidate top |
|---|---:|---:|---:|---|---|
| rq1 | 1.000000 | 1.000000 | 0.000000 | r1 | r1 |
| rq10 | 1.000000 | 1.000000 | 0.000000 | r14 | r14 |
| rq11 | 1.333333 | 1.333333 | 0.000000 | r17 | r17 |
| rq12 | 1.000000 | 1.000000 | 0.000000 | r18 | r18 |
| rq13 | 1.000000 | 1.000000 | 0.000000 | r19 | r19 |
| rq14 | 1.000000 | 1.000000 | 0.000000 | r20 | r20 |
| rq15 | 1.333333 | 1.666667 | 0.333333 | r21 | r21 |
| rq16 | 1.000000 | 1.000000 | 0.000000 | r22 | r22 |
| rq17 | 1.000000 | 1.000000 | 0.000000 | r23 | r23 |
| rq18 | 1.333333 | 1.333333 | 0.000000 | r24 | r24 |
| rq19 | 1.333333 | 1.333333 | 0.000000 | r25 | r25 |
| rq2 | 1.000000 | 1.000000 | 0.000000 | r2 | r2 |
| rq20 | 1.333333 | 1.333333 | 0.000000 | r30 | r30 |
| rq3 | 1.000000 | 1.000000 | 0.000000 | r3 | r3 |
| rq4 | 1.000000 | 1.000000 | 0.000000 | r4 | r4 |
| rq5 | 1.000000 | 1.000000 | 0.000000 | r5 | r5 |
| rq6 | 1.333333 | 1.333333 | 0.000000 | r6 | r6 |
| rq7 | 1.000000 | 1.000000 | 0.000000 | r7 | r7 |
| rq8 | 1.000000 | 1.000000 | 0.000000 | r8 | r8 |
| rq9 | 1.000000 | 1.000000 | 0.000000 | r9 | r9 |

## Next actions

- Increase query count and add harder cases.
- Do not claim improvement from this mode yet.
- Inspect rank movement explanations for near misses.
