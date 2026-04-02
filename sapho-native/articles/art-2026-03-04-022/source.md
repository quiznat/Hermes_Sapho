---
version: source-capture.v1
article_id: art-2026-03-04-022
ticket_id: ticket-import-art-2026-03-04-022
source_url: https://arxiv.org/abs/2512.18925
canonical_url: https://arxiv.org/abs/2512.18925
source_title: An Empirical Study of Developer-Provided Context for AI Coding Assistants
  in Open-Source Projects
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-30T17:55:40Z'
linked_paper_urls: []
---
# Source Capture

## Title

An Empirical Study of Developer-Provided Context for AI Coding Assistants in Open-Source Projects

## Body

An Empirical Study of Developer-Provided Context for AI Coding Assistants in Open-Source Projects

Shaokang Jiang shj@uci.edu University of California, Irvine Irvine California USA and Daye Nam daye.nam@uci.edu University of California, Irvine Irvine California USA

(2025)

Abstract.

While Large Language Models (LLMs) have demonstrated remarkable capabilities, research shows that their effectiveness depends not only on explicit prompts but also on the broader context provided. This requirement is especially pronounced in software engineering, where the goals, architecture, and collaborative conventions of an existing project play critical roles in response quality. To support this, many AI coding assistants have introduced ways for developers to author persistent, machine-readable directives that encode a project’s unique constraints. Although this practice is growing, the content of these directives remains unstudied.

This paper presents a large-scale empirical study to characterize this emerging form of developer-provided context. Through a qualitative analysis of 401 open-source repositories containing cursor rules, we developed a comprehensive taxonomy of project context that developers consider essential, organized into five high-level themes: Conventions, Guidelines, Project Information, LLM Directives, and Examples. Our study also explores how this context varies across different project types and programming languages, offering implications for the next generation of context-aware AI developer tools.

† † copyright: acmlicensed † † journalyear: 2025 † † doi: XXXXXXX.XXXXXXX † † conference: Make sure to enter the correct
conference title from your rights confirmation email; June 03–05,
2025; Woodstock, NY † † isbn: 978-1-4503-XXXX-X/2025/06 † † copyright: none † † ccs: Software and its engineering Software development techniques † † ccs: Human-centered computing Empirical studies in HCI

1. Introduction

Research has consistently shown that the effectiveness of Large Language Models (LLMs) is highly
dependent not only on the direct prompts they receive ( brown2020language ) but also on the broader context in which
those prompts are situated ( lewis2020retrieval ; shaikh2024aligning ) .
Context serves as the critical mechanism for guiding an LLM, influencing the quality and relevance
of its output and aligning the model with user expectations.

While this principle applies universally, the need for precise and structured context is particularly
pronounced in software engineering ( zhang2025coderag ; wang2025coderag ) .
This distinction arises from the inherent nature of software development tasks.
A developer’s work is rarely self-contained;
it is a goal-oriented task that must, in most cases, integrate into an existing project ( begel2010codebook ) .
Furthermore, since most real-world software is built by collaborative teams, any new contribution
must adhere to a shared set of conventions, including style guides, design patterns, and established
processes, to ensure the codebase remains readable, consistent, and maintainable ( bird2011sociotechnical ; storey2014revolution ) .
Consequently, the context needed to guide an AI in these tasks could better be less about general knowledge
but more about a rich set of prescriptive constraints around goal-oriented tasks.

This rule provides standards for frontend components:
 When working in components directory:
 - Always use Tailwind for styling
 - Use Framer Motion for animations
 - Follow component naming conventions

This rule enforces validation for API endpoints:
 In API directory:
 - Use zod for all validation
 - Define return types with zod schemas
 - Export types generated from schemas 
Figure 1 . Example cursor rule illustrating project conventions and usage constraints ( cursor2025rules )

While early research has focused on helping developers more effectively prompt LLMs for code generation ( nam2025promptingllmscodeediting ; yang2025prompts ; pickering2025howhumans ) ,
more recently, developer-authored project-specific directives for AI agents have
emerged as an effective approach ( cursor2025rules ; windsurf2025rules ; copilot2025rules ) .
These “rule files,” exemplified by the cursor.md files in the Cursor IDE (See Figure 1 ),
are distinct from ephemeral, single-shot prompts; they are authored by the end-user for
a machine collaborator, with the purpose of providing global context.

While the practice of authoring these AI directives is growing, their content remains unstudied.
Excessive or unoptimized context can lead to more complex and less accurate responses, as well as higher costs and latency. A lack of systematic understanding of what developers consider important, and what common patterns exist for their AI assistants, can result in ineffective use of these tools. Thus, developing such an understanding is crucial for improving the design and usability of AI coding assistants.

Figure 2 . Taxonomy of context types in cursor rules.

This paper presents a large-scale empirical study to characterize this new form of developer-provided context. We conducted a qualitative study of a curated dataset of 401 open-source repositories containing developer-authored rule files, seeking to understand what aspects developers consider essential for AI first. And then, we explored how this context varies across different project types and programming languages.

Our analysis reveals that developers provide a rich variety of context types, which we organized into five high-level themes: Conventions, Guidelines, Project Information, Examples and LLM Directives. We also found that many of the rules overlap with existing software documentation practices, such as contribution guidelines and project overviews, suggesting that developers are adapting traditional documentation norms to the new context of AI-assisted development. Meanwhile, we observed unique patterns specific to AI directives, such as explicit instructions targeted at LLM behavior, which have no direct analog in human-oriented documentation but more closely resemble prompt engineering techniques.

The contributions of this paper are threefold:

- •

We present a large-scale empirical study of developer-authored rule files for AI coding assistants,
providing a systematic characterization of the types of context developers consider essential.

- •

We developed a comprehensive taxonomy of context types ( Figure 2 ), organized into five high-level themes,
which can inform the design of future context-aware AI developer tools.

- •

We explored how context provision varies across different project types and programming languages,
offering insights into the different needs of software developers when working with AI assistants.

2. Backgrounds and Related Work

2.1. Context Engineering

In recent years, with the advancement of LLMs, context engineering has become a critical area of research. Many studies have shown that the performance of LLMs is highly dependent on how tasks are communicated, i.e., prompt engineering, and the context provided to the model ( feldman2024ragged ; kojima2022large ) . Significant attention has been given to different prompting techniques, such as chain-of-thought prompting ( wei2022chain ; kojima2023large ) , self-consistency ( wang2023self ) , zero-shot ( kojima2022large ) , and few-shot learning ( brown2020language ) . These techniques demonstrate that providing examples or instructions in the prompt can significantly improve model performance on various tasks.
Retrieval-augmented generation ( lewis2020retrieval ; guu2020retrieval ; shuster2021retrieval ) also has been widely adopted to enhance context by incorporating relevant information from external sources, such as documents or databases, into the model’s input. This approach allows LLMs to access a broader range of information and improve their performance on specific tasks. More recently, efforts have focused on creating more structured and persistent forms of context that can be easily retrieved and utilized by the model during interactions. One promising direction is the development of memory-augmented models, which can maintain a long-term memory of past interactions and user preferences ( shaikh2024aligning ; zhang2018personalizing ) to provide personalized and context-aware responses.

