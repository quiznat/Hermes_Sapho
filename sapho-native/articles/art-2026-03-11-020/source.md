---
version: source-capture.v1
article_id: art-2026-03-11-020
ticket_id: ticket-import-art-2026-03-11-020
source_url: https://arxiv.org/html/2511.00872v1
canonical_url: https://arxiv.org/abs/2511.00872
source_title: A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centric
  Software Engineering Tasks
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-11T13:18:35Z'
linked_paper_urls: []
---
# Source Capture

## Title

A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centric Software Engineering Tasks

## Body

A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centric Software Engineering Tasks

Zhuowen Yin yinzhuowen@stumail.neu.edu.cn 0009-0005-4063-2509 Institute of Al for Industries, Chinese Academy of Sciences 168 Tianquan Road Nanjing Jiangsu China 211135 Northeastern University 96 Jinzhai Road Shenyang Liaoning China 110819 , Cuifeng Gao gcf20225162@mail.ustc.edu.cn 0000-0003-0672-1485 University of Science and Technology of China 96 Jinzhai Road Hefei Anhui China 230026 , Chunsong Fan fanchunsong25@mails.ucas.ac.cn 0009-0009-4142-599X Institute of Al for Industries, Chinese Academy of Sciences 168 Tianquan Road Nanjing Jiangsu China 211135 , Wenzhang Yang wzhyang@iaii.ac.cn 0009-0006-7836-1246 Institute of Al for Industries, Chinese Academy of Sciences 168 Tianquan Road Nanjing Jiangsu China 211135 , Yinxing Xue yxxue@ustc.edu.cn 0000-0002-2979-7151 Institute of Al for Industries, Chinese Academy of Sciences 168 Tianquan Road Nanjing Jiangsu China 211135 and Lijun Zhang zhanglj@ios.ac.cn 0000-0002-3692-2088 Institute of Al for Industries, Chinese Academy of Sciences 168 Tianquan Road Nanjing Jiangsu China 211135

Abstract.

The rapid advancement of large language models (LLMs) has led to the emergence of intelligent agents capable of reasoning, acting, and observing in dynamic environments. Unlike traditional automation tools or static LLM-based systems, agents combine decision-making and tool utilization to autonomously accomplish complex tasks, showing great potential in software engineering. However, existing studies largely focus on specific tasks or isolated aspects, providing an incomplete picture of agents’ practical capabilities.

To address this, we conduct a comprehensive empirical study evaluating seven general-purpose agent frameworks across three representative code-centric tasks: software development, vulnerability detection, and program repair. Each task is assessed using standard, widely adopted benchmarks to ensure objective and comparable evaluation. Agent performance is systematically analyzed from three complementary perspectives: effectiveness (task success), efficiency (execution process), and overhead (token consumption).

Our findings reveal distinct capability patterns and trade-offs among the evaluated frameworks. In terms of effectiveness, agents achieve moderate overall performance, with OpenHands showing the most balanced results in software development, GPTswarm achieving the highest detection accuracy in vulnerability analysis, and only a subset of agents repairing about half of the issues in program repair. Regarding efficiency, AgentOrchestra tends to exhibit the longest trajectories and the most correction attempts due to coordination overhead, whereas OpenHands demonstrate stronger reflective reasoning abilities. For overhead, software development incurs the highest monetary cost, with OpenHands consuming the most tokens but benefiting from input caching, while GPTswarm remains the most cost-efficient. Furthermore, we conduct an in-depth cross-analysis of the relationship between effectiveness and efficiency, exploring the underlying reasons behind their interplay. These findings guide both practical adoption and future research toward more autonomous and efficient software engineering agents.

Agent Framework, Software Development, Vulnerability Detection, Program Repair

1. INTRODUCTION

With the rapid advancement of large language models (LLMs), their level of intelligence has grown remarkably, driving a new wave of innovation in intelligent agents. Agents are not simply more complex LLMs; rather, the ability to use tools—a defining feature that distinguishes humans from animals—also distinguishes agents from plain LLMs (goo, 2025 ) . By leveraging external tools, agents can not only execute actions but also make decisions and manage workflows, thereby enabling them to handle more intricate tasks. The Reason–Act–Observe paradigm has emerged as a cutting-edge technique toward achieving artificial general intelligence (AGI) (Gao et al., 2025a ) .

Recently, increasingly elaborate and sophisticated agent frameworks have demonstrated tremendous potential in the software engineering domain (Luo et al., 2025 ) . They are being adopted throughout the software development life cycle (Liu et al., 2024 ) , particularly in code-centric software engineering tasks such as software development (Qian et al., 2023b ) , vulnerability detection (Wei et al., 2025 ) , and program repair (Pabba et al., 2025 ) . Despite their widespread application, their practical capabilities in these tasks remain largely unclear to researchers and practitioners.

With the growing interest in agents, several empirical studies have begun to investigate the behavior and performance of agents from different perspectives. For instance, Gao et al. (Gao et al., 2025b ) compared the performance of multi-agent and single-agent systems across diverse domains beyond software engineering. In the context of automated program repair, Ceka et al. (Ceka et al., 2025 ) conducted an in-depth investigation into how agent decision-making workflows affect performance, while Meng et al. (Meng et al., 2025 ) performed fine-grained experiments to assess the effectiveness of agents.
However, despite these contributions, existing studies remain insufficient for a comprehensive evaluation of agent capabilities in software engineering due to two main limitations:
(1) they focus on specific tasks, predominantly automated program repair; and
(2) they emphasize isolated aspects, such as traceability or effectiveness, rather than providing a holistic assessment.

To address these limitations, we conduct a comprehensive empirical study to systematically evaluate the practical performance of state-of-the-art agent frameworks across diverse code-centric software engineering tasks. Specifically, to ensure fair and consistent comparisons across multiple tasks, we focus on general-purpose agent frameworks that are designed to be adaptable across domains, rather than task-specific systems optimized for a single purpose. In total, seven representative frameworks are selected as the evaluation subjects. In addition, given the absence of a unified benchmark applicable to all code-centric tasks, we adopt widely used, high-quality benchmarks for each individual task: SRDD (Qian et al., 2023a ) benchmark for software development task, LLM-SmartAudit benchmark (Wei et al., 2025 ) for vulnerability detection task, and SWE-bench Lite (swe, 2024a ) benchmark for program repair task.

To systematically evaluate agent capabilities, we note that their workflows differ fundamentally from both LLM-based and traditional code-based tools. Unlike pre-trained systems, agents make autonomous and dynamic decisions during task execution. Hence, it is essential to assess not only what they achieve (functional effectiveness) but also how they achieve it (process efficiency). Moreover, the complex reasoning and decision-making inherent in agent execution often result in substantially higher token consumption compared to single-pass LLMs. Thus, we further investigate the overhead of task completion, including how token expenditure is distributed across reasoning and execution steps. Evaluating both the outcomes and the processes provides a holistic understanding of an agent framework’s true level of intelligence. Consequently, our study is guided by three complementary research questions addressing the effectiveness , efficiency , and overhead of agent frameworks.

Our results reveal notable distinctions across the three evaluation dimensions:

Effectiveness (RQ1): Agents demonstrate moderate performance across all tasks. OpenHands achieves the most balanced quality in software development, while GPTswarm leads in vulnerability detection with a 77
% accuracy. In program repair, only a subset of agents successfully repair about half of the issues, leaving substantial room for improvement. We observe clear effectiveness trade-offs and underscore the ongoing challenges in fully automating complex, code-centric software engineering tasks.

Efficiency (RQ2): The execution efficiency varies across frameworks and tasks. SE-Agent (Iter-3) exhibits the longest steps across all experiments. AgentOrchestra exhibits the longest correction sequences, whereas OpenHands ranks second, demonstrating stable and convergent behavior.
Correction rates further reveal reflective adaptability. Specifically, both AgentOrchestra achieve high correction rates across tasks, while SE-Agent (Iter-1) attains the better result in software development, suggesting that lightweight orchestration with focused reasoning can rival more complex designs. Overall, efficiency depends less on agent quantity than on reasoning depth, coordination strategy, and feedback integration.

Overhead (RQ3): Software development is the most expensive task in terms of monetary cost, with AgentOrchestra being the most resource-intensive. Token consumption patterns vary significantly across frameworks. For instance, OpenHands uses the most tokens overall but benefits from caching, while GPTswarm uniquely produces more output than input tokens. Breakdown analyses further reveal that planning and reflection stages dominate multi-agent workflows, in contrast to single-agent systems that concentrate their costs on execution and editing stages.

Additionally, we explore the relationship between effectiveness and efficiency from the perspectives of multi-agent and single-agent frameworks, analyzing the underlying factors driving these dynamics. Overall, this study provides actionable insights for both researchers and practitioners. For framework developers, our findings highlight opportunities to optimize agent architecture design, reasoning coordination, and token usage efficiency. For end users, the results offer practical guidance in selecting agent frameworks that best balance performance, efficiency, and cost according to their specific application needs.

Contributions. Our contributions are summarized as follows:

- •

We provide the first comprehensive comparison of seven general-purpose agent frameworks across three representative code-centric software engineering tasks.

- •

We systematically assess these agent frameworks across each task from three holistic perspectives: effectiveness, efficiency, and overhead.

- •

We present new empirical findings to guide practical adoption and future research. All experimental results are publicly available in our GitHub repository 1 1 1 https://github.com/YCHYZW/Agents-for-Software-Engineering .

2. Background and Priliminaries

2.1. LLM-based Agents

The term “agent” is used with varying meanings across different communities (ant, 2025 ) . In some contexts, it refers to highly autonomous systems that operate over long time spans and employ multiple tools to solve complex tasks. In others, the same term may describe a more prescriptive workflow wrapped around an LLM, offering limited autonomy and decision-making capability. Such inconsistent usage often blurs the line between general LLM automation and true agent architectures (Luo et al., 2025 ) , making it difficult to evaluate and compare existing work.

Definition. To clearly establish the scope of this study, we adopt the definition of LLM-based agents from Google’s recent Agent White Paper (goo, 2025 ) .

“This combination of reasoning, logic, and access to external information that are all connected to a generative AI model invokes the concept of an agent.”

According to the white paper, an agent is viewed as a system driven by a cognitive architecture that governs its behavior, interaction, and decision-making. This architecture consists of three essential components:
(1) Model , which serves as the central decision-making engine, typically implemented using one or multiple instruction-following language models;
(2) Tools , which empower the agent to interact with external data and services beyond pure text generation; and
(3) Orchestration , which manages the iterative perception–reasoning–action loop, including planning, tool invocation, action execution, and reflection until the task goal is reached.
In this work, we therefore focus on agent frameworks that embody these components.

Categories. Based on the scale of collaboration, agent systems can be divided into single-agent and multi-agent paradigms (Gao et al., 2025b ) . Single-agent systems employ a centralized architecture in which one agent independently performs perception, reasoning, and decision-making. Their simplicity and low communication overhead make them suitable for applications such as personal assistants and basic chatbots. However, a single agent can easily become a bottleneck under high concurrency, and its generalization capability is fundamentally constrained by the capacity of the underlying LLM.
In contrast, multi-agent systems distribute work across multiple agents, each specializing in specific tasks to improve performance through division of labor, parallel execution, and dynamic coordination. Expanding the number of agents can further enhance system adaptability. Depending on interaction dynamics, multi-agent systems can be cooperative, competitive, or hybrid. Nevertheless, they introduce considerable coordination complexity and high resource consumption. In this paper, we investigate both single-agent and multi-agent systems to ensure a comprehensive and unbiased analysis of LLM-based agent frameworks.

2.2. Code-centric Software Engineering Tasks

The software engineering life-cycle typically comprises several sequential and iterative phases, including requirements analysis, design, implementation or development, testing and verification, deployment, and maintenance or evolution.
Each phase involves distinct objectives and artifacts, ranging from specifying system requirements and designing architecture to implementing, verifying, and maintaining the software.
In this study, we focus on the code-centric phases of the life-cycle, particularly those that involve direct manipulation of source code, such as code development , vulnerability detection , and program repair .
These tasks serve as representative scenarios for evaluating the capability and adaptability of agent frameworks in software engineering contexts.

