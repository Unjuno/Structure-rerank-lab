# Workflow archive policy

This repository separates lightweight checks from experiment refresh jobs.

## Rule

- Lightweight validation may run on every push.
- Heavy experiment workflows must not run on every push.
- Once an experiment result is recorded under `results/`, the workflow should be archived or converted to manual dispatch only.

## Current archived experiment families

- expanded real-like experiments
- BEIR benchmark refresh jobs
- BEIR summary refresh jobs
- BEIR vertical rank movement jobs
- angle sweep jobs

## Refresh procedure

1. Create a temporary branch.
2. Re-enable only the one experiment workflow that is needed.
3. Run it intentionally.
4. Commit the generated `results/` files.
5. Update `docs/current-state.md`.
6. Archive the workflow again before merging.

## Reason

Keeping result-generation workflows active on every push creates runner queues and makes it hard to tell whether a code change failed or a queued experiment has simply not started.
