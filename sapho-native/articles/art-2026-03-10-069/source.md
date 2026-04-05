---
version: source-capture.v1
article_id: art-2026-03-10-069
ticket_id: ticket-import-art-2026-03-10-069
source_url: https://arxiv.org/abs/2601.00477
canonical_url: https://arxiv.org/abs/2601.00477
source_title: 'Security in the Age of AI Teammates: An Empirical Study of Agentic
  Pull Requests on GitHub'
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-05T16:08:04Z'
linked_paper_urls: []
---
# Source Capture

## Title

Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub

## Body

Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub

Mohammed Latif Siddiq, Xinye Zhao, Vinicius Carvalho Lopes, Beatrice Casey, Joanna C. S. Santos

Abstract

Background. Autonomous coding agents are increasingly deployed as AI teammates in modern software engineering, independently authoring pull requests (PRs) that modify production code at scale. Prior empirical studies have primarily examined their productivity and acceptance rates, leaving the role of autonomous agents in software security and the dynamics of human review largely unexplored.

Objective. This study aims to systematically characterize how autonomous coding agents contribute to software security in practice, how these security-related contributions are reviewed and accepted, and which observable signals are associated with PR rejection.

Methods. We conduct a large-scale empirical analysis of agent-authored PRs using the AIDev dataset, comprising of over 33,000 curated PRs from popular GitHub repositories. Security-relevant PRs are identified using a keyword filtering strategy, followed by manual validation, resulting in 1,293 confirmed security-related agentic-PRs. We then analyze prevalence, acceptance outcomes, and review latency across autonomous agents, programming ecosystems, and types of code changes. Moreover, we apply qualitative open coding to identify recurring security-related actions and underlying intents, and examine review metadata to identify early signals associated with PR rejection.

Results. Security-related Agentic-PRs constitute a meaningful share of agent activity (approximately 4%). Rather than focusing solely on narrow vulnerability fixes, agents most frequently perform supportive security hardening activities, including testing, documentation, configuration, and improved error handling. Compared to non-security PRs, security-related Agentic-PRs exhibit lower merge rates and longer review latency, reflecting heightened human scrutiny, with variation across agents and programming ecosystems. PR rejection is more strongly associated with PR complexity and verbosity than
with explicit security topics.

Conclusions. Autonomous coding agents already perform a non-trivial amount of security-relevant work in real-world repositories, but these contributions are reviewed more cautiously by human maintainers. Security review of agent-authored code extends beyond vulnerability content alone and is shaped by contextual and
cognitive factors.

keywords: 
Large Language Models (LLMs) , AI Agent , Security , GitHub 
† † journal: Information and Software Technology

ythonSourceCode]python
labelposition=topline,
frame=single,
numbersep=2pt,
fontsize= ,
xleftmargin=5pt,
framerule=0.5pt,
linenos avaSourceCode]java
labelposition=topline,
frame=single,
numbersep=2pt,
fontsize= ,
xleftmargin=5pt,
framerule=0.5pt,
linenos odePython]pythonfontsize=
odeJava]javafontsize=
nippetJava]javafontsize= ,bgcolor=magnolia nippetPython]pythonfontsize= ,bgcolor=magnolia nippetPerl]perlfontsize= ,bgcolor=magnolia

\affiliation

organization=Department of Computer Science and Engineering,addressline=University of Notre Dame,
city=Notre Dame,
postcode=46556,
state=IN,
country=USA

{highlights}

We quantify the prevalence of security-relevant Agentic-PRs, identifying 1,293 confirmed cases (3.85% of agent activity), with a variation across agents and Claude Code exhibiting the highest proportion (14.6%).

We show that acceptance outcomes for security-related Agentic-PRs vary widely by agent, language, and change type, with merge rates ranging from 49.60% (Copilot) to 86.59% (OpenAI Codex) and Rust security PRs showing the lowest acceptance (51.16%).

Through qualitative analysis, we identify recurring security actions and intents, revealing that security work is often embedded within broader development goals, most commonly code refactoring and functionality improvement.

We find that security-related Agentic-PRs receive heightened human scrutiny, with substantially longer review latency than non-security PRs (median 3.92 vs. 0.11 hours).

We identify early PR-level signals associated with rejection, showing that perceived risk is more strongly linked to complexity and verbosity ( e.g. ,  longer titles) than to explicit security terminology.

1 Introduction

Large Language Models (LLMs) are increasingly prevalent in everyday applications and assistive tasks, driven by advances in transformer-based architectures and large-scale training [ brown2020language , ouyang2022training , openai2023gpt4 , attention2017 ] . These advances have enabled models with unprecedented scale (often comprising billions or even trillions of parameters) and strong capabilities across a wide range of natural language and code-related tasks [ openai2023gpt4 ] . As a result, software engineering (SE) is entering a new phase increasingly shaped by AI teammates : autonomous, task-driven agents capable of performing complex software development activities such as feature implementation, debugging, testing, and code review with limited human oversight [ li2025se30 , hassan2025agenticse ] .

Autonomous coding agents are now being deployed in modern software engineering workflows, where they independently author pull requests (PRs) that modify production code at scale. Recent progress in LLM reasoning, tool use, and autonomous planning has enabled such agents to perform multi-step development tasks, interact with version control systems, and submit PRs with minimal human intervention [ yao2023reactsynergizingreasoningacting , zhou2024webarenarealisticwebenvironment ] . Consequently, agent-authored PRs are no longer confined to experimental demonstrations but are increasingly observed in real-world GitHub repositories and open-source projects [ watanabe2025agenticpr , jie2025domain ] .

Prior empirical research on LLMs and autonomous agents in software engineering has largely focused on productivity-oriented outcomes, including code generation quality, task completion rates, acceptance ratios, and developer efficiency [ watanabe2025agenticpr , chen2021evaluatinglargelanguagemodels , zhang2024surveylargelanguagemodels ] . These studies demonstrate that autonomous agents can accelerate development workflows and contribute meaningfully to large codebases. However, productivity alone is an incomplete proxy for trustworthiness, particularly in security-critical contexts, where subtle defects may introduce latent vulnerabilities rather than immediate functional failures [ pearce2022asleep , siddiq2022empirical , allegrini2025formalizing , moshkovich2025uncertainty ] .

Software security poses distinct challenges for autonomous coding agents. Security-relevant code changes often require nuanced reasoning about threat models, privilege boundaries, cryptographic usage, configuration semantics, and backward compatibility, areas in which prior work has shown that LLMs may exhibit inconsistent understanding, brittle reasoning, or overconfidence [ pearce2022asleep , li2024knowledge ] . Errors in such changes may evade test suites and static analysis tools, weakening a system’s security posture without immediately observable failures. Despite these risks, the role of autonomous coding agents in security-relevant software development remains poorly understood.

Existing empirical studies provide limited insight into this problem space. Most analyses treat agent-authored pull requests as a largely homogeneous category, without distinguishing security-relevant changes from routine maintenance tasks such as refactoring, dependency updates, or formatting fixes [ zhang2024surveylargelanguagemodels , watanabe2025agenticpr , wang2025automated ] . At the same time, research on LLM-based security evaluation has primarily focused on isolated tasks, such as vulnerability detection, secure code generation, formal verification, or question answering, rather than on how security work unfolds within realistic development workflows and human review processes [ pearce2022asleep , siddiq2024sallm , chatterjee2025proofwright ] . While these efforts help understand models’ capabilities, they offer limited visibility into how autonomous agents contribute to security in practice and how such contributions are scrutinized by human developers.

Consequently, we lack a systematic understanding of (i) how frequently autonomous coding agents engage in security-relevant development, (ii) what types of security work they perform in practice, (iii) the actions and intents reflected in agent-authored security changes, and (iv) how human developers evaluate and scrutinize such work during code review. Addressing these gaps is essential for assessing the trustworthiness and governance of GenAI-enabled software systems as autonomous coding agents become increasingly embedded in real-world development workflows.

