# Regina Lead Reports — Index & Triage
Created: 2026-04-01
Purpose: single index of all reports with keep/archive decision

## Legend
- **KEEP** = still relevant, represents current truth or durable reference
- **ARCHIVE** = superseded, intermediate, or historical only — move to `reports/archive/`
- **DATA** = reference data file, not a report — move to `reports/archive/data/`

---

## KEEP — Core Analytical Outputs (11 files)

These represent the strongest durable analytical work product:

| File | Why keep |
|---|---|
| `regina_claim_evidence_table_primary_2026-03-12.md` | Primary-source claim/evidence table from official records |
| `regina_investigative_memo_method_evidence_limits_2026-03-12.md` | Method and evidence-limits memo — still valid framing |
| `regina_burden_weight_literature_review_2026-03-16.md` | Peer-reviewed lit review for burden weighting — durable reference |
| `regina_child_cognitive_burden_prototype_v2_2026-03-16.md` | Recalibrated child burden model after lit review |
| `regina_child_burden_crosswalk_duration_hardening_2026-03-16.md` | Method hardening for child burden lane |
| `regina_flint_calibration_memo_2026-03-16.md` | Flint comparator calibration — durable reference |
| `regina_health_burden_qaly_framework_2026-03-16.md` | QALY/DALY framework — foundation for PostGIS matviews |
| `regina_healthy_life_burden_scenarios_2026-03-16.md` | Low/base/high scenario sheet |
| `regina_health_burden_endpoint_table_2026-03-16.md` | Endpoint table for burden model |
| `regina_health_burden_technical_appendix_2026-03-16.md` | Technical appendix — publication-grade |
| `ct_factor_significance_2019plus_2026-03-06.md` | CT factor significance scan — statistical results |

## KEEP — Public-Facing Package (11 files)

Deliverables for public site, outreach, and journalism:

| File | Why keep |
|---|---|
| `regina_public_brief_plain_language_2026-03-12.md` | Public brief — plain language |
| `regina_public_handout_2026-03-16.md` | Public handout |
| `regina_journalist_memo_2026-03-16.md` | Journalist memo |
| `regina_outreach_pack_councillor_2026-03-16.md` | Councillor outreach pack |
| `regina_outreach_pack_journalist_2026-03-16.md` | Journalist outreach pack |
| `regina_outreach_pack_resident_2026-03-16.md` | Resident outreach pack |
| `regina_criticism_preemption_note_2026-03-16.md` | Criticism pre-emption — useful framing |
| `regina_media_pitch_note_2026-03-16.md` | Media pitch note |
| `regina_public_bundle_2026-03-16.html` | Public bundle HTML |
| `regina_public_bundle_2026-03-16.pdf` | Public bundle PDF — final deliverable |
| `regina_health_burden_public_table_2026-03-16.md` | Conservative public health-burden table |

## KEEP — Current State & Control (9 files)

Most recent authoritative state snapshots and active contracts:

| File | Why keep |
|---|---|
| `regina_authoritative_state_2026-03-27.md` | Latest authoritative state snapshot |
| `regina_current_claim_status_2026-03-16.md` | Canonical claim-status ledger |
| `regina_control_inventory_2026-03-28.md` | Control inventory — lane/authority map |
| `regina_control_summary_2026-03-28.md` | Combined control view |
| `regina_build_repro_contract_2026-03-28.md` | Active build/reproducibility contract |
| `regina_git_pr_workflow_contract_2026-03-28.md` | Active PR workflow contract |
| `regina_pr_review_gate_checklist_2026-03-28.md` | PR review checklist — reusable |
| `regina_lane_stack_map_2026-03-29.md` | Lane disambiguation map — important architecture doc |
| `regina_knowledge_layer_model_2026-03-27.md` | Knowledge layer model — governance reference |

## KEEP — Data Contracts & Map Specs (5 files)

Active specs for map build and public data:

| File | Why keep |
|---|---|
| `regina_public_scene1_data_contract_2026-03-21.md` | Scene 1 public data contract |
| `regina_kepler_package_contract_2026-03-21.md` | Kepler analyst package contract |
| `regina_map_build_gate_checklist_2026-03-21.md` | Map build gates |
| `reproducibility_appendix_equity_2026-03-06.md` | Reproducibility appendix |
| `regina_decision_to_delivery_tracker_2026-03-16.md` | Decision-to-delivery tracker |

