---
version: source-capture.v1
article_id: art-2026-03-04-032
ticket_id: ticket-import-art-2026-03-04-032
source_url: https://arxiv.org/abs/2512.10398
canonical_url: https://arxiv.org/abs/2512.10398
source_title: 'Confucius Code Agent: An Open-sourced AI Software Engineer at Industrial
  Scale'
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-30T18:16:47Z'
linked_paper_urls: []
---
# Source Capture

## Title

Confucius Code Agent: An Open-sourced AI Software Engineer at Industrial Scale

## Body

1]Meta
2]Harvard \contribution [*] Core Contributors

Confucius Code Agent: An Open-sourced AI Software Engineer at Industrial Scale

Zhaodong Wang Zhenting Qi Sherman Wong Nathan Hu Samuel Lin Jun Ge Erwin Gao Yining Yang Ben Maurer Wenlin Chen David Recordon Yilun Du Minlan Yu Ying Zhang [ [ zhentingqi@g.harvard.edu

( December 11, 2025 )

Abstract

Real-world AI software engineering demands coding agents that can reason over massive repositories, maintain durable memory across and within long sessions, and robustly coordinate complex toolchains at test time.
Existing open-source coding agents provide transparency but frequently fall short when pushed to these industrial-scale workloads, while proprietary coding agents offer strong practical performance but limited extensibility, interpretability, and controllability.
We present the Confucius Code Agent (CCA) , an open-sourced AI software engineer that can operate at an industrial scale. CCA is built atop the Confucius SDK , an open-sourced agent development platform designed around three complementary perspectives: Agent Experience (AX) , User Experience (UX) , and Developer Experience (DX) . The SDK introduces a unified orchestrator with hierarchical working memory for long-context reasoning, a persistent note-taking system for cross-session continual learning, and a modular extension module for robust tool use.
Moreover, a meta-agent automates the synthesis, evaluation, and refinement of agent configurations through a build-test-improve loop, enabling rapid agent development on new tasks, environments, and tool stacks.
Instantiated on Confucius SDK with these mechanisms, CCA delivers strong performance on real-world software engineering tasks. On SWE-Bench-Pro, CCA achieves a state-of-the-art Resolve@1 performance of 54.3% , substantially improving over prior coding agents.
Together, the Confucius SDK and CCA provide a transparent, extensible, and reproducible foundation for AI agents, bridge gaps between research prototypes and production-grade systems, and support agent development and deployment at industrial scale.

\correspondence

Zhenting Qi at \metadata [Code] https://github.com/facebook/confucius

1 Introduction 
Figure 1 : Confucius SDK overview. The SDK unifies an orchestrator for iterative reasoning and action execution, long-term memory for continual learning, and modular extensions for tool use and interacting with the external environment.

Software engineering has rapidly emerged as a frontier application area for large language models (LLMs).
As models have grown more capable, they have progressed from simple program synthesis (Austin et al., 2021 ) , to automatic code completion (Chen et al., 2021 ) , to general-purpose code generation (Li et al., 2022 ; Lai et al., 2023 ) , to understanding code execution (Gu et al., 2024 ) , and competition-level programming (Jain et al., 2024 ) .
Most recently, LLMs have demonstrated strong software engineering ability to tackle real-world issue resolution in open-source repositories (Jimenez et al., 2023 ; Yang et al., 2024 ; Xia et al., 2025 ; Zeng et al., 2025 ) .
To support such capabilities, more sophisticated agentic frameworks such as OpenHands (Wang et al., 2024 ) scaffold LLMs with tools for search, code editing, and command execution, while agentless prompting-based approaches (Xia et al., 2024 ) have shown that carefully structured prompts alone can also perform well on multi-step software engineering tasks.

However, as LLMs transition from simple code assistants to more sophisticated AI software engineers operating inside real-world repositories, practitioners often face a trade-off between open-source and proprietary ecosystems.
On one hand, open-source systems provide transparency and reproducibility, but are often limited to narrower tasks with heuristic pipelines and limited capability in large-scale codebases.
On the other hand, modern proprietary systems such as Cursor (Cursor, 2025 ) and Claude Code (Anthropic, 2025a ) have become de facto choices for handling large-scale software engineering workflows.
Although highly effective, these systems are closed, offering limited transparency, restricted extensibility, opaque reasoning processes, and potential risks of exposing sensitive code or violating license constraints (Zhao et al., 2025 ) .

This tension is exacerbated in industrial-scale codebases, which are usually orders of magnitude larger than typical benchmark projects, contain deeply interdependent components, and evolve continuously (Deng et al., 2025 ) .
In practice, when pushed into such environments, existing open coding agents fall short along two core dimensions of challenges :

- •

C1 : Long-context reasoning. Beyond understanding large files, agents should localize relevant code segments inside massive repositories and perform multi-hop reasoning across dispersed modules and long execution traces.

- •

C2 : Long-term memory. Effective agents should accumulate persistent knowledge—learning from both successes and failures, retaining useful patterns and invariants, and avoiding repeated invalid actions or dead-end strategies across tasks and sessions.

Beyond these agent-level challenges, there is a broader system-level gap: there is a lack of a development platform that is explicitly designed to optimize
1) how LLM agents see, think, and learn,
2) how end users understand, trust, and interact with them, and
3) how agent developers observe, evaluate, extend, and maintain them across complex enterprise stacks.
We articulate this gap through three complementary perspectives: Agent Experience (AX) , User Experience (UX) , and Developer Experience (DX) .
AX concerns how effectively the agent can reason, act, and adapt given the constraints of context length, memory, and available tools.
UX concerns how human users experience the agent: interpretability, controllability, and safety, especially when the agent operates on sensitive production code.
DX spans and integrates both AX and UX: developers have deep observability into the agent’s internal reasoning traces and tool interactions (AX), as well as visibility into how the agent communicates with users (UX), together with reliable evaluation channels for diagnosing and improving agent behavior (Figure 2 ).
To build AI software engineers that are powerful, trustworthy, and maintainable, we therefore need an open, extensible development platform that explicitly balances AX, UX, and DX rather than optimizing for only one dimension .

We first present the Confucius SDK , an extensible, production-grade agent development platform designed around these three axes.
Through support for AX, UX, and DX, the SDK enables developers to compose agent behaviors, plug in custom tools, and instrument agents for rich observability and evaluation, while giving agents themselves precise control over context, memory, and tool usage.
On this platform, we instantiate our first agent, the Confucius Code Agent (CCA) , an AI software engineer designed for real-world, industrial-scale development.
CCA is built as a concrete configuration of the Confucius SDK tailored to software engineering: it binds together search, file editing, CLI, testing, planning, and optimization extensions, and deploys them over large repositories.

The Confucius SDK provides a set of features , each explicitly aligned with AX, UX, or DX, and each instantiated by CCA to address the above-mentioned core challenges of large-scale software engineering:

- •

F1 ( C1 ; AX): Context management. The Confucius SDK structures long execution trajectories into a hierarchical working-memory scheme and applies adaptive context compression, enabling agents to focus on the most relevant information in the execution history while respecting context limits.
Instantiated in CCA, this mechanism combines hierarchical scopes with a planner agent that summarizes and compacts histories, making long-horizon software engineering on industrial-scale repositories feasible.

- •

F2 ( C2 ; AX, UX): Note-taking. A dedicated note-taking agent distills execution trajectories into persistent, hierarchical Markdown notes, including “hindsight notes” capturing both successful strategies and characteristic failure modes.
For AX, CCA reuses these notes as a durable knowledge base that helps it learn from past experiences .
For UX, the same notes provide human developers with an interpretable record of agent behavior and repository-specific insights that persist across sessions.

- •

F3 ( C1 ; AX, DX): Extensions. In the Confucius SDK, nearly all tool-use capabilities are modularized into extensions attached to the orchestrator via typed callbacks.
These components handle parsing, prompt shaping, and tool execution while maintaining their own state and interacting with structured memory and I/O.
This separation strengthens AX by giving the agent fine-grained control over tools, context, and long-term memory, and strengthens DX by enabling developers to plug in utilities, monitoring, observability hooks, or safety guards without redesigning the agent.

- •

F4 (DX): Meta-agent. The Confucius SDK includes a Meta Agent that automatically builds and refines agents through a build–improve–test loop guided by natural language specifications and task feedback.
In our deployment, CCA is itself produced through this meta-agent process: its prompts, tool stack, and orchestration patterns are synthesized and improved on a set of testing tasks.
This yields strong DX benefits, as developers can rapidly create new agents and support test-time adaptation to various user expectations and evolving environments.

Unlike proprietary systems, CCA is fully transparent and reproducible: its orchestration logic, prompts, and tool stack are exposed, enabling detailed analysis, ablation, and customization.
To evaluate CCA as a real-world AI software engineer, we conduct experiments across both established benchmarks and industrial-style tasks.
We report results on SWE-Bench-Verified (Jimenez et al., 2023 ) and SWE-Bench-Pro (Deng et al., 2025 ) using the public evaluation pipelines, and construct a tiny PyTorch-Bench for more in-depth analysis of agent behaviors in a realistic, widely used ecosystem.
We further provide ablations that isolate the impact of context management, note-taking, and extensions, as well as error analyses that categorize common failure modes and remaining gaps.

