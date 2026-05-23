# Vector feedback report

Status: **pending CI artifact refresh**

This file is a repository-visible snapshot target for the dependency-free TF-IDF vector experiment.

The CI now runs:

```bash
python -m structure_rerank.vector_experiment
python -m structure_rerank.evaluate --results results/vector_results.jsonl --skip-rerank
python -m structure_rerank.feedback --results results/vector_results.jsonl --feedback-md results/vector_feedback.md --feedback-json results/vector_feedback.json --skip-rerank
```

## Modes

- `vector_baseline`
- `vector_structure_rerank`

## Purpose

This checks whether structure-aware reranking still helps when the baseline is a vector-space scorer instead of raw lexical overlap.

## Next action

Inspect the CI artifact and replace this snapshot with the generated metrics.
