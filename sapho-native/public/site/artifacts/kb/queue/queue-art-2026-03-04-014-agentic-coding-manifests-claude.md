# Queue Artifact — art-2026-03-04-014

Source URL: https://arxiv.org/abs/2509.14744  
Canonical URL: https://arxiv.org/abs/2509.14744  
Lane: agent-factory  
Decision: retain

## Thesis

Agentic coding manifest files (e.g., `CLAUDE.md`) are now analyzable engineering artifacts with recurring structure/content patterns, and their current documentation standards are immature.

## Mechanism summary

This empirical study analyzes 253 `CLAUDE.md` files from 242 repositories (plus commit-history traces) and finds shallow hierarchical structure with dominant instruction categories centered on operational commands, implementation details, and architecture. The mechanism claim is practical: agent behavior quality depends heavily on manifest structure and specificity, yet teams lack comprehensive standards and often learn via trial-and-error.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| View a PDF of the paper titled On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code, by Worawalan Chatlatanagulchai and 7 other authors | 7 | View a PDF of the paper titled On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code, by Worawalan Chatlatanagulchai and 7 other authors | View a PDF of the paper titled On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code, by Worawalan Chatlatanagulchai and 7 other authors | — |
| [2509.14744] On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code | 2509.14744 | [2509.14744] On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code | [2509.14744] On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code | — |

## Confidence

High for directional structural findings and dataset-backed claims; this is a primary empirical source with explicit sampling criteria and methodology.

## Why it matters for Sapho

This gives concrete evidence for Sapho’s manifest-contract lane: enforce consistent structure and explicit instruction categories, then audit evolution over time rather than treating context files as ad-hoc notes.
