tags: [regina:canonical, regina:support, regina:contradiction-review, regina:control]
created_by: ChaosClaw
created_at: 2026-03-29T08:17:00+02:00

# Regina support-layer contradiction review — 2026-03-29

Status: active substantive-lane checkpoint
Purpose: begin the post-recovery substantive Regina lane by reviewing support-layer burden and appendix artifacts for contradiction risk, claim-envelope drift, and required demotion/preservation rules.

---

## Executive summary

The support-layer burden artifacts are broadly usable, but only under a strict lane split.

### Main judgment
The current support-layer burden materials are **not fundamentally invalid**, but they contain several predictable contradiction/drift hazards if they are allowed to leak upward into public-facing or canonical state language without explicit envelope controls.

### Core conclusion
The support layer should remain active, but under this rule:
- **support-layer burden outputs are support-only unless explicitly promoted through claim-control gates**.

That rule is consistent with the existing support-lane note and with the broader recovery doctrine.

---

## Reviewed artifact set

Primary support-layer entry artifacts reviewed in this pass:
- `reports/regina_support_lane_review_note_2026-03-28.md`
- `reports/regina_health_burden_public_table_2026-03-16.md`
- `reports/regina_health_burden_technical_appendix_2026-03-16.md`
- `reports/regina_healthy_life_burden_scenarios_2026-03-16.md`
- `reports/regina_health_burden_qaly_framework_2026-03-16.md`

---

## Existing lane guardrail already present

The support-lane review note already contains the correct control principle:
- support-layer and appendix-adjacent artifacts must stay separate from public package and control-surface work;
- support-layer language must not silently widen the public claim envelope;
- required reviews are provenance review, method review, contradiction review, and claim-envelope review.

This contradiction review adopts that rule as governing policy.

---

## Contradiction-risk assessment by artifact class

### 1. Conservative public burden table
Artifact:
- `regina_health_burden_public_table_2026-03-16.md`

#### Strength
This artifact is relatively safe because it repeatedly says what should **not** be claimed yet.
It is framed as conservative and public-safe.

#### Contradiction risk
Moderate.
Why:
- it is public-oriented, but still discusses burden lanes that could be misread as more quantified than they are;
- it invites inference about human harm while trying to avoid numeric overclaim.

#### Control rule
Keep as **supporting/public-safe framing aid**, not as proof of a settled quantified burden total.

#### Status
**Preserve, no demotion required, but do not allow numeric implication creep.**

---

### 2. Technical appendix burden envelope
Artifact:
- `regina_health_burden_technical_appendix_2026-03-16.md`

#### Strength
This artifact is unusually careful.
It explicitly says:
- appendix-only
- bounded inherited modeled estimate
- not a citywide settled total
- not a confidence interval
- not suitable for homepage or slogan-level use

#### Contradiction risk
Low-to-moderate internally, high if quoted lazily elsewhere.
The main contradiction hazard is not the artifact itself, but downstream misuse of its numeric center/range as if it were validated population truth.

#### Control rule
Treat as **support-only technical appendix**.
Its numeric outputs must remain inherited-modeled-envelope language only.

#### Status
**Preserve strongly.** This is a good support-layer artifact precisely because it carries its own caveats.

---

### 3. Healthy-life-burden scenarios sheet
Artifact:
- `regina_healthy_life_burden_scenarios_2026-03-16.md`

#### Strength
Good scenario discipline:
- low / base / high framing
- repeated refusal to publish a settled citywide QALY/DALY total
- clear readiness table
- clear recommendation to start with low scenario only

#### Contradiction risk
Moderate.
Why:
- scenario sheets can drift into pseudo-results if later readers forget they are scenario envelopes rather than accepted outputs;
- the base/high framing can be overread as endorsement rather than exploratory structure.

#### Control rule
Treat as **planning/support artifact**, not canonical burden truth.
When cited, require the phrase that it is a scenario envelope, not a settled total.

#### Status
**Preserve, with explicit “scenario-only” boundary.**

---

### 4. QALY/DALY framework memo
Artifact:
- `regina_health_burden_qaly_framework_2026-03-16.md`

#### Strength
This is strong as a framework memo.
It clearly separates:
- public narrative layer
- conservative burden table
- technical appendix/model layer
- anti-double-counting guardrails

#### Contradiction risk
Moderate.
Why:
- framework memos often read more mature than the underlying model actually is;
- readers may mistake “model structure exists” for “model outputs are decision-settled.”

#### Control rule
Treat as **method/framework support**, not as proof that full burden quantification is complete.

#### Status
**Preserve.** Keep under support/method layer, not canonical state layer.

---

## Main contradiction/drift hazards identified

### Hazard A — appendix numerics leaking into headline truth
Example risk:
- bounded technical appendix outputs later cited as if they were validated citywide burden totals.

### Hazard B — scenario envelope mistaken for settled burden estimate
Example risk:
- low/base/high burden scenarios later described as accepted burden findings.

### Hazard C — framework maturity overstated as model maturity
Example risk:
- QALY/DALY framework existence later used to imply the burden model is complete.

### Hazard D — support-layer human-burden framing silently widening the public package
Example risk:
- support-only burden language gradually becoming homepage/public-brief language without explicit promotion review.

---

## Contradiction review decisions

### Preserve as support-only, no demotion
- `regina_health_burden_public_table_2026-03-16.md`
- `regina_health_burden_technical_appendix_2026-03-16.md`
- `regina_healthy_life_burden_scenarios_2026-03-16.md`
- `regina_health_burden_qaly_framework_2026-03-16.md`

### Explicit non-promotion rule
None of the above should be treated as:
- canonical current-state truth,
- proof of a settled Regina burden total,
- or public-package headline language,
unless separately promoted through claim-control review.

### No invalidation required in this pass
Current review does **not** find these artifacts invalid.
The problem is mainly potential misuse, not internal contradiction severe enough to invalidate them outright.

---

## Promotion / citation rules to use going forward

When these artifacts are cited outside the support lane:

### Allowed citation shape
- “support-layer / appendix-only”
- “bounded modeled estimate”
- “scenario envelope”
- “framework memo, not settled total”

### Disallowed citation shape
- “Regina’s burden is X”
- “the appendix proves Y citywide burden”
- “the QALY model is complete”
- “the scenarios establish a settled total”

---

## Immediate graph/recall hardening implication

These support artifacts should be queryable, but retrieval must preserve:
- canonical current-state truth above support-layer burden artifacts;
- explicit support-only labeling;
- separation between burden framework, scenario sheet, and canonical state answers.

That makes this contradiction review directly relevant to the graph/recall hardening sub-lane.

---

## Recommended next action in this phase

Next step:
- promote a small set of support-layer boundary claims into retrieval/graph surfaces so support artifacts remain discoverable **without** outranking canonical state truth.

That would complete the first serious post-recovery use of the rebuilt control plane.
