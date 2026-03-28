# Regina Operator Release Note — 2026-03-23

Status: canonical operator-facing release note for the bounded Regina MVP

## Purpose
This file is the short deploy/use note for the current Regina public package. It is meant to remove ambiguity between:
- the public narrative homepage,
- the public Scene 1 map,
- the analyst-only package,
- and deferred/non-public layers.

## Canonical public entry points
- Homepage / narrative landing page: `index.html`
- Public MVP map: `public/map/index.html`
- Public Scene 1 dataset: `public/data/scene1_observed_area_replacements_2019_2025.geojson`
- Public Scene 1 metadata: `public/data/scene1_observed_area_replacements_2019_2025.meta.json`

## What ships publicly
These are in-scope for the current public MVP:
- `index.html`
- `styles.css`
- `public/map/index.html`
- `public/map/app.css`
- `public/map/app.js`
- `public/map/config/scene-registry.json`
- `public/map/config/legend-copy.json`
- `public/data/scene1_observed_area_replacements_2019_2025.geojson`
- `public/data/scene1_observed_area_replacements_2019_2025.meta.json`
- controlled public reading artifacts linked from the homepage, including:
  - `reports/public-brief.html`
  - `reports/public-handout.html`
  - `reports/journalist-memo.html`
  - `reports/claim-evidence.html`
  - `reports/delivery-tracker.html`
  - `reports/technical-appendix.html`

## Analyst / internal only
These are not public-truth entry points and should not be promoted as the public MVP:
- `analyst/kepler/2026-03-21/`
- analyst manifests, field dictionaries, QA notes, and internal datasets under that directory
- internal gate/control docs in `reports/` that exist for planning, QA, or release discipline rather than public consumption

## Deferred / not part of the public MVP default
Do not promote these as part of the shipped public MVP unless separately approved:
- 2026 public counts
- CT estimated default public layers
- unsupported or proxy-first layers
- GTLO / Google My Maps as validation authority
- public impacted-children numeric promotion
- any endpoint-specific burden framing outside the support-layer restrictions already documented in package-gate files

## Current public posture
The public MVP is intentionally conservative:
- observed area replacements only
- 2019–2025 only
- story-first homepage plus bounded interactive map
- analyst package kept separate from the public runtime

## Validation references
Use these files when checking release readiness:
- `reports/regina_mvp_release_checklist_2026-03-22.md`
- `reports/regina_release_docs_hardening_2026-03-22.md`
- `reports/regina_public_scene1_dataset_qa_2026-03-21.json`
- `reports/regina_public_scene1_join_qa_2026-03-21.json`
- `reports/regina_package_gate_status_2026-03-16.md`

## Static hosting assumptions
- Root path should expose `index.html` as the story-first landing surface.
- `public/map/index.html` should remain directly reachable as the interactive Scene 1 surface.
- Public data assets under `public/data/` must remain adjacent to the map app’s relative-path assumptions.
- Analyst package paths are retained in-repo for internal/analyst use and should not be treated as public release navigation.

## Quick operator checklist
1. Confirm `index.html` loads.
2. Confirm `public/map/index.html` loads.
3. Confirm `public/data/scene1_observed_area_replacements_2019_2025.geojson` is present.
4. Confirm the public map remains bounded to observed area replacements for 2019–2025.
5. Confirm no analyst-only or deferred layers are being presented as public default truth.

## Bottom line
If you need the simplest release rule:
- publish the homepage and Scene 1 map,
- keep the analyst package separate,
- keep the MVP observed-only and 2019–2025 bounded,
- and do not widen the public claim envelope from this repo state without a fresh approval pass.
