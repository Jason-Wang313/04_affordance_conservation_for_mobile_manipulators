# Submission Version Log

| Version | Date | Changes | PDF |
|---|---|---|---|
| v1 | 2026-06-11 | Generated batch paper with 40-seed synthetic CAQ evidence and initial PDF. | `C:/Users/wangz/Downloads/04.pdf` |
| v2 | 2026-06-12 | Added access-gate noise stress test, stress figure, narrowed claims, and readiness docs. | `C:/Users/wangz/Downloads/04.pdf` |
| v3 | 2026-06-13 | Rebuilt as a full-scale final manuscript: detailed execution plan, reproduced baseline, new full-scale CAQ runner, eight experiment suites, 7040 compact metric rows, 10.844M evaluated test predictions, 10 paper figures, expanded limitations, appendix audit, and verified 28-page final PDF. | `C:/Users/wangz/Downloads/04.pdf` |

## v3 Evidence Delta

- `scripts/run_full_scale_caq.py`: new full-scale runner.
- `docs/full_scale_execution_plan.md`: required per-paper plan before expansion.
- `results/full_scale/*.csv`: compact full-scale metric artifacts.
- `results/full_scale/full_scale_summary.json`: scale and headline summary.
- `paper/figures/*.png`: final paper figures copied from full-scale outputs.
- `paper/main.tex`: rewritten final manuscript.

## v3 Verification

- Final PDF page count: 28.
- Final PDF file size: 1,136,853 bytes.
- Log scan: no unresolved citations/references, overfull boxes, fatal errors, or emergency stops.
- PDF text scan: expected full-scale claims present; internal hardening markers absent.
