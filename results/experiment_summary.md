# Experiment summary

Overall status: **PASS**

## Top-3 comparison

| family | baseline | candidate | baseline nDCG@3 | candidate nDCG@3 | delta nDCG@3 | baseline AvgRel@3 | candidate AvgRel@3 | delta AvgRel@3 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| lexical | baseline | structure_rerank | 0.799869 | 0.873721 | 0.073852 | 1.633333 | 1.700000 | 0.066667 |
| vector | vector_baseline | vector_structure_rerank | 0.827494 | 0.867478 | 0.039984 | 1.700000 | 1.800000 | 0.100000 |

## Blockers

- none

## Degrading modes

- structure_causal_only: 1
- structure_rerank: 1

## Degrading intent-matched modes

- none

## Degrading off-intent modes

- structure_causal_only: 1
- structure_rerank: 1

## Next actions

- track off-intent ablation degradation separately: structure_causal_only, structure_rerank
- add a real-like exported sample without secrets
- keep TF-IDF vector baseline as CI-safe baseline
- add optional neural embedding backend only after real-like sample check
