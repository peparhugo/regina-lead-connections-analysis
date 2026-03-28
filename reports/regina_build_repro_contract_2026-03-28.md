# Regina build / reproducibility contract — 2026-03-28

Status: active PR3 contract
Purpose: define the minimum reproducibility layer required before shipping public map assets, analyst assets, or public-package copy that depends on them.

## Core rule
No Regina delivery artifact should be treated as stable if it cannot be traced to:
1. an input surface
2. a generating script or explicit manual build step
3. a QA / acceptance artifact
4. a release/readiness note

## Covered surfaces
### Public package render surface
- `index.html`
- `reports/public-brief.html`
- `reports/public-handout.html`
- `reports/journalist-memo.html`
- `reports/technical-appendix.html`

Generator path:
- `scripts/render_public_pages.py`

Source markdowns:
- `reports/regina_public_brief_plain_language_2026-03-12.md`
- `reports/regina_public_handout_2026-03-16.md`
- `reports/regina_journalist_memo_2026-03-16.md`
- `reports/regina_health_burden_technical_appendix_2026-03-16.md`

### Analyst / CT Kepler diagnostic surface
Current script:
- `scripts/build_ct_kepler_dataset.py`

Current outputs:
- `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- `data/derived/ct_factor_diagnostics_kepler_2026-03-06.csv`
- `reports/ct_geometry_crosswalk_2026-03-06.csv`

Current supporting docs:
- `reports/kepler_phase_a_quickstart_2026-03-06.md`
- `reports/kepler_config_phase_a_2026-03-06.json`

### Equity reproducibility surface
Current reproducibility note:
- `reports/reproducibility_appendix_equity_2026-03-06.md`

Expected supporting script family:
- `scripts/build_equity_panel_and_tests.py` when present / restored
- related provenance/data-generation helpers when present / restored

## Acceptance gates for PR3
### Gate R1 — traceability
Each shipped or referenced delivery artifact must point to a generator or an explicit manual-build note.

### Gate R2 — QA visibility
Each generator-backed surface must have either:
- a QA artifact
- or an explicit note saying QA is pending and the artifact is not yet release-grade

### Gate R3 — release boundary clarity
The repo must distinguish clearly between:
- generator scripts
- generated outputs
- release/readiness notes
- support-only or prototype outputs

### Gate R4 — no fake completeness
If a referenced asset family is not yet first-class in the repo, public/package copy must not imply it is already fully shipped.

## Practical operator rule
PR3 may land the reproducibility contract even if every target generator is not yet restored, as long as:
- the current state is described honestly
- missing build steps are named
- later asset/package PRs are gated on those missing pieces

## Why this exists
The Regina repo currently spans:
- hand-authored narrative content
- generated HTML outputs
- data-derived analytical outputs
- possible future shipped map/analyst assets

Without a reproducibility contract, those surfaces drift apart and make later PR review unreliable.
