# Reproducibility Appendix — Equity Analysis (2026-03-06)

## Scope of this run
This run executed three actions:
1. Build a merged CT/DA **proxy** panel with replacement intensity plus tenure/demographic schema columns.
2. Run significance and robustness checks (nonparametric + regression with robust SE).
3. Publish upgraded equity summary language with explicit confidence and limitations.

## Exact command used
```bash
cd /root/.openclaw/workspace/projects/regina-lead-github-pages
python3 scripts/build_equity_panel_and_tests.py
```

## Script added
- `scripts/build_equity_panel_and_tests.py`

## Inputs
Local derived inputs:
- `data/derived/area_priority_signals.csv`
- `data/derived/strict_replacements_by_area_month.csv`

Public endpoint used for profile-link metadata:
- `https://opengis.regina.ca/arcgis/rest/services/CGISViewer/Neighbourhood_Profile/MapServer/0/query`
  - fields used: `CA`, `PDF_Link`

## Outputs produced
- `data/derived/ct_da_equity_panel_2026-03-06.csv`
- `data/derived/equity_significance_results_2026-03-06.csv`
- `reports/phd_equity_summary_2026-03-06.html` (upgraded)
- `reports/reproducibility_appendix_equity_2026-03-06.md` (this file)

## Statistical methods (implemented in script)
1. **Spearman rank correlation** between lead burden (`lead_per`) and replacement intensity (`strict_repl_rate_vs_lead_total`), with permutation p-value (10,000 reps).
2. **Mann–Whitney U test** on replacement intensity split by median lead burden (high vs low), with permutation p-value (10,000 reps).
3. **OLS linear model with HC1 robust SE**:
   - outcome: `strict_repl_rate_vs_lead_total`
   - predictors: intercept, `lead_per`, `log1p(lead_total)`, `log1p(wc_total)`
   - p-values are normal-approximation two-sided; confidence intervals are 95% Wald (robust).

## Key numeric outputs from this run
From `data/derived/equity_significance_results_2026-03-06.csv`:
- Spearman rho = `0.714286`, permutation p = `0.006199`
- Mann–Whitney median difference (high-low lead burden) = `0.220721`, permutation p = `0.012499`
- OLS HC1 coefficient on `lead_per` = `-0.003066`, 95% CI `[-0.012411, 0.006279]`, p = `0.520197`

## Interpretation discipline
- Treat findings as **observational and descriptive**.
- Do **not** infer causality or fairness proof from these tests.
- Sample is small (n=14 DA-proxy units).

## Data/measurement limitations
- The CT/DA panel here is explicitly a **proxy geography panel** built from LeadConnectionAreas, not an official StatsCan CT/DA spatial join.
- Tenure and demographic fields are included in schema but remain pending numeric extraction in this run.
- Public neighbourhood profile links are included to support future extraction and audit trail.
