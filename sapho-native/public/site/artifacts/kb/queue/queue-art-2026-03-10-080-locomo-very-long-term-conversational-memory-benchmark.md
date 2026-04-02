# Queue Artifact — art-2026-03-10-080

Source URL: https://snap-research.github.io/locomo/  
Canonical URL: https://arxiv.org/abs/2402.17753  
Lane: agent-memory  
Decision: retain

## Thesis

LoCoMo is a primary benchmark for very long-horizon conversational memory, exposing persistent recall and temporal-causal reasoning gaps in current LLM agents.

## Mechanism summary

The work introduces a machine-human data-generation pipeline that grounds two simulated agents in personas plus temporal event graphs, then produces and human-edits long conversations. It evaluates memory competence through three tasks: question answering, event-graph summarization, and multimodal dialogue generation.

## Why it matters for Sapho

This gives the Agent Memory Systems lane a citation-grade benchmark for stress-testing memory modules beyond short context windows, especially around temporal consistency and long-range causal recall.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions. | 300, 35 | Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions. | Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions. | — |

## Confidence

High (primary arXiv benchmark + project page with explicit dataset/task/result claims).
