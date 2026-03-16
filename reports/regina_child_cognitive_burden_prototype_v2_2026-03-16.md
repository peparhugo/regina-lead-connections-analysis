# Regina Lead Program — Child Cognitive Burden Prototype v2

Date: 2026-03-16  
Status: Recalibrated after literature review, burden-source-family selection, and Flint comparator review

## What changed from v1
Version 1 was an intentionally simple QALY-equivalent bridge.

Version 2 is more defensible because it now rests on:
1. a chosen **burden-weight source family**,
2. a clarified role for Flint as **calibration comparator only**, and
3. a more conservative interpretation of what the current Regina proxy-context data can support.

---

## Chosen framing
### Primary framing
**GBD-style disability-weight / YLD-equivalent planning envelope**

### Why this is now preferred over direct QALY language
At this stage the model still lacks:
- exact endpoint-to-utility crosswalk selection,
- exact duration validation,
- and validated overlap controls with ADHD or other downstream outcomes.

A disability-weight-equivalent / YLD-style planning envelope is therefore more defensible than claiming a formal Regina QALY estimate.

---

## Scope
Still intentionally narrow:
- child cognitive burden only,
- no ADHD stacking,
- no adult chronic disease stacking,
- no mortality lane,
- no single public headline citywide burden total.

---

## Inputs used
### Population basis
- children 0–14 in the current proxy exposure context: **1,540**

Guardrail:
- this is a proxy-context figure, not an audited harmed cohort.

### Formula
`proxy_children_context × incremental_burden_share × disability_weight_equivalent × duration_years`

This remains an illustrative model, but it is now more tightly framed.

---

## Scenario assumptions and outputs

| Scenario | Incremental burden share | Disability-weight-equivalent per affected child-year | Duration | YLD-equivalent loss |
|---|---:|---:|---:|---:|
| Low | 1% | 0.005 | 3 years | 0.231 |
| Base | 3% | 0.010 | 8 years | 3.696 |
| High | 7% | 0.020 | 12 years | 25.872 |

CSV artifact:
- `data/derived/regina_child_cognitive_burden_prototype_v2_2026-03-16.csv`

---

## Why the v2 numbers are lower than the earlier prototype
That is intentional.

After the literature review, the safer method is to:
- narrow the burden lane further,
- reduce the chance of implicit overclaiming,
- and treat the current Regina denominator as a proxy exposure context rather than a harmed-case count.

So v2 is a better planning artifact even if it is less dramatic.

---

## How Flint affected v2
Flint did **not** determine the numeric values directly.

Instead, Flint supports keeping a meaningful upper envelope on the table because it shows that municipal water-system lead failures can produce measurable child blood-lead impact.

So Flint influences:
- seriousness calibration,
- not direct value transfer.

---

## Interpretation
### Low scenario — 0.231 YLD-equivalent loss
A very conservative lower envelope.
Appropriate if one assumes only a small fraction of the proxy child context carries incremental burden and that the decrement is very mild and limited in duration.

### Base scenario — 3.696 YLD-equivalent loss
This is the recommended current planning anchor.
It is still conservative but more realistic than the minimum case.

### High scenario — 25.872 YLD-equivalent loss
This is an upper envelope for the narrow child cognitive lane only.
Even this does not include ADHD burden, adult chronic disease burden, or mortality burden.

---

## What v2 does and does not support
### Supports
- a more defensible burden-envelope prototype,
- a documented reason for preferring YLD-style framing first,
- a clearer separation between source family and comparator calibration,
- and a cleaner bridge to later hardening.

### Does not support
- a public headline like “Regina lost X DALYs,”
- a final burden estimate,
- or a merged total across all lead-related endpoints.

---

## Hardening pass outcome
The next hardening pass has now been completed in:
- `reports/regina_child_burden_crosswalk_duration_hardening_2026-03-16.md`
- `data/derived/regina_child_cognitive_burden_hardened_basecase_2026-03-16.csv`

Key result:
- pinned crosswalk = **mild developmental cognitive-function burden equivalent**
- pinned base-case duration = **8 years**
- hardened base-case result = **3.696 YLD-equivalent loss**
- publication decision = **technical appendix yes, headline public use no**

---

## Bottom line
Version 2 is a better analytic bridge than Version 1.

It is:
- more conservative,
- more literature-aware,
- more methodologically honest,
- and better aligned with what the current Regina evidence base can actually support.
