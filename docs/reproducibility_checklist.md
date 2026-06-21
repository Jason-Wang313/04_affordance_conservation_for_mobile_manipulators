# Reproducibility Checklist

## Environment

- Python dependencies: `matplotlib`, `numpy`, `pandas`, `requests`.
- LaTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.
- Full-scale runner is RAM-light: compact CSV outputs, no raw trajectory dumps.

## Commands

```powershell
python scripts/run_simulation.py
python scripts/run_full_scale_caq.py --suite main --seed-scale 20 --fresh
python scripts/run_full_scale_caq.py --suite access --seed-scale 20
python scripts/run_full_scale_caq.py --suite correspondence --seed-scale 20
python scripts/run_full_scale_caq.py --suite support --seed-scale 20
python scripts/run_full_scale_caq.py --suite residual --seed-scale 20
python scripts/run_full_scale_caq.py --suite geometry --seed-scale 20
python scripts/run_full_scale_caq.py --suite negative --seed-scale 20
python scripts/run_full_scale_caq.py --suite summarize --seed-scale 20
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Expected Outputs

- `results/full_scale/main_shift_metrics.csv`: 900 rows.
- `results/full_scale/access_error_taxonomy.csv`: 1120 rows.
- `results/full_scale/correspondence_stress.csv`: 360 rows.
- `results/full_scale/support_burden.csv`: 1520 rows.
- `results/full_scale/residual_diagnostics.csv`: 1600 rows.
- `results/full_scale/geometry_sensitivity.csv`: 1040 rows.
- `results/full_scale/negative_controls.csv`: 500 rows.
- `results/full_scale/leaderboard.csv`: 18 rows.
- `results/full_scale/full_scale_summary.json`: seed scale 20, 7040 compact rows, 10,844,000 evaluated test predictions counted across model/suite evaluations.
- `paper/figures/*.png`: final paper figures.
- `C:/Users/wangz/Downloads/04.pdf`: final verified 28-page PDF, 1,135,968 bytes, SHA256 `BE3F6E60B846255AF672975E04F62AC8B3BDCBB040A15321CF6C3EC218031EA0`.

## Verification

- `pdfinfo C:/Users/wangz/Downloads/04.pdf` reports 28 pages.
- `pdftotext` confirms expected full-scale claims including `10.844`, `0.0294`, and `0.0726`.
- PDF body scan has no hardening prompt text, internal decision labels, or accidental `Downloads` path text.
- `rg` log scan has no unresolved citations, unresolved references, overfull boxes, fatal errors, or emergency stops.
- VLA-style boxed-link audit confirms 238 annotations; green = 218, red = 20, cyan = 0; all borders `(0, 0, 1)`.
- Oversized annotation audit confirms 0 malformed page-edge rectangles.
- Visual PDF audit rendered pages 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 19, 20, 23, and 26; boxes are crisp and aligned.
