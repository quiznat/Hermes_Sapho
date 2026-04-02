# Queue Artifact — art-2026-03-04-023

Source URL: https://arxiv.org/abs/2310.06770  
Canonical URL: https://arxiv.org/abs/2310.06770  
Lane: agent-research  
Decision: retain

## Thesis

Real-world software issue resolution remains a hard frontier for language models, and benchmarking on synthetic coding tasks materially overestimates practical engineering capability.

## Mechanism summary

SWE-bench frames software-agent evaluation as end-to-end GitHub issue resolution over real repositories, requiring cross-file edits, execution feedback loops, and long-context reasoning. The benchmark’s core mechanism is ecological validity: grounding tasks in real issue/PR pairs reveals failure modes hidden in toy code-generation settings. Initial results show very low solve rates for then-frontier models, highlighting large room for systems-level improvements.

## Confidence

High for benchmark framing and directional findings; this is a primary source introducing the dataset/evaluation protocol.

## Why it matters for Sapho

Critical for factory governance: reinforces that success criteria must track real repository issue closure and verification outcomes, not just snippet quality or one-shot generation metrics.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Real-repository issue resolution remains a steep capability gap for language-model coding agents. | SWE-bench includes **2,294** real GitHub issues across **12** popular Python repositories; the best reported model in the paper evaluation (Claude 2) resolves **1.96%** of issues. | End-to-end benchmark over real issue/PR pairs: model receives repository + issue description and must produce code edits that resolve the issue. | Issue-resolution success rate on SWE-bench. | Reported solve rate is a paper-timepoint baseline (not a permanent ceiling); benchmark outcomes vary by model generation and harness design. |