In summary, our contributions are fourfold:

- •

We release the Confucius Code Agent (CCA) , an open-sourced AI software engineer explicitly designed to operate on industrial-scale repositories.

- •

We release the Confucius SDK , an open-sourced, AX/UX/DX-balanced agent development platform that separates orchestration from capabilities and provides structured memory, modular extensions, and persistent note-taking.

- •

We show that agent scaffolding—not just backbone model capability—is a primary determinant of agentic software-engineering performance, providing concrete evidence that appropriate orchestration, context management, and tool abstractions can outperform stronger backbone models.

- •

We conduct a comprehensive empirical study on SWE-Bench-Verified, SWE-Bench-Pro, and a custom PyTorch-Bench, including ablations and error analyses, establishing Confucius SDK and CCA as an open-sourced foundation for both research and production in AI agents.

2 Method

2.1 Design Philosophy: AX, UX, and DX 
Figure 2 : An illustration for AX, UX, and DX.

Most agent frameworks implicitly optimize for a single audience—either the human user, the agent itself, or the developer building the agent. The Confucius SDK instead adopts a three-axis design philosophy that treats all Agent Experience , User Experience , and Developer Experience as first-class and interdependent design concerns.
Below, we elaborate on each of the three axes:

Agent Experience (AX).

AX defines the agent’s internal cognitive workspace: which information it receives, how that information is structured, and what affordances it has for reasoning and tool use. Unlike UX, AX must avoid noise. Verbose logs, raw diffs, and metadata that help humans often distract or bias the model. AX therefore emphasizes distilled working memory, hierarchical memories, and adaptive summaries that preserve essential state while keeping prompts concise and stable.

User Experience (UX).

UX indicates how humans observe and interact with the agent. It prioritizes transparency and interpretability through readable logs, execution traces, and artifact previews. UX determines what users see and aims to maximize clarity and trust.

Developer Experience (DX).

DX concerns building, inspecting, and improving agents. It requires observability into both the agent’s reasoning (AX) and its external behavior (UX), along with modular interfaces for prompts, tools, and memory. Strong DX enables reproducibility, ablations, debugging, and rapid iteration.

Decoupling the Three Axes.

Many frameworks implicitly equate UX and AX, passing human-oriented traces directly into the model. This harms all three axes: AX suffers from context overflow and spurious anchors; UX suffers when information must be trimmed; DX becomes harder when human- and agent-facing representations entangle. CCA avoids this by separating the channels. Users see rich, instrumented traces; the agent sees compressed, structured memory; developers see both.
Below shows a concrete example between AX and UX:

For UX (Users See):

⬇

Creating file at config . py

File created successfully at config . py

Here is the diff :

+ PORT =8080

+ DEBUG = true

+ MAX_CONNECTIONS =100

For AX (Agent Sees):

⬇

Human : [ previous user message ]

AI : < file_edit type =" create " file_path =" config . py ">...</ file_edit >

Human : < result > File created successfully </ result >

In this case, users are presented with rich, streaming updates, whereas the agent receives only a compressed summary of the outcome stored in the memory manager, without the lengthy file diff message.

2.2 The Orchestrator

At the core of CCA lies the Confucius Orchestrator , a minimal yet extensible execution loop that repeatedly invokes the LLM, interprets its outputs, and coordinates tool use. Although conceptually simple, the orchestrator is engineered to support multi-step reasoning, long-term memory, and extension-based tool integrations. Its behavior can be summarized as in Algorithm 1.
The long-term memory module is described in detail in Section ˜ 2.3.2 , while the extension system is elaborated in Section ˜ 2.3.3 .

Algorithm 1: Confucius Orchestrator Loop 1: Initialize session context, memory, extensions 2: while iteration < max_iters <\texttt{max\_iters} do 3: Invoke LLM with system prompt + memory 4: Parse LLM output into actions 5: for all actions a a do 6: Route a a to its extension 7: Execute extension; update memory 8: if extension signals continuation then 9: add observations (results, error, etc.) to memory 10: continue 11: end if 12: end for 13: Check for completion; break if done 14: end while 15: return final output and artifacts

Output Processing.

The orchestrator supports two modes of interaction with the LLM. Models with native tool-use APIs (e.g., Claude 4) emit structured JSON tool calls that are routed directly to extension handlers. Models without native tool-use emit XML-style tags (e.g., <bash>...</bash> ), which the orchestrator parses into the same structured action format. This dual interface provides broad model compatibility while preserving reliability when advanced features are available.

Iteration Control.

Each orchestrator loop is bounded by a maximum iteration limit to prevent runaway execution, but termination is primarily agent-driven. At the start of every iteration, the orchestrator invokes the LLM and parses its output into structured actions. If the agent does not emit further actions, the orchestrator interprets this as a completion signal, and the loop terminates automatically.
Extensions may also explicitly request continuation: for example, after executing a shell command, the Bash extension raises an interrupt containing the command output, prompting the orchestrator to invoke the LLM again with updated memory. Together, these mechanisms allow the agent to control when to stop while still supporting multi-turn tool use, iterative refinement, and dynamic planning within safe iteration bounds.

2.3 Keys Features in Details

2.3.1 F1 : Context Management

Running agents on large-scale repositories quickly stresses even long-context LLMs: long debugging sessions, multi-file refactors, and nested tool calls all contribute to unbounded conversation growth. In many existing coding agent frameworks, agents either accumulate a single flat history (risking hard context limits and “forgotten” early decisions) or rely on naive truncation and ad-hoc retrieval, which can silently drop important information and are difficult to tune for different workloads.
The Confucius SDK addresses this by providing an explicit agent context management layer that combines hierarchical working memory with adaptive context compression.

At the SDK level, each instantiated agent is backed by a hierarchical working-memory with configurable visibility scopes (e.g., session, entry, runnable).
Below is an example of hierarchical memory for a SWE-Bench-Pro instance. The agent maintains this hierarchy throughout execution so that when context is pruned, important insights and intermediate artifacts can be stored and later retrieved efficiently:

+-- instance_qutebrowser__qutebrowser-c09e1439...
 +-- hierarchical_memory_3a7488c6-bf8c-11f0-8236-cfd9fd0d56b4
 +-- qutebrowser_process_cleanup
 |-- analysis.md
 |-- implementation_summary.md
 +-- todo.md

On top of this hierarchy, Confucius SDK integrates an adaptive context compression mechanism ( Figure ˜ 3 ) driven by a planner agent, the Architect . When the effective prompt length for a given analect approaches configurable thresholds, the Architect is invoked in a separate LLM call to analyze the conversation history and construct a structured summary that explicitly preserves key information categories (e.g., task goals, decisions made, open TODOs, and critical error traces). The system then replaces marked historical messages with this compressed summary, while maintaining a rolling window of recent messages in their original form. The summary is inserted as a new AI message, and all future turns will see both the compact summary and the recent raw history.

Our context management design provides two key benefits.
First, structured summarization triggered only when needed preserves semantically important information and maintains access to long reasoning chains, avoiding the brittleness of fixed-window truncation or simple retrieval.
Second, the hierarchical memory stores and refines key insights throughout execution, complementing the summaries and ensuring that important state persists even as the raw history is compressed.
In the Confucius Code Agent, these mechanisms are essential for handling long-running software engineering sessions on industrial-scale codebases, improving performance on long-context coding tasks without requiring changes to the underlying orchestrator or extensions. Similar context engineering techniques are also reported in recent production-level LLMs (Anthropic, 2025b ; OpenAI, 2025 ) , and we view CCA as a step toward consolidating these emerging practices into an open-sourced and extensible framework for long-horizon agent reasoning.

Figure 3 : Context compression overview. When the context window approaches configurable thresholds, the Architect agent summarizes earlier turns into a structured plan containing goals, decisions, errors, and open TODOs. These compressed summaries replace original large spans of history while preserving a short window of recent interactions, enabling the agent to sustain multi-step reasoning over long trajectories without exceeding context limits.

2.3.2 F2 : Note-Taking Agent

Flat chat logs are not an ideal representation for long-term memory: they are verbose and difficult to reuse without manually rereading entire transcripts. In typical frameworks, any cross-session “memory” is either absent or implemented via coarse-grained embeddings over whole turns, which tends to miss important structure such as architectures, design decisions, and failure modes. To support agents that improve over time and can pick up long-running projects where they left off, the Confucius SDK includes an explicit note-taking functionality that turns interaction traces into structured persistent knowledge.

At the SDK level, every interaction is logged into a structured session “trajectory”, including user messages, tool invocations, LLM outputs, and system events. A dedicated note-taking agent (an extra agent also built on the Confucius orchestrator) can distill these trajectories into compact notes without affecting the online latency of the primary agent. Persistent notes are stored as Markdown files in a file-system-like tree: each session has an associated directory, under which the note-taking agent can create paths such as project/architecture.md , research/findings.md , or solutions/bug_fix.md . Leaves in this hierarchy are Markdown documents with lightweight tags, maintained as typed memory nodes. The SDK exposes structured tools to search, read, write, edit, delete, and import these nodes, so notes can be programmatically updated and reused across sessions. Examples of notes are shown in Appendix 8 .

