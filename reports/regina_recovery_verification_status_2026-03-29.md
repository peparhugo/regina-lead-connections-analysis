tags: [regina:canonical, regina:recovery, regina:verification, regina:control]
created_by: ChaosClaw
created_at: 2026-03-29T07:39:00+02:00

# Regina recovery verification status — 2026-03-29

Status: canonical recovery verification checkpoint
Purpose: record which recovery conditions are now satisfied versus which still fail, with explicit emphasis on retrieval-governance rather than mere file presence.

---

## Executive verdict

Regina recovery is **not yet fully complete**.

### What succeeded
- cross-workspace split-brain was identified explicitly;
- the deeper canonical workspace was confirmed as `/root/.openclaw/workspace`;
- newer Regina control/recovery docs were mirrored into the deeper canonical workspace;
- those mirrored docs were placed under governed repo history via PR `#7`;
- deeper historical data-catalog and source-contract artifacts were confirmed present in the canonical workspace.

### What still fails
The current retrieval path is **not yet reliably surfacing the new Regina recovery/control layer as dominant authority**.

This means:
- physical recovery is substantially complete;
- retrieval-governance recovery is not.

---

## Artifact-class verification matrix

### 1. Canonical recovery/control docs
Examples:
- `memory/2026-03-27-regina-canonical-summary.md`
- `memory/2026-03-27-regina-completion-vs-enrichment.md`
- `memory/2026-03-27-regina-layer-ranking-rules.md`
- `reports/regina_post_recovery_control_status_2026-03-29.md`
- `reports/regina_full_recovery_ledger_2026-03-29.md`
- `reports/regina_cross_workspace_reconciliation_2026-03-29.md`

Status:
- present in canonical workspace: **YES**
- mirrored from salvage overlay: **YES**
- under GitHub PR discipline: **YES** (`PR #7`)
- dominant in retrieval answers: **NO / NOT YET VERIFIED; current probe failed**

### 2. Regina data catalog metadata
Examples:
- `reports/regina_governance_catalog_2026-03-24.md`
- `reports/regina_analysis_artifact_catalog_2026-03-24.md`
- `reports/regina_harm_source_metadata_2026-03-24.json`
- OpenGIS catalog scan / field review / lineage artifacts

Status:
- present in canonical workspace: **YES**
- included in recovery scope: **YES**
- retrievable as governed support metadata: **NOT YET VERIFIED**
- explicitly promoted into current retrieval contract: **NO / NOT YET**

### 3. Raw / stage / mart lineage surfaces
Examples:
- `data/raw/regina_opengis/2026-03-24/`
- `data/stage/regina_opengis/2026-03-24/`
- `data/mart/regina_opengis/2026-03-24/`

Status:
- present in canonical workspace: **YES**
- stranded in salvage only: **NO**
- retrieval-critical as direct top authority: **NO**
- available for drift/invalidation lineage: **YES**

### 4. Cross-workspace reconciliation doctrine
Status:
- written: **YES**
- mirrored into canonical workspace: **YES**
- under PR discipline: **YES**
- enforced by retrieval/runtime path automatically: **NO / NOT YET**

---

## Retrieval verification evidence

### Probe method used
Queried the canonical workspace via:
- `scripts/repo_memory_cross_repo_query.py`

### Probe result
The retrieval path returned broad repo-memory patterns and generic file-observation matches instead of clearly elevating the new canonical recovery/control docs.

### Interpretation
This is a governance failure in retrieval ranking / answer shaping, not a file-presence failure.

The current retrieval path is still anchored too heavily to generic repo-memory extraction and lacks a dedicated contract for the new recovery/control artifacts.

---

## Main blocker now

### Blocker
**No explicit retrieval contract yet protects the new Regina recovery/control docs.**

### Why this happened
Existing Regina retrieval/ranking tests appear to protect some older bounded-framing claims, but do not yet cover:
- the 2026-03-27 canonical current-state summary
- the 2026-03-27 completion-vs-enrichment rule
- the 2026-03-27 ranking rule itself
- the 2026-03-29 post-recovery / full-recovery / cross-workspace control notes

So the retrieval layer has no specific test-backed obligation to surface them first.

---

## Current status label

**Recovery state: physically reconciled, retrieval-governance incomplete**

That is the current honest status.

---

## Required next steps

1. add an explicit retrieval contract / ranking path for Regina recovery-control docs;
2. add tests that force current-state and recovery questions to surface the new canonical docs first;
3. rerun retrieval verification after the ranking/test fix;
4. only then mark Regina full recovery complete.

---

## Operational rule

Until retrieval verification passes, do not rely on the current repo-memory answer path alone for Regina current-state, completion, or full-recovery questions.
Prefer the canonical control docs directly.
