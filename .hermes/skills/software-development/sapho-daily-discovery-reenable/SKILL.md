---
name: sapho-daily-discovery-reenable
description: Trace and re-enable Sapho daily discovery/queue-building and PM publication scheduling in either the legacy openclaw-backed runtime or the Hermes-native compact runtime.
---

Use this when someone says Sapho remediation is done and they want daily scanning/discovery turned back on so new articles enter the queue automatically and lawful articles keep publishing each day.

## What this skill is for

This skill covers two runtime modes:
1. Legacy openclaw-backed discovery under `/home/openclaw/.openclaw/workspace`
2. Hermes-native compact discovery under `/home/hermes/sapho-native/runtime`

In both modes, the user goal is the same: restore daily scanning so new articles enter the queue automatically and lawful articles keep publishing each day on Website 2.0.

The goal is to answer three questions quickly and accurately:
1. What code actually performs discovery/scanning?
2. What scripts form the daily AM and PM job chain?
3. What execution identity, credentials, and scheduling mechanism are required to turn it back on?

## Core pipeline to trace

### AM discovery + queue-building
Primary wrapper:
- `/home/hermes/sapho-native/scripts/run_runtime_am_job.py`

This calls:
- `/home/hermes/sapho-native/scripts/run_micro_am_shift.py`

`run_micro_am_shift.py` does the real orchestration:
1. `refresh_live_discovery()`
   - runs `/home/hermes/sapho-native/scripts/run_brave_feeder_local.py`
   - then calls `refresh_live_intake_ops_mirror()` from `runtime_ops.py`
2. `live_order()`
   - prefers `discover_checkin_order()`
   - falls back to `load_default_order()`
3. `ensure_local_article(...)`
   - imports discovered runtime items locally when needed
4. `run_article_lane(...)`
   - runs `/home/hermes/sapho-native/scripts/run_micro_article_lane.py --article-id ...`

### Discovery/scanning engine
Primary scanner:
- `/home/hermes/sapho-native/scripts/run_brave_feeder_local.py`

It aggregates:
- Brave web search
- RSS feeds
- sitemap roots
- arXiv

Config:
- `/home/hermes/sapho-native/discovery/config.seed.yaml`

### Runtime article store / live queue
Discovery inserts live article bundles through:
- `/home/hermes/sapho-native/scripts/article_bundle_store_local.py`

Key function:
- `ensure_article_bundle_for_discovery(...)`

Legacy mode writes to:
- `/home/openclaw/.openclaw/workspace/research/articles`

Hermes-native compact mode writes to:
- `/home/hermes/sapho-native/runtime/research/articles`

New discovered bundles default to:
- `filter_state: pending`
- `last_stage: intake`

That is the live intake queue.

### Live checkin / queue order
Queue/checkin plumbing:
- `/home/hermes/sapho-native/scripts/runtime_ops.py`

Key functions:
- `build_runtime_checkin_payload(...)`
- `write_runtime_checkin(...)`
- `refresh_live_intake_ops_mirror()`

Legacy mode writes:
- `/home/openclaw/.openclaw/workspace/research/factory/checkins/article-checkin-latest.json`

Hermes-native compact mode writes:
- `/home/hermes/sapho-native/runtime/research/factory/checkins/article-checkin-latest.json`

Important experiential fix:
- native checkins should include `processablePendingArticleIds`, not just `stalledPendingArticles`
- `discover_checkin_order()` should prefer `processablePendingArticleIds` and fall back to stalled items only if needed

That checkin is consumed by:
- `/home/hermes/sapho-native/scripts/import_runtime_backlog.py`
  - `discover_checkin_order()`
  - `discover_front_half_order()`
  - `load_default_order()`

### PM daily publish
Primary wrapper:
- `/home/hermes/sapho-native/scripts/run_runtime_pm_job.py`

This calls:
- `/home/hermes/sapho-native/scripts/run_micro_pm_publish.py`

`run_micro_pm_publish.py`:
- checks whether there are `ready-for-daily` articles for the target date
- runs the PM cycle
- blocks if conclave verdict is not pass
- renders/deploys the daily briefing surfaces

## How to inspect current readiness

### 1. Check whether anything is already scheduled
Use:
- `cronjob(action='list')`
- `terminal("crontab -l 2>/dev/null || true")`
- `terminal("systemctl list-timers --all ...")` if systemd is available