Software Development Software development is the systematic application of engineering principles, methods, and tools to the production and evolution of software (Basili, 1989 ) .
Its primary goal is to transform stakeholder requirements into operational, high-quality software. The process is conventionally structured by a software development life cycle that consists of interdependent phases including requirements elicitation and analysis, architectural design, implementation, verification and validation and deployment (Aggarwal, 2005 ) .
With the advent of generative AI, large language models have shown considerable potential to transform development workflows (JACKSON et al., 2025 ) . Agents aim to extend these capabilities further by supporting end-to-end coverage of the development life cycle. A high-quality solution generated by an agent should satisfy the stated requirements, incur low execution or generation cost, require minimal manual refinement and scale seamlessly to larger codebases (Luo et al., 2025 ) .

Vulnerability Detection. Vulnerability detection is a critical discipline within software security, focused on the systematic identification of security‑critical flaws in software systems (Bessey et al., 2010 ) . Its primary objective is to proactively uncover and remediate weaknesses before they can be exploited by malicious actors, thereby safeguarding the confidentiality, integrity, and availability of the system. Recent advances in artificial intelligence have significantly accelerated research in this area (Chakraborty et al., 2021 ) . Agent-based approaches further enhance detection by combining multi-agent co-inspection, integration of additional knowledge from tool executions, and traditional static analysis techniques (Luo et al., 2025 ) , aiming to improve accuracy, diversify the types of detected vulnerabilities, and enhance overall performance.

Program Repair Program Repair, often referred to as Automated Program Repair (APR), is a subfield of Software Engineering that aims to automatically correct software faults (Le Goues et al., 2019 ) . Its primary objective is to mitigate the substantial manual effort, time, and cost associated with the debugging and maintenance phases. The typical APR pipeline involves fault localization, patch synthesis, and patch validation (Liu et al., 2019 ) . Learning-based APR treats program repair either as a translation task, in which buggy code is converted to correct code, or as a generation task, where the correct code is infilled within the buggy code context (Zhang et al., 2023 ) . LLM-based agents generally follow an iterative paradigm, refining patches based on model or tool feedback until correctness is achieved, effectively balancing scope and accuracy (Luo et al., 2025 ) .

3. Methodology

3.1. Research Questions 
Figure 1 . Agentic workflow paradigm.

To derive our research questions, we first abstract a generalized agentic workflow paradigm that characterizes how agent frameworks operate in code-centric software engineering tasks, as illustrated in Figure 1 . This paradigm adopts the cognitive architecture proposed in Google’s Agent White Paper (goo, 2025 ) , encompassing the model, tool, and orchestration components introduced in § 2.1 .
The agentic workflow comprises three conceptual layers that interact synergistically to enable adaptive, goal-driven task execution, as follows:

Orchestration and Reasoning. This layer governs high-level decision-making and adaptive reasoning processes. It is responsible for dynamic task planning, self-reflection, and continuous evolution of strategies based on intermediate feedback. It typically incorporates memory mechanisms to retain contextual knowledge across iterations, enabling long-term consistency and informed reasoning. Reflection modules allow agents to analyze prior failures or inefficiencies, while evolution components iteratively refine prompts, goals, or workflows to enhance overall performance.

Collaborative Role This layer defines specialized agent roles and their interactions within a cooperative framework. Common configurations include a planner that decomposes complex tasks into executable subtasks, workers that perform targeted actions or reasoning steps, and evaluators that assess the quality or correctness of intermediate outputs. This division of labor enables structured coordination and feedback loops among agents, thereby improving robustness and accountability in multi-agent collaboration.

Tool Augmentation This layer extends the agent’s capabilities through external tools. These tools include browsers for retrieving up-to-date information from the web, command-line interfaces (CLI) for system-level operations, and code executors for testing or debugging generated code. Such augmentations bridge the gap between purely language-based reasoning and real-world execution, supporting more practical and context-aware problem solving.

These layers form an integrated ecosystem with rich interdependencies. The most distinctive feature of agent execution is its dynamic, adaptive intelligence, which differentiates agents from other approaches such as traditional code-based tools (e.g., static and dynamic analysis techniques) with fixed programs and static rules, or LLM-based tools that rely on manually engineered mechanisms (e.g., diversity chain-of-thought paradigms, fine-tuning, or retrieval-augmented generation), where processes and models are largely fixed.

Consequently, a comprehensive and systematic evaluation of agent frameworks requires assessing three complementary aspects: the quality of their function , the characteristics of their processes underlying task execution, and the overhead associated with their token consumption.
In terms of function , we assess whether agents can effectively complete target tasks, focusing on final outcomes, as in traditional automation tools.
In terms of process , it is equally important to examine how agents achieve these goals, with particular emphasis on the efficiency and dynamics of their execution. This procedural aspect serves as a key indicator of the core intelligence level of the frameworks.
In terms of overhead , it is not sufficient to measure only the total resources expended to complete a task; we must also analyze how resources are consumed across different stages of the reasoning process. Such a detailed examination provides deeper insights into the operational characteristics of agents and the significance of their execution strategies.

Based on this analysis, we formulate the following research questions:

- •

RQ1 [Effectiveness]: How effectively do agent frameworks complete code-centric software engineering tasks?

- •

RQ2 [Efficiency]: How efficiently do agent frameworks utilize reasoning cycles and external tools to complete code-centric software engineering tasks?

- •

RQ3 [Overhead]: What is the token cost incurred by agent frameworks in completing code-centric software engineering tasks?

3.2. Studied Agent Frameworks 
Table 1. Comparison of architectural components across the studied agent frameworks.

Agents Year URL Multi Agent Planner Context Builder Worker Evolution Tool Selection Test-Time Scaling

AgentOrchestra ( Zhang et al. , 2025 ) 2025 https://github.com/SkyworkAI/DeepResearchAgent ✔ ✔ ✔ ✔ ✘ ✔ ✘

OWL ( Hu et al. , 2025 ) 2025 https://github.com/camel-ai/owl ✔ ✔ ✔ ✔ ✘ ✘ ✔

SE-Agent ( Lin et al. , 2025 ) 2025 https://github.com/JARVIS-Xs/SE-Agent ✘ ✘ ✔ ✔ ✔ ✘ ✔

Trae ( Team et al. , 2025 ) 2025 https://github.com/bytedance/trae-agent ✘ ✘ ✘ ✔ ✔ ✔ ✔

GPTswarm ( Zhuge et al. , [n. d.] ) 2024 https://github.com/metauto-ai/GPTSwarm ✘ ✘ ✔ ✔ ✘ ✘ ✘

OpenHands ( Wang et al. , 2025 ) 2024 https://github.com/All-Hands-AI/OpenHands ✘ ✘ ✔ ✔ ✘ ✔ ✔

SWE-Agent ( Yang et al. , 2024 ) 2024 https://github.com/SWE-agent/SWE-agent ✘ ✘ ✔ ✔ ✘ ✔ ✘

To comprehensively collect state-of-the-art agent frameworks that support code-centric software engineering tasks, we began with the survey by Liu et al. (Liu et al., 2024 ) , which provides an a comprehensive collection of research papers on LLM-based agents for software engineering. Note that this survey also includes LLM-based works that fall outside the scope of agents as defined in § 2.1 . We thus carefully identified the relevant agent frameworks that meet our target criteria.

We then expanded this collection by searching both academic literature and industrial implementations available on the Internet.
In line with the research goals of this study, which span diverse code-centric tasks, we prioritized general-purpose agent frameworks over ad hoc, task-specific systems, thereby enabling consistent and fair comparisons.
Therefore, only frameworks that satisfied the following inclusion criteria were considered in our study:

- C1

The agent framework can be applied to all three tasks, namely software development, vulnerability detection, and program repair.
This criterion excludes task-specific agents that are tailored to a single scenario, such as those exclusively designed for vulnerability repair or code generation.

- C2

The agent framework is publicly available.
This criterion excludes proprietary or closed-source frameworks that are not accessible for independent evaluation.

In total, as shown in Table 1 , we identified 7 that satisfy the inclusion criteria and summarizes the architectural components adopted by these frameworks.

AgentOrchestra (Zhang et al., 2025 ) created by researchers at Skywork AI and Nanyang Technological University. It is a multi-agent framework that supports unified multimodal tool integration, flexible component composition, and efficient hierarchical collaboration. Through dynamic tool creation, intelligent retrieval, and automatic reuse.

OWL (Hu et al., 2025 ) developed by researchers from The University of Hong Kong and the CAMEL team, OWL is a hierarchical multi-agent framework. A Planner Agent decomposes tasks, a Coordinator Agent manages subtasks, and Worker Agents invoke domain-specific tools to execute work. Adding or modifying Worker Agents improves overall generalization during inference. Furthermore, OWL employs reinforcement learning with real-world feedback to optimize a domain-agnostic Planner Agent, thereby enhancing cross-domain generalization.

SE-Agent (Lin et al., 2025 ) jointly developed by Tsinghua University and StepFun team. It is a self-evolving, multi-step reasoning agent. SE-Agent first constructs an initial trajectory pool by injecting five distinct reasoning strategies and controlled trajectory mutations. The agent then performs reflection and revision to identify issues, followed by cross-trajectory fusion via Crossover, Transfer, and Restructuring. Finally, it conducts multi-dimensional trajectory selection to produce robust solutions.

Trae (Team et al., 2025 ) built by engineers at ByteDance for code engineering. It orchestrates a Code Agent that integrates multiple tools to iteratively generate candidate patches across prescribed steps. It then applies a two-stage pruning process—patch deduplication and regression testing—to reduce the search complexity for the optimal patch. To select candidates, a Selector Agent with repository-level understanding ranks solutions, and a voting mechanism determines the final patch.

GPTswarm (Zhuge et al., [n. d.] ) proposed by researchers from KAUST and the Swiss AI Lab IDSIA. It models agents as computation graphs: nodes are functions that process multimodal data or query LLMs, edges represent interaction flows, and graphs can be recursively composed into larger hierarchies to capture inter-agent collaboration structures. GPTswarm introduces novel graph-level optimization operators: it refines node-level LLM prompts and adjusts graph connectivity to improve agent orchestration.

OpenHands (Wang et al., 2025 ) is an open-source platform co-developed by academic and industry contributors to provide a unified, powerful, and safe environment for building and evaluating general-purpose “AI software developer” agents. 1) It centers on an event-stream interaction mechanism that precisely logs each agent action and environment observation, forming complete task trajectories. 2) It bundles a ready-to-use Python tool library that encapsulates common but complex operations—file editing, multimodal parsing (e.g., PDFs, images), and code search—into simple function calls. 3) It pioneered a multi-agent delegation mechanism that allows a generalist agent (e.g., CodeAct Agent) to outsource specialized subtasks to expert agents (e.g., a Browsing Agent), enabling capability complementarity for complex composite tasks. As a result, OpenHands supports diverse real-world scenarios, such as automated software development and maintenance, intelligent data analysis, efficient research assistance, and personal automation workflows.

SWE-Agent (Yang et al., 2024 ) developed by researchers at Princeton University. It is a single-agent framework tailored to software engineering. SWE-Agent augments an agent’s ability to create and modify files, navigate codebases, and run tests via an agent–computer interface (ACI). Its design mirrors human use of IDEs: (1) manual inspection of agent behaviors to identify failure modes and suggest improvements; and (2) grid search to select optimal ACI configurations. Together, these mechanisms strengthen the agent’s capacity to tackle complex software engineering tasks.

3.3. Benchmark Suite 
Table 2. The benchmark suite for code-centric software engineering tasks.

Task Benchmark Dataset Year URL Instances

Software Development SRDD ( Qian et al. , 2023a ) 2023 https://github.com/OpenBMB/ChatDev/tree/main/SRDD 1,200

