---
name: Idea, review, or reproducibility concern
about: Propose a concrete idea, counterexample, review comment, or reproducibility fix.
title: "[idea] "
labels: [idea, review]
assignees: ""
---

## Claim

State the claim in one or two sentences.

Example:

```text
The current query_angle_router fails on queries that look scientific but are actually argument retrieval tasks.
```

## Evidence or intuition

Explain why this might be true.

Include links, examples, or observed result rows if available.

## Smallest check

Describe the smallest experiment or inspection that would confirm or reject the claim.

Good checks are narrow.

Examples:

```text
Run the current router on 10 affected queries and list selected angle, top-3 results, and relevance labels.
```

```text
Compare diagonal_vertical_20 vs diagonal_vertical_35 only on queries containing explicit argument terms.
```

## Category

Select one:

- [ ] failure case or counterexample
- [ ] vertical / diagonal axis construction idea
- [ ] query/task angle routing idea
- [ ] reproducibility issue
- [ ] dataset suggestion
- [ ] interpretation too strong / too weak
- [ ] documentation issue
- [ ] other

## Expected impact

What would change if this issue is correct?

- [ ] changes the safe default
- [ ] changes a router rule
- [ ] adds a diagnostic report
- [ ] adds or fixes a dataset
- [ ] weakens a claim in the report
- [ ] strengthens a claim in the report
- [ ] only improves documentation

## Constraints

Note any constraints or risks.

Examples:

- dataset must be public and safe to include
- no secrets or private logs
- keep CI lightweight
- do not re-enable heavy workflows on every push

## Minimal acceptance condition

Define what would count as resolved.

Example:

```text
A diagnostic table is added showing selected angle per query and helped / unchanged / hurt classification.
```
