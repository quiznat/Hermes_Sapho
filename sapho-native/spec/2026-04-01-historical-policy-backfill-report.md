# Historical Policy Backfill Report

Date: 2026-04-01
Workspace: `/home/hermes/sapho-native`

## Purpose

Make historical-package policy explicit without greenwashing legacy published material.

The backfill now writes `historical-policy.json` for each article package.
This policy artifact distinguishes:
- `legacy_quarantined` — imported historical package remains published in the old corpus but is not eligible under current law because contradiction/mechanism requirements are still missing
- `blocked_not_publishable` — imported package is already blocked/discarded/duplicate-rejected and is not a publication candidate under current law
- `current_law_compliant` — imported package satisfies current law with the required lawful artifacts present

## Result summary

After running `python scripts/backfill_structured_bundles.py` across the corpus:

- `legacy_quarantined`: 34
- `blocked_not_publishable`: 28
- `current_law_compliant`: 1

Representative examples:
- `legacy_quarantined`: `art-2026-03-01-001`
- `blocked_not_publishable`: `art-2026-03-01-006`
- `current_law_compliant`: `art-2026-03-04-018`

## Interpretation

This backfill does not pretend that historical packages are lawful when they are not.
Instead it makes the status explicit:
- historical published packages missing contradiction/mechanism review are quarantined from current-law eligibility
- already blocked historical packages are marked as non-candidates
- the small number that really satisfy current law are identified as compliant

## Operational implication

This resolves the immediate policy ambiguity in the corpus, but it does not replace real legal review backfill.
The next substantive step remains:
- perform real contradiction/mechanism backfill where desired, or
- leave packages explicitly quarantined under current law
