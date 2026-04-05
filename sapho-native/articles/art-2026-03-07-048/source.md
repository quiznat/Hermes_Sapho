---
version: source-capture.v1
article_id: art-2026-03-07-048
ticket_id: ticket-import-art-2026-03-07-048
source_url: https://arxiv.org/html/2506.12508v1
canonical_url: https://arxiv.org/abs/2506.12508
source_title: 'AgentOrchestra: A Hierarchical Multi-Agent Framework for General-Purpose
  Task Solving'
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-05T04:19:13Z'
linked_paper_urls: []
---
# Source Capture

## Title

AgentOrchestra: A Hierarchical Multi-Agent Framework for General-Purpose Task Solving

## Body

† † footnotetext: † † \dagger † Correspondence to Wentao Zhang: zhangwent963@gmail.com, Bo An: boan@ntu.edu.sg † † footnotetext: 1 Our Repository: https://github.com/SkyworkAI/DeepResearchAgent

AgentOrchestra: A Hierarchical Multi-Agent Framework for General-Purpose Task Solving

Wentao Zhang Skywork AI Ce Cui Skywork AI Yilei Zhao Nanyang Technological University Yang Liu Skywork AI Bo An Nanyang Technological University Skywork AI

Abstract

Recent advances in agent systems based on large language models (LLMs) have demonstrated strong capabilities in solving complex tasks. However, most current methods lack mechanisms for coordinating specialized agents and have limited ability to generalize to new or diverse domains. We introduce AgentOrchestra , a hierarchical multi-agent framework for general-purpose task solving that integrates high-level planning with modular agent collaboration. Inspired by the way a conductor orchestrates a symphony and guided by the principles of extensibility , multimodality , modularity , and coordination , AgentOrchestra features a central planning agent that decomposes complex objectives and delegates sub-tasks to a team of specialized agents. Each sub-agent is equipped with general programming and analytical tools, as well as abilities to tackle a wide range of real-world specific tasks, including data analysis, file operations, web navigation, and interactive reasoning in dynamic multimodal environments. AgentOrchestra supports flexible orchestration through explicit sub-goal formulation, inter-agent communication, and adaptive role allocation. We evaluate the framework on three widely used benchmark datasets covering various real-world tasks, searching web pages, reasoning over heterogeneous modalities, etc. Experimental results demonstrate that AgentOrchestra consistently outperforms flat-agent and monolithic baselines in task success rate and adaptability. These findings highlight the effectiveness of hierarchical organization and role specialization in building scalable and general-purpose LLM-based agent systems.

1 Introduction

Recent advances in Large Language Models (LLMs) or Large Multimodal Models (LMMs) have led to a shift from simple dialogue LLMs/LMMs chatgpt2022optimizing ; hurst2024gpt ; anthropic2024claude35 ; team2023gemini ; touvron2023llama ; bai2023qwen to models capable of performing sophisticated reasoning jaech2024openai ; openai2025o3 ; anthropic2025claude37systemcard ; guo2025deepseek ; yang2024qwen2 ; qwen2025qwen3 , enabling progress from answering straightforward questions to responding to complex, multi-step queries. However, current LLMs remain largely disconnected from real-world environments due to the absence of interactive tool integration, which constrains their ability to perform grounded, general-purpose, and complex tasks. Overcoming this limitation requires augmenting LLMs with executable tools as well as perceptual and action interfaces, thereby transforming LLMs into interactive agents capable of perceiving, acting, and reasoning across both virtual and real-world environments.

These LLM-based agents have shown strong capabilities in real-world tasks such as browser use openai2025operator ; browser_use2024 , computer use openai2025operator ; anthropic2024computeruse ; qin2025ui , code act wang2024executablecodeactionselicit , game playing wang2023voyager ; tan2024cradle , and research assistance openai2024deepresearch ; google2024deepresearch ; xai2025grok3 . In parallel, a new wave of generalist agents has emerged, characterized by their ability to operate across various domains rather than being restricted to single-task settings. Systems such as Manus shen2025mindmachinerisemanus and open-source agent frameworks including OpenHands wang2024openhands , OpenManus openmanus2025 , and smolagents smolagents2025 exemplify this trend by demonstrating unified perception, reasoning, and tool-augmented action. The development of tool-use interfaces such as OpenAI’s Function Calling and Anthropic’s Model-Context Protocol (MCP) openai2023functioncalling ; anthropic2024mcp further facilitates seamless tool integration and supports a broader diversity of tasks. Collectively, these advances mark a transition from narrow, single-domain specialization toward integrated, general-purpose intelligence.

Despite recent advances, current generalist agents have yet to achieve genuine general-purpose intelligence, particularly when confronted with complex, real-world multimodal tasks. They still face significant difficulties in robust perception, reasoning, and action across heterogeneous modalities and dynamic environments. Consequently, realizing truly general-purpose agent systems still faces several fundamental challenges:
i) Limited Generalization and Transferability : Most existing agent frameworks are narrowly tailored to specific domains or tasks, exhibiting limited ability to generalize across heterogeneous environments or adapt to novel, unseen scenarios. Such limitations significantly constrain their deployment in open-ended or real-world contexts.
ii) Insufficient Multimodal Perception and Reasoning : Current agents often struggle to effectively perceive, align, and reason over diverse modalities such as text, image, audio, video, and structured data, thereby impeding their performance on complex tasks that require integrated multimodal understanding and reasoning.
iii) Limited Scalability and Maintainability : Prevailing agent architectures frequently lack modularity and extensibility, making it challenging to incorporate new models, tools, or adapt to emerging application scenarios. This deficiency hinders the development of scalable and sustainable agent ecosystems.
iv) Inefficient Multi-Agent Collaboration and Communication : Existing approaches rarely support efficient collaboration and communication among multiple agents, limiting their capacity for dynamic role allocation, coordinated planning, and effective teamwork on compositional or large-scale tasks.

To address these challenges based on the principles of extensibility , multimodality , modularity , and coordination , we propose AgentOrchestra , a hierarchical multi-agent framework for general-purpose task solving. AgentOrchestra features a top-level planning agent that coordinates specialized sub-agents equipped with domain-specific tools. This enables flexible task decomposition, extensible collaboration, and unified handling of multimodal inputs, making it well-suited for real-world applications. Contributions of this work are as follows:

- •

( Extensibility ) We introduce AgentOrchestra , a hierarchical framework that integrates a top-level planner with modular sub-agents. New capabilities can be easily added by incorporating additional specialized sub-agents, making the system highly extensible and adaptable to diverse domains.

- •

( Multimodality ) AgentOrchestra provides a unified tool interface that supports plug-and-play integration of specialized tools such as web browsers, document analyzers, and code interpreters across text, image, audio, video, and structured data. This enables agents to process and reason over heterogeneous modalities seamlessly.

- •

( Modularity ) AgentOrchestra adopts a modular architecture that separates agent, tool, and model layers, enabling flexible combination, extension, and replacement of components. This design supports scalable deployment and adaptation to diverse application scenarios.

- •

( Coordination ) AgentOrchestra enables efficient collaboration and communication among specialized sub-agents through hierarchical planning and dynamic role allocation, facilitating coordinated problem solving on complex tasks.

