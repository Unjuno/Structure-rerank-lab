# Experiment summary

Overall status: **PASS**

## Top-3 comparison

| family | baseline | candidate | baseline nDCG@3 | candidate nDCG@3 | delta nDCG@3 | baseline AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| lexical | baseline | structure_rerank | 0.799869 | 0.871324 | 0.071455 | 1.633333 | 1.733333 | 0.100000 |
| vector | vector_baseline | vector_structure_rerank | 0.827494 | 0.860886 | 0.033392 | 1.700000 | 1.800000 | 0.100000 |

## Blockers

- none

## Degrading modes

- structure_causal_only: 1

## Degrading intent-matched modes

- none

## Degrading off-intent modes

- structure_causal_only: 1

## Next actions

- track off-intent ablation degradation separately: structure_causal_only
- add a real-like exported sample without secrets
- keep TF-IDF vector baseline as CI-safe baseline
- add optional neural embedding backend only after real-like sample check
