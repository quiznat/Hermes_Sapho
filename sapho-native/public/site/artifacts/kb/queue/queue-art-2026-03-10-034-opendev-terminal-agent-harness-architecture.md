# Queue Artifact — art-2026-03-10-034

Source URL: https://arxiv.org/html/2603.05344v1  
Canonical URL: https://arxiv.org/abs/2603.05344  
Lane: agent-memory  
Decision: retain

## Thesis

Terminal-native coding agents need explicit harness architecture (scaffolding, runtime orchestration, context compaction, safety layers, and memory persistence) to stay reliable over long-horizon development tasks.

## Mechanism summary

The OpenDev technical report frames the agent as a compound system with workflow-specialized model routing, dual-agent planning/execution separation, event-driven reminders, adaptive context compaction, and defense-in-depth controls around shell/file/tool execution.

## Why it matters for Sapho

This is direct architecture evidence for reliable autonomous software-factory operation: it gives implementation-level design patterns for lane-safe execution, memory continuity, context budget control, and operational safety gating in terminal-first environments.

## Evidence snapshot

| Finding | Quantitative signal | Context |
|---|---|---|
| Four-level runtime hierarchy | session → agent → workflow → LLM | Explicit system decomposition for controllable model binding and trade-off routing. |
| Defense-in-depth safety framing | 5 safety layers | Safety controls span prompt guardrails, runtime approvals, tool validation, and lifecycle hooks. |
| CLI-agent adoption signal | GitHub Copilot reported at 15M+ developers (paper citation context) | Used by authors to motivate industrial relevance of autonomous coding assistance. |

## Confidence

Medium-high (primary arXiv technical report with concrete architecture details; limited direct benchmark deltas in extracted section).