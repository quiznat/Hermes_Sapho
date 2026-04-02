# Technical Executive Report

Date: `2026-03-12`
Run ID: `pm-live-20260312T233011Z`

## Narrative
The six-source set is directionally consistent around conditional deployment. ReliabilityBench reframes readiness as a multi-axis surface rather than a single success rate, showing why repeated-run consistency, perturbation robustness, and fault tolerance must be jointly tested. Framework-comparison evidence shows no globally dominant stack across code-centric tasks, while composition evidence shows specialist collaboration plus runtime debugging can help or hurt depending on model-family interaction effects. LoCoMo adds a persistent continuity constraint: long-horizon recall and temporal-causal reasoning gaps remain unresolved and can propagate into planning drift and handoff inconsistency. PR-scale evidence indicates local code-communication strength can coexist with weaker PR-level alignment and elevated churn, increasing integration burden; security-focused agent PRs contribute value but move through stricter review pathways with lower merge rates and longer latency.

## Evidence Rows
- `art-2026-03-12-004`: Single-run success rates materially overstate production readiness for tool-using LLM agents; reliability under repeated runs, semantic perturbation, and tool/API faults needs direct stress testing before deployment decisions.
  - Mechanism: ReliabilityBench defines a joint reliability surface over repeat consistency, perturbation robustness, and injected tool/API fault tolerance, and evaluates ReAct/Reflexion across operational domains to expose failures that single-pass metrics miss.
  - Artifact: research/kb/queue/queue-art-2026-03-12-004-reliabilitybench-production-stress-llm-agents.md
  - Source: https://arxiv.org/html/2601.06112v1
- `art-2026-03-11-020`: Agent-framework performance on code-centric software engineering is currently moderate and highly trade-off-driven; framework selection materially affects effectiveness, efficiency, and cost outcomes by task type.
  - Mechanism: Comparative evaluation of seven agent frameworks across software development, vulnerability detection, and program repair shows task-dependent shifts in correctness, runtime efficiency, and token/cost overhead.
  - Artifact: research/kb/queue/queue-art-2026-03-11-020-agent-frameworks-code-centric-se-eval.md
  - Source: https://arxiv.org/html/2511.00872v1
- `art-2026-03-11-017`: Combining multi-agent collaboration with runtime-execution debugging measurably changes code-generation performance, and model response to this composition is heterogeneous enough to matter for system design decisions.
  - Mechanism: A chained analyst/coder/tester-style decomposition followed by runtime-feedback debugging is benchmarked against standalone strategies, showing model-dependent net effects rather than uniform uplift.
  - Artifact: research/kb/queue/queue-art-2026-03-11-017-multi-agent-runtime-debugging-codegen-eval.md
  - Source: https://arxiv.org/html/2505.02133v1
- `art-2026-03-10-080`: LoCoMo is a primary benchmark for very long-horizon conversational memory, exposing persistent recall and temporal-causal reasoning gaps in current LLM agents.
  - Mechanism: Grounded long-conversation generation with persona and temporal event-graph structure is evaluated via QA, event-graph summarization, and multimodal dialogue generation, revealing durable long-horizon memory weaknesses.
  - Artifact: research/kb/queue/queue-art-2026-03-10-080-locomo-very-long-term-conversational-memory-benchmark.md
  - Source: https://snap-research.github.io/locomo/
- `art-2026-03-10-077`: Agentic pull requests demonstrate strong local-level commit communication but weaker PR-level alignment and higher short-horizon code churn compared with human pull requests.
  - Mechanism: At large scale, agent PRs show higher commit-level semantic similarity but weaker PR-summary alignment, faster symbol removal, and higher short-horizon churn, indicating local coherence does not guarantee stable integration intent.
  - Artifact: research/kb/queue/queue-art-2026-03-10-077-change-characteristics-description-alignment.md
  - Source: https://arxiv.org/html/2601.17627v1
- `art-2026-03-10-069`: Agent-authored pull requests make meaningful security contributions in real repositories, but those contributions face stricter human scrutiny, lower merge rates, and longer review latency than non-security agentic PRs.
  - Mechanism: Large-scale AIDev analysis with manual validation of security-related PRs shows governance and review burden are stronger constraints in security lanes than in non-security agent PR lanes.
  - Artifact: research/kb/queue/queue-art-2026-03-10-069-security-age-of-ai-teammates-agentic-prs.md
  - Source: https://arxiv.org/abs/2601.00477

## Gate Telemetry
```json
{
  "status": "PASS",
  "topLineClaims": 6,
  "traceableClaims": 6,
  "traceabilityCoverage": 1.0,
  "unsupportedClaims": 0,
  "citationFailures": 0,
  "conflictCandidates": 2,
  "contradictionChecks": 2,
  "disagreementsFound": 0,
  "traceabilityRows": [
    {
      "claimId": "art-2026-03-12-004",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-11-020",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
    {
      "claimId": "art-2026-03-11-017",
      "traceable": true,
      "hasRecord": true,
      "hasMechanism": true,
      "hasSource": true
    },
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
    }
  ],
  "contradictionAudit": [
    {
      "leftId": "art-2026-03-12-004",
      "rightId": "art-2026-03-11-020",
      "label": "unclear",
      "overlapTerms": [
        "across",
        "materially"
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
    }
  ],
  "evidenceIssues": [
    {
      "index": 0,
      "queueId": "art-2026-03-12-004",
      "issue": "confidence_normalized_to_evidence",
      "agentConfidence": "medium",
      "evidenceConfidence": "high"
    }
  ],
  "fatalEvidenceIssues": [],
  "generatedAtUtc": "2026-03-12T23:33:34Z"
}
```
