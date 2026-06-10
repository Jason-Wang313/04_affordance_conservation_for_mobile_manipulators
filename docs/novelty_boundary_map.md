# Novelty Boundary Map

## Boundary Claim
The paper is not novel if it is only an affordance predictor, a reachability map, a base-placement planner, a clutter rearrangement planner, a language-conditioned value map, or an equivariant representation. It is only novel if the central object is a quotient representation that explicitly separates the conserved object/contact term from the mutable base/clutter access term and uses that separation for estimation, prediction, and diagnosis.

## Not Novel by Cluster

### mobile manipulation and base placement
- Representative hostile records: Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation; Optimal Base Placement and Motion Planning for Mobile Manipulators; Real-Time Collision-Free Motion Planning and Control for Mobile Manipulation with Quadrupeds; Enabling Failure Recovery for On-The-Move Mobile Manipulation; Model-Free Large-Scale Cloth Spreading With Mo...
- Makes less novel: base-pose selection and whole-body feasibility reasoning.
- Leaves open: how object affordances should be conserved while access changes.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### grasp/contact manipulation
- Representative hostile records: Visual Grasp Affordance Localization in Point Clouds Using Curved Contact Patches; Implicit contact-rich manipulation planning for a manipulator with insufficient payload; Probabilistic Spatio-Temporal Fusion of Affordances for Grasping and Manipulation; A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation; Affordance-Based Multi-Co...
- Makes less novel: broad robotics motivation and related empirical settings.
- Leaves open: task-level conservation beyond local grasp/contact scores.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### robot affordance learning
- Representative hostile records: AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter; RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation; DORA: Object Affordance-Guided Reinforcement Learning for Dexterous Robotic Manipulation; Information-driven Affordance Discovery for Efficient Robotic Manipulatio...
- Makes less novel: generic affordance prediction from perception.
- Leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### clutter and rearrangement manipulation
- Representative hostile records: Tree Search-based Task and Motion Planning with Prehensile and Non-prehensile Manipulation for Obstacle Rearrangement in Clutter; Review of Learning-Based Robotic Manipulation in Cluttered Environments; Efficient Obstacle Rearrangement for Object Manipulation Tasks in Cluttered Environments; Position‐aware pushing and grasping synergy with deep reinforcem...
- Makes less novel: planning around or rearranging clutter to access targets.
- Leaves open: formal separation between changed access and changed object action semantics.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### robot foundation/vision-language manipulation
- Representative hostile records: VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models; Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks; Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics; Empowering Large Language Models on Robotic Manipulation with Affordance Prompting;...
- Makes less novel: using broad pretrained representations for robot actions.
- Leaves open: a mechanism-level account of conserved affordance under mobile manipulation context shift.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### reachability and workspace models
- Representative hostile records: Optimal Order Pick-and-Place of Objects in Cluttered Scene by a Mobile Manipulator; A Shared Autonomous Nursing Robot Assistant with Dynamic Workspace for Versatile Mobile Manipulation; Reuleaux: Robot Base Placement by Reachability Analysis; Predictive Reachability for Embodiment Selection in Mobile Manipulation Behaviors; Linear manipulator: Motion cont...
- Makes less novel: using reachability as a manipulation feasibility signal.
- Leaves open: how to quotient reachability out of affordance labels instead of replacing them.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### task and motion planning
- Representative hostile records: Task and motion planning for mobile manipulators; A Hierarchical Motion Planning Method for Mobile Manipulator; Fast and resilient manipulation planning for target retrieval in clutter; Review on Motion Planning of Robotic Manipulator in Dynamic Environments; Multi-robot geometric task-and-motion planning for collaborative manipulation tasks
- Makes less novel: calling geometric feasibility checks from symbolic plans.
- Leaves open: a learned predicate whose conserved component is explicit and auditable.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### embodied AI/action models
- Representative hostile records: A Survey of Embodied Learning for Object-centric Robotic Manipulation; Robot Manipulation Based on Embodied Visual Perception: A Survey; From Nano Robotic Manipulation to Nano Manipulation Robot; The GummiArm Project: A Replicable and Variable-Stiffness Robot Arm for Experiments on Embodied AI; Young children’s embodied interactions with a social robot
- Makes less novel: broad robotics motivation and related empirical settings.
- Leaves open: a mechanism-level account of conserved affordance under mobile manipulation context shift.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

### invariance/equivariance/transport
- Representative hostile records: USEEK: Unsupervised SE(3)-Equivariant 3D Keypoints for Generalizable Manipulation; RiEMann: Near Real-Time SE(3)-Equivariant Robot Manipulation without Point Cloud Segmentation; Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation; PI-VLA: A Symmetry-Aware Predictive and Interactive Vision--Language--Action Framework for Rob...
- Makes less novel: standard geometric invariance/equivariance for manipulation.
- Leaves open: context-dependent conservation where only a quotient, not the full label, is invariant.
- Boundary: our contribution must not stop at this cluster's mechanism; it must show how the mechanism changes under the conservation quotient.

## Positive Novelty Boundary
- Define affordance as a contact-frame latent variable that can be conserved even when observed task success is not.
- Define access as a base/clutter-dependent gate computed from reachability and swept-volume obstruction.
- Provide an estimator that projects observed successes onto conserved equivalence classes after quotienting by access.
- Prove a sample-complexity or identifiability statement under explicit assumptions.
- Demonstrate under controlled base-pose and clutter shifts that the broken assumption matters.

## Negative Boundary
- Do not claim full real-robot validation.
- Do not claim full manipulation planning is solved.
- Do not claim all affordances are conserved; conservation is conditional on stable object/contact state and correct correspondence.
- Do not claim the access model is learned or perfect outside the controlled evidence.
