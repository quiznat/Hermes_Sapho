---
version: source-capture.v1
article_id: art-2026-03-04-027
ticket_id: ticket-import-art-2026-03-04-027
source_url: https://arxiv.org/abs/2601.18341
canonical_url: https://arxiv.org/abs/2601.18341
source_title: Agentic Much? Adoption of Coding Agents on GitHub
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-30T18:09:04Z'
linked_paper_urls: []
---
# Source Capture

## Title

Agentic Much? Adoption of Coding Agents on GitHub

## Body

Agentic Much? Adoption of Coding Agents on GitHub

Romain Robbes romain.robbes@labri.fr 0000-0003-4569-6868 INP, LaBRI, UMR 5800 Univ. Bordeaux, CNRS Bordeaux France , Théo Matricon theo.matricon@inria.fr 0000-0002-5043-3221 Univ. Rennes, Inria, CNRS, IRISA Rennes France , Thomas Degueule thomas.degueule@labri.fr 0000-0002-5961-7940 INP, LaBRI, UMR 5800 Univ. Bordeaux, CNRS Bordeaux France , Andre Hora andrehora@dcc.ufmg.br 0000-0003-4900-1330 Department of Computer Science UFMG Belo Horizonte Brazil and Stefano Zacchiroli stefano.zacchiroli@telecom-paris.fr 0000-0002-4576-136X LTCI, Télécom Paris Institut Polytechnique de Paris Palaiseau France

(2025)

Abstract.

In the first half of 2025, coding agents have emerged as a category of development tools that have very quickly transitioned to the practice.
Unlike “traditional” code completion LLMs such as Copilot, agents like Cursor, Claude Code, or Codex operate with high degrees of autonomy, up to generating complete pull requests starting from a developer-provided task description.
This new mode of operation is poised to change the landscape in an even larger way than code completion LLMs did, making the need to study their impact critical.
Also, unlike traditional LLMs, coding agents tend to leave more explicit traces in software engineering artifacts, such as co-authoring commits or pull requests.
We leverage these traces to present the first large-scale study (129,134 projects) of the adoption of coding agents on GitHub, finding an estimated adoption rate of 15.85%–22.60%, which is very high for a technology only a few months old–and increasing.
We carry out an in-depth study of the adopters we identified, finding that adoption is broad: it spans the entire spectrum of project maturity; it includes established organizations; and it concerns diverse programming languages or project topics. At the commit level, we find that commits assisted by coding agents are larger than commits only authored by human developers, and have a large proportion of features and bug fixes. These findings highlight the need for further investigation into the practical use of coding agents.

Coding Agents,
AI4SE,
Large Language Models,
Software Repositories 
† † copyright: rightsretained † † journalyear: 2026 † † doi: XXXXXXX.XXXXXXX

1. Introduction

In the span of a year, coding agents such as Claude Code, Codex, or Gemini (among many others) have transitioned from promising tools in research papers to practical products seeing practical adoption. While the emergence of LLMs in programming, such as earlier versions of Copilot, has been and is still the subject of extensive study, coding agents, even if they leverage the same underlying technology, are markedly different. What distinguishes coding agents is both the scale of the tasks that they undertake and the degree of autonomy with which they undertake these tasks. Developers can use a traditional LLM to accelerate their programming by completing lines or blocks of code. However, they can (and do–see Section 10 ) delegate entire tasks to coding agents, such as finding and fixing bugs, or implementing new features. Depending on their workflow, coding agents can operate under close supervision (with a developer manually approving each action), up to nearly complete autonomy, e.g., acting on a bug report and submitting a complete pull request for review.

The first coding assistant offering “agentic” capabilities appeared in 2024. In the spring of 2025, virtually all major AI providers released their take on a coding agent. Since then, the adoption of such programming tools has ballooned (see Figure 7 ), in line with their increase in capability. Indeed, studies show that the length of tasks that AI systems can solve at a fixed success rate currently doubles every 7 months (Kwa et al. , 2025 ) . The ability to delegate tasks to a coding agent in such a fashion holds great promise. However, the few human studies on coding agents show contrasting results (Becker et al. , 2025 ; Kumar et al. , 2025 ) . We detail the working of coding agents in Section 2 and the related work on empirical studies of coding assistants in Section 3 .

The paucity of work studying coding agents motivates us to study this from another angle. While completion-based coding assistance embedded in the IDE is hard to track in the wild, since it leaves no explicit traces, coding agents leave abundant traces in software repositories, in the form of configuration files, summaries of knowledge they acquired, or even explicit metadata (e.g., author or co-author information) in commits and pull requests (Robbes et al. , 2025 ) . This paves the way to study the adoption of coding agents in the real world at a very large scale, a point of view that is highly complementary to the existing qualitative studies (Stol and Fitzgerald, 2018 ) . We detail our methodology, based on the analysis of software artifacts on a very large scale, in Section 4 .

We find that the adoption of coding agents has been very rapid. At the end of October 2025, in a sample of 129,134 projects, 7.89% of the projects present traces of adoption at the file level. At the commit level, the proportion is likely even larger (8.64%), leading us to estimate a total adoption of 15.85%, with a high estimate of up to 22.60% (See Section 5 ).

Beyond quantifying adoption in a binary way, we conduct more detailed analyses to quantify the extent of adoption and its distribution over the project maturity spectrum. We find a bias towards younger projects; beyond that, and somewhat unexpectedly, we find that larger and more mature projects adopt coding agents in comparable proportions to smaller and less mature ones. We also find that a sizeable proportion of projects have adopted coding agents in a pervasive manner, with a small, but non-negligible set of extreme adopters. We detail these findings in Section 6 .

Going further, we study the adoption in more specific contexts; finding adoption in diverse contexts such as established organizations, types of projects as described by their GitHub topics, and programming languages ( Section 7 ). We study the evolution of the adoption over time and across tools and organizations, observing a rapid growth since March 2025, and identify that a small number of coding agents account for the majority of adoption ( Section 8 ). Finally, we study the contributions authored or co-authored by coding agents at the commit level, finding that they are larger than those authored by humans only ( Section 9 ); we perform a manual analysis of the content of a sample of commits, to find the types of tasks that are performed with the help of coding agents, finding it is concentrated in features and fixes ( Section 10 ).

The current extent and the rapid increase of the adoption of coding agents have several implications, both in practice and in research (notably, there are ample avenues for future work). Our study has limitations: in particular, we discuss in which ways our heuristics may lead to overcounts or undercounts of the adoption. We discuss the implications, limitations, and future work related to our study in Section 11 .

2. Background

2.1. Coding Agents

The agentic loop

We use the following definition for coding agents: a coding agent is a LLM running in a loop with tool access that aims to complete a given goal. The tools enable the LLMs to have rich interactions with its environment.
The LLM loop, which we call agent loop , is simple: the LLM proposes a solution, it gets feedback and then use the feedback to offer another modification, more precisely:

- (1)

query the LLM with a sequence of interactions, initially this is just the task description;

- (2)

parse the response given by the LLM for the presence of tool usages and task completion;

- (3)

if tool calls are present: optionally ask the user for permission before using sensitive tools;

- (4)

if task is not completed: add the LLM’s response to the sequence of interactions, replacing tool calls with their results.

Figure 1 shows a graphical depiction of this process.
The agent notifies the user when it believes it has completed the task, ending the loop.
Some agents go as far as to commit the changes to the repository, or author a pull request.
Depending on its configuration, the agent may insert co-authorship information at this point (e.g., Co-authored-by:copilot-swe-agent ).

Start: Task Desc. Query LLM with Interactions Parse Response Task Complete? End: Task Done Tool Calls Present? Sensitive Tools? Request Permission Execute Tools Update Interactions Yes No Yes No Yes No Figure 1. Typical workflow of a coding agent

The biggest contributor to the performance of coding agents is the LLM. There has been rapid progress of LLMs towards producing structured output or improved tool usage, which are key for agentic use. Furthermore, there has been a recent growth in the reasoning capabilities of agents over long sequence of interactions which is key driving factor for the performance of coding agents.

LLM Harness and tool use

Tools access boosts coding agents with more reliable capabilities, the LLM’s harness connects the LLM to these tools. The harness provides the list of available tools to the LLM as part of its prompt. Part of the LLM’s training involve tool use, which, from the LLM’s point of view, consists in outputting a tool call using a structured format such as JSON.
The harness will query the LLM, and parses the LLM’s output in order to detect tool calls. It then invokes the tools on behalf of the LLM, and feeds the output of the tool back to the LLM. Depending on the degree of autonomy desired, the harness may ask the user for confirmation before executing certain tools (e.g., to review code edits, or to approve shell commands).

Tools and context

Software projects constitute a large context for an LLM, which has a limited context window. For traditional coding assistants, context is often pre-calculated by the IDE, and included to the LLM’s prompt. Coding agent allow the same functionality; they also allow developer to manually specify relevant context by mentioning specific files. However, a coding agent can also augment its context: tool calls enable dynamic and interactive queries. This enable coding agents to perform more autonomous workflows, such as:

- •

Adapt its context to the task at hand, by using tool calls to explore the code base dynamically;

- •

Automatic debug of the code thanks to compilation and a potential suite of tests, using the feedback given from these tools the agent can propose solutions.

There is a large variety of tools that agents can use. Some coding agents can run arbitrary shell commands in a terminal (this defines a small set of tools, but allows great flexibility), whereas other operates in more controlled environments that restrict the commands they can run.
Some specific tools enable browsing the web to gather information available. Other tools allow coding agents run a project test suite; this is highly valuable for the agent to gain feedback on their work. The specific tools available are user dependent; emerging standards such as the Model Context Protocol (MCP) ease the definition of new tools.

Given a task (e.g., “implement feature X and make sure the tests pass”), the agent will execute the LLM in a loop until it determines that the task is completed. In the feature implementation example, the agent could start by exploring the code base to find relevant code, then edit the code until it compiles (processing errors from the compiler), and then iterate until tests pass (if they exist; the agent may also be tasked to write tests in the first place).

Autonomy and oversight

Notably, this process can be lengthy, as the LLM is used multiple times, processing inputs of increasing size (often growing to tens of thousands of tokens). Agents tend to have an asynchronous mode of interaction: they do their work in the background, only stopping when the task is done, or when they require input from the developer. Developers can tend to the agents in between their other tasks.

Depending on the degree of autonomy desired, the developer may interrupt the process at any point and provide some guidance to the LLM. Particularly trusting users (or careful developers using sandboxes and extensive test suites) may provide high or full autonomy to the LLM, setting the harness to auto-accept any tool the LLM desires.

Developers may provide guidance to the agent by providing more detailed instructions (e.g., “implement feature X in module Y, using library Z”), which will reduce the need for searches, or give feedback on the work (e.g., “this code does not conform to the project’s convention, always do X, not Y”).
The LLM may also compile this guidance in the form of instructions in text files; with appropriate conventions, the harness will automatically add these files to the LLM’s context window in subsequent iterations. The footnote below links to two examples of such files containing guidance about a specific projects, describing their high-level organization, commands to interact with the project, conventions to follow, among others. 1 1 1 Example 1 and Example 2 ; the next section has additional examples As such knowledge is valuable, such files are often committed to the repository, so that the agent can consult them overtime, and, if necessary, update them. In this study, we look for the presence of these guidance files , as markers for the use of LLMs, together with other explicit markers in commits and pull requests.

Figure 2. Evolution of the number of AI coding agents since 2022

Notable coding agents

Let us present a few of the most popular or notable AI coding agents, at the time of writing:

- •

Claude Code , is Anthropic’s take on agentic AI for code. Initially available as a terminal application as a preview in February 2025. The default guidance file for Claude Code is CLAUDE.md . If allowed, it typically commits on behalf of users. Claude Code can now integrate as a plugin in most code editors, and is since recently available on the web and as GitHub actions; and can recently make pull requests.

- •

Codex from OpenAI (different from the earlier model with the same name), was released as a command-line application in April 2025, followed by a variant available on the web in May 2025. It can run on a cloud virtual machine which can download repositories before performing tasks on them. The default guidance file for Codex is AGENTS.md , which, since August 2025, has become an emerging standard which other agents use. Codex typically create one branch for each task it is assigned, and submits a Pull Request when finishing its work.

- •

GitHub Copilot started as a code completion tool in 2021. Over the years, it added the functionality to query the code base with natural language. It offers an agent mode since May 2025, which can be interacted with from the IDE. It is also directly available within the GitHub user interface, where it can be assigned an issue which it tackles by making a plan, iterating on commits, and submit a draft pull request that it can modify in response to comments. Copilot uses a copilot-instructions.md files for guidance.

- •

Cursor is based on a fork of Visual Studio Code, with the idea to make the next generation of IDE, an IDE that targets collaborative development between human and AI. Like Copilot, Cursor started as a code completion tool in 2023, before offering a chat mode, and finally an agent in late 2024. The agent is directly available from the different panes of the IDE so that the user can quickly start a conversation or delegate a task to the agent. It integrates with most LLMs. Cursor stores guidance as “rules” in a .cursorrules files or a .cursor/ directory.

- •

Aider is an open-source framework where the agent lives in your terminal but it can also be plugged into existing IDEs. Aider pioneered the command-line agent format, with development starting as early as 2023. Aider works with any LLM. Aider is also largely developed with the help of the tool itself: for example, 88% of the code in their last release was authored by their agent. Aider’s guidance is often contained in a file called CONVENTIONS.md

Figure 2 shows a timeline of the release date of a subset of agents, as much as we could determine them. In some cases, we could determine only the products’ initial release date (likely too early); nevertheless, the figure shows the drastic increase in the quantity of coding agents over time.

2.2. Traces and heuristics

Coding agents often leave visible traces of their use. These traces can be in the form of a specific pattern in commit messages or metadata, a branch name, or the presence of a specific file in a repository.
To detect traces of coding agents activity in this work, we rely on our previous work (Robbes et al. , 2025 ) in which we produced an extensive list of heuristics about the traces left by more than 50 different coding agents.
These heuristics were validated with the data found on the GitHub platform.
Heuristics are, by definition, not perfect, but we ensure that they do not produce many false positives. We provide below a short overview of the traces left by coding agents. Each agent has a specific workflow, and may leave a subset of these traces.

2.2.1. Files

Files can be used to configure coding agents and add specific instructions for them.
We distinguish the following file types used to configure agents behavior: Configuration files , Rules , and Guidance files .
Configuration files allow to choose between predefined options of the agent in a structured language such as YAML, whereas rules and guidance files enable guiding the agent with custom instructions in natural language.

