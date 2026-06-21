# Paper04 VLA Highlight Hardening Plan

Date: 2026-06-21

## Objective

Make `C:/Users/wangz/Downloads/04.pdf` explicitly match the visible VLA-v4
role model's boxed-link behavior while preserving the final 28-page affordance
conservation paper:

- citation links use green one-point boxes;
- internal figure/table/equation/section links use red one-point boxes;
- URL links use green one-point boxes;
- no cyan link boxes appear;
- the final PDF is rebuilt, copied to Downloads, visually checked, and leaves
  no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/04.pdf`
- Pages: 28
- Size: 1,136,853 bytes
- SHA256: `2CB63C8BCBC29AD4B60B630D2D19C6E9E263F87C7915959FC219172F8F33EB0E`
- Local `paper/main.pdf`: absent
- Repository branch: `master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[(1, 44), (2, 41), (3, 2), (4, 20), (5, 122), (7, 2), (8, 2), (9, 1), (10, 2), (11, 1), (13, 1), (19, 1), (20, 1), (23, 2), (26, 1)]`
- Annotation colors: green = 223, red = 20, cyan = 0
- Border widths: `(0, 0, 1)` for all link annotations

Source finding:

- `paper/main.tex` is the active manuscript source.
- The active manuscript already loads `hyperref`, and the baseline PDF already
  has green citation/URL boxes and red internal-reference boxes.
- The source does not explicitly pin the VLA-v4 `\hypersetup` policy, so this
  pass will make the matching behavior explicit and auditable.
- Use the documented manual LaTeX flow from `paper/`: `pdflatex`, `bibtex`,
  and repeated `pdflatex` passes before export.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\hypersetup` block in the active `paper/main.tex` preamble
   immediately after the existing `\usepackage{hyperref}`.
2. Rebuild manually from `paper/` with `pdflatex`, `bibtex`, and repeated
   `pdflatex` passes.
3. If the log asks for another pass for cross-references, run the final
   canonical pass before recording metadata.
4. Copy the rebuilt `paper/main.pdf` to `C:/Users/wangz/Downloads/04.pdf`.
5. Remove local `paper/main.pdf` after export.
6. Recompute page count, byte size, SHA256, annotation colors, border widths,
   and link pages from the final Downloads PDF.
7. Render every page that contains final link annotations into
   `tmp/pdfs/paper04_after`.
8. Visually inspect rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
9. Update README/status/audit/version/validation metadata with the new hash and
   VLA-style boxed-link inventory.
10. Validate build logs, diff hygiene, final PDF hash, expected claim markers,
    and absence of local `paper/main.pdf`.
11. Remove Paper04 temp renders, leaving only the shared role-model render
    directory.
12. Stage only Paper04 source and metadata files, commit, push, and verify a
    clean repository before moving to Paper03.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations, references, URLs, or template examples merely
  to change link counts.
- Do not create an additional `4.pdf`; keep the repository's canonical
  Downloads target as `04.pdf`.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Added the explicit VLA `\hypersetup` block immediately after the existing
  `\usepackage{hyperref}` in active `paper/main.tex`.
- Split one page-crossing citation cluster so link rectangles remain local; no
  citation keys were added or removed.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Exported canonical PDF: `C:/Users/wangz/Downloads/04.pdf`
- Pages: 28
- Size: 1,135,968 bytes
- SHA256: `BE3F6E60B846255AF672975E04F62AC8B3BDCBB040A15321CF6C3EC218031EA0`
- Link inventory: 238 annotations on pages `[(1, 41), (2, 39), (3, 2), (4, 20), (5, 122), (7, 2), (8, 2), (9, 1), (10, 2), (11, 1), (13, 1), (19, 1), (20, 1), (23, 2), (26, 1)]`; green = 218, red = 20, cyan = 0; all borders `(0, 0, 1)`.
- Oversized annotation audit: 0 malformed page-edge rectangles.
- Visual audit: rendered pages 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 19, 20, 23, and 26; green citation/URL boxes and red internal-reference boxes are crisp and aligned.
- Local `paper/main.pdf`: removed after export.
- Duplicate `C:/Users/wangz/Downloads/4.pdf`: not created.
