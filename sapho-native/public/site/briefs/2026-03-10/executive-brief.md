# Executive Brief

Date: `2026-03-10`
Run ID: `pm-live-20260310T233009Z`

## Executive Summary
Evidence supports a productivity-with-friction interpretation, not an autonomy-forward one. Agent PR pipelines are active and locally communicative, but they show weaker PR-level alignment, higher short-horizon churn, and persistent non-merge pressure driven by socio-technical workflow conditions. Security contributions are real but governance-heavy, and enterprise-like long-horizon benchmarks still show unresolved reliability gaps.

## Top Findings
- **art-2026-03-10-077** (agent-factory · confidence=high): Agentic pull requests demonstrate strong local-level commit communication but weaker PR-level alignment and higher short-horizon code churn compared with human pull requests.
  - Mechanism: In a comparison of 33,596 agent-generated PRs and 6,618 human PRs, APR changes show faster symbol removal, higher symbol churn, stronger commit-message semantic similarity, and weaker PR-level summarization alignment, indicating local coherence does not guarantee durable review-scope stability.
  - Source: https://arxiv.org/html/2601.17627v1
- **art-2026-03-10-069** (agent-factory · confidence=high): Agent-authored pull requests make meaningful security contributions in real repositories, but those contributions face stricter human scrutiny, lower merge rates, and longer review latency than non-security agentic PRs.
  - Mechanism: Large-scale AIDev analysis plus manual validation of 1,293 security-related PRs shows security lane outcomes are constrained by stronger governance and review burdens relative to non-security agent PRs.
  - Source: https://arxiv.org/abs/2601.00477
- **art-2026-03-10-065** (agent-factory · confidence=high): Agent-authored pull requests fail for systematic socio-technical reasons, not just code quality issues.
  - Mechanism: MSR 2026 evidence across ~33k PRs and qualitative coding of 600 failed cases links outcomes to workflow factors including task type, change scope, CI behavior, and review dynamics.
  - Source: https://arxiv.org/abs/2601.15195v1
- **art-2026-03-10-061** (agent-factory · confidence=high): Pull-request merge success in mixed human/agentic software workflows is strongly driven by submitter attributes, while review dynamics affect human and agentic PRs differently.
  - Mechanism: Regression analysis on 40,214 PRs with 64 features across six families shows merge outcomes are materially confounded by author/process variables, complicating pure model-capability attribution.
  - Source: https://www.arxiv.org/pdf/2601.18749
- **art-2026-03-10-034** (agent-memory · confidence=high): Terminal-native coding agents need explicit harness architecture (scaffolding, runtime orchestration, context compaction, safety layers, and memory persistence) to stay reliable over long-horizon development tasks.
  - Mechanism: The OpenDev report specifies a compound harness with workflow-specialized routing, planning/execution separation, event-driven reminders, adaptive compaction, and defense-in-depth execution controls; this is architectural guidance rather than direct large-sample outcome validation.
  - Source: https://arxiv.org/html/2603.05344v1
- **art-2026-03-10-015** (agent-factory · confidence=high): Agentic coding performance on real enterprise software work remains far from autonomous reliability once evaluated on long-horizon, contamination-resistant tasks rather than easier public bug-fix subsets.
  - Mechanism: SWE-Bench Pro introduces 1,865 human-verified tasks across public, held-out, and commercial-like splits, showing substantial degradation under more realistic long-horizon constraints.
  - Source: https://arxiv.org/html/2509.16941

## Actions
- Adopt paired quality metrics that jointly track commit-level communication quality and PR-level alignment/churn before declaring productivity gains.
- Segment deployment and gate policy by PR class (security vs non-security), scope tier, and task type, with stricter controls for high-risk lanes.
- Build a unified rejection taxonomy that maps socio-technical failure modes to enforceable controls (scope caps, CI gates, reviewer protocol, handoff rules).
- Use feature-informed triage and routing so submitter/process effects are modeled explicitly rather than inferred from raw merge rate.
- Separate empirical outcome findings from architectural guidance in reporting, with explicit confidence tier labels.
- Bind autonomy-readiness claims to realism-tier benchmarks (public vs held-out/commercial-like) and require passing thresholds before production expansion.

## Risks
- High throughput can mask instability when churn and fast symbol reversion remain elevated.
- Security-focused agent PR lanes can become governance bottlenecks because of stricter review and longer latency.
- Socio-technical failure drivers may persist even if base model code quality improves.
- Submitter/process confounds can bias merge metrics and misstate actual agent capability.
- Architectural prescriptions may be over-weighted if not clearly separated from empirical outcome evidence.
- Performance on easier public subsets may be misread as enterprise readiness without realism-tier controls.
