# Submission Version Log

| Version | Date | Changes | PDF |
|---|---|---|---|
| v1 | 2026-06-11 | Generated batch paper with 40-seed synthetic CAQ evidence and initial PDF. | `C:/Users/wangz/Downloads/04.pdf` |
| v2 | 2026-06-12 | Added access-gate noise stress test, stress figure, narrowed claims, and readiness docs. | `C:/Users/wangz/Downloads/04.pdf` |
| v3 | 2026-06-13 | Rebuilt as a full-scale final manuscript: detailed execution plan, reproduced baseline, new full-scale CAQ runner, eight experiment suites, 7040 compact metric rows, 10.844M evaluated test predictions, 10 paper figures, expanded limitations, appendix audit, and verified 28-page final PDF. | `C:/Users/wangz/Downloads/04.pdf` |
| Final-link-hardening | 2026-06-21 | Added explicit VLA-style boxed-link policy, split one page-crossing citation cluster without changing cited keys, rebuilt the 28-page final PDF, and verified no cyan or oversized page-edge link boxes. | `C:/Users/wangz/Downloads/04.pdf` |

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

## Final-Link-Hardening Verification

- Canonical PDF: `C:/Users/wangz/Downloads/04.pdf` (28 pages, 1,135,968 bytes).
- SHA256: `BE3F6E60B846255AF672975E04F62AC8B3BDCBB040A15321CF6C3EC218031EA0`.
- Link inventory: 238 annotations on pages `[(1, 41), (2, 39), (3, 2), (4, 20), (5, 122), (7, 2), (8, 2), (9, 1), (10, 2), (11, 1), (13, 1), (19, 1), (20, 1), (23, 2), (26, 1)]`; green = 218, red = 20, cyan = 0; all borders `(0, 0, 1)`.
- Oversized annotation audit: 0 malformed page-edge rectangles.
- Rendered pages 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 19, 20, 23, and 26 after export and confirmed crisp green citation/URL boxes and red internal-reference boxes.
- Local `paper/main.pdf` removed after the canonical copy.
- No additional `C:/Users/wangz/Downloads/4.pdf` duplicate was created.
