tags: [regina:canonical, regina:recovery, regina:promotion, regina:control]
created_by: ChaosClaw
created_at: 2026-03-29T07:47:00+02:00

# Regina recovery promotion status — 2026-03-29

Status: canonical recovery promotion checkpoint
Purpose: freeze the transition from merely mirrored recovery/control docs to active retrieval-layer promotion, so the system can distinguish physical reconciliation from indexed authority recovery.

---

## Executive result

A meaningful recovery threshold has now been crossed.

### Before this step
- canonical Regina recovery/control docs existed on disk;
- they had been mirrored into the deeper canonical workspace;
- but the active Regina repo-memory layer did not contain those recovery/control claims;
- therefore live retrieval continued to return generic repo-memory residue and low-signal file observations.

### After this step
- a compact canonical Regina recovery/control claim set was promoted into the active indexed repo-memory layer;
- live Regina recovery queries now surface the expected canonical control docs at the top;
- the system is materially better positioned to detect drift and resist stale/louder non-canonical residue.

---

## What was promoted into active repo-memory

The active Regina repo-memory layer now includes canonical claims for:
- current state (`regina_current_state_2026_03_27`)
- completion vs enrichment (`regina_completion_vs_enrichment_2026_03_27`)
- retrieval ranking rule (`regina_retrieval_ranking_rule_2026_03_27`)
- cross-workspace reconciliation (`regina_cross_workspace_reconciliation_2026_03_29`)
- full recovery scope (`regina_full_recovery_scope_2026_03_29`)
- catalog metadata recovery (`regina_catalog_metadata_recovery_2026_03_29`)
- recovery verification status (`regina_recovery_verification_status_2026_03_29`)

These were promoted into:
- `/root/.openclaw/workspace/repo_knowledge/regina-lead-connections-analysis/claim_records.jsonl`

---

## Retrieval verification outcome after promotion

### Query: current state / property-tax scope
Top results now correctly surface:
1. canonical current-state summary
2. completion-vs-enrichment summary
3. retrieval ranking rule

### Query: deeper canonical workspace
Top result now correctly surfaces:
1. cross-workspace reconciliation note

### Query: catalog metadata / source-contract drift detection
Top result now correctly surfaces:
1. catalog metadata recovery claim
with evidence refs including governance catalog, analysis artifact catalog, and harm source metadata.

---

## Important remaining caveat

This does **not** mean the Regina retrieval layer is fully clean.

### Still true
- the indexed corpus still contains a large amount of low-signal `file_observation` residue;
- generic file-observation rows still outnumber authoritative recovery/control claims;
- further cleanup or downweighting of low-signal artifact observations is still worthwhile.

### But the key failure has changed
The key blocker is no longer:
- “canonical recovery truth is absent from active retrieval.”

It is now:
- “canonical recovery truth is present and winning key queries, but the broader retrieval surface is still noisier than ideal.”

---

## Status label

### Updated recovery label
**physically reconciled, canonical recovery claims promoted into active retrieval, broader retrieval cleanup still pending**

That is the current honest state.

---

## Operational rule

For Regina recovery/state/completion/drift questions, the promoted canonical control claims should now be treated as the preferred repo-memory entrypoint layer.

Further cleanup should focus on reducing low-signal residue rather than re-litigating whether the canonical recovery layer exists.
