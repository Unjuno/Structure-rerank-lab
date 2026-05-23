# Mode feedback report

Judgment: **PASS**
Baseline mode: **vector_baseline**
Candidate mode: **vector_structure_rerank**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | vector_baseline | 0.827494 | 0.933333 | 1.700000 |
| 3 | vector_structure_rerank | 0.869689 | 0.950000 | 1.766667 |
| 5 | vector_baseline | 0.863475 | 0.933333 | 1.160000 |
| 5 | vector_structure_rerank | 0.885063 | 0.950000 | 1.160000 |
| 10 | vector_baseline | 0.904456 | 0.933333 | 0.670000 |
| 10 | vector_structure_rerank | 0.926044 | 0.950000 | 0.670000 |

## Primary query deltas

| query_id | baseline AvgRel | candidate AvgRel | delta | baseline top | candidate top |
|---|---:|---:|---:|---|---|
| q1 | 1.000000 | 1.000000 | 0.000000 | p1 | p1 |
| q10 | 1.666667 | 1.666667 | 0.000000 | p20 | p20 |
| q2 | 2.000000 | 2.000000 | 0.000000 | p8 | p8 |
| q3 | 0.333333 | 1.000000 | 0.666667 | p15 | p15 |
| q4 | 2.000000 | 2.000000 | 0.000000 | p4 | p4 |
| q5 | 2.000000 | 2.000000 | 0.000000 | p6 | p6 |
| q6 | 1.666667 | 1.666667 | 0.000000 | p13 | p13 |
| q7 | 2.000000 | 2.000000 | 0.000000 | p5 | p11 |
| q8 | 2.000000 | 2.000000 | 0.000000 | p14 | p14 |
| q9 | 2.333333 | 2.333333 | 0.000000 | p19 | p19 |

## Next actions

- Keep the candidate mode for the next dataset expansion.
- Add harder negative examples before tuning weights.
- Compare against an optional neural embedding backend later.