Do not assume the jobs still exist.

### 2. Check whether discovery credentials are available
`run_brave_feeder_local.py` looks for:
- `BRAVE_API_KEY` env var
or
- `/home/openclaw/.openclaw/openclaw.json` with `tools.web.search.apiKey`

### 3. Check whether the scheduler identity can access the live runtime
The important live path is:
- `/home/openclaw/.openclaw/workspace`

Many scripts are hard-wired to that path.

`run_micro_am_shift.py` also uses:
- `sudo -n -u openclaw ...`
for live discovery steps.

If the executing user does not have non-interactive access to `openclaw`, Hermes-level scheduling may fail even if the scripts are present.

## Critical experiential findings

1. Do not treat a dead-looking feeder as necessarily broken.

`run_brave_feeder_local.py` intentionally pauses discovery when pending backlog exceeds the configured threshold.

The key config is in `/home/hermes/sapho-native/discovery/config.seed.yaml`.

Current proven operating preference in Hermes-native mode:
- `maxPendingNonXBeforePause: 32`
- daily artifact publication target: `8`
- AM ingest run should use `--max-inclusions 8`

So if scanning appears “off,” verify whether it is actually:
- paused due to backlog above the configured threshold,
- missing credentials,
- unscheduled,
- or blocked by execution identity/permissions.

2. In Hermes-native compact mode, a dry-run can look healthy even while the real queue is not draining correctly.

A real issue encountered:
- discovery wrote native runtime bundles and checkins successfully
- `run_micro_am_shift.py --dry-run` looked fine
- but real processing initially left runtime items stuck in `pending`
- cause: the native runtime bundle state was not being synced back from the compact article result

Fix:
- after `run_micro_article_lane.py`, update the native runtime article bundle's `filter_state` and `last_stage`
- then regenerate the runtime checkin so `processablePendingArticleIds` shrinks correctly

3. In Hermes-native compact mode, some newly discovered items may exist only as runtime article stubs without local `source-material/*.json` / `*.txt` snapshots.

A real issue encountered:
- the import bridge expected runtime source json/txt files and would otherwise classify items as missing-runtime-source-* and skip them

Reusable fix:
- allow ticket-only import when runtime source snapshots are absent
- write a compact queue ticket anyway
- then run `capture_source.py` locally from that queue ticket before handing off to `run_micro_article_lane.py`
- after lane completion, sync the local article result back into the native runtime article bundle so `filter_state` becomes `kept` or `discarded` instead of remaining `pending`

4. In github-pages mode, the old ops/site deploy seam can silently remain coupled to `/home/openclaw/.openclaw/workspace`.

Reusable fix:
- for Hermes-native compact mode, publish or mirror ops surfaces locally instead of trying to run the legacy live-site deploy path
- likewise, in PM publish, skip the old deploy seam when `SAPHO_SITE_MODE=github-pages`

## Recommended execution model

First determine which runtime mode you are in.

### A. Legacy openclaw-backed mode
Prefer scheduling the daily jobs under `openclaw` or `root` at the system level when the code is still coupled to `/home/openclaw/.openclaw/workspace`.

Recommended jobs:
- AM: `python3 /home/hermes/sapho-native/scripts/run_runtime_am_job.py`
- PM: `python3 /home/hermes/sapho-native/scripts/run_runtime_pm_job.py`

Why this is usually better than Hermes cron:
- the scripts are written for the openclaw runtime and paths
- they expect access to `/home/openclaw/.openclaw/workspace`
- Hermes scheduling may fail without passwordless sudo or equivalent non-interactive access

Only use Hermes cron in legacy mode if you first verify:
- the live runtime can be accessed non-interactively from the Hermes execution context
- Brave credentials are available in that scheduled context

### B. Hermes-native compact mode
If the user wants adaptation to Sapho compact rules and Hermes-native runtime, migrate the discovery pipeline to a local runtime under:
- `/home/hermes/sapho-native/runtime`

