# Queue Artifact — art-2026-03-10-004

Source URL: https://arxiv.org/html/2512.18470v1  
Canonical URL: https://arxiv.org/abs/2512.18470  
Lane: agent-factory  
Decision: retain

## Thesis

Current coding agents that look strong on single-issue benchmarks break down on long-horizon software evolution tasks that require sustained multi-file planning, modification, and verification.

## Mechanism summary

SWE-EVO is constructed from release notes and version histories of seven mature open-source Python repositories, then evaluates agents on 48 evolution tasks that require coordinated multi-step repository changes validated by large test suites.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Constructed from release notes and version histories of seven mature open-source Python projects, SWE-EVO comprises 48 evolution tasks that require agents to implement multi-step modifications spanning an average of 21 files, validated against comprehensive test suites averaging 874 tests per instance. | 21, 48, 5, 65, 874 | Constructed from release notes and version histories of seven mature open-source Python projects, SWE-EVO comprises 48 evolution tasks that require agents to implement multi-step modifications spanning an average of 21 files, validated against comprehensive test suites averaging 874 tests per instance. | Constructed from release notes and version histories of seven mature open-source Python projects, SWE-EVO comprises 48 evolution tasks that require agents to implement multi-step modifications spanning an average of 21 files, validated against comprehensive test suites averaging 874 tests per instance. | Experiments with state-of-the-art models reveal a striking capability gap: even GPT-5 with OpenHands achieves only a 21 percent resolution rate on SWE-EVO, compared to 65 percent on the single-issue SWE-Bench Verified. |

## Why it matters for Sapho

This is direct benchmark evidence that software-factory claims should be stress-tested on long-horizon evolution tasks, not only on issue-level benchmarks. It supports stricter evaluation policy in Lane 1: prioritize repository-evolution benchmarks for readiness claims and treat single-issue scores as necessary but insufficient.

## Confidence

High.
