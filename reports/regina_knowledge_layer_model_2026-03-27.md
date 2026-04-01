# Regina Knowledge Layer Model — 2026-03-27

Status: operator control model for the Regina project knowledge base
Role: ChaosClaw
Purpose: define how Regina knowledge should be separated, ranked, and maintained so bounded current truth is preserved while exploratory/support work remains searchable without causing drift.

---

## Why this exists

Regina is not a simple repo or a single report.
It is a layered project with:
- bounded public truth,
- support-layer analysis,
- exploratory and enrichment work,
- stale and invalidated historical artifacts,
- and an evolving repo-memory / KG system.

Without explicit knowledge layers, retrieval drift becomes likely:
- stale generic descriptions can outrank later bounded posture;
- support-layer material can be mistaken for canonical truth;
- exploratory enrichment can look like unfinished core work;
- old project-state assumptions can pull the project backward after a bounded release state was already achieved.

The solution is not “store less.”
The solution is to store **with authority structure**.

---

# Layer model

## Layer 1 — Canonical Regina State

### Purpose
This is the narrow, high-authority control layer.
It answers:
- what is the current accepted Regina state?
- what is the current claim ceiling?
- what is public vs support vs blocked?
- what is the current gate state?

### Content allowed here
- project state rows
- accepted canonical state updates
- bounded current public posture
- current gate status
- current approved claim ceilings
- explicit risks that affect how the project must be described
- accepted current M3/M4 public-framing posture once promoted

### Regina examples
- `projects/_registry/project_state/regina.json`
- accepted current state updates from governed writes
- later approved bounded M3/M4 framing updates

### Rules
- small and curated
- high authority
- default answer layer for status questions
- must outrank all other Regina layers in retrieval
- changes require explicit review / bounded promotion logic

### Retrieval rank
**Rank 1 (highest)**

---

## Layer 2 — Support Knowledge / Bounded Analytical Knowledge

### Purpose
This is the main Regina project knowledge base.
It answers:
- what has been validated enough to support analysis or operator decisions?
- what bounded reasoning, synthesis, and supporting docs exist?
- what method notes and confidence explanations should inform interpretation?

### Content allowed here
- phase syntheses and execution notes
- operator release notes
- bounded confidence explanations
- support-only analytical memos
- repo-memory curated artifacts
- validation reports
- reconciliation reports
- support-layer M3/M4 framing before or alongside promotion

### Regina examples
- `projects/regina-lead-github-pages/reports/regina_phase1_analytic_classification_synthesis_2026-03-21.md`
- `projects/regina-lead-github-pages/reports/regina_phase2_replacement_confidence_synthesis_2026-03-21.md`
- `projects/regina-lead-github-pages/reports/regina_operator_release_note_2026-03-23.md`
- `projects/regina-lead-github-pages/reports/regina_2026_progress_reconciliation_2026-03-22.md`
- curated repo-memory artifacts for the analysis repo

### Rules
- searchable and broad
- may influence interpretation
- must not silently override Layer 1
- may contain bounded support claims and technical framing
- should be retrieval-eligible after Layer 1, not before it

### Retrieval rank
**Rank 2**

---

## Layer 3 — Exploratory / Enrichment Backlog

### Purpose
This layer preserves useful work that is real but not yet part of the accepted current Regina baseline.
It answers:
- what promising expansions exist?
- what additive lanes were investigated?
- what could be resumed later without pretending it was already core completion?

### Content allowed here
- property tax enrichment
- parcel/account join expansion
- taxweb/propertysearch experiments
- postgis enrichment scaffolds
- broader fiscal context integrations
- optional map/platform expansion ideas
- unpromoted but serious future-work plans

### Regina examples
- `workspace-main/reports/regina_propertysearch_v1_execution_board_2026-03-25.md`
- `workspace-main/reports/regina_propertysearch_v1_build_plan_2026-03-25.md`
- `workspace-main/reports/regina_propertysearch_join_validation_2026-03-25.md`
- `workspace-main/memory/regina_propertysearch_10016630.html`
- `workspace-main/memory/regina_taxweb_10016630.html`

### Rules
- should remain searchable
- should **not** be treated as proof the core Regina project was unfinished
- should not outrank Layers 1 or 2 when answering “what is the current Regina state?”
- should be explicitly labeled as expansion / enrichment / optional next lane

### Retrieval rank
**Rank 3**

---

## Layer 4 — Stale / Invalidated / Suppressed Knowledge

