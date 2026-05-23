# BEIR summary

| dataset | mode | verdict | base nDCG@3 | candidate nDCG@3 | delta nDCG@3 | base AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| arguana | vector_structure_rerank | UNCERTAIN | 0.174341 | 0.174341 | 0.000000 | 0.098333 | 0.098333 | 0.000000 |
| arguana | vertical_vector_rerank | PASS | 0.174341 | 0.198268 | 0.023927 | 0.098333 | 0.111667 | 0.013334 |
| scifact | vector_structure_rerank | FAIL | 0.552231 | 0.558092 | 0.005861 | 0.220000 | 0.215000 | -0.005000 |
| scifact | vertical_vector_rerank | UNCERTAIN | 0.552231 | 0.558624 | 0.006393 | 0.220000 | 0.225000 | 0.005000 |
| nfcorpus | vector_structure_rerank | UNCERTAIN | 0.391228 | 0.398333 | 0.007105 | 0.393333 | 0.396667 | 0.003334 |
| nfcorpus | vertical_vector_rerank | UNCERTAIN | 0.391228 | 0.399580 | 0.008352 | 0.393333 | 0.401667 | 0.008334 |

## Current read

- Compare each dataset separately.
- Do not average these datasets yet.
- `vertical_vector_rerank` is the current main candidate.
