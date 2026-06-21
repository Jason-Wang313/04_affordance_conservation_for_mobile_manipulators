# Full-Scale CAQ Results Summary

The expanded suite is a synthetic mechanism study. It strengthens the CAQ claim only under the stated assumptions: known or accurate access gate, stable object/contact state, and available contact correspondence.

## Artifacts
- `results/full_scale/access_error_taxonomy.csv`
- `results/full_scale/correspondence_stress.csv`
- `results/full_scale/geometry_sensitivity.csv`
- `results/full_scale/leaderboard.csv`
- `results/full_scale/main_shift_metrics.csv`
- `results/full_scale/negative_controls.csv`
- `results/full_scale/residual_diagnostics.csv`
- `results/full_scale/support_burden.csv`

## Scale
- Seed scale: `20`.
- Compact metric rows: `7040`.
- Evaluated test predictions, counting model/suite evaluations: `10844000`.

## Main Readout
- Best medium-shift Brier model: `oracle_intrinsic` with mean Brier `0.0293`.
- Best medium-shift AUC model: `oracle_intrinsic` with mean AUC `0.8881`.
- Medium-shift CAQ Brier: `0.0294` (SEM `0.0005`).
- Medium-shift interaction-logistic Brier: `0.0323`.
- Medium-shift context-table Brier: `0.1009`.
- Oracle-intrinsic Brier reference: `0.0293`.

## Access-Gate Stress
- Correct-gate CAQ Brier in taxonomy suite: `0.0282`.
- Symmetric 20% gate error CAQ Brier: `0.0726`.
- False-access-only 20% error CAQ Brier: `0.0699`.
- False-blocked-only 20% error CAQ Brier: `0.0362`.

## Support Burden
- At 160 training samples and 8 context bins, CAQ Brier is `0.0285` versus context table `0.0967`.
- At 2560 training samples and 8 context bins, CAQ Brier is `0.0283` versus context table `0.0873`.

## Negative Control
- CAQ Brier rises from `0.0284` at conservation strength 0 violation to `0.0519` at violation strength 1.
- Interaction logistic Brier at violation strength 1 is `0.0343`.

## Figures
- `paper/figures/main_brier_leaderboard.png`
- `paper/figures/main_calibration_leaderboard.png`
- `paper/figures/calibration_scatter.png`
- `paper/figures/access_error_taxonomy.png`
- `paper/figures/support_burden.png`
- `paper/figures/correspondence_stress.png`
- `paper/figures/residual_detection.png`
- `paper/figures/geometry_sensitivity_heatmap.png`
- `paper/figures/negative_control.png`

## Final PDF Verification

- Canonical PDF: `C:/Users/wangz/Downloads/04.pdf`
- Pages: 28
- Size: 1,135,968 bytes
- SHA256: `BE3F6E60B846255AF672975E04F62AC8B3BDCBB040A15321CF6C3EC218031EA0`
- VLA-style boxed-link audit: 238 annotations on pages `[(1, 41), (2, 39), (3, 2), (4, 20), (5, 122), (7, 2), (8, 2), (9, 1), (10, 2), (11, 1), (13, 1), (19, 1), (20, 1), (23, 2), (26, 1)]`; green = 218, red = 20, cyan = 0; all borders `(0, 0, 1)`.
- Oversized annotation audit: 0 malformed page-edge rectangles.
- Visual audit: rendered pages 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 19, 20, 23, and 26; boxes are crisp and aligned.