- •

Extensive experiments demonstrate that AgentOrchestra consistently outperforms existing agent baselines in generalization, multimodal understanding, and collaborative problem solving across diverse real-world and benchmark tasks.

2 Related Work

2.1 Tool-Augmented Agent Systems

The integration of tools with LLMs marks a paradigm shift in AI agent development. Compared to traditional rule-based agents, tool-augmented LLM agents exhibit greater flexibility, cross-domain reasoning, and natural language interaction liang2025llm . These agents have shown strong capabilities in web browsing openai2025operator ; browser_use2024 , computer operation anthropic2024computeruse ; qin2025ui , code execution wang2024executablecodeactionselicit , and game playing wang2023voyager ; tan2024cradle . Standardized tool interfaces, such as OpenAI’s Function Calling and Anthropic’s Model-Context Protocol (MCP), have further streamlined tool integration and expanded the range of executable tasks openai2023functioncalling ; anthropic2024mcp . Recent work on frameworks like ToolMaker wolflein2025llm enables automatic transformation of code-based research into LLM-compatible tools, reducing reliance on manual tool development.

2.2 General-Purpose Agent Frameworks

The rise of generalist agents and open-source frameworks, such as Manus shen2025mindmachinerisemanus , OpenHands wang2024openhands , OpenManus openmanus2025 , and smolagents smolagents2025 —has advanced unified perception, reasoning, and tool-augmented action beyond domain-specific applications. These frameworks target broader, general-purpose intelligence across diverse tasks. Comprehensive surveys lu2020general have documented this evolution, highlighting the shift from task-specific agents to more flexible, general-purpose systems.

2.3 Multi-Agent Collaboration Systems

The field of multi-agent systems has seen substantial growth, with research focusing on both task-oriented communication (collaborative exchanges and adversarial interactions) and open-ended conversations. Recent systems such as MetaGPT hong2023metagpt demonstrate how multiple specialized agents can coordinate to solve complex problems beyond the reach of single agents. Li et al. li2024mateval explored personal LLM agents, examining their capabilities, efficiency, and security in collaborative settings. While these advances highlight the adaptability and promise of multi-agent collaboration, many existing approaches still lack mechanisms for efficient communication, dynamic role allocation, and coordinated teamwork in large-scale tasks. In this work, we address these challenges by proposing a hierarchical multi-agent framework designed to achieve more efficient execution and collaboration compared to existing agent and multi-agent systems.

3 AgentOrchestra

AgentOrchestra is a hierarchical multi-agent framework designed to systematically address the key challenges of generalization, multimodal reasoning, scalability, and collaboration in complex task-solving environments. The framework adopts a two-tier architecture, where a top-level planning agent decomposes tasks and coordinates modular sub-agents responsible for domain-specific processing and multimodal reasoning. This design enables flexible composition, seamless collaboration, and robust adaptation across diverse domains, while naturally scaling to complex and heterogeneous tasks through the dynamic expansion of specialized sub-agents. Section 3.1 introduces the core design principles of our framework. Section 3.2 details the implementation of the planning agent, and Section 3.3 discusses the architecture and interaction patterns of specialized sub-agents.

3.1 Agent Design Principles

Agent. An agent is an autonomous computational entity that perceives and interprets the environment,
maintains a history of actions and observations, and flexibly generates actions to accomplish a wide variety of user-specified tasks across diverse domains.

Model. LLMs are the core drivers of our framework. To enhance flexibility and adaptability, we introduce a unified LLM abstraction layer that supports both leading commercial models (e.g., GPT-4.1, Claude-4-Sonnet) and local open-source models (e.g., Qwen2.5). This design enables agents to dynamically select and switch between different LLMs during task execution, aligning each model’s unique strengths with the requirements of specific sub-tasks and environments. By supporting seamless integration of new models as they become available, our modular architecture ensures long-term extensibility and consistently strong performance across a wide range of applications.

Observation. An observation encompasses all information perceived by the agent at each step of execution.
This includes the user’s task description, any attached files, screenshots, and other relevant contextual data. The observation also maintains a complete history (including error messages) of previous steps, providing the agent with a comprehensive view of the ongoing process. Each step’s observation is stored in the agent’s memory, enabling effective reasoning, error recovery, and context-aware decision making throughout the task-solving process.

Action. In our framework, actions are operationalized through a set of pre-defined tools wang2024openhands ; openmanus2025 ; smolagents2025 , each exposed via function calling openai2023functioncalling ; anthropic2024mcp interfaces that specify parameters and expected behaviors. Importantly, actions are not equivalent to tools. A single tool can support multiple actions by accepting different action parameters. For example, a planning tool may support create , update , and delete actions, all accessible through a unified interface with action-specific arguments. This design improves modularity and extensibility, allowing the agent to perform diverse operations with fewer, more flexible tools.

To ensure safety and system integrity, all operations with potential side effects are executed within a docker-based sandbox, such as an isolated Linux container or virtual machine. This sandboxing mechanism provides strong isolation, preventing unintended modifications or security risks to the underlying environment while allowing the agent to safely and reliably interact with external tools.

Memory. Memory serves as a fundamental component of the agent, persistently recording the complete history of agent execution. This comprehensive execution trace, which records task sequences, observations, actions, and errors, allows the agent to reason effectively, recover from errors robustly, and make context-aware decisions. At each step, the agent summarizes and updates its memory, allowing it to utilize prior context and improve its ability to correct errors and adapt to evolving task requirements.

The execution flow of an agent in our framework follows an iterative cycle: the agent perceives the environment through observation (including task descriptions, attached files, and execution history), stores these observations in memory , leverages its memory and the model selected from the unified LLM abstraction layer to interpret the context and select an appropriate action from pre-defined tools, executes the action within a sandbox environment, and records the outcomes in memory for subsequent reasoning and adaptation. This cycle repeats until the task is completed or a termination condition is met.

Figure 1: Architecture of AgentOrchestra .

3.2 Planning Agent

Planning Agent Overview . The Planning Agent serves as the central orchestrator in our hierarchical framework, dedicated to high-level reasoning, task decomposition, and adaptive planning. Rather than directly interacting with the environment or executing low-level actions, the Planning Agent interprets user objectives and systematically decomposes complex, long-horizon tasks into manageable sub-tasks. These sub-tasks are then assigned to specialized sub-agents based on their expertise and the evolving context.

A distinctive feature of the Planning Agent is its ability to maintain a global perspective throughout the execution process, aggregating feedback from sub-agents and monitoring progress toward the overall objective. This enables the agent to perform dynamic plan updates, adapting its strategy in real time in response to intermediate results, unexpected challenges, or shifting user requirements. Such closed-loop coordination is crucial for robustness and generalization across diverse domains. To ensure modularity and scalability, the Planning Agent interacts with sub-agents using a standard interface. This design conceals domain-specific details and facilitates the addition of new types of agents. By separating high-level planning from specialized task execution, our architecture avoids the limitations of monolithic agents, such as low flexibility and poor adaptation to new tasks. The core workflow is managed by a Planning Tool, which oversees task planning and execution tracking.

