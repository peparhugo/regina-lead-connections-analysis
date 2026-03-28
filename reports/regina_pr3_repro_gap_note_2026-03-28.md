# Regina PR3 reproducibility gap note — 2026-03-28

Status: explicit honesty note for PR3
Purpose: prevent the build/QA lane from pretending to be more complete than it is.

## Current reality
The repo already contains some reproducibility-critical pieces:
- `scripts/render_public_pages.py`
- `scripts/build_ct_kepler_dataset.py`
- `reports/kepler_phase_a_quickstart_2026-03-06.md`
- `reports/reproducibility_appendix_equity_2026-03-06.md`

But the larger desired delivery/build family is still incomplete in currently landed repo state.
Examples of expected-but-not-yet-first-class surfaces include:
- dedicated public scene build scripts
- dedicated public scene QA outputs
- complete analyst package build contract
- some release/readiness artifacts referenced by later package copy

## What PR3 should honestly do
PR3 should:
- define the reproducibility contract
- land the currently available generator/contract surfaces
- document the missing pieces clearly
- gate future asset/package PRs on those missing pieces

It should **not** pretend that all later delivery assets are already fully generator-backed if they are not.

## Why this matters
This repo is in a control-hardening phase.
Honest incompleteness is better than fake neatness.
