# CT factor significance scan (2019+ replacements)

Outcome: `strict_replaced` (CT normalized, constrained to 2019+ city totals).
Method: Spearman rank correlation + permutation p-value (4,000 reps), n=54 CTs.

| Factor | Spearman rho | Permutation p | Signal |
|---|---:|---:|---|
| Active lead connections (CT normalized) (`active_lead_count`) | 1.000 | 0.0002 | strong |
| Immigrant count (`immigrant_count`) | 0.773 | 0.0002 | strong |
| Visible minority count (`visible_minority_count`) | 0.741 | 0.0002 | strong |
| Bachelor+ 25-64 count (`education_bachelor_or_higher_25_64`) | 0.722 | 0.0002 | strong |
| Lone-parent family count (`lone_parent_family_count`) | 0.674 | 0.0002 | strong |
| No certificate 25-64 count (`education_no_certificate_25_64`) | 0.580 | 0.0002 | strong |
| Renter share % (`tenure_renter_pct`) | 0.270 | 0.0487 | moderate |
| LIM-AT prevalence % (`lim_at_prevalence_pct`) | 0.112 | 0.4361 | weak |
| Median after-tax household income (`median_after_tax_income_households`) | -0.085 | 0.5574 | weak |
| Indigenous identity % (`indigenous_identity_pct`) | -0.083 | 0.5576 | weak |
| Children LIM-AT prevalence % (`lim_at_children_0_17_pct`) | 0.081 | 0.5454 | weak |
| Unemployment rate % (`unemployment_rate_pct`) | 0.039 | 0.7856 | weak |
| Children 0-14 share % (`children_0_14_pct`) | -0.008 | 0.9563 | weak |

## Preliminary interpretation
- `active_lead_count` should be treated as exposure denominator/control and expectedly dominates replacement counts.
- Socioeconomic factors with lower p-values are candidates for multivariable modeling next (partial effects).
- This is still ecological CT-level analysis (non-causal).
