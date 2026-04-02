# Executive Actionable Research Brief

Date: 2026-03-03
Version: executive-brief-v1.1.0
Last updated (UTC): 2026-03-04T03:49:08Z
Run: status=PASS inserted=0 candidates=105 dropped=105
Sapho preflight: status=PASS traceability=1.0 unsupported=0 citationFailures=0 contradictionChecks=124
Quality gate: qualified=5 required=2

## Executive Summary
Core read: Single-file agent manifests do not scale reliably for complex codebases; a tiered “codified context infrastructure” (hot-memory constitution + specialist agents + cold-memory knowledge base) can preserve cross-session coherence and reduce repeated failure patterns. Current qualified evidence spans 5 items across lanes (agent-memory=5).

## High-Conviction Findings
- **Single-file agent manifests do not scale reliably for complex codebases; a tiered “codified context infrastructure” (hot-memory constitution + specialist agents + cold-memory knowledge base) can preserve cross-session coherence and reduce repeated failure patterns.** (art-2026-03-03-013 · agent-memory · confidence=medium · evidence=medium)
  - Mechanism: The paper reports a large-project case (108k-line distributed system) and proposes a three-tier memory architecture: always-loaded core conventions, task-invoked domain specialists, and on-demand deep specs. The claimed mechanism is scoped context loading: keep universal guardrails persistent while routing detailed domain knowledge only when needed, avoiding both context amnesia and context overload.
  - Source: https://arxiv.org/html/2602.20478v1
  - Artifact: `research/kb/queue/queue-art-2026-03-03-013-codified-context-infrastructure.md`
- **The practical failure mode is not “context files bad,” but “over-broad context files backfire.” This synthesis argues for minimal, operationally relevant agent context with explicit boundaries and commands.** (art-2026-03-03-008 · agent-memory · confidence=medium · evidence=medium)
  - Mechanism: The post integrates multiple studies and highlights a recurring mechanism: broad context files increase agent exploration and instruction-following overhead, which can raise cost and reduce correctness on many tasks. It also surfaces an important tradeoff from another study: some context configurations improve speed/token efficiency while not necessarily improving correctness. The actionable pattern is conditional governance: optimize for task success first, then efficiency, using tightly scoped context requirements.
  - Source: https://notchrisgroves.com/when-agents-md-backfires/
  - Artifact: `research/kb/queue/queue-art-2026-03-03-008-agents-md-backfires-practitioner-synthesis.md`
- **This paper reports that AGENTS.md can improve operational efficiency for coding-agent runs, with lower median runtime and lower output-token usage in a paired with/without-file setup across sampled pull requests.** (art-2026-03-03-004 · agent-memory · confidence=medium · evidence=medium)
  - Mechanism: The mechanism claim is configuration compression and guidance efficiency: a repository-level instruction file can reduce exploratory overhead by providing persistent project constraints and workflows up front. In the reported data (10 repositories, 124 PRs), this is associated with faster completion and lower token spend while maintaining comparable completion behavior.
  - Source: https://arxiv.org/pdf/2601.20404
  - Artifact: `research/kb/queue/queue-art-2026-03-03-004-agents-md-efficiency-impact.md`
- **Agent context files (AGENTS.md/CLAUDE.md/copilot-instructions style files) have become operational control artifacts, but in practice they are often complex, hard to read, and unevenly scoped: teams emphasize functional execution guidance while under-specifying non-functional guardrails.** (art-2026-03-03-002 · agent-memory · confidence=medium · evidence=medium)
  - Mechanism: The paper reports a large empirical sample (2,303 context files across 1,925 repositories). It finds that maintenance behavior looks like configuration drift management (frequent small additions), and that instruction content is skewed toward build/run, implementation details, and architecture. Security and performance instructions appear far less frequently, creating a governance gap where agents are guided on how to make things work more than how to keep outcomes safe and efficient.
  - Source: https://arxiv.org/html/2511.12884v1
  - Artifact: `research/kb/queue/queue-art-2026-03-03-002-agent-readmes-empirical-study.md`
- **Repository-level context files (for example AGENTS.md) are not automatically performance-improving for coding agents. In the paper’s evaluations, context files often reduced task success while increasing inference cost.** (art-2026-03-03-001 · agent-memory · confidence=medium · evidence=medium)
  - Mechanism: The reported mechanism is behavioral over-constraint: context files induce broader exploration and instruction-following (more file traversal/testing and stricter requirement adherence), but this added process overhead can make task completion harder when requirements are unnecessary or overly broad. The authors observe that LLM-generated context files trend negative on success, while developer-authored files provide only marginal benefit.
  - Source: https://arxiv.org/abs/2602.11988
  - Artifact: `research/kb/queue/queue-art-2026-03-03-001-agents-md-evaluation.md`

## Recommended Actions
- Dispatch the next highest-conviction non-X queue item and finalize with telemetry evidence.
- Apply weekly query retire/promote output to suppress low-yield discovery channels.
- Continue with current quality gate; maintain strict retain+confidence inclusion policy.

## Risks / Watchlist
- No immediate critical reporting-quality risk observed under current gate settings.

## Artifacts
- `research/firehose/logs/firehose-daily-20260304T024547Z.json`
- `research/queue/article-intake-queue.jsonl`
- `research/kb/queue/queue-art-2026-03-03-013-codified-context-infrastructure.md`
- `research/kb/queue/queue-art-2026-03-03-008-agents-md-backfires-practitioner-synthesis.md`
- `research/kb/queue/queue-art-2026-03-03-004-agents-md-efficiency-impact.md`