## KEEP — Reference Data (5 files)

Data files used by scripts or needed for reproducibility:

| File | Why keep |
|---|---|
| `evidence_registry_curated_2026-03-06.csv` | Curated evidence registry |
| `statscan_variable_ids_pinned_2026-03-06.csv` | Pinned StatsCan variable IDs |
| `regina_build_lane_question_battery_2026-03-28.json` | Build lane question battery |
| `regina_public_scene1_dataset_qa_2026-03-21.json` | Scene 1 QA results |
| `regina_public_scene1_join_qa_2026-03-21.json` | Scene 1 join QA results |

## KEEP — Rendered HTML (keep alongside source) (5 files)

| File | Why keep |
|---|---|
| `public-brief.html` | Rendered public brief |
| `public-handout.html` | Rendered handout |
| `journalist-memo.html` | Rendered journalist memo |
| `technical-appendix.html` | Rendered technical appendix |
| `factor_diagnostics_map_2026-03-06.html` | Factor diagnostics map |

---

## ARCHIVE — Superseded State Snapshots (10 files)

Explicitly superseded by later documents or marked as historical:

| File | Superseded by |
|---|---|
| `regina_authoritative_state_2026-03-16.md` | `_2026-03-27.md` version |
| `regina_canonical_summary_2026-03-27.md` | Duplicate of `authoritative_state_2026-03-27.md` |
| `regina_completion_vs_enrichment_2026-03-27.md` | Subsumed into control inventory |
| `regina_layer_ranking_rules_2026-03-27.md` | Subsumed into knowledge layer model |
| `regina_PICKUP_POINT_2026-03-16.md` | Self-declares superseded |
| `regina_session_switch_summary_2026-03-16.md` | Self-declares superseded |
| `regina_prepublish_audit_and_curation_plan_2026-03-16.md` | Self-declares superseded |
| `regina_publish_cleanup_checklist_2026-03-16.md` | Self-declares superseded |
| `regina_package_gate_status_2026-03-16.md` | Superseded by control inventory |
| `final_synthesis_2026-03-06.md` | Early synthesis, superseded by later state docs |

## ARCHIVE — Intermediate/Phase Artifacts (14 files)

Transition documents from completed phases:

| File | Why archive |
|---|---|
| `phase2_kickoff_status_2026-03-06.md` | Phase 2 kickoff — done |
| `phase2_progress_report_2026-03-06_0535.md` | Intermediate progress |
| `phase3_publication_gate_status_2026-03-10.md` | Phase 3 gate — passed |
| `next_phase_handoff_pack_2026-03-10.md` | Handoff — consumed |
| `regina_phase_next_tasks_2026-03-09.md` | Task pack — consumed |
| `regina_terminal_stability_2026-03-09.md` | Terminal stability check — done |
| `regina_acp_restart_plan_2026-03-09.md` | ACP restart — done |
| `resume_pack_regina_2026-03-08.md` | Resume pack — consumed |
| `interim_public_update_2026-03-06.md` | Interim update — superseded |
| `effect_extraction_progress_2026-03-06.md` | Early extraction — superseded |
| `regina_project_completion_checklist_2026-03-16.md` | Completion checklist — done |
| `regina_lead_program_progress_2019_forward_2026-03-06.md` | Self-declares superseded |
| `regina_homepage_final_qa_2026-03-19.md` | QA — done |
| `mission-log.md` | Raw mission tick log — historical |

## ARCHIVE — Recovery Lane (completed) (10 files)

Recovery work is done; these document the process but aren't needed going forward:

| File | Why archive |
|---|---|
| `regina_recovery_lane_note_2026-03-28.md` | Recovery process doc |
| `regina_recovery_completion_status_2026-03-28.md` | Recovery completed |
| `regina_recovery_governance_surface_2026-03-29.md` | Recovery governance |
| `regina_recovery_verification_status_2026-03-29.md` | Recovery verification |
| `regina_recovery_promotion_status_2026-03-29.md` | Recovery promotion |
| `regina_full_recovery_ledger_2026-03-29.md` | Full recovery catalog |
| `regina_cross_workspace_reconciliation_2026-03-29.md` | Cross-workspace reconciliation |
| `regina_post_recovery_control_status_2026-03-29.md` | Post-recovery status |
| `regina_non_blocking_caveats_resolution_2026-03-29.md` | Caveats resolution |
| `regina_m3_m4_knowledge_layer_formalization_2026-03-27.md` | M3/M4 formalization — consumed into knowledge model |