A distinctive aspect of the Confucius SDK’s note-taking is its emphasis on hindsight notes for failures. The note-taking layer encourages agents to record not only successful solutions but also compilation errors, runtime exceptions, and unproductive strategies, together with eventual resolutions or reasons for abandonment. Over time, this yields a corpus of failure cases indexed by error messages, stack traces, and affected components. When a similar failure appears in a future session, an agent can retrieve the corresponding hindsight note and immediately surface known fixes or workarounds, rather than rediscovering them from scratch. In the Confucius Code Agent, these mechanisms turn day-to-day usage on large codebases into a steadily growing, human-readable body of durable knowledge that improves continuity across sessions and reduces repeated “thrashing” on recurring issues; the same APIs are available to enterprise users who wish to endow their own Confucius-based agents with long-lived, interpretable memory.

2.3.3 F3 : Extensions

The Confucius Orchestrator ( Section ˜ 2.2 ) provides a minimal agent loop, but on its own it does not specify how to parse model outputs, invoke tools, or manage side effects. In many existing frameworks, these behaviors are wired together in ad-hoc Python code or model-specific prompting, which makes it difficult to (i) reuse behaviors across agents, (ii) audit or modify individual capabilities, and (iii) adapt to new tool stacks without rewriting the agent. The Confucius SDK addresses this by factoring most agent behaviors into extensions : modular components that attach to the orchestrator and participate in each iteration of the loop.

Concretely, an extension in the Confucius SDK is a typed configuration object that registers callbacks (e.g., on_input_messages , on_plain_text , on_tag , on_llm_output ). At each step of the orchestrator’s while-loop, these callbacks are invoked in a fixed order, with access to a shared run context that exposes the I/O interface, session-wide storage, hierarchical memory, and artifact store. This allows extensions to shape prompts before they reach the LLM, interpret model outputs (including XML-style tags or native tool calls), and inject or filter messages in the conversation history, while maintaining their own state. Within this interface, extensions cover perception, reasoning, and action. Perception extensions map raw model outputs into structured actions, such as the file-edit and command-line extensions that parse tagged spans, validate them, and route them through safe executors. Reasoning extensions (e.g., planning or “thinking” modules) rewrite or annotate messages prior to LLM invocation, adding format instructions or task decompositions without altering the user’s utterance. Action extensions execute tools—shell commands, file edits, function calls, or code search—and then persist results into memory or artifacts, returning summarized views back into the dialogue. For example, naive grep calls can be rewritten into scalable BigGrep queries, CLI commands are intercepted by per-command validators before execution, and prompt-caching extensions insert provider-specific cache-control metadata to reuse long prefixes and reduce latency and token cost.

By routing all tool use and prompt shaping through extensions, the Confucius SDK cleanly separates the core orchestration loop from agent capabilities. This yields several benefits. First, extensions can be composed and reused across agents: a planning extension or a guarded-shell extension can be attached to any orchestrator-based analect without modifying its core loop. Second, behaviors are easier to observe and ablate, since each extension has a narrow, well-defined contract and its callbacks are logged as part of the run context.

Extension system concretizes CCA from the Confucius SDK: the production CCA is not a separate, hard-coded system, but an orchestrator instantiated with a particular bundle of extensions (file-editing, CLI, code search, planning, prompt-caching, and others).
When we report tool-use ablations in Table ˜ 2 , what we vary is exactly which extensions are enabled or how they are configured, while the orchestrator loop is held fixed. As a result, any improvement discovered while iterating on CCA’s extensions (e.g., a more robust guarded-shell policy or a better file-edit parser) can be immediately reused by other agents built on the Confucius SDK simply by selecting the corresponding extensions.

Figure 4 : Meta-agent build–test–improve loop. The Meta-agent synthesizes agent configurations, wires together orchestrator components and extensions, evaluates candidate agents on representative tasks, and iteratively refines prompts and tool-use policies based on observed failures.

2.3.4 F4 : Meta-agent

A recurring limitation of existing agent frameworks is that agent behavior is largely static : humans hand-design prompts, tool wiring, and guardrails, then periodically revise them by trial and error. This is labor-intensive, does not scale with growing tool ecosystems, and makes it difficult to develop agents to new tool stacks and environments. Moreover, we find that naive implementations of file-editing or command-line tools—even when they are functionally correct—often underperform because the surrounding prompts and error-handling conventions are not tuned to realistic workloads. Confucius SDK addresses this by introducing a Meta Agent , an agent that automatically builds and refines other agents through an explicit build-test-improve loop, turning agent design itself into an agentic, evaluation-driven automatic process.

Within the Confucius SDK, the Meta-agent is implemented as an extra agent built on the Confucius Orchestrator that interactively constructs new agents from high-level specifications. A developer begins by describing, in natural language, what the target agent should do and under what constraints (e.g., “an agent that triages CI failures for our monorepo” or “a refactoring agent with read-only access to production configs”). The Meta-agent then generates a structured configuration form that asks for more concrete requirements: repository scope, latency or safety constraints, which existing extensions (file editing, Bash, code search, internal tools) to attach, and what evaluation tasks or test suites should be used. After the user confirms this specification, the Meta-agent automatically (i) synthesizes the agent’s configuration and prompts and (ii) wires in the selected extensions and memory policies.

Importantly, the Meta-agent also automates testing and debugging of the newly created agent. Using the same SDK runtime, it spins up the candidate agent locally, drives it on a suite of regression tasks (e.g., representative GitHub issues or internal tickets), and observes the agent’s outputs, logs, and tool traces. When failures or undesirable behaviors are detected—such as brittle tool selection, incorrect file-edit patterns, or poor recovery from compiler errors—the Meta Agent proposes concrete modifications to prompts, extension configurations, or even new tool wrappers. These patches are applied to the agent, and the test loop is rerun, yielding a “build-test-improve” process that incrementally improves the agent until target metrics are met. The same mechanism can be invoked not only to build new agents, but also to assist in designing and debugging new tools that plug into the extension layer.

This Meta-agent capability lives at the Confucius SDK level but directly benefits CCA. In fact, the production Confucius Code Agent proposed in this paper is itself the outcome of the Meta-agent’s build–improve–test loop: we start from a high-level description of a repository-level software engineering assistant, let the Meta-agent synthesize the orchestrator configuration, tool wiring, and prompts, and then repeatedly refine them against a production-grade test set until performance stabilizes. The resulting agent exhibits more reliable tool selection and recovery behaviors than our initial hand-written designs, and these improvements are reflected in the tool-use ablations reported in Section ˜ 3.3 . At the same time, the same Meta-agent interface allows enterprise users to rapidly spin up organization-specific agents (e.g., release-management or data-quality agents) using this automated iteration loop; extending this process to a broader family of specialized agents is an active direction for future work.

2.4 Agent Development Cycle

The Confucius SDK promotes an easy-to-use agent development cycle where the meta-agent assist in onboarding and refining other agents.
This iterative process of build-test-improve loop is further supported by a full suite of developer tools:

- •

Trace UI: fine-grained visualization of call stacks, tool interactions, and memory flows (see Section ˜ 10 );

- •

Playground: an interactive environment for prompt refinement and parameter tuning;

- •

Eval UI: built-in support for regression tests, A/B comparisons, and benchmark evaluations;

- •

Centralized agent management: a unified interface for developing, integrating, deploying, and monitoring agents at scale.

These tools ensure that the Confucius SDK is not just a research prototype, but a production-grade framework that facilitates agent developers and continuously improves with usage.

3 Experiments

3.1 Setup

Models and agent scaffold.

We use Claude 4 Sonnet, Claude 4.5 Sonnet, Claude 4.5 Opus as the primary backbone LLMs to ensure comparability with published baselines. We use SWE-Agent (Yang et al., 2024 ) as the baseline scaffold. Our CCA agent replaces the SWE-Agent orchestration stack with the Confucius Orchestrator.
We also report results from the Live-SWE-Agent (Xia et al., 2025 ) as baseline, while keeping the tool environment and repository setup identical.

Benchmark.

For main results, we evaluate CCA on the SWE-Bench-Pro (Deng et al., 2025 ) public split consisting of 731 tasks, following the identical environment configuration and infrastructure used by the SWE-Agent baseline (Yang et al., 2024 ) . We also report results from the SWE-Bench-Verified (Jimenez et al., 2023 ) consisting of 500 tasks to compare with existing open-sourced coding agents, including SWE-Agent and OpenHands (Wang et al., 2024 ) .

Metrics.

We follow the official SWE-Bench-Pro Resolve Rate metric, defined as the percentage of tasks for which the agent’s proposed patch successfully passes all repository-provided tests without human intervention. 1 1 1 https://scale.com/leaderboard/swe_bench_pro_public Each trial is repeated with different random seeds for trajectory sampling to account for stochasticity in tool invocation and LLM responses. We report mean Resolve@1 across three runs.

3.2 Main Results on SWE-Bench-Pro

Backbone Model Scaffold Resolve Rate (Pass@1)

Claude 4 Sonnet SWE-Agent (Yang et al., 2024 ) 42.7

CCA 45.5

Claude 4.5 Sonnet SWE-Agent 43.6

Live-SWE-Agent (Xia et al., 2025 ) 45.8

CCA 52.7

Claude 4.5 Opus Proprietary to Anthropic* 52.0

