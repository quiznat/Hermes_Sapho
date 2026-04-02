# Queue Artifact — art-2026-03-04-030

Source URL: https://arxiv.org/abs/2510.04905  
Canonical URL: https://arxiv.org/abs/2510.04905  
Lane: agent-factory  
Decision: retain

## Thesis

Repository-level code generation should be treated as a retrieval-and-orchestration problem, not a pure generation problem, because practical software work requires cross-file coherence and long-range dependency handling.

## Mechanism summary

This survey frames Retrieval-Augmented Code Generation (RACG) with emphasis on repository-level settings, organizing methods by generation strategy, retrieval modality, architecture, training, and evaluation. The core mechanism is retrieval-grounded context assembly: pull the right repository evidence into generation loops so models can maintain global consistency across modules and files.

## Confidence

Medium-high. This is a survey source (broad synthesis rather than a single controlled benchmark), but it provides a useful taxonomy and unified analytic lens for repo-scale agent design.

## Why it matters for Sapho

It reinforces Sapho’s factory direction toward context pipelines and evidence-grounded generation contracts, especially for multi-file tasks where naive prompt-only generation fails.
