# Historical Remediation Batch 1 Report

Date: 2026-04-02
Workspace: `/home/hermes/sapho-native`
Replay date used: `2026-04-01`
Batch size: 5

## Summary

The first sanity-check batch was run with:

`python scripts/remediate_historical_imports.py --limit 5 --replay-date 2026-04-01`

Results:
- ok: 3
- error: 2
- artifact auto-publication: none

## Outcome table

1. `art-2026-03-01-001`
- before: `published` / `legacy_quarantined`
- after: `discarded` / `blocked_not_publishable`
- result: Curator now discards the package under the new lane

2. `art-2026-03-02-001`
- before: `published` / `legacy_quarantined`
- after: `discarded` / `blocked_not_publishable`
- result: Curator now discards the package under the new lane

3. `art-2026-03-02-013`
- before: `published` / `legacy_quarantined`
- after: `discarded` / `blocked_not_publishable`
- result: Curator now discards the package under the new lane

4. `art-2026-03-02-025`
- before: `published` / `legacy_quarantined`
- after: unchanged
- result: replay error `extractor_evidence_count_mismatch`

5. `art-2026-03-03-001`
- before: `published` / `legacy_quarantined`
- after: unchanged
- result: replay error `extractor_evidence_count_mismatch`

## Interpretation

This first batch suggests two distinct historical outcomes:

- some legacy published packages are not merely missing law reviews; they are no longer worthy under the stricter current bounded Curator lane and are now discarded
- some packages hit an Extractor contract mismatch during replay and need debugging before larger batch rollout

Because 2 of 5 failed at the Extractor contract stage, wider replay should pause until that error class is understood.

## Human validation artifacts

Primary batch report:
- `/home/hermes/sapho-native/state/reports/historical-remediation-20260402T004418Z.json`

Per-article artifact paths for review:

### art-2026-03-01-001
- `/home/hermes/sapho-native/articles/art-2026-03-01-001/article.md`
- `/home/hermes/sapho-native/articles/art-2026-03-01-001/micro-worthiness.md`
- `/home/hermes/sapho-native/articles/art-2026-03-01-001/historical-policy.json`
- `/home/hermes/sapho-native/articles/art-2026-03-01-001/validation.json`
- `/home/hermes/sapho-native/articles/art-2026-03-01-001/source.md`

### art-2026-03-02-001
- `/home/hermes/sapho-native/articles/art-2026-03-02-001/article.md`
- `/home/hermes/sapho-native/articles/art-2026-03-02-001/micro-worthiness.md`
- `/home/hermes/sapho-native/articles/art-2026-03-02-001/historical-policy.json`
- `/home/hermes/sapho-native/articles/art-2026-03-02-001/validation.json`
- `/home/hermes/sapho-native/articles/art-2026-03-02-001/source.md`

### art-2026-03-02-013
- `/home/hermes/sapho-native/articles/art-2026-03-02-013/article.md`
- `/home/hermes/sapho-native/articles/art-2026-03-02-013/micro-worthiness.md`
- `/home/hermes/sapho-native/articles/art-2026-03-02-013/historical-policy.json`
- `/home/hermes/sapho-native/articles/art-2026-03-02-013/validation.json`
- `/home/hermes/sapho-native/articles/art-2026-03-02-013/source.md`

### art-2026-03-02-025
- `/home/hermes/sapho-native/articles/art-2026-03-02-025/article.md`
- `/home/hermes/sapho-native/articles/art-2026-03-02-025/historical-policy.json`
- `/home/hermes/sapho-native/articles/art-2026-03-02-025/validation.json`
- `/home/hermes/sapho-native/articles/art-2026-03-02-025/source.md`

### art-2026-03-03-001
- `/home/hermes/sapho-native/articles/art-2026-03-03-001/article.md`
- `/home/hermes/sapho-native/articles/art-2026-03-03-001/historical-policy.json`
- `/home/hermes/sapho-native/articles/art-2026-03-03-001/validation.json`
- `/home/hermes/sapho-native/articles/art-2026-03-03-001/source.md`

## Commitability note

The underlying article/runtime artifacts live under gitignored runtime paths (`sapho-native/articles/` and `sapho-native/state/`), so this report is the committed record of the batch while the raw package artifacts remain available on-disk for human validation.