CCA 54.3 
Table 1 : SWE-Bench-Pro public split comparison across scaffolds and backbone models.
All methods share identical environments; improvements arise solely from the agent scaffolds.
(* Anthropic’s proprietary scaffold, from Claude Opus 4.5 System Card. 3 3 3 https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf )

Footnote ˜ 3 summarizes our main results on the SWE-Bench-Pro public split. Under identical environment and tool conditions, CCA consistently surpasses the SWE-Agent baseline across settings with different backbone models.
With Claude 4 Sonnet, CCA reaches Resolve@1 at 45.5% . With Claude 4.5 Sonnet, CCA reaches 52.7% , largely surpassing the best open-sourced agent, Live-SWE-Agent, at 45.8%.
And with Claude 4.5 Opus, CCA achieves 54.3% , outperforming results from Anthropic’s proprietary scaffold and establishing a new state-of-the-art score.
These improvements arise purely from stronger agentic scaffolding—enhanced orchestration, context management, and tool-use extensions—rather than differences in backbone models or evaluation setups.
More broadly, these results underscore the central role of scaffolding: even a weaker model equipped with a strong agent scaffold (Claude 4.5 Sonnet + CCA at 52.7% ) can outperform a stronger model (Claude 4.5 Opus + proprietary scaffold at 52.0% ). This highlights that agent scaffold—not only backbone model capability—is a decisive factor in real-world software engineering tasks.

Because Claude Code (CC) does not expose a programmatic tool interface compatible with containerized evaluation environments such as SWE-rex (SWE-agent, 2025 ) , we cannot compare CCA with CC’s results on SWE-Bench-Pro. Instead, to provide a qualitative comparison, we constructed a small curated benchmark (a mini PyTorch-Bench) and executed CC solutions using the Claude Code CLI directly on a host machine where CC is installed (i.e., outside a Docker-based runtime), as seen in Section ˜ 9 . These complementary experiments highlight behavioral differences between CC and CCA in realistic debugging and development tasks, but they are not directly comparable to SWE-Bench-Pro due to differences in execution environment and toolability.

3.3 Meta-Agent Learned Tool-Use

CCA’s tool-use behavior is not purely hand-engineered; instead, it is learned through the Meta-agent, which automatically refines how the agent invokes tools such as file editors and command-line utilities.
To measure the contribution of this learned tool-use stack, we perform an ablation that disables these Meta-agent–derived tools and instead reverts CCA to a simpler, “naive” tool-use pattern similar to traditional agent scaffolds. This naive mode lacks advanced learned features such as file editing and command-line operations. Table ˜ 2 reports the results of this ablation alongside a separate ablation on context management. Experiments are conducted on a 100-example subset of the SWE-Bench-Pro public set. As shown in the Claude 4.5 Sonnet rows, removing the learned tool-use features leads to a large decline in Resolve@1—even when context management is held constant. This confirms that tool-use conventions learned by the Meta-agent are a major driver of CCA’s performance, independent of (and complementary to) hierarchical working memory and context compression.

3.4 Long-context Reasoning

3.4.1 Context Management

To quantify the impact of hierarchical working memory and context compression, we evaluate CCA on the above-mentioned subset of SWE-Bench-Pro, where both variants (with and without context management) successfully produced executable solutions. Without any context control, many trajectories exceed model token limits and fail to complete, hence the restricted subset.
Results in Table ˜ 2 demonstrate a clear improvement in problem resolution when hierarchical memory and context compression are enabled. For Claude 4 Sonnet, advanced context management improves Resolve@1 from 42.0 42.0 to 48.6 48.6 on this subset (a +6.6 performance gain). On Claude 4.5, the improvement between the no-context-management and advanced variants is smaller, but both substantially outperform the simple tool-use configuration. Manual inspection further reveals that the planner agent frequently reduces prompt length by over 40 % 40\% without omitting key reasoning chains. The number of distinct planning iterations per trajectory also increases (mean of 2.7 2.7 vs. 1.4 1.4 without context management), indicating that hierarchical summarization encourages deeper multi-step reasoning rather than shallow single-pass edits. This supports the hypothesis that structured context compression not only prevents overflow but also improves reasoning quality by enforcing periodic consolidation of long-horizon plans.

Backbone Model Context Management Tool Use Resolve Rate (Pass@1)

Claude 4 Sonnet No advanced 42.0

Yes advanced 48.6

Claude 4.5 Sonnet No simple 44.0

No advanced 51.0

Yes advanced 51.6 
Table 2 : Ablation on hierarchical context management and tool-use sophistication. Results are obtained from evaluating CCA on a 100-example subset of the SWE-Bench-Pro public set.

3.4.2 Endless-Read Robustness

We further analyze CCA’s robustness under tasks that require editing multiple files. Each SWE-Bench-Pro task is grouped by the number of modified files (“edited-file bucket”), and we measure the Resolve Rate within each group. As shown in Table ˜ 3 , the agent maintains stable performance across varying edit volumes, with only moderate regression when more files are touched. The degradation likely stems from cumulative localization uncertainty and compounding diffs, suggesting future work on finer-grained diff validation and multi-file dependency tracking.

Edited Files Bucket Resolve Rate (Pass@1) Sample Count

1–2 files 57.8 294

3–4 files 49.2 203

5–6 files 44.1 86

7–10 files 52.6 38

10+ files 44.4 18 
Table 3 : CCA’s resolve rate on SWE-Bench-Pro as a function of the number of files modified.
Performance remains robust even for multi-file refactoring scenarios.

Overall, these results show that CCA’s hierarchical memory and context compression yield substantial gains in both efficiency and robustness for long-context reasoning.

3.5 Long-term Memory

We next study CCA’s note-taking module, designed to accumulate durable cross-session memory. Unlike transient hierarchical working memory, the note-taking agent asynchronously summarizes each session into structured Markdown notes, which capture both successful strategies and failure cases. This persistent “memory” is then available for retrieval in subsequent tasks, supporting test-time self-improvement.

Since no public benchmark explicitly evaluates memory in coding agents, we assess CCA’s memory module by running it on two consecutive passes, i.e., with memory maintained, of SWE-Bench-Pro instances. During the first run, the NoteTaker agent analyzes each trajectory and produces persistent notes for 151 instances—skipping cases where no meaningful insight can be distilled. We then rerun exactly these 151 tasks, providing CCA with the corresponding note directory to measure how prior experience improves efficiency and solution quality.

- 1.

Run 1: Execute the task from scratch (no context editing either); use note taker agent to write down notes.

- 2.

Run 2: Pass the notes from Run 1 to CCA and rerun.

Trial Avg. Turns Avg. Token Cost Resolve Rate (Pass@1)

Run 1 (from scratch) 64 104k 53.0

Run 2 (using notes) 61 (-3) 93k (-11k) 54.4 (+1.4) 
Table 4 : CCA performance across repeated runs using notes. Token cost excludes system prompt tokens; the underlying model is Claude 4.5 Sonnet.

Cumulative note-taking reduces the iteration turns (from 64 to 61) and the token cost (from 104 104 k to 93 93 k), and also yield improvements on resolve rate (from 53% to 54.4%). These gains indicate that the notes distilled in the first run capture actionable, reusable knowledge. In effect, the note-taking system provides CCA with a lightweight form of cross-session learning , enabling more efficient reasoning and more reliable patch generation in subsequent attempts. A detailed example of the notes produced by the note-taking agent is provided in Appendix 8 .

3.6 Comparison with Open-Sourced Scaffolds on SWE-Bench-Verified

We further conduct evaluations on the SWE-Bench-Verified benchmark (Jimenez et al., 2023 ) to compare CCA against existing open-source scaffolds. 4 4 4 As of Dec 2025, OpenHands remains the strongest open-sourced coding agent on SWE-Bench-Verified, reported from SWE-Bench’s official leaderboard. Using Claude 4 Sonnet, CCA achieves a Resolve Rate of 74.6% , exceeding the strongest open-source system (OpenHands) under identical backbone conditions and outperforming a mini-SWE-Agent variant that relies on the more capable Claude 4.5 Sonnet model. These results reinforce the central role of agentic scaffolding: improved orchestration, memory handling, and tool-use abstractions can close—or even surpass—the gap introduced by differences in backbone model capability. We also observe that SWE-Bench-Verified is unusually sensitive to Claude’s internal thinking budget; a detailed analysis appears in Appendix 7 .

Backbone Model Scaffold Resolve Rate (Pass@1)

Claude 4 Sonnet SWE-Agent 66.6

OpenHands 72.8

CCA 74.6

Claude 4.5 Sonnet mini-SWE-Agent 70.6 
Table 5 : CCA performance on SWE-Bench-Verified. CCA matches the best open-source framework (OpenHands) under the same Claude 4 Sonnet backbone, and outperforms a mini-SWE-Agent variant even when that variant uses a stronger Claude 4.5 Sonnet backbone.

4 Related Work

4.1 Large-scale Software Engineering

