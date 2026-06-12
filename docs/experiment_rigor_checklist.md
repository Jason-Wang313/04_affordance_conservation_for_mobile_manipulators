# Experiment Rigor Checklist

| Item | Status | Evidence |
|---|---|---|
| Multiple seeds | Done | 40 simulation seeds. |
| Baselines | Done | Object-only, access-only, context table, monolithic logistic. |
| Shifted test context | Done | Base-pose shift and heavier clutter. |
| Residual diagnostic | Done | Changed handle class detected in 100% of seeds. |
| Access-gate stress | Done | `results/access_noise_sweep.csv`. |
| Uncertainty/error bars | Done | Figure uses 95% confidence intervals; summary CSV has SEM. |
| Hardware validation | Missing | Non-recoverable locally. |
| Learned access gate | Missing | Non-recoverable locally. |
| Contact correspondence discovery | Missing | Non-recoverable locally. |
| Claims narrowed to evidence | Done | Paper, claims, reviewer response, and final audit updated. |

## Rigor Decision

Adequate for a workshop mechanism paper under known access gates. Not adequate for a main robotics or ICLR submission.