Planning Tool Design . The Planning Tool offers structured functionalities for creating, updating, and managing plans for complex tasks. Each plan comprises a sequence of discrete steps, each explicitly grounded in the available tools and agent capabilities. The module supports key operations such as plan creation, modification, status marking, and progress monitoring, while ensuring that every complex task is decomposed into several actionable steps, each assigned to specialized sub-agents or tool invocations. The Planning Tool maintains unique identifiers for each plan, enables concurrent management of multiple plans, and tracks execution states (e.g., not started, in progress, completed, blocked) for all steps. Importantly, the Planning Tool dynamically updates and adapts the plan in response to the evolving execution context, intermediate outcomes, and feedback from sub-agents. All agent-plan interactions are conducted via a standardized, extensible interface, facilitating seamless integration of new task types and agent capabilities.

3.3 Specialized Sub-Agents

To address real-world challenges such as comprehensive information retrieval from the internet, acquisition of domain-specific or time-sensitive expertise, statistical analysis, gaming, and computational tasks, it is essential to possess a set of foundational capabilities. These include reasoning, multimodal information processing, web browsing, and, more generally, proficiency in tool use. To further enhance these foundational abilities and adapt to diverse, complex tasks, there is a growing need to incorporate an expandable set of low-level specialized sub-agents. By continually extending the repertoire and capabilities of these sub-agents, the hierarchical multi-agent system as a whole can achieve scalable improvements, mirroring scaling laws at the agent level and enabling more robust, generalizable problem-solving.

Therefore, we further instantiate our hierarchical multi-agent framework with a set of specialized sub-agents tailored for distinct stages of complex tasks. First, a Deep Researcher Agent is responsible for extensive information retrieval, efficiently scanning and filtering web pages to identify promising sources, much like the initial human exploration of online information. Next, a Browser Use Agent enables fine-grained interactions with web content, allowing direct engagement with videos, PDFs, and various HTML elements to extract precise information. Finally, a Deep Analyzer Agent is designed to perform advanced reasoning and comprehensive analysis, integrating and interpreting information collected by previous agents to address tasks such as statistical inference, image analysis, gaming, and market analysis. In addition to their dedicated specialized tools, each sub-agent is also equipped with a python interpreter tool, enabling the automatic generation and execution of code for data analysis, computational verification, and analytical support. This further enhances each agent’s ability to handle complex tasks and perform self-verification through code-based analysis.

3.3.1 Deep Researcher Agent

Deep Researcher Agent Overview . The Deep Researcher Agent represents a specialized agent designed to perform comprehensive information gathering tasks. This agent implements a sophisticated research methodology through a dual-tool architecture: a dedicated Deep Researcher Tool for web-based information retrieval and a Python Interpreter Tool for advanced data processing. The Deep Researcher Tool operates on a query-based paradigm, enabling the agent to perform targeted web searches, extract relevant insights, and generate concise summaries of web content. This approach allows for efficient information gathering while maintaining context awareness and relevance to the research objectives. The integration of a Python Interpreter Tool further enhances the agent’s capabilities by enabling heterogeneous data processing and analysis workflows, particularly useful for handling complex or unstructured information sources. This architectural design enables the Deep Researcher to effectively bridge the gap between raw information gathering and meaningful knowledge synthesis.

Deep Researcher Tool Design . The Deep Researcher Tool constitutes the core of the information gathering process, drawing inspiration from the OpenManus openmanus2025 system and is designed for extensible, domain-agnostic research. Upon receiving a research query, the tool first optimizes the query using an LLM-based prompt, then conducts a breadth-first web search across multiple engines (e.g., Google, Bing, Baidu) to maximize coverage and information diversity. For each result, the tool extracts key insights via LLM-driven content analysis, assigning relevance scores and recording source attribution. It dynamically generates follow-up queries based on uncovered insights, recursively exploring the search space up to a predefined depth or time limit. All visited URLs, insights, and generated queries are tracked in a structured research context. The final output is a structured, relevance-ranked summary that aggregates key findings and explicitly cites all information sources, enabling transparent and scalable knowledge synthesis.

3.3.2 Browser Use Agent

Browser Use Agent Overview . The Browser Use Agent is a unified framework for automated web interaction, centered on the Auto Browser Use Tool. Unlike the Deep Researcher Agent, which focuses on broad and exploratory information gathering, the Browser Use Agent is designed for precise and targeted information acquisition from the web. It supports a wide range of browser-based tasks such as web search, navigation, content extraction, and document manipulation through a parameterized action. This enables the agent to execute complex workflows, including dynamic form filling, PDF and video control, and tab management, while maintaining fine-grained execution control and robust state management. Integration with a Python Interpreter Tool further enhances automation flexibility and enables custom scripting for advanced web scenarios.

Auto Browser Use Tool Design . The Auto Browser Use Tool adopts a modular, action-centric architecture in which each browser operation is defined as an independent, parameterized action and systematically registered in a central action registry. Supported actions encompass search queries, URL navigation, DOM element manipulation, content extraction, scrolling, PDF and video control, tab and session management, and interaction with complex page elements such as drop down menus and iframes. Each action is specified by a clear parameter schema, enabling precise, context-aware execution. The tool maintains comprehensive session and state management and incorporates robust error handling for browser events and asynchronous tasks. This extensible design facilitates the integration of new browser actions and ensures reliable automation across a wide range of web environments.

3.3.3 Deep Analyzer Agent

Deep Analyzer Agent Overview. The Deep Analyzer Agent is designed for advanced data analysis and interpretation tasks, integrating both a dedicated Deep Analyzer Tool and a Python Interpreter Tool. Unlike above agents focused on the information retrieval, the Deep Analyzer Agent operates on user-defined analytical tasks and specified source materials, providing comprehensive, context-aware reasoning across diverse data types. The Python Interpreter Tool component enables the execution of custom analytical scripts, further enhancing the agent’s ability to process complex, multimodal data sources.

Deep Analyzer Tool Design . The Deep Analyzer Tool employs a question-source paradigm, supporting both direct analytical tasks and analysis based on attached files or external URIs. It accommodates a wide range of data formats, including text, image, audio, video, and compressed archives, automatically extracting and structuring content for analysis. For each task, the tool invokes one or more large language models to conduct step-by-step reasoning, optionally synthesizing results from multiple models to ensure accuracy and robustness. All analyses are summarized and consolidated through a dedicated summarization model, producing coherent, interpretable outputs. This modular, extensible design allows the Deep Analyzer Agent to flexibly adapt to new data formats and evolving analytical requirements.

4 Experiments

This section presents our experimental setup and results. We first describe the baseline methods implemented for comparison, followed by an overview of the benchmarks used for evaluation. We then detail the evaluation metrics and implementation specifics of our framework and baselines. Finally, we provide a comprehensive analysis of the experimental results. Additional qualitative examples and case studies are included in the Appendix B for further illustration.

4.1 Benchmarks

- •

SimpleQA wei2024measuringshortformfactualitylarge is a widely-used open-domain benchmark for evaluating the factual accuracy of language models. It consists of 4,326 adversarially constructed, fact-seeking questions spanning various domains, requiring precise entity and relation extraction. This benchmark serves as a fundamental testbed for assessing agents’ information retrieval, reasoning ability, and their capacity to recognize their own limitations.

- •