Modern software engineering at scale has driven interest in AI assistance that can handle massive codebases and performance-critical systems. Potvin and Levenberg’s seminal description of Google’s single vast code repository illustrates the challenges and benefits of the monorepo model (Potvin and Levenberg, 2016 ) . This approach centralizes billions of lines of code, enabling unified tooling and refactoring, but it demands automated support for code discovery, understanding, and consistent changes at scale. Recent LLM-based systems are beginning to tackle such issues. For instance, Lin et al. introduce ECO, an LLM-driven code optimizer designed for warehouse-scale computers (Lin et al., 2025 ) . ECO leverages a code-generating model to suggest performance improvements in large distributed software, aiming to reduce runtime and resource usage while preserving correctness. Results show that AI-powered optimization can uncover non-trivial efficiency gains in complex systems, hinting at a future where coding agents assist not only in writing code but also in optimizing and maintaining it across ultra-large codebases. The combination of monorepo development and LLM-based tools like ECO underscores a trend toward holistic scale: treating an entire organization’s code as a single evolvable system, with AI agents providing the intelligence to manage global changes, dependency analysis, and performance tuning in ways humans alone could not easily scale. This context also motivates advanced context management techniques: instead of feeding billions of lines directly into an LLM, agents must learn to retrieve and focus on the relevant project fragments, a theme that connects to memory and tool-use innovations discussed later.

4.2 Agents for Software Engineering

Benchmarking Coding Agents.

The past two years have seen the emergence of comprehensive benchmarks to evaluate autonomous code-writing and code-fixing agents on realistic tasks. One prominent example is SWE-Bench (Jimenez et al., 2023 ) , which poses real-world GitHub issues and provides the full repository context; an agent succeeds by producing a patch that passes all project tests.
It has since evolved into a family of benchmarks targeting different scenarios: for instance, variants like SWE-Bench-Multilingual (Yang et al., 2025b ) and SWE-Bench-Multimodal (Yang et al., 2025a ) extend the evaluation to codebases with multiple programming languages and to tasks that involve not only code but other modalities (such as modifying documentation or configurations), respectively. An expanded challenge, SWE-Bench Pro (Deng et al., 2025 ) , was released to assess long-horizon problem solving: it includes complex, enterprise-level issues that may require dozens of files to be modified across a codebase. These benchmarks have become a driving force for the community, with public leaderboards spurring rapid progress. Beyond bug-fixing, entirely new benchmarks are probing other dimensions of software work. SWE-fficiency (Ma et al., 2025 ) is a recent benchmark that challenges agents to optimize the runtime performance of real codebases given defined workloads.

Autonomous Coding Agent Architectures.

In response to these benchmarks, a variety of agent designs have been proposed to improve the capabilities of LLM-based software engineers.
A starting point for modern autonomous software engineering systems is SWE-Agent (Yang et al., 2024 ) , which first demonstrated that an LLM augmented with a small set of tools—file editing, command execution, and testing—can repeatedly interact with a real repository to resolve GitHub issues. Follow-up work has steadily refined SWE-Agent’s design. For example, Live-SWE-Agent (Xia et al., 2025 ) asked whether an agent can self-evolve during inference. By monitoring its own partial progress, Live-SWE-Agent adjusts strategies and occasionally updates its own prompt, tools, or configuration mid-run.
Satori-SWE (Zeng et al., 2025 ) proposes an evolutionary approach at test time: instead of one monolithic agent, it runs a population of agent instances or solution candidates and evolves them to increasingly better solutions. Satori-SWE’s evolutionary scaling showed improved sample efficiency, meaning an agent could reach a correct answer with fewer attempts by systematically refining partial solutions, effectively implementing a build-test-improve loop at the meta-level of agent behavior. On the opposite end of the spectrum, some researchers argue that increasing agent complexity is not the only path to better performance. Agentless (Xia et al., 2024 ) is a framework that binds the traditional agent loop altogether. Instead of having the LLM decide among many tools and steps, Agentless breaks the problem into a fixed three-phase pipeline managed externally, avoiding the open-ended search that autonomous agents perform and achieving state-of-the-art results on the SWE-Bench Lite subset.
In addition to academic prototypes, community-driven platforms have played a role in advancing SWE agents. OpenHands (Wang et al., 2024 ) is one such open-source toolkit, providing a unified framework for building coding agents. It offers a standard API for file I/O, code execution, and version control operations, and implements a ReAct-style planner on top of popular base models. By open-sourcing these components, OpenHands lowers the barrier to entry for researchers and companies to create their own AI dev assistants, and has amassed a large user base.

Training LLMs for Software Engineering.

SWE-Gym (Pan et al., 2024 ) provides the first publicly available executable environment tailored for real-world software engineering tasks: it bundles complete Python repositories with dependencies, unit tests, and realistic issue descriptions, enabling agents to propose patches which can be validated via execution. Later, SWE-Smith (Yang et al., 2025b ) generalizes the idea: given any Python repository, it automatically generates hundreds to thousands of new bug-fix or issue-resolution tasks by perturbing code or simulating realistic faults, producing a dataset of around 50,000 instances across 128 GitHub projects. Training on this large-scale synthetic data significantly improves agent performance on benchmark tasks, indicating that domain-specific, execution-aware fine-tuning is critical for bringing coding agents closer to real-world software engineering demands.
Recent research have explored reinforcement learning for code agents. SWE-RL (Wei et al., 2025 ) takes advantage of the abundant software evolution data in open-source repositories – commit histories, diff patches, and issue resolutions – and uses these as implicit demonstrations to fine-tune an LLM via RL. The insight is that by learning from how human developers iteratively improve code over many commits, an agent can internalize more realistic problem-solving trajectories. Results from SWE-RL show improved reasoning and success rates on long-horizon software tasks, as the RL-trained model learns to recover intermediate reasoning steps (e.g. the decision to run tests or check certain files) that are often needed for complex bug fixes.

5 Future Work — Toward an End-to-End Reinforcement Learning Framework for Agentic Software Engineering

Recent advances suggest that reinforcement learning (RL) can substantially enhance LLM-based software engineering agents beyond what is achievable with supervised fine-tuning alone. For example, SWE-RL (Wei et al., 2025 ) demonstrates meaningful gains through end-to-end RL with verifiable rewards, while frameworks such as Agent Lightning (Luo et al., 2025 ) highlight a crucial architectural insight: by viewing agent execution as a Markov Decision Process, RL training can be decoupled from agent implementation via unified trajectory interfaces.

This decoupled perspective aligns naturally with the design philosophy behind CCA. The Agent Experience (AX) framework already structures an agent’s internal reasoning traces in a trajectory-friendly format, making them directly suitable for RL training. Moreover, CCA’s Meta-agent produces rich, fine-grained feedback signals from both tool extensions and environment interactions—signals that can be transformed into diverse reward functions for outcome-based, process-based, or hybrid supervision. Examples include rewards tied to note-taking quality, tool-use robustness, recovery behaviors, or the efficiency of multi-step exploration.

In addition, the extensibility of the Confucius Orchestrator provides a natural substrate for curriculum design in RL. Developers can introduce progressively richer toolsets, varied execution environments (e.g., shell, file editing, SQL databases), and increasingly complex tasks, enabling models to acquire generalizable agentic capabilities rather than overfitting to specific tool behaviors. This opens the door to RL-driven improvement not only of individual policies, but of the broader agent stack itself.

We envision CCA evolving into both a production-grade SDK for agent builders and a scalable trajectory collection and experimentation layer for end-to-end RL on foundation models. Future work includes formalizing trajectory export formats, designing principled reward extraction protocols, and supporting online or hybrid policy-update mechanisms that operate seamlessly within the Confucius agentic ecosystem.

6 Conclusion

We introduced the Confucius Code Agent (CCA) , a fully open-sourced, production-grade framework for building AI software engineers capable of operating on industrial-scale codebases. CCA is instantiated atop the Confucius SDK that explicitly separates and optimizes for Agent Experience (AX) , User Experience (UX) , and Developer Experience (DX) , enabling robust multi-step reasoning, modular tool use, structured memory management, and interpretable execution traces.
CCA achieves strong performance across public benchmarks and real-world engineering scenarios, demonstrating that agentic scaffolding —the orchestration, memory structures, and tool abstractions surrounding the model—can outweigh raw model scale. The SDK’s hierarchical working memory, adaptive context compression, and persistent note-taking provide durable reasoning stability over long horizons, while its extension system and meta-agent enable rapid adaptation to new environments, tools, and organization-specific workflows.

More broadly, CCA establishes a transparent and reproducible foundation for AI software engineering research. Its modular architecture invites experimentation: from studying long-context reasoning and continual memory, to exploring test-time adaptation, to integrating reinforcement learning with structured trajectory traces. We hope this release accelerates progress toward AI developers that are powerful, interpretable, safe to deploy, and continuously improving—bridging the persistent gap between research prototypes and the demands of real-world software engineering.

References

- Anthropic (2025a) Anthropic. Claude code, 2025a. https://code.claude.com/ . AI-powered agentic coding assistant.

- Anthropic (2025b) Anthropic. Effective context engineering for ai agents, 2025b. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents . Accessed: 2025-12-10.

- Austin et al. (2021) Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732 , 2021.

- Chen et al. (2021) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating Large Language Models Trained on Code. arXiv e-prints , art. arXiv:2107.03374, July 2021. 10.48550/arXiv.2107.03374 .

- Cursor (2025) Cursor. Cursor, 2025. https://www.cursor.com/ . AI-powered code editor.

- Deng et al. (2025) Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, et al. Swe-bench pro: Can ai agents solve long-horizon software engineering tasks? arXiv preprint arXiv:2509.16941 , 2025.

