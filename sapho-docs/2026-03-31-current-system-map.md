# Current Sapho System Map

Status: revised after direct live-file inspection
Date: 2026-03-31
Author: Hermes

## 1. Scope

This map is based on direct reads from the live OpenClaw workspace at:
- `/home/openclaw/.openclaw/workspace`
- especially `/home/openclaw/.openclaw/workspace/parallel-sapho`
- plus the public site at `/home/openclaw/.openclaw/workspace/website`

The purpose is to describe the actual running daily rail, not the older proving snapshot.

## 2. Operating identity and law

The live workspace defines Sapho this way:
- Piter is the operating personality and editorial executive
- Quiznat is the operator
- the live daily rail runs from `parallel-sapho`
- the public site runs from `website`
- one working path is preferred over multiple competing paths

Key live identity files confirm:
- `AGENTS.md` — one working path, current runtime only
- `SOUL.md` — Piter is editor/executive, not a generic assistant
- `USER.md` — compact, argument-led, mechanism/economics/implications style; queue links by default; route pipeline material through the rail
- `ACTIVE-SYSTEM-STATE.md` — current live rail and exact job chain

## 3. Exact active job chain

The live rail is scheduled from the `openclaw` crontab, with these logical jobs:
- AM ingest at `06:00 America/New_York`
- artifact publish poller every `5` minutes with `--max-items 1`
- PM briefing publish at `19:30 America/New_York`

Exact active chain from `ACTIVE-SYSTEM-STATE.md`:
- AM: `run_runtime_am_job.py` -> `run_micro_am_shift.py`
- Artifact publish: `run_runtime_artifact_job.py` -> `run_micro_artifact_watch.py` -> `run_micro_artifact_publish.py`
- PM: `run_runtime_pm_job.py` -> `run_micro_pm_publish.py` -> `run_pm_cycle.py` -> `run_micro_daily.py`

This is important: cron itself is already plain runtime execution. The main remaining OpenClaw seam is inside the micro agent calls.

## 4. What each active script actually does

### 4.1 `run_runtime_am_job.py`
Wrapper job.
- calls `run_micro_am_shift.py`
- captures stdout/stderr
- writes receipt `research-am-ingest-shift-latest.json`
- syncs runtime ops mirrors after execution

### 4.2 `run_micro_am_shift.py`
Real AM driver.
Responsibilities:
- refresh live discovery via `run_brave_feeder_local.py`
- refresh the live intake ops mirror
- get backlog order from:
  - preferred: latest `front-half*.json`
  - fallback: `research/factory/checkins/article-checkin-latest.json`
- import local copies of runtime items through `import_runtime_backlog.py`
- process each article through `run_micro_article_lane.py`
- stop after daily inclusion cap, default `8`
- publish runtime ops surfaces

This is the actual heart of the AM shift.

### 4.3 `run_runtime_artifact_job.py`
Wrapper job.
- calls `run_micro_artifact_watch.py --max-items 1`
- writes receipt `research-artifact-publish-poller-latest.json`
- syncs ops mirrors

### 4.4 `run_micro_artifact_watch.py`
Artifact poller.
Responsibilities:
- scan all `articles/*/article.md`
- find items with:
  - `publication_status=ready-for-daily`
  - minted artifact timestamp present
  - artifact publication not yet current
- dispatch one article at a time to `run_micro_artifact_publish.py`

This means artifact publication is incremental and decoupled from PM.

### 4.5 `run_micro_artifact_publish.py`
Artifact publication step.
Responsibilities:
- stage current live artifact surfaces from `website` into local `public/site`
- assign or reuse a publication alias
- generate public artifact markdown
- generate `/a/<alias>.html` and `/s/<alias>.html` redirects
- update `kept-links.html`, `data/kept-links.json`, `rss.xml`, `artifacts.xml`, `data/artifacts-feed.json`
- optionally deploy only artifact-related paths to the live website
- update article metadata with artifact publication fields

This script is effectively the Scriptorium rail for kept artifacts.

### 4.6 `run_runtime_pm_job.py`
Wrapper job.
- calls `run_micro_pm_publish.py`
- writes receipt `research-pm-live-synthesis-shift-latest.json`
- syncs ops mirrors

