# Regina MVP Release Checklist — 2026-03-22

Status: release-traceability artifact for the bounded Regina MVP

## PR / gate mapping

### PR1 — Scene 1 data contract + generated assets + QA
Artifacts:
- `scripts/build_public_scene1_dataset.py`
- `scripts/qa_public_scene1_dataset.py`
- `public/data/scene1_observed_area_replacements_2019_2025.geojson`
- `public/data/scene1_observed_area_replacements_2019_2025.meta.json`
- `reports/regina_public_scene1_join_qa_2026-03-21.json`
- `reports/regina_public_scene1_dataset_qa_2026-03-21.json`

Gate mapping:
- `G5-A` — PASS

### PR2 — Public app shell
Artifacts:
- `public/map/index.html`
- `public/map/app.css`
- `public/map/app.js`
- `public/map/config/scene-registry.json`
- `public/map/config/legend-copy.json`
- controlled entry points in `index.html` and `reports/regina_public_bundle_2026-03-16.html`

Gate mapping:
- `G5-B` — PASS_WITH_LIMITS moving to repaired-ready
- `G5-C` — PASS

### PR3 — Analyst package baseline
Artifacts:
- `analyst/kepler/2026-03-21/README.md`
- `analyst/kepler/2026-03-21/manifest.json`
- `analyst/kepler/2026-03-21/kepler_config.json`
- `analyst/kepler/2026-03-21/FIELD_DICTIONARY.md`
- `analyst/kepler/2026-03-21/QA_NOTES.md`
- `analyst/kepler/2026-03-21/datasets/*`

Gate mapping:
- `G5-D` — PASS

### PR4 — Hardening / docs / release cleanup
Artifacts:
- `README.md`
- `reports/regina_mvp_release_checklist_2026-03-22.md`
- `reports/regina_mvp_hardening_synthesis_2026-03-22.md`
- `reports/regina_operator_release_note_2026-03-23.md`
- bounded repair changes from the hardening swarm

Gate mapping:
- `G5-E` — PASS_WITH_LIMITS (release/operator note added; branch/PR hygiene still separate from content readiness)

## What ships publicly
- root narrative landing page
- Scene 1 observed area map
- observed area data payload + metadata

## What does not ship publicly in the MVP default
- promoted 2026 counts
- CT estimated default layer
- unsupported/proxy layers
- GTLO/My Maps validation framing
- public impacted-children numeric claims
