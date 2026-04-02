# Queue Artifact — art-2026-03-06-021

Source URL: https://arxiv.org/html/2509.14745v1  
Canonical URL: https://arxiv.org/abs/2509.14745  
Lane: agent-factory  
Decision: retain

## Thesis

Agentic coding PRs are broadly mergeable in real repositories, but they underperform human PRs on acceptance rate and still require meaningful human revision pressure, especially on bug-fix correctness, documentation quality, and project-standard alignment.

## Mechanism summary

The paper analyzes 567 Claude Code-authored PRs across 157 open-source projects and compares them with human PR behavior across purpose, acceptance/rejection, revision burden, and edit taxonomy. The mechanism is that agents are strong at scoped non-functional contributions (tests, refactoring, docs), while project-context constraints and integration expectations drive rejection/rework more than raw syntax generation ability.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Dataset | 567 agentic PRs (Claude Code) across 157 projects. | — | — | — |
| Most common revision categories for accepted agentic PRs include bug-fix corrections (~45.1%), documentation updates (~27.4%), refactoring (~25.7%), and style conformance (~22.1%). | — | — | — | — |

## Confidence

High. Primary empirical study with explicit sample, comparative statistics, and revision taxonomy.

## Why it matters for Sapho

Directly supports Sapho’s harness doctrine: keep agent tasks scoped, enforce merge/CI gates, and treat human review + revision loops as a designed system component rather than an exceptional fallback.
