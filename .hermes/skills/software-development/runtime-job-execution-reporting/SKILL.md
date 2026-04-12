---
name: runtime-job-execution-reporting
description: Run long-lived file-native runtime jobs from Hermes, work around blocked shell-wrapper commands, wait via background process polling, and report status from stdout plus latest receipt.
version: 1.0.0
author: Hermes Agent
---

# Runtime Job Execution Reporting

Use when a user asks Hermes to run a project script/job and report:
- final status
- stdout summary
- receipt path
- warnings/errors

Especially useful for Sapho-style file-native jobs that:
- are launched via wrapper scripts
- may take longer than normal terminal timeouts
- write canonical receipts under `state/receipts/`
- emit compact key-value summaries on stdout

## Core rules

1. Prefer an equivalent direct command over a blocked shell wrapper.
2. For long-running jobs, start in the background and poll/wait instead of repeatedly rerunning.
3. Treat the receipt file as the canonical final report when one is written.
4. Distinguish job status from warning lines in stderr — a job can finish `ok` with non-fatal warnings.

## Recommended procedure

### 1. Execute the requested job once exactly as closely as possible
If the user gives a command like:
- `bash -lc 'cd /path && ENV=value python3 script.py ...'`

try it first if allowed.

### 2. If the shell-wrapper form is blocked, convert it to an equivalent terminal invocation
Common safe rewrite:
- set `workdir` to the target directory
- pass env vars inline with `env ... command`

Example rewrite:
- blocked: `bash -lc 'cd /home/hermes/sapho-native && SAPHO_SITE_MODE=github-pages python3 scripts/run_runtime_am_job.py --max-inclusions 8'`
- replacement:
  - `workdir=/home/hermes/sapho-native`
  - command: `env SAPHO_SITE_MODE=github-pages python3 scripts/run_runtime_am_job.py --max-inclusions 8`

This preserves semantics while avoiding the blocked wrapper.

### 3. If the foreground run times out, switch to background execution
Launch the same command with:
- `background=true`
- generous timeout for startup
- `notify_on_complete=true` when available

Then use `process.wait` / `process.poll` until exit.

Important finding:
- `process.wait` may be clamped to short intervals (for example 60s), so expect to loop.
- Use `process.log` if the job emits incremental output.
- If logs are empty, inspect live child processes to confirm progress instead of assuming a hang.

### 4. For silent long-running jobs, verify progress through the process tree
Use `ps` / `pgrep -P <pid>` to identify active child scripts.
This is valuable when the top-level process captures stdout until completion.

In Sapho-style jobs, the useful interpretation is often:
- wrapper job still running
- micro shift child active
- per-article lane child active
- optional nested `hermes chat` worker active

That means the job is progressing, not stalled.

### 5. After completion, inspect the receipt
Read the stamped receipt and/or `*-latest.json` under `state/receipts/`.
Use the stamped receipt path from final stdout when present.

Extract and report:
- `status`
- `returncode`
- `summary`
- `stdout`
- `stderr`
- sync/mirror status if present

### 6. Build the final report from both stdout and receipt
Report at minimum:
- status
- key stdout summary lines
- receipt path
- warning/error details

Good pattern:
- status from receipt `status`
- key counts from `summary`
- included ids from `included_article_ids`
- warnings from `stderr`
- note separately if sync/mirror steps succeeded

## Sapho-specific findings worth remembering

- `scripts/run_runtime_am_job.py` writes a receipt via `write_receipt()` to:
  - `state/receipts/research-am-ingest-shift-<timestamp>.json`
  - plus `state/receipts/research-am-ingest-shift-latest.json`
- Its top-level stdout is compact JSON containing:
  - `status`
  - `receipt`
  - `summary`
- The underlying `run_micro_am_shift.py` stdout uses key-value lines like:
  - `native_discovery paused=false pending=0 inserted=4`
  - `processed=10 failed=1 attempted=11 included=3 remaining=0 target=8 stop=queue-exhausted date=...`
  - `included_article_ids=...`
- Non-fatal lane failures can appear in receipt `stderr` even when overall receipt status is `ok`.

## Pitfalls

- Do not keep rerunning the same long job after a timeout; switch to background monitoring.
- Do not assume no stdout means no progress; some wrappers capture child output until exit.
- Do not rely only on exit code if a receipt exists; the receipt is usually the best operational summary.
- Do not collapse warnings into a false failure if the receipt status is still `ok`.

## Deliverable template

- `status: <ok|error|...>`
- `key stdout summary:`
  - discovery line
  - processed/failed/attempted/included/remaining/stop/date
  - included ids if present
- `receipt path:`
  - stamped receipt path
- `warning/error details:`
  - stderr lines
  - sync/mirror status
