# Regina Kepler Analyst Package — 2026-03-21

This is the bounded analyst-facing Kepler package baseline for Regina.

## Included datasets
- `datasets/area_observed_2019_2025.geojson` — observed area replacements, public-safe backbone
- `datasets/area_inferred_broad.geojson` — inferred broad continuity comparison
- `datasets/ct_estimated_context.geojson` — estimated CT allocation context

## Use rules
- Start with `area_observed_2019_2025` first.
- Treat `area_inferred_broad` as inferred analytics, not a direct event ledger.
- Treat `ct_estimated_context` as allocation-based tract context, not direct tract replacement truth.
- Do not use this package alone as a public approval artifact.
- Do not treat GTLO / Google My Maps as a validation backbone.

## Exclusions
- No promoted 2026 counts
- No unsupported layers
- No DA proxy package in this baseline