Vulnerability Detection LLM-SmartAudit ( Wei et al. , 2025 ) 2025 https://github.com/LLMAudit/LLMSmartAuditTool 115

Program Repair SWEBench-Lite ( swe , 2024a ) 2024 https://www.swebench.com/lite.html 300

To ensure a rigorous and unbiased evaluation of the studied agent frameworks, we carefully curate a benchmark suite from publicly available software engineering benchmarks. Although agents are built on LLMs, LLM evaluation datasets and agent evaluation datasets differ fundamentally in their objectives, task granularity, and required interactions: the former measure intrinsic text understanding and generation abilities of LLMs, while the latter assess end-to-end task execution and autonomy in real workflows. Accordingly, agent evaluation typically incurs substantially higher costs than LLM evaluation. Therefore, we primarily consider the benchmarks used in prior software-engineering agent research, as catalogued in the survey by Liu et al. (Liu et al., 2024 ) . The selection was guided by the principles of broad community adoption, comprehensive task coverage, appropriate dataset scale, data reliability, and reproducibility to support consistent assessment and verification.

As summarized in Table 2 , the final benchmark suite includes three benchmarks that span software development, vulnerability detection, and program repair tasks. In the following, we present the details of each benchmark and discuss the rationale behind its selection.

SRDD (Qian et al., 2023a ) for Software Development. To evaluate existing LLM-based agents for end-to-end software development, as reported by Liu et al. (Liu et al., 2024 ) , many existing studies adopt classic code generation benchmarks such as HumanEval (Chen et al., 2021a ) and MBPP (Austin et al., 2021 ) . However, these benchmarks mainly involve simplified programming tasks on isolated pieces of code, which do not accurately represent practical development environments. To address this limitation, more advanced benchmarks have emerged, including SRDD (Qian et al., 2023a ) and ProjectDev (Nguyen et al., 2025 ) , which support development tasks across multiple files and demonstrate increasing popularity in recent works.

Among these benchmarks, Software requirement description dataset (SRDD) has become the most frequently adopted one, since it contains the largest and most diverse collection of software development tasks with 1,200 curated prompts. Therefore, in this study, we select SRDD to evaluate agents on software development tasks. SRDD consists of 1,200 natural language prompts, organized into five major categories and 40 subcategories. The prompts were collected from ChatGPT 3.5 and thoroughly curated to ensure high task quality and relevance to realistic development scenarios.

LLM-SmartAudit (Wei et al., 2025 ) for Vulnerbaility Detection. Although many benchmarks have been used to evaluate LLM-based approaches for static bug detection, as reported by Liu et al. (Liu et al., 2024 ) , none are specifically curated for evaluating agent frameworks. In our investigation of recent works, LLM-SmartAudit is the only one we identified that applies agents for vulnerability detection tasks. Therefore, we select the dataset used by LLM-SmartAudit in this study to enable a fair and standardized comparison of different agent-based approaches under consistent evaluation conditions.

LLM-SmartAudit consists of three subset datasets: a common-vulnerability set, a real-world set, and a CVE set. Among them, only the common-vulnerability set and the CVE set provide standardized vulnerability type labels. In contrast, the real-world set is categorized based on their nature rather than their exact labels. Therefore, our evaluation focuses on the two well-labeled subsets, comprising 102 contracts from the common-vulnerability set and 13 contracts from the CVE set. In total, we analyze 115 vulnerability instances across these datasets.

SWEBench-Lite (swe, 2024a ) for Program Repair. For the task of program repair, many LLM-based approaches (Liu et al., 2024 ) have been evaluated on classical benchmarks such as Defects4J (Just et al., 2014 ) and QuixBugs (Lin et al., 2017 ) , which mainly target small-scale defects. In contrast, most agent-based works (Pabba et al., 2025 ; Mu et al., 2025 ; Yu et al., 2025 ) are consistently evaluated on the derivatives of the SWE-bench benchmark (Jimenez et al., 2023 ) (e.g., SWE-bench Lite (swe, 2024a ) , SWE-bench Lite-S (Xia et al., 2024a ) , etc.), because it is grounded in real-world development scenarios by constructing tasks directly from GitHub issues and corresponding codebases, thereby ensuring practical relevance to authentic software maintenance workflows.

SWE-bench (Jimenez et al., 2023 ) is a comprehensive benchmark, comprising over 2,000 real-world GitHub issues drawn from 12 widely-used Python repositories. Each task includes the original issue description, the full code repository, a predefined execution environment, and associated validation tests. However, evaluating the full SWE-bench benchmark incurs substantial computational costs and includes particularly challenging or problematic tasks (Xia et al., 2024b ) , which may lead to underestimation of the practical capability of LLM-based agents.

To address these limitations, researchers have manually curated high-quality tasks that balance difficulty, provide self-contained information, include informative issue descriptions, and offer sufficient evaluation tests, which constitutes SWE-bench Lite (swe, 2024a ) . Accordingly, we adopt SWE-bench Lite in this study to evaluate LLM-based agents on program repair tasks. This dataset comprises 300 carefully selected repair instances, covering all of the original 12 repositories while preserving the diversity and difficulty distribution of the full benchmark.

3.4. Evaluation Framework

To ensure a fair and systematic evaluation across different agent frameworks, we design a unified evaluation framework that adopt tailored assessment metrics for each research question and standardizes the experimental setup for all agents.

Table 3. Evaluation metrics for each research question.

Research Question Task Metrics

Effectiveness (RQ1) Software Development Q ​ u ​ a ​ l ​ i ​ t ​ y = C ​ o ​ m ​ p ​ l ​ e ​ t ​ e ​ n ​ e ​ s ​ s × E ​ x ​ e ​ c ​ u ​ t ​ a ​ b ​ i ​ l ​ i ​ t ​ y × C ​ o ​ n ​ s ​ i ​ s ​ t ​ e ​ n ​ c ​ y Quality=Completeness\times Executability\times Consistency

Vulnerability Detection A ​ c ​ c ​ u ​ r ​ a ​ c ​ y = T ​ P ​ s / ( T ​ P ​ s + F ​ P ​ s ) Accuracy=TPs/(TPs+FPs)

Program Repair R ​ e ​ p ​ a ​ i ​ r ​ _ ​ R ​ a ​ t ​ e = ( C ​ o ​ r ​ r ​ e ​ c ​ t ​ l ​ y ​ _ ​ F ​ i ​ x ​ e ​ d ​ _ ​ I ​ s ​ s ​ u ​ e ​ s ) / ( T ​ o ​ t ​ a ​ l ​ _ ​ I ​ s ​ s ​ u ​ e ​ s ) Repair\_Rate=(Correctly\_Fixed\_Issues)/(Total\_Issues)

Efficiency (RQ2) All Tasks Average Trajectory Steps, Correction Attempts, and Correction Rate

Overhead (RQ3) All tasks Monetary Cost, Token Usage

Evaluation Metrics As shown in Table 3 , we present the evaluation metrics corresponding to each research question.
Effectiveness (RQ1) is measured using task-specific metrics aligned with the respective benchmarks. Specifically:
(1) On the SRDD benchmark, the evaluation script provided by ChatDev (Qian et al., 2023b ) leverages OpenAI’s text-embedding-ada-002 model to extract features from the project’s Python files, task descriptions, and requirement documents. This evaluation assesses the completeness, executability, and consistency of the generated code, which are combined into a final quality index.
(2) For the LLM-SmartAudit benchmark, agents generate vulnerability analysis reports that indicate the presence or absence of vulnerabilities and provide detailed classifications when applicable. These reports are compared against ground truth annotations to compute true positive (TP) and false positive (FP) rates.
(3) On the SWEBench-lite benchmark, we follow the official Docker-based evaluation protocol. The diff-format patch files generated by the seven agent frameworks are aggregated and standardized into a unified JSON format. Evaluation is performed via a command line interface (CLI), with repair rate as the primary metric.

Efficiency (RQ2) is assessed by analyzing the agents’ execution processes. Specifically, we measure average trajectory steps, correction attempts, and correction rate. These metrics quantify how efficiently each agent framework completes the assigned tasks, capturing the dynamic decision-making behaviors intrinsic to intelligent agents.
Overhead (RQ3) measures the monetary cost incurred during task completion. We also record token consumption—including both input and output tokens—and analyze how these tokens are distributed across different stages of the agent workflow. This detailed breakdown offers insights into the cost-efficiency trade-offs among the evaluated frameworks.

Experimental Setup. For the seven general-purpose agent frameworks, our experimental setup is primarily characterized by several key parameters, including, Step Limit , Agent Quantity , Tool Set , Prompt , Iteration and Backend LLM . The detailed configurations for each parameter are described as follows:

- •

Step Limit. For all tasks and agent frameworks, the maximum step limit was set to 100 to ensure consistent termination conditions and to keep the monetary overhead within a controllable range.

- •

Agent Quantity. We adhere to the default configurations specified by each agent framework for executing code-related tasks. Notably, in AgentOrchestra ’s setup, all four agents are utilized for the software development task, whereas the BrowserUse agent is excluded from vulnerability detection and program repair tasks. This exclusion is due to the code-centric nature of these tasks, which rely primarily on direct source code interaction and static analysis within the repository, rendering browser capabilities unnecessary.

- •

Tool Set For all tasks and agents, the default tool sets provided by each framework were used without modification, ensuring an objective and faithful evaluation of their out-of-the-box capabilities.

- •

Prompt. The prompts are carefully aligned with the specific tasks and datasets to ensure relevance and consistency. To maintain comparability across frameworks, we employed prompt configurations previously validated on each respective benchmark. Specifically, for the software development task, we utilized prompts from ChatDev (Qian et al., 2023b ) ; for vulnerability detection, we adopted prompts from LLM-SmartAudit (Wei et al., 2025 ) ; and for the program repair task, we adapted prompts from SWE-Agent (Yang et al., 2024 ) with minor modifications to support all seven agent frameworks under evaluation.

- •

Iteration. Following SE-Agent ’s official example, three iterations are used with summary operators null , alternative_strategy which generates distinct alternatives from recent failures, and traj_pool_summary which analyzes trajectory pool failures to identify blind spots and risks. We evaluate the performance across these three iterations and present the corresponding results in RQ1, RQ2, and RQ3 for comprehensive comparison.

- •

Backend LLM. To ensure consistency and control costs, all agents utilize the DeepSeek-v3.1 (DeepSeek-AI, 2024 ) as their backend LLM, capitalizing on DeepSeek’s renowned innovation in training highly efficient models at low cost, thus offering an excellent price-performance ratio.

4. Results and Analaysis

In this section, we provide a comprehensive analysis of the empirical findings, focusing on the effectiveness (RQ1), efficiency (RQ2), and overhead (RQ3) of the seven general-purpose agent frameworks evaluated in this study.

4.1. Effectiveness of Agent Frameworks (RQ1)

To address RQ1, we leverage the benchmark suite introduced in § 3.3 , which covers three representative code-centric software engineering tasks: software development (SRDD), vulnerability detection (LLM-SmartAudit), and program repair (SWE-bench Lite). Across these tasks, we evaluate seven state-of-the-art agent frameworks, as presented in § 3.2 .

Table 4. Comparison of software development effectiveness across different task classes and metrics on the SRDD benchmark.

Agent Game Education Work Life Creation Average Quality

Comp. Exec. Cons. Comp. Exec. Cons. Comp. Exec. Cons. Comp. Exec. Cons. Comp. Exec. Cons. Comp. Exec. Cons.

AgentOrchestra 0.82 0.50 0.78 0.90 0.58 0.77 0.83 0.56 0.78 0.91 0.58 0.78 0.81 0.49 0.77 0.86 0.55 0.78 0.36

OWL 0.69 0.78 0.79 0.61 0.72 0.78 0.60 0.71 0.79 0.73 0.76 0.78 0.65 0.38 0.78 0.66 0.70 0.78 0.36

SE-Agent (Iter-1) 0.72 0.91 0.71 0.77 0.91 0.71 0.67 0.93 0.71 0.74 0.96 0.72 0.64 0.65 0.71 0.71 0.90 0.71 0.46

