# Feedback report

Judgment: **PASS**
Primary cutoff: **top-3**

## Metrics

| k | mode | nDCG | MRR | AvgRel |
|---:|---|---:|---:|---:|
| 3 | baseline | 0.799869 | 0.933333 | 1.633333 |
| 3 | structure_causal_only | 0.782264 | 0.883333 | 1.600000 |
| 3 | structure_conclusion_only | 0.840654 | 0.933333 | 1.733333 |
| 3 | structure_contrast_only | 0.834062 | 0.933333 | 1.733333 |
| 3 | structure_definition_only | 0.841327 | 1.000000 | 1.666667 |
| 3 | structure_premise_only | 0.804065 | 0.933333 | 1.666667 |
| 3 | structure_rerank | 0.871324 | 1.000000 | 1.733333 |
| 5 | baseline | 0.825725 | 0.933333 | 1.080000 |
| 5 | structure_causal_only | 0.817942 | 0.883333 | 1.100000 |
| 5 | structure_conclusion_only | 0.855526 | 0.933333 | 1.120000 |
| 5 | structure_contrast_only | 0.832459 | 0.933333 | 1.060000 |
| 5 | structure_definition_only | 0.898532 | 1.000000 | 1.200000 |
| 5 | structure_premise_only | 0.835272 | 0.933333 | 1.120000 |
| 5 | structure_rerank | 0.919919 | 1.000000 | 1.220000 |
| 10 | baseline | 0.876868 | 0.933333 | 0.660000 |
| 10 | structure_causal_only | 0.864540 | 0.883333 | 0.660000 |
| 10 | structure_conclusion_only | 0.896243 | 0.933333 | 0.670000 |
| 10 | structure_contrast_only | 0.888890 | 0.933333 | 0.670000 |
| 10 | structure_definition_only | 0.935066 | 1.000000 | 0.690000 |
| 10 | structure_premise_only | 0.878141 | 0.933333 | 0.660000 |
| 10 | structure_rerank | 0.950782 | 1.000000 | 0.700000 |

## Ablation summary at primary cutoff

| mode | nDCG | AvgRel | MRR | delta nDCG | delta AvgRel |
|---|---:|---:|---:|---:|---:|
| structure_rerank | 0.871324 | 1.733333 | 1.000000 | 0.071455 | 0.100000 |
| structure_definition_only | 0.841327 | 1.666667 | 1.000000 | 0.041458 | 0.033334 |
| structure_conclusion_only | 0.840654 | 1.733333 | 0.933333 | 0.040785 | 0.100000 |
| structure_contrast_only | 0.834062 | 1.733333 | 0.933333 | 0.034193 | 0.100000 |
| structure_premise_only | 0.804065 | 1.666667 | 0.933333 | 0.004196 | 0.033334 |
| structure_causal_only | 0.782264 | 1.600000 | 0.883333 | -0.017605 | -0.033333 |

## Primary query deltas

| query_id | baseline AvgRel | structure AvgRel | delta | baseline top | structure top |
|---|---:|---:|---:|---|---|
| q1 | 1.000000 | 1.000000 | 0.000000 | p1 | p1 |
| q10 | 1.666667 | 1.666667 | 0.000000 | p20 | p20 |
| q2 | 2.000000 | 2.000000 | 0.000000 | p8 | p8 |
| q3 | 1.000000 | 1.000000 | 0.000000 | p3 | p3 |
| q4 | 2.333333 | 2.333333 | 0.000000 | p4 | p10 |
| q5 | 1.000000 | 2.000000 | 1.000000 | p6 | p6 |
| q6 | 1.000000 | 1.000000 | 0.000000 | p3 | p13 |
| q7 | 2.000000 | 2.000000 | 0.000000 | p5 | p11 |
| q8 | 2.000000 | 2.000000 | 0.000000 | p14 | p14 |
| q9 | 2.333333 | 2.333333 | 0.000000 | p19 | p19 |

## Next actions

- Use structure_rerank as the first candidate for the next real-like dataset comparison.
- Add a small real exported dataset without production secrets.
- Inspect improved queries to identify which structure type carried the gain.
