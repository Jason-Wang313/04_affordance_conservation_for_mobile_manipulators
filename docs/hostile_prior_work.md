# Hostile Prior Work Set

This set contains the top 100 records most likely to attack novelty. Each extraction is abstract/metadata-level unless marked otherwise in the matrix.

## H001. Kinematics and Local Motion Planning for Quasi-static Whole-body Mobile Manipulation (2016.0)
- Venue/source: not listed
- Authors: Krishna Shankar
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H002. Visual Grasp Affordance Localization in Point Clouds Using Curved Contact Patches (2016.0)
- Venue/source: International Journal of Humanoid Robotics
- Authors: Dimitrios Kanoulas; Jinoh Lee; Darwin G. Caldwell; Nikos G. Tsagarakis
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Visual Grasp Affordance Localization in Point Clouds Using Curved Contact Patches.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H003. Optimal Base Placement and Motion Planning for Mobile Manipulators (2012.0)
- Venue/source: not listed
- Authors: Bin Du; Jing Zhao; Chunyu Song
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A sampling or optimization planner for continuous robot motion.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H004. AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter (2025.0)
- Venue/source: not listed
- Authors: Yingbo Tang; Shuaike Zhang; Xiaoshuai Hao; Pengwei Wang; Jianlong Wu; Zhongyuan Wang; Shanghang Zhang
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A large learned representation or transformer-conditioned manipulation module.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H005. Implicit contact-rich manipulation planning for a manipulator with insufficient payload (2023.0)
- Venue/source: Robotic Intelligence and Automation
- Authors: Kento Nakatsuru; Weiwei Wan; Kensuke Harada
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Implicit contact-rich manipulation planning for a manipulator with insufficient payload.
- Actual mechanism introduced: A sampling or optimization planner for continuous robot motion.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H006. RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (2025.0)
- Venue/source: arXiv (Cornell University)
- Authors: Soroush Nasiriany; Sean Kirmani; Tianli Ding; Laura Smith; Yuke Zhu; Danny Driess; Dorsa Sadigh; Ted Xiao
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H007. Real-Time Collision-Free Motion Planning and Control for Mobile Manipulation with Quadrupeds (2023.0)
- Venue/source: not listed
- Authors: Zhefeng Cao; Hua Chen; Sen Li; Wei Zhang
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H008. Enabling Failure Recovery for On-The-Move Mobile Manipulation (2023.0)
- Venue/source: arXiv (Cornell University)
- Authors: Ben Burgess-Limerick; Leitner, Chris Lehnert Jurgen; Peter Corke
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H009. Model-Free Large-Scale Cloth Spreading With Mobile Manipulation: Initial Feasibility Study (2023.0)
- Venue/source: not listed
- Authors: Xiangyu Chu; Shengzhi Wang; Minjian Feng; Jiaxi Zheng; Yuxuan Zhao; Jing Huang; Kwok Wai Samuel Au
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H010. DORA: Object Affordance-Guided Reinforcement Learning for Dexterous Robotic Manipulation (2025.0)
- Venue/source: ArXiv.org
- Authors: Lei Zhang; Soumya Mondal; Zhenshan Bing; Kaixin Bai; Diwen Zheng; Zhaopeng Chen; Alois Knoll; Jianwei Zhang
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H011. Probabilistic Spatio-Temporal Fusion of Affordances for Grasping and Manipulation (2022.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Christoph Pohl; Tamim Asfour
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Probabilistic Spatio-Temporal Fusion of Affordances for Grasping and Manipulation.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H012. Information-driven Affordance Discovery for Efficient Robotic Manipulation (2024.0)
- Venue/source: arXiv (Cornell University)
- Authors: Pietro Mazzaglia; Taco Cohen; Daniel Dijkman
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H013. Generalized Affordance Templates for Mobile Manipulation (2022.0)
- Venue/source: 2022 International Conference on Robotics and Automation (ICRA)
- Authors: Stephen Hart; Ana Huamán Quispe; Michael W. Lanighan; Seth Gee
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H014. Tree Search-based Task and Motion Planning with Prehensile and Non-prehensile Manipulation for Obstacle Rearrangement in Clutter (2021.0)
- Venue/source: not listed
- Authors: Jinhwi Lee; Changjoo Nam; Jong-Hyeon Park; Chang-Hwan Kim
- Cluster: clutter and rearrangement manipulation
- Problem claimed: Manipulate target objects despite obstacles, occlusion, or required rearrangement.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: clutter changes feasibility but not the latent object action property; observed failures can be repaired by moving objects or replanning
- Variables treated as fixed: target affordance; robot kinematics; object geometry after rearrangement
- Failure modes ignored: moving clutter changes the object state; false negatives caused by temporary occlusion
- What it makes less novel: planning around or rearranging clutter to access targets
- What it leaves open: formal separation between changed access and changed object action semantics
- Evidence basis: abstract-level

## H015. Harmonious Sampling for Mobile Manipulation Planning (2019.0)
- Venue/source: not listed
- Authors: Mincheul Kang; Donghyuk Kim; Sung‐Eui Yoon
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A sampling or optimization planner for continuous robot motion.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H016. The UMass Mobile Manipulator UMan: An Experimental Platform for Autonomous Mobile Manipulation (2006.0)
- Venue/source: ScholarWorks@UMassAmherst (University of Massachusetts Amherst)
- Authors: Dov Katz; Emily Horrell; Yuandong Yang; Brendan Burns; Thomas Buckley; Anna Grishkan; Volodymyr Zhylkovskyy; Oliver Brock; Erik Learned-Miller
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H017. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023.0)
- Venue/source: arXiv (Cornell University)
- Authors: Wenlong Huang; Chen Wang; Ruohan Zhang; Yunzhu Li; Jiajun Wu; Li Fei-Fei
- Cluster: robot foundation/vision-language manipulation
- Problem claimed: Use broad multimodal representations to condition robot manipulation behavior.
- Actual mechanism introduced: A large learned representation or transformer-conditioned manipulation module.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: dataset distribution; robot embodiment; task definition
- Failure modes ignored: distribution shift, unmodeled geometry, and embodiment mismatch
- What it makes less novel: using broad pretrained representations for robot actions
- What it leaves open: a mechanism-level account of conserved affordance under mobile manipulation context shift
- Evidence basis: abstract-level

