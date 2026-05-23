# structure-rerank-lab

Experimental lab for testing whether extracted reasoning structures improve search reranking.

## Hypothesis

Search over question/discussion logs can improve when baseline retrieval is reranked with explicit structure signals such as conclusions, premises, causal explanations, contrasts, and definitions.

## Scope

This repository is intentionally small.

It does **not** start by building a new vector database, a ColBERT-style retriever, an MCP server, or a production integration. It first tests whether structure-aware reranking has measurable value on reproducible sample data.

## Initial structure types

- `conclusion`
- `premise`
- `causal`
- `contrast`
- `definition`

## Minimal experiment

1. Run baseline lexical search over sample posts.
2. Read pre-extracted structures for each post.
3. Score candidates by structure match.
4. Combine baseline score and structure score.
5. Compare baseline and structure rerank with simple relevance judgments.

## Run

```bash
python -m structure_rerank.rerank
python -m structure_rerank.evaluate
```

## Current status

Initial lab scaffold. The first goal is not performance optimization; it is to produce a small, inspectable PASS / FAIL / UNCERTAIN result.