A similar idea has also been explored in the software engineering domain, where researchers have investigated various techniques to augment the context provided to LLMs for code generation and understanding tasks.
For example, Mathews et al. ( mathews2024test ) found that including test cases enhances function-level code generation in benchmarks such as MBPP ( austin2021program ) and HumanEval ( chen2021evaluating ) .
Jiang et al. ( jiang2024self ) showed that dividing the coding process into planning and implementation phases provides valuable guidance for large language models.
Similar ideas were demonstrated to be useful for code summarization ( ahmed2024automatic ) , repository-level code completion ( li2024enhancing ) , and program repair ( autorecover ) .
RAG has also been applied in software engineering tasks, where relevant code snippets, documentation, and abstraction information are retrieved to supplement the model’s context ( zhong2025rag ; zhang2025coderag ; liu2024graphcoder ; rag6 ) . This has allowed LLMs to access a broader range of information and improve their performance on code-related tasks. However, most approaches have focused on enhancing LLM performance in tasks that are well-defined and self-contained, such as code completion or code summarization, as covered by existing benchmarks.

Research in IDE settings, where many real-world users interact with LLMs for software development tasks, is still limited. Most efforts are driven by industry players, such as GitHub Copilot ( copilot2025rules ) and Cursor ( cursor2025rules ) . Although not formally studied, these tools have introduced various techniques to provide context to LLMs in IDE settings, such as retrieving open files, linter errors, or allowing developers to specify files or code snippets. needmorecontext conducted a survey of 131 software professionals using LLMs for coding tasks and found that more context is necessary, but did not identify what specific context is needed. Similarly, contextnotpersonalized found that contextual information is helpful, but LLMs may not know where to focus.

The purpose of providing context to LLMs should not focus solely on fixing coding errors or improving coding accuracy. Other aspects—such as workflow, usability, maintainability, communication, and alignment with project goals—are equally important in software development, yet have not been well studied in prior work. developerneed1 conducted a large-scale difference-in-differences study of Cursor’s impact on software projects and found that projects adopting Cursor suffered from an increase in static analysis warnings and code complexity, indicating higher technical debt in the future. Several studies have assessed the usability issues of AI coding assistants ( developerneed2 ; developerneed3 ) , finding that developers often struggle to effectively use AI coding assistants for certain tasks, such as generating test cases or writing natural language artifacts in interview settings. Other studies have attempted to build fully automated AI coding assistants with predetermined workflows ( fullyautomate3 ; fullyautomate1 ; fullyautomate2 ) , but these typically do not consider that workflows may vary significantly across disciplines or projects. Multi-agent systems have also been proposed to handle complex software engineering tasks; nevertheless, these approaches often emphasize the need for more explicit context from developers to guide the agents ( agentneedcontext ) , or rely on fabricated context ( lackcontext ) . However, previous studies may have failed to recognize what developers actually need or want to convey to AI coding assistants in real-world settings. Our study is the first to systematically investigate the context developers consider essential when working with AI coding assistants in real-world software projects, using cursor rule files as a proxy.

2.2. Rules for AI Coding Assistants

Many AI coding assistants have introduced ways for developers to author system-level instructions that provide globally available context, preferences, or workflows for the underlying AI agents to follow. These directives, often referred to as “rule files,” can include project-specific, team-level, or user-specific guidelines that guide the behavior of AI coding assistants. For example, Cursor, an AI-powered code editor, allows developers to create “cursor rules” in ‘.mdc‘ files that specify guidelines and constraints for code generation ( cursor2025rules ) . Because LLMs, by default, do not retain memory between sessions and may not know where to focus when generating code, these rules provide a way to persistently encode important context that the LLM should consider. When a developer includes these rules in their project, AI coding assistants can incorporate them as part of the context when generating responses, leading to more relevant and accurate suggestions.

Other AI coding assistants have also introduced similar features. For example, GitHub Copilot allows developers to define custom instructions that guide the behavior of the AI assistant. Several CLI tools, such as Claude CLI and Continue CLI, also integrate similar custom instruction features at the personal, project, and global levels. Some rules for these other AI coding assistants focus on integrating third-party tools, such as creating issues, running tests, or deploying code, into the agent workflow. In this paper, we focus solely on text-based rules that provide context for LLMs.

2.3. Documentation and Communication in Software Engineering

Software engineering is an information-intensive and collaborative activity, making effective documentation and communication critical to the success of software projects. Numerous studies have investigated various aspects of software documentation, including the types of information developers seek ( brandt2009two ; maalej2013patterns ; freund2015contextualizing ; meng2018application ) , as well as tools and techniques to improve documentation practices ( robillard2011field ; aghajani2019software ) . For example, Maalej and Robillard ( maalej2013patterns ) conducted a large-scale study of API documentation and identified common patterns of information needs among developers, finding twelve distinct types of information frequently sought in API documentation. Similarly, other studies have explored the types of knowledge used in GitHub README files ( prana2019categorizing ; fronchetti2023contributing ) , categorizing the information developers use when collaborating on open-source projects. These studies have provided valuable insights into the information needs of developers and the challenges they face in accessing and utilizing documentation effectively. While we have a good understanding of the types of information developers need and provide when working with human collaborators, less is known about how they communicate with AI agents. Since AI coding agents have only recently become widely adopted and started to be considered collaborators, the ways developers document their needs for these agents remain largely unexplored. In this paper, we build upon prior work by focusing specifically on the context provided by developers for AI coding assistants, and how this context differs from traditional documentation practices.

3. Methodology 
Figure 3 . Overview of the qualitative coding process used to develop the taxonomy of cursor rule
codes and the coded rules for quantitative analysis.

To understand the types of context developers provide when authoring cursor rules, we conducted a qualitative study of cursor rules from real-world open-source software repositories. A brief overview of our coding process is illustrated in Figure 3 . We selected cursor rules because they were among the earliest to introduce this feature, have been widely adopted in the open-source community, and are frequently discussed in developer forums such as Reddit 1 1 1 https://www.reddit.com/r/cursor/comments/1ju63ig/the_one_golden_cursor_rule_that_improved/ and Hacker News 2 2 2 https://news.ycombinator.com/item?id=43305919 .

3.1. Data Collection and Preprocessing

Data Fetching. For data fetching, we used Sourcegraph 3 3 3 https://sourcegraph.com/ client.
Sourcegraph is an open-source code search tool that indexes all public GitHub repositories with at least one star, providing a good representation of the most popular open-source repositories on GitHub.
We fetched repositories containing at least one cursor rule file (i.e., with the .mdc extension),
excluding any forked or archived repositories, which resulted in 487 repositories.
We cloned all the repositories locally and fetched metadata using GitHub’s official API for further analysis.

Data Cleaning. We removed 15 repositories that did not contain any .mdc files after cloning (e.g., the files may have been deleted in later commits).
We then manually checked the content of the remaining repositories and removed 11 repositories
whose .mdc files were used for other purposes, such as SD card configuration.
Next, we manually checked whether the .mdc files in the remaining repositories were written
in English and removed 43 repositories that were not.
This left us with 418 repositories for further analysis.

Since some repositories contained only empty data or were exact duplicates of others,
we removed 12 such repositories after manual review.
Additionally, some repositories included only template or example .mdc files intended for others to use,
such as awesome-cursor-rules-mdc 4 4 4 https://github.com/PatrickJS/awesome-cursorrules .
Because the main purpose of our study is to analyze the usage of cursor rules in real-world applications,
we removed five such repositories after manual review, leaving 401 repositories for further analysis.

3.2. Dataset

