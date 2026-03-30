tags: [regina:canonical, regina:dream, regina:dmg, regina:boundary-correction]
created_by: ChaosClaw
created_at: 2026-03-29T08:44:00+02:00

# Dream vs DMG boundary correction — 2026-03-29

Status: canonical anti-split-brain correction
Purpose: explicitly correct the conceptual split-brain that came from treating Dream, DMG, and Dream Monkey Generator as if they were the same layer.

---

## Executive correction

They are **not** the same thing.

### Correct relationship
- **Dream / Dream Monkey / Dream Lab** = the broader orchestration and lifecycle system
- **DMG** = a narrower generation sublayer/pass inside that broader system

This is not a cosmetic distinction.
It affects how lane counts, route maps, experiment design, and capability expectations should be interpreted.

---

## Evidence from canonical pipeline docs

The clearest direct evidence is:
- `projects/dream-lab/PIPELINE_DREAM_LEARN_DMG_v1.md`

That pipeline explicitly defines:
1. raw repo ingest
2. candidate generation
3. learning pass
4. **DMG mutation pass**
5. experiment execution
6. refinement
7. simulation
8. approval / materialization

This proves DMG is only one stage/pass inside a larger Dream pipeline.

---

## Correct layer model

## Layer 1 — Dream / Dream Monkey / Dream Lab
This is the broader orchestration and lifecycle machinery.
It includes things like:
- candidate generation
- packetization / handoff packets
- bridge runs
- JTB router / feedback loops
- lifecycle states and transition routing
- branch outputs
- triage scoring
- refinement
- simulation
- promotion / materialization
- full experiment runs

Canonical evidence includes:
- `PIPELINE_DREAM_LEARN_DMG_v1.md`
- `blueprints/dream_lab_state_transition_router_spec.md`
- `blueprints/dream_lab_jtb_bridge_v1.md`
- bridge run artifacts under `projects/dream-lab/bridge_runs/`
- full-run artifacts like `dream_full_v0_*`, `dream_cycle_*`, `dream_monkey_*`

## Layer 2 — DMG
This is a narrower generation-oriented sublayer.
It appears responsible for things like:
- question generation
- learning suggestions
- mutation generation
- route-shaped experiment prompts/specs

Canonical evidence includes:
- `scripts/dmg_question_generator.py`
- `reports/dmg_question_generator_impl_2026-03-28.md`
- `dmg_learning_lane_taxonomy_2026-03-28.md`
- `dmg_recall_eval_generator.py`
- DMG suggestion/mutation artifacts in run directories

## Layer 3 — execution/service routes
These are the service paths used by Dream/DMG outputs, such as:
- `internal_validation_service.py`
- `project_scoped_live_learning.py`
- route matrices
- audit paths
- rerank-debug paths
- experiment execution paths

---

## What went wrong

A conceptual regression happened in operator language:
- the small DMG lane taxonomy was treated as if it were the full Dream Monkey execution universe.

That produced a false impression that Dream Monkey had only a handful of lanes.

In reality:
- the DMG learning taxonomy is small by design;
- the Dream execution/orchestration universe is much larger.

---

## Correct interpretation of lane counts

### DMG lane count
Small / normalized / generator-oriented.
Examples:
- validation_or_contradiction
- benchmark_or_comparison
- operator_decision_support
- transferable_methods
- tooling_patterns

### Dream Monkey execution-path count
Much larger.
Includes combinations across:
- candidate lifecycle states
- bridge/router paths
- learning pass routes
- mutation families
- experiment execution paths
- refinement/simulation routes
- project-specific substantive lanes

So the expectation that Dream Monkey should have "far more lanes" is correct **if Dream Monkey means the broader Dream system**, not just the DMG taxonomy.

---

## Operational correction rule

From this point on:

### Do not say “DMG” when meaning the whole Dream system.
Use:
- **Dream / Dream Monkey / Dream Lab** for the broader orchestration system
- **DMG** for the generator/question/mutation sublayer only

### Do not compare lane counts across layers without naming the layer.
Always specify whether the count refers to:
- substantive work lanes
- DMG learning lanes
- execution/service routes
- Dream lifecycle/orchestration paths

---

## Immediate implication for Regina work

When planning the next Regina experiment/path map:
- the small DMG lane taxonomy should be treated only as one sublayer;
- it should not be mistaken for the full Dream Monkey path universe;
- external follow-up work should be framed against the full Dream stack (substantive lane + learning lane + execution route), not just the DMG taxonomy label.

---

## Corrected mental model

### Dream / Dream Monkey
The bigger machine.

### DMG
One generator/mutation/questioning subsystem inside that machine.

### Result
There is no contradiction once the layers are separated.
The contradiction came from using the same word for different layers.