GAIA mialon2023gaiabenchmarkgeneralai is a comprehensive benchmark designed to evaluate general AI assistants on real-world tasks requiring reasoning, multimodal information processing, web browsing, and tool use. The benchmark comprises 450 questions spanning three difficulty levels and includes scenarios such as web browsing, document analysis, and interactive reasoning. GAIA rigorously tests an agent’s ability to integrate diverse resources and demonstrate human-level robustness across practical, multimodal tasks.

- •

Humanity’s Last Exam (HLE) phan2025humanity is a multimodal benchmark designed to rigorously evaluate AI systems’ human-level reasoning and general intelligence. It comprises 2,500 questions spanning a wide range of subjects, requiring advanced logical deduction, abstraction, and cross-domain reasoning. HLE closely emulates the complexity of real human examinations and serves as a gold standard for assessing advanced generalist AI capabilities.

4.2 Evaluation Metrics

Accuracy Score (pass@1) measures the proportion of questions for which the model’s top prediction is fully correct, providing an overall assessment of single-attempt success in open-ended tasks.

4.3 Baselines

We compare our hierarchical multi-agent with mainstream models and agents, including Manus shen2025mindmachinerisemanus , OpenAI Deep Research openai2024deepresearch , HuggingFace Open DeepResearch huggingface_open_deep_research_2024 , as well as other leading agents or models listed on the SimpleQA Leaderboard simpleqa2024leaderboard , GAIA Leaderboard mialon2023gaialeaderboard , and HLE Leaderboard hleleaderboard2025 .

4.4 Implementation Details

In terms of agent implementation, we utilize claude-3.7-sonnet with the thinking mode as the backbone for both the Planning Agent and the Deep Researcher Agent. For the Planning Agent, we cap the maximum number of steps at 20, while for the Deep Researcher Agent, the step limit is set to 3. The Browser Use Agent is implemented using gpt-4.1 , with a maximum of 5 reasoning steps per episode. For the Auto Browser Use Tool, the maximum number of interaction steps per single invocation is set to 50. The Deep Analyzer Agent leverages both gemini-2.5-pro-preview-05-06 and o3 models, with the maximum steps limited to 3.

4.5 Results

We compare our agent with other baseline methods on three benchmarks and conduct a detailed analysis of the experimental results.

Table 1: Performance comparison on SimpleQA, GAIA, and HLE benchmarks.

Model and Agent SimpleQA GAIA HLE

Level 1 Level 2 Level 3 Average

Models

o3 (w/o tools) 49.4 - - - - 20.3

claude-3.7-sonnet (w/o tools) - - - - - 8.9

gemini-2.5-pro-preview-05-06 50.8 - - - - 17.8

Agents

HF Open DeepResearch (o1) - 67.92 53.49 34.62 55.15 -

OpenAI Deep Research - 74.29 69.06 47.60 67.36 26.6

Manus - 86.50 70.10 57.69 73.90 -

Langfun Agent - 86.79 76.74 57.69 76.97 -

AWorld - 88.68 77.91 53.85 77.58 -

Perplexity Deep Research 93.9 - - - - 21.1

Ours 95.3 92.45 83.72 57.69 82.42 25.9

4.6 SimpleQA Benchmark

As shown in Table 1 , our hierarchical agent framework achieves state-of-the-art performance on the SimpleQA benchmark, with an accuracy of 95.3%. This result substantially outperforms leading LLM baselines such as o3 (49.4%), gemini-2.5-pro-preview-05-06 (50.8%), and surpasses strong agent-based baselines, including Perplexity Deep Research (93.9%). The superior accuracy of our method demonstrates the effectiveness of a hierarchical, role-based agent composition for factoid question answering, especially when compared to both monolithic LLMs and recent retrieval-augmented agents.

The primary strength of our approach is its modular decomposition of the question answering process. The Planning Agent is responsible for interpreting user intent and orchestrating the collaboration among specialized sub-agents, such as the Browser Use Agent for information retrieval and the Deep Researcher Agent for verification. This division of responsibilities enables effective cross-verification of candidate answers and substantially reduces the risk of hallucination. For instance, when presented with a question like “Who received the IEEE Frank Rosenblatt Award in 2010?”, the system is able to systematically retrieve potential answers from the web, assess their reliability, and synthesize a well-validated response. Nevertheless, the use of multiple agents may introduce additional computational overhead, which can be suboptimal for handling very simple queries that could be efficiently addressed by a single LLM. To address this, future work will focus on developing adaptive mechanisms to dynamically streamline the workflow for trivial cases, thereby enhancing overall system efficiency.

4.7 GAIA Benchmark

AgentOrchestra achieves state-of-the-art results on the GAIA validation dataset, with accuracies of 92.45% on Level 1, 83.72% on Level 2, and 57.69% on Level 3, for an overall average of 82.42%. The agent consistently outperforms advanced baselines such as AWORLD (77.58%) and Langfun Agent (76.97%), especially as task difficulty increases. Notably, the performance decline of our agent from Level 1 to Level 3 is more gradual than that of the competing methods, demonstrating greater robustness and adaptability to complex, multi-stage reasoning challenges. This suggests that hierarchical coordination and dynamic task allocation can effectively mitigate the increased cognitive demands associated with higher-level GAIA tasks.

The key strength of our AgentOrchestra lies in its ability to decompose complex problems and flexibly assign them to the most appropriate sub-agents. For example, in a Level 3 GAIA scenario that required extracting numerical data from an embedded table within a PDF and then performing multi-step calculations, the Planning Agent first invoked the Browser Use Agent to locate and download the file, then delegated parsing to the Deep Analyzer Agent, and finally coordinated the synthesis of the answer. This layered process ensures high reliability and transparency in multimodal, tool-driven tasks. However, we observe that frequent information exchange between agents can introduce additional latency and system overhead. To address this, our design explicitly aims to minimize unnecessary agent switching whenever possible. In future work, we plan to further explore adaptive routing and sub-agent selection strategies to enhance both the efficiency and scalability of the system.

4.8 HLE Benchmark

Our hierarchical agent achieves an average score of 25.9% on the HLE benchmark, outperforming most of baseline models and agent systems, including o3 (20.3%), gemini-2.5-pro-preview-05-06 (17.8%), and claude-3.7-sonnet (8.9%). Notably, our approach also surpasses Perplexity Deep Research (21.1%) and demonstrates a clear advantage over single-agent architectures, particularly on tasks that require high-level reasoning, expert knowledge integration, or multi-step tool use. These results highlight the effectiveness of our system for tackling challenging, real-world problems that demand both in-depth analysis and adaptive problem-solving.

5 Limitations and Future Work

Limitations. Despite the promising results achieved by our hierarchical agent framework, several limitations remain. First, the increased architectural complexity and inter-agent communication can result in additional system latency and computational overhead, particularly for tasks that could otherwise be addressed by a single, highly capable model. Second, the reliance on external tools and web resources exposes the system to potential issues related to tool reliability, web content variability, and compatibility across diverse formats, which may affect robustness in certain real-world deployments. Third, while the agent’s design enables powerful reasoning and flexible information access, it also raises new challenges for ethical oversight and responsible AI use. For example, the dynamic integration of third-party tools and real-time Internet content requires careful monitoring to prevent the propagation of misinformation, protect user privacy, and ensure compliance with relevant legal and ethical standards.

