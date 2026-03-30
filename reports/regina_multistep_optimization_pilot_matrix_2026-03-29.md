tags: [regina:canonical, regina:dream, regina:dmg, regina:pilot-matrix]
created_by: ChaosClaw
created_at: 2026-03-29T08:53:00+02:00

# Regina multi-step optimization pilot matrix — 2026-03-29

Status: canonical pilot design
Purpose: define the first bounded path-stack pilot for question-driven Dream Monkey + DMG optimization, using a small number of cells that are meaningful enough to compare while remaining auditably bounded.

---

## Executive decision

Start with a **4-stack pilot matrix**.

This is large enough to compare materially different path-stack strategies, but small enough to execute and score without losing operator visibility.

---

## Pilot objective set

The first pilot should optimize for three tightly connected Regina objectives:

1. **support contradiction discipline**
2. **support communication comparison**
3. **graph/recall boundary hardening**

These are the highest-value post-recovery objectives because they test whether the rebuilt control plane can produce useful next actions without reintroducing drift.

---

## Pilot matrix structure

Each cell includes:
- substantive objective
- question family
- Dream path family
- DMG role
- execution route
- expected operator value

---

## Stack A — internal contradiction stack

### Purpose
Pressure-test current support-layer boundaries against internal canonical artifacts.

### Configuration
- substantive objective: `support-layer contradiction review`
- question family: `contradiction`
- Dream path family: `direct learning path`
- DMG role: `question generation only`
- execution route: `internal_validation_service.py`

### Primary output target
- contradiction bundle
- governing artifact stack reinforcement
- support-only vs canonical boundary recommendations

### Why include it
This is the strongest currently validated internal stack and serves as the baseline anchor.

---

## Stack B — internal decision stack

### Purpose
Convert current contradiction/boundary evidence into operator-grade next-step decisions.

### Configuration
- substantive objective: `support promotion / demotion decision support`
- question family: `operator decision support`
- Dream path family: `direct learning path`
- DMG role: `question generation only`
- execution route: `internal_validation_service.py`

### Primary output target
- preserve / promote / demote guidance
- next-lane recommendation inputs
- operator-facing prioritization bundle

### Why include it
This stack has already shown immediate productivity and pairs well with Stack A.

---

## Stack C — external support communication comparison stack

### Purpose
Find external comparison patterns for support communication, uncertainty framing, appendix discipline, and pseudo-precision control.

### Configuration
- substantive objective: `support communication comparison`
- question family: `support communication comparison`
- Dream path family: `learning + mutation path`
- DMG role: `route-aware question variation`
- execution route: `project_scoped_live_learning.py` with support/communication-specific query anchoring

### Primary output target
- accepted comparison findings
- comparison patterns worth importing
- route-quality evidence for support communication questions

### Why include it
This is the most important external stack to evaluate fairly after correcting the technical-scope drift in earlier question generation.

---

## Stack D — graph/recall boundary hardening stack

### Purpose
Test and improve whether support-layer boundaries survive in live retrieval/ranking behavior.

### Configuration
- substantive objective: `graph/recall boundary hardening`
- question family: `governance/boundary`
- Dream path family: `route comparison path`
- DMG role: `mutation generation`
- execution route: `internal validation + rerank-debug comparison`

### Primary output target
- boundary-query route comparisons
- ranking failure / improvement evidence
- next retrieval-hardening actions

### Why include it
This is the direct bridge from support-layer review into retrieval safety.

---

## Question count rule

To keep the pilot bounded:
- **2 questions per stack**
- **8 total questions**

This is smaller than the earlier 12-question Wave A sweep because the optimization unit is now richer (each stack is more structured).

---

## Proposed question families per stack

## Stack A questions
1. Which current support-layer artifacts most risk contradiction with canonical current-state truth if not explicitly bounded?
2. What internal evidence most strongly supports keeping support-layer burden materials support-only rather than canonical/public truth?

## Stack B questions
1. Which support-layer artifacts should be preserved as support-only, promoted, or demoted right now?
2. Which contradiction-review findings most change the next Regina lane choice?

## Stack C questions
1. What external public-interest or public-health communication patterns best separate technical appendices from headline claims without pseudo-precision?
2. What comparison examples best preserve public usefulness while maintaining scenario-envelope / bounded-estimate discipline?

## Stack D questions
1. Which current boundary queries still risk surfacing support-layer artifacts above canonical state truth?
2. What ranking/debug interventions most improve support-vs-canonical boundary preservation in live Regina retrieval?

---

## Scoring model for the pilot

Each stack should be scored on a 1–5 basis across:
- usefulness
- contradiction_safety
- canonicality
- operator_clarity
- route_fit
- next_step_leverage
- drift_resistance

### Optional bonus dimensions
- evidence_freshness
- reproducibility
- promotion_readiness

---

## Decision rules after pilot

### Keep / expand a stack when
- average core score is high,
- findings are concrete,
- operator action is clearer after the run,
- contradiction safety remains strong.

### Refine a stack when
- route_fit is weak,
- question-family quality appears good but route or query anchoring is off,
- some useful findings appear but noise remains high.

### Drop or demote a stack when
- findings are generic,
- route mismatch remains strong,
- operator clarity does not improve,
- the stack creates more ambiguity than resolution.

---

## Execution order

Recommended order:
1. Stack A
2. Stack B
3. Stack C
4. Stack D

Reason:
- internal stacks anchor the current truth first;
- external communication comparison then adds bounded fresh information;
- graph/recall hardening then uses the improved boundary understanding.

---

## Immediate next execution step

Materialize the pilot as a run-local matrix artifact with:
- stack definitions
- per-stack question specs
- scoring sheet
- audit output contract

Then execute Stack A and Stack B first as the internal baseline half.
