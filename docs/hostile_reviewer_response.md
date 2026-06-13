# Hostile Reviewer Response

## Likely Decision

For a synthetic mechanism venue or theory/mechanism track, the v3 paper is now a credible full-scale submission candidate. For a hardware-heavy robotics venue, reviewers may still require real-robot validation, learned/certified access estimation, and correspondence handling.

## Core Responses

| Reviewer Objection | Response in v3 |
|---|---|
| This is just reachability gating. | Access is the gate; CAQ estimates the conserved contact variable after quotienting the gate. Access-only is included and underperforms CAQ on medium-shift Brier/F1. |
| The access gate is assumed known. | Conceded and measured. The access taxonomy shows 20% symmetric gate error raises CAQ Brier from 0.0282 to 0.0726. |
| A larger policy could learn this. | Possibly; the paper is about label semantics, support burden, and auditable residuals. Logistic and interaction-logistic baselines are included. |
| Monolithic logistic is competitive. | Reported honestly. On medium shift, CAQ Brier is 0.0294, monolithic logistic 0.0313, interaction logistic 0.0323. |
| Synthetic evidence is weak. | The evidence is now broad synthetic evidence, not hardware. The final paper includes eight suites, 7040 compact rows, and negative controls. |
| Correspondence is unsolved. | Conceded and stress-tested via random class corruption and handle-slot swaps. |
| Conservation can be false. | Conceded and tested. In the negative control, CAQ Brier rises from 0.0284 to 0.0519 when conservation is deliberately violated. |
| Residuals are not guaranteed detectors. | Conceded. Residuals are framed as alarms; small changes are explicitly unreliable. |

## Claims We Should Not Make

- Do not claim real-robot deployment readiness.
- Do not claim learned access-gate robustness.
- Do not claim automatic contact correspondence.
- Do not claim all affordances are conserved under object/clutter interactions.
- Do not claim universal dominance over arbitrary learned policies.