Key reusable changes:
- add a small path shim module (for example `scripts/runtime_paths.py`) and route all runtime roots through it
- change `article_bundle_store_local.py` to write runtime article bundles under `sapho-native/runtime/research/articles`
- change `runtime_ops.py` to read/write native runtime checkins under `sapho-native/runtime/research/factory/checkins`
- remove `sudo -n -u openclaw` assumptions from `run_micro_am_shift.py` and run discovery locally
- teach `run_brave_feeder_local.py` to load `BRAVE_API_KEY` from Hermes context too (for example `~/.hermes/.env`), not just `~/.openclaw/openclaw.json`
- make `run_micro_am_shift.py` able to import ticket-only runtime discoveries, run `capture_source.py`, then run `run_micro_article_lane.py`
- after local article processing, sync the result back into the native runtime bundle so processed items stop remaining `pending` forever in the runtime checkin
- in github-pages mode, avoid the old live-site deploy seam for PM publish and ops surfaces; use local/public-site outputs instead

In Hermes-native compact mode, Hermes cron is appropriate.

Example daily jobs:
- AM: `SAPHO_SITE_MODE=github-pages python3 scripts/run_runtime_am_job.py --max-inclusions 8`
- PM: `SAPHO_SITE_MODE=github-pages python3 scripts/run_runtime_pm_job.py`

A proven schedule used successfully:
- AM: `0 13 * * *` (13:00 UTC, about 9 AM America/New_York in DST)
- PM: `0 22 * * *` (22:00 UTC, about 6 PM America/New_York in DST)

## Fast answer template for users

When the user asks what must be turned back on, give them:
1. the AM chain: `run_runtime_am_job.py -> run_micro_am_shift.py -> run_brave_feeder_local.py`
2. the live queue store: `article_bundle_store_local.py` into `/home/openclaw/.openclaw/workspace/research/articles`
3. the live checkin: `runtime_ops.py` writing `article-checkin-latest.json`
4. the PM chain: `run_runtime_pm_job.py -> run_micro_pm_publish.py`
5. the missing operational pieces:
   - schedule
   - correct execution identity
   - Brave credential availability
   - backlog pause threshold awareness

## Pitfalls

- Do not confuse this with Website 2.0 GitHub Pages deployment. This is the live runtime discovery path.
- Do not claim scanning is broken before checking the pause threshold in `config.seed.yaml`.
- Do not schedule Hermes cron blindly if the environment cannot access `/home/openclaw/.openclaw/workspace` non-interactively.
- Do not assume existing cron/timer jobs are still present; verify first.
- Do not forget PM publishing; re-enabling only AM scanning builds backlog but does not restore daily publication cadence.

## Git tracking guidance after Hermes-native re-enable

Once the Hermes-native compact runtime is working, keep durable artifacts tracked but ignore transient runtime noise.

Track:
- code and config changes under `sapho-native/scripts/` and `sapho-native/discovery/`
- durable article packages under `sapho-native/articles/`
- durable queue tickets under `sapho-native/queue/`
- durable native runtime article bundle state under `sapho-native/runtime/research/articles/`
- durable publication-authority artifacts when they are part of the reviewed corpus state

Ignore:
- `sapho-native/state/receipts/`
- `sapho-native/state/discovery/logs/`
- `sapho-native/state/discovery/query-yield-scoreboard.jsonl`
- `sapho-native/public/site/artifacts/ops/`
- `sapho-native/public/site/data/ops-latest.json`
- `sapho-native/runtime/research/factory/checkins/`
- `sapho-native/runtime/website/artifacts/ops/`
- `sapho-native/runtime/website/data/ops-latest.json`

Practical note:
- if transient files were already tracked before ignore rules were added, remove them from git tracking with `git rm --cached` and commit the cleanup alongside the `.gitignore` update
- zero-byte placeholder `claims.jsonl` / `evidence.jsonl` / `facts.jsonl` / `findings.jsonl` files should not be committed; delete them locally if they were created during partial runs

## Useful validation checks

After re-enabling, verify:
- `run_brave_feeder_local.py` returns a summary JSON with `paused`, `inserted`, and `pendingArticles`
- live runtime bundles appear under the active runtime article root (`/home/openclaw/.openclaw/workspace/research/articles` in legacy mode or `/home/hermes/sapho-native/runtime/research/articles` in Hermes-native mode)
- `article-checkin-latest.json` is updated
- `run_runtime_am_job.py` writes a receipt for `research-am-ingest-shift`
- `run_runtime_pm_job.py` writes a receipt for `research-pm-live-synthesis-shift`
- PM publish exits cleanly or explicitly reports `blocked <date> <verdict>`
