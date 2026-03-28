# Regina G5 git discipline status — 2026-03-28

Gate: `G5_GIT_DISCIPLINE_READY`
Current practical status: `PASS_WITH_LIMITS`

<<<<<<< HEAD
## Why this is now materially live
=======
## Why this is no longer NOT_STARTED
>>>>>>> origin/main
The following now exist:
- branch naming contract
- stronger PR template
- review gate checklist
- combined control summary tying Dream/DMG and GitHub state together
<<<<<<< HEAD
- first real Regina PR under the new workflow discipline

## Why this is still only PASS_WITH_LIMITS
The workflow discipline is now both documented and used once, but not yet proven through repeated real PR/review/merge use across multiple Regina changes.

## What would upgrade this gate further
- multiple material Regina changes go through branch -> PR -> review -> merge
- repo-history ingest captures those changes cleanly over time
- the control summary reflects recurring review/merge state instead of a first example only
=======

## Why this is still only PASS_WITH_LIMITS
The workflow discipline is now documented, but not yet proven through repeated real PR/review/merge use in the Regina repo.

## What would upgrade this gate further
- at least one material Regina change goes through branch -> PR -> review -> merge
- repo-history ingest captures that activity cleanly
- the control summary reflects real review state rather than zero-PR truth
>>>>>>> origin/main

## Relevant artifacts
- `.github/pull_request_template.md`
- `reports/regina_git_pr_workflow_contract_2026-03-28.md`
- `reports/regina_pr_review_gate_checklist_2026-03-28.md`
- `reports/regina_control_summary_2026-03-28.md`
<<<<<<< HEAD
- `reports/regina_first_pr_review_note_2026-03-28.md`

## Operator note
The remaining gap is repeatability and continued use, not missing governance docs.
=======

## Operator note
The remaining gap is behavioral adoption, not missing governance docs.
>>>>>>> origin/main
