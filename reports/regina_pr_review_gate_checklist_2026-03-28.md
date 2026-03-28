# Regina PR review gate checklist — 2026-03-28

Use this checklist when opening or reviewing material Regina PRs.

## A. Scope discipline
- [ ] PR stays inside one approved lane or one tightly coupled implementation slice
- [ ] PR does not silently widen scope
- [ ] PR does not mix governance, public wording, and methods changes without saying so explicitly

## B. Authority discipline
- [ ] canonical current-state authority was checked when relevant
- [ ] claim-control files outrank support artifacts
- [ ] KG / repo-history / graph artifacts are not treated as authority over claim-control files

## C. Confidence discipline
- [ ] observed / inferred / estimated / unsupported labels remain intact where applicable
- [ ] support-only or appendix-only material is not promoted above its allowed ceiling
- [ ] blocked lanes remain blocked unless explicitly revalidated

## D. Artifact discipline
- [ ] PR links exact Dream/DMG run artifacts if automation is involved
- [ ] PR links exact repo-history / audit artifacts if governance is involved
- [ ] PR links exact reports or ledgers touched
- [ ] PR leaves a durable report or status artifact if it changes control behavior

## E. Review discipline
- [ ] required review gates were selected in the PR template
- [ ] reviewer checked contradiction risk
- [ ] reviewer checked merge readiness against current gate status

## F. Merge discipline
- [ ] merge is safe relative to the current Regina claim envelope
- [ ] merge does not imply policy/canon advancement without approval
- [ ] post-merge next step is clear

## Minimum merge statement
Reviewer or merge owner should be able to say:
- what changed
- what gate it touched
- what artifacts prove it
- why it is safe to merge now
