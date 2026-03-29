tags: [regina:canonical, regina:state, regina:control, regina:recovery]
created_by: ChaosClaw
created_at: 2026-03-29T06:41:00+02:00

# Regina post-recovery control status — 2026-03-29

Status: canonical post-recovery checkpoint
Purpose: freeze what is actually present, what is canonically established, what is merely recovered locally, and what still needs explicit ingest/promotion for full recovery discipline.

---

## Executive summary

Recovery is now strong enough to proceed, but not strong enough to be sloppy.

The correct current posture is:
- dated recovery artifacts for **2026-03-24 through 2026-03-28** are present locally;
- canonical Regina state/control artifacts from **2026-03-27** are present locally;
- substantive forward work from **2026-03-28** is present locally;
- **presence is confirmed**, but **full ingest/promotion should not be assumed** unless explicitly recorded;
- next active Regina lane should be **support-layer contradiction review + graph/recall hardening**, not property-tax enrichment.

---

## Date coverage confirmed locally

Confirmed local dated artifact coverage:

### 2026-03-24
Present in local corpus across memory/docs.
Includes daily memory plus chronology/Neo4j/recovery-era docs.

### 2026-03-25
Present in local corpus across memory/reports/docs.
Includes extensive JTB, dispatcher, MCP, and Regina propertysearch-related artifacts.

### 2026-03-26
Present in local corpus across memory/docs.
Includes JTB pipeline and audit artifacts.

### 2026-03-27
Present in local corpus across memory/reports/project reports.
Includes canonical Regina control artifacts:
- `memory/2026-03-27-regina-canonical-summary.md`
- `memory/2026-03-27-regina-completion-vs-enrichment.md`
- `memory/2026-03-27-regina-layer-ranking-rules.md`
- `projects/regina-lead-github-pages/reports/regina_authoritative_state_2026-03-27.md`

### 2026-03-28
Present in local corpus across memory.
Includes Dream/DMG harness work, Regina fix work, DNS/debug, and next-move artifacts.

### 2026-03-29
Daily control log created today to mark this checkpoint.

---

## Canonical truth currently established

The canonical Regina state remains:
- `overall_state: pass_with_repairs`
- public/package baseline: publishable within limits
- research status: mixed
- maintain explicit research/publication split

The canonical governance also remains:
- property-tax enrichment is additive
- enrichment should not be treated as reopening core validation

The canonical retrieval rule remains:
- state/status/completeness answers must prefer `regina:canonical` control docs over non-canonical/repo-memory residue

---

## Presence vs ingest / promotion status

This distinction matters for full recovery.

### Confirmed present locally
The following are confirmed present in the workspace:
- dated memory artifacts for 2026-03-24 through 2026-03-28
- dated reports/docs across 2026-03-24 through 2026-03-27
- canonical Regina project reports under `projects/regina-lead-github-pages/reports/`
- Regina 2026-03-28 forward-work memory artifacts

### Not yet safe to assume from presence alone
Until explicitly recorded elsewhere, do **not** automatically assume:
- every recovered artifact has been re-ingested into every recall/KG layer
- every canonical Regina artifact has been re-promoted into all live retrieval surfaces
- repo history currently expresses the recovery state cleanly
- all stale/scratch residue has been classified or archived

### Working recovery judgment
Recovery is **operationally sufficient for forward work**, but **full recovery discipline still requires explicit ingest/promotion accounting**.

---

## Residue / backlog policy

### Keep in active repo
- canonical control docs
- active phase/gate/control docs
- validated reports
- live scripts/workflows
- authoritative Regina reports
- dated memory files needed for continuity

### Archive
- stale one-off debug outputs
- superseded temporary diagnostics
- scratch JSON/TXT check files
- residue already captured in a canonical summary

### Ignore / keep out of active truth
- caches
- `__pycache__`
- transient temp state
- tool/vendor internals

### Externalize when practical
- bulky raw fetchable source payloads
- large reproducible raw datasets
- backlog material worth preserving but not worth keeping as active control-plane truth

---

## Chosen next active substantive lane

### Active lane
**support-layer contradiction review + graph/recall hardening**

### Why this lane wins now
Because current canonical state says:
- core validation is already substantially landed;
- property-tax is enrichment, not the current control bottleneck;
- remaining risk is mixed research interpretation and retrieval/control drift;
- the rebuilt system should now prove itself in contradiction-sensitive forward motion.

### Deferred lane
Property-tax enrichment remains queued, but is not the active priority.

---

## Explicit recovery follow-up needed for full recovery

To claim full recovery cleanly, verify and/or record:
1. which dated artifacts have been re-ingested into live recall/KG surfaces;
2. which canonical Regina control docs are promoted and ranking correctly in live retrieval;
3. which scratch/debug files have been archived or excluded from active truth;
4. whether repo-history / commit structure now reflects post-recovery reality;
5. whether any pre-2026-03-24 canonical Regina state still needs import from the older workspace.

---

## Operational rule

Proceed with real work now.
But for any future “fully recovered / fully ingested” claim, require explicit evidence rather than inferring from local file presence alone.
