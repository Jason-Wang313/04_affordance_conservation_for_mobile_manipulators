# Full-Scale Execution Plan

Paper 04: Affordance Conservation for Mobile Manipulators

## Current Claim

The current paper claims that observed mobile-manipulation success labels should be factored into a conserved contact-frame affordance and a mutable base/clutter access gate. The conserved affordance quotient (CAQ) estimates intrinsic contact-class success from accessible observations only, transports that estimate across base/clutter shifts, and uses conservation residuals as diagnostics for access, correspondence, or object-state failures.

The existing evidence is honest but narrow: a 40-seed 2D synthetic mobile-manipulation simulation with a known geometric access gate, five predictors, one shifted test distribution, one residual diagnostic, and one random access-gate flip stress. The manuscript is about seven pages, so it is not yet a final full-scale paper under the batch standard.

## Main Gaps To Close

1. The empirical scope is too small for a final manuscript.
2. The current access-noise result only uses random symmetric flips; it does not separate false-access and false-blocked errors.
3. The current simulation has one train/test shift; it does not sweep shift severity, clutter severity, support scarcity, reach geometry, or contact-correspondence noise.
4. The residual diagnostic only tests a large handle affordance drop; it needs magnitude sweeps and false-positive controls.
5. Baselines are useful but limited; the final pass should add an oracle-intrinsic bound, a class-access interaction model, shrinkage variants, and context-oracle upper/lower references where appropriate.
6. The paper does not yet include calibration/reliability analysis, support-burden curves, negative controls, or detailed per-regime failure taxonomy.
7. The writing must expand from a mechanism note into a final paper with a full experimental section, ablations, related work boundary, limitations, reproducibility, and appendix details.

## Target Experiments

All experiments should keep the central claim conditional: CAQ works when contact correspondence is stable and the access gate is known or accurate. The new results should strengthen both the positive mechanism and the negative boundary.

1. Large shifted benchmark
   - Increase seeds while keeping each seed compact.
   - Run multiple train/test distribution shifts: mild, medium, severe, and reverse.
   - Report Brier, log loss, accuracy, F1, AUC, blocked false positives, affordance loss, calibration error, reliability slope, and accessible prediction variance.

2. Access-gate error taxonomy
   - Sweep symmetric random flips.
   - Sweep false-access errors only, where blocked contacts are incorrectly declared accessible.
   - Sweep false-blocked errors only, where accessible contacts are incorrectly declared blocked.
   - Sweep structured errors tied to reach margin, approach margin, and clutter-line margin.
   - Report where CAQ degrades gradually versus catastrophically.

3. Contact-correspondence stress
   - Randomly remap a fraction of contact classes during training and/or testing.
   - Add site-level label swaps and class-level confusion.
   - Measure how residuals and predictive metrics respond.

4. Support-burden study
   - Vary training set size and number of base/clutter bins.
   - Compare CAQ to context-table and interaction models under sparse support.
   - Show the empirical version of the theorem: context-specific estimators need support in many cells, while CAQ needs accessible support per class.

5. Residual diagnostics
   - Sweep object-state changes: handle drop magnitudes, slot/button changes, and flat false changes.
   - Include no-change controls.
   - Report residual detection AUC and false-positive rates, not just one success rate.

6. Geometry and clutter sensitivity
   - Sweep reach annulus width, approach-cone threshold, clutter density, obstacle radius, and base distribution concentration.
   - Report heatmaps or compact tables to show when access dominates and when intrinsic affordance dominates.

7. Negative controls
   - Break the conservation assumption by letting affordance depend on base direction or clutter contact.
   - Show that CAQ should lose its advantage or raise residuals under these violations.
   - Use this as evidence of honest scope rather than trying to hide the failure mode.

8. Calibration analysis
   - Reliability bins and expected calibration error for CAQ, logistic, context table, object-only, and access-only.
   - Include calibration-sensitive interpretation because CAQ's strongest current win is Brier/log loss rather than AUC.

## Baselines And Comparators

Required models:

