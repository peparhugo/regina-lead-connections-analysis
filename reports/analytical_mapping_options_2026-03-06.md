# Analytical Mapping Options Review (Regina Lead, publication-ready)

## Goal
Publish an impressive, analysis-forward GIS experience that supports:
1) tract-level factor exploration,
2) 2019+ replacement progress storytelling,
3) reproducible methods.

## Options reviewed

### 1) Kepler.gl (recommended for rapid wow-factor)
- Strengths:
  - fast, high-performance WebGL exploration
  - built on deck.gl + MapLibre stack
  - excellent for interactive filtering, brushing, and thematic layers
- Weaknesses:
  - less control over narrative UX unless embedded/customized
  - config/state management can get messy if not versioned
- Best use here:
  - publish an interactive exploratory companion with CT metrics, replacement intensity, and socioeconomic overlays.

### 2) deck.gl + MapLibre custom app (recommended for final flagship)
- Strengths:
  - maximum control on interactions, tooltips, animation, and branding
  - strongest for bespoke analytical storytelling and future extensibility
- Weaknesses:
  - more engineering effort than Kepler.gl
- Best use here:
  - final "city dashboard" with scenario toggles and significance overlays.

### 3) MapLibre + plugin stack (story map oriented)
- Strengths:
  - easy to add compare slider, temporal controls, export, legends
  - good balance between control and speed
- Weaknesses:
  - advanced heavy analytics need extra custom coding
- Best use here:
  - production public report map with 2-3 polished views.

## Recommended path (phased)

### Phase A (fast, 1-2 days)
- Kepler.gl exploratory map package:
  - CT layer with normalized 2019+ active/replaced values
  - socioeconomic choropleth selector
  - trend filter for high-replacement tracts
- Output: embedded Kepler scene link/config in report page.

### Phase B (next, 3-5 days)
- deck.gl + MapLibre flagship view:
  - dual-mode map: `Program Progress` and `Factor Diagnostics`
  - tract tooltip with active/replaced/children proxy + key covariates
  - significance legend and caveat panel

## Data products needed for Phase A/B
- `ct_equity_panel_official_2026-03-06_regina.csv` (already present)
- CT boundary geometry (StatsCan CT boundary file / WKT/GeoJSON)
- Optional: year-by-year replacements by area/tract for temporal animation

## Recommendation
- Start with Kepler.gl now to get immediate high-impact visual publishing.
- In parallel, prepare deck.gl/MapLibre architecture for durable final product.
