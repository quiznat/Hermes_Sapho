# Queue Artifact — art-2026-03-04-029

Source URL: https://arxiv.org/abs/2511.09268  
Canonical URL: https://arxiv.org/abs/2511.09268  
Lane: agent-factory  
Decision: retain

## Thesis

AI coding-agent outcomes are heavily shaped by configuration artifacts, and those artifacts encode a broad, non-trivial set of engineering constraints that function like an operational control plane.

## Mechanism summary

This paper studies 328 configuration files from public Claude Code projects and analyzes both the concerns they specify and the way those concerns co-occur. The core empirical takeaway is that high-performing agent setups are not just prompt tweaks; they are structured bundles of architecture directives, coding practices, and tool-usage policy. The strongest repeated pattern is explicit architectural guidance, suggesting that agent reliability and consistency are upstream of model choice and downstream of configuration design quality.

## Confidence

Medium-high for practical directional use: the sample is specific to Claude Code projects, but the measured configuration-centric mechanism is likely transferable to broader agentic software factory systems.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Agent behavior consistency depends strongly on explicit configuration-layer constraints, not just model selection. | Analysis covers **328 configuration files** from public Claude Code projects. | Empirical mining of real-world coding-agent configuration artifacts with concern/co-occurrence analysis. | Pattern prevalence and co-occurrence structure across architecture directives, coding practices, and tool-policy rules. | Sample is ecosystem-specific (Claude Code repos); transferability beyond this population is plausible but not guaranteed without cross-tool replication. |

## Why it matters for Sapho

This reinforces Sapho Chapterhouse Institute doctrine that execution quality should be contract-driven: configuration files are first-class governance objects, so queue processing and synthesis reliability should continue emphasizing explicit architecture constraints, tool-policy declarations, and auditable lane-tagged output contracts.
