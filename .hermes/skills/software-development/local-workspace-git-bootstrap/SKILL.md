---
name: local-workspace-git-bootstrap
description: Initialize a new git repo for an existing local workspace while excluding secrets, runtime state, caches, and nested upstream repos; add a fallback backup script for ignored state.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [git, bootstrap, backup, monorepo, workspace, safety]
---

# Local Workspace Git Bootstrap

Use when a user wants an existing server/workspace put under git for change tracking and rollback, especially when the directory contains secrets, caches, runtime state, or nested git repos.

## Goals

1. Create a safe top-level git repository.
2. Track reproducible source/config/docs.
3. Exclude secrets and volatile state.
4. Detect nested git repos and avoid accidentally embedding them.
5. Add a simple backup path for ignored-but-important state.

## Procedure

### 1. Inspect before initializing

Check the workspace size and top-level contents first.

- Search for files/directories under the target root and important subdirs.
- Inspect likely secret/config files such as:
  - `.env`
  - auth/token JSON files
  - config files under app-specific hidden directories
- Identify runtime/state directories such as:
  - logs
  - caches
  - sessions
  - checkpoints
  - generated outputs
  - databases

Useful heuristics:
- version source, docs, prompts, tests, skills, scripts, safe config
- ignore auth, tokens, private message history, caches, logs, generated artifacts, state DBs

### 2. Detect nested git repos before `git add .`

This is important.

If a subdirectory already has its own `.git`, do not blindly stage it from the parent repo. Instead either:
- ignore it in the parent repo, or
- intentionally convert it to a submodule if the user wants that

Practical check:
- run `git status` inside suspicious subdirs
- inspect remotes with `git remote -v`
- if the nested repo is independently tracked upstream, usually add it to the parent `.gitignore`

Why:
- otherwise git warns about an embedded repository
- clones of the outer repo will not include the nested repo content as expected

### 3. Create a defensive `.gitignore`

Include categories like:
- secrets/auth
- shell history and machine-local noise
- app runtime state/private history
- caches/package artifacts
- test caches
- generated app outputs
- temp files
- nested upstream repos

Example patterns that often matter:
- auth/token files
- `.env*`
- session/history directories
- checkpoint/log/cache/image/audio dirs
- sqlite/db WAL/SHM files
- generated `state/`, `public/`, `articles/`, `runtime/`-style dirs
- nested source trees already managed elsewhere

### 4. Add a README that explains the split

Document:
- what is intentionally tracked
- what is intentionally ignored
- why ignored data must be backed up separately
- which nested repos are excluded and why

### 5. Initialize and stage carefully

Steps:
1. `git init -b main`
2. inspect `git status`
3. dry-run with `git add -n .` before full staging
4. if git warns about embedded repos, stop and fix `.gitignore`
5. only then run `git add .`

### 6. Commit identity fallback

If commit fails because `user.name` / `user.email` are unset, prefer repo-local config rather than global unless the user requested global setup.

Example approach:
- `git config user.name "Hermes Agent"`
- `git config user.email "hermes@local"`

Then retry the commit.

If the user later gives their preferred authorship after bootstrap, update the repo-local identity and rewrite the bootstrap commits so the visible history matches the requested author.

Practical approach for a small fresh repo:
- `git config user.name "<User Name>"`
- `git config user.email "<user@example.com>"`
- amend the latest commit with `git commit --amend --reset-author --no-edit`
- if earlier bootstrap commits already used placeholder authorship, rewrite the small local history with an env-filter so both author and committer become the requested identity

Only do history rewriting before the repo is shared/pushed, or warn if force-push would be required.

### 7. Add a backup script for ignored state

If the repo intentionally excludes critical runtime state, add a simple script such as `scripts/backup-<name>-state.sh` that archives ignored-but-important paths to a timestamped tarball.

Typical backup candidates:
- auth files
- memory/session history
- state databases
- generated publication/runtime directories

Document the script in the README and recommend off-machine encrypted backup copies.

## Pitfalls

- Do not commit auth/token files just because they live near config.
- Do not commit private user/channel/session data by accident.
- Do not embed an existing upstream repo unless the user explicitly wants a submodule.
- Do not assume generated runtime directories belong in version control just because they are business-critical; usually they belong in backups instead.
- Avoid changing global git identity unless requested.

## Verification

After setup, verify:
- `git status --short --branch` is clean after commit
- `git log --oneline --decorate -3` shows the bootstrap commits
- ignored secrets/state remain untracked
- nested repo warnings no longer appear in `git add -n .`
- backup script exists and is executable

## Good outcome pattern

A successful bootstrap usually ends with:
- one new top-level repo
- a documented `.gitignore`
- initial commit(s)
- backup script for ignored state
- clear note about excluded nested repos and next step to add/push remote

## Remote setup notes

- It is safe to add `origin` before credentials are ready.
- A first HTTPS push may fail simply because no GitHub credential helper/PAT is configured yet; that is a credential issue, not a repo bootstrap failure.
- If push fails with username/password or PAT errors, leave the local repo intact, confirm `git remote -v`, and resume once the PAT or auth helper is available.
