tags: [regina:canonical, regina:recovery, regina:cleanup, regina:control]
created_by: ChaosClaw
created_at: 2026-03-29T08:06:00+02:00

# Regina non-blocking caveats resolution — 2026-03-29

Status: canonical cleanup note
Purpose: record the immediate resolution steps taken against the main non-blocking caveats after recovery governance was put in place.

---

## Caveat 1 — commit authorship hygiene

### Problem
Recent commits were being authored with the default local identity (`root@...`), which is functional but poor hygiene for ongoing governed work.

### Resolution
Global git identity was set for future commits to:
- `user.name = ChaosClaw`
- `user.email = chaosclaw@local.invalid`

### Meaning
This does not rewrite past commits, but it fixes forward commit authorship hygiene.

---

## Caveat 2 — low-signal retrieval residue

### Problem
The active Regina repo-memory layer still contains a large number of low-signal `file_observation` rows.
These rows are not the main source of truth and should not compete with promoted canonical recovery/control claims.

### Resolution
Applied an explicit topic-level rank demotion in retrieval logic:
- `file_observation_summary` → mild negative bias
- `file_observation` → strong negative bias

### Meaning
This is a safe incremental cleanup step.
It does not delete historical extraction residue, but it reduces the chance that low-signal observations crowd out canonical recovery/control answers.

---

## What was deliberately not done yet

To avoid overreaching during recovery cleanup, the following were not attempted in this step:
- mass deletion or rewrite of the broader canonical workspace dirty tree
- broad pruning of historical repo-memory artifacts
- rewrite/amend of already-pushed commits for author identity cleanup
- wide retrieval refactors beyond the minimum needed to demote obvious low-signal residue

That restraint is intentional.

---

## Current posture after caveat resolution

The remaining caveats are now materially smaller:
- future commit identity hygiene is fixed;
- low-signal retrieval residue is explicitly downweighted;
- broader repository dirtiness remains real but is operationally separated from the scoped recovery PRs.

This keeps the recovery posture disciplined without turning caveat cleanup into another uncontrolled cleanup wave.
