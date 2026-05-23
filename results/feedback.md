# Feedback report

Judgment: **PASS**

## Metrics

| mode | nDCG@10 | MRR | AvgRel@10 |
|---|---:|---:|---:|
| baseline | 0.951711 | 1.000000 | 0.625000 |
| structure_rerank | 0.967181 | 1.000000 | 0.625000 |

## Interpretation

- Structure rerank improves nDCG@10 from 0.951711 to 0.967181.
- MRR remains 1.000000 because the top relevant item is already first in this synthetic sample.
- AvgRel@10 remains 0.625000 because the dataset has only 8 posts and the top-10 window includes all posts.
- Therefore the current improvement is a rank-order improvement inside a too-small candidate set, not strong proof.

## Query deltas

| query_id | baseline AvgRel | structure AvgRel | delta | baseline top | structure top |
|---|---:|---:|---:|---|---|
| q1 | 0.750000 | 0.750000 | 0.000000 | p1 | p1 |
| q2 | 0.625000 | 0.625000 | 0.000000 | p8 | p8 |
| q3 | 0.625000 | 0.625000 | 0.000000 | p3 | p3 |
| q4 | 0.500000 | 0.500000 | 0.000000 | p4 | p4 |
| q5 | 0.625000 | 0.625000 | 0.000000 | p6 | p6 |

## Next actions

- Add a small real exported dataset without production secrets.
- Keep the same metrics and compare again before changing the scoring formula.
- Inspect ranking-order changes where AvgRel@10 is unchanged but nDCG@10 improves.
