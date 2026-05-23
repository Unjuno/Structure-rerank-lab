# Vector baseline

This lab now includes a dependency-free vector-space baseline.

It is **not** a neural embedding model. It is a sparse TF-IDF cosine scorer that can run in CI without downloads, model weights, API keys, or external services.

## Why start with this

The project needs a fast check before adding heavy embedding dependencies.

The current vector baseline tests whether structure-aware reranking still helps after moving from raw lexical overlap to a vector-space similarity model.

## Modes

The vector experiment emits:

- `vector_baseline`
- `vector_structure_rerank`

## Pipeline

```text
posts
  -> build TF-IDF vectors
queries
  -> vectorize query
  -> cosine similarity against post vectors
  -> vector_baseline ranking
  -> add structure score
  -> vector_structure_rerank ranking
```

## What this proves

A positive result means:

```text
structure reranking can improve over a simple dependency-free vector-space baseline on the sample dataset.
```

It does **not** prove:

```text
structure reranking improves over modern neural embeddings.
```

That requires a later optional embedding backend.

## Next upgrade path

1. Keep the TF-IDF vector baseline as the CI-safe baseline.
2. Add optional neural embedding output later.
3. Compare:
   - lexical baseline
   - TF-IDF vector baseline
   - TF-IDF vector + structure rerank
   - optional neural embedding baseline
   - optional neural embedding + structure rerank
