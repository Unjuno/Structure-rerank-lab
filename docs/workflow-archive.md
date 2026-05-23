# Workflow archive policy

This repository separates lightweight checks from experiment refresh jobs.

## Rule

- Lightweight validation may run on every push.
- Heavy experiment workflows should not run on every push.
- Once an experiment result is recorded under `results/`, the workflow should be archived or converted to manual dispatch only.

## Current archived experiment families

- expanded real-like experiments
- BEIR benchmark refresh jobs
- BEIR summary refresh jobs
- BEIR vertical rank movement jobs
- angle sweep jobs

## Refresh procedure

1. Create a temporary experiment branch.
2. Re-enable only the workflow needed for that experiment.
3. Run it intentionally.
4. Commit generated `results/` files.
5. Update `docs/current-state.md`.
6. Archive the workflow again before merging.

## Reason

Keeping result-generation workflows active on every push creates runner queues and makes it hard to distinguish code failure from queued experiments.
