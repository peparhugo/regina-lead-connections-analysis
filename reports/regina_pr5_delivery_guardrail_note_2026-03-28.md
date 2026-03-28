# Regina PR5 delivery guardrail note — 2026-03-28

Purpose: keep the public-package content lane merge-safe while PR4 shipped assets remain missing from current repo reality.

## Rule applied
Content in PR5 must not imply that shipped map assets currently exist in repo reality if PR4 has not yet restored or regenerated them.

## Current adjustment
The public package content was allowed to advance, but live links to the missing observed-area map asset were temporarily neutralized.

Affected surfaces:
- `index.html`
- `reports/regina_public_bundle_2026-03-16.html`

## Re-enable condition
Restore or regenerate PR4 shipped assets first, then re-enable direct map links in a later delivery asset follow-on.

## Why this matters
This preserves the phase order honestly:
- PR3 = reproducibility/build contract
- PR4 = shipped assets restore/regeneration
- PR5 = public package/content

Since PR4 is currently incomplete, PR5 must not overstate current delivery reality.
