# Regina PR3 DMG review note — 2026-03-28

Purpose: anti-drift review note for the build/QA/reproducibility lane.

## Questions this lane must answer cleanly
1. Which delivery surfaces are actually generator-backed today?
2. Which outputs are generated artifacts versus source-of-truth inputs?
3. Which later public/package claims depend on assets that are not yet first-class in repo state?
4. Which missing scripts or QA artifacts block safe promotion of shipped map/analyst assets?

## Current conclusion
- The public HTML render surface is generator-backed via `scripts/render_public_pages.py`.
- The CT Kepler diagnostic lane is generator-backed via `scripts/build_ct_kepler_dataset.py`.
- The broader public-scene / shipped-asset family is not yet fully first-class in current landed repo state.
- Therefore PR3 should focus on reproducibility contract + honest gap declaration, not fake completeness.

## Merge safety reading
Safe to merge if framed as:
- reproducibility/control hardening
- current-state contract
- explicit statement of missing build surfaces

Not safe to frame as:
- all delivery assets are now fully reproducible and release-ready
