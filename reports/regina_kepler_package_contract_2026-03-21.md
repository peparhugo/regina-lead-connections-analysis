# Regina Kepler Analyst Package Contract — 2026-03-21

Purpose: define the bounded analyst-facing package for the approved KeplerGL workbench.

This package is internal / analyst-facing only. It exists to support exploration, QA, comparison, and later scene design. It is **not** the public control plane and must not be treated as publishable truth by default.

Memory validation tools were unavailable in this runtime. This contract is conservative and based on approved Regina control files plus direct repo inspection.

---

## 1. Package role

### Analyst package is for
- inspecting the observed area lane
- comparing strict observed vs broad inferred area continuity
- opening CT estimated context with explicit caveats
- diagnosing geometry match types and allocation behavior
- preserving versioned reproducibility for internal review

### Analyst package is not for
- direct public embed
- claim promotion by screenshot alone
- hiding confidence distinctions
- validating GTLO / My Maps as a truth backbone

---

## 2. Recommended package location

Recommended versioned package root:
- `analyst/kepler/2026-03-21/`

Recommended contents:
- `README.md`
- `manifest.json`
- `kepler_config.json`
- `datasets/area_observed_2019_2025.geojson`
- `datasets/area_inferred_broad.geojson`
- `datasets/ct_estimated_context.geojson`
- `FIELD_DICTIONARY.md`
- `QA_NOTES.md`

If the repo owner prefers `reports/` for interim storage, keep a mirror there during transition, but the package should converge on one analyst-specific directory so it does not blur with public reports.

---

## 3. Required versioned inputs

## A. Observed area dataset
Purpose: analyst reference for the public-safe backbone.

Preferred dataset id:
- `area_observed_2019_2025`

Required source inputs:
- area geometry / OpenGIS backbone export
- `data/derived/strict_replacements_by_area.csv`
- `data/derived/strict_replacements_by_area_month.csv`

Required fields:
- `area_name`
- `lead_connections_total`
- `water_connections_total`
- `lead_share_pct`
- `observed_replacements_2019_2025`
- `confidence_class` = `observed`

## B. Inferred broad area dataset
Purpose: support-only continuity comparison.

Preferred dataset id:
- `area_inferred_broad`

Required source inputs:
- area geometry / OpenGIS backbone export
- `data/derived/inferred_replacements_by_area.csv`
- `data/derived/inferred_replacements_meta.json`

Required fields:
- `area_name`
- `inferred_replacements_broad`
- `confidence_class` = `inferred`
- `method_note`
- `meta_generated_at`

Mandatory note text must preserve that this is inferred analytics, not an official city replacement-event ledger.

## C. Estimated CT context dataset
Purpose: analyst-only tract exploration and future caveated scene prep.

Preferred dataset id:
- `ct_estimated_context`

Required source inputs:
- `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- optionally cross-checked against `data/derived/ct_equity_panel_official_2026-03-06_regina.csv`

Required fields observed in current repo inputs:
- `ct_uid_code`
- `ct_dguid`
- `geometry_match_type`
- `active_lead_count`
- `replaced_since_2019`
- `replacement_rate`
- `impacted_people_est`
- `impacted_children_0_14_est`
- `tenure_renter_pct`
- `median_after_tax_income_households`
- `lim_at_prevalence_pct`
- `unemployment_rate_pct`
- `children_0_14_pct`
- `confidence_class` = `estimated`
- `notes`

Mandatory note text must preserve that tract replacement values are estimated allocations derived from area-level source data, not direct observed tract replacement counts.

---

## 4. Manifest contract

`manifest.json` should include:
- `package_name`
- `package_version`
- `generated_at`
- `kepler_config_file`
- `datasets`
- `source_files`
- `confidence_taxonomy`
- `restrictions`
- `warnings`

### Required warnings
- analyst package contains support-only and estimated layers
- package is not a public approval artifact by itself
- 2026 promoted counts are excluded unless separately versioned as provisional internal-only material
- unsupported layers must not be exported as public-ready views

---

## 5. Kepler config rules

`kepler_config.json` must:
1. default the analyst session to the observed area dataset first;
2. keep inferred broad and CT estimated datasets available but not confused with observed truth;
3. include tooltip fields that surface confidence and method notes clearly;
4. avoid any default state that centers impacted-children numerics as the main story;
5. exclude GTLO/My Maps as a validation layer.

### Recommended default layer order
1. `area_observed_2019_2025`
2. `area_inferred_broad`
3. `ct_estimated_context`

### Recommended default visibility
- observed area: on
- inferred broad: off
- CT estimated: off

This keeps the analyst package aligned with the public-first confidence hierarchy while still enabling internal exploration.

---

## 6. Field dictionary contract

`FIELD_DICTIONARY.md` must define for each exposed field:
- field name
- source file
- geography
- confidence class
- human meaning
- approved use
- forbidden use

At minimum, dictionary entries are required for:
- `observed_replacements_2019_2025`
- `inferred_replacements_broad`
- `replacement_rate`
- `active_lead_count`
- `impacted_people_est`
- `impacted_children_0_14_est`
- `geometry_match_type`

---

## 7. Versioning rules

1. Every analyst package must be date-versioned.
2. Config and datasets must move together under one package version.
3. If CT estimated inputs change, the package version must increment even if the observed public dataset is unchanged.
4. If 2026 provisional material is ever included later, it must be placed in a separate dataset clearly marked `provisional` and excluded from default visibility.

---

## 8. Acceptance checks

The Kepler analyst package passes its contract only if:
1. all included datasets are labeled `observed`, `inferred`, or `estimated` explicitly;
2. observed, inferred, and estimated datasets remain separate instead of being merged into one confidence-neutral file;
3. default visibility starts with observed area data only;
4. CT fields retain allocation caveats;
5. GTLO / My Maps is absent as a validation layer;
6. public-safe Scene 1 can be derived without depending on analyst-only fields.

---

## 9. Deferred from the analyst package MVP

Deferred items:
- unsupported / blocked dataset shipping in the first analyst package version
- 2026 provisional surface
- DA proxy review tab
- burden / QALY appendix overlays
- automated publication/export workflows

These can be added only after the public MVP and analyst package baseline both stabilize.
