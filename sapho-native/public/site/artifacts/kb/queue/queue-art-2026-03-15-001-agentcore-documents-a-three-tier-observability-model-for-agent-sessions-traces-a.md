# Queue Item Processing — art-2026-03-15-001

## Source metadata
- URL: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-15T00:52:01Z
- Finalized at (UTC): 2026-03-15T01:53:32Z

## Source custody
- Qualified signal ID: `QS-art-2026-03-15-001-curator-extractor-20260315T005117Z`
- Shared evidence entry ID: `SE-art-2026-03-15-001-curator-extractor-20260315T005117Z`
- Source snapshot: `research/evidence/source-material/2026-03-15/art-2026-03-15-001.json`
- Clean text path: `research/evidence/source-material/2026-03-15/art-2026-03-15-001.txt`

## Core thesis
The document defines agent observability in AgentCore as a hierarchical system in which sessions capture full user interaction contexts, traces capture individual request-response cycles, and spans capture fine-grained operations within those cycles.

## Mechanism summary
Sessions provide conversation-level state, context persistence, and runtime metrics; traces provide per-invocation execution detail including tool calls, timestamps, errors, and resource use; spans provide operation-level timing, parent-child structure, status, and events. Default observability is uneven across resources, with some metrics and memory-resource spans available out of the box, while deeper agent and gateway span/trace capture requires ADOT-based instrumentation.

## Why it matters for Sapho
This matters because it gives a first-party production framing for how agent telemetry should be organized when operators need to debug behavior across conversation state, request execution, and low-level operations. The hierarchy clarifies that useful observability is not a single log stream but a layered model with different scopes of accountability, while the instrumentation boundary makes clear that default platform telemetry is incomplete unless teams add their own tracing for deeper agent and gateway visibility. As a result, the document is significant less as performance evidence than as an architecture reference for building inspectable, supportable agent systems on Bedrock.

## Confidence
high

Justification: The rating is high because the source is first-party vendor documentation and is directly reliable for the platform’s stated observability model, default telemetry surface, and instrumentation requirements. The main caveat is that the page is descriptive and architectural rather than empirical, so confidence applies to intended system design and terminology, not to measured operational outcomes.
