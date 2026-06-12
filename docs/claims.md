# Claims

## Main Claim
Observed mobile-manipulation success labels conflate a conserved contact affordance with a mutable base/clutter access gate. Estimating the conserved quotient improves cross-context generalization when object state is stable and access can be certified.

Status: supported by formal assumptions and planned synthetic evidence, not yet by real-robot experiments.

## Formal Claim
If observations satisfy `Y_i = A_g Z_i + epsilon_i`, where `A_g` is the latent contact affordance for contact class `g`, `Z_i` is a known binary access gate for the sampled base/clutter context, and `epsilon_i` is bounded zero-mean noise observed only when `Z_i=1`, then the quotient estimator `hat A_g = mean(Y_i/Z_i : Z_i=1, class=g)` is unbiased and has Hoeffding concentration using only accessible samples. A context-specific estimator over `K` base/clutter bins needs samples in each bin, yielding a `K`-factor support burden for the same contact class.

Status: proof sketch will be included. This is not a claim about arbitrary learned access models.

## Experimental Claim
In a 2D mobile-manipulation simulator with fixed object contacts, shifted base-pose distributions, and changed clutter, conserved quotient prediction should reduce Brier/log-loss and false blocked-contact predictions relative to object-only, access-only, context-table, and monolithic logistic baselines.

Status: supported in the synthetic simulator by `scripts/run_simulation.py`. Across 40 seeds, CAQ has the best Brier score (0.0276), log loss (0.1159), accuracy, and F1; monolithic logistic slightly has the best AUC.

## Access-Gate Stress Claim
CAQ is fragile to incorrect access certificates. Randomly flipping the access gate in training and shifted test contexts raises CAQ Brier from 0.0276 at 0% flips to 0.0721 at 20% flips and log loss from 0.1159 to 0.2540.

Status: supported by `results/access_noise_sweep.csv`; this is a limitation, not a positive deployment claim.

## Diagnostic Claim
Large conservation residuals after quotienting indicate either a wrong access certificate, wrong correspondence, or a true object/contact state change.

Status: conceptual and partially testable; should be framed as a diagnostic, not a guaranteed detector.

## Non-Claims
- No claim of superior large-scale robot foundation modeling.
- No claim of solving generic task-and-motion planning.
- No claim of real-world deployment or hardware robustness.
- No claim of robustness to noisy or learned access gates.
- No claim that every affordance is conserved under all clutter changes.