Configuration files indicate that the agent has been set up within the repository.
They contain the most important options for configuring the agent’s behavior and thus can offer insight into how the agents work, such as permissions, i.e., the actions the agent can take without waiting for the user’s permission.
These settings are highly tool-specific. Some settings influence the presence of absence of other traces, hindering the detection of agents. For instance, Claude Code’s .claude/settings.json has an option to disable traces left in commits, while Codex can change the default prefix it uses to create branches.

Rules and Guidance files aim to guide the agent through natural language specifications that the agent should follow.
They are generally written in markdown format and are added to the user prompt before sending it to the LLM.
They can have large or specific scopes. They are sometimes generated by an agent.
Their goal is to encode tacit knowledge that is necessary to the agent to tackle the tasks; this is why they are often shared among developers and most of the time committed to the repository. Rules are context specific 2 2 2 Example cursor rules with technology stack, programming principles, style issues, and how to test (27 lines). whereas guidance files are broader. 3 3 3 Example high-level project description for Claude, with: overview; key features; build, launch, test, and lints commands; project architecture (main modules and classes); development workflow; and typical tasks (239 lines) Guidance files may contain detailed task descriptions that highlight the steps to solve a specific task 4 4 4 Implementation plan for a feature, with: context; principal decisions and rationales; architecture of the solution; breakdown of the implementation in phases and steps; description of follow-up tests; risks; and deliverables (188 lines) or tactics and strategies the LLM should use to tackle problems in general. 5 5 5 Example guidance with strategy , for clarifying specifications that are under-specified (176 lines)

For example, the guidance file AGENTS.md 6 6 6 https://agents.md , listing 19 agents using the format on 14/11/25 , originally used by Codex, is a simple open format for guiding coding agents and is adopted by several agents, including, Jules, Cursor, Aider, and Copilot.
Claude uses CLAUDE.md , as stated in its documentation: “ CLAUDE.md is a special file that Claude automatically pulls into context when starting a conversation. This makes it an ideal place for documenting: common bash commands, core files and utility functions, code style guidelines, testing instructions […] ”. 7 7 7 https://www.anthropic.com/engineering/claude-code-best-practices

2.2.2. Commits

Most agents are given the capability to commit their work automatically or given a tool to do so, for example via the shell.
If allowed to commit, the agent should also write the commit message.
Within commits, agents can advertise their contribution to the commit through different mechanisms:

- •

By adding themselves as a co-author of the commit, with the agent’s user advertised as the main author. In this case, they use the “ Co-authored-by: ” trailer, which is added to the commit. Of note, agents may not adhere to the convention exactly, occasionally using different casings. 8 8 8 Example commit , co-authored by Claude Code, fixing a bug and adding tests (two files changed, +75/-2 lines).

- •

Less commonly, agents can be recorded as commit authors, similarly to how bots such as dependabot operate. To do so they provide a standard name and email address in commit metadata like Git’s ”author” and/or ”committer” fields. 9 9 9 Example commit , authored by Copilot, adding a feature and tests (16 files in 13 directories changed, +380/-48 lines)

- •

Some agents also add additional trailer pseudo-headers to the commit message, e.g.,“ Generated by: Claude ”.

All these traces can be explicitly disabled via configuration files, hiding the participation of agents.

2.2.3. Users, Issues, and Pull requests

Specific user accounts can be linked to coding agents, i.e., the activity of those users are in fact agent activities.
This enables users to assign reviews or issues to specific coding agents as users. 10 10 10 Example coding agent account for OpenHands Issues can then be used as the descriptions of tasks that are then delegated to coding agents. Some agents, when assigned such an issue or a more general task, will work via Pull Requests (PRs), in which they may author multiple commits depending on the task scope. Developers can interact with the agent via the GitHub interface, for example, delegating additional tasks. 11 11 11 Example PR with user delegating additional tasks to OpenHands (improving documentation and code consistency) A PR provides more information than a commit, with the whole trace of the development and the interaction with GitHub Actions, users, and reviewers.
The complexity of PRs authored by coding agents can range from the quite simple to authoring complex new features from scratch. 12 12 12 Example PR with user interacting with Copilot to implement a feature (3 follow-ups, 8 commits, +350/-15 lines)

3. Related work

3.1. Studies of LLM-based coding assistants

Controlled experiments

Early productivity studies showed mixed results. Imai (Imai, 2022 ) found higher productivity but lower code quality when using Copilot versus pair programming with humans. Vaithilingam et al. (Vaithilingam et al. , 2022 ) showed participants failed tasks more often with Copilot than Intellisense due to incorrectly generated code, despite preferring Copilot. However, Peng et al. (Peng et al. , 2023 ) found substantial improvements, with 95 programmers completing HTTP server implementations 55% faster using Copilot. Security studies yielded contrasting results. Sandoval et al. (Sandoval et al. , 2023 ) found similar overall security bug rates between assisted and control groups, with 36% of bugs originating from AI suggestions. Perry et al. (Perry et al. , 2023 ) found AI-assisted code was less secure across 6 tasks, though participants overestimated their code’s security. Asare et al. (Asare et al. , 2023 ) found no significant security differences on realistic tasks like sign-in functionality.

Observation studies

Barke et al. (Barke et al. , 2023 ) observed 20 participants using Grounded Theory. They identified two fundamental usage modes: acceleration , where developers have clear implementation goals and prefer small, quickly-validated suggestions to maintain flow; and exploration , where developers lack clear plans (e.g., working with unfamiliar APIs) and prefer larger suggestions as starting points. This framework explains much of the variation in how developers interact with AI assistants.

Surveys and interviews

Liang et al. (Liang et al. , 2024 ) surveyed 410 developers, identifying successful use cases (boilerplate, proof of concepts) and barriers (validation time, non-functional requirements). Mozannar et al. (Mozannar et al. , 2022 ) observed 21 programmers: participants spent 22% of time evaluating Copilot suggestions versus only 14% writing new functionality. This suggests that common metrics like acceptance rate significantly underestimate the cognitive overhead and time investment required for AI-assisted programming. Wang et al. (Wang et al. , 2023 ) studied trust in AI assistants through interviews with developers based on real-world Copilot usage. Developers emphasized understanding Copilot’s limitations and expressed concerns about negative impacts on learning—a key consideration for software engineering practice and education.

Telemetry

Using telemetry to monitor adoption of coding assistants can be done in controlled environments such as companies. Murali et al. (Murali et al. , 2023 ) reported Meta’s deployment of CodeCompose, achieving 22% acceptance rate and generating 8% of company-wide code.
Ziegler et al. (Ziegler et al. , 2022 ) found that among 2,000 Copilot users the best factor to predict perceived productivity was acceptance rate. Izadi et al. (Izadi et al. , 2024 ) developed an IDE extension in order to study model failures via the interaction data of 1200 users.

Usage in software repositories.

Tufano et al. (Tufano et al. , 2024 ) analyzed ChatGPT usage traces in 467 GitHub instances, developing a taxonomy of 45 software engineering tasks including feature implementation, documentation, software quality, and development processes. Some usage patterns were unexpected, such as assistance in motivating proposed changes. Xiao et al. (Xiao et al. , 2025 ) analyzed more than 1,200 traces of generative AI from ChatGPT and Copilot in a qualitative fashion when usage was explicitly written by developers in their software artifacts. They looked at the targeted tasks of generative AI but also looked the churn before and after adoption of generative AI and found no significant change in churn post-adoption.

The white papers from GitClear (Harding and Kloster, 2024 ; Harding, 2025 ) paint a different picture. They studied the evolution of churn before and after the adoption of Copilot. They found that churn increased post-adoption as time passes with an also increased incidence of code duplication. However one weakness of this study is the lack in the data of traces of use of Copilot, making it impossible to distinguish between cases where Copilot was used and when it was not, making it a rough approximation that does not exclude other possible factors.

3.2. Coding Agents

Academic Agents

The field of coding agents is not industry specific, there has been a strong interest in the academic community as goal.
The development of benchmarks such as SWE-Bench (Jimenez et al. , 2024 ; Chowdhury et al. , 2024 ) that are now used both by academics and industrials as a standard benchmark to evaluate the performance of their coding agents. SWE-Bench use data from real world Git Hub issues that were successfully merged with enough description and tests in order to assess the ability of the agent to go from the natural language description of the issue to making changes in order to pass the tests.
Coding Agents are also developed by the academic community such as AutoCode Rover (Zhang et al. , 2024 ) or Agentless (Xia et al. , 2024 ) , with a focus on lowering the cost of solving tasks of SWE-Bench.
These papers highlights also flaws in SWE-Bench with tests for some issues that are lacking (Wang et al. , 2025 ) or the possibility of agents to change the tests or remove features in order to solve tasks.

Studies of coding agents

Becker et al. (Becker et al. , 2025 ) studied the perceived increase of productivity relative to the effective productivity in a controlled experiments of software developers using Cursor. Software developers believed that Cursor usage increased their productivity by an average of 20% but actually it decreased their effective productivity by 19% on average.
The proposed explanation is that developers do not choose efficiently the tasks to delegate to cursor, some are worth it while others are not but many potential factors can have an effect.
Interesting metrics are that only 44% of code generations are accepted and 9% of the time is spent waiting on AI to generate code, improving generation speed or quality has clear benefits.
Importantly, the agent used had limited capabilities, and was used in interactive rather than autonomous mode.

Kumar et al. (Kumar et al. , 2025 ) studied the barriers to successes of coding agent use with observations from 19 developers using Cursor. The developers were split in two groups, one who delegated the whole to the agent and one who split the tasks into several sub tasks with the agent and the agent had to solve the sub tasks. The developers had to provide the agent with contextual information specific to the repository. The main barrier was the lack of tacit knowledge of the agent.

Bouzenia and Pradel (Bouzenia and Pradel, 2025 ) studied the interactions traces of agents trying to solve tasks from the SWE-bench benchmark.
These traces are thus purely agent, there is no human interaction except from the initial prompt however at the same time they highlight the diversity of traces between the different less established agents considered. Variability is shown between the length of interaction traces, their type and the differences between successful and failed attempts.

MSR studies of coding agents

Concurrent to this work, a few studies using MSR techniques have emerged (all are currently preprints). Li et al. present AIDev, a dataset of coding agent pull requests (Li et al. , 2025 ) , showing a sharp increase in the number of pull requests authored by a subset of agents (Codex, Devin, Copilot, Cursor, and Claude Code). They classify the PRs according to their conventional commit type, with results similar to ours in RQ6.

Mohsenimofidi et al. (Mohsenimofidi et al. , 2025 ) performed a preliminary qualitative study of the content found in coding agent guidance filesfinding that the content is very diverse, and that the most common categories of content include conventions and best practices, contribution guidelines, project structure, and build and testing instructions, among others.

He et al. study projects adopting an early coding agent, Cursor, to find whether it is associated to increases in productiviy and quality issues using a difference in differences design (He et al. , 2025 ) . They find that the increase in velocity in the first two months of cursor adoption, while static analysis warnings and code complexity increase over time.

4. Methodology

We study the adoption of coding agents in the real world, at a very large scale, a point of view that is highly complementary to the existing studies, obtained from observations of very few developers (Stol and Fitzgerald, 2018 ) .
We decided to target open-source GitHub repositories, so the data comes from Git repositories and is available through the GitHub APIs.

4.1. Heuristics for Detecting Coding Agents

One significant challenge is the diversity of the ways the different agents work, as well as the sheer number of available agents (Robbes et al. , 2025 ) . Some agents are integrated in IDEs, while others operate on the command line; some agents are very autonomous, primarily interacting via pull requests. We employ a multi–faceted approach to identify repositories that use software‑engineering (SE) agents such as Copilot, Claude, Codex, and others. The heuristics are grouped into four categories:

- (1)

File‑based : presence of specific configuration files or documentation artifacts that are typical for an agent’s usage (e.g., presence of a .cursorrules file).

- (2)

Author-based : authorship or co-authorship of a commit by a known coding agent (e.g. Co-Authored-By: Claude <noreply@anthropic.com> ).

- (3)

Branch‑based : creation of branches whose names follow a convention used by agents (e.g. copilot/fix-… ).

- (4)

Label‑based : pull requests or issues labelled with the corresponding agent name (e.g. codex ).

The heuristics were obtained through a systematic manual investigation that involved the following steps:

- (1)

Mapping agent names to repository identifiers.

- (2)

Studying documentation to learn how agents are configured and what files they use or generate.

- (3)

Manually inspecting repositories likely to employ agents and recording relevant artifacts.

- (4)

Performing targeted GitHub searches to confirm hypotheses, such as:

Path:CLAUDE.md
 Co-authored-by:copilot-swe-agent
 is:pr label:codex

- (5)

Cross‑checking results to discover new patterns when a repository uses multiple agents simultaneously.

Each heuristic was rigorously validated for false positives. A notable
example concerns the file CONVENTIONS.md . While the Aider
website recommends placing agent‑related information in this file, it is
also commonly used to advertise general project conventions to all
developers. Because the risk of misclassifying such files outweighs the
potential underestimation of Aider usage, we have excluded CONVENTIONS.md from our final heuristic set.
Similarly, the AGENTS.md file was originally introduced by Codex; however, it is now used by dozens of coding agents, including Copilot, Jules, Cursor, and Aider.
Consequently, the presence of this file alone is insufficient to reliably identify the coding agent in use.

At the time of writing, we maintain 86 86 file‑based heuristics, 20 20 branch‑based heuristics, and 4 4 label‑based
heuristics for 48 coding agents. In addition, we also maintain a set of general bot
patterns, using authorship heuristics (e.g. dependabot ); we use this to filter commits and focus on human-authored and AI-assisted commits.

It is important to note that the users can hide the traces of AI-assisted commits by removing the metadata or not adding their files to the repository; these commits, therefore, will be identified as human-authored in our study.

4.2. Analysis Pipeline

Since the adoption of AI agents is very recent and evolving rapidly, recent data is needed. This is why we put a particular focus on automation in this work. We ran the last iteration of our analysis pipeline on October 31st, 2025 and the following day, to get data on entire months of activity. Our study period starts on 01/01/2025 and ends on October 31st, 2025 13 13 13 Note to reviewers: when revising this paper, we plan to extend the study period with updated data. . Early runs of the analysis included 2024: we found that adoption was extremely limited then; as the complexity of our analysis grew, we decided to focus on the period with the most significant adoption.

We first filter repositories to find relevant active repositories, then we detect agent use and collect statistics.
We perform different analyses based on the overall data that we have gathered this way.

4.2.1. Selection of the Data

We start with a sample using the sampling tool by Dabic et al. (Dabic et al. , 2021 ) .
The original dataset contains repositories with at least 10 stars.
From this dataset, we select projects that satisfy the following characteristics:

- •

not forks,

- •

a minimum of 5 000 5\,000 lines of code (non‑blank, non‑comment),

- •

at least 100 100 commits,

- •

active in the last three months (at least one commit),

