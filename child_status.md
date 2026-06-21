# Child Status

Stage: VLA-style boxed-link hardening complete

Current facts:

- Chosen thesis: Conserved Affordance Quotients for mobile manipulators.
- Literature sweep complete: `docs/related_work_matrix.csv` contains 1100 deduplicated OpenAlex records.
- Full-scale execution plan created before the v3 expansion: `docs/full_scale_execution_plan.md`.
- Baseline evidence reproduced with `python scripts/run_simulation.py`.
- Full-scale evidence complete with `scripts/run_full_scale_caq.py`.
- Full-scale scale:
  - Seed scale: 20
  - Compact metric rows: 7040
  - Evaluated test predictions, counting model/suite evaluations: 10,844,000
- Main result:
  - Medium-shift CAQ Brier: 0.0294
  - Medium-shift oracle intrinsic Brier: 0.0293
  - Medium-shift context-table Brier: 0.1009
  - 20% symmetric access-gate error CAQ Brier: 0.0726
- Manuscript source: `paper/main.tex`.
- Final local build completed successfully.
- Final PDF copied to and verified at `C:\Users\wangz\Downloads\04.pdf`.
- Verified Downloads PDF page count: 28.
- Verified Downloads PDF file size: 1,135,968 bytes.
- Verified Downloads PDF SHA256: `BE3F6E60B846255AF672975E04F62AC8B3BDCBB040A15321CF6C3EC218031EA0`.
- Added explicit VLA-style boxed-link policy after the existing `hyperref` import in `paper/main.tex`.
- Split a page-crossing citation cluster without adding or removing citation keys so link boxes remain local.
- Verified final link inventory: 238 annotations on pages `[(1, 41), (2, 39), (3, 2), (4, 20), (5, 122), (7, 2), (8, 2), (9, 1), (10, 2), (11, 1), (13, 1), (19, 1), (20, 1), (23, 2), (26, 1)]`; colors green = 218, red = 20, cyan = 0; all borders `(0, 0, 1)`.
- Oversized annotation audit found 0 malformed page-edge rectangles.
- Rendered and visually inspected pages 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 19, 20, 23, and 26; highlighted boxes are crisp and aligned.
- Verified no duplicate `C:\Users\wangz\Downloads\4.pdf` was created.
- PDF body scan found expected full-scale claims and no internal hardening markers.
- LaTeX log scan found no unresolved citations/references, overfull boxes, fatal errors, or emergency stops.
- Public GitHub repository:
  - `https://github.com/Jason-Wang313/04_affordance_conservation_for_mobile_manipulators`

Important files:

- `docs/full_scale_execution_plan.md`
- `docs/full_scale_results_summary.md`
- `results/full_scale/full_scale_summary.json`
- `results/full_scale/*.csv`
- `paper/figures/*.png`
- `paper/main.tex`
- `C:\Users\wangz\Downloads\04.pdf`

Commands run in v3:

- `python scripts/run_simulation.py`
- `python scripts/run_full_scale_caq.py --suite main --seed-scale 20 --fresh`
- `python scripts/run_full_scale_caq.py --suite access --seed-scale 20`
- `python scripts/run_full_scale_caq.py --suite correspondence --seed-scale 20`
- `python scripts/run_full_scale_caq.py --suite support --seed-scale 20`
- `python scripts/run_full_scale_caq.py --suite residual --seed-scale 20`
- `python scripts/run_full_scale_caq.py --suite geometry --seed-scale 20`
- `python scripts/run_full_scale_caq.py --suite negative --seed-scale 20`
- `python scripts/run_full_scale_caq.py --suite summarize --seed-scale 20`
- `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, final `pdflatex` from `paper/`
- `Copy-Item paper\main.pdf C:\Users\wangz\Downloads\04.pdf`

Failures and recovery:

- Initial reproduction run hit the short command timeout after seed 20; reran with a longer timeout and completed.
- First full-scale access suite was too slow because it regenerated train/test worlds for every error mode and rate; patched it to reuse per-seed worlds.
- Residual and geometry suites exceeded time windows at their first full sample sizes; patched them to keep the full condition grids and seed scale while using compact per-condition sample sizes suitable for secondary diagnostics.
- First manuscript compile was 18 pages; expanded with substantive appendices and full-scale audit material until the verified final was 28 pages.
- A LaTeX macro collision with `\E` was fixed by renaming the expectation/probability macros.

Next step:

- Proceed to paper 03 after this VLA-style boxed-link hardening changeset is pushed.
