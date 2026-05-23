# structure-rerank-lab

Experimental lab for testing whether extracted reasoning structures improve search reranking.

## Core hypothesis

Search over question/discussion logs can improve when baseline retrieval is reranked with explicit structure signals:

- `conclusion`
- `premise`
- `causal`
- `contrast`
- `definition`

## Current baselines

This repository currently tests two lightweight baselines:

| family | baseline | candidate |
|---|---|---|
| lexical | token-overlap lexical ranking | lexical + structure rerank |
| vector | dependency-free TF-IDF sparse vector cosine ranking | TF-IDF vector + structure rerank |

The vector baseline is **not** a neural embedding model. It is a CI-safe sparse TF-IDF vector baseline. Neural embeddings are intentionally left for a later optional backend.

## Experiment loop

```text
sample data
  -> baseline ranking
  -> structure-aware reranking
  -> metric evaluation
  -> feedback report
  -> diagnostics
  -> rank movement explanations
  -> combined experiment summary
```

The goal is not to claim production validity from a tiny synthetic dataset. The goal is to create a closed loop that can say:

- whether structure reranking helped
- which structure types helped
- which modes hurt
- which posts moved up or down
- what to fix next

## Main commands

```bash
# lexical experiment
python -m structure_rerank.rerank
python -m structure_rerank.evaluate --skip-rerank
python -m structure_rerank.feedback --skip-rerank
python -m structure_rerank.diagnose --skip-rerank
python -m structure_rerank.explain_moves --skip-rerank

# TF-IDF vector experiment
python -m structure_rerank.vector_experiment
python -m structure_rerank.evaluate --results results/vector_results.jsonl --skip-rerank
python -m structure_rerank.mode_feedback \
  --results results/vector_results.jsonl \
  --output-md results/vector_feedback.md \
  --output-json results/vector_feedback.json \
  --baseline-mode vector_baseline \
  --candidate-mode vector_structure_rerank
python -m structure_rerank.explain_moves \
  --results results/vector_results.jsonl \
  --explanations-md results/vector_rank_movements.md \
  --explanations-json results/vector_rank_movements.json \
  --baseline-mode vector_baseline \
  --compare-mode vector_structure_rerank \
  --skip-rerank

# combined summary
python -m structure_rerank.experiment_summary
```

## CI artifacts

GitHub Actions generates the following artifacts:

- `results/sample_results.jsonl`
- `results/feedback.md`
- `results/feedback.json`
- `results/diagnostics.md`
- `results/diagnostics.json`
- `results/rank_movements.md`
- `results/rank_movements.json`
- `results/vector_results.jsonl`
- `results/vector_feedback.md`
- `results/vector_feedback.json`
- `results/vector_rank_movements.md`
- `results/vector_rank_movements.json`
- `results/experiment_summary.md`
- `results/experiment_summary.json`

`results/` files committed to the repository are snapshots or placeholders. The CI artifact is the source of truth for the latest generated result.

## Current limitations

This lab does **not** yet prove:

- improvement over neural embeddings
- improvement on real production data
- robust automatic structure extraction
- usefulness of dimension gating

It currently tests a narrower claim:

```text
Given extracted structure labels, does structure-aware reranking improve retrieval over lexical and TF-IDF sparse-vector baselines on a small controlled dataset?
```

## Next step

After lexical and TF-IDF vector experiments both pass on the sample dataset, add a small real-like exported dataset with no secrets and rerun the same closed loop.
