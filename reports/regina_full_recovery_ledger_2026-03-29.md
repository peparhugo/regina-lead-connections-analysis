tags: [regina:canonical, regina:recovery, regina:control, regina:catalog]
created_by: ChaosClaw
created_at: 2026-03-29T06:46:00+02:00

# Regina full recovery ledger — 2026-03-29

Status: canonical recovery ledger
Purpose: establish a recovery-grade ledger for Regina so future work can detect drift, identify stale branches of truth, and invalidate superseded conclusions without confusing local presence for proven ingest or promotion.

---

## Recovery objective

Full Regina recovery requires explicit accounting for:
1. corpus/date coverage
2. canonical control truth
3. artifact authority ordering
4. data catalog metadata
5. ingest/promotion status
6. invalidation targets
7. residue classification

This ledger is the control-plane anchor for that recovery discipline.

---

## A. Date coverage ledger

### Confirmed locally present

#### 2026-03-24
Present across `memory/`, `docs/`, and the older canonical workspace.
Includes chronology/recovery docs plus the main Regina data-catalog and OpenGIS metadata artifacts in the older workspace.

#### 2026-03-25
Present across `memory/`, `reports/`, and `docs/`.
Includes propertysearch / tax / scaffold / join-related execution artifacts.

#### 2026-03-26
Present across `memory/` and `docs/`.
Includes JTB pipeline/audit material.

#### 2026-03-27
Present across `memory/`, `reports/`, and `projects/regina-lead-github-pages/reports/`.
Includes canonical Regina state/control artifacts.

#### 2026-03-28
Present across `memory/`.
Includes Dream/DMG harness work, retrieval fixes, DNS/debug, and next-move artifacts.

#### 2026-03-29
Daily recovery checkpoint created in local memory.

### Recovery interpretation
Date coverage from 2026-03-24 through 2026-03-28 is locally confirmed.
This is sufficient for recovery analysis.
It is not by itself proof of full ingest into every recall/KG layer.

---

## B. Canonical control truth ledger

### Current canonical state
The authoritative Regina state remains:
- `overall_state: pass_with_repairs`
- public/package baseline: publishable within limits
- research status: mixed
- maintain explicit research/publication split

### Core governance rule
Property-tax enrichment is additive and should not be treated as reopening core validation.

### Retrieval authority rule
For state/status/completeness queries, `regina:canonical` control docs must outrank repo-memory residue and non-canonical artifacts.

### Current active-lane judgment
Until full recovery is complete, the highest-priority substantive Regina lane is:
- **support-layer contradiction review + graph/recall hardening**

Property-tax enrichment remains queued rather than active.

---

## C. Authority ordering ledger

### Tier 1 — canonical control truth
Use as authority for current-state / completeness / project-status questions:
- `memory/2026-03-27-regina-canonical-summary.md`
- `memory/2026-03-27-regina-completion-vs-enrichment.md`
- `memory/2026-03-27-regina-layer-ranking-rules.md`
- `projects/regina-lead-github-pages/reports/regina_authoritative_state_2026-03-27.md`
- `projects/regina-lead-github-pages/reports/regina_post_recovery_control_status_2026-03-29.md`
- this file: `projects/regina-lead-github-pages/reports/regina_full_recovery_ledger_2026-03-29.md`

### Tier 2 — recovery/governance reconstruction
Use for explanation and drift analysis, not as top authority over Tier 1:
- `reports/regina_knowledge_completion_reconstruction_2026-03-27.md`
- `reports/regina_knowledge_layer_model_2026-03-27.md`
- `reports/regina_m3_m4_knowledge_layer_formalization_2026-03-27.md`
- older workspace governance/data-catalog reports from 2026-03-24

### Tier 3 — analytic / operational / enrichment artifacts
Use as supporting evidence, not direct canonical state truth:
- propertysearch execution reports
- join validation reports
- OpenGIS scan/field review reports
- Dream/DMG run notes and lane-fix notes
- raw/stage/mart outputs

### Tier 4 — scratch / residue / debug
Never treat as authoritative without explicit promotion:
- scratch JSON/TXT files
- temporary validation snippets
- one-off debug dumps
- cached raw pages / HTML captures

---

## D. Regina lead data catalog metadata ledger

This section is explicitly part of full recovery scope.

