tags: [regina:canonical, regina:dream, regina:dmg, regina:merge-scope]
created_by: ChaosClaw
created_at: 2026-03-29T16:24:00+02:00

# DMG merge scope inventory — 2026-03-29

Status: canonical merge-scope note
Purpose: inventory the DMG features, custom scripts, and adapter surfaces that must be accounted for if DMG is to be genuinely merged into Dream Lab / Dream runner rather than reduced to only question generation.

---

## Executive summary

The merge scope is larger than question batteries.

DMG currently spans at least four classes of capability:
1. **core generator features**
2. **mutation / recommendation features**
3. **experiment-specific adapter features**
4. **benchmark / comparison utilities**

Only a subset of class (1) is currently integrated into the Dream runner.
The rest would be lost or shadowed if we declared the merge finished too early.

---

# 1. Core DMG features (must absorb into Dream runner)

These should become first-class native Dream runner stages.

## 1.1 Question generation
Confirmed by:
- `scripts/dmg_question_generator.py`
- `reports/dmg_question_generator_impl_2026-03-28.md`

Currently supports:
- machine-readable question specs
- learning type / mode / lane metadata
- scope terms / anti-scope terms
- route hints
- rationale / evidence-shape hints

## 1.2 Learning suggestion compatibility
Confirmed by:
- `scripts/dmg_learning_suggestions.py`
- runner artifacts that still emit `learning_suggestions.json`

This matters because older flows still consume legacy-compatible suggestion outputs.

## 1.3 Native question battery handling
Now partially integrated into:
- `scripts/run_dream_learn_dmg_cycle.py`

But should be treated as core, not optional glue.

---

# 2. Mutation / recommendation features (must not be forgotten)

These are substantial DMG-adjacent capabilities and should either be absorbed or explicitly registered.

## 2.1 Dream Monkey mutation generation
Confirmed by:
- `scripts/dream_monkey_generator.py`
- run artifacts with `mutations.json`

This is broader than question generation and clearly part of the Dream/DMG interaction surface.

## 2.2 DMG recommendation prompts / outputs
Confirmed by:
- `experiments/recall-answer-quality/dmg_recommendation_prompts_v1.md`
- run artifacts like `dmg_recommendations_v1.json`
- `dmg_recommendations_mutations_v1.json`
- `dmg_recommendations_mutations_summary_v1.json`

This means DMG also supports recommendation synthesis, not just raw question emission.

## 2.3 DMG-generated mutation specs
Confirmed by run artifacts like:
- `dmg_generated_specs_v1.json`
- `dmg_generated_mutations_v1.json`
- `dmg_generated_mutations_v2.json`

This is a separate capability family that must be accounted for in the merge.

---

# 3. Experiment-specific adapter features (register explicitly if not absorbed)

These are likely best treated as registered adapters/plugins if not promoted to full core stages.

## 3.1 Recall answer quality adapter surface
Confirmed by:
- `experiments/recall-answer-quality/README.md`
- `build_dmg_mutations_from_battery_v1.py`
- `run_recall_answer_quality_v1.py`
- `run_recall_answer_quality_mutations_v1.py`
- `run_recall_answer_quality_mutations_v2.py`

This family supports:
- battery-driven mutation generation
- recall-eval experiment task construction
- evaluation schemas
- experiment task/result packaging

This is not just “one-off noise”; it is a real adapter surface.

## 3.2 Prompt mutation matrix experiment pack
Confirmed by:
- `experiments/prompt_mutation_matrix/README.md`
- benchmark task sets
- scoring sheets
- results schemas/templates

This family supports:
- prompt-family comparison
- benchmark-driven mutation testing
- structured scoring and rollups

This should not vanish under a simplistic merge.

---

# 4. Existing Dream runner integration status

## Already partially integrated
- DMG question generation
- machine-readable question payloads
- legacy suggestion compatibility
- native question battery ingestion (newly added)
- routed execution of generated/supplied questions

## Not yet integrated enough
- mutation generation as a native stage
- recommendation outputs as native artifacts
- adapter registration/execution inside the runner
- benchmark/mutation matrix support
- stack-level comparison artifacts that understand DMG-originated variants

---

# 5. Merge classification

## Class A — absorb into Dream runner now
These should become first-class Dream runner capabilities:
- question generation
- question battery ingestion
- legacy suggestion emission
- mutation generation
- recommendation generation / summaries

## Class B — register as Dream runner adapters
These may remain separate scripts, but should be explicitly registered and invocable through Dream runner:
- recall-answer-quality mutation/eval harness
- prompt mutation matrix benchmark harness
- other experiment-specific transforms using DMG outputs

## Class C — defer but track
These should be connected later to the richer Dream Monkey surface:
- branch competition with DMG mutation families
- candidate merge/triage interplay
- bridge/handoff packet generation from DMG-derived candidate variants
- refinement/simulation stages that consume DMG mutation results

---

# 6. Operational rule

Do not declare DMG “merged into Dream Lab” unless all three are true:
1. core DMG generator features are native Dream runner stages;
2. experiment-specific DMG adapters are explicitly registered or deprecated;
3. mutation/recommendation outputs are no longer shadow workflows outside the Dream runner control plane.

---

# 7. Immediate next implication

The next implementation phase should not stop at question-battery support.
It should add at least:
- native mutation artifact support in the runner;
- native recommendation artifact support in the runner;
- an adapter registry contract for recall-answer-quality and prompt-mutation-matrix style DMG workflows.

That is the minimum honest scope for “finishing the merge.”
