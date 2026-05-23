# Feedback loop

This repository should not stop at running a metric script.

The experiment loop is:

```text
sample data
  -> baseline retrieval
  -> structure rerank
  -> evaluation metrics
  -> feedback report
  -> next actions
```

## Feedback outputs

The feedback step produces:

- overall judgment: `PASS`, `FAIL`, or `UNCERTAIN`
- metric deltas between baseline and structure rerank
- queries where structure rerank improved rank quality
- queries where structure rerank made rank quality worse
- concrete next actions

## Judgment rule

Initial rule:

- `PASS`: structure rerank improves nDCG@10 by at least 0.01 and AvgRel@10 does not decrease.
- `FAIL`: structure rerank decreases nDCG@10 by at least 0.01 or decreases AvgRel@10.
- `UNCERTAIN`: neither clear improvement nor clear degradation.

This rule is intentionally strict enough to prevent self-congratulation on tiny noisy changes.

## Use in CI

The CI should run:

```bash
python -m structure_rerank.feedback
```

The script writes:

```text
results/feedback.md
results/feedback.json
```

These files are CI artifacts. They do not need to be committed after every run.

## Local clone policy

This lab is designed so the experiment can be run by GitHub Actions and inspected from the repository. A local clone is optional, not required for the workflow.
