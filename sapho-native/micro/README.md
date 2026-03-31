Micro-step Daily rail rebuild.

Design rules:
- archive the old rail, do not delete it
- keep early stages loose and tolerant
- no deterministic scripted content or judgment generation
- keep frontmatter and canonical ids for the end only
- use fresh agent sessions per item and per stage
- hand off only the minimum context needed for the next step

Layout:
- `micro/jobs/`: small stage prompts
- `scripts/micro_common.py`: shared helpers for the micro rail
- `scripts/run_micro_article_lane.py`: one article through curator, findings, facts, summary, package
- `scripts/run_micro_am_cycle.py`: queue runner for article lanes
- `scripts/run_micro_daily.py`: daily synthesis, conclave, canonical package, render
- `scripts/run_micro_replay_batch.py`: clean-scratch replay runner for proofing
