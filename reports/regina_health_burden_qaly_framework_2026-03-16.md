# Regina Lead Program — Health Burden and QALY/DALY Framework

Date: 2026-03-16  
Status: Conservative analytical framework for public-facing use and future model implementation

## Purpose
This memo adds the missing human-impact layer to the Regina lead program project.

The current public bundle already shows:
- what Council and committee decided,
- what changed in program design,
- what remains unproven in the decision-to-delivery chain, and
- what financial burden may be associated with lead-related harms.

What it does **not** yet fully communicate is the burden to actual lives:
- child cognitive and behavioural harm,
- later-life chronic disease burden,
- reduced quality of life,
- healthy years of life lost,
- and the difference between policy delay and prevention.

This memo provides a defensible structure for that layer.

---

## Bottom line
Lead exposure should not be framed only as a financing or infrastructure problem.

The stronger public-health framing is:
1. delayed replacement can mean prolonged exposure,
2. prolonged exposure can mean lasting developmental and chronic-disease harms,
3. those harms affect not only public budgets but also cognition, schooling, behaviour, cardiovascular risk, kidney risk, and healthy life years,
4. therefore the cost of delay should be described in both **financial terms** and **human-life-burden terms**.

---

## Existing project evidence already supporting this frame
The current project already includes endpoint-level effect anchors for:
- **IQ / cognitive decrement**
- **ADHD / neurodevelopmental burden**
- **cardiovascular burden**
- **CKD / kidney burden**

Primary extracted effect anchors already in repo:
- `reports/tier_ab_top10_effect_extract_2026-03-06.csv`
- `reports/tier_ab_top10_triage_summary_2026-03-06.md`
- `reports/model_scenario_endpoint_uncertainty_2026-03-06.md`
- `reports/npv_policy_summary_cad_v4_2026-03-06.md`

Current city-level proxy exposure context already in repo:
- estimated remaining active lead connections: **2,442**
- impacted people proxy: **8,319**
- impacted children 0–14 proxy: **1,540**

Source artifacts:
- `reports/phd_equity_summary_2026-03-06.html`
- `reports/regina_lead_program_progress_2019_forward_2026-03-06.md`

Important guardrail: these are **proxy population-impact figures**, not audited household/person counts.

---

## Public-facing framing recommendation
Use this wording family in the public bundle:

> Lead service line delay is not just a budget or engineering issue. It is also a child-development and healthy-life-years issue. The literature connects lead exposure with cognitive loss, ADHD-type harms, and later chronic disease burden. That means the cost of delay should be understood not only in dollars, but in reduced quality of life and preventable lifetime harm.

This framing is strong, understandable, and still conservative.

---

## Recommended burden model structure

### Layer 1 — Public narrative layer
Use plain language only:
- children can experience lasting developmental harm,
- adults can carry later cardiovascular and kidney burden,
- prevention avoids not only spending but also suffering,
- some harms accumulate across a lifetime.

No single headline QALY estimate should appear here unless fully validated.

### Layer 2 — Conservative burden table
For each endpoint, provide:
- endpoint,
- evidence tier,
- exposed subgroup,
- burden type,
- likely persistence horizon,
- financial anchor present? yes/no,
- QALY/DALY feasible? yes/no,
- current confidence.

### Layer 3 — Technical appendix / model
Build a low / base / high scenario model for healthy-life burden using:
- affected-population proxy,
- exposure-response anchor,
- condition incidence or severity mapping,
- utility decrement or disability weight,
- duration,
- discounting assumptions,
- anti-double-counting rules.

---

## Why QALY and DALY both matter

### QALY use case
QALYs are helpful when the goal is to communicate:
- reduced quality of life,
- preventable suffering,
- health-economic burden,
- benefit of prevention/intervention.

### DALY use case
DALYs are helpful when the goal is to communicate:
- burden-of-disease style population impact,
- years of healthy life lost,
- comparability with global/public-health literature,
- conservative disability-weight framing.

### Practical recommendation
Use:
- **public page:** “quality of life / healthy life years” language,
- **technical memo:** both QALY and DALY framework,
- **first implementation:** whichever has the stronger and cleaner evidence chain for each endpoint.

In practice, DALY/YLD-style framing may be easier to defend first for broad burden communication, while QALY framing is stronger for cost-effectiveness and policy value.

---

## Candidate endpoint map