The 401 collected repositories containing cursor rules were created between 2008 and 2025, with the median creation date in 2023. The average repository size was 219.7 MB (SD = 727.6), with the largest repository being 12.63 GB. All collected repositories contained an average of 5,511.27 commits (SD = 11,201.06) per repository. Among all repositories, 291 (72.57%) were created under an organization account, while the remaining 110 (27.43%) were created under an individual account. The most commonly used licenses were MIT (152, 40.21%), Apache-2.0 (76, 20.10%), and NOASSERTION (76, 20.10%). On average, each repository had 7,064 stars (SD = 21,509.10) and 916 forks (SD = 2,995.03). Across all repositories, the most commonly used programming languages were TypeScript (206, 51.37%), Python (60, 14.96%), and Go (24, 5.98%).

Among all repositories, we identified a total of 1,876 .mdc files. On average, each repository contained 4.68 .mdc files (SD = 6.89), with the maximum number of .mdc files in a single repository being 56. According to the latest cursor rule documentation, it is recommended to place all cursor rule files in a dedicated directory at the root of the repository, called .cursor . We found that 374 repositories (93.27%) followed this recommendation. In these repositories, an average of 1.72 authors contributed to the directory (SD = 1.32), with a maximum of 8 authors. The average number of commits to the cursor rule directory was 5.68 (SD = 9.31), with a maximum of 98 commits. Among the 281 repositories that had at least two commits in the cursor rule directory, people spent an average of 16 days (SD = 15.90) between each commit updating their cursor rules. The average length of all cursor rule files was 462.67 lines (SD = 1,197.00), with the longest file containing 11,076 lines.

The entire dataset, prompt, reproduce package is available via this link 5 5 5 https://anonymous.4open.science/r/cursorrule-supp-110E .

3.3. Qualitative Analysis

We qualitatively analyzed the content of cursor rules to understand the types of context developers provide when authoring these files. We employed thematic analysis, following established procedures ( braun2006using ; clarke2013teaching ) , to systematically identify recurring patterns and themes. The analysis was conducted iteratively, involving multiple rounds of coding, discussion, and refinement among the research team.

We specifically focused on analyzing the content of cursor rules, excluding code blocks and other non-textual elements, such as images, since the purpose and content of these non-textual elements were mostly self-explanatory. For example, code blocks were typically included to provide code examples or snippets, which did not require further interpretation. We programmatically excluded these non-textual elements from our analysis to focus on the textual content.

We, the two authors, began by familiarizing ourselves with the data, reading through cursor rules in the selected repositories. Given that analyzing each cursor rule file in all 401 repositories would be impractical, we selected 30 repositories from the entire pool of 401 repositories for open coding. To ensure diversity, we sampled repositories across distinct domains and programming languages. We fetched the list of topics each repository owner assigned to their repository using GitHub’s official API. We then selected the top 10 most popular topics, which are ”AI”, ”TypeScript”, ”tag-production”, ”Java”, ”security”, ”Prisma”, ”ecommerce”, ”MCP-Server”, ”PHP”, and ”DeepSeek”. To prevent class imbalance, we randomly selected 3 repositories from each topic, resulting in a total of 30 repositories. We carefully examined the cursor rules, their descriptions, and related repository documentation to understand the context in which they were written. This process typically required several hours per repository. During this initial review, we decided to code at the line level, as developers often expressed a single idea per line in cursor rule files. As there were lines that were not directly related to context provision, such as section headers or empty lines, we introduced ”No Code” to indicate they did not contain relevant context information. Guided by these insights, we generated initial codes to describe the purpose and content of each cursor rule line through an inductive approach. We recorded notes on emerging impressions and potential themes, referencing prior literature on documentation, developer communication, and context engineering to inform our perspective.

After the in-depth review of the initial sample, we convened to discuss and refine the codes into a preliminary coding scheme. We then coded these repositories using the preliminary coding scheme again to ensure consistency and reliability. Discrepancies were discussed and resolved, and the coding scheme and definitions were further refined. We organized the codes into higher-level categories and themes through axial coding, iteratively improving the scheme through team consensus. Finally, independent coding of the initial 30 repositories by two researchers yielded substantial agreement ( kappa ; kappa1 ) (Cohen’s Kappa = 0.71).

To scale the analysis to the full dataset of 401 repositories, we leveraged a large language model (LLM) to assist with the coding process, following prior work ( LLMannotation1 ; cancode ; cancode2 ; cancode3 ; cancode4 ) . We prompted the LLM with the final coding scheme and up to three representative examples for each code from our initial analysis, instructing it to assign codes to each line in the cursor rules with some surrounding context. We used gemini-2.5-flash-preview-09-2025 with temperature 0.0 and dynamic thinking enabled. To enhance reliability, we repeated the labeling process three times and selected the majority vote as the final label for each line. If all three labels were different, we marked it as “No Code” to indicate uncertainty.
To validate the LLM-assisted coding, we ran this process on the initial 30 repositories and found
substantial agreement between the LLM and both human raters (Cohen’s Kappa = 0.64 and 0.65), before applying it to the rest of the dataset.

3.4. Threats to Validity

Our research suffers from the usual threats of qualitative research in software engineering. While qualitative analysis enables a deep exploration and understanding of the data, it limits our ability to generalize beyond the studied dataset without further validation.

We focused exclusively on cursor rules, which may not represent other forms of developer-provided context for different coding agents. Additionally, our analysis was restricted to repositories that adopted cursor rules relatively early, potentially capturing developers’ initial exploration of new project-level context provision, and may not reflect the sustained use of cursor rules, which could evolve as developers gain more experience with these tools.

A further limitation arises from the use of a large language model (LLM) to assist in the coding process. To improve reliability, we repeated the labeling process three times, selected the majority vote as the final label, and found substantial agreement with human coding on the initial 30 repositories. Nevertheless, there remains a possibility that the LLM introduced biases or misinterpretations, and its outputs may not fully capture the nuances, context, or intent behind developers’ cursor rules. Such potential bias is a common limitation of qualitative analysis, especially when conducted at scale. Based on a human manual verification, LLM usually disagree with human coders on functionality and language/framework specific rules. If all three labels were different, we marked it as “No Code” to indicate uncertainty. There are 2.1% of all lines fall into this disagreement. However, considering the size of our dataset, this number should be treated as a lower bound.

Our dataset is limited to open-source repositories indexed by Sourcegraph, which focuses on popular GitHub projects. While not exhaustive, this provides a reasonable sample of widely used repositories. In addition, although we focused on cursor rules, other rule formats exist, such as Copilot custom instructions, which may include different types of context. However, since cursor rules were among the earliest to introduce this feature, have been widely adopted in the open-source community, and the mechanisms of other rules are similar to cursor rules, we believe our selection is sufficiently representative to provide initial insights into this emerging practice. Nevertheless, future work could study rules authored for other AI coding assistants to validate and extend our findings.

As part of the data cleaning steps, if multiple repositories contained identical cursor rules, we kept only one and excluded the duplicates (11 repositories) to ensure a comprehensive capture of all unique rules.
This approach may underrepresent some rules that are widely copied across different repositories, and it may also influence our subsequent quantitative analysis of rule reuse frequency. However, since only a small portion of repositories are removed due to duplication and most are copied from similar domains, we believe this threat is minimal.

4. Context Types in Cursor Rules 
Table 1. Taxonomy of context types provided in cursor rules, including definitions and
representative examples. Highlighted codes are the high-level categories, that encompass
the sub-codes listed below them.
% Repo indicates the proportion of repositories that included each
category and context type, and % Code indicates the proportion of each category and context type
across all cursor rule lines.

