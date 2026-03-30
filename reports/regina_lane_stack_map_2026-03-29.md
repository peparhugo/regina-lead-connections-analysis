tags: [regina:canonical, regina:lanes, regina:control, regina:dmg]
created_by: ChaosClaw
created_at: 2026-03-29T08:39:00+02:00

# Regina lane stack map — 2026-03-29

Status: canonical lane-map note
Purpose: disambiguate the different meanings of “lane” by explicitly separating (1) substantive Regina work lanes, (2) Dream/DMG learning lanes, and (3) execution/service routes.

---

## Executive summary

“Lane” has been overloaded.

At minimum, the Regina system currently needs to distinguish three layers:

1. **Substantive Regina work lanes** — the real project workstreams
2. **Dream/DMG learning lanes** — the kind of learning/questioning being done
3. **Execution/service routes** — the service path that actually runs the work

The DMG taxonomy is intentionally small.
The substantive lane universe is much larger.
The route layer is also larger than the DMG taxonomy.

---

# 1. Substantive Regina work lanes

These are the real workstreams Regina can move through.
They are not limited to the current DMG taxonomy.

## A. Recovery / control-plane lanes
- cross-workspace reconciliation
- recovery verification
- recovery promotion
- recovery governance / PR discipline
- repo-history truth
- gate-status truth
- canonical authority ordering
- invalidation ledger maintenance
- residue classification / backlog policy
- control summary / phase-map sync

## B. Support / contradiction lanes
- support-layer contradiction review
- support wording boundary review
- appendix boundary review
- burden communication discipline
- scenario-envelope discipline
- framework-vs-result separation
- support promotion review
- support demotion review
- support-layer retrieval boundary hardening
- contradiction-sensitive support extraction

## C. Publication / package lanes
- public-package hardening
- build/reproducibility truth
- publication-safe claim selection
- headline-vs-appendix separation
- public/package QA
- package gate review
- journalist brief packaging
- support/public wording synchronization
- public-brief confidence discipline
- prepublish audit and curation

## D. Research / evidence lanes
- direct burden evidence lane
- supporting exposure-context lane
- scholarly evidence lane
- accountability/media evidence lane
- contradiction evidence lane
- public-interest framing comparison lane
- council/delegate concern validation lane
- timeline/documentary evidence lane
- support communication comparison lane
- claim-envelope governance comparison lane

## E. Data / graph / recall lanes
- OpenGIS catalog recovery
- data catalog metadata governance
- source-contract recovery
- parcel/account linkage
- property-tax enrichment
- graph integration
- repo-memory KG promotion
- retrieval ranking hardening
- low-signal residue suppression
- canonical claim promotion
- graph-backed contradiction surfacing
- recall boundary enforcement

## F. Decision / sequencing lanes
- next active lane selection
- operator decision support
- stop/continue gate review
- enrichment-vs-core arbitration
- experiment triage
- route-quality comparison
- wave-design planning
- active-lane reprioritization

---

# 2. Dream/DMG learning lanes

These are the bounded question/intelligence patterns used to learn about a project lane.
They are not the project lane itself.

## Focused learning lanes
- direct_implementation
- validation_or_contradiction
- benchmark_or_comparison
- failure_diagnosis
- operator_decision_support

## Adjacent learning lanes
- transferable_methods
- tooling_patterns
- neighboring_domain_analogy
- weak_signal_opportunities
- strategic_option_expansion

## Regina-specific extensions / reinterpretations needed
For Regina, several additional learning-lane labels make more sense than relying only on the generic defaults:
- support_communication_comparison
- claim_envelope_governance
- public_evidence_framing
- support_boundary_validation
- retrieval_boundary_hardening

These may be implemented as explicit extensions or as project-specific overrides/mappings on top of the current DMG taxonomy.

---

# 3. Execution / service routes

These are the actual service paths or runner types that execute work.
A single substantive lane may use multiple learning lanes and multiple routes.

## Internal / local routes
- internal_validation_service.py
- repo-memory interrogation
- canonical current-state arbitration
- claim-order review
- contradiction bundle generation
- operator decision bundle generation
- graph/recall local probes
- retrieval ranking probes

## External / live routes
- project_scoped_live_learning.py
- web-heavy external retrieval
- scholarly-heavy external retrieval
- mixed web + scholarly retrieval
- reranked external retrieval
- allowlisted-domain retrieval
- evidence-class-targeted retrieval (e.g. direct burden evidence, exposure context)

## Experiment / audit routes
- question battery runs
- DMG mutation runs
- route comparison runs
- audit-only runs
- rerank-debug runs
- smoke runs
- canonical-path validation runs
- multi-cell lane/route matrix runs

---

# 4. How the layers combine

A meaningful Regina experiment cell should be described as:

- **Substantive lane**
- **Learning lane**
- **Execution route**

Example:
- substantive lane: `support-layer contradiction review`
- learning lane: `validation_or_contradiction`
- execution route: `internal_validation_service.py`

Another example:
- substantive lane: `support communication comparison`
- learning lane: `support_communication_comparison` (or benchmark/comparison mapped to this)
- execution route: `project_scoped_live_learning.py` with support/communication-specific external query anchoring

---

# 5. Current best-fit Regina lane stack after recovery

## Current best substantive lane
- support-layer contradiction review + graph/recall hardening

## Current high-yield learning lanes
- validation_or_contradiction
- operator_decision_support

## Current validated external route use
- external retrieval is viable after bootstrap fix
- but route quality depends heavily on lane-specific topical anchoring

## Current misfit to avoid
Treating generic `failure_diagnosis` as if it were the substantive Regina lane is conceptually wrong.
That was a route/question-shape artifact, not the real project lane.

---

# 6. Operational rule

When planning future Regina work, always name all three layers explicitly:

1. **What substantive work lane are we in?**
2. **What learning/question lane are we using?**
3. **What service/runner route is executing it?**

Do not use the word “lane” alone when ambiguity matters.

---

# 7. Immediate next implication

For the current Regina phase, the clean next experiment framing is:

- substantive lane: `support communication comparison`
- learning lane: `support_communication_comparison` (or benchmark/comparison remapped to that function)
- route: `project_scoped_live_learning.py` with support/communication-specific scope terms

That is more precise than calling it simply a “failure_diagnosis lane” or a generic “benchmark lane.”
