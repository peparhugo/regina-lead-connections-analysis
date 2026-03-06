# StatsCan Data Availability Map — Regina Lead Equity Study

Date: 2026-03-06

This note maps what is currently available from StatsCan for the Regina lead-equity analysis and how it is used.

## 1) Discovery/catalogue layer
- Master data catalogue: https://www150.statcan.gc.ca/n1/en/type/data
- Use: discover candidate tables by topic (tenure, income, Indigenous identity, demographics) and geography support.
- Caveat: this is an index/discovery surface, not one machine-friendly endpoint for all values.

## 2) Census profile/tabular APIs (2016 scaffold already in repo)
- Geography list: `CR2016Geo.json`
- Geography profile data: `CPR2016.json`
- Existing script reference: `scripts/stats_can_data.py` (from prior Regina presentation scaffold)

Current known endpoints in use:
- https://www12.statcan.gc.ca/rest/census-recensement/CR2016Geo.json
- https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json

## 3) GIS boundary availability
- Census Tract boundary product catalogue: https://www150.statcan.gc.ca/n1/en/catalogue/92-168-X
- Includes links to 2021 and 2016 CT boundary files.
- Boundary types:
  - digital boundaries (full extents)
  - cartographic boundaries (generalized for display)

## 4) Candidate equity dimensions for this study
Target dimensions:
1. Tenure: owner vs renter
2. Income: median after-tax income and low-income metrics
3. Demographics: age mix, household structure (if needed for controls)
4. Indigenous: aggregate identity indicators only

## 5) Geography strategy
- Primary analysis target: CT and DA (official StatsCan geographies)
- Current interim artifact: DA/CT proxy panel from LeadConnectionAreas
- Upgrade path:
  1. Pull official CT/DA boundaries
  2. Pull matching census tabular variables
  3. Build official CT/DA panel
  4. Re-run significance + robustness tests

## 6) Artifact plan (next build)
- `data/derived/ct_equity_panel_official_<date>.csv`
- `data/derived/da_equity_panel_official_<date>.csv`
- `data/derived/equity_significance_results_official_<date>.csv`
- `reports/phd_equity_summary_<date>.html` (updated with official panel results)

## 7) Guardrails
- Do not claim causality from ecological cross-sectional patterns.
- Keep Indigenous analysis aggregate-only and suppression-aware.
- Keep city-reported replacement totals as official benchmark; GIS-derived counts are analytic estimates.
