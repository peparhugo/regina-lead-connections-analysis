# Regina Public Scene 1 Data Contract — 2026-03-21

Purpose: define the exact public MVP data contract for **Scene 1: observed area replacements, 2019–2025 only**.

This contract is intentionally narrow. It is the public-safe first scene for the MapLibre + deck.gl app and must not absorb CT estimates, 2026 continuation data, DA proxies, GTLO cross-reference logic, or burden numerics.

Memory validation tools were unavailable in this runtime. This contract is therefore conservative and grounded in the approved Regina control files plus direct repo inspection.

---

## 1. Scene boundary

### In scope
- geography: **area / LeadConnectionArea-native backbone**
- time window: **2019-01-01 through 2025-12-31 only**
- confidence class: **`observed`**
- public purpose: show observed program progress on the strongest safe geography

### Out of scope
- any 2026 counts or slider positions
- any CT allocation values
- any DA/proxy geometry
- any impacted-people or impacted-children numerics
- inferred broad continuity totals as primary display values
- GTLO / Google My Maps cross-reference fields

---

## 2. Source-of-truth inputs

## Required source files
1. Area geometry / backbone source
   - source family: Regina OpenGIS `LeadConnectionAreas`
   - required baseline fields named in current Regina artifacts:
     - `NAME`
     - `WC_Total`
     - `Lead_Total`
     - `Lead_Per`

2. Observed replacement totals by area
   - `data/derived/strict_replacements_by_area.csv`
   - current header:
     - `area`
     - `count`

3. Observed replacement monthly series for gating / window checks
   - `data/derived/strict_replacements_by_area_month.csv`
   - current header:
     - `area`
     - `month`
     - `count`

## Optional non-runtime support file
- `reports/regina_layer_spec_v1_2026-03-21.md`
  - used for copy/legend rules, not map rendering data

---

## 3. Required build output

Recommended generated artifact:
- `public/data/scene1_observed_area_replacements_2019_2025.geojson`

Recommended metadata sidecar:
- `public/data/scene1_observed_area_replacements_2019_2025.meta.json`

If the implementation chooses JSON instead of GeoJSON for tabular side data, the geometry-bearing artifact must still remain the canonical public scene payload.

---

## 4. Canonical output schema

Each feature in `scene1_observed_area_replacements_2019_2025.geojson` must contain these properties.

### Identity / provenance
- `scene_id` — fixed string: `scene1_observed_area_replacements_2019_2025`
- `layer_id` — fixed string: `obs_area_replacements_2019_2025`
- `confidence_class` — fixed string: `observed`
- `geography_type` — fixed string: `area`
- `source_version_date` — build date or pinned source snapshot date
- `time_window_start` — fixed string: `2019-01-01`
- `time_window_end` — fixed string: `2025-12-31`

### Area identifiers / labels
- `area_name` — from backbone `NAME`
- `area_slug` — normalized stable slug for UI state / URL fragments

### Backbone values
- `water_connections_total` — from `WC_Total`
- `lead_connections_total` — from `Lead_Total`
- `lead_share_pct` — from `Lead_Per`

### Observed replacement values
- `observed_replacements_2019_2025` — integer, joined from `strict_replacements_by_area.csv` after enforcing 2019–2025 window logic
- `observed_replacement_share_of_lead` — numeric ratio = `observed_replacements_2019_2025 / lead_connections_total`, nullable if denominator missing or zero

### UI / copy helper fields
- `tooltip_title` — recommended: area name
- `tooltip_subtitle` — fixed copy equivalent to `Observed area replacements, 2019–2025`
- `confidence_note` — fixed copy equivalent to `Observed area replacements from the area/month source backbone.`

### Forbidden public fields in Scene 1 payload
Do **not** include:
- CT IDs or CT metrics
- DA/proxy IDs
- `impacted_people_est`
- `impacted_children_0_14_est`
- inferred broad counts
- provisional 2026 counts
- unsupported validation notes tied to GTLO

---

## 5. Join rules

1. Join key is area name from backbone `NAME` to CSV field `area`.
2. Join must be exact after deterministic normalization only.
3. Build must fail closed if any area in the replacement CSV does not resolve to exactly one public area geometry.
4. Build must emit a join QA report with:
   - matched area count
   - unmatched area names
   - duplicate matches
   - total observed replacements in output
5. Output totals must reflect **2019–2025 only**.

---

## 6. Time-window enforcement rules

1. `strict_replacements_by_area_month.csv` is the enforcement file for the promoted window.
2. Public Scene 1 totals must exclude rows earlier than `2019-01`.
3. Public Scene 1 totals must exclude rows later than `2025-12`.
4. If `strict_replacements_by_area.csv` is used as a convenience source, implementation must still validate that its totals match the 2019–2025 aggregation logic or explicitly document the discrepancy.
5. Any unresolved mismatch blocks Scene 1 release until reconciled.

---

## 7. Metadata sidecar schema

`scene1_observed_area_replacements_2019_2025.meta.json` should include:
- `scene_id`
- `layer_id`
- `confidence_class`
- `time_window`
- `source_files`
- `build_script`
- `generated_at`
- `feature_count`
- `sum_observed_replacements_2019_2025`
- `join_validation`
- `notes`

Recommended note text should state materially:
- Scene 1 is area-native and observed.
- This file does not encode tract-level replacement truth.
- 2026 is intentionally excluded.

---

## 8. Public map behavior contract

Scene 1 runtime behavior must enforce:
- Scene 1 loads by default.
- Legend shows `observed` as the active confidence class.
- No unsupported toggles appear.
- Tooltip first line shows the confidence badge.
- Side panel copy states that this is the strongest direct replacement map surface currently approved.

---

## 9. Acceptance checks for this contract

Scene 1 data contract passes only if:
1. the output is area geography only;
2. the time window is bounded to 2019–2025;
3. feature totals reconcile to the approved observed window logic;
4. the payload excludes CT/proxy/impact fields;
5. the output clearly self-identifies as `observed`.

---

## 10. Deferrals

Explicitly deferred from this contract:
- Scene 2 CT estimated context contract
- any public time slider beyond 2019–2025
- public multi-scene orchestration beyond a single observed-first experience
- analyst-specific diagnostic fields
- impacted-population overlays
- 2026 continuation display