## ARCHIVE — PR/Git Process Notes (7 files)

Per-PR review notes from the March 28 git discipline setup:

| File | Why archive |
|---|---|
| `regina_first_pr_review_note_2026-03-28.md` | PR1 review |
| `regina_pr3_dmg_review_note_2026-03-28.md` | PR3 review |
| `regina_pr3_repro_gap_note_2026-03-28.md` | PR3 gap note |
| `regina_pr4_asset_gap_note_2026-03-28.md` | PR4 gap note |
| `regina_pr5_delivery_guardrail_note_2026-03-28.md` | PR5 guardrail |
| `regina_g5_git_discipline_status_2026-03-28.md` | G5 gate — passed |
| `regina_support_lane_review_note_2026-03-28.md` | Support lane review |

## ARCHIVE — Dream/DMG Experiment Artifacts (17 files)

Dream Runner and DMG experiment designs, audits, and pilot results. These are infrastructure/tooling artifacts, not Regina substantive outputs:

| File | Why archive |
|---|---|
| `dream_runner_executor_audit_2026-03-29.md` | Dream tooling audit |
| `dream_runner_native_question_battery_dmg_integration_2026-03-29.md` | DMG integration design |
| `dream_vs_dmg_boundary_correction_2026-03-29.md` | Tooling boundary correction |
| `dmg_merge_scope_inventory_2026-03-29.md` | Merge scope inventory |
| `regina_dmg_question_experiment_design_2026-03-29.md` | Experiment design |
| `regina_dream_monkey_dmg_multistep_optimization_architecture_2026-03-29.md` | Optimization architecture |
| `regina_multistep_optimization_pilot_matrix_2026-03-29.md` | Pilot matrix |
| `regina_multistep_pilot_progress_2026-03-29.md` | Pilot progress |
| `regina_runner_experiments_next6_2026-03-29.md` | Next experiments |
| `regina_waveA_dmg_experiment_review_2026-03-29.md` | Wave A review |
| `regina_waveA_external_retry_review_2026-03-29.md` | External retry review |
| `regina_support_communication_source_profile_2026-03-29.md` | Source profile |
| `regina_support_layer_contradiction_review_2026-03-29.md` | Contradiction review |
| `regina_stack_v2_first_runner_plan_2026-03-30.md` | Stack v2 plan |
| `regina_stack_v2_manifest_2026-03-30.md` | Stack v2 manifest |
| `regina_stack_v2_mini_dreamer_contract_2026-03-30.md` | Mini-dreamer contract |
| `regina_stack_v2_phase1_packet_2026-03-30.json` | Phase 1 packet |

## ARCHIVE — PropertySearch Swarm Artifacts (22 files)

Detailed swarm packet specs for property-search enrichment. The work was designed but not fully executed. Archive as reference for if/when this lane resumes:

| File | Why archive |
|---|---|
| `regina_propertysearch_v1_build_plan_2026-03-25.md` | Build plan |
| `regina_propertysearch_v1_execution_board_2026-03-25.md` | Execution board |
| `regina_propertysearch_stage0_audit_contract_2026-03-25.md` | Audit contract |
| `regina_propertysearch_scaffold_hardening_brief_2026-03-25.md` | Scaffold hardening |
| `regina_propertysearch_postgis_catalog_contract_2026-03-25.md` | PostGIS catalog contract |
| `regina_propertysearch_parser_smoke_contract_2026-03-25.md` | Parser smoke contract |
| `regina_propertysearch_loader_contract_2026-03-25.md` | Loader contract |
| `regina_propertysearch_join_validation_2026-03-25.md` | Join validation |
| `regina_swarm_packet_A_parser_contract_2026-03-25.md` | Swarm A |
| `regina_swarm_packet_B_account_audit_2026-03-25.md` | Swarm B |
| `regina_swarm_packet_C_reconciliation_mart_2026-03-25.md` | Swarm C |
| `regina_swarm_packet_D_claim_guardrails_2026-03-25.md` | Swarm D |
| `regina_swarm_packet_E_parser_impl_spec_2026-03-25.md` | Swarm E |
| `regina_swarm_packet_F_stage0_sampler_spec_2026-03-25.md` | Swarm F |
| `regina_swarm_packet_G_db_loader_spec_2026-03-25.md` | Swarm G |
| `regina_swarm_packet_H_mart_promotion_spec_2026-03-25.md` | Swarm H |
| `regina_swarm_packet_I_education_warning_2026-03-25.md` | Swarm I |
| `regina_swarm_packet_J_smokefive_decision_2026-03-25.md` | Swarm J |
| `regina_swarm_packet_K_stage0_gate_2026-03-25.md` | Swarm K |
| `regina_knowledge_completion_reconstruction_2026-03-27.md` | Knowledge reconstruction |
| `regina_mvp_release_checklist_2026-03-22.md` | MVP release checklist — done |
| `regina_operator_release_note_2026-03-23.md` | Operator release — done |

