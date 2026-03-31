# Sapho Phase 1 Handoff

Date: 2026-03-31
Workspace: `/home/hermes/sapho-native`
Status: Phase 1 complete enough to clear chat context and resume with Phase 2.

## Planning baseline
Use these docs as authoritative planning set:
- `/home/hermes/sapho-docs/2026-03-31-current-system-map.md`
- `/home/hermes/sapho-docs/2026-03-31-piter-2-control-plane-spec.md`
- `/home/hermes/sapho-docs/2026-03-31-sapho-full-implementation-plan.md`
- `/home/hermes/sapho-docs/2026-03-31-sapho-parallel-system-roadmap.md`
- `/home/hermes/sapho-docs/2026-03-31-sapho-operations-blueprint.md`
- `/home/hermes/sapho-docs/2026-03-31-daily-rail-schema-spec.md`
- `/home/hermes/sapho-docs/2026-03-31-daily-rail-validator-spec.md`
- `/home/hermes/sapho-docs/2026-03-31-execution-substrate-replacement-spec.md`
- `/home/hermes/sapho-docs/2026-03-31-shadow-publication-and-cutover-spec.md`
- `/home/hermes/sapho-docs/2026-03-31-implementation-task-breakdown.md`

## Scope rule still in force
- Build order:
  1. replace execution seam
  2. strengthen internal artifact bundles
  3. add validators in warn mode
  4. add Piter 2.0 control plane
  5. add shadow publication targets
  6. run shadow proof
  7. cut over
- Canon remains out of scope until Daily Rail parity++ is proven through shadow operation.

## What was built in Phase 1
A clean new build workspace was created at:
- `/home/hermes/sapho-native`

It was copied from:
- `/home/openclaw/.openclaw/workspace/parallel-sapho`

But work is now happening in the new workspace, not in the live runtime tree.

### New files
- `/home/hermes/sapho-native/scripts/task_runner.py`
- `/home/hermes/sapho-native/micro/task_runner.json`
- `/home/hermes/sapho-native/tests/test_task_runner.py`

### Modified files
- `/home/hermes/sapho-native/scripts/micro_common.py`

## Phase 1 result
The execution seam was replaced at the compatibility boundary:
- old path: `micro_common.py -> run_loose_agent() -> run_pocket_agent() -> OpenClaw worker`
- new default path: `micro_common.py -> run_loose_agent() -> task_runner.run_task() -> Hermes CLI`

### Canonical runtime interface added
`run_task(role, prompt, timeout, thinking, context=None) -> TaskResult`

### TaskResult fields
- `status`
- `role`
- `raw_output`
- `clean_output`
- `started_at_utc`
- `finished_at_utc`
- `duration_seconds`
- `backend`
- `model`
- `error`
- `receipt_path`

### Receipts
Task-run receipts write to:
- `/home/hermes/sapho-native/state/receipts/task-runs/`

### Role config surface
Role/backend config is now in:
- `/home/hermes/sapho-native/micro/task_runner.json`

Current configured role mapping:
- provider: `openai-codex`
- model: `gpt-5.4`
for curator, extractor, synthesist, orchestrator

This was chosen because initial OpenRouter-style model strings failed under the local Hermes/Codex environment.

## Rollback path
Legacy execution remains available behind env flag:
- `SAPHO_USE_LEGACY_OPENCLAW=1`

That causes `run_loose_agent()` to use the old `run_pocket_agent()` path.

## Validation performed
### Test suite
Ran:
- `python3 -m unittest discover -s tests -p 'test_*.py' -v`

Result at completion:
- 16 tests passed

### Smoke tests run
1. direct task runner smoke test:
- `run_task('curator', 'Reply with exactly KEEP and nothing else.', ...)`
- result: status `ok`, clean output `KEEP`

2. compatibility adapter smoke test:
- `run_loose_agent('curator', 'Reply with exactly KEEP and nothing else.', ...)`
- result: `KEEP`

## Important implementation details
### Output cleaning
`task_runner.py` normalizes Hermes CLI output by stripping:
- terminal chrome / box drawing lines
- session_id lines
- code fences
- common CLI noise prefixes
- repeated blank lines

It also classifies obvious CLI/provider failure text as `error` instead of falsely treating it as usable output.

### What was intentionally not touched yet
Many files in `/home/hermes/sapho-native/scripts/` still contain old-runtime/live-path assumptions unrelated to the phase-1 seam change, including some references to `/home/openclaw/...` for import, deployment, and publication surfaces.
Those are expected follow-on phases, not incomplete phase-1 seam work.

## What Phase 2 should do next
Phase 2 target from plan:
- strengthen internal article bundles
- preserve current public/article behavior
- add structured internals alongside compatibility markdown outputs

Minimum intended outputs to add:
- `curator.json`
- `findings.jsonl`
- `facts.jsonl`
- `claims.jsonl`
- `evidence.jsonl`
- `lineage.json`
- `validation.json`

Keep existing compatibility outputs in place:
- `micro-worthiness.md`
- `micro-findings.md`
- `micro-facts.md`
- `micro-summary.md`
- existing `article.md` public-facing structure

Likely first files to inspect for Phase 2:
- `/home/hermes/sapho-native/scripts/run_micro_article_lane.py`
- `/home/hermes/sapho-native/scripts/common.py`
- `/home/hermes/sapho-native/scripts/article_bundle_store_local.py`
- existing article fixture/package examples under `/home/hermes/sapho-native/articles/`

## Resume instruction
When resuming in a fresh chat, start from:
- workspace: `/home/hermes/sapho-native`
- current milestone: Phase 2 structured artifact bundle upgrade
- constraint: do not tie new work back into current live runtime; build in the clean workspace and keep rollback clear