- Gu et al. (2024) Alex Gu, Baptiste Rozière, Hugh Leather, Armando Solar-Lezama, Gabriel Synnaeve, and Sida I Wang. Cruxeval: A benchmark for code reasoning, understanding and execution. arXiv preprint arXiv:2401.03065 , 2024.

- Han et al. (2025) Tingxu Han, Zhenting Wang, Chunrong Fang, Shiyu Zhao, Shiqing Ma, and Zhenyu Chen. Token-budget-aware llm reasoning. In Findings of the Association for Computational Linguistics: ACL 2025 , pages 24842–24855, 2025.

- Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. arXiv preprint arXiv:2403.07974 , 2024.

- Jimenez et al. (2023) Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. Swe-bench: Can language models resolve real-world github issues? arXiv preprint arXiv:2310.06770 , 2023.

- Lai et al. (2023) Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettlemoyer, Wen-tau Yih, Daniel Fried, Sida Wang, and Tao Yu. Ds-1000: A natural and reliable benchmark for data science code generation. In International Conference on Machine Learning , pages 18319–18345. PMLR, 2023.

- Li et al. (2025) Junyan Li, Wenshuo Zhao, Yang Zhang, and Chuang Gan. Steering llm thinking with budget guidance. arXiv preprint arXiv:2506.13752 , 2025.

- Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. Competition-level code generation with alphacode. Science , 378(6624):1092–1097, 2022.

- Lin et al. (2025) Hannah Lin, Martin Maas, Maximilian Roquemore, Arman Hasanzadeh, Fred Lewis, Yusuf Simonson, Tzu-Wei Yang, Amir Yazdanbakhsh, Deniz Altinbüken, Florin Papa, et al. Eco: An llm-driven efficient code optimizer for warehouse scale computers. arXiv preprint arXiv:2503.15669 , 2025.

- Luo et al. (2025) Xufang Luo, Yuge Zhang, Zhiyuan He, Zilong Wang, Siyun Zhao, Dongsheng Li, Luna K. Qiu, and Yuqing Yang. Agent lightning: Train any ai agents with reinforcement learning, 2025. https://arxiv.org/abs/2508.03680 .

- Ma et al. (2025) Jeffrey Jian Ma, Milad Hashemi, Amir Yazdanbakhsh, Kevin Swersky, Ofir Press, Enhui Li, Vijay Janapa Reddi, and Parthasarathy Ranganathan. Swe-fficiency: Can language models optimize real-world repositories on real workloads? arXiv preprint arXiv:2511.06090 , 2025.

- OpenAI (2025) OpenAI. Session memory in the openai agents sdk, 2025. https://cookbook.openai.com/examples/agents_sdk/session_memory . Accessed: 2025-12-10.

- Pan et al. (2024) Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep Jaitly, Heng Ji, Alane Suhr, and Yizhe Zhang. Training software engineering agents and verifiers with swe-gym. arXiv preprint arXiv:2412.21139 , 2024.

- Potvin and Levenberg (2016) Rachel Potvin and Josh Levenberg. Why google stores billions of lines of code in a single repository. Communications of the ACM , 59:78–87, 2016. http://dl.acm.org/citation.cfm?id=2854146 .

- PyTorch (2025) PyTorch. Pytorch, 2025. https://github.com/pytorch/pytorch . Open-source deep learning library.

- SWE-agent (2025) SWE-agent. Swe-rex: A framework for swe-agent docker-based execution. https://github.com/SWE-agent/SWE-ReX , 2025. [Online; accessed 10-December-2025].

- Wang et al. (2024) Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, et al. Openhands: An open platform for ai software developers as generalist agents. arXiv preprint arXiv:2407.16741 , 2024.

- Wei et al. (2025) Yuxiang Wei, Olivier Duchenne, Jade Copet, Quentin Carbonneaux, Lingming Zhang, Daniel Fried, Gabriel Synnaeve, Rishabh Singh, and Sida I Wang. Swe-rl: Advancing llm reasoning via reinforcement learning on open software evolution. arXiv preprint arXiv:2502.18449 , 2025.

- Wen et al. (2025) Hao Wen, Xinrui Wu, Yi Sun, Feifei Zhang, Liye Chen, Jie Wang, Yunxin Liu, Yunhao Liu, Ya-Qin Zhang, and Yuanchun Li. Budgetthinker: Empowering budget-aware llm reasoning with control tokens. arXiv preprint arXiv:2508.17196 , 2025.

- Xia et al. (2024) Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. Agentless: Demystifying llm-based software engineering agents. arXiv preprint arXiv:2407.01489 , 2024.

- Xia et al. (2025) Chunqiu Steven Xia, Zhe Wang, Yan Yang, Yuxiang Wei, and Lingming Zhang. Live-swe-agent: Can software engineering agents self-evolve on the fly? arXiv preprint arXiv:2511.13646 , 2025.

- Yang et al. (2024) John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. Swe-agent: Agent-computer interfaces enable automated software engineering. Advances in Neural Information Processing Systems , 37:50528–50652, 2024.

- Yang et al. (2025a) John Yang, Carlos E Jimenez, Alex L Zhang, Kilian Lieret, Joyce Yang, Xindi Wu, Ori Press, Niklas Muennighoff, Gabriel Synnaeve, Karthik R Narasimhan, Diyi Yang, Sida Wang, and Ofir Press. Swe-bench multimodal: Do ai systems generalize to visual software domains? In The Thirteenth International Conference on Learning Representations , 2025a. https://openreview.net/forum?id=riTiq3i21b .

- Yang et al. (2025b) John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, and Diyi Yang. Swe-smith: Scaling data for software engineering agents, 2025b. https://arxiv.org/abs/2504.21798 .

- Zeng et al. (2025) Guangtao Zeng, Maohao Shen, Delin Chen, Zhenting Qi, Subhro Das, Dan Gutfreund, David Cox, Gregory Wornell, Wei Lu, Zhang-Wei Hong, et al. Satori-swe: Evolutionary test-time scaling for sample-efficient software engineering. arXiv preprint arXiv:2505.23604 , 2025.

- Zhao et al. (2025) Songwen Zhao, Danqing Wang, Kexun Zhang, Jiaxuan Luo, Zhuo Li, and Lei Li. Is vibe coding safe? benchmarking vulnerability of agent-generated code in real-world tasks. arXiv preprint arXiv:2512.03262 , 2025.

\beginappendix

7 Thinking Budget Scaling on SWE-bench-Verified

We define the thinking budget as the maximum number of reasoning or chain-of-thought “thinking” tokens that the LLM is permitted to generate before producing a response. Recent work shows that reasoning length can be controlled by prompting or internal budget-aware mechanisms. At inference time, the model can be guided either by: (i) prompt instructions like “use at most X X tokens of reasoning” Han et al. ( 2025 ) ; (ii) control tokens inserted periodically that signal remaining budget to the model during generation Wen et al. ( 2025 ) ; or (iii) a predictor estimating task complexity and adjusting budget dynamically Li et al. ( 2025 ) .

Anthropic’s Claude model series expose a thinkingBudget parameter at inference time to directly cap the reasoning tokens. We run our CCA agent using Claude 4 Sonnet with identical setup except varying its thinking budget in three settings: 8 8 k, 16 16 k, and 32 32 k tokens. We record Resolve Rate on the SWE-Bench-Pro public split.

Thinking Budget Resolve Rate (Pass@1)

8k 67.3

16k 68.4

32k 68.7 
Table 6 : CCA Resolve Rate as a function of thinking budget on SWE-Bench-Pro.

We observe diminishing returns beyond 16 16 k thinking tokens. Note that the thinkingBudget parameter cannot precisely control the internal thinking trace length of the Claude model, and that during inference, Claude only returns a summarized version of the reasoning without exposing full traces. As a result, we do not have the exact scaling curve of Resolve Rate with respect to the true thinking length on SWE-Bench-Pro.

8 Example Notes

Here is an example structured note hierarchy generated by Note Taker Agent for SWE-bench-Pro instance: instance_internetarchive__openlibrary-f343c08f89c772f7ba6c0246f384b9e6c3dc0add-v08d8e8889ec945ab 821fb156c04c7d2e2810debb .

.
+-- projects
| +-- openlibrary
| +-- escaping_wildcards_in_infobase_queries.md
| +-- multi_stage_author_matching_pipeline.md
| +-- year_based_author_matching_strategy.md
+-- README.md
+-- shared
 +-- python
 | +-- dict_copy_forgotten_field_update.md
 +-- string_manipulation
 +-- prefix_removal_empty_string_edge_case.md

The note is well organized into "shared" (ONLY for truly generic insights that apply across MANY projects) and "project" (For project-specific knowledge that primarily applies to ONE specific domain). The README.md summarized all the notes md files and provide instructions on how to navigate them. Here are some insights from "escaping_wildcards_in_infobase_queries.md"

---
id: escaping_wildcards_in_infobase_queries
title: Escaping Wildcards in Infobase Queries
description: How to handle asterisk characters in \\
Infobase queries to prevent unintended wildcard matching
keywords:
 - infobase
 - queries
 - wildcards
 - escaping
 - openlibrary
---

# Escaping Wildcards in Infobase Queries

