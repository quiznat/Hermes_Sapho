# Executive Brief

Date: `2026-03-04`
Run ID: `pm-live-20260304T055013Z`

## Executive Summary
The evidence supports a conditional-effects conclusion with moderate confidence: AGENTS.md-style repository context files are neither uniformly beneficial nor uniformly harmful. Outcome direction depends on context governance quality, scope discipline, and evaluation framing. Efficiency gains are credible in some studies, but can coincide with flat or negative task-success outcomes when instruction regimes are over-broad or misaligned.

## Top Findings
- **art-2026-03-04-003** (agent-memory · confidence=medium): AI context files are now a measurable OSS phenomenon, but usage patterns remain heterogeneous and structurally immature.
  - Mechanism: A large OSS sampling frame (10,000 sampled repositories; detailed analysis on 466 projects) shows mixed instruction modes without canonical structure, increasing interpretation and behavior variance.
  - Source: https://arxiv.org/html/2510.21413
- **art-2026-03-03-013** (agent-memory · confidence=medium): Single-file agent manifests do not reliably scale for complex codebases; tiered codified context is proposed as a scaling pattern.
  - Mechanism: The reported three-tier model (always-loaded core conventions, task-invoked specialists, on-demand deep specs) targets the overload-amnesia tradeoff through scoped context loading.
  - Source: https://arxiv.org/html/2602.20478v1
- **art-2026-03-03-008** (agent-memory · confidence=medium): The practical failure mode is over-broad context design, not context files themselves.
  - Mechanism: Broad files can increase exploration and compliance overhead, raising cost and harming correctness on many tasks; the recommended pattern is minimal, operationally relevant context with explicit boundaries.
  - Source: https://notchrisgroves.com/when-agents-md-backfires/
- **art-2026-03-03-004** (agent-memory · confidence=medium): AGENTS.md can improve operational efficiency in paired evaluations.
  - Mechanism: Repository-level instruction compression appears to reduce exploratory overhead, with reported lower median runtime and output tokens in a 10-repository, 124-PR setup.
  - Source: https://arxiv.org/pdf/2601.20404
- **art-2026-03-03-002** (agent-memory · confidence=medium): Context files function as operational control artifacts but are often complex and unevenly scoped.
  - Mechanism: Empirical analysis (2,303 files across 1,925 repositories) shows content skew toward build/run and implementation guidance, with weaker security/performance coverage and resulting governance gaps.
  - Source: https://arxiv.org/html/2511.12884v1
- **art-2026-03-03-001** (agent-memory · confidence=medium): Repository-level context files are not automatically performance-improving and can reduce task success while increasing cost.
  - Mechanism: Behavioral over-constraint can induce broader traversal and stricter low-value compliance, consuming budget and lowering completion; LLM-generated files trend more negative than developer-authored files.
  - Source: https://arxiv.org/abs/2602.11988

## Actions
- Publish boundary-conditioned conclusions with explicit moderate-confidence labeling.
- Require four-metric scorecards for promotion decisions: task success, runtime, token cost, and failure taxonomy.
- Run matched minimal-versus-broad context ablations on identical tasks, agents, and repositories.
- Add explicit non-functional clauses (security and performance) to context governance and evaluate deltas.
- Treat tiered codified context as a testable hypothesis until replicated across multiple repositories and task regimes.

## Risks
- Overstating conditional findings as universal guidance.
- Declaring efficiency wins that mask correctness or robustness regressions.
- Cross-study confounding from heterogeneous agents, repositories, tasks, and metrics.
- Configuration drift that degrades context quality over time.
- Evidence weighting shifts as remaining queued backlog (32) is processed.
