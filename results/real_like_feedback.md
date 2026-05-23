# Mode feedback report

Judgment: **UNCERTAIN**
Baseline mode: **baseline**
Candidate mode: **structure_rerank**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | baseline | 0.868817 | 1.000000 | 1.133333 |
| 3 | structure_rerank | 0.873356 | 1.000000 | 1.166667 |
| 5 | baseline | 0.892627 | 1.000000 | 0.760000 |
| 5 | structure_rerank | 0.891870 | 1.000000 | 0.760000 |
| 10 | baseline | 0.909588 | 1.000000 | 0.420000 |
| 10 | structure_rerank | 0.908830 | 1.000000 | 0.420000 |

## Primary query deltas

| query_id | baseline AvgRel | candidate AvgRel | delta | baseline top | candidate top |
|---|---:|---:|---:|---|---|
| rq1 | 1.333333 | 1.666667 | 0.333333 | r1 | r1 |
| rq10 | 1.333333 | 1.333333 | 0.000000 | r14 | r14 |
| rq2 | 1.000000 | 1.000000 | 0.000000 | r2 | r2 |
| rq3 | 1.333333 | 1.333333 | 0.000000 | r3 | r3 |
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