In this work, we present the first large-scale empirical study of security-related Agentic pull requests (Agentic-PRs) in real-world GenAI-enabled GitHub repositories . To conduct this study, we used the AIDev dataset [ li2025aidev ] , which contains a curated dataset of 33,596 PRs authored by five widely deployed autonomous coding agents across diverse repositories, programming languages, and software ecosystems. From this corpus, we systematically identify security-related Agentic-PRs using a rule-based filtering strategy applied to PR titles and descriptions, and then manually vetted them.
We analyze each security-related Agentic-PRs along multiple complementary dimensions. First, we measure prevalence , quantifying how frequently autonomous agents engage in security-relevant development relative to their overall activity. Second, we examine security outcomes by analyzing merge and rejection patterns across agents, ecosystems, and types of security-related changes. Third, we analyze the security actions taken by the agents and their intents behind them. Fourth, we study human review behavior using review latency and merge decisions as conservative proxies for reviewer scrutiny in security-related Agentic-PRs. Finally, we investigate early indicators of perceived risk by analyzing lightweight, early-available signals, such as PR size, title, and description length, and security-sensitive terminology, to assess which characteristics are associated with PR rejection.

Throughout the study, we employ a rigorous analysis process that combines quantitative measurement with qualitative interpretation. In particular, we complement large-scale statistical analyses with open coding of a manually validated subset of security-related Agentic-PRs to characterize recurring security actions and underlying intents. Disagreements in qualitative coding are resolved through discussion to ensure interpretive consistency. Together, this methodology enables us to systematically characterize how autonomous coding agents engage with security-critical development tasks in practice and how human developers evaluate and scrutinize such contributions during real-world code review.

- •

RQ1: How frequently do autonomous coding agents contribute security-relevant software changes to GitHub repositories? We quantify the prevalence of security-related agentic pull requests across five widely deployed autonomous coding agents. Our analysis establishes a system-level baseline showing that security-relevant contributions constitute a non-trivial but minority share of agent activity and vary substantially across agents and task categories.

- •

RQ2: How do the outcomes of agent-authored security-related PRs vary across agents, programming ecosystems, and types of code changes? We compare merge rates and closure outcomes of security-related Agentic-PRs across agents, programming languages, ecosystem domains, and PR types. The results reveal notable differences in acceptance patterns, indicating that security outcomes are sensitive to both agent design and contextual factors such as ecosystem and change type.

- •

RQ3: What security-related actions and design intents are reflected in agent-authored security PRs? Using open coding on a manually validated subset of security-related Agentic-PRs, we identify recurring security actions ( e.g. ,  testing, documentation, error handling, vulnerability mitigation) and the underlying intents motivating these changes. This analysis shows that agent-authored security work often emphasizes supportive and preventive security activities rather than narrowly scoped vulnerability fixes.

- •

RQ4: How does human review shape the outcomes of agent-authored security PRs? We analyze reviewer behavior by comparing merge decisions and review latency for security-related versus non-security Agentic-PRs. Our findings indicate that security-related agent contributions are subject to heightened human scrutiny, reflected in lower merge rates and longer review times, with substantial variation across agents.

- •

RQ5: Which early, observable signals help identify potentially risky or rejected security-related agent-authored pull requests? We examine lightweight signals available at pull-request creation time, such as PR size, title and description length, and security-sensitive terminology, and assess their association with PR rejection. The results suggest that complexity and verbosity are stronger predictors of rejection than explicit security topics, highlighting the nuanced nature of reviewer risk assessment.

1.1 Manuscript Contributions

This work makes the following contributions:

- •

Quantify the prevalence and distribution of security-relevant Agentic-PRs autonomous coding agents perform in practice.

- •

Analyze how merge rates, rejection patterns, and review outcomes for security-related Agentic-PRs vary across autonomous coding agents, programming ecosystems, and types of code changes.

- •

Identify recurring security actions and underlying intents reflected in agent-authored PRs, providing qualitative insight into how agents engage with security-relevant tasks.

- •

Examine review latency and merge decisions to assess whether and to what extent human reviewers apply heightened scrutiny to security-related PRs authored by autonomous agents.

- •

Identify early, observable metadata and textual features available at PR creation time that are associated with PR rejection, shedding light on factors that influence perceived risk and human trust in agent-authored security contributions.

1.2 Manuscript Organization

The remainder of this manuscript is organized as follows. Section 2 introduces the necessary background and situates our work within the existing literature on autonomous coding agents, pull requests, and software security. Section 3 describes our empirical study design, including the dataset, security relevance identification, and analysis procedures. Section 4 presents the results addressing each research question. Section 5 discusses the implications of our findings, limitations, and directions for future work. Finally, Section 6 concludes the paper.

2 Background & Related Work

This section introduces the background necessary to contextualize our study and positions it with respect to prior work on LLMs in software engineering, software security evaluation, and empirical studies of pull requests and code review.

2.1 LLMs and Autonomous Coding Agents in Software Engineering

Large Language Models (LLMs) have rapidly become integral to modern software engineering workflows, supporting tasks such as code completion, code generation, debugging, testing, and documentation [ chen2021evaluatinglargelanguagemodels , zhang2024surveylargelanguagemodels ] . Recent advances in model scale, reasoning, and tool use have enabled the emergence of autonomous coding agents : systems that can independently perform multi-step development tasks, interact with development tools and version control systems, and author PRs with limited or no human intervention [ yao2023reactsynergizingreasoningacting , zhou2024webarenarealisticwebenvironment ] .

Early empirical studies of LLM-authored artifacts have primarily emphasized productivity-oriented outcomes, such as task completion rates, merge or acceptance ratios, and developer efficiency [ chen2021evaluatinglargelanguagemodels , zhang2024surveylargelanguagemodels ] . While these results demonstrate that autonomous agents can meaningfully contribute to real-world repositories, they provide limited insight into how such contributions affect non-functional properties , particularly software security. Our work builds on this line of research by explicitly examining agent-authored PRs through a security-specific and workflow-centric lens.

Several works have established conceptual foundations for agentic software engineering. Hassan et al. [ hassan2025agenticse ] articulate the notion of Software Engineering 3.0 , positioning autonomous AI agents as collaborative teammates and outlining foundational pillars and open research challenges. Complementing this perspective, Hoda [ hoda2025beyondcode ] argues that agentic software engineering must extend beyond code to encompass shared vision, values, and vocabulary, while Sapkota and Roumeliotis [ sapkota2025vibecoding ] contrast agentic coding with more ad-hoc “vibe coding” practices. Earlier work in agent-oriented software engineering [ zambonelli2004ao ] provides historical context for many of the coordination, autonomy, and governance challenges that now re-emerge in LLM-based agentic systems.

Beyond conceptual framing, multiple studies propose methodologies and platforms for agent-based software development. Bandara et al. [ bandara2025agentsway ] introduce Agentsway , a development methodology for AI-agent-based software teams, while Rasheed et al. [ rasheed2024codepori ] and Sami et al. [ sami2024unified ] present large-scale multi-agent platforms that support autonomous software development. Surveys by Wang et al. [ wang2025agenticprogramming ] and Li et al. [ li2025se30 ] further synthesize techniques, challenges, and opportunities in agentic programming and AI teammates, highlighting issues of coordination, evaluation, and reliability.

Understanding how humans collaborate with autonomous agents is also critical for their adoption in practice. Klieger et al. [ klieger2024chatcollab ] empirically study collaboration patterns between humans and AI agents in software teams, while Ronanki [ ronanki2025trustworthy ] focuses on mechanisms for fostering trustworthy human–agent collaboration in LLM-based multi-agent systems. Practitioner-oriented studies reinforce these socio-technical concerns, emphasizing trust calibration, accountability, and workflow disruption across the software development life cycle [ akbar2025practitioner , sarkar2025productivity ] .

Empirical evidence on the behavior of agentic systems in real-world software artifacts is rapidly accumulating. Watanabe et al. [ watanabe2025agenticpr ] analyze agent-authored PRs on GitHub and report high merge rates ( i.e. ,  54.9%), highlighting the productivity potential of autonomous coding agents. Complementary work by Jie et al. [ jie2025domain ] examines AI-authored PRs from a domain-level perspective, showing that acceptance rates and review latency vary substantially across software domains. Hasan et al. [ hasan2025testing ] investigate testing practices in open-source agent frameworks and agentic applications, revealing gaps in test coverage and quality assurance. In contrast to these studies, our work does not focus on general productivity or domain-level acceptance patterns of agent-authored PRs; instead, we explicitly center on security-relevant Agentic-PRs and analyze the security intents, actions, and review scrutiny that emerge when autonomous agents engage in security-sensitive software changes, dimensions not examined in prior work.

