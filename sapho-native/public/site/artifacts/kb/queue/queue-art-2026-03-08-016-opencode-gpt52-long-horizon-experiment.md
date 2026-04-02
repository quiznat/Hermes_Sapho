# Queue Artifact — art-2026-03-08-016

Source URL: https://dev.to/maximsaplin/long-horizon-agents-opencode-gpt-52-codex-experiment-1f4h  
Canonical URL: https://dev.to/maximsaplin/long-horizon-agents-opencode-gpt-52-codex-experiment-1f4h  
Lane: agent-factory  
Decision: retain

## Thesis

Long-horizon coding can be cost-effective when an orchestrator/sub-agent topology compresses coordination context while delegating implementation and test loops to parallel sub-sessions.

## Mechanism summary

The author reports a real run using OpenCode with GPT-5.2 Codex where one orchestrator session delegated concrete implementation tasks to 16 sub-agent sessions, then integrated and validated output. This architecture kept the main session context relatively compact while executing ~2M tokens of aggregate work.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Runtime-to-human leverage was substantial | **~4h agent time** with **~30 min human effort** and ~10 user messages | Long-horizon provider refactor task | Human-in-the-loop efficiency | Self-reported measurements |
| Cost envelope was bounded for multi-session run | **$13.86 total** (`$4.13` orchestrator + `$9.73` sub-agents) | GPT-5.2 Codex high/medium/xhigh reasoning mix | End-to-end cost observability | Not directly comparable across model pricing/tokens over time |
| Delivery quality reached functional threshold | **26 files changed**, **5 tests written**, tests green, real LLM interaction path validated after fix loop | LiteLLM provider refactor with tracing UI | Functional completion with verification | Test depth limited (author notes low test count) |

## Confidence

Medium. First-person first-party run telemetry with concrete numbers, but not independently replicated and not benchmark-controlled.

## Why it matters for Sapho

Provides practical evidence for orchestrator/sub-agent execution design and cost/token instrumentation strategy in long-horizon coding loops—useful for factory operations heuristics even as non-rigorous field data.