Future Work. Future work will proceed along several directions. First, we aim to further optimize the efficiency of agent orchestration by introducing adaptive routing and lightweight coordination mechanisms, minimizing unnecessary agent switching and reducing response latency for routine tasks. Second, we plan to expand the ecosystem of specialized sub-agents to support a broader range of complex functions, such as advanced data visualization, knowledge base construction, and integration with domain-specific expert systems. In particular, we are interested in developing agents for automated scientific research assistance, including literature review, automatic paper writing, and hypothesis generation, inspired by recent advances in AI for Science. Third, we will enhance the system’s transparency, safety, and ethical accountability by incorporating explainable decision pathways, robust monitoring, and user-controllable access to web and tool-based resources, ensuring responsible and trustworthy deployment in high-stake environments.

6 Conclusion

In this work, we present a hierarchical multi-agent framework AgentOrchestra that integrates specialized sub-agents for planning, research, web interaction, and deep analysis. Extensive experiments on multiple benchmarks, including SimpleQA, GAIA, and HLE, demonstrate that our approach consistently surpasses existing baselines, especially on tasks requiring complex reasoning and dynamic use of external tools. The modular architecture supports flexible expansion and robust adaptation to a wide variety of open-domain and expert-level tasks. While certain challenges remain regarding system efficiency, tool reliability, and ethical oversight, our results highlight the effectiveness and versatility of hierarchical agent collaboration for advancing autonomous reasoning systems. We believe this paradigm establishes a foundation for developing more general, transparent, and trustworthy AI agents capable of addressing real-world problems at scale.

References

- [1] Anthropic. Claude 3.5 Sonnet. https://www.anthropic.com/news/claude-3-5-sonnet , 2024.

- [2] Anthropic. Introducing Computer Use, a New Claude 3.5 Sonnet, and Claude 3.5 Haiku. https://www.anthropic.com/news/3-5-models-and-computer-use , 2024. Accessed: 2025-05-13.

- [3] Anthropic. Introducing the Model Context Protocol. https://www.anthropic.com/news/model-context-protocol , 2024.

- [4] Anthropic. Claude 3.7 Sonnet System Card. https://www.anthropic.com/claude-3-7-sonnet-system-card , 2025.

- [5] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen Technical Report. arXiv preprint arXiv:2309.16609 , 2023.

- [6] OpenAI ChatGPT. Optimizing Language Models for Dialogue. OpenAI. com , 30, 2022.

- [7] Google DeepMind. Gemini Deep Research. https://gemini.google/overview/deep-research/?hl=en , 2024.

- [8] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. arXiv preprint arXiv:2501.12948 , 2025.

- [9] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. MetaGPT: Meta Programming for Multi-agent Collaborative Framework. arXiv preprint arXiv:2308.00352 , 3(4):6, 2023.

- [10] HuggingFace. Open-source DeepResearch - Freeing Our Search Agents. https://huggingface.co/blog/open-deep-research , 2024.

- [11] Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. GPT-4o System Card. arXiv preprint arXiv:2410.21276 , 2024.

- [12] Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. OpenAI o1 System Card. arXiv preprint arXiv:2412.16720 , 2024.

- [13] Yu Li, Shenyu Zhang, Rui Wu, Xiutian Huang, Yongrui Chen, Wenhao Xu, Guilin Qi, and Dehai Min. MATEval: A Multi-Agent Discussion Framework for Advancing Open-Ended Text Evaluation. In International Conference on Database Systems for Advanced Applications , pages 415–426. Springer, 2024.

- [14] Guannan Liang and Qianqian Tong. LLM-Powered AI Agent Systems and Their Applications in Industry. arXiv preprint arXiv:2505.16120 , 2025.

- [15] Xinbin Liang, Jinyu Xiang, Zhaoyang Yu, Jiayi Zhang, Sirui Hong, Sheng Fan, and Xiao Tang. OpenManus: An Open-Source Framework for Building General AI Agents, 2025.

- [16] Cewu Lu and Shiquan Wang. The General-purpose Intelligent Agent. Engineering , 6(3):221–226, 2020.

- [17] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. GAIA: A Benchmark for General AI Assistants, 2023.

- [18] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. GAIA Leaderboard. https://huggingface.co/spaces/gaia-benchmark/leaderboard , 2023.

- [19] Magnus Müller and Gregor Žunič. Browser Use: Enable AI to Control Your Browser, 2024.

- [20] OpenAI. Function Calling. https://platform.openai.com/docs/guides/function-calling , 2023.

- [21] OpenAI. Introducing Deep Research. https://openai.com/index/introducing-deep-research , 2024.

- [22] OpenAI. Introducing OpenAI o3 and o4-mini. https://openai.com/index/introducing-o3-and-o4-mini/ , 2025.

- [23] OpenAI. Introducing Operator. https://openai.com/blog/operator , 2025.

- [24] Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed Shaaban, John Ling, Sean Shi, et al. HLE Leaderboard. https://agi.safe.ai/ , 2025.

- [25] Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed Shaaban, John Ling, Sean Shi, et al. Humanity’s Last Exam. arXiv preprint arXiv:2501.14249 , 2025.

- [26] Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, et al. UI-TARS: Pioneering Automated GUI Interaction with Native Agents. arXiv preprint arXiv:2501.12326 , 2025.

- [27] Aymeric Roucher, Albert Villanova del Moral, Thomas Wolf, Leandro von Werra, and Erik Kaunismäki. smolagents: A Smol Library to Build Great Agentic Systems. https://github.com/huggingface/smolagents , 2025.

- [28] Minjie Shen and Qikai Yang. From Mind to Machine: The Rise of Manus AI as a Fully Autonomous Digital Agent, 2025.

- [29] Weihao Tan, Wentao Zhang, Xinrun Xu, Haochong Xia, Ziluo Ding, Boyu Li, Bohan Zhou, Junpeng Yue, Jiechuan Jiang, Yewen Li, et al. Cradle: Empowering Foundation Agents toward General Computer Control. arXiv preprint arXiv:2403.03186 , 2024.

- [30] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: A Family of Highly Capable Multimodal Models. arXiv preprint arXiv:2312.11805 , 2023.

- [31] Qwen Team. Qwen3: Think Deeper, Act Faster. https://qwenlm.github.io/blog/qwen3/ , 2025.

- [32] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and Efficient Foundation Language Models. arXiv preprint arXiv:2302.13971 , 2023.

- [33] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv preprint arXiv:2305.16291 , 2023.

- [34] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. Executable Code Actions Elicit Better LLM Agents, 2024.

- [35] Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, et al. OpenHands: An Open Platform for AI Software Developers as Generalist Agents. In The Thirteenth International Conference on Learning Representations , 2024.

- [36] Jason Wei, Nguyen Karina, Hyung Won Chung, Yunxin Joy Jiao, Spencer Papay, Amelia Glaese, John Schulman, and William Fedus. Measuring Short-Form Factuality in Large Language Models, 2024.

- [37] Jason Wei, Nguyen Karina, Hyung Won Chung, Yunxin Joy Jiao, Spencer Papay, Amelia Glaese, John Schulman, and William Fedus. SimpleQA Leaderboard. https://github.com/openai/simple-evals , 2024.