Beyond productivity and collaboration, several studies examine correctness, safety, and reliability properties of agentic systems. Allegrini et al. [ allegrini2025formalizing ] formalize safety, security, and functional properties of agentic AI systems, while Chatterjee et al. [ chatterjee2025proofwright ] introduce agentic approaches to formal verification for CUDA programs. Moshkovich and Zeltyn [ moshkovich2025uncertainty ] further explore techniques for observing, analyzing, and optimizing agentic systems under uncertainty, underscoring the need for principled governance and monitoring mechanisms.

While prior research has advanced conceptual frameworks, development methodologies, and empirical analyses of agentic software artifacts, most studies either focus on productivity and collaboration or analyze agentic outputs at a coarse granularity. In contrast, our work specifically examines security-relevant behavior of autonomous coding agents within real-world pull-request workflows, integrating large-scale quantitative analysis with qualitative interpretation of agent actions, intents, and human review dynamics.

2.2 LLMs and Software Security

A growing body of work has examined the security implications of LLM-generated code. Early studies found that a substantial fraction of LLM-generated programs contain vulnerabilities, even when models produce syntactically correct and functional code [ pearce2022asleep ] . Subsequent empirical analyses further document security weaknesses across languages and tasks [ siddiq2022empirical , sandoval2022security , hajipour2023systematically ] , and propose mitigation strategies such as static-analysis–guided ranking or filtering of model outputs [ siddiq2023franc ] .

To support systematic security evaluation of LLM-generated code, several benchmarks and frameworks have been proposed. These include scenario-based vulnerability assessments [ pearce2022asleep ] , CWE-driven prompt suites such as SecurityEval [ siddiq2022seceval ] , and static-analysis–based testing pipelines such as CyberSecEval [ bhatt2023purple ] . While these efforts advance the evaluation of LLMs for secure code generation and vulnerability detection, they largely focus on isolated code-level tasks. In contrast, our study investigates security behavior in a workflow-centric setting , analyzing how autonomous agents perform security-related work within real PR-based development processes.

2.3 PRs and Security

Pull requests (PRs) are a central coordination mechanism in modern software development, serving as a primary vehicle for code contribution as well as a focal point for review, discussion, and quality assurance. Several empirical research has examined PR processes, identifying factors that influence acceptance and rejection decisions, review latency, and reviewer behavior. Prior studies show that PR outcomes are shaped by a combination of technical characteristics, such as code complexity, change size, and test coverage, and social or contextual factors, including contributor experience and reputation, reviewer workload, and social signals embedded in discussion threads [ mcintosh2014impact , rigby2014peer , baysal2016investigating ] . Subsequent work further demonstrates that review difficulty and latency are influenced by how changes are scoped and presented, with large or complex PRs being harder to review and more likely to experience delays or rejection [ ram2018easierreview , zhang2022prlatency ] .

Security-related pull requests introduce additional challenges beyond those observed for general code changes, as they often involve subtle design decisions, domain-specific expertise, and risk-sensitive trade-offs. In this work, we define a security-related PR as a pull request whose stated intent or code changes explicitly involve security-relevant concerns, such as vulnerability mitigation, authentication or authorization logic, cryptographic usage, secure configuration, dependency security updates, or compliance with security standards and regulations. This definition is consistent with prior empirical security studies that operationalize security relevance using a combination of developer intent, textual artifacts ( e.g. ,  PR titles and descriptions), and the nature of the modified code [ rigby2014peer , wang2025automated ] .

Empirical studies suggest that security-related PRs are treated differently from general PRs during review. Lenarduzzi et al. [ lenarduzzi2021codequalitypr ] show that PRs containing quality issues, including security-related problems, are less likely to be accepted, while Zhang et al. [ zhang2021prdecision ] highlight that decision-making criteria vary substantially depending on the perceived risk and impact of the change. More recent work has examined security PRs in the context of automated dependency management tools. Rebatchi et al. [ rebatchi2024dependabotsecurityprs ] conduct a large-scale empirical study of Dependabot security PRs and show that, despite being automated and security-focused, such PRs still face non-trivial review delays and rejection rates, reflecting developer caution toward security updates. These findings reinforce the notion that security-related PRs often receive heightened scrutiny due to their potential to introduce subtle but severe vulnerabilities. Complementary work [ wang2025automated ] compares AI-generated and human security patches using the AIDev dataset and examines domain-level variation in agentic pull-request acceptance; in contrast, our study centers security as a first-class dimension by examining the specific security actions agents perform, the intents underlying those actions, how human reviewers scrutinize security-relevant Agentic-PRs, and what early risk signals emerge during review.

Despite this growing body of work, existing PR research has largely focused on human-authored contributions or on automated tools operating in narrowly scoped settings, such as dependency updates. At the same time, recent studies of agent-authored PRs tend to treat security as a secondary concern or subsume it under general productivity metrics. As autonomous coding agents increasingly submit PRs that touch security-sensitive code paths, understanding how security-related agent-authored PRs are evaluated, scrutinized, and governed within real-world review workflows remains an open and underexplored problem which is addressed in this current work.

3 Methodology

This section describes the methodology followed to answer our RQs. As shown in Figure 1 , our work follows a structured, multi-stage empirical process. First, we identify security-relevant Agentic-PRs through keyword-based filtering followed by manual validation. Second, we conduct large-scale quantitative analyses to examine the prevalence of security-related contributions, their outcomes, and patterns of human review and scrutiny. Finally, we perform qualitative open coding and predictive modeling to analyze agent security actions, design intents, and early indicators of risk or rejection.

Figure 1: Overview of our Study’s Methodology.

3.1 Research Questions (RQs)

Autonomous coding agents can author pull requests that modify production code, including changes with potential security implications. In the following research questions (RQs), we investigate the prevalence, outcomes, and oversight of security-related agent activity in practice.

RQ1: How frequently do autonomous coding agents contribute security-relevant software changes to GitHub repositories?

This RQ characterizes how often autonomous coding agents engage in security-critical development activities. By analyzing the frequency and distribution of security-relevant PRs across agents, we establish a system-level baseline of agent participation in security-sensitive software engineering tasks.

RQ2: How do the outcomes of agent-authored security-related PRs vary across agents, programming ecosystems, and code change types?

This research question investigates how security-related PR outcomes differ across autonomous coding agents, programming ecosystems ( e.g. , languages and domains), and categories of code changes. By comparing merge rates and review outcomes across these dimensions, we assess how reliably agents contribute security-relevant changes in different technical contexts.

RQ3: What security-related actions and design intents are reflected in agent-authored security PRs?

This RQ examines how autonomous coding agents engage with security in practice. Using open coding, we analyze agent-authored security-relevant pull requests, including titles, descriptions, and code changes, to identify recurring security actions and the underlying intents that motivate them. This analysis provides insight into the patterns through which agents attempt to improve or modify system security.

RQ4: How does human review shape the outcomes of agent-authored security PRs?

This research question explores how human reviewers respond to security-relevant contributions produced by autonomous coding agents. By analyzing merge decisions and review latency, we assess whether security-related agent contributions receive heightened scrutiny and how such scrutiny varies across agents and repositories.

RQ5: Which early, observable signals help identify potentially risky or rejected security-related agent-authored pull requests?

This research question investigates which early signals available at PR creation time are associated with rejection or perceived risk. By analyzing metadata and textual characteristics, we identify factors that may serve as lightweight indicators for risk assessment and governance of security-relevant contributions produced by autonomous coding agents.

3.2 Dataset of Pull Requests Authored by Autonomous Coding Agents

To answer our RQs, we need a dataset of AI-authored PRs that supports fine-grained analysis of security-related development and human oversight. To this end, we use the AIDev dataset [ li2025aidev ] , a large-scale corpus containing 932,791 PRs authored by autonomous coding agents in real-world GitHub repositories.
The AIDev dataset also provides a curated subset of 33,596 gentic-authored PRs drawn from 2,807 GitHub repositories with at least 100 stars. This curated subset of PRs includes enriched artifacts such as PR titles , descriptions , timestamps , merge outcomes , review comments , review decisions , commit metadata , and file-level diffs .

