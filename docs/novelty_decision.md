# Novelty Decision

## Candidate Evaluation
| Candidate | Broken assumption | Central mechanism | Evidence path | Score |
|---|---|---|---|---:|
| Conserved Affordance Quotients | binary success labels directly measure object affordance | divide observed success into a conserved contact-frame affordance and a mutable access term, then project labels onto equivalence classes across base/clutter orbits | sample-complexity claim plus mobile-manipulation simulation with controlled base/clutter shifts | 9.6 |
| Censored Negative Affordance Learning | failed action attempts are true negative labels | treat unreachable trials as censored observations in a survival-style affordance estimator | compare censored and uncensored estimators under unreachable contexts | 8.2 |
| Clutter Topology Affordance Gates | clutter density is the relevant variable | use swept-volume homotopy classes rather than object counts to gate contact access | show identical density with different access topology | 7.8 |
| Morphology-Relative Affordance Gauges | affordances transfer between embodiments without changing coordinates | represent affordance in a robot-specific quotient space induced by reachable contact screws | compare arm lengths and bases in simulation | 7.5 |
| Affordance Residuals for Object-State Change | conservation violations are model error | use repeated quotient residuals to detect when an object part or articulation changed state | detect handle removal/articulation lock from residuals | 7.3 |

## Chosen Thesis
**Affordance Conservation for Mobile Manipulators**: in mobile manipulation, the observed success of an action contact under a base pose and clutter state should be modeled as a mutable access gate times a conserved contact-frame affordance. Learning or planning directly on the observed success label entangles object semantics with base/clutter censoring. A conserved affordance quotient recovers the object-side variable, transports it across base and clutter changes, and exposes residuals when the object/contact state truly changes.

## Why This Wins
- It changes the central mechanism from prediction or planning to conservation-aware factorization.
- It attacks a false hidden assumption shared by affordance predictors and mobile-base planners from opposite sides.
- It admits a clean theorem: quotient projection reduces sample complexity from context-specific labels to contact-class labels when access is known or certified.
- It is testable with a small mobile-manipulation simulator where base pose and clutter can change while object affordance remains fixed.

## What Will Be Unsupported
- Real-robot transfer is not established.
- The access gate is geometric/certified in the experiment, not learned from raw depth.
- The theorem requires correct contact correspondence and stable object state.