These criteria ensure that we have projects with a reasonable level of maturity, as we enforce minimum thresholds for activity and code size. In particular, we do not want forks to dominate our sample. In most cases, the bulk of development occurs in the “original” project. In some cases, this may cause us to miss interesting projects–e.g., when an original repository is now inactive but a fork continues development—but we consider this a reasonable compromise.

We accessed the sampling tool to download the dataset used in the remainder of the study on 29/08/2025. After applying the filters above, we are left with a set of 130,621 projects. Considering that GitHub hosts hundreds of millions of projects, we were initially surprised at this relatively low number, given that the sampling tool by Dabic et al. monitors all public projects on GitHub. However, the minimum threshold of 10 stars excludes the vast majority of repositories, and the exclusion of forks substantially reduces the pool of candidates. The minimum activity and size thresholds reduce it further.

We initially considered using Software Heritage (Cosmo and Zacchiroli, 2017 ) , as it is the most comprehensive dataset of public source code. However, Software Heritage lags behind GitHub by a few months, which is problematic in our case, as we want data to be as fresh as possible to study such a rapidly changing phenomenon.

Beyond the project names and URLs, this dataset includes an important number of metrics (e.g., number of contributors, number of commits, number of forks, etc.), some of which we use in the remainder of this study.

At the end of the analysis process described next, we have data on 129,134 project, the difference with the original number (130,621) is due to 900 900 failures of the pipeline, and 500 500 “dotfiles” repositories that we filter out from the analysis as they are not representative of software development. In the vast majority of cases, failures occur when a repository cannot be found on GitHub (typically because it was made private between the time we downloaded the list of repositories and the time we fetched the file list).

4.2.2. Identification of Agent Adoption via Tools

Next, we use our file-based heuristics to identify agent adopters in our sample. For each repository selected in step 1, we query the GitHub REST API to download the file list of the main branch when we execute the study (on October 31st, 2025). For very large repositories, the API fails because the file list is too large; in that case, we perform a shallow clone of the repository to obtain the file list. For every repository, we store a single text file containing one file path per line.

We then search each file list for names that match our compiled set of file‑based heuristics; any repository containing at least one file identified by a heuristic is classified as an adopter at the file level. Nevertheless, we always match all heuristics: by matching all heuristics, we can identify every tool that a repository might use, since a repository may employ more than one agent, and every file that matches heuristics.

4.2.3. Identification of Agent Adoption via .gitignore

Although knowledge in coding agent files is valuable, and thus should be shared in the repository, this is not always the case. To have a better coverage of agent adoption, we also look for the presence of agent configuration files in the .gitignore file, which would prevent them from being committed to the repository despite being present. In this way, we identify potential adopters who do not wish to commit certain (or all) agent configuration files. To do so, we query the GitHub API for the main .gitignore file, and we scan it for heuristics in the same way we do for the file list.

4.2.4. Collecting Agent File Statistics

For each of the repositories that we have classified as an adopter, we collect fine‑grained
information about the agent configuration files that signal agent usage.

- (1)

Shallow clone. We clone each repository with --depth 1 and --no-checkout , and populate the index with the information of the files in the latest commit, so that the working tree contains only the minimal information to carry out the next steps, to keep storage needs low (even then, the whole analysis still requires more than half a terabyte in total).

- (2)

Checkout matched files. After cloning, we check out all agent configuration files–those that matched our heuristics
(e.g., CLAUDE.md , .cursorrules ). This step lets us confirm the correctness of the heuristics by inspecting the actual file contents, if needed.

- (3)

Gather per‑file statistics. For each agent configuration file, we query its commit history, computing the following descriptive statistics:

- •

the date on which it was first added,

- •

the total number of commits that modified the file
(including the initial addition),

- •

the size, in lines, of the most recent version.

- (4)

Aggregate metrics. From the per‑file data we compute repository‑wide summaries:

- •

total number of agent configuration files,

- •

cumulative size of all agent configuration file,

- •

overall count of commits that touched any agent configuration file,

- •

adoption date – the earliest commit that added an agent
configuration file in the repository, and

- •

per‑tool adoption dates – the earliest commit of an agent configuration file that is specific for a given agent (e.g., the first commit containing CLAUDE.md ).

These metrics provide a quantitative view of how and when agents are introduced into open‑source projects, and they serve as the basis for subsequent analyses, such as maturity classification and usage trends.

4.2.5. Commit and Pull Request Level Adoption

After having identified the repositories that contain agent configuration files,
we perform a more granular analysis on their commit history and pull requests.
In addition, we examine a random sample of non‑adopter repositories
to uncover “silent adopters” (repositories that use agents but have no
explicit agent configuration file).

We estimate the sample size needed for estimating a proportion of adopters in our population (Cochran, 1977 ) . For an infinite population, the sample size for a proportion is given by:

(1) n 0 = Z 2 ​ p ​ ( 1 − p ) e 2 n_{0}=\frac{Z^{2}\,p(1-p)}{e^{2}}

where Z Z is the critical value corresponding to the desired confidence level, p p is the estimated proportion, and e e is the margin of error. For a finite population of size N N , the corrected sample size is:

(2) n = N ​ n 0 N + n 0 − 1 n=\frac{N\,n_{0}}{N+n_{0}-1}

This correction accounts for the finite population effect and prevents oversampling when N N is not large. Based on an earlier run of the analysis, we set N N = 120,000, assuming the worst-case p = 0.5 p=0.5 , a 99% confidence interval and a 1% margin error yields a sample size of 14,575. We increase the sample size to 16,000 as, after the first analysis run, we expect some projects to become file-level adopters, and others to become private.

Pull Request extraction.

For each repository we study in this step, using the GitHub GraphQL API, we download, for each project, up to 10,000 pull requests (PR) that were created on or after 01/01/2025 and their metadata, including their commits (only 19 projects exceed that number).
This includes the associated branch of the pull request, as well as any labels associated with it. These two data sources are the two sources of information for our PR identification heuristics. If a pull request matches one of our branch or PR heuristics, it is tagged as AI‑assisted . Inside the PR such an AI-assisted PR, we tag all the commits by the PR author as AI-assisted. This allows us to detect commit activity for agents that do not leave markers in commits, but do so in PRs, such as Codex. For each PR, we also determine its merge status, and merge type (merge, rebase, squash), in order to locate the commits that appear in the main branch.

Commit extraction

For each repository we study, we perform the following steps:

- (1)

Repository clone (historical snapshot). Given the storage requirements, we perform a shallow clone of each project up to the start of the study period 01/01/2025. At that time, coding agents were still very confidential (as confirmed by an earlier run of the analysis that included 2024): established tools like Copilot and Cursor allowed conversations inside the IDE, but started to propose agent-like functionality in 2025.

- (2)

Commit log parsing. For scalability reasons, we do not checkout files or compute diffs. From each cloned repository, we run “git log” to obtain: (a) the commit message; (b) authorship information, including any “Co‑authored‑by” trailers (extracted from the commit message); (c) the list of files (and file paths) affected by the commit, as well as their status; (d) file‑change statistics (added/deleted lines) for each file.

- (3)

Commit‑level heuristics. We match each commit against our list of commit‑level heuristics
(e.g., specific message patterns or authorship attributions). If any
heuristic matches, the commit is classified as AI‑assisted .

- (4)

Linking commits to pull requests. For each main branch commit, we check whether it appears in at least one
AI‑assisted PR, and was labelled as AI-assisted there. We take in account the merge type (commits merge with rebase or squash will have distinct commit hashes (Bird et al. , 2009 ) ). If so, we label the commit as
AI‑assisted. This choice is motivated by the fact that a commit’s provenance is often clearer when it belongs to an AI‑assisted PR (such as for Codex). For “squash merged” PR, this adds some imprecision, since the PR is condensed in a single commit which may be only partially AI-assisted.
An alternative would be to treat only
commits that match our commit‑level heuristics as AI‑assisted,
regardless of PR association. We adopt the former strategy while
documenting the trade‑off.

- (5)

Bot exclusions. Commits authored by known non‑AI bots (e.g., CI or release bots)
are identified via a manually curated list and labelled. They are excluded from the metrics computed in this study, as we wish to get insights on the adoption of AI coding agents
in relation to human development activities.
The remaining commits are
classified as human-authored.

- (6)

Filtering out noise. Merge commits, revert commits, bump‑version releases, and other
housekeeping changes are removed to focus on substantive work.

The result of this pipeline is a per‑repository catalog of AI‑assisted
commits, both at the PR level (PR‑AI‑assisted) and at the individual commit
level. These data form the basis for the subsequent metrics detailed next.

4.3. Metric Computation

For each adopter repository, we compute the following metrics.

Commit‑level statistics

For every commit that has been labeled as AI‑assisted,
or human-authored, we extract the following raw numbers from “git log”:
the count of lines added and deleted, and the number of files that were
added, modified, or removed. These figures provide a granular view of how much work is performed in each commit.

Unified adoption date

We refine the adoption date as the earliest commit that either adds an agent configuration file (the tool adoption date) or that is identified as AI-assisted by our heuristics. We refine the per-tool adoption date in the same manner.

File‑type and language classification

Using GitHub Linguist’s file‑extension database, we classify each file in a
commit as either source code , documentation , configuration , or other (data, images, etc).
The same lookup is then used to assign a programming language. Because we only rely on the extension, we avoid the prohibitive cost of parsing every file’s contents at scale.

Sometimes an extension maps to multiple languages (e.g., “.rs” could be the Rust programming language, or the deprecated RenderScript language). In important cases, we resolve the ambiguity by choosing the most popular language for that extension in our dataset. The resulting per‑commit tables contain, for each file type and programming language, the same line‑add/delete statistics as above, enabling downstream analyses such as agent activity by language.

Temporal aggregation

For each repository we aggregate commits over our period of interest, which is the activity from the project’s adoption date, to the end of the study November 1st, 2025. We then compute the following metrics

- (1)

The ratio # ​ AI commits # ​ all commits \displaystyle\frac{\#\text{AI commits}}{\#\text{all commits}} ,
a key indicator of how much work is performed by agents.

- (2)

Analogous ratios for subsets of commits that touch source code,
documentation, configuration files, or specific programming
languages.

- (3)

Counts of file additions and modifications per period, broken
down by file type and language, which reveal the magnitude of
agent‑driven changes over time.

- (4)

We also compute the ratio of the unique number of files touched by agents over all files touched.

- (5)

Finally, we compute the fraction of AI-assisted human authors, that is, the fraction of humans that use AI agents as co-authors for at least one commit during the period.

Commit-level adoption

Our first use of these metrics is to categorize projects in terms of their commit-level adoption . For any chosen time window we classify a repository into one of five commit‑level adoption levels.

- •

No Commits : The period contains no AI-assisted commits.

- •

Experimental : An AI commit ratio below 1 %.

- •

Limited Use A ratio between 1 % and 5 %, but still below 5 %.

- •

Consistent Use AI commits represent 5–20 % of all activity in the period.

- •

Pervasive More than 20 % of commits are AI-assisted, indicating widespread use.

4.4. Research questions

To carry out our study, we formulate the following research questions:

- •

RQ1. What is the estimated adoption of coding agents on GitHub? We answer this question in Section 5 by analyzing file and commit-level adoption overall.

- •

RQ2. What are the characteristics of projects adopting coding agents? We answer this question in Section 6 by analyzing the distribution of commit adoption metrics, and its relationship with basic project metrics, such as size and age.

- •

RQ3. In which context are coding agents used? We answer this in Section 7 by looking at adoption for specific organizations, topics, and programming languages.

- •

RQ4. How has adoption evolved, and which agents are driving it? We look at the evolution of adoption over time, and at specific coding agents, in Section 8 .

- •

RQ5. How large are AI-assisted contributions? We look at the size of commits (co)-authored by agents, and compare it to commits authored by humans and bots in Section 9 .

- •

RQ6. What types of contributions are AI-assisted? We classify a sample of commits in various types, following the conventional commit classification, in Section 10 .

5. RQ1: estimation of overall adoption

Table 1 presents our overall statistics on the datasets of projects we study. We study the adoption along several dimensions: (1) at the file level, on all the projects (with and without the .gitignore file); (2) at the commit level, based on a sample of projects; (3) based on the earlier, we extrapolate for overall adoption rates according to two scenarios.

Table 1. Overall adoption statistics. For each statistic, the middle rows show the subset of the data the adoption is measured in.

Metric File Ignored Sampled Commit Count Out of Percent

File-level tool usage

File-level use ✓ – – – 8,257 129,134 6.39%

Ignored files (all) – ✓ – – 3,302 129,134 2.56%

Ignored files (only) ✗ ✓ – – 1,934 129,134 1.50%

All file-level use ✓(either) – – 10,191 129,134 7.89%

Commit-level tool usage

Commit use (file level) ✓ – – ✓ 4,813 8,257 58.29%

Commit use (all files) ✓(either) – ✓ 5,517 10,191 54.14%

Commit use in sample ✗ ✗ ✓ ✓ 1,364 15,783 8.64%

Extrapolation

All non-file users ✗ ✗ – – 118,943 – –

Extrapolated Commit Users ✗ ✗ ✗ ✓ ≈ \approx 10,279 118,943 8.64%

Overall Adoption Estimate – – – – ≈ \approx 20,470 129,134 15.85%

High estimate

High Estimate Commit Users ✗ ✗ ✗ ✓ ≈ \approx 18,988 118,943 8.64 % 54.14 % \frac{8.64\%}{54.14\%}

High Estimate Overall Adoption Rate – – – – ≈ \approx 29,179 129,134 22.60%

5.1. File-based adoption

The first section of Table 1 shows adoption of coding agents based on file-level heuristics. Using our file-based heuristics, we find that out of our dataset of 129,134 projects, 8,257 have files indicating that they use coding agents in their repositories (6.39%). In addition, 3,302 projects instruct their version control not to commit files corresponding to our heuristics via their .gitignore file; of these 1,934 projects have no visible coding agent files in their repository, save their mention in the .gitignore . Summing both together, we find that 10,191 (8,257 + 1,934) projects reference coding agent files in their repositories, or 7.89%.

5.2. Commit-level adoption

The second section of Table 1 presents commit-level statistics. We investigate commit-level adoption in various ways: (1) we analyze a sample of projects for which we have no sign of file-level adoption for commit-level adoption, and (2) we analyze all the projects that have signs of file-level adoption for commit-level adoption to get insights on the overlap between these heuristics.

Sample adoption

As mentioned earlier, we selected a large sample of non-adopters at the file level for this analysis, in order to have a 99% confidence interval and a small 1% margin of error. The sample size set between analysis runs was 16,000 projects, out of which 15,783 could be analyzed by our pipeline on October 31st, and were still non-adopters (out of a final population of non-adopters of 118,943 projects–our base population, minus the 10,191 file-level adopters). Out of our sample, we find that 1,364, or 8.64% are commit-level adopters. Surprisingly, this is a higher percentage than the percentage of projects presenting file-level adoption.

