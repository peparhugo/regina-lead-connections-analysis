# Regina PR4 asset gap note — 2026-03-28

Status: active execution note
Purpose: explain why the planned shipped-assets PR cannot be executed as a straightforward recovery from current repo state.

## Current truth
The planned PR4 lane was intended to land:
- `public/map/*`
- `public/data/*`
- `analyst/kepler/2026-03-21/*`

But in current live repo state:
- `public/` is not present on `main`
- `analyst/` is not present on `main`
- these paths are not available as tracked files in the active branch
- they are also not recoverable from the currently inspected stash slice used for the public-package lane

## What this means
PR4 cannot honestly proceed yet as “commit the existing shipped assets” because the expected asset surface is not actually present in current landed repo state.

## Correct reframing
PR4 is now an **asset restoration / regeneration task**, not a simple commit-slice task.

That means it should only proceed after one of these happens:
1. the missing shipped assets are recovered from a known source, or
2. the missing shipped assets are regenerated from accepted build scripts and source inputs, or
3. the project is explicitly re-scoped so those assets are not required for the current phase

## Operational consequence
The next executable lane after PR3 is therefore:
- PR5 public/package content, but only if content is edited so it does not reference missing asset families beyond current repo truth

Or alternatively:
- perform a dedicated recovery/regeneration pass to make PR4 real before PR5 lands

## Blunt operator rule
Do not merge content that implies shipped map/analyst assets exist if they do not currently exist in repo reality.
