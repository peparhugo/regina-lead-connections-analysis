# Interim Public Update — Regina Lead Research (Preliminary)

**Status:** In progress (Phase 2)  
**Date:** 2026-03-06

## What we have completed so far
- Built a reproducible research scaffold (plan, assumptions, reproducibility checklist, and phase runner).
- Ingested a first-pass multi-source literature seed and produced triage/curation artifacts.
- Generated initial inferred GIS replacement analytics from available internal/snapshot data.

## What we are using right now
### Evidence artifacts
- `data/raw/evidence_seed_2026-03-06.json`
- `reports/evidence_registry_seed_2026-03-06.csv`
- `reports/evidence_registry_curated_2026-03-06.csv`
- `reports/effect_size_normalized_2026-03-06.csv`

### GIS-related artifacts (preliminary)
- `data/derived/inferred_replacements_by_area.csv`
- `data/derived/inferred_replacements_by_area_month.csv`
- `data/derived/inferred_replacements_detailed.csv`
- `data/derived/inferred_replacements_meta.json`

## Important caveats (read first)
1. **This is preliminary.** Current findings are not final policy-grade estimates.
2. **GIS replacement data is inferred**, not an official replacement-event ledger.
3. Key official GIS inputs are still pending (e.g., lead service line inventory, water sampling layers, and finalized spatial joins).
4. Effect-size extraction is currently based mostly on title/abstract-level evidence and needs full-text validation for decision-grade use.

## What we can responsibly say today
- We have an operational, reproducible pipeline and early evidence inventory.
- We have identified candidate signals and built a structured queue for deeper extraction.
- We are actively moving from scaffold + inference toward validated inputs and stronger estimates.

## What we are doing next (already in motion)
1. Upgrade evidence extraction quality (prioritize stronger Tier A/B studies and extract effect sizes with confidence metadata).
2. Complete validated GIS input acquisition and joins.
3. Build outcome-to-cost bridge and populate NPV model with verified assumptions.

## Publication posture
This update is intended as a **transparency checkpoint** while research continues. It should not be interpreted as a final estimate of health or economic impact.