- [38] Georg Wölflein, Dyke Ferber, Daniel Truhn, Ognjen Arandjelović, and Jakob Nikolas Kather. LLM Agents Making Agent Tools. arXiv preprint arXiv:2502.11705 , 2025.

- [39] xAI. Grok 3 Beta — The Age of Reasoning Agents. https://x.ai/news/grok-3 , 2025.

- [40] An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, et al. Qwen2.5 Technical Report. arXiv preprint arXiv:2412.15115 , 2024.

\appendixpage

Appendix A Agents and Tools

Agent Tool Parameters Note

Planning Agent Planning Tool action

The action to be executed. Action can be:

create : Create a new plan;

update : Update the plan;

delete : Delete the plan;

mark : Mark a step as completed.

Deep Researcher Agent Deep Researcher Tool query Search, extract insight, and summarize the web page contents

Python Interpreter Tool code Execute the code

Deep Analyzer Agent Deep Analyzer Tool question , source Analyze and summarize the question with the source (e.g., files)

Python Interpreter Tool code Execute the code

Browser Use Agent Auto Browser Use Tool action

The action to be executed. Action can be:

search : Search the web with a query.

go_to_url : Go to a specific URL.

find_archive_url : Find the archive URL.

click : Click on a specific element on the page.

go_back : Go back to the previous page.

input : Input text into a specific input field.

pdf_viewer : Interact with the PDF.

e.g., next page, search keywords, etc.

video_viewer : Interact with the video.

e.g., play, pause, seek, etc.

scroll : Scroll the page.

extract_content : Extract the content of the page.

open_tab : Open a new tab.

switch_tab : Switch to a specific tab.

close_tab : Close a specific tab.

Python Interpreter Tool code Execute the code 
Table 2: Agent tools and their parameters.

Appendix B Case Study

In this section, we systematically present representative cases of AgentOrchestra , accompanied by critical analyses to elucidate the underlying factors contributing to these outcomes. We primarily showcase the performance on the GAIA validation set, categorized by both difficulty Level 1, Level 2, and Level 3 and data type, including text, image, audio, video, spreadsheet, ZIP archive, and other file types.

Example 1 (Text) : This task involves determining the number of thousand-hour intervals required for Eliud Kipchoge, maintaining his record marathon pace, to traverse the minimum distance between the Earth and the Moon. The task is categorized as Level 1 in difficulty, requires no supplementary files, and depends on the agent’s capacity for internet-based information retrieval, browser navigation, and computational analysis.

From Figure 2 , it can be seen that AgentOrchestra first generates a plan and then sequentially executes this plan by invoking sub-agents. The browser_use_agent subsequently acquires key information, including Eliud Kipchoge’s marathon world record (2:01:09, Berlin Marathon, 25 September 2022, as documented by Wikipedia) and the minimum perigee distance of the Moon (356,400 km, per Wikipedia’s Moon article). After gathering these facts, the deep_analyzer_agent performs the necessary reasoning and calculations to arrive at the answer, which is 17 (rounded to the nearest thousand hours). Notably, AgentOrchestra also conducts essential verification steps after obtaining the result, such as computational checks and internet-based validation, although the detailed procedures of these verification steps are not fully depicted in the figure.

Figure 2: Execution trajectory of AgentOrchestra for Example 1.

Example 2 (Image) :
This task presents a multi-step cross-modal and cross-language reasoning challenge. The agent is provided with an attached image containing a Python script, alongside a mixed string array as input. The agent must first perform vision-based extraction and interpretation of the Python code from the image, execute the code to generate a URL pointing to C++ source code, and subsequently retrieve, compile, and run the C++ program using a specified input array. The final answer is derived by reasoning over the program’s output. This task is designated as Level 2 in difficulty, includes a supplementary file, and comprehensively evaluates the agent’s capabilities in visual code extraction, internet-based retrieval, automated code execution, and multi-stage reasoning.

As illustrated in Figure 3 , AgentOrchestra first generates a structured plan and then executes it by sequentially invoking specialized sub-agents. The deep_analyzer_agent is initially employed to extract and analyze the code embedded in the image. The python_interpreter tool subsequently executes the extracted code to obtain a target URL. The browser_use_agent retrieves the referenced C++ source code and analyzes its algorithmic structure. Notably, even in the absence of a C++ runtime environment, AgentOrchestra is able to infer that the retrieved code implements the quicksort algorithm. Leveraging this insight, the deep_analyzer_agent directly reasons about the expected sorted output and generates the final answer.

Figure 3: Execution trajectory of AgentOrchestra for Example 2.

Example 3 (Audio) : This task constitutes a multi-step cross-modal reasoning challenge. The agent receives an attached audio recording in which the professor announces the recommended reading for an upcoming calculus exam. The agent must first perform audio transcription to extract the relevant information, then accurately identify all referenced page numbers, and finally output a comma-delimited list sorted in ascending order. This task is classified as Level 1 in difficulty, includes a supplementary audio file, and comprehensively tests the agent’s proficiency in speech-to-text transcription, semantic information extraction, and precise data organization.

As illustrated in Figure 4 , AgentOrchestra first constructs a structured plan, which is executed via the sequential coordination of specialized sub-agents. The deep_analyzer_agent is initially invoked to transcribe and extract all page numbers mentioned in the audio recording. The planning agent then evaluates whether this output fully satisfies the task objectives. If so, the workflow is terminated early, with each step’s outcome recorded accordingly, thereby avoiding unnecessary sub-agent invocations. Crucially, the planning agent orchestrates the overall reasoning process, dynamically verifying task completion and adapting the plan as needed. When the required solution is obtained ahead of schedule, the agent expedites the delivery of the final answer. Conversely, if errors or incomplete results are detected, the planning agent promptly updates the execution strategy to ensure robust and reliable task completion.

Figure 4: Execution trajectory of AgentOrchestra for Example 3.

Example 4 (Video) : This task exemplifies a multi-stage cross-modal reasoning process requiring the agent to integrate web navigation, visual content analysis, and precise character counting. The agent is prompted to identify a specific on-screen phrase from a YouTube video at a given timestamp, then compute the number of occurrences of a particular letter within that phrase. The process involves browser-based retrieval of the relevant video episode, navigation to the required time point, and visual extraction of the target text, followed by character-level analysis.

As depicted in Figure 5 , AgentOrchestra systematically devises and executes a stepwise plan, leveraging specialized agents for browser automation and deep analysis. Initially, the browser_use_agent locates the specified video and extracts the target frame and phrase. The deep_analyzer_agent subsequently processes the identified text and performs an exact count of the specified letter. Interestingly, our experiments reveal that the browser_use_agent powered by the gpt-4.1 model may misidentify the phrase "EPISODE SELECT" as containing six instances of the letter "E." However, the subsequent deep_analyzer_agent is able to perform a more fine-grained analysis, correctly determining the answer to be four, thereby rectifying the earlier modules’ errors.

Figure 5: Execution trajectory of AgentOrchestra for Example 4.

