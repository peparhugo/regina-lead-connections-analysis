# Kepler Phase A Quickstart (CT diagnostics)

## Ready dataset
- GeoJSON: `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- CSV (attributes): `data/derived/ct_factor_diagnostics_kepler_2026-03-06.csv`
- CT geometry join coverage: **49 / 54 CTs (90.74%)**

## Core fields
- `active_lead_count`
- `replaced_since_2019`
- `replacement_rate`
- `impacted_people_est`
- `impacted_children_0_14_est`
- socioeconomic factors (`tenure_renter_pct`, `lim_at_prevalence_pct`, `unemployment_rate_pct`, `children_0_14_pct`, etc.)

## Kepler setup
1. Open `https://kepler.gl/demo`
2. Drag/drop the GeoJSON file above.
3. Configure layers:
   - Polygon fill by `replacement_rate`
   - Tooltip: active/replaced/impacted fields + key socioeconomic factors
   - Secondary view: color by `lim_at_prevalence_pct` or `tenure_renter_pct`
4. Save map config JSON and commit under `reports/kepler_config_phase_a_2026-03-06.json`.

## Caveats to display in map subtitle
- Replaced counts are constrained to 2019+ monthly series.
- Active counts are city-baseline-normalized allocations to CT.
- Impacts are ecological proxies (not audited household-level counts).