### 4.7 `run_micro_pm_publish.py`
PM publication coordinator.
Responsibilities:
- count articles ready for PM or already published for the date
- if there are ready articles, call `run_pm_cycle.py`
- if Conclave blocks, exit with block code
- refresh live intake ops mirror
- render daily briefing site surfaces
- deploy the daily-specific website paths

### 4.8 `run_pm_cycle.py`
Thin wrapper.
- calls `run_micro_daily.py --replay-date <date>`

### 4.9 `run_micro_daily.py`
The actual daily synthesis engine.
Responsibilities:
- select all articles ready for PM on the date
- assert canonical uniqueness of publication records
- chunk into clusters
- generate cluster notes with Synthesist
- generate technical daily and executive daily with Synthesist
- generate a pass/block verdict with Conclave via the orchestrator role
- write:
  - `technical-executive-report.md`
  - `executive-brief.md`
  - `daily.md`
  - `conclave.md`
  - `publish.md`
- require artifact publication to already be current for every included article
- mark article status as `published`
- stamp `published_in_daily`
- render the site

This is the actual Collegium/Daily rail.

## 5. Source capture and import reality

There are two distinct intake modes.

### 5.1 Imported runtime backlog
`import_runtime_backlog.py` pulls from canonical OpenClaw custody paths:
- `research/articles/*.md`
- `research/source-material/*.json`
- `research/source-material/*.txt`
- `research/reports/shifts/front-half*.json`
- `research/factory/checkins/article-checkin-latest.json`

It creates local working artifacts:
- `queue/ticket-import-<article>.md`
- `articles/<article_id>/article.md`
- `articles/<article_id>/source.md`

It also records provenance like:
- `imported_from_runtime_article_id`
- `runtime_filter_state`
- `runtime_last_stage`
- refresh-live-source flags

### 5.2 Fresh source capture
`capture_source.py` is used for direct source capture.
Important live rule:
- abstract-only paper capture is blocked
- arXiv `/abs` does not count as valid paper capture
- the system tries HTML/PDF full text paths and falls back carefully

`pdf_markdown_local.py` is substantial and real. It is not a placeholder. It includes:
- arXiv HTML fetch
- arXiv source bundle parsing
- PDF stream extraction fallback
- markdown normalization for downstream LLM use

This confirms the paper full-text rule is operational, not aspirational.

## 6. The current per-article micro lane

`run_micro_article_lane.py` does the following on one article package:

1. Read:
- `article.md`
- `source.md`
- linked ticket

2. Normalize canonical URL.

3. If paper-like and not full-text enough:
- attempt remediation for arXiv full text
- if remediation fails, mark:
  - `publication_status=capture-blocked`
  - `source_capture_gate_reason=abstract-only-paper-source`
  - `source_remediation_required=true`

4. Ask Curator for KEEP/DISCARD.
- writes `micro-worthiness.md`
- on unusable output, falls back to discard

5. If discarded:
- mark article discarded
- mark ticket discarded
- stop

6. Run duplicate gate before proceeding.
- if canonical duplicate conflict found, mark `duplicate-rejected`
- record duplicate-of fields
- stop

7. Run findings extraction.
- writes `micro-findings.md`

8. Run facts extraction.
- writes `micro-facts.md`

9. Run summary synthesis.
- writes `micro-summary.md`

10. Update article metadata:
- `evidence_count`
- `claim_count`
- extraction/synthesis mode fields
- `artifact_minted_at_utc`
- `publication_status=ready-for-daily`

This is the live source-to-artifact rail.

## 7. Real current states and gates

### Article states observed in the live rail
- `pending`
- `capture-blocked`
- `discarded`
- `duplicate-rejected`
- `ready-for-daily`
- `published`

### Additional publication fields
Artifact publication is tracked separately from daily publication:
- `artifact_publication_status`
- `artifact_publication_alias`
- `artifact_publication_minted_at_utc`
- `artifact_publication_published_at_utc`
- `published_in_daily`

This is a crucial live truth: an article can be ready for daily, have its artifact published, and only later be included in the Daily briefing.

## 8. Real publication policy encoded in scripts

The live system enforces this publication rule:
- AM stops after `8` inclusions for the day
- kept artifact pages publish incrementally throughout the day via the artifact poller
- PM publishes only the Daily briefing surfaces
- Daily publication requires every included article’s artifact surface to already be published

