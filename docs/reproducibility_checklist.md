# Reproducibility Checklist

## Environment

- Python dependencies: `matplotlib`, `numpy`, `pandas`, `requests`.
- LaTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.

## Commands

```powershell
python scripts/retrieve_literature.py
python scripts/analyze_literature.py
python scripts/run_simulation.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Expected Outputs

- `results/simulation_metrics.csv`
- `results/simulation_summary.csv`
- `results/change_residuals.csv`
- `results/access_noise_sweep.csv`
- `results/experiment_summary.md`
- `results/simulation_metadata.json`
- `figures/results_summary.png`
- `figures/benchmark_schematic.png`
- `figures/access_noise_sensitivity.png`
- `paper/main.pdf`
- `C:/Users/wangz/Downloads/04.pdf`

## Known Non-Reproducible Pieces

- Literature retrieval depends on external API state if rerun.
- No hardware data exists.
- No pinned lockfile exists.
