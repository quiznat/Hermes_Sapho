# Hermes Setup Repository

This repository tracks the Hermes server setup rooted at `/home/hermes`.

Tracked on purpose:
- Hermes configuration that is safe to version (`.hermes/config.yaml`, skills, hooks, scripts)
- Sapho source, specs, tests, personas, jobs, and implementation docs
- local handoffs and documentation under this workspace
- shell dotfiles and lightweight machine setup files that help reproduce this environment

Handled separately:
- `.hermes/hermes-agent/` is already its own upstream git repository and is left out of this super-repo to avoid nesting conflicts

Ignored on purpose:
- provider credentials and tokens
- private conversation/session history
- caches, logs, checkpoints, audio/image artifacts
- generated Sapho runtime/state/publication outputs

Why this split:
- git should give us a reproducible fallback path for code, prompts, config, skills, and docs
- secrets and volatile runtime state should be backed up separately, not committed into version control

Recommended fallback strategy:
1. push this repo to a remote origin
2. periodically snapshot ignored runtime/state directories to encrypted storage
3. tag known-good milestones before major Hermes or Sapho changes

Important ignored paths for separate backup if needed:
- `/home/hermes/.hermes/auth.json`
- `/home/hermes/.hermes/memories/`
- `/home/hermes/.hermes/sessions/`
- `/home/hermes/sapho-native/state/`
- `/home/hermes/sapho-native/public/`
