# Queue Artifact — art-2026-03-03-008

Source URL: https://notchrisgroves.com/when-agents-md-backfires/  
Canonical URL: https://notchrisgroves.com/when-agents-md-backfires  
Lane: agent-memory  
Decision: retain

## Thesis

The practical failure mode is not “context files bad,” but “over-broad context files backfire.” This synthesis argues for minimal, operationally relevant agent context with explicit boundaries and commands.

## Mechanism summary

The post integrates multiple studies and highlights a recurring mechanism: broad context files increase agent exploration and instruction-following overhead, which can raise cost and reduce correctness on many tasks. It also surfaces an important tradeoff from another study: some context configurations improve speed/token efficiency while not necessarily improving correctness. The actionable pattern is conditional governance: optimize for task success first, then efficiency, using tightly scoped context requirements.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| Developer-provided files fared better — showing approximately a 4 percentage point improvement on AGENTbench — but came at a cost: all context file types, regardless of source, increased inference costs by 20 to 23% and added an average of 2.45 to 3.92 additional steps per task. | 0.5, 2, 2.45, 20, 23%, 3.92, 4, 5, 8 | LLM-generated context files reduced task success rates in 5 of 8 evaluation settings , with an average performance drop of 0.5 to 2 percentage points. | Developer-provided files fared better — showing approximately a 4 percentage point improvement on AGENTbench — but came at a cost: all context file types, regardless of source, increased inference costs by 20 to 23% and added an average of 2.45 to 3.92 additional steps per task. | — |
| A November 2025 empirical study of 2,303 context files confirmed that developers treat these files seriously — between 59 and 67% of them receive multiple commits over time, maintained at roughly daily update rates. | 2,303, 2025, 59, 67% | A November 2025 empirical study of 2,303 context files confirmed that developers treat these files seriously — between 59 and 67% of them receive multiple commits over time, maintained at roughly daily update rates. | A November 2025 empirical study of 2,303 context files confirmed that developers treat these files seriously — between 59 and 67% of them receive multiple commits over time, maintained at roughly daily update rates. | — |
| LLM-generated context files reduced task success rates in 5 of 8 evaluation settings , with an average performance drop of 0.5 to 2 percentage points. | 0.5, 2, 2.45, 20, 23%, 3.92, 4, 5, 8 | LLM-generated context files reduced task success rates in 5 of 8 evaluation settings , with an average performance drop of 0.5 to 2 percentage points. | LLM-generated context files reduced task success rates in 5 of 8 evaluation settings , with an average performance drop of 0.5 to 2 percentage points. | Developer-provided files fared better — showing approximately a 4 percentage point improvement on AGENTbench — but came at a cost: all context file types, regardless of source, increased inference costs by 20 to 23% and added an average of 2.45 to 3.92 additional steps per task. |
| Submitted to the Journal Ahead Workshop (JAWs) 2026, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents" ran a different kind of experiment: the same tasks executed by Codex, paired, with and without AGENTS.md files, across 124 pull requests. | 124, 2026 | Submitted to the Journal Ahead Workshop (JAWs) 2026, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents" ran a different kind of experiment: the same tasks executed by Codex, paired, with and without AGENTS.md files, across 124 pull requests. | Submitted to the Journal Ahead Workshop (JAWs) 2026, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents" ran a different kind of experiment: the same tasks executed by Codex, paired, with and without AGENTS.md files, across 124 pull requests. | — |
| The first was AGENTbench, a new benchmark of 138 software engineering tasks drawn from real GitHub pull requests across 12 Python repositories, each of which already contained a developer-written AGENTS.md or equivalent file. | 12, 138 | The first was AGENTbench, a new benchmark of 138 software engineering tasks drawn from real GitHub pull requests across 12 Python repositories, each of which already contained a developer-written AGENTS.md or equivalent file. | The first was AGENTbench, a new benchmark of 138 software engineering tasks drawn from real GitHub pull requests across 12 Python repositories, each of which already contained a developer-written AGENTS.md or equivalent file. | — |

## Confidence

Medium. This is a secondary synthesis source (not primary experimental artifact), but it consolidates cross-study interpretation and implementation guidance that is useful for operational policy design.

## Why it matters for Sapho

This directly supports Sapho’s contract approach: keep context manifests short, command-oriented, security-aware, and continuously pruned; treat them as governed configuration rather than static documentation.
