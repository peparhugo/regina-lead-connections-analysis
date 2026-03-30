tags: [regina:canonical, regina:dream, regina:dmg, regina:optimization-architecture]
created_by: ChaosClaw
created_at: 2026-03-29T08:49:00+02:00

# Regina Dream Monkey + DMG multi-step optimization architecture — 2026-03-29

Status: canonical architecture design
Purpose: define how Regina should use the full Dream Monkey / Dream Lab system, the DMG sublayer, and question-driven experiment routing together as a multi-step optimization loop rather than as isolated lane guesses.

---

## Executive goal

Use the full Dream Monkey / Dream Lab capability surface plus the DMG generator sublayer to run **question-driven multi-step optimization** for Regina.

This means:
- not using only a small DMG lane list;
- not treating one question as one route;
- not treating one route as one substantive lane;
- instead using questions to drive branching, mutation, route comparison, refinement, and operator-grade selection of the best next path.

---

## Core principle

A good Regina question should not just produce an answer.
It should be able to travel through multiple path stacks, where each stack can be compared.

The optimization target is not just “best answer.”
It is:
- best **question formulation**,
- best **Dream path family**,
- best **DMG generation/mutation pattern**,
- best **execution route**,
- best **operator action**.

---

# 1. Layered architecture

## Layer A — substantive Regina objective
What real project objective is being optimized?

Examples:
- support-layer contradiction review
- support communication comparison
- graph/recall hardening
- public-package hardening
- property-tax enrichment
- evidence/accountability validation

This is the top-level intent.

## Layer B — question family
How is the objective interrogated?

Examples:
- contradiction question
- decision-support question
- communication-comparison question
- claim-envelope governance question
- external evidence question
- route-failure explanation question

A single substantive objective may generate multiple question families.

## Layer C — Dream Monkey path family
Which broader Dream path is used?

Examples:
- candidate-generation path
- learning pass path
- bridge / JTB feedback loop path
- mutation path
- experiment path
- refinement path
- simulation path
- promotion/materialization path
- route-matrix comparison path

This is larger than DMG.

## Layer D — DMG sublayer use
What DMG role is active?

Examples:
- question generation
- suggestion generation
- mutation generation
- route-shaped question spec generation
- route-family prompt variation

DMG is one generator/mutation layer inside the broader Dream path family.

## Layer E — execution/service route
What actually runs?

Examples:
- internal_validation_service.py
- project_scoped_live_learning.py
- scholarly-heavy external retrieval
- rerank-debug path
- route-comparison run
- audit-only run
- simulation run

## Layer F — scoring / selection
How do we judge the outputs?

Dimensions should include:
- usefulness
- contradiction safety
- canonicality / authority discipline
- operator clarity
- route fit
- next-step leverage
- drift resistance

---

# 2. Optimization unit

The basic optimization unit should be a **path stack cell**.

One path stack cell =
- 1 substantive objective
- 1 question formulation
- 1 Dream path family
- 1 DMG generation/mutation pattern
- 1 execution route
- 1 scored output bundle

This is the object to compare.

---

# 3. Regina-specific optimization domains

## Domain 1 — support contradiction domain
Primary objective:
- preserve support-only artifacts without allowing claim-envelope drift

Best question families:
- contradiction
- decision support
- claim-envelope governance

Likely Dream paths:
- learning pass
- mutation pass
- experiment execution
- refinement

Likely routes:
- internal validation
- mixed internal + external comparison

## Domain 2 — support communication domain
Primary objective:
- find how support-layer work should be framed publicly without pseudo-precision or silent promotion

Best question families:
- support communication comparison
- uncertainty framing
- public evidence framing
- bounded-estimate communication

Likely Dream paths:
- learning pass
- mutation path
- route-comparison path
- refinement

Likely routes:
- external live learning
- scholarly-heavy retrieval
- rerank-debug comparison

## Domain 3 — graph/recall hardening domain
Primary objective:
- ensure canonical/support boundaries survive in live retrieval and answer shaping

Best question families:
- contradiction validation
- route-quality comparison
- retrieval-boundary explanation
- ranking-hardening tests

Likely Dream paths:
- learning pass
- mutation path
- experiment execution
- simulation

Likely routes:
- internal validation
- rerank-debug
- route-matrix experiments

## Domain 4 — forward evidence/enrichment domain
Primary objective:
- add new evidence or enrichment only after control discipline holds

Best question families:
- evidence comparison
- decision support
- transferable methods
- bounded external evidence

