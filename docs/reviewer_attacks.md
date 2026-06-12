# Reviewer Attacks

## Likely Attacks and Required Answers
1. Attack: This is just reachability gating.
   Response: No: reachability is the mutable gate; the paper's object is the quotient estimator for the conserved contact variable. The experiment must include access-only and reachability-only baselines.
2. Attack: Affordance templates already did this.
   Response: Templates encode action-relevant geometry, but the novelty boundary is explicit separation of observed success into conserved contact affordance and mutable base/clutter access, with a concentration claim.
3. Attack: Task-and-motion planning already checks feasibility.
   Response: TAMP checks feasibility for fixed predicates. The proposed mechanism changes the predicate semantics by treating negative labels under inaccessible contexts as censored, not false.
4. Attack: A larger policy could learn this implicitly.
   Response: Possibly, but the paper's claim is about identifiability and sample support. The central mechanism is explicit quotient projection and auditable residuals.
5. Attack: The access gate is assumed known.
   Response: Correct. This is a limitation and a deliberate scope choice. Submission-hardening v2 adds an access-noise stress test: CAQ Brier rises from 0.0276 at 0% gate flips to 0.0721 at 20% flips.
6. Attack: Synthetic evidence is too weak.
   Response: Yes for submission strength. The final audit should likely recommend workshop/revise unless the simulation results are unusually compelling.
7. Attack: Conservation is trivial if the object does not change.
   Response: The nontrivial part is that the observed success label does change under base/clutter shifts; only the quotient is conserved.
8. Attack: Correspondence across contacts is unsolved.
   Response: Correct. The current paper assumes contact correspondence or class labels. This must be explicit in theorem and limitations.
9. Attack: Clutter can change the object state.
   Response: Then conservation should fail and residuals should rise. The claim is conditional on stable object/contact state.
10. Attack: The monolithic logistic baseline is weak.
   Response: The evidence should include both context table and monolithic learned predictor, and report exactly what features each receives.
11. Attack: The theorem is just a mean estimator.
   Response: The simplicity is intentional: it isolates the variable change. The paper should not oversell mathematical depth.
12. Attack: The 1000-paper sweep is API-level, not full-text.
   Response: Correct. The audit should state literature coverage as metadata/abstract-level with hostile top-set extraction.
13. Attack: If the access gate is learned, quotienting can amplify perception errors.
   Response: Correct. The current paper should not claim learned-gate robustness. The access-noise sweep is the negative evidence and should be cited directly.

## Hostile Prior Work Most Likely To Be Cited By Reviewers
| Rank | Title | Year | Cluster | Less novel | Leaves open |
|---:|---|---:|---|---|---|
| 1 | Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation | 2016.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 2 | Visual Grasp Affordance Localization in Point Clouds Using Curved Contact Patches | 2016.0 | grasp/contact manipulation | broad robotics motivation and related empirical settings | task-level conservation beyond local grasp/contact scores |
| 3 | Optimal Base Placement and Motion Planning for Mobile Manipulators | 2012.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 4 | AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter | 2025.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 5 | Implicit contact-rich manipulation planning for a manipulator with insufficient payload | 2023.0 | grasp/contact manipulation | broad robotics motivation and related empirical settings | task-level conservation beyond local grasp/contact scores |
| 6 | RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation | 2025.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 7 | Real-Time Collision-Free Motion Planning and Control for Mobile Manipulation with Quadrupeds | 2023.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 8 | Enabling Failure Recovery for On-The-Move Mobile Manipulation | 2023.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 9 | Model-Free Large-Scale Cloth Spreading With Mobile Manipulation: Initial Feasibility Study | 2023.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 10 | DORA: Object Affordance-Guided Reinforcement Learning for Dexterous Robotic Manipulation | 2025.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 11 | Probabilistic Spatio-Temporal Fusion of Affordances for Grasping and Manipulation | 2022.0 | grasp/contact manipulation | broad robotics motivation and related empirical settings | task-level conservation beyond local grasp/contact scores |
| 12 | Information-driven Affordance Discovery for Efficient Robotic Manipulation | 2024.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 13 | Generalized Affordance Templates for Mobile Manipulation | 2022.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 14 | Tree Search-based Task and Motion Planning with Prehensile and Non-prehensile Manipulation for Obstacle Rea... | 2021.0 | clutter and rearrangement manipulation | planning around or rearranging clutter to access targets | formal separation between changed access and changed object action semantics |
| 15 | Harmonious Sampling for Mobile Manipulation Planning | 2019.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
