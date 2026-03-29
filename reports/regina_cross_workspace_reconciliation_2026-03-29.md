tags: [regina:canonical, regina:recovery, regina:control, regina:workspace]
created_by: ChaosClaw
created_at: 2026-03-29T06:53:00+02:00

# Regina cross-workspace reconciliation — 2026-03-29

Status: canonical reconciliation note
Purpose: resolve the current Regina split-brain by explicitly identifying which workspace is deeper/canonical for which artifact classes and how the newer control layer should relate to it.

---

## Executive answer

### The deeper level is:
**`/root/.openclaw/workspace`**

That workspace is deeper because it contains:
- the larger historical Regina corpus
- deeper `projects/regina-lead-github-pages/reports/` history
- the recovered data catalog metadata layer
- raw/stage/mart OpenGIS lineage
- the canonical runtime/data/code posture established during prior recovery

### The newer control overlay currently lives in:
**`/root/.openclaw/workspace-main`**

That workspace currently holds:
- the restored local memory/control surface for this session family
- the 2026-03-27 canonical Regina control docs copied into local memory/project reports
- the 2026-03-29 post-recovery and full-recovery ledgers

### Reconciliation judgment
Neither workspace alone is sufficient right now.
The correct relationship is:
- `/root/.openclaw/workspace` = **deeper canonical runtime/data corpus**
- `/root/.openclaw/workspace-main` = **newer control overlay / salvage workspace pending reconciliation**

---

## Why `/root/.openclaw/workspace` is the deeper level

### Evidence
Compared with `workspace-main`, `/root/.openclaw/workspace` contains:
- far more Regina project reports (`projects/regina-lead-github-pages/reports/`)
- `reports/regina_governance_catalog_2026-03-24.md`
- `reports/regina_analysis_artifact_catalog_2026-03-24.md`
- `reports/regina_harm_source_metadata_2026-03-24.json`
- OpenGIS catalog scan / field-review / lineage artifacts
- raw OpenGIS payloads under `data/raw/regina_opengis/2026-03-24/`
- stage outputs under `data/stage/regina_opengis/2026-03-24/`
- mart outputs under `data/mart/regina_opengis/2026-03-24/`

### Prior durable rule already established
Earlier recovery notes already set:
- canonical runtime/data/code = `/root/.openclaw/workspace`
- `workspace-main` = salvage-only unless explicitly reconciled

So the deeper-level decision is not new improvisation.
It is consistent with the already established recovery doctrine.

---

## Artifact-class reconciliation map

### 1. Runtime / code / data corpus
**Canonical home:** `/root/.openclaw/workspace`

Use this workspace as authoritative for:
- live code/runtime assumptions
- raw/stage/mart data lineage
- broad historical Regina repo/report corpus
- Dream/recall/JTB runtime discipline when scripts/assets live there

### 2. Regina control/recovery overlay
**Current active control overlay:** `/root/.openclaw/workspace-main`

Use this workspace as current source for:
- `memory/2026-03-27-regina-canonical-summary.md`
- `memory/2026-03-27-regina-completion-vs-enrichment.md`
- `memory/2026-03-27-regina-layer-ranking-rules.md`
- `projects/regina-lead-github-pages/reports/regina_post_recovery_control_status_2026-03-29.md`
- `projects/regina-lead-github-pages/reports/regina_full_recovery_ledger_2026-03-29.md`
- this reconciliation note

### 3. Historical/source catalog metadata
**Canonical content home:** `/root/.openclaw/workspace`

This includes:
- governance catalog
- artifact catalog
- harm source metadata
- OpenGIS catalog metadata / field reviews / lineage notes

### 4. Recovery-grade canonical state answers
**Authority rule:** use the control docs, regardless of workspace location, but prefer their current newest versions.

At present the newest control docs are in `workspace-main`.
However their supporting corpus and data lineage live more deeply in `/root/.openclaw/workspace`.

---

## Operational reconciliation rule

### Rule 1 — deeper corpus wins over shallower salvage
If an artifact class exists deeply in `/root/.openclaw/workspace` and only partially in `workspace-main`, treat `/root/.openclaw/workspace` as the authoritative corpus/source layer.

### Rule 2 — newer control docs can temporarily live in overlay
If a newer canonical control note exists only in `workspace-main`, it may remain authoritative **only if**:
- it does not contradict the deeper corpus; and
- it is eventually promoted/reconciled into the canonical workspace or equivalent canonical retrieval surface.

### Rule 3 — no silent dual-canonical state
Do not allow both workspaces to behave as independent canon.
The deeper workspace is the canonical base.
The newer overlay must either:
- be promoted into canonical base, or
- be explicitly marked as temporary control overlay.

---

## Immediate reconciliation conclusion for Regina

### Deeper canonical base
`/root/.openclaw/workspace`

### Temporary control overlay
`/root/.openclaw/workspace-main`

### Current practical truth
To answer Regina recovery/state questions correctly right now, the system must read across both:
- base corpus + data catalog metadata from `/root/.openclaw/workspace`
- newest control/recovery ledgers from `workspace-main`

That is the current honest state.

---

## Required next reconciliation action

To finish reconciliation properly, promote or mirror the new 2026-03-27 / 2026-03-29 Regina control docs into the deeper canonical workspace or another explicitly canonical retrieval layer, then verify retrieval prefers them while retaining the deeper source/catalog lineage.

Until that happens, recovery should be treated as:
- **cross-workspace reconciled in doctrine**
- but **not yet physically unified**

---

## Recovery-safety rule

When future retrieval, Dream, DMG, recall, or Regina control work runs against one workspace only, default to `/root/.openclaw/workspace` unless there is an explicit, reviewed reason to use `workspace-main`.

`workspace-main` should not silently become the canonical cwd for Regina or Dream/recall operations.
