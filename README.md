# structure-rerank-lab

Experimental lab for testing whether extracted reasoning structures improve search reranking.

## Current status

Discovery phase is closed.

Active experimentation should pause here. Resume only for comments, reviews, reproducibility fixes, or a deliberate next-session plan for failure-case analysis.

Current practical result:

- safe fixed default: `vertical_vector_rerank` / `diagonal_vertical_20`
- useful but task-dependent: `diagonal_vertical_35`, `diagonal_vertical_50`
- not promoted in the current implementation: `corpus_vertical_rerank`, `diagonal_corpus_20`
- first query-only router: tiny improvement only, not yet a strong result

Primary docs:

1. `docs/current-state.md`
2. `docs/experiment-report.md`
3. `docs/discovery-phase-summary.md`

## Ideas and review comments

If you have an idea, criticism, reproducibility concern, or a better experiment design, please open a GitHub Issue.

Useful issues include:

- a concrete failure case or counterexample
- a better way to build vertical or diagonal axes
- a proposal for query/task-conditioned angle selection
- a reproducibility problem in the current reports
- a small public dataset that can be safely added
- a reason the current interpretation is too strong or too weak

Please keep issues specific. A useful issue should state the claim, the evidence or intuition behind it, and the smallest check that would confirm or reject it.

## Core hypothesis

Search over question/discussion logs can improve when baseline retrieval is combined with explicit structure or vertical-vector signals.

The current tested signal families are:

- horizontal sparse-vector search
- structure-aware reranking
- vertical vector reranking
- diagonal mixtures of horizontal and vertical scores
- simple router experiments for angle selection

## Current baselines and candidates

| family | baseline | candidate |
|---|---|---|
| lexical | token-overlap lexical ranking | lexical + structure rerank |
| vector | dependency-free TF-IDF sparse vector cosine ranking | TF-IDF vector + structure/vertical/diagonal rerank |
| router | fixed `vertical_vector_rerank` / `diagonal_vertical_20` | oracle dataset router and first query-only router |

The vector baseline is **not** a neural embedding model. It is a CI-safe sparse TF-IDF vector baseline. Neural embeddings are intentionally left for a later optional backend.

## Key discovery-phase findings

The vertical-vector signal is useful.

A single fixed strong diagonal is not supported. The best angle depends on the dataset/task:

| dataset | best observed mode |
|---|---|
| expanded real-like | `diagonal_vertical_50` |
| ArguAna | `diagonal_vertical_35` |
| SciFact | `vertical_vector_rerank` / `diagonal_vertical_20` |
| NFCorpus | `diagonal_vertical_35` |

The first query-only router produced only a tiny expanded real-like improvement:

| mode | nDCG@3 | AvgRel@3 | MRR |
|---|---:|---:|---:|
| `vertical_vector_rerank` | 0.875672 | 1.166667 | 1.000000 |
| `query_angle_router` | 0.876477 | 1.166667 | 1.000000 |

This keeps the router hypothesis alive, but it is not enough to claim a strong query-only router.

## Experiment loop

```text
sample / real-like / BEIR-derived data
  -> baseline sparse-vector ranking
  -> structure / vertical / diagonal reranking
  -> metric evaluation
  -> feedback report
  -> diagnostics
  -> result snapshots
  -> report update
```

The goal is not to claim production validity from the small real-like dataset. The goal is to create a closed loop that can say:

- whether structure or vertical reranking helped
- which angle mixtures helped
- which modes hurt
- which datasets disagree
- what to inspect next

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

# angle sweep
python -m structure_rerank.angle_sweep \
  --results results/vector_results.jsonl \
  --judgments examples/sample_judgments.jsonl

# query router, requires vector results and query rows
python -m structure_rerank.angle_router \
  --results results/vector_results.jsonl \
  --queries examples/sample_queries.jsonl \
  --output results/query_router_results.jsonl \
  --router query
```

## Current limitations

This lab does **not** yet prove:

- improvement over neural dense embeddings
- improvement on production data
- robust automatic structure extraction
- robust learned angle routing
- usefulness beyond the tested sparse TF-IDF setting

It currently supports a narrower claim:

```text
Given extracted structure labels and sparse TF-IDF vectors, vertical reranking is useful, diagonal mixtures can help, but angle choice is task-dependent.
```

## Next phase

Failure-case analysis only.

Do not add more ad hoc angle rules before doing this:

1. list selected angle per query
2. compare changed ranks against `vertical_vector_rerank`
3. classify helped / unchanged / hurt cases
4. then revise query router rules if evidence supports it

## Repository operation note

Heavy result-generation workflows should not run on every push. Use temporary experiment branches for future runs, record results, update docs, then archive workflows again before merging.
