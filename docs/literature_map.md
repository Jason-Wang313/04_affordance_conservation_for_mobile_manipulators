# Literature Map

## Sweep Protocol
- Landscape sweep: 1100 OpenAlex records from 30 robotics/mobile-manipulation/affordance queries.
- Serious skim: top 300 ranked records, using titles, venues, abstracts when available, concepts, and query provenance.
- Deep read set: top 250 ranked records, still at abstract/metadata level unless the record itself exposed more detail.
- Hostile prior-work set: top 100 records most likely to make the seed idea less novel.
- Ranking is not a citation-impact ranking; it is tuned for mobile manipulation, affordance, reachability, base pose, clutter, invariance, and action-model terms.

## Field Box
The selected field box is mobile manipulation under changing base pose and clutter, with affordance learning/planning as the interface between object-centered action semantics and whole-body access. The box includes learned object/part affordance predictors, reachability maps, whole-body mobile manipulation planning, task-and-motion planning, clutter rearrangement, equivariant manipulation representations, and recent language/foundation-model manipulation systems.

## Cluster Counts
| Cluster | Count in 1100 | Top hostile examples |
|---|---:|---|
| mobile manipulation and base placement | 410 | Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation; Optimal Base Placement and Motion Planning for Mobile Manipulators; Real-Time Collision-Free Motion Planning and Control for Mobile Manipulation with Quadrupeds |
| grasp/contact manipulation | 234 | Visual Grasp Affordance Localization in Point Clouds Using Curved Contact Patches; Implicit contact-rich manipulation planning for a manipulator with insufficient payload; Probabilistic Spatio-Temporal Fusion of Affordances for Grasping and Manipulation |
| robot affordance learning | 178 | AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter; RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation; DORA: Object Affordance-Guided Reinforcement Learning for Dexte... |
| task and motion planning | 89 | Task and motion planning for mobile manipulators; A Hierarchical Motion Planning Method for Mobile Manipulator; Fast and resilient manipulation planning for target retrieval in clutter |
| robot foundation/vision-language manipulation | 75 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks; Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Mode... |
| clutter and rearrangement manipulation | 49 | Tree Search-based Task and Motion Planning with Prehensile and Non-prehensile Manipulation for Obstacle Rearrangement in Clutter; Review of Learning-Based Robotic Manipulation in Cluttered Environments; Efficient Obstacle Rearrangement for Object Manipulati... |
| embodied AI/action models | 31 | A Survey of Embodied Learning for Object-centric Robotic Manipulation; Robot Manipulation Based on Embodied Visual Perception: A Survey; From Nano Robotic Manipulation to Nano Manipulation Robot |
| invariance/equivariance/transport | 19 | USEEK: Unsupervised SE(3)-Equivariant 3D Keypoints for Generalizable Manipulation; RiEMann: Near Real-Time SE(3)-Equivariant Robot Manipulation without Point Cloud Segmentation; Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipula... |
| reachability and workspace models | 15 | Optimal Order Pick-and-Place of Objects in Cluttered Scene by a Mobile Manipulator; A Shared Autonomous Nursing Robot Assistant with Dynamic Workspace for Versatile Mobile Manipulation; Reuleaux: Robot Base Placement by Reachability Analysis |

## Year Distribution
- pre-2000: 11
- 2000-2009: 41
- 2010-2015: 145
- 2016-2020: 325
- 2021-2026: 577

## What the Sweep Says
1. Affordance papers often learn a map from perception to action possibilities, but the binary labels are usually entangled with whether the robot could approach the part from the sampled base pose.
2. Mobile-manipulation and base-placement papers model access well, but usually take the affordance predicate or target contact as already specified.
3. Reachability maps and inverse-reachability models explain kinematic access but do not preserve a separate object-side affordance variable.
4. Clutter and rearrangement work shows the access variable is physically important, yet often treats the object affordance as fixed background knowledge.
5. Invariance/equivariance work gives useful transport machinery, but most label-preserving groups are rigid geometric groups; the mobile-manipulation problem needs a quotient where the full success label is not conserved, only one factor is.
6. Vision-language and robot foundation models make dense action values convenient, but do not by themselves distinguish a changed object affordance from a temporarily inaccessible one.

