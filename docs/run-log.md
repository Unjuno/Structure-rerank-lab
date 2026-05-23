# Run log

This file records repository-level experiment workflow changes.

## 2026-05-24

- README was updated to reflect the current lexical + TF-IDF vector experiment loop.
- CI was changed to commit generated `results/` snapshots back to the repository on push.
- Diagnostics were updated to split structure-type degradation into intent-matched and off-intent cases.
- Experiment summary was updated to report those categories separately.

Next expected generated snapshot:

- `results/experiment_summary.md` should show both lexical and vector top-3 deltas.
- `results/diagnostics.md` should show `Harmful intent-matched modes` separately from `Harmful off-intent modes`.