Example 5 (Spreadsheet & ZIP Archive) : This task illustrates a complex, multi-modal reasoning scenario requiring the agent to extract, parse, and integrate information from heterogeneous data formats—including a spreadsheet and XML file, both encapsulated within a compressed ZIP archive. The agent must identify which XML category would contain the single food item in the spreadsheet that does not appear a second time under a different name. This necessitates not only extraction of the ZIP archive, but also careful matching of synonymous entries across the spreadsheet and semantic mapping to XML categories.

As depicted in Figure 6 , AgentOrchestra constructs a comprehensive stepwise plan, coordinating the invocation of specialized agents to process each data modality. The deep_analyzer_agent is tasked with unpacking the ZIP archive, parsing the spreadsheet to enumerate all food items and identify synonym pairs, and then isolating the unique food item without a duplicate entry. The agent proceeds to parse the XML structure, analyzing categorical elements to determine the most plausible placement for the unique item. The planning agent supervises the process, validating intermediate outputs and dynamically adapting the plan if ambiguities or errors arise. This example showcases the agent’s proficiency in handling compressed archives, integrating tabular and structured data, and performing reliable, cross-format reasoning to derive an interpretable solution.

Figure 6: Execution trajectory of AgentOrchestra for Example 5.

Appendix C Agent Prompts and Tool Pseudocodes

C.1 Agent Prompts

This prompt instructs the Planning Agent to generate a detailed, step-by-step plan to solve a given complex task. The agent is required to explicitly incorporate available tools and team members, specify file paths for attachments, and delegate subtasks as needed. The agent must ensure correctness by running verification steps and output a comprehensive solution plan.

Planning Agent Description A planning agent that can plan the steps to complete the task. Task Instruction You have one question to answer. It is paramount that you provide a correct answer. Give it all you can: I know for a fact that you have access to all the relevant tools and team members to solve it and find the correct answer (the answer does exist).
Failure or ’I cannot answer’ or ’None found’ will not be tolerated, success will be rewarded. * You must begin by creating a detailed plan that explicitly incorporates the available TOOLS and TEAM MEMBERS. Then, follow the plan step by step to solve the complex task. * If the task involves attached files, you are required to specify the absolute path in your plan and share it explicitly with your team members. * If the task need to use the team members, you are required to provide the ORIGINAL TASK as the ‘task‘ parameter for the agents to understand the task. DO NOT modify the task. * If the task involves interacting with web pages or conducting web searches, start with the ‘browser_use_agent‘ and follow up with the ‘deep_researcher_agent‘.
- Firstly, please use ‘browser_use_agent‘ to search and interact with the most relevant web pages to find the answer. If the answer is found, please output the answer directly.
- Secondly, if the answer is not found, please use ‘deep_researcher_agent‘ to perform extensive web searches to find the answer. * If the task involves analyzing an ATTACHED FILE, a URL, performing CALCULATIONS, or playing GAME, please use ‘deep_analyzer_agent‘. * Run verification steps if that’s needed, you must make sure you find the correct answer! Here is the task: {{task}} User Prompt You should think step by step and provide a detailed plan for the task.

This prompt guides the Deep Researcher Agent to conduct thorough web searches to answer the assigned task. The agent can utilize specialized tools for web and archive searches, extracting key insights from relevant sources and providing structured, stepwise reasoning to arrive at an accurate answer.

Deep Researcher Agent Description A deep researcher agent that can conduct extensive web searches. Task Instruction You can search for the most relevant web pages and interact with them to accurately find answers to tasks. * Please use ‘deep_researcher‘ tool to search the web and the find the answer. * You can also use the ‘archive_searcher‘ tool to use Wayback Machine to find the archived version of the url and extract the key insights from it. Here is the task:
{{task}} User Prompt You should think step by step to solve the task.

The Browser Use Agent is prompted to interact directly with web pages, employing browser automation tools to search for and extract relevant content. The agent is encouraged to leverage both browser interaction and code execution capabilities to support its reasoning, ensuring no relevant information is overlooked.

Browser Use Agent Description A browser use agent that can search relevant web pages and interact with them. Task Instruction You can search for the most relevant web pages and interact with them to accurately find answers to tasks. * Please use ‘auto_browser_use‘ tool to search the web and interact with them to find the answer. When you require to use it, please provide the original task as the ‘task‘ parameter for the tool. DO NOT modify the task. - When you need to extract the content from the web page, do not ignore the content in the web screen shot. * You can also use the ‘python_interpreter‘ tool to run any code to support your analysis. Here is the task:
{{task}} User Prompt You should think step by step to solve the task.

This prompt enables the Deep Analyzer Agent to systematically analyze tasks involving attached files or URLs. The agent is instructed to employ specialized analysis tools and, if necessary, execute code for data processing and computation, delivering detailed reasoning and well-justified answers.

Deep Analyzer Agent Description A deep analyzer agent that can perform systematic, step-by-step analysis. Task Instruction You can analyze and solve any task based on attached file or uri. * Please use ‘deep_analyzer‘ tool to analyze and solve the task, and provide detailed reasoning and an answer. When you require to use it, please provide the original task as the ‘task‘ parameter for the tool. DO NOT modify the task. * When the task involves calculation and statistics for attached files or data, you can use the ‘python_interpreter‘ to run code to convert the data into a table at first. And then run the code to analyze the data. Here is the task:
{{task}} User Prompt You should think step by step to solve the task.

C.2 Tool Pseudocodes

The following pseudocode defines the internal workflow of the PlanningTool, a core component responsible for managing high-level task planning within the agent system. It supports a variety of planning operations, including creation, updating, progress marking, and deletion of task plans. It accepts an action and associated parameters, ensuring structured tracking and coordination of multi-step task plans.

Input: Action action , parameters ( plan_id , title , …)

Output: Result or status message

Function PlanningToolForward( action, plan_id, title, steps, step_index, step_status, step_notes ) :

if action == “create” then

CreatePlan( plan_id, title, steps ) ;

else if action == “update” then

UpdatePlan( plan_id, title, steps ) ;

else if action == “mark” then

Mark( plan_id, step_index, step_status, step_notes ) ;

else if action == “delete” then

DeletePlan( plan_id ) ;

else

return Error;

Function CreatePlan( plan_id, title, steps ) :

Initialize plan and store in plans;

Function UpdatePlan( plan_id, title, steps ) :

Update plan’s title or steps;

Function Mark( plan_id, step_index, step_status, step_notes ) :

Update the step’s status and notes;

Function DeletePlan( plan_id ) :

Remove plan from plans;

Algorithm 1 Pseudocode of PlanningTool

The DeepResearcherTool pseudocode describes an iterative research process. The tool searches the web for relevant results, extracts new insights in each iteration, and summarizes findings into a structured research output to support comprehensive task resolution.

Input: Research query q 𝑞 q italic_q

Output: Structured research summary

Function DeepResearchForward( q 𝑞 q italic_q ) :

i ⁢ n ⁢ s ⁢ i ⁢ g ⁢ h ⁢ t ⁢ s ← [ ] ← 𝑖 𝑛 𝑠 𝑖 𝑔 ℎ 𝑡 𝑠 insights\leftarrow[~{}] italic_i italic_n italic_s italic_i italic_g italic_h italic_t italic_s ← [ ] ;

for i = 1 𝑖 1 i=1 italic_i = 1 to max_depth do