Code Definition & Example % Repo % Code

Convention Prescribed standards that define how code should be written and organized within a project. 0.84 0.15

\arrayrulecolor black!30 \arrayrulecolor black Structure Conventions for how files and directories are created, named, and organized within a software project. Use the ‘apps‘ directory for Next.js and Expo applications. 0.59 0.04

Language/ Framework Conventions specific to the project’s language, framework, or library, such as preferred functions or constructs. Favor WordPress hooks (actions and filters) for extending functionality. 0.64 0.06

Code Style Conventions for the code style, including naming, formatting, code writing, and other stylistic choices. Favor the use of functional components over class components. 0.65 0.05

Guideline Prescriptive instructions to follow specific practices or avoid certain pitfalls. 0.89 0.33

\arrayrulecolor black!30 \arrayrulecolor blackUI Principles to improve usability, accessibility, and internationalization (i18n). All interactive elements (links, buttons, form controls, custom components) must be operable via a keyboard. 0.34 0.02

Consistency Guidance to align new code with existing patterns, styles, structures, and logic. Follow existing patterns from similar components. 0.38 0.01

Dependency Practices to manage dependencies (e.g., avoid duplicates, manage versions) and to ensure compatibility. Ensure packages are properly isolated and dependencies are correctly managed. 0.31 0.01

QA Practices for managing, preventing, and reporting errors, including logging, exception handling, and test requirements for verification. Comprehensive testing: Test all integration features. 0.68 0.10

Perf. Practices aimed at efficient resource usage, performance monitoring, and reuse with performance considerations. Cache expensive operations. 0.43 0.03

Security Guidelines and practices to protect software from vulnerabilities and ensure data privacy. Implement proper nonce verification for form submissions. 0.34 0.02

General High-level design and programming guidelines, including design patterns, separation of concerns, modularity, type safety, and code reuse. Maintain module separation of concerns. 0.65 0.06

Comm. Guidelines for clear communication across the development workflow, including planning, implementation notes, PR documentation, and issue references. Include a clear title and description of the feature being implemented. 0.64 0.07

LLM Directives that instruct LLMs on how to generate responses for the project. 0.50 0.08

\arrayrulecolor black!30 \arrayrulecolor blackGranularity Directives instructing an LLM to adjust response detail. Avoid unnecessary verbosity and tangential remarks. 0.12 0.00

Formatting Directs an LLM to generate output that strictly conforms to a specification such as a template, required format, language, or inclusion of references. Format should match: ”Added/Improved/Fixed - Description of the change” 0.16 0.01

Behavior Directs LLMs to follow specific rules and guidelines when generating responses, e.g., to reference other documentation, use tools, or add verification steps. Always ask clarifying questions when you don’t have full context or understanding of a task or question. 0.36 0.02

Persona Directives that instruct an LLM to adopt a specific role or persona while performing a task. You are an expert in Python, writing an AI application called chatgpt-mirai-qq-bot. 0.18 0.00

Workflow Specifies a structured, multi-step process or orders of tasks an LLM must satisfy to complete a task. Update the scratchpad as progress is made (mark completed steps with [X]) 0.30 0.05

Project Captures context that describes the software project of the repositories. 0.85 0.35

\arrayrulecolor black!30 \arrayrulecolor blackChange Describes shifts or updates in a project’s technical implementation or configuration. No need for ‘postcss-import‘ or ‘autoprefixer‘ anymore 0.17 0.01

Func. Describes the overall architecture, purpose, and key components of a software project, or the intended use of its various modules. ‘setup/‘: Setting up the environment, installing dependencies. 0.71 0.26

Env. Specifies the technology stack (e.g., libraries, tools, hardware) and commands used to build, initialize, run, or test the project. Run the CLI ‘init‘ command: ‘npx trigger.dev@latest init‘. 0.72 0.07

Example Demonstrates good and bad practices or provides a basic template. 0.50 0.09

From the qualitative analysis, we identified five high-level categories of context types that developers commonly provide: Project, Convention, Guideline, LLM Directives, and Examples. The taxonomy of context types is illustrated in Figure 2 . Detailed definitions, representative examples of each context type, and their usage distributions with explanations are provided in Section 4 . In the following sections, we describe each category and its subcategories in detail, with representative examples.

4.1. Project

Most projects provided project-related context in their cursor rules.
Codes in this category capture context that describes the software project, similar to the project overview and usage sections in traditional software documentation ( maalej2013patterns ; freund2015contextualizing ) .

Functionality. For functionality, this refers to descriptions of the overall architecture, purpose, and key components of a software project, or the intended use of its various modules. We observed many rules that explain different files or directories in the project, detailing their functionality and relationships to other components, often with links to those files or directories. This may be because developers want Cursor to properly reference those files.

Environment. Many cursor rules describe the technology stack, including the programming languages, frameworks, libraries, and tools used in the project. They also outline the setup and configuration steps required to run the project, such as environment variables, configuration files, and necessary initialization commands. Most of this information overlaps with content typically found in the installation section of software documentation. The main purpose appears to be constraining the LLM to generate code compatible with the existing technology stack. Detailed explanations of the setup and commands can help LLM agents understand how to run tests, build the project, or deploy it.

Change. We discovered that many cursor rules contain text describing recent updates to the project or its dependencies. Much of this content overlaps with what is typically found in release notes, such as “No need for ‘postcss-import‘ or ‘autoprefixer‘ anymore” . These rules can help LLM agents avoid generating code that relies on deprecated features or conflicts with recent changes. This information is usually not obvious from the codebase itself.

4.2. Convention

The convention category captures rules that prescribe specific conventions or standards to follow when contributing to a software project. It is usually tied to a project-selected style guide or specific project usage requirement.

Project Structure. Project structure includes conventions related to what developers need to follow when they want to make changes to the current project, such as directory structure, naming conventions for files and folders, and organization of modules or components. For example, “don’t just create new directories and files that do not fit this pattern
otherwise Tanstack router” .

Language/Framework Specific. Language/framework usage includes conventions related to the specific programming languages, frameworks, or libraries used in the project, such as preferred idioms, patterns, or best practices. For example, “Use WordPress ‘@wordpress/element‘ instead of direct React import.”

Code Style. Code style includes conventions related to code formatting, naming conventions, commenting practices, and other stylistic guidelines that developers should follow when writing code for the project. Many rules reference existing style guides, such as the Google Style Guide, Airbnb Style Guide, or PEP 8.

4.3. Guideline

The guideline category captures context that provides high-level principles, best practices, and recommendations for developers to follow when contributing to a software project. Compared to conventions, guidelines are usually more general and abstract, covering common standards or best practices for areas not limited to a specific or a series of similar projects.

Quality Assurance. The most frequently mentioned code in the guideline was quality assurance. These rules provided recommendations on testing, code reviews, debugging, and other quality assurance practices to ensure the reliability and maintainability of the software. For example, “Utilize guard clauses to handle preconditions and invalid states early.”

General Programming. Many cursor rules include very high-level programming best practices, such as separation of concerns, modularity, type safety, and code reuse, which any experienced developer would already be familiar with. For example, “Maintain module separation of concerns” .

