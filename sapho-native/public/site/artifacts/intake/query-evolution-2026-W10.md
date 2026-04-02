
# Query Evolution Report — 2026-W10 (refined 2026-03-02)

Generated: 2026-03-02T09:35:00Z

Yesterday’s intake quality showed that broad, generic discovery terms underperformed and drifted away from the two active lanes. The lane update retires weak generic terms and upgrades to query terms that bias toward empirical coding-agent evidence, software-factory mechanism write-ups, and production reliability patterns.

## Retired (weak yield / drift-prone)
- agentic software factory
- LLM agent memory architecture
- harness engineering agents
- tool-using agents benchmark
- autonomous coding loops reliability

## Added (lane-aligned)
- AGENTS.md repository context files coding agents empirical study
- context engineering AI agents open-source software workflows
- self-hosted personal AI agent operational architecture
- software factory AI coding agents production workflow
- harness engineering coding agents CI gates
- failed agentic pull requests empirical study github
- multi-agent coding system architecture reliability evaluation

## Config changes applied
- Updated `research/firehose/config.seed.yaml` query list to the seven lane-aligned queries above.
- Updated `recency_filter` from `week` to `month` to reduce starvation while still preserving freshness.

## Next evolution move
After one additional full-cycle run, compute per-query keep-rate and median novelty score from the 2026-03-02 ledgers and retire any new query that remains below a 0.20 keep-rate threshold.
