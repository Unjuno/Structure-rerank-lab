# Hypothesis

## Core hypothesis

Adding explicit reasoning-structure signals to baseline search results improves retrieval quality for question and discussion logs.

The first tested structures are:

- conclusion
- premise
- causal explanation
- contrast
- definition

## Why this may work

A single text similarity score often mixes several different signals:

- topical similarity
- wording similarity
- formatting similarity
- explanation style
- argument structure
- conclusion similarity
- premise similarity

For discussion search, users often want more than a topically similar document. They may want:

- the same conclusion with a different premise
- the same premise with a different conclusion
- a causal explanation
- a contrastive explanation
- a definition-like explanation

The experiment tests whether these structure-level signals improve reranking over a simple baseline.

## Minimal claim

This repository does not claim that structure-aware retrieval is always superior. It tests the narrower claim that structure-aware reranking can improve a small controlled retrieval task.

## PASS / FAIL / UNCERTAIN

PASS:

- structure rerank improves nDCG@10, MRR, or AvgRel@10 over baseline.
- failure cases are explainable and bounded.

FAIL:

- structure rerank does not improve retrieval quality.
- structure signals introduce obvious false positives.

UNCERTAIN:

- improvement appears only on a small subset of query types.
- sample size is too small.
- judgments are too noisy.
