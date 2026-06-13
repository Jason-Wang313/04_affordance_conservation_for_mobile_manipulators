# Final Audit

1. **Chosen thesis**
   - Mobile-manipulation success labels should be factored into a conserved contact-frame affordance and a mutable base/clutter access gate. The paper calls this representation a Conserved Affordance Quotient (CAQ).

2. **Field assumption broken**
   - The broken assumption is that a failed or successful affordance observation directly measures object affordance. In mobile manipulation, the observed label may be censored by base pose, approach direction, reachability, and clutter obstruction.

3. **New central mechanism**
   - CAQ estimates the object-side contact-class affordance only from accessible observations and separately recomputes the access gate for each base/clutter context. The central object is the quotient, not a larger predictor or planner wrapper.

4. **Full-scale evidence**
   - `scripts/run_full_scale_caq.py` expands the evidence to eight suites at seed scale 20.
   - Compact metric rows: 7040.
   - Evaluated test predictions, counting model/suite evaluations: 10,844,000.
   - Main medium-shift CAQ Brier: 0.0294 versus oracle intrinsic 0.0293.
   - 20% symmetric access-gate error raises CAQ Brier from 0.0282 to 0.0726.
   - At 160 training samples and 8 context bins, CAQ Brier is 0.0285 versus context table 0.0967.
   - At full conservation violation, CAQ Brier rises to 0.0519 while interaction logistic reaches 0.0343.

5. **Biggest remaining weaknesses**
   - Evidence is synthetic and 2D.
   - Access is known or corrupted synthetically, not learned from real perception.
   - Contact correspondence is assumed and only stress-tested by label corruption.
   - No hardware validation.
   - The theorem is a support-burden concentration statement, not a broad manipulation theorem.

6. **Paper-readiness judgment**
   - Batch-final full-scale synthetic mechanism paper. It clears the 25-page gate and the final artifact is a genuine expanded manuscript with stronger experiments, negative controls, limitations, reproducibility details, and measured boundaries.
   - For venues requiring real robot evidence or learned perception, the correct classification remains revise-for-hardware rather than deployment-ready.

7. **Final PDF verification**
   - Final PDF path: `C:/Users/wangz/Downloads/04.pdf`
   - Verified page count: 28 pages.
   - Verified file size: 1,136,853 bytes.
   - Marker scan found no hardening prompt text, internal decision labels, or accidental Downloads-path text in the PDF body.

8. **Build verification**
   - `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, final `pdflatex`.
   - Log scan found no unresolved citations, unresolved references, overfull boxes, fatal errors, or emergency stops.
   - MiKTeX printed update notices; they did not affect successful compilation.

9. **Repository status expectation**
   - Commit and push after this audit update.
   - Remove local `paper/main.pdf` after copying/verifying the Downloads artifact.
