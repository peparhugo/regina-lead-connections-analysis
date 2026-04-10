# Burden Model Methodology (v5)

## Two-track model

### Track 1: Healthcare (bottom-up, condition-specific)

| Condition | Prevalence increase | Annual cost (CAD) | Duration (years) | Expected cost per exposed child | Source |
|---|---:|---:|---:|---:|---|
| ADHD | 12% | $8,000 | 12 | $11,520 | Goodlad 2013, CADDRA formulary, Globe and Mail 2024 |
| Learning disability | 20% | $10,000 | 8 | $16,000 | Provincial special education funding, OT/speech therapy rates |
| Behavioral/conduct | 10% | $4,000 | 8 | $3,200 | CIHI mental health CMGs, provincial program costs |
| Adult cardiovascular | 7% | $5,000 | 15 | $5,250 | CIHI cardiovascular CMGs, Heart & Stroke Foundation |
| Chronic kidney disease | 5% | $15,000 | 10 | $750 | CIHI renal CMGs, Kidney Foundation of Canada |
| **Raw total** | | | | **$36,720** | |
| **After comorbidity (×0.85)** | | | | **$31,212** | ADHD/LD overlap ~30-50% |

### Comorbidity correction
ADHD (12%) and learning disability (20%) have ~30-50% comorbidity.
Correction factor: ×0.85 applied to total healthcare cost.
Corrected healthcare per child: $31,212

### Track 2: Earnings loss (IQ-point based)

| Parameter | Value | Source |
|---|---|---|
| IQ loss per child | 2.0 points | Lanphear (2005) dose-response at measured Cathedral water levels |
| Cost per IQ point | $24,000 CAD | Salkever (1995): 2.4% earnings/pt × Regina median $42K × 40yr NPV at 3% |
| Earnings loss per child | $48,000 | 2.0 × $24,000 |

### IQ loss validation
Cathedral Village testing (Sept 2025): 71% of 54 homes exceeded 5 μg/L.
Dose-response chain: water lead 15-30 μg/L (median exceedance) → BLL 1.5-6 μg/dL → IQ loss 0.7-2.8 points.
2.0 points is mid-range. Validated by actual local measurements, not just literature.

### Per-child total
Healthcare: $31,212
Earnings: $48,000
**Total: $79,212**

### Convergence check
Top-down (Gould 2009): $17,815/IQ point (2006 USD) → $35,131 CAD (2026) → $70,262 per child at 2 IQ points.
Bottom-up: $79,212 per child.
The bottom-up is higher because it includes healthcare conditions beyond earnings loss.
The earnings components converge within 3% ($48K bottom-up vs $46.6K Salkever Canadian calc).

### Per-neighbourhood burden

| Neighbourhood | Children at risk | Children prevented | At-risk burden | Prevented burden |
|---|---:|---:|---:|---:|
| North Central | 95 | 104 | $7,525,140 | $8,238,048 |
| Cathedral (east) | 57 | 72 | $4,515,084 | $5,703,264 |
| Cathedral (west) | 70 | 46 | $5,544,840 | $3,643,752 |
| Heritage | 61 | 21 | $4,831,932 | $1,663,452 |
| North Central (south) | 46 | 36 | $3,643,752 | $2,851,632 |
| Heritage (north) | 25 | 21 | $1,980,300 | $1,663,452 |
| Old Lakeview | 35 | 16 | $2,772,420 | $1,267,392 |
| Cathedral (south) | 27 | 16 | $2,138,724 | $1,267,392 |
| Warehouse District | 17 | 36 | $1,346,604 | $2,851,632 |
| Downtown | 3 | 0 | $237,636 | $0 |
| McNab | 18 | 4 | $1,425,816 | $316,848 |
| Eastview | 16 | 8 | $1,267,392 | $633,696 |
| Ross Industrial | 2 | 0 | $158,424 | $0 |
| Rosemont | 4 | 2 | $316,848 | $158,424 |
| Centre Square | 4 | 0 | $316,848 | $0 |
| **TOTAL** | **480** | **382** | **$38,021,760** | **$30,258,984** |
