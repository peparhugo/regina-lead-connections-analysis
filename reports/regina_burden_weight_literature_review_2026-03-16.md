# Regina Lead Program — Peer-Reviewed Literature Review for Burden Weighting and Calibration

Date: 2026-03-16  
Status: Focused literature review to support Phase A/B/C of the human-burden model

## Why this review was run
The project moved from:
- policy/delivery analysis,
- to public human-impact framing,
- to a first numeric child-burden prototype.

Before that prototype can be treated as more than illustrative, it needs stronger support from peer-reviewed literature in three areas:
1. **lead-related child outcome evidence**,
2. **documented burden-weight / utility-weight source families**, and
3. **comparator-case calibration evidence** such as Flint.

---

## Search tracks run
Machine-readable search outputs created in this pass:
- `reports/lit_child_burden_weights_2026-03-16.json`
- `reports/lit_flint_calibration_2026-03-16.json`
- `reports/lit_lead_child_outcomes_2026-03-16.json`

Queries used:
- `lead exposure children cognitive impairment disability weight utility quality of life`
- `Flint Michigan lead exposure children cognition quality of life burden educational outcomes`
- `lead exposure children IQ ADHD long term cohort meta analysis blood lead low level`

### Important search note
The broad scholarly aggregation step returned **some useful records and a lot of noisy retrievals**. This is normal for cross-source literature aggregation. The practical outcome is:
- use the search outputs as a triage pool,
- rely on already-curated endpoint anchors where available,
- and use only the cleaner comparator papers for calibration logic.

---

## Curated peer-reviewed anchors used in this phase

### Child cognition / developmental harm
1. **Lanphear et al. 2005**  
   *Low-Level Environmental Lead Exposure and Children’s Intellectual Function: An International Pooled Analysis*  
   DOI: `10.1289/ehp.7688`  
   Role: strongest existing pooled anchor in repo for low-level lead and IQ decrement.

2. **Needleman et al. 1990**  
   *Low-Level Lead Exposure and the IQ of Children*  
   DOI: `10.1001/jama.1990.03440050067035`  
   Role: longstanding synthesis anchor for low-level exposure and IQ harm.

3. **Heidari et al. 2022**  
   systematic review/meta-analysis  
   DOI: `10.1186/s13643-022-01963-y`  
   Role: later review anchor supporting cognitive harm signal.

### ADHD / behavioural burden
4. **Goodlad et al. 2013**  
   *Lead and Attention-Deficit/Hyperactivity Disorder (ADHD) symptoms: A meta-analysis*  
   DOI: `10.1016/j.cpr.2013.01.009`  
   Role: core ADHD signal anchor.

5. **Dimitrov et al. 2024**  
   systematic review/meta-analysis  
   DOI in existing registry: `10.1007/s11121-023-01617-z`  
   Role: updated ADHD association anchor already curated in repo.

### Comparator calibration case
6. **Pediatric lead exposure and the water crisis in Flint, Michigan** (2017)  
   DOI: `10.1097/01.jaa.0000511794.60054.eb`  
   Role: practical comparator anchor. Crossref abstract states that elevated blood lead incidence in children in the affected Flint area nearly doubled after the source-water change.

### Burden-weight source family
7. **Global Burden of Disease disability-weight literature family**  
   Used here as the preferred source family for a **YLD-style / disability-weight-equivalent approach**.

8. **Estimated disability weights for the severity of health outcomes: a systematic review and meta-analysis** (2025)  
   PubMed indexed; useful as secondary context for variability in disability-weight estimates, but not the primary source family chosen here.

---

## Phase A conclusion — preferred burden-weight source family
### Chosen primary family
**GBD disability weights / YLD-style framing**

### Why this family was chosen
It is the best fit for this stage because it:
- is recognized and widely used,
- is designed for healthy-life-burden communication,
- works better for public-health burden framing than ad hoc utility guesses,
- and supports a conservative non-fatal burden pathway without forcing a premature cost-effectiveness style QALY headline.

### Why not use Flint as the weight source
Flint is a **comparator case**, not a burden-weight source family.
Flint can help calibrate plausible burden-share or severity envelopes, but it should not determine the disability weight itself.

### Why not jump straight to condition-specific utility papers only
Condition-specific utilities may later refine the model, but at this stage they create a risk of:
- patchwork sourcing,
- poor comparability,
- and uncontrolled overlap between cognitive, behavioural, and educational pathways.

So the cleanest first hardening path is:
- **GBD-style burden frame first**,
- then condition-specific refinements later.

---

## Phase B conclusion — how Flint should be used
### Flint should be used as:
- an **external calibration and sensitivity anchor**,
- an example of what a severe municipal lead exposure failure can look like,
- and a plausibility bound for child-risk concern.

### Flint should not be used as:
- a one-to-one estimate for Regina,
- proof that similar water numbers imply identical burden,
- or a direct substitute for Regina-specific exposure prevalence.

### Reason
Flint and Regina can differ in:
- exposure duration,
- corrosion chemistry,
- surveillance intensity,
- age structure,
- timing of response,
- baseline housing/environmental conditions,
- and case ascertainment.

So Flint is strongest as a **bounding case**, not as a direct transfer model.

---

## Phase C implication — what changed in the numeric prototype
The first prototype used transparent placeholder utility assumptions.

After this review, the model direction changes to:
- a **GBD/YLD-style disability-weight-equivalent framing**,
- with Flint only used to justify conservative scenario bounding,
- and with the child-cognitive lane still kept separate from ADHD and adult chronic disease.

This means the recalibrated prototype should be:
- narrower,
- more conservative,
- more explicit about uncertainty,
- and less likely to be mistaken for a settled citywide attributable total.

---

## Recommended modeling discipline after this review
1. Keep the first numeric lane as **child cognitive burden only**.
2. Express it as **disability-weight-equivalent / YLD-style burden** or **QALY-equivalent planning envelope**, not a final settled QALY figure.
3. Use Flint only to inform upper/lower sensitivity thinking.
4. Do not stack ADHD into the same total until overlap control is explicit.
5. Do not stack adult chronic disease into the same total in this phase.

---

## Bottom line
This review supports the following method choice:
- **Phase A:** choose a GBD disability-weight / YLD-style source family
- **Phase B:** use Flint as a calibration comparator only
- **Phase C:** recalculate the child-cognitive prototype with more conservative, explicitly bounded assumptions

That is the cleanest path from public narrative to defensible burden modeling without pretending that Regina-specific household-level clinical surveillance exists.
