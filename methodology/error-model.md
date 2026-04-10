# Error Model: 84.1% ± 2.9%

## Method
Confirmed replacements detected as CBMH(Pb) ∩ DomesticWaterNetworkTrace(Cu) crossover.
Completion date: MAINTENANCEDATE from Trace.
Validated against city-published LSC replacement counts.

## Calibration data

| Year | Our MAINT count | City reported (LSC) | Hydrovac confirms | Coverage |
|---:|---:|---:|---:|---:|
| 2020 | 96 | 118 | 0 | 81.4% |
| 2021 | 170 | 193 | 0 | 88.1% |
| 2022 | 175 | 210 | 23 | 83.3% |
| 2023 | 146 | 175 | 107 | 83.4% |

Mean: **84.1%**. Stdev: **2.9%**. Correction factor: **×1.189**

## Source
City replacement counts from: https://www.regina.ca/home-property/water/water/lead-service-connections/
Note: 2022 and 2023 include hydrovac confirmations (dig up, confirm not lead) as "Total Removal".
Our comparison uses LSC Replacements only, not Total Removal.

## Interpretation
The 16% undercount is systematic — same data entry bottleneck every year.
This is a data management capacity issue, not random error.
The city does the work but does not always record it in GIS.

## Five-system reconciliation

| System | Pb count | State | Source URL |
|---|---:|---|---|
| CBMH Layer 8 | 6,943 | Frozen ~2016 | opengis.regina.ca/.../CBMH_Survey_Map/FeatureServer/8 |
| DomesticWaterNetworkTrace/4 | 5,405 | Live (2026) | opengis.regina.ca/.../DomesticWaterNetworkTrace/MapServer/4 |
| SewerWaterCondition Lead+PolyB | 2,760 | Filtered active | opengis.regina.ca/.../SewerWaterCondition/MapServer/4 |
| LeadConnectionAreas | 3,637 | Stale aggregate | opengis.regina.ca/.../LeadConnectionAreas/MapServer/0 |
| GTLO Committee list | ~2,305 | Independent (Sept 2025) | Google My Maps KML |

No official reconciliation of these systems exists.