Overlap between file-level and commit-level adoption

File-level adoption and commit-level adoption have some overlap, but it is far from complete. As we have just seen, an important proportion of projects have commit-level adoption, but no file-level adoption. The reverse is also true: an important proportion of projects that have file-level adoption would not be detected by commit-level heuristics. Out of visible file-level users, a little bit more than half (58.29%) are detected by commit-level heuristics; adding projects that are visible only by their .gitignore file, the proportion drops to 54.14%.

5.3. Extrapolating to the whole population

The third and fourth sections of Table 1 extrapolate the adoption rate in the entire population according to two scenarios.

Conservative scenario

For this scenario, we assume the sample estimate (8.64%) is accurate, and simply apply it to the entire population of projects that do not present file-level adoption (118,943 projects). This brings us to an estimate of a ​ p ​ p ​ r ​ o ​ x approx 10,279 (plus or minus 1%, with a 99% confidence interval). If we add the projects identified at the file level (10,191), we arrive at a total of ≈ \approx 20,470, or an adoption rate of 15.85%.

High estimate

For this scenario, we use the sample estimate, but also consider that a large proportion of projects (almost half) that are visible at the file levels, are not visible at the commit level. Therefore, it is possible that projects have adopted coding agents, without having any visible files in their repository, nor visible commits. An example of this would be a user of Claude Code that stores their configuration files in a separate repository such as a dotfiles repository, and either instructs Claude Code not to sign the commits, or prefers to commit manually ( Section 11.4 mentions concrete examples). If we assume that the proportion of such projects is comparable to the ones that have file markers, then only a ​ p ​ p ​ r ​ o ​ x approx 54.14% of the projects are detected by the commit heuristics. Following this assumption leads to an estimated number of projects adopting coding agents among those that do not present file-level adoption of 118 , 943 × 8.64 % 54.14 % = 18 , 988 118,943\times\frac{8.64\%}{54.14\%}=18,988 . This leads to an estimated percentage of 22.60% in the whole population when we also take into account the file-based users.

Needless to say, given that these projects are very difficult to observe, we can not know their true proportion, making this estimate a very rough approximation. Overall, as of November 2025, we estimate the true adoption to be somewhere in between our conservative estimate and our high estimate. Regardless of its definitive value, the fact that coding agents, a tool category that saw early products in 2024, and more established products in the Spring of 2025, have already reached 15 to 20% of adoption among GitHub projects in the Fall of 2025 points to an extremely rapid adoption.

6. RQ2: Adoption and project characteristics

To dive into the characteristics of adoption, we first examine the distribution of file and commit-level adoption. We then analyze how adoption varies with high-level project metrics, such as size, age, or activity.

6.1. Extant of file and commit level adoption 
Table 2. Binned distributions of file and commit level adoption metrics

Metric Bin 1 Bin 2 Bin 3 Bin 4 Bin 5 Bin 6 Bin 7

Total Files 1 2-5 6-10 11-20 21+

55.8% 30.7% 7.4% 3.7% 2.4%

Total Lines 0-10 11-50 51-100 101-250 251-500 501-1000 1001+

6.0% 16.2% 14.8% 30.0% 15.0% 8.8% 9.3%

Total Changes 1 2-5 6-10 11-20 21+

24.6% 37.4% 15.6% 11.1% 11.4%

Adoption Ratio None Experimental Limited Consistent Pervasive

41.2% 7.3% 16.1% 17.6% 17.8%

Table 2 shows statistics on the distribution of file-level adoption in terms of number of files, lines in these files, and number of changes, and of commit-level adoption. This analysis excludes projects which we detect solely via .gitignore , as we cannot measure these metrics for them. We grouped the metrics in bins to ease the interpretation of the data by providing reference points.

Number of files

We see that more than half of projects (55.8%) have a single rule or guidance file, and more than 85% of projects have 5 files or less. On the other hand, a small amount of projects have an extensive amount of guidance files (more than 10: 3.7%; more than 20: 2.4%), indicating that some projects use either sophisticated guidance for their coding agents, or multiple agents.

Number of lines

In terms of the amount of content in the rules and guidance files, we see that a small number of projects have very short guidance (10 lines or less: 6.0%). Such a small amount indicates projects having default or very basic configurations. The bulk of the projects have between 11 and 100 lines (16.2% and 14.8%, ≈ \approx 30%), and 101 and 250 lines (30.0%). At the extreme end, close to 10% of projects have more than 1,000 lines of guidance (9.3%), once again indicating sophisticated guidance.

Number of changes

In terms of changes, we see that almost a quarter of projects added their guidance file and never changed it (24.6%), while most projects occasionally change or add new guidance files (37.4%). On the other hand, some projects update their guidance regularly (more than 10 additions or changes: 11.1%; more than 20: 11.4%).

Commit ratio

In terms of commit ratio (shown on the last row), we see that, as shown in Table 1 , more than 40% of file-using projects have no commit-level activity. Of the remainder, we see that a majority of the projects have significant of commit level adoption: Consistent users (5 to 20% of AI-assisted commits) are at 17.6%; Pervasive users are at an even higher 17.8%. Of note, some of these ratios may be high for projects having low activity (e.g., a project with a single post-adoption commit, that happens to be AI-assisted, will have a commit ratio of 100%). For this reason, in the remainder of the analysis, we only consider projects with at least 10 post-adoption commits.

Relationship between the metrics

Figure 3 shows the distribution of the four adoption metrics, and how each pair of metrics relate to each other via scatterplots and hexbin plots (showing density); we also compute the correlation. Since many projects have an adoption ratio of 0, we focus only on the ones with a positive commit ratio; further, we include only projects with at least 10 post-adoption commits. The figure shows that there is a high degree of correlation between the file-level adoption metrics: projects that have larger or more numerous files also tend to change them more often. The correlation is strongest between number of files and total content, and somewhat weaker between lines of code and changes. On the other hand, even when filtering for absence of commit ratio and low activity, the correlation between the commit ratio and the file-level activity, if positive, is very low (at best, 0.1 with changes). Clearly, there are more factors at play to explain the relationship between the two categories of metrics.

Figure 3. Pairwise relations of file and commit level adoption metrics

Overall, this points to a large proportion of projects that adopt coding agents, but with a modest amount of guidance. A sizeable minority uses a large amount of actively-maintained guidance for coding agents. Whether and how this translates to a large amount of visible coding agent activity is another matter: there is a large minority of projects that have a high visible agent usage; however they are not necessarily the ones with the largest amount of guidance.

6.2. Project characteristics and file-level adoption

We investigate the characteristics of the projects adopting agents. We first focus on the adoption rate at the file level. As earlier, we count projects that show file-level adoption by usages of .gitignore as adopters. To look into project-level metrics, we split each metric of interest in our dataset into deciles, and we compute the file-level adoption ratio for each decile. This allows us to see whether projects that have larger/smaller metrics tend to have a larger/smaller adoption ratio.

Table 3. File adoption statistics versus project-level metrics, by deciles

Metric Aspect Sparkline D1 D2 D3 D4 D5 D6 D7 D8 D9 D10

LOC Deciles 5.0K 7.5K 11K 15K 21K 30K 45K 71K 130K 329K

File 4.66% 5.33% 6.29% 6.41% 7.74% 8.74% 10.07% 9.83% 10.25% 10.00%

Contributors Deciles 0 1 3 4 6 9 14 21 34 69

File 7.22% 8.33% 7.88% 7.70% 7.06% 7.33% 7.50% 7.36% 7.80% 11.02%

Commits Deciles 100 159 234 326 448 614 854 1.2K 2.0K 4.0K

File 7.71% 6.97% 6.83% 6.53% 7.03% 7.15% 7.43% 8.08% 9.87% 11.72%

Issues Deciles 0 3 9 19 34 60 104 194 458

File 6.91% 7.37% 7.48% 6.88% 7.17% 7.57% 7.94% 8.75% 12.38%

Pull Requests Deciles 0 1 8 22 46 84 144 243 434 934

File 4.65% 5.59% 6.02% 7.38% 7.27% 7.26% 7.86% 8.17% 9.51% 15.71%

Age (years) Deciles 0 1 2 3 4 5 6 7 9 11

File 21.17% 9.72% 8.42% 6.56% 6.31% 6.28% 5.68% 5.18% 4.94% 4.69%

Table 3 presents the deciles and adoption ratio for 6 metrics: size in (non-blank, non-comment) lines of code, age in years, number of contributors, commits, issues, and pull requests. For better readability, we also depict the trends using Sparklines (Tufte, 2004 ) –word-size graphical representation of trends or distributions of data. While there is a common conception that coding agents work best with “greenfield” projects (Osmani, 2025 ) , as it is much easier to write ”new” code without needing to integrate it in a large codebase, our results are more nuanced. We describe each metric in turn.

- •

Lines of Code: we first check whether larger projects have more or less adoption than smaller projects. We find that, somewhat contrary to expectations, adoption is higher for larger projects. Projects in the smallest deciles have an adoption rate hovering around 5%, while the largest project categories (from 50K lines of code and up) have double the adoption rate at around 10%. This trend maintains itself for the very largest decile (329K lines of code and up).

- •

Contributors: in terms of contributors, adoption hovers between 7 and 8% for all deciles, except the largest decile (69 contributors and up), in which the adoption reaches 11%. Note that the contributor count (extracted from GitHub) includes all contributors (human, bots, agents). However, this does not impact the trend that the very largest projects have more adoption.

- •

Commits: for commits, both the smallest decile (7.7%) and the largest deciles (1000+) show larger adoption, with the very largest decile (4,000+ commits) having the largest adoption rate at close to 12%. This confirms the impression that agents are adopted in more active projects, although they do contribute to this activity themselves. For the smallest decile, this might reflect the fact that new projects starting from scratch (“greenfield” projects) are indeed more likely to start using agents.

- •

Issues: as with other metrics, we find that projects with more issues tend to have a higher adoption rate. This is especially the case of the top decile (450+ issues), where the adoption rate exceeds 12%.

- •

Pull Requests: the tendency that projects in larger deciles have higher adoption is further confirmed by pull requests, where the difference is even more stark, with the highest decile jumping to close to 16% of adoption. Note that, depending on their workflows, agents can, and do, contribute pull requests to projects. Thus, it is likely that the stark difference observed is at least partly self-fulfilling, with projects having a heavy usage of coding agents seeing a fast growth in pull requests.

- •

Age: While larger metric values are associated with higher usage for the other metrics, age goes strongly in the other direction. Younger projects have a far higher adoption rate than older projects, with a factor of 4 difference between the smallest decile (1 year or less, 21%), and the largest (more than a decade, 4.7%). On its own, this does comfort the narrative that coding agents are best used in greenfield projects; however, we see that even old projects see a non-negligible adoption rate (close to 5%).

Thus, we see two trends at play here: clearly, younger projects have a much higher adoption than older projects. On the other hand, there is also a trend towards larger projects with more contributors, commits, issues, and pull requests having a higher adoption rate. This trend is partially self-fulfilling, since agents are contributors, and can contribute commits and pull requests to a project.

We applied a Chi-square goodness-of-fit test to assess whether the observed values are evenly distributed across categories or tend to be concentrated; in our case, the categories correspond to deciles.
We also computed the effect size associated with the Chi-square test.
The results show statistically significant differences for all metrics ( p-value < < 0.01), indicating that the distributions are not uniform across bins. The effect sizes are small for lines of code, contributors, commits, and issues, and medium for pull requests and age.

To tease apart these two effects, we re-ran the same analysis, excluding projects younger than one year. While the values of all the deciles and their adoption ratios changed slightly, we see the same trends, with higher adoption for higher metric values, and decrease of adoption with age (e.g., lines of code: ; contributors: ). The main changes were that, as expected, the very high peak for the first decile in age disappeared ( ); in addition, the adoption in commit deciles rose steadily ( ), instead of having a higher first decile and a flat progression. This is in line with our hypothesis that this may come from new projects.

We also carried out the same analysis, excluding projects younger than two years, finding again similar results (e.g.: lines of code: ; issues: ; pull requests: ). This conforts the observation that there are two distinct effects: a large effect of age for younger projects; however when removing young projects, there is still a tendency towards higher adoption of coding agents in projects with higher numbers of lines of code, contributors, commits, issues, or pull requests.

6.3. Project characteristics and commit-level adoption

Table 4 presents our analysis of the AI-assisted commit ratio of the projects in our dataset, since their adoption of coding agents. For this analysis, we only consider projects that have at least 10 commits since adoption; this avoids cases of projects having a very high commit ratio but little activity (e.g., a project that has a 100% AI-assisted commit ratio, but a single commit). We carry out this analysis for several categories of projects, and the per-decile analysis we applied for the file-level usage. We use the commit ratio categories defined in Section 4 (Experimental: < 1 % <1\% ; Limited: < 5 % <5\% ; Consistent: < 20 % <20\% ; Pervasive: >= 20 % >=20\% ).

Table 4. Commit adoption across different project categories

Category N None Experimental Limited Consistent Pervasive

All Files 7,596 33.11% 9.47% 20.43% 20.83% 16.17%

by LOC

by Contributors

by Age

All Files with commits 5,081 0.00% 14.15% 30.55% 31.14% 24.17%

by LOC

by Contributors

by Age

File level 4,450 0.00% 13.64% 29.82% 30.97% 25.57%

by LOC

by Contributors

by Age

Files ignored only 631 0.00% 17.75% 35.66% 32.33% 14.26%

by LOC

by Contributors

by Age

Commits only 1,035 0.00% 15.46% 38.26% 33.62% 12.66%

by LOC

by Contributors

by Age

Caveats

Note that this analysis comes with important caveats. In particular, there are good reasons to think the AI-assisted commit ratio is an under estimate of the actual one, since: 1) not all agents sign their commits or tag their pull requests; 2) even if they do, this behaviour can often be turned off; and 3) some developers may use agents, but prefer to commit manually. This can cause projects to have a commit ratio of 0 if all the activity is unobserved, or just to reduce the commit ratio if, e.g. a developer disables commit signing at a given moment. We expand on this in Section 11 .

Overall adoption

The first section of Table 4 shows the distribution of the commit ratio for all the projects that have file adoption markers. Overall, 33.11% of projects have a ratio of AI-assisted commit of 0 (this is smaller than the value among all adopters, ≈ \approx 46%, as we filter projects with few commits for this analysis). Out of the projects that have AI-assisted commits, the smallest category is the “Experimental” category (9.47%). The second smallest is the “Pervasive” category, the one with the largest degree of AI assistance (16.17%). The bulk of the remaining projects are roughly equally distributed between the “Limited” and “Consistent” category.