r ⁢ e ⁢ s ⁢ u ⁢ l ⁢ t ⁢ s ← ← 𝑟 𝑒 𝑠 𝑢 𝑙 𝑡 𝑠 absent results\leftarrow italic_r italic_e italic_s italic_u italic_l italic_t italic_s ← SearchWeb( q 𝑞 q italic_q ) ;

n ⁢ e ⁢ w ⁢ _ ⁢ i ⁢ n ⁢ s ⁢ i ⁢ g ⁢ h ⁢ t ⁢ s ← ← 𝑛 𝑒 𝑤 _ 𝑖 𝑛 𝑠 𝑖 𝑔 ℎ 𝑡 𝑠 absent new\_insights\leftarrow italic_n italic_e italic_w _ italic_i italic_n italic_s italic_i italic_g italic_h italic_t italic_s ← ExtractInsights( r ⁢ e ⁢ s ⁢ u ⁢ l ⁢ t ⁢ s 𝑟 𝑒 𝑠 𝑢 𝑙 𝑡 𝑠 results italic_r italic_e italic_s italic_u italic_l italic_t italic_s ) ;

Add n ⁢ e ⁢ w ⁢ _ ⁢ i ⁢ n ⁢ s ⁢ i ⁢ g ⁢ h ⁢ t ⁢ s 𝑛 𝑒 𝑤 _ 𝑖 𝑛 𝑠 𝑖 𝑔 ℎ 𝑡 𝑠 new\_insights italic_n italic_e italic_w _ italic_i italic_n italic_s italic_i italic_g italic_h italic_t italic_s to i ⁢ n ⁢ s ⁢ i ⁢ g ⁢ h ⁢ t ⁢ s 𝑖 𝑛 𝑠 𝑖 𝑔 ℎ 𝑡 𝑠 insights italic_i italic_n italic_s italic_i italic_g italic_h italic_t italic_s ;

s ⁢ u ⁢ m ⁢ m ⁢ a ⁢ r ⁢ y ← ← 𝑠 𝑢 𝑚 𝑚 𝑎 𝑟 𝑦 absent summary\leftarrow italic_s italic_u italic_m italic_m italic_a italic_r italic_y ← Summarize( i ⁢ n ⁢ s ⁢ i ⁢ g ⁢ h ⁢ t ⁢ s 𝑖 𝑛 𝑠 𝑖 𝑔 ℎ 𝑡 𝑠 insights italic_i italic_n italic_s italic_i italic_g italic_h italic_t italic_s ) ;

return s ⁢ u ⁢ m ⁢ m ⁢ a ⁢ r ⁢ y 𝑠 𝑢 𝑚 𝑚 𝑎 𝑟 𝑦 summary italic_s italic_u italic_m italic_m italic_a italic_r italic_y ;

Function SearchWeb( q 𝑞 q italic_q ) :

Return web results for q 𝑞 q italic_q ;

Function ExtractInsights( r ⁢ e ⁢ s ⁢ u ⁢ l ⁢ t ⁢ s 𝑟 𝑒 𝑠 𝑢 𝑙 𝑡 𝑠 results italic_r italic_e italic_s italic_u italic_l italic_t italic_s ) :

Return key insights from r ⁢ e ⁢ s ⁢ u ⁢ l ⁢ t ⁢ s 𝑟 𝑒 𝑠 𝑢 𝑙 𝑡 𝑠 results italic_r italic_e italic_s italic_u italic_l italic_t italic_s ;

Function Summarize( i ⁢ n ⁢ s ⁢ i ⁢ g ⁢ h ⁢ t ⁢ s 𝑖 𝑛 𝑠 𝑖 𝑔 ℎ 𝑡 𝑠 insights italic_i italic_n italic_s italic_i italic_g italic_h italic_t italic_s ) :

Return structured summary of insights;

Algorithm 2 Pseudocode of DeepResearcherTool

This pseudocode specifies the operation of an automated browser tool. It supports a wide range of web interaction actions, such as searching, navigation, clicking, inputting, scrolling, content extraction, and multi-tab management, enabling agents to automate complex browser workflows.

Input: Action action , parameters ( query , url , element , …)

Output: Result or page state

Function AutoBrowserUseForward( action, params ) :

if action == “search” then

Search( params.query ) ;

else if action == “go_to_url” then

GoToUrl( params.url ) ;

else if action == “find_archive_url” then

FindArchiveUrl( params.url, params.date ) ;

else if action == “click” then

Click( params.element ) ;

else if action == “go_back” then

GoBack( ) ;

else if action == “input” then

InputText( params.element, params.text ) ;

else if action == “pdf_viewer” then

PdfViewer( params ) ;

else if action == “video_viewer” then

VideoViewer( params ) ;

else if action == “scroll” then

Scroll( params.amount ) ;

else if action == “extract_content” then

ExtractContent( params.goal ) ;

else if action == “open_tab” then

OpenTab( params.url ) ;

else if action == “switch_tab” then

SwitchTab( params.tab_id ) ;

else if action == “close_tab” then

CloseTab( params.tab_id ) ;

else

return Error;

Function Search( query ) :

Search the web with the query.

Function GoToUrl( url ) :

Navigate to the given URL.

Function FindArchiveUrl( url, date ) :

Find the archive URL for the given URL and date.

Function Click( element ) :

Click on the specified page element.

Function GoBack( ) :

Go back to the previous page.

Function InputText( element, text ) :

Input text into the specified field.

Function PdfViewer( params ) :

Interact with the PDF (e.g., scroll, jump, search, etc.).

Function VideoViewer( params ) :

Interact with the video (e.g., play, pause, seek, etc.).

Function Scroll( amount ) :

Scroll the page by the specified amount.

Function ExtractContent( goal ) :

Extract content from the page for the given goal.

Function OpenTab( url ) :

Open a new tab with the specified URL.

Function SwitchTab( tab_id ) :

Switch to the tab with the given ID.

Function CloseTab( tab_id ) :

Close the tab with the given ID.

Algorithm 3 Pseudocode of AutoBrowserUseTool

The DeepAnalyzerTool pseudocode outlines a systematic analysis process that can handle both tasks and external sources. It distributes the analysis across multiple models, integrates their outputs, and summarizes the results to deliver a comprehensive answer or report.

Input: Task description task (optional), source file or uri source (optional)

Output: Final comprehensive analysis and summary

Function DeepAnalyzerForward( task, source ) :

if task == None and source == None then

return Error ("At least one of task or source must be provided");

foreach model ∈ \in ∈ analyzer_models do

analysis[model] ← ← \leftarrow ← Analyze( model, task, source ) ;

summary ← ← \leftarrow ← Summarize( summary_model, analysis ) ;

return Formatted output of analysis and summary;

Function Analyze( model, task, source ) :

if task is None then

task ← ← \leftarrow ← "Please write a detailed caption for the attached file or uri.";

if source is image then

Append image to input;

else if source is file then

Extract file content and append to input;

Send input to model and return response;

Function Summarize( summary_model, analysis ) :

Format step-by-step comparison and summary prompt with all model outputs;

Send to summary_model and return final summary;

Algorithm 4 Pseudocode of DeepAnalyzerTool
