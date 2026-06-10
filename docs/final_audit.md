# Final Audit

1. **Chosen thesis**
   - Mobile-manipulation success labels should be factored into a conserved contact-frame affordance and a mutable base/clutter access gate. The paper calls this representation a Conserved Affordance Quotient (CAQ).

2. **Field assumption broken**
   - The broken assumption is that a failed or successful affordance observation is a direct object/part label. In mobile manipulation, the label may be censored by base pose, approach direction, reachability, and clutter obstruction.

3. **New central mechanism**
   - CAQ estimates the object-side contact-class affordance only from accessible observations and separately recomputes a geometric access gate for each base/clutter context. The central object is the quotient, not a larger predictor or a planner wrapper.

4. **Genuine novelty**
   - Affordance learning, base placement, reachability maps, clutter rearrangement, and value-map composition are all well covered by prior work. The novelty is the explicit conservation-aware factorization of the observed mobile-manipulation label and its use for estimation, context transport, and residual diagnostics.

5. **Closest hostile prior work**
   - The closest hostile areas are generalized affordance templates for mobile manipulation, mobile-manipulator base placement/reachability methods, grasp/contact affordance localization, and clutter-aware task-and-motion planning. Representative hostile records include `Generalized Affordance Templates for Mobile Manipulation`, `Optimal Base Placement and Motion Planning for Mobile Manipulators`, `Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation`, and `Tree Search-based Task and Motion Planning with Prehensile and Non-prehensile Manipulation for Obstacle Rearrangement in Clutter`.

6. **Literature coverage**
   - `docs/related_work_matrix.csv` contains 1100 deduplicated OpenAlex records from 30 robotics/mobile-manipulation/affordance queries.
   - Top 300 records were used as the serious skim tier.
   - Top 250 records were used as the deep-read tier at abstract/metadata level.
   - Top 100 records form `docs/hostile_prior_work.md`.
   - Coverage is broad but not full-text-complete; this limitation is recorded in the manuscript and reviewer attacks.

7. **Proof/formal-claim status**
   - The paper includes a proved Hoeffding-style concentration proposition for the quotient estimator under explicit assumptions: known binary access gate, stable contact correspondence, independent bounded accessible observations, and stable object/contact state.
   - The theorem does not cover learned access gates, noisy correspondence, adversarial shifts, or real robot execution.

8. **Strongest evidence**
   - `scripts/run_simulation.py` runs a 40-seed 2D mobile-manipulation simulation with shifted base poses and heavier test clutter.
   - CAQ has the best Brier score, log loss, accuracy, and F1 among the tested methods.
   - Monolithic logistic slightly has the best AUC, which is honestly reported.
   - Controlled object-change residuals flag the changed handle class in 100% of seeds.

9. **Biggest weaknesses**
   - Evidence is synthetic and 2D.
   - Access is known from geometry rather than learned from raw perception.
   - Contact correspondence and contact-class labels are assumed.
   - No hardware validation.
   - The formal result is intentionally simple and conditional.

10. **Paper-readiness judgment**
    - **Workshop / revise.** The mechanism and audit are coherent, the paper is runnable, and the result is honest. It is not ready as a main-conference submission without stronger 3D or real-robot evidence and a learned or certified access module in realistic scenes.

11. **Exact Downloads PDF path**
    - `C:/Users/wangz/Downloads/04.pdf`

12. **GitHub URL**
    - `https://github.com/Jason-Wang313/04_affordance_conservation_for_mobile_manipulators`

13. **Visible Desktop PDF copy status**
    - `pending orchestrator copy`
    - At audit time, `C:\Users\wangz\OneDrive\Desktop\04.pdf` was not present.
