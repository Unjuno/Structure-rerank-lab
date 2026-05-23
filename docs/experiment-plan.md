# Experiment plan

## Goal

Test whether structure-aware reranking improves search quality over a simple baseline.

## Dataset

The initial dataset is intentionally synthetic and small. It contains short posts with manually prepared structure annotations and relevance judgments.

This avoids external API dependence and keeps CI reproducible.

## Pipeline

1. Load `examples/sample_posts.jsonl`.
2. Load `examples/sample_structures.jsonl`.
3. Load `examples/sample_queries.jsonl`.
4. Run baseline lexical retrieval.
5. Apply structure-aware reranking.
6. Evaluate baseline and reranked outputs using `examples/sample_judgments.jsonl`.

## Baseline

The baseline is a dependency-free lexical scorer using token overlap.

This is intentionally weak. It is not meant to beat modern retrieval systems. It is a controlled baseline that makes the first experiment reproducible.

## Structure rerank

The structure reranker adds a structure match score to the baseline score.

Initial score:

```text
final_score = alpha * baseline_score + beta * structure_score
```

Initial weights:

```text
alpha = 0.8
beta = 0.2
```

## Evaluation metrics

- AvgRel@10
- MRR
- nDCG@10

## Expected failure modes

- structure labels are too coarse.
- query intent is not captured by the structure type.
- lexical baseline is too weak and distorts the comparison.
- sample data is too small.

## Next step after first PASS

Replace the synthetic sample with real exported discussion/search examples, while keeping production data out of the repository.
