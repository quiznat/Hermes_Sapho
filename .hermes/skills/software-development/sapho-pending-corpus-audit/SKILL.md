---
name: sapho-pending-corpus-audit
description: Audit Sapho article corpus state when someone asks about the remaining pending corpus; distinguish current publication_status from stale imported runtime filter metadata.
---

# Sapho pending corpus audit

Use this when a user asks questions like:
- "find the pending article corpus"
- "what pending items are left?"
- "audit the remaining pending corpus"
- "is there any non-imported pending corpus left?"

This workflow is for `/home/hermes/sapho-native` and is specifically meant to avoid a common misread: imported articles may still carry `imported_from_runtime_filter_state: pending` even when the actual local Sapho remediation state is no longer pending.

## Core insight

There are at least two different meanings of "pending":

1. `publication_status` in `articles/*/article.md`
   - This is the current Sapho-native workflow state.
   - This is the field to use when the user asks what work remains locally.

2. `imported_from_runtime_filter_state` in `articles/*/article.md`
   - This is inherited runtime-import metadata from the original source/checkin.
   - It may remain `pending` even after local remediation is complete.
   - Do not mistake this field for current actionable backlog.

## Audit procedure

1. Count actual local article statuses.
   - Inspect `articles/art-*/article.md` frontmatter.
   - Count `publication_status` values.
   - Specifically check whether any are truly `pending`.

2. Check whether the corpus is imported, non-imported, or mixed.
   - Count packages with and without `imported_from_runtime_article_id`.
   - If all packages have that field, the visible corpus is entirely imported-runtime remediation output.

3. Separately count stale runtime-import metadata.
   - Count `imported_from_runtime_filter_state` values.
   - Report this separately and explicitly label it as inherited metadata, not current workflow state.

4. Inspect historical remediation reports under `state/reports/`.
   - Look for files like `historical-remediation-*.json` and `old-runtime-unseen-stalled-pending-*.json`.
   - Use them to answer:
     - whether earlier pending/stalled items were absorbed into `sapho-native/articles`
     - whether the final remediation slice exhausted the backlog

5. Check `historical-policy.json` coverage.
   - Count `policy_status` values such as `current_law_compliant` and `blocked_not_publishable`.
   - Note any packages missing policy files; these may be duplicate-rejected edge cases.

6. If the user asked about a non-imported pending corpus, verify whether it exists at all.
   - If `non_imported_count == 0`, say so directly.
   - Do not imply there is a local non-imported pending set unless you actually find one.

## Useful commands / patterns

Use file tools or a small Python script to parse frontmatter over `articles/art-*/article.md`.

Recommended derived outputs:
- total article count
- `publication_status` counts
- imported vs non-imported counts
- `imported_from_runtime_filter_state` counts
- top source domains
- representative examples by outcome
- report reconciliation: how many old pending IDs are now present vs still missing

## Interpretation rules

- If `publication_status: pending` count is zero, the local pending corpus is drained.
- If `imported_from_runtime_filter_state: pending` remains nonzero, present it as stale provenance metadata unless repo code proves it is still actively consumed as current truth.
- If all articles are imported, then any request about the "non-imported pending corpus" likely refers to some other location outside `sapho-native/articles`.
- If an older report says items were "stalled pending not present in sapho_native", reconcile that report against current article IDs before concluding anything is still missing.

## Verification checklist

Before reporting back, confirm all of the following:
- You counted `publication_status`, not just any field containing the word `pending`.
- You explicitly distinguished runtime-import metadata from current local status.
- You checked whether any non-imported articles exist at all.
- You reconciled at least one relevant `state/reports/*.json` file if the user referenced historical remediation.
- Any claim that the backlog is exhausted is backed by current counts and/or final remediation reports.

## Common pitfall

Do not answer "yes, many pending articles remain" just because many packages contain `imported_from_runtime_filter_state: pending`. In this repo that field can persist after remediation, so the actionable pending queue may actually be zero.