## Problem Context

When searching for authors by name in OpenLibrary’s Infobase, asterisk characters
(‘*‘) in author names can cause unexpected behavior because they are treated as
wildcards by the query system. For example, searching for an author named "John*"
would match "John Smith", "Johnny", etc., rather than the literal name "John*".

## The Solution

Escape asterisks in name fields using a backslash when performing exact or alternate
name matches, but **intentionally preserve wildcards for surname matching queries**.

### Code Example

‘‘‘python
# In find_author() function:

# Escape asterisks for exact name matching
escaped_name = author["name"].replace("*", r"\*")

queries = [
 # Use escaped name for exact match
 {"type": "/type/author", "name˜": escaped_name},
 # Use escaped name for alternate names
 {"type": "/type/author", "alternate_names˜": escaped_name},
]

# For surname matching, intentionally use wildcards
if birth_year and death_year:
 surname = author[’name’].split()[-1]
 queries.append({
 "type": "/type/author",
 "name˜": f"* {surname}", # Wildcard intentional here
 "birth_date˜": f"*{birth_year}*",
 "death_date˜": f"*{death_year}*",
 })
‘‘‘

## Key Insights

1. **Context-Dependent Escaping**: Wildcards need to be escaped in some query contexts
(exact/alternate name matching) but preserved in others (surname matching).

2. **Backslash Escaping**: In Infobase queries, use ‘r"\*"‘ to escape asterisks. The
raw string ‘r‘ prefix prevents Python from interpreting the backslash.

3. **Query Order Matters**: The queries are tried in sequence. Exact matches (with
escaped wildcards) are tried first, then alternate names, then surname matching (with
intentional wildcards).

4. **Creating New Records**: When no match is found and a new author record must be
created, preserve the original name including any asterisks exactly as provided -
don’t use the escaped version.

## Related Files

- ‘/app/openlibrary/catalog/add_book/load_book.py‘ - ‘find_author()‘ function
- ‘/app/openlibrary/catalog/add_book/tests/test_load_book.py‘ - Tests for wildcard
behavior

These insights saves the agent a lot of effort to rediscover the issue in Run 2.
Here are the insights from prefix_removal_empty_string_edge_case.md

---
id: prefix_removal_empty_string_edge_case
title: Prefix Removal Empty String Edge Case
description: How to handle the edge case where removing a prefix leaves an empty string
keywords:
 - string
 - manipulation
 - edge
 - case
 - prefix
 - validation
---

# Prefix Removal Empty String Edge Case

## Problem

When removing a prefix from a string, you may end up with an empty string if the input
consists only of the prefix. This can cause unexpected behavior if downstream code
doesn’t handle empty strings properly.

### Example Scenario

In OpenLibrary’s honorific removal function, names like "Mr." or "Dr." consist
entirely of an honorific:

‘‘‘python
def remove_author_honorifics(author: dict[str, Any]) -> dict[str, Any]:
 raw_name: str = author["name"]

if honorific := find_matching_honorific(raw_name):
 author["name"] = raw_name[len(honorific):].lstrip()
 return author
‘‘‘

**Problem**: If ‘raw_name = "Mr."‘ and we remove "mr.", we get an empty string ‘""‘,
which can cause issues in database queries or display logic.

## The Solution

Check if the result is empty after removing the prefix, and if so, return the original value unchanged:

‘‘‘python
def remove_author_honorifics(author: dict[str, Any]) -> dict[str, Any]:
 """Remove honorifics from an author’s name field."""
 raw_name: str = author["name"]

# Check for exceptions first (e.g., "Dr. Seuss")
 if raw_name.casefold() in HONORIFC_NAME_EXECPTIONS:
 return author

if honorific := next(
 (
 honorific
 for honorific in HONORIFICS
 if raw_name.casefold().startswith(honorific)
 ),
 None,
 ):
 new_name = raw_name[len(honorific):].lstrip()
 # If the name is only an honorific, return unchanged
 if not new_name:
 return author
 author["name"] = new_name
 return author
‘‘‘

## Key Insights

1. **Check Before Assignment**: Store the result in a temporary variable and validate
it before assigning to the final location.

2. **Preserve Original on Invalid Result**: When validation fails (empty string),
return the original input unchanged rather than the invalid result.

3. **Common in Text Processing**: This pattern applies to any string manipulation
where you’re removing parts of the string:
 - Removing file extensions
 - Removing URL protocols
 - Stripping whitespace/punctuation
 - Removing prefixes/suffixes

This documents a concrete edge case when solving the instance; this not only save the agent tokens in Run 2, but also avoid runs where in consecutive runs such edge cases could be missed hence fail the case.

9 Case Studies: Comparison with Claude Code

In addition to standardized benchmarks, we conducted a controlled experiment using real GitHub issues from the PyTorch repository. These issues not only exemplify the complex challenges encountered in real-world production but also require deep domain specialist expertise. Hence, these issues reflect agent’s robustness and generalization under specialist software engineering scenarios. Our experiment holds the model capabilities constant while varying only the agent framework. We compare CCA with Claude Code (CC) , a command-line tool developed by Anthropic that enables direct interaction with Claude models for coding tasks. Both frameworks utilize identical Claude Sonnet 4.5 models in environments with equivalent codebases and access to file manipulation, bash tools, and NVIDIA A100 80GB GPU resources. To compare the solution between CC and CCA, we have enlisted a few experts in this field to judge and compare the solutions created by the 2 agents.

9.1 PyTorch-Bench

To construct PyTorch-Bench, we scanned GitHub issues on the open-source PyTorch repository (PyTorch, 2025 ) from Jan 2025 to Jul 2025. We selected 8 issues that are reproducible on an NVIDIA A100 80 GB GPU and that provide actionable structure, including a detailed description, a reproduction script, and instructions for replication of the issue. Both agents receive the same system prompt, which instructs them to start from a clean commit, attempt to reproduce the issue first, stop if reproduction fails in the current environment, and verify any proposed fix. We show an example task below and discuss it in more detail in the following sections.