Since we can not know for certain whether the projects with a ratio of 0% have absolutely no AI-assisted commits or not, we filter them out in the subsequent analysis. Of the remaining projects, we see that a significant proportion of projects have a very high usage of coding agents, with almost a quarter (24.17%) of such projects having more than one in five commits that are AI-assisted. We find this number to be very high, especially considering that it is likely to be an undercount. We note that some projects have very high ratios of AI assistance at the commit level. In particular, 8.66% of projects with non-zero commit adoption have the majority of their commits that are AI-assisted; 3.05% have three quarters or more of their commits that are AI-assisted.

As in the prior section, we also applied a Chi-square goodness-of-fit test to assess whether the observed values are evenly distributed across the commit ratio categories.
We also computed the effect size associated with the Chi-square test.
The results show statistically significant differences for all metrics ( p-value < < 0.01), confirming that the distributions are not uniform across categories. The effect sizes are medium for all metrics.

Adoption across categories

The bottom three sections of Table 4 focus on specific categories of projects, and can be directly compared with the second section, since they all filter projects with no AI-assisted commits (the projects detected by the commit-level heuristics have this by definition). Notably, we see that projects that do not have visible files in their repositories (either detected through .gitignore or through commit-level heuristics only) tend to have lower levels of adoption than the ones detected by file-level heuristics. In particular, they have approximately half as much projects in the “Pervasive” category , while having more projects in the remaining categories. In both cases, the relative growth is larger in the “Experimental” and “Limited” categories ( ≈ \approx 15 to 30%), while it is considerably smaller for the “Consistent” categories ( ≈ \approx 5 to 10%).

Variation with project metrics

Looking at the variation of the distribution of commit ratio categories across project metrics in deciles paints a contrasting picture with the file-level adoption. We focus on lines of code and contributors, but we see similar trends in the other metrics (commits, issues, and pull requests). In all cases, larger or more established projects (e.g. with more contributors) tend to have a smaller ratio of AI-assisted commits: across deciles, the proportion of “Experimental” projects rises steadily, while the proportion of “Pervasive” projects decreases. The pattern is less clear for the “Limited” and “Consistent” categories: for file-level adopters, the “Limited” category rises with deciles, and the “Consistent” category is stable; for projects detected via .gitignore or commits, the “Limited” category seems to rise with deciles, while the “Consistent” category seems to decrease, although the trends are noisier due to the smaller size of the sample.

For Age, the trends are less clear: the first decile tends to have a higher proportion of “Pervasive” projects (except for commit-only projects). Beyond the first decile, the trend appears to be relatively stable across all the categories.

If we compare to the file-level adoption, we see that if larger or more established projects have more file-level adoption, this does not translate to a higher level of commit adoption. This echoes the earlier finding that the correlation of the metrics is very low, but gives is addition insights. Adopters that are larger or more established seem to use coding agents in more limited settings than smaller projects. In terms of age, we still see a trend that younger projects are more extensive adopters, similar to the file-level adoption. Beyond that, the age of a project in itself does not appear to be correlated to the intensity of use of coding agents. While larger, more established projects have less adoption at the commit level, it is worth noting that a small but significant proportion of these projects have high levels of adoption: for instance, the proportion of “Pervasive” file-level adopters in the largest LOC decile is close to 5%.

A final remark is that the proportion of projects that have no AI-assisted commits is decreasing with deciles. The effect is particularly visible for the number of contributors. Given that each contributor can have their own setting and workflow for a coding agent, it is possible that projects with more contributors would have a higher probability that at least some of them leave visible traces, leading to this observed behavior.

7. RQ3: contexts of use of coding agents

We refine our analysis of adoption by looking at specific contexts: we start with the adoption in specific organizations, before looking at projects that have specific GitHub topics, before analysing adoption by programming languages.

7.1. Adoption in specific organizations 
Table 5. File-based adoption for top 20 organizations

Organization Adoption pct Repositories Organization Adoption pct Repositories

Microsoft 18.57% 964 Mozilla 4.05% 74

Google 6.76% 636 Automattic 20.00% 65

Apache 5.24% 534 Shopify 11.11% 63

Amazon 8.33% 420 Alibaba 12.28% 57

Hashicorp 2.26% 133 Rust 3.85% 52

Nvidia 7.21% 111 Kubernetes 2.04% 49

Meta 1.85% 108 Huggingface 12.24% 49

Grafana 18.09% 94 Symfony 4.08% 49

Jetbrains 10.00% 90 Tencent 2.08% 48

Elastic 4.82% 83 Cloudflare 20.45% 44

Since our dataset contains projects from large organizations, we were interested in seeing the variation in adoption across these. This is especially relevant since projects belonging to large organizations are generally more mature than other GitHub projects. To do so, we started with a list of the top 100 organizations according to gitstar-ranking 14 14 14 https://gitstar-ranking.com/organizations . We then manually grouped some organizations into groups representing companies (e.g., Microsoft, GitHub, Azure, DotNet are all parts of Microsoft). We then simply compute the file-level adoption ratio for the top twenty of these organizations (for each one, and overall). Over all the repositories in the top twenty organizations, file-level adoption is at 10.18%. For reference, the file-level adoption over all the repositories is 7.89%. This means that among open-source repositories of top organizations, there is a higher adoption of coding agents (a relative increase of ≈ \approx 29 %).

Looking at specific organizations, Table 5 shows the top 20 organizations and their file-level adoption rate. We can see that there are large variations, with some organizations well below the average. Meta is the lowest (1.85%); however, we know that they have deployed code completion tools internally (Murali et al. , 2023 ) . It is possible that the usage in internal repositories and external repositories is different. Other organizations, on the other hand, are well above the average, notably Microsoft, which, with a few other organizations, has close to double the mean adoption (18.57%); given that Microsoft, through GitHub Copilot, is itself a provider of a leading coding agent, there is certainly a strong interest in using coding agents in practice.

7.2. Adoption by topic

7.2.1. File-level adoption by topic 
Figure 4. Topics of GitHub projects showing file-based evidence of the adoption of coding agents, for topics associated to at least 350 projects (with file-based evidence of use). Each topic is plotted with adoption rate, i.e., ratio of projects using agents among projects with the same topic, on the X axis; and the number of projects using agents on the Y axis (log scale).

Figure 4 shows the GitHub topics of projects with evidence of file-based adoption of coding agents.
The figure focuses on the top topics in our dataset, i.e., it only shows topics associated to ≥ 350 \geq 350 projects (with file-based evidence of adoption); this threshold was chosen to have both a large enough number of project and sufficient legibility. Note that projects can, and often are, associated to multiple topics; hence a single project can contribute to multiple points in this visualization. For each retained topic we show: the adoption rate on the X axis, as a percentage of projects for that topic that use agents; and the number (frequency) of adopting projects on the Y axis, on a log scale. We filter out programming languages (which we see next), and split the figure in two sections to increase legibility.

The average adoption rate in this dataset is around 8%, and very scattered around topics (X axis).
It is below average, for topics like minecraft , system and network programming topics (e.g., those related to game engines, windows linux , or network protocols like http ). Even topics related to AI but on the more foundational side, like machine-learning and deep-learning are near the average. While some topics are below average, we stress that very few topics have extremely low adoption.

In between the average and around 17% (which is still far lower the upper-end of the scale, above 40%), we find several topics related to Web development (e.g., React, rest-api , wasm , electron ), others related to cloud and automation ( cloud , docker , terraform , devops ), as well as many specific database management systems.
We also see a few cross-cutting themes, and technologies, like open-source , dotnet , and vscode (the latter presumably related to coding agents integrated with the popular IDE).

Among the topics with highest adoption ratio (20%–60%) some entries can be interpreted as “dog fooding”, i.e., projects that either develop agents themselves (and use agents for agent development!), e.g.: agent .
Other high-adoption topics are for neighboring technologies, like mcp , but also ai , llm , chatgpt , and openai .
Other high-adopter topics are more surprising, like angular , nextjs , and ethereum ; the communities behind blockchains and some frontend Web development frameworks appear to be more likely to use coding agents than other technology communities.
Investigating why this is the case is beyond the scope of this paper, and left as interesting future work to pursue.

7.2.2. Commit-level adoption by topic 
Figure 5. Commit Ratio distribution by topic of commit-level adopters projects

Figure 5 shows the distribution of commit ratios among commit-level adopters categorized by topic.
In black, on the overall data, that is over all topics, we show in dotted lines the first and third quartiles and in solid line the median.
In red, we plot the same lines but for the specific topic. As earlier, we only consider projects with at least 10 post-adoption commits.

Unlike Figure 4 which shows a high discrepancy of file-level adoption depending on the topic, Figure 5 shows an homogeneous commit ratio across topics.
This observation confirms the data from Figure 3 , where we saw that the correlation between file-level and commit-level activity is very low: similarly, there appears to be little correlation between adoption rate based on topics, and commit ratio based on topics.
We would have thought that topics linked to AI, LLMs or agents had a higher commit ratio than other topics such as android or linux , but that is not the case, it is actually the opposite.
The topics openai and llm have a 30% file-level adoption rate whereas the median commit ratio at nearly 5% which is under the average median commit ratio among commit-level adopters. One possible reason for that developers for these topics have a higher awareness of the workings of coding agents, and are more likely to change their configuration, leading to a decrease in observable traces.

Instead, android which has close to 8% file-level adoption, has a median commit ratio of nearly 8%. This is also the case for linux , which had below average file-level adoption. The leaders in commit ratio are dotnet , claude , and docker which have median commit ratio a few percentage higher than the overall median. There is not a lot of variance by topic except for the claude topic which has a significantly higher third quartile compared to other topics.

7.2.3. Takeaway

The main takeaway of this analysis is that adoption is broad : at the file level, it spans a diversity of topics, with topics with very high adoption, but surprisingly few topics with very limited adoption. At the commit level, adoption is more uniform, showing again the diversity of topics in which coding agents are used.

7.3. Adoption by programming language 
Figure 6. Commit Ratio distribution by programming language of commit-level adopters projects

For programming languages we only show the commit-level data analysis, as it is much more precise. When computing commit ratio, we count commits that affect files belonging to a given programming language (identified by GitHub linguist). We only consider projects with at least 10 post-adoption commits, but apply this filter for the language of interest.

Figure 6 shows the distribution of commit ratios among commit-level adopters categorized by programming language.
In black, on the overall data, that is over all programming languages (i.e. the commit ratio among commits that change source code), we show in dotted lines the first and third quartiles and in solid line the median. In red, we plot the same lines but for the specific programming language.

The data shows some differences but overall most single programming languages see comparable commit ratios within ± \pm 10%.
Surprisingly, languages such as C, C++ or Rust who were expected to have lower commit ratios, due to their low-level nature, are in the middle of the pack, with close to the same median as all programming languages overall. Widely used languages such as Javascript, Python, Java have also median commit ratios close to the overall median.

Interestingly, some less popular languages such as Dart, Swift, or Kotlin, have commit ratios comparable to the most popular languages. This shows that coding agents have some usefulness beyond the very popular languages with ample training data. However, less established languages such as GraphQL, SCSS, Svelte and Elixir are trailing in median commit ratio compared to the others. Doing this analysis for additional languages would be interesting, but our filters reduce the number of repositories, preventing this analysis.

The leaders are Shell, HTML and PowerShell which have medians up to nearly 8% above the overall median. Shell languages are good use cases for coding agents: they typically are small-size scripts, in languages that are common, yet are used less frequently day-to-day by developers.

Notice that there is a high variance in commit ratio for most programming languages. Most commit-level adopters have commit ratios under the 20% but there are always some projects with very high commit ratio from 40% up to 100%. This is reflected in the upper quartile, which tends to be higher than in Figure 5 .

All in all, this analysis also comforts the idea that adoption is broad: it is not limited to a small subset of very popular languages, but extends also to less popular ones.

8. RQ4: evolution of adoption over time, and tool-specific adoption

In this section, we investigate the evolution of adoption over time, as well as the adoption of specific tools.

8.1. Evolution of adoption over time

Figure 7 presents the cumulative adoption of coding accross all the projects for which we could identify it. We record as adoption date the earliest date for which we have evidence of adoption, either through files or through commits. We can see several inflections point on the curve:

Figure 7. Cumulative adoption of any tool across all 10 344 projects from 2025-01-01 to 2025-11-03.

- •

At the end of February 2025, the slope increases, indicating a faster take-off; this corresponds to the initial release of Claude Code.

- •

The slope increases further around mid-May 2025; from then on the adoption occured at the fastest rate. Around this period, multiple coding agents were released (e.g. Codex, Gemini, Jules), which likely raised the popularity of the whole category.

- •

Finally, adoption seems to slow down slightly at the end of August 2025. However, the current slope is still higher than it was before the second inflection point.

Overall, we see a fast increase of adoption, with early signs of slowing down, consistent with an S-curve. It is however early to determine if that is the case; tracking the adoption over the next few months will be useful to confirm if the adoption is indeed slowing down. The current rate of increase of adoption is still in a decidedly onward slope.

8.2. Adoption per tool

Figure 8 shows the evolution of the adoption for the 48 specific tools that we track, via a two-panel ridgeline plot. Overall, the 10 344 projects have adopted 17 280 tools; thus some projects adopt multiple tools (we analyse this next).

We separate the visualization in two parts as there are wide differences in terms of popularity across tools. The left part shows the 6 most popular tools (all with more than 500 adopting projects), as well as an “other” category for the remaining tools. The right panel zooms in on this “other” category, specifically on the next 15 most popular tools (50 or more adopting projects). The remaining 34 tools that we identified are shown in the rightmost “other” category; these tools have a more limited adoption, but make a sizeable minority together.

Of note, the “Generic” category is made up of projects that use the AGENTS.md guidance file. This was initially the file used for the Codex coding agent; however, a standardization effort has started on this file format as the default guidance file for coding agents 15 15 15 https://agents.md . This is why we can no longer attribute it with certainty to Codex , although we suspect that the majority of its usage stems from Codex .

Figure 8 shows that a minority of tools show a significantly higher adoption than the rest. The top 5 tools (assuming most of Generic tool usage is Codex ) account for more than 80% of the overall adoption. Just Claude and Copilot are responsible for more than half of the adoption.

If we remove the 119 projects that adopt both (see Figure 9 ), and estimate that ≈ \approx 90% of the remainder is likely projects adopting Codex rather than other agents, we arrive at an estimate of 2200 to 2300 projects adopting Codex , which would place it in a clear third position behind Claude and Copilot .

