# Queue Artifact — art-2026-03-04-032

Source URL: https://arxiv.org/abs/2512.10398  
Canonical URL: https://arxiv.org/abs/2512.10398  
Lane: agent-factory  
Decision: retain

## Thesis

Scaling coding agents to production repositories depends heavily on scaffold design (context architecture, memory, tool extensions), not only on base-model size.

## Mechanism summary

The paper introduces Confucius Code Agent (CCA) and its SDK around AX/UX/DX design axes: hierarchical context management for long-horizon reasoning, persistent note-taking for cross-session learning, modular extensions for tool control, and a meta-agent build-test-improve loop. Reported benchmark results suggest strong SWE-Bench-Pro performance under controlled tool/model settings. The mechanism is structured scaffolding: explicit orchestration and memory primitives improve reliability on large, real-world codebases.

## Confidence

Medium-high. Primary source with concrete architecture and benchmark claims; independent replication of full stack behavior remains important.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Scaffold-centric agent architecture can materially lift real-repo issue-resolution performance under controlled backend/tool parity. | Reported **Resolve@1 = 59% on SWE-Bench-Pro** under identical repositories, model backends, and tool access. | Confucius Code Agent (CCA) evaluated with Confucius SDK + meta-agent build-test-improve loop on SWE-Bench-Pro. | Resolve@1 issue-resolution success on production-style software engineering benchmark. | Benchmark-era comparison and implementation stack are platform-specific; independent replication and cross-stack validation remain necessary. |

## Why it matters for Sapho

High relevance to factory reliability work: confirms that orchestrator/memory/tooling contracts are first-order levers for production performance, aligning with Sapho’s contract-first pipeline doctrine.
