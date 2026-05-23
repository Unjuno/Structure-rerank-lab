# Experiment summary

Status: **pending CI artifact refresh**

This file is the repository-visible summary target for the full experiment loop.

The CI generates:

```bash
python -m structure_rerank.experiment_summary
```

## What it summarizes

- lexical baseline vs structure rerank
- TF-IDF vector baseline vs vector + structure rerank
- top-3 deltas
- harmful modes from diagnostics
- blockers
- next actions

## Current expected decision rule

- If lexical and vector structure rerank both improve nDCG@3, the sample experiment can move to a real-like exported dataset.
- If vector structure rerank fails, fix weighting or query-intent gating before adding more data.
- If harmful modes remain, inspect their rank movements before increasing their weight.

## Next action

Inspect the latest CI artifact, then replace this placeholder with generated values if needed.