In terms of trends, we clearly see all the inflection points on the Claude trendline. On the other hand, the trendlines of Copilot and Cursor and more regular. The trend for Codex , if we also account for the “Generic” trend, shows an interesting behaviour, since it rises more starting in August/September, unlike the remainder of the coding agents, and the overall trend. If this continues, it is possible that the slowdown we see in the general trendline does not materialize.

In the remainder of projects, we see different trends: some projects such as Aider, Devin, or Coderabbit have been available for longer (starting in 2024), and seem to rise steadily over time. Others (such as Kiro or Serena) are more recent agents, who may increase in popularity in the future.

Figure 8. Ridgeline plot showing adoption patterns for the top 48 tools, with Claude_Code being the most adopted (4 896 projects).

8.3. Co-adoption of coding agents

As mentioned earlier, the 10 344 projects have adopted 17 280 tools, representing more than 1.6 adopted agents per adopting project. As such, it is interesting to analyse the projects that have adopted more than one coding agent. We select the coding agents having at least 100 adopting projects, and count the number of co-occurrences of multiple agents.
Figure 9 presents an UpSet plot of the co-occurrences. An UpSet plot is similar to a Venn diagram, but can scale more gracefully as the number of categories increase (Lex et al. , 2014 ) .
The figure displays the number of projects that use multiple agents, filtering for cases where at least 30 projects adopt more than one combination of agents. Each agent is represented by a horizontal line. Each combination (ranging from one to four agents in the figure) is represented as a series of points, connected by a line if there are more than one coding agents in the combination. Simpler combination and more frequent combinations are on the left, so the figure starts with single usage of the most popular agents, and ends with the complex combinations. The plot also shows horizontal and vertical bar charts to show: 1) the count of projects using a particular agent in the horizontal bar chart, and 2) the count of projects using a particular combination in the vertical bar charts.

The figure shows that most projects (6 244 in total) use a single agent, but a significant minority has used more than one. Unsurprisingly, the most popular combinations involve the most popular agents (e.g. Copilot ∩ \cap Claude_Code (593)). It also shows that, as expected, the intersection between Codex and the “Generic” category is large: Codex ∩ \cap Generic (119). And it also gives insights on relatively popular combinations of three or four agents: Codex ∩ \cap Copilot ∩ \cap Claude_Code (45), Copilot ∩ \cap Claude_Code ∩ \cap Generic (111), and Codex ∩ \cap Copilot ∩ \cap Claude_Code ∩ \cap Generic (55), indicating that the amount of projects that likely use all of Claude , Copilot and Codex together, has around 200 projects. Another popular combination is Copilot ∩ \cap Claude_Code ∩ \cap Cursor (96). All in all, 397 use four difference agents, while 286 projects use five or more agents

Figure 9. UpSet plot showing tool co-adoption patterns among 14 tools with at least 30 projects per intersection.

8.4. Adoption evolution in organizations

Figure 10 shows the evolution of adoption across the larger organization in our dataset over time. Note that the list is different from the top 20 organizations we had earlier, as this one focuses on the organizations with the most adoption. We once again use a two-sided ridgeline plot.

Figure 10. Adoption patterns across 7 952 organizations, with microsoft leading at 251 adoptions.

We see that at the organization level, the adoption has a few distinct profiles. In particular some organizations, once they start to adopt coding agents, do so very quickly (e.g., Micronaut, Auth0), and in some cases, almost overnight (e.g., iobroker, Pulumi). Other organizations have a more regular adoption (e.g. Apache, Google).

We also see similar inflection points than in the overall adoption curve (Figure 7 . Notably, some organization start to adopt coding agents in February or March (e.g. Automattic, Antiwork, Posthog), and there is a significant takeoff in the May to July period (e.g. Getsentry, Datadog, Reown). The last months see slower adoption overall, save a few exceptions (e.g. Getsentry, Openshift, Grafana).

Very few top organizations had adoption as soon as January 2025: Microsoft is the exception, being the earliest and the largest overall adopter. Given that they are a provider of coding agents with Copilot, Microsoft certainly has some incentives to adopt it itself and serve as an example.

9. RQ5: Size of AI contributions

Beyond the commit ratio analysis, in this section, we compare the size of AI-assisted contributions with the size of human-written contributions. To do so, we measure the size of commits with three metrics: 1), the number of lines added in the commit; 2), the number of lines deleted in the commit; and 3), the number of files involved in the commit (added, deleted, modified, or renamed). We limit the number of metrics to simplify the presentation. We then use our heuristics to determine if a commit was authored by a human, a software bot, or was assisted by a coding agent. We do this analysis for all commits by file-level adopters that have commit-level adoption. This allows us to minimize the number of AI-assisted commits mislabelled as human contributions, although this mitigation is not perfect (e.g., a contributor may decide to stop their coding agent signing commits, while still using it).

Figure 11. Distribution for commit size in terms of lines and files by type of contribution.

Figure 11 shows the distribution of the commit sizes for the three types of commits. We clearly see that across all three metrics, Bots make smaller contributions than humans, whereas coding agents make larger ones. For instance, the median number of added lines for a human contribution is 10, while for a bot, it is only 3; on the other hand, for AI-assisted commits, it rises to 34, a value triple the median for humans, and closer to the third quartile of human contributions (41). The third quartile of AI-assisted contributions is considerably larger (119).

For deleted lines, the differences are not as stark: we see that the amount of deleted lines per commits for bots is smaller than the other two categories (median: 3), while AI-assisted contributions are larger (median: 7) than Human contributions (median: 5). The same is true at the file level. However, the metric being coarser, the differences are smaller: the median bot commit involves a single file, while both AI-assisted and human commits involve two files. Only in the upper part of the distribution do we see a difference (Q3 for humans: 3; for AI-assisted commits: 4).

Another way to look at the data is to categorize it into discrete size categories. Figure 12 shows the difference in the proportion of size categories for commits, focusing on human-authored and AI-assisted commits. The figure shows that the trend observed in Figure 11 is even more true at the edges of the distribution.

For line additions, the smallest category of commits (adding one to 5 lines) is 41% smaller when they are AI-assisted. On the other hand, the largest commits are almost twice as frequent for AI-assisted commits; this holds true even for commits that add more than 1,000 lines.

We see the same trend, albeit less pronounced, for line deletions: smaller commits (1 to 5 deleted lines) are 13.5% less frequent in AI-assisted commits, while the larger commits (thousands of deleted lines) are close to half as much more frequent. Files follow the same pattern, with single-file AI-assisted commits being close to 20% less frequent, while commits with more than 20 files are 30% more frequent.

Figure 12. Comparison between the frequency among size cetegories of human-authored and AI-assisted commits (lines added, lines deleted, and files involved).

In summary, AI-assisted commits tend to add more lines, in more files, than human-authored commits. In addition, and perhaps somewhat surprisingly, they also delete more code than human-authored commits. Taken together, these trends point towards an increased churn for AI-assisted commits, and for commits changing multiple files with increased frequency. This increased churn and non-local changes, in turn, brings questions on the sustainability of coding agents over time: further study is necessary to evaluate their impact on code quality.

10. RQ6: Types of commits authored by coding agents

As semi-autonomous development assistants, coding agents can contribute in various ways to code bases and support developers across multiple aspects of software development: fix bugs, write documentation, refactor code, write test cases, add new features, etc. Starting from the observation that the adoption of coding agents has surged, with this research question we now focus on which tasks agents perform: What kind of contributions, visible in version control system histories, do developers perform with the help of coding agents?

To answer this question, we qualitatively examine concrete contributions, at the granularity of individual commits, made by or with agents in git repositories that have adopted them, to better understand the tasks they are used for.

10.1. Dataset

Given the sheer amount of agent-authored commits in our adoption data and the cost of qualitative analysis, we resort to studying a random sample of commit-level contributions.
Among the coding agents identified in Section 8 , Claude Code leads in popularity (see Figure 8 ), which makes it a good candidate for qualitative analyzes.
Claude Code also defaults to annotating its commits with the Co-authored-by trailer, making the identification of its contributions at the commit level both practical and robust. 16 16 16 https://docs.claude.com/en/docs/claude-code/settings

From the 90,321 commits identified as Claude-authored in our adoption dataset, we draw a sample of 790 for further qualitative analysis using Cochran’s formula for categorical classification into seven categories with a 5% margin of error and a 95% confidence level (Goodman, 1965 ) .
We then adjust for the finite population size.
As our previous test used a confidence level of 99% and ran 9 statistical tests with p-values ¡ 10 − 16 10^{-16} , we apply Bonferroni’s correction (Rupert Jr and others, 2012 ) to adjust the interval from 95% to 96%, maintaining an overall 95% probability that all our results are correct.
These calculations yield a required sample size of 759 commits; we analyze 790 to be conservative.
For each commit, we extract the first line of the commit message, diff statistics (added and deleted lines and files), the kind of files impacted by the changes (source code, documentation, configuration, data), and the programming languages used in impacted files.

Table 6 shows some descriptive statistics of the sample.

Table 6. Descriptive statistics of the random sample of 790 commits authored by Claude Code, qualitatively analyzed to determine their type.

Metric Min. Med. Avg. Max.

Lines added 0 70 3743.0 1.6 M

Lines deleted 0 9 909.0 576 K

Files added 0 1 18.2 10.7 K

Files modified 0 1 3.7 138

Files deleted 0 0 3.0 1959

Type of Commit

changed files count

source code 573

documentation 296

data 287

configuration 202

other 68

build 17

image 4

Language of Commit count

changed files (top-10)

Markdown 254

TypeScript 213

XML 106

JSON 105

Python 102

YAML 92

JavaScript 73

Rust 57

Go 35

TOML 33

10.2. Protocol

As manually inspecting the code changes in a large set of commits is impractical (4,652 modified lines per commit on average in our sample), we classify commits based on the content of their messages.
In particular, we rely on the Conventional Commits specification, 17 17 17 https://www.conventionalcommits.org/en/v1.0.0/ a convention that has seen growing adoption over the past years which encodes the nature of the changes made in a commit within the commit message itself (e.g. feat for new features, fix for bug corrections, docs for documentation) (Zeng et al. , 2025 ) .
Originally designed to ease semantic versioning, it defines two core categories: fix for bug patching (corresponding to patch version increments) and feat for new features (corresponding to minor version increments).
In practice, this set of categories is open-ended and a popular extension is that of semantic commits, which defines seven types of tasks: chore , docs , feat , fix , refactor , style , and test . 18 18 18 https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716 A commit following that convention has a message prefixed with the name of one of these categories, followed by a colon (e.g. feat: Enable filtering clients per organization ).
This convention enables a structured and scalable way to infer the intent and type of work represented by each commit without examining the underlying code.
By leveraging this convention, we can analyze contribution patterns systematically and with reasonable confidence in the accuracy of the classification.

To our surprise, the majority of Claude commits in our sample already follows this convention: 513 of the 790 commits (65%) can automatically be classified into one of the seven categories by matching their prefix.
Indeed, coding agents may imitate the style of commit messages made by developers (in the current project or in their training data), or be explicitly instructed to follow that specific convention.
When a commit can be classified automatically, we retain the classification made by the agent or developer who made the commit.
Then, two authors were tasked to manually and individually classify the remaining 277 commits into one of the seven categories by inspecting their commit message and diff, with an initial agreement on 250 of the 277 commits (90%).
The remaining 27 commits were finally classified after discussion.

10.3. Results

In a recent study, Zeng et al. analyze 88,704 human-authored commit messages in 116 repositories from diverse domains following the Conventional Commit specification.
They find that chore commits are the most frequent (non-functional changes, including updating build scripts, dependencies, and continuous integration—31%), followed by fix (bug fixes—27%) and feat (implementation of new features—17%) (Zeng et al. , 2025 ) .

Table 7. Types of commits co-authored by Claude Code, for a random sample of 790 commits.
Commit types are from the semantic commit messages convention.
Commit classification performed by either parsing the first line of commit messages according to the Conventional Commits specification, version 1.0.0 (for the 513 commits that conform to it) or via manual review performed by two authors independently (for the remaining 277 commits).

Type Count Ratio (%)

feat 282 35.7%

fix 236 29.9%

docs 86 10.9%

refactor 78 9.9%

chore 56 7.1%

test 43 5.4%

style 9 1.1%

Total 790

This is in stark contrast with our sample of Claude commits, as shown in Table 7 .
Commits of types feat and fix are the most frequent in our sample, accounting for two thirds of the analyzed commits, while chore commits only account for 7.1%.
Notably, feature-introducing commits are about twice as common for agents as for humans.
This likely contributes to the pattern observed in Section 9 that AI-assisted commits tend to modify more lines and touch more files than human-authored ones.
For the remaining categories, the percentages differ by two percent or less between the study of Zeng et al. and ours, reflecting a similar distribution for these tasks between humans and agents.

Several factors might explain these differences.
As shown in Table 3 , while agent adoption spans the whole spectrum, it is the highest in younger projects, where the implementation of new features might be prioritized over bug fixing and maintenance tasks such as chore .
Besides, several chore tasks are already handled well by automated bots (e.g. dependabot for dependency management), so the cost of running agents might offset their benefits in this situation.
The low number of test commits doesn’t necessarily mean agents aren’t being used for testing.
The Conventional Commit specification requires choosing a single category, so tests added alongside a new feature might be included in a feat commit instead.
For example, commit d8d58f61 in nizos/tdd-guard ( feat: add AnthropicModelClient with API key configuration ) introduces a new feature together with corresponding test cases and is classified as a feat commit.
The proportion of standalone test commits is similar to the proportion found by Zeng et al. (Zeng et al. , 2025 ) .

Moreover, in line with the observation on contribution size, test commits, as well as other categories such as refactorings and documentation, despite being less common, can be quite large. For instance, commit 4a9dd8f adds extensive unit tests for two components (two files added, +488 lines of code); commit 3bcefd2 is a large refactoring that changes the structure of the code (and also adds some tests, 14 files changed; +912/-19 lines); commit f6315ff adds a high-level documentation of the structure of a module written in Zig, describing components, providing examples of use, with specific details on performance (one new file, 180 lines).

In summary, agents are used for a wide range of software development tasks, spanning the full set of categories defined by the Conventional Commits specification.
Compared with humans, however, agents are used more often to introduce new features and less often for long-term maintenance tasks such as dependency and continuous integration management.
These observations align with our previous findings about the age of agent-adopting projects and the size of the contributions attributed to them.

11. Discussion

We first discuss the limitations of our study, focusing in particular on the ways our study could either under-estimate or over-estimate adoption; we conclude that an under-estimate is more likely. We then discuss the implications of this work for practitioners and researchers, keeping in mind that it is likely we are under-approximating coding agent adoption.

11.1. Limitations

Generalizability of our findings

