# Claims

## Main Claim
Observed mobile-manipulation success labels conflate a conserved contact affordance with a mutable base/clutter access gate. Estimating the conserved quotient improves cross-context generalization when object state is stable and access can be certified.

Status: supported by formal assumptions and planned synthetic evidence, not yet by real-robot experiments.

## Formal Claim
If observations satisfy `Y_i = A_g Z_i + epsilon_i`, where `A_g` is the latent contact affordance for contact class `g`, `Z_i` is a known binary access gate for the sampled base/clutter context, and `epsilon_i` is bounded zero-mean noise observed only when `Z_i=1`, then the quotient estimator `hat A_g = mean(Y_i/Z_i : Z_i=1, class=g)` is unbiased and has Hoeffding concentration using only accessible samples. A context-specific estimator over `K` base/clutter bins needs samples in each bin, yielding a `K`-factor support burden for the same contact class.

Status: proof sketch will be included. This is not a claim about arbitrary learned access models.

## Experimental Claim
In a 2D mobile-manipulation simulator with fixed object contacts, shifted base-pose distributions, and changed clutter, conserved quotient prediction should reduce Brier/log-loss and false blocked-contact predictions relative to object-only, access-only, context-table, and monolithic logistic baselines.

Status: to be tested by `scripts/run_simulation.py`.

## Diagnostic Claim
Large conservation residuals after quotienting indicate either a wrong access certificate, wrong correspondence, or a true object/contact state change.

Status: conceptual and partially testable; should be framed as a diagnostic, not a guaranteed detector.

## Non-Claims
- No claim of superior large-scale robot foundation modeling.
- No claim of solving generic task-and-motion planning.
- No claim of real-world deployment or hardware robustness.
- No claim that every affordance is conserved under all clutter changes.