While the full dataset enables broad coverage, it does not uniformly provide the artifacts required to study security outcomes and human review behavior. Therefore, we use the AIDev’s curated subset of 33,596 PRs .

3.3 Answering RQ1: Prevalence of Security-Relevant Agentic-PRs

To answer RQ1 , we quantify the prevalence of security-relevant pull requests authored by autonomous coding agents. This analysis establishes a system-level baseline of how frequently GenAI-enabled software systems engage in security-critical development activities.
To do so, we identify security-related Agentic-PRs through a two-stage process that combines automated filtering with manual validation.

3.3.1 Stage 1: Keyword-based PR filtering

In the first stage, we used a conservative, keyword-based filter to identify candidate security-related PRs based on their titles and descriptions. This step is intentionally inclusive and designed to capture PRs that may involve security concerns. Specifically, we searched for a curated list of security-related terms commonly used in software development practice, spanning multiple security dimensions.
These terms are:
(i) general security concepts ( i.e. , security , vulnerability , threat );
(ii) vulnerability identifiers and exploit terminology ( i.e. , CVE , exploit , patch , audit );
(iii) attack classes and adversarial behaviors ( i.e. , XSS , CSRF , injection , buffer overflow , RCE , remote code execution , privilege escalation , DoS , DDoS , malicious );
(iv) authentication and authorization mechanisms ( i.e. , auth , authentication , authorization , password , token , credential , secret );
(v) data protection and cryptographic concepts ( i.e. , encryption , sanitize , PII , leaks ); and
(vi) regulatory and compliance-related terms ( i.e. , GDPR , HIPAA , compliance ).

These keywords are matched using case-insensitive regular expressions with word-boundary constraints to reduce false positives. A PR is then flagged as a candidate security PR if at least one keyword appears in its title or body. After this filtering step, we initially identify 2,598 candidate security-related agentic authored PRs in the curated AIDev subset.

3.3.2 Stage 2: Manual Vetting

In the second stage, we manually inspect these 2,598 candidate PRs to determine whether they are genuinely security-relevant . Three of our authors are involved in this manual analysis who have experience in software development and software security research for 4-6 years.

A security PR is one whose primary intent is to prevent, mitigate, detect, or remediate a security vulnerability or security risk , including fixes for known vulnerabilities, hardening of security mechanisms, corrections to authentication or authorization logic, cryptographic updates, or changes explicitly motivated by security or compliance concerns. PRs that merely mention security-related terms incidentally ( e.g. , documentation, configuration defaults, or unrelated refactoring) are treated as false positives. Based on this manual validation, we identified 1,293 security-related PRs .

3.4 Answering RQ2: Differences Across Agents, Ecosystems, and Code Change Types

To answer RQ2 , we analyze how the outcomes of Agentic-PRs vary across autonomous coding agents, programming ecosystems, and types of code changes. We group security-relevant Agentic-PRs by coding agent and compute, for each agent, the total amount of security PRs, the number of closed PRs, and the corresponding merge rate. To provide additional context, we also identify the dominant programming language associated with each agent’s security PRs.

We further examine how security outcomes vary across different types of code changes.
As a starting point, we leverage the coarse-grained PR-type tags provided by the AIDev dataset [ li2025aidev ] , which are automatically inferred using lightweight, rule-based heuristics applied to PR titles ( e.g. , fix , feat , add , config , etc. ).
As noted by Li et al. [ li2025aidev ] , these tags are intended to provide an approximate characterization of PR intent rather than definitive ground truth and may exhibit overlap or ambiguity, particularly for security-related changes.

To address these limitations, we manually inspected all 1,293 security-relevant Agentic-PRs identified in RQ1 (Section 3.3 ). During this process, we considered both the PR content (code diffs, descriptions, and discussion) and the AIDev-provided PR-type tags as contextual cues. Rather than relying on individual fine-grained labels ( e.g. , fix vs. patch vs. resolve ), we assigned each PR to a single coarse-grained security change category that best reflects the primary nature of the security-related modification. This manual categorization follows the same validation protocol used for security relevance labeling in RQ1. Specifically, we classify security-related Agentic-PRs into four mutually exclusive categories:

- •

Dependency Update : PRs that modify third-party dependencies or library versions without directly changing application logic. These changes are typically preventive or maintenance-oriented and may incorporate upstream security fixes. These PRs are frequently flagged with bump , upgrade , dependency , and chore(deps) tags.

- •

Vulnerability Fix : PRs that directly remediate identified security flaws or weaknesses in the codebase, including fixes associated with known vulnerabilities, CVEs, or exploitable behaviors.
These PRs are commonly flagged with fix , patch , resolve , vuln , cve , and exploit tags.

- •

Security Feature : PRs that introduce new security-related functionality or extend existing security mechanisms, such as authentication, authorization, access control, encryption, or auditing logic.
These PRs are frequently flagged with feat , add , implement , support , and new tags.

- •

Config / Compliance : PRs that adjust security-relevant configuration files, policy definitions, or compliance-related artifacts ( e.g. , access rules, security settings, or regulatory constraints) without introducing new application logic.
These PRs are frequently flagged with config , setting , policy , audit , and compliance tags.

Using these manually validated coarse-grained categories, we compute the volume and merge rate of security-related Agentic-PRs across agents, ecosystems, and change types. This approach enables systematic comparison of security outcomes while avoiding reliance on noisy or overlapping fine-grained PR labels.

3.5 Answering RQ3: Security Actions and Intents in Agentic-PRs

To answer RQ3 , we conduct a qualitative analysis of security-relevant pull requests authored by autonomous coding agents using open coding [ strauss1998basics ] . Our goal is to understand what security-relevant Agentic-PRs are doing in practice , rather than to evaluate their correctness or downstream impact.

For each of the 1,293 agentic security PRs we collected in RQ1, we analyze their title and description, which often articulate the agent’s stated intent. We apply open coding following established qualitative analysis practices. Two authors independently examine PR artifacts line by line and assign two complementary types of codes:
(1) security-related actions , which capture what concrete change the agent performs in the code ( e.g. ,  adding input validation, modifying authentication logic, introducing access controls, or updating dependencies); and
(2) security intents , which capture why the change is being made , reflecting the agent’s stated or implied motivation ( e.g. ,  mitigating a vulnerability, hardening security posture, preventing misuse, or improving compliance).

Actions and intents are coded separately to avoid conflating implementation mechanisms with their underlying security rationale. Codes are derived inductively from the data without relying on predefined vulnerability taxonomies such as Common Weakness Enumeration (CWE) or the Open Worldwide Application Security Project (OWASP).

To better illustrate our qualitative analysis process, Figure 2 presents three representative security-related Agentic-PRs annotated using open coding.
In each example, salient security-relevant elements in the PR title and description are highlighted (shown in red) and mapped to corresponding action and intent codes.

For instance, in PR #291, which addresses an open redirect vulnerability, phrases such as “validating the Referer header” and “using safeRedirect ” are highlighted and coded as Actions capturing the concrete remediation steps taken by the agent.
The stated rationale, “fix open redirect vulnerability”, is separately coded as the Intent , reflecting the underlying security motivation rather than the implementation mechanism. Similarly, PR #3470 focuses on preventing header injection by sanitizing newline characters and adding unit tests. In this example, the introduction of sanitization logic and test cases is coded as Actions , while the broader goal of ensuring header security is captured as the Intent . In contrast, PR #6759 addresses CVE-2023-36665 by upgrading the protobufjs dependency to a secure version. The dependency upgrade is coded as the primary Action , whereas mitigating a known vulnerability constitutes the associated Intent .

Throughout the process, we employ constant comparison, iteratively refining codes as new PRs are analyzed. Conceptually overlapping codes are merged, while distinct patterns are preserved to maintain analytic granularity. Analytic memos are maintained to document coding decisions and emerging themes. Disagreements between coders are resolved through discussion and consensus. The final codebook is then applied consistently across the dataset.