## Top Hostile Papers Snapshot
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
| 16 | The UMass Mobile Manipulator UMan: An Experimental Platform for Autonomous Mobile Manipulation | 2006.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 17 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | 2023.0 | robot foundation/vision-language manipulation | using broad pretrained representations for robot actions | a mechanism-level account of conserved affordance under mobile manipulation context shift |
| 18 | Unsupervised learning of object affordances for planning in a mobile manipulation platform | 2011.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 19 | Combined Path and Motion Planning for Workspace Restricted Mobile Manipulators in Planetary Exploration | 2023.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 20 | Affordance based Part Recognition for Grasping and Manipulation | 2011.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 21 | A Versatile Affordance Modeling Framework Using Screw Primitives to Increase Autonomy During Manipulation C... | 2022.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 22 | Pose optimization for mobile manipulator grasping based on hybrid manipulability | 2023.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 23 | Manipulation-Oriented Object Perception in Clutter through Affordance Coordinate Frames | 2022.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 24 | Towards affordance detection for robot manipulation using affordance for parts and parts for affordance | 2018.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 25 | A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation | 2023.0 | grasp/contact manipulation | broad robotics motivation and related empirical settings | task-level conservation beyond local grasp/contact scores |
| 26 | Affordance-Based Multi-Contact Whole-Body Pose Sequence Planning for Humanoid Robots in Unknown Environments | 2018.0 | grasp/contact manipulation | broad robotics motivation and related empirical settings | task-level conservation beyond local grasp/contact scores |
| 27 | Extraction of Whole-Body Affordances for Loco-Manipulation Tasks | 2015.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 28 | The Affordance Template ROS package for robot task programming | 2015.0 | robot affordance learning | generic affordance prediction from perception | whether a failed affordance observation is intrinsic or only base/clutter-censored |
| 29 | Development of Human Support Robot as the research platform of a domestic mobile manipulator | 2019.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |
| 30 | Elastic Roadmaps: Globally Task-Consistent Motion for Autonomous Mobile Manipulation in Dynamic Environments | 2006.0 | mobile manipulation and base placement | base-pose selection and whole-body feasibility reasoning | how object affordances should be conserved while access changes |

## Hidden Assumptions That May Be False
1. Affordance is an object- or part-level property rather than a context-censored observation.
2. Changing the mobile base pose changes access, not the latent affordance itself.
3. Clutter can be represented as generic observation noise or an obstacle field without changing the affordance variable.
4. A failed attempt is negative evidence about the object rather than evidence that access was blocked.
5. Reachability is a sufficient proxy for manipulation success.
6. Graspability and task affordance are interchangeable.
7. The robot's base pose distribution in training covers deployment.
8. Action primitives have a fixed frame independent of base and scene layout.
9. The correspondence between contacts across context changes is known or trivial.
10. Scene graphs preserve enough geometry to decide swept-volume access.
11. Occlusion, collision, and semantic non-affordance can be learned from the same binary label.
12. A planner may query affordances as static predicates without corrupting their meaning.
13. Object state is unchanged by prior navigation, contact, or clutter motions.
14. Clutter perturbations are independent and identically distributed.
15. Manipulation failures are independent across base poses once the object is fixed.
16. The manipulator morphology is fixed and does not enter the affordance definition.
17. A learned affordance map can be recomputed cheaply for each base pose.
18. The relevant invariance group is a rigid scene transform rather than a quotient over access variables.
19. Language-conditioned affordances inherit physical validity from visual grounding.
20. Negative labels are uncensored, even when the robot could not physically try the action.
21. Benchmark train/test splits contain the base-clutter shifts that matter in homes, labs, and warehouses.
22. Base placement is a downstream planning problem after affordance prediction.
23. Dense value maps are semantically calibrated across unreachable and reachable regions.
24. Conservation failures indicate model error, not possible object or clutter state change.
25. Arm-base coupling can be separated from contact semantics without an explicit interface.

## Directions That Break Those Assumptions

### Conserved Affordance Quotients
- Broken assumption: binary success labels directly measure object affordance.
- Central mechanism: divide observed success into a conserved contact-frame affordance and a mutable access term, then project labels onto equivalence classes across base/clutter orbits.
- Why it is not a weak move: changes the target variable and estimator rather than adding a verifier, uncertainty head, or bigger predictor.
- Evidence path: sample-complexity claim plus mobile-manipulation simulation with controlled base/clutter shifts.
- Score: 9.6/10.

### Censored Negative Affordance Learning
- Broken assumption: failed action attempts are true negative labels.
- Central mechanism: treat unreachable trials as censored observations in a survival-style affordance estimator.
- Why it is not a weak move: new label semantics, but less directly distinct from positive-unlabeled and missing-data literature.
- Evidence path: compare censored and uncensored estimators under unreachable contexts.
- Score: 8.2/10.

### Clutter Topology Affordance Gates
- Broken assumption: clutter density is the relevant variable.
- Central mechanism: use swept-volume homotopy classes rather than object counts to gate contact access.
- Why it is not a weak move: a genuine physical abstraction, but narrower and closer to motion planning.
- Evidence path: show identical density with different access topology.
- Score: 7.8/10.

### Morphology-Relative Affordance Gauges
- Broken assumption: affordances transfer between embodiments without changing coordinates.
- Central mechanism: represent affordance in a robot-specific quotient space induced by reachable contact screws.
- Why it is not a weak move: mechanistic but broad enough to become a survey unless scoped tightly.
- Evidence path: compare arm lengths and bases in simulation.
- Score: 7.5/10.

### Affordance Residuals for Object-State Change
- Broken assumption: conservation violations are model error.
- Central mechanism: use repeated quotient residuals to detect when an object part or articulation changed state.
- Why it is not a weak move: useful diagnostic, but closest to change detection unless paired with quotient estimator.
- Evidence path: detect handle removal/articulation lock from residuals.
- Score: 7.3/10.


## Strongest Direction
The strongest direction is **Conserved Affordance Quotients**. It has a sharper mechanism-level distinction than a new benchmark, active learner, verifier, or larger policy: the paper changes what is estimated. The observed mobile-manipulation success label is treated as a product or gate of (i) a conserved contact-frame affordance and (ii) a mutable base/clutter access field. The research question becomes when and how the first term can be transported across context changes while the second term is recomputed geometrically.
