# Reviewer Attacks

## Likely Attacks and Required Answers

1. Attack: This is just reachability gating.
   Response: Reachability supplies the mutable gate; CAQ estimates the conserved contact variable after quotienting that gate. Access-only is a baseline and does not match CAQ on medium-shift Brier/F1.

2. Attack: Affordance templates already did this.
   Response: Templates encode action-relevant geometry, but CAQ's novelty is the explicit separation of observed mobile-manipulation labels into conserved contact affordance and mutable access, plus support-burden and failure-mode analysis.

3. Attack: Task-and-motion planning already checks feasibility.
   Response: TAMP checks feasibility for fixed predicates. CAQ changes how the predicates are estimated from censored labels.

4. Attack: A larger policy could learn this implicitly.
   Response: Possibly, but the paper targets label semantics and auditability. The full-scale suite includes monolithic and interaction logistic baselines.

5. Attack: The access gate is assumed known.
   Response: Correct. v3 measures the failure: 20% symmetric gate error raises CAQ Brier from 0.0282 to 0.0726; structured-margin errors are worse.

6. Attack: Synthetic evidence is too weak.
   Response: The final version is a full-scale synthetic mechanism paper with eight suites and 7040 compact rows. It still does not claim hardware deployment.

7. Attack: Conservation is trivial if the object does not change.
   Response: Observed labels change under access shifts; only the quotient is conserved. The support-burden and negative-control suites test this distinction.

8. Attack: Correspondence across contacts is unsolved.
   Response: Correct. The full-scale suite stress-tests correspondence corruption but does not solve perception.

9. Attack: Clutter can change the object state.
   Response: Correct. Then conservation should fail. The residual and negative-control suites are included for this reason.

10. Attack: The monolithic logistic baseline is weak.
    Response: v3 uses a ridge-regularized Newton solver and includes an interaction logistic baseline. Larger learned policies remain future work.

11. Attack: The theorem is just a mean estimator.
    Response: The theorem is intentionally a support-burden statement. It is paired with empirical support sweeps and a gate-bias proposition.

12. Attack: The literature sweep is API-level, not full text.
    Response: Correct. The novelty audit is metadata/abstract-level and is described as such.

13. Attack: If access is learned, quotienting can amplify perception errors.
    Response: Correct. This is the central measured limitation in the access taxonomy.

## Hostile Prior Work Most Likely To Be Cited

The closest hostile areas remain affordance templates for mobile manipulation, reachability/base-placement methods, contact affordance localization, clutter-aware task-and-motion planning, spatial action maps, and language-conditioned manipulation value maps.
