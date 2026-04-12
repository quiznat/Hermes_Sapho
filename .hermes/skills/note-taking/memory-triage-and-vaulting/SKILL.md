---
name: memory-triage-and-vaulting
description: Triage Hermes active memory when it gets crowded, move long-form project knowledge into markdown vault files, and keep only compact steering facts in active memory.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [memory, vault, note-taking, pruning, project-notes]
---

# Memory Triage and Vaulting

Use this when Hermes active memory is getting full or when project-operational detail is crowding out durable steering facts.

## Goal

Keep active memory small and high-signal while preserving useful long-form knowledge in durable markdown files.

## Core split

Use three layers:
- Active memory: short steering facts, stable environment facts, hard project posture
- User profile: durable user preferences and recurring corrections
- Vault markdown files: longer project memory, accepted examples, operational notes, deferred ideas

Skills remain the right home for reusable procedures.

## Triage rule

For each current memory entry, classify it as one of:
1. Enduring preference
2. Stable environment fact
3. Strategic project posture
4. Procedural workflow
5. Historical/example note
6. Deferred idea

Keep only 1–3 in active memory or user profile.
Move 4–6 into skills or vault notes.

## Practical workflow

### 1. Inspect current memory and user profile
Read the injected memory/user profile and list all entries plainly for the user if they want review before changes.

### 2. Propose what stays vs moves
A good active-memory set usually includes only:
- user environment posture
- main workspace / repo locations
- top-level strategic project constraints
- live-vs-retired system posture
- a note that long-form notes live in the vault

A good user-profile set usually includes:
- quality bar
- communication/reporting preferences
- git/operational preferences
- recurring architectural corrections

### 3. Create or inspect a vault structure
First check whether a vault/note location already exists. If not, a compact default layout that worked well is:

```text
/home/hermes/vault/hermes/
  README.md
  environment.md
  user-preferences.md
  sapho/
    charter-operating-rules.md
    current-system-state.md
    accepted-artifact-examples.md
    historical-remediation-playbook.md
    deferred-ideas.md
```

Adjust names to fit the project, but keep them human-browsable and topic-oriented.

Important practical step discovered in rollout:
- if you create or update vault files inside a tracked workspace, commit them as their own documentation slice so the storage strategy itself is durable and reviewable

### 4. Write long-form notes
Move detailed content into markdown files, especially:
- workflow details
- accepted reference examples
- historical debugging findings
- reporting conventions
- parked future ideas

Use brief headings and explicit bullets so future retrieval is easy.

### 5. Prune active memory aggressively
Use `memory replace/remove` to compress long entries.
Patterns that worked:
- replace detailed workspace entries with one short path fact
- replace long repo-policy entries with one concise repo location fact
- remove specific operational workflows once captured in vault notes or skills
- remove exemplar references from active memory once they exist in vault notes
- add one compact memory entry pointing to the vault location and rule

### 6. Trim redundant user-profile entries
If two user-profile entries say nearly the same thing, merge them.
Keep the sharper version.

If the user profile is full and a new correction or strong preference arrives:
- replace a lower-priority or redundant entry instead of trying to append blindly
- prioritize corrections about build sequencing, deployment targets, and output expectations over more generic project reminders

## Heuristics for what belongs where

### Keep in active memory
- server/OS posture
- main workspace path
- main repo path
- project identity and top strategic boundary
- active-vs-retired system posture

### Keep in user profile
- charter-first preference
- fail-closed preference
- article quality preference
- reporting preference
- git authorship preference
- tracking/commit preferences

### Move to vault
- exact remediation flows
- accepted artifact examples
- known bug classes
- deferred architecture ideas
- detailed status snapshots

### Move to skills
- repeatable runbooks with commands and verification steps
- debugging patterns
- reporting workflows

## Important lesson

Memory pressure is often caused by procedural/project detail living in active memory.
The fix is not just deleting entries; it is creating a better storage split so detail remains recoverable.

## Success criteria

You are done when:
- active memory contains only compact steering facts
- user profile contains only durable preferences/corrections
- long-form detail exists in markdown vault notes
- there is at least one memory entry pointing to the vault location/rule
- the user can inspect the vault structure and understand where future knowledge should go
