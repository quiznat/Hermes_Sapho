# Queue Artifact — art-2026-03-13-009

Source URL: https://openreview.net/forum?id=41xrZ3uGuI  
Canonical URL: https://openreview.net/forum?id=41xrZ3uGuI  
Lane: agent-factory  
Decision: retain

## Thesis

Current agentic coding performance is substantially lower on end-to-end feature development than prior bug-fix-centric benchmarks suggest, indicating a major capability gap for production software-factory workflows.

## Mechanism summary

The paper introduces FeatureBench, an execution-based benchmark for feature-oriented software development tasks spanning multiple commits/PRs. It uses a scalable test-driven task-construction method over dependency graphs and curates 200 tasks with 3,825 executable environments from 24 repositories. Reported evaluation shows a large drop from SWE-bench-era headline performance (e.g., model-level 74.4% on SWE-bench vs 11.0% resolved on FeatureBench), highlighting the challenge of multi-step feature development.

## Why retain

This is a primary empirical benchmark artifact directly aligned with queue priorities (agentic software development reliability, executable evaluation protocol, quantified outcomes, and benchmark-level evidence quality).

## Confidence

High.
