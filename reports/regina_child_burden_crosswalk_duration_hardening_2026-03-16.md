# Regina Lead Program — Child Burden Crosswalk and Duration Hardening Pass

Date: 2026-03-16  
Status: Method hardening pass for the child-cognitive burden lane

## Purpose
This memo completes the next hardening step for the Regina burden model by doing four things:
1. pinning the closest developmental-burden health-state crosswalk,
2. tightening the duration logic,
3. recomputing the base-case child burden under fixed assumptions, and
4. deciding whether the current base-case YLD-equivalent envelope is clean enough for a public appendix.

This pass is intentionally conservative.

---

## 1) Health-state crosswalk decision

### Chosen crosswalk
The closest defensible crosswalk for the current Regina child-cognitive lane is:

**mild developmental intellectual / cognitive functioning burden equivalent**

In practice, this should be treated as a **GBD-style mild developmental cognitive-burden proxy**, not as a claim that exposed Regina children meet diagnostic criteria for intellectual disability.

That distinction matters.

### Why this is the closest fit
The current lead evidence base in the project supports:
- low-level lead exposure linked to IQ decrement,
- persistent cognitive effects into later childhood/adolescence,
- and child-development burden that is meaningful but usually **subclinical-to-mild distributed impairment**, not automatically diagnosed intellectual disability.

So the model should **not** crosswalk directly to a moderate or severe neurodevelopmental disability state.

It also should **not** pretend that an average IQ decrement is equivalent to a diagnosed disability case.

The closest defendable bridge is therefore:
- a **mild developmental cognitive-function burden equivalent**,
- applied only to an assumed incremental share of children in the proxy exposure context,
- at a deliberately discounted annual burden weight.

### Why this is more defendable than direct IQ-to-diagnosis conversion
Because it avoids saying:
- “lead caused X diagnosed disability cases,”
- or “all children in the exposure context carry the same burden.”

Instead it says:
- there is a distributed developmental burden signal,
- a subset of the proxy child context likely carries incremental harm,
- and the burden weight should be mild and conservative.

---

## 2) Source-family logic for the annual burden weight

### Source-family retained
**GBD-style disability-weight / YLD-equivalent framing** remains the chosen source family.

### Exact weighting approach used in this hardening pass
Because the current project does not yet pin a single exact published GBD health-state coefficient for this specific lead-linked developmental distribution, the safest move is:
- keep the crosswalk fixed at **mild developmental cognitive-burden equivalent**,
- keep the annual burden weight conservative,
- and explicitly state that the numeric coefficient is a **crosswalk-equivalent planning value**, not a claimed one-to-one GBD label transfer.

### Fixed annual base-case coefficient
**0.010 disability-weight-equivalent per affected child-year**

### Why 0.010 remains defensible for the base case
This value is intentionally mild.

It reflects:
- a burden level below what many full syndrome/disability states would imply,
- a distributed developmental decrement rather than a fully expressed diagnostic case,
- and the need to avoid overstating quality-of-life loss from an IQ-shift literature base alone.

In plain language:
- it is a small annual burden weight,
- used only for a subset of children in the proxy context,
- and therefore functions as a conservative translation device rather than a maximalist claim.

---

## 3) Duration hardening

### Chosen base-case duration
**8 years**

### Why 8 years is the preferred base case
The project’s child-cognitive literature supports persistence beyond immediate exposure windows.
Key anchors already in repo include:
- **Lanphear et al. 2005** — low-level lead and child intellectual function,
- **Heidari et al. 2022** — meta-analytic support for cognitive effects, with larger deficits under longer exposure duration,
- **Halabicky et al. 2023** — association between blood lead in early childhood and adolescent IQ.

This supports a duration assumption that is:
- longer than a short transient school-year effect,
- but still more conservative than assuming lifelong full-severity burden in the first hardening pass.

### Why not use 3–5 years as base case
That is probably too short given the literature suggesting persistence into later developmental windows.

### Why not use lifetime duration as base case
That would be harder to defend at this stage because:
- the current model is not yet structured around lifelong utility tracking,
- the evidence base supports persistence but not a clean single lifetime annualized decrement assumption,
- and a shorter medium-run window is more conservative for first public-facing hardening.

### Duration decision
Use:
- **Low:** 3 years
- **Base:** 8 years
- **High:** 12 years

That is the current best disciplined spread.

---

## 4) Fixed base-case model inputs

### Population denominator
- proxy child context: **1,540 children 0–14**

### Incremental burden share
**3%**

### Why 3% is kept as base case
This remains conservative because:
- the denominator is a proxy exposure context, not a harmed cohort,
- not all exposed children will carry meaningful persistent cognitive burden,
- and a low single-digit share better reflects uncertainty than a broad application to the full denominator.

### Base-case formula
`1,540 × 0.03 × 0.010 × 8 = 3.696`

### Base-case result
**3.696 YLD-equivalent loss**

---

## 5) What this base-case number means
It means:
- under a conservative mild developmental-burden crosswalk,
- using a low burden-share assumption,
- and using a medium persistence horizon,
- the child-cognitive lane alone produces a non-zero, non-trivial burden envelope.

It does **not** mean:
- Regina has a settled attributable burden of exactly 3.696 YLDs,
- 3% of all children are confirmed clinically affected,
- or the project has now quantified the full human cost of the lead-service-line issue.

This remains a **bounded planning envelope**.

---

## 6) Public appendix decision

### Decision
**Conditional yes — but only as a technical appendix, not a headline public claim.**

### Why yes
The model is now stronger because it has:
- a pinned crosswalk,
- a clearer duration justification,
- a fixed base-case coefficient,
- explicit denominator caveats,
- and explicit exclusion of ADHD/adult/mortality stacking.

### Why only conditional
It still depends on:
- a proxy child denominator,
- a crosswalk-equivalent burden coefficient rather than a fully validated condition-specific weight,
- and scenario assumptions that remain partly inferential.

So the number is not clean enough for:
- homepage use,
- one-line public messaging,
- or adversarial “gotcha-proof” headline deployment.

But it **is** clean enough for:
- a technical appendix,
- a methods note,
- or an operator-facing burden annex with very explicit guardrails.

---

## 7) Recommended appendix wording

### Public-safe appendix sentence
Using a conservative mild developmental-burden crosswalk, low assumed burden share, and medium persistence horizon, the child-cognitive lane alone yields a base-case burden envelope of roughly **3.7 YLD-equivalent units**. This is an illustrative technical estimate, not a settled citywide attributable burden total.

### Guardrail sentence
This appendix estimate is based on proxy exposure context and should not be read as a diagnosed-case count, a final attributable burden estimate, or a merged total across all lead-related harms.

---

## 8) Recommendation
For the current project stage:
- keep the base-case value in the technical appendix layer only,
- do not move it to the homepage,
- do not merge it with ADHD or adult chronic disease yet,
- and do one later pass to pin the nearest named GBD health-state coefficient more explicitly if a source table can be locked cleanly.

---

## Bottom line
This hardening pass improves the model enough to support a **technical appendix-grade base-case burden envelope**.

It does **not** yet support a simple public burden headline.