SE-Agent (Iter-2) 0.71 0.43 0.78 0.78 0.34 0.78 0.73 0.29 0.78 0.76 0.35 0.78 0.81 0.46 0.79 0.75 0.37 0.78 0.22

SE-Agent (Iter-3) 0.73 0.23 0.79 0.79 0.25 0.79 0.71 0.18 0.79 0.80 0.29 0.79 0.76 0.34 0.79 0.76 0.26 0.79 0.15

Trae 0.48 0.96 0.81 0.50 0.94 0.81 0.51 0.91 0.81 0.64 0.93 0.81 0.43 0.90 0.81 0.53 0.93 0.81 0.40

GPTswarm 0.76 0.64 0.85 0.69 0.81 0.85 0.71 0.77 0.85 0.80 0.58 0.85 0.77 0.81 0.86 0.75 0.70 0.85 0.45

OpenHands 0.62 1.00 0.80 0.59 1.00 0.79 0.49 1.00 0.78 0.68 1.00 0.80 0.59 1.00 0.79 0.60 1.00 0.79 0.47

SWE-Agent 0.53 0.84 0.78 0.64 0.84 0.77 0.58 0.90 0.78 0.61 0.94 0.80 0.47 0.85 0.79 0.57 0.87 0.78 0.39

Average 0.70 0.68 0.80 0.70 0.71 0.79 0.66 0.68 0.79 0.76 0.67 0.80 0.69 0.65 0.80 0.69 0.70 0.79 0.36

Software Development. The results of our study on automated software development tasks are summarized in Table 4 , which presents a comparative evaluation of seven distinct agent frameworks. The evaluation was conducted using the SRDD dataset, a comprehensive collection of 1,200 instances distributed across five categories: Education (210), Work (240), Life (330), Game (270), and Creation (150).

Our methodology for this assessment was as follows: (1) We benchmarked the seven agent frameworks against the 1,200 simulated software development problems from the SRDD dataset. (2) The generated software projects—comprising Python files, metadata text files, and requirements text files—were quantitatively evaluated for Completeness, Executability, and Consistency using the official evaluation script provided by ChatDev (Qian et al., 2023b ) . (3) A category-by-category analysis was performed to identify the specific software development tasks in which each agent excels.

As illustrated in Table 4 , the quality of the software produced by the agents exhibits significant disparities across the three metrics. A key finding is that no single agent framework is omnipotent; each demonstrates a unique profile of strengths and weaknesses. This provides empirical evidence of the current limitations of agent frameworks in code generation, thereby informing future work aimed at their improvement.

A detailed analysis of the metrics reveals the following. For completeness, AgentOrchestra demonstrated the highest effectiveness, achieving an impressive average score of 0.86 across the five categories, significantly outperforming the collective average of 0.69. In contrast, Trae registered the poorest effectiveness in completeness, with an average of 0.53. In terms of executability, the OpenHands framework proved exceptionally proficient, attaining perfect scores (1.00) in the Game, Education, Life, and Creation categories, and a near-perfect score of 1.00 in the Work category. This outstanding result stands in stark contrast to the overall average executability of 0.79 across all agents.For consistency, GPTswarm emerged as the leader, with a superior average score of 0.85, surpassing the overall agent average of 0.79.Across these five categories, AgentOrchestra demonstrated superior performance in completeness, while OpenHands excelled in executability, and GPTswarm maintained a leading position in consistency.

To assess overall effectiveness, we utilized the quality score metric proposed by ChatDev , calculated as Q ​ u ​ a ​ l ​ i ​ t ​ y = C ​ o ​ m ​ p ​ l ​ e ​ t ​ e ​ n ​ e ​ s ​ s × E ​ x ​ e ​ c ​ u ​ t ​ a ​ b ​ i ​ l ​ i ​ t ​ y × C ​ o ​ n ​ s ​ i ​ s ​ t ​ e ​ n ​ c ​ y Quality=Completeness\times Executability\times Consistency . Based on this composite metric, OpenHands is the top-performing framework for software development tasks, achieving a quality score of 0.47.

Despite the strong effectiveness of OpenHands , our findings suggest that its capabilities are not yet sufficient to serve as a universal replacement for all other agents. Each framework possesses distinct advantages, indicating that the landscape of agent-driven software development benefits from a diversity of specialized tools rather than a single, all-encompassing solution.

Table 5. Comparison of vulnerability detection effectiveness across different vulnerability types on the LLM-SmartAudit benchmark.

