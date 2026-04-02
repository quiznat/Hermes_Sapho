---
version: source-capture.v1
article_id: art-2026-03-03-008
ticket_id: ticket-import-art-2026-03-03-008
source_url: https://notchrisgroves.com/when-agents-md-backfires/
canonical_url: https://notchrisgroves.com/when-agents-md-backfires
source_title: 'When AGENTS.md Backfires: What a New Study Says About Context Files
  and Coding Agents'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-07T19:27:13Z'
---
# Source Capture

## Title

When AGENTS.md Backfires: What a New Study Says About Context Files and Coding Agents

## Body

When AGENTS.md Backfires: What a New Study Says About Context Files and Coding Agents
Intelligence Adjacent
About
Setup Guide
Referrals
Sign in
Subscribe
framework
When AGENTS.md Backfires: What a New Study Says About Context Files and Coding Agents
A new ETH Zurich study finds that LLM-generated context files reduce task success rates and raise inference costs by 20%. Here's what the data actually shows.
Chris Groves
23 Feb 2026
— 8 min read
OpenAI's own monorepo contains 88 AGENTS.md files . The format has been adopted across more than 60,000 public repositories . GitHub, Google, Anthropic, and Cursor all support their own variants of the pattern. The broad consensus from industry guidance is that giving coding agents a dedicated context file — a README written for the agent rather than the human — leads to better outcomes.
A paper published in February 2026 by researchers at ETH Zurich puts that consensus under empirical scrutiny. The findings are more nuanced than the headlines suggest, but there are specific, data-backed reasons to reconsider how — not whether — you use these files.
What AGENTS.md Is and How It Got Here
The format emerged in mid-2025 when OpenAI launched Codex, its cloud-based coding agent. AGENTS.md was introduced as a machine-readable configuration layer: a Markdown file at the repository root that a coding agent reads before starting work. It describes project structure, build and test commands, coding conventions, and any operational constraints the agent should respect.
The concept spread quickly because it addressed a real problem. Developers were frustrated maintaining parallel configuration artifacts — .cursorrules for Cursor, CLAUDE.md for Anthropic's Claude Code, copilot-instructions.md for GitHub Copilot, GEMINI.md for Google's Gemini CLI. AGENTS.md was positioned as the unified standard , eventually handed to the Agentic AI Foundation under the Linux Foundation for stewardship.
The value proposition was intuitive: agents that know your project's conventions should require less back-and-forth, produce more consistent code, and fail less often on environment-specific quirks like tool invocation or test runner flags. A November 2025 empirical study of 2,303 context files confirmed that developers treat these files seriously — between 59 and 67% of them receive multiple commits over time, maintained at roughly daily update rates.
The question the ETH Zurich team set out to answer was whether that investment was paying off in measurable task outcomes.
What the ETH Zurich Study Measured
The researchers constructed two evaluation environments. The first was AGENTbench, a new benchmark of 138 software engineering tasks drawn from real GitHub pull requests across 12 Python repositories, each of which already contained a developer-written AGENTS.md or equivalent file. The second was SWE-bench Lite, an existing benchmark of 300 tasks used as a comparison baseline.
They tested four coding agents across three conditions: no context file, an LLM-generated (large language model) context file, and the developer-provided file. The agents were Claude Code (Sonnet 4.5), Codex (GPT-5.2 and GPT-5.1 Mini), and Qwen Code (Qwen3-30B-Coder).
The headline results:
LLM-generated context files reduced task success rates in 5 of 8 evaluation settings , with an average performance drop of 0.5 to 2 percentage points. Developer-provided files fared better — showing approximately a 4 percentage point improvement on AGENTbench — but came at a cost: all context file types, regardless of source, increased inference costs by 20 to 23% and added an average of 2.45 to 3.92 additional steps per task.
The reasoning token overhead is also notable. For GPT-series models, reasoning tokens increased by 14 to 22% when a context file was present. The agent was thinking harder, taking more steps, and costing more — while succeeding at the same rate or less.
The Exploration Paradox
One of the more striking findings in the paper concerns agent behavior rather than task outcomes. When context files were present, agents explored more: more file traversal, more test execution, more careful tool usage. The 1.6x increase in uv invocations when uv was mentioned in the context file illustrates the pattern — agents follow tooling instructions faithfully.
The paradox is that broader exploration and faithful instruction-following did not translate into higher success rates. The authors' interpretation is that context files function primarily as execution constraints, not as navigation aids. An agent given a context file has to satisfy both the task requirements and the context file's directives. When those two sets of requirements conflict — or when the context file imposes requirements the agent would not have needed to satisfy on its own — the additional constraint space costs steps and tokens without proportionally improving outcomes.
The researchers phrase their recommendation carefully: human-written files should describe "only minimal requirements to avoid making tasks unnecessarily difficult." That framing is precise. The problem is not context per se — it is context that does not directly address the agent's actual gaps.
The Counter-Study: Fast vs. Right
Before drawing firm conclusions, a second study warrants attention. Submitted to the Journal Ahead Workshop (JAWs) 2026, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents" ran a different kind of experiment: the same tasks executed by Codex, paired, with and without AGENTS.md files, across 124 pull requests.
The results read as a direct contradiction. With AGENTS.md, median completion time dropped from 98.57 to 70.34 seconds — a 28.64% reduction . Output tokens fell by 20%. The results were statistically significant.
The studies are not actually contradicting each other. They are measuring different things.
The JAWs study measured efficiency — wall-clock time and token consumption. The ETH Zurich study measured effectiveness — whether the task passed its test suite. An agent that completes a task 28% faster but produces incorrect output has not improved outcomes; it has optimized the wrong metric. Equally, the JAWs study used only Codex on small, narrow PRs (under 100 lines changed, under 5 files modified). The ETH Zurich study used multiple agents across more complex, real-world tasks.
The picture that emerges from both studies together is a specific tradeoff: context files may reduce the exploratory work an agent does (which saves time and tokens) while simultaneously constraining the action space in ways that reduce the probability of correct task completion. You can be faster and less accurate at the same time.
The LLM-Generated Context File Problem
There is a workflow that deserves scrutiny here: pointing an LLM at your codebase and asking it to generate AGENTS.md for you. It is fast, low-friction, and increasingly supported by tooling. The ETH Zurich study suggests it is counterproductive.
The reasoning is traceable. An LLM generating a context file defaults to comprehensiveness — it includes overviews of architecture, file structure, key dependencies, and conventions, because all of those things seem potentially relevant. The paper found that 95 to 100% of LLM-generated context files include repository overviews , yet agents with these files discovered relevant files no faster than agents with no file at all. The overview content was redundant with information the agent could derive by reading the codebase itself.
A revealing experiment in the paper removes existing documentation from repositories before testing. In that condition, LLM-generated context files improved performance by 2.7%. The implication: when LLMs generate context, they largely restate what the README and source files already say. Add a context file on top of a well-documented repository, and you have added cost without information gain.
How This Changes What to Include
The empirical studies converge on a consistent practical model, even if their headlines seem to conflict.
Write it yourself. LLM-generated context files should be omitted or treated as a first draft requiring significant editorial reduction. The LLM's instinct is to include everything; the evidence says include less.
Include what agents cannot infer. An agent can read your source files, discover your test runner, and identify your import style. What it cannot infer are things specific to your environment: which flag combination actually works with your particular CI (Continuous Integration) setup, which directory should never be touched, which tool the team is migrating to and when. That is the class of information worth including.
Short files are followed more reliably. A November 2025 analysis found that the average Claude Code context file scores 16.6 on the Flesch Reading Ease scale (a standard readability measure where lower scores indicate harder text) — the same range as legal documents. Dense, hard-to-parse files impose parsing overhead on both agents and humans. The Dometrain and HumanLayer research independently reached the same conclusion: context files under 60 to 100 lines are more reliably followed than longer ones. Claude Code itself injects a system reminder that CLAUDE.md content "may or may not be relevant to your tasks," making selective application a built-in behavior rather than an exception.
Commands over descriptions. GitHub's analysis of 2,500+ files found a clear divide between files that work and files that fail. Executable commands ( pytest -v --no-cov ) outperform architectural descriptions. Agents can read architecture; they benefit from explicit, correct invocation syntax.
Security is almost always missing. The November 2025 study found that only 14.5% of agent context files include security instructions . Agents operating with file write access, package management, and the ability to modify configuration are making consequential changes autonomously. Explicitly stating what they should not touch — credentials, production configs, dependency pinning — is not optional.
Tool-Specific Notes
The research is primarily framed around AGENTS.md and Codex, but the pattern holds across agents. Claude Code uses CLAUDE.md with the same functional role. Anthropic has an open GitHub issue requesting native AGENTS.md support , reflecting community pressure for cross-tool compatibility. In practice, many teams already symlink AGENTS.md → CLAUDE.md → GEMINI.md as a single-source-of-truth workaround.
The model-level behavior differs meaningfully. Claude Code applies context selectively and signals this to the model. Codex builds an instruction chain once per run from the full file hierarchy. These differences matter when deciding how to structure content: with Claude, depth via separate referenced files is viable; with Codex, front-loading the most critical instructions matters more since the chain is assembled before execution begins.
A concurrent 2026 study, SWE Context Bench, found that oracle-guided experience reuse achieves the highest task resolution rates, but autonomous reuse without reliable selection may degrade performance . The pattern maps directly onto the AGENTS.md finding: context that is correctly scoped and reliably relevant helps; context that is broadly assembled and autonomously applied hurts.
What This Means in Practice
The ETH Zurich study's core recommendation — minimal, human-written, requirement-focused — aligns with what empirical analysis of thousands of real-world files shows actually works. The practical translation:
Do not use an LLM to generate your initial context file. Write it by hand with a specific problem in mind.
Keep the file short enough that every line is genuinely load-bearing.
Prioritize executable commands and explicit boundaries over narrative description.
Specify at least one security boundary. Most files currently do not have any.
If a piece of information is already in your README or your source code, do not duplicate it in the context file.
Treat the file as configuration: version control it, review changes to it, and remove instructions that are no longer accurate.
The research does not say context files are useless. Developer-written files with appropriately scoped requirements produced measurable improvement in the ETH Zurich benchmarks. The finding is narrower and more actionable than the headline: the current dominant pattern — comprehensive, LLM-generated, architecture-heavy — is adding cost and reducing correctness. The format's potential is real; the way most teams currently use it is working against them.
Found This Helpful?
The research on AI coding agents is moving fast. If you want analysis like this — measured, evidence-backed, no hype — subscribe for free.
Subscribe to Intelligence Adjacent
Sources
Primary Research
Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? (ETH Zurich, Feb 2026)
On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents (JAWs 2026)
Agent READMEs: An Empirical Study of Context Files for Agentic Coding (Nov 2025)
On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code (Sep 2025)
SWE Context Bench: A Benchmark for Context Learning in Coding (arXiv, 2026)
Official Documentation & Specification
OpenAI Codex AGENTS.md Official Documentation
AGENTS.md GitHub Spec Repository
Industry Coverage & Analysis
AGENTS.md Emerges as Open Standard for AI Coding Agents (InfoQ, Aug 2025)
How to write a great agents.md: Lessons from over 2,500 repositories (GitHub Blog)
Context files for coding agents often don't help — and may even hurt performance (The Decoder)
AGENTS.md becomes the convention (pnote.eu)
Practitioner Guidance
AGENTS.md Community Guide (agentsmd.net)
Writing a good CLAUDE.md (HumanLayer Blog)
Creating the Perfect CLAUDE.md for Claude Code (Dometrain)
Community Discussions
Claude Code AGENTS.md feature request issue (GitHub)
Read more
From Root to Project-Only: Restructuring Your IA Framework Installation
A step-by-step guide for existing IA Framework users to migrate from symlink-based root installation to clean project-only architecture.
By Chris Groves
06 Mar 2026
AI Red Teaming: Beyond Prompt Injection
Prompt injection is just the beginning. As AI systems evolve from chatbots to autonomous agents, the attack surface expands into territory traditional security teams have never defended.
By Chris Groves
04 Mar 2026
Switching from Claude Code to OpenCode: A Deep Dive into MiniMax-M2.5 as Primary LLM
After months using Claude Code with Anthropic models, I tried switching to OpenCode with MiniMax-M2.5. Here's the honest analysis of cost, speed, accuracy, and whether the tradeoffs are worth it.
By Chris Groves
02 Mar 2026
Evolution to Agentic SaaS
From CLI tool to multi-tenant platform: the architecture decisions that enable BYOK trust, agent deployment, and collaborative compliance workflows.
By Chris Groves
02 Mar 2026
Intelligence Adjacent
Privacy Policy
Terms of Service
Github
X
Powered by Ghost
Intelligence Adjacent
Democratizing expertise through deployable modules within Intelligence Adjacent. I'm Chris Groves, sharing lessons learned building AI systems that augment human capability instead of replace it.
Subscribe

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-03-008.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-03-008.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-03-008.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
- refreshed_live_source: false