Issue: RuntimeError: Expected curr_block->next == nullptr to be true, when I call setSegmentStateToCheckpoint. (#161356)
URL: https://github.com/pytorch/pytorch/issues/161356

### Describe the bug

Hello, when I was using checkpoint state to implement shared output memory for two cudagraphs, an assert ERROR occurred:
curr_block->next == nullptr, in function setSegmentStateToCheckpoint.

‘‘‘
# PyTorch version: 2.6.0+cu124

torch._C._cuda_setCheckpointPoolState(com_device, small_state, [], output1_new_storage)
RuntimeError: Expected curr_block->next == nullptr to be true, but got false.
(Could this error message be improved? If so, please report an enhancement request to PyTorch.)
’’’

**This error only appears only when I set env ‘export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True‘.
If I unset this env, the following case code executes successfully.**

This is my test code:
‘‘‘
import gc
import torch
print(f"torch version is: {torch.__version__}.")
stream0 = torch.cuda.Stream()
torch.cuda.set_stream(stream0)

def tensor_metadata(x):
 return {
 "nbytes": x.untyped_storage().nbytes(),
 "data_ptr": x.untyped_storage().data_ptr(),
 "size": x.shape,
 "stride": x.stride(),
 "dtype": x.dtype,
 "device": x.device,
 "storage_offset": x.storage_offset(),}

def reconstruct_from_tensor_metadata(metadata):
 s = torch._C._construct_storage_from_data_pointer(
 metadata["data_ptr"], metadata["device"], metadata["nbytes"])
 t = torch.empty([0], device=metadata["device"], dtype=metadata["dtype"])
 t.set_(source=s, storage_offset=metadata["storage_offset"],
 size=metadata["size"], stride=metadata["stride"], )
 return t

def print_mem_stats(name):
 segments = torch.cuda.memory_snapshot()
 seg = []
 for segment in segments:
 if "segment_pool_id" in segment:
 tmp = ({"stream": segment["stream"]},
 {"pool_id": segment["segment_pool_id"]},
 {"block_num": len(segment["blocks"])},
 {"activate_num": sum(int(blk["state"] == "active_allocated") for blk in segment["blocks"])},
 {"total_size": segment["total_size"]},
 {"allocated_size": segment["allocated_size"]},)
 seg.append(tmp)
 seg_str = "\n".join([str(seg_iter) for seg_iter in seg])
 seg_str = ’\n’ + seg_str
 print(f"{name}, snapshot: {seg_str}")

def cudagraphify(fn, inputs, pool, stream):
 torch.cuda.synchronize()
 gc.collect()
 torch.cuda.empty_cache()

graph = torch.cuda.CUDAGraph()
 with torch.cuda.graph(graph, stream=stream, pool=pool):
 static_outputs = fn(*inputs)
 return graph, static_outputs

def foo(x, idx):
 r1 = x.expand([1, 2097152 // 8]).sqrt()
 r2 = x.expand([idx, 2097152]).clone()
 return (r1, r2)

# init
pool_id = torch.cuda.graph_pool_handle()
com_stream = torch.cuda.Stream()
com_device = torch.cuda.current_device()
inp = torch.tensor([7], device=com_device)

# record original state
with torch.cuda.stream(com_stream):
 g = torch.cuda.CUDAGraph()
 g.capture_begin(pool=pool_id)
 g.capture_end()
original_mem_state = torch._C._cuda_getCheckpointState(com_device, pool_id)

# start capture graph1
graph1, outputs1 = cudagraphify(foo, [inp, 1], pool=pool_id, stream=com_stream)
small_state = torch._C._cuda_getCheckpointState(com_device, pool_id)
print_mem_stats("\n-----------------after_small_state_run_g0_step0 ")
output1_metadata = [tensor_metadata(t) for t in outputs1]
outputs1 = None

# set to original state and capture graph2
torch._C._cuda_setCheckpointPoolState(com_device, original_mem_state, [], [])
print_mem_stats("\n-----------------after_set_origin_state ")
graph2, outputs2 = cudagraphify(foo, [inp, 2], pool=pool_id, stream=com_stream)
biiig_state = torch._C._cuda_getCheckpointState(com_device, pool_id)
print_mem_stats("\n-----------------after_biiig_state_run_g1_step0 ")
output2_storage = [output.untyped_storage()._cdata for output in outputs2]

# set to original state and replay graph1
torch._C._cuda_setCheckpointPoolState(com_device, original_mem_state, output2_storage, [])
print_mem_stats("\n-----------------after_set_origin_state ")
graph1.replay()
reconstructed_tensors1 = [reconstruct_from_tensor_metadata(metadata) for metadata in output1_metadata]
output1_new_storage = [output.untyped_storage()._cdata for output in reconstructed_tensors1]
torch._C._cuda_setCheckpointPoolState(com_device, small_state, [], output1_new_storage)
print_mem_stats("\n-----------------after_small_state_run_g0_step1 ")
‘‘‘

After analyzing the error, the logic of the assertion seems to be: when allocing a new memory block, the last block must be an unmapped
nullptr block. Therefore, when setting to the recorded CheckpointState, the last block should also be unmapped nullptr block.

Why does it fail only when enabling expandable_segments? It seems that after enabling expandable_segments, the reserved memory blocks
will be merged. Therefore, when allocing a small block, releasing this small block, and then allocing a large block again, the total reserved
memory size increases. So, when setting to the state of a small memory block again, it triggers this assert error.

Could you please help check if these failed validations are always necessary? And how the current checkpoint memory management interface
can solve the above problems when expandable_segments is enabled? Thanks a lot.

### Versions

Collecting environment information...
PyTorch version: 2.6.0+cu124
Is debug build: False
CUDA used to build PyTorch: 12.4
ROCM used to build PyTorch: N/A

OS: Ubuntu 20.04.6 LTS (x86_64)
GCC version: (Ubuntu 9.4.0-1ubuntu1˜20.04.3) 9.4.0
Clang version: Could not collect
CMake version: version 3.16.3
Libc version: glibc-2.31

Python version: 3.11.4 (main, Jul 5 2023, 13:45:01) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.15.0-72-generic-x86_64-with-glibc2.31
Is CUDA available: True
CUDA runtime version: 12.9.41
CUDA_MODULE_LOADING set to: LAZY
GPU models and configuration:
GPU 0: NVIDIA A100-SXM4-80GB
GPU 1: NVIDIA A100-SXM4-80GB
GPU 2: NVIDIA A100-SXM4-80GB
GPU 3: NVIDIA A100-SXM4-80GB
GPU 4: NVIDIA A100-SXM4-80GB
GPU 5: NVIDIA A100-SXM4-80GB
GPU 6: NVIDIA A100-SXM4-80GB
GPU 7: NVIDIA A100-SXM4-80GB

Nvidia driver version: 575.51.03
cuDNN version: Could not collect
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

9.2 Issues and Comparative Solutions

We present three representative cases that demonstrate divergent agent behaviors:

CUDA Memory Checkpoint Assertion Failure with Expandable Segments

As shown above, PyTorch Issue #161356 describes an error in PyTorch’s CUDA graph checkpointing with expandable segments enabled. During a sequence that saves a small memory state, then a larger one, and restores the smaller state, PyTorch raises the error: “Expected curr_block->next == nullptr to be true.” Assertion failures occur in the allocator’s checkpoint restoration logic, where terminal blocks in expandable segments are expected to have null next pointers.

Both frameworks identified the same underlying issue but proposed fundamentally different solutions. CCA viewed the assertions as overly restrictive and simply removed the problematic TORCH_CHECK(curr_block->next == nullptr) assertions (–2 lines), while preserving other essential safety checks. CC viewed the assertions as important architectural guardrails and, instead of removing them, added logic (+7 lines) to explicitly set remaining->next = nullptr during block splitting, effectively making expandable segments comply with the assertion. CCA favored minimal intervention, while CC pursued a more holistic solution. In this case, we note that the PyTorch team’s eventual fix matched CCA’s approach, providing human validation of CCA’s principled engineering style.

Excessive Memory Allocation and Deallocation during Llama-2 Training

PyTorch Issue #135837 highlights a memory allocation problem encountered during Llama-2 (70B) model training. When GPU memory utilization approaches hardware limits, the allocator must decide whether to reclaim cached memory or retain it for performance optimization. On A100 GPUs (80GB), excessive memory deallocation and reallocation cycles occurred when reserved memory exceeded 70GB despite expandable_segments=True , resulting in significant training slowdowns.

The issue was identified in PyTorch’s CUDA allocator logic: even when the user explicitly enables expandable segments, the release_cached_blocks() function continues to unmap expandable segments, causing unintended memory deallocation. This created a contradiction between user intent (maintaining expanded memory) and system behavior (aggressive memory reclamation).

To solve this issue, CCA implemented a single guard clause (+6 lines) to fully disable memory reclamation when expandable segments are enabled, thus strictly adhering to the user’s intent. In contrast, CC developed a more complex solution (+63 lines), dynamically measuring memory pressure and raising the reclamation threshold from 87.5% to 95%, while preserving emergency mechanisms above 95% to prevent out-of-memory errors. Both solutions effectively addressed the immediate issue but reflected contrasting philosophies. CCA identified and minimally fixed the problematic behavior, while CC addressed the broader memory management challenge with a more sophisticated approach.

Neural Network Precision Regression during Weight Manipulation

PyTorch Issue #163072 involves a test failure where test_partial_flat_weights produces numerical accuracy errors on A100 and H100 GPUs, with relative differences of approximately 0.003 versus the expected tolerance of 1.3e-06. The test validates that partial flat weights (a memory optimization that stores select neural network layers in contiguous memory blocks) yield results equivalent to standard weight storage. The failure occurred during a sequence where LSTM weights were deleted, the module was moved to CUDA, and weights were manually restored.

Both CCA and CC correctly identified the root cause as inappropriate test tolerances for GPU operations and implemented the same adjustment: changing the tolerance parameters from exact equality to atol=1e-4, rtol=1e-4 (+1 line). This modification allowed the test to pass.

However, CC did not stop there. While confirming that the adjusted test passes, CC encountered a benign warning about non-contiguous memory layout. In response, CC implemented additional changes (+20 lines), modifying setattr in RNNBase to automatically call flatten_parameters() whenever weights are manually assigned. Ultimately, CC addressed not only the immediate test failure but also the underlying warning, resulting in a more comprehensive but potentially over-engineered solution.

9.3 Architectural Analysis 
Figure 5 : Simplified traces for CCA and CC on PyTorch issue #161356

This section analyzes the problem-solving behavior of CCA versus CC on Issue #161356. Figure 5 shows simplified traces of the solutions of both agents. Both employed similar high-level strategies: (1) initial reproduction attempts, (2) code exploration when reproduction failed, (3) root cause identification through systematic analysis.

Both agents also recognized the need for two directions of exploration: locating assertion failures in the CUDA memory allocator and understanding expandable segments logic. However, they perform these explorations differently:

- 1.

Single-Agent: CCA performed explorations directly within the original context, maintaining awareness of the user’s problem, system instructions, and previous observations. As such, CCA’s explorations are subsequences of the overall reasoning chain.

- 2.

Multi-Agent: CC delegates investigations to separate, stateless subagents. As shown in Figure 5 , CC even executes one of the subagents concurrently, while the main agent is running the reproduction script. These agents do not access the main agent’s context, but they are initialized with a detailed prompt that emphasizes thoroughness (“use a thorough approach to find all relevant files”).

The architectural differences between CCA and CC significantly influenced solution characteristics. CCA’s solution was simpler and more cautious, whereas CC was more ambitious and overengineered its solution. CC opted for this solution because it was the suggestion returned by the subagent, which was tasked with performing an exhaustive analysis. The subagent’s mandate for thoroughness, combined with its lack of the original context, leads it to over-analyze the problem and provide a more complex solution than is necessary. The main agent, trusting the subagent’s expertise, implements the solution despite preferring simpler solutions independently. This highlights a fundamental challenge in multi-agent systems. Generally, subagents separate concerns and allow the main agent to focus on its main task. However, our analysis suggests that for well-scoped debugging tasks, the benefits of delegation may be outweighed by the risk of context loss and derailment via inter-agent misalignment.

10 Trace UI

As shown in Figure 6 , the CCA Trace UI provides developers with detailed visibility into agent execution, showing the hierarchical call stack, latency metrics, token usage, and tool invocations for debugging and performance optimization.

Figure 6 : CCA Trace UI with call stack visualization and tool invocation details.
