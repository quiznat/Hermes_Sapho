# Executive Brief

Date: `2026-03-11`
Run ID: `pm-live-20260311T000251Z`

## Executive Summary
Current evidence supports a two-constraint interpretation for agentic software delivery: long-horizon memory weakness and socio-technical pull-request workflow friction are both first-order limits. Agent output volume and local commit-level coherence are real, but elevated churn, weaker PR-level alignment, stricter security-lane review drag, and process-conditioned merge outcomes keep autonomy claims bounded. Harness architecture appears necessary for reliability but is not equivalent to proven outcome uplift in this evidence set.

## Top Findings
- **art-2026-03-10-080** (agent-memory · confidence=high): LoCoMo is a primary benchmark for very long-horizon conversational memory, exposing persistent recall and temporal-causal reasoning gaps in current LLM agents.
  - Mechanism: The benchmark uses grounded personas plus temporal event graphs to produce long conversations, then evaluates memory competence via question answering, event-graph summarization, and multimodal dialogue generation, revealing long-horizon degradation.
  - Source: https://snap-research.github.io/locomo/
- **art-2026-03-10-077** (agent-factory · confidence=high): Agentic pull requests demonstrate strong local-level commit communication but weaker PR-level alignment and higher short-horizon code churn compared with human pull requests.
  - Mechanism: Across 33,596 agent PRs and 6,618 human PRs, the study reports stronger commit-message similarity but weaker PR-level summarization alignment, along with faster symbol removal and higher symbol churn for agent changes.
  - Source: https://arxiv.org/html/2601.17627v1
- **art-2026-03-10-069** (agent-factory · confidence=high): Agent-authored pull requests make meaningful security contributions in real repositories, but those contributions face stricter human scrutiny, lower merge rates, and longer review latency than non-security agentic PRs.
  - Mechanism: Large-scale AIDev analysis with manual validation of 1,293 security-related PRs shows security lanes are governed by tighter acceptance and longer review pathways than non-security lanes.
  - Source: https://arxiv.org/abs/2601.00477
- **art-2026-03-10-065** (agent-factory · confidence=high): Agent-authored pull requests fail for systematic socio-technical reasons, not just code quality issues.
  - Mechanism: Empirical analysis of 33k agent PRs plus qualitative coding of 600 failures links merged versus non-merged outcomes to task class, change scope, CI results, and review interaction dynamics.
  - Source: https://arxiv.org/abs/2601.15195v1
- **art-2026-03-10-061** (agent-factory · confidence=high): Pull-request merge success in mixed human/agentic software workflows is strongly driven by submitter attributes, while review dynamics affect human and agentic PRs differently.
  - Mechanism: Regression over 40,214 PRs with 64 engineered features shows author/process variables materially influence merge outcomes and modulate review effects by submitter type.
  - Source: https://www.arxiv.org/pdf/2601.18749
- **art-2026-03-10-034** (agent-memory · confidence=high): Terminal-native coding agents need explicit harness architecture (scaffolding, runtime orchestration, context compaction, safety layers, and memory persistence) to stay reliable over long-horizon development tasks.
  - Mechanism: OpenDev specifies a compound system with specialized routing, planning/execution separation, event-driven reminders, adaptive context compaction, and defense-in-depth execution controls; this functions as architectural prescription rather than direct large-sample causal validation.
  - Source: https://arxiv.org/html/2603.05344v1

## Actions
- Create a normalized metric layer that jointly tracks PR-level alignment, churn, merge probability, and review latency.
- Segment deployment policy by PR risk class (security sensitivity, task type, scope) with differentiated acceptance gates.
- Prioritize socio-technical controls: tighter scope caps, stronger CI requirements, standardized reviewer protocol, and handoff-quality checks.
- Map LoCoMo failure signatures to coding-session continuity breakdowns and add targeted temporal-consistency tests.
- Separate empirical findings from architectural prescriptions in synthesis confidence scoring and policy recommendations.
- Tie harness-control requirements to explicit review-capacity and security-escalation planning before expanding autonomy.

## Risks
- High PR throughput can mask instability when churn and rapid symbol reversion remain elevated.
- Security-focused PR lanes can become persistent bottlenecks because of stricter scrutiny and longer review latency.
- Socio-technical failure modes may persist even if model-level code generation quality improves.
- Long-horizon memory deficits can degrade planning continuity and temporal consistency in extended tasks.
- Submitter/process confounds can mislead capability interpretation when merge metrics are used naively.
- Architectural guidance may be over-weighted if not clearly separated from empirical outcome evidence.