| Endpoint | Life-course relevance | Already in repo | Human-burden signal | Suitable for public bundle now? | Suitable for future QALY/DALY model? |
|---|---|---:|---|---:|---:|
| IQ decrement / cognitive loss | High | Yes | Very strong | Yes | Yes |
| ADHD / behavioural burden | High | Yes | Strong | Yes | Yes |
| Educational / later-life functioning loss | Medium-High | Partial | Strong but indirect | Narrative only | Yes, later |
| CVD / blood pressure burden | Medium | Yes | Strong | Yes, cautiously | Yes |
| CKD / kidney burden | Medium | Yes | Moderate-Strong | Yes, cautiously | Yes |
| Mortality / life expectancy | Medium | Partial | Important but requires stronger mapping | Not yet as headline | Later |

---

## Proposed anti-double-counting guardrails
This is the biggest modeling risk.

### Rule 1
Do **not** add IQ decrement burden and ADHD burden as if they are fully independent if both arise from the same childhood exposure chain without adjustment.

### Rule 2
Do **not** simultaneously count:
- direct cognitive utility loss,
- educational attainment loss,
- and lifetime earnings loss,
if they are all being treated as separate downstream expressions of the same developmental injury.

### Rule 3
When reporting both human burden and financial burden:
- make clear that financial cost is a **different lens**,
- not an additional “harm unit” to be summed with QALYs.

### Rule 4
Separate life-course domains where possible:
- childhood neurodevelopment,
- adult chronic disease,
- mortality / long-run survival,
then disclose overlap risk explicitly.

---

## Conservative implementation sequence

### Option A — immediate public bundle upgrade
Add a public-facing section:
- title: **Health Burden Beyond Dollars**
- plain-language summary of child and adult harms,
- no headline numeric QALY claim yet,
- explicit note that formal healthy-life-burden modeling is the next step.

### Option B — burden appendix
Add a compact technical table showing:
- endpoint,
- evidence source,
- burden type,
- model feasibility,
- confidence,
- what remains missing.

### Option C — full framework memo
This memo is that layer. It should be linked from the homepage and public bundle as the technical backbone.

---

## Suggested public-bundle wording

### Short paragraph
Lead service line delay is not only a financial issue. The literature used in this project links lead exposure with child cognitive harm, ADHD-type burden, and later chronic disease risk. That means the cost of delay should be understood in both dollars and human terms: reduced quality of life, impaired development, and healthy years of life put at risk.

### Caution line
This project does **not** yet publish a single headline QALY estimate for Regina. The current evidence supports the burden framing, but a full QALY/DALY model requires endpoint-specific utility mapping and explicit anti-double-counting controls.

---

## Current model-ready starting points

### Neurodevelopment lane
Existing anchors already support a first conservative burden build around:
- IQ decrement,
- ADHD-related burden,
- persistence into adolescence/adulthood.

### Chronic disease lane
Existing anchors already support a first conservative burden build around:
- blood-pressure / cardiovascular burden,
- CKD risk burden.

### Population denominator lane
Current proxy population anchors already support scenario modeling using:
- impacted children 0–14 proxy,
- impacted people proxy,
- low/base/high scenario analysis.

---

## What is still missing before a hard numeric Regina QALY headline
1. Endpoint-specific utility weights or disability weights selected and documented.
2. Duration assumptions for each endpoint.
3. Overlap handling between neurodevelopment endpoints.
4. Clear choice of whether burden is modeled as:
   - attributable cases,
   - attributable severity shift,
   - or exposure-distribution decrement.
5. A conservative presentation rule for uncertainty.

---

## Recommended next artifacts
1. `reports/regina_health_burden_qaly_framework_2026-03-16.md` — this memo
2. `reports/regina_health_burden_endpoint_table_2026-03-16.md` — compact endpoint/burden/evidence table
3. `reports/regina_health_burden_public_note_2026-03-16.md` — one-page public version
4. later: `data/derived/regina_qaly_scenarios_YYYY-MM-DD.csv` — low/base/high scenario outputs

---

## Public recommendation
For now, the strongest defensible public message is:
- Regina’s lead-service-line issue is not just about infrastructure and cost.
- It is also about children’s development, later chronic disease burden, and quality of life.
- The public should judge delay not only in dollars, but in preventable human harm.

That message is already supported by the current evidence base, even before a full QALY estimate is published.
