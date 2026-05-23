# Real-like experiment summary

Overall status: **VECTOR_ONLY_PASS**

| family | verdict | base | candidate | base nDCG@3 | candidate nDCG@3 | delta nDCG@3 | base AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| lexical | UNCERTAIN | baseline | structure_rerank | 0.884787 | 0.889326 | 0.004539 | 1.200000 | 1.233333 | 0.033333 |
| vector | PASS | vector_baseline | vector_structure_rerank | 0.853298 | 0.865597 | 0.012299 | 1.066667 | 1.133333 | 0.066666 |

## Decision

- Use vector_structure_rerank as the main real-like candidate.
- Treat lexical structure rerank as unstable on real-like data.
