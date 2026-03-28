# Regina Kepler Package Hardening QA — 2026-03-22

Status: PASS

Scope audited:
- `analyst/kepler/2026-03-21/README.md`
- `analyst/kepler/2026-03-21/manifest.json`
- `analyst/kepler/2026-03-21/kepler_config.json`
- `analyst/kepler/2026-03-21/FIELD_DICTIONARY.md`
- `analyst/kepler/2026-03-21/QA_NOTES.md`
- `analyst/kepler/2026-03-21/datasets/*`

## Verdict
The analyst package is hardened correctly for analyst-only use. Confidence classes are cleanly separated, caveats are preserved across docs and data, GTLO/My Maps are explicitly excluded from any validation-backbone role, no substantive 2026 content drift was found, and the Kepler config defaults to an observed-first view.

## Findings by requirement

### 1) Confidence separation
PASS
- `manifest.json` declares dataset-level confidence classes:
  - `area_observed_2019_2025` → `observed`
  - `area_inferred_broad` → `inferred`
  - `ct_estimated_context` → `estimated`
- Dataset feature-level checks confirmed clean separation:
  - `area_observed_2019_2025.geojson` → 14/14 `observed`
  - `area_inferred_broad.geojson` → 14/14 `inferred`
  - `ct_estimated_context.geojson` → 54/54 `estimated`
- `FIELD_DICTIONARY.md` preserves per-field confidence language and forbidden-use boundaries.

### 2) Caveat preservation
PASS
Caveats are preserved in all key surfaces:
- `README.md`
  - observed-first instruction
  - inferred layer not a direct event ledger
  - CT layer not direct tract truth
  - not a public approval artifact by itself
- `manifest.json`
  - warnings and restrictions repeat analyst-only / estimated-context limits
- `FIELD_DICTIONARY.md`
  - forbidden uses explicitly documented for observed, inferred, and estimated fields
- `QA_NOTES.md`
  - repeats strongest-backbone and non-tract-truth caveats
- Dataset content
  - `area_inferred_broad.geojson` contains `method_note`: inferred continuity only, not direct replacement-event ledger
  - `ct_estimated_context.geojson` contains `notes` on every feature; 0 missing notes, 0 missing `geometry_match_type`

### 3) No GTLO / My Maps role
PASS
- `README.md`: “Do not treat GTLO / Google My Maps as a validation backbone.”
- `manifest.json`: “GTLO/My Maps excluded as validation backbone”
- No dataset file contained `GTLO`, `My Maps`, or `Google My Maps` references.

### 4) No 2026 drift
PASS with note
- No promoted 2026 count/window drift found.
- Observed package remains bounded to `2019-01-01` through `2025-12-31`.
- `README.md`, `manifest.json`, and `QA_NOTES.md` all explicitly state 2026 promoted counts are excluded.
- The only `2026` strings found in package contents were package/version metadata or source-generation references, e.g.:
  - package date/version (`2026-03-21`)
  - source/reference filenames such as `ct_factor_diagnostics_kepler_2026-03-06.geojson`
  - feature metadata timestamps like `source_version_date` / `meta_generated_at`
- These are provenance timestamps, not analytical-window drift.

### 5) Default observed-first config
PASS
- `kepler_config.json` visibility defaults:
  - `area_observed_2019_2025` → `isVisible: true`
  - `area_inferred_broad` → `isVisible: false`
  - `ct_estimated_context` → `isVisible: false`
- Tooltip configuration keeps the observed layer as the default visible promoted frame.

## Cross-file consistency
PASS
- Feature counts are internally consistent across `manifest.json`, `QA_NOTES.md`, and the dataset files:
  - observed areas: 14
  - inferred areas: 14
  - estimated CT features: 54
- Dataset IDs used in `kepler_config.json` match manifest dataset IDs.
- Documentation and dataset semantics align.

## Repair list
None.

## Final disposition
PASS
