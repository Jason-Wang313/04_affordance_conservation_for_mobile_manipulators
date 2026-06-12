# Submission Attack Log

Paper: 04_affordance_conservation_for_mobile_manipulators

Hardening version: v2
Date: 2026-06-12 20:12:00 +01:00

## Attack Rounds

| Round | Attack | Action | Residual Risk |
|---:|---|---|---|
| 1 | This is just reachability gating. | Reaffirmed quotient-vs-gate distinction and retained access-only baseline. | Moderate; reviewers may still see it as decomposition. |
| 2 | The known access gate is unrealistic. | Added access-gate noise stress test. | High; real gate learning is unsolved. |
| 3 | CAQ may amplify perception errors. | Reported Brier/log-loss degradation under access flips. | High; no learned perception module. |
| 4 | Synthetic 2D evidence is too weak. | Marked workshop-only. | Non-recoverable locally. |
| 5 | Monolithic logistic is competitive. | Kept AUC win for logistic and reported it honestly. | Moderate. |
| 6 | Conservation is trivial if object state is fixed. | Emphasized that observed labels change under access shifts while quotient stays conserved. | Moderate. |
| 7 | Contact correspondence is assumed. | Kept as limitation and checklist item. | High. |
| 8 | Object/contact state can change under clutter. | Retained residual diagnostic and non-conservation caveat. | Residual is not guaranteed detector. |
| 9 | The theorem is just Hoeffding for means. | Kept theorem as support-burden statement, not mathematical depth. | Low for workshop, high for main conference. |
| 10 | Literature sweep is metadata-level. | Kept limitation. | Moderate. |
| 11 | Reproducibility did not list new stress output. | Updated README and reproducibility docs. | Low. |
| 12 | Main-conference readiness is overstated. | Final decision set to workshop-only / strong-revise. | None for current terminal decision. |

## Stop Condition

Stopped before 50 rounds because recoverable issues converged on the known-gate boundary. The access-noise stress test, documentation, manuscript limitation, and terminal readiness decision were completed.