### D1. Recovered catalog-metadata artifacts from older workspace
Confirmed present in `/root/.openclaw/workspace/reports/`:
- `regina_governance_catalog_2026-03-24.md`
- `regina_analysis_artifact_catalog_2026-03-24.md`
- `regina_harm_source_metadata_2026-03-24.json`
- `regina_opengis_catalog_scan_2026-03-24.md`
- `regina_opengis_catalog_field_review_2026-03-24.md`
- `regina_opengis_memory_dataset_profile_2026-03-24.md`
- `regina_opengis_memory_mart_qa_2026-03-24.md`
- `regina_opengis_memory_next_step_design_2026-03-24.md`
- `regina_opengis_geometry_lineage_audit_2026-03-24.md`
- `regina_opengis_property_tax_linkage_2026-03-24.md`
- `regina_opengis_lead_table_ranking_2026-03-24.md`

### D2. Recovered raw/stage/mart lineage surfaces from older workspace
Confirmed present under `/root/.openclaw/workspace/data/`:
- raw OpenGIS metadata and payloads under `data/raw/regina_opengis/2026-03-24/`
- spatial exports under `data/spatial/regina_opengis/2026-03-24/`
- stage parquet outputs under `data/stage/regina_opengis/2026-03-24/`
- mart outputs under `data/mart/regina_opengis/2026-03-24/`
- `data/regina_gisid_ingest/2026-03-24/raw/parcels_service.json`

### D3. Preferred source-ordering metadata recovered
Recovered/confirmed design posture:
- OpenRegina / OpenGIS structured sources were preferred first
- `propertysearch.regina.ca` was fallback, not primary truth
- account/parcel/tax linkage was a controlled enrichment lane

### D4. Core source-contract surfaces recovered
Recovered source spine includes at least these major service/layer contracts:
- current water connection lines
- snapshot/historical water connection lines
- address points
- parcel polygons / APN/account surfaces
- lead-connection area polygons
- related support polygons

### D5. Catalog metadata recovery rule
These catalog/source metadata artifacts are part of full recovery and must be queryable in recovery decisions.
Do not treat them as optional side notes.

---

## E. Ingest / promotion status ledger

### Confirmed present locally
- canonical control docs
- recovery/governance reports
- older workspace catalog metadata artifacts
- raw/stage/mart data lineage artifacts
- recent Dream/DMG and Regina fix notes

### Not yet proven by this ledger alone
The following must still be treated as unverified until explicitly checked:
- whether all recovered catalog metadata has been re-ingested into live recall/KG
- whether all canonical Regina control docs rank correctly in live retrieval
- whether older workspace catalog artifacts are discoverable from the active workspace retrieval path
- whether data-catalog metadata has been promoted into current canonical query surfaces

### Current recovery status label
**Recovery state: present-and-mapped, ingest/promotion verification pending**

---

## F. Invalidation ledger

### Invalidations / demotions already established conceptually
- property-tax enrichment must not be used to imply core validation was incomplete
- non-canonical repo-memory residue must not outrank canonical control docs for state questions
- exploratory/support/enrichment artifacts must not be mistaken for current authoritative project status

### Classes of artifacts that may need invalidation or demotion
- stale generic package summaries
- old retrieval surfaces that ignore canonical ranking rules
- scratch/debug checks that look like status evidence but were never promoted
- enrichment-lane outputs later mistaken for core state
- source-contract assumptions tied to fallback propertysearch behavior when better structured source metadata exists

### Recovery rule for invalidation
No historical artifact should be treated as live truth unless it is either:
1. canonical by designation, or
2. explicitly linked as supporting evidence beneath a canonical statement.

---

## G. Residue classification ledger

### Keep active
- canonical control docs
- current recovery ledgers
- authoritative project reports
- validated runbooks and scripts
- dated memory files needed for continuity

### Archive
- superseded debug outputs
- stale one-off checks
- transient recovery residue already captured in canonical ledgers

### Ignore / non-truth
- caches
- `__pycache__`
- vendor/tool internals
- transient temp outputs

### Externalize when practical
- bulky raw payloads reproducible from official sources
- large datasets that are useful lineage but not active control truth

---

## H. Recovery completion gate

Do not mark Regina full recovery complete until all of the following are explicitly verified:
1. live retrieval returns Tier 1 canonical control docs for state/completeness queries;
2. recovered data-catalog metadata is reachable from the active recovery process and not stranded only in the old workspace;
3. ingest status is explicitly recorded for recovered canonical and catalog artifacts;
4. invalidation/demotion rules are frozen for stale or enrichment-only branches;
5. residue classes are separated enough that scratch outputs cannot masquerade as truth.

---

## I. Immediate next recovery action

Next action after this ledger:
- run live retrieval / ingest verification against Tier 1 canonical docs and recovered catalog metadata artifacts;
- then write a recovery verification note that marks each artifact class as: present / retrievable / promoted / pending / invalidated.