While our goal is not statistical generalization, this process ensures interpretive rigor and transparency. Using the finalized codes, we report the frequency and distribution of recurring security actions and intents across agents and programming ecosystems.

Figure 2: Examples of open coding applied to security-related Agentic pull requests.

3.6 Answering RQ4: Reviewer Behavior and Scrutiny of Security Agentic-PRs

To address RQ4 , we analyze whether human reviewers treat security-relevant Agentic-PRs differently from non-security Agentic-PRs, focusing on observable review outcomes and review latency as proxies for reviewer scrutiny.

Review Scrutiny Proxies

Since a reviewer’s intent and reasoning are not directly observable, we operationalize reviewer scrutiny using two conservative, outcome-based proxies commonly used in empirical software engineering research [ li2025aidev ] :

- (1)

Merge rate , where lower acceptance rates may indicate heightened reviewer caution or stricter evaluation criteria. We compute the merge rate as being the number of merged PRs divided by the total number of closed PRs.

- (2)

Review latency , measured as the elapsed time between PR creation and PR closure (merged or rejected). Longer review times may reflect deeper inspection or extended discussion, whereas shorter times may indicate expedited handling, such as urgent security fixes.

For all closed PRs in the curated subset of the AIDev dataset [ li2025aidev ] , we compute review latency (in hours) as the difference between the PR creation timestamp and its closure timestamp. We exclude PRs with missing timestamps or non-positive durations to ensure reliable measurement. This analysis is conducted on two disjoint sets of Agentic-PRs: 1,130 close PRs identified as security-related using our keyword-based filtering and manual validation procedure, and 30,154 remaining closed Agentic-PRs in the curated subset that were not identified as security-related by this procedure.

To assess whether observed differences in review latency are statistically significant, we apply the non-parametric Mann–Whitney U test [ mann1947test ] . This choice is motivated by the highly skewed distribution of PR review times and avoids assumptions of normality. We report in Section 4.4 descriptive statistics alongside statistical test results to support robust interpretation.

To account for variation in reviewer trust across agents, we further compute agent-specific median review latencies for security and non-security PRs. By comparing within-agent differences, we assess whether certain agents experience disproportionately higher or lower scrutiny when submitting security-relevant changes relative to their typical contributions.

3.7 Answering RQ5: Early Predictors of Risky or Rejected PRs

To address RQ5 , we investigate whether early, observable signals available at PR creation time can help predict whether a security-relevant Agentic-PR will ultimately be rejected.

Dataset and Target Definition

We restrict this analysis to closed security-relevant Agentic-PRs, since open PRs lack definitive outcomes. In our dataset of 1,293 security-relevant PRs , 1,130 of them were closed. Following our dataset schema, we label a PR as rejected if it is closed without being merged ( i.e. , merged_at is missing), and as merged otherwise. In this way, we have 435 rejected PRs (38.5%) and 695 merged PRs . This binary outcome serves as a conservative proxy for perceived risk, insufficient confidence, or lack of acceptance of the agent-generated security contribution.

Early Feature Extraction (Structured Signals)

From each PR, we extract lightweight features that are available at creation time (or immediately after PR creation in the platform metadata). Concretely, we compute: (i) PR size , defined as additions + deletions when available; when unavailable, we use PR body length as a fallback proxy; (ii) description length and title length ; (iii) a binary indicator for whether the PR title contains sensitive security keywords as defined in Section 3.4 ( e.g. , auth , crypto , token , password , key , credential , payment ); and (iv) agent identity , encoded via label encoding. Before training predictive models, we perform descriptive analysis by comparing feature distributions across merged vs. rejected PRs and examining associations between individual features and rejection outcomes.

Train/Test Split and Class Imbalance

We use a stratified random split, holding out 30% of PRs for testing and using the remaining 70% for training. Because merged and rejected PRs are typically imbalanced, we apply class-balanced weighting during model training across all classifiers.

Structured-Feature Prediction Models

We evaluate two structured-data classifiers. First, we train a logistic regression model with feature standardization as a simple, interpretable baseline [ hosmer2013applied ] . Second, we train a Random Forest classifier [ breiman2001random ] to capture potential non-linear relationships and feature interactions among early signals. We choose Random Forests because they (i) perform robustly on mixed-scale tabular features with minimal tuning, (ii) naturally model non-linearities and interactions, and (iii) provide feature-importance estimates that support interpretability. We report precision, recall, and F1-score on the held-out test set, and we analyze coefficient magnitudes (logistic regression) and feature importance (Random Forest) to identify the most influential early predictors.

Text-Based Prediction Models

To evaluate whether PR text alone can predict rejection, we train three text classifiers using PR titles and descriptions concatenated into a single document. As a lightweight linear baseline, we train a TF–IDF + linear SVM classifier [ salton1988term , joachims1998text ] with class-balanced weighting. We then train a fastText supervised classifier [ joulin2017fasttext ] as an efficient embedding-based model suitable for short technical text. Finally, we fine-tune a pre-trained DistilBERT model [ sanh2019distilbert ] for binary sequence classification using standard training settings (max sequence length 128, 3 epochs, learning rate 2 × 10 − 5 2\times 10^{-5} ) and incorporate class weights in the loss function to account for imbalance. We compare performance across the structured-feature models and text-only models to assess whether semantic cues in PR text provide a predictive signal beyond lightweight metadata.

4 Results

In this section, we present the answers to our research questions.

4.1 RQ1: Prevalence and Distribution of Security-Relevant Agentic PRs

We first examine how frequently autonomous coding agents contribute security-relevant pull requests and how these contributions are distributed across agents.
Figure 3 summarizes the prevalence of security-relevant Agentic-PRs. From the curated AIDev dataset, we identified 1,293 security-related PRs . These 1,293 PRs represent 3.85% of all 33,596 Agentic-PRs in the curated dataset.

Figure 3: RQ1 Results – Prevalence of Security-relevant PRs Across Different Autonomous Coding Agents

Security-relevant contributions are unevenly distributed across agents. Claude Code shows the highest proportion of security-relevant PRs ( 459 PRs – 14.6% ), followed by Copilot ( 4,970 PRs – 10% ) and Devin ( 4,827 PRs – 7.6% ). OpenAI Codex is the agent with the least proportion of security-focused PRs, with only 1.3% of its PRs confirmed as security-relevant after manual validation.

4.2 RQ2: Security Outcomes Across Agents, Ecosystems, and Code Types

This RQ examines whether the merge rates of security-related PRs vary across autonomous coding agents, programming ecosystems, and types of code changes. We compute the merge rate as being the number of merged PRs divided by the total number of closed PRs (merged or un-merged).

Merge Rates Per Agent

Figure 4 summarizes the statuses of the security-related pull requests authored by each agent.
As observed in this figure, we found that OpenAI Codex achieves the highest merge rate (86.59%) followed by Cursor (76.47%) Claude Code (58.62%), and Devin (52.12%) while Copilot (49.60%) demonstrates the lowest merge rate.

Figure 4: RQ2 Results – Outcomes of Security-Related Pull Requests Authored by Agents.

Merge Rates Across Programming Languages

Table 1 reports the most frequent programming languages among security-related Agentic-PRs and their corresponding merge rates, sorted by merge rate.
While TypeScript accounts for the largest numbers of security PRs (447 PRs), it exhibits a comparatively lower merge rate (56.51%), suggesting stricter review or higher rejection likelihood in this ecosystem.
In contrast, Python security PRs (252 PRs) achieve a higher merge rate (68.30%), indicating more favorable acceptance outcomes.

Languages with smaller numbers, such as Ruby and HTML , exhibit the highest merge rates (above 80%); however, these results should be interpreted cautiously due to limited sample sizes. Mid-volume systems-oriented languages, including Go , Java , and C# , show relatively consistent merge rates around 60–62%, suggesting more uniform reviewer expectations in these ecosystems. Notably, Rust security PRs have the lowest merge rate (51.16%), which may reflect heightened scrutiny in safety-critical or performance-sensitive contexts.

Table 1: Top 10 languages for security PRs and their merge rates.

Language Total # PRs Merge Rate (%)

Ruby 20 83.33

HTML 26 82.61

Python 252 68.30

JavaScript 48 65.00

Dart 19 63.16

