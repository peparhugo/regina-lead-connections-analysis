# Regina Lead Program — Healthy-Life-Burden Scenarios (Low / Base / High)

Date: 2026-03-16  
Status: Conservative scenario sheet for public-health framing and future QALY/DALY implementation

## Purpose
This document is the first bridge between:
- the public-facing claim that lead-service-line delay has a human cost, and
- a future formal QALY/DALY model.

It does **not** publish a single settled Regina QALY or DALY number.
Instead, it defines a defensible **low / base / high** scenario envelope so later modeling stays conservative, explicit, and reviewable.

---

## What this scenario sheet does
It translates the current evidence base into three scenario frames:
- **Low:** use only the narrowest, most defensible burden framing.
- **Base:** use the strongest currently supported child + adult burden lanes with conservative overlap handling.
- **High:** reflect a broader life-course burden view while still avoiding unsupported city-level attributable claims.

---

## Current evidence anchors already in repo
This scenario sheet relies on evidence already assembled in the project for:
- **IQ / child cognitive burden**
- **ADHD / behavioural burden**
- **cardiovascular burden**
- **CKD / kidney burden**

Population context already in repo:
- remaining active lead connections: **2,442**
- impacted people proxy: **8,319**
- impacted children 0–14 proxy-context figure: **1,540**

Important guardrail: these are **proxy context figures**, not audited harmed cohorts.

---

## Scenario table (public-health framing)

| Scenario | Burden lanes included | Population basis | Human-impact interpretation | Main exclusions / controls | Confidence |
|---|---|---|---|---|---|
| Low | Child cognitive burden only | Child proxy context near remaining lead burden | Delay may carry a measurable child-development cost even under narrow assumptions | Excludes ADHD as separate count, excludes adult chronic disease, excludes mortality, excludes downstream education/earnings stacking | Medium-High |
| Base | Child cognitive burden + ADHD-type burden + cautious adult chronic disease framing | Child proxy context + broader people proxy context | Delay likely carries both child-development burden and some long-run adult health burden | ADHD must not be fully stacked on top of IQ burden without overlap controls; adult burden stays conservative and risk-framed, not fully attributed | Medium |
| High | Child cognitive burden + ADHD-type burden + broader life-course chronic disease framing + healthy-life-years framing | Child and broader people proxy contexts under a full scenario envelope | Delay may produce development, behaviour, and chronic-disease burden across the life course, affecting quality of life and healthy years | Still excludes one-number headline unless utility mapping, duration assumptions, and overlap controls are completed | Low-Medium |

---

## Scenario implementation logic

### Low scenario
This is the safest public-health burden interpretation.

It assumes:
- the most defensible and best-established burden lane is **child cognitive harm**,
- the project can already say that lead exposure is linked in the literature to developmental burden,
- the public message can focus on children’s development without needing to fully quantify adult disease burden.

### Base scenario
This is the recommended current working scenario.

It assumes:
- child cognitive burden remains the strongest lane,
- ADHD-type burden is important enough to include,
- adult cardiovascular and kidney burden should be acknowledged cautiously,
- overlap controls are required before any numeric aggregation.

This scenario is the best fit for current public and operator use.

### High scenario
This is the broadest still-defensible scenario envelope.

It assumes:
- the burden is truly life-course,
- child developmental harms and later chronic disease harms both matter,
- the right public-health language includes quality of life and healthy years at risk,
- but a single citywide headline number still should not be published yet.

---

## If converted later into QALY/DALY modeling

### Low scenario → likely first numeric implementation
Recommended future burden unit:
- **QALY decrement envelope** or **YLD-style burden envelope** for child cognitive harm only

Why first:
- narrowest scope,
- lowest overlap risk,
- easiest to defend publicly.

### Base scenario → recommended medium-term implementation
Recommended future burden unit:
- **separate lane outputs**, not one immediately summed headline:
  - child neurodevelopment burden,
  - adult chronic-disease burden,
  - quality-of-life framing note.

Why:
- keeps the project decision-grade,
- avoids premature aggregation.

### High scenario → later synthesis only
Recommended future burden unit:
- integrated QALY/DALY scenario only after:
  - utility/disability-weight selection,
  - duration assumptions,
  - overlap rules,
  - uncertainty presentation discipline.

---

## Quantification readiness table

| Burden lane | Numeric modeling readiness | Best next step |
|---|---|---|
| Child cognitive burden | Medium | define utility / disability-weight approach for developmental decrement |
| ADHD-type burden | Medium | map incremental burden without double-counting cognitive lane |
| Adult cardiovascular burden | Low-Medium | define incidence/severity mapping from current evidence anchors |
| Adult CKD burden | Low-Medium | define duration and severity mapping |
| Single integrated healthy-life-years headline | Low | do not publish until overlap controls and utility mapping are completed |

---

## Public-safe summary lines

### Safest one-line version
Lead-service-line delay is not only a cost problem — even under narrow assumptions, it may also carry a child-development burden.

### Recommended public version
Lead-service-line delay should be understood in both financial and human terms: the literature supports concern about child-development burden now, and broader quality-of-life and chronic-disease burden over time.

### Strongest still-conservative version
Even before publishing a single citywide QALY estimate, the current evidence base supports a clear conclusion: delay can matter not only for budgets, but for development, health, and healthy years of life put at risk.

---

## What this sheet does not claim
This sheet does **not** claim:
- a settled Regina QALY total,
- a settled Regina DALY total,
- audited citywide case counts,
- or a fully attributed chronic-disease burden already quantified for Regina.

It is a scenario envelope for disciplined next-step modeling.

---

## Recommended next move
Build the first numeric burden prototype using the **Low scenario only**:
1. child cognitive burden lane,
2. explicit low/base/high duration assumptions,
3. one utility/disability-weight method,
4. no stacking with ADHD or adult chronic disease yet.

That will produce the cleanest first numeric burden output without overshooting the evidence.

Prototype completed in this pass:
- `reports/regina_child_cognitive_burden_prototype_2026-03-16.md`
- `data/derived/regina_child_cognitive_burden_prototype_2026-03-16.csv`

### Status update
A first prototype now exists:
- `reports/regina_child_cognitive_burden_prototype_2026-03-16.md`
- `data/derived/regina_child_cognitive_burden_prototype_2026-03-16.csv`

Important guardrail: this prototype still uses placeholder sensitivity assumptions and should not be treated as a final public QALY headline.
