# Vector baseline

This lab includes dependency-free vector-space baselines and rerankers.

It is not a neural embedding model. It uses sparse TF-IDF cosine scoring so CI can run without model downloads or API keys.

## Modes

The vector experiment emits:

- `vector_baseline`
- `vector_structure_rerank`
- `vertical_vector_rerank`
- `corpus_vertical_rerank`

## Pipeline

```text
posts
  -> build TF-IDF vectors
queries
  -> vectorize query
  -> cosine similarity against post vectors
  -> vector_baseline ranking
  -> add horizontal or vertical structure score
```

## Current meaning

`vertical_vector_rerank` estimates structure axes as vectors, then compares query vectors against those axes and post structure vectors.

`corpus_vertical_rerank` estimates latent corpus axes from post vectors, then scores query/post alignment through those axes.

This is still not neural embedding search. It is the CI-safe sparse-vector version of the vertical-vector idea.

## External benchmark check

BEIR vertical-vector workflows run the same mode on ArguAna, SciFact, and NFCorpus.

ArguAna also has a compact corpus-vertical workflow for quick validation.

## Next upgrade path

1. Keep the TF-IDF vector baseline as the CI-safe baseline.
2. Compare `vector_structure_rerank`, `vertical_vector_rerank`, and `corpus_vertical_rerank`.
3. Add optional neural embedding output later.