1. Conserved quotient (CAQ)
2. CAQ with stronger shrinkage
3. Object-only class means
4. Access-only reachability predictor
5. Context table over class, base-angle bin, clutter bin
6. Monolithic logistic predictor with class, geometry, clutter, blocked, and access features
7. Class-access interaction logistic predictor
8. Oracle intrinsic-affordance predictor using the generator's true class affordance and true gate
9. Oracle gate plus learned class means, to separate class-estimation error from access-certification error
10. Context-oracle table or saturated empirical table when enough support exists, used only as a reference and not oversold

## Figures And Tables

Planned final figures:

1. Benchmark schematic showing conserved contact classes and mutable base/clutter access.
2. Full-scale leaderboard with calibration and classification metrics.
3. Access-error taxonomy curves.
4. Support-burden curves over training size and context-bin count.
5. Residual diagnostic ROC or change-magnitude curves.
6. Contact-correspondence stress curves.
7. Geometry/clutter sensitivity heatmap.
8. Reliability/calibration plots.
9. Negative-control failure plot.

Planned tables:

1. Main aggregate metrics with confidence intervals.
2. Per-shift leaderboard.
3. Access-error taxonomy summary.
4. Support-burden summary.
5. Residual diagnostic summary.
6. Correspondence stress summary.
7. Negative-control summary.
8. Experiment configuration and sample counts.
9. Failure-mode taxonomy.

## Writing Expansion Strategy

The final manuscript should be at least 25 pages when compiled, with length coming from real content:

1. Expand the introduction to motivate label censoring in mobile manipulation and precisely define what is conserved.
2. Expand related work into separate subsections for affordance learning, reachability/base placement, TAMP/clutter, value maps/foundation robotics, and invariance/censoring.
3. Add a clearer problem setup with notation for sites, classes, contexts, gates, access margins, and residuals.
4. Strengthen the formal section with assumptions, estimator, theorem, proof, support-burden interpretation, and failure conditions.
5. Add a detailed simulator and evaluation protocol section.
6. Add full experimental sections for each planned suite, with honest interpretation of both wins and failures.
7. Add a broad limitations section that emphasizes known access, assumed correspondence, 2D synthetic evidence, and conservation violations.
8. Add a reproducibility appendix with commands, seeds, dataset sizes, result files, plotting, and compute/memory notes.

## Page-Count Strategy

The gate is strict: the final PDF must compile to at least 25 pages and be judged a real final paper, not padded. Page growth should come from the expanded experiment suites, additional figures/tables, proofs, related work, limitations, reproducibility, and appendices. The PDF must not be copied to Downloads until this gate is satisfied.

## RAM-Light Execution Strategy

1. Run experiments sequentially, not as a large in-memory sweep.
2. Store only compact row-level metrics and small diagnostic aggregates.
3. Avoid retaining raw obstacle trajectories unless needed for a figure.
4. Use per-suite CSV files in `results/full_scale/`.
5. Write progress logs after every suite and seed block.
6. Build summary tables and figures from compact CSVs.
7. Keep plot generation separated from simulation generation so failed plots do not erase completed experiment data.
8. Use deterministic seeds and resumable outputs where practical.

## Acceptance Checklist

Before Paper 04 can be considered final:

1. `docs/full_scale_execution_plan.md` exists before implementation changes.
2. Existing evidence is reproduced or intentionally superseded.
3. Full-scale experiment script runs successfully and writes compact CSVs.
4. Main figures and tables are generated from the full-scale results.
5. Manuscript is rewritten as a full final paper with honest claims.
6. Compiled local PDF is at least 25 pages.
7. Marker scan confirms no hardening prompt text, internal decision labels, or accidental file-path/provenance text appears in the paper body.
8. `C:\Users\wangz\Downloads\04.pdf` is overwritten only after the final manuscript passes the page and content gate.
9. The Downloads PDF is verified as the actual paper and at least 25 pages.
10. README, claims, rigor checklist, final audit, readiness decision, reviewer attacks, reproducibility checklist, and version log are updated.
11. Local build artifacts that should not be final deliverables are removed or ignored.
12. The repository is committed and pushed.
13. Only then may work proceed to Paper 05.