## H018. Unsupervised learning of object affordances for planning in a mobile manipulation platform (2011.0)
- Venue/source: not listed
- Authors: Emre Uğur; Erol Şahi̇n; Erhan Öztop
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H019. Combined Path and Motion Planning for Workspace Restricted Mobile Manipulators in Planetary Exploration (2023.0)
- Venue/source: IEEE Access
- Authors: Gonzalo J. Paz-Delgado; J. Ricardo Sánchez-Ibáñez; Raúl Domínguez; Carlos J. Pérez-del-Pulgar; Frank Kirchner; Alfonso García-Cerezo
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H020. Affordance based Part Recognition for Grasping and Manipulation (2011.0)
- Venue/source: not listed
- Authors: Karthik Mahesh Varadarajan; Markus Vincze
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H021. A Versatile Affordance Modeling Framework Using Screw Primitives to Increase Autonomy During Manipulation Contact Tasks (2022.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Adam Pettinger; Farshid Alambeigi; Mitch Pryor
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H022. Pose optimization for mobile manipulator grasping based on hybrid manipulability (2023.0)
- Venue/source: Industrial Robot the international journal of robotics research and application
- Authors: Yangmin Xie; Jiajia Liu; Yusheng Yang
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H023. Manipulation-Oriented Object Perception in Clutter through Affordance Coordinate Frames (2022.0)
- Venue/source: 2022 IEEE-RAS 21st International Conference on Humanoid Robots (Humanoids)
- Authors: Xiaotong Chen; Kaizhi Zheng; Zhen Zeng; Cameron Kisailus; Shreshtha Basu; James Cooney; Jana Pavlasek; Odest Chadwicke Jenkins
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H024. Towards affordance detection for robot manipulation using affordance for parts and parts for affordance (2018.0)
- Venue/source: Autonomous Robots
- Authors: Safoura Rezapour Lakani; Antonio Rodrı́guez-Sánchez; Justus Piater
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: metadata-level

## H025. A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation (2023.0)
- Venue/source: Sensors
- Authors: Dong Han; Beni Mulyana; Vladimir Stanković; Samuel Cheng
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H026. Affordance-Based Multi-Contact Whole-Body Pose Sequence Planning for Humanoid Robots in Unknown Environments (2018.0)
- Venue/source: not listed
- Authors: Peter Kaiser; Christian Mandery; Andreas Boltres; Tamim Asfour
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Affordance-Based Multi-Contact Whole-Body Pose Sequence Planning for Humanoid Robots in U....
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H027. Extraction of Whole-Body Affordances for Loco-Manipulation Tasks (2015.0)
- Venue/source: International Journal of Humanoid Robotics
- Authors: Peter Kaiser; Nikolaus Vahrenkamp; F. Schultje; Júlia Borràs; Tamim Asfour
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H028. The Affordance Template ROS package for robot task programming (2015.0)
- Venue/source: not listed
- Authors: Stephen Hart; Paul C. Dinh; Kimberly Hambuchen
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H029. Development of Human Support Robot as the research platform of a domestic mobile manipulator (2019.0)
- Venue/source: ROBOMECH Journal
- Authors: Takashi Yamamoto; Koji Terada; Akiyoshi Ochiai; Fuminori Saito; Yoshiaki Asahara; Kazuto Murase
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H030. Elastic Roadmaps: Globally Task-Consistent Motion for Autonomous Mobile Manipulation in Dynamic Environments (2006.0)
- Venue/source: not listed
- Authors: Y. Yang; Oliver Brock
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H031. Optimal Order Pick-and-Place of Objects in Cluttered Scene by a Mobile Manipulator (2021.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Fengyi Wang; J. Rogelio Guadarrama-Olvera; Gordon Cheng
- Cluster: reachability and workspace models
- Problem claimed: Represent whether an end effector can reach task frames under robot kinematics.
- Actual mechanism introduced: A reachability map, inverse reachability model, or kinematic feasibility estimator.
- Hidden assumptions: kinematic reachability can stand in for task affordance; clutter and contact semantics are external to the reachability model
- Variables treated as fixed: task/contact success model; object state; obstacle dynamics
- Failure modes ignored: reachable contacts that fail task semantics; blocked swept volumes; calibration error
- What it makes less novel: using reachability as a manipulation feasibility signal
- What it leaves open: how to quotient reachability out of affordance labels instead of replacing them
- Evidence basis: abstract-level

## H032. Posture evaluation for mobile manipulators using manipulation ability, tolerance on grasping, and pose error of end-effector (2021.0)
- Venue/source: Advanced Robotics
- Authors: Satoshi Suzuki; Daisuke Endo; Kimitoshi Yamazaki
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H033. Affordance-Driven Next-Best-View Planning for Robotic Grasping (2023.0)
- Venue/source: arXiv (Cornell University)
- Authors: Xuechao Zhang; Dong Wang; Han Sun; Weichuang Li; Bin Zhao; Zhigang Wang; Xiaoming Duan; Chongrong Fang; Xuelong Li; Jianping He
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Affordance-Driven Next-Best-View Planning for Robotic Grasping.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H034. Affordances in Psychology, Neuroscience, and Robotics: A Survey (2016.0)
- Venue/source: IEEE Transactions on Cognitive and Developmental Systems
- Authors: Lorenzo Jamone; Emre Uğur; Angelo Cangelosi; Luciano Fadiga; Alexandre Bernardino; Justus Piater; José Santos-Victor
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H035. The Grasp Strategy of a Robot Passer Influences Performance and Quality of the Robot-Human Object Handover (2020.0)
- Venue/source: Frontiers in Robotics and AI
- Authors: Valerio Ortenzi; Francesca Cini; Tommaso Pardi; Naresh Marturi; Rustam Stolkin; Peter Corke; Marco Controzzi
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to The Grasp Strategy of a Robot Passer Influences Performance and Quality of the Robot-Huma....
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H036. Semantic Grasping Via a Knowledge Graph of Robotic Manipulation: A Graph Representation Learning Approach (2022.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Ji Ho Kwak; Jaejun Lee; Joyce Jiyoung Whang; Sungho Jo
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Semantic Grasping Via a Knowledge Graph of Robotic Manipulation: A Graph Representation L....
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H037. Perceiving, learning, and exploiting object affordances for autonomous pile manipulation (2014.0)
- Venue/source: Autonomous Robots
- Authors: Dov Katz; Arun Venkatraman; Moslem Kazemi; J. Andrew Bagnell; Anthony Stentz
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H038. Learning Push-Grasping in Dense Clutter (2022.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Marios Kiatos; Iason Sarantopoulos; Leonidas Koutras; Sotiris Malassiotis; Zoe Doulgeri
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Learning Push-Grasping in Dense Clutter.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H039. An autonomous mobile manipulator for collecting sample containers (2014.0)
- Venue/source: QUT ePrints (Queensland University of Technology)
- Authors: Sankaranarayanan Natarajan; Sebastian Kasperski; Markus Eich
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H040. A Shared Autonomous Nursing Robot Assistant with Dynamic Workspace for Versatile Mobile Manipulation (2023.0)
- Venue/source: not listed
- Authors: Nikita Boguslavskii; Zhuoyun Zhong; Lorena Maria Genua; Zhi Li
- Cluster: reachability and workspace models
- Problem claimed: Represent whether an end effector can reach task frames under robot kinematics.
- Actual mechanism introduced: A reachability map, inverse reachability model, or kinematic feasibility estimator.
- Hidden assumptions: kinematic reachability can stand in for task affordance; clutter and contact semantics are external to the reachability model
- Variables treated as fixed: task/contact success model; object state; obstacle dynamics
- Failure modes ignored: reachable contacts that fail task semantics; blocked swept volumes; calibration error
- What it makes less novel: using reachability as a manipulation feasibility signal
- What it leaves open: how to quotient reachability out of affordance labels instead of replacing them
- Evidence basis: abstract-level

## H041. TARS: Tactile Affordance in Robot Synesthesia for Dexterous Manipulation (2024.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Qiwei Wu; Haidong Wang; Jiayu Zhou; Xiaogang Xiong; Yunjiang Lou
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H042. Affordance-Based Grasping and Manipulation in Real World Applications (2020.0)
- Venue/source: not listed
- Authors: Christoph Pohl; Kevin Hitzler; Raphael Grimm; Antonio Zea; Uwe D. Hanebeck; Tamim Asfour
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Affordance-Based Grasping and Manipulation in Real World Applications.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H043. Task and motion planning for mobile manipulators (2011.0)
- Venue/source: Rice Digital Scholarship Archive (Rice University)
- Authors: Ioan A. Şucan
- Cluster: task and motion planning
- Problem claimed: Compose symbolic action choices with continuous geometric feasibility.
- Actual mechanism introduced: A sampling or optimization planner for continuous robot motion.
- Hidden assumptions: symbolic predicates are stable under geometric context changes; continuous feasibility checks do not change the meaning of an affordance predicate
- Variables treated as fixed: predicate vocabulary; low-level controllers; scene object identities
- Failure modes ignored: predicate drift under clutter/base changes; expensive replanning; brittle discretization
- What it makes less novel: calling geometric feasibility checks from symbolic plans
- What it leaves open: a learned predicate whose conserved component is explicit and auditable
- Evidence basis: abstract-level

## H044. Whole-Body MPC for a Dynamically Stable Mobile Manipulator (2019.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Maria Vittoria Minniti; Farbod Farshidian; Ruben Grandia; Marco Hutter
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H045. Stability-constrained mobile manipulation planning on rough terrain (2022.0)
- Venue/source: Robotica
- Authors: Jiazhi Song; Inna Sharf
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A sampling or optimization planner for continuous robot motion.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H046. Variable impedance control on contact-rich manipulation of a collaborative industrial mobile manipulator: An imitation learning approach (2024.0)
- Venue/source: Robotics and Computer-Integrated Manufacturing
- Authors: Zhengxue Zhou; Xingyu Yang; Xuping Zhang
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H047. Body Extension by Using Two Mobile Manipulators (2023.0)
- Venue/source: Cyborg and Bionic Systems
- Authors: Yusuke Hirao; Weiwei Wan; Dimitrios Kanoulas; Kensuke Harada
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H048. Task-Oriented Robot Cognitive Manipulation Planning Using Affordance Segmentation and Logic Reasoning (2023.0)
- Venue/source: IEEE Transactions on Neural Networks and Learning Systems
- Authors: Zhongli Wang; Guohui Tian
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H049. Interactive Open-Ended Object, Affordance and Grasp Learning for Robotic Manipulation (2019.0)
- Venue/source: not listed
- Authors: Hamidreza Kasaei; Nima Shafii; Luís Seabra Lopes; Ana Maria Tomé
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Interactive Open-Ended Object, Affordance and Grasp Learning for Robotic Manipulation.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H050. RLAfford: End-to-End Affordance Learning for Robotic Manipulation (2023.0)
- Venue/source: not listed
- Authors: Yiran Geng; Boshi An; Haoran Geng; Yuanpei Chen; Yaodong Yang; Hao Dong
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H051. A Hierarchical Motion Planning Method for Mobile Manipulator (2023.0)
- Venue/source: Sensors
- Authors: Hanlin Chen; Xizhe Zang; Yubin Liu; Xuehe Zhang; Jie Zhao
- Cluster: task and motion planning
- Problem claimed: Compose symbolic action choices with continuous geometric feasibility.
- Actual mechanism introduced: A sampling or optimization planner for continuous robot motion.
- Hidden assumptions: symbolic predicates are stable under geometric context changes; continuous feasibility checks do not change the meaning of an affordance predicate
- Variables treated as fixed: predicate vocabulary; low-level controllers; scene object identities
- Failure modes ignored: predicate drift under clutter/base changes; expensive replanning; brittle discretization
- What it makes less novel: calling geometric feasibility checks from symbolic plans
- What it leaves open: a learned predicate whose conserved component is explicit and auditable
- Evidence basis: abstract-level

## H052. Reuleaux: Robot Base Placement by Reachability Analysis (2018.0)
- Venue/source: not listed
- Authors: Abhijit Makhal; Alex K. Goins
- Cluster: reachability and workspace models
- Problem claimed: Represent whether an end effector can reach task frames under robot kinematics.
- Actual mechanism introduced: A reachability map, inverse reachability model, or kinematic feasibility estimator.
- Hidden assumptions: kinematic reachability can stand in for task affordance; clutter and contact semantics are external to the reachability model
- Variables treated as fixed: task/contact success model; object state; obstacle dynamics
- Failure modes ignored: reachable contacts that fail task semantics; blocked swept volumes; calibration error
- What it makes less novel: using reachability as a manipulation feasibility signal
- What it leaves open: how to quotient reachability out of affordance labels instead of replacing them
- Evidence basis: abstract-level

## H053. Examples of Gibsonian Affordances in Legged Robotics Research Using an Empirical, Generative Framework (2020.0)
- Venue/source: Frontiers in Neurorobotics
- Authors: Sonia F. Roberts; Daniel E. Koditschek; Lisa J. Miracchi
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H054. Synergies Between Affordance and Geometry: 6-DoF Grasp Detection via Implicit Representations (2021.0)
- Venue/source: not listed
- Authors: Zhenyu Jiang; Yifeng Zhu; Maxwell Svetlik; Kuan Fang; Yuke Zhu
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Synergies Between Affordance and Geometry: 6-DoF Grasp Detection via Implicit Representat....
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H055. Learning 6-DoF Fine-grained Grasp Detection Based on Part Affordance Grounding (2023.0)
- Venue/source: arXiv (Cornell University)
- Authors: Yaoxian Song; Penglei Sun; Jin, Piaopiao; Yi Ren; Yu Zheng; Li, Zhixu; Chu, Xiaowen; Yue Zhang; Li, Tiefeng; Gu, Jason
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Learning 6-DoF Fine-grained Grasp Detection Based on Part Affordance Grounding.
- Actual mechanism introduced: A large learned representation or transformer-conditioned manipulation module.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H056. Spatial Action Maps for Mobile Manipulation (2020.0)
- Venue/source: not listed
- Authors: Jimmy Wu; Xingyuan Sun; Andy Zeng; Shuran Song; Johnny Lee; Szymon Rusinkiewicz; Thomas Funkhouser
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H057. Mobile Manipulation for the HSR Intelligent Home Service Robot (2019.0)
- Venue/source: not listed
- Authors: Jae-Bong Yi; Seung‐Joon Yi
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H058. Base Placement Optimization for Coverage Mobile Manipulation Tasks (2023.0)
- Venue/source: arXiv (Cornell University)
- Authors: Huiwen Zhang; Kai Mi; Zhijun Zhang
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H059. Kinesthetic Learning Based on Fast Marching Square Method for Manipulation (2023.0)
- Venue/source: Applied Sciences
- Authors: Adrián Prados; Alicia Mora; Blanca Muñoz López; Javier Muñoz; Santiago Garrido; Ramón Barber
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H060. ImageManip: Image-based Robotic Manipulation with Affordance-guided Next View Selection (2023.0)
- Venue/source: arXiv (Cornell University)
- Authors: Xiaoqi Li; Yanzi Wang; Yan Shen; Ponomarenko Iaroslav; Haoran Lu; Qianxu Wang; Boshi An; Jiaming Liu; Hao Dong
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H061. An Affordances and Electromyography Based Telemanipulation Framework for Control of Robotic Arm-Hand Systems (2023.0)
- Venue/source: not listed
- Authors: Ricardo V. Godoy; Bonnie Guan; Anany Dwivedi; Minas Liarokapis
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A large learned representation or transformer-conditioned manipulation module.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H062. Attribute-Based Robotic Grasping with One-Grasp Adaptation (2021.0)
- Venue/source: not listed
- Authors: Yang Yang; Yuanhao Liu; Hengyue Liang; Xibai Lou; Changhyun Choi
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Attribute-Based Robotic Grasping with One-Grasp Adaptation.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H063. An Intuitive, Affordances Oriented Telemanipulation Framework for a Dual Robot Arm Hand System: On the Execution of Bimanual Tasks (2019.0)
- Venue/source: not listed
- Authors: Gal Gorjup; Anany Dwivedi; Nathan Elangovan; Minas Liarokapis
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H064. Exercising Affordances of Objects: A Part-Based Approach (2018.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Safoura Rezapour Lakani; Antonio Rodrı́guez-Sánchez; Justus Piater
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H065. Predictive Reachability for Embodiment Selection in Mobile Manipulation Behaviors (2025.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Xiaoxu Feng; Takato Horii; Takayuki Nagai
- Cluster: reachability and workspace models
- Problem claimed: Represent whether an end effector can reach task frames under robot kinematics.
- Actual mechanism introduced: A reachability map, inverse reachability model, or kinematic feasibility estimator.
- Hidden assumptions: kinematic reachability can stand in for task affordance; clutter and contact semantics are external to the reachability model
- Variables treated as fixed: task/contact success model; object state; obstacle dynamics
- Failure modes ignored: reachable contacts that fail task semantics; blocked swept volumes; calibration error
- What it makes less novel: using reachability as a manipulation feasibility signal
- What it leaves open: how to quotient reachability out of affordance labels instead of replacing them
- Evidence basis: abstract-level

## H066. Learning and Reasoning with Action-Related Places for Robust Mobile Manipulation (2012.0)
- Venue/source: Journal of Artificial Intelligence Research
- Authors: F. Stulp; A. Fedrizzi; L. Mösenlechner; M. Beetz
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H067. Learning Instruction-Guided Manipulation Affordance via Large Models for Embodied Robotic Tasks (2024.0)
- Venue/source: arXiv (Cornell University)
- Authors: Dayou Li; Chenkun Zhao; Shuo Yang; Lin Ma; Yibin Li; Wei Zhang
- Cluster: robot foundation/vision-language manipulation
- Problem claimed: Use broad multimodal representations to condition robot manipulation behavior.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: dataset distribution; robot embodiment; task definition
- Failure modes ignored: distribution shift, unmodeled geometry, and embodiment mismatch
- What it makes less novel: using broad pretrained representations for robot actions
- What it leaves open: a mechanism-level account of conserved affordance under mobile manipulation context shift
- Evidence basis: abstract-level

## H068. Deep Reinforcement Learning for Robotic Pushing and Picking in Cluttered Environment (2019.0)
- Venue/source: not listed
- Authors: Yuhong Deng; Xiaofeng Guo; Yixuan Wei; Kai Lu; Bin Fang; Di Guo; Huaping Liu; Fuchun Sun
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H069. Learning relational affordance models for two-arm robots (2014.0)
- Venue/source: not listed
- Authors: Bogdan Moldovan; Luc De Raedt
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A graph or relational representation over scene entities and action relations.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H070. Topological mapping for robot navigation using affordance features (2015.0)
- Venue/source: not listed
- Authors: Karthik Mahesh Varadarajan
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H071. Linear manipulator: Motion control of an n-link robotic arm mounted on a mobile slider (2023.0)
- Venue/source: Heliyon
- Authors: Sandeep A. Kumar; Ravinesh Chand; Ronal P. Chand; Bibhya Sharma
- Cluster: reachability and workspace models
- Problem claimed: Represent whether an end effector can reach task frames under robot kinematics.
- Actual mechanism introduced: A reachability map, inverse reachability model, or kinematic feasibility estimator.
- Hidden assumptions: kinematic reachability can stand in for task affordance; clutter and contact semantics are external to the reachability model
- Variables treated as fixed: task/contact success model; object state; obstacle dynamics
- Failure modes ignored: reachable contacts that fail task semantics; blocked swept volumes; calibration error
- What it makes less novel: using reachability as a manipulation feasibility signal
- What it leaves open: how to quotient reachability out of affordance labels instead of replacing them
- Evidence basis: abstract-level

## H072. A Survey of Embodied Learning for Object-centric Robotic Manipulation (2025.0)
- Venue/source: Machine Intelligence Research
- Authors: Ying Zheng; Lei Yao; Yuejiao Su; Yi Zhang; Yi Wang; Sicheng Zhao; Yiyi Zhang; Lap‐Pui Chau
- Cluster: embodied AI/action models
- Problem claimed: Address a robotics or AI problem related to A Survey of Embodied Learning for Object-centric Robotic Manipulation.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: dataset distribution; robot embodiment; task definition
- Failure modes ignored: distribution shift, unmodeled geometry, and embodiment mismatch
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: a mechanism-level account of conserved affordance under mobile manipulation context shift
- Evidence basis: abstract-level

## H073. HRP: Human affordances for Robotic Pre-training (2024.0)
- Venue/source: not listed
- Authors: Mohan Kumar Srirama; Sudeep Dasari; Shikhar Bahl; Abhinav Gupta
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H074. Approaching motion planning for mobile manipulators considering the uncertainty of self-positioning and object’s pose estimation (2022.0)
- Venue/source: Robotics and Autonomous Systems
- Authors: Kimitoshi Yamazaki; Satoshi Suzuki; Yusuke Kuribayashi
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H075. Demonstrating Mobile Manipulation in the Wild: A Metrics-Driven Approach (2023.0)
- Venue/source: not listed
- Authors: Max Bajracharya; James Borders; Richard Cheng; Dan Helmick; Lukas Kaul; Dan Kruse; John Leichty; Jeremy Ma; Carolyn Matl; Frank Michel; Chavdar Papazov; Josh Petersen
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H076. Seeking Human Help to Manage Plan Failure Risks in Semi-Autonomous Mobile Manipulation (2022.0)
- Venue/source: Journal of Computing and Information Science in Engineering
- Authors: Sarah Al-Hussaini; Neel Dhanaraj; Jason M. Gregory; Rex Jomy Joseph; Shantanu Thakar; Brual C. Shah; Jeremy A. Marvel; Satyandra K. Gupta
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H077. A4T: Hierarchical Affordance Detection for Transparent Objects Depth Reconstruction and Manipulation (2022.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Jiaqi Jiang; Guanqun Cao; Thanh-Toan Do; Shan Luo
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H078. Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics (2024.0)
- Venue/source: not listed
- Authors: Peiqi Liu; Yaswanth Orru; Jay Vakil; Chris Paxton; Nur Muhammad Mahi Shafiullah; Lerrel Pinto
- Cluster: robot foundation/vision-language manipulation
- Problem claimed: Use broad multimodal representations to condition robot manipulation behavior.
- Actual mechanism introduced: A large learned representation or transformer-conditioned manipulation module.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: dataset distribution; robot embodiment; task definition
- Failure modes ignored: distribution shift, unmodeled geometry, and embodiment mismatch
- What it makes less novel: using broad pretrained representations for robot actions
- What it leaves open: a mechanism-level account of conserved affordance under mobile manipulation context shift
- Evidence basis: abstract-level

## H079. 3D Laser Scanner for Underwater Manipulation (2018.0)
- Venue/source: Sensors
- Authors: Albert Palomer; Pere Ridao; Dina Youakim; David Ribas; Josep Forest; Yvan Pétillot
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to 3D Laser Scanner for Underwater Manipulation.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H080. Learning to grasp and extract affordances: the Integrated Learning of Grasps and Affordances (ILGA) model (2015.0)
- Venue/source: Biological Cybernetics
- Authors: James Bonaiuto; Michael A. Arbib
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H081. Singularity Avoidance Control of a Non-Holonomic Mobile Manipulator for Intuitive Hand Guidance (2019.0)
- Venue/source: Robotics
- Authors: Matthias Weyrer; Mathias Brandstötter; Manfred Husty
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H082. RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation (2026.0)
- Venue/source: ArXiv.org
- Authors: Xiao, Zhanqi; Ruiping Wang; Xilin Chen
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H083. MIRA: Mental Imagery for Robotic Affordances (2022.0)
- Venue/source: arXiv (Cornell University)
- Authors: Yen-Chen Lin; Pete Florence; Andy Zeng; Jonathan T. Barron; Yilun Du; Wei-Chiu Ma; Anthony Simeonov; Alberto Rodriguez Garcia; Phillip Isola
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H084. Articulated Object Interaction in Unknown Scenes with Whole-Body Mobile Manipulation (2022.0)
- Venue/source: 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- Authors: Mayank Mittal; David Hoeller; Farbod Farshidian; Marco Hutter; Animesh Garg
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H085. A survey of robot manipulation in contact (2022.0)
- Venue/source: Robotics and Autonomous Systems
- Authors: Markku Suomalainen; Yiannis Karayiannidis; Ville Kyrki
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to A survey of robot manipulation in contact.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H086. Affordance-Based Human–Robot Interaction With Reinforcement Learning (2023.0)
- Venue/source: IEEE Access
- Authors: Francisco Munguia‐Galeano; Satheeshkumar Veeramani; Juan David Hernández; Qingmeng Wen; Ze Ji
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H087. Towards a hierarchy of loco-manipulation affordances (2016.0)
- Venue/source: not listed
- Authors: Peter Kaiser; Eren Erdal Aksoy; Markus Grotz; Tamim Asfour
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H088. Learning Affordance Segmentation for Real-World Robotic Manipulation via Synthetic Images (2019.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Fu-Jen Chu; Ruinian Xu; Patricio A. Vela
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A representation constrained by geometric invariance or equivariance.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H089. The Design of Stretch: A Compact, Lightweight Mobile Manipulator for Indoor Human Environments (2022.0)
- Venue/source: 2022 International Conference on Robotics and Automation (ICRA)
- Authors: Charles C. Kemp; Aaron Edsinger; Henry Clever; Blaine Matulevich
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H090. Incorporating Object Intrinsic Features Within Deep Grasp Affordance Prediction (2020.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Matthew Veres; Ian Cabral; Medhat Moussa
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Incorporating Object Intrinsic Features Within Deep Grasp Affordance Prediction.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H091. Learning of Tool Affordances for autonomous tool manipulation (2011.0)
- Venue/source: not listed
- Authors: Raghvendra Jain; Tetsunari Inamura
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H092. Review of Learning-Based Robotic Manipulation in Cluttered Environments (2022.0)
- Venue/source: Sensors
- Authors: Marwan Qaid Mohammed; Lee Chung Kwek; Shing Chyi Chua; Arafat Al-Dhaqm; Saeid Nahavandi; Taiseer Abdalla Elfadil Eisa; Muhammad Fahmi Miskon; Mohammed Nasser Al‐Mhiqani; Abdulalem Ali; Mohammed Abaker; Esmail Ali Alan...
- Cluster: clutter and rearrangement manipulation
- Problem claimed: Manipulate target objects despite obstacles, occlusion, or required rearrangement.
- Actual mechanism introduced: A learned policy/value mechanism optimized from rewards or interaction data.
- Hidden assumptions: clutter changes feasibility but not the latent object action property; observed failures can be repaired by moving objects or replanning
- Variables treated as fixed: target affordance; robot kinematics; object geometry after rearrangement
- Failure modes ignored: moving clutter changes the object state; false negatives caused by temporary occlusion
- What it makes less novel: planning around or rearranging clutter to access targets
- What it leaves open: formal separation between changed access and changed object action semantics
- Evidence basis: abstract-level

## H093. KPAM: KeyPoint Affordances for Category-Level Robotic Manipulation (2022.0)
- Venue/source: Springer proceedings in advanced robotics
- Authors: Lucas Manuelli; Wei Gao; Pete Florence; Russ Tedrake
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H094. Mixed Reality Interface for Improving Mobile Manipulator Teleoperation in Contamination Critical Applications (2020.0)
- Venue/source: Procedia Manufacturing
- Authors: Bence Bejczy; Rohat Bozyil; Evaldas Vaičekauskas; Sune Baagø Krogh Petersen; Simon Bøgh; Sebastian Hjorth; Emil Blixt Hansen
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H095. Fast and resilient manipulation planning for target retrieval in clutter (2020.0)
- Venue/source: arXiv (Cornell University)
- Authors: Changjoo Nam; Jinhwi Lee; Sang Hun Cheong; Brian Y. Cho; ChangHwan Kim
- Cluster: task and motion planning
- Problem claimed: Compose symbolic action choices with continuous geometric feasibility.
- Actual mechanism introduced: A task-and-motion planning interface between discrete actions and continuous feasibility.
- Hidden assumptions: symbolic predicates are stable under geometric context changes; continuous feasibility checks do not change the meaning of an affordance predicate
- Variables treated as fixed: predicate vocabulary; low-level controllers; scene object identities
- Failure modes ignored: predicate drift under clutter/base changes; expensive replanning; brittle discretization
- What it makes less novel: calling geometric feasibility checks from symbolic plans
- What it leaves open: a learned predicate whose conserved component is explicit and auditable
- Evidence basis: abstract-level

## H096. Garbage Collection and Sorting with a Mobile Manipulator using Deep Learning and Whole-Body Control (2021.0)
- Venue/source: not listed
- Authors: Jingyi Liu; Pietro Balatti; Kirsty Ellis; Denis Hadjivelichkov; Danail Stoyanov; Arash Ajoudani; Dimitrios Kanoulas
- Cluster: grasp/contact manipulation
- Problem claimed: Address a robotics or AI problem related to Garbage Collection and Sorting with a Mobile Manipulator using Deep Learning and Whole-Bo....
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: task labels remain meaningful across the deployment contexts considered
- Variables treated as fixed: candidate contacts; gripper model; local surface geometry
- Failure modes ignored: graspability does not imply task affordance; unseen base approach directions
- What it makes less novel: broad robotics motivation and related empirical settings
- What it leaves open: task-level conservation beyond local grasp/contact scores
- Evidence basis: abstract-level

## H097. Keep It Upright: Model Predictive Control for Nonprehensile Object Transportation With Obstacle Avoidance on a Mobile Manipulator (2023.0)
- Venue/source: IEEE Robotics and Automation Letters
- Authors: Adam Heins; Angela P. Schoellig
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H098. An Architecture for Online Affordance‐based Perception and Whole‐body Planning (2014.0)
- Venue/source: Journal of Field Robotics
- Authors: Maurice Fallon; Scott Kuindersma; Sisir Karumanchi; Matthew Antone; Toby Schneider; Hongkai Dai; Claudia Pérez D’Arpino; Robin Deits; M. DiCicco; Dehann Fourie; Twan Koolen; Pat Marion
- Cluster: robot affordance learning
- Problem claimed: Predict or learn where and how a robot can act on objects or parts from perception.
- Actual mechanism introduced: A perception-to-affordance predictor trained from demonstrations, labels, or interaction.
- Hidden assumptions: affordance labels are object/part properties rather than censored access observations; base pose and clutter variation are covered by training data or can be ignored
- Variables treated as fixed: robot morphology; base pose distribution; clutter process; action primitive frame
- Failure modes ignored: confusing inaccessible views with non-affordant parts; spurious base/clutter correlations
- What it makes less novel: generic affordance prediction from perception
- What it leaves open: whether a failed affordance observation is intrinsic or only base/clutter-censored
- Evidence basis: abstract-level

## H099. Multi-skill Mobile Manipulation for Object Rearrangement (2022.0)
- Venue/source: arXiv (Cornell University)
- Authors: Jiayuan Gu; Devendra Singh Chaplot; Hao Su; Jitendra Malik
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level

## H100. Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation (2024.0)
- Venue/source: arXiv (Cornell University)
- Authors: Zipeng Fu; Tony Z. Zhao; Chelsea Finn
- Cluster: mobile manipulation and base placement
- Problem claimed: Choose base/whole-body configurations that make manipulation tasks feasible.
- Actual mechanism introduced: A domain-specific model, planner, or learned predictor described by the paper.
- Hidden assumptions: the manipulation target or affordance query is already fixed before base planning; reachability is sufficient to represent action success
- Variables treated as fixed: object affordance predicate; contact semantics; environment map quality
- Failure modes ignored: reachable but semantically wrong contacts; clutter-induced censoring of affordance evidence
- What it makes less novel: base-pose selection and whole-body feasibility reasoning
- What it leaves open: how object affordances should be conserved while access changes
- Evidence basis: abstract-level