Go 108 61.70

Java 48 60.00

C# 103 60.53

TypeScript 447 56.51

Rust 51 51.16

Merge Rates Per Domain

Table 2 aggregates security-related PRs into broader ecosystem domains. At the domain level, Data/ML exhibits the highest merge rate among the major domains (63.71%), followed closely by Web (62.11%) and Enterprise (60.18%), while Systems has the lowest merge rate (56.15%). Operations security PRs achieve the highest overall merge rate (69.70%); however, it is important to highlight this result is based on a very small number of PRs (35) and should therefore be interpreted with caution.

Table 2: Security PR outcomes aggregated by ecosystem domain.

Domain Total # PRs Merge Rate (%)

Web 606 62.11

Data/ML 262 63.71

Enterprise 156 60.18

Systems 216 56.15

Operations 35 69.70

Distribution and Merge Rates of Security Change Types

Table 3 summarizes how autonomous coding agents distribute their security-related work across major security change categories and also reports aggregate category totals and merge rates. Overall, Security Feature and Vulnerability Fix PRs account for the largest share of security-related changes, with Security Feature PRs being both the most prevalent and exhibiting higher aggregate merge rates than Vulnerability Fix PRs. In contrast, Configuration/Compliance and Dependency Update PRs occur less frequently but achieve comparatively high merge rates.

At the agent level, variation emerges in how security work is distributed. For example, Claude Code predominantly contributes Security Feature PRs (68.7%), whereas Copilot places greater emphasis on Vulnerability Fix PRs (50.5%). Cursor and OpenAI Codex exhibit more balanced distributions between these two categories while also contributing a non-trivial share of Configuration/Compliance PRs. Overall, these patterns indicate that agents prioritize distinct forms of security work rather than converging on a uniform security contribution profile.

Table 3: Nature of security work by agent: percentage breakdown of categories within each agent’s security PRs. Aggregate category volumes and merge rates are shown at the top.

Agent / Aggregate Sec. Feat. Vuln. Fix Conf./Compl. Depn. Update

Total # PRs 554 506 134 113

Merge Rate (%) 64.61 53.94 70.08 65.66

Claude Code 68.7 25.4 0.0 6.0

Copilot 33.1 50.5 3.8 12.5

Cursor 40.3 41.6 14.3 3.9

Devin 51.6 27.5 13.9 7.1

OpenAI Codex 40.6 35.7 17.8 5.9

4.3 RQ3 Results: Security Actions and Intents in Agentic-PRs

After open coding 1,293 manually confirmed security-relevant Agentic-PRs from the curated AIDev subset, we identify recurring security actions (what agents do) and security intents (why agents do it). We report only themes that appear in at least 10 PRs to focus on stable and recurrent patterns.

4.3.1 Security Actions Performed by Autonomous Agents

Distribution of Security Actions and Intents

Table 4 summarizes the most frequent security actions and security intents identified through open coding across the 1,293 security-relevant Agentic-PRs. Actions capture how agents modify the codebase, while intents capture why those changes are made.

Table 4: Security actions and intents identified via open coding (themes with fewer than 10 occurrences omitted).

Actions

Theme # Theme #

Code Refactoring 957 Testing 755

Documentation 692 Error Handling 595

Security Improvements 580 API Development 540

Configuration Management 495 User Experience Enhancement 484

Input Validation 434 Authentication & Authorization 377

Dependency Management 367 Performance Optimization 313

Logging and Monitoring 262 Compatibility Maintenance 179

Version Control 143 Database Management 49

Others 28

Intents

Theme # Theme #

Functionality Improvement 890 Vulnerability Mitigation 741

User Experience 697 Error Handling 604

Security Enhancement 531 Testing and Reliability 468

Compatibility Assurance 457 Performance Optimization 389

Code Quality 376 User Guidance 340

Maintainability 335 Compliance and Standards 255

Documentation Improvement 218 Development Efficiency 183

Resource Management 82

Overall, agentic security work is dominated by a small number of recurring implementation patterns. On the action side, Code Refactoring (957), Testing (755), and Documentation (692) are most prevalent, indicating that security improvements are often realized through restructuring existing code, adding or extending tests, and clarifying usage or constraints rather than introducing entirely new mechanisms. Lower-level but still common actions such as Error Handling , Configuration Management , and Input Validation further suggest a focus on robustness and defensive hardening.

Figure 5: Co-occurrence Network of Security Actions.

On the intent side, Functionality Improvement (890) and Vulnerability Mitigation (741) are the two dominant motivations. Notably, a large fraction of security-relevant PRs are framed as improving functionality or developer experience rather than narrowly fixing a specific vulnerability, reinforcing that security work in practice is often intertwined with broader maintenance and evolution goals. Intents related to User Experience , Reliability , and Compatibility Assurance also appear frequently, reflecting a preventive and quality-oriented framing of security changes.

Action–Intent Co-occurrence Patterns

To move beyond marginal frequencies, we analyze how security-related actions and intents co-occur within the same Agentic-PRs. We quantify these associations using pairwise lift , which measures how much more frequently two themes co-occur than would be expected if they were independent, and the ϕ \phi coefficient, which captures the strength of correlation between two binary-coded themes. We identify recurring and statistically strong links between how agents modify code and why those changes are made. The resulting co-occurrence patterns show that agentic security work is rarely one-dimensional. Instead, agents systematically pair concrete implementation techniques with aligned security motivations. In Figure 5 and Figure 6 , we present their co-occurrence networks.

From the result, we found several strong and intuitive associations. Documentation actions exhibit one of the strongest links to intent, co-occurring frequently with both User Guidance (lift = 2.77, ϕ \phi = 0.41) and Documentation Improvement (lift = 2.70, ϕ \phi = 0.31). This indicates that documentation-related security PRs are commonly motivated by steering correct and secure usage rather than by purely descriptive goals. Similarly, User Experience Enhancement actions show a strong association with User Experience intents (lift = 2.50, ϕ \phi = 0.43), suggesting that agents often frame security improvements as usability fixes that reduce misuse or error-prone interactions.

Performance-related work displays particularly strong coupling. Performance Optimization actions co-occur most frequently with both Performance Optimization intents (lift = 3.50, ϕ \phi = 0.39) and Resource Management intents (lift = 3.54, ϕ \phi = 0.17). These high-lift associations suggest that performance tuning is often treated as security-relevant when it mitigates resource exhaustion, reliability issues, or denial-of-service risks. Likewise, Error Handling actions strongly align with Error Handling intents (lift = 2.05, ϕ \phi = 0.31), reflecting direct remediation of failure modes that could otherwise be exploited.

Beyond direct action–intent pairs, we also observe meaningful co-occurrence among actions themselves. For example, Dependency Management frequently co-occurs with Version Control actions (lift = 2.38), and API Development co-occurs with Database Management (lift = 2.46), indicating that security-related changes often span multiple technical layers within a single PR.
Overall, these co-occurrence patterns demonstrate that agentic security PRs are not collections of isolated fixes. Instead, autonomous agents consistently align specific implementation choices with coherent security rationales. This reinforces the analytical value of separating actions from intents and shows that agent-authored security work blends vulnerability remediation, preventive hardening, and quality improvement within broader software engineering activities.

Figure 6: Co-occurrence Network of Security Intents.

4.4 RQ4: Reviewer Behavior Toward Security Agentic-PRs

To understand how human reviewers treat security-relevant Agentic-PRs, we examine not only aggregate merge outcomes and review latency, but also how reviewer behavior varies with the nature of the security change itself . Rather than treating all security PRs as homogeneous, we analyze reviewer response patterns across different security change categories.

Table 5 summarizes review latency statistics. From the results, we found that security-relevant Agentic-PRs have consistently lower merge rates than non-security PRs i.e. ,  security PRs are merged at only 61.50% , compared to 77.33% for non-security PRs. We also found that Security PRs have a median review latency of 3.92 hours, compared to only 0.11 hours for non-security PRs, and a mean latency more than twice as long (97.45 vs. 38.29 hours). This difference is statistically significant ( p < 0.001 p<0.001 ), indicating substantially increased review time for confirmed security-relevant Agentic-PRs.

Table 5: Review latency (hours) for security vs. non-security merged Agentic-PRs.

