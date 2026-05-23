# Vector baseline

This lab includes dependency-free vector-space baselines and rerankers.

It is not a neural embedding model. It uses sparse TF-IDF cosine scoring so CI can run without model downloads or API keys.

## Modes

The vector experiment emits:

- `vector_baseline`
- `vector_structure_rerank`
- `vertical_vector_rerank`
- `corpus_vertical_rerank`
- `diagonal_vertical_05`
- `diagonal_vertical_20`
- `diagonal_vertical_35`
- `diagonal_vertical_50`
- `diagonal_corpus_20`

## Pipeline

```text
posts
  -> build TF-IDF vectors
queries
  -> vectorize query
  -> cosine similarity against post vectors
  -> vector_baseline ranking
  -> add horizontal, vertical, or diagonal auxiliary score
```

## Current meaning

`vertical_vector_rerank` estimates structure axes as vectors, then compares query vectors against those axes and post structure vectors.

`corpus_vertical_rerank` estimates latent corpus axes from post vectors, then scores query/post alignment through those axes.

`diagonal_*` modes sweep different mixtures of horizontal and vertical-style scores.

The compact angle workflow writes `results/angle_sweep.*` when it completes.

This is still not neural embedding search. It is the CI-safe sparse-vector version of the vertical-vector idea.

## External benchmark check

BEIR vertical-vector workflows run the same mode on ArguAna, SciFact, and NFCorpus.

ArguAna also has a compact corpus-vertical workflow with a persisted status file.

## Next upgrade path

1. Keep the TF-IDF vector baseline as the CI-safe baseline.
2. Compare `vector_structure_rerank`, `vertical_vector_rerank`, `corpus_vertical_rerank`, and diagonal variants.
3. Add optional neural embedding output later.
