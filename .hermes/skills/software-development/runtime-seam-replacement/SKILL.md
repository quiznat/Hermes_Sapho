---
name: runtime-seam-replacement
description: Replace a legacy task execution seam with a clean adapter-backed runner while preserving business logic, receipts, and rollback.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [runtime, adapter, migration, receipts, rollback, python]
    related_skills: [writing-plans, subagent-driven-development, systematic-debugging]
---

# Runtime Seam Replacement

## When to use

Use this when a system has a narrow execution seam like:
- `compat_fn(...) -> legacy_backend(...)`
- one-shot agent or worker invocation hidden behind a helper
- production logic that should stay stable while the backend is swapped

This is especially useful when you must:
- avoid tying new work to the old runtime
- preserve current behavior first
- keep rollback simple
- add receipts and observability during the swap

## Core pattern

Keep business logic unchanged.
Replace only the seam.

Target shape:
- existing callers continue to call the compatibility function
- compatibility function calls a new canonical runner
- canonical runner returns a structured result object
- compatibility function returns only the cleaned payload expected by existing code
- legacy path remains behind an explicit feature flag for rollback

Example layering:
- `micro_common.run_loose_agent()`
  -> `task_runner.run_task(...)`
  -> returns `TaskResult.clean_output`

## Recommended implementation steps

### 1. Work in a clean build tree

If the live system exists elsewhere, copy into a new workspace first.
Do not start by editing the live runtime tree.

Example:
- source: `/home/openclaw/.openclaw/workspace/parallel-sapho`
- clean build: `/home/hermes/sapho-native`

Keep the new tree isolated from the old runtime.

### 2. Find the real seam

Search for the actual narrow call path, not every runtime dependency.

For Sapho this was:
- `scripts/micro_common.py`
- `run_loose_agent()`
- `openclaw_pocket_agent.run_pocket_agent()`

Do not boil the ocean. Replace the seam first.

### 3. Add a canonical runner module

Create a new module like `scripts/task_runner.py` with:
- `TaskResult` dataclass
- `run_task(role, prompt, timeout, thinking, context=None)`
- config loader
- output normalization
- receipt writing
- clear status classification: `ok | error | timeout | malformed`

Recommended TaskResult fields:
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

### 4. Make role mapping file-driven

Add a config file for role -> provider/model/persona mapping.

Example path:
- `micro/task_runner.json`

Include per-role:
- persona file
- identity name
- provider
- model

This keeps the new seam replaceable.

### 5. Preserve the old compatibility interface

Update the old helper to call the new runner by default.
Keep legacy behavior behind an env flag.

Example rollback flag:
- `SAPHO_USE_LEGACY_OPENCLAW=1`

Pattern:
- if rollback flag set -> call old backend
- else -> call `run_task(...)`
- if result is not `ok`, raise an explicit error
- otherwise return `result.clean_output`

### 6. Add tests at the seam

Add focused tests for:
- output normalization
- command construction
- receipt writing
- default path uses new runner
- rollback flag uses legacy backend
- backend failure text is classified as `error`

Do not rely only on full end-to-end tests.
The seam needs direct unit tests.

### 7. Run a real smoke test

After tests pass, invoke the new runner for a minimal real prompt.
Then invoke the compatibility adapter too.
Confirm both succeed and receipts are written.

## Output normalization pitfalls

CLI wrappers may print non-answer text even in quiet mode.
Do not assume stdout is only the answer.

Observed Hermes CLI quirks worth handling:
- banner box-drawing lines still appear in quiet mode
- `session_id: ...` trailer still appears
- provider/model warning lines may appear on stdout
- retry/failure diagnostics may appear on stdout instead of stderr

So normalization should strip at least:
- ANSI escape codes
- box-drawing/chrome lines
- `session_id:` lines
- obvious CLI warning prefixes like `⚠️`, `⏳`, `❌`, `🔌`, `🌐`, `📝`, `📋`, `💀`
- outer code fences
- excessive blank lines

Important:
backend failure text can survive normalization. Detect failure patterns explicitly and classify as `error`, not `ok`.

Patterns worth checking:
- `API call failed`
- `Max retries`
- `BadRequestError`
- HTTP 4xx/5xx markers
- model unsupported messages

## Model/provider compatibility pitfall

Do not assume configured provider/model pairs work in the current environment.
A real failure encountered:
- Hermes CLI running via `openai-codex`
- configured model `openrouter/google/gemini-2.5-flash-lite`
- result: HTTP 400 unsupported model for Codex ChatGPT account

Lesson:
- validate the runner with a real smoke test after wiring it up
- if the configured pair is unsupported, switch to a known-good local environment pair
- in this environment, `provider=openai-codex` with `model=gpt-5.4` worked

## Receipt guidance

Write one receipt per task invocation.
Include:
- role
- backend
- model
- timeout
- thinking
- context
- prompt hash
- timestamps
- duration
- status
- error
- receipt path

Suggested directory:
- `state/receipts/task-runs/`

## Verification checklist

- unit tests for the seam pass
- real `run_task()` smoke test passes
- compatibility adapter smoke test passes
- receipt file is written
- rollback env flag still works
- no production business-logic callers needed rewrites

## What not to do

- do not rewrite higher-level production logic during seam replacement
- do not remove the old path before proving the new one
- do not trust CLI quiet mode to mean clean stdout
- do not classify any non-empty stdout as success
- do not bind the new system to live runtime directories if the goal is clean separation

## Sapho-specific note

For Sapho Daily Rail, phase 1 should stop after the `run_loose_agent()` seam is replaced in the clean build tree. Other old-runtime references in import, publication, or deploy paths are separate later slices and should not be mixed into seam replacement.
