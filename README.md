# Affordance Conservation for Mobile Manipulators

This repository contains the paper-04 child run for a robotics research batch.
The chosen thesis is **Conserved Affordance Quotients**: observed mobile-manipulation success labels should be factored into a conserved contact-frame affordance and a mutable base/clutter access gate.

## Reproduce

```powershell
python scripts/retrieve_literature.py
python scripts/analyze_literature.py
python scripts/run_simulation.py
python scripts/fetch_iclr_template.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The compiled batch deliverable is saved at:

```text
C:/Users/wangz/Downloads/04.pdf
```

## Key Artifacts

- `docs/related_work_matrix.csv`: 1100-entry literature sweep.
- `docs/literature_map.md`: field map and assumptions.
- `docs/hostile_prior_work.md`: 100-paper hostile prior-work set.
- `docs/novelty_boundary_map.md`: what is and is not novel.
- `docs/novelty_decision.md`: selected thesis and rejected alternatives.
- `docs/claims.md`: supported and unsupported claims.
- `docs/reviewer_attacks.md`: likely reviewer attacks.
- `results/experiment_summary.md`: simulation readout.
- `results/access_noise_sweep.csv`: access-gate noise stress test.
- `figures/access_noise_sensitivity.png`: access-gate noise sensitivity figure.
- `paper/main.tex`: anonymous ICLR-style manuscript.

## Scope

The evidence is a synthetic mechanism test with a known geometric access gate.
Submission-hardening v2 adds an access-gate noise stress test; CAQ Brier rises from 0.0276 at 0% gate flips to 0.0721 at 20% flips. It does not claim real-robot deployment, learned access estimation, or automatic contact correspondence.