Communication. Guidelines on documentation and communication were also among the most frequently mentioned codes in cursor rules. These rules provided recommendations on how to communicate effectively throughout the development workflow, such as writing clear commit messages, documenting code changes, and collaborating efficiently with team members.

4.4. LLM Directives

Another category we detected is LLM Directives , which captures context that provides specific instructions and directives for LLMs to follow when generating code snippets. Unlike the previous three categories, which contain more general information that could be helpful for any developer working on the project and have also been widely discussed in prior literature on software documentation or developer communication practices ( maalej2013patterns ; freund2015contextualizing ) , this category specifically targets the capabilities of LLMs and provides guidance tailored to them.

Unlike the previous three categories, which are more prevalent in cursor rules, LLM Directives are less frequently mentioned. Only about 50% of repositories (compared to 85% for Project, 84% for Convention, and 89% for Guideline) contain LLM-specific instructions in their cursor rules, suggesting that many developers may not yet be familiar with the practice of authoring these prompt engineering strategies for LLMs ( sahoo2024systematic ; schulhoff2024prompt ) .

Behavior. As the most frequently mentioned code in the LLM Directives category, the behavior code provides instructions on how the LLM should behave when generating code snippets, such as being cautious, avoiding assumptions, verifying information, and asking clarifying questions. In more details, developers often uses a variety of strategies to guide LLM behavior in their projects. One common approach is structured reasoning, where prompts explicitly direct the model’s thought process using techniques such as chain-of-thought prompting ( wei2023chain ; kojima2023large ) or self-consistency ( wang2023self ) , helping the model arrive at more reliable outputs. Another frequent practice is asking for clarification: when prompts are ambiguous or underspecified, instructions may tell the LLM to request additional context, for instance, “Always ask clarifying questions when you don’t have full context or understanding of a task or question.” Many developers also include self-verification steps, requiring the LLM to check its assumptions, dependencies, or constraints before generating code, such as “Before generating any code, you MUST verify: 1. Are you importing from @trigger.dev/sdk/v3? If not, STOP and FIX.” To prevent errors or undesired outcomes, instructions sometimes include specific prohibitions or antipatterns. Finally, developers frequently embed project-specific rules that are non-generalizable but essential for their particular context, for example, “Do not run test-teardown even if tests are successful—I will do that manually or request it explicitly.” These practices collectively help ensure that LLMs behave predictably, safely, and in alignment with project requirements.

Workflow. The next most commonly mentioned theme in the LLM Directives category was workflow, which specifies a structured, multistep process or sequence of tasks that an LLM should follow to complete a task, often by mimicking real-world human software development processes. Many of these workflows are designed to decompose complex tasks into smaller, manageable steps, such as “Before responding to any request, follow these steps: 1. Request Analysis, …, 2. Solution Planning, …” . Some rules are written as conditional sequences, under which certain steps are executed only when specific conditions are met, for example, “When a user request begins with CHANGELOG:, add a changelog entry based on the provided prompt in the following files:” .

Persona. Many cursor rules specified the persona the LLM should adopt, such as “You are an expert in Python, writing an AI application called chatgpt-mirai-qq-bot. It is a workflow-based chatbot system.” Along with these persona definitions, some rules provide a high-level overview of the entire project, which the LLM is expected to be familiar with. We also observed that most persona instructions directed the LLM to assume technical roles, such as software engineer, with fewer projects emphasizing non-technical personas, such as personal assistants or friends. Comparing to behavior and workflow codes, persona instructions were less frequently mentioned in cursor rules.

Output Formatting and Granularity are used to provide instructions on how the agent should respond in terms of format and level of detail. Formatting mainly directs the LLM on how to structure its responses, such as specifying templates, required formats, languages (e.g., “Respond in Chinese” ), or inclusion of references. Granularity provides instructions on the level of detail the LLM should include in its responses, such as “Deliver the response in a minimal yet complete form. Avoid unnecessary verbosity and tangential remarks.”

4.5. Examples

There is one auxiliary content category called Examples, which captures different types of examples provided,
usually alongside established rules, such as naming, formatting, or usage examples.
For example, “Example: https://github.com/brainlid/langchain/pull/261 ” .
The documentation literature ( maalej2013patterns ) has highlighted the importance of examples, especially the code examples,
in helping developers understand and apply guidelines effectively.
While we found the similar trend in cursor rules, the proportion of examples is represented relatively low in our quantitative results,
because we programmatically excluded code blocks from the analysis ( Section 3.3 ).
Therefore, the number of example codes should be treated as a lower bound.

4.6. Discussion

Overall, our qualitative analysis revealed that developers provide a diverse range of context types in cursor rules, spanning project-specific information, coding conventions, high-level guidelines, LLM-specific instructions, and examples. The prevalence of project-related context highlights developers’ emphasis on conveying the unique aspects of their software projects to LLMs, which is crucial for generating relevant and accurate code snippets. The widespread use of conventions and guidelines indicates developers’ desire to maintain consistency and quality in code contributions, aligning with established best practices. The presence of LLM-specific instructions, although less common, underscores the growing recognition of the need to tailor LLM behavior to better suit the requirements of software development tasks.

We also found that the spectrum of context types, except for LLM-specific instructions, largely aligns with established best practices for software documentation and developer communication ( maalej2013patterns ; freund2015contextualizing ) . This suggests that developers are leveraging cursor rules as an extension of traditional documentation, adapting familiar practices to the context of LLM-assisted coding.

The relatively low adoption rate of LLM-specific instructions in cursor rules is noteworthy. One possible reason is that developers treat cursor rules as general background information for LLMs and may not recognize the importance of providing instructions tailored to the model. Another possibility is that developers are unsure whether such instructions are necessary or how to effectively communicate their needs and constraints to LLMs. Additionally, some may prefer LLMs to simply answer questions rather than generate code, providing only general context instead.

