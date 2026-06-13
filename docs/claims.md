# Claims

## Main Claim

Observed mobile-manipulation success labels conflate a conserved contact affordance with a mutable base/clutter access gate. Estimating the conserved quotient improves cross-context calibration when object/contact state is stable, contact correspondence is available, and access can be certified or estimated accurately.

Status: supported by formal assumptions and the full-scale synthetic evidence suite. Not supported as a raw-perception or real-robot deployment claim.

## Formal Claim

Under a known binary access gate and stable contact classes, the accessible quotient estimator has Hoeffding concentration using accessible samples per class. A context-specific estimator over `K` base/clutter bins requires support in many contact-by-context cells, yielding a larger support burden.

Status: proved in the manuscript as an explicit conditional support-burden statement.

## Full-Scale Experimental Claim

In the 20-seed expanded simulator, CAQ nearly matches the oracle intrinsic predictor on the medium base/clutter shift and improves calibration-sensitive metrics over object-only, access-only, context-table, monolithic logistic, and interaction-logistic baselines.

Evidence:

- `results/full_scale/main_shift_metrics.csv`
- `results/full_scale/leaderboard.csv`
- Medium-shift CAQ Brier: 0.0294
- Medium-shift oracle intrinsic Brier: 0.0293
- Medium-shift context-table Brier: 0.1009

## Access-Gate Stress Claim

CAQ is fragile to incorrect access certificates. In the access taxonomy, correct-gate CAQ Brier is 0.0282; 20% symmetric gate error raises Brier to 0.0726, false-access-only 20% error raises it to 0.0699, false-blocked-only 20% error raises it to 0.0362, and structured-margin 20% error raises it to 0.0799.

Status: supported by `results/full_scale/access_error_taxonomy.csv`.

## Support-Burden Claim

CAQ remains stable at low training support because it estimates accessible class-level means, while context tables remain brittle under shifted context support.

Evidence: at 160 training samples and 8 context bins, CAQ Brier is 0.0285 versus context table 0.0967.

## Diagnostic Claim

Large conservation residuals can act as alarms for access error, correspondence error, execution shift, or object/contact state change. They are not guaranteed detectors.

Evidence: residual detection improves with object-change magnitude but is weak for small changes, especially 0.10 handle drops.

## Negative-Control Claim

When contact affordance is deliberately made approach-dependent, the conserved quotient fails as expected.

Evidence: CAQ Brier rises from 0.0284 at zero violation to 0.0519 at full violation; interaction logistic reaches 0.0343 at full violation.

## Non-Claims

- No claim of real-robot deployment readiness.
- No claim of learned access-gate robustness.
- No claim of automatic contact correspondence.
- No claim that all affordances are conserved.
- No claim of dominance over arbitrary large robot policies.
