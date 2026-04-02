# Queue Artifact — art-2026-03-07-040

Source URL: https://datadome.co/engineering/how-datadome-automated-post-mortem-creation-with-domescribe-ai-agent/  
Canonical URL: https://datadome.co/engineering/how-datadome-automated-post-mortem-creation-with-domescribe-ai-agent/  
Lane: operations-reliability  
Decision: retain

## Thesis

Incident-postmortem drafting can be reliably automated as an SRE-assist workflow when teams constrain extraction scope, enforce structured prompts, and keep human engineers on analysis-critical sections.

## Mechanism summary

DataDome describes a productionized Slack-to-Notion agent (“DomeScribe”) deployed on EKS with Bedrock-backed LLM inference. The pipeline selects relevant incident threads, normalizes Slack-specific tokens/mentions, applies a constrained postmortem prompt, and writes a draft to Notion. Human responders retain final judgment while automation removes timeline and formatting overhead.

## Empirical findings (snapshot)

- Build/deploy lead time: production-ready implementation reported in under 2 days.
- Cost profile: Bedrock pay-per-token usage reported as only a few cents per postmortem volume regime.
- Model selection: Llama 3.1 405B chosen after comparative testing for consistency/complexity handling vs cost.
- Failure mode discovered: unconstrained prompts produced hallucinations when business context was implicit; constrained section prompts improved output usefulness.
- Operational boundary: strongest value in drafting summary/impact/timeline; humans remain necessary for deeper causal interpretation.

## Confidence

Medium-high. First-party engineering write-up with concrete architecture and bounded numerics, but without externally audited benchmark datasets.

## Why it matters for Sapho

Supports Sapho’s fail-closed publication doctrine: agent automation should prioritize structured extraction and draft acceleration while preserving human-controlled, evidence-checked synthesis at decision boundaries.