So the institute is already split in practice into:
- artifact publication rail
- daily synthesis/publication rail

That separation should be preserved.

## 9. Live persona/job contracts

Micro personas are simple and sharp:
- `curator.md`
- `extractor.md`
- `synthesist.md`
- `conclave.md`

Micro jobs are also very compact:
- `curator-worthiness.md`
- `findings.md`
- `facts.md`
- `article-summary.md`
- `daily-cluster.md`
- `daily-technical.md`
- `daily-executive.md`
- `conclave-gate.md`

The system therefore relies on:
- plain-text contracts
- regex parsing of KEEP/DISCARD and PASS/BLOCK
- a filesystem state machine around markdown bundles

This is lightweight and works, but it is brittle and under-specified for longform institutional law.

## 10. The main remaining OpenClaw seam

The direct live-file inspection confirms the migration boundary stated in `ACTIVE-SYSTEM-STATE.md`.

The main OpenClaw-specific seam is:
- `parallel-sapho/scripts/openclaw_pocket_agent.py`

This file:
- provisions disposable OpenClaw agents in `/tmp`
- seeds them from live OpenClaw agent configs
- boots tiny workspace files for the assignment
- calls `openclaw agent --local`
- sanitizes output
- tears down the worker

`micro_common.py` calls `run_pocket_agent()` through `run_loose_agent()`.

This means the cleanest replacement seam really is the micro execution adapter.
The scheduler itself is not the problem.
The daily/publication chain is not the problem.
The pocket-agent substrate is the problem.

## 11. Truth surfaces actually in use

Live truth surfaces from the real files:
- runtime check-in:
  - `research/factory/checkins/article-checkin-latest.json`
- receipts:
  - `parallel-sapho/state/receipts/research-am-ingest-shift-latest.json`
  - `parallel-sapho/state/receipts/research-artifact-publish-poller-latest.json`
  - `parallel-sapho/state/receipts/research-pm-live-synthesis-shift-latest.json`
- public site:
  - `website/kept-links.html`
  - `website/rss.xml`
  - `website/artifacts.xml`
  - `website/daily/latest.html`
  - `website/briefs/latest/meta.json`

Heartbeat is explicitly not part of the active rail, but remains an observation/reporting surface.

## 12. One real article package example

The real article package for `art-2026-03-04-034` confirms the live shape.

Internal package includes:
- `article.md`
- `source.md`
- `micro-worthiness.md`
- `micro-findings.md`
- `micro-facts.md`
- `micro-summary.md`

The final `article.md` carries both:
- public-facing artifact prose
- workflow/publication metadata

This is efficient, but it still compresses the internal lineage too aggressively compared with full charter ambitions.
There are findings and facts, but not yet explicit canonical claim objects, evidence objects, contradiction objects, or mechanism objects.

## 13. Diagnosis from direct live inspection

What is genuinely working now:
- source capture and remediation for paper-like sources
- imported backlog ordering from runtime truth surfaces
- bounded per-article micro conversion
- duplicate gate before keep enters the rail
- incremental kept artifact publication
- PM daily synthesis gated by Conclave
- receipt-driven operational truth

What is structurally weak:
- execution depends on disposable OpenClaw workers
- persona/job contracts are too loose for institutional law
- article package internal lineage is too compressed
- Conclave is still prompt-shaped instead of contract-first
- longform/Canon is not implemented as a real operating rail

## 14. Consequence for the rewrite plan

The live system should be treated as a successful daily operating core with one major dependency seam and several epistemic limitations.

Therefore the correct rewrite path is:
1. preserve the live job topology and publication split
2. replace `openclaw_pocket_agent.py`
3. keep the current source/article/daily filesystem state machine at first
4. enrich article packages into proper evidence bundles
5. make Conclave deterministic and contract-first
6. add dossiers and Canon on top of the strengthened daily substrate

## 15. Bottom line

The real live system is better than a prototype but narrower than the charter.

It is already an operational Daily rail with:
- intake
- artifact conversion
- artifact publication
- PM synthesis
- gating
- deploy

The shortest path to institute takeover is not a total rebuild.
It is a controlled refactor around the one remaining OpenClaw seam, followed by evidence-package hardening and then Canon construction.
