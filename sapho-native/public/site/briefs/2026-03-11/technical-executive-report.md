# Technical Executive Report

Date: `2026-03-11`
Run ID: `pm-live-20260311T000251Z`

## Narrative
The six findings are directionally consistent around governance and continuity limits. LoCoMo shows persistent long-horizon recall and temporal-causal reasoning gaps that can degrade multi-step software continuity. Large-scale PR evidence indicates a local-global split: stronger commit-level semantic coherence can coexist with weaker PR-level alignment and faster short-horizon churn. Security-relevant agent PRs contribute value but pass through a stricter acceptance funnel with longer latency. Additional PR studies show non-merge outcomes are largely socio-technical (task type, scope, CI behavior, reviewer dynamics) and are materially confounded by submitter/process attributes, limiting naive capability inference from merge rates alone. OpenDev contributes a high-detail harness design for long-horizon reliability, but as architectural guidance it should be treated separately from empirical causal outcome claims.

## Evidence Rows
- `art-2026-03-10-080`: LoCoMo is a primary benchmark for very long-horizon conversational memory, exposing persistent recall and temporal-causal reasoning gaps in current LLM agents.
  - Mechanism: The benchmark uses grounded personas plus temporal event graphs to produce long conversations, then evaluates memory competence via question answering, event-graph summarization, and multimodal dialogue generation, revealing long-horizon degradation.
  - Artifact: research/kb/queue/queue-art-2026-03-10-080-locomo-very-long-term-conversational-memory-benchmark.md
  - Source: https://snap-research.github.io/locomo/
- `art-2026-03-10-077`: Agentic pull requests demonstrate strong local-level commit communication but weaker PR-level alignment and higher short-horizon code churn compared with human pull requests.
  - Mechanism: Across 33,596 agent PRs and 6,618 human PRs, the study reports stronger commit-message similarity but weaker PR-level summarization alignment, along with faster symbol removal and higher symbol churn for agent changes.
  - Artifact: research/kb/queue/queue-art-2026-03-10-077-change-characteristics-description-alignment.md
  - Source: https://arxiv.org/html/2601.17627v1
- `art-2026-03-10-069`: Agent-authored pull requests make meaningful security contributions in real repositories, but those contributions face stricter human scrutiny, lower merge rates, and longer review latency than non-security agentic PRs.
  - Mechanism: Large-scale AIDev analysis with manual validation of 1,293 security-related PRs shows security lanes are governed by tighter acceptance and longer review pathways than non-security lanes.
  - Artifact: research/kb/queue/queue-art-2026-03-10-069-security-age-of-ai-teammates-agentic-prs.md
  - Source: https://arxiv.org/abs/2601.00477
- `art-2026-03-10-065`: Agent-authored pull requests fail for systematic socio-technical reasons, not just code quality issues.
  - Mechanism: Empirical analysis of 33k agent PRs plus qualitative coding of 600 failures links merged versus non-merged outcomes to task class, change scope, CI results, and review interaction dynamics.
  - Artifact: research/kb/queue/queue-art-2026-03-10-065-where-ai-coding-agents-fail-failed-agentic-prs.md
  - Source: https://arxiv.org/abs/2601.15195v1
- `art-2026-03-10-061`: Pull-request merge success in mixed human/agentic software workflows is strongly driven by submitter attributes, while review dynamics affect human and agentic PRs differently.
  - Mechanism: Regression over 40,214 PRs with 64 engineered features shows author/process variables materially influence merge outcomes and modulate review effects by submitter type.
  - Artifact: research/kb/queue/queue-art-2026-03-10-061-meaningful-prs-human-vs-agentic-analysis.md
  - Source: https://www.arxiv.org/pdf/2601.18749
- `art-2026-03-10-034`: Terminal-native coding agents need explicit harness architecture (scaffolding, runtime orchestration, context compaction, safety layers, and memory persistence) to stay reliable over long-horizon development tasks.
  - Mechanism: OpenDev specifies a compound system with specialized routing, planning/execution separation, event-driven reminders, adaptive context compaction, and defense-in-depth execution controls; this functions as architectural prescription rather than direct large-sample causal validation.
  - Artifact: research/kb/queue/queue-art-2026-03-10-034-opendev-terminal-agent-harness-architecture.md
  - Source: https://arxiv.org/html/2603.05344v1

## Gate Telemetry
```json
{
  "status": "PASS",
  "topLineClaims": 6,
  "traceableClaims": 6,
  "traceabilityCoverage": 1.0,
  "unsupportedClaims": 0,
  "citationFailures": 0,
  "conflictCandidates": 7,
  "contradictionChecks": 7,
  "disagreementsFound": 0,
  "traceabilityRows": [
    {
      "claimId": "art-2026-03-10-080",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-10-077",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-10-069",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-10-065",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-10-061",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-10-034",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    }
  ],
  "contradictionAudit": [
    {
      "leftId": "art-2026-03-10-080",
      "rightId": "art-2026-03-10-034",
      "label": "unclear",
      "overlapTerms": [
        "long-horizon",
        "memory"
      ]
    },
    {
      "leftId": "art-2026-03-10-077",
      "rightId": "art-2026-03-10-069",
      "label": "unclear",
      "overlapTerms": [
        "agentic",
        "human",
        "prs",
        "pull",
        "requests"
      ]
    },
    {
      "leftId": "art-2026-03-10-077",
      "rightId": "art-2026-03-10-065",
      "label": "unclear",
      "overlapTerms": [
        "code",
        "prs",
        "pull",
        "requests"
      ]
    },
    {
      "leftId": "art-2026-03-10-077",
      "rightId": "art-2026-03-10-061",
      "label": "unclear",
      "overlapTerms": [
        "agentic",
        "human",
        "prs"
      ]
    },
    {
      "leftId": "art-2026-03-10-069",
      "rightId": "art-2026-03-10-065",
      "label": "unclear",
      "overlapTerms": [
        "agent-authored",
        "analysis",
        "prs",
        "pull",
        "requests",
        "review"
      ]
    },
    {
      "leftId": "art-2026-03-10-069",
      "rightId": "art-2026-03-10-061",
      "label": "unclear",
      "overlapTerms": [
        "agentic",
        "human",
        "merge",
        "prs",
        "review",
        "shows"
      ]
    },
    {
      "leftId": "art-2026-03-10-065",
      "rightId": "art-2026-03-10-061",
      "label": "unclear",
      "overlapTerms": [
        "dynamics",
        "outcomes",
        "prs",
        "review"
      ]
    }
  ],
  "evidenceIssues": [
    {
      "index": 5,
      "queueId": "art-2026-03-10-034",
      "issue": "confidence_normalized_to_evidence",
      "agentConfidence": "medium",
      "evidenceConfidence": "high"
    }
  ],
  "fatalEvidenceIssues": [],
  "generatedAtUtc": "2026-03-11T00:06:06Z"
}
```