Subset Dataset Vulnerability Type (#Contracts) AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent

Common- Vulnerability IO (10) 0 (0%) 1 (10%) 7 (70%) 6 (60%) 9 (90%) 2 (20%) 9 (90%) 8 (80%) 7 (70%)

RP (10) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 9 (90%)

GL (11) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 1 (9%) 1 (9%) 2 (18%) 1 (9%) 0 (0%)

RE (10) 7 (70%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%)

TM (10) 1 (10%) 3 (30%) 4 (40%) 5 (50%) 4 (40%) 4 (40%) 6 (60%) 1 (10%) 6 (60%)

TOD (10) 3 (30%) 9 (90%) 9 (90%) 7 (70%) 8 (80%) 9 (90%) 8 (80%) 4 (40%) 8 (80%)

USE (10) 0 (0%) 2 (20%) 8 (80%) 8 (80%) 8 (80%) 2 (20%) 9 (90%) 3 (30%) 9 (90%)

TX (10) 7 (70%) 7 (70%) 7 (70%) 7 (70%) 7 (70%) 6 (60%) 7 (70%) 6 (60%) 8 (80%)

UD (10) 9 (90%) 8 (80%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 10 (100%) 9 (90%)

USU (11) 11 (100%) 10 (91%) 11 (100%) 10 (91%) 10 (91%) 10 (91%) 10 (91%) 6 (55%) 11 (100%)

CVE Access Control (4) 0 (0%) 1 (25%) 2 (50%) 3 (75%) 2 (50%) 2 (50%) 4 (100%) 4 (100%) 4 (100%)

Overflow (3) 1 (33%) 3 (100%) 3 (100%) 3 (100%) 3 (100%) 3 (100%) 3 (100%) 3 (100%) 3 (100%)

Logic Error (4) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 1 (25%) 1 (25%)

Delegatecall (1) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%)

Bad Randomness (1) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 1 (100%) 0 (0%) 1 (100%)

Total (115) 51 (44%) 66 (57%) 83 (72%) 81 (70%) 84 (73%) 71 (62%) 80 (78%) 68 (59%) 87 (76%)

Vulnerability Detection. Table 5 shows the experimental results of seven agent frameworks on vulnerability detection task.
The common-vulnerability subset dataset contains 10 types of vulnerabilities, specifically Reentrancy (RE), Integer Overflow/Underflow (IO), Unchecked send (USE), Unsafe Delegatecall (UD), Transaction Order Dependence (TOD), Time Manipulation (TM), Randomness Prediction (RP), Authorization Issue using ‘tx.origin’ (TX), Unsafe Suicide (USU), and Gas Limitation (GL). The CVE subset dataset contains 5 types of vulnerabilities, including Access Control, Overflow, Logic Error, Delegatecall, and Bad Randomness.

We adopt the following methods to answer this question: (1) We evaluate seven agent frameworks in our assessment on the 115 vulnerable smart contracts across different vulnerability types. (2) When the vulnerability detection report generated by the agent framework is compared with the ground truth of the labeled dataset, the detection accuracy rate for each vulnerability type can be calculated. (3) Through type-by-type analysis, we can observe which vulnerability detection tasks these agents perform well in.

For the research results of vulnerability detection presented in Table 5 , which shows the vulnerability detection effectiveness of seven agent frameworks across 5 types of CVE dataset and 10 types of labeled dataset. When the agent framework generates a vulnerability detection report, it details whether vulnerabilities exist and the types of vulnerabilities present. Each row in Table 5 represents a vulnerability detection type, and each cell represents the number of vulnerabilities detected by the agent framework for this vulnerability type, along with the percentage relative to the total number of vulnerabilities.

Table 5 shows that the accuracy rates of smart contract vulnerability detection across various agents are slightly similar. In fact, for the GL vulnerability type, all seven agents demonstrated very low detection efficiency, basically failing to discover any vulnerabilities. However, for vulnerability types such as PR and UD, the results are very significant, approaching a detection accuracy rate of 100%.
We observe that the seven agents demonstrate comparable performance in the vulnerability detection task, with GPTswarm achieving the highest score of 77%, AgentOrchestra recording the lowest at 44%, and SE-Agent in Iter-2 representing the median at 70%. However, they have not broken through 90%, which indicates that the seven agent frameworks we evaluated still have room for improvement.

Table 6. Comparison of program repair effectiveness across different repositories on the SWE-bench Lite benchmark.

Repository (#Issues) AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent

astropy (6) 0 (0%) 1 (17%) 2 (33%) 3 (50%) 2 (33%) 3 (50%) 0 (0%) 3 (50%) 2 (33%)

django (114) 7 (6%) 7 (6%) 59 (52%) 67 (59%) 68 (60%) 68 (60%) 14 (12%) 61 (54%) 66 (58%)

flask (3) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%) 0 (0%)

matplotlib (23) 0 (0%) 2 (9%) 9 (39%) 14 (61%) 14 (61%) 11 (48%) 0 (0%) 11 (48%) 14 (61%)

seaborn (4) 0 (0%) 1 (25%) 3 (75%) 4 (100%) 3 (75%) 3 (75%) 0 (0%) 3 (75%) 4 (100%)

pylint (6) 0 (0%) 0 (0%) 2 (33%) 3 (50%) 2 (33%) 3 (50%) 0 (0%) 2 (33%) 3 (50%)

pytest (17) 0 (0%) 1 (6%) 6 (35%) 6 (35%) 6 (35%) 6 (35%) 0 (0%) 8 (47%) 5 (29%)

requests (6) 1 (17%) 2 (33%) 1 (17%) 1 (17%) 3 (50%) 3 (50%) 0 (0%) 0 (0%) 4 (67%)

scikit (23) 0 (0%) 1 (4%) 17 (74%) 16 (70%) 15 (65%) 14 (61%) 1 (4%) 16 (70%) 16 (70%)

sphinx (16) 1 (6%) 1 (6%) 7 (44%) 9 (56%) 9 (56%) 8 (50%) 0 (0%) 3 (19%) 9 (56%)

sympy (77) 0 (0%) 15 (19%) 34 (44%) 34 (44%) 37 (48%) 33 (43%) 0 (0%) 37 (48%) 34 (44%)

xarray (5) 0 (0%) 0 (0%) 2 (40%) 2 (40%) 2 (40%) 2 (40%) 0 (0%) 2 (40%) 2 (40%)

Total (300) 10 (3%) 31 (10%) 142 (47%) 159 (53%) 161 (54%) 154 (51%) 15 (5%) 146 (49%) 159 (53%)

Program Repair. The SWEBench-Lite benchmark comprises 12 GitHub repositories with a total of 300 instances. Our methodology for the program repair task was as follows: (1) we evaluated the seven agent frameworks on the 300 real-world issues spanning the 12 repositories; (2) the agents generated patches in diff format, which we standardized into the official JSON schema; (3) we further stratified the 300 instances by repository type across the 12 GitHub projects—for example, django is a web development framework repository with 114 issues; and (4) by analyzing results repository-by-repository, we identified which issues were successfully repaired by each agent.

The detailed results for program repair are summarized in Table 6 , which reports the number of successfully repaired issues per agent framework for each of the 12 repositories. A repair is considered successful if the diff-format patch generated by an agent passes the official test suite. In Table 6 , each row corresponds to a repository, and each cell represents the number of issues successfully repaired by a specific agent within that repository.

Table 6 reveals substantial differences in accuracy across agents. Notably, SE-Agent (Iter-3) achieved the highest accuracy, repairing 54% of the total issues.,
whereas the average success rate across all agents was only 36%.
Additionally, for the django repository, which contains the largest number of issues (114), Trae and SE-Agent (Iter-3) achieved the best performance, each successfully repairing 68 issues.
In contrast, for flask repository, which contains the fewest issues (3), none of the agents succeeded in repairing any issue, an unexpected outcome suggesting that the number of issues does not necessarily correlate with task difficulty.
Note that AgentOrchestra , OWL , and GPTswarm exhibit distinctly poor effectiveness. The underlying reason is that they do not leverage Patch tooling (Yang et al., 2024 ) , which leads to failures in generating correct diff-format patches. This limitation reflects a broader challenge inherent to current LLM capabilities.

In total, SE-Agent (Iter-2) and SWE-Agent fully repaired (100This indicates that agent frameworks are not universally effective for program repair. Although overall effectiveness was modest, these findings provide concrete evidence of the limitations of current agent frameworks in program repair and offer actionable insights for future improvements.

Answer to RQ1. The key takeaways are as follows: • Software Development: A clear effectiveness trade-off is observed among completeness, executability, and consistency. OpenHands achieves the best overall balance, with the highest quality score of 0.47. • Vulnerability Detection: The average success rate across the seven agent frameworks is approximately 66%, with GPTswarm achieving the highest detection accuracy of 77%. Nevertheless, this performance remains suboptimal and leaves considerable room for improvement. • Program Repair: Effectiveness is modest, with at most roughly half of the issues repaired by only 4 out of 7 agents, while the rest achieve low repair rates, highlighting significant potential for improvement.

4.2. Efficiency of Agent Frameworks (RQ2)

To address RQ2, we analyze the efficiency of the seven agent frameworks in the same set of code-centric software engineering tasks introduced in § 4.1 . Unlike RQ1, which focuses solely on final outcomes, RQ2 delves into the agents’ execution processes, providing a more nuanced understanding of their operational behavior.
In contrast to traditional software engineering automation tools, which execute pre-defined, statically encoded procedures, agents operate in a dynamic and adaptive manner. Consequently, assessing the efficiency of these processes is essential for gaining insights into the level of intelligence and adaptability demonstrated by each framework.

Table 7. Comparison of software development efficiency across different agent frameworks.

Metric AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent Average

Average Trajectory Steps 40.20 19.90 43.90 3.70 3.20 28.20 7.00 81.28 27.40 28.31

Correction Attempts 16.7 4.20 3.60 1.10 0.70 6.10 1.21 7.79 1.90 4.81

Correction Rate 41.54% 21.10% 8.20% 29.73% 21.86% 21.63% 17.19% 9.58% 6.93% 16.99%

Software Development. Table 7 presents the execution trajectory analysis for the software development task, revealing distinct operational characteristics across different agent frameworks. Statistical analysis shows that seven frameworks exhibit an average trajectory length of 28.31 steps, with OpenHands recording the longest trajectory of 81.28 steps.
Note that SE-Agent exhibits a distinctive iterative pattern: the first iteration comprises 43.9 steps, while the second and third iterations show markedly shorter trajectories of 3.70 and 3.20 steps, respectively. This progressive reduction suggests that SE-Agent employs an adaptive refinement strategy, in which an initial comprehensive exploration is followed by focused, targeted adjustments in subsequent iterations. Such a pattern reflects efficient convergence behavior, as the agent leverages insights from earlier iterations to streamline problem-solving in later stages.

Our analysis reveals that AgentOrchestra exhibits the highest correction attempts at 16.7, accounting for approximately 41.54% of its trajectory length. This substantially exceeds the average correction attempts of 4.81 and correction rate of 16.99%, representing the highest values among all evaluated agents.
In contrast, SWE-Agent achieves the lowest correction rate among all agents at merely 6.93%, while GPTswarm requires the fewest correction attempts at 1.21.
Notably, SE-Agent (Iter-1) initially exhibits the lowest correction rate at 8.20%. However, an intriguing pattern emerges across subsequent iterations: although the absolute number of correction attempts decreases to 1.10 in the second iteration and 0.70 in the third iteration, the correction rate paradoxically increases. This phenomenon is attributable to the substantial reduction in trajectory length across iterations, resulting in a higher proportional correction rate despite fewer absolute corrections.

Table 8. Comparison of vulnerability detection efficiency across different agent frameworks.

Metric AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent Average

Average Trajectory Steps 46.50 7.50 1.00 1.40 7.00 8.90 1.00 11.00 9.50 10.40

Correction Attempts 21.04 0.80 0.00 0.10 1.30 2.10 0.00 3.70 0.50 3.28

Correction Rate 45.25% 10.67% 0.00% 7.14% 18.57% 23.60% 0.00% 33.64% 5.26% 31.54%

Vulnerability Detection. Table 8 presents the trajectory statistics of these agents in the vulnerability detection task. The analysis reveals that seven frameworks exhibit an average trajectory length of 10.40 steps, with AgentOrchestra demonstrating the longest trajectory at 46.5 steps. In contrast, SE-Agent demonstrate the shortest trajectories, with the third iteration reaching only 7.00 steps.
Furthermore, Table 8 presents the correction attempts and corresponding correction rates for each agent framework in the vulnerability detection task. AgentOrchestra exhibits 21.04 correction attempts, constituting nearly 45.25% of its total trajectory steps, which represents the highest correction-to-execution ratio among the evaluated systems. This substantially exceeds the average of 3.28 correction attempts and 31.54% correction rate.
Moreover, both SE-Agent (Iter-1) and GPTswarm exhibit zero correction attempts, representing the most efficient execution patterns among all evaluated agents.

Table 9. Comparison of program repair efficiency across different agent frameworks.

Metric AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent Average

Average Trajectory Steps 46.80 64.50 51.50 67.40 69.10 78.10 2.90 69.30 67.40 57.44

Correction Attempts 21.10 1.00 6.70 9.90 9.50 19.50 0.50 25.20 10.40 11.53

Correction Rate 45.09% 1.55% 13.01% 14.69% 13.75% 24.97% 17.24% 36.36% 15.43% 20.08%

Program Repair. Table 9 presents the execution trajectory analysis for the program repair task.
Statistical analysis demonstrates that seven frameworks exhibit an average trajectory length of 57.44 steps, Trae records the longest average trajectory of 78.1 steps among single-agent frameworks, warranting a detailed examination of its execution pattern. Our analysis reveals that the repair process of Trae consists of: (1) 41.1 Bash commands for environment configuration, code execution, and repair validation; (2) 30 file editing operations; (3) 6 problem analysis steps; and (4) 1 completion command, totaling 78.1 steps. This decomposition indicates that Trae ’s extended trajectory primarily stems from its more comprehensive problem analysis phase and increased reliance on environment validation commands, distinguishing it from other frameworks that adopt more streamlined execution strategies.
Moreover, since GPTswarm employs the CodeReact (Zhuge et al., [n. d.] ) mechanism with a predetermined constraint of exactly 3 React cycles, it exhibits the shortest trajectory length of 2.90 steps among all seven evaluated agent frameworks, representing a distinct operational paradigm that prioritizes execution efficiency through fixed iteration constraints rather than adaptive exploration.

Although Trae exhibits the longest trajectory among all agents, its correction attempts of 19.50 do not represent the maximum value. OpenHands records the highest correction attempts at 25.20, accounting for 36.36% of its trajectory length, substantially exceeding averages of 11.53 attempts at 20.08% rate.
In contrast, GPTswarm demonstrates the fewest correction attempts at merely 0.5, while OWL exhibits the lowest correction rate at only 1.55%. However, these minimal correction metrics do not translate to superior performance in program repair tasks. Both GPTswarm and OWL fail to identify errors in their self-generated content, suggesting that their low correction frequencies reflect inadequate self-monitoring capabilities rather than execution efficiency. This observation underscores a critical insight: the absence of correction attempts may indicate a deficiency in error detection mechanisms rather than optimal performance. This deficiency can be attributed to the fact that neither GPTswarm nor OWL incorporates version control tools such as Git , utilized by SWE-Agent , or employs specialized diff format validation utilities like unidiff . The absence of these essential tools significantly undermines their operational efficiency and error detection capabilities.

Answer to RQ2. The key takeaways are as follows: • Trajectory Steps: OpenHands , AgentOrchestra , and SE-Agent (Iter-3) record the longest trajectories in software development, vulnerability detection, and program repair, respectively. • Correction Attempts: AgentOrchestra shows the longest correction attempts in software development and vulnerability detection, while OpenHands records the longest in program repair. • Correction Rate: Across the three tasks, AgentOrchestra achieves the highest correction rate, reflecting its lower efficiency due to frequent revisions.

4.3. Overhead of Agent Frameworks (RQ3) 
Table 10. Comparison of monetary overhead (USD) across different agent frameworks on three tasks.

Task AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent Total

Software Development $292.01 $21.05 $43.10 $31.01 $25.37 $48.90 $13.49 $39.98 $29.99 $544.90

Vulnerability Detection $14.13 $1.89 $0.29 $0.26 $1.27 $1.91 $0.67 $20.91 $1.07 $42.40

Program Repair $64.05 $2.49 $27.78 $38.40 $40.73 $15.53 $2.13 $54.48 $42.16 $287.75

Total $370.19 $25.43 $208.21 $66.34 $16.29 $115.37 $73.22 $875.05

Table 11. Comparison of token count across different agent frameworks on three tasks.

Task Component AgentOrchestra OWL SE-Agent (Iter-1) SE-Agent (Iter-2) SE-Agent (Iter-3) Trae GPTswarm OpenHands SWE-Agent

Software Development Input 380.34 M 42.88 M 440.69 M 28.31 M 20.54 M 32.09 M 287.31 K 1.26 B 371.70 M

Output 22.71 M 3.34 M 8.53 M 11.15 M 9.26 M 23.09 M 7.98 M 30.54 M 814.04 K

Vulnerability Detection Input 36.30 M 2.64 M 216.91 K 360.03 K 7.98 M 1.57 M 13.66 K 192.75 M 4.17 M

Output 1.60 M 632.38 K 248.32 K 202.15 K 537.87 K 841.91 K 394.12 K 5.85 M 227.90 K

Program Repair Input 99.59 M 6.72 M 332.03 M 447.96 M 484.44 M 13.28 M 54.10 K 663.55 M 495.50 M

Output 2.16 M 220.74 K 524.66 K 853.67 K 839.23 K 4.82 M 485.46 K 4.56 M 836.83 K

To address RQ3, we evaluate the costs of seven agents across three tasks. Comprehensive results are presented in Table 10 . The first column indicates the three evaluation tasks: software development, vulnerability detection, and program repair. Columns 2-9 show the costs (USD) incurred by each of the seven agents for these three tasks, while the last column presents the total cost across all seven agents for each task. The bottom row displays the total cost for each agent across all three tasks.

The results reveal that AgentOrchestra incurred the highest cost at $370.19 across the three tasks, whereas GPTswarm solved all problems across the three tasks with merely $16.29. Software development emerged as the most expensive task, with a total cost of $544.90, where AgentOrchestra consumed $292.01, the highest among all agents. The seven agents collectively spent $42.40 to complete the vulnerability detection task, with OpenHands leading at $20.91, while SE-Agent (Iter-1) required only $0.29, the lowest expenditure. For the program repair task, the total cost reached $287.75, with AgentOrchestra again ranking first at $64.05 for a single iteration. SE-Agent ’s cumulative cost across three iterations totaled $106.91, while GPTswarm remained the most economical at just $2.13.

Economic costs are determined by token consumption and model pricing. Since we employed the same LLM with consistent token pricing, we focus our analysis on token consumption, where the input price is $0.56 per million tokens, and the output price is $1.69 per million tokens. Notably, since the agent often reuses the same context across multiple interactions, the model can leverage a caching mechanism to reuse previously processed inputs. Consequently, even with a large number of input tokens, the overall cost may remain low due to the lower pricing of cached tokens ($0.07 per million). Table 11 presents the token consumption results for these agents, organized into three major rows representing the three tasks. Each major row contains two sub-rows indicating input and output token counts, respectively, with each column representing the token consumption for each agent.

As shown in Table 11 , despite AgentOrchestra incurring the highest cost in the software development task, it did not consume the most tokens. Instead, OpenHands consumed 1.26 B input tokens and 30.54 M output tokens, making it the highest consumer. GPTswarm consumed the fewest input tokens at 287.31 K, while SWE-Agent used only 814.04 K output tokens, the lowest among all agents. This discrepancy is attributable to the caching mechanism: although OpenHands processed the highest number of input and output tokens, these largely consisted of accumulated historical data that, when fed back to the agent, did not incur proportional costs. In the vulnerability detection task, OpenHands again consumed the most input tokens at 192.75 M and output tokens at 5.85 M. GPTswarm used the fewest input tokens at 13.66 K, while SWE-Agent consumed the least output tokens at 227.90 K. For the program repair task, OpenHands consumed 663.55 M input tokens, the highest among all agents, while Trae generated the most output tokens at 4.82 M. In contrast, GPTswarm consumed merely 54.10 K input tokens, and OWL used 220.74 K output tokens.
A notable observation is that, except for GPTswarm , all agents consumed more input tokens than output tokens. For GPTswarm , this pattern is reversed, with output token consumption exceeding input token consumption.

Figure 2 . Breakdown of token consumption across execution stages for software development among the seven agent frameworks.

To further investigate how token consumption is distributed across different execution stages among the seven agent frameworks, we employ the classification framework presented in Figure 2 for software development, Figure 3 for vulnerability detection, and Figure 4 for program repair. The first row comprises two multi-agent systems
for which we analyze token consumption at the individual sub-agent level. Given that SE-Agent ’s worker agents operate analogously to SWE-Agent as single agents and utilize a summary operators for post-evaluation trajectory synthesis, we apply a unified statistical methodology to SE-Agent ’s worker agents along with the four single-agent systems shown in the second row,
decomposing token consumption into four action categories: execution, editing, thinking, and management.

Software Development As illustrated in Figure 2 , AgentOrchestra employs four distinct agents for software development tasks: Planning agent, DeepAnalysis agent, DeepResearch agent, and BrowserUse agent. The token consumption is predominantly attributed to the Planning agent, which accounts for 67.2% of the total consumption, followed by the DeepAnalysis agent at 15.3% and the DeepResearch agent at 12.9%, while the BrowserUse agent contributes the least at 4.6%. OWL comprises two agents: User agent and Assistant agent, where the User agent dominates token consumption at 92.8%, with the Assistant agent accounting for merely 7.2%.

For SE-Agent in its first iteration, token consumption is primarily distributed between editing and execution, representing 49.3% and 45.7% of the total respectively, whereas management and thinking constitute only 0.1% and 1.3%. This distribution stems from SE-Agent ’s well-structured prompts with examples, and the post-evaluation summary accounts for only 3.6% of total consumption. In subsequent iterations, the streamlined prompts afford SE-Agent greater flexibility, resulting in increased proportions of management and thinking activities. Nevertheless, editing and execution continue to dominate total consumption, while the reduced prompt complexity leads to elevated summary operators consumption of 17.7% and 13.3% in the second and third iterations respectively.

Figure 2 further reveals that single-agent systems allocate the majority of token consumption to editing activities in software development tasks, specifically 48.9% for Trae and 45.2% for OpenHands . GPTswarm exclusively utilizes editing due to its IO-agent architecture, resulting in 100% editing consumption. Conversely, SWE-Agent exhibits the highest execution consumption at 51.2% of total tokens, with editing as the second-largest category at 47.4%. Trae and OpenHands demonstrate execution consumption of 37.5% and 38.7% respectively. Thinking activities constitute a minimal proportion in OpenHands and SWE-Agent , while accounting for 9.0% in Trae . Similarly, management activities represent a negligible share in SWE-Agent , whereas Trae and OpenHands allocate 4.7% and 16.1% of total consumption to management respectively.

Figure 3 . Breakdown of token consumption across execution stages for vulnerability detection among the seven agent frameworks.

Vulnerability Detection As depicted in Figure 3 , AgentOrchestra employs three agents for vulnerability detection tasks: Planning agent, DeepAnalysis agent, and DeepResearch agent. Token consumption is predominantly concentrated in the Planning agent at 65.8% of the total, followed by the deep analysis agent at 30.4% and the deep research agent at 3.8%. For OWL , the User agent accounts for 80.7% of total consumption, while the Assistant agent represents 19.3%.

In SE-Agent ’s first two iterations, token consumption is overwhelmingly dominated by the summary process, constituting 51.9% and 73.9% of total consumption respectively, whereas the third iteration allocates only 1.2% to summary activities. Editing operations account for 38.8%, 21.0%, and 66.4% across the three iterations respectively. Execution activities demonstrate minimal presence in the first two iterations but increase substantially to 31.4% in the third iteration, while thinking and management activities maintain negligible proportions throughout all iterations.

Figure 3 further demonstrates that single-agent systems allocate the majority of token consumption to editing activities in vulnerability detection tasks, specifically 72.8% for Trae , 80.4% for OpenHands , and 75.6% for SWE-Agent . Execution represents the second-largest consumption category across these three agents, accounting for 26.1%, 11.6%, and 21.6% respectively. Other activities including thinking and management constitute minimal proportions across all three agents. These three agents exhibit remarkable consistency in their token consumption patterns when addressing vulnerability detection tasks.

Figure 4 . Breakdown of token consumption across execution stages for program repair among the seven agent frameworks.

Program Repair As illustrated in Figure 4 , AgentOrchestra employs three agents for program repair tasks: Planning agent, DeepAnalysis agent, and DeepResearch agent. Token consumption is primarily attributed to the Planning agent at 66.2% of the total, followed by the DeepAnalysis agent at 21.6%, with the DeepResearch agent contributing the least at 12.2%. OWL comprises two agents: User agent and Assistant agent, where the User agent dominates token consumption at 94.2%, while the Assistant agent accounts for merely 5.5%.

For SE-Agent in its first iteration, token consumption is predominantly distributed between editing and execution, representing 51.9% and 47.0% of the total respectively, whereas management and thinking constitute only 0.1% and 0.4%. This distribution is attributable to SE-Agent ’s well-structured prompts with examples, and the post-evaluation summary accounts for only 0.6% of total consumption. In subsequent iterations, the streamlined prompts afford SE-Agent greater flexibility, resulting in increased proportions of management and thinking activities. Nevertheless, editing and execution continue to dominate total consumption, while the reduced prompt complexity leads to elevated summary operators consumption of 5.7% and 1.6% in the second and third iterations respectively.

Figure 4 further reveals that single-agent systems allocate the majority of token consumption to execution activities in program repair tasks, specifically 51.5% for Trae , 56.2% for OpenHands , and 45.3% for SWE-Agent . Editing operations account for 39.1%, 100.0%, 35.0%, and 35.2% of total consumption for Trae , GPTswarm , OpenHands , and SWE-Agent respectively. While thinking and management activities constitute minimal proportions in Trae and OpenHands , management activities notably account for 18.3% of total consumption in SWE-Agent .

Answer to RQ3. The key takeaways are as follows: • Monetary Cost: Among the three tasks, software development incurs the highest cost, while vulnerability detection requires the lowest. Of the seven agents, AgentOrchestra is the most expensive, whereas GPTswarm is the most cost-efficient. • Token Usage: OpenHands consumes the most tokens across all three tasks but does not incur the highest cost due to input token caching. GPTswarm consumes the fewest tokens and is the only agent where input tokens are fewer than output tokens, while all other agents exhibit higher input token consumption. • Consumption Breakdown: Agent systems exhibit similar patterns across tasks. For example,in AgentOrchestra , the Planning agent dominates. SE-Agent shows varying distributions due to prompt modifications. Single-agent systems focus consumption on execution and editing actions.

5. Discussion

After independently analyzing the effectiveness and efficiency of the evaluated agent frameworks, we now explore their interrelationships, with a particular focus on the intuitive notion that more complex reasoning and execution processes often lead to improved performance outcomes. We then address the potential threats to validity in our study to provide a balanced understanding of the results and their generalizability.

5.1. More steps, better effectiveness? 
Figure 5 . multi-agent systems vs single-agent systems in Software Development.

To facilitate a more comprehensive discussion of this issue, we categorize the seven agents into two groups based on the findings of RQ2: multi-agent systems (Multi-Agent system) and single-agent systems (Single-Agent system). This classification is motivated by the observation that multi-agent systems exhibit substantially longer average steps across all three tasks compared to their single-agent counterparts, with the disparity being particularly pronounced in the vulnerability detection and program repair task, where multi-agent systems require nearly twice the number of steps. Building upon the results from RQ1, we further conduct a statistical analysis to determine whether multi-agent systems leverage their extended execution trajectories to achieve superior effectiveness compared to single-agent systems across the three tasks.

Software Development. To systematically compare the differences between multi-agent systems and single-agent systems in software development tasks, we computed the average completeness, executability, and consistency of code projects generated by multi-agent systems and single-agent systems agents across five software development categories. The comparative results are illustrated in Figure 5 .
The analysis reveals nuanced performance trade-offs between the two paradigms across three evaluation dimensions. In terms of completeness, multi-agent systems demonstrates superior performance across all five software categories, consistently outperforming single-agent systems metrics. This suggests that Multi-Agent frameworks are more effective at generating comprehensive solutions that address all specified requirements.

Regarding executability, the generated code by single-agent systems exhibits a substantial advantage, significantly surpassing multi-agent systems performance. This indicates that single-agent systems produce more syntactically correct and immediately executable code. In the consistency evaluation, single-agent systems marginally outperforms multi-agent systems, suggesting slightly better adherence to coding standards and internal coherence. OpenHands demonstrates the best quality of 0.47. Overall, single-agent systems demonstrates greater effectiveness in software development, particularly excelling in code executability and consistency. When combined with the conclusions of RQ2, it is evident that single-agent systems holds a slight advantage over multi-agent systems.

Figure 6 . multi-agent systems vs single-agent systems in Vulnerability Detection.

Vulnerability Detection. We focused on two critical subsets: (1) the union of successfully completed tasks by both system types, and (2) the intersection of tasks that neither system could complete.
To compare the efficiency of multi-agent systems and single agent systems in smart contract vulnerability detection, we categorized the detection results into multi-agent systems and single-agent systems groups and conducted a comparative analysis across 10 vulnerability types of common dataset and 5 vulnerability types of CVE. This approach provides a more intuitive visualization of detection accuracy, as illustrated in Figure 6 . The results demonstrate that multi-agent systems and single-agent systems exhibit highly consistent detection effectiveness across nine vulnerability types, including Bad Randomness and RE. However, single-agent systems outperforms multi-agent systems in detecting six specific vulnerability types: Access Control, Logic Error, GL, IO, TM, and USE. Notably, no vulnerability types were exclusively detected by multi-agent systems. According to the results of RQ2, the number of steps in multi-agent systems is higher than that in single-agent systems, therefore single-agent systems demonstrates an advantage in this task.

Figure 7 . multi-agent systems vs single-agent systems in Program Repair.

Program Repair. To compare the problem-solving efficiency between multi-agent systems and single-agent systems, we conducted a controlled analysis by selecting two distinct subsets: (1) the union of successfully repaired issues by both system types, and (2) the intersection of issues that neither system could repair. The statistical results are presented in Figure 7 .
Similarly, we partition the experimental results into multi-agent systems and single-agent systems categories. Our analysis reveals that single-agent systems demonstrate superior repair effectiveness across all 12 repositories compared to multi-agent systems. When synthesized with the empirical evidence from RQ2, these findings substantiate that single-agent systems possesses a pronounced advantage in program repair tasks.

Reason Analysis. Based on the statistical analysis across the three aforementioned tasks, it is evident that single-agent system consistently demonstrates superior performance compared to multi-agent system in software engineering applications. To investigate this phenomenon, we conducted a comprehensive analysis of the underlying mechanisms.

In multi-agent system, multiple agents typically collaborate by invoking shared tools or utilizing specialized agent-specific tools, with a planning agent orchestrating the problem-solving workflow. Conversely, single-agent system architectures employ a single agent equipped with tools and follow a predefined workflow tailored to each specific task. However, the proliferation of agents in multi-agent system introduces substantial interaction overhead between the planning agent and downstream specialized agents. This results in information overload for the planning agent, leading to decision-making errors characterized by overthinking and erroneous outputs. Furthermore, inter-agent hallucinations significantly impact overall accuracy. As demonstrated in RQ2, multi-agent system exhibits higher correction attempts and correction rates compared to single-agent system. This phenomenon is attributable to two primary factors: (1) the increased number of agents generates excessive input tokens that exceed the LLM’s maximum context length, resulting in information loss, and (2) inherent LLM hallucinations. In contrast, single-agent system operates with a single agent, generating minimal context that remains within the LLM’s long-context constraints, thereby enabling comprehensive access to historical information and better control over FPs and hallucinations. These factors collectively contribute to multi-agent system underperforming single-agent system across all three tasks.

Theoretically, the presence of planning mechanisms in multi-agent system should confer superior generalization capabilities; however, our empirical findings reveal the contrary. As previously noted, frameworks such as AgentOrchestra and OWL fail to generate correctly formatted diff patches, resulting in diminished repair success rates in program repair tasks. This indicates that multi-agent collaboration is susceptible to propagating identical errors, where agents may fail to detect mistakes in outputs generated by other agents. In contrast, specialized repair agents like SWE-Agent are equipped with dedicated patch tools that circumvent format-related failures. Similarly, GPTswarm ’s lack of specialized tools leads to the generation of malformed diff patches, consequently reducing repair rates.

Notably, SE-Agent deviates from conventional multi-agent collaborative generation paradigms. Instead, it employs a single agent for task execution, followed by a summary agent that synthesizes trajectory information. In subsequent iterations, the worker agent learns from successful experiences or avoids failed trajectories—a process we characterize as vertical iteration. Our analysis reveals that SE-Agent ’s performance improves progressively across three iterations. For instance, in program repair tasks, the initial repair success rate of 47.33% improved to 53.00% after the first summarization iteration, and ultimately reached 53.67% after two summarization rounds and three complete iterations.

Another noteworthy approach is GPTswarm ’s group execution strategy, which partitions instances into predetermined groups within a single testing round. Upon completing each group, the agent synthesizes lessons learned from both successful and failed cases, providing experiential guidance for subsequent groups. This methodology proves particularly advantageous in vulnerability detection tasks, making GPTswarm the top-performing agent in accuracy.

These findings collectively demonstrate that in software engineering lifecycle tasks, incorporating specialized tools yields superior results compared to adding dedicated agents, facilitating rapid generalization and adaptation to novel tasks. Moreover, both vertical and horizontal summarization of historical trajectories during task execution effectively enhance agent performance, providing a training-free approach to performance augmentation.

5.2. Threats to Validity

Internal. Several factors may influence the internal validity of our study.
(1) Regarding the selection of agent frameworks, proprietary task-specific agents may perform optimally on particular tasks; however, they lack generality, which is inconsistent with the current trend toward developing AGI. Therefore, we focus on general-purpose agent frameworks, which are more cutting-edge, have broader applicability, and allow fair comparisons across multiple tasks.
(2) Concerning dataset selection, an ideal general-purpose agent would handle the full software engineering lifecycle, from requirements to reliable code. However, evaluating each stage of the lifecycle is challenging and resource-intensive, and no single benchmark currently covers the entire process. To ensure objective evaluation, we concentrate on key code-centric tasks and adopt existing benchmarks for each task.
(3) Regarding the choice of underlying LLMs, we acknowledge that different base models can lead to variations in agent performance. Considering the considerable economic overhead of agents, we employed DeepSeek-V3.1 as the underlying LLM consistently across all agents and tasks. This controlled approach allows for comparable results. In future work, when resources permit, it would be worthwhile to explore different base models and potential model selection optimizations.

External. The primary external validity threats stem from implementation discrepancies between the published frameworks and their released codebases. For instance, certain auxiliary components described in Trae ’s design are not fully reflected in the official example code. We retained the functional integrity of the released implementation and fixed random seeds to ensure consistent comparison. Although the results may not fully represent the idealized design, they faithfully reflect the framework’s practical behavior in real-world use. Additionally, some frameworks adopt simplified configurations in their released code for code-related tasks. We therefore explicitly reported the actual agent and role settings used in our experiments to avoid overinterpreting their collaborative capabilities.

6. Related Work

As discussed in § 2 , the use of intelligent agents in code-centric software engineering has recently attracted increasing research attention. Numerous frameworks have been introduced to automate a range of tasks, including software development, vulnerability detection, and program repair. However, to the best of our knowledge, this work is the first to conduct a systematic empirical comparison of contemporary agent-based approaches, aiming to provide a deeper understanding of their actual capabilities and limitations across diverse software engineering scenarios.

Agents for Software Engineering. In recent years, a growing number of versatile agent frameworks have emerged and been applied to increasingly complex scientific and productivity tasks (Luo et al., 2025 ) . As software engineering represents a core pillar of productivity, enhancing its automation through agent technologies holds substantial promise for improving development efficiency and reliability. Accordingly, many studies have explored the application of intelligent agents to code-centric SE tasks, as discussed in § 3.2 .
Among them, some agent frameworks are designed for specific tasks, such as ExpeRepair (Mu et al., 2025 ) and SemAgent (Pabba et al., 2025 ) , which focus exclusively on program repair.
In contrast, general-purpose agent frameworks that are capable of handling diverse complex tasks exhibit stronger generalization and better alignment with real-world software engineering workflows. For instance, to support complex software engineering environments, SWE-Agent (Yang et al., 2024 ) enhances repository-scale operations with a customized agent–computer interface that enables autonomous file manipulation, repository navigation, and test execution. Likewise, Trae (Team et al., 2025 ) provides a research-friendly command-line interface for orchestrating real-world development workflows in a extensible manner. To align agent behavior more closely with human development practices, OpenHands (Wang et al., 2025 ) equips agents with human-like operational abilities, such as interacting with terminals and browsing the web. To better orchestrate agent behaviors, AgentOrchestra (Zhang et al., 2025 ) employs hierarchical task decomposition through a top-level planner directing multiple specialized workers, while OWL (Hu et al., 2025 ) structures multi-agent collaboration following a workforce-style paradigm aimed at large-scale productivity. GPTswarm (Zhuge et al., [n. d.] ) further advances scalable coordination by leveraging graph-based composition and self-organized swarm intelligence. In addition, to optimize the reasoning trajectory, SE-Agent (Lin et al., 2025 ) proposes a self-evolving multi-step reasoning paradigm that refines solutions through strategy diversification and trajectory optimization.
Overall, these developments highlight the growing convergence between agent technologies and software engineering, underscoring the need for a systematic evaluation of their actual capabilities across diverse software engineering tasks.

Benchmarks for Software Engineering Agents. Although intelligent agents have demonstrated the potential to handle multiple phases of the software engineering lifecycle in an end-to-end manner, the community still lacks a comprehensive benchmark capable of holistically evaluating their capabilities across different development stages. Existing evaluations remain fragmented and rely on task-specific datasets.

For software development tasks, widely used benchmarks include HumanEval (Chen et al., 2021a ) and MBPP (Austin et al., 2021 ) , which focus on single-function code generation and contain only a few hundred tasks. More complex datasets requiring multi-file development have emerged, such as SRDD (Qian et al., 2023a ) , CAASD (Zhang et al., 2024 ) , SoftwareDev (Hong et al., 2023 ) , and ProjectDev (Nguyen et al., 2025 ) . With over a thousand tasks, SRDD achieves broader task coverage, while the other datasets include only dozens and therefore fall short in representing realistic, large-scale development workflows.

For vulnerability detection, curated datasets such as SySeVR (Li et al., 2021 ) for C/C++, CWE-Bench-Java (Li et al., 2024 ) for Java, and BigBench (Srivastava et al., 2023 ) for Python enable the evaluation of LLM-based vulnerability prediction. However, these datasets primarily measure static detection performance while overlooking the interactive reasoning and environment orchestration capabilities expected from agents. To the best of our knowledge, LLM-SmartAudit (Wei et al., 2025 ) is the first work that introduces an agent-based approach for vulnerability detection, and its dataset thus serves as an important reference for evaluating existing agent capabilities in this domain.

For vulnerability repair, classical benchmarks like Defects4J (Just et al., 2014 ) , BugsInPy (Widyasari et al., 2020 ) , HumanEval-Java (Chen et al., 2021b ) , and QuixBugs (Lin et al., 2017 ) contain small-scale defects localized in specific functions or modules. They are suitable for evaluating traditional automated repair techniques or single LLM capabilities, but insufficient for assessing multi-step repair behaviors in realistic engineering environments.
To better align with real-world workflows, recent benchmarks construct repair tasks directly from GitHub issues and their associated repositories, such as SWE-bench (Jimenez et al., 2023 ) , SWE-bench Lite (swe, 2024a ) , SWE-bench Lite-S (Xia et al., 2024a ) , and SWE-bench Verified (swe, 2024b ) , which are widely adopted for evaluating agent-based program repair.

Overall, no single benchmark can comprehensively evaluate the full spectrum of capabilities exhibited by software engineering agents. A unified evaluation framework that integrates diverse datasets across different task categories is needed to fully assess their robustness and generalizability throughout the entire software engineering life-cycle.

Empirical Evaluation of Software Engineering Agents. The recent surge in intelligent software engineering agents has drawn increasing attention from the research community, prompting systematic empirical studies of their capabilities. Researchers have examined agent behavior from multiple perspectives, including architectural design, reasoning processes, and task-specific effectiveness.

Regarding architectural design, studies focus on the intrinsic characteristics of agent systems, such as single-agent versus multi-agent configurations. Gao et al. (Gao et al., 2025b ) conducted an extensive comparison across 15 software engineering tasks, showing that multi-agent systems generally perform better on complex tasks due to long-horizon context tracking and role-specific error correction, whereas single-agent systems often achieve higher efficiency on simpler tasks. They further proposed a hybrid paradigm, cascading requests between multi-agent systems and single-agent systems, to balance accuracy and deployment cost.

In terms of reasoning processes, empirical analyses have investigated agent decision-making workflows. Ceka et al. (Ceka et al., 2025 ) present the first systematic study of software engineering agents through the lens of execution traces. They classify decision pathways, identify core components such as bug localization, patch generation, and test generation, and analyze how reasoning about error context influences successful outcomes. These insights illuminate the internal mechanisms that drive agent performance, independent of specific task instances.

Moreover, task-specific evaluations provide complementary evidence of agent effectiveness. Meng et al. (Meng et al., 2025 ) conducted fine-grained empirical studies of LLM-based agents for automated bug fixing, assessing fault localization accuracy at file- and line-levels, bug reproduction capabilities, and overall repair performance. Their findings highlight that improving agent effectiveness requires advances in both the underlying LLM models and the design of agent workflows.

Unlike previous studies, which often focus on specific tasks or architectural configurations, our work provides a systematic evaluation of general-purpose software engineering agents across a range of code-centric tasks. We assess not only their effectiveness but also their efficiency and deployment cost, offering a holistic perspective on agent performance throughout the software engineering life-cycle. This comprehensive approach allows us to identify strengths and limitations of current frameworks and informs the design of more capable and practical agent systems.

7. Conclusion

This study presents a comprehensive empirical evaluation of seven general-purpose agent frameworks across three critical code-centric software engineering tasks: software development, vulnerability detection, and program repair. By systematically examining agent performance from the perspectives of effectiveness, efficiency, and overhead, we reveal important insights into the current capabilities and limitations of intelligent agents in real-world software engineering scenarios.
Our study reveals important insights into agent frameworks from three key angles. In terms of effectiveness, agents show moderate success: OpenHands balances code quality well in software development, GPTswarm excels in vulnerability detection accuracy, and program repair remains challenging with only some agents fixing about half of the issues. Efficiency analysis indicates that SE-Agent (Iter-3) requires the most steps across all experiments. AgentOrchestra has the longest correction sequences, while OpenHands ranks second, demonstrating stable and convergent behavior. Regarding overhead, software development tasks are the most costly. The token consumption breakdown reveals multi-agent frameworks dominated by planning stages, while single-agent systems concentrate costs on execution and editing activities. These findings collectively highlight the trade-offs and potentials of current frameworks, guiding future improvements in building more capable and resource-aware software engineering agents.

References

- (1)

- swe (2024a) 2024a. SWE-bench Lite . https://www.swebench.com/lite.html

- swe (2024b) 2024b. SWE-bench Verified . https://openai.com/index/introducing-swe-bench-verified/

- ant (2025) 2025. Building effective agents. https://www.anthropic.com/engineering/building-effective-agents

- goo (2025) 2025. Google’s Whitepaper on Agents. https://drive.google.com/file/d/1oEjiRCTbd54aSdB_eEe3UShxLBWK9xkt/view?pli=1

- Aggarwal (2005) Krishan Kumar Aggarwal. 2005. Software engineering . New Age International.

- Austin et al. (2021) Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. 2021. Program synthesis with large language models. arXiv preprint arXiv:2108.07732 (2021).

- Basili (1989) Victor R Basili. 1989. Software development: A paradigm for the future. In [1989] Proceedings of the Thirteenth Annual International Computer Software & Applications Conference . IEEE, 471–485.

- Bessey et al. (2010) Al Bessey, Ken Block, Ben Chelf, Andy Chou, Bryan Fulton, Seth Hallem, Charles Henri-Gros, Asya Kamsky, Scott McPeak, and Dawson Engler. 2010. A few billion lines of code later: using static analysis to find bugs in the real world. Commun. ACM 53, 2 (Feb. 2010), 66–75. doi: 10.1145/1646353.1646374

- Ceka et al. (2025) Ira Ceka, Saurabh Pujar, Shyam Ramji, Luca Buratti, Gail Kaiser, and Baishakhi Ray. 2025. Understanding Software Engineering Agents Through the Lens of Traceability: An Empirical Study. arXiv preprint arXiv:2506.08311 (2025).

- Chakraborty et al. (2021) Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2021. Deep learning based vulnerability detection: Are we there yet? IEEE Transactions on Software Engineering 48, 9 (2021), 3280–3296.

- Chen et al. (2021a) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. 2021a. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 (2021).

- Chen et al. (2021b) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. 2021b. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 (2021).

- DeepSeek-AI (2024) DeepSeek-AI. 2024. DeepSeek-V3 Technical Report. arXiv:2412.19437 [cs.CL] https://arxiv.org/abs/2412.19437

- Gao et al. (2025a) Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, et al. 2025a. A survey of self-evolving agents: On path to artificial super intelligence. arXiv preprint arXiv:2507.21046 (2025).

- Gao et al. (2025b) Mingyan Gao, Yanzi Li, Banruo Liu, Yifan Yu, Phillip Wang, Ching-Yu Lin, and Fan Lai. 2025b. Single-agent or Multi-agent Systems? Why Not Both? arXiv preprint arXiv:2505.18286 (2025).

- Hong et al. (2023) Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zi Hen Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. 2023. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. In International Conference on Learning Representations . https://api.semanticscholar.org/CorpusID:265301950

- Hu et al. (2025) Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin, Yingru Li, Qiguang Chen, Zeyu Zhang, Yifeng Wang, Qianshuo Ye, Bernard Ghanem, Ping Luo, and Guohao Li. 2025. OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation. arXiv:2505.23885 [cs.AI] https://arxiv.org/abs/2505.23885

- JACKSON et al. (2025) VICTORIA JACKSON, BOGDAN VASILESCU, DANIEL RUSSO, PAUL RALPH, RAFAEL PRIKLADNICKI, MALIHEH IZADI, SARAH D’ANGELO, SARAH INMAN, ANIELLE ANDRADE, and ANDRÉ VAN DER HOEK. 2025. The Impact of Generative AI on Creativity in Software Development: A Research Agenda. (2025).

- Jimenez et al. (2023) Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. 2023. Swe-bench: Can language models resolve real-world github issues? arXiv preprint arXiv:2310.06770 (2023).

- Just et al. (2014) René Just, Darioush Jalali, and Michael D Ernst. 2014. Defects4J: A database of existing faults to enable controlled testing studies for Java programs. In Proceedings of the 2014 international symposium on software testing and analysis . 437–440.

- Le Goues et al. (2019) Claire Le Goues, Michael Pradel, and Abhik Roychoudhury. 2019. Automated program repair. Commun. ACM 62, 12 (2019), 56–65.

- Li et al. (2024) Ziyang Li, Saikat Dutta, and Mayur Naik. 2024. IRIS: LLM-assisted static analysis for detecting security vulnerabilities. arXiv preprint arXiv:2405.17238 (2024).

- Li et al. (2021) Zhen Li, Deqing Zou, Shouhuai Xu, Hai Jin, Yawei Zhu, and Zhaoxuan Chen. 2021. Sysevr: A framework for using deep learning to detect software vulnerabilities. IEEE Transactions on Dependable and Secure Computing 19, 4 (2021), 2244–2258.

- Lin et al. (2017) Derrick Lin, James Koppel, Angela Chen, and Armando Solar-Lezama. 2017. QuixBugs: A multi-lingual program repair benchmark set based on the Quixey Challenge. In Proceedings Companion of the 2017 ACM SIGPLAN international conference on systems, programming, languages, and applications: software for humanity . 55–56.

- Lin et al. (2025) Jiaye Lin, Yifu Guo, Yuzhen Han, Sen Hu, Ziyi Ni, Licheng Wang, Mingguang Chen, Hongzhang Liu, Ronghao Chen, Yangfan He, Daxin Jiang, Binxing Jiao, Chen Hu, and Huacan Wang. 2025. SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents. arXiv:2508.02085 [cs.AI] https://arxiv.org/abs/2508.02085

- Liu et al. (2024) Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng, Zhenpeng Chen, Lingming Zhang, and Yiling Lou. 2024. Large language model-based agents for software engineering: A survey. arXiv preprint arXiv:2409.02977 (2024).

- Liu et al. (2019) Kui Liu, Anil Koyuncu, Dongsun Kim, and Tegawendé F Bissyandé. 2019. TBar: Revisiting template-based automated program repair. In Proceedings of the 28th ACM SIGSOFT international symposium on software testing and analysis . 31–42.

- Luo et al. (2025) J. Luo, W. Zhang, Y. Yuan, et al. 2025. Large Language Model Agent: A Survey on Methodology, Applications and Challenges. arXiv preprint arXiv:2503.21460 (2025).

- Meng et al. (2025) Xiangxin Meng, Zexiong Ma, Pengfei Gao, and Chao Peng. 2025. An Empirical Study on LLM-based Agents for Automated Bug Fixing. arXiv:2411.10213 [cs.SE] https://arxiv.org/abs/2411.10213

- Mu et al. (2025) Fangwen Mu, Junjie Wang, Lin Shi, Song Wang, Shoubin Li, and Qing Wang. 2025. EXPEREPAIR: Dual-Memory Enhanced LLM-based Repository-Level Program Repair. arXiv preprint arXiv:2506.10484 (2025).

- Nguyen et al. (2025) Minh Huynh Nguyen, Thang Phan Chau, Phong X Nguyen, and Nghi DQ Bui. 2025. Agilecoder: Dynamic collaborative agents for software development based on agile methodology. In 2025 IEEE/ACM Second International Conference on AI Foundation Models and Software Engineering (Forge) . IEEE, 156–167.

- Pabba et al. (2025) Anvith Pabba, Alex Mathai, Anindya Chakraborty, and Baishakhi Ray. 2025. SemAgent: A Semantics Aware Program Repair Agent. arXiv:2506.16650 [cs.SE] https://arxiv.org/abs/2506.16650

- Qian et al. (2023a) Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu, and Maosong Sun. 2023a. Communicative agents for software development. arXiv preprint arXiv:2307.07924 6, 3 (2023), 1.

- Qian et al. (2023b) Cheng Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. 2023b. ChatDev: Communicative Agents for Software Development. In Annual Meeting of the Association for Computational Linguistics . https://api.semanticscholar.org/CorpusID:270257715

- Srivastava et al. (2023) Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. 2023. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on machine learning research (2023).

- Team et al. (2025) Trae Research Team, Pengfei Gao, Zhao Tian, Xiangxin Meng, Xinchen Wang, Ruida Hu, Yuanan Xiao, Yizhou Liu, Zhao Zhang, Junjie Chen, Cuiyun Gao, Yun Lin, Yingfei Xiong, Chao Peng, and Xia Liu. 2025. Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling. (2025). arXiv:2507.23370 [cs.SE] https://arxiv.org/abs/2507.23370

- Wang et al. (2025) Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, and Graham Neubig. 2025. OpenHands: An Open Platform for AI Software Developers as Generalist Agents. arXiv:2407.16741 [cs.SE] https://arxiv.org/abs/2407.16741

- Wei et al. (2025) Zhiyuan Wei, Jing Sun, Yuqiang Sun, Ye Liu, Daoyuan Wu, Zijian Zhang, Xianhao Zhang, Meng Li, Yang Liu, Chunmiao Li, et al. 2025. Advanced smart contract vulnerability detection via llm-powered multi-agent systems. IEEE Transactions on Software Engineering (2025).

- Widyasari et al. (2020) Ratnadira Widyasari, Sheng Qin Sim, Camellia Lok, Haodi Qi, Jack Phan, Qijin Tay, Constance Tan, Fiona Wee, Jodie Ethelda Tan, Yuheng Yieh, et al. 2020. Bugsinpy: a database of existing bugs in python programs to enable controlled testing and debugging studies. In Proceedings of the 28th ACM joint meeting on european software engineering conference and symposium on the foundations of software engineering . 1556–1560.

- Xia et al. (2024a) Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. 2024a. Agentless: Demystifying llm-based software engineering agents. arXiv preprint arXiv:2407.01489 (2024).

- Xia et al. (2024b) Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. 2024b. Agentless: Demystifying llm-based software engineering agents. arXiv preprint arXiv:2407.01489 (2024).

- Yang et al. (2024) John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. 2024. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. arXiv:2405.15793 [cs.SE] https://arxiv.org/abs/2405.15793

- Yu et al. (2025) Zhongming Yu, Hejia Zhang, Yujie Zhao, Hanxian Huang, Matrix Yao, Ke Ding, and Jishen Zhao. 2025. OrcaLoca: An LLM Agent Framework for Software Issue Localization. arXiv:2502.00350 [cs.SE] https://arxiv.org/abs/2502.00350

- Zhang et al. (2023) Quanjun Zhang, Chunrong Fang, Yuxiang Ma, Weisong Sun, and Zhenyu Chen. 2023. A survey of learning-based automated program repair. ACM Transactions on Software Engineering and Methodology 33, 2 (2023), 1–69.

- Zhang et al. (2024) Simiao Zhang, Jiaping Wang, Guoliang Dong, Jun Sun, Yueling Zhang, and Geguang Pu. 2024. Experimenting a new programming practice with llms. arXiv preprint arXiv:2401.01062 (2024).

- Zhang et al. (2025) Wentao Zhang, Liang Zeng, Yuzhen Xiao, Yongcong Li, Ce Cui, Yilei Zhao, Rui Hu, Yang Liu, Yahui Zhou, and Bo An. 2025. AgentOrchestra: Orchestrating Hierarchical Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol. arXiv:2506.12508 [cs.AI] https://arxiv.org/abs/2506.12508

- Zhuge et al. ([n. d.]) Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, and Jürgen Schmidhuber. [n. d.]. GPTSwarm: Language Agents as Optimizable Graphs. In Forty-first International Conference on Machine Learning .
