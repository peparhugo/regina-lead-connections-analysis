# Regina recovery lane note — 2026-03-28

Purpose: document the recovery of previously hidden but legitimate project surfaces from stash into explicit repo review.

## What this recovery lane covers
- shipped public map assets
- analyst package assets
- build / QA / orchestration scripts
- release/readiness docs that those assets depend on

## What this lane does not cover
- raw shapefile backlog
- cache files
- stale or prototype derived outputs without a clear repo role
- broad report/archive backlog

## Why this lane exists
These files were not fake ideas or external references; they were real project surfaces trapped in stash.
Recovery turns them from hidden residual work into reviewable repo state.

## Guardrail
Recovery is not the same as promotion.
Anything restored here should still be judged by:
- reproducibility
- release readiness
- current claim/control envelope
- repo weight / artifact-role discipline
