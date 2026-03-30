tags: [regina:canonical, regina:dream, regina:dmg, regina:integration-design]
created_by: ChaosClaw
created_at: 2026-03-29T16:19:00+02:00

# Dream runner native question battery + embedded DMG integration — 2026-03-29

Status: canonical integration design
Purpose: define the corrected architecture where all stacks run through the Dream runner, the question battery is first-class inside that runner, and DMG is embedded as a sublayer rather than operating beside Dream Lab.

---

## Executive decision

From this point on, the desired architecture is:

### 1. all stacks run through the Dream runner
### 2. the Dream runner owns the question battery
### 3. DMG is embedded inside the Dream runner as a generator/mutation stage
### 4. direct route scripts become execution backends, not parallel top-level workflows

This is the clean anti-split-brain end-state.

---

## Current problem being corrected

The current system still has three partially separate surfaces:
- Dream orchestration / runner surface
- DMG question/mutation surface
- direct route execution surface (`internal_validation_service.py`, `project_scoped_live_learning.py`)

That separation makes it too easy to run stacks outside the Dream runner and too hard to treat question batteries as first-class Dream inputs.

---

## Correct target architecture

## Dream runner responsibilities
The Dream runner should become the single top-level execution entrypoint for stack work.

It should own:
- stack manifest ingestion
- question battery ingestion
- Dream path-family selection
- DMG question / mutation generation
- route execution planning
- child-run execution
- scoring
- audit bundling
- packet / bridge outputs
- comparative stack summaries

## DMG responsibilities inside the runner
DMG should remain responsible for:
- question generation
- route-aware mutation generation
- suggestion/spec generation
- question-family variation

But it should be called by the runner as an internal stage, not used as an external sibling workflow.

## Direct route scripts
Scripts like:
- `internal_validation_service.py`
- `project_scoped_live_learning.py`

should be treated as execution backends invoked by the Dream runner.

---

## Native question battery contract

The Dream runner should accept a first-class `question_battery.json` input.

That battery should support:
- stack ids
- substantive objectives
- question families
- Dream path-family preferences
- DMG mutation settings
- execution route hints
- success-shape targets
- scoring preferences

Question batteries should no longer need to live as ad hoc side artifacts loosely attached to runs.

---

## Stack execution contract

Each stack inside the Dream runner should be represented as:
- stack_id
- substantive_objective
- question_family
- dream_path_family
- dmg_role
- execution_route
- questions[]
- success_shape[]
- scoring_dimensions[]

This gives the runner enough information to execute and compare stacks cleanly.

---

## Proposed Dream runner stage order

1. ingest stack manifest
2. ingest question battery
3. normalize stack cells
4. run DMG generation/mutation for each stack as configured
5. select/expand execution cells
6. execute routes
7. collect child-run artifacts
8. score stack cells
9. emit audit bundle
10. emit comparative operator summary
11. optionally emit bridge/handoff packets

---

## Migration rule

### Old pattern
- battery outside runner
- DMG outside runner
- direct route scripts called manually

### New pattern
- battery inside runner
- DMG called by runner
- direct route scripts only called through runner

This migration should be the default for all future stack work.

---

## Immediate implementation target

The fastest path is not to replace Dream runner entirely.
It is to evolve `run_dream_learn_dmg_cycle.py` so it can:
- accept a question battery file directly;
- accept stack metadata;
- preserve DMG generation as an internal stage;
- execute stack-specific route plans;
- emit comparative stack-level summaries.

That gives us the architecture correction without rebuilding the whole runner from scratch.

---

## Immediate operational rule

Until the implementation is complete:
- do not design new stacks as top-level direct-route runs;
- treat all new stack work as Dream-runner work, even if the current implementation still needs transitional glue.

---

## Final judgment

The split-brain fix is not another Stack C patch in isolation.
It is making the Dream runner the single stack execution surface and embedding DMG inside it with a native question-battery contract.