PR Type Total # PRs Mean Median Std. Dev.

Security 1,130 97.45 3.92 239.91

Non-Security 30,154 38.29 0.11 140.42

Agent-level analysis (Table 6 ) shows that this effect holds across all agents, though with heterogeneous magnitude. Security-related PRs authored by Devin experience the largest median delay (+16.08 hours), followed by Copilot (+5.46 hours) and Claude Code (+3.42 hours), while OpenAI Codex exhibits minimal latency differences. These differences suggest varying degrees of reviewer scrutiny and trust across agents.

Table 6: Agent-specific median review latency (hours) for security vs. non-security PRs.

Agent Security Non-Security Delta

Devin 23.76 7.68 +16.08

Copilot 18.32 12.87 +5.46

Claude Code 5.13 1.71 +3.42

Cursor 1.08 0.89 +0.18

OpenAI Codex 0.07 0.02 +0.05

To move beyond aggregate counts, we further examine how review latency varies across different security action categories .
Table 7 summarizes review latency statistics conditioned on the primary type of security change.

Table 7: Review latency (hours) for security-related Agentic-PRs by security change category.

Category Total # PRs Mean Std. Dev. Median

Config / Compliance 127 127.17 341.67 0.86

Security Feature 486 105.53 253.86 9.95

Vulnerability Fix 432 84.19 190.43 3.35

Dependency Update 99 83.40 185.83 4.36

Security Feature PRs exhibit the longest median review latency ( 9.95 hours), substantially exceeding that of Vulnerability Fix PRs ( 3.35 hours) and Dependency Update PRs ( 4.36 hours).
In contrast, Config/Compliance PRs are reviewed markedly faster, with a median latency of only 0.86 hours.
These differences suggest that reviewers distinguish between classes of security work: changes that introduce or extend security mechanisms tend to trigger deeper inspection and longer deliberation, whereas configuration-level or compliance-oriented changes are often resolved more quickly.

4.5 RQ5: Early Predictors of Risky or Rejected Security Agentic-PRs

This research question examines whether early, observable signals available at pull-request creation time can help predict whether a security-relevant Agentic-PR will be rejected ( i.e. , closed without merge). Our analysis focuses on the curated dataset of manually validated security-related Agentic-PRs. In total, we analyze 1,130 closed security PRs, of which 435 are rejected, corresponding to a rejection rate of 38.5% .

Table 8: Association between early signals and PR rejection in the curated security PR dataset (logistic regression coefficients).

Feature Coefficient ( β \beta )

Title length 0.316

PR size 0.049

Description length 0.049

Sensitive keyword in title − - 0.054

Agent (encoded) − - 0.268

Among the examined early signals, title length shows the strongest positive association with PR rejection, exhibiting the largest logistic regression coefficient ( β = 0.316 \beta=0.316 ), followed by PR size and description length (both β ≈ 0.049 \beta\approx 0.049 ). Consistent with these associations, rejected PRs tend to be larger and more verbose on average: rejected PRs involve a mean of 2,720.3 lines changed compared to 1,873.1 for merged PRs, and have longer titles on average (59.8 vs. 52.7 characters). Together, these results suggest that early signals related to PR complexity and explanatory burden are associated with a higher likelihood of rejection.
In contrast, the presence of sensitive security-related keywords in PR titles exhibits a weak negative association with rejection ( β = − 0.054 \beta=-0.054 ) and low importance across predictive models. This indicates that explicitly referencing security-sensitive topics ( e.g. ,  authentication, cryptography, credentials) is not, by itself, a strong early signal of rejection for security-related Agentic PRs.

Table 9: Predictive performance for rejection prediction on the curated security-related Agentic-PR dataset (held-out test set). Metrics are reported for the Rejected class.

Model Accuracy Rej. Precision Rej. Recall Rej. F1

Logistic Regression (structured) 0.58 0.46 0.48 0.47

Random Forest (structured) 0.61 0.49 0.41 0.45

SVM (TF–IDF text) 0.65 0.53 0.72 0.61

fastText (title + description) 0.71 0.62 0.60 0.61

DistilBERT (fine-tuned) 0.64 0.52 0.85 0.64

We next evaluate the predictive power of early signals using both structured-feature and text-based models (Table 9 ). Among structured-feature approaches, logistic regression and Random Forest achieve modest performance, with accuracies of 0.58 and 0.61, respectively, and rejected-class F1-scores below 0.50. Feature-importance analysis for the Random Forest indicates that PR size, description length, and title length dominate prediction, whereas agent identity and the presence of sensitive security-related keywords contribute comparatively little.

Text-based models substantially outperform structured-feature approaches in identifying rejected PRs. A TF–IDF + linear SVM classifier achieves a rejected-class F1-score of 0.61, while a fastText classifier attains comparable rejected-class performance (F1 = 0.61) with the highest overall accuracy (0.71). Fine-tuning a DistilBERT model further increases rejected-class recall to 0.85 and achieves the highest rejected-class F1-score (0.64), indicating that semantic cues in PR titles and descriptions provide strong predictive signal for rejection.

Overall, these results suggest that early indicators of potential rejection are more strongly encoded in the semantic content and verbosity of PR text than in lightweight structured metadata alone. While structured features offer interpretable and low-cost signals, text-based models, particularly pre-trained language models, are more effective at flagging potentially risky or untrusted security-related Agentic-PRs at creation time.

5 Discussion

In this section, we synthesize our findings and discuss their implications for agent security participation, human review dynamics, and the design of autonomous coding agents in security-sensitive software engineering workflows.

5.1 Security Work Is a Meaningful but Secondary Part of Agent Activity

Our results show that security-related Agentic-PRs constitute a non-trivial but minority portion of agent-authored contributions. In the curated AIDev dataset, only 3.85% of Agentic-PRs were manually confirmed as security-relevant (RQ1). While this fraction is small relative to total agent activity, it nevertheless corresponds to over a thousand security-related changes, indicating that autonomous agents are already engaging with security concerns at scale in real-world repositories.

Importantly, this security work is not limited to narrow vulnerability patching. Our qualitative analysis (RQ3) reveals that agents frequently perform substantive security-related actions such as refactoring security-sensitive code, improving error handling, strengthening authentication or input validation logic, managing dependencies, and enhancing tests and documentation. However, many of these actions are framed around broader software engineering goals, such as functionality improvement, usability, maintainability, or compatibility, rather than explicitly as vulnerability remediation. This suggests that agentic security work often takes the form of preventive hardening and quality improvement embedded within routine development tasks, rather than isolated “security-only” interventions.

At the same time, security-related outcomes vary substantially across agents, ecosystems, and change types (RQ2). Some agents consistently achieve high merge rates for security PRs, while others experience lower acceptance, even within the same curated dataset. Similarly, security feature PRs and refactoring-oriented changes tend to be treated differently from vulnerability fixes or dependency updates. These patterns indicate that agent effectiveness in security contexts depends not only on whether a change is security-related, but also on how that security work is expressed, scoped, and integrated into existing development practices.

5.2 Security Actions and Intents Reveal Structured Agent Behavior

By separating security actions (what agents do) from security intents (why they do it), our open-coding analysis exposes systematic patterns in agent-authored security work (RQ3). On the action side, a small set of recurring behaviors, such as code refactoring, testing, documentation, error handling, and configuration management, dominates agentic security contributions. On the intent side, functionality improvement and vulnerability mitigation emerge as the most common motivations, followed closely by user experience, reliability, and compatibility concerns.

Crucially, co-occurrence analysis shows that these actions and intents are not randomly paired. Instead, agents consistently align specific implementation strategies with coherent motivations. For example, documentation actions are strongly associated with user guidance and documentation-improvement intents, while performance optimizations align closely with both performance and resource-management intents. Error-handling actions frequently co-occur with error-handling intents, reflecting direct remediation of failure modes that could otherwise be exploited. These structured action–intent pairings indicate that agentic security PRs are not ad hoc collections of fixes, but rather reflect internally consistent reasoning about security-related changes.

This finding reinforces the analytical value of distinguishing actions from intents: it allows us to capture how agents operationalize security goals through concrete code changes, and how security is often framed as a byproduct of improving robustness, usability, or system quality rather than as an isolated objective.

