tags: [regina:canonical, regina:recovery, regina:governance, regina:control]
created_by: ChaosClaw
created_at: 2026-03-29T08:03:00+02:00

# Regina recovery governance surface — 2026-03-29

Status: canonical governance checkpoint
Purpose: tie together the two active PR-governed recovery surfaces so project truth and retrieval truth are tracked as one operator-visible recovery state.

---

## Executive summary

Regina recovery is now governed across **two PR surfaces**:

1. **Project/control-plane truth** in the Regina repo
2. **Retrieval/indexing truth** in the memory-recall / canonical workspace repo

This is the correct split.

The Regina repo governs what the project truth is.
The memory-recall repo governs whether the retrieval system actually returns that truth.

---

## Governance surface A — Regina project repo

### Repo
- `peparhugo/regina-lead-connections-analysis`

### Active PR
- PR `#7`
- title: `regina: add recovery control ledgers and reconciliation`

### What it governs
- post-recovery control status
- full recovery ledger
- cross-workspace reconciliation
- recovery completion status
- recovery verification status
- recovery promotion status

### Meaning
This PR is the project-side recovery/control record.
It governs the explicit narrative of what was recovered, what remains incomplete, and how the project should answer recovery/state questions.

---

## Governance surface B — retrieval/system repo

### Repo
- `fire-horse-labs/memory-recall`

### Active PR
- PR `#10`
- title: `fix: promote regina recovery canon into repo-memory retrieval`

### What it governs
- promotion of canonical Regina recovery claims into the active repo-memory layer
- retrieval ranking/support logic improvements for Regina recovery queries
- recovery-focused regression coverage

### Meaning
This PR is the system-side recovery record.
It governs whether the active retrieval layer actually surfaces the newly recovered canonical Regina truth instead of low-signal residue.

---

## Why the split is correct

A single PR could not honestly govern both layers because they live in different repos and serve different functions.

### Regina repo answers:
- what is the project truth?
- what is canonical?
- what is the recovery/invalidation posture?

### memory-recall repo answers:
- does the retrieval system index that truth?
- does the retrieval system rank that truth correctly?
- can the system resist residue and drift during live queries?

Both are required for credible recovery.

---

## Current operator judgment

### Recovery posture now
Recovery is no longer just “files restored.”
It is now:
- mirrored into canonical workspace
- promoted into active retrieval
- documented in project control docs
- and tracked through explicit PR governance on both surfaces

### Remaining caution
This does **not** mean all cleanup is finished.
The broader retrieval surface is still noisier than ideal, and the canonical workspace repo remains operationally dirty outside the narrowly scoped retrieval PR.

But the core recovery/governance loop is now materially in place.

---

## Status label

**Regina recovery is now dual-governed across project truth and retrieval truth.**

That is the correct current operator-facing description.
