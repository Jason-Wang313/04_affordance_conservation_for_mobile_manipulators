# Affordance Conservation for Mobile Manipulators

This repository contains paper 04 in the robotics research batch. The thesis is **Conserved Affordance Quotients (CAQ)**: observed mobile-manipulation success labels should be factored into a conserved contact-frame affordance and a mutable base/clutter access gate.

## Final Artifact

- Final PDF: `C:/Users/wangz/Downloads/04.pdf`
- Verified page count: 28 pages
- Verified PDF size: 1,135,968 bytes
- Verified SHA256: `BE3F6E60B846255AF672975E04F62AC8B3BDCBB040A15321CF6C3EC218031EA0`
- Final manuscript source: `paper/main.tex`
- Full-scale execution plan: `docs/full_scale_execution_plan.md`

VLA-style boxed-link verification:

- Link annotations: 238 total on pages `[(1, 41), (2, 39), (3, 2), (4, 20), (5, 122), (7, 2), (8, 2), (9, 1), (10, 2), (11, 1), (13, 1), (19, 1), (20, 1), (23, 2), (26, 1)]`.
- Annotation colors: green = 218, red = 20, cyan = 0.
- Border widths: `(0, 0, 1)` for all link annotations.
- Oversized annotation audit: 0 malformed page-edge rectangles.
- Visual audit: rendered pages 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 19, 20, 23, and 26; green citation/URL boxes and red internal-reference boxes are crisp and aligned.

## Main Evidence

The final version expands the original mechanism test into an eight-suite synthetic study:

- Main base/clutter distribution shifts
- Access-gate error taxonomy
- Contact-correspondence stress
- Support-burden sweeps
- Residual diagnostics
- Geometry/clutter sensitivity
- Calibration analysis
- Conservation-violation negative control

Final scale:

- Seed scale: 20
- Compact metric rows: 7040
- Evaluated test predictions, counting model/suite evaluations: 10,844,000
- Full-scale outputs: `results/full_scale/`
- Paper figures: `paper/figures/`

Key readout:

- Medium-shift CAQ Brier: 0.0294, nearly matching oracle intrinsic 0.0293.
- Medium-shift CAQ improves over monolithic logistic 0.0313, interaction logistic 0.0323, access-only 0.0361, object-only 0.0849, and context-table 0.1009.
- Correct-gate CAQ Brier in the access taxonomy is 0.0282; 20% symmetric gate error raises it to 0.0726.
- At 160 training samples and 8 context bins, CAQ Brier is 0.0285 versus context table 0.0967.
- When conservation is deliberately false, CAQ Brier rises from 0.0284 to 0.0519.

## Reproduce

```powershell
python scripts/run_simulation.py
python scripts/run_full_scale_caq.py --suite all --seed-scale 20
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final run was executed suite by suite with the same seed scale to keep progress auditable and RAM use low.

## Scope

This is a full-scale synthetic mechanism paper, not a real-robot deployment claim. The evidence assumes a known or accurate access gate, stable contact correspondence, and stable object/contact state. The final manuscript measures the boundary cases rather than hiding them: access-gate errors, correspondence corruption, residual limitations, and non-conserved affordances are all reported.
