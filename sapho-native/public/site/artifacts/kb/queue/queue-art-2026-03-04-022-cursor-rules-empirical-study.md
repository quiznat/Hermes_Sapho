# Queue Artifact — art-2026-03-04-022

Source URL: https://arxiv.org/abs/2512.18925  
Canonical URL: https://arxiv.org/abs/2512.18925  
Lane: agent-research  
Decision: retain

## Thesis

Prompt quality is not enough for reliable coding-agent performance; persistent project-level rule files ("Cursor rules") are emerging as a practical control layer, and their structure can be systematically characterized.

## Mechanism summary

The paper studies 401 open-source repositories that include Cursor rules and derives a five-theme taxonomy of developer-authored context: conventions, guidelines, project information, LLM directives, and examples. The core mechanism is context externalization: teams encode architecture norms, collaboration constraints, and behavior expectations into durable machine-readable rules so assistant behavior is shaped by project reality rather than one-off prompts. Variation across project types and languages suggests these rule systems should be adaptive rather than one-size-fits-all.

## Confidence

High for the directional conclusion that persistent contextual directives are now a meaningful software-engineering practice; medium for transferability across all repositories, teams, and tools beyond the sampled set.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Cursor rule files are a structured, recurring repository-level control layer rather than ad-hoc prompt fragments. | **401 repositories** analyzed; **5-theme taxonomy** identified (conventions, guidelines, project info, LLM directives, examples). | Empirical analysis of open-source repositories containing Cursor rules. | Taxonomic prevalence and pattern characterization of persistent context directives. | `qualitative_only` for performance impact: study characterizes structure/usage patterns, not direct task-success deltas or causal productivity gains. |

## Why it matters for Sapho

This reinforces Sapho Chapterhouse Institute doctrine: production-grade agent systems need explicit, persistent context contracts and governance primitives (not just prompt tuning), with clear separation between policy, project constraints, and executable examples.