## ARCHIVE — Early Data Exploration (15 files)

Data exploration artifacts from Phase 1 that fed into later work:

| File | Why archive |
|---|---|
| `analytical_mapping_options_2026-03-06.md` | Early mapping options |
| `kepler_phase_a_quickstart_2026-03-06.md` | Kepler quickstart |
| `kepler_config_phase_a_2026-03-06.json` | Early Kepler config |
| `ct_geometry_crosswalk_2026-03-06.csv` | CT geometry crosswalk |
| `statscan_data_availability_map_2026-03-06.md` | StatsCan availability scan |
| `statscan_census_polygon_expansion_plan_2026-03-06.md` | Census polygon plan |
| `statscan_gis_inventory_2026-03-06.csv` | GIS inventory |
| `statscan_table_inventory_regina_equity_2026-03-06.csv` | Table inventory |
| `statscan_table_inventory_regina_equity_2026-03-06.advanced.csv` | Advanced table inventory |
| `effect_size_normalized_2026-03-06.csv` | Effect sizes |
| `effect_extraction_seed_now_next_2026-03-06.csv` | Effect extraction seed |
| `evidence_triage_priority_queue_2026-03-06.csv` | Evidence triage queue |
| `evidence_triage_effect_seed_2026-03-06.csv` | Effect seed |
| `socioeconomic_significance_summary_2026-03-06.md` | Significance summary |
| `phd_resume_readiness_review_2026-03-06.md` | Resume readiness — done |

## ARCHIVE — Rendered HTML (superseded or historical) (3 files)

| File | Why archive |
|---|---|
| `claim-evidence.html` | Rendered claim-evidence — intermediate |
| `delivery-tracker.html` | Delivery tracker — intermediate |
| `phd_equity_summary_2026-03-06.html` | Early equity summary HTML |

## ARCHIVE — Other (5 files)

| File | Why archive |
|---|---|
| `public_onepager_template_v1.md` | Template — unused |
| `knowledge-gaps.md` | Empty |
| `decision-ledger.md` | Stub — 3 lines |
| `table_advance_loop_log.md` | Loop log — historical |
| `regina_jtb_integrity_review_2026-03-16.md` | JTB review — consumed into claim status |

## ARCHIVE — Swarm directory (9 files)

| File | Why archive |
|---|---|
| `swarm/README_latest_swarm_setup.md` | Early swarm setup |
| `swarm/t1_baseline_audit.md` | Task output |
| `swarm/t2_openclaw_json_patch.json5` | Patch file |
| `swarm/t2_openclaw_json_patch.md` | Patch notes |
| `swarm/t2_patch_notes.md` | Patch notes |
| `swarm/t3_validation_checklist.md` | Validation |
| `swarm/t4_cron_plan.md` | Cron plan |
| `swarm/t5_integration_bundle.md` | Integration |
| `swarm/t6_decision_brief.md` | Decision brief |

## KEEP — External Delivery (2 files)

| File | Why keep |
|---|---|
| `regina_external_delivery_send_kit_2026-03-16.md` | Operator delivery instructions |
| `regina_journalist_story_package_plan_2026-03-16.md` | Story package plan |

## KEEP — True Policy Analysis (1 file)

| File | Why keep |
|---|---|
| `regina_true_policy_shift_scorecard_2026-03-12.md` | Policy shift scorecard |

---

## Summary

| Category | Count |
|---|---|
| **KEEP** | 49 |
| **ARCHIVE** | 107 |
| **Total** | 156 |

Reports root after triage: 49 files (clean, navigable)
Archive: 107 files preserved in `reports/archive/` for reference
