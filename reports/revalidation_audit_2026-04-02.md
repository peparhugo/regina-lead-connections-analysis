# Regina Lead Project — Full Number Revalidation Audit

**Date:** 2026-04-02
**Triggered by:** Pepar's challenge — "I have a feeling the number of remaining lead connections is incorrect"
**Method:** Primary source verification against live ArcGIS endpoint, media reports, and internal data pipeline tracing

---

## Executive Summary

The site's headline number (1,089 active connections) is **wrong by 60%**. The actual current count is **2,698** per the City's live ArcGIS service. Multiple other numbers on the site are also wrong or internally inconsistent.

---

## Verified Primary Sources (fetched live 2026-04-02)

### ArcGIS LeadConnectionAreas service
- Endpoint: `https://opengis.regina.ca/arcgis/rest/services/CGISViewer/LeadConnectionAreas/MapServer`
- Layer 0 (close zoom) = **Baseline/FOI total**: 3,637 lead connections across 14 community areas
- Layer 1 (far zoom) = **Current remaining**: 2,698 lead connections
- Implied city-owned replacements: 939

### Media-reported numbers (cross-checks)
| Source | Date | Claim | Consistent? |
|---|---|---|---|
| LSLR Collaborative | ~2021 | "nearly 3,300 LSCs" posted from FOI | Slightly below ArcGIS 3,637 |
| LeaderPost | ~2022 | "approximately 3,400 remaining" | Yes (pre-2023) |
| CBC | Sep 2023 | "approximately 3,000 remaining" | Yes (ArcGIS now shows 2,698 after more replacements) |
| Cathedral Village | Sep 2025 | Links to same ArcGIS map | Yes |

### City-reported annual replacements
| Year | Replaced | Source |
|---|---|---|
| 2019 | 180 | LeaderPost |
| 2020 | 118 | LeaderPost |
| 2021 | 193 | LeaderPost |
| 2022 | 233 | LeaderPost (city + private combined) |
| 2023 | ~280-300 est | CBC (207 in first 7 months) |
| 2024-2025 | unknown | No media found |
| **Sum 2019-2022** | **724** | |

---

## Claims vs Reality

### CLAIM 1: "1,089 active lead service connections"
**VERDICT: ❌ WRONG**

| Measure | Value |
|---|---|
| Site claims | 1,089 |
| ArcGIS Layer 1 (current, live) | **2,698** |
| Undercount | 1,609 (60%) |

**Root cause:** The PostGIS pipeline uses a spatial join through `address_points_crosswalk` that only matched ~30% of FOI addresses to census tract geometry. The remaining ~70% of addresses fell through the join and were silently dropped.

**Pipeline trace:**
```
known_lead_address_reconciliation_triaged
  → LEFT JOIN address_points_crosswalk (spatial: ST_Intersects)
    → GROUP BY census tract
      → ct_direct_lead_synthesis_20260324
```

### CLAIM 2: "~1,540 children in affected census tracts"
**VERDICT: ⚠️ UNCLEAR / TWO CONFLICTING NUMBERS**

| Source | Children | Notes |
|---|---|---|
| Site hero text | ~1,540 | Displayed prominently |
| CT harm GeoJSON (17 CTs) | 463 | Used in map tooltips |
| Equity panel (54 CTs) | 1,516 | Full CT coverage |

- The "~1,540" appears rounded from the equity panel's 1,516 impacted children estimate
- But the GeoJSON only shows 463 because it only contains 17 CTs
- The map and the hero text contradict each other
- The equity panel's `active_lead_count` sums to 3,611 (baseline-era, not current)
- If recalculated with current ArcGIS numbers (2,698), the impacted children estimate would change

### CLAIM 3: "$39.6M in realized healthcare cost"
**VERDICT: ⚠️ DERIVED FROM WRONG INPUT**

- The cost model formula: `lead_connections × exposure_years × QALY_weight × cost_per_QALY`
- Since the lead connection count feeding this model is wrong, the cost is proportionally wrong
- However: the true number is HIGHER than claimed (more connections = more exposure = more cost)
- The methodology itself (QALY framework) is defensible; the input data is not

### CLAIM 4: Replacement counts disagree internally
**VERDICT: ❌ INTERNAL INCONSISTENCY**

| Source | Replacements |
|---|---|
| Scene1 area-level GeoJSON | 1,146 |
| CT harm GeoJSON | 900 |
| ArcGIS implied (3,637 - 2,698) | 939 |
| City reported 2019-2022 only | 724 (city + private) |

- Our 1,146 likely over-counts (inferred/estimated replacements beyond what ArcGIS shows)
- Our 900 uses a different methodology at CT level
- ArcGIS 939 is the most authoritative (direct baseline minus current)
- City reports of 724+ include private-side replacements that ArcGIS may not track

### CLAIM 5: Equity panel baseline
**VERDICT: ⚠️ STALE**

- Equity panel `active_lead_count` sums to 3,611
- ArcGIS baseline: 3,637
- These are baseline-era numbers, not current remaining
- The 26-unit gap is likely vintage/rounding

---

## Anomaly: NORTHEAST area

NORTHEAST went from 1 lead connection (baseline) to 2 (current). This is the only area that increased, suggesting either reclassification or newly discovered lead pipe.

---

## What Needs Fixing

1. **Lead connection count**: Replace 1,089 with 2,698 (ArcGIS Layer 1 current)
2. **Children count**: Recalculate using correct per-area lead distribution from ArcGIS
3. **Healthcare cost**: Recalculate with corrected connection count
4. **Replacement count**: Use ArcGIS-derived 939 as the authoritative number
5. **CT-level breakdown**: Either fix the spatial join pipeline or redistribute the area-level ArcGIS totals across census tracts using overlap ratios
6. **Internal consistency**: Ensure scene1, CT harm, and equity panel all use the same source numbers

---

## Data Quality Root Cause

The fundamental problem is **the spatial join bottleneck**: converting street addresses to census tract locations. The `address_points_crosswalk` table matched only ~1,100 of ~3,600 FOI addresses. This is a common GIS problem — address matching is lossy, especially with older neighborhoods, multi-unit buildings, and address format variations.

The ArcGIS service bypasses this problem because the City geocoded the addresses themselves and provides area-level aggregates directly.
