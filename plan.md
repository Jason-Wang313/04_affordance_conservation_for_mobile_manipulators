# Plan

## Objective
Produce a complete robotics / embodied-intelligence research paper for paper `04`, including a large prior-work sweep, novelty decision artifacts, runnable evidence, an anonymous ICLR-style manuscript, compiled PDF at `C:/Users/wangz/Downloads/04.pdf`, GitHub repository publication if credentials allow, and a final audit.

## Stages
1. Initialize run records
   - Create and maintain `child_status.md`.
   - Inspect existing files and reuse any valid artifacts.
2. Literature landscape
   - Retrieve at least 1000 related papers using scholarly APIs / search.
   - Save `docs/related_work_matrix.csv`.
   - Skim 300, deep-read 200-250 metadata/abstract-level records, and construct a 100-paper hostile prior-work set.
   - Write `docs/literature_map.md` and `docs/hostile_prior_work.md`.
3. Novelty selection
   - Identify field assumptions, at least 20 hidden assumptions, candidate directions that break them, and a final chosen thesis.
   - Save `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, and `docs/reviewer_attacks.md`.
4. Runnable evidence
   - Implement a compact, reproducible simulation and analysis around the chosen mechanism.
   - Generate figures/tables and write a README explaining how to rerun.
5. Manuscript
   - Obtain or recreate the latest official ICLR LaTeX template available at runtime.
   - Write an anonymous ICLR-style paper with honest claims and limitations.
   - Compile with direct `pdflatex`/`bibtex` passes where available; if unavailable or failing, document logs and produce the strongest fallback artifact.
6. Publication and audit
   - Save final PDF only to `C:/Users/wangz/Downloads/04.pdf`.
   - Create public GitHub repo `04_affordance_conservation_for_mobile_manipulators` and push complete repo if authentication allows.
   - Write `docs/final_audit.md` answering all required audit questions.

## Safety Notes
- Avoid nonzero diagnostic exits by wrapping probes or using existence checks.
- Use explicit generous timeouts for literature retrieval, experiments, and LaTeX builds.
- Do not delete prior artifacts unless proven invalid.
- Keep final claims conservative and mark unsupported claims.