Likely Dream paths:
- learning pass
- mutation pass
- experiment execution
- refinement

Likely routes:
- external live learning
- scholarly-heavy
- hybrid internal/external

---

# 4. Question-family strategy

Each substantive objective should be represented by multiple question formulations rather than one.

## Recommended question families per objective
For each objective, generate at least:
1. contradiction form
2. decision-support form
3. comparison form
4. governance/boundary form

Optional:
5. transferable-methods form
6. simulation/test form

This avoids overfitting to one wording or one route vocabulary.

---

# 5. Dream Monkey path families to compare

The following broad path families should be treated as distinct optimization surfaces.

## P1 — direct learning path
Question -> learning pass -> route output -> audit

Use when:
- fast evidence is needed
- low orchestration overhead preferred

## P2 — learning + mutation path
Question -> learning pass -> DMG mutation pass -> experiment execution -> audit

Use when:
- route variants or prompt families should be compared
- initial answers are likely too brittle

## P3 — learning + bridge validation path
Question -> learning pass -> packet / bridge / feedback loop -> refined result

Use when:
- claim-level review or JTB-like gating matters
- overclaim risk is high

## P4 — route comparison path
Question family -> multiple route variants -> comparative scoring -> best route selected

Use when:
- route quality is uncertain
- system drift or mismatch is suspected

## P5 — refinement path
Question family -> route output -> refinement pass -> re-ask / narrower next-step question

Use when:
- first-pass answers are directionally useful but too noisy or broad

## P6 — simulation path
Question/path candidate -> simulate downstream effect on operator clarity or retrieval quality

Use when:
- route choice may affect future governance or answer safety

---

# 6. DMG role inside the optimization loop

DMG should be used as a generator/mutation subsystem, not mistaken for the whole system.

## DMG responsibilities in this architecture
- generate multiple question specs for a substantive objective
- generate route-aware variations
- generate mutation candidates
- generate suggestion bundles for internal vs external runs
- support prompt/path comparison experiments

## DMG should not be treated as
- the entire Dream path universe
- the sole source of substantive lane definitions
- the final arbiter of truth

---

# 7. Scoring model

Each path stack cell should be scored across at least these dimensions:

## Core dimensions
- usefulness
- contradiction_safety
- canonicality
- operator_clarity
- route_fit
- next_step_leverage
- drift_resistance

## Optional dimensions
- evidence_freshness
- reproducibility
- promotion_readiness
- public-wording_safety

## Output
Each cell should produce:
- score summary
- operator note
- keep / refine / drop recommendation

---

# 8. Phased rollout

## Phase O1 — capability surface map
Map the actual Dream Monkey execution-path surface and connect it explicitly to DMG and service routes.

## Phase O2 — objective-to-question map
For current Regina objectives, generate multi-family question sets.

## Phase O3 — path-stack pilot
Run a bounded pilot matrix using a small number of cells per objective.

## Phase O4 — comparative scoring
Score outputs and identify the best-performing path families.

## Phase O5 — adaptive optimization
Use the scoring results to favor the best question/path stacks in future Regina work.

---

# 9. Immediate Regina application

The current best immediate substantive objective remains:
- support-layer contradiction review + support communication comparison + graph/recall hardening

For that objective, the first true multi-step optimization pilot should compare path stacks like:

### Stack A
- objective: support contradiction review
- question family: contradiction
- Dream path: direct learning
- DMG role: question generation only
- route: internal validation

### Stack B
- objective: support communication comparison
- question family: comparison
- Dream path: learning + mutation
- DMG role: route-aware question variation
- route: external live learning with support/communication anchors

### Stack C
- objective: graph/recall hardening
- question family: governance/boundary
- Dream path: route comparison
- DMG role: mutation generation
- route: rerank-debug + internal validation

### Stack D
- objective: support promotion boundary
- question family: decision support
- Dream path: learning + bridge validation
- DMG role: suggestion generation
- route: internal validation + bridge review

---

# 10. Operating rule

From now on, questions should be treated as optimization seeds, not just prompts.

For every important Regina objective, the system should ask:
1. what is the substantive objective?
2. what question families should represent it?
3. what Dream path families should be compared?
4. what DMG generation/mutation role should be used?
5. what execution routes should run the cell?
6. how will the cell be scored?

Only then should runs be executed.

---

## Final judgment

The next evolution of Regina work should not be a single-lane DMG rerun.
It should be a **question-driven Dream Monkey + DMG multi-step optimization program**.

That is the correct frame for using the full capability surface rather than a flattened subset.