5.3 Human Reviewers Apply Heightened and Differentiated Scrutiny to Security PRs

Across both aggregate and category-specific analyses, human reviewers treat security-related Agentic-PRs with greater caution than non-security PRs (RQ4). Security PRs exhibit significantly lower merge rates and substantially longer review latencies. In the curated dataset, security PRs are merged at only 61.5% , compared to 77.3% for non-security PRs, and their median review latency is an order of magnitude higher.

This increased scrutiny is not uniform. Agent-level analysis shows that some agents experience much larger review delays for security PRs than others, suggesting that reviewer trust and expectations differ across agents. Moreover, category-level analysis reveals that reviewers distinguish between different kinds of security work. Security feature PRs, which introduce or extend security mechanisms, exhibit the longest review latency, whereas configuration and compliance-related PRs are reviewed much more quickly. This indicates that reviewers apply deeper inspection when changes potentially alter security semantics, while treating configuration-level adjustments as lower risk.

These findings suggest that reviewers do not simply react to the presence of “security” in a PR, but instead make nuanced judgments based on the type, scope, and perceived risk of the security change.

5.4 Rejection Is Driven More by Complexity Than by Security Topic

Our analysis of early predictors of rejection (RQ5) further clarifies how reviewers evaluate security-related Agentic-PRs. Rejection is most strongly associated with indicators of complexity and explanatory burden, such as larger PR size, longer titles, and more verbose descriptions, rather than with explicit references to sensitive security topics. In fact, the presence of security-related keywords in PR titles exhibits little predictive value and is slightly negatively associated with rejection.

Text-based models outperform structured-feature models in predicting rejection, highlighting the importance of semantic cues in PR descriptions. However, even the best-performing models achieve only moderate accuracy, underscoring the context-dependent and nuanced nature of reviewer decision-making in security settings. These results suggest that reviewers may be wary of large, complex agent-authored security changes, regardless of the specific security domain involved, and that acceptance depends heavily on how clearly and narrowly a change is presented.

5.5 Implications for Designing Review-Aware Secure AI Teammates

Our findings have several implications for the design and deployment of autonomous coding agents in security-sensitive workflows. First, agents should prioritize scoped, focused, and well-explained security changes, as increased size and verbosity are associated with higher rejection and longer review times. Second, agent design should account for ecosystem- and language-specific review norms, rather than assuming uniform expectations across repositories. Third, given the heightened scrutiny applied to security PRs, especially those introducing new security mechanisms, agents may benefit from providing structured rationales, risk summaries, or targeted tests to support reviewer trust and reduce review burden.

Overall, our study shows that autonomous coding agents are already participating meaningfully in security-relevant development, but their effectiveness is tightly coupled to human oversight and perception. Designing AI teammates that are not only technically capable, but also review-aware and context-sensitive, is essential as agentic systems become increasingly embedded in collaborative software engineering practice.

5.6 Threats to Validity

As with any large-scale empirical study, our findings are subject to several threats to validity, which we discuss below along with the steps taken to mitigate them.

5.6.1 Construct Validity

A primary threat to construct validity concerns how we operationalize security relevance . We identify security-related Agentic-PRs using keyword-based filtering and heuristic rules applied to PR titles and descriptions. While this approach is consistent with prior empirical security studies, it may still yield false positives or false negatives: PRs that do not match our keyword filters are not manually inspected and are therefore treated as non-security-related, even though some may still contain security-relevant changes.

To mitigate this risk, we deliberately designed our keyword set to be broad and recall-oriented , covering vulnerability terminology, authentication and authorization concepts, cryptographic and data-protection terms, exploit identifiers, and compliance-related language. This inclusive strategy reduces the likelihood of systematically missing entire classes of security-relevant PRs. Candidate PRs identified through keyword matching were then manually inspected to remove incidental or non-security-related cases. Although PRs that did not match any keyword were not manually reviewed and may still contain security-relevant changes, we expect such cases to be comparatively rare given the breadth of the keyword set and the subsequent manual validation step.

5.6.2 Construct Validity

A primary threat to construct validity concerns how we operationalize security relevance . We identify security-related Agentic-PRs using keyword-based filtering and heuristic rules applied to PR titles and descriptions. While this approach is consistent with prior empirical security studies [ kim08 ] , it may still yield false positives or false negatives. To mitigate this risk, we deliberately designed our keyword set to be broad and recall-oriented , covering vulnerability terminology, authentication and authorization concepts, cryptographic and data-protection terms, exploit identifiers, and compliance-related language. This inclusive strategy reduces the likelihood of systematically missing entire classes of security-relevant PRs. Candidate PRs identified through keyword matching were then manually inspected to remove non-security-related cases. While PRs that did not match any keyword were not manually reviewed and may still contain security-relevant changes, we expect such cases to be comparatively rare given the breadth of the keyword set and the subsequent manual validation step.

A second construct validity concern arises from using merge status and review latency as proxies for security outcomes. These measures capture perceived risk and reviewer scrutiny rather than ground-truth security correctness. Accordingly, our conclusions focus on how security-related Agentic-PRs are treated during human review, not on whether merged PRs are objectively secure or rejected PRs are insecure. We further mitigate this threat by complementing quantitative analyses with qualitative open coding (RQ3), which provides insight into the nature and intent of security-related changes beyond outcome metrics alone.

5.6.3 Internal Validity

Threats to internal validity stem from confounding factors such as repository-specific contribution norms, CI failures, reviewer availability, or concurrent project activity that may influence merge decisions and review timelines. While it is infeasible to control for all such factors at scale, we mitigate this threat by comparing security and non-security PRs within the same repositories and by analyzing a manually curated subset of popular repositories.

Observed differences across agents may also reflect unmeasured factors such as deployment context, prompting strategies, task allocation, or configuration settings. Consequently, our findings should be interpreted as descriptive associations rather than causal effects .

5.6.4 External Validity

Our study is based on the AIDev dataset, which captures Agentic-PRs authored by five widely used autonomous coding agents on GitHub. The results may not generalize to proprietary development environments, non-GitHub platforms, or organizations with stricter security governance or different review cultures. In addition, both agent capabilities and reviewer practices are evolving rapidly; replication on future datasets will be necessary to assess the stability of the observed patterns over time.

5.6.5 Conclusion Validity

Threats to conclusion validity arise from statistical uncertainty and modeling choices. Large sample sizes may render small effects statistically significant; therefore, we emphasize effect direction, magnitude, and qualitative patterns alongside statistical tests. Our rejection-prediction models are exploratory and rely solely on early observable signals; their moderate performance underscores the complexity and context-dependence of reviewer decision-making in security-related PRs and cautions against overinterpretation.

6 Conclusion

In this paper, we presented the first large-scale empirical study of security-relevant Agentic pull requests in real-world GitHub repositories. By analyzing security-related PRs authored by five autonomous coding agents, we show that security-related work constitutes a meaningful but minority share of agent activity and is often expressed through supportive security hardening rather than narrowly scoped vulnerability fixes. We find that security-related Agentic-PRs are subject to heightened human scrutiny, exhibiting lower merge rates and substantially longer review latency than non-security PRs, with notable variation across agents, ecosystems, and code-change types. Our results further indicate that PR rejection is more strongly associated with complexity and verbosity than with explicit security topics. Together, these findings highlight that the effectiveness of AI teammates in security-critical workflows depends not only on technical capability, but also on alignment with human review practices and expectations in GenAI-enabled software systems.

7 Declarations

7.1 Funding

Not applicable.

7.2 Ethical Approval

Not applicable.

7.3 Informed Consent

Not applicable.

7.4 Author Contributions

M. L. Siddiq: Conceptualization, methodology design, data collection, data analysis, writing, and editing. X. Zhao: Data analysis, validation, writing—review and editing. V. C. Lopes: Data analysis, validation, writing—review and editing. B. Casey: Data analysis, validation, writing—review and editing. J. C. S. Santos: Supervision, project administration, data analysis, writing — review, and editing.

7.5 Data Availability

The replication package is available at [ ReplicationPackage ] .

7.6 Conflict of Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

7.7 Clinical Trial Number

Not applicable.