We took several precautions to maximize the external validity of our findings. We purposefully selected a large dataset of GitHub projects, selecting for projects that reach minimum size and activity requirements (5,000 lines of code; 100 commits). These minimum size and activity requirements are high enough to ensure we select projects that are more likely to reflect real programming activity, but low enough to increase diversity (e.g., including both small and large projects, projects with few and many contributors, that span many topics and programming languages). Further, after estimating adoption as a whole in RQ1, in RQ2 we analyzed our adoption metrics by relating them to other project characteristics (size; age; contributors; and activity indicators: commits, issues, pull requests) in order to better understand how adoption varied with these characteristics. However, we restricted these analyses to high-level metrics only, as carrying out similar analyses in the other RQs would have significantly lengthened the paper.

Similarly, we opted to exclude forks to avoid including copies of seemingly large projects, but with possibly limited activity. Finally, to increase the relevance of our findings to real-world coding scenarios, we specifically looked at the adoption from repositories of specific, established organizations.

Despite all of these mitigations, it is possible that our results do not translate well to more general use, and to industry in particular: we have reasons to think that industry use might be different than use in open-source. More generally, we have identified several reasons why our specific metrics could lead us to either over-estimate the adoption and use of coding agents, or on the contrary, to under-estimate it. We expand on these themes below. When relevant, we mention some of the perils of agent mining, that we identified and developed in another work (Robbes et al. , 2025 ) . In particular, many of the reasons for under or over-approximating agent activity stem from the Peril of Partial Observability.

Other limitations

The commit ratio, for reasons explained earlier, is an imperfect metric. It is particularly the case at the individual project level, where the observability depends on the choices of individual contributors. This is why refrain from studying projects in isolation. We assume that these kind of errors are evenly distributed when analyzing multiple projects, but we can not guarantee it. In particular, populations with a higher knowledge of coding agents may behave differently.

For the label analysis in RQ3, we are limited by the labels chosen by developers. A small minority of projects have such labels; moreover, many labels co-occur, which adds some degree of correlation between individual labels.

For the programming language analysis, we rely on GitHub Linguist. This is a proven solution, but in ideal scenarios, it uses both file names and file contents. This would not scale to our study, as we apply it to all committed files in 2025 for 129,134 projects; we limit GitHub linguist to file names and extensions, which makes it less precise. For instance, PHP is misclassified as one of its dialects, Hack. We tried to resolve the most important issues (i.e., Rust), but can not guarantee we found all the errors.

Pull requests that are “squash merged” condense multiple commits in a single one (Bird et al. , 2009 ) . If parts of the commits in the PR was AI-assisted, we are forced to label the entire merge commit as AI-assisted. This may lead us to over-estimate the size of the AI contributions when the proportion of AI-assisted commits in the PR is small. Aside from analyzing the diff, which is difficult at the scale of the analysis, the other option left would be to ignore these commits, which we found to be a worse tradeoff.

11.2. Reasons for over-estimating coding agent use

We first focus on the reasons why we could over-estimate adoption.

Under-use of agents

A large proportion of projects have evidence of coding agent use at the file level, but none at the commit level: only 54.14% of projects do; moreover, Figure 3 shows that the correlation between the metrics is very weak. This a manifestation of the Peril of Partial Observability, and we can not know to which extent agents are used in these projects. It is very likely that, after early experiments, some of these projects are not using coding agents, but we do not know the proportion.

Extent of the involvement of the agent

When we detect agentic activity, we can never be sure of the proportion of the activity that is due to the agent, due to the Peril of Partial Observability. In general, we can only observe the end result of the work (commits or pull requests). For a commit authored or co-authored by an agent, the involvement of the developer may range from the minimal (e.g. “vibe-coding”, or trusting the agent enough to give it extensive permissions and autonomy), to a very close oversight, closely reading the code, or even significantly editing it.

Similarly, when we identify agent activity in a pull request for an agent that does not sign their commit (such as Codex), we assume that all the commits from the initial author stem from the agent. However it is possible that only part of the commits were done by the agent, and follow-up work was performed by the developer. The Peril of Diversity (Robbes et al. , 2025 ) implies that there is a diversity of agent workflows, which makes tailoring heuristics for this difficult.

Size is not everything

In RQ5, we compare the size of the commits, finding that AI-assisted commits are larger in terms of lines added, lines deleted, and files involved. How this affects productivity is an open question, which we do not try to answer (we leave that to future work). For instance, the data is consistent with a high churn (lines added and quickly deleted), which might not translate to real productivity. Similarly, our analysis does not look at whether AI-assisted commits are more likely to be reverted (which we have seen on occasion), whether in other AI-assisted commits, or by humans. Computing churn in this way would require running origin analyses (Godfrey and Zou, 2005 ) at scale (particularly in case of extensive refactorings (Hora et al. , 2018 ) ), which is a significant endeavor.

11.3. Reasons for under-estimating coding agent use

On the other hand, there are several reasons why we may under-estimate the use of coding agents.

Absence of evidence is not evidence of absence

The flipside of the Peril of Partial Observability is that, for the projects in which we have no evidence of use (either at the commit level, or at the file level), there might very well be significant use of coding agents. First, there is the simple fact that some agents simply do not co-author commits; this is an implementation choice in the harness. For instance, Codex does not sign it commits, partly because its workflow is more based on pull requests. Second, if a coding agent signs their commits or leaves traces in pull requests, there can be ways to disable this behavior. For instance, there is a boolean setting to toggle this in Claude Code; and there is a similar setting to set the branch prefix that Codex uses. This makes it very easy to make their activity undetectable. Anecdotally, we have seen developers go to considerable lengths to disable this behavior even without using these settings, such as including extensive guidance instructing Claude Code not to sign commits, or setting up a GitHub action to auto-remove labels inserted by Codex. Finally, developers whishing more oversight may integrate agents in their workflow, but prefer to commit manually, after checking the agent’s contributions; we suspect this is a sizeable portion.

In addition, we rely on the presence of files to scale our search for coding agent usage, but we have also found that as many projects, if not more, have visible coding agent activity only in commits. Once again, this depends on both the coding agent and the developer workflow. Some agents, such as Devin, work primarily using a cloud setup, where they clone the project and handle their state without committing to the repository. Other agents such as Lovable or Vercel v0 19 19 19 Lovable: https://lovable.dev/ ; Vercel v0: https://v0.app are dedicated to fast prototyping, starting from an installation in the cloud, and as such are under-represented in Github repositories.

Some developers will avoid to have configuration files in their GitHub repositories, using specialized dotfiles repositories. Indeed we have several hundred such dotfiles repositories in our dataset (which we filter out to estimate overall adoption). To further improve our coverage of projects, we could check for the presence of agent configuration files in a dotfiles repository, and link it to other repositories the developer contributes in. However, this would significantly complexify our mining pipeline, and it would add noise: not every developer has a public dotfiles repository, and their agent use could be confined to a few of their repositories.

Missing heuristics

There is a large number of coding agents (Peril of Multiplicity (Robbes et al. , 2025 ) ), which is increasing, and the agents themselves are evolving (Peril of Velocity). Keeping track of all the coding agents, and finding appropriate heuristics for all of them, is a significant endeavor (rendered more complex by the Peril of Diversity: each agent works differently). We tried to be as thorough as possible, but we have almost certainly missed some agents, or at least some heuristics for a given agent. This will lead us to under-estimate the use of these specific agents. Related to this is the fact that some agents can use the guidance of others, making the identification of individual agents difficult. This is why, for instance, we can not attribute with 100% certainty all uses of AGENTS.md to Codex .

Unmerged commits

Our analysis focuses on the commits that are merged in the main branch. There is more use of coding agents in unmerged Pull Request and branches, which we do not consider as we focus on the contributions that end up in the main version of the project. These PRs can be unmerged for a variety of reasons: e.g., they are very recent and have not been reviewed yet; or, the agent’s work was subpar. We have occasionally seen pull requests that have been merged in non-conventional ways (e.g. manually), which our study can not detect. In addition, unmerged PRs can represent proof of concept or prototyping work, which might be useful even if the actual code does not last.

Things may be different in the industry

While it is well-known that studying open-source software is an imperfect proxy for industry software, it is particularly so for coding agents, due to their cost (Peril of Costs Shape Usage (Robbes et al. , 2025 ) ). Coding agents rely on long LLM inferences, over multiple turns, which is expensive. As a consequence, using coding agents most often requires a subscription, or metered API usage; free usage is limited to less powerful models and stricter rate limits. This means that industry developers may use coding agents more as part of a paid job (especially if it is subsidized by their employer), while open-source developers, who may not have such ease of access, may limit their usage. In addition, beyond the amount of usage, the kind of usages made possible by less restrained use may be different (e.g., using multiple agents in parallel). Anecdotally, developers running high coding agent bills (hundreds of dollars per month or more) are not unheard of, while some are curious about the possibilities offered by spending even more 20 20 20 For instance, this Shopify executive wondering how a developer may spend ca. 10,000 dollars a month on coding agents https://xcancel.com/fnthawar/status/1930367595670274058 . Thus, it is possible that the usage in industry is higher than in open-source. We tried to look into this by studying specific organizations, finding that they had higher file-level adoption in RQ3 (a relative increase of 29%). However, since this only based on public repositories, it likely does not reflect the internal usage.

11.4. Putting it all together

Considering all the reasons for undercounting and overcounting AI adoption, we think it is more likely that we are undercounting it. First, we think that projects adopting coding agents at the file level that have no AI-assisted commits are more likely to be using coding agents, rather than having abandoned them. This is because it is very easy to configure the main coding agents not to leave traces in commits or PRs, and because, for now, we can not account for developers that commit manually yet still use coding agents. While this is only anecdotal, there seem to be a non negligeable number of projects that fit these cases 21 21 21 For some clear cut cases that our heuristics nevertheless would miss, see the following examples: https://github.com/cloudflare/workers-oauth-provider , https://github.com/mitsuhiko/sloppy-xml-py , https://github.com/jackdoe/pico2-swd-riscv . While it is conceivable that projects with very limited and unchanging guidance have abandoned coding agents, it is less likely that projects with extensive and/or actively maintained guidance have done so.

We did a preliminary analysis of a related issue: after an initial usage, some projects experience a fall of their commit ratio to 0. A straightforward interpretation of this would be that such a project has abandoned coding agents. However, we found that on a sample of such projects (the 500 projects that had the largest commit ratio drop to zero), half of them had added or modified at least one agent guidance or configuration file after the commit ratio dropped to 0. It seems unlikely that a project that has abandoned coding agents would continue maintaining their coding agent guidance.

As another datapoint that fits with this narrative, consider Figure 5 , in which some topics have surprisingly low commit ratios (namely projects in the “agents”, “openai”, “ai”, or “llm” categories), despite these topics showing very high file-level adoption in Figure 4 . Rather than having a lower than average level of adoption, we hypothesize it is more likely that contributors to these projects, having more knowledge of coding agents, are more likely to be aware of how to change their settings and disable the visibility of their activity.

Second, given the high ratio of file-level activity that has no commit level activity, we think there is a sizeable proportion of “undetected use” of coding agents: projects that have neither file-level nor commit-level agent activity, yet still use agents. For instance, the projects mentioned in this earlier footnote 21 fit this profile, making us believe that the true adoption is higher than our conservative estimate. To be clear, this is so far only a hypothesis; future work should define heuristics to detect coding agent activity in these (and more challenging cases) with sufficient precision. Only such a study could determine with more certainty where the true adoption lies between our conservative and our high estimate, and could provide a more precise estimate of the AI-assisted commit ratio in adopting projects.

Finally, the third way adoption could be higher is the difference between open-source and industry, for the reasons mentioned above. Taken together, we think that these three factors make it more likely that: 1) for a sizeable subset of projects where we have detected activity, the true commit ratio is significantly higher than what we can measure; 2) some projects we classify as non adopters are actually adopters; and 3) adoption in private repositories from industry (on GitHub and elsewhere) is likely higher than OSS. While on the other hand, there is certainly a portion of projects that do have abandoned coding agents, we think the balance weights towards higher, rather than lesser adoption.

11.5. Implications

The adoption of coding agents is fast, and broad.

According to RQ1, our conservative estimate of coding agents is 15.85%, as of the end of October, 2025, while our high estimate is 22.60%. This is a technology that saw the light of day in 2024; it was confidential in 2024 and before the spring of 2025, when increase in model capabilities and the release of coding agents by major actors coincided with a drastic increase in adoption rate.

Moreover, if there are variations in adoption intensity in terms of project characteristics, project topic, or programming language, we can see that the adoption is broad :

- •

Adoption is not especially concentrated on smaller projects (be it measured in lines of code, contributors or commits). File-level adoption rather suggests the opposite, and commit-level adoption, even if less strong on such larger projects, is far from insignificant (“Pervasive” adopters are decreasing with size, but “Consistent” adopters are stable). Moreover, important organizations have high adoption of coding agents. There is, however, a bias towards younger projects.

- •

Likewise, adoption is not especially concentrated on particular types of projects. Some categories of projects may be more or less popular than the average, but there does not appear to be many categories that have near-zero adoption. This holds for both file-level and commit-level adoption. At the file level, some categories of projects are seeing much larger adoption, particularly in topics close to AI (a sort of “dogfooding” effect?), however, at the commit level even these categories see comparable usage to the rest.

- •

Finally, adoption is not especially concentrated on the small set of the most popular programming languages. Some less common languages (e.g., Dart, Ruby, Swift, PHP) see similar commit-level adoption to major languages. However, data is limited for the truly uncommon languages.

Coding agents are a step change from LLM-based code completion

Looking at the results of RQ5 and RQ6, we can infer that coding agents go beyond traditional LLM-based code completion. While LLM-based code completion helped developers write lines or blocks of code, the scope of coding agents is larger. This can be seen just by the size of AI contributions, which is clearly larger than human contributions: the median lines of code in an AI-assisted commit is triple that of human-authored ones; the proportion of very large AI-assisted commits (500 or more lines of code, or even more than 1000) is twice as frequent. AI-assisted commits are also larger in terms of deleted lines, and involved files. In addition, the type of contributions is telling: the most common type of contributions that we see in RQ6 are the implementation of features , indicating that coding agents are used in tasks spanning a relatively wide scope.

Note that, if, as we suspect, we are missing a sizeable proportion of AI-assisted commits, it is likely that the difference between the human and AI-assisted commits is larger , since those undetected commits are at the moment classified as human-authored commits.

Performance Outlook