We also observed that developers in different domains may have different expectations and requirements when working with LLMs. For instance, frontend developers often focus on rapid iteration and want the LLM to automate more tasks. During our initial coding of cursor rules, we observed one frontend development repository (appsmith 6 6 6 https://github.com/appsmithorg/appsmith ) that provided logic for the LLM to automatically decide the workflow and complete development tasks step by step, with detailed linting and preflight checking code included in the cursor rules. At the time we collected the data and performed our analysis, cursor rules were not capable of executing such complex logic. However, as new features have been added to Cursor, such as hooks 7 7 7 https://cursor.com/docs/agent/hooks released in late September, developers may now be able to define more advanced workflows with LLM assistants.

5. Characteristics of Cursor Rules

In Section 3.3 , we identified different types of context that developers commonly provide in cursor rules. During this process, we observed that the context types may vary depending on various project characteristics, such as programming language and application domain. In this section, we further investigate these variations by exploring the following research questions, which are motivated by our observations during the coding process and by related literature on developer communication practices ( maalej2013patterns ; freund2015contextualizing ) , project characteristics ( plinfluencecontext ) , and LLM prompt engineering strategies ( sahoo2024systematic ; schulhoff2024prompt ) .

RQ1: How does context provision in cursor rules differ by programming language?

Prior research ( plinfluencecontext ; plinfluencecontext1 ) has shown that different programming languages influence developers’ communication practices and the types of context they prioritize. For instance, statically typed languages such as Java, Rust, and TypeScript may require less explicit context regarding type safety, as their type systems enforce correctness at compile time.
In contrast, dynamically typed languages such as Python and JavaScript could require more detailed context related to type checking and error handling, since such issues are only detectable at runtime. Furthermore, for recently adopted programming languages such as Rust ( rustneeddifferent ; rustneeddifferent1 ) , developers may need to provide additional context about language-specific features and idiomatic practices.
In this question, we investigated whether these language-specific differences are actually reflected in the context provided in cursor rules.

RQ2: How does context provision in cursor rules differ by application domain?

Previous work on best practices and conventions has shown that developers adhere to different sets of guidelines depending on the application domain of the software project ( domainneedspecific1 ) . For example, in web development, best practices often emphasize responsive design, accessibility, and performance optimization, whereas embedded systems development prioritizes real-time constraints, resource management, and hardware interfacing ( webreq ; generaldomain ) .
With this research question, we investigated whether such domain-specific differences are also reflected in the context provided in cursor rules.

RQ3: To what extent do developers provide multiple types of context in cursor rules?

Many guidelines for traditional documentation recommend that developers provide multiple types of information to give a comprehensive overview of the project. For example, Maalej and Robillard ( maalej2013patterns ) suggest that effective documentation should include both high-level overviews and low-level implementation details to support various developer needs. Similarly, many studies on documentation have found that developers face challenges when documentation lacks code examples or explanations of the rationale behind design decisions ( sohan2017study ; ebert2021exploratory ) .
In RQ3, we investigated whether developers follow these best practices when authoring cursor rules.

RQ4: To what extent do developers reuse cursor rules?

In software engineering, reusability is a key principle that promotes efficiency and consistency ( copypaste ) . Developers are encouraged to reuse existing code snippets, libraries, and frameworks to expedite development and maintain consistency across projects. Similarly, prior work on prompt engineering has highlighted the benefits of reusing effective prompts from external sources or previous projects to enhance LLM performance ( prompt11 ) . In our analysis, we observed that developers often reuse context from existing documentation, coding standards, and best practices when authoring cursor rules. Additionally, we found several community-maintained repositories providing template cursor rules, which encourage the reuse of existing cursor rules.
With this research question, we aimed to understand the extent to which developers reuse cursor rules from external sources or prior projects when authoring their own rules.

RQ5: How does the timing of cursor rule addition relative to repository creation affect the context provided?

Since writing documentation for LLMs is a relatively new practice, we hypothesized that the timing of when developers add cursor rules to their projects may influence the type of context they provide. For example, if a repository was created long before cursor rules were introduced, developers might have reuse project-related information by copying from existing documentation in the repository, rather than writing detailed and diverse context specifically for LLMs. Conversely, for newly created repositories, developers could provide more high-level and LLM-specific instructions to guide LLMs in generating code from scratch.
Thus, we aimed to understand how the timing of cursor rule addition relative to repository creation affects the context provided.

To answer these research questions, we collected additional metadata for 401 repositories we
analyzed in Section 3.3 , and present our analysis and findings below.

Figure 4. Distribution of the average number of codes for each context type by programming language.

5.1. RQ1: Programming Language

To answer RQ1, we first identified the primary programming language used in each repository
with value provided by GitHub’s API, and analyzing the distribution of context types across different programming languages.
We only included those programming languages that were top 10 in our dataset.
To make the result more reliable, we only included programming languages that had at least 6 repositories, resulting in the following top 10 languages: Typescript (206 repositories), Python (60), Go (24), JavaScript (17), Rust (16), PHP (10), Java (9), Swift (8), C# (7), and C++ (6).

Findings. Figure 4 shows the distribution of the average number of codes for each context type by programming language.
Overall, different programming languages tend to have different distributions of context types.

Developers tend to provide less context when working with statically typed languages such as Go, C#, and Java,
and provide more context when working with dynamic languages like JavaScript and PHP.
This suggests that developers expect that the stricter syntax and type checking in statically typed
languages allow LLMs to infer more information directly from the code, reducing the need for additional context ( typeisgood1 ; typeisgood ) .
For example, repositories of JavaScript as main languages tend to provide more guideline-related context ( M ean=92)
and more conventions (M=34)
while those using TypeScript, a statically typed superset of JavaScript,
has a lower average number of guideline-related context (M=50) and conventions (M=34).

Developers provided more overall context (M=207) for PHP projects compared to other languages,
possibly because PHP is an older language with a wide variety of coding styles and practices,
which may make it challenging for LLMs to infer the appropriate conventions and best practices without additional context.

Some less dominant and more domain specific programming languages, such as C#, tend to have more LLM-related context (M=31) provided in cursor rules.
This may be because C# is often used in enterprise applications and game development, where LLMs need to be more cautious about the code they generate to avoid potential issues. Additionally, its similarity in structure to Java and other object-oriented languages—which are more commonly used and prevalent in LLM training data—may increase the necessity of providing additional context.

Among all programming languages, JavaScript and TypeScript are the most common languages for which
developers provide examples (M=24 and M=21, respectively).
This may be because JavaScript and TypeScript are often used for frontend development with a wide
variety of frameworks and libraries that are updated at a fast pace, so developers feel the need to provide
more examples to help LLMs understand specific usage patterns and best practices for these languages.

Limitations. Our analysis only considered the dominant programming language of each repository,
as the GitHub API only provides a single primary language per repository.
This may oversimplify the analysis for multi-language projects,
such as web development projects that are full-stack and contain multiple programming languages.
However, we believe the relative comparisons between programming languages still hold,
as we applied the same criteria across all repositories.

Additionally, our dataset is skewed, with over 50% of repositories being Typescript or JavaScript.
While this represents the current distribution of repositories adopting cursor rules on GitHub,
more studies should be conducted to better understand the differences and requirements when working with LLMs
across various programming languages.

5.2. RQ2: Application Domain

To identify application domains, we used the list of GitHub topics set by the repository owners
via the official GitHub API.
Considering that each repository can have multiple topics and can be assigned by owners freely,
we first performed clustering over these topics.
We removed generic terms such as “ai” and “open source,” and excluded non-English topics.
Then, we used repositories that had at least two topics assigned (317 repositories) for further analysis.
Then, we performed topic modeling with BERTopic ( berttopic ) on concatenated topics.
We then used UMAP ( umap ) with the number of neighbors set to 15 for dimensionality reduction and HDBSCAN ( hdbscan ) for clustering.
We chose HDBSCAN because it does not require pre-defining the number of clusters,
and can identify noise points that do not belong to any cluster.
We set the minimum cluster size as 20, 5% of the dataset, and a minimum sample size of 2 to enforce at least two repositories per topic.
In addition, we performed a greedy search over different hyperparameter combinations, optimizing and balancing the number of topics, the meaningfulness of topics, the ratio of unclustered topics, and the coherence of individual items with topics (measured using the c_v metric with the Gensim model ( c-v1 ; c-v2 ) ), along with topic diversity (measured by the number of unique tokens over the entire document length), to determine the most appropriate clustering outcomes. The final selected number of topics was six. The selected combination of hyperparameter allowed us to achieve a low unclustered topic ratio (0.3%), acceptable topic coherence (0.52), and good topic diversity (0.93). The research team manually checked the meaningfulness of the topics by reviewing the top keywords and representative repositories for each topic. Since the c_v metric is highly dependent on the corpus ( lim2024aligning ) , and the topics assigned by developers were usually quite diverse, we believe these metrics indicate a good clustering result.
For the embedding model, we used the officially recommended “all-MiniLM-L6-v2” ( all-MiniLM-L6-v2 ) .
We excluded any unclustered repositories from further analysis.

We identified six distinct topics from 317 repositories: : Web Development (70 repositories), representing general web projects. : LLM Agent (62 repositories), for projects focused on building or evaluating large language model agents. : Frontend Development (61 repositories), for projects using frontend languages or frameworks such as React or WordPress, including domain-specific areas like e-commerce. For example, Angular (angular/angular). : Data Analysis (50 repositories), for projects centered on performing or managing data analysis tasks. : UI Development (44 repositories), for projects focused on design work, design utilities, and user interfaces. For example, ant-design-web3 (ant-design/ant-design-web3). : MCP Tools (29 repositories), for projects related to plugin development for coding assistants.

Figure 5. Distribution of the average number of codes for each context type by application domain.

Findings. Figure 5 presents the distribution of the average number of codes
in each context category across detected domains.
Overall, we found that different application domains tend to have different distributions of context types.

Front-end and visually focused implementation projects, such as data analysis, web development, and
frontend development, tend to provide more examples for LLMs (M=43, M=13, and M=13, respectively).
Since these projects are usually written in JavaScript or TypeScript, this aligns with our finding ( Section 5.1 )
that JavaScript/TypeScript projects include more examples.

For domains that do not have many publicly available, up-to-date API, such as MCP code server projects;
developers tend to provide more project context to help LLMs understand the requirements and constraints
of the project (M=69) ( apihard ) .
In contrast, for domains with abundant online resources, such as UI design projects, developers tend
to provide less project context (M=45).

Developers tend to provide more guideline-related context when working on frontend development
for projects that require more complex and unpredictable tasks that demand careful consideration
before execution, such as LLM agent projects and data analysis projects (M=64 and M=66, respectively).

Limitations. It is possible that our topic clustering have misclassified some repositories, potentially affecting
the analysis of domain topics and context types.
We mitigated the risk of misclassification by manually reviewing the top keywords and representative repositories
for each topic to ensure the quality of our clustering.

In addition, there is a strong correlation between application domain and programming language,
as certain domains tend to use specific programming languages.
For example, frontend development projects predominantly use JavaScript and TypeScript,
while data analysis projects often utilize Python and R.
This correlation may confound our analysis of context types by application domain,
as the programming language itself also influences the context types provided ( Section 5.1 ).
However, this is common in software engineering research, and disentangling the effects of programming
language and application domain is inherently challenging.
We found new insights that were not directly explained by programming language alone,
such as the higher amount of guideline-related context in LLM agent projects and data analysis projects,
showing that application domain can also play a significant role in shaping context provision.

5.3. RQ3: Context Co-occurrence

To test whether developers tend to provide extensive context covering multiple aspects of the project
when authoring cursor rules, we analyzed the co-occurrence of different context categories
within individual repositories.

In addition, we also counted the number of unique codes in each repository to understand the coverage of different context types.

Figure 6. Venn diagram of context type co-occurrences in cursor rules.

Findings. Figure 6 shows the co-occurrence of different context category in cursor rules. In general, developers were motivated to provide comprehensive context for LLMs, with 149 repositories
(37.16%) providing four actual content context categories in their cursor rules and 99 repositories (24.69%) providing all five context categories (including examples).

Developers prefer to write cursor rules in a style similar to traditional project or collaboration documentation,
which typically covers best practices and standards for software development ( prana2019categorizing ; fronchetti2023contributing ) .
In our case, this includes project, conventions, and guidelines category.
People usually pay the same amount of attention to the tuple combinations of those three context types,
which were relatively evenly distributed (Project and Convention: 296 repositories, 73.8%; Project and Guideline: 310 repositories, 77.3%; Guideline and Convention: 311 repositories, 77.6%).
Examples are usually provided by the traditional documentation to illustrate other context types and help people use the other context types more effectively as well ( exampleeffectiveness ) .
In our case, the Example category is usually co-occurs with all other three categories: Guideline, LLM Directive, and Convention (172 repositories, 42.9%). Individually, examples are most frequently provided alongside Guidelines (193, 48.1%), Conventions (189, 47.1%), LLM Directives (187 repositories, 46.6%)

Some developers choose to only focus on specific aspects when writing cursor rules to let LLM focus
on a really specific aspects while generating code.
32 repositories (7.98%) provided only one category of context in their cursor rules;
most of them were for guideline-related context (11 repositories, 2.74%).

Figure 7. Distribution of the number of unique code types provided by repositories.

At a more granular level, developers usually provide a selected amount of codes in their cursor rules
to prevent overwhelming LLMs with excessive context and keep LLM focus on the most critical aspects of the project. Figure 7 shows the distribution between the number of codes covered by a
single repository.
Very few repositories provide more than 19 unique codes and most of the repositories (323 repositories, 80.55%)
provide a moderate amount of unique code types (between 3 and 15 types) with a peak at 9 unique code types.
This indicates that developers tend to provide a balanced amount of context, covering multiple
aspects of the project.
At the same time, this also suggests that developers are selective in the specific codes they include,
or they miss out on certain aspects that could be beneficial for LLMs to understand the project better,
which aligns with prior findings on documentation practices ( maalej2013patterns ) .

5.4. RQ4: Proportion of Duplicated Lines

During our initial coding, we observed that a large portion of cursor rules appeared to be directly
copied from other documents within similar repositories or from shared template repositories,
such as “awesome-cursor-rules” 8 8 8 https://github.com/PatrickJS/awesome-cursorrules .
To quantitatively assess the extent of such duplication, we analyzed the proportion of exactly
duplicated lines across all repositories in our dataset.

Figure 8. Percentage of code that are duplicated by context category.

Findings. Overall, we identified a total of 19917 (28.70%) duplicated lines across all repositories with an average of 49.67 duplicate lines (SD=164.20) per repository.
Figure 8 shows the percentage of code that are duplicated by context category.

Developers usually provide unique information about their own projects. We found that the proportion of duplicated lines is higher among LLM-specific instructions, which may indicate that such instructions are easier to generalize across different projects or that developers tend to reuse them because they represent a relatively new type of information.

Figure 9 shows the distribution of the average number of duplicated lines for each context type by programming language. We found that different programming languages tend to have different copying practices when writing cursor rules. For example, developers using programming languages for desktop and enterprise applications, such as C#, which require high domain specificity and are less tolerant of errors, tend to replicate cursor rules from similar projects more frequently (M=61.14, SD=161.77). In contrast, developers using languages for frontend applications, such as TypeScript, often copy bits and pieces from various sources but also contribute a large amount of original content, resulting in the highest total number of duplicated lines (7,838 lines).

For individual repositories that are not complete duplicates of others, we found an average duplication rate of 16.30% of lines, with the top 10 repositories having over 96% of their lines duplicated. This suggests that some developers tend to extensively reuse existing cursor rules when writing their own, rather than creating everything from scratch.

A manual investigation of duplicated lines revealed that developers reuse content from diverse sources. Some rules are directly copied from the documentation or cursor rules of dependencies used in the project for project-related context. For example, mfts/papermark copied “You MUST use @trigger.dev/sdk/v3 ” from triggerdotdev/trigger.dev . Developers also reuse guidelines from repositories with similar setups or architectures; for instance, github.com/sadmann7/shadcn-table copies rules like “Prefer iteration and modularization over code duplication” from other repositories in the same ecosystem. Additionally, some cursor rules are taken from community-maintained template repositories, such as awesome-cursor-rules , which provide standardized rule sets for common use cases. A small proportion of cursor rule files appear to be generated by LLMs, as indicated by meta-comments or conversational lines. For example, “Okay, I can help you summarize this pattern for creating a new Cursor rule, focusing on the TanStack Query integration and the preferred error handling strategy.”

Figure 9. Distribution of the average number of duplicated lines for each context type by programming language.

5.5. RQ5: Cursor Rule Composition Over Time

To answer this research question, we calculated the time difference between the first commit in the cursor rule folder (using the official default directory, i.e., .cursor/ ) and the repository creation date. Since many repositories did not follow the official default directory structure, we were only able to obtain this information for 281 repositories. We then grouped the repositories based on this time difference into four buckets, ensuring a balanced number of repositories in each group with meaningful time intervals. This resulted in four groups: within seven months (91 repositories), within two years (82), within five years (100), and more than five years (101).

Findings. Figure 10 shows the distribution of the average number of codes for each context type across these time difference groups. Contrary to our initial assumption, developers use similar strategies when writing project context and convention context in cursor rules, regardless of when the repository was created.

Projects created two to five years before the introduction of cursor rules tend to provide the largest amount of guideline-related context. This may be because these projects are old enough to require more context to ensure LLMs understand legacy constraints, but not so old that their technical guidelines have already become widely established online.

The most notable trend is observed in the LLM Directives category. As the time difference increases, the amount of LLM-related context shows a slight decrease. Developers of older repositories seem to care less about LLMs and primarily use cursor rules as a form of documentation, focusing more on guidelines and project information. In contrast, newly created repositories tend to be more aware of the boundaries and capabilities of LLMs, and thus provide more LLM-specific instructions.

The amount and type of context included in cursor rules vary systematically with the age of the project relative to cursor rule creation, reflecting changes in developer needs over time.
Groups created within seven months tend to provide the least median amount of all context types, suggesting either they are more concise in their cursor rules overall, or these projects are newer and have less accumulated complexity, requiring less context for LLMs to understand the project effectively.
For groups with a time difference greater than seven months, as the time difference increases, there is a slight decrease in the median amount of project-related and convention-related context provided. This suggests that as projects mature, developers may streamline their cursor rules to focus on the continued maintenance of essential guidelines and LLM instructions, rather than extending current project details.

Limitations. According to official guidance for writing cursor rules, developers are required to place their cursor rules in the .cursor/ directory by default for Cursor to index.
Therefore, we only checked the .cursor/ folder, which may miss monorepos or custom structures. This bias is consistent across all groups and does not affect the relative comparisons.

Figure 10. The evolution of the number of codes for each category over time.

6. Discussion and Implications

6.1. Rule Authoring

The Need for Broader Context Support. Current AI-powered code editors typically utilize context retrieved from the IDE or from user-highlighted code. Our data show that developers actively provide additional context beyond source code, such as conventions (15%), guidelines (33%), and even instructions on how the LLM should behave (8%). This aligns with the emerging trend in popular AI assistants to expand their context mechanisms to ingest non-code artifacts—such as documentation, configuration files, and explicit rule files—to improve the relevance and accuracy of generated responses.

Enhancing Context Transparency. Our analysis revealed that a significant portion of cursor rules are duplicates (28.7% of all lines), indicating that developers often copy and paste content from documentation or community-shared templates that might already be accessible to the coding agent. This practice, along with rules that reference external documents (e.g., “Consider WordPress coding standards compliance”) without providing links, suggests that developers may be uncertain about the capabilities of AI. This introduces inefficient use of the context budget, which could be better utilized for information not already available to the AI. Enhancing developers’ understanding of what context is accessible to the AI (i.e., context transparency) and what information is necessary for the AI, such as providing clearer indications through documentation or UI affordances, would help them provide more targeted and effective context. A real-time feedback mechanism could also be helpful, indicating which rule is currently being used by the coding assistant so that developers can adjust their rules accordingly.

6.2. Tool Building

Context-Aware Rule Generation. We observed that the types of rules that are most effective can vary by programming language or application domain. For example, statically typed languages like C# tend to require more project-specific context, while frontend languages like JavaScript/TypeScript benefit from more examples.
However, developers are currently adopting existing rule templates (28.7% of all lines) or using LLMs to help generate their cursor rules, as observed in at least one repository among the 30 we initially coded. Cursor also officially provides a command to help developers generate initial cursor rules using LLMs. Without proper context awareness, these generated rules may not be optimal for the specific characteristics of each project.
This indicates significant potential for future tools to generate more context-aware rules, tailored to the specific characteristics of each project, rather than relying on generic templates. This could further increase the efficiency of the entire development process. Further research on automatically identifying necessary domain- or language-specific context is needed to inform the design of such tools. Future work can also focus on building better cursor rule generation or context assessment tools to help developers create and evaluate the comprehensiveness of their provided context. Additionally, computer use agents could further support agentic systems by automatically generating context rules based on project structure and existing documentation.

6.3. Future Research Directions

Qualifying the Efficacy of Context Rules. The rules we observed are primarily based on developer intuition; their actual impact on LLM performance remains an open question. For example, it is unclear whether project-related context is more beneficial than allowing LLMs to automatically index project files. In rare cases, excessive context may even degrade performance if it confuses the LLM. Future work is needed to quantify how different types of context—such as the themes in our taxonomy—contribute to task performance and to determine the optimal amount for each context type. Similar to how prompt engineering techniques are empirically tested, the ”usefulness” of different context types could be evaluated by comparing end-task results with and without certain context types. This would help prioritize which context is most valuable, especially since authoring and maintaining these rules imposes a cognitive load on developers.

Longitudinal Analysis. Our study provides a cross-sectional snapshot of how developers use cursor rules. However, this is a rapidly evolving practice. As developers become more familiar with LLM capabilities, their use of these rules may change. For example, they may shift from providing detailed project information to focusing more on LLM-specific instructions as they become more aware of LLM capabilities. Furthermore, as LLMs themselves become more powerful, the relative importance of different context types may shift. A longitudinal study is needed to track the evolution of these rules over time. One potential approach, common in the MSR community, is to monitor changes in cursor rules as a proxy for their effectiveness. Observing whether repositories abandon, expand, or refine their rules would provide critical insights into their perceived usefulness and the changing nature of human-AI collaboration in software engineering.

Future Education. With the emergence of AI in development workflows across all areas, educating developers on how to effectively collaborate with AI systems is critical. Our analysis of creation time differences also shows that newly created repositories often have less context, suggesting that developers may be unsure about what needs to be included. This highlights the need for further education. Our findings reveal several dimensions of how developers currently provide context to LLMs, which can inform future educational materials instead of treating AI as a magic box. For example, developers may benefit from learning about the importance of balancing different context types, such as project information, conventions, guidelines, and LLM directives. Future educational resources should help developers understand and apply best practices when authoring context for LLM-powered coding assistants.

7. Conclusion

In this paper, we presented a large-scale empirical study of 401 open-source repositories containing cursor rules to understand what types of context developers provide to LLM-powered coding assistants. We identified five main categories of context: Project Information, Conventions, Guidelines, LLM Directives and Examples, with some overlapping information traditionally shared between human developers and others specific to LLMs. We believe our findings, particularly the detailed taxonomy, provide a valuable foundation for the design of future LLM-powered coding assistants, as well as for understanding the knowledge and information that will be shared within teams as LLMs become new collaborators.