### Purpose
This layer preserves historical and debugging value without letting drift poison first-line retrieval.
It answers:
- what used to be believed but should not rank first now?
- what was repaired, superseded, or suppressed?
- what should be used only for audit/debug lineage?

### Content allowed here
- stale generic repo descriptions
- outdated path-mismatch claims
- superseded project-state prose
- noisy extractor artifacts
- exploratory outputs explicitly demoted below later validator-backed posture
- historical reports whose numbers were superseded by stronger lineage

### Regina examples
- stale generic repo-memory descriptions cited by the stale-claim audit
- older presentation-repo mismatch posture
- March 6 progress-report totals when used against the stricter later lineage
- noisy file-observation artifacts suppressed by the repo-memory repair pass

### Rules
- preserve for audit/debug only
- do not use as first-line truth
- should only surface when explicitly investigating lineage, contradiction, or drift
- should be marked as stale/suppressed/superseded wherever possible

### Retrieval rank
**Rank 4 (lowest normal rank)**

---

# Authority ordering

When answering Regina questions, the authority stack should be:

1. **Canonical Regina State (Layer 1)**
2. **Support Knowledge (Layer 2)**
3. **Exploratory / Enrichment Backlog (Layer 3)**
4. **Stale / Invalidated / Suppressed (Layer 4)**

If lower layers conflict with higher layers:
- higher layer wins
- lower layer is used only as lineage/debug context

---

# Question-routing rules

## A. If the question is “What is the current Regina state?”
Use:
- Layer 1 first
- Layer 2 only to explain nuance
- do not let Layer 3 redefine completion
- do not let Layer 4 rank first

## B. If the question is “What had been validated already?”
Use:
- Layer 1 + Layer 2
- include bounded gates and accepted syntheses
- mention Layer 3 only if it was later drift/expansion

## C. If the question is “What could we do next?”
Use:
- Layer 1 to respect current ceiling and risks
- Layer 2 for support-ready next steps
- Layer 3 for expansion options

## D. If the question is “Why did drift happen?”
Use:
- Layer 4 plus the authority-order explanation
- identify stale retrieval, expansion confusion, or gate collapse

---

# Regina-specific current mapping

## Canonical now
- bounded public/documentary MVP baseline
- pass-with-repairs project state
- research vs publication split
- current gate structure and claim ceilings

## Support knowledge now
- phase syntheses
- replacement-confidence and map-platform decisions
- repo-memory curated analysis pack
- 2026 support-ready bounded reconciliation
- M3/M4 bounded public framing candidates

## Enrichment backlog now
- propertysearch/taxweb/property-tax enrichment lane
- parcel/account join expansion
- postgis enrichment contracts

## Stale/suppressed now
- stale repo-memory descriptions that outrank bounded posture
- older presentation mismatch claims
- March 6 weaker totals when treated as controlling truth
- low-signal extraction noise

---

# Maintenance rules

## 1. Promote carefully
Only move Regina material upward when:
- validator-backed,
- bounded,
- provenance-explicit,
- and consistent with current gate state.

## 2. Never collapse support into canon silently
Support knowledge may explain canon, but it may not replace it unless explicitly promoted.

## 3. Preserve exploration without letting it steer status
Enrichment work should remain queryable, but it must stay visibly separate from completion state.

## 4. Keep stale material auditable, not dominant
Do not delete drift history blindly.
Preserve it, but rank it correctly.

## 5. Use retrieval tests as a gate
A knowledge-layer model is not complete until representative Regina queries return:
- Layer 1 first,
- Layer 2 next,
- Layer 3 only when expansion is asked,
- Layer 4 only when lineage/drift is asked.

---

# Immediate next implementation moves

1. Ingest / formalize the March 23 M3/M4 bounded public-framing candidates into the Regina support/canonical stack appropriately.
2. Run the targeted Regina repo-memory → KG refresh using the repaired curated artifacts.
3. Mark identified stale Regina repo-memory claims as suppressed in retrieval ranking.
4. Add a Regina retrieval test set:
   - current state
   - what was validated
   - what is pending
   - what is enrichment
   - what is stale
5. Verify the system answers those correctly using this layer model.

---

# Bottom line

Yes, Regina should have a project knowledge base.
But that knowledge base must be layered.

If we do this right:
- Regina stays queryable,
- enrichment work stays reusable,
- stale work stays auditable,
- and bounded current truth does not get lost again.
