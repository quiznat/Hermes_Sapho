# Testing and Enhancing Multi-Agent Systems for Robust Code Generation

## Source metadata
- Title: Testing and Enhancing Multi-Agent Systems for Robust Code Generation
- URL: https://arxiv.org/abs/2510.10460
- Source type: Sapho Daily artifact
- Curated at (UTC): 2026-03-30T17:59:36Z
- Finalized at (UTC): 2026-03-30T18:03:06Z

## Core thesis
Multi-agent systems for automated code generation exhibit severe fragility when subjected to semantic-preserving input mutations, with a "planner-coder gap"—where planning agents provide insufficient detail and coding agents misinterpret instructions—emerging as the dominant failure mode. A novel fuzzing-based study reveals these systems are far less robust than previously understood, while demonstrating that targeted repair mechanisms can substantially mitigate these vulnerabilities.

## Why it matters for Sapho
As organizations increasingly deploy multi-agent systems for critical code generation tasks, unacknowledged robustness gaps pose material risks to software reliability and security. Understanding the precise mechanisms of failure—and having validated methods to repair them—enables engineering teams to harden these systems before production deployment rather than discovering fragility through operational incidents.

## Key findings
- Multi-agent code generation systems fail on between 7.9% and 83.3% of previously solved problems after minor semantic-preserving mutations, indicating substantial brittleness under realistic input variation.
- The "planner-coder gap" accounts for 75.3% of all robustness failures, driven by vague specifications from planning agents and subsequent misinterpretation by coding agents.
- A repairing method combining multi-prompt generation with a dedicated monitor agent resolves 40.0%–88.9% of identified failures while reducing new failure introduction by up to 85.7% upon re-execution.

## Limits
These findings derive from an excerpt of an academic research paper; full methodological details, replication protocols, and edge-case analyses may be more extensive in the complete source document.
