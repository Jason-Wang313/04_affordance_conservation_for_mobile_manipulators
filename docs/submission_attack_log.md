# Submission Attack Log

Paper: 04_affordance_conservation_for_mobile_manipulators

Hardening version: v3 full-scale final

Date: 2026-06-13 23:25:00 +01:00

## Attack Rounds

| Round | Attack | Action | Residual Risk |
|---:|---|---|---|
| 1 | This is just reachability gating. | Added explicit quotient-vs-gate formalism and retained access-only baseline. | Moderate; decomposition may still look simple. |
| 2 | Known access gate is unrealistic. | Added access taxonomy with symmetric, false-access, false-blocked, and structured-margin errors. | High for real robots; measured rather than solved. |
| 3 | CAQ may amplify perception errors. | Reported large degradation: 20% symmetric gate error raises Brier 0.0282 to 0.0726. | High without certified/learned gate calibration. |
| 4 | Synthetic 2D evidence is too weak. | Expanded to eight-suite full-scale synthetic study and 28-page manuscript. | Hardware evidence still missing. |
| 5 | Monolithic logistic is competitive. | Added monolithic and interaction logistic baselines with Newton solver; reported wins/losses honestly. | Moderate; larger learned models remain future work. |
| 6 | Conservation is trivial if object state is fixed. | Added support-burden study, residual diagnostics, and negative controls. | Low for the mechanism claim. |
| 7 | Contact correspondence is assumed. | Added random class corruption and handle-slot swap stress tests. | High for real perception; assumption remains. |
| 8 | Object/contact state can change under clutter. | Added residual magnitude sweeps and conservation-violation negative control. | Residuals remain alarms, not proofs. |
| 9 | The theorem is just Hoeffding for means. | Added gate-bias proposition and empirical support-burden suite. | Theoretical depth remains intentionally modest. |
| 10 | Literature sweep is metadata-level. | Kept novelty boundary and limitation explicit. | Moderate; full-text literature review would improve venue confidence. |
| 11 | Metrics could be misleading under rare positives. | Added calibration, access-rate/positive-rate schema, and geometry/clutter sensitivity discussion. | Low. |
| 12 | Short paper was not final. | Rewrote as 28-page final manuscript with real new experiments and appendices. | Resolved under batch standard. |

## Stop Condition

Stopped after the full-scale v3 pass because recoverable synthetic-evidence weaknesses were addressed and the remaining weaknesses require external hardware/perception work, not more local simulation.
