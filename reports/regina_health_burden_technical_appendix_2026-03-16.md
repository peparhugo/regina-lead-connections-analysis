# Regina Lead Program — Technical Appendix: Child Cognitive Burden Envelope

Date: 2026-03-16  
Status: Public-facing technical appendix artifact

## Purpose
This appendix adds a narrow, conservative human-burden estimate to the Regina lead project.

It is designed to answer one limited question:

> If the current Regina evidence base is translated into a cautious child-development burden model, what does the child-cognitive burden lane look like under a conservative base case?

This appendix is intentionally narrow and should be read as a bounded technical estimate, not a headline claim.

---

## Appendix bottom line
Using a conservative mild developmental-burden crosswalk, a low assumed burden share, and a medium persistence horizon, the **child-cognitive lane alone** produces the following base-case model output under the appendix assumptions:

# **3.696 YLD-equivalent units**

This is a technical appendix estimate only.

---

## What is included
This appendix includes only:
- the **child cognitive / developmental burden lane**,
- a **proxy child exposure-context denominator** already used in the project,
- a **conservative disability-weight-equivalent crosswalk**,
- and a **medium-run duration assumption**.

### Fixed base-case inputs
- proxy child context: **1,540 children 0–14**
- incremental burden share: **3%**
- annual disability-weight-equivalent: **0.010**
- duration: **8 years**

### Base-case formula
`1,540 × 0.03 × 0.010 × 8 = 3.696`

---

## Why this appendix uses this framing
The current evidence base permits a cautious child-development burden framing because the project already includes peer-reviewed literature linking low-level lead exposure to:
- cognitive decrement,
- IQ-related developmental burden,
- and persistence into later developmental stages.

For this appendix, that evidence is translated into a **mild developmental cognitive-function burden equivalent**.

That phrasing is deliberate. It does **not** claim that Regina children in the proxy context are being counted as diagnosed intellectual disability cases.

---

## Why the estimate is conservative
This appendix is conservative in several ways:

1. It uses only the **child cognitive** lane.
2. It does **not** stack ADHD burden into the same total.
3. It does **not** include adult cardiovascular or kidney burden.
4. It does **not** include mortality or life-expectancy burden.
5. It uses a **low burden-share assumption** rather than applying burden to the full denominator.
6. It uses a **medium-run duration** instead of a lifetime annualized burden assumption.

---

## What this does not mean
This appendix estimate does **not** mean:
- Regina has a settled attributable burden of exactly **3.696 YLDs**,
- **3%** of Regina children are confirmed clinically affected,
- the project has identified all impacted families,
- the child proxy denominator is an audited harmed cohort,
- or the full human burden of Regina’s lead-service-line problem has been quantified.

It also does **not** mean that this estimate should be added directly to separate ADHD, cardiovascular, kidney, or mortality burden estimates without explicit overlap controls.

---

## How to read the number correctly
The right reading is:

- the current Regina evidence base supports a non-zero child-development burden concern,
- that burden can be translated into a cautious technical envelope,
- and under conservative assumptions the child-cognitive lane alone produces a non-zero burden estimate that is material enough to document in a technical appendix.

The wrong reading is:

- “Regina definitively lost 3.696 YLDs,”
- or “this is the final total human cost.”

It is neither of those things.

---

## Why this is appendix-only
This estimate is suitable for a technical appendix because it has:
- a pinned developmental-burden crosswalk,
- fixed base-case assumptions,
- explicit exclusions,
- and explicit proxy-denominator caveats.

It is **not intended** for:
- homepage use,
- slogan-level public messaging,
- or adversarial one-line burden claims.

---

## Source path
Method basis and hardening details are documented in:
- `reports/regina_child_burden_crosswalk_duration_hardening_2026-03-16.md`
- `reports/regina_burden_weight_literature_review_2026-03-16.md`
- `reports/regina_flint_calibration_memo_2026-03-16.md`
- `data/derived/regina_child_cognitive_burden_hardened_basecase_2026-03-16.csv`

---

## Recommended publication posture
Use this appendix as:
- a technical note,
- a burden-method appendix,
- or an operator-facing support artifact.

Do not use it as a stand-alone headline or as proof that Regina-specific child clinical surveillance has already been completed.
