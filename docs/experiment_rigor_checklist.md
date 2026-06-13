# Experiment Rigor Checklist

| Item | Status | Evidence |
|---|---|---|
| Detailed per-paper plan before expansion | Done | `docs/full_scale_execution_plan.md` |
| Baseline reproduction | Done | `python scripts/run_simulation.py` |
| Full-scale main benchmark | Done | `results/full_scale/main_shift_metrics.csv` |
| Multiple seeds | Done | Seed scale 20 across full-scale suites |
| Baselines | Done | CAQ, CAQ shrinkage, object-only, access-only, context table, monolithic logistic, interaction logistic, oracle-gate class mean, oracle intrinsic |
| Shifted test context | Done | Five train/test shifts |
| Access-gate stress | Done | Symmetric, false-access-only, false-blocked-only, and structured-margin modes |
| Correspondence stress | Done | Random class corruption and handle-slot swap |
| Support-burden study | Done | Training sizes 80 to 2560 and context bins 4/8/12 |
| Residual diagnostics | Done | Four classes, no-change controls, four change magnitudes |
| Geometry/clutter sensitivity | Done | Reach scale by clutter multiplier grid |
| Negative controls | Done | Approach-dependent non-conserved affordance violation |
| Calibration metrics | Done | ECE and calibration figures |
| Uncertainty/error bars | Done | SEM in CSV summaries and plotted confidence intervals |
| RAM-light execution | Done | Compact CSV rows; no raw trajectory dumps |
| Hardware validation | Missing | Outside local recoverability |
| Learned access gate | Missing | Measured as future-risk boundary, not solved |
| Automatic contact correspondence | Missing | Stress-tested as corruption, not solved |

## Rigor Decision

The final paper is a full-scale synthetic mechanism study with measured boundaries. It is substantially stronger than the v2 workshop artifact, but it remains conditional on known/accurate access and correspondence and does not claim real-robot deployment.
