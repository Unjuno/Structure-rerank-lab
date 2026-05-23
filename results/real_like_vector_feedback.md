# Mode feedback report

Judgment: **PASS**
Baseline mode: **vector_baseline**
Candidate mode: **vector_structure_rerank**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | vector_baseline | 0.853298 | 1.000000 | 1.066667 |
| 3 | vector_structure_rerank | 0.865597 | 1.000000 | 1.133333 |
| 5 | vector_baseline | 0.891060 | 1.000000 | 0.780000 |
| 5 | vector_structure_rerank | 0.893304 | 1.000000 | 0.780000 |
| 10 | vector_baseline | 0.909955 | 1.000000 | 0.440000 |
| 10 | vector_structure_rerank | 0.912199 | 1.000000 | 0.440000 |

## Primary query deltas

| query_id | baseline AvgRel | candidate AvgRel | delta | baseline top | candidate top |
|---|---:|---:|---:|---|---|
| rq1 | 1.000000 | 1.333333 | 0.333333 | r1 | r1 |
| rq10 | 1.000000 | 1.000000 | 0.000000 | r14 | r14 |
| rq2 | 1.000000 | 1.000000 | 0.000000 | r2 | r2 |
| rq3 | 1.333333 | 1.333333 | 0.000000 | r3 | r3 |
| rq4 | 1.000000 | 1.000000 | 0.000000 | r4 | r4 |
| rq5 | 1.000000 | 1.000000 | 0.000000 | r5 | r5 |
| rq6 | 1.333333 | 1.666667 | 0.333333 | r6 | r6 |
| rq7 | 1.000000 | 1.000000 | 0.000000 | r7 | r7 |
| rq8 | 1.000000 | 1.000000 | 0.000000 | r8 | r8 |
| rq9 | 1.000000 | 1.000000 | 0.000000 | r9 | r9 |

## Next actions

- Keep the candidate mode for the next dataset expansion.
- Add harder negative examples before tuning weights.
- Compare against an optional neural embedding backend later.
