# Field Dictionary — Regina Kepler Analyst Package (2026-03-21)

## `observed_replacements_2019_2025`
- Source: `public/data/scene1_observed_area_replacements_2019_2025.geojson`
- Geography: area
- Confidence: `observed`
- Meaning: observed replacements in the promoted 2019–2025 window
- Approved use: public-safe backbone and analyst baseline
- Forbidden use: extending to 2026 or tract truth

## `inferred_replacements_broad`
- Source: `data/derived/inferred_replacements_by_area.csv`
- Geography: area
- Confidence: `inferred`
- Meaning: broad continuity estimate from record-comparison logic
- Approved use: analyst comparison only
- Forbidden use: claiming direct replacement-event truth

## `replacement_rate`
- Source: `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- Geography: census tract
- Confidence: `estimated`
- Meaning: allocation-based replacement rate proxy
- Approved use: analyst tract context
- Forbidden use: public direct tract replacement truth

## `active_lead_count`
- Source: `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- Geography: census tract
- Confidence: `estimated`
- Meaning: estimated active lead allocation for CT context
- Approved use: analyst context
- Forbidden use: direct tract inventory claim

## `impacted_people_est`
- Source: `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- Geography: census tract
- Confidence: `estimated`
- Meaning: proxy impacted people estimate
- Approved use: analyst/support-only context
- Forbidden use: promoted public numeric truth

## `impacted_children_0_14_est`
- Source: `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- Geography: census tract
- Confidence: `estimated`
- Meaning: proxy impacted children estimate
- Approved use: analyst/support-only context
- Forbidden use: promoted public numeric truth

## `geometry_match_type`
- Source: `data/derived/ct_factor_diagnostics_kepler_2026-03-06.geojson`
- Geography: census tract
- Confidence: `estimated`
- Meaning: match/allocation geometry note for the CT layer
- Approved use: analyst diagnostics and caveat inspection
- Forbidden use: hiding allocation limits