If, as the adoption curve in RQ4 suggest, this trend continues, we can expect coding agents to become extremely common in 2026 or 2027.
This is even more the case, if, as we hypothesize, we are under-estimating, rather than over-estimating, the adoption of coding agents. Related to this is the increase of capabilities of the underlying models: much as stronger models were a contributing factor to the adoption of coding agents in 2025, similar increases could drive the adoption further in 2026 and beyond. The Anthropic economic index (Anthropic, 2025 ) finds that a growing number of tasks are delegated to LLMs, pointing at increased autonomy. Similarly, recent work (Kwa et al. , 2025 ) looks at 50% and 80%-task-completion time horizon for agents (the time humans typically take to complete tasks that AI models can complete with 50%/80% success rate). They observe that, historically, the task completion time has been doubling every 7 months. This increased autonomy, due to evolving model capabilities, is consistent with the way coding agents work in the ideal cases, and is consistent with the increased adoption we observe in Figure 7 .

The use of coding agents in practice should be studied extensively

Taken together, the previous three observations come to an important implication. Coding agents, making large contributions are adopted quickly, broadly and sometimes very extensively (a small but non-negligeable proportion of projects have a very high ratio of AI-assisted commits). We have reasons to expect this trend to continue further. Therefore, it is extremely important to study their impact in practice, in order to provide actionable advice to practitioners.

Since the emergent of practical coding agents is very new, the body of work so far is very limited (see Section 2 ). Given the speed of the phenomenon, we argue that the research community should study this with urgency; we hope that the initial strides we made in this field will be helpful for others 22 22 22 we will share all the datasets and analyses that we made to facilitate this . While many aspects can be studied, we have identified a few we wish to highlight:

- •

While the large contributions of coding agents can be seen as an indicator of productivity, the large amount of deleted code is an indicator of churn, which has been traditionally associated with defects (Nagappan and Ball, 2005 ) . It is thus important to investigate to which extent coding agents cause high code churn, and what its consequences are. There is already evidence that AI-assisted development in general contributes to high code churn (Harding and Kloster, 2024 ; Harding, 2025 ) . In addition, recent work points at emerging quality issues associated with the use of coding agents (He et al. , 2025 ) .

- •

On the other hand, perhaps such a high churn is not always problematic. Coding agents, by making code extremely cheap to write, can enable scenarios that were not possible before (e.g., prototyping multiple variants of a solution to a problem, before making a more informed decision). In essence, coding agents greatly facilitate the creation of disposable, exploratory code, which may have a very short, but very useful, life. Characterizing these scenarios would be valuable future work.

- •

More generally, we think it is valuable to study the minority of extreme adopters of coding agents (those that we identify as having very high commit ratios). These adopters may give us early signals that could be useful to the broader community. They might act as “canaries in a coal mine”, or cautionary tales for prospective users of coding agents. On the other hand, they might help discover new usages of coding agents that may be useful to the community at large.

- •

An essential component of coding agents is their guidance. As we have seen in RQ2, the amount of guidance used, and its update frequency, varies by several orders of magnitude, from the most basic to the most sophisticated. Detailed studies of this guidance, what it contains, and how it is used, will be essential to better understand how it impacts the behavior of coding agents. There is very early work in classifying the type of guidance (Mohsenimofidi et al. , 2025 ) .

- •

Last but not least, underlying all of this is the identification of coding agent activity that we are not able to detect at the moment. There is considerable future work in devising heuristics to detect this activity, and strengthen the body of work that will be based on this.

A call for clear attribution

To study the use of coding agents in the best conditions, proper identification is essential. While we think detecting agent activity is an important avenue for future research, an even more effective solution would be to reliably document it. This is why we call on the practitioners to document, rather than hide, their use of coding agents. We also call on providers of coding agents to continue their standardization efforts, while defining mechanisms to identify individual coding agents.

12. Conclusion

Coding agents based on LLMs appeared in 2024, and took off in 2025. This work presented a study of the adoption of coding agents in GitHub projects. We find that, as of the end of October 2025, between 15.85% and 22.60% of projects in a large dataset of 129,134 GitHub projects show traces of use of coding agents. We find that this adoption was fast (it happened mainly from March to October 2025), broad (it includes all kinds of projects, in a variety of programming languages and organizations), and is still increasing. At the commit level, we find that a sizeable proportion of projects exhibit “Consistent” (5 to 20%) or even “Pervasive” use (more than 20%); a small, but non-negligible proportion of projects show extreme use. Moreover, we find that coding agents are used to implement features and bugs fixes, and do so via large contributions (larger than humans). These findings have implications both for the practice, which is seeing a very rapid transition towards coding agents, and for researchers, which should study this phenomenon in order to provide advice to practictioners during this transition.

References

- Anthropic (2025) Anthropic economic index: uneven geographic and enterprise ai adoption . Technical report Anthropic PBC . Note: Report, 15 Sept 2025 External Links: Link Cited by: §11.5 .

- O. Asare, M. Nagappan, and N. Asokan (2023) A user-centered security evaluation of copilot . arXiv preprint arXiv:2308.06587 . Cited by: §3.1 .

- S. Barke, M. B. James, and N. Polikarpova (2023) Grounded copilot: how programmers interact with code-generating models . Proceedings of the ACM on Programming Languages 7 ( OOPSLA1 ), pp. 85–111 . Cited by: §3.1 .

- J. Becker, N. Rush, E. Barnes, and D. Rein (2025) Measuring the impact of early-2025 ai on experienced open-source developer productivity . arXiv preprint arXiv:2507.09089 . Cited by: §1 , §3.2 .

- C. Bird, P. C. Rigby, E. T. Barr, D. J. Hamilton, D. M. German, and P. Devanbu (2009) The promises and perils of mining git . In 2009 6th IEEE International Working Conference on Mining Software Repositories , pp. 1–10 . Cited by: §11.1 , item 4 .

- I. Bouzenia and M. Pradel (2025) Understanding software engineering agents: a study of thought-action-result trajectories . arXiv preprint arXiv:2506.18824 . Cited by: §3.2 .

- N. Chowdhury, J. Aung, C. J. Shern, O. Jaffe, D. Sherburn, G. Starace, E. Mays, R. Dias, M. Aljubeh, M. Glaese, C. E. Jimenez, J. Yang, L. Ho, T. Patwardhan, K. Liu, and A. Madry (2024) Introducing SWE-bench verified . External Links: Link Cited by: §3.2 .

- W. G. Cochran (1977) Sampling techniques . 3rd edition , John Wiley & Sons , New York . External Links: ISBN 978-0471162407 Cited by: §4.2.5 .

- R. D. Cosmo and S. Zacchiroli (2017) Software heritage: why and how to preserve software source code . In Proceedings of the 14th International Conference on Digital Preservation (iPRES 2017) , pp. 1–10 . External Links: Document , Link Cited by: §4.2.1 .

- O. Dabic, E. Aghajani, and G. Bavota (2021) Sampling projects in github for msr studies . In 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR) , pp. 560–564 . Cited by: §4.2.1 .

- M. W. Godfrey and L. Zou (2005) Using origin analysis to detect merging and splitting of source code entities . IEEE Transactions on Software Engineering 31 ( 2 ), pp. 166–181 . Cited by: §11.2 .

- L. A. Goodman (1965) On simultaneous confidence intervals for multinomial proportions . Technometrics 7 ( 2 ), pp. 247–254 . Cited by: §10.1 .

- W. Harding and M. Kloster (2024) Coding on copilot: 2023 data suggests downward pressure on code quality . Note: Accessed on 03 24, 2024 External Links: Link Cited by: 1st item , §3.1 .

- W. Harding (2025) AI copilot code quality: evaluating 2024’s increased defect rate via code quality metrics . Note: Accessed on October 13th, 2025 External Links: Link Cited by: 1st item , §3.1 .

- H. He, C. Miller, S. Agarwal, C. Kästner, and B. Vasilescu (2025) Speed at the cost of quality? the impact of llm agent assistance on software development . arXiv preprint arXiv:2511.04427 . Cited by: 1st item , §3.2 .

- A. Hora, D. Silva, M. T. Valente, and R. Robbes (2018) Assessing the threat of untracked changes in software evolution . In Proceedings of the 40th International Conference on Software Engineering , pp. 1102–1113 . Cited by: §11.2 .

- S. Imai (2022) Is github copilot a substitute for human pair-programming? an empirical study . In Proceedings of the ACM/IEEE 44th International Conference on Software Engineering: Companion Proceedings , pp. 319–321 . Cited by: §3.1 .

- M. Izadi, J. Katzy, T. Van Dam, M. Otten, R. M. Popescu, and A. Van Deursen (2024) Language models for code completion: a practical evaluation . In Proceedings of the IEEE/ACM 46th International Conference on Software Engineering , pp. 1–13 . Cited by: §3.1 .

- C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. R. Narasimhan (2024) SWE-bench: can language models resolve real-world github issues? . In The Twelfth International Conference on Learning Representations,
ICLR 2024, Vienna, Austria, May 7-11, 2024 , Cited by: §3.2 .

- A. Kumar, Y. Bajpai, S. Gulwani, G. Soares, and E. Murphy-Hill (2025) Sharp tools: how developers wield agentic ai in real software engineering tasks . arXiv e-prints , pp. arXiv–2506 . Cited by: §1 , §3.2 .

- T. Kwa, B. West, J. Becker, A. Deng, K. Garcia, M. Hasin, S. Jawhar, M. Kinniment, N. Rush, S. Von Arx, et al. (2025) Measuring ai ability to complete long tasks . arXiv preprint arXiv:2503.14499 . Cited by: §1 , §11.5 .

- A. Lex, N. Gehlenborg, H. Strobelt, R. Vuillemot, and H. Pfister (2014) UpSet: visualization of intersecting sets . IEEE Transactions on Visualization and Computer Graphics 20 ( 12 ), pp. 1983–1992 . External Links: Document Cited by: §8.3 .

- H. Li, H. Zhang, and A. E. Hassan (2025) AIDev: studying AI coding agents on GitHub . Note: https://doi.org/10.5281/zenodo.16919051 Accessed 2025-10-21 Cited by: §3.2 .

- J. T. Liang, C. Yang, and B. A. Myers (2024) A large-scale survey on the usability of ai programming assistants: successes and challenges . In Proceedings of the 46th IEEE/ACM International Conference on Software Engineering , pp. 1–13 . Cited by: §3.1 .

- S. Mohsenimofidi, M. Galster, C. Treude, and S. Baltes (2025) Context engineering for ai agents in open-source software . arXiv preprint arXiv:2510.21413 . Cited by: 4th item , §3.2 .

- H. Mozannar, G. Bansal, A. Fourney, and E. Horvitz (2022) Reading between the lines: modeling user behavior and costs in ai-assisted programming . arXiv preprint arXiv:2210.14306 . Cited by: §3.1 .

- V. Murali, C. Maddila, I. Ahmad, M. Bolin, D. Cheng, N. Ghorbani, R. Fernandez, and N. Nagappan (2023) CodeCompose: a large-scale industrial deployment of ai-assisted code authoring . arXiv preprint arXiv:2305.12050 . Cited by: §3.1 , §7.1 .

- N. Nagappan and T. Ball (2005) Use of relative code churn measures to predict system defect density . In Proceedings of the 27th international conference on Software engineering , pp. 284–292 . Cited by: 1st item .

- A. Osmani (2025) The reality of ai-assisted software engineering productivity . Note: Substack blog post“What the data really shows about AI coding tools in 2025.” External Links: Link Cited by: §6.2 .

- S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer (2023) The impact of ai on developer productivity: evidence from github copilot . arXiv preprint arXiv:2302.06590 . Cited by: §3.1 .

- N. Perry, M. Srivastava, D. Kumar, and D. Boneh (2023) Do users write more insecure code with ai assistants? . In Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security , pp. 2785–2799 . Cited by: §3.1 .

- R. Robbes, T. Matricon, T. Degueule, A. Hora, and S. Zacchiroli (2025) Promises, perils, and (timely) heuristics for mining coding agent activity . Under submission . Cited by: §1 , §11.1 , §11.2 , §11.3 , §11.3 , §2.2 , §4.1 .

- G. Rupert Jr et al. (2012) Simultaneous statistical inference . Cited by: §10.1 .

- G. Sandoval, H. Pearce, T. Nys, R. Karri, S. Garg, and B. Dolan-Gavitt (2023) Lost at c: a user study on the security implications of large language model code assistants . In 32nd USENIX Security Symposium (USENIX Security 23) , pp. 2205–2222 . Cited by: §3.1 .

- K. Stol and B. Fitzgerald (2018) The abc of software engineering research . ACM Transactions on Software Engineering and Methodology (TOSEM) 27 ( 3 ), pp. 1–51 . Cited by: §1 , §4 .

- R. Tufano, A. Mastropaolo, F. Pepe, O. Dabić, M. Di Penta, and G. Bavota (2024) Unveiling chatgpt’s usage in open source projects: a mining-based study . arXiv preprint arXiv:2402.16480 . Cited by: §3.1 .

- E. R. Tufte (2004) Sparkline theory and practice . Note: Online article“A small, intense, word-sized graphic with typographic resolution.” External Links: Link Cited by: §6.2 .

- P. Vaithilingam, T. Zhang, and E. L. Glassman (2022) Expectation vs. experience: evaluating the usability of code generation tools powered by large language models . In Chi conference on human factors in computing systems extended abstracts , pp. 1–7 . Cited by: §3.1 .

- R. Wang, R. Cheng, D. Ford, and T. Zimmermann (2023) Investigating and designing for trust in ai-powered code generation tools . arXiv preprint arXiv:2305.11248 . Cited by: §3.1 .

- Y. Wang, M. Pradel, and Z. Liu (2025) Are” solved issues” in swe-bench really solved correctly? an empirical study . arXiv preprint arXiv:2503.15223 . Cited by: §3.2 .

- C. S. Xia, Y. Deng, S. Dunn, and L. Zhang (2024) Agentless: demystifying llm-based software engineering agents . arXiv preprint arXiv:2407.01489 . Cited by: §3.2 .

- T. Xiao, Y. Fan, F. Calefato, C. Treude, R. G. Kula, H. Hata, and S. Baltes (2025) Self-admitted genai usage in open-source software . CoRR abs/2507.10422 . External Links: Link , Document , 2507.10422 Cited by: §3.1 .

- Q. Zeng, Y. Zhang, Z. Qiu, and H. Liu (2025) A first look at conventional commits classification . In Proceedings of the IEEE/ACM 47th International Conference on Software Engineering , pp. 2277–2289 . Cited by: §10.2 , §10.3 , §10.3 , §10.3 .

- Y. Zhang, H. Ruan, Z. Fan, and A. Roychoudhury (2024) Autocoderover: autonomous program improvement . In Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis , pp. 1592–1604 . Cited by: §3.2 .

- A. Ziegler, E. Kalliamvakou, X. A. Li, A. Rice, D. Rifkin, S. Simister, G. Sittampalam, and E. Aftandilian (2022) Productivity assessment of neural code completion . In Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming , pp. 21–29 . Cited by: §3.1 .
