# StatsCan Census Polygon Expansion Plan — 2026-03-06

## Goal
Expand the Regina lead analysis from community-area aggregation into census-anchored polygons to support stronger neighborhood narrative and reproducible socioeconomic overlays.

## Polygon levels (priority order)
1. **Dissemination Area (DA)** — smallest broadly usable census unit for demographic/socioeconomic storytelling.
2. **Census Tract (CT)** — stable reporting layer for public communication and trend framing.
3. (Optional) **Dissemination Block (DB)** for geometry-only micro-spatial checks where available; avoid over-interpretation due to high noise/sparsity.

## Planned data pulls
- StatsCan boundary files (cartographic boundary file, latest census vintage) for DA + CT.
- Target geographies for Regina city context (CSD/CMA-aligned subset where applicable).
- Join keys prepared for enrichment tables (population age bands, household indicators, housing-era proxies where available).

## Integration path
1. Fetch and stage DA/CT polygons into `data/raw/statscan/`.
2. Normalize CRS + simplify for web map performance.
3. Build crosswalk from current lead-community areas to DA/CT overlays.
4. Generate derived artifacts under `data/derived/`:
   - `regina_da_overlay_summary.csv`
   - `regina_ct_overlay_summary.csv`
5. Publish methods + caveats before any public claim.

## Caveats
- Ecological fallacy risk: area-level overlays are not individual-level causal evidence.
- Boundary mismatch between municipal service zones and census units must be explicitly documented.
- DA-level narrative is useful for context, not deterministic attribution.
