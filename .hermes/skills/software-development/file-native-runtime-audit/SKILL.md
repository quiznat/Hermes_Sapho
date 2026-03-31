---
name: file-native-runtime-audit
description: Audit a file-native autonomous system/runtime before redesigning it. Use for live rails driven by scripts, receipts, cron jobs, markdown bundles, and public surfaces.
version: 1.0.0
author: Hermes Agent
---

# File-Native Runtime Audit

Use when a user wants a full plan before coding, especially for systems that:
- run from cron/systemd wrappers
- persist state in files/markdown rather than a DB
- have multiple rails (ingest, publish, synthesis, etc.)
- mix live workspace paths with older snapshots or legacy paths

## Goal

Produce an implementation-quality map of the real live system:
- what is actually running
- which scripts are wrappers vs core logic
- what the canonical state objects are
- where the clean replacement seam is
- what to preserve vs replace

## Core rule

Do not trust snapshots or inferred structure when the live workspace might be readable. Verify direct access first.

## Steps

1. Verify access to the real workspace
- Try reading the exact live files the user points to.
- If reads fail, check parent-directory traversal/ACL issues, not just file existence.
- If blocked, tell the user exactly which parent dirs still need traverse/read access.
- Treat snapshot/tmp copies as provisional only.

2. Read identity and operating-law files first
Typical high-value docs:
- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `HEARTBEAT.md`
- `ACTIVE-SYSTEM-STATE.md`

Extract from them:
- operator posture
- active rail declarations
- retired paths not to revive
- runtime schedule
- explicit migration boundary

3. Map wrapper jobs before diving into internals
Find the actual live chain, e.g.:
- runtime wrapper -> micro shift
- artifact wrapper -> artifact watch -> artifact publish
- PM wrapper -> PM publish -> daily synthesis

Important: distinguish wrappers/receipts from the scripts that do the real work.

4. Inspect the core scripts in execution order
Prioritize:
- intake/import script
- per-item/article processing script
- publication poller
- daily synthesis script
- render/deploy scripts
- execution substrate/agent adapter
- shared helpers (`common.py`, runtime helpers)

Document for each:
- inputs
- outputs
- state transitions
- hard gates
- environment assumptions

5. Inspect real truth surfaces and receipts
Read actual latest files such as:
- `state/receipts/*-latest.json`
- runtime check-ins
- shift/front-half reports
- public meta surfaces

Use them to verify:
- the scheduler contract
- latest successful run shape
- operational counts/caps
- what is considered canonical truth today

6. Inspect one gold-path package and one edge-case package
At minimum, read:
- one successfully published article/item bundle
- its source capture file
- stage outputs (`micro-findings`, `micro-facts`, etc.)
- one blocked/discarded/remediation case if available

This reveals the true package schema better than helper code alone.

7. Identify the narrowest replacement seam
Look for the smallest layer that can be swapped first without changing business logic.
Common example:
- a disposable-agent execution adapter under otherwise-good pipeline scripts

Prefer replacing:
- execution substrate
before replacing:
- scheduler
- state model
- publication flow

8. Write permanent docs before coding
Create at least:
- current system map
- roadmap
- operations/architecture blueprint
- full implementation plan

## What to preserve if the live system works
Usually preserve:
- live job topology
- file-native canonical state
- receipt-based ops truth
- separation between incremental artifact publishing and later synthesis publication
- hard gates already encoded in scripts

## Common pitfalls

- Mistaking snapshots for live truth.
- Assuming “file not found” when the real issue is parent directory traversal.
- Rebuilding the scheduler when only the execution substrate is problematic.
- Ignoring incremental publication rails (e.g. artifact poller) because the daily rail gets more attention.
- Treating article/item markdown as the full schema without reading adjacent stage files.
- Letting prompt-only gates stand in for deterministic validation.

## Deliverable shape

A good audit should end with:
1. exact active job chain
2. real canonical objects and statuses
3. actual publication rule(s)
4. primary remaining dependency seam
5. preserve/replace recommendations
6. phased plan that starts with the narrow seam, not a full rewrite

## Example outcome pattern

For a live research-publishing rail, a strong conclusion often looks like:
- preserve the real ingest -> artifact publish -> PM synthesis chain
- replace the disposable agent substrate first
- enrich package lineage next
- add deterministic validators
- build longform/canon rail on dossiers over the hardened daily substrate
