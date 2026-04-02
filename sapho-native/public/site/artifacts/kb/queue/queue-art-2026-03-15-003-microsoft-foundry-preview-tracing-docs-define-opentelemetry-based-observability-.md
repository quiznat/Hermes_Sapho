# Queue Item Processing — art-2026-03-15-003

## Source metadata
- URL: https://learn.microsoft.com/en-us/azure/ai-foundry/observability/concepts/trace-agent-concept?view=foundry
- Source type: firehose-brave
- Lane tags: `reach-engagement-marketing-lane, reach-engagement-marketing-lane`
- Curated at (UTC): 2026-03-15T00:52:57Z
- Finalized at (UTC): 2026-03-15T01:54:22Z

## Source custody
- Qualified signal ID: `QS-art-2026-03-15-003-curator-extractor-20260315T005117Z`
- Shared evidence entry ID: `SE-art-2026-03-15-003-curator-extractor-20260315T005117Z`
- Source snapshot: `research/evidence/source-material/2026-03-15/art-2026-03-15-003.json`
- Clean text path: `research/evidence/source-material/2026-03-15/art-2026-03-15-003.txt`

## Core thesis
The document presents tracing in Microsoft Foundry as an OpenTelemetry-based observability layer for agent systems, centered on traces, spans, attributes, and exporters, with additional semantic conventions for multi-agent workflows and storage in Azure Application Insights.

## Mechanism summary
The page explains that tracing records inputs, outputs, tool use, retries, latencies, and costs across agent runs, exposing ordered primitive-level execution for debugging. It defines traces and spans using OpenTelemetry concepts, describes Foundry’s use of Azure Application Insights as the trace backend, and lists new multi-agent semantic conventions for task execution, agent interaction, memory/state management, planning, orchestration, tool arguments/results, and evaluation events.

## Why it matters for Sapho
This matters because it shows how a major vendor is translating general observability standards into agent-specific operational practice, especially for multi-agent workflows that need more than conventional application traces. The page is significant as a reference for the emerging control plane of agent systems: not only recording latency and errors, but structuring visibility around planning, tool usage, memory, orchestration, and evaluation events. It also reinforces the broader pattern that vendor agent observability is converging on OpenTelemetry concepts while adding new semantic layers for agent-native behavior.

## Confidence
high

Justification: The rating is high because the source is first-party Microsoft documentation and is directly reliable for the platform’s stated tracing model, storage path, and semantic conventions. The main caveat is that the page is preview documentation rather than an empirical study, so confidence applies to product design and terminology, not to measured performance or validated operational impact.
