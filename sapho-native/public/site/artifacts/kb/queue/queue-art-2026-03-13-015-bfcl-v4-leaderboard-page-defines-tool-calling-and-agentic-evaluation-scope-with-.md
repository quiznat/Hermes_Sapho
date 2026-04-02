# Queue Item Processing — art-2026-03-13-015

## Source metadata
- URL: https://gorilla.cs.berkeley.edu/leaderboard.html
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T04:07:59Z
- Finalized at (UTC): 2026-03-13T20:00:59Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-015.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-015.txt`

## Core thesis
BFCL V4 is positioned as a periodically updated real-world leaderboard for evaluating LLM function and tool-calling accuracy, with an expanded framing from tool use toward holistic agentic evaluation.

## Mechanism summary
The captured page functions as benchmark governance and methodology documentation rather than a result-bearing benchmark snapshot. It specifies version lineage across BFCL releases, metric semantics such as overall accuracy as an unweighted subcategory average plus latency and cost notes, and reproducibility handles including commit pinning at f7cf735 and bfcl-eval==2025.12.17 with checkpoint and PyPI references.

## Why it matters for Sapho
This matters as methodology infrastructure for agent-factory evaluation because it clarifies what BFCL V4 is intended to measure and how runs can be reproduced or audited. Its significance is bounded by the source itself: this snapshot can support benchmark framing, metric interpretation, and protocol traceability, but it cannot by itself support comparative performance claims because no model-level quantitative outcomes are visible in the captured text.

## Confidence
high

Justification: The source is a first-party Berkeley-hosted benchmark surface, so confidence is high for claims about benchmark scope, metric semantics, and reproducibility artifacts. The evidence is strong for methodology and governance content, but the main caveat is that the snapshot contains no extractable model-level results, so confidence does not extend to any comparative performance interpretation.
