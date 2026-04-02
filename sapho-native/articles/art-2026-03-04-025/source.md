---
version: source-capture.v1
article_id: art-2026-03-04-025
ticket_id: ticket-import-art-2026-03-04-025
source_url: https://arxiv.org/abs/2507.13334
canonical_url: https://arxiv.org/abs/2507.13334
source_title: A Survey of Context Engineering for Large Language Models
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-30T18:03:09Z'
linked_paper_urls: []
---
# Source Capture

## Title

A Survey of Context Engineering for Large Language Models

## Body

A Survey of Context Engineering for Large Language Models

Lingrui Mei 1,6,† Jiayu Yao 1,6,† Yuyao Ge 1,6,† Yiwei Wang 2 Baolong Bi 1,6,† Yujun Cai 3 Jiazhi Liu 1 Mingyu Li 1 Zhong-Zhi Li 6 Duzhen Zhang 6 Chenlin Zhou 4 Jiayi Mao 5 Tianze Xia 6 Jiafeng Guo 1,6,† Shenghua Liu 1 , 6 , † , = 1 6 † = {}^{1,6,{\dagger},\leavevmode{\mbox{=\hskip 0.0pt plus 0.70004pt}}} start_FLOATSUPERSCRIPT 1 , 6 , † , = end_FLOATSUPERSCRIPT 1 Institute of Computing Technology, Chinese Academy of Sciences, 2 University of California, Merced, 3 The University of Queensland 4 Peking University, 5 Tsinghua University, 6 University of Chinese Academy of Sciences

Abstract

Abstract: The performance of Large Language Models (LLMs) is fundamentally determined by the contextual information provided during inference. This survey introduces Context Engineering , a formal discipline that transcends simple prompt design to encompass the systematic optimization of information payloads for LLMs. We present a comprehensive taxonomy decomposing Context Engineering into its foundational Components and the sophisticated Implementations that integrate them into intelligent systems.
We first examine the foundational Components : (1) Context Retrieval and Generation , encompassing prompt-based generation and external knowledge acquisition; (2) Context Processing , addressing long sequence processing, self-refinement, and structured information integration; and (3) Context Management , covering memory hierarchies, compression, and optimization. We then explore how these components are architecturally integrated to create sophisticated System Implementations : (1) Retrieval-Augmented Generation (RAG) , including modular, agentic, and graph-enhanced architectures; (2) Memory Systems , enabling persistent interactions; (3) Tool-Integrated Reasoning , for function calling and environmental interaction; and (4) Multi-Agent Systems , coordinating communication and orchestration.
Through this systematic analysis of over 1400 research papers, our survey not only establishes a technical roadmap for the field but also reveals a critical research gap: a fundamental asymmetry exists between model capabilities. While current models, augmented by advanced context engineering, demonstrate remarkable proficiency in understanding complex contexts, they exhibit pronounced limitations in generating equally sophisticated, long-form outputs. Addressing this gap is a defining priority for future research. Ultimately, this survey provides a unified framework for both researchers and engineers advancing context-aware AI.

† Also affiliated with: (1)Key Laboratory of Network Data Science and Technology,
ICT, CAS; (2)State Key Laboratory of AI Safety

= = {}^{\leavevmode{\mbox{=\hskip 0.0pt plus 0.70004pt}}} start_FLOATSUPERSCRIPT = end_FLOATSUPERSCRIPT Corresponding Author

Keywords : Context Engineering, Large Language Models, LLM Agent, Multi-Agent Systems

= Date : July 17, 2025

Code Repository : https://github.com/Meirtz/Awesome-Context-Engineering

= Contact : meilingrui23b@ict.ac.cn , liushenghua@ict.ac.cn

Contents

- 1 Introduction

- 2 Related Work

- 3 Why Context Engineering?

- 3.1 Definition of Context Engineering

- 3.2 Why Context Engineering

- 3.2.1 Current Limitations

- 3.2.2 Performance Enhancement

- 3.2.3 Resource Optimization

- 3.2.4 Future Potential

- 4 Foundational Components

- 4.1 Context Retrieval and Generation

- 4.1.1 Prompt Engineering and Context Generation

- 4.1.2 External Knowledge Retrieval

- 4.1.3 Dynamic Context Assembly

- 4.2 Context Processing

- 4.2.1 Long Context Processing

- 4.2.2 Contextual Self-Refinement and Adaptation

- 4.2.3 Multimodal Context

- 4.2.4 Relational and Structured Context

- 4.3 Context Management

- 4.3.1 Fundamental Constraints

- 4.3.2 Memory Hierarchies and Storage Architectures

- 4.3.3 Context Compression

- 4.3.4 Applications

- 5 System Implementations

- 5.1 Retrieval-Augmented Generation

- 5.1.1 Modular RAG Architectures

- 5.1.2 Agentic RAG Systems

- 5.1.3 Graph-Enhanced RAG

- 5.1.4 Applications

- 5.2 Memory Systems

- 5.2.1 Memory Architectures

- 5.2.2 Memory-Enhanced Agents

- 5.2.3 Evaluation and Challenges

- 5.3 Tool-Integrated Reasoning

- 5.3.1 Function Calling Mechanisms

- 5.3.2 Tool-Integrated Reasoning

- 5.3.3 Agent-Environment Interaction

- 5.4 Multi-Agent Systems

- 5.4.1 Communication Protocols

- 5.4.2 Orchestration Mechanisms

- 5.4.3 Coordination Strategies

- 6 Evaluation

- 6.1 Evaluation Frameworks and Methodologies

- 6.1.1 Component-Level Assessment

- 6.1.2 System-Level Integration Assessment

- 6.2 Benchmark Datasets and Evaluation Paradigms

- 6.2.1 Foundational Component Benchmarks

- 6.2.2 System Implementation Benchmarks

- 6.3 Evaluation Challenges and Emerging Paradigms

- 6.3.1 Methodological Limitations and Biases

- 6.3.2 Emerging Evaluation Paradigms

- 6.3.3 Safety and Robustness Assessment

- 7 Future Directions and Open Challenges

- 7.1 Foundational Research Challenges

- 7.1.1 Theoretical Foundations and Unified Frameworks

- 7.1.2 Scaling Laws and Computational Efficiency

- 7.1.3 Multi-Modal Integration and Representation

- 7.2 Technical Innovation Opportunities

- 7.2.1 Next-Generation Architectures

- 7.2.2 Advanced Reasoning and Planning

- 7.2.3 Complex Context Organization and Solving Graph Problems

- 7.2.4 Intelligent Context Assembly and Optimization

- 7.3 Application-Driven Research Directions

- 7.3.1 Domain Specialization and Adaptation

- 7.3.2 Large-Scale Multi-Agent Coordination

- 7.3.3 Human-AI Collaboration and Integration

- 7.4 Deployment and Societal Impact Considerations

- 7.4.1 Scalability and Production Deployment

- 7.4.2 Safety, Security, and Robustness

- 7.4.3 Ethical Considerations and Responsible Development

- 8 Conclusion

1 Introduction

The advent of LLMs has marked a paradigm shift in artificial intelligence, demonstrating unprecedented capabilities in natural language understanding, generation, and reasoning [ 103 , 1059 , 453 ] . However, the performance and efficacy of these models are fundamentally governed by the context they receive. This context—ranging from simple instructional prompts to sophisticated external knowledge bases—serves as the primary mechanism through which their behavior is steered, their knowledge is augmented, and their capabilities are unleashed. As LLMs have evolved from basic instruction-following systems into the core reasoning engines of complex applications, the methods for designing and managing their informational payloads have correspondingly evolved into the formal discipline of Context Engineering [ 25 , 1256 , 1060 ] .

The landscape of context engineering has expanded at an explosive rate, resulting in a proliferation of specialized yet fragmented research domains. We conceptualize this landscape as being composed of foundational components and their subsequent implementations . The foundational components represent the systematic pipeline of context engineering through three critical phases: Context Retrieval and Generation , encompassing prompt-based generation and external knowledge acquisition [ 25 , 591 , 48 ] ; Context Processing , involving long sequence processing, self-refinement mechanisms, and structured information integration [ 196 , 735 , 489 ] ; and Context Management , addressing memory hierarchies, compression techniques, and optimization strategies [ 1362 , 1074 , 813 ] .

These foundational components serve as the building blocks for more complex, application-oriented implementations that bridge LLMs to external realities. These systems include Advanced Retrieval-Augmented Generation (RAG) , which has evolved into modular and agentic architectures for dynamic knowledge injection [ 591 , 312 , 965 , 311 ] ; explicit Memory Systems that mimic human cognitive faculties for persistent information retention [ 1182 , 935 , 1362 ] ; and the entire ecosystem of Intelligent Agent Systems . This latter category represents the pinnacle of context engineering, where agents leverage Function Calling and Tool-Integrated Reasoning to interact with the world [ 931 , 858 , 663 ] , and rely on sophisticated Agent Communication protocols and Context Orchestration to achieve complex goals in multi-agent configurations [ 356 , 246 , 894 , 128 ] .

While each of these domains has generated substantial innovation, they are predominantly studied in isolation. This fragmented development obscures the fundamental connections between techniques and creates significant barriers for researchers seeking to understand the broader landscape and practitioners aiming to leverage these methods effectively. The field urgently requires a unified framework that systematically organizes these diverse techniques, clarifies their underlying principles, and illuminates their interdependencies.

To address this critical gap, this survey provides the first comprehensive and systematic review of Context Engineering for LLMs. Our primary contribution is a novel, structured taxonomy that classifies the multifaceted techniques used to design, manage, and optimize context. This taxonomy organizes the field into coherent categories, distinguishing between foundational Components and their integration into sophisticated System Implementations . Through this framework, we: (1) provide a clear and structured overview of the state-of-the-art across each domain; (2) analyze the core mechanisms, strengths, and limitations of different approaches; and (3) identify overarching challenges and chart promising directions for future research. This work serves as both a technical roadmap for navigating the complex landscape of context engineering and a foundation for fostering deeper understanding and catalyzing future innovation.

The remainder of this paper is organized as follows. After discussing related work and formally defining Context Engineering, we first examine the Foundational Components of the field, covering Context Retrieval and Generation, Context Processing, and Context Management. We then explore their System Implementations , including Retrieval-Augmented Generation, Memory Systems, Tool-Integrated Reasoning, and Multi-Agent Systems. Finally, we discuss evaluation methodologies, future research directions, and conclude the survey. Figure 1 provides a comprehensive overview of our taxonomy, illustrating the hierarchical organization of techniques and their relationships within the Context Engineering landscape.

{forest}

forked edges,
for tree=
grow=east,
reversed=true,
anchor=base west,
parent anchor=east,
child anchor=west,
base=left,
font= ,
rectangle,
draw=hidden-black,
rounded corners,
align=left,
minimum width=4em,
edge+=darkgray, line width=1pt,
s sep=3pt,
inner xsep=2pt,
inner ysep=4pt,
line width=1.1pt,
ver/.style=rotate=90, child anchor=north, parent anchor=south, anchor=center, ,
where level=1text width=10.5em,font=,,
where level=2text width=11.5em,font=,,
where level=3text width=12em,font=,,
where level=4text width=50em,font=,,
[  Context Engineering   , ver
[       Foundational Components (§ 4 ),ver
[      Context Generation Retrieval &  (§ 4.1 )
[ e.g., Chain-of-Thought [ 1138 ] , Zero-shot CoT [ 553 ] , ToT [ 1246 ] , GoT [ 69 ] , Self-consistency [ 1114 ] , ReAct [ 1245 ] , Auto-CoT [ 1099 ] , Automatic Prompt [ 307 ] , CLEAR Framework [ 702 ] , RAG [ 591 ] , Cognitive Prompting [ 558 ] , KAPING [ 48 ] , Dynamic Assembly [ 307 ] , etc. , leaf, text width=44em]
]
[             Context Processing (§ 4.2 )
[ e.g., Mamba [ 1258 ] , LongNet [ 216 ] , FlashAttention [ 196 ] , Ring Attention [ 676 ] , YaRN [ 833 ] , Infini-attention [ 792 ] , StreamingLLM [ 1176 ] , InfLLM [ 1175 ] , Self-Refine [ 735 ] , Reflexion [ 956 ] , StructGPT [ 489 ] , GraphFormers [ 1221 ] , KG Integration [ 1321 ] , Long CoT [ 147 ] , MLLMs [ 49 ] , etc. , leaf, text width=44em]
]
[             Context Management (§ 4.3 )
[ e.g., Context Compression [ 317 ] , StreamingLLM [ 1176 ] , KV Cache Management [ 1389 ] , Heavy Hitter Oracle [ 1333 ] , Hierarchical Memory [ 499 ] , Recurrent Context Compression [ 441 ] , Activation Refilling [ 859 ] , Context Window Management [ 1074 ] , etc. , leaf, text width=44em]
]
]
[  Implementations  (§ 5 ), ver
[    Retrieval-Augmented Generation (§ 5.1 )
[ e.g., FlashRAG [ 500 ] , KRAGEN [ 749 ] , ComposeRAG [ 1159 ] , Self-RAG [ 41 ] , CDF-RAG [ 531 ] , GraphRAG [ 374 ] , LightRAG [ 360 ] , HippoRAG [ 366 ] , RAPTOR [ 928 ] , RAG-Gym [ 1183 ] , Agentic RAG Systems [ 965 ] , Graph-Enhanced RAG [ 832 ] , Modular RAG Architectures [ 312 ] , etc. , leaf3, text width=44em]
]
[             Memory Systems (§ 5.2 )
[ e.g., MemoryBank [ 1362 ] , MemLLM [ 779 ] , Self-Controlled Memory [ 649 ] , REMEMBERER [ 1299 ] , MemOS [ 637 ] , Charlie Mnemonic [ 578 ] , RecMind [ 1115 ] , Sandbox [ 455 ] , LongMemEval [ 1171 ] , MADail-Bench [ 386 ] , MEMENTO [ 566 ] , A-MEM [ 1202 ] , CAMELoT [ 393 ] , Architectures [ 1182 ] , Short-term & Long-term Memory [ 935 ] , MemGPT [ 813 ] , Memory-Enhanced Agents [ 571 ] , etc. , leaf3, text width=44em]
]
[       Tool-Integrated Reasoning (§ 5.3 )
[ e.g., Toolformer [ 931 ] , ReAct [ 1245 ] , Gorilla [ 828 ] , ToolLLM [ 867 ] , Granite-FunctionCalling [ 5 ] , Program-Aided Language Models [ 305 ] , ToRA [ 341 ] , ReTool [ 270 ] , Chameleon [ 709 ] , a1 [ 760 ] , API-Bank [ 615 ] , MCP-RADAR [ 310 ] , GTA benchmark [ 1090 ] , PLAY2PROMPT [ 259 ] , etc. , leaf3, text width=44em]
]
[          Multi-Agent Systems (§ 5.4 )
[ e.g., KQML [ 280 ] , FIPA ACL [ 1146 ] , MCP protocols [ 37 ] , A2A [ 1007 ] , ACP [ 462 ] , ANP [ 1 ] , AutoGen [ 1158 ] , MetaGPT [ 408 ] , CAMEL [ 600 ] , CrewAI [ 184 ] , Swarm Agent [ 808 ] , 3S orchestrator [ 893 ] , SagaLLM [ 128 ] , Communication Protocols [ 1210 ] , Orchestration [ 894 ] , Coordination Strategies [ 625 ] , Agent Communication Languages [ 356 ] , CoA [ 1327 ] , etc. , leaf3, text width=44em]
]
]
[     Evaluation  (§ 6 ), ver
[          Evaluation Frameworks (§ 6.1 )
[ e.g., Component-Level Assessment [ 835 ] , System-Level Integration [ 1132 ] , Self-Refinement [ 735 ] , MCP-RADAR [ 310 ] , LongMemEval [ 1171 ] , BFCL Tool Evaluation [ 829 ] , SagaLLM [ 128 ] , Brittleness Assessment [ 1259 ] , Contextual Calibration [ 380 ] , Multi-dimensional Feedback [ 284 ] , etc. , leaf5, text width=44em]
]
[          Benchmark Datasets (§ 6.2 )
[ e.g., GAIA [ 772 ] , GTA [ 1090 ] , WebArena [ 1368 ] , VideoWebArena [ 476 ] , Deep Research Bench [ 87 ] , StableToolBench [ 359 ] , NesTools [ 373 ] , ToolHop [ 1255 ] , T-Eval [ 157 ] , BFCL [ 829 ] , NarrativeQA [ 550 ] , MEMENTO [ 566 ] , API-Bank [ 615 ] , Mind2Web [ 202 ] , SWE-Bench [ 494 ] , etc. , leaf5, text width=44em]
]
[          Evaluation Challenges (§ 6.3 )
[ e.g., Performance Gap Assessment [ 772 , 1090 ] , Memory System Isolation Problems [ 1330 , 1171 ] , O(n²) Scaling Limitations [ 731 , 295 ] , Transactional Integrity [ 128 ] , Multi-Tool Coordination [ 310 ] , Self-Validation Dependencies [ 390 ] , Context Handling Failures [ 210 ] , Attribution Challenges [ 1113 ] , Safety-oriented Evaluation [ 87 ] , Agent Assessment [ 965 ] , Orchestration Evaluation [ 893 ] , etc. , leaf5, text width=44em]
]
]
[    Future Directions & Challenges (§ 7 ), ver
[         Foundational Research (§ 7.1 )
[ e.g., Theoretical Foundations [ 1132 ] , Scaling Laws [ 731 ] , O(n²) Computational Challenges [ 295 ] , Multi-modal Integration [ 476 ] , Compositional Understanding [ 835 ] , Context Optimization [ 663 ] , Frameworks for Multi-agent Coordination [ 128 ] , Information-theoretic Analysis [ 310 ] , etc. , leaf2, text width=44em]
]
[           Technical Innovation (§ 7.2 )
[ e.g., LongMamba [ 1258 ] , Sliding Attention [ 295 ] , Memory-Augmented Architectures [ 1362 ] , Modular RAG [ 312 ] , GraphRAG [ 374 ] , Context Assembly Optimization [ 1132 ] , Tool-Integrated Reasoning [ 310 ] , Agentic Systems [ 965 ] ,Self-Refinement Mechanisms [ 735 ] , etc. , leaf2, text width=44em]
]
[      Application-Driven Research (§ 7.3 )
[ e.g., Domain Specialization [ 87 ] , Healthcare Applications [ 386 ] , Protocol Standardization [ 246 ] , MCP/A2A/ACP/ANP Protocols [ 616 ] , Human-AI Collaboration [ 1368 ] , Security Issues [ 926 ] , Production Deployment Scalability [ 1227 ] , Safety [ 965 ] and Ethical Considerations [ 835 ] , etc. , leaf2, text width=44em]
]
]
]

Figure 1 : The taxonomy of Context Engineering in Large Language Models is categorized into foundational components, system implementations, evaluation methodologies, and future directions. Each area encompasses specific techniques and frameworks that collectively advance the systematic optimization of information payloads for LLMs.

2 Related Work

The rapid maturation of LLMs has spurred a significant body of survey literature aiming to map its multifaceted landscape. This existing work, while valuable, has largely focused on specific vertical domains within the broader field of what we define as Context Engineering. Our survey seeks to complement these efforts by providing a horizontal, unifying taxonomy that distinguishes between foundational components and their integration into complex systems, thereby bridging these specialized areas.

Foundational Components

Numerous surveys have addressed the foundational Components of context engineering that form the core technical capabilities for effective context manipulation. The challenge of Context Retrieval and Generation encompasses both prompt engineering methodologies and external knowledge acquisition techniques. Surveys on prompt engineering have cataloged the vast array of techniques for guiding LLM behavior, from basic few-shot methods to advanced, structured reasoning frameworks [ 25 , 253 , 1313 ] . External knowledge retrieval and integration techniques, particularly through knowledge graphs and structured data sources, are reviewed in works that survey representation techniques, integration paradigms, and applications in enhancing the factual grounding of LLMs [ 483 , 428 , 817 , 889 ] .

The domain of Context Processing addresses the technical challenges of handling long sequences, self-refinement mechanisms, and structured information integration. Long context processing is addressed in surveys analyzing techniques for extending context windows, optimizing attention mechanisms, and managing memory efficiently [ 831 , 645 , 1289 , 268 ] . The internal cognitive processes of LLMs are increasingly surveyed, with works on self-contextualizing techniques and self-improvement paradigms gaining prominence [ 1329 , 227 , 1167 , 935 ] .

Finally, Context Management literature focuses on memory hierarchies, compression techniques, and optimization strategies that enable effective information organization and retrieval within computational constraints. While comprehensive surveys specifically dedicated to context management as a unified domain remain limited, related work on memory systems and context compression techniques provides foundational insights into these critical capabilities.

System Implementation

In parallel, the literature has extensively covered the System Implementations that integrate foundational components into sophisticated architectures addressing real-world application requirements. The domain of RAG has received substantial attention, with foundational surveys tracing its development and impact on mitigating hallucinations [ 311 , 253 , 1131 ] . More recent work has surveyed the evolution towards modular, agentic, and graph-enhanced RAG architectures [ 162 , 622 , 120 , 312 , 1391 ] .

Memory Systems that enable persistent interactions and cognitive architectures have been explored through surveys focusing on memory-enhanced agents and their applications. The broader category of LLM-based Agents serves as a foundational area, with comprehensive overviews of autonomous agents, their architecture, planning, and methodologies [ 1091 , 719 , 277 , 843 , 1340 , 498 , 1272 ] .

Tool-Integrated Reasoning encompassing function calling mechanisms and agent-environment interaction are well-documented, exploring the evolution from single-tool systems to complex orchestration frameworks [ 663 , 858 , 771 , 867 ] . The evolution towards Multi-Agent Systems (MAS) represents another focal point, with surveys detailing MAS workflows, infrastructure, communication protocols, and coordination mechanisms [ 625 , 356 , 246 , 1235 , 38 , 503 , 187 , 458 ] .

Evaluation

The critical aspect of evaluating these complex systems has been thoroughly reviewed, with works analyzing benchmarks and methodologies for assessing component-level and system-level capabilities and performance [ 1259 , 380 , 835 , 310 ] . This evaluation literature spans both foundational component assessment and integrated system evaluation paradigms.

Our Contribution

While these surveys provide indispensable, in-depth analyses of their respective domains, they inherently present a fragmented view of the field. The connections between RAG as a form of external memory, tool use as a method for context acquisition, and prompt engineering as the language for orchestrating these components are often left implicit. Our work distinguishes itself by proposing Context Engineering as a unifying abstraction that explicitly separates foundational components from their integration in complex implementations. By organizing these disparate fields into a single, coherent taxonomy, this survey aims to elucidate the fundamental relationships between them, providing a holistic map of how context is generated, processed, managed, and utilized to steer the next generation of intelligent systems.

Figure 2 : Context Engineering Evolution Timeline: A comprehensive visualization of the development trajectory of Context Engineering implementations from 2020 to 2025, showing the evolution from foundational RAG systems to sophisticated multi-agent architectures and tool-integrated reasoning systems.

3 Why Context Engineering?

As Large Language Models (LLMs) evolve from simple instruction-following systems into the core reasoning engines of complex, multi-faceted applications, the methods used to interact with them must also evolve. The term “prompt engineering,” while foundational, is no longer sufficient to capture the full scope of designing, managing, and optimizing the information payloads required by modern AI systems. These systems do not operate on a single, static string of text; they leverage a dynamic, structured, and multifaceted information stream. To address this, we introduce and formalize the discipline of Context Engineering .

3.1 Definition of Context Engineering

To formally define Context Engineering, we begin with the standard probabilistic model of an autoregressive LLM. The model, parameterized by θ 𝜃 \theta italic_θ , generates an output sequence Y = ( y 1 , … , y T ) 𝑌 subscript 𝑦 1 … subscript 𝑦 𝑇 Y=(y_{1},\dots,y_{T}) italic_Y = ( italic_y start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_y start_POSTSUBSCRIPT italic_T end_POSTSUBSCRIPT ) given an input context C 𝐶 C italic_C by maximizing the conditional probability:

P θ ⁢ ( Y | C ) = ∏ t = 1 T P θ ⁢ ( y t | y < t , C ) subscript 𝑃 𝜃 conditional 𝑌 𝐶 superscript subscript product 𝑡 1 𝑇 subscript 𝑃 𝜃 conditional subscript 𝑦 𝑡 subscript 𝑦 absent 𝑡 𝐶 P_{\theta}(Y|C)=\prod_{t=1}^{T}P_{\theta}(y_{t}|y_{<t},C) italic_P start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT ( italic_Y | italic_C ) = ∏ start_POSTSUBSCRIPT italic_t = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_T end_POSTSUPERSCRIPT italic_P start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT ( italic_y start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT | italic_y start_POSTSUBSCRIPT < italic_t end_POSTSUBSCRIPT , italic_C ) (1)

Historically, in the paradigm of prompt engineering, the context C 𝐶 C italic_C was treated as a monolithic, static string of text, i.e., C = prompt 𝐶 prompt C=\text{prompt} italic_C = prompt . This view is insufficient for modern systems.

Context Engineering re-conceptualizes the context C 𝐶 C italic_C as a dynamically structured set of informational components, c 1 , c 2 , … , c n subscript 𝑐 1 subscript 𝑐 2 … subscript 𝑐 𝑛 c_{1},c_{2},\dots,c_{n} italic_c start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_c start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_c start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT . These components are sourced, filtered, and formatted by a set of functions, and finally orchestrated by a high-level assembly function, 𝒜 𝒜 \mathcal{A} caligraphic_A :

C = 𝒜 ⁢ ( c 1 , c 2 , … , c n ) 𝐶 𝒜 subscript 𝑐 1 subscript 𝑐 2 … subscript 𝑐 𝑛 C=\mathcal{A}(c_{1},c_{2},\dots,c_{n}) italic_C = caligraphic_A ( italic_c start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_c start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_c start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) (2)

The components c i subscript 𝑐 𝑖 c_{i} italic_c start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT are not arbitrary; they map directly to the core technical domains of this survey:

- •

c instr subscript 𝑐 instr c_{\text{instr}} italic_c start_POSTSUBSCRIPT instr end_POSTSUBSCRIPT : System instructions and rules ( Context Retrieval and Generation , Sec. 4.1 ).

- •

c know subscript 𝑐 know c_{\text{know}} italic_c start_POSTSUBSCRIPT know end_POSTSUBSCRIPT : External knowledge, retrieved via functions like RAG or from integrated knowledge graphs ( RAG , Sec. 5.1 ; Context Processing , Sec. 4.2 ).

- •

c tools subscript 𝑐 tools c_{\text{tools}} italic_c start_POSTSUBSCRIPT tools end_POSTSUBSCRIPT : Definitions and signatures of available external tools ( Function Calling & Tool-Integrated Reasoning , Sec. 5.3 ).

- •

c mem subscript 𝑐 mem c_{\text{mem}} italic_c start_POSTSUBSCRIPT mem end_POSTSUBSCRIPT : Persistent information from prior interactions ( Memory Systems , Sec. 5.2 ; Context Management , Sec. 4.3 ).

- •

c state subscript 𝑐 state c_{\text{state}} italic_c start_POSTSUBSCRIPT state end_POSTSUBSCRIPT : The dynamic state of the user, world, or multi-agent system ( Multi-Agent Systems & Orchestration , Sec. 5.4 ).

- •

c query subscript 𝑐 query c_{\text{query}} italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT : The user’s immediate request.

The Optimization Problem of Context Engineering.

From this perspective, Context Engineering is the formal optimization problem of finding the ideal set of context-generating functions (which we denote collectively as ℱ = { 𝒜 , Retrieve , Select , … } ℱ 𝒜 Retrieve Select … \mathcal{F}=\{\mathcal{A},\text{Retrieve},\text{Select},\dots\} caligraphic_F = { caligraphic_A , Retrieve , Select , … } ) that maximizes the expected quality of the LLM’s output. Given a distribution of tasks 𝒯 𝒯 \mathcal{T} caligraphic_T , the objective is:

ℱ ∗ = arg ⁡ max ℱ ⁡ 𝔼 τ ∼ 𝒯 ⁢ [ Reward ⁢ ( P θ ⁢ ( Y | C ℱ ⁢ ( τ ) ) , Y τ ∗ ) ] superscript ℱ subscript ℱ subscript 𝔼 similar-to 𝜏 𝒯 delimited-[] Reward subscript 𝑃 𝜃 conditional 𝑌 subscript 𝐶 ℱ 𝜏 subscript superscript 𝑌 𝜏 \mathcal{F}^{*}=\arg\max_{\mathcal{F}}\mathbb{E}_{\tau\sim\mathcal{T}}[\text{%
Reward}(P_{\theta}(Y|C_{\mathcal{F}}(\tau)),Y^{*}_{\tau})] caligraphic_F start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT = roman_arg roman_max start_POSTSUBSCRIPT caligraphic_F end_POSTSUBSCRIPT blackboard_E start_POSTSUBSCRIPT italic_τ ∼ caligraphic_T end_POSTSUBSCRIPT [ Reward ( italic_P start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT ( italic_Y | italic_C start_POSTSUBSCRIPT caligraphic_F end_POSTSUBSCRIPT ( italic_τ ) ) , italic_Y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_τ end_POSTSUBSCRIPT ) ] (3)

where τ 𝜏 \tau italic_τ is a specific task instance, C ℱ ⁢ ( τ ) subscript 𝐶 ℱ 𝜏 C_{\mathcal{F}}(\tau) italic_C start_POSTSUBSCRIPT caligraphic_F end_POSTSUBSCRIPT ( italic_τ ) is the context generated by the functions in ℱ ℱ \mathcal{F} caligraphic_F for that task, and Y τ ∗ subscript superscript 𝑌 𝜏 Y^{*}_{\tau} italic_Y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_τ end_POSTSUBSCRIPT is the ground-truth or ideal output. This optimization is subject to hard constraints, most notably the model’s context length limit, | C | ≤ L max 𝐶 subscript 𝐿 max |C|\leq L_{\text{max}} | italic_C | ≤ italic_L start_POSTSUBSCRIPT max end_POSTSUBSCRIPT .

Mathematical Principles and Theoretical Frameworks.

This formalization reveals deeper mathematical principles. The assembly function 𝒜 𝒜 \mathcal{A} caligraphic_A is a form of Dynamic Context Orchestration , a pipeline of formatting and concatenation operations, 𝒜 = Concat ∘ ( Format 1 , … , Format n ) 𝒜 Concat subscript Format 1 … subscript Format 𝑛 \mathcal{A}=\text{Concat}\circ(\text{Format}_{1},\dots,\text{Format}_{n}) caligraphic_A = Concat ∘ ( Format start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , Format start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) , where each function must be optimized for the LLM’s architectural biases (e.g., attention patterns).

The retrieval of knowledge, c know = Retrieve ⁢ ( … ) subscript 𝑐 know Retrieve … c_{\text{know}}=\text{Retrieve}(\dots) italic_c start_POSTSUBSCRIPT know end_POSTSUBSCRIPT = Retrieve ( … ) , can be framed as an Information-Theoretic Optimality problem. The goal is to select knowledge that maximizes the mutual information with the target answer Y ∗ superscript 𝑌 Y^{*} italic_Y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT , given the query c query subscript 𝑐 query c_{\text{query}} italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT :

Retrieve ∗ = arg ⁡ max Retrieve ⁡ I ⁢ ( Y ∗ ; c know | c query ) superscript Retrieve subscript Retrieve 𝐼 superscript 𝑌 conditional subscript 𝑐 know subscript 𝑐 query \text{Retrieve}^{*}=\arg\max_{\text{Retrieve}}I(Y^{*};c_{\text{know}}|c_{\text%
{query}}) Retrieve start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT = roman_arg roman_max start_POSTSUBSCRIPT Retrieve end_POSTSUBSCRIPT italic_I ( italic_Y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ; italic_c start_POSTSUBSCRIPT know end_POSTSUBSCRIPT | italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT ) (4)

This ensures that the retrieved context is not just semantically similar, but maximally informative for solving the task.

Furthermore, the entire process can be viewed through the lens of Bayesian Context Inference . Instead of deterministically constructing the context, we infer the optimal context posterior P ⁢ ( C | c query , History , World ) 𝑃 conditional 𝐶 subscript 𝑐 query History World P(C|c_{\text{query}},\text{History},\text{World}) italic_P ( italic_C | italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT , History , World ) . Using Bayes’ theorem, this posterior is proportional to the likelihood of the query given the context and the prior probability of the context’s relevance:

P ⁢ ( C | c query , … ) ∝ P ⁢ ( c query | C ) ⋅ P ⁢ ( C | History , World ) proportional-to 𝑃 conditional 𝐶 subscript 𝑐 query … ⋅ 𝑃 conditional subscript 𝑐 query 𝐶 𝑃 conditional 𝐶 History World P(C|c_{\text{query}},\dots)\propto P(c_{\text{query}}|C)\cdot P(C|\text{%
History},\text{World}) italic_P ( italic_C | italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT , … ) ∝ italic_P ( italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT | italic_C ) ⋅ italic_P ( italic_C | History , World ) (5)

The decision-theoretic objective is then to find the context C ∗ superscript 𝐶 C^{*} italic_C start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT that maximizes the expected reward over the distribution of possible answers:

C ∗ = arg ⁡ max C ⁢ ∫ P ⁢ ( Y | C , c query ) ⋅ Reward ⁢ ( Y , Y ∗ ) ⁢ 𝑑 Y ⋅ P ⁢ ( C | c query , … ) superscript 𝐶 subscript 𝐶 ⋅ ⋅ 𝑃 conditional 𝑌 𝐶 subscript 𝑐 query Reward 𝑌 superscript 𝑌 differential-d 𝑌 𝑃 conditional 𝐶 subscript 𝑐 query … C^{*}=\arg\max_{C}\int P(Y|C,c_{\text{query}})\cdot\text{Reward}(Y,Y^{*})\,dY%
\cdot P(C|c_{\text{query}},\dots) italic_C start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT = roman_arg roman_max start_POSTSUBSCRIPT italic_C end_POSTSUBSCRIPT ∫ italic_P ( italic_Y | italic_C , italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT ) ⋅ Reward ( italic_Y , italic_Y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ) italic_d italic_Y ⋅ italic_P ( italic_C | italic_c start_POSTSUBSCRIPT query end_POSTSUBSCRIPT , … ) (6)

This Bayesian formulation provides a principled way to handle uncertainty, perform adaptive retrieval by updating priors, and maintain belief states over context in multi-step reasoning tasks.

Comparison of Paradigms

The formalization of Context Engineering highlights its fundamental distinctions from traditional prompt engineering. The following table summarizes the key differences.

Dimension Prompt Engineering Context Engineering

Model C = prompt 𝐶 prompt C=\text{prompt} italic_C = prompt (static string) C = 𝒜 ⁢ ( c 1 , c 2 , … , c n ) 𝐶 𝒜 subscript 𝑐 1 subscript 𝑐 2 … subscript 𝑐 𝑛 C=\mathcal{A}(c_{1},c_{2},\dots,c_{n}) italic_C = caligraphic_A ( italic_c start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_c start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_c start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) (dynamic, structured assembly)

Target arg ⁡ max prompt ⁡ P θ ⁢ ( Y | prompt ) subscript prompt subscript 𝑃 𝜃 conditional 𝑌 prompt \arg\max_{\text{prompt}}P_{\theta}(Y|\text{prompt}) roman_arg roman_max start_POSTSUBSCRIPT prompt end_POSTSUBSCRIPT italic_P start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT ( italic_Y | prompt ) ℱ ∗ = arg ⁡ max ℱ ⁡ 𝔼 τ ∼ 𝒯 ⁢ [ Reward ⁢ ( P θ ⁢ ( Y | C ℱ ⁢ ( τ ) ) , Y τ ∗ ) ] superscript ℱ subscript ℱ subscript 𝔼 similar-to 𝜏 𝒯 delimited-[] Reward subscript 𝑃 𝜃 conditional 𝑌 subscript 𝐶 ℱ 𝜏 subscript superscript 𝑌 𝜏 \mathcal{F}^{*}=\arg\max_{\mathcal{F}}\mathbb{E}_{\tau\sim\mathcal{T}}[\text{%
Reward}(P_{\theta}(Y|C_{\mathcal{F}}(\tau)),Y^{*}_{\tau})] caligraphic_F start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT = roman_arg roman_max start_POSTSUBSCRIPT caligraphic_F end_POSTSUBSCRIPT blackboard_E start_POSTSUBSCRIPT italic_τ ∼ caligraphic_T end_POSTSUBSCRIPT [ Reward ( italic_P start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT ( italic_Y | italic_C start_POSTSUBSCRIPT caligraphic_F end_POSTSUBSCRIPT ( italic_τ ) ) , italic_Y start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_τ end_POSTSUBSCRIPT ) ]

Complexity Manual or automated search over a string space. System-level optimization of ℱ = { 𝒜 , Retrieve , Select , … } ℱ 𝒜 Retrieve Select … \mathcal{F}=\{\mathcal{A},\text{Retrieve},\text{Select},\dots\} caligraphic_F = { caligraphic_A , Retrieve , Select , … } .

Information Information content is fixed within the prompt. Aims to maximize task-relevant information under constraint | C | ≤ L max 𝐶 subscript 𝐿 max |C|\leq L_{\text{max}} | italic_C | ≤ italic_L start_POSTSUBSCRIPT max end_POSTSUBSCRIPT .

State Primarily stateless. Inherently stateful, with explicit components for c mem subscript 𝑐 mem c_{\text{mem}} italic_c start_POSTSUBSCRIPT mem end_POSTSUBSCRIPT and c state subscript 𝑐 state c_{\text{state}} italic_c start_POSTSUBSCRIPT state end_POSTSUBSCRIPT .

Scalability Brittleness increases with length and complexity. Manages complexity through modular composition.

Error Analysis Manual inspection and iterative refinement. Systematic evaluation and debugging of individual context functions.

Table 1 : Comparison of Prompt Engineering and Context Engineering Paradigms.

In summary, Context Engineering provides the formal, systematic framework required to build, understand, and optimize the sophisticated, context-aware AI systems that are coming to define the future of the field. It shifts the focus from the “art” of prompt design to the “science” of information logistics and system optimization.

Context Scaling

Context scaling encompasses two fundamental dimensions that collectively define the scope and sophistication of contextual information processing. The first dimension, length scaling , addresses the computational and architectural challenges of processing ultra-long sequences, extending context windows from thousands to millions of tokens while maintaining coherent understanding across extended narratives, documents, and interactions. This involves sophisticated attention mechanisms, memory management techniques, and architectural innovations that enable models to maintain contextual coherence over vastly extended input sequences.

The second, equally critical dimension is multi-modal and structural scaling , which expands context beyond simple text to encompass multi-dimensional, dynamic, cross-modal information structures. This includes temporal context (understanding time-dependent relationships and sequences), spatial context (interpreting location-based and geometric relationships), participant states (tracking multiple entities and their evolving conditions), intentional context (understanding goals, motivations, and implicit objectives), and cultural context (interpreting communication within specific social and cultural frameworks).

Modern context engineering must address both dimensions simultaneously, as real-world applications require models to process not only lengthy textual information but also diverse data types including structured knowledge graphs, multimodal inputs (text, images, audio, video), temporal sequences, and implicit contextual cues that humans naturally understand. This multi-dimensional approach to context scaling represents a fundamental shift from parameter scaling toward developing systems capable of understanding complex, ambiguous contexts that mirror the nuanced nature of human intelligence in facing a complex world [ 1036 ] .

3.2 Why Context Engineering

3.2.1 Current Limitations

Large Language Models face critical technical barriers necessitating sophisticated context engineering approaches. The self-attention mechanism imposes quadratic computational and memory overhead as sequence length increases, creating substantial obstacles to processing extended contexts and significantly impacting real-world applications such as chatbots and code comprehension models [ 1017 , 977 ] . Commercial deployment compounds these challenges through repeated context processing that introduces additional latency and token-based pricing costs [ 1017 ] .

Beyond computational constraints, LLMs demonstrate concerning reliability issues including frequent hallucinations, unfaithfulness to input context, problematic sensitivity to input variations, and responses that appear syntactically correct while lacking semantic depth or coherence [ 951 , 1279 , 523 ] .

The prompt engineering process presents methodological challenges through approximation-driven and subjective approaches that focus narrowly on task-specific optimization while neglecting individual LLM behavior [ 800 ] . Despite these challenges, prompt engineering remains critical for effective LLM utilization through precise and contextually rich prompts that reduce ambiguity and enhance response consistency [ 964 ] .

3.2.2 Performance Enhancement

Context engineering delivers substantial performance improvements through techniques like retrieval-augmented generation and superposition prompting, achieving documented improvements including 18-fold enhancement in text navigation accuracy, 94% success rates, and significant gains from careful prompt construction and automatic optimization across specialized domains [ 267 , 768 , 681 ] .

Structured prompting techniques, particularly chain-of-thought approaches, enable complex reasoning through intermediate steps while enhancing element-aware summarization capabilities that integrate fine-grained details from source documents [ 1138 , 750 , 1120 ] . Few-shot learning implementations through carefully selected demonstration examples yield substantial performance gains, including 9.90% improvements in BLEU-4 scores for code summarization and 175.96% in exact match metrics for bug fixing [ 306 ] .

Domain-specific context engineering proves especially valuable in specialized applications, with execution-aware debugging frameworks achieving up to 9.8% performance improvements on code generation benchmarks and hardware design applications benefiting from specialized testbench generation and security property verification [ 1360 , 873 , 44 ] . These targeted approaches bridge the gap between general-purpose model training and specialized domain requirements.

3.2.3 Resource Optimization

Context engineering provides efficient alternatives to resource-intensive traditional approaches by enabling intelligent content filtering and direct knowledge transmission through carefully crafted prompts [ 630 , 670 ] . LLMs can generate expected responses even when relevant information is deleted from input context, leveraging contextual clues and prior knowledge to optimize context length usage while maintaining response quality, particularly valuable in domains with significant data acquisition challenges [ 630 , 670 ] .

Specialized optimization techniques further enhance efficiency gains through context awareness and responsibility tuning that significantly reduce token consumption, dynamic context optimization employing precise token-level content selection, and attention steering mechanisms for long-context inference [ 426 , 944 , 350 ] . These approaches maximize information density while reducing processing overhead and maintaining performance quality [ 944 , 350 ] .

3.2.4 Future Potential

Context engineering enables flexible adaptation mechanisms through in-context learning that allows models to adapt to new tasks without explicit retraining, with context window size directly influencing available examples for task adaptation [ 617 ] . Advanced techniques integrate compression and selection mechanisms for efficient model editing while maintaining contextual coherence [ 619 ] . This adaptability proves especially valuable in low-resource scenarios, enabling effective utilization across various prompt engineering techniques including zero-shot approaches, few-shot examples, and role context without requiring domain-specific fine-tuning [ 924 , 129 , 1075 ] .

Sophisticated context engineering techniques including in-context learning, chain-of-thought, tree-of-thought, and planning approaches establish foundations for nuanced language understanding and generation capabilities while optimizing retrieval and generation processes for robust, context-aware AI applications [ 797 , 974 ] .

Future research directions indicate substantial potential for advancing context-sensitive applications through chain-of-thought augmentation with logit contrast mechanisms [ 953 ] , better leveraging different context types across domains, particularly in code intelligence tasks combining syntax, semantics, execution flow, and documentation [ 1094 ] , and understanding optimal context utilization strategies as advanced language models continue demonstrating prompt engineering’s persistent value [ 1079 ] . Evolution toward sophisticated filtering and selection mechanisms represents a critical pathway for addressing transformer architectures’ scaling limitations while maintaining performance quality.

4 Foundational Components

Context Engineering is built upon three fundamental components that collectively address the core challenges of information management in large language models: Context Retrieval and Generation sources appropriate contextual information through prompt engineering, external knowledge retrieval, and dynamic context assembly; Context Processing transforms and optimizes acquired information through long sequence processing, self-refinement mechanisms, and structured data integration; and Context Management tackles efficient organization and utilization of contextual information through addressing fundamental constraints, implementing sophisticated memory hierarchies, and developing compression techniques. These foundational components establish the theoretical and practical basis for all context engineering implementations, forming a comprehensive framework where each component addresses distinct aspects of the context engineering pipeline while maintaining synergistic relationships that enable comprehensive contextual optimization and effective context engineering strategies.

Figure 3 : Context Engineering Framework: A comprehensive taxonomy of Context Engineering components including Context Retrieval and Generation, Context Processing, and Context Management, integrated into System Implementations such as RAG systems, memory architectures, tool-integrated reasoning, and multi-agent coordination mechanisms.

4.1 Context Retrieval and Generation

Context Retrieval and Generation forms the foundational layer of context engineering, encompassing the systematic retrieval and construction of relevant information for LLMs. This component addresses the critical challenge of sourcing appropriate contextual information through three primary mechanisms: prompt-based generation that crafts effective instructions and reasoning frameworks, external knowledge retrieval that accesses dynamic information sources, and dynamic context assembly that orchestrates acquired components into coherent, task-optimized contexts.

4.1.1 Prompt Engineering and Context Generation

Prompt engineering and context generation forms the foundational layer of context retrieval, encompassing strategic input design that combines art and science to craft effective instructions for LLMs. The CLEAR Framework—conciseness, logic, explicitness, adaptability, and reflectiveness—governs effective prompt construction, while core architecture integrates task instructions, contextual information, input data, and output indicators [ 702 , 1133 , 569 , 209 , 25 ] .

Zero-Shot and Few-Shot Learning Paradigms

Zero-shot prompting enables task performance without prior examples, relying exclusively on instruction clarity and pre-trained knowledge [ 1361 , 336 , 553 , 67 , 1046 ] . Few-shot prompting extends this capability by incorporating limited exemplars to guide model responses, demonstrating task execution through strategic example selection [ 1361 , 401 , 103 , 546 , 788 , 1371 ] . In-context learning facilitates adaptation to novel tasks without parameter updates by leveraging demonstration examples within prompts, with performance significantly influenced by example selection and ordering strategies [ 365 , 103 , 1287 , 1016 , 920 , 846 , 1139 , 348 , 576 ] .

Chain-of-Thought Foundations

Chain-of-Thought (CoT) prompting decomposes complex problems into intermediate reasoning steps, mirroring human cognition [ 1138 , 401 , 336 , 939 , 603 ] . Zero-shot CoT uses trigger phrases like “Let’s think step by step,” improving MultiArith accuracy from 17.7% to 78.7% [ 553 , 1099 , 472 , 662 ] , with Automatic Prompt Engineer refinements yielding additional gains [ 1215 , 526 ] .

Tree-of-Thoughts (ToT) organizes reasoning as hierarchical structures with exploration, lookahead, and backtracking capabilities, increasing Game of 24 success rates from 4% to 74% [ 1246 , 217 , 557 , 598 ] . Graph-of-Thoughts (GoT) models reasoning as arbitrary graphs with thoughts as vertices and dependencies as edges, improving quality by 62% and reducing costs by 31% compared to ToT [ 69 , 826 , 1366 ] .

Cognitive Architecture Integration

Cognitive prompting implements structured human-like operations including goal clarification, decomposition, filtering, abstraction, and pattern recognition, enabling systematic multi-step task resolution through deterministic, self-adaptive, and hybrid variants [ 558 , 557 , 1205 , 1164 ] . Guilford’s Structure of Intellect model provides psychological foundations for categorizing cognitive operations such as pattern recognition, memory retrieval, and evaluation, enhancing reasoning clarity, coherence, and adaptability [ 556 , 191 ] . Advanced implementations incorporate cognitive tools as modular reasoning operations, with GPT-4.1 performance on AIME2024 increasing from 26.7% to 43.3% through structured cognitive operation sequences [ 243 , 1030 ] .

Method Description

Self-Refine [ 735 , 916 ] Enables LLMs to improve outputs through iterative feedback and refinement cycles using the same model as the generator, feedback provider, and refiner, without supervised training.

Multi-Aspect Feedback [ 799 ] Integrates multiple feedback modules (frozen LMs and external tools), each focusing on specific error categories to enable more comprehensive, independent evaluation.

N-CRITICS [ 789 ] Implements an ensemble of critics that evaluate an initial output. Compiled feedback from the generating LLM and other models guides refinement until a stopping criterion is met.

ISR-LLM [ 1373 ] Improves LLM-based planning by translating natural language to formal specifications, creating an initial plan, and then systematically refining it with a validator.

SELF [ 704 ] Teaches LLMs meta-skills (self-feedback, self-refinement) with limited examples, then has the model continuously self-evolve by generating and filtering its own training data.

ProMiSe [ 884 ] Addresses self-refinement in smaller LMs using principle-guided iterative refinement, combining proxy metric thresholds with few-shot refinement and rejection sampling.

A2R [ 577 ] Augments LLMs through Metric-based Iterative Feedback Learning, using explicit evaluation across multiple dimensions (e.g., correctness) to generate feedback and refine outputs.

Experience Refinement [ 857 ] Enables LLM agents to refine experiences during task execution by learning from recent (successive) or all previous (cumulative) experiences, prioritizing high-quality ones.

I-SHEEP [ 654 ] Allows LLMs to continuously self-align from scratch by generating, assessing, filtering, and training on high-quality synthetic datasets without external guidance.

CaP [ 1271 ] Uses external tools to refine chain-of-thought (CoT) responses, addressing the limitation of models that get stuck in non-correcting reasoning loops.

Agent-R [ 1277 ] Enables language agents to reflect “on the fly” through iterative self-training, using Monte Carlo Tree Search (MCTS) to construct training data that corrects erroneous paths.

GenDiE [ 610 ] Enhances context faithfulness with sentence-level optimization, combining generative and discriminative training to give LLMs self-generation and self-scoring capabilities.

Self-Developing [ 466 ] Enables LLMs to autonomously discover, implement, and refine their own improvement algorithms by generating them as code, evaluating them, and using DPO to recursively improve.

SR-NLE [ 1121 ] Improves the faithfulness of post-hoc natural language explanations via an iterative critique and refinement process using self-feedback and feature attribution.

Table 2 : Self-refinement methods in large language models and their key characteristics.

4.1.2 External Knowledge Retrieval

External knowledge retrieval represents a critical component of context retrieval, addressing fundamental limitations of parametric knowledge through dynamic access to external information sources including databases, knowledge graphs, and document collections.

Retrieval-Augmented Generation Fundamentals

RAG combines parametric knowledge stored in model parameters with non-parametric information retrieved from external sources, enabling access to current, domain-specific knowledge while maintaining parameter efficiency [ 591 , 311 , 253 ] . FlashRAG provides comprehensive evaluation and modular implementation of RAG systems, while frameworks like KRAGEN and ComposeRAG demonstrate advanced retrieval strategies with substantial performance improvements across diverse benchmarks [ 500 , 749 , 1159 ] .

Self-RAG introduces adaptive retrieval mechanisms where models dynamically decide when to retrieve information and generate special tokens to control retrieval timing and quality assessment [ 41 ] . Advanced implementations include RAPTOR for hierarchical document processing, HippoRAG for memory-inspired retrieval architectures, and Graph-Enhanced RAG systems that leverage structured knowledge representations for improved information access [ 928 , 366 , 360 ] .

Knowledge Graph Integration and Structured Retrieval

Knowledge graph integration addresses structured information retrieval through frameworks like KAPING, which retrieves relevant facts based on semantic similarities and prepends them to prompts without requiring model training [ 48 , 673 ] . KARPA provides training-free knowledge graph adaptation through pre-planning, semantic matching, and relation path reasoning, achieving state-of-the-art performance on knowledge graph question answering tasks [ 258 ] .

Think-on-Graph enables sequential reasoning over knowledge graphs to locate relevant triples, conducting exploration to retrieve related information from external databases while generating multiple reasoning pathways [ 1000 , 720 ] . StructGPT implements iterative reading-then-reasoning approaches that construct specialized functions to collect relevant evidence from structured data sources [ 489 ] .

Agentic and Modular Retrieval Systems

Agentic RAG systems treat retrieval as dynamic operations where agents function as intelligent investigators analyzing content and cross-referencing information [ 648 , 162 , 965 ] . These systems incorporate sophisticated planning and reflection mechanisms requiring integration of task decomposition, multi-plan selection, and iterative refinement capabilities [ 438 , 1183 ] .

Modular RAG architectures enable flexible composition of retrieval components through standardized interfaces and plug-and-play designs. Graph-Enhanced RAG systems leverage structured knowledge representations for improved information access, while Real-time RAG implementations address dynamic information requirements in streaming applications [ 312 , 1391 ] .

4.1.3 Dynamic Context Assembly

Dynamic context assembly represents the sophisticated orchestration of acquired information components into coherent, task-optimized contexts that maximize language model performance while respecting computational constraints.

Assembly Functions and Orchestration Mechanisms

The assembly function 𝒜 𝒜 \mathcal{A} caligraphic_A encompasses template-based formatting, priority-based selection, and adaptive composition strategies that must adapt to varying task requirements, model capabilities, and resource constraints [ 702 , 1133 , 569 ] . Contemporary orchestration mechanisms manage agent selection, context distribution, and interaction flow control in multi-agent systems, enabling effective cooperation through user input processing, contextual distribution, and optimal agent selection based on capability assessment [ 894 , 53 , 171 ] .

Advanced orchestration frameworks incorporate intent recognition, contextual memory maintenance, and task dispatching components for intelligent coordination across domain-specific agents. The Swarm Agent framework utilizes real-time outputs to direct tool invocations while addressing limitations in static tool registries and bespoke communication frameworks [ 808 , 263 , 246 ] .

Multi-Component Integration Strategies

Context assembly must address cross-modal integration challenges, incorporating diverse data types including text, structured knowledge, temporal sequences, and external tool interfaces while maintaining coherent semantic relationships [ 529 , 1221 , 496 ] . Verbalization techniques convert structured data including knowledge graph triples, table rows, and database records into natural language sentences, enabling seamless integration with existing language systems without architectural modifications [ 12 , 782 , 1064 , 13 ] .

Programming language representations of structured data, particularly Python implementations for knowledge graphs and SQL for databases, outperform traditional natural language representations in complex reasoning tasks by leveraging inherent structural properties [ 1166 ] . Multi-level structurization approaches reorganize input text into layered structures based on linguistic relationships, while structured data representations leverage existing LLMs to extract structured information and represent key elements as graphs, tables, or relational schemas [ 681 , 1125 , 1324 ] .

Automated Assembly Optimization

Automated prompt engineering addresses manual optimization limitations through systematic prompt generation and refinement algorithms. Automatic Prompt Engineer (APE) employs search algorithms for optimal prompt discovery, while LM-BFF introduces automated pipelines combining prompt-based fine-tuning with dynamic demonstration incorporation, achieving up to 30% absolute improvement across NLP tasks [ 307 , 417 , 590 ] . Promptbreeder implements self-referential evolutionary systems where LLMs improve both task-prompts and mutation-prompts governing these improvements through natural selection analogies [ 275 , 508 ] .

Self-refine enables iterative output improvement through self-critique and revision across multiple iterations, with GPT-4 achieving approximately 20% absolute performance improvement through this methodology [ 735 , 670 ] . Multi-agent collaborative frameworks simulate specialized team dynamics with agents assuming distinct roles (analysts, coders, testers), resulting in 29.9-47.1% relative improvement in Pass@1 metrics compared to single-agent approaches [ 434 , 1257 ] .

Tool integration frameworks combine Chain-of-Thought reasoning with external tool execution, automating intermediate reasoning step generation as executable programs strategically incorporating external data. LangChain provides comprehensive framework support for sequential processing chains, agent development, and web browsing capabilities, while specialized frameworks like Auto-GPT and Microsoft’s AutoGen facilitate complex AI agent development through user-friendly interfaces [ 963 , 1087 , 25 , 867 ] .

4.2 Context Processing

Context Processing focuses on transforming and optimizing acquired contextual information to maximize its utility for LLMs. This component addresses challenges in handling ultra-long sequence contexts, enables iterative self-refinement and adaptation mechanisms, and facilitates integration of multimodal, relational and structured information into coherent contextual representations.

4.2.1 Long Context Processing

Ultra-long sequence context processing addresses fundamental computational challenges arising from transformer self-attention’s O(n²) complexity, which creates significant bottlenecks as sequence lengths increase and substantially impacts real-world applications [ 1059 , 731 , 295 , 268 , 416 ] . Increasing Mistral-7B input from 4K to 128K tokens requires 122-fold computational increase, while memory constraints during prefilling and decoding stages create substantial resource demands, with Llama 3.1 8B requiring up to 16GB per 128K-token request [ 1032 , 1227 , 425 ] .

Architectural Innovations for Long Context

State Space Models (SSMs) maintain linear computational complexity and constant memory requirements through fixed-size hidden states, with models like Mamba offering efficient recurrent computation mechanisms that scale more effectively than traditional transformers [ 1258 , 347 , 346 ] . Dilated attention approaches like LongNet employ exponentially expanding attentive fields as token distance grows, achieving linear computational complexity while maintaining logarithmic dependency between tokens, enabling processing of sequences exceeding one billion tokens [ 216 ] .

Toeplitz Neural Networks (TNNs) model sequences with relative position encoded Toeplitz matrices, reducing space-time complexity to log-linear and enabling extrapolation from 512 training tokens to 14,000 inference tokens [ 868 , 869 ] . Linear attention mechanisms reduce complexity from O(N²) to O(N) by expressing self-attention as linear dot-products of kernel feature maps, achieving up to 4000× speedup when processing very long sequences [ 522 ] . Alternative approaches like non-attention LLMs break quadratic barriers by employing recursive memory transformers and other architectural innovations [ 547 ] .

Position Interpolation and Context Extension

Position interpolation techniques enable models to process sequences beyond original context window limitations by intelligently rescaling position indices rather than extrapolating to unseen positions [ 150 ] . Neural Tangent Kernel (NTK) approaches provide mathematically grounded frameworks for context extension, with YaRN combining NTK interpolation with linear interpolation and attention distribution correction [ 833 , 471 , 1021 ] .

LongRoPE achieves 2048K token context windows through two-stage approaches: first fine-tuning models to 256K length, then conducting positional interpolation to reach maximum context length [ 218 ] . Position Sequence Tuning (PoSE) demonstrates impressive sequence length extensions up to 128K tokens by combining multiple positional interpolation strategies [ 1377 ] . Self-Extend techniques enable LLMs to process long contexts without fine-tuning by employing bi-level attention strategies—grouped attention and neighbor attention—to capture dependencies among distant and adjacent tokens [ 499 ] .

Optimization Techniques for Efficient Processing

Grouped-Query Attention (GQA) partitions query heads into groups that share key and value heads, striking a balance between multi-query attention and multi-head attention while reducing memory requirements during decoding [ 16 , 1341 ] . FlashAttention exploits asymmetric GPU memory hierarchy to achieve linear memory scaling instead of quadratic requirements, with FlashAttention-2 providing approximately twice the speed through reduced non-matrix multiplication operations and optimized work distribution [ 196 , 195 ] .

Ring Attention with Blockwise Transformers enables handling extremely long sequences by distributing computation across multiple devices, leveraging blockwise computation while overlapping communication with attention computation [ 676 ] . Sparse attention techniques include Shifted sparse attention (S²-Attn) in LongLoRA and SinkLoRA with SF-Attn, which achieve 92% of full attention perplexity improvement with significant computation savings [ 1304 , 1217 ] .

Efficient Selective Attention (ESA) proposes token-level selection of critical information through query and key vector compression into lower-dimensional representations, enabling processing of sequences up to 256K tokens [ 1084 ] . BigBird combines local attention with global tokens that attend to entire sequences, plus random connections, enabling efficient processing of sequences up to 8× longer than previously possible [ 1285 ] .

Memory Management and Context Compression

Memory management strategies include Rolling Buffer Cache techniques that maintain fixed attention spans, reducing cache memory usage by approximately 8× on 32K token sequences [ 1341 ] . StreamingLLM enables processing infinitely long sequences without fine-tuning by retaining critical “attention sink” tokens together with recent KV cache entries, demonstrating up to 22.2× speedup over sliding window recomputation with sequences up to 4 million tokens [ 1176 ] .

Infini-attention incorporates compressive memory into vanilla attention, combining masked local attention with long-term linear attention in single Transformer blocks, enabling processing of infinitely long inputs with bounded memory and computation [ 792 ] . Heavy Hitter Oracle (H 2 O) presents efficient KV cache eviction policies based on observations that small token portions contribute most attention value, improving throughput by up to 29× while reducing latency by up to 1.9× [ 1333 ] .

Context compression techniques like QwenLong-CPRS implement dynamic context optimization mechanisms enabling multi-granularity compression guided by natural language instructions [ 944 ] . InfLLM stores distant contexts in additional memory units and employs efficient mechanisms to retrieve token-relevant units for attention computation, allowing models pre-trained on sequences of a few thousand tokens to effectively process sequences up to 1,024K tokens [ 1175 ] .

4.2.2 Contextual Self-Refinement and Adaptation

Self-refinement enables LLMs to improve outputs through cyclical feedback mechanisms mirroring human revision processes, leveraging self-evaluation through conversational self-interaction via prompt engineering distinct from reinforcement learning approaches [ 735 , 916 , 25 , 1211 ] .

Foundational Self-Refinement Frameworks

The Self-Refine framework uses the same model as generator, feedback provider, and refiner, demonstrating that identifying and fixing errors is often easier than producing perfect initial solutions [ 735 , 1313 , 227 ] . Reflexion maintains reflective text in episodic memory buffers for future decision-making through linguistic feedback [ 956 ] , while structured guidance proves essential as simplistic prompting often fails to enable reliable self-correction [ 672 , 587 ] .

Multi-Aspect Feedback integrates frozen language models and external tools focusing on specific error categories to enable more comprehensive, independent evaluation [ 799 ] . The N-CRITICS framework implements ensemble-based evaluation where initial outputs are assessed by both generating LLMs and other models, with compiled feedback guiding refinement until task-specific stopping criteria are fulfilled [ 789 ] .

The A2R framework adopts explicit evaluation across multiple dimensions including correctness and citation quality, formulating natural language feedback for each aspect and iteratively refining outputs [ 577 ] . ISR-LLM improves LLM-based planning by translating natural language to formal specifications, creating an initial plan, and then systematically refining it with a validator [ 1373 ] .

Meta-Learning and Autonomous Evolution

SELF teaches LLMs meta-skills (self-feedback, self-refinement) with limited examples, then has the model continuously self-evolve by generating and filtering its own training data [ 704 ] . Self-rewarding mechanisms enable models to improve autonomously through iterative self-judgment, where a single model adopts dual roles as performer and judge, maximizing rewards it assigns itself [ 1163 , 1278 ] .

The Creator framework extends this paradigm by enabling LLMs to create and use their own tools through a four-module process encompassing creation, decision-making, execution, and recognition [ 946 , 856 ] . The Self-Developing framework represents the most autonomous approach, enabling LLMs to discover, implement, and refine their own improvement algorithms through iterative cycles generating algorithmic candidates as executable code [ 466 ] .

In-context learning fundamentally represents a form of meta-learning where models learn optimization strategies during pre-training that generalize across diverse tasks, enabling rapid adaptation to novel challenges during inference [ 179 , 1165 ] . Meta-in-context learning demonstrates that in-context learning abilities can be recursively improved through in-context learning itself, adaptively reshaping model priors over expected tasks and modifying in-context learning strategies [ 177 ] .

Memory-Augmented Adaptation Frameworks

Memory augmentation represents a powerful approach for implementing meta-learning through frameworks like Memory of Amortized Contexts, which uses feature extraction and memory-augmentation to compress information from new documents into compact modulations stored in memory banks [ 1011 ] . Context-aware Meta-learned Loss Scaling addresses outdated knowledge challenges by meta-training small autoregressive models to dynamically reweight language modeling loss for each token during online fine-tuning [ 430 ] .

Decision-Pretrained Transformers demonstrate how transformers can be trained to perform in-context reinforcement learning, solving previously unseen RL problems by generalizing beyond pretraining distribution [ 1013 , 582 ] . Context-based meta-reinforcement learning methods enhance performance through direct supervision of context encoders, improving sample efficiency compared to end-to-end training approaches [ 1072 ] .

Long Chain-of-Thought and Advanced Reasoning

Long Chain-of-Thought has emerged as a significant evolution characterized by substantially longer reasoning traces enabling thorough problem exploration, as implemented in advanced models including OpenAI-o1, DeepSeek-R1, QwQ, and Gemini 2.0 Flash Thinking [ 147 , 718 , 1214 ] . LongCoT effectiveness appears linked to context window capacity, with empirical evidence suggesting larger context windows often lead to stronger reasoning performance [ 1229 ] .

Extended reasoning enables self-reflection and error correction mechanisms allowing models to identify and rectify mistakes during problem-solving processes [ 1334 ] . The effectiveness of increasing reasoning step length, even without adding new information, considerably enhances reasoning abilities across multiple datasets through test-time scaling [ 1345 ] .

Optimization strategies address computational inefficiencies due to verbose reasoning traces through self-generated shorter reasoning paths via best-of-N sampling, adaptive reasoning modes including Zero-Thinking and Less-Thinking approaches, and explicit compact CoT methods reducing token usage while maintaining reasoning quality [ 791 , 1348 , 697 ] . Auto Long-Short Reasoning enables dynamic adjustment of reasoning path length according to question complexity, helping models decide when longer chains are necessary [ 715 ] .

4.2.3 Multimodal Context

Multimodal Large Language Models (MLLMs) extend context engineering beyond text by integrating diverse data modalities including vision, audio, and 3D environments into unified contextual representations. This expansion introduces new challenges in modality fusion, cross-modal reasoning, and long-context processing while enabling sophisticated applications that leverage rich multimodal contextual understanding.

Multimodal Context Integration

Foundational Techniques

Multimodal MLLMs expand upon traditional LLMs by integrating data from diverse modalities like vision, audio, and 3D environments [ 105 , 49 , 957 ] . A primary integration method converts visual inputs into discrete tokens concatenated with text tokens, conditioning the LLM’s generative process on a combined representation [ 1286 ] . This is often facilitated by Visual Prompt Generators (VPGs) trained on image-caption pairs to map visual features into the LLM’s embedding space [ 607 ] . The dominant architectural paradigm connects specialized, external multimodal encoders—such as CLIP for vision or CLAP for audio—to the LLM backbone via alignment modules like Q-Former or simple MLPs [ 19 , 86 , 609 , 1130 ] , a modular design that allows for independent encoder updates without retraining the entire model [ 618 ] .

Advanced Integration Strategies

More sophisticated approaches enable deeper modality fusion. Cross-modal attention mechanisms learn fine-grained dependencies between textual and visual tokens directly within the LLM’s embedding space, enhancing semantic understanding for tasks like image editing [ 564 , 901 , 102 ] . To manage lengthy inputs, hierarchical designs process modalities in stages to ensure scalability [ 155 ] , while the “browse-and-concentrate” paradigm fuses the contexts of multiple images before LLM ingestion to overcome the limitations of isolated processing [ 1134 ] . Some research bypasses the adaptation of text-only LLMs, opting for unified training paradigms that jointly pre-train models on multimodal data and text corpora from the start to mitigate alignment challenges [ 1381 , 1224 ] . Other methods leverage text as a universal semantic space, using LLM in-context learning to improve generalization across diverse modality combinations [ 1050 ] . For video, context integration techniques range from prompt tuning to adapter-based methods that transform video content into a sequence for reasoning [ 1080 ] . The development of these models is often constrained by the need for vast, high-quality multimodal data and significant computational resources [ 1295 , 609 , 211 ] .

Core Challenges in Multimodal Context Processing

Modality Bias and Reasoning Deficiencies

A primary obstacle in MLLM development is modality bias, where models favor textual inputs, generating plausible but multimodally ungrounded responses by relying on learned linguistic patterns rather than integrated visual or auditory information [ 1358 , 24 , 315 , 1325 ] . This issue is exacerbated by training methodologies; for instance, VPGs trained on simple image-captioning tasks learn to extract only salient features for captions, neglecting other visual details crucial for more complex, instruction-based tasks, which fundamentally limits deep multimodal understanding [ 607 , 504 ] . Consequently, MLLMs frequently struggle with fine-grained spatial or temporal reasoning, such as precise object localization or understanding detailed event sequences in videos [ 1031 , 957 ] , particularly in complex domains like social media where interpreting the interplay of text and images to understand misinformation or sarcasm is difficult [ 505 ] . Effective multimodal reasoning requires not just comprehending each modality but also inferring their combined holistic meaning [ 385 ] . Compounding these issues is our limited mechanistic understanding of MLLMs themselves; their internal workings are largely a black box, hindering the development of better architectures [ 1274 ] .

Advanced Contextual Capabilities and Future Directions

In-Context and Long-Context Learning

A key capability of MLLMs is in-context learning, where models adapt to new tasks from multimodal examples in the prompt without weight updates [ 1397 , 1398 , 551 ] . Link-context learning (LCL) enhances this by providing demonstrations with explicit causal links, improving generalization [ 1012 ] . However, in-context learning is constrained by fixed context windows, as image tokens consume significant space, limiting many-shot learning [ 437 ] . Performance is also sensitive to input order and the relative importance of each modality varies by task [ 1020 , 1197 ] . Processing long multimodal contexts, crucial for applications like video analysis, remains a major research frontier [ 1086 ] . Innovations include adaptive hierarchical token compression for video [ 1119 ] , variable visual position encoding (V2PE) [ 1381 ] , specialized modules like ContextQFormer for conversational memory [ 589 ] , and dynamic, query-aware frame selection for video [ 581 ] . MLLMs also show emergent communication efficiency over extended interactions, a phenomenon still under investigation [ 436 ] .

Emerging Applications

The ability to process rich multimodal context is unlocking new applications. MLLMs are used for predictive reasoning, such as forecasting human activity from visual scenes [ 1382 ] , and have demonstrated impressive perception and cognitive capabilities across various multimodal benchmarks [ 290 ] . In VQA, context is leveraged for more precise answers, for instance, by prompting the MLLM to generate its own descriptive text context of an image [ 1346 ] or by integrating external knowledge via RAG [ 993 , 105 ] . Other applications include planning digital actions based on sensory inputs [ 605 ] , enhancing surgical decision support through memory-augmented context comprehension [ 418 ] , and enabling nuanced video understanding by integrating visual information with speech and audio cues [ 642 , 1193 , 7 ] . Researchers have also extended MLLMs to emerging modalities like tactile information, event data, and graph structures [ 1358 , 1023 , 1213 ] . The growing importance of these real-world use cases has spurred the development of comprehensive evaluation frameworks to assess contextual comprehension [ 1109 ] . These advancements enable applications previously impossible with text-only models, such as image captioning and sophisticated multimodal reasoning [ 1173 , 677 , 139 ] .

4.2.4 Relational and Structured Context

Large language models face fundamental constraints processing relational and structured data including tables, databases, and knowledge graphs due to text-based input requirements and sequential architecture limitations [ 489 , 47 , 1136 ] . Linearization often fails to preserve complex relationships and structural properties, with performance degrading when information is dispersed throughout contexts [ 586 , 585 , 938 ] .

Knowledge Graph Embeddings and Neural Integration

Advanced encoding strategies address structural limitations through knowledge graph embeddings that transform entities and relationships into numerical vectors, enabling efficient processing within language model architectures [ 12 , 1250 , 930 , 1194 ] . Graph neural networks capture complex relationships between entities, facilitating multi-hop reasoning across knowledge graph structures through specialized architectures like GraphFormers that nest GNN components alongside transformer blocks [ 974 , 404 , 1221 , 483 ] .

GraphToken demonstrates substantial improvements by explicitly representing structural information, achieving up to 73 percentage points enhancement on graph reasoning tasks through parameter-efficient encoding functions [ 836 ] . Heterformer and other hybrid GNN-LM architectures perform contextualized text encoding and heterogeneous structure encoding in unified models, addressing the computational challenges of scaling these integrated systems [ 496 , 465 , 751 ] .

Method Approach Performance Key Innovation

ODA [ 1001 ] Observation-driven agent framework 12.87% and 8.9% improvements Recursive observation with action-reflection

RAG-KG [ 1206 ] Historical issue KG construction 77.6% MRR, 0.32 BLEU improvement Query parsing and sub-graph retrieval

KARPA [ 258 ] Training-free KG adaptation State-of-the-art KGQA performance Pre-planning relation paths

Faithful Reasoning [ 720 ] Planning-retrieval-reasoning framework N/A LLM-KG synergy with relation paths

Table 3 : Knowledge graph integration methods for enhanced reasoning in large language models.

Verbalization and Structured Data Representations

Verbalization techniques convert structured data including knowledge graph triples, table rows, and database records into natural language sentences, enabling seamless integration with existing language systems without architectural modifications [ 12 , 782 , 1064 , 13 ] . Multi-level structurization approaches reorganize input text into layered structures based on linguistic relationships, while structured data representations leverage existing LLMs to extract structured information and represent key elements as graphs, tables, or relational schemas [ 681 , 1125 , 1324 , 1035 , 602 ] .

Programming language representations of structured data, particularly Python implementations for knowledge graphs and SQL for databases, outperform traditional natural language representations in complex reasoning tasks by leveraging inherent structural properties [ 1166 ] . Resource-efficient approaches using structured matrix representations offer promising directions for reducing parameter counts while maintaining performance on structured data tasks [ 343 ] .

Integration Frameworks and Synergized Approaches

The integration of knowledge graphs with language models follows distinct paradigms characterized by different implementation strategies and performance trade-offs [ 817 , 1140 ] . Pre-training integration methods like K-BERT inject knowledge graph triples during training to internalize factual knowledge, while inference-time approaches enable real-time knowledge access without requiring complete model retraining [ 690 , 1237 , 712 ] .

KG-enhanced LLMs incorporate structured knowledge to improve factual grounding through retrieval-based augmentation methods like KAPING, which retrieves relevant facts based on semantic similarities and prepends them to prompts without requiring model training [ 48 , 673 , 591 ] . More sophisticated implementations embed KG-derived representations directly into model latent spaces through adapter modules and cross-attention mechanisms, with Text2Graph mappers providing linking between input text and KG embedding spaces [ 132 , 1066 , 428 ] .

Synergized approaches create unified systems where both technologies play equally important roles, addressing fundamental limitations through bidirectional reasoning driven by data and knowledge [ 817 , 853 , 1111 ] . GreaseLM facilitates deep interaction across all model layers, allowing language context representations to be grounded by structured world knowledge while linguistic nuances inform graph representations [ 1321 ] . QA-GNN implements bidirectional attention mechanisms connecting question-answering contexts and knowledge graphs through joint graph formation and mutual representation updates via graph-based message passing [ 1250 , 974 ] .

Applications and Performance Enhancement

Structured data integration significantly enhances LLM capabilities across multiple dimensions, with knowledge graphs providing structured information that reduces hallucinations by grounding responses in verifiable facts and improving factual accuracy through clearly defined information sources [ 1002 , 1342 , 200 , 565 ] . Knowledge graphs enhance reasoning capabilities by providing structured entity relationships that enable complex multi-hop reasoning and logical inferences, with their rich repository of hierarchical knowledge significantly improving precision and reliability of inferences [ 1166 , 208 , 1018 ] .

Real-world applications demonstrate substantial improvements across specialized domains. Healthcare systems combine structured medical knowledge with contextual understanding through Retrieval-Augmented Generation frameworks to improve disease progression modeling and clinical decision-making [ 842 , 583 ] . Scientific research platforms organize findings into structured knowledge supporting hypothesis generation and research gap identification, while business analytics systems balance rule-based precision with AI pattern recognition for more actionable insights [ 1326 , 1062 ] .

Question answering systems benefit from natural language interfaces over structured data sources, with integration creating more robust systems capable of handling multimodal queries and providing personalized responses that overcome static knowledge base limitations [ 1317 , 1116 , 914 , 1206 ] . Research demonstrates that structured knowledge representations can improve summarization performance by 40% and 14% across public datasets compared to unstructured memory approaches, with Chain-of-Key strategies providing additional performance gains through dynamic structured memory updates [ 459 ] .

Method Data Type Integration Method Key Innovation Task Scope

K-LAMP [ 48 ] Knowledge graphs Retrieval-based augmentation KAPING framework Zero-shot QA

Pan et al. [ 817 ] Knowledge graphs Pre-training & inference integration Synergized LLMs + KGs Multi-domain reasoning

StructLM [ 1392 ] Tables, graphs, databases Instruction tuning 1.1M example dataset 18 datasets, 8 SKG tasks

Shao et al. [ 938 ] Tables, databases, KGs Linearization methods Schema linking & syntax prediction Text-to-SQL tasks

Table 4 : Representative approaches for structured data integration in large language models.

4.3 Context Management

Context Management addresses the efficient organization, storage, and utilization of contextual information within LLMs. This component tackles fundamental constraints imposed by finite context windows, develops sophisticated memory hierarchies and storage architectures, and implements compression techniques to maximize information density while maintaining accessibility and coherence.

4.3.1 Fundamental Constraints

LLMs face fundamental constraints in context management stemming from finite context window sizes inherent in most architectures, which significantly reduce model efficacy on tasks requiring deep understanding of lengthy documents while imposing substantial computational demands that hinder applications requiring quick responses and high throughput [ 1074 ] . Although extending context windows enables models to handle entire documents and capture longer-range dependencies, traditional transformer architectures experience quadratic computational complexity growth as sequence length increases, making processing extremely long texts prohibitively expensive [ 999 ] . While innovative approaches like LongNet have reduced this complexity to linear, balancing window size and generalization capabilities remains challenging [ 999 , 216 ] .

Empirical evidence reveals the “lost-in-the-middle” phenomenon, where LLMs struggle to access information positioned in middle sections of long contexts, performing significantly better when relevant information appears at the beginning or end of inputs [ 128 , 685 , 648 ] . This positional bias severely impacts performance in extended chain-of-thought reasoning tasks where critical earlier results become susceptible to forgetting, with performance degrading drastically by as much as 73% compared to performance with no prior context [ 128 , 1138 , 377 ] .

LLMs inherently process each interaction independently, lacking native mechanisms to maintain state across sequential exchanges and robust self-validation mechanisms, constraints stemming from fundamental limits identified in Gödel’s incompleteness theorems [ 128 , 368 ] . This fundamental statelessness necessitates explicit management systems to maintain coherent operation sequences and ensure robust failure recovery mechanisms [ 128 ] . Context management faces opposing challenges of context window overflow, where models “forget” prior context due to exceeding window limits, and context collapse, where enlarged context windows or conversational memory cause models to fail in distinguishing between different conversational contexts [ 985 ] . Research demonstrates that claimed benefits of chain-of-thought prompting don’t stem from genuine algorithmic learning but rather depend on problem-specific prompts, with benefits deteriorating as problem complexity increases [ 984 ] . The computational overhead of long-context processing creates additional challenges in managing key-value caches which grow substantially with input length, creating bottlenecks in both latency and accuracy, while multi-turn and longitudinal interaction challenges further complicate context management as limited effective context hinders longitudinal knowledge accumulation and token demands of many-shot prompts constrain space available for system and user inputs while slowing inference [ 911 , 719 , 389 ] .

4.3.2 Memory Hierarchies and Storage Architectures

Modern LLM memory architectures employ sophisticated hierarchical designs organized into methodological approaches to overcome fixed context window limitations. OS-inspired hierarchical memory systems implement virtual memory management concepts, with MemGPT exemplifying this approach through systems that page information between limited context windows (main memory) and external storage, similar to traditional operating systems [ 813 ] . These architectures consist of main context containing system instructions, FIFO message queues, and writable scratchpads, alongside external context holding information accessible through explicit function calls, with memory management through function-calling capabilities enabling autonomous paging decisions [ 831 ] . PagedAttention, inspired by virtual memory and paging techniques in operating systems, manages key-value cache memory in LLMs [ 57 ] .

Dynamic memory organizations implement innovative systems based on cognitive principles, with MemoryBank using Ebbinghaus Forgetting Curve theory to dynamically adjust memory strength according to time and significance [ 1202 , 1362 ] . ReadAgent employs episode pagination to segment content, memory gisting to create concise representations, and interactive look-up for information retrieval [ 1202 ] . Compressor-retriever architectures support life-long context management by using base model forward functions to compress and retrieve context, ensuring end-to-end differentiability [ 1236 ] .

Architectural adaptations enhance model memory capabilities through internal modifications including augmented attention mechanisms, refined key-value cache mechanisms, and modified positional encodings [ 160 , 1352 ] . Knowledge-organization methods structure memory into interconnected semantic networks enabling adaptive management and flexible retrieval, while retrieval mechanism-oriented approaches integrate semantic retrieval with memory forgetting mechanisms [ 515 , 1362 , 444 ] .

System configurations balance efficiency and scalability through organizational approaches where centralized systems coordinate tasks efficiently but struggle with scalability as topics increase, leading to context overflow, while decentralized systems reduce context overflow but increase response time due to inter-agent querying [ 396 ] . Hybrid approaches balance shared knowledge with specialized processing for semi-autonomous operation, addressing challenges in balancing computational efficiency with contextual fidelity while mitigating memory saturation where excessive storage of past interactions leads to retrieval inefficiencies [ 160 , 396 ] . Context Manager Components provide fundamental capabilities for snapshot creation, restoration of intermediate generation states, and overall context window management for LLMs [ 757 ] .

4.3.3 Context Compression

Context compression techniques enable LLMs to handle longer contexts efficiently by reducing computational and memory burden while preserving critical information. Autoencoder-based compression achieves significant context reduction through In-context Autoencoder (ICAE), which achieves 4× context compression by condensing long contexts into compact memory slots that LLMs can directly condition on, significantly enhancing models’ ability to handle extended contexts with improved latency and memory usage during inference [ 317 ] . Recurrent Context Compression (RCC) efficiently expands context window length within constrained storage space, addressing challenges of poor model responses when both instructions and context are compressed by implementing instruction reconstruction techniques [ 441 ] .

Memory-augmented approaches enhance context management through kNN-based memory caches that store key-value pairs of past inputs for later lookup, improving language modeling capabilities through retrieval-based mechanisms [ 393 ] . Contrastive learning approaches enhance memory retrieval accuracy, while side networks address memory staleness without requiring LLM fine-tuning, and consolidated representation methods dynamically update past token representations, enabling arbitrarily large context windows without being limited by fixed memory slots [ 393 ] .

Hierarchical caching systems implement sophisticated multi-layer approaches, with Activation Refilling (ACRE) employing Bi-layer KV Cache where layer-1 cache captures global information compactly and layer-2 cache provides detailed local information, dynamically refilling L1 cache with query-relevant entries from L2 cache to integrate broad understanding with specific details [ 859 ] . Infinite-LLM addresses dynamic context length management through DistAttention for distributing attention computation across GPU clusters, liability mechanisms for borrowing memory across instances, and global planning coordination [ 935 ] . KCache optimizes inference by storing K Cache in high-bandwidth memory while keeping V Cache in CPU memory, selectively copying key information based on attention calculations [ 935 ] .

Multi-agent distributive processing represents an emerging approach using LLM-based multi-agent methods to handle massive inputs in distributed manner, addressing core bottlenecks in knowledge synchronization and reasoning processes when dealing with extensive external knowledge [ 699 ] . Analysis of real-world key-value cache access patterns reveals high cache reusability in workloads like RAG and agents, highlighting the need for efficient distributed caching systems with optimized metadata management to reduce redundancy and improve speed [ 1389 ] . These compression techniques can be combined with other long-context modeling approaches to further enhance LLMs’ capacity to process and utilize extended contexts efficiently while reducing computational overhead and preserving information integrity [ 317 ] .

Method Strategy Efficiency Accuracy Length Mgmt Scalability

O1-Pruner [ 718 ] RL fine-tuning N/A +Acc, -Overhead Auto pruning +Efficiency

InftyThink [ 1214 ] Iterative + summarization Complexity reduction +3-13% Iterative control Scalable

Long-CoT Survey [ 147 ] Long CoT + reasoning +Efficiency frameworks +Complex domains Deep exploration Test-time scaling

PREMISE [ 1273 ] Prompt opt + diagnostics Gradient-inspired opt Maintained/+Acc -87.5% tokens Performance maintained

Prune-on-Logic [ 721 ] Structure-aware pruning Selective pruning +Accuracy Selective framework Logic-based opt

Table 5 : Long-chain reasoning methods and their characteristics in large language models. O1-Pruner uses reinforcement learning-style fine-tuning to shorten reasoning chains while maintaining accuracy. InftyThink employs iterative reasoning with intermediate summarization to reduce computational complexity. Long-CoT Survey explores long chain-of-thought characteristics that enhance reasoning abilities through efficiency improvements and enhanced knowledge frameworks. PREMISE optimizes prompts with trace-level diagnostics using gradient-inspired optimization, achieving 87.5% token reduction. Prune-on-Logic performs structure-aware pruning of logic graphs through selective removal of low-utility reasoning steps.

4.3.4 Applications

Effective context management extends LLMs’ capabilities beyond simple question-answering to enable sophisticated applications leveraging comprehensive contextual understanding across multiple domains. Document processing and analysis capabilities enable LLMs to handle entire documents or comprehend full articles rather than fragments, allowing for contextually relevant responses through comprehensive understanding of input material, particularly valuable for inherently long sequential data such as gene sequences, legal documents, and technical literature where maintaining coherence across extensive content is critical [ 999 ] .

Extended reasoning capabilities facilitated by context management techniques support complex reasoning requiring maintenance and building upon intermediate results across extended sequences. By capturing longer-range dependencies, these systems support multi-step problem solving where later reasoning depends on earlier calculations or deductions, enabling sophisticated applications in fields requiring extensive contextual awareness like complex decision support systems and scientific research assistance [ 999 , 160 ] .

Collaborative and multi-agent systems benefit from effective context management in multi-turn dialogues or sequential tasks where maintaining consistent state and synchronizing internal information between collaborating models is essential [ 154 ] . These capabilities support applications including distributed task processing, collaborative content creation, and multi-agent problem-solving where contextual coherence across multiple interactions must be maintained [ 154 ] .

Enhanced conversational interfaces leverage robust context management to seamlessly handle extensive conversations without losing thread coherence, enabling more natural, persistent dialogues that closely resemble human conversations [ 883 ] . Task-oriented LLM systems benefit from structured context management approaches, with sliding window storage implementing minimal context management systems that permanently append prompts and responses to context stores, and Retrieval-Augmented Generation systems supplementing LLMs with access to external sources of dynamic information [ 212 , 926 ] . These capabilities support applications like personalized virtual assistants, long-term tutoring systems, and therapeutic conversational agents that maintain continuity across extended interactions [ 883 ] .

Memory-augmented applications implement strategies enabling LLMs to persistently store, manage, and dynamically retrieve relevant contextual information, supporting applications requiring knowledge accumulation over time through building personalized user models via continuous interaction, implementing effective knowledge management across extended interactions, and supporting long-term planning scenarios depending on historical context [ 160 ] . Advanced memory frameworks like Contextually-Aware Intelligent Memory (CAIM) enhance long-term interactions by incorporating cognitive AI principles through modules that enable storage and retrieval of user-specific information while supporting contextual and time-based relevance filtering [ 1143 ] . Memory management for LLM agents incorporates processes analogous to human memory reconsolidation, including deduplication, merging, and conflict resolution, with approaches like Reflective Memory Management combining prospective and retrospective reflection for dynamic summarization and retrieval optimization [ 1167 , 382 ] . Case-based reasoning systems provide theoretical foundations for LLM agent memory through architectural components that enable cognitive integration and persistent context storage techniques that implement caching strategies for faster provisioning of necessary context [ 383 , 381 ] . The benefits extend beyond processing longer texts to fundamentally enhancing LLM interaction quality through improved comprehension, more relevant responses, and greater continuity across extended engagements, significantly expanding LLMs’ utility and resolving limitations imposed by restricted context windows [ 883 ] .

5 System Implementations

Building upon the foundational components of Context Engineering, this section examines sophisticated system implementations that integrate these components into practical, intelligent architectures. These implementations represent the evolution from theoretical frameworks to deployable systems that leverage context engineering principles. We present four major categories of system implementations. RAG systems demonstrate external knowledge integration through modular architectures and graph-enhanced approaches. Memory Systems showcase persistent context management through sophisticated memory architectures enabling long-term learning. Tool-Integrated Reasoning transforms language models into world interactors through function calling and environment interaction. Multi-Agent Systems present coordinated approaches through communication protocols and orchestration mechanisms. Each implementation builds upon foundational components while addressing specific challenges in context utilization, demonstrating how theoretical principles translate into practical systems.

5.1 Retrieval-Augmented Generation

Retrieval-Augmented Generation bridges the gap between parametric knowledge and dynamic information access by integrating external knowledge sources with language model generation. This implementation enables models to access current, domain-specific information through modular architectures, agentic frameworks, and graph-enhanced approaches that extend beyond static training data.

Figure 4 : Retrieval-Augmented Generation Framework: Overview of RAG system architectures including Modular RAG, Agentic RAG Systems, and Graph-Enhanced RAG approaches for external context integration.

5.1.1 Modular RAG Architectures

Modular RAG shifts from linear retrieval-generation architectures toward reconfigurable frameworks with flexible component interaction [ 311 , 1131 , 591 ] . Unlike Naive RAG and Advanced RAG’s query rewriting, Modular RAG introduces hierarchical architectures: top-level RAG stages, middle-level sub-modules, and bottom-level operational units [ 312 , 730 ] . This transcends linear structures through routing, scheduling, and fusion mechanisms enabling dynamic reconfiguration [ 312 ] .

The formal representation RAG = R, G operates through sophisticated module arrangements enabling Rewrite-Retrieve-Read models and Generate-Read approaches, incorporating adaptive search modules, RAGFusion for multi-query processing, routing modules for optimal data source selection, and hybrid retrieval strategies addressing retrieval accuracy and context relevance [ 311 , 491 , 908 , 1045 , 880 , 95 ] .

Contemporary frameworks demonstrate significant improvements in retrieval accuracy and trustworthiness [ 1372 ] . FlashRAG provides a modular toolkit with 5 core modules and 16 subcomponents enabling independent adjustment and pipeline combination [ 500 ] . KRAGEN enhances biomedical problem-solving by integrating knowledge graphs with vector databases, utilizing biomedical knowledge graph-optimized prompt generation to address hallucination in complex reasoning [ 397 , 749 , 973 ] . ComposeRAG implements atomic modules for Question Decomposition and Query Rewriting, incorporating self-reflection mechanisms for iterative refinement [ 1159 ] . This modularity facilitates integration with fine-tuning and reinforcement learning, enabling customization for specific applications and comprehensive toolkits supporting diverse NLP tasks [ 312 , 912 , 4 ] .

5.1.2 Agentic RAG Systems

Agentic RAG embeds autonomous AI agents into the RAG pipeline, enabling dynamic, context-sensitive operations guided by continuous reasoning [ 965 , 277 ] . These systems leverage reflection, planning, tool use, and multi-agent collaboration to manage retrieval strategies dynamically and adapt workflows to complex task requirements [ 965 ] . RAG and agent workflows align through query rewriting corresponding to semantic comprehension, while retrieval phases correspond to planning and execution [ 622 ] .

LLM-based autonomous agents extend basic language model capabilities through multimodal perception, tool utilization, and external memory integration [ 1160 , 1091 , 931 , 843 ] . External long-term memory serves as a knowledge datastore enabling agents to incorporate and access information over extended periods [ 1160 , 382 ] . Unlike static approaches, Agentic RAG treats retrieval as dynamic operation where agents function as intelligent investigators analyzing content and cross-referencing information [ 648 , 162 ] .

Implementation paradigms encompass prompt-based methods requiring no additional training and training-based approaches optimizing models through reinforcement learning for strategic tool invocation [ 648 , 1318 , 965 ] . Advanced systems enable LLM agents to query vector databases, access SQL databases, or utilize APIs within single workflows, with methodological advances focusing on reasoning capabilities, tool integration, memory mechanisms, and instruction fine-tuning for autonomous decision-making [ 703 , 6 ] .

Core capabilities include reasoning and planning components through task decomposition, multi-plan selection, and memory-augmented planning strategies enabling agents to break down complex tasks and select appropriate strategies [ 438 , 439 ] . PlanRAG improves decision-making through plan-then-retrieve approaches, enabling agents to evaluate multiple information sources and optimize retrieval strategies, while SLA management frameworks address reconfigurable multi-agent architectures [ 162 , 461 ] . Tool utilization enables systems to employ diverse resources including search engines, calculators, and APIs, with frameworks like ReAct and Reflexion exemplifying how interleaving reasoning with actions enhances adaptability [ 162 , 1160 , 956 ] . Memory mechanisms provide external long-term storage, while adaptive retrieval strategies enable autonomous analysis of complexity and context [ 162 , 1128 ] .

Self-reflection and adaptation mechanisms enable Agentic RAG systems to operate in dynamic environments through iterative feedback loops refining operations based on previous interaction outcomes [ 1183 , 686 ] . Advanced memory systems like MemoryBank implement update mechanisms inspired by the Ebbinghaus Forgetting Curve, enhancing agents’ ability to retrieve and apply learnings from past interactions [ 1362 , 165 ] . CDF-RAG employs closed-loop processes combining causal graph retrieval with reinforcement learning-driven query refinement and hallucination correction [ 531 ] . Self-RAG trains models that retrieve passages on demand while reflecting on retrievals and generations, using reflection tokens to control behavior during inference [ 239 , 41 ] .

5.1.3 Graph-Enhanced RAG

Graph-based Retrieval-Augmented Generation shifts from document-oriented approaches toward structured knowledge representations capturing entity relationships, domain hierarchies, and semantic connections [ 120 , 1353 , 360 , 1391 ] . This enables extraction of specific reasoning paths providing relevant information to language models while supporting multi-hop reasoning through structured pathway navigation [ 120 ] . Graph structures minimize context drift and hallucinations by leveraging interconnectivity for enhanced context-aware retrieval and logical coherence [ 512 , 806 ] .

Knowledge graphs serve as foundational representations encapsulating entities and interrelationships in structured formats enabling efficient querying and semantic relationship capture [ 162 , 1058 ] . Graph-based knowledge representations categorize into knowledge-based GraphRAG using graphs as knowledge carriers, index-based GraphRAG employing graphs as indexing tools, and hybrid GraphRAG combining both approaches [ 1199 ] . Sophisticated implementations include GraphRAG’s hierarchical indexing with community detection, PIKE’s multi-level heterogeneous knowledge graphs organizing documents into three-layer hierarchies, and EMG-RAG’s Editable Memory Graph architecture [ 313 ] .

Graph Neural Networks enhance RAG systems by addressing limitations in handling structured knowledge, with GNNs excelling at capturing entity associations and improving knowledge consistency [ 228 , 116 ] . GNN-RAG implementations adopt lightweight architectures for effective knowledge graph element retrieval, improving graph structure capture before interfacing with language models [ 1370 , 162 ] . The integration process encompasses graph building through node and edge extraction, retrieval based on queries, and generation incorporating retrieved information [ 1370 ] .

Multi-hop reasoning capabilities enable graph-based systems to synthesize information across multiple connected knowledge graph nodes, facilitating complex query resolution requiring interconnected fact integration [ 1058 , 166 ] . These systems employ structured representations capturing semantic relationships between entities and domain hierarchies in ways that unstructured text cannot [ 1058 , 166 ] . Advanced frameworks like Hierarchical Lexical Graph preserve statement provenance while clustering topics for flexible retrieval and linking entities for graph-based traversal [ 329 ] . Systems like GraphRAG, LightRAG, and derivatives implement dual-level retrieval, hierarchical indexing, and graph-enhanced strategies enabling robust multilevel reasoning [ 1174 , 313 ] .

Prominent architectures demonstrate diverse approaches to graph-enhanced retrieval, with optimization strategies showing significant improvements in retrieval effectiveness [ 106 ] . LightRAG integrates graph structures with vector representations through dual-level retrieval paradigms improving efficiency and content quality [ 412 , 717 ] . HippoRAG leverages Personalized PageRank over knowledge graphs achieving notable improvements in multi-hop question answering [ 1088 , 746 , 366 ] . HyperGraphRAG proposes hypergraph structured representations advancing beyond binary relations [ 717 ] . RAPTOR provides hierarchical summary tree construction for recursive context generation, while PathRAG introduces pruning techniques for graph-based retrieval [ 1349 , 928 , 134 ] . These structured approaches enable transparent reasoning pathways with explicit entity connections, reducing noise and improving semantic understanding while overcoming traditional RAG challenges [ 1174 , 512 ] .

5.1.4 Applications

Real-time RAG systems address critical challenges in production environments where dynamic knowledge bases require continuous updates and low-latency responses [ 1339 , 528 ] . Core challenges include efficient deployment and processing pipeline optimization, with existing frameworks lacking plug-and-play solutions necessitating system-level optimizations [ 1339 ] . Integration of streaming data introduces complications as traditional architectures demonstrate poor accuracy with frequently changing information and decreased efficiency as document volumes grow [ 514 ] .

Dynamic retrieval mechanisms advance over static approaches by continuously updating strategies during generation, adjusting goals and semantic vector spaces in real-time based on generation states and identified knowledge gaps [ 384 ] . Current limitations in determining optimal retrieval timing and query formulation are addressed through Chain-of-Thought reasoning, iterative retrieval processes, decomposed prompting, and LLM-generated content for dynamic retrieval enabling adaptive information selection, with approaches extending to adaptive control mechanisms enhancing generation quality through reflective tags [ 992 , 530 , 85 , 533 , 1239 ] .

Low-latency retrieval approaches leverage graph-based methods demonstrating significant promise in speed-accuracy optimization, with dense passage retrieval techniques providing foundational improvements [ 519 ] . LightRAG’s dual-level retrieval system enhances information discovery while integrating graph structures with vector representations for efficient entity relationship retrieval, reducing response times while maintaining relevance [ 360 ] . Multi-stage retrieval pipelines optimize computational efficiency through techniques like graph-based reranking, enabling dynamic access to current information while reducing storage requirements [ 974 ] .

Scalability solutions incorporate distributed processing architectures with efficient data partitioning, query optimization, and fault tolerance mechanisms adapting to changing stream conditions [ 1040 , 35 ] . Memory optimization through transformed heavy hitters streaming algorithms intelligently filters irrelevant documents while maintaining quality, particularly valuable for frequently changing content [ 514 ] . Production frameworks demonstrate efficiency gains through modular RAG architectures supporting pre-retrieval processes like query expansion and post-retrieval refinements such as compression and selection, enabling fine-tuning of individual components [ 1069 ] .

Incremental indexing and dynamic knowledge updates ensure systems adapt to new information without full retraining, particularly crucial in rapidly evolving domains like cybersecurity and climate finance applications [ 830 , 1056 ] . Modern frameworks incorporate dynamic knowledge retrieval methods enabling continuous strategy adjustment based on evolving input and contextual information, enhancing interactivity and semantic understanding while increasing applicability across cross-domain integration [ 384 ] . Advanced agent-based approaches demonstrate sophisticated task allocation capabilities in complex environments, such as coordinated UAV operations requiring real-time decision-making, with applications extending to grounded planning for embodied agents [ 1315 , 975 ] . Dynamic Retrieval Augmented Generation frameworks like DRAGON-AI showcase specialized implementations for ontology generation, combining textual and logical components while incorporating self-memory mechanisms enabling iterative improvement [ 1043 ] . These advances represent significant evolution toward seamlessly integrating real-time knowledge with flexible retrieval capabilities in dynamic environments.

5.2 Memory Systems

Memory Systems enable LLMs to transcend stateless interactions by implementing persistent information storage, retrieval, and utilization mechanisms. This implementation transforms models from pattern-matching processors into sophisticated agents capable of learning, adaptation, and long-term contextual understanding across extended interactions.

Figure 5 : Memory Systems Framework: Overview of memory architectures, memory-enhanced agents, and evaluation challenges for ultra-long context processing in LLMs.

5.2.1 Memory Architectures

Memory distinguishes sophisticated language systems from pattern-matching models, enabling information processing, storage, and utilization across natural language tasks [ 1182 , 1167 , 296 ] . LLMs face considerable memory system constraints despite breakthroughs in text generation and multi-turn conversations [ 1182 ] . Neural memory mechanisms struggle with inadequate structured information storage and reliance on approximate vector similarity calculations rather than precise symbolic operations, challenging accurate storage and retrieval for multi-hop reasoning [ 423 ] . These limitations represent critical challenges for developing AI systems operating effectively in complex real-world applications [ 544 ] .

Memory Classification Frameworks

LLM memory systems can be organized into multiple classification frameworks. The primary temporal classification divides memory into three categories: sensory memory (input prompts), short-term memory (immediate context processing), and long-term memory (external databases or dedicated structures) [ 935 ] . From a persistence perspective, short-term memory includes key-value caches and hidden states existing only within single sessions, while long-term memory encompasses text-based storage and knowledge embedded in model parameters, persisting across multiple interaction cycles [ 935 , 818 ] .

Implementation-based classifications identify parametric memory (knowledge encoded in model weights), ephemeral activation memory (context-limited runtime states), and plaintext memory accessed through Retrieval-Augmented Generation methods [ 637 ] . Current implementations lack sophisticated lifecycle management and multi-modal integration, limiting long-term knowledge evolution. Feed-forward network layers serve as key-value tables storing memory, functioning as “inner lexicon” for word retrieval and creating mechanisms analogous to human associative memory [ 518 , 325 , 326 , 764 , 464 ] . These classification schemes reflect attempts to develop LLM memory architectures paralleling human cognitive systems [ 1167 ] .

Short-Term Memory Mechanisms

Short-term memory in LLMs operates through the context window, serving as working memory maintaining immediate access to previously processed tokens [ 1282 ] . This functionality is implemented through key-value caches storing token representations but disappearing when sessions terminate [ 891 ] . Architectural variations demonstrate significant differences: transformer-based models implement working memory systems flexibly retrieving individual token representations across arbitrary delays, while LSTM architectures maintain coarser, rapidly-decaying semantic representations weighted toward earliest items [ 40 ] .

Modern LLM short-term memory frequently manifests as in-context learning, reflecting models’ ability to acquire and process information temporarily within context windows [ 1180 , 103 ] . This enables few-shot learning and task adaptation without parameter updates. Research identifies three primary memory configurations: full memory (utilizing entire context history), limited memory (using context subsets), and memory-less operation (without historical context) [ 1044 ] . Despite advances expanding context windows to millions of tokens, LLMs struggle with effective reasoning over extended contexts, particularly when relevant information appears in middle positions [ 891 , 685 ] .

Long-Term Memory Implementations

LLMs face significant challenges maintaining long-term memory due to context window limitations and catastrophic forgetting [ 114 ] . External memory-based methods address these limitations by utilizing physical storage to cache historical information, allowing relevant history retrieval without maintaining all information within constrained context windows [ 682 , 1362 ] . These approaches contrast with internal memory-based methods focusing on reducing self-attention computational costs to expand sequence length [ 682 , 287 ] .

Long-term memory implementations categorize into knowledge-organization methods (structuring memory into interconnected semantic networks), retrieval mechanism-oriented approaches (integrating semantic retrieval with forgetting curve mechanisms), and architecture-driven methods (implementing hierarchical structures with explicit read-write operations) [ 515 , 1362 , 444 ] . Memory storage representations can be further divided into token-level memory (information stored as structured text for direct retrieval) and latent-space memory (utilizing high-dimensional vectors for abstract and compact information representation) [ 1216 , 1124 ] . Advanced approaches incorporate psychological principles, with MemoryBank implementing Ebbinghaus Forgetting Curve theory for selective memory preservation based on temporal factors [ 1362 ] , emotion-aware frameworks employing Mood-Dependent Memory theory [ 444 ] , and memorization mechanisms balancing performance advantages with privacy concerns through extraction vulnerability analysis [ 1041 , 122 , 123 ] .

Memory Access Patterns and Structures

LLMs exhibit characteristic memory access patterns with notable similarities to human cognitive processes, demonstrating clear primacy and recency effects when recalling information lists [ 477 ] . Memory retrieval operates through sequential access (retrieving content in consecutive order) and random access (accessing information from arbitrary points without processing preceding content) [ 1387 ] . Memory persistence studies employ recognition experiments, recall experiments, and retention experiments to quantify information accessibility duration and retrieval conditions [ 810 ] , with cognitive psychology concepts like semantic and episodic memory integration improving LLM information synthesis capabilities [ 240 ] .

Memory organization encompasses diverse structural approaches including textual-form storage (complete and recent agent-environment interactions, retrieved historical interactions, external knowledge), knowledge representation structures (chunks, knowledge triples, atomic facts, summaries, mixed approaches), hierarchical systems with library-enhanced reasoning components, and functional patterns organized by tasks, temporal relevance, or semantic relationships [ 1329 , 1290 , 1027 ] . Core memory operations include encoding (transforming textual information into latent space embeddings), retrieval (accessing relevant information based on semantic relevance, importance, and recency), reflection (extracting higher-level insights), summarization (condensing texts while highlighting critical points), utilization (integrating memory components for unified outputs), forgetting (selective information discarding), truncation (formatting within token limitations), and judgment (assessing information importance for storage prioritization) [ 1331 ] . These structures offer varying trade-offs between comprehensiveness, retrieval efficiency, and computational requirements.

Model Textual Form Parametric Form

Complete Recent Retrieved External Fine-tuning Editing

Core Memory Systems

MemoryBank [ 1363 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

RET-LLM [ 778 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

ChatDB [ 423 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

TiM [ 683 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

Voyager [ 1078 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

MemGPT [ 814 ] × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

RecMind [ 1115 ] ✓ ✓ \checkmark ✓ × \times × × \times × × \times × × \times × × \times ×

Retroformer [ 1249 ] ✓ ✓ \checkmark ✓ × \times × × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times ×

ExpeL [ 1337 ] ✓ ✓ \checkmark ✓ × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times ×

Synapse [ 1357 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

Agent-Based Systems

ChatDev [ 855 ] ✓ ✓ \checkmark ✓ × \times × × \times × × \times × × \times × × \times ×

InteRecAgent [ 450 ] × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times ×

TPTU [ 909 , 554 ] ✓ ✓ \checkmark ✓ × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times ×

MetaGPT [ 409 ] ✓ ✓ \checkmark ✓ × \times × × \times × × \times × × \times × × \times ×

S³ [ 301 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

Mem0 [ 169 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

Advanced Memory Architectures

Larimar [ 198 ] × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times × ✓ ✓ \checkmark ✓

EM-LLM [ 286 ] × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

Controllable Working Memory [ 597 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × ✓ ✓ \checkmark ✓ × \times ×

Working Memory Hub [ 355 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times ×

Recent and Emerging Systems

LLM-based Opinion Dynamics [ 175 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

Memory Sandbox [ 456 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × ✓ ✓ \checkmark ✓

A-MEM [ 1203 ] × \times × × \times × ✓ ✓ \checkmark ✓ × \times × × \times × ✓ ✓ \checkmark ✓

MemEngine [ 1331 ] × \times × × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times ×

HIAGENT [ 429 ] × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times × × \times ×

MemInsight [ 917 ] × \times × × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times ×

Memory Sharing (MS) [ 302 ] × \times × × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × × \times ×

MemoRAG [ 860 ] ✓ ✓ \checkmark ✓ × \times × ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times ×

Echo [ 694 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ × \times × 
Table 6 : Extended from [ 1329 ] : Memory implementation patterns. ✓ ✓ \checkmark ✓ = Adopted, × \times × = Not Adopted

5.2.2 Memory-Enhanced Agents

Memory systems fundamentally transform LLMs from stateless pattern processors into sophisticated agents capable of persistent learning and adaptation across extended interactions [ 1259 ] . Memory-enhanced agents leverage both short-term memory (facilitating real-time responses and immediate context awareness) and long-term memory (supporting deeper understanding and knowledge application over extended periods) to adapt to changing environments, learn from experiences, and make informed decisions requiring persistent information access [ 1259 ] .

Agent Architecture Integration

Contemporary LLM agents employ memory systems analogous to computer memory hierarchies, with short-term memory functioning as primary storage for contextual understanding within context windows, while long-term memory serves as persistent storage for extended information retention [ 770 ] . From object-oriented perspectives, AI systems generate personal memories related to individual users and system memories containing intermediate task results [ 1167 ] . Structured frameworks like MemOS classify memory into Parametric Memory (knowledge encoded in model weights), Activation Memory, and Plaintext Memory, with parametric memory representing long-term knowledge embedded within feedforward and attention layers enabling zero-shot generation [ 637 ] .

Memory integration frameworks have evolved to address LLM limitations through sophisticated architectures. The Self-Controlled Memory (SCM) framework enhances long-term memory through LLM-based agent backbones, memory streams, and memory controllers managing updates and utilization [ 649 ] . The REMEMBERER framework equips LLMs with experience memory exploiting past episodes across task goals, enabling success/failure learning without parameter fine-tuning through verbal reinforcement and self-reflective feedback mechanisms [ 1299 ] . Advanced systems like MemLLM implement structured read-write memory modules addressing challenges in memorizing rare events, updating information, and preventing hallucinations [ 779 ] . Autonomous agents leveraging LLMs rely on four essential components—perception, memory, planning, and action—working together to enable environmental perception, interaction recall, and real-time planning and execution [ 614 , 38 ] .

Real-World Applications

Memory-enhanced LLM agents have demonstrated transformative impact across diverse application domains. In conversational AI, memory systems enable more natural, human-like interactions by recalling past experiences and user preferences to deliver personalized, context-aware responses. Commercial implementations include Charlie Mnemonic (combining Long-Term, Short-Term, and episodic memory using GPT-4), Google Gemini (leveraging long-term memory for personalized experiences across Google’s ecosystem), and ChatGPT Memory (remembering conversations across sessions) [ 578 ] . User simulation applications employ LLM-powered conversational agents mimicking human behavior for cost-effective dialogue system evaluation, adapting flexibly across open-domain dialogues, task-oriented interactions, and conversational recommendation [ 204 ] , with systems like Memory Sandbox enabling user control over conversational memories through data object manipulation [ 455 ] .

Task-oriented agents utilize memory to perform complex autonomous operations with minimal human intervention, employing LLMs as controllers extended through multimodal perception, tool utilization, and external memory [ 1160 ] . Applications span recommendation systems (RecMind providing personalized recommendations through planning and external knowledge, InteRecAgent employing LLMs with recommender models as tools), autonomous driving (DiLu instilling human-like knowledge through reasoning, reflection, and memory), scientific research (ChemCrow automating chemical synthesis design and execution), and social simulation (generative agents exhibiting believable behavior through memory storage and synthesis) [ 1019 , 647 , 92 , 825 ] . Proactive conversational agents address challenges in strategic dialogue scenarios requiring goal-oriented conversation steering through prompt-based policy planning methods and AI feedback generation based on dialogue history [ 204 , 203 ] .

Personalized assistant applications leverage memory to maintain coherent long-term relationships with users, with memory components serving as structured repositories storing contextually relevant information including user preferences and historical interactions [ 438 ] . Domain-specific implementations include healthcare assistants employing memory coordination for medical interactions [ 1316 , 1307 ] , recommendation agents leveraging external knowledge bases [ 1316 , 1293 ] , educational agents providing context-aware support through memory-enabled progress tracking [ 647 ] , and specialized frameworks like MARK enhancing personalized AI assistants through user preference memory [ 299 ] .

Memory Technologies and Integration Methods

Memory technology evolution addresses fundamental context window limitations through RAG, which combines parametric and non-parametric memory for language generation using pre-trained seq2seq models and dense vector indices [ 1209 , 591 ] . This approach enables access to information beyond parameter storage without requiring retraining, significantly extending knowledge capabilities. Advanced memory mechanisms including vector databases and retrieval-augmented generation enable vast information storage with quick relevant data access, incorporating short-term contextual memory and long-term external storage [ 38 , 367 , 1184 , 507 ] .

Non-parametric approaches maintain frozen LLM parameters while leveraging external resources like RAG to enrich task contexts [ 934 ] . Systems like Reflexion implement verbal reinforcement through self-reflective feedback in episodic memory buffers, while REMEMBERER incorporates persistent experience memory enabling learning from past successes and failures. Advanced architectures like MemoryBank enable memory retrieval, continuous evolution through updates, and personality adaptation by integrating previous interaction information [ 1202 , 1362 ] .

Specialized memory architectures address particular agent requirements through sophisticated organization and retrieval mechanisms. While early systems required predefined storage structures and retrieval timing, newer systems like Mem0 incorporate graph databases following RAG principles for more effective memory organization and relevance-based retrieval [ 1202 ] . Commercial and open-source implementations including OpenAI ChatGPT Memory, Apple Personal Context, mem0, and MemoryScope demonstrate widespread adoption of memory systems for enhanced personalization capabilities [ 1167 ] . Tool-augmentation paradigms validate effectiveness in complex task decomposition while leveraging world interaction tools, with memory-enhanced agents becoming central to modern AI systems performing complex tasks through natural language integration of planning, tool use, memory, and multi-step reasoning [ 247 , 356 , 1091 , 34 ] .

5.2.3 Evaluation and Challenges

Memory evaluation frameworks have emerged as critical components for systematically assessing LLM agent capabilities across multiple dimensions, reflecting the multifaceted nature of memory in intelligent systems. These comprehensive evaluation approaches reveal significant challenges while pointing toward promising research directions that could unlock new capabilities for memory-enhanced agents.

Evaluation Frameworks and Metrics

Contemporary memory evaluation employs specialized metrics extending beyond traditional NLP performance indicators to capture nuanced memory functionality aspects [ 1330 ] . Effectiveness metrics focus on factual information storage and utilization through accuracy measures (correctness of responses based on historical messages) and recall@5 indicators (percentage of relevant messages retrieved within top-5 results). Efficiency metrics examine temporal aspects through response time (duration for information retrieval and utilization) and adaptation time (period required for new information storage) [ 1330 ] .

Extensive benchmarks such as LongMemEval assess five fundamental long-term memory capabilities: information extraction, temporal reasoning, multi-session reasoning, knowledge updates, and abstention through 500 carefully selected questions, demonstrating 30% accuracy degradation in commercial assistants throughout prolonged interactions, while automated memory evaluation frameworks facilitate thorough assessment extending beyond passkey search methodologies [ 1171 ] . Dedicated frameworks target episodic memory via benchmarks assessing temporally-situated experiences, with research demonstrating that cutting-edge models including GPT-4, Claude variants, and Llama 3.1 encounter difficulties with episodic memory challenges involving interconnected events or intricate spatio-temporal associations even in comparatively brief contexts [ 457 ] . Contemporary LLM benchmarks predominantly concentrate on assessing models’ retention of factual information and semantic relationships while substantially overlooking episodic memory assessment—the capacity to contextualize memories with temporal and spatial occurrence details [ 841 ] .

Task-specific evaluations encompass long-context passage retrieval (locating specific paragraphs within extended contexts), long-context summarization (developing comprehensive understanding for concise summaries), NarrativeQA (answering questions based on lengthy narratives), and specialized benchmarks like MADail-Bench evaluating both passive and proactive memory recall in conversational contexts with novel dimensions including memory injection, emotional support proficiency, and intimacy assessment [ 1329 , 1380 , 550 , 386 ] . Additional task-specific frameworks include QMSum for meeting summarization, QuALITY for reading comprehension, DialSim for dialogue-based QA requiring spatiotemporal memory, and MEMENTO for personalized embodied agent evaluation using two-stage processes to assess memory utilization in physical environment tasks [ 1380 , 566 ] .

Current Limitations and Challenges

Memory evaluation faces substantial challenges limiting effective assessment of capabilities. Fundamental limitations include absence of consistent, rigorous methodologies for assessing memory performance, particularly regarding generalization beyond training data [ 284 ] . The lack of standardized benchmarks specifically designed for long-term memory evaluation represents another significant obstacle, with existing frameworks often failing to capture the full spectrum of memory capabilities needed for human-like intelligence [ 1071 ] .

Architectural constraints significantly complicate evaluation efforts, as most contemporary LLM-based agents operate in fundamentally stateless manners, treating interactions independently without truly accumulating knowledge incrementally over time [ 1355 , 1354 ] , despite advances in working memory through attentional tagging mechanisms enabling flexible memory representation control [ 864 ] . This limitation prevents genuine lifelong learning assessment—a cornerstone of human-level intelligence involving continuous knowledge acquisition, retention, and reuse across diverse contexts and extended time horizons.

Methodological issues arise when isolating memory-specific performance from other intelligence aspects, challenging determination of whether failures stem from inadequate memory mechanisms or reasoning limitations [ 284 ] . Dynamic memory usage in real-world applications poses evaluation challenges, as controlled laboratory tests inadequately capture memory system performance in complex scenarios where information relevance changes unpredictably [ 1071 ] .

Optimization Strategies and Future Research Directions

Memory optimization encompasses diverse techniques enhancing utilization while minimizing computational overhead and maximizing efficiency. Biologically-inspired forgetting mechanisms provide effective optimization approaches, with frameworks like MemoryBank implementing Ebbinghaus forgetting curves to selectively preserve and discard information based on temporal factors and significance [ 1362 ] . Reflection-based optimization through systems like Reflexion enables performance assessment through integrated evaluation and self-reflection, creating dual feedback systems refining memory and behavior through continuous learning [ 300 ] .

Hierarchical memory structures optimize information organization through multi-level formats enabling efficient retrieval, demonstrated by Experience-based Hierarchical Control frameworks with rapid memory access modules [ 862 ] , memory consolidation processes through bidirectional fast-slow variable interactions [ 63 ] , and Adaptive Cross-Attention Networks dynamically ranking memories based on query relevance [ 406 ] .

Future research directions encompass hybrid memory frameworks combining parametric precision with non-parametric efficiency [ 934 ] , automated feedback mechanisms for scalable response evaluation [ 885 ] , multi-agent memory systems enabling collaborative learning through shared external memories [ 302 ] , enhanced metadata learning with knowledge graph integration [ 888 , 382 ] , domain-specific memory architectures for specialized applications [ 501 ] , cognitive-inspired optimization incorporating memory consolidation during inactive periods [ 752 ] , and parameter-efficient memory updates through techniques like Low-Rank Adaptation for efficient knowledge integration [ 424 , 252 ] . These developments promise advancing memory-enhanced LLM agents toward sophisticated, human-like cognitive capabilities while addressing computational and architectural limitations, with applications extending to long-term robotic planning, real-world decision-making systems, and collaborative AI assistants through streaming learning scenarios and continuous feedback integration [ 1150 , 1336 , 1269 ] .

5.3 Tool-Integrated Reasoning

Tool-Integrated Reasoning transforms language models from passive text generators into active world interactors capable of dynamic tool utilization and environmental manipulation. This implementation enables models to transcend their inherent limitations through function calling mechanisms, integrated reasoning frameworks, and sophisticated environment interaction capabilities.

Figure 6 : Tool-Augmented Systems Framework: Evolution from text generators to world interactors through function calling mechanisms, tool-integrated reasoning, and environment interaction capabilities.

5.3.1 Function Calling Mechanisms

Function calling transforms LLMs from generative models into interactive agents through structured output generation leveraging functions’ abstraction mechanism, enabling external tool manipulation and access to current, domain-specific information for complex problem-solving [ 5 , 663 , 331 , 874 , 58 , 517 , 1104 ] .

Evolution began with Toolformer’s self-supervised approach demonstrating autonomous API learning, inspiring ReAct’s “thought-action-observation” cycle, progressing through specialized models like Gorilla and comprehensive frameworks including ToolLLM, RestGPT, with OpenAI’s JSON standardization, while advanced systems like Chameleon enabled multimodal question answering and TaskMatrix.AI managed AI models across domains [ 931 , 248 , 648 , 541 , 915 , 866 , 867 , 709 , 653 , 945 ] .

Technical implementation involves fine-tuning (dominant method providing stable capabilities via extensive API training but requiring significant resources) and prompt engineering (flexible, resource-efficient but unstable), with approaches like “Reverse Chain” enabling API operation via prompts, addressing challenges in large tool management [ 388 , 5 , 1323 , 785 , 144 , 250 ] .

Core process encompasses intent recognition, function selection, parameter-value-pair mapping, function execution, and response generation, with modern implementations utilizing structured LLM outputs for external program interaction, while tools include diverse interfaces (digital systems, scratch pads, user interactions, other LLMs, developer code), requiring complex navigation of tool selection, argument formulation, and result parsing [ 1259 , 663 , 1132 , 189 , 952 , 584 , 902 ] .

Training Methodologies and Data Systems

Training methodologies evolved from basic prompt-based approaches to sophisticated multi-task learning frameworks, with fine-tuning on specialized datasets through systems like ToolLLM and Granite-20B-FunctionCalling, beginning with synthetic single-tool data followed by human annotations [ 388 , 5 , 353 , 771 , 1226 ] .

Data generation strategies include Weaver’s GPT-4-based environment synthesis, APIGen’s hierarchical verification pipelines (format checking, function execution, semantic verification), generating 60,000+ high-quality entries across thousands of APIs [ 1104 , 1177 , 1259 , 1156 , 65 , 1393 , 743 ] .

Tool selection enhancement involves irrelevance-aware data augmentation, with Hammer’s function masking techniques, oracle tool mixing for increased difficulty, tool intent detection synthesis for over-triggering mitigation, emphasizing high-quality data through stringent filtering and format verification [ 664 , 10 , 353 , 467 , 1291 , 214 ] .

Self-improvement paradigms reduce external supervision dependence through JOSH algorithm’s sparse reward simulation environments and TTPA’s token-level optimization with error-oriented scoring, demonstrating improvements while preserving general capabilities [ 573 , 440 , 362 , 1262 ] .

Sophisticated benchmarks include API-Bank (73 APIs, 314 dialogues), StableToolBench (API instability solutions), NesTools (nested tool evaluation), ToolHop (995 queries, 3,912 tools), addressing single-tool to multi-hop scenarios [ 615 , 359 , 373 , 1255 , 821 , 987 , 1248 , 979 ] .

5.3.2 Tool-Integrated Reasoning

Tool-Integrated Reasoning (TIR) represents a paradigmatic advancement in Large Language Model capabilities, addressing fundamental limitations including outdated knowledge, calculation inaccuracy, and shallow reasoning by enabling dynamic interaction with external resources during the reasoning process [ 858 ] . Unlike traditional reasoning approaches that rely exclusively on internal model knowledge, TIR establishes a synergistic relationship where reasoning guides complex problem decomposition into manageable subtasks while specialized tools ensure accurate execution of each computational step [ 771 ] . This paradigm extends beyond conventional text-based reasoning by requiring models to autonomously select appropriate tools, interpret intermediate outputs, and adaptively refine their approach based on real-time feedback [ 858 ] .

The evolution of TIR methodologies encompasses three primary implementation categories addressing distinct aspects of tool utilization optimization. Prompting-based methods guide models through carefully crafted instructions without additional training, exemplified by approaches that decompose mathematical problems into executable code while delegating computation to Python interpreters [ 152 , 595 ] . Supervised fine-tuning approaches teach tool usage through imitation learning, with systems like ToRA focusing on mathematical problem-solving by integrating natural language reasoning with computational libraries and symbolic solvers [ 341 ] . Reinforcement learning methods optimize tool-use behavior through outcome-driven rewards, though current implementations often prioritize final correctness without considering efficiency, potentially leading to cognitive offloading phenomena where models over-rely on external tools [ 223 ] .

In operational terms, TIR-based agents serve as intelligent orchestrators that systematically interweave cognitive processing with external resource engagement to achieve targeted outcomes [ 1087 ] . This mechanism requires the harmonious integration of intrinsic reasoning capabilities and extrinsic tool utilization for progressive knowledge synthesis toward objective fulfillment, where the agent’s execution pathway is formally characterized as a structured sequence of tool activations coupled with corresponding information assimilation events [ 1087 ] . Emerging developments have established Agentic Reasoning architectures that amplify language model intelligence by incorporating autonomous tool-deploying agents, fluidly orchestrating web-based information retrieval, computational processing, and layered reasoning-memory integration to tackle sophisticated challenges necessitating comprehensive research and cascaded logical analysis [ 1153 ] .

Implementation Frameworks and Paradigms

Single-tool frameworks established foundational principles of tool-integrated reasoning through specialized implementations targeting specific computational domains. Program-Aided Language Models (PAL) pioneered problem decomposition strategies by generating executable code while delegating mathematical computations to Python interpreters [ 305 ] . ToolFormer demonstrated that language models could learn external API usage with minimal demonstrations, incorporating calculators, search engines, and diverse tools to enhance computational capabilities [ 931 ] . ToRA advanced mathematical reasoning by integrating natural language processing with computational libraries and symbolic solvers, while ReTool applied reinforcement learning to optimize code interpreter usage, demonstrating improvements in self-correction patterns [ 341 , 1311 , 965 ] . Self-Edit utilizes execution results of generated code to improve code quality for competitive programming tasks, employing a fault-aware code editor to correct errors based on test case results [ 1309 ] .

Multi-tool coordination systems address the complexity of orchestrating heterogeneous tools within integrated reasoning architectures. ReAct pioneered the interleaving of reasoning traces with task-specific actions, enabling models to think and act complementarily where reasoning supports plan tracking while actions interface with external information sources [ 1245 ] . Chameleon introduced plug-and-play compositional reasoning by synthesizing programs combining vision models, search engines, and Python functions with an LLM-based planner core [ 709 ] . AutoTools established automated frameworks transforming raw tool documentation into executable functions, reducing manual engineering requirements in tool integration [ 419 , 952 ] . Chain-of-Agents (CoA) trains models to decode reasoning chains with abstract placeholders, subsequently calling domain-specific tools to fill knowledge gaps [ 594 , 1327 ] .

Agent-based frameworks represent the most sophisticated evolution of TIR systems, moving beyond static prompting approaches to create autonomous and adaptive AI systems. Unlike conventional tool-use that follows rigid patterns, agent models learn to couple Chain-of-Thought (CoT) and Chain-of-Action (CoA) patterns into their core behavior, resulting in stronger logical coherence and natural transitions between reasoning and action [ 1328 ] . These systems build upon foundational agent architectures including reactive systems that map perceptions directly to actions, deliberative systems implementing Belief-Desire-Intention (BDI) models, and hybrid architectures combining multiple subsystems in hierarchical structures [ 728 ] .

Method Tool Categories

Search &

Retrieval

Computation &

Code Execution

Knowledge Base

& QA

APIs &

External Services

Multimodal

Tools

Language

Processing

Interactive

Environments

Domain-Specific

Tools

ReAct [ 1247 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

Toolformer [ 931 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ToolkenGPT [ 378 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ToolLLM [ 867 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ToRA [ 341 ] ✓ ✓ \checkmark ✓

PAL [ 303 ] ✓ ✓ \checkmark ✓

HuggingGPT [ 945 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

GPT4Tools [ 1225 ] ✓ ✓ \checkmark ✓

CRITIC [ 340 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

Chain of Code [ 595 ] ✓ ✓ \checkmark ✓

TRICE [ 863 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

TP-LLaMA [ 149 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

AlignToolLLaMA [ 161 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ReTool [ 270 ] ✓ ✓ \checkmark ✓

Tool-Star [ 221 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ARTIST [ 965 ] ✓ ✓ \checkmark ✓

Ego-R1 [ 1038 ] ✓ ✓ \checkmark ✓

VTool-R1 [ 1155 ] ✓ ✓ \checkmark ✓

KG-Agent [ 487 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

CACTUS [ 755 ] ✓ ✓ \checkmark ✓

MuMath-Code [ 1265 ] ✓ ✓ \checkmark ✓

ToRL [ 621 ] ✓ ✓ \checkmark ✓

MetaTool [ 452 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ToolEyes [ 1253 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

Graph-CoT [ 495 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

ToolRL [ 858 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

LATS [ 1364 ] ✓ ✓ \checkmark ✓ ✓ ✓ \checkmark ✓

Table 7 : Tool-augmented language model architectures: Comparison of multiple methods across 8 tool categories including search, computation, knowledge bases, APIs, multimodal, language tools, interactive environments, and domain-specific applications.

5.3.3 Agent-Environment Interaction

Reinforcement learning approaches have emerged as superior alternatives to prompting-based methods and supervised fine-tuning for tool integration, enabling models to autonomously discover optimal tool usage strategies through exploration and outcome-driven rewards [ 223 ] . ReTool exemplifies this advancement by focusing on code interpreter optimization for mathematical reasoning, achieving 67.0% accuracy on AIME2024 benchmarks after only 400 training steps, substantially outperforming text-based RL baselines reaching 40.0% accuracy with extensive training [ 270 ] . This demonstrates that explicitly modeling tool use within decision processes enhances both reasoning capabilities and training efficiency.

Search-augmented reasoning systems represent innovative integrations of information retrieval directly into reasoning processes through specialized learning environments. The Search-R1 framework trains models to make dynamic decisions about when to search and what queries to generate during multi-step reasoning tasks, unlike traditional retrieval-augmented generation systems [ 976 ] . The architecture employs specialized token systems structuring reasoning and search processes, where models learn to generate reasoning steps interspersed with explicit search actions triggered through tokens that encapsulate generated queries [ 648 ] .

Multi-turn and customizable tool invocation frameworks address the complexity of coordinating multiple heterogeneous tools during reasoning processes. Recent developments include frameworks like VisTA that use reinforcement learning to enable visual agents to dynamically explore, select, and combine tools from diverse libraries based on empirical performance [ 454 ] . ReVeal demonstrates self-evolving code agents via iterative generation-verification processes [ 506 ] . In multimodal domains, systems like VideoAgent employ vision-language foundation models as tools for translating and retrieving visual information, achieving impressive performance on video understanding benchmarks [ 1108 , 254 ] .

Evaluation and Applications

Comprehensive evaluation of tool-integrated reasoning systems requires specialized benchmarks that measure tool-integrated capabilities rather than general model performance. MCP-RADAR provides a standardized evaluation framework employing strictly objective metrics derived from quantifiable performance data, with extensible design spanning software engineering, mathematical reasoning, and general problem-solving domains [ 310 ] . The framework visualizes performance through radar charts highlighting model strengths and weaknesses across multiple dimensions, enabling systematic comparison of tool-integrated language models regardless of implementation mechanisms.

Real-world evaluation approaches reveal significant performance gaps between current systems and human-level capabilities, providing crucial insights into practical limitations and optimization opportunities. The General Tool Agents (GTA) benchmark addresses limitations in existing evaluations by featuring real human-written queries with implicit tool-use requirements, evaluation platforms with deployed tools across perception, operation, logic, and creativity categories, and authentic multimodal inputs including images and code snippets [ 1090 ] . Results demonstrate substantial challenges for current LLMs, with GPT-4 completing less than 50

Function calling enabled sophisticated multi-agent systems where multiple LLM agents collaborate through coordinated tool use and task decomposition, with MAS leveraging collective intelligence through parallel processing, information sharing, and adaptive role assignment, while LLM integration enhanced capabilities in planning, specialization, and task decomposition through frameworks like DyLAN, MAD, and MetaGPT [ 239 , 903 , 344 , 140 , 625 ] . Advanced multi-agent function calling employs sophisticated orchestration mechanisms decomposing complex tasks into manageable subtasks, with fundamental approaches involving splitting reward machines into parallel execution units, each agent maintaining individual reward machines, local state spaces, and propositions, while adaptive orchestration enables dynamic agent selection based on context, responses, and status reports [ 39 , 1048 , 691 , 117 ] .

5.4 Multi-Agent Systems

Multi-Agent Systems represent the pinnacle of collaborative intelligence, enabling multiple autonomous agents to coordinate and communicate for solving complex problems beyond individual agent capabilities. This implementation focuses on sophisticated communication protocols, orchestration mechanisms, and coordination strategies that enable seamless collaboration across diverse agent architectures.

Figure 7 : Multi-Agent Systems Framework: Overview of communication protocols, orchestration mechanisms, and coordination strategies for collaborative AI agent systems.

5.4.1 Communication Protocols

Agent communication systems originate from the Knowledge Sharing Effort of the early 1990s, establishing foundational principles for autonomous entity coordination through standardized languages addressing interoperability challenges [ 369 , 93 ] . KQML emerged as the pioneering Agent Communication Language, introducing multi-layered architecture separating content, message, and communication layers while employing speech act theory [ 369 , 82 , 657 , 280 ] . FIPA ACL enhanced this foundation through semantic frameworks based on modal logic, feasibility preconditions, and rational effects [ 1146 , 369 , 82 ] .

Interoperability requirements necessitate semantic-level communication capabilities enabling cross-platform agent understanding without extensive pre-communication setup, addressing increasing heterogeneity through ontology-based protocol formalization and Semantic Web technologies, while incorporating security mechanisms against communication vulnerabilities [ 480 , 66 , 443 , 481 , 786 , 1055 ] .

Contemporary Protocol Ecosystem

Contemporary standardized protocols address fragmentation challenges hindering LLM agent collaboration [ 1235 , 1128 , 408 ] . MCP functions as “USB-C for AI,” standardizing agent-environment interactions through JSON-RPC client-server interfaces, enabling hundreds of servers across diverse domains while introducing security vulnerabilities [ 926 , 246 , 616 , 266 , 15 , 257 , 922 , 1094 , 370 , 1185 , 297 , 1008 , 713 , 269 ] .

A2A standardizes peer-to-peer communication through capability-based Agent Cards enabling task delegation and secure collaboration via JSON-based lifecycle models [ 616 , 246 , 926 ] . ACP provides general-purpose RESTful HTTP communication supporting multipart messages and synchronous/asynchronous interactions with discovery, delegation, and orchestration features [ 277 , 246 ] .

ANP extends interoperability to open internet through W3C decentralized identifiers and JSON-LD graphs, with emerging protocols AGNTCY and Agora diversifying standardization ecosystems [ 246 , 679 , 1128 ] . Progressive layering strategy: MCP provides tool access, ACP enables message exchange, A2A supports peer interaction, ANP extends network interoperability [ 1007 , 926 ] .

LLM-Enhanced Communication Frameworks

LLMs transform agent communication through sophisticated natural language processing enabling unprecedented context sensitivity across academic and industrial applications spanning social science, natural science, and engineering domains [ 486 , 684 , 498 , 1091 , 1170 , 1127 , 896 , 1052 , 871 ] . Enhanced systems demonstrate cognitive synergy through specialized knowledge bases, planning, memory, and introspection capabilities, supporting cooperative, debate-oriented, and competitive communication paradigms [ 486 , 356 ] .

Communication structures encompass layered hierarchical organization, decentralized peer-to-peer networks, centralized coordination, and shared message pool architectures, complemented by sequential exchanges, universal language interfaces, and message-passing strategies [ 356 , 1240 , 1210 , 167 , 396 , 485 , 537 , 659 , 793 , 941 ] .

Framework implementations support comprehensive ecosystems: AutoGen enables dynamic response generation, MetaGPT provides shared message pools, CAMEL offers integrated orchestration, CrewAI facilitates adaptation, with reinforcement learning integration enhancing reward redesign, action selection, and policy interpretation [ 184 , 38 , 119 , 996 , 224 , 865 , 927 , 950 , 1264 ] . Human-agent communication introduces complex interaction landscapes through flexible participation and cognitive diversity, with agents inferring communicator properties and mirroring human communicative intentions [ 1399 , 34 , 669 ] .

5.4.2 Orchestration Mechanisms

Orchestration mechanisms constitute the critical coordination infrastructure for multi-agent systems, managing agent selection, context distribution, and interaction flow control [ 894 ] , enabling effective cooperation among human and non-human actors through user input processing, contextual distribution, and optimal agent selection based on capability assessment and response evaluation [ 53 ] , while managing message flow, ensuring task progression, and addressing task deviations [ 171 ] . Advanced orchestration frameworks incorporate intent recognition, contextual memory maintenance, and task dispatching components for intelligent coordination across domain-specific agents, with the Swarm Agent framework utilizing real-time outputs to direct tool invocations while addressing limitations in static tool registries and bespoke communication frameworks [ 808 , 263 , 246 ] .

Contemporary orchestration strategies exhibit distinct operational paradigms: a priori orchestration determines agent selection through pre-execution analysis of user input and agent capabilities, while posterior orchestration distributes inputs to multiple agents simultaneously, utilizing confidence metrics and response quality assessment as demonstrated by the 3S orchestrator framework [ 893 ] ; function-based orchestration emphasizes agent selection from available pools, contextual information management, and conversation flow control [ 54 ] ; component-based orchestration employs dynamic planning processes where orchestrators arrange components in logical sequences based on user instructions, utilizing LLMs as component orchestration tools to generate workflows with embedded orchestration logic [ 675 ] .

Emergent orchestration paradigms include puppeteer-style orchestration featuring centralized orchestrators that dynamically direct agents in response to evolving task states through reinforcement learning-based adaptive sequencing and prioritization, and serialized orchestration addressing collaboration topology complexity by unfolding collaboration graphs into reasoning sequences guided by topological traversal, enabling orchestrators to select single agents at each step based on global system state and task specifications [ 194 ] .

Context Management and Environmental Adaptation

Context serves as the foundational element guiding agent actions and interactions within orchestrated systems, supporting operational mode diversity while maintaining application individuality and task execution sequencing through global state maintenance that enables orchestration systems to track task execution progress across distributed nodes, providing agents with contextual awareness necessary for effective subtask performance within broader workflow contexts [ 26 ] . Session-based context refinement defines collaborative scope boundaries, facilitating event-driven orchestration where agents can enter and exit dynamically, create output streams, and contribute to shared session streams, with configurable sessions enabling agent inclusion based on user input or autonomous decision-making to create adaptable systems responsive to changing task requirements [ 513 ] .

Well-designed interaction structures and task orchestration mechanisms underscore context’s critical role in scalable multi-agent collaboration. Systems adapt communication patterns and agent roles to contextual requirements, supporting dynamic collaboration tailored to specific task demands through complex task decomposition and suitable agent assignment for subtask execution [ 1128 ] . This contextual adaptation encompasses both organizational and operational dimensions, enabling systems to maintain coherence while accommodating environmental variability and evolving user requirements.

5.4.3 Coordination Strategies

Multi-agent orchestration encounters significant challenges in maintaining transactional integrity across complex workflows, with contemporary frameworks including LangGraph, AutoGen, and CAMEL demonstrating insufficient transaction support: LangGraph provides basic state management while lacking atomicity guarantees and systematic compensation mechanisms, AutoGen prioritizes flexible agent interactions without adequate compensatory action management potentially resulting in inconsistent system states following partial failures, and validation limitations emerge as many frameworks rely exclusively on large language models’ inherent self-validation capabilities without implementing independent validation procedures, exposing systems to reasoning errors, hallucinations, and inter-agent inconsistencies [ 128 ] .

Context handling failures compound these challenges as agents struggle with long-term context maintenance encompassing both episodic and semantic information [ 210 , 1113 ] , while central orchestrator topologies introduce non-deterministic, runtime-dependent execution paths that enhance adaptability while complicating anomaly detection, requiring dynamic graph reconstruction rather than simple path matching [ 390 ] , and environmental misconfigurations and LLM hallucinations can distract agentic systems, with poor recovery leading to goal deviation that becomes amplified in multi-agent setups with distributed subtasks [ 210 , 1091 ] .

Inter-agent dependency opacity presents additional concerns as agents may operate on inconsistent assumptions or conflicting data without explicit constraints or validation layers, necessitating anomaly detection incorporating reasoning over orchestration intent and planning coherence [ 390 ] , while addressing these challenges requires comprehensive solutions such as the SagaLLM framework providing transaction support, independent validation procedures, and robust context preservation mechanisms [ 128 ] , and approaches like CodeAct integrating Python interpreters with LLM agents to enable code action execution and dynamic revision capabilities through multi-turn interactions [ 1113 ] .

Applications and Performance Implications

Agent and context orchestration demonstrates practical utility across diverse application domains: healthcare applications employ context-switching mechanisms within specialized agent-based architectures performing information retrieval, question answering, and decision support, utilizing supervisory agents to interpret input features and assign subtasks to specialized agents based on clinical query type, user background, and data modality requirements [ 613 , 754 , 1051 ] ; network management applications leverage context-aware orchestration to address complexity challenges by equipping Points of Access with agents dedicated to unique contexts, enabling efficient network dynamics management through context-specific action sets including available service instances and network paths [ 958 ] .

Business process management and simulation represent significant application areas through platforms like AgentSimulator, enabling process behavior discovery and simulation in orchestrated and autonomous settings where orchestrated behavior follows global control-flow patterns with activity selection dependent on previous activities and agent assignment based on capabilities and availability, while autonomous behavior operates through local control-flow and handover patterns acknowledging agent autonomy in collaborative work [ 543 ] .

Performance implications indicate that well-designed orchestration improves system effectiveness by leveraging distinct agent capabilities, with research demonstrating that human users frequently struggle with effective agent selection from available sets while automated orchestration enhances overall performance [ 72 ] , motivating frameworks that learn agent capabilities online and orchestrate multiple agents under real-world constraints including cost, capability requirements, and operational limitations, with autonomy levels varying across implementations where some systems exhibit pronounced autonomy within designated phases, demonstrating adaptability in action management corresponding to task specificity and reaching Level 2 autonomy through contextual resource utilization [ 460 ] .

6 Evaluation

The evaluation of context-engineered systems presents unprecedented challenges that transcend traditional language model assessment paradigms. These systems exhibit complex, multi-component architectures with dynamic, context-dependent behaviors requiring comprehensive evaluation frameworks that assess component-level diagnostics, task-based performance, and overall system robustness [ 835 , 1132 ] .

The heterogeneous nature of context engineering components—spanning retrieval mechanisms, memory systems, reasoning chains, and multi-agent coordination—demands evaluation methodologies that can capture both individual component effectiveness and emergent system-level behaviors [ 310 , 931 ] .

6.1 Evaluation Frameworks and Methodologies

This subsection presents comprehensive approaches for evaluating both individual components and integrated systems in context engineering.

6.1.1 Component-Level Assessment

Intrinsic evaluation focuses on the performance of individual components in isolation, providing foundational insights into system capabilities and failure modes.

For prompt engineering components, evaluation encompasses prompt effectiveness measurement through semantic similarity metrics, response quality assessment, and robustness testing across diverse input variations. Current approaches reveal brittleness and robustness challenges in prompt design, necessitating more sophisticated evaluation frameworks that can assess contextual calibration and adaptive prompt optimization [ 1132 , 663 ] .

Long context processing evaluation requires specialized metrics addressing information retention, positional bias, and reasoning coherence across extended sequences. The “needle in a haystack” evaluation paradigm tests models’ ability to retrieve specific information embedded within long contexts, while multi-document reasoning tasks assess synthesis capabilities across multiple information sources. Position interpolation techniques and ultra-long sequence processing methods face significant computational challenges that limit practical evaluation scenarios [ 731 , 295 ] .

Self-contextualization mechanisms undergo evaluation through meta-learning assessments, adaptation speed measurements, and consistency analysis across multiple iterations. Self-refinement frameworks including Self-Refine, Reflexion, and N-CRITICS demonstrate substantial performance improvements, with GPT-4 achieving approximately 20% improvement through iterative self-refinement processes [ 735 , 956 , 789 ] . Multi-dimensional feedback mechanisms and ensemble-based evaluation approaches provide comprehensive assessment of autonomous evolution capabilities [ 577 , 704 ] .

Structured and relational data integration evaluation examines accuracy in knowledge graph traversal, table comprehension, and database query generation. However, current evaluation frameworks face significant limitations in assessing structural reasoning capabilities, with high-quality structured training data development presenting ongoing challenges. LSTM-based models demonstrate increased errors when sequential and structural information conflict, highlighting the need for more sophisticated benchmarks testing structural understanding [ 763 , 668 , 163 ] .

6.1.2 System-Level Integration Assessment

Extrinsic evaluation measures end-to-end performance on downstream tasks, providing holistic assessments of system utility through comprehensive benchmarks spanning question answering, reasoning, and real-world applications.

System-level evaluation must capture emergent behaviors arising from component interactions, including synergistic effects where combined components exceed individual performance and potential interference patterns where component integration degrades overall effectiveness [ 835 , 1132 ] .

Retrieval-Augmented Generation evaluation encompasses both retrieval quality and generation effectiveness through comprehensive metrics addressing precision, recall, relevance, and factual accuracy. Agentic RAG systems introduce additional complexity requiring evaluation of task decomposition accuracy, multi-plan selection effectiveness, and memory-augmented planning capabilities. Self-reflection mechanisms demonstrate iterative improvement through feedback loops, with MemoryBank implementations incorporating Ebbinghaus Forgetting Curve principles for enhanced memory evaluation [ 438 , 162 , 1362 , 1183 , 41 ] .

Memory systems evaluation encounters substantial difficulties stemming from the absence of standardized assessment frameworks and the inherently stateless characteristics of contemporary LLMs. LongMemEval offers 500 carefully curated questions that evaluate fundamental capabilities encompassing information extraction, temporal reasoning, multi-session reasoning, and knowledge updates. Commercial AI assistants exhibit 30% accuracy degradation throughout extended interactions, underscoring significant deficiencies in memory persistence and retrieval effectiveness [ 1330 , 1171 , 457 , 841 , 386 ] . Dedicated benchmarks such as NarrativeQA, QMSum, QuALITY, and MEMENTO tackle episodic memory evaluation challenges [ 550 , 566 ] .

Tool-integrated reasoning systems require comprehensive evaluation covering the entire interaction trajectory, including tool selection accuracy, parameter extraction precision, execution success rates, and error recovery capabilities. The MCP-RADAR framework provides standardized evaluation employing objective metrics for software engineering and mathematical reasoning domains. Real-world evaluation reveals significant performance gaps, with GPT-4 completing less than 50% of tasks in the GTA benchmark, compared to human performance of 92% [ 310 , 1090 , 126 , 931 ] . Advanced benchmarks including BFCL (2,000 testing cases), T-Eval (553 tool-use cases), API-Bank (73 APIs, 314 dialogues), and ToolHop (995 queries, 3,912 tools) address multi-turn interactions and nested tool calling scenarios [ 259 , 359 , 373 , 1255 , 157 , 829 ] .

Multi-agent systems evaluation captures communication effectiveness, coordination efficiency, and collective outcome quality through specialized metrics addressing protocol adherence, task decomposition accuracy, and emergent collaborative behaviors. Contemporary orchestration frameworks including LangGraph, AutoGen, and CAMEL demonstrate insufficient transaction support, with validation limitations emerging as systems rely exclusively on LLM self-validation capabilities without independent validation procedures. Context handling failures compound challenges as agents struggle with long-term context maintenance encompassing both episodic and semantic information [ 128 , 390 , 893 ] .

6.2 Benchmark Datasets and Evaluation Paradigms

This subsection reviews specialized benchmarks and evaluation paradigms designed for assessing context engineering system performance.

6.2.1 Foundational Component Benchmarks

Long context processing evaluation employs specialized benchmark suites designed to test information retention, reasoning, and synthesis across extended sequences. Current benchmarks face significant computational complexity challenges, with O(n²) scaling limitations in attention mechanisms creating substantial memory constraints for ultra-long sequences. Position interpolation and extension techniques require sophisticated evaluation frameworks that can assess both computational efficiency and reasoning quality across varying sequence lengths [ 731 , 295 , 1227 ] .

Advanced architectures including LongMamba and specialized position encoding methods demonstrate promising directions for long context processing, though evaluation reveals persistent challenges in maintaining coherence across extended sequences. The development of sliding attention mechanisms and memory-efficient implementations requires comprehensive benchmarks that can assess both computational tractability and task performance [ 1258 , 347 ] .

Structured and relational data integration benchmarks encompass diverse knowledge representation formats and reasoning patterns. However, current evaluation frameworks face limitations in assessing structural reasoning capabilities, with the development of high-quality structured training data presenting ongoing challenges. Evaluation must address the fundamental tension between sequential and structural information processing, particularly in scenarios where these information types conflict [ 763 , 668 , 163 ] .

6.2.2 System Implementation Benchmarks

Retrieval-Augmented Generation evaluation leverages comprehensive benchmark suites addressing diverse retrieval and generation challenges. Modular RAG architectures demonstrate enhanced flexibility through specialized modules for retrieval, augmentation, and generation, enabling fine-grained evaluation of individual components and their interactions. Graph-enhanced RAG systems incorporating GraphRAG and LightRAG demonstrate improved performance in complex reasoning scenarios, though evaluation frameworks must address the additional complexity of graph traversal and multi-hop reasoning assessment [ 312 , 965 , 360 ] .

Agentic RAG systems introduce sophisticated planning and reflection mechanisms requiring evaluation of task decomposition accuracy, multi-plan selection effectiveness, and iterative refinement capabilities. Real-time and streaming RAG applications present unique evaluation challenges in assessing both latency and accuracy under dynamic information conditions [ 438 , 162 , 1183 ] .

Tool-integrated reasoning system evaluation employs comprehensive benchmarks spanning diverse tool usage scenarios and complexity levels. The Berkeley Function Calling Leaderboard (BFCL) provides 2,000 testing cases with step-by-step and end-to-end assessments measuring call accuracy, pass rates, and win rates across increasingly complex scenarios. T-Eval contributes 553 tool-use cases testing multi-turn interactions and nested tool calling capabilities [ 259 , 1380 , 829 ] . Advanced benchmarks including StableToolBench address API instability challenges, while NesTools evaluates nested tool scenarios and ToolHop assesses multi-hop tool usage across 995 queries and 3,912 tools [ 359 , 373 , 1255 ] .

Web agent evaluation frameworks including WebArena and Mind2Web provide comprehensive assessment across thousands of tasks spanning 137 websites, revealing significant performance gaps in current LLM capabilities for complex web interactions. VideoWebArena extends evaluation to multimodal agents, while Deep Research Bench and DeepShop address specialized evaluation for research and shopping agents respectively [ 1368 , 202 , 87 , 476 ] .

Multi-agent system evaluation employs specialized frameworks addressing coordination, communication, and collective intelligence. However, current frameworks face significant challenges in transactional integrity across complex workflows, with many systems lacking adequate compensation mechanisms for partial failures. Orchestration evaluation must address context management, coordination strategy effectiveness, and the ability to maintain system coherence under varying operational conditions [ 128 , 893 ] .

Release Date Open Source Method / Model Success Rate (%) Source

2025-02 × \times × IBM CUGA 61.7 [ 747 ]

2025-01 × \times × OpenAI Operator 58.1 [ 807 ]

2024-08 × \times × Jace.AI 57.1 [ 470 ]

2024-12 × \times × ScribeAgent + GPT-4o 53.0 [ 942 ]

2025-01 ✓ AgentSymbiotic 52.1 [ 1314 ]

2025-01 ✓ Learn-by-Interact 48.0 [ 990 ]

2024-10 ✓ AgentOccam-Judge 45.7 [ 1222 ]

2024-08 × \times × WebPilot 37.2 [ 1322 ]

2024-10 ✓ GUI-API Hybrid Agent 35.8 [ 980 ]

2024-09 ✓ Agent Workflow Memory 35.5 [ 1135 ]

2024-04 ✓ SteP 33.5 [ 971 ]

2025-06 ✓ TTI 26.1 [ 943 ]

2024-04 ✓ BrowserGym + GPT-4 23.5 [ 234 ] 
Table 8 : WebArena [ 1368 ] Leaderboard: Top performing models with their success rates and availability status.

6.3 Evaluation Challenges and Emerging Paradigms

This subsection identifies current limitations in evaluation methodologies and explores emerging approaches for more effective assessment.

6.3.1 Methodological Limitations and Biases

Traditional evaluation metrics prove fundamentally inadequate for capturing the nuanced, dynamic behaviors exhibited by context-engineered systems. Static metrics like BLEU, ROUGE, and perplexity, originally designed for simpler text generation tasks, fail to assess complex reasoning chains, multi-step interactions, and emergent system behaviors. The inherent complexity and interdependencies of multi-component systems create attribution challenges where isolating failures and identifying root causes becomes computationally and methodologically intractable. Future metrics must evolve to capture not just task success, but the quality and robustness of the underlying reasoning process, especially in scenarios requiring compositional generalization and creative problem-solving [ 835 , 1132 ] .

Memory system evaluation faces particular challenges due to the lack of standardized benchmarks and the stateless nature of current LLMs. Automated memory testing frameworks must address the isolation problem where different memory testing stages cannot be effectively separated, leading to unreliable assessment results. Commercial AI assistants demonstrate significant performance degradation during sustained interactions, with accuracy drops of up to 30% highlighting critical gaps in current evaluation methodologies and pointing to the need for longitudinal evaluation frameworks that track memory fidelity over time [ 1330 , 1171 , 457 ] .

Tool-integrated reasoning system evaluation reveals substantial performance gaps between current systems and human-level capabilities. The GAIA benchmark demonstrates that while humans achieve 92% accuracy on general assistant tasks, advanced models like GPT-4 achieve only 15% accuracy, indicating fundamental limitations in current evaluation frameworks and system capabilities [ 772 , 1090 , 126 ] . Evaluation frameworks must address the complexity of multi-tool coordination, error recovery, and adaptive tool selection across diverse operational contexts [ 310 , 931 ] .

6.3.2 Emerging Evaluation Paradigms

Self-refinement evaluation paradigms leverage iterative improvement mechanisms to assess system capabilities across multiple refinement cycles. Frameworks including Self-Refine, Reflexion, and N-CRITICS demonstrate substantial performance improvements through multi-dimensional feedback and ensemble-based evaluation approaches. GPT-4 achieves approximately 20% improvement through self-refinement processes, highlighting the importance of evaluating systems across multiple iteration cycles rather than single-shot assessments. However, a key future challenge lies in evaluating the meta-learning capability itself—not just whether the system improves, but how efficiently and robustly it learns to refine its strategies over time [ 735 , 956 , 789 , 577 ] .

Multi-aspect feedback evaluation incorporates diverse feedback dimensions including correctness, relevance, clarity, and robustness, providing comprehensive assessment of system outputs. Self-rewarding mechanisms enable autonomous evolution and meta-learning assessment, allowing systems to develop increasingly sophisticated evaluation criteria through iterative refinement [ 704 ] .

Criticism-guided evaluation employs specialized critic models to provide detailed feedback on system outputs, enabling fine-grained assessment of reasoning quality, factual accuracy, and logical consistency. These approaches address the limitations of traditional metrics by providing contextual, content-aware evaluation that can adapt to diverse task requirements and output formats [ 789 , 577 ] .

Orchestration evaluation frameworks address the unique challenges of multi-agent coordination by incorporating transactional integrity assessment, context management evaluation, and coordination strategy effectiveness measurement. Advanced frameworks including SagaLLM provide transaction support and independent validation procedures to address the limitations of systems that rely exclusively on LLM self-validation capabilities [ 128 , 390 ] .

6.3.3 Safety and Robustness Assessment

Safety-oriented evaluation incorporates comprehensive robustness testing, adversarial attack resistance, and alignment assessment to ensure responsible development of context-engineered systems. Particular attention must be paid to the evaluation of agentic systems that can operate autonomously across extended periods, as these systems present unique safety challenges that traditional evaluation frameworks cannot adequately address [ 965 , 360 ] .

Robustness evaluation must assess system performance under distribution shifts, input perturbations, and adversarial conditions through comprehensive stress testing protocols. Multi-agent systems face additional challenges in coordination failure scenarios, where partial system failures can cascade through the entire agent network. Evaluation frameworks must address graceful degradation strategies, error recovery protocols, and the ability to maintain system functionality under adverse conditions. Beyond predefined failure modes, future evaluation must grapple with assessing resilience to “unknown unknowns”—emergent and unpredictable failure cascades in highly complex, autonomous multi-agent systems [ 128 , 390 ] .

Alignment evaluation measures system adherence to intended behaviors, value consistency, and beneficial outcome optimization through specialized assessment frameworks. Context engineering systems present unique alignment challenges due to their dynamic adaptation capabilities and complex interaction patterns across multiple components. Long-term evaluation must assess whether systems maintain beneficial behaviors as they adapt and evolve through extended operational periods [ 893 ] .

Looking ahead, the evaluation of context-engineered systems requires a paradigm shift from static benchmarks to dynamic, holistic assessments. Future frameworks must move beyond measuring task success to evaluating compositional generalization for novel problems and tracking long-term autonomy in interactive environments. The development of ’living’ benchmarks that co-evolve with AI capabilities, alongside the integration of socio-technical and economic metrics, will be critical for ensuring these advanced systems are not only powerful but also reliable, efficient, and aligned with human values in real-world applications [ 310 , 1368 , 1330 ] .

The evaluation landscape for context-engineered systems continues evolving rapidly as new architectures, capabilities, and applications emerge. Future evaluation paradigms must address increasing system complexity while providing reliable, comprehensive, and actionable insights for system improvement and deployment decisions. The integration of multiple evaluation approaches—from component-level assessment to system-wide robustness testing—represents a critical research priority for ensuring the reliable deployment of context-engineered systems in real-world applications [ 835 , 1132 ] .

7 Future Directions and Open Challenges

Context Engineering stands at a critical inflection point where foundational advances converge with emerging application demands, creating unprecedented opportunities for innovation while revealing fundamental challenges that require sustained research efforts across multiple dimensions [ 835 , 1132 ] .

As the field transitions from isolated component development toward integrated system architectures, the complexity of research challenges grows exponentially, demanding interdisciplinary approaches that bridge theoretical computer science, practical system engineering, and domain-specific expertise [ 310 , 931 ] .

This section systematically examines key research directions and open challenges that will define the evolution of Context Engineering over the coming decade.

7.1 Foundational Research Challenges

This subsection examines core theoretical and computational challenges that must be addressed to advance context engineering systems beyond current limitations.

7.1.1 Theoretical Foundations and Unified Frameworks

Context Engineering currently operates without unified theoretical foundations that connect disparate techniques and provide principled design guidelines, representing a critical research gap that limits systematic progress and optimal system development.

The absence of mathematical frameworks characterizing context engineering capabilities, limitations, and optimal design principles across different architectural configurations impedes both fundamental understanding and practical optimization [ 1132 , 663 , 835 , 310 ] .

Information-theoretic analysis of context engineering systems requires comprehensive investigation into optimal context allocation strategies, information redundancy quantification, and fundamental compression limits within context windows. Current approaches lack principled methods for determining optimal context composition, leading to suboptimal resource utilization and performance degradation. Research must establish mathematical bounds on context efficiency, develop optimization algorithms for context selection, and create theoretical frameworks for predicting system behavior across varying context configurations [ 731 , 295 ] .

Compositional understanding of context engineering systems demands formal models describing how individual components interact, interfere, and synergize within integrated architectures. The emergence of complex behaviors from component interactions requires systematic investigation through both empirical studies and theoretical modeling approaches. Multi-agent orchestration presents particular challenges in developing mathematical frameworks for predicting coordination effectiveness and emergent collaborative behaviors [ 128 , 893 ] .

7.1.2 Scaling Laws and Computational Efficiency

The fundamental asymmetry between LLMs’ remarkable comprehension capabilities and their pronounced generation limitations represents one of the most critical challenges in Context Engineering research.

This comprehension-generation gap manifests across multiple dimensions including long-form output coherence, factual consistency maintenance, and planning sophistication, requiring investigation into whether limitations stem from architectural constraints, training methodologies, or fundamental computational boundaries [ 835 , 1132 ] .

Long-form generation capabilities demand systematic investigation into planning mechanisms that can maintain coherence across thousands of tokens while preserving factual accuracy and logical consistency. Current systems exhibit significant performance degradation in extended generation tasks, highlighting the need for architectural innovations beyond traditional transformer paradigms. State space models including Mamba demonstrate potential for more efficient long sequence processing through linear scaling properties, though current implementations require substantial development to match transformer performance across diverse tasks [ 731 , 1258 , 347 , 216 ] .

Context scaling efficiency faces fundamental computational challenges, with current attention mechanisms scaling quadratically (O(n²)) with sequence length, creating prohibitive memory and computational requirements for ultra-long sequences. Sliding attention mechanisms and memory-efficient implementations represent promising directions, though significant research is needed to address both computational tractability and reasoning quality preservation [ 295 , 1227 , 347 ] . Position interpolation and extension techniques require advancement to handle sequences exceeding current architectural limitations while maintaining positional understanding and coherence.

7.1.3 Multi-Modal Integration and Representation

The integration of diverse modalities within context engineering systems presents fundamental challenges in representation learning, cross-modal reasoning, and unified architectural design. Current approaches typically employ modality-specific encoders with limited cross-modal interaction, failing to capture the rich interdependencies that characterize sophisticated multi-modal understanding. VideoWebArena demonstrates the complexity of multimodal agent evaluation, revealing substantial performance gaps in current systems when processing video, audio, and text simultaneously [ 476 ] .

Beyond these sensory modalities, context engineering must also handle more abstract forms of information such as graphs, whose structural semantics are not directly interpretable by language models. Capturing the high-level meaning encoded in graph structures introduces unique challenges, including aligning graph representations with language model embeddings and expressing graph topology efficiently. Recent efforts like GraphGPT [ 1024 ] and GraphRAG [ 244 ] attempt to bridge this gap through cross-modal alignment strategies, while others explore converting graphs into natural language descriptions to facilitate model understanding [ 262 , 319 ] . Bi et al. [ 75 ] further propose a divide-and-conquer approach to encode text-attributed heterogeneous networks, addressing context length limitations and enabling effective link prediction. Graph reasoning thus emerges as a core difficulty in context engineering, requiring models to navigate complex relational structures beyond raw modalities.

Temporal reasoning across multi-modal contexts requires sophisticated architectures capable of tracking object persistence, causal relationships, and temporal dynamics across extended sequences. Web agent frameworks including WebArena showcase the challenges of maintaining coherent understanding across complex multi-step interactions involving diverse modalities and dynamic content. Current systems demonstrate significant limitations in coordinating multi-modal information processing with action planning and execution [ 1368 , 202 ] .

Cross-modal alignment and consistency present ongoing challenges in ensuring that information extracted from different modalities remains factually consistent and semantically coherent. Deep Research Bench evaluation reveals that current multi-modal agents struggle with complex research tasks requiring synthesis across textual, visual, and structured data sources, highlighting the need for more sophisticated alignment mechanisms [ 87 ] .

7.2 Technical Innovation Opportunities

This subsection explores emerging technical approaches and architectural innovations that promise to enhance context engineering capabilities.

7.2.1 Next-Generation Architectures

Architectural innovations beyond traditional transformer paradigms offer promising directions for addressing current limitations in context engineering systems. State space models including LongMamba demonstrate potential for more efficient long sequence processing through linear scaling properties and improved memory utilization, though current implementations require substantial development to match transformer performance across diverse tasks [ 1258 , 731 ] . Specialized position encoding methods and parameter-efficient architectures present opportunities for scaling to ultra-long sequences while maintaining computational tractability [ 347 , 295 ] .

Memory-augmented architectures require advancement beyond current external memory mechanisms to enable more sophisticated long-term memory organization, hierarchical memory structures, and adaptive memory management strategies. MemoryBank implementations incorporating Ebbinghaus Forgetting Curve principles demonstrate promising approaches to memory persistence, though significant research is needed to address the fundamental stateless nature of current LLMs [ 1362 , 1330 , 1171 , 813 , 1202 ] . The development of episodic memory systems capable of maintaining coherent long-term context across extended interactions represents a critical architectural challenge [ 457 , 841 , 393 ] .

Modular and compositional architectures enable flexible system construction through specialized component integration while maintaining overall system coherence. Modular RAG architectures demonstrate enhanced flexibility through specialized modules for retrieval, augmentation, and generation, enabling fine-grained optimization of individual components. Graph-enhanced approaches including GraphRAG and LightRAG showcase the potential for integrating structured knowledge representation with neural processing [ 312 , 965 , 360 ] .

7.2.2 Advanced Reasoning and Planning

Context engineering systems require enhanced reasoning capabilities spanning causal reasoning, counterfactual thinking, temporal reasoning, and analogical reasoning across extended contexts. Current systems demonstrate limited capacity for sophisticated reasoning patterns that require integration of multiple evidence sources, consideration of alternative scenarios, and maintenance of logical consistency across complex inference chains [ 1132 , 835 ] .

Multi-step planning and execution capabilities represent critical advancement areas enabling systems to decompose complex tasks, formulate execution strategies, monitor progress, and adapt plans based on intermediate results. Agentic RAG systems demonstrate sophisticated planning and reflection mechanisms requiring integration of task decomposition, multi-plan selection, and iterative refinement capabilities. However, current implementations face significant challenges in maintaining coherence across extended planning horizons and adapting to dynamic information conditions [ 438 , 162 , 1183 ] .

Tool-integrated reasoning represents a paradigmatic advancement requiring dynamic interaction with external resources during reasoning processes. The GAIA benchmark demonstrates substantial performance gaps, with human achievement of 92% accuracy compared to advanced models achieving only 15%, highlighting fundamental limitations in current reasoning and planning capabilities [ 772 , 1090 , 126 ] . Advanced tool integration must address autonomous tool selection, parameter extraction, multi-tool coordination, and error recovery across diverse operational contexts [ 310 , 931 ] .

7.2.3 Complex Context Organization and Solving Graph Problems

Graph reasoning represents a fundamental challenge in context engineering, requiring systems to navigate complex structural relationships while maintaining semantic understanding across interconnected elements. Recent advances in graph-language model integration demonstrate multiple paradigms: specialized architectural approaches that incorporate graph-specific components and text-based encoding strategies that transform graph structures into natural language representations [ 1085 , 1023 ] .

Architectural integration approaches include GraphGPT, which employs dual-stage instruction tuning aligning graph structural information with language tokens via self-supervised graph matching [ 1023 , 741 ] . This framework introduces specialized GraphTokens refined through Graph Instruction Tuning and utilizes a lightweight graph-text alignment projector for transitioning between textual and structural processing modalities [ 1270 , 274 ] . Building upon instruction-tuning paradigms, GraphWiz extends this approach by incorporating DPO to enhance reasoning reliability, achieving 65% average accuracy across diverse graph tasks and significantly outperforming GPT-4’s 43.8% [ 145 ] . Chain-of-thought distillation mechanisms enhance step-by-step reasoning performance [ 1138 , 1391 ] . RL presents another promising direction, as demonstrated by G1, which trains LLMs on synthetic graph-theoretic tasks using the Erdős dataset comprising 50 diverse tasks, achieving strong zero-shot generalization with a 3B parameter model outperforming significantly larger models [ 357 ] .

Text-based encoding approaches transform graph structures into natural language descriptions using few-shot prompting and chain-of-thought reasoning without architectural modifications [ 262 , 192 ] . These methods introduce diverse graph description templates contextualizing structural elements through multiple semantic interpretations [ 936 , 716 ] . Recent work investigates the impact of graph description ordering on LLM performance, revealing that sequential presentation significantly influences model comprehension and reasoning accuracy [ 319 ] . Benchmark evaluations have expanded with GraphArena, offering both polynomial-time tasks and NP-complete challenges with a rigorous evaluation framework that classifies outputs as correct, suboptimal, hallucinatory, or missing [ 1025 ] . Combined with existing benchmarks like NLGraph and GraphDO, these evaluations reveal substantial performance disparities between simple connectivity problems and complex tasks like maximum flow computation [ 1085 , 895 , 319 ] .

Current implementations face challenges in scaling to large structures, maintaining consistency across multi-hop relationships, and generalizing to novel topologies, with text-based approaches offering interpretability at reduced structural precision while specialized architectures provide enhanced performance through increased complexity [ 889 , 1100 ] . Emerging hybrid approaches including InstructGraph and GraphAdapter attempt to bridge these paradigms through structured format verbalizers and GNN-based adapters, though limitations persist in handling dynamic structures and temporal evolution of relationships [ 261 ] . Looking forward, broad connection paradigms that organize information through associative networks rather than fragmented searches, spreading outward from central nodes to discover potential connections between entities, may represent the next generation of RAG systems for complex context organization [ 131 ] .

7.2.4 Intelligent Context Assembly and Optimization

Automated context engineering systems capable of intelligently assembling contexts from available components represent a critical research frontier requiring development of context optimization algorithms, adaptive selection strategies, and learned assembly functions. Current approaches rely heavily on heuristic methods and domain-specific engineering, limiting scalability and optimality across diverse applications [ 1132 , 663 ] .

Self-refinement mechanisms demonstrate substantial potential for intelligent context optimization through iterative improvement processes. Self-Refine, Reflexion, and N-CRITICS frameworks achieve significant performance improvements, with GPT-4 demonstrating approximately 20% improvement through iterative refinement. However, these approaches require advancement in optimization strategies for autonomous evolution and meta-learning across diverse contexts [ 735 , 956 , 789 , 577 ] .

Multi-dimensional feedback mechanisms incorporating diverse feedback dimensions including correctness, relevance, clarity, and robustness provide promising directions for context optimization. Self-rewarding mechanisms enable autonomous evolution capabilities, though research must address fundamental questions about optimal adaptation rates, stability-plasticity trade-offs, and preservation of beneficial adaptations across varying operational conditions [ 704 ] .

7.3 Application-Driven Research Directions

This subsection addresses research challenges arising from real-world deployment requirements and domain-specific applications.

7.3.1 Domain Specialization and Adaptation

Context engineering systems require sophisticated specialization mechanisms for diverse domains including healthcare, legal analysis, scientific research, education, and engineering applications, each presenting unique requirements for knowledge integration, reasoning patterns, safety considerations, and regulatory compliance. Domain-specific optimization demands investigation into transfer learning strategies, domain adaptation techniques, and specialized training paradigms that preserve general capabilities while enhancing domain-specific performance [ 1132 , 663 ] .

Scientific research applications require sophisticated reasoning capabilities over complex technical content, mathematical expressions, experimental data, and theoretical frameworks while maintaining rigorous accuracy standards. Deep Research Bench evaluation reveals significant challenges in current systems’ ability to conduct complex research tasks requiring synthesis across multiple information sources and reasoning over technical content. Research must address integration of symbolic reasoning with neural approaches and incorporation of domain-specific knowledge bases [ 87 ] .

Healthcare applications demand comprehensive safety evaluation frameworks, regulatory compliance mechanisms, privacy protection protocols, and integration with existing clinical workflows while maintaining interpretability and auditability requirements. Medical context engineering must address challenges in handling sensitive information, ensuring clinical accuracy, supporting diagnostic reasoning, and maintaining patient privacy across complex healthcare ecosystems. Current evaluation frameworks reveal substantial gaps in medical reasoning capabilities and safety assessment methodologies [ 386 ] .

7.3.2 Large-Scale Multi-Agent Coordination

Scaling multi-agent context engineering systems to hundreds or thousands of participating agents requires development of distributed coordination mechanisms, efficient communication protocols, and hierarchical management structures that maintain system coherence while enabling local autonomy. Research must address fundamental challenges in distributed consensus, fault tolerance, and emergent behavior prediction in large-scale agent populations [ 239 , 140 ] .

Communication protocol standardization represents a critical research frontier, with emerging protocols including MCP (“USB-C for AI”), A2A (Agent-to-Agent), ACP (Agent Communication Protocol), and ANP (Agent Network Protocol) demonstrating the need for unified frameworks enabling interoperability across diverse agent ecosystems. However, current implementations face security vulnerabilities and scalability limitations that must be addressed for large-scale deployment [ 37 , 1007 , 462 , 1 , 246 , 926 , 616 ] .

Orchestration challenges including transactional integrity, context management, and coordination strategy effectiveness represent significant obstacles to large-scale multi-agent deployment. Contemporary frameworks including LangGraph, AutoGen, and CAMEL demonstrate insufficient transaction support and validation limitations, requiring systems that rely exclusively on LLM self-validation capabilities. Advanced coordination frameworks must address compensation mechanisms for partial failures and maintain system coherence under varying operational conditions [ 128 , 390 , 893 ] .

7.3.3 Human-AI Collaboration and Integration

Sophisticated human-AI collaboration frameworks require deep understanding of human cognitive processes, communication preferences, trust dynamics, and collaboration patterns to enable effective hybrid teams that leverage complementary strengths. Research must investigate optimal task allocation strategies, communication protocols, and shared mental model development between humans and AI systems [ 1132 , 835 ] .

Web agent evaluation frameworks reveal significant challenges in human-AI collaboration, particularly in complex task scenarios requiring sustained interaction and coordination. WebArena and Mind2Web demonstrate that current systems struggle with multi-step interactions across diverse websites, highlighting fundamental gaps in collaborative task execution. Advanced interfaces require investigation into context-aware adaptation and personalization mechanisms that enhance human-AI team performance [ 1368 , 202 ] .

Trust calibration and transparency mechanisms represent critical research areas for ensuring appropriate human reliance on AI systems while maintaining human agency and decision-making authority. Evaluation frameworks must address explanation generation, uncertainty communication, and confidence calibration to support informed human decision-making in collaborative scenarios. The substantial performance gaps revealed by benchmarks like GAIA underscore the importance of developing systems that can effectively communicate their limitations and capabilities [ 772 , 1090 ] .

7.4 Deployment and Societal Impact Considerations

This subsection examines critical considerations for deploying context engineering systems at scale while ensuring responsible and beneficial outcomes.

7.4.1 Scalability and Production Deployment

Production deployment of context engineering systems requires addressing scalability challenges across multiple dimensions including computational resource management, latency optimization, throughput maximization, and cost efficiency while maintaining consistent performance across diverse operational conditions. The O(n²) scaling limitation of current attention mechanisms creates substantial barriers to deploying ultra-long context systems in production environments, necessitating advancement in memory-efficient architectures and sliding attention mechanisms [ 295 , 1227 ] .

Reliability and fault tolerance mechanisms become critical as context engineering systems assume increasingly important roles in decision-making processes across domains. Multi-agent orchestration frameworks face particular challenges in maintaining transactional integrity across complex workflows, with current systems lacking adequate compensation mechanisms for partial failures. Research must address graceful degradation strategies, error recovery protocols, and redundancy mechanisms that maintain system functionality under adverse conditions [ 128 , 390 ] .

Maintainability and evolution challenges require investigation into system versioning, backward compatibility, continuous integration protocols, and automated testing frameworks that support ongoing system improvement without disrupting deployed services. Memory system implementations face additional challenges due to the stateless nature of current LLMs and the lack of standardized benchmarks for long-term memory persistence and retrieval efficiency [ 1330 , 1171 ] .

7.4.2 Safety, Security, and Robustness

Comprehensive safety evaluation requires development of assessment frameworks that can identify potential failure modes, safety violations, and unintended behaviors across the full spectrum of context engineering system capabilities. Agentic systems present particular safety challenges due to their autonomous operation capabilities and complex interaction patterns across extended operational periods [ 965 , 360 ] .

Security considerations encompass protection against adversarial attacks, data poisoning, prompt injection, model extraction, and privacy violations while maintaining system functionality and usability. Multi-agent communication protocols including MCP, A2A, and ACP introduce security vulnerabilities that must be addressed while preserving interoperability and functionality. Research must develop defense mechanisms and detection systems that address evolving threat landscapes across distributed agent networks [ 246 , 926 ] .

Alignment and value specification challenges require investigation into methods for ensuring context engineering systems behave according to intended objectives while avoiding specification gaming, reward hacking, and goal misalignment. Context engineering systems present unique alignment challenges due to their dynamic adaptation capabilities and complex interaction patterns across multiple components. The substantial performance gaps revealed by evaluation frameworks underscore the importance of developing robust alignment mechanisms that can maintain beneficial behaviors as systems evolve and adapt [ 772 , 128 ] .

7.4.3 Ethical Considerations and Responsible Development

Bias mitigation and fairness evaluation require comprehensive assessment frameworks that can identify and address systematic biases across different demographic groups, application domains, and use cases while maintaining system performance and utility. Research must investigate bias sources in training data, model architectures, and deployment contexts while developing mitigation strategies that address root causes rather than symptoms [ 1132 , 835 ] .

Privacy protection mechanisms must address challenges in handling sensitive information, preventing data leakage, and maintaining user privacy while enabling beneficial system capabilities. Memory systems face particular privacy challenges due to their persistent information storage and retrieval capabilities, requiring advanced frameworks for secure memory management and selective forgetting mechanisms [ 1330 , 457 ] .

Transparency and accountability frameworks require development of explanation systems, audit mechanisms, and governance structures that enable responsible oversight of context engineering systems while supporting innovation and beneficial applications. The substantial performance gaps revealed by evaluation frameworks like GAIA (human 92% vs AI 15%) highlight the importance of transparent capability communication and appropriate expectation setting for deployed systems [ 772 , 1090 ] .

The future of Context Engineering will be shaped by our ability to address these interconnected challenges through sustained, collaborative research efforts that bridge technical innovation with societal considerations.

Success will require continued investment in fundamental research, interdisciplinary collaboration, and responsible development practices that ensure context engineering systems remain beneficial, reliable, and aligned with human values as they become increasingly integrated into critical societal functions [ 835 , 1132 , 310 ] .

8 Conclusion

This survey has presented the first comprehensive examination of Context Engineering as a formal discipline that systematically designs, optimizes, and manages information payloads for LLMs. Through our analysis of over 1400 research papers, we have established Context Engineering as a critical foundation for developing sophisticated AI systems that effectively integrate external knowledge, maintain persistent memory, and interact dynamically with complex environments.

Our primary contribution lies in introducing a unified taxonomic framework that organizes context engineering techniques into Foundational Components (Context Retrieval and Generation, Context Processing, and Context Management) and System Implementations (Retrieval-Augmented Generation, Memory Systems, Tool-Integrated Reasoning, and Multi-Agent Systems). This framework demonstrates how core technical capabilities integrate into sophisticated architectures addressing real-world requirements.

Through this systematic examination, we have identified several key insights. First, we observe a fundamental asymmetry between LLMs’ remarkable capabilities in understanding complex contexts and their limitations in generating equally sophisticated outputs. This comprehension-generation gap represents one of the most critical challenges facing the field. Second, our analysis reveals increasingly sophisticated integration patterns where multiple techniques combine synergistically, creating capabilities that exceed their individual components. Third, we observe a clear trend toward modularity and compositionality, enabling flexible architectures adaptable to diverse applications while maintaining system coherence. The evaluation challenges we identified underscore the need for comprehensive assessment frameworks that capture the complex, dynamic behaviors exhibited by context-engineered systems. Traditional evaluation methodologies prove insufficient for systems that integrate multiple components, exhibit adaptive behaviors, and operate across extended time horizons. Our examination of future research directions reveals significant opportunities including developing next-generation architectures for efficient long context handling, creating intelligent context assembly systems, and advancing multi-agent coordination mechanisms. Key challenges span theoretical foundations, technical implementation, and practical deployment, including the lack of unified theoretical frameworks, scaling limitations, and safety considerations.

Looking toward the future, Context Engineering stands poised to play an increasingly central role in AI development as the field moves toward complex, multi-component systems. The interdisciplinary nature of Context Engineering necessitates collaborative research approaches spanning computer science, cognitive science, linguistics, and domain-specific expertise.

As LLMs continue to evolve, the fundamental insight underlying Context Engineering—that AI system performance is fundamentally determined by contextual information—will remain central to artificial intelligence development. This survey provides both a comprehensive snapshot of the current state and a roadmap for future research, establishing Context Engineering as a distinct discipline with its own principles, methodologies, and challenges to foster innovation and support responsible development of context-aware AI systems.

Acknowledgments

This survey represents an ongoing effort to comprehensively map the rapidly evolving landscape of Context Engineering for Large Language Models. Given the dynamic nature of this field, with new developments emerging continuously, we acknowledge that despite our best efforts, some recent works or emerging trends may have been inadvertently overlooked or underrepresented. We welcome feedback from the research community to help improve future iterations of this work. We are grateful to the broader research community whose foundational contributions have made this survey possible. This work would not have been achievable without the invaluable support of both the research community and the open-source community, whose collaborative efforts in developing frameworks, tools, and resources have significantly advanced the field of Context Engineering.

References

- [1] Anp-agent communication meta-protocol specification(draft). https://agent-network-protocol.com/specs/communication.html . [Online; accessed 17-July-2025].

- A. [2022] S. A. Automating human evaluation of dialogue systems. North American Chapter of the Association for Computational Linguistics , 2022.

- Abdaljalil et al. [2025] Samir Abdaljalil, Hasan Kurban, Khalid A. Qaraqe, and E. Serpedin. Theorem-of-thought: A multi-agent framework for abductive, deductive, and inductive reasoning in language models. arXiv preprint, 2025.

- Abdallah et al. [2025] Abdelrahman Abdallah, Bhawna Piryani, Jamshid Mozafari, Mohammed Ali, and Adam Jatowt. Rankify: A comprehensive python toolkit for retrieval, re-ranking, and retrieval-augmented generation, arXiv preprint arXiv:2502.02464, 2025. URL https://arxiv.org/abs/2502.02464v3 .

- Abdelaziz et al. [2024] Ibrahim Abdelaziz, Kinjal Basu, Mayank Agarwal, Sadhana Kumaravel, Matt Stallone, Rameswar Panda, Yara Rizk, G. Bhargav, M. Crouse, Chulaka Gunasekara, S. Ikbal, Sachin Joshi, Hima P. Karanam, Vineet Kumar, Asim Munawar, S. Neelam, Dinesh Raghu, Udit Sharma, Adriana Meza Soria, Dheeraj Sreedhar, P. Venkateswaran, Merve Unuvar, David Cox, S. Roukos, Luis A. Lastras, and P. Kapanipathi. Granite-function calling model: Introducing function calling abilities via multi-task learning of granular tasks. Conference on Empirical Methods in Natural Language Processing , 2024.

- Acharya et al. [2025] D. Acharya, Karthigeyan Kuppan, and Divya Bhaskaracharya. Agentic ai: Autonomous intelligence for complex goals—a comprehensive survey. IEEE Access , 2025.

- Acharya et al. [2018] Manoj Acharya, Kushal Kafle, and Christopher Kanan. Tallyqa: Answering complex counting questions. AAAI Conference on Artificial Intelligence , 2018.

- Acharya et al. [2024] Shantanu Acharya, Fei Jia, and Boris Ginsburg. Star attention: Efficient llm inference over long sequences, arXiv preprint arXiv:2411.17116, 2024. URL https://arxiv.org/abs/2411.17116v3 .

- Acikgoz et al. [2025] Emre Can Acikgoz, Jeremy Greer, Akul Datta, Ze Yang, William Zeng, Oussama Elachqar, Emmanouil Koukoumidis, Dilek Hakkani-Tur, and Gokhan Tur. Can a single model master both multi-turn conversations and tool use? coalm: A unified conversational agentic language model, arXiv preprint arXiv:2502.08820, 2025. URL https://arxiv.org/abs/2502.08820v3 .

- Acikgoz et al. [20252] Emre Can Acikgoz, Cheng Qian, Hongru Wang, Vardhan Dongre, Xiusi Chen, Heng Ji, Dilek Hakkani-Tur, and Gokhan Tur. A desideratum for conversational agents: Capabilities, challenges, and future directions, arXiv preprint arXiv:2504.16939, 20252. URL https://arxiv.org/abs/2504.16939v1 .

- Afzal et al. [2024] Anum Afzal, Juraj Vladika, Gentrit Fazlija, Andrei Staradubets, and Florian Matthes. Towards optimizing a retrieval augmented generation using large language model on academic data. International Conference on Natural Language Processing and Information Retrieval , 2024.

- Agarwal et al. [2023] Ankush Agarwal, Sakharam Gawade, A. Azad, and P. Bhattacharyya. Kitlm: Domain-specific knowledge integration into language models for question answering. ICON , 2023.

- Agarwal et al. [2020] Oshin Agarwal, Heming Ge, Siamak Shakeri, and Rami Al-Rfou. Large scale knowledge graph based synthetic corpus generation for knowledge-enhanced language model pre-training. arXiv preprint, 2020.

- Agrawal et al. [2022] Monica Agrawal, S. Hegselmann, Hunter Lang, Yoon Kim, and D. Sontag. Large language models are few-shot clinical information extractors. Conference on Empirical Methods in Natural Language Processing , 2022.

- Ahmadi et al. [2025] Arash Ahmadi, S. Sharif, and Yaser Mohammadi Banadaki. Mcp bridge: A lightweight, llm-agnostic restful proxy for model context protocol servers, arXiv preprint arXiv:2504.08999, 2025. URL https://arxiv.org/abs/2504.08999v1 .

- Ainslie et al. [2023] J. Ainslie, J. Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebr’on, and Sumit K. Sanghai. Gqa: Training generalized multi-query transformer models from multi-head checkpoints. Conference on Empirical Methods in Natural Language Processing , 2023.

- Al-Jumaily [2006] Adel Al-Jumaily. Multi-agent system concepts theory and application phases. arXiv preprint, 2006.

- Al-Khateeb et al. [2023] Faisal Al-Khateeb, Nolan Dey, Daria Soboleva, and Joel Hestness. Position interpolation improves alibi extrapolation. arXiv preprint, 2023.

- Alayrac et al. [2022] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, A. Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andy Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, O. Vinyals, Andrew Zisserman, and K. Simonyan. Flamingo: a visual language model for few-shot learning. Neural Information Processing Systems , 2022.

- Albrecht and Stone [2017] Stefano V. Albrecht and P. Stone. Autonomous agents modelling other agents: A comprehensive survey and open problems. Artificial Intelligence , 2017.

- AlMulla et al. [2025] Buthayna AlMulla, Maram Assi, and Safwat Hassan. Understanding the challenges and promises of developing generative ai apps: An empirical study, arXiv preprint arXiv:2506.16453, 2025. URL https://arxiv.org/abs/2506.16453v2 .

- Alsuhaibani et al. [2021] Reem S. Alsuhaibani, Christian D. Newman, M. J. Decker, Michael L. Collard, and Jonathan I. Maletic. On the naming of methods: A survey of professional developers. International Conference on Software Engineering , 2021.

- Alzetta et al. [2020] Francesco Alzetta, P. Giorgini, A. Najjar, M. Schumacher, and Davide Calvaresi. In-time explainability in multi-agent systems: Challenges, opportunities, and roadmap. EXTRAAMAS@AAMAS , 2020.

- Amara et al. [2024] Kenza Amara, Lukas Klein, Carsten T. Lüth, Paul F. Jäger, Hendrik Strobelt, and Mennatallah El-Assady. Why context matters in vqa and reasoning: Semantic interventions for vlm input modalities, arXiv preprint arXiv:2410.01690v1, 2024. URL https://arxiv.org/abs/2410.01690v1 .

- Amatriain [2024] Xavier Amatriain. Prompt design and engineering: Introduction and advanced methods, arXiv preprint arXiv:2401.14423, 2024. URL https://arxiv.org/abs/2401.14423v4 .

- Aminiranjbar et al. [2024] Zahra Aminiranjbar, Jianan Tang, Qiudan Wang, Shubha Pant, and Mahesh Viswanathan. Dawn: Designing distributed agents in a worldwide network, arXiv preprint arXiv:2410.22339, 2024. URL https://arxiv.org/abs/2410.22339v3 .

- An et al. [2024] Chenxin An, Jun Zhang, Ming Zhong, Lei Li, Shansan Gong, Yao Luo, Jingjing Xu, and Lingpeng Kong. Why does the effective context length of llms fall short? International Conference on Learning Representations , 2024.

- An et al. [20242] Kaikai An, Fangkai Yang, Liqun Li, Junting Lu, Sitao Cheng, Shuzheng Si, Lu Wang, Pu Zhao, Lele Cao, Qingwei Lin, et al. Thread: A logic-based data organization paradigm for how-to question answering with retrieval augmented generation. arXiv preprint arXiv:2406.13372 , 20242.

- An et al. [20243] Kaikai An, Fangkai Yang, Junting Lu, Liqun Li, Zhixing Ren, Hao Huang, Lu Wang, Pu Zhao, Yu Kang, Hua Ding, et al. Nissist: An incident mitigation copilot based on troubleshooting guides. In Proceedings of the 27th European Conference on Artificial Intelligence (ECAI 2024) , pages 4471–4474, 20243.

- An et al. [2025] Kaikai An, Li Sheng, Ganqu Cui, Shuzheng Si, Ning Ding, Yu Cheng, and Baobao Chang. Ultraif: Advancing instruction following from the wild. pages 7930–7957, 2025.

- An et al. [20252] Sumin An, Junyoung Sung, Wonpyo Park, Chanjun Park, and Paul Hongsuck Seo. Lcirc: A recurrent compression approach for efficient long-form context and query dependent modeling in llms. North American Chapter of the Association for Computational Linguistics , 20252.

- Anagnostidis et al. [2023] Sotiris Anagnostidis, Dario Pavllo, Luca Biggio, Lorenzo Noci, Aurélien Lucchi, and Thomas Hofmann. Dynamic context pruning for efficient and interpretable autoregressive transformers. Neural Information Processing Systems , 2023.

- Anderson et al. [1997] John R. Anderson, M. Matessa, and C. Lebiere. Act-r: A theory of higher level cognition and its relation to visual attention. Hum. Comput. Interact. , 1997.

- Andreas [2022] Jacob Andreas. Language models as agent models. Conference on Empirical Methods in Natural Language Processing , 2022.

- Aniello et al. [2013] Leonardo Aniello, R. Baldoni, and Leonardo Querzoni. Adaptive online scheduling in storm. Distributed Event-Based Systems , 2013.

- Anokhin et al. [2024] Petr Anokhin, Nikita Semenov, Artyom Sorokin, Dmitry Evseev, M. Burtsev, and Evgeny Burnaev. Arigraph: Learning knowledge graph world models with episodic memory for llm agents, arXiv preprint arXiv:2407.04363, 2024. URL https://arxiv.org/abs/2407.04363v3 .

- Anthropic [2024] Anthropic. Introducing the model context protocol, November 2024. URL https://www.anthropic.com/news/model-context-protocol . [Online; accessed 17-July-2025].

- Aratchige and Ilmini [2025] RM Aratchige and Dr. Wmks Ilmini. Llms working in harmony: A survey on the technological aspects of building effective llm-based multi agent systems, arXiv preprint arXiv:2504.01963, 2025. URL https://arxiv.org/abs/2504.01963v1 .

- Ardon et al. [2023] Leo Ardon, Daniel Furelos-Blanco, and A. Russo. Learning reward machines in cooperative multi-agent tasks. AAMAS Workshops , 2023.

- Armeni et al. [2022] K. Armeni, C. Honey, and Tal Linzen. Characterizing verbatim short-term memory in neural language models. Conference on Computational Natural Language Learning , 2022.

- Asai et al. [2023] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. Self-rag: Learning to retrieve, generate, and critique through self-reflection. International Conference on Learning Representations , 2023.

- Asano et al. [2025] Hikaru Asano, Tadashi Kozuno, and Yukino Baba. Self iterative label refinement via robust unlabeled learning, arXiv preprint arXiv:2502.12565, 2025. URL https://arxiv.org/abs/2502.12565v1 .

- Athiwaratkun et al. [2024] Ben Athiwaratkun, Sujan Kumar Gonugondla, Sanjay Krishna Gouda, Haifeng Qian, Hantian Ding, Qing Sun, Jun Wang, Jiacheng Guo, Liangfu Chen, Parminder Bhatia, Ramesh Nallapati, Sudipta Sengupta, and Bing Xiang. Bifurcated attention: Accelerating massively parallel decoding with shared prefixes in llms, arXiv preprint arXiv:2403.08845, 2024. URL https://arxiv.org/abs/2403.08845v2 .

- Ayalasomayajula et al. [2024] Avinash Ayalasomayajula, Rui Guo, Jingbo Zhou, Sujan Kumar Saha, and Farimah Farahmandi. Lasp: Llm assisted security property generation for soc verification. Workshop on Machine Learning for CAD , 2024.

- Aytes et al. [2025] Simon A. Aytes, Jinheon Baek, and Sung Ju Hwang. Sketch-of-thought: Efficient llm reasoning with adaptive cognitive-inspired sketching. arXiv preprint, 2025.

- Azad et al. [2023] Bobby Azad, Reza Azad, Sania Eskandari, Afshin Bozorgpour, A. Kazerouni, I. Rekik, and D. Merhof. Foundational models in medical imaging: A comprehensive survey and future vision, arXiv preprint arXiv:2310.18689, 2023. URL https://arxiv.org/abs/2310.18689v1 .

- Badaro et al. [2023] Gilbert Badaro, Mohammed Saeed, and Paolo Papotti. Transformers for tabular data representation: A survey of models and applications. Transactions of the Association for Computational Linguistics , 2023.

- Baek et al. [2023] Jinheon Baek, N. Chandrasekaran, Silviu Cucerzan, Allen Herring, and S. Jauhar. Knowledge-augmented large language models for personalized contextual query suggestion. The Web Conference , 2023.

- Bai et al. [2024] Tianyi Bai, Hao Liang, Binwang Wan, Ling Yang, Bozhou Li, Yifan Wang, Bin Cui, Conghui He, Binhang Yuan, and Wentao Zhang. A survey of multimodal large language model from a data-centric perspective, arXiv preprint arXiv:2405.16640v2, 2024. URL https://arxiv.org/abs/2405.16640v2 .

- Bai et al. [20242] Yu Bai, Xiyuan Zou, Heyan Huang, Sanxing Chen, Marc-Antoine Rondeau, Yang Gao, and Jackie Chi Kit Cheung. Citrus: Chunked instruction-aware state eviction for long sequence modeling. Conference on Empirical Methods in Natural Language Processing , 20242.

- Bai et al. [2022] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, and Jared Kaplan. Constitutional ai: Harmlessness from ai feedback, arXiv preprint arXiv:2212.08073, 2022. URL https://arxiv.org/abs/2212.08073 .

- Bakkali et al. [2023] Souhail Bakkali, Sanket Biswas, Zuheng Ming, Mickaël Coustaty, Marccal Rusinol, O. R. Terrades, and Josep Llad’os. Globaldoc: A cross-modal vision-language framework for real-world document image retrieval and classification. IEEE Workshop/Winter Conference on Applications of Computer Vision , 2023.

- Bandlamudi et al. [2023] Jayachandu Bandlamudi, K. Mukherjee, Prerna Agarwal, Sampath Dechu, Siyu Huo, Vatche Isahagian, Vinod Muthusamy, N. Purushothaman, and Renuka Sindhgatta. Towards hybrid automation by bootstrapping conversational interfaces for it operation tasks. AAAI Conference on Artificial Intelligence , 2023.

- Bandlamudi et al. [2024] Jayachandu Bandlamudi, Kushal Mukherjee, Prerna Agarwal, Ritwik Chaudhuri, R. Pimplikar, Sampath Dechu, Alex Straley, Anbumunee Ponniah, and Renuka Sindhgatta. Building conversational artifacts to enable digital assistant for apis and rpas. AAAI Conference on Artificial Intelligence , 2024.

- Bao et al. [2024] Keqin Bao, Jizhi Zhang, Xinyu Lin, Yang Zhang, Wenjie Wang, and Fuli Feng. Large language models for recommendation: Past, present, and future. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 2024.

- Bartolomeo et al. [2023] Sara Di Bartolomeo, Giorgio Severi, V. Schetinger, and Cody Dunne. Ask and you shall receive (a graph drawing): Testing chatgpt’s potential to apply graph layout algorithms. Eurographics Conference on Visualization , 2023.

- Barua [2024] Saikat Barua. Exploring autonomous agents through the lens of large language models: A review, arXiv preprint arXiv:2404.04442, 2024. URL https://arxiv.org/abs/2404.04442v1 .

- Basu et al. [2024] Kinjal Basu, Ibrahim Abdelaziz, Kelsey Bradford, M. Crouse, Kiran Kate, Sadhana Kumaravel, Saurabh Goyal, Asim Munawar, Yara Rizk, Xin Wang, Luis A. Lastras, and P. Kapanipathi. Nestful: A benchmark for evaluating llms on nested sequences of api calls, arXiv preprint arXiv:2409.03797, 2024. URL https://arxiv.org/abs/2409.03797v3 .

- Beheshti [2024] Amin Beheshti. Natural language-oriented programming (nlop): Towards democratizing software creation. 2024 IEEE International Conference on Software Services Engineering (SSE) , 2024.

- Beiranvand and Vahidipour [2025] Azadeh Beiranvand and S. M. Vahidipour. Integrating structural and semantic signals in text-attributed graphs with bigtex, arXiv preprint arXiv:2504.12474, 2025. URL https://arxiv.org/abs/2504.12474v2 .

- Ben-Kish et al. [2024] Assaf Ben-Kish, Itamar Zimerman, Shady Abu-Hussein, Nadav Cohen, Amir Globerson, Lior Wolf, and Raja Giryes. Decimamba: Exploring the length extrapolation potential of mamba. International Conference on Learning Representations , 2024.

- Ben-Kish et al. [2025] Assaf Ben-Kish, Itamar Zimerman, M. J. Mirza, James R. Glass, Leonid Karlinsky, and Raja Giryes. Overflow prevention enhances long-context recurrent llms. arXiv preprint, 2025.

- Benna and Fusi [2015] M. Benna and Stefano Fusi. Complex synapses as efficient memory systems. BMC Neuroscience , 2015.

- Benna and Fusi [20152] M. Benna and Stefano Fusi. Computational principles of biological memory, arXiv preprint arXiv:1507.07580, 20152. URL https://arxiv.org/abs/1507.07580v1 .

- Bensal et al. [2025] Shelly Bensal, Umar Jamil, Christopher Bryant, M. Russak, Kiran Kamble, Dmytro Mozolevskyi, Muayad Ali, and Waseem Alshikh. Reflect, retry, reward: Self-improving llms via reinforcement learning, arXiv preprint arXiv:2505.24726, 2025. URL https://arxiv.org/abs/2505.24726v1 .

- Berges et al. [2008] Idoia Berges, J. Bermúdez, A. Goñi, and A. Illarramendi. Semantic web technology for agent communication protocols. Extended Semantic Web Conference , 2008.

- Beri and Srivastava [2024] Gaurav Beri and Vaishnavi Srivastava. Advanced techniques in prompt engineering for large language models: A comprehensive study. 2024 IEEE 4th International Conference on ICT in Business Industry & Government (ICTBIG) , 2024.

- Bertsch et al. [2023] Amanda Bertsch, Uri Alon, Graham Neubig, and Matthew R. Gormley. Unlimiformer: Long-range transformers with unlimited length input. Neural Information Processing Systems , 2023.

- Besta et al. [2023] Maciej Besta, Nils Blach, Aleš Kubíček, Robert Gerstenberger, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Michal Podstawski, H. Niewiadomski, P. Nyczyk, and Torsten Hoefler. Graph of thoughts: Solving elaborate problems with large language models. AAAI Conference on Artificial Intelligence , 2023.

- Betz and Richardson [2022] Gregor Betz and Kyle Richardson. Judgment aggregation, discursive dilemma and reflective equilibrium: Neural language models as self-improving doxastic agents. Frontiers in Artificial Intelligence , 2022.

- Bezalel et al. [2024] L. Bezalel, Eyal Orgad, and Amir Globerson. Teaching models to improve on tape. AAAI Conference on Artificial Intelligence , 2024.

- Bhatt et al. [2025] Umang Bhatt, Sanyam Kapoor, Mihir Upadhyay, Ilia Sucholutsky, Francesco Quinzan, Katherine M. Collins, Adrian Weller, Andrew Gordon Wilson, and Muhammad Bilal Zafar. When should we orchestrate multiple agents?, arXiv preprint arXiv:2503.13577, 2025. URL https://arxiv.org/abs/2503.13577v1 .

- Bi et al. [2024] Baolong Bi, Shaohan Huang, Yiwei Wang, Tianchi Yang, Zihan Zhang, Haizhen Huang, Lingrui Mei, Junfeng Fang, Zehao Li, Furu Wei, et al. Context-dpo: Aligning language models for context-faithfulness. ACL 2025 , 2024.

- Bi et al. [20242] Baolong Bi, Shenghua Liu, Lingrui Mei, Yiwei Wang, Pengliang Ji, and Xueqi Cheng. Decoding by contrasting knowledge: Enhancing llms’ confidence on edited facts. ACL 2025 , 20242.

- Bi et al. [20243] Baolong Bi, Shenghua Liu, Yiwei Wang, Lingrui Mei, and Xueqi Cheng. Lpnl: Scalable link prediction with large language models. ACL 2024 , 20243.

- Bi et al. [20244] Baolong Bi, Shenghua Liu, Yiwei Wang, Lingrui Mei, Hongcheng Gao, Junfeng Fang, and Xueqi Cheng. Struedit: Structured outputs enable the fast and accurate knowledge editing for large language models. 20244.

- Bi et al. [20245] Baolong Bi, Shenghua Liu, Yiwei Wang, Lingrui Mei, Hongcheng Gao, Yilong Xu, and Xueqi Cheng. Adaptive token biaser: Knowledge editing via biasing key entities. EMNLP 2024 , 20245.

- Bi et al. [2025] Baolong Bi, Shenghua Liu, Xingzhang Ren, Dayiheng Liu, Junyang Lin, Yiwei Wang, Lingrui Mei, Junfeng Fang, Jiafeng Guo, and Xueqi Cheng. Refinex: Learning to refine pre-training data at scale from expert-guided programs. 2025.

- Bi et al. [20252] Baolong Bi, Shenghua Liu, Yiwei Wang, Lingrui Mei, Junfeng Fang, Hongcheng Gao, Shiyu Ni, and Xueqi Cheng. Is factuality enhancement a free lunch for llms? better factuality can lead to worse context-faithfulness. ICLR 2025 , 20252.

- Bi et al. [20253] Baolong Bi, Shenghua Liu, Yiwei Wang, Yilong Xu, Junfeng Fang, Lingrui Mei, and Xueqi Cheng. Parameters vs. context: Fine-grained control of knowledge reliance in language models. 20253.

- Bi et al. [2020] Bin Bi, Chenliang Li, Chen Wu, Ming Yan, and Wei Wang. Palm: Pre-training an autoencoding&autoregressive language model for context-conditioned generation. Conference on Empirical Methods in Natural Language Processing , 2020.

- Bien et al. [2009] Dinh Doan Van Bien, David Lillis, and Rem W. Collier. Call graph profiling for multi agent systems. Multi-Agent Logics, Languages, and Organisations Federated Workshops , 2009.

- Bode et al. [2024] Jonas Bode, Bastian Pätzold, Raphael Memmesheimer, and Sven Behnke. A comparison of prompt engineering techniques for task planning and execution in service robotics. IEEE-RAS International Conference on Humanoid Robots , 2024.

- Bonzon [2023] P. Bonzon. Grounding mental representations in a virtual multi-level functional framework. Journal of Cognition , 2023.

- Borgeaud et al. [2021] Sebastian Borgeaud, A. Mensch, Jordan Hoffmann, Trevor Cai, Eliza Rutherford, Katie Millican, George van den Driessche, Jean-Baptiste Lespiau, Bogdan Damoc, Aidan Clark, Diego de Las Casas, Aurelia Guy, Jacob Menick, Roman Ring, T. Hennigan, Saffron Huang, Lorenzo Maggiore, Chris Jones, Albin Cassirer, Andy Brock, Michela Paganini, G. Irving, O. Vinyals, Simon Osindero, K. Simonyan, Jack W. Rae, Erich Elsen, and L. Sifre. Improving language models by retrieving from trillions of tokens. International Conference on Machine Learning , 2021.

- Borsos et al. [2022] Zalán Borsos, Raphaël Marinier, Damien Vincent, E. Kharitonov, O. Pietquin, Matthew Sharifi, Dominik Roblek, O. Teboul, David Grangier, M. Tagliasacchi, and Neil Zeghidour. Audiolm: A language modeling approach to audio generation. IEEE/ACM Transactions on Audio Speech and Language Processing , 2022.

- Bosse et al. [2025] FutureSearch Nikos I. Bosse, Jon Evans, Robert G. Gambee, Daniel Hnyk, Peter Muhlbacher, Lawrence Phillips, Dan Schwarz, and Jack Wildman. Deep research bench: Evaluating ai web research agents, arXiv preprint arXiv:2506.06287, 2025. URL https://arxiv.org/abs/2506.06287v1 .

- Botti [2025] Vicent Botti. Agentic ai and multiagentic: Are we reinventing the wheel?, arXiv preprint arXiv:2506.01463, 2025. URL https://arxiv.org/abs/2506.01463v1 .

- Brach et al. [2025] William Brach, Kristián Kostál, and Michal Ries. The effectiveness of large language models in transforming unstructured text to standardized formats. IEEE Access , 2025.

- Brainerd et al. [2015] C. Brainerd, C. F. Gomes, and K. Nakamura. Dual recollection in episodic memory. Journal of experimental psychology. General , 2015.

- Bramão et al. [2022] Inês Bramão, Jiefeng Jiang, A. Wagner, and M. Johansson. Encoding contexts are incidentally reinstated during competitive retrieval and track the temporal dynamics of memory interference. Cerebral Cortex , 2022.

- Bran et al. [2023] Andrés M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, and P. Schwaller. Augmenting large language models with chemistry tools. Nat. Mac. Intell. , 2023.

- Bravo and Coronel [2008] Maricela Claudia Bravo and Martha Coronel. Aligning agent communication protocols - a pragmatic approach. International Conference on Software and Data Technologies , 2008.

- Brazier et al. [1997] F. Brazier, B. Dunin-Keplicz, N. Jennings, and Jan Treur. Desire: Modelling multi-agent systems in a compositional formal framework. International Journal of Cooperative Information Systems , 1997.

- Brehme et al. [2025] Lorenz Brehme, Thomas Ströhle, and Ruth Breu. Can llms be trusted for evaluating rag systems? a survey of methods and datasets, arXiv preprint arXiv:2504.20119, 2025. URL https://arxiv.org/abs/2504.20119v2 .

- Breil et al. [2017] R. Breil, D. Delahaye, Laurent Lapasset, and E. Feron. Multi-agent systems to help managing air traffic structure. arXiv preprint, 2017.

- Brinkmann and Bizer [2025] Alexander Brinkmann and Christian Bizer. Self-refinement strategies for llm-based product attribute value extraction. Datenbanksysteme für Business, Technologie und Web , 2025.

- Britz et al. [2017] D. Britz, M. Guan, and Minh-Thang Luong. Efficient attention using a fixed-size memory representation. Conference on Empirical Methods in Natural Language Processing , 2017.

- Broitman and Kahana [2024] Adam W. Broitman and M. J. Kahana. Neural context reinstatement of recurring events. bioRxiv , 2024.

- Brooks et al. [2022] Ethan A. Brooks, Logan Walls, Richard L. Lewis, and Satinder Singh. Large language models can implement policy iteration. Neural Information Processing Systems , 2022.

- Brooks [1986] Rodney A. Brooks. A robust layered control system for a mobile robot. IEEE J. Robotics Autom. , 1986.

- Brooks et al. [20222] Tim Brooks, Aleksander Holynski, and Alexei A. Efros. Instructpix2pix: Learning to follow image editing instructions. Computer Vision and Pattern Recognition , 20222.

- Brown et al. [2020] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, J. Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, T. Henighan, R. Child, A. Ramesh, Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Ma teusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, I. Sutskever, and Dario Amodei. Language models are few-shot learners. Neural Information Processing Systems , 2020.

- Brown et al. [20202] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners, arXiv preprint arXiv:2005.14165, 20202. URL https://arxiv.org/abs/2005.14165 .

- Caffagni et al. [2024] Davide Caffagni, Federico Cocchi, Nicholas Moratelli, Sara Sarto, Marcella Cornia, L. Baraldi, and R. Cucchiara. Wiki-llava: Hierarchical retrieval-augmented generation for multimodal llms. 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW) , 2024.

- Cahoon et al. [2025] Joyce Cahoon, Prerna Singh, Nick Litombe, Jonathan Larson, Ha Trinh, Yiwen Zhu, Andreas Mueller, Fotis Psallidas, and Carlo Curino. Optimizing open-domain question answering with graph-based retrieval augmented generation, arXiv preprint arXiv:2503.02922, 2025. URL https://arxiv.org/abs/2503.02922v1 .

- Cai et al. [2024] Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, and Tat-Seng Chua. Large language models empowered personalized web agents. The Web Conference , 2024.

- Cai et al. [2018] Yujun Cai, Liuhao Ge, Jianfei Cai, and Junsong Yuan. Weakly-supervised 3d hand pose estimation from monocular rgb images. In Proceedings of the European conference on computer vision (ECCV) , pages 666–682, 2018.

- Cai et al. [2019] Yujun Cai, Liuhao Ge, Jun Liu, Jianfei Cai, Tat-Jen Cham, Junsong Yuan, and Nadia Magnenat Thalmann. Exploiting spatial-temporal relationships for 3d pose estimation via graph convolutional networks. In Proceedings of the IEEE/CVF International Conference on Computer Vision , pages 2272–2281, 2019.

- Cai et al. [2020] Yujun Cai, Liuhao Ge, Jianfei Cai, Nadia Magnenat Thalmann, and Junsong Yuan. 3d hand pose estimation using synthetic data and weakly labeled rgb images. IEEE transactions on pattern analysis and machine intelligence , 43(11):3739–3753, 2020.

- Cai et al. [20202] Yujun Cai, Lin Huang, Yiwei Wang, Tat-Jen Cham, Jianfei Cai, Junsong Yuan, Jun Liu, Xu Yang, Yiheng Zhu, Xiaohui Shen, et al. Learning progressive joint propagation for human motion prediction. In Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part VII 16 , pages 226–242. Springer International Publishing, 20202.

- Cai et al. [2021] Yujun Cai, Yiwei Wang, Yiheng Zhu, Tat-Jen Cham, Jianfei Cai, Junsong Yuan, Jun Liu, Chuanxia Zheng, Sijie Yan, Henghui Ding, et al. A unified 3d human motion synthesis model via conditional variational auto-encoder. In Proceedings of the IEEE/CVF International Conference on Computer Vision , pages 11645–11655, 2021.

- Camos and Barrouillet [2014] V. Camos and P. Barrouillet. Attentional and non-attentional systems in the maintenance of verbal information in working memory: the executive and phonological loops. Frontiers in Human Neuroscience , 2014.

- Cao et al. [2023] Boxi Cao, Qiaoyu Tang, Hongyu Lin, Xianpei Han, Jiawei Chen, Tianshu Wang, and Le Sun. Retentive or forgetful? diving into the knowledge memorizing mechanism of language models. International Conference on Language Resources and Evaluation , 2023.

- Cao et al. [20232] He Cao, Zhenwei An, Jiazhan Feng, Kun Xu, Liwei Chen, and Dongyan Zhao. A step closer to comprehensive answers: Constrained multi-stage question decomposition with large language models, arXiv preprint arXiv:2311.07491, 20232. URL https://arxiv.org/abs/2311.07491v1 .

- Cao et al. [2018] Nicola De Cao, Wilker Aziz, and Ivan Titov. Question answering by reasoning across documents with graph convolutional networks. North American Chapter of the Association for Computational Linguistics , 2018.

- Cao et al. [2025] Pengfei Cao, Tianyi Men, Wencan Liu, Jingwen Zhang, Xuzhao Li, Xixun Lin, Dianbo Sui, Yanan Cao, Kang Liu, and Jun Zhao. Large language models for planning: A comprehensive and systematic survey, arXiv preprint arXiv:2505.19683, 2025. URL https://arxiv.org/abs/2505.19683v1 .

- Cao et al. [2012] Yongcan Cao, Wenwu Yu, W. Ren, and Guanrong Chen. An overview of recent progress in the study of distributed multi-agent coordination. IEEE Transactions on Industrial Informatics , 2012.

- Cao et al. [2024] Yuji Cao, Huan Zhao, Yuheng Cheng, Ting Shu, Yue Chen, Guolong Liu, Gaoqi Liang, Junhua Zhao, Jinyue Yan, and Yunjie Li. Survey on large language model-enhanced reinforcement learning: Concept, taxonomy, and methods. IEEE Transactions on Neural Networks and Learning Systems , 2024.

- Cao et al. [20242] Yukun Cao, Zengyi Gao, Zhiyang Li, Xike Xie, and S. K. Zhou. Lego-graphrag: Modularizing graph-based retrieval-augmented generation for design space exploration. arXiv preprint, 20242.

- Cardoso and Ferrando [2021] R. C. Cardoso and Angelo Ferrando. A review of agent-based programming for multi-agent systems. De Computis , 2021.

- Carlini et al. [2018] Nicholas Carlini, Chang Liu, Ú. Erlingsson, Jernej Kos, and D. Song. The secret sharer: Evaluating and testing unintended memorization in neural networks. USENIX Security Symposium , 2018.

- Carlini et al. [2020] Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom B. Brown, D. Song, Ú. Erlingsson, Alina Oprea, and Colin Raffel. Extracting training data from large language models. USENIX Security Symposium , 2020.

- Casanueva-Morato et al. [2022] Daniel Casanueva-Morato, A. Ayuso-Martinez, J. P. Dominguez-Morales, A. Jiménez-Fernandez, and G. Jiménez-Moreno. A bio-inspired implementation of a sparse-learning spike-based hippocampus memory model. IEEE Transactions on Emerging Topics in Computing , 2022.

- Casanueva-Morato et al. [2023] Daniel Casanueva-Morato, A. Ayuso-Martinez, J. P. Dominguez-Morales, A. Jiménez-Fernandez, and G. Jiménez-Moreno. Bio-inspired computational memory model of the hippocampus: an approach to a neuromorphic spike-based content-addressable memory. Neural Networks , 2023.

- Chakraborty et al. [2025] Amartya Chakraborty, Paresh Dashore, Nadia Bathaee, Anmol Jain, Anirban Das, Shi-Xiong Zhang, Sambit Sahu, M. Naphade, and Genta Indra Winata. T1: A tool-oriented conversational dataset for multi-turn agentic planning, arXiv preprint arXiv:2505.16986, 2025. URL https://arxiv.org/abs/2505.16986v1 .

- Chalamalasetti et al. [2023] Kranti Chalamalasetti, Jana Gotze, Sherzod Hakimov, Brielen Madureira, Philipp Sadler, and David Schlangen. clembench: Using game play to evaluate chat-optimized language models as conversational agents. Conference on Empirical Methods in Natural Language Processing , 2023.

- Chang and Geng [2025] Edward Y. Chang and Longling Geng. Sagallm: Context management, validation, and transaction guarantees for multi-agent llm planning, arXiv preprint arXiv:2503.11951, 2025. URL https://arxiv.org/abs/2503.11951v2 .

- Chang et al. [2023] Yu-Chu Chang, Xu Wang, Jindong Wang, Yuan Wu, Kaijie Zhu, Hao Chen, Linyi Yang, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Weirong Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qian Yang, and Xingxu Xie. A survey on evaluation of large language models. ACM Transactions on Intelligent Systems and Technology , 2023.

- Chaudhury et al. [2025] Subhajit Chaudhury, Payel Das, Sarathkrishna Swaminathan, Georgios Kollias, Elliot Nelson, Khushbu Pahwa, Tejaswini Pedapati, Igor Melnyk, and Matthew Riemer. Epman: Episodic memory attention for generalizing to longer contexts, arXiv preprint arXiv:2502.14280, 2025. URL https://arxiv.org/abs/2502.14280v1 .

- CHEGN et al. [2022] Xueqi CHEGN, Shenghua Liu, and Ruqing ZHANG. Thinking on new system for big data technology. Bulletin of Chinese Academy of Sciences (Chinese Version) , 37(1):60–67, 2022.

- Chekalina et al. [2024] Viktoriia Chekalina, Anton Razzigaev, Elizaveta Goncharova, and Andrey Kuznetsov. Addressing hallucinations in language models with knowledge graph embeddings as an additional modality, arXiv preprint arXiv:2411.11531, 2024. URL https://arxiv.org/abs/2411.11531v2 .

- Chen et al. [2024] Bo Chen, Yingyu Liang, Zhizhou Sha, Zhenmei Shi, and Zhao Song. Hsr-enhanced sparse attention acceleration, arXiv preprint arXiv:2410.10165, 2024. URL https://arxiv.org/abs/2410.10165v2 .

- Chen et al. [2025] Boyu Chen, Zirui Guo, Zidan Yang, Yuluo Chen, Junze Chen, Zhenghao Liu, Chuan Shi, and Cheng Yang. Pathrag: Pruning graph-based retrieval augmented generation with relational paths, arXiv preprint arXiv:2502.14902, 2025. URL https://arxiv.org/abs/2502.14902v1 .

- Chen et al. [2023] Fei-Long Chen, Du-Zhen Zhang, Ming-Lun Han, Xiu-Yi Chen, Jing Shi, Shuang Xu, and Bo Xu. Vlp: A survey on vision-language pre-training. Machine Intelligence Research , 20(1):38–56, 2023.

- Chen et al. [20252] Feiyang Chen, Yu Cheng, Lei Wang, Yuqing Xia, Ziming Miao, Lingxiao Ma, Fan Yang, Jilong Xue, Zhi Yang, Mao Yang, and Haibo Chen. Attentionengine: A versatile framework for efficient attention mechanisms on diverse hardware platforms, arXiv preprint arXiv:2502.15349, 20252. URL https://arxiv.org/abs/2502.15349v1 .

- Chen [2023] Huajun Chen. Large knowledge model: Perspectives and challenges. Data Intelligence , 2023.

- Chen et al. [20253] Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, and Yucheng Zhang. Haif-gs: Hierarchical and induced flow-guided gaussian splatting for dynamic scene. 20253.

- Chen et al. [20254] Jiaqi Chen, Xiaoye Zhu, Yue Wang, Tianyang Liu, Xinhui Chen, Ying Chen, Chak Tou Leong, Yifei Ke, Joseph Liu, Yiwen Yuan, Julian McAuley, and Li jia Li. Symbolic representation for any-to-any generative tasks, arXiv preprint arXiv:2504.17261v1, 20254. URL https://arxiv.org/abs/2504.17261v1 .

- Chen et al. [20255] Jiayi Chen, J. Ye, and Guiling Wang. From standalone llms to integrated intelligence: A survey of compound al systems, arXiv preprint arXiv:2506.04565, 20255. URL https://arxiv.org/abs/2506.04565v1 .

- Chen et al. [20232] Jin Chen, Zheng Liu, Xu Huang, Chenwang Wu, Qi Liu, Gangwei Jiang, Yuanhao Pu, Yuxuan Lei, Xiaolong Chen, Xingmei Wang, Defu Lian, and Enhong Chen. When large language models meet personalization: Perspectives of challenges and opportunities. World wide web (Bussum) , 20232.

- Chen et al. [20256] Jiyu Chen, Shuang Peng, Daxiong Luo, Fan Yang, Renshou Wu, Fangyuan Li, and Xiaoxin Chen. Edgeinfinite: A memory-efficient infinite-context transformer for edge devices, arXiv preprint arXiv:2503.22196, 20256. URL https://arxiv.org/abs/2503.22196v1 .

- Chen et al. [20242] Justin Chih-Yao Chen, Archiki Prasad, Swarnadeep Saha, Elias Stengel-Eskin, and Mohit Bansal. Magicore: Multi-agent, iterative, coarse-to-fine refinement for reasoning, arXiv preprint arXiv:2409.12147, 20242. URL https://arxiv.org/abs/2409.12147v1 .

- Chen et al. [20243] Mingyang Chen, Haoze Sun, Tianpeng Li, Fan Yang, Hao Liang, Keer Lu, Bin Cui, Wentao Zhang, Zenan Zhou, and Weipeng Chen. Facilitating multi-turn function calling for llms via compositional instruction tuning. International Conference on Learning Representations , 20243.

- Chen et al. [20244] Nuo Chen, Yuhan Li, Jianheng Tang, and Jia Li. Graphwiz: An instruction-following language model for graph computational problems. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining , pages 353–364, 20244.

- Chen et al. [20257] Nuo Chen, Zhiyuan Hu, Qingyun Zou, Jiaying Wu, Qian Wang, Bryan Hooi, and Bingsheng He. Judgelrm: Large reasoning models as a judge, arXiv preprint arXiv:2504.00050, 20257. URL https://arxiv.org/abs/2504.00050v1 .

- Chen et al. [20258] Qiguang Chen, Libo Qin, Jinhao Liu, Dengyun Peng, Jiannan Guan, Peng Wang, Mengkang Hu, Yuhang Zhou, Te Gao, and Wangxiang Che. Towards reasoning era: A survey of long chain-of-thought for reasoning large language models, arXiv preprint arXiv:2503.09567, 20258. URL https://arxiv.org/abs/2503.09567v3 .

- Chen et al. [20259] Qiguang Chen, Mingda Yang, Libo Qin, Jinhao Liu, Zheng Yan, Jiannan Guan, Dengyun Peng, Yiyan Ji, Hanjing Li, Mengkang Hu, Yimeng Zhang, Yihao Liang, Yuhang Zhou, Jiaqi Wang, Zhi Chen, and Wanxiang Che. Ai4research: A survey of artificial intelligence for scientific research, arXiv preprint arXiv:2507.01903, 20259. URL https://arxiv.org/abs/2507.01903 .

- Chen et al. [20245] S Chen, Y Wang, YF Wu, and Q Chen…. Advancing tool-augmented large language models: Integrating insights from errors in inference trees. 20245. URL https://proceedings.neurips.cc/paper_files/paper/2024/hash/c0f7ee1901fef1da4dae2b88dfd43195-Abstract-Conference.html .

- Chen et al. [20233] Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation, arXiv preprint arXiv:2306.15595, 20233. URL https://arxiv.org/abs/2306.15595v2 .

- Chen et al. [2020] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey E. Hinton. A simple framework for contrastive learning of visual representations. International Conference on Machine Learning , 2020.

- Chen et al. [2022] Wenhu Chen, Xueguang Ma, Xinyi Wang, and William W. Cohen. Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks. Trans. Mach. Learn. Res. , 2022.

- Chen et al. [2021] Yanda Chen, Ruiqi Zhong, Sheng Zha, G. Karypis, and He He. Meta-learning via language model in-context tuning. Annual Meeting of the Association for Computational Linguistics , 2021.

- Chen et al. [202510] Yi Chen, JiaHao Zhao, and HaoHao Han. A survey on collaborative mechanisms between large and small language models, arXiv preprint arXiv:2505.07460, 202510. URL https://arxiv.org/abs/2505.07460v1 .

- Chen et al. [20246] Yixin Chen, Shuai Zhang, Boran Han, Tong He, and Bo Li. Camml: Context-aware multimodal learner for large models. Annual Meeting of the Association for Computational Linguistics , 20246.

- Chen et al. [20234] Z Chen, K Zhou, B Zhang, Z Gong, and WX Zhao…. Chatcot: Tool-augmented chain-of-thought reasoning on chat-based large language models. 20234. URL https://arxiv.org/abs/2305.14323 .

- Chen et al. [20235] Zehui Chen, Weihua Du, Wenwei Zhang, Kuikun Liu, Jiangning Liu, Miao Zheng, Jingming Zhuo, Songyang Zhang, Dahua Lin, Kai Chen, et al. T-eval: Evaluating the tool utilization capability step by step. arXiv preprint arXiv:2312.14033 , 20235.

- Chen et al. [20247] Zehui Chen, Kuikun Liu, Qiuchen Wang, Jiangning Liu, Wenwei Zhang, Kai Chen, and Feng Zhao. Mindsearch: Mimicking human minds elicits deep ai searcher, arXiv preprint arXiv:2407.20183, 20247. URL https://arxiv.org/abs/2407.20183v1 .

- Chen et al. [20236] Zhikai Chen, Haitao Mao, Hang Li, Wei Jin, Haifang Wen, Xiaochi Wei, Shuaiqiang Wang, Dawei Yin, Wenqi Fan, Hui Liu, and Jiliang Tang. Exploring the potential of large language models (llms)in learning on graphs. SIGKDD Explorations , 20236.

- Chen et al. [202511] Zihan Chen, Song Wang, Zhen Tan, Xingbo Fu, Zhenyu Lei, Peng Wang, Huan Liu, Cong Shen, and Jundong Li. A survey of scaling in large language model reasoning, arXiv preprint arXiv:2504.02181, 202511. URL https://arxiv.org/abs/2504.02181v1 .

- Chen et al. [20248] ZY Chen, S Shen, G Shen, and G Zhi…. Towards tool use alignment of large language models. 20248. URL https://aclanthology.org/2024.emnlp-main.82/ .

- Cheng et al. [2025] Mingyue Cheng, Yucong Luo, Ouyang Jie, Qi Liu, Huijie Liu, Li Li, Shuo Yu, Bohou Zhang, Jiawei Cao, Jie Ma, Daoyu Wang, and Enhong Chen. A survey on knowledge-oriented retrieval-augmented generation, arXiv preprint arXiv:2503.10677, 2025. URL https://arxiv.org/abs/2503.10677v2 .

- Cheng et al. [2024] Ning Cheng, Zhaohui Yan, Ziming Wang, Zhijie Li, Jiaming Yu, Zilong Zheng, Kewei Tu, Jinan Xu, and Wenjuan Han. Potential and limitations of llms in capturing structured semantics: A case study on srl. International Conference on Intelligent Computing , 2024.

- Cheng et al. [20242] Sitao Cheng, Ziyuan Zhuang, Yong Xu, Fangkai Yang, Chaoyun Zhang, Xiaoting Qin, Xiang Huang, Ling Chen, Qingwei Lin, Dongmei Zhang, et al. Call me when necessary: Llms can efficiently and faithfully reason over structured environments. In Association for Computational Linguistics 2024 , pages 4275–4295, 20242.

- Cheng et al. [2023] Xin Cheng, Di Luo, Xiuying Chen, Lemao Liu, Dongyan Zhao, and Rui Yan. Lift yourself up: Retrieval-augmented text generation with self memory. Neural Information Processing Systems , 2023.

- Cheng et al. [20252] Yao Cheng, Yibo Zhao, Jiapeng Zhu, Yao Liu, Xing Sun, and Xiang Li. Human cognition inspired rag with knowledge graph for complex problem solving, arXiv preprint arXiv:2503.06567, 20252. URL https://arxiv.org/abs/2503.06567v1 .

- Cheng et al. [20243] Yuheng Cheng, Ceyao Zhang, Zhengwen Zhang, Xiangrui Meng, Sirui Hong, Wenhao Li, Zihao Wang, Zekai Wang, Feng Yin, Junhua Zhao, and Xiuqiang He. Exploring large language model based intelligent agents: Definitions, methods, and prospects, arXiv preprint arXiv:2401.03428, 20243. URL https://arxiv.org/abs/2401.03428v1 .

- Cherepanov et al. [2025] Egor Cherepanov, Nikita Kachaev, A. Kovalev, and Aleksandr I. Panov. Memory, benchmark & robots: A benchmark for solving complex tasks with reinforcement learning, arXiv preprint arXiv:2502.10550, 2025. URL https://arxiv.org/abs/2502.10550v2 .

- Chhikara et al. [2025] Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. Mem0: Building production-ready ai agents with scalable long-term memory, arXiv preprint arXiv:2504.19413, 2025. URL https://arxiv.org/abs/2504.19413 .

- Chia et al. [2022] Yew Ken Chia, Lidong Bing, Soujanya Poria, and Luo Si. Relationprompt: Leveraging prompts to generate synthetic data for zero-shot relation triplet extraction. Findings , 2022.

- Choi et al. [2024] Jihye Choi, Nils Palumbo, P. Chalasani, Matthew M. Engelhard, Somesh Jha, Anivarya Kumar, and David Page. Malade: Orchestration of llm-powered agents with retrieval augmented generation for pharmacovigilance, arXiv preprint arXiv:2408.01869, 2024. URL https://arxiv.org/abs/2408.01869v1 .

- Choromanski et al. [2020] K. Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamás Sarlós, Peter Hawkins, Jared Davis, Afroz Mohiuddin, Lukasz Kaiser, David Belanger, Lucy J. Colwell, and Adrian Weller. Rethinking attention with performers. International Conference on Learning Representations , 2020.

- Chu et al. [2025] Zhendong Chu, Shen Wang, Jian Xie, Tinghui Zhu, Yibo Yan, Jinheng Ye, Aoxiao Zhong, Xuming Hu, Jing Liang, Philip S. Yu, and Qingsong Wen. Llm agents for education: Advances and applications, arXiv preprint arXiv:2503.11733, 2025. URL https://arxiv.org/abs/2503.11733v1 .

- Chu et al. [2023] Zhixuan Chu, Huaiyu Guo, Xinyuan Zhou, Yijia Wang, Fei Yu, Hong Chen, Wanqing Xu, Xin Lu, Qing Cui, Longfei Li, Junqing Zhou, and Sheng Li. Data-centric financial large language models, arXiv preprint arXiv:2310.17784, 2023. URL https://arxiv.org/abs/2310.17784v2 .

- Chuang et al. [2024] Yun-Shiuan Chuang, Agam Goyal, Nikunj Harlalka, Siddharth Suresh, Robert Hawkins, Sijia Yang, Dhavan Shah, Junjie Hu, and Timothy T. Rogers. Simulating opinion dynamics with networks of llm-based agents, arXiv preprint arXiv:2311.09618, 2024. URL https://arxiv.org/abs/2311.09618 .

- Chuang et al. [2025] Yung-Sung Chuang, Benjamin Cohen-Wang, Shannon Zejiang Shen, Zhaofeng Wu, Hu Xu, Xi Victoria Lin, James Glass, Shang-Wen Li, and Wen tau Yih. Selfcite: Self-supervised alignment for context attribution in large language models, arXiv preprint arXiv:2502.09604, 2025. URL https://arxiv.org/abs/2502.09604v3 .

- Coda-Forno et al. [2023] Julian Coda-Forno, Marcel Binz, Zeynep Akata, M. Botvinick, Jane X. Wang, and Eric Schulz. Meta-in-context learning in large language models. Neural Information Processing Systems , 2023.

- Coelho et al. [2025] Joao Coelho, Jingjie Ning, Jingyuan He, Kangrui Mao, A. Paladugu, Pranav Setlur, Jiahe Jin, James P. Callan, João Magalhães, Bruno Martins, and Chenyan Xiong. Deepresearchgym: A free, transparent, and reproducible evaluation sandbox for deep research, arXiv preprint arXiv:2505.19253, 2025. URL https://arxiv.org/abs/2505.19253v2 .

- Contal and McGoldrick [2024] Emile Contal and Garrin McGoldrick. Ragsys: Item-cold-start recommender as rag system. IR-RAG@SIGIR , 2024.

- Coppolillo [2025] Erica Coppolillo. Injecting knowledge graphs into large language models, arXiv preprint arXiv:2505.07554, 2025. URL https://arxiv.org/abs/2505.07554v1 .

- Costa et al. [2015] R. P. Costa, R. Froemke, P. J. Sjöström, and Mark C. W. van Rossum. Unified pre- and postsynaptic long-term plasticity enables reliable and flexible learning. eLife , 2015.

- Costello et al. [2025] Caia Costello, Simon Guo, Anna Goldie, and Azalia Mirhoseini. Think, prune, train, improve: Scaling reasoning without scaling models, arXiv preprint arXiv:2504.18116, 2025. URL https://arxiv.org/abs/2504.18116v1 .

- Craig et al. [2016] Michael Craig, Karla Butterworth, Jonna Nilsson, Colin J Hamilton, P. Gallagher, and T. Smulders. How does intentionality of encoding affect memory for episodic information? Learning & memory (Cold Spring Harbor, N.Y.) , 2016.

- crewAI Inc. [2024] crewAI Inc. crewai: Framework for orchestrating role-playing, autonomous ai agents. https://github.com/crewAIInc/crewAI , 2024. [Online; accessed 17-July-2025].

- Cruz et al. [2021] A. Cruz, André V. dos Santos, R. Santiago, and B. Bedregal. A fuzzy semantic for bdi logic. Fuzzy Information and Engineering , 2021.

- Cuconasu et al. [2024] Florin Cuconasu, Giovanni Trappolini, F. Siciliano, Simone Filice, Cesare Campagnano, Y. Maarek, Nicola Tonellotto, and Fabrizio Silvestri. The power of noise: Redefining retrieval for rag systems. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 2024.

- Cui et al. [2022] Kai Cui, Anam Tahir, Gizem Ekinci, Ahmed Elshamanhory, Yannick Eich, Mengguang Li, and H. Koeppl. A survey on large-population systems and scalable multi-agent reinforcement learning, arXiv preprint arXiv:2209.03859, 2022. URL https://arxiv.org/abs/2209.03859v1 .

- Cui et al. [2024] Yuanning Cui, Zequn Sun, and Wei Hu. A prompt-based knowledge graph foundation model for universal in-context reasoning. In Advances in Neural Information Processing Systems , 2024.

- Cui et al. [2025] Yue Cui, Liuyi Yao, Shuchang Tao, Weijie Shi, Yaliang Li, Bolin Ding, and Xiaofang Zhou. Enhancing tool learning in large language models with hierarchical error checklists, arXiv preprint arXiv:2506.00042, 2025. URL https://arxiv.org/abs/2506.00042v1 .

- Curto et al. [2010] C. Curto, A. Degeratu, and V. Itskov. Flexible memory networks. Bulletin of Mathematical Biology , 2010.

- Dai et al. [2024] Ruiting Dai, Yuqiao Tan, Lisi Mo, Shuang Liang, Guohao Huo, Jiayi Luo, and Yao Cheng. G-sap: Graph-based structure-aware prompt learning over heterogeneous knowledge for commonsense reasoning. International Conference on Multimedia Retrieval , 2024.

- Dai et al. [20242] Xinnan Dai, Haohao Qu, Yifen Shen, Bohang Zhang, Qihao Wen, Wenqi Fan, Dongsheng Li, Jiliang Tang, and Caihua Shan. How do large language models understand graph patterns? a benchmark for graph pattern comprehension, arXiv preprint arXiv:2410.05298v2, 20242. URL https://arxiv.org/abs/2410.05298v2 .

- Daneshfar and Bevrani [2009] Fatemeh Daneshfar and H. Bevrani. Multi-agent systems in control engineering: a survey. arXiv preprint, 2009.

- Dang et al. [2025] Yufan Dang, Cheng Qian, Xueheng Luo, Jingru Fan, Zihao Xie, Ruijie Shi, Weize Chen, Cheng Yang, Xiaoyin Che, Ye Tian, Xuantang Xiong, Lei Han, Zhiyuan Liu, and Maosong Sun. Multi-agent collaboration via evolving orchestration, arXiv preprint arXiv:2505.19591, 2025. URL https://arxiv.org/abs/2505.19591v1 .

- Dao [2023] Tri Dao. Flashattention-2: Faster attention with better parallelism and work partitioning. International Conference on Learning Representations , 2023.

- Dao et al. [2022] Tri Dao, Daniel Y. Fu, Stefano Ermon, A. Rudra, and Christopher R’e. Flashattention: Fast and memory-efficient exact attention with io-awareness. Neural Information Processing Systems , 2022.

- Das et al. [2024] D Das, D Banerjee, S Aditya, and A Kulkarni. Mathsensei: a tool-augmented large language model for mathematical reasoning. 2024. URL https://arxiv.org/abs/2402.17231 .

- Das et al. [20242] Payel Das, Subhajit Chaudhury, Elliot Nelson, Igor Melnyk, Sarath Swaminathan, Sihui Dai, Aurélie Lozano, Georgios Kollias, Vijil Chenthamarakshan, Jiří, Navrátil, Soham Dan, and Pin-Yu Chen. Larimar: Large language models with episodic memory control, arXiv preprint arXiv:2403.11901, 20242. URL https://arxiv.org/abs/2403.11901 .

- de Wynter et al. [2023] Adrian de Wynter, Xun Wang, Qilong Gu, and Si-Qing Chen. On meta-prompting, arXiv preprint arXiv:2312.06562, 2023. URL https://arxiv.org/abs/2312.06562v3 .

- Dehal et al. [2025] Ramandeep Singh Dehal, Mehak Sharma, and Enayat Rajabi. Knowledge graphs and their reciprocal relationship with large language models. Machine Learning and Knowledge Extraction , 2025.

- Delgado et al. [2004] Mauricio R. Delgado, V. Stenger, and J. Fiez. Motivation-dependent responses in the human caudate nucleus. Cerebral Cortex , 2004.

- Deng et al. [2023] Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, and Yu Su. Mind2web: Towards a generalist agent for the web. Neural Information Processing Systems , 2023.

- Deng et al. [20232] Yang Deng, Wenqiang Lei, Hongru Wang, and Tat seng Chua. Prompting and evaluating large language models for proactive dialogues: Clarification, target-guided, and non-collaboration. Conference on Empirical Methods in Natural Language Processing , 20232.

- Deng et al. [2024] Yang Deng, An Zhang, Yankai Lin, Xu Chen, Ji-Rong Wen, and Tat-Seng Chua. Large language model powered agents in the web. The Web Conference , 2024.

- Deng et al. [20242] Yang Deng, Xuan Zhang, Wenxuan Zhang, Yifei Yuan, See-Kiong Ng, and Tat-Seng Chua. On the multi-turn instruction following for conversational web agents. Annual Meeting of the Association for Computational Linguistics , 20242.

- Denis and Rémy [2019] Brouillet Denis and Versace Rémy. The nature of the traces and the dynamics of memory. Psychology and Behavioral Sciences , 2019.

- Derakhshani et al. [2023] Mohammad Mahdi Derakhshani, Ivona Najdenkoska, Cees G. M. Snoek, M. Worring, and Yuki Asano. Self-supervised open-ended classification with small visual language models, arXiv preprint arXiv:2310.00500, 2023. URL https://arxiv.org/abs/2310.00500v2 .

- Dernbach et al. [2024] Stefan Dernbach, Khushbu Agarwal, Alejandro Zuniga, Michael Henry, and Sutanay Choudhury. Glam: Fine-tuning large language models for domain knowledge graph alignment via neighborhood partitioning and generative subgraph encoding. AAAI Spring Symposia , 2024.

- Deshmukh et al. [2025] Rushali Deshmukh, Rutuj Raut, Mayur Bhavsar, Sanika Gurav, and Y. Patil. Optimizing human-ai interaction: Innovations in prompt engineering. 2025 3rd International Conference on Intelligent Data Communication Technologies and Internet of Things (IDCIoT) , 2025.

- Deshpande et al. [2025] Darshan Deshpande, Varun Gangal, Hersh Mehta, Jitin Krishnan, Anand Kannappan, and Rebecca Qian. Trail: Trace reasoning and agentic issue localization, arXiv preprint arXiv:2505.08638, 2025. URL https://arxiv.org/abs/2505.08638v3 .

- Devlin et al. [2019] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. North American Chapter of the Association for Computational Linguistics , 2019.

- Dhamani and Maher [2023] Dhruv Dhamani and Mary Lou Maher. The tyranny of possibilities in the design of task-oriented llm systems: A scoping survey, arXiv preprint arXiv:2312.17601, 2023. URL https://arxiv.org/abs/2312.17601v1 .

- Dillon et al. [2025] Frederick Dillon, Gregor Halvorsen, Simon Tattershall, Magnus Rowntree, and Gareth Vanderpool. Contextual memory reweaving in large language models using layered latent state reconstruction, arXiv preprint arXiv:2502.02046, 2025. URL https://arxiv.org/abs/2502.02046v2 .

- Ding et al. [2025] Hanxing Ding, Shuchang Tao, Liang Pang, Zihao Wei, Jinyang Gao, Bolin Ding, Huawei Shen, and Xueqi Chen. Toolcoder: A systematic code-empowered tool learning framework for large language models, arXiv preprint arXiv:2502.11404, 2025. URL https://arxiv.org/abs/2502.11404v2 .

- Ding et al. [2024] Hongxin Ding, Yue Fang, Runchuan Zhu, Xinke Jiang, Jinyang Zhang, Yongxin Xu, Xu Chu, Junfeng Zhao, and Yasha Wang. 3ds: Decomposed difficulty data selection’s case study on llm medical domain adaptation. 2024.

- Ding et al. [2023] Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, and Furu Wei. Longnet: Scaling transformers to 1, 000, 000, 000 tokens. arXiv preprint, 2023.

- Ding et al. [20232] Tianyu Ding, Tianyi Chen, Haidong Zhu, Jiachen Jiang, Yiqi Zhong, Jinxin Zhou, Guangzhi Wang, Zhihui Zhu, Ilya Zharkov, and Luming Liang. The efficiency spectrum of large language models: An algorithmic survey, arXiv preprint arXiv:2312.00678, 20232. URL https://arxiv.org/abs/2312.00678v2 .

- Ding et al. [20242] Yiran Ding, L. Zhang, Chengruidong Zhang, Yuanyuan Xu, Ning Shang, Jiahang Xu, Fan Yang, and Mao Yang. Longrope: Extending llm context window beyond 2 million tokens. International Conference on Machine Learning , 20242.

- Ding et al. [20243] Yiwen Ding, Zhiheng Xi, Wei He, Zhuoyuan Li, Yitao Zhai, Xiaowei Shi, Xunliang Cai, Tao Gui, Qi Zhang, and Xuanjing Huang. Mitigating tail narrowing in llm self-improvement via socratic-guided sampling. North American Chapter of the Association for Computational Linguistics , 20243.

- Djeffal [2025] Christian Djeffal. Reflexive prompt engineering: A framework for responsible prompt engineering and ai interaction design. Conference on Fairness, Accountability and Transparency , 2025.

- Dong et al. [2025] G Dong, Y Chen, X Li, J Jin, H Qian, and Y Zhu…. Tool-star: Empowering llm-brained multi-tool reasoner via reinforcement learning. 2025. URL https://arxiv.org/abs/2505.16410 .

- Dong et al. [2023] Guanting Dong, Jinxu Zhao, Tingfeng Hui, Daichi Guo, Wenlong Wan, Boqi Feng, Yueyan Qiu, Zhuoma Gongque, Keqing He, Zechen Wang, and Weiran Xu. Revisit input perturbation problems for llms: A unified robustness evaluation framework for noisy slot filling task. Natural Language Processing and Chinese Computing , 2023.

- Dong et al. [20252] Guanting Dong, Yifei Chen, Xiaoxi Li, Jiajie Jin, Hongjin Qian, Yutao Zhu, Hangyu Mao, Guorui Zhou, Zhicheng Dou, and Ji-Rong Wen. Tool-star: Empowering llm-brained multi-tool reasoner via reinforcement learning. arXiv preprint, 20252.

- Dong [2024] Kaiwen Dong. Large language model applied in multi-agent systema survey. Applied and Computational Engineering , 2024.

- Dong et al. [20253] Peijie Dong, Zhenheng Tang, Xiang-Hong Liu, Lujun Li, Xiaowen Chu, and Bo Li. Can compressed llms truly act? an empirical evaluation of agentic capabilities in llm compression, arXiv preprint arXiv:2505.19433, 20253. URL https://arxiv.org/abs/2505.19433v2 .

- Dong et al. [2024] Vicky Dong, Hao Yu, and Yao Chen. Graph-augmented relation extraction model with llms-generated support document, arXiv preprint arXiv:2410.23452, 2024. URL https://arxiv.org/abs/2410.23452v1 .

- Dong et al. [20242] Xiangjue Dong, Maria Teleki, and James Caverlee. A survey on llm inference-time self-improvement, arXiv preprint arXiv:2412.14352, 20242. URL https://arxiv.org/abs/2412.14352v1 .

- Dong et al. [20243] Yuxin Dong, Shuo Wang, Hongye Zheng, Jiajing Chen, Zhenhong Zhang, and Chihang Wang. Advanced rag models with graph structures: Optimizing complex knowledge reasoning and text generation. 2024 5th International Symposium on Computer Engineering and Intelligent Communications (ISCEIC) , 20243.

- Dong et al. [20244] Zican Dong, Junyi Li, Xin Men, Wayne Xin Zhao, Bingbing Wang, Zhen Tian, Weipeng Chen, and Ji-Rong Wen. Exploring context window of large language models via decomposed positional vectors. Neural Information Processing Systems , 20244.

- Doostmohammadi and Kuhlmann [2025] Ehsan Doostmohammadi and Marco Kuhlmann. Studying the role of input-neighbor overlap in retrieval-augmented language models training efficiency, arXiv preprint arXiv:2505.14309, 2025. URL https://arxiv.org/abs/2505.14309v1 .

- Doostmohammadian et al. [2024] Mohammadreza Doostmohammadian, Alireza Aghasi, Mohammad Pirani, Ehsan Nekouei, H. Zarrabi, Reza Keypour, Apostolos I. Rikos, and K. H. Johansson. Survey of distributed algorithms for resource allocation over multi-agent systems, arXiv preprint arXiv:2401.15607, 2024. URL https://arxiv.org/abs/2401.15607v1 .

- Dorri et al. [2018] A. Dorri, S. Kanhere, and R. Jurdak. Multi-agent systems: A survey. IEEE Access , 2018.

- Dragone [2012] Mauro Dragone. Component & service-based agent systems: Self-osgi. International Conference on Agents and Artificial Intelligence , 2012.

- Drouin et al. [2024] Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, David Vazquez, Nicolas Chapados, and Alexandre Lacoste. WorkArena: How capable are web agents at solving common knowledge work tasks? In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, Proceedings of the 41st International Conference on Machine Learning , volume 235 of Proceedings of Machine Learning Research , pages 11642–11662. PMLR, 21–27 Jul 2024. URL https://proceedings.mlr.press/v235/drouin24a.html .

- Du et al. [2024] Hung Du, Srikanth Thudumu, Rajesh Vasa, and K. Mouzakis. A survey on context-aware multi-agent systems: Techniques, challenges and future directions, arXiv preprint arXiv:2402.01968, 2024. URL https://arxiv.org/abs/2402.01968v2 .

- Du et al. [2020] Jingfei Du, Edouard Grave, Beliz Gunel, Vishrav Chaudhary, Onur Çelebi, Michael Auli, Ves Stoyanov, and Alexis Conneau. Self-training improves pre-training for natural language understanding. North American Chapter of the Association for Computational Linguistics , 2020.

- Du et al. [2025] Jusen Du, Weigao Sun, Disen Lan, Jiaxi Hu, and Yu Cheng. Mom: Linear sequence modeling with mixture-of-memories, arXiv preprint arXiv:2502.13685, 2025. URL https://arxiv.org/abs/2502.13685v2 .

- Du et al. [20252] Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, and Zhendong Mao. Deepresearch bench: A comprehensive benchmark for deep research agents, arXiv preprint arXiv:2506.11763, 20252. URL https://arxiv.org/abs/2506.11763v1 .

- Du et al. [20253] Shangheng Du, Jiabao Zhao, Jinxin Shi, Zhentao Xie, Xin Jiang, Yanhong Bai, and Liang He. A survey on the optimization of large language model-based agents, arXiv preprint arXiv:2503.12434, 20253. URL https://arxiv.org/abs/2503.12434v1 .

- Du et al. [20242] Yiming Du, Hongru Wang, Zhengyi Zhao, Bin Liang, Baojun Wang, Wanjun Zhong, Zezhong Wang, and Kam-Fai Wong. Perltqa: A personal long-term memory dataset for memory classification, retrieval, and synthesis in question answering, arXiv preprint arXiv:2402.16288, 20242. URL https://arxiv.org/abs/2402.16288v1 .

- Duan et al. [2024] Hanqi Duan, Yao Cheng, Jianxiang Yu, and Xiang Li. Can large language models act as ensembler for multi-gnns?, arXiv preprint arXiv:2410.16822, 2024. URL https://arxiv.org/abs/2410.16822v2 .

- Duan et al. [20242] Peitong Duan, Chin yi Chen, Bjoern Hartmann, and Yang Li. Visual prompting with iterative refinement for design critique generation, arXiv preprint arXiv:2412.16829, 20242. URL https://arxiv.org/abs/2412.16829v2 .

- Ebouky et al. [2025] Brown Ebouky, A. Bartezzaghi, and Mattia Rigotti. Eliciting reasoning in language models with cognitive tools, arXiv preprint arXiv:2506.12115, 2025. URL https://arxiv.org/abs/2506.12115v1 .

- Edge et al. [2024] Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, and Jonathan Larson. From local to global: A graph rag approach to query-focused summarization. arXiv preprint arXiv:2404.16130 , 2024.

- Edwards [2024] Candace Edwards. Hybrid context retrieval augmented generation pipeline: Llm-augmented knowledge graphs and vector database for accreditation reporting assistance, arXiv preprint arXiv:2405.15436, 2024. URL https://arxiv.org/abs/2405.15436v1 .

- Ehtesham et al. [2025] Abul Ehtesham, Aditi Singh, Gaurav Kumar Gupta, and Saket Kumar. A survey of agent interoperability protocols: Model context protocol (mcp), agent communication protocol (acp), agent-to-agent protocol (a2a), and agent network protocol (anp), arXiv preprint arXiv:2505.02279, 2025. URL https://arxiv.org/abs/2505.02279v2 .

- Epperson et al. [2025] Will Epperson, Gagan Bansal, Victor Dibia, Adam Fourney, Jack Gerrits, Erkang Zhu, and Saleema Amershi. Interactive debugging and steering of multi-agent ai systems. International Conference on Human Factors in Computing Systems , 2025.

- Erdogan et al. [2024] Lutfi Eren Erdogan, Nicholas Lee, Siddharth Jha, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Hooper, G. Anumanchipalli, Kurt Keutzer, and A. Gholami. Tinyagent: Function calling at the edge. Conference on Empirical Methods in Natural Language Processing , 2024.

- Fagbohun et al. [2024] Oluwole Fagbohun, Rachel M. Harrison, and Anton Dereventsov. An empirical categorization of prompting techniques for large language models: A practitioner’s guide. arXiv preprint, 2024.

- Faghih et al. [2025] Kazem Faghih, Wenxiao Wang, Yize Cheng, Siddhant Bharti, Gaurang Sriramanan, S. Balasubramanian, Parsa Hosseini, and S. Feizi. Gaming tool preferences in agentic llms, arXiv preprint arXiv:2505.18135, 2025. URL https://arxiv.org/abs/2505.18135v1 .

- Fan et al. [2022] Linxi (Jim) Fan, Guanzhi Wang, Yunfan Jiang, Ajay Mandlekar, Yuncong Yang, Haoyi Zhu, Andrew Tang, De-An Huang, Yuke Zhu, and Anima Anandkumar. Minedojo: Building open-ended embodied agents with internet-scale knowledge. Neural Information Processing Systems , 2022.

- Fan et al. [2025] Siqi Fan, Xiusheng Huang, Yiqun Yao, Xuezhi Fang, Kang Liu, Peng Han, Shuo Shang, Aixin Sun, and Yequan Wang. If an llm were a character, would it know its own story? evaluating lifelong learning in llms, arXiv preprint arXiv:2503.23514, 2025. URL https://arxiv.org/abs/2503.23514v1 .

- Fan et al. [2024] Wenqi Fan, Yujuan Ding, Liang bo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li. A survey on rag meeting llms: Towards retrieval-augmented large language models. Knowledge Discovery and Data Mining , 2024.

- Fan et al. [20242] Yue Fan, Xiaojian Ma, Rujie Wu, Yuntao Du, Jiaqi Li, Zhi Gao, and Qing Li. Videoagent: A memory-augmented multimodal agent for video understanding, arXiv preprint arXiv:2403.11481, 20242. URL https://arxiv.org/abs/2403.11481v2 .

- Fang and Xie [2022] Hongchao Fang and Pengtao Xie. An end-to-end contrastive self-supervised learning framework for language understanding. Transactions of the Association for Computational Linguistics , 2022.

- Fang et al. [2020] Hongchao Fang, Sicheng Wang, Meng Zhou, Jiayuan Ding, and Pengtao Xie. Cert: Contrastive self-supervised learning for language understanding, arXiv preprint arXiv:2005.12766, 2020. URL https://arxiv.org/abs/2005.12766v2 .

- Fang et al. [2025] Junfeng Fang, Zijun Yao, Ruipeng Wang, Haokai Ma, Xiang Wang, and Tat-Seng Chua. We should identify and mitigate third-party safety risks in mcp-powered agent systems, arXiv preprint arXiv:2506.13666, 2025. URL https://arxiv.org/abs/2506.13666v1 .

- Fang et al. [2024] Siyuan Fang, Kaijing Ma, Tianyu Zheng, Xinrun Du, Ningxuan Lu, Ge Zhang, and Qingkun Tang. Karpa: A training-free method of adapting knowledge graph as references for large language model’s reasoning path aggregation. arXiv preprint, 2024.

- Fang et al. [20252] Wei-Wen Fang, Yang Zhang, Kaizhi Qian, James Glass, and Yada Zhu. Play2prompt: Zero-shot tool instruction optimization for llm agents via tool play, arXiv preprint arXiv:2503.14432, 20252. URL https://arxiv.org/abs/2503.14432v2 .

- Fang et al. [20242] Yi Fang, Dongzhe Fan, D. Zha, and Qiaoyu Tan. Gaugllm: Improving graph contrastive learning for text-attributed graphs with large language models. Knowledge Discovery and Data Mining , 20242.

- Fang et al. [20253] Yi Fang, Bowen Jin, Jiacheng Shen, Sirui Ding, Qiaoyu Tan, and Jiawei Han. Graphgpt-o: Synergistic multimodal comprehension and generation on graphs. arXiv preprint, 20253.

- Fatemi et al. [2023] Bahare Fatemi, Jonathan J. Halcrow, and Bryan Perozzi. Talk like a graph: Encoding graphs for large language models. International Conference on Learning Representations , 2023.

- Fatouros et al. [2025] George Fatouros, Georgios Makridis, George Kousiouris, John Soldatos, A. Tsadimas, and D. Kyriazis. Towards conversational ai for human-machine collaborative mlops, arXiv preprint arXiv:2504.12477, 2025. URL https://arxiv.org/abs/2504.12477v1 .

- Fauth et al. [2015] M. Fauth, F. Wörgötter, and Christian Tetzlaff. Formation and maintenance of robust long-term information storage in the presence of synaptic turnover. bioRxiv , 2015.

- Fayyaz et al. [2021] Zahra Fayyaz, Aya Altamimi, Sen Cheng, and Laurenz Wiskott. A model of semantic completion in generative episodic memory. Neural Computation , 2021.

- Fei et al. [2025] Xiang Fei, Xiawu Zheng, and Hao Feng. Mcp-zero: Proactive toolchain construction for llm agents from scratch. arXiv preprint, 2025.

- Feldman et al. [2024] Philip Feldman, James R. Foulds, and Shimei Pan. Ragged edges: The double-edged sword of retrieval-augmented chatbots, arXiv preprint arXiv:2403.01193, 2024. URL https://arxiv.org/abs/2403.01193v3 .

- Feng et al. [2024] Aosong Feng, Rex Ying, and L. Tassiulas. Long sequence modeling with attention tensorization: From sequence to tensor learning. Conference on Empirical Methods in Natural Language Processing , 2024.

- Feng et al. [2025] Erhu Feng, Wenbo Zhou, Zibin Liu, Le Chen, Yunpeng Dong, Cheng Zhang, Yisheng Zhao, Dong Du, Zhi-Hua Zhou, Yubin Xia, and Haibo Chen. Get experience from practice: Llm agents with record & replay, arXiv preprint arXiv:2505.17716, 2025. URL https://arxiv.org/abs/2505.17716v1 .

- Feng et al. [20252] Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin Chi, and Wanjun Zhong. Retool: Reinforcement learning for strategic tool use in llms, arXiv preprint arXiv:2504.11536, 20252. URL https://arxiv.org/abs/2504.11536v2 .

- Feng et al. [20242] Kaituo Feng, Changsheng Li, Xiaolu Zhang, Jun Zhou, Ye Yuan, and Guoren Wang. Keypoint-based progressive chain-of-thought distillation for llms. International Conference on Machine Learning , 20242.

- Feng et al. [2023] Leo Feng, Frederick Tung, Hossein Hajimirsadeghi, Y. Bengio, and M. O. Ahmed. Constant memory attention block, arXiv preprint arXiv:2306.12599, 2023. URL https://arxiv.org/abs/2306.12599v1 .

- Feng et al. [2020] Yanlin Feng, Xinyue Chen, Bill Yuchen Lin, Peifeng Wang, Jun Yan, and Xiang Ren. Scalable multi-hop relational reasoning for knowledge-aware question answering. Conference on Empirical Methods in Natural Language Processing , 2020.

- Feng et al. [20253] Yifan Feng, Shiquan Liu, Xiangmin Han, Shaoyi Du, Zongze Wu, Han Hu, and Yue Gao. Hypergraph foundation model, arXiv preprint arXiv:2503.01203v1, 20253. URL https://arxiv.org/abs/2503.01203v1 .

- Fernando et al. [2023] Chrisantha Fernando, Dylan Banarse, H. Michalewski, Simon Osindero, and Tim Rocktäschel. Promptbreeder: Self-referential self-improvement via prompt evolution. International Conference on Machine Learning , 2023.

- Fernando et al. [2017] Tharindu Fernando, Simon Denman, A. Mcfadyen, S. Sridharan, and C. Fookes. Tree memory networks for modelling long-term temporal dependencies. Neurocomputing , 2017.

- Ferrag et al. [2025] M. Ferrag, Norbert Tihanyi, and M. Debbah. From llm reasoning to autonomous ai agents: A comprehensive review, arXiv preprint arXiv:2504.19678, 2025. URL https://arxiv.org/abs/2504.19678v1 .

- Ferrag et al. [20252] M. Ferrag, Norbert Tihanyi, and M. Debbah. Reasoning beyond limits: Advances and open problems for llms, arXiv preprint arXiv:2503.22732, 20252. URL https://arxiv.org/abs/2503.22732v1 .

- Fifty et al. [2023] Christopher Fifty, Dennis Duan, Ronald G. Junkins, Ehsan Amid, Jurij Leskovec, Christopher R’e, and Sebastian Thrun. Context-aware meta-learning. International Conference on Learning Representations , 2023.

- Finin et al. [1994] Tim Finin, Richard Fritzson, Donald P McKay, Robin McEntire, et al. Kqml-a language and protocol for knowledge and information exchange. In 13th Int. Distributed Artificial Intelligence Workshop , pages 93–103, 1994.

- Finn et al. [2017] Chelsea Finn, P. Abbeel, and S. Levine. Model-agnostic meta-learning for fast adaptation of deep networks. International Conference on Machine Learning , 2017.

- Finotelli and Eustache [2023] Paolo Finotelli and Francis Eustache. Mathematical modeling of human memory. Frontiers in Psychology , 2023.

- Fioretto et al. [2016] Ferdinando Fioretto, Enrico Pontelli, and W. Yeoh. Distributed constraint optimization problems and applications: A survey. Journal of Artificial Intelligence Research , 2016.

- Fortunato et al. [2019] Meire Fortunato, Melissa Tan, Ryan Faulkner, S. Hansen, Adrià Puigdomènech Badia, Gavin Buttimore, Charlie Deck, Joel Z. Leibo, and C. Blundell. Generalization of reinforcement learners with working and episodic memory. Neural Information Processing Systems , 2019.

- Foudil et al. [2021] Samy Foudil, Claire Pleche, and E. Macaluso. Memory for spatio-temporal contextual details during the retrieval of naturalistic episodes. Scientific Reports , 2021.

- Fountas et al. [2024] Zafeirios Fountas, Martin A Benfeghoul, Adnan Oomerjee, Fenia Christopoulou, Gerasimos Lampouras, Haitham Bou-Ammar, and Jun Wang. Human-like episodic memory for infinite context llms, arXiv preprint arXiv:2407.09450, 2024. URL https://arxiv.org/abs/2407.09450 .

- Fournier et al. [2021] Quentin Fournier, G. Caron, and D. Aloise. A practical survey on faster and lighter transformers. ACM Computing Surveys , 2021.

- Franceschi et al. [2018] Luca Franceschi, P. Frasconi, Saverio Salzo, Riccardo Grazzi, and M. Pontil. Bilevel programming for hyperparameter optimization and meta-learning. International Conference on Machine Learning , 2018.

- Frankford et al. [2024] Eduard Frankford, Daniel Crazzolara, Clemens Sauerwein, Michael Vierhauser, and Ruth Breu. Requirements for an online integrated development environment for automated programming assessment systems. International Conference on Computer Supported Education , 2024.

- Fu et al. [2024] Chaoyou Fu, Yuhan Dai, Yondong Luo, Lei Li, Shuhuai Ren, Renrui Zhang, Zihan Wang, Chenyu Zhou, Yunhang Shen, Mengdan Zhang, Peixian Chen, Yanwei Li, Shaohui Lin, Sirui Zhao, Ke Li, Tong Xu, Xiawu Zheng, Enhong Chen, Rongrong Ji, and Xing Sun. Video-mme: The first-ever comprehensive evaluation benchmark of multi-modal llms in video analysis. arXiv preprint, 2024.

- Fu et al. [2023] Honghao Fu, Yilang Shen, Yuxuan Liu, Jingzhong Li, and Xiang Zhang. Sgcn: a multi-order neighborhood feature fusion landform classification method based on superpixel and graph convolutional network. International Journal of Applied Earth Observation and Geoinformation , 122:103441, 2023.

- Fu et al. [20242] Honghao Fu, Yufei Wang, Wenhan Yang, Alex C Kot, and Bihan Wen. Dp-iqa: Utilizing diffusion prior for blind image quality assessment in the wild. 20242.

- Fu et al. [2025] Honghao Fu, Hao Wang, Jing Jih Chin, and Zhiqi Shen. Brainvis: Exploring the bridge between brain and visual signals via image reconstruction. In ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , pages 1–5. IEEE, 2025.

- Fu et al. [20252] Yuchuan Fu, Xiaohan Yuan, and Dongxia Wang. Ras-eval: A comprehensive benchmark for security evaluation of llm agents in real-world environments. arXiv preprint, 20252.

- Fu et al. [20253] Zichuan Fu, Wentao Song, Yejing Wang, Xian Wu, Yefeng Zheng, Yingying Zhang, Derong Xu, Xuetao Wei, Tong Xu, and Xiangyu Zhao. Sliding window attention training for efficient large language models, arXiv preprint arXiv:2502.18845, 20253. URL https://arxiv.org/abs/2502.18845v2 .

- Fusi [2021] Stefano Fusi. Memory capacity of neural network models, arXiv preprint arXiv:2108.07839, 2021. URL https://arxiv.org/abs/2108.07839v2 .

- Gan and Sun [2025] Tiantian Gan and Qiyao Sun. Rag-mcp: Mitigating prompt bloat in llm tool selection via retrieval-augmented generation. arXiv preprint, 2025.

- Gandhi et al. [2021] Kanishk Gandhi, Gala Stojnic, B. Lake, and M. Dillon. Baby intuitions benchmark (bib): Discerning the goals, preferences, and actions of others. Neural Information Processing Systems , 2021.

- Ganguli et al. [2025] Anish Ganguli, Prabal Deb, and Debleena Banerjee. Mark: Memory augmented refinement of knowledge, arXiv preprint arXiv:2505.05177, 2025. URL https://arxiv.org/abs/2505.05177v1 .

- Gao et al. [2023] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large language models empowered agent-based modeling and simulation: A survey and perspectives. Humanities and Social Sciences Communications , 2023.

- Gao et al. [2025] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, and Yong Li. S 3 : Social-network simulation system with large language model-empowered agents, arXiv preprint arXiv:2307.14984, 2025. URL https://arxiv.org/abs/2307.14984 .

- Gao and Zhang [2024] Hang Gao and Yongfeng Zhang. Memory sharing for large language model based agents, arXiv preprint arXiv:2404.09982, 2024. URL https://arxiv.org/abs/2404.09982v2 .

- Gao et al. [20232] L Gao, A Madaan, S Zhou, and U Alon…. Pal: Program-aided language models. 20232. URL https://proceedings.mlr.press/v202/gao23f .

- Gao et al. [2022] Luyu Gao, Xueguang Ma, Jimmy J. Lin, and Jamie Callan. Precise zero-shot dense retrieval without relevance labels. Annual Meeting of the Association for Computational Linguistics , 2022.

- Gao et al. [20222] Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, and Graham Neubig. Pal: Program-aided language models. International Conference on Machine Learning , 20222.

- Gao et al. [20233] Shuzheng Gao, Xinjie Wen, Cuiyun Gao, Wenxuan Wang, and Michael R. Lyu. What makes good in-context demonstrations for code intelligence tasks with llms? International Conference on Automated Software Engineering , 20233.

- Gao et al. [2021] Tianyu Gao, Adam Fisch, and Danqi Chen. Making pre-trained language models better few-shot learners. Annual Meeting of the Association for Computational Linguistics , 2021.

- Gao [2024] Weiguo Gao. Mep: Multiple kernel learning enhancing relative positional encoding length extrapolation, arXiv preprint arXiv:2403.17698, 2024. URL https://arxiv.org/abs/2403.17698v1 .

- Gao et al. [20252] Xian Gao, Zongyun Zhang, Mingye Xie, Ting Liu, and Yuzhuo Fu. Graph of ai ideas: Leveraging knowledge graphs and llms for ai research idea generation, arXiv preprint arXiv:2503.08549, 20252. URL https://arxiv.org/abs/2503.08549v1 .

- Gao et al. [20253] Xuanqi Gao, Siyi Xie, Juan Zhai, Shqing Ma, and Chao Shen. Mcp-radar: A multi-dimensional benchmark for evaluating tool use capabilities in large language models. arXiv preprint, 20253.

- Gao et al. [20234] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Qianyu Guo, Meng Wang, and Haofen Wang. Retrieval-augmented generation for large language models: A survey, arXiv preprint arXiv:2312.10997, 20234. URL https://arxiv.org/abs/2312.10997v5 .

- Gao et al. [2024] Yunfan Gao, Yun Xiong, Meng Wang, and Haofen Wang. Modular rag: Transforming rag systems into lego-like reconfigurable frameworks, arXiv preprint arXiv:2407.21059, 2024. URL https://arxiv.org/abs/2407.21059v1 .

- Gao et al. [20254] Yunfan Gao, Yun Xiong, Yijie Zhong, Yuxi Bi, Ming Xue, and Haofen Wang. Synergizing rag and reasoning: A systematic review, arXiv preprint arXiv:2504.15909, 20254. URL https://arxiv.org/abs/2504.15909v2 .

- Gao et al. [20242] Zhangyang Gao, Daize Dong, Cheng Tan, Jun Xia, Bozhen Hu, and Stan Z. Li. A graph is worth k words: Euclideanizing graph using pure transformer. International Conference on Machine Learning , 20242.

- Gat et al. [2021] Itai Gat, Idan Schwartz, and A. Schwing. Perceptual score: What data modalities does your model perceive? Neural Information Processing Systems , 2021.

- Gat et al. [2022] Itai Gat, Felix Kreuk, Tu Nguyen, Ann Lee, Jade Copet, Gabriel Synnaeve, Emmanuel Dupoux, and Yossi Adi. Augmentation invariant discrete representation for generative spoken language modeling. International Workshop on Spoken Language Translation , 2022.

- Ge et al. [2023] Tao Ge, Jing Hu, Xun Wang, Si-Qing Chen, and Furu Wei. In-context autoencoder for context compression in a large language model. International Conference on Learning Representations , 2023.

- Ge et al. [20232] Yuyao Ge, Zhongguo Yang, Lizhe Chen, Yiming Wang, and Chengyang Li. Attack based on data: a novel perspective to attack sensitive points directly. Cybersecurity , 6(1):43, 20232.

- Ge et al. [2024] Yuyao Ge, Shenghua Liu, Baolong Bi, Yiwei Wang, Lingrui Mei, Wenjie Feng, Lizhe Chen, and Xueqi Cheng. Can graph descriptive order affect solving graph problems with llms? ACL 2025 , 2024.

- Ge et al. [2025] Yuyao Ge, Shenghua Liu, Yiwei Wang, Lingrui Mei, Lizhe Chen, Baolong Bi, and Xueqi Cheng. Innate reasoning is not enough: In-context learning enhances reasoning large language models with less overthinking. 2025.

- Geng et al. [2024] Binzong Geng, Zhaoxin Huan, Xiaolu Zhang, Yong He, Liang Zhang, Fajie Yuan, Jun Zhou, and Linjian Mo. Breaking the length barrier: Llm-enhanced ctr prediction in long textual user behaviors. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 2024.

- Geng et al. [2023] Hejia Geng, Boxun Xu, and Peng Li. Upar: A kantian-inspired prompting framework for enhancing large language model capabilities, arXiv preprint arXiv:2310.01441, 2023. URL https://arxiv.org/abs/2310.01441v2 .

- Georgiou et al. [2021] Antonios Georgiou, M. Katkov, and M. Tsodyks. Retroactive interference model of forgetting. Journal of Mathematical Neuroscience , 2021.

- Gershman et al. [2013] S. Gershman, A. Schapiro, A. Hupbach, and K. Norman. Neural context reinstatement predicts memory misattribution. Journal of Neuroscience , 2013.

- Geva et al. [2020] Mor Geva, R. Schuster, Jonathan Berant, and Omer Levy. Transformer feed-forward layers are key-value memories. Conference on Empirical Methods in Natural Language Processing , 2020.

- Geva et al. [2022] Mor Geva, Avi Caciularu, Ke Wang, and Yoav Goldberg. Transformer feed-forward layers build predictions by promoting concepts in the vocabulary space. Conference on Empirical Methods in Natural Language Processing , 2022.

- Gezdur and Bhattacharjya [2025] Arda Gezdur and J. Bhattacharjya. Innovators and transformers: enhancing supply chain employee training with an innovative application of a large language model. International Journal of Physical Distribution & Logistics Management , 2025.

- Ghafarollahi and Buehler [2024] Alireza Ghafarollahi and Markus J. Buehler. Protagents: protein discovery via large language model multi-agent collaborations combining physics and machine learning. Digital Discovery , 2024.

- Ghassel et al. [2025] Abdellah Ghassel, Ian Robinson, Gabriel Tanase, Hal Cooper, Bryan Thompson, Zhen Han, V. Ioannidis, Soji Adeshina, and H. Rangwala. Hierarchical lexical graph for enhanced multi-hop retrieval, arXiv preprint arXiv:2506.08074, 2025. URL https://arxiv.org/abs/2506.08074v1 .

- Ghetti and Bunge [2012] S. Ghetti and S. Bunge. Neural changes underlying the development of episodic memory during middle childhood. Developmental Cognitive Neuroscience , 2012.

- Ghica [2009] D. Ghica. Function interface models for hardware compilation: Types, signatures, protocols, arXiv preprint arXiv:0907.0749, 2009. URL https://arxiv.org/abs/0907.0749v1 .

- Giallanza et al. [2024] Tyler Giallanza, Declan Campbell, and Jonathan D. Cohen. Toward the emergence of intelligent control: Episodic generalization and optimization. Open Mind , 2024.

- Gim et al. [2024] In Gim, Seung seob Lee, and Lin Zhong. Asynchronous llm function calling, arXiv preprint arXiv:2412.07017, 2024. URL https://arxiv.org/abs/2412.07017v1 .

- Glaese et al. [2022] Amelia Glaese, Nat McAleese, Maja Trębacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger, Martin Chadwick, Phoebe Thacker, Lucy Campbell-Gillingham, Jonathan Uesato, Po-Sen Huang, Ramona Comanescu, Fan Yang, Abigail See, Sumanth Dathathri, Rory Greig, Charlie Chen, Doug Fritz, Jaume Sanchez Elias, Richard Green, Soňa Mokrá, Nicholas Fernando, Boxi Wu, Rachel Foley, Susannah Young, Iason Gabriel, William Isaac, John Mellor, Demis Hassabis, Koray Kavukcuoglu, Lisa Anne Hendricks, and Geoffrey Irving. Improving alignment of dialogue agents via targeted human judgements, arXiv preprint arXiv:2209.14375, 2022. URL https://arxiv.org/abs/2209.14375 .

- Godden and Baddeley [1975] D. Godden and A. Baddeley. Context-dependent memory in two natural environments: on land and underwater. arXiv preprint, 1975.

- Goknil et al. [2024] Arda Goknil, Femke B. Gelderblom, Simeon Tverdal, Shukun Tokas, and Hui Song. Privacy policy analysis through prompt engineering for llms, arXiv preprint arXiv:2409.14879, 2024. URL https://arxiv.org/abs/2409.14879v1 .

- Golubev et al. [2021] Yaroslav Golubev, Zarina Kurbatova, E. Alomar, T. Bryksin, and Mohamed Wiem Mkaouer. One thousand and one stories: a large-scale survey of software refactoring. ESEC/SIGSOFT FSE , 2021.

- Gordon et al. [2014] Alan M Gordon, Jesse Rissman, Roozbeh Kiani, and Anthony D Wagner. Cortical reinstatement mediates the relationship between content-specific encoding activity and subsequent recollection decisions. Cerebral Cortex , 2014.

- Gordon and Logan [2005] E. Gordon and B. Logan. Managing goals and resources in dynamic environments. arXiv preprint, 2005.

- Gou et al. [2023] Z Gou, Z Shao, Y Gong, Y Shen, and Y Yang…. Critic: Large language models can self-correct with tool-interactive critiquing. 2023. URL https://arxiv.org/abs/2305.11738 .

- Gou et al. [20232] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Minlie Huang, Nan Duan, and Weizhu Chen. Tora: A tool-integrated reasoning agent for mathematical problem solving. International Conference on Learning Representations , 20232.

- Graves et al. [2013] Alex Graves, Abdel rahman Mohamed, and Geoffrey E. Hinton. Speech recognition with deep recurrent neural networks. IEEE International Conference on Acoustics, Speech, and Signal Processing , 2013.

- Grishina et al. [2025] Ekaterina Grishina, Mikhail Gorbunov, and Maxim Rakhuba. Procrustesgpt: Compressing llms with structured matrices and orthogonal transformations, arXiv preprint arXiv:2506.02818, 2025. URL https://arxiv.org/abs/2506.02818v1 .

- Gronauer and Diepold [2021] Sven Gronauer and K. Diepold. Multi-agent deep reinforcement learning: a survey. Artificial Intelligence Review , 2021.

- Gros [2008] C. Gros. Complex and adaptive dynamical systems, arXiv preprint arXiv:0807.4838, 2008. URL https://arxiv.org/abs/0807.4838v3 .

- Gu et al. [2021] Albert Gu, Karan Goel, and Christopher R’e. Efficiently modeling long sequences with structured state spaces. International Conference on Learning Representations , 2021.

- Gu et al. [2022] Albert Gu, Ankit Gupta, Karan Goel, and Christopher Ré. On the parameterization and initialization of diagonal state space models. Neural Information Processing Systems , 2022.

- Gu et al. [2024] Jian Gu, Chunyang Chen, and A. Aleti. Vocabulary-defined semantics: Latent space clustering for improving in-context learning, arXiv preprint arXiv:2401.16184, 2024. URL https://arxiv.org/abs/2401.16184v6 .

- Gu et al. [2025] Yongli Gu, Xiang Yan, Hanlin Qin, Naveed Akhtar, Shuai Yuan, Honghao Fu, Shuowen Yang, and Ajmal Mian. Hdtcnet: A hybrid-dimensional convolutional network for multivariate time series classification. Pattern Recognition , page 111837, 2025.

- Gu et al. [20242] Zhuohan Gu, Jiayi Yao, Kuntai Du, and Junchen Jiang. Llmsteer: Improving long-context llm inference by steering attention on reused contexts, arXiv preprint arXiv:2411.13009, 20242. URL https://arxiv.org/abs/2411.13009v2 .

- Guan et al. [2025] Shengyue Guan, Haoyi Xiong, Jindong Wang, Jiang Bian, Bin Zhu, and Jian guang Lou. Evaluating llm-based agents for multi-turn conversations: A survey, arXiv preprint arXiv:2503.22458, 2025. URL https://arxiv.org/abs/2503.22458v1 .

- Guan et al. [2024] Zhong Guan, Hongke Zhao, Likang Wu, Ming He, and Jianpin Fan. Langtopo: Aligning language descriptions of graphs with tokenized topological modeling, arXiv preprint arXiv:2406.13250, 2024. URL https://arxiv.org/abs/2406.13250v1 .

- Gunter et al. [2024] Tom Gunter, Zirui Wang, Chong Wang, Ruoming Pang, Andy Narayanan, Aonan Zhang, Bowen Zhang, Chen Chen, Chung-Cheng Chiu, David Qiu, Deepak Gopinath, Dian Ang Yap, Dong Yin, Feng Nan, Floris Weers, Guoli Yin, Haoshuo Huang, Jianyu Wang, Jiarui Lu, John Peebles, Kewei Ye, Mark Lee, Nan Du, Qibin Chen, Quentin Keunebroek, Sam Wiseman, Syd Evans, Tao Lei, Vivek Rathod, Xiang Kong, Xianzhi Du, Yanghao Li, Yongqiang Wang, Yuan Gao, Zaid Ahmed, Zhaoyang Xu, Zhiyun Lu, Al Rashid, Albin Madappally Jose, Alec Doane, Alfredo Bencomo, Allison Vanderby, Andrew Hansen, Ankur Jain, A. Anupama, Areeba Kamal, Bugu Wu, Carolina Brum, Charlie Maalouf, Chinguun Erdenebileg, Chris Dulhanty, Dominik Moritz, Doug Kang, Eduardo Jimenez, Evan Ladd, Fang Shi, Felix Bai, Frank Chu, Fred Hohman, Hadas Kotek, Hannah Gillis Coleman, Jane Li, Jeffrey P. Bigham, Jeffery Cao, Jeff Lai, Jessica Cheung, Jiulong Shan, Joe Zhou, John Li, Jun Qin, Karanjeet Singh, Karla Vega, Kelvin Zou, Laura Heckman, Lauren Gardiner, Margit Bowler, Maria
Cordell, Meng Cao, Nicole Hay, Nilesh Shahdadpuri, Otto Godwin, Pranay Dighe, Pushyami Rachapudi, Ramsey Tantawi, Roman Frigg, Sam Davarnia, Sanskruti Shah, Saptarshi Guha, Sasha Sirovica, Shen Ma, Shuang Ma, Simon Wang, Sulgi Kim, Suma Jayaram, Vaishaal Shankar, Varsha Paidi, Vivek Kumar, Xin Wang, Xin Zheng, Walker Cheng, Y. Shrager, Yang Ye, Yasu Tanaka, Yihao Guo, Yun Meng, Zhaoping Luo, Ouyang Zhi, Alp Aygar, Alvin Wan, Andrew D. Walkingshaw, Tzu-Hsiang Lin, Arsalan Farooq, Brent Ramerth, Colorado Reed, Chris Bartels, Chris Chaney, David Riazati, Eric Liang Yang, Erin Feldman, Gabriel Hochstrasser, Guillaume Seguin, Irina Belousova, J. Pelemans, Karen Yang, Keivan A. Vahid, Liangliang Cao, Mahyar Najibi, Marco Zuliani, Max Horton, Minsik Cho, Nikhil Bhendawade, Patrick Dong, Piotr Maj, Pulkit Agrawal, Qi Shan, Qichen Fu, R. Poston, Sam Xu, Shuangning Liu, Sushma Rao, Tashweena Heeramun, Thomas Merth, Uday Rayala, Victor Cui, Vivek Rangarajan Sridhar, Wencong Zhang, Wenqi Zhang, Wentao Wu, Xingyu Zhou,
Xinwen Liu, Yang Zhao, Yin Xia, Zhile Ren, and Zhongzheng Ren. Apple intelligence foundation language models, arXiv preprint arXiv:2407.21075, 2024. URL https://arxiv.org/abs/2407.21075v1 .

- Guo et al. [2023] Jiayan Guo, Lun Du, and Hengyu Liu. Gpt4graph: Can large language models understand graph structured data ? an empirical evaluation and benchmarking, arXiv preprint arXiv:2305.15066, 2023. URL https://arxiv.org/abs/2305.15066v2 .

- Guo et al. [2024] Jing Guo, Nan Li, Jianchuan Qi, Hang Yang, Ruiqiao Li, Yuzhen Feng, Si Zhang, and Ming Xu. Empowering working memory for large language model agents, arXiv preprint arXiv:2312.17259, 2024. URL https://arxiv.org/abs/2312.17259 .

- Guo et al. [20242] Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, N. Chawla, Olaf Wiest, and Xiangliang Zhang. Large language model based multi-agents: A survey of progress and challenges. International Joint Conference on Artificial Intelligence , 20242.

- Guo et al. [2025] Xiaojun Guo, Ang Li, Yifei Wang, Stefanie Jegelka, and Yisen Wang. G1: Teaching llms to reason on graphs with reinforcement learning. arXiv preprint arXiv:2505.18499 , 2025.

- Guo et al. [20252] Yuan Guo, Tingjia Miao, Zheng Wu, Pengzhou Cheng, Ming Zhou, and Zhuosheng Zhang. Atomic-to-compositional generalization for mobile agents with a new benchmark and scheduling system, arXiv preprint arXiv:2506.08972, 20252. URL https://arxiv.org/abs/2506.08972v1 .

- Guo et al. [20243] Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan Liu, Maosong Sun, and Yang Liu. Stabletoolbench: Towards stable large-scale benchmarking on tool learning of large language models. Annual Meeting of the Association for Computational Linguistics , 20243.

- Guo et al. [20244] Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, and Chao Huang. Lightrag: Simple and fast retrieval-augmented generation, arXiv preprint arXiv:2410.05779, 20244. URL https://arxiv.org/abs/2410.05779v3 .

- Gupta et al. [2024] Sharut Gupta, Chenyu Wang, Yifei Wang, T. Jaakkola, and Stefanie Jegelka. In-context symmetries: Self-supervised learning through contextual world models. Neural Information Processing Systems , 2024.

- Gupta et al. [20242] Tanmay Gupta, Luca Weihs, and Aniruddha Kembhavi. Codenav: Beyond tool-use to using real-world codebases with llm agents, arXiv preprint arXiv:2406.12276, 20242. URL https://arxiv.org/abs/2406.12276v1 .

- Gur et al. [2023] I Gur, H Furuta, A Huang, M Safdari, and Y Matsuo…. A real-world webagent with planning, long context understanding, and program synthesis. 2023. URL https://arxiv.org/abs/2307.12856 .

- Gur et al. [20232] Izzeddin Gur, Hiroki Furuta, Austin Huang, Mustafa Safdari, Yutaka Matsuo, D. Eck, and Aleksandra Faust. A real-world webagent with planning, long context understanding, and program synthesis. International Conference on Learning Representations , 20232.

- Gururajan et al. [2024] Ashwin Kumar Gururajan, Enrique Lopez-Cuena, Jordi Bayarri-Planas, Adrián Tormos, Daniel Hinjos, Pablo Bernabeu Perez, Anna Arias-Duart, Pablo A. Martin-Torres, Lucia Urcelay-Ganzabal, Marta Gonzalez-Mallo, S. Álvarez Napagao, Eduard Ayguad’e-Parra, and Ulises Cortés Dario Garcia-Gasulla. Aloe: A family of fine-tuned open healthcare llms, arXiv preprint arXiv:2405.01886, 2024. URL https://arxiv.org/abs/2405.01886v1 .

- Gutierrez et al. [2024] Bernal Jimenez Gutierrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, and Yu Su. Hipporag: Neurobiologically inspired long-term memory for large language models. Neural Information Processing Systems , 2024.

- Guu et al. [2020] Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Ming-Wei Chang. Realm: Retrieval-augmented language model pre-training. International Conference on Machine Learning , 2020.

- Gödel et al. [1966] K. Gödel, B. Meltzer, and R. Schlegel. On formally undecidable propositions of principia mathematica and related systems. arXiv preprint, 1966.

- Habler et al. [2025] Idan Habler, Ken Huang, Vineeth Sai Narajala, and Prashant Kulkarni. Building a secure agentic ai application leveraging a2a protocol, arXiv preprint arXiv:2504.16902, 2025. URL https://arxiv.org/abs/2504.16902v2 .

- Halloran [2025] John Halloran. Mcp safety training: Learning to refuse falsely benign mcp exploits using improved preference alignment, arXiv preprint arXiv:2505.23634, 2025. URL https://arxiv.org/abs/2505.23634v1 .

- Ham et al. [2021] Tae Jun Ham, Yejin Lee, Seong Hoon Seo, Soo-Uck Kim, Hyunji Choi, Sungjun Jung, and Jae W. Lee. Elsa: Hardware-software co-design for efficient, lightweight self-attention mechanism in neural networks. International Symposium on Computer Architecture , 2021.

- Han et al. [2025] Feijiang Han, Licheng Guo, Hengtao Cui, and Zhiyuan Lyu. Question tokens deserve more attention: Enhancing large language models without training through step-by-step reading and question attention recalibration, arXiv preprint arXiv:2504.09402, 2025. URL https://arxiv.org/abs/2504.09402v1 .

- Han et al. [2024] Han Han, Tong Zhu, Xiang Zhang, Mengsong Wu, Hao Xiong, and Wenliang Chen. Nestools: A dataset for evaluating nested tool learning abilities of large language models. International Conference on Computational Linguistics , 2024.

- Han et al. [20252] Haoyu Han, Yu Wang, Harry Shomer, Kai Guo, Jiayuan Ding, Yongjia Lei, Mahantesh Halappanavar, Ryan A. Rossi, Subhabrata Mukherjee, Xianfeng Tang, Qi He, Zhigang Hua, Bo Long, Tong Zhao, Neil Shah, Amin Javari, Yinglong Xia, and Jiliang Tang. Retrieval-augmented generation with graphs (graphrag), arXiv preprint arXiv:2501.00309, 20252. URL https://arxiv.org/abs/2501.00309 .

- Han et al. [20242] Tingxu Han, Zhenting Wang, Chunrong Fang, Shiyun Zhao, Shiqing Ma, and Zhenyu Chen. Token-budget-aware llm reasoning, arXiv preprint arXiv:2412.18547, 20242. URL https://arxiv.org/abs/2412.18547v5 .

- Han et al. [20243] Yuanning Han, Ziyi Qiu, Jiale Cheng, and Ray Lc. When teams embrace ai: Human collaboration strategies in generative prompting in a creative design task. International Conference on Human Factors in Computing Systems , 20243.

- Hankache et al. [2025] R. Hankache, Kingsley Nketia Acheampong, Liang Song, Marek Brynda, Raad Khraishi, and Greig A. Cowan. Evaluating the sensitivity of llms to prior context, arXiv preprint arXiv:2506.00069, 2025. URL https://arxiv.org/abs/2506.00069v1 .

- Hao et al. [2023] S Hao, T Liu, Z Wang, and Z Hu. Toolkengpt: Augmenting frozen language models with massive tools via tool embeddings. 2023. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html .

- Hariharan [2025] Mohanakrishnan Hariharan. Semantic mastery: Enhancing llms with advanced natural language understanding, arXiv preprint arXiv:2504.00409, 2025. URL https://arxiv.org/abs/2504.00409v1 .

- Hartmann and Koller [2024] Mareike Hartmann and Alexander Koller. A survey on complex tasks for goal-directed interactive agents, arXiv preprint arXiv:2409.18538, 2024. URL https://arxiv.org/abs/2409.18538v1 .

- Hassani et al. [2019] A. Hassani, A. Medvedev, P. D. Haghighi, Sea Ling, A. Zaslavsky, and P. Jayaraman. Context definition and query language: Conceptual specification, implementation, and evaluation. Italian National Conference on Sensors , 2019.

- Hatalis et al. [2024] Kostas Hatalis, Despina Christou, Joshua Myers, Steven Jones, Keith Lambert, Adam Amos-Binks, Zohreh Dannenhauer, and Dustin Dannenhauer. Memory matters: The need to improve long-term memory in llm-agents. Proceedings of the AAAI Symposium Series , 2024.

- Hatalis et al. [2025] Kostas Hatalis, Despina Christou, and Vyshnavi Kondapalli. Review of case-based reasoning for llm agents: Theoretical foundations, architectural components, and cognitive integration, arXiv preprint arXiv:2504.06943, 2025. URL https://arxiv.org/abs/2504.06943v2 .

- He et al. [2025] Jacky He, Guiran Liu, Binrong Zhu, Hanlu Zhang, Hongye Zheng, and Xiaokai Wang. Context-guided dynamic retrieval for improving generation quality in rag models, arXiv preprint arXiv:2504.19436, 2025. URL https://arxiv.org/abs/2504.19436v1 .

- He et al. [2024] Jianben He, Xingbo Wang, Shiyi Liu, Guande Wu, Claudio Silva, and Huamin Qu. Poem: Interactive prompt optimization for enhancing multimodal reasoning of large language models. IEEE Pacific Visualization Symposium , 2024.

- He et al. [20242] Junqing He, Liang Zhu, Rui Wang, Xi Wang, Gholamreza Haffari, and Jiaxing Zhang. Madial-bench: Towards real-world evaluation of memory-augmented dialogue generation. North American Chapter of the Association for Computational Linguistics , 20242.

- He et al. [20243] Shawn He, Surangika Ranathunga, Stephen Cranefield, and B. Savarimuthu. Norm violation detection in multi-agent systems using large language models: A pilot study. COINE , 20243.

- He [2024] Shengtao He. Achieving tool calling functionality in llms using only prompt engineering without fine-tuning, arXiv preprint arXiv:2407.04997, 2024. URL https://arxiv.org/abs/2407.04997v1 .

- He et al. [20252] Wenchong He, Liqian Peng, Zhe Jiang, and Alex Go. You only fine-tune once: Many-shot in-context fine-tuning for large language model, arXiv preprint arXiv:2506.11103, 20252. URL https://arxiv.org/abs/2506.11103v1 .

- He et al. [20253] Xu He, Di Wu, Yan Zhai, and Kun Sun. Sentinelagent: Graph-based anomaly detection in multi-agent systems, arXiv preprint arXiv:2505.24201, 20253. URL https://arxiv.org/abs/2505.24201v1 .

- He et al. [20254] Yang He, Xiao Ding, Bibo Cai, Yufei Zhang, Kai Xiong, Zhouhao Sun, Bing Qin, and Ting Liu. Self-route: Automatic mode switching via capability estimation for efficient reasoning. arXiv preprint, 20254.

- He et al. [20255] Yu He, Yingxi Li, Colin White, and Ellen Vitercik. Dsr-bench: Evaluating the structural reasoning abilities of llms via data structures. arXiv preprint, 20255.

- He et al. [20244] Zexue He, Leonid Karlinsky, Donghyun Kim, Julian McAuley, Dmitry Krotov, and Rogério Feris. Camelot: Towards large language models with training-free consolidated associative memory, arXiv preprint arXiv:2402.13449, 20244. URL https://arxiv.org/abs/2402.13449v1 .

- Heald et al. [2022] James B. Heald, M. Lengyel, and D. Wolpert. Contextual inference in learning and memory. Trends in Cognitive Sciences , 2022.

- Hedayati et al. [2021] Shekoofeh Hedayati, Ryan E. O’Donnell, and Brad Wyble. A model of working memory for latent representations. Nature Human Behaviour , 2021.

- Helmi [2025] Tooraj Helmi. Modeling response consistency in multi-agent llm systems: A comparative analysis of shared and separate context approaches, arXiv preprint arXiv:2504.07303, 2025. URL https://arxiv.org/abs/2504.07303v1 .

- Hemmat et al. [2024] Arshia Hemmat, Kianoosh Vadaei, Mohammad Hassan Heydari, and Afsaneh Fatemi. Leveraging retrieval-augmented generation for persian university knowledge retrieval. Conference on Information and Knowledge Technology , 2024.

- Herrera et al. [2020] M. Herrera, Marco Pérez-Hernández, A. Kumar Parlikad, and J. Izquierdo. Multi-agent systems and complex networks: Review and applications in systems engineering. Processes , 2020.

- Herweg et al. [2018] Nora A. Herweg, A. Sharan, M. Sperling, A. Brandt, A. Schulze-Bonhage, and M. Kahana. Reactivated spatial context guides episodic recall. Journal of Neuroscience , 2018.

- Heston and Khun [2023] Thomas F. Heston and Charya Khun. Prompt engineering in medical education. International Medical Education , 2023.

- Hirunyasiri et al. [2023] Dollaya Hirunyasiri, Danielle R. Thomas, Jionghao Lin, K. Koedinger, and Vincent Aleven. Comparative analysis of gpt-4 and human graders in evaluating human tutors giving praise to students. Human-AI Math Tutoring@AIED , 2023.

- Hoang [2024] Thomas Hoang. Gnn: Graph neural network and large language model for data discovery, arXiv preprint arXiv:2408.13609, 2024. URL https://arxiv.org/abs/2408.13609v2 .

- Hoek and Wooldridge [2003] W. Hoek and M. Wooldridge. Towards a logic of rational agency. Logic Journal of the IGPL , 2003.

- Hogan et al. [2020] Aidan Hogan, E. Blomqvist, Michael Cochez, C. d’Amato, Gerard de Melo, C. Gutierrez, J. E. L. Gayo, S. Kirrane, S. Neumaier, A. Polleres, Roberto Navigli, A. Ngomo, S. M. Rashid, Anisa Rula, Lukas Schmelzeisen, Juan Sequeda, Steffen Staab, and Antoine Zimmermann. Knowledge graphs. ACM Computing Surveys , 2020.

- Holla et al. [2020] Nithin Holla, Pushkar Mishra, H. Yannakoudakis, and Ekaterina Shutova. Meta-learning with sparse experience replay for lifelong language learning, arXiv preprint arXiv:2009.04891, 2020. URL https://arxiv.org/abs/2009.04891v2 .

- Hong and He [2025] Chuanyang Hong and Qingyun He. Enhancing memory retrieval in generative agents through llm-trained cross attention networks. Frontiers in Psychology , 2025.

- Hong et al. [2019] M. Hong, Sean M. Polyn, and Lisa K. Fazio. Examining the episodic context account: does retrieval practice enhance memory for context? Cognitive Research , 2019.

- Hong et al. [2023] Sirui Hong, Xiawu Zheng, Jonathan P. Chen, Yuheng Cheng, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Z. Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, and Chenglin Wu. Metagpt: Meta programming for multi-agent collaborative framework. arXiv preprint, 2023.

- Hong et al. [2024] Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. Metagpt: Meta programming for a multi-agent collaborative framework, arXiv preprint arXiv:2308.00352, 2024. URL https://arxiv.org/abs/2308.00352 .

- Hong et al. [20232] Wenyi Hong, Weihan Wang, Qingsong Lv, Jiazheng Xu, Wenmeng Yu, Junhui Ji, Yan Wang, Zihan Wang, Yuxiao Dong, Ming Ding, and Jie Tang. Cogagent: A visual language model for gui agents. Computer Vision and Pattern Recognition , 20232.

- Hong et al. [20242] Xiangyu Hong, Che Jiang, Biqing Qi, Fandong Meng, Mo Yu, Bowen Zhou, and Jie Zhou. On the token distance modeling ability of higher rope attention dimension. Conference on Empirical Methods in Natural Language Processing , 20242.

- Hong et al. [2025] Yubin Hong, Chaofan Li, Jingyi Zhang, and Yingxia Shao. Fg-rag: Enhancing query-focused summarization with context-aware fine-grained graph rag. arXiv preprint, 2025.

- Horsuwan et al. [2024] Thanapapas Horsuwan, Piyawat Lertvittayakumjorn, Kasidis Kanwatchara, B. Kijsirikul, and P. Vateekul. Meta lifelong-learning with selective and task-aware adaptation. IEEE Access , 2024.

- Hoskin et al. [2017] A. N. Hoskin, A. Bornstein, K. Norman, and J. Cohen. Refresh my memory: Episodic memory reinstatements intrude on working memory maintenance. Cognitive, Affective, & Behavioral Neuroscience , 2017.

- Hospedales et al. [2020] Timothy M. Hospedales, Antreas Antoniou, P. Micaelli, and A. Storkey. Meta-learning in neural networks: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence , 2020.

- Hosseini et al. [2024] Peyman Hosseini, Ignacio Castro, Iacopo Ghinassi, and Matthew Purver. Efficient solutions for an intriguing failure of llms: Long context window does not mean llms can analyze long sequences flawlessly. International Conference on Computational Linguistics , 2024.

- Hou et al. [2024] Haowen Hou, Fei Ma, Binwen Bai, Xinxin Zhu, and F. Yu. Enhancing and accelerating large language models via instruction-aware contextual compression, arXiv preprint arXiv:2408.15491, 2024. URL https://arxiv.org/abs/2408.15491v1 .

- Hou et al. [20242] Wenjun Hou, Yi Cheng, Kaishuai Xu, Yan Hu, Wenjie Li, and Jiangming Liu. Memory-augmented multimodal llms for surgical vqa via self-contained inquiry, arXiv preprint arXiv:2411.10937v1, 20242. URL https://arxiv.org/abs/2411.10937v1 .

- Hou et al. [2025] Xinyi Hou, Yanjie Zhao, Shenao Wang, and Haoyu Wang. Model context protocol (mcp): Landscape, security threats, and future research directions, arXiv preprint arXiv:2503.23278, 2025. URL https://arxiv.org/abs/2503.23278v2 .

- Hou et al. [2022] Zejiang Hou, Julian Salazar, and George Polovets. Meta-learning the difference: Preparing large language models for efficient adaptation. Transactions of the Association for Computational Linguistics , 2022.

- Houlsby et al. [2019] N. Houlsby, A. Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, and S. Gelly. Parameter-efficient transfer learning for nlp. International Conference on Machine Learning , 2019.

- Howard and Kahana [2002] Marc W Howard and M. Kahana. A distributed representation of temporal context. arXiv preprint, 2002.

- Hu et al. [2023] Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo, J. Zhao, and Hang Zhao. Chatdb: Augmenting llms with databases as their symbolic memory, arXiv preprint arXiv:2306.03901, 2023. URL https://arxiv.org/abs/2306.03901v2 .

- Hu et al. [2021] J. E. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models. International Conference on Learning Representations , 2021.

- Hu et al. [2025] Junhao Hu, Wenrui Huang, Weidong Wang, Zhenwen Li, Tiancheng Hu, Zhixia Liu, XuSheng Chen, Tao Xie, and Yizhou Shan. Raas: Reasoning-aware attention sparsity for efficient llm reasoning, arXiv preprint arXiv:2502.11147, 2025. URL https://arxiv.org/abs/2502.11147v2 .

- Hu et al. [20252] Junwei Hu, Weicheng Zheng, Yan Liu, and Yihan Liu. Optimizing token consumption in llms: A nano surge approach for code reasoning efficiency, arXiv preprint arXiv:2504.15989, 20252. URL https://arxiv.org/abs/2504.15989v2 .

- Hu et al. [2020] Junyan Hu, Hanlin Niu, J. Carrasco, B. Lennox, and F. Arvin. Voronoi-based multi-robot autonomous exploration in unknown environments via deep reinforcement learning. IEEE Transactions on Vehicular Technology , 2020.

- Hu et al. [2022] Linmei Hu, Zeyi Liu, Ziwang Zhao, Lei Hou, Liqiang Nie, and Juanzi Li. A survey of knowledge enhanced pre-trained language models. IEEE Transactions on Knowledge and Data Engineering , 2022.

- Hu et al. [2024] Mengkang Hu, Tianxing Chen, Qiguang Chen, Yao Mu, Wenqi Shao, and Ping Luo. Hiagent: Hierarchical working memory management for solving long-horizon agent tasks with large language model, arXiv preprint arXiv:2408.09559, 2024. URL https://arxiv.org/abs/2408.09559 .

- Hu et al. [20232] Nathan J. Hu, E. Mitchell, Christopher D. Manning, and Chelsea Finn. Meta-learning online adaptation of language models. Conference on Empirical Methods in Natural Language Processing , 20232.

- Hu et al. [20242] Shengxiang Hu, Guobing Zou, Song Yang, Yanglan Gan, Bofeng Zhang, and Yixin Chen. Large language model meets graph neural network in knowledge distillation. AAAI Conference on Artificial Intelligence , 20242.

- Hu et al. [20243] Siyuan Hu, Mingyu Ouyang, Difei Gao, and Mike Zheng Shou. The dawn of gui agent: A preliminary case study with claude 3.5 computer use. arXiv preprint, 20243.

- Hu et al. [20233] Ting Hu, Christoph Meinel, and Haojin Yang. Scaled prompt-tuning for few-shot natural language generation, arXiv preprint arXiv:2309.06759, 20233. URL https://arxiv.org/abs/2309.06759v1 .

- Hu et al. [20244] Xiang Hu, Hongyu Fu, Jinge Wang, Yifeng Wang, Zhikun Li, Renjun Xu, Yu Lu, Yaochu Jin, Lili Pan, and Zhenzhong Lan. Nova: An iterative planning and search approach to enhance novelty and diversity of llm generated ideas, arXiv preprint arXiv:2410.14255, 20244. URL https://arxiv.org/abs/2410.14255v2 .

- Hu et al. [20234] Yuntong Hu, Zhengwu Zhang, and Liang Zhao. Beyond text: A deep dive into large language models’ ability on understanding graph data, arXiv preprint arXiv:2310.04944, 20234. URL https://arxiv.org/abs/2310.04944v1 .

- Hua and Artzi [2024] Yilun Hua and Yoav Artzi. Talk less, interact better: Evaluating in-context conversational adaptation in multimodal llms, arXiv preprint arXiv:2408.01417v1, 2024. URL https://arxiv.org/abs/2408.01417v1 .

- Huang et al. [2024] Brandon Huang, Chancharik Mitra, Assaf Arbelle, Leonid Karlinsky, Trevor Darrell, and Roei Herzig. Multimodal task vectors enable many-shot multimodal in-context learning. Neural Information Processing Systems , 2024.

- Huang et al. [2025] Chengkai Huang, Hongtao Huang, Tong Yu, Kaige Xie, Junda Wu, Shuai Zhang, Julian J. McAuley, Dietmar Jannach, and Lina Yao. A survey of foundation model-powered recommender systems: From feature-based, generative to agentic paradigms, arXiv preprint arXiv:2504.16420, 2025. URL https://arxiv.org/abs/2504.16420v1 .

- Huang et al. [20252] Chengkai Huang, Junda Wu, Yu Xia, Zixu Yu, Ruhan Wang, Tong Yu, Ruiyi Zhang, Ryan A. Rossi, B. Kveton, Dongruo Zhou, Julian J. McAuley, and Lina Yao. Towards agentic recommender systems in the era of multimodal large language models, arXiv preprint arXiv:2503.16734, 20252. URL https://arxiv.org/abs/2503.16734v1 .

- Huang et al. [20253] Chengrui Huang, Shen Gao, Zhengliang Shi, Dongsheng Wang, and Shuo Shang. Ttpa: Token-level tool-use preference alignment training framework with fine-grained evaluation, arXiv preprint arXiv:2505.20016, 20253. URL https://arxiv.org/abs/2505.20016v1 .

- Huang et al. [20242] Chensen Huang, Guibo Zhu, Xuepeng Wang, Yifei Luo, Guojing Ge, Haoran Chen, Dong Yi, and Jinqiao Wang. Recurrent context compression: Efficiently expanding the context window of llm, arXiv preprint arXiv:2406.06110, 20242. URL https://arxiv.org/abs/2406.06110v1 .

- Huang et al. [2016] Jing Huang, X. Ruan, Naigong Yu, Qingwu Fan, Jiaming Li, and Jianxian Cai. A cognitive model based on neuromodulated plasticity. Computational Intelligence and Neuroscience , 2016.

- Huang et al. [20254] Ken Huang, Akram Sheriff, Vineeth Sai Narajala, and Idan Habler. Agent capability negotiation and binding protocol (acnbp), arXiv preprint arXiv:2506.13590, 20254. URL https://arxiv.org/abs/2506.13590v1 .

- Huang et al. [20243] Le Huang, Hengzhi Lan, Zijun Sun, Chuan Shi, and Ting Bai. Emotional rag: Enhancing role-playing agents through emotional retrieval. 2024 IEEE International Conference on Knowledge Graph (ICKG) , 20243.

- Huang et al. [20255] Lisheng Huang, Yichen Liu, Jinhao Jiang, Rongxiang Zhang, Jiahao Yan, Junyi Li, and Wayne Xin Zhao. Manusearch: Democratizing deep search in large language models with a transparent and open multi-agent framework, arXiv preprint arXiv:2505.18105, 20255. URL https://arxiv.org/abs/2505.18105v1 .

- Huang et al. [20256] Shiting Huang, Zhen Fang, Zehui Chen, Siyu Yuan, Junjie Ye, Yu Zeng, Lin Chen, Qi Mao, and Feng Zhao. Critictool: Evaluating self-critique capabilities of large language models in tool-calling error scenarios, arXiv preprint arXiv:2506.13977, 20256. URL https://arxiv.org/abs/2506.13977v1 .

- Huang et al. [20244] Sirui Huang, Yanggan Gu, Xuming Hu, Zhonghao Li, Qing Li, and Guandong Xu. Reasoning factual knowledge in structured data with large language models, arXiv preprint arXiv:2408.12188, 20244. URL https://arxiv.org/abs/2408.12188v1 .

- Huang et al. [20257] Sirui Huang, Hanqian Li, Yanggan Gu, Xuming Hu, Qing Li, and Guandong Xu. Hyperg: Hypergraph-enhanced llms for structured knowledge, arXiv preprint arXiv:2502.18125, 20257. URL https://arxiv.org/abs/2502.18125v1 .

- Huang et al. [2022] Wenlong Huang, P. Abbeel, Deepak Pathak, and Igor Mordatch. Language models as zero-shot planners: Extracting actionable knowledge for embodied agents. International Conference on Machine Learning , 2022.

- Huang et al. [20245] Xu Huang, Jianxun Lian, Yuxuan Lei, Jing Yao, Defu Lian, and Xing Xie. Recommender ai agent: Integrating large language models for interactive recommendations, arXiv preprint arXiv:2308.16505, 20245. URL https://arxiv.org/abs/2308.16505 .

- Huang et al. [20246] Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang, Ruiming Tang, and Enhong Chen. Understanding the planning of llm agents: A survey, arXiv preprint arXiv:2402.02716, 20246. URL https://arxiv.org/abs/2402.02716v1 .

- Huang et al. [2023] Y Huang, J Shi, Y Li, C Fan, S Wu, and Q Zhang…. Metatool benchmark for large language models: Deciding whether to use tools and which to use. 2023. URL https://arxiv.org/abs/2310.03128 .

- Huang et al. [20232] Yunpeng Huang, Jingwei Xu, Zixu Jiang, Junyu Lai, Zenan Li, Yuan Yao, Taolue Chen, Lijuan Yang, Zhou Xin, and Xiaoxing Ma. Advancing transformer architecture in long-context large language models: A comprehensive survey, arXiv preprint arXiv:2311.12351, 20232. URL https://arxiv.org/abs/2311.12351v2 .

- Huang et al. [20258] Zeyi Huang, Yuyang Ji, Anirudh Sundara Rajan, Zefan Cai, Wen Xiao, Junjie Hu, and Yong Jae Lee. Visualtoolagent (vista): A reinforcement learning framework for visual tool selection, arXiv preprint arXiv:2505.20289, 20258. URL https://arxiv.org/abs/2505.20289v1 .

- Huang et al. [20233] Ziheng Huang, S. Gutierrez, Hemanth Kamana, and S. Macneil. Memory sandbox: Transparent and interactive memory management for conversational agents. ACM Symposium on User Interface Software and Technology , 20233.

- Huang et al. [20234] Ziheng Huang, Sebastian Gutierrez, Hemanth Kamana, and Stephen MacNeil. Memory sandbox: Transparent and interactive memory management for conversational agents, arXiv preprint arXiv:2308.01542, 20234. URL https://arxiv.org/abs/2308.01542 .

- Huet et al. [2025] Alexis Huet, Zied Ben-Houidi, and Dario Rossi. Episodic memories generation and evaluation benchmark for large language models. International Conference on Learning Representations , 2025.

- Huh and Mohapatra [2023] Dom Huh and Prasant Mohapatra. Multi-agent reinforcement learning: A comprehensive survey, arXiv preprint arXiv:2312.10256, 2023. URL https://arxiv.org/abs/2312.10256v2 .

- Hwang et al. [2024] Eunjeong Hwang, Yichao Zhou, James Bradley Wendt, Beliz Gunel, Nguyen Vo, Jing Xie, and Sandeep Tata. Enhancing incremental summarization with structured representations. Conference on Empirical Methods in Natural Language Processing , 2024.

- Händler [2023] Thorsten Händler. Balancing autonomy and alignment: A multi-dimensional taxonomy for autonomous llm-powered multi-agent architectures. arXiv preprint, 2023.

- Iannelli et al. [2024] Michael Iannelli, Sneha Kuchipudi, and Vera Dvorak. Sla management in reconfigurable multi-agent rag: A systems approach to question answering, arXiv preprint arXiv:2412.06832, 2024. URL https://arxiv.org/abs/2412.06832v2 .

- IBM [2025] IBM. What is agent communication protocol (acp)? https://www.ibm.com/think/topics/agent-communication-protocol , 2025. [Online; accessed 17-July-2025].

- Inaba et al. [2023] T Inaba, H Kiyomaru, F Cheng, and S Kurohashi. Multitool-cot: Gpt-3 can use multiple external tools with chain of thought prompting. 2023. URL https://arxiv.org/abs/2305.16896 .

- Indiveri and Liu [2015] G. Indiveri and Shih-Chii Liu. Memory and information processing in neuromorphic systems. Proceedings of the IEEE , 2015.

- Ioannidis et al. [2022] V. Ioannidis, Xiang Song, Da Zheng, Houyu Zhang, Jun Ma, Yi Xu, Belinda Zeng, Trishul M. Chilimbi, and G. Karypis. Efficient and effective training of language and graph neural network models, arXiv preprint arXiv:2206.10781, 2022. URL https://arxiv.org/abs/2206.10781v1 .

- Ishibashi et al. [2024] Yoichi Ishibashi, Taro Yano, and M. Oyamada. Can large language models invent algorithms to improve themselves?: Algorithm discovery for recursive self-improvement through reinforcement learning, arXiv preprint arXiv:2410.15639, 2024. URL https://arxiv.org/abs/2410.15639v5 .

- Iskander et al. [2024] Shadi Iskander, Nachshon Cohen, Zohar S. Karnin, Ori Shapira, and Sofia Tolmach. Quality matters: Evaluating synthetic data for tool-using llms. Conference on Empirical Methods in Natural Language Processing , 2024.

- Ismail and Sariff [2018] Z. Ismail and N. Sariff. A survey and analysis of cooperative multi-agent robot systems: Challenges and directions. Applications of Mobile Robots , 2018.

- Izmirlioglu et al. [2024] Yusuf Izmirlioglu, Loc Pham, Tran Cao Son, and Enrico Pontelli. A survey of multi-agent systems for smartgrids. Energies , 2024.

- Jace.AI [2024] Jace.AI. Jace.ai web agent, 2024. URL https://www.jace.ai/ . Accessed: 2025-07-14.

- Jacot et al. [2018] Arthur Jacot, Franck Gabriel, and Clément Hongler. Neural tangent kernel: Convergence and generalization in neural networks. Neural Information Processing Systems , 2018.

- Jade and Yartsev [2025] Tejas Jade and Alex Yartsev. Chatgpt for automated grading of short answer questions in mechanical ventilation, arXiv preprint arXiv:2505.04645, 2025. URL https://arxiv.org/abs/2505.04645v1 .

- Jafarpour et al. [2014] A. Jafarpour, L. Fuentemilla, A. Horner, W. Penny, and E. Duzel. Replay of very early encoding representations during recollection. Journal of Neuroscience , 2014.

- Jaiswal et al. [2024] A. Jaiswal, Nurendra Choudhary, Ravinarayana Adkathimar, M. P. Alagappan, G. Hiranandani, Ying Ding, Zhangyang Wang, E-Wen Huang, and Karthik Subbian. All against some: Efficient integration of large language models for message passing in graph neural networks, arXiv preprint arXiv:2407.14996, 2024. URL https://arxiv.org/abs/2407.14996v1 .

- Jaleel et al. [2020] H. Jaleel, Jane J. Stephan, and Sinan Naji. Multi-agent systems: A review study. Ibn AL- Haitham Journal For Pure and Applied Sciences , 2020.

- Jang et al. [2024] Lawrence Jang, Yinheng Li, Charles Ding, Justin Lin, Paul Pu Liang, Dan Zhao, Rogerio Bonatti, and K. Koishida. Videowebarena: Evaluating long context multimodal agents with video understanding web tasks. International Conference on Learning Representations , 2024.

- Janik [2023] R. Janik. Aspects of human memory and large language models, arXiv preprint arXiv:2311.03839, 2023. URL https://arxiv.org/abs/2311.03839v3 .

- Javaid et al. [2024] Shumaila Javaid, Hamza Fahim, Bin He, and Nasir Saeed. Large language models for uavs: Current state and pathways to the future. IEEE Open Journal of Vehicular Technology , 2024.

- Jayram et al. [2018] T. S. Jayram, Younes Bouhadjar, Ryan L. McAvoy, Tomasz Kornuta, Alexis Asseman, K. Rocki, and A. Ozcan. Learning to remember, forget and ignore using attention control in memory, arXiv preprint arXiv:1809.11087, 2018. URL https://arxiv.org/abs/1809.11087v1 .

- Jeong [2025] Cheonsu Jeong. A study on the mcp x a2a framework for enhancing interoperability of llm-based autonomous agents, arXiv preprint arXiv:2506.01804, 2025. URL https://arxiv.org/abs/2506.01804v2 .

- Ji and Bilmes [2004] Gang Ji and J. Bilmes. Multi-speaker language modeling. North American Chapter of the Association for Computational Linguistics , 2004.

- Ji et al. [2024] Ke Ji, Junying Chen, Anningzhe Gao, Wenya Xie, Xiang Wan, and Benyou Wang. Llms could autonomously learn without external supervision, arXiv preprint arXiv:2406.00606, 2024. URL https://arxiv.org/abs/2406.00606v2 .

- Ji et al. [2020] Shaoxiong Ji, Shirui Pan, E. Cambria, P. Marttinen, and Philip S. Yu. A survey on knowledge graphs: Representation, acquisition, and applications. IEEE Transactions on Neural Networks and Learning Systems , 2020.

- Jiang et al. [2025] Bowen Jiang, Runchuan Zhu, Jiang Wu, Zinco Jiang, Yifan He, Junyuan Gao, Jia Yu, Rui Min, Yinfan Wang, Haote Yang, et al. Evaluating large language model with knowledge oriented language specific simple question answering. 2025.

- Jiang et al. [2022] Caigao Jiang, Siqiao Xue, James Zhang, Lingyue Liu, Zhibo Zhu, and Hongyan Hao. Learning large-scale universal user representation with sparse mixture of experts, arXiv preprint arXiv:2207.04648, 2022. URL https://arxiv.org/abs/2207.04648v1 .

- Jiang et al. [2023] Feibo Jiang, Li Dong, Yubo Peng, Kezhi Wang, Kun Yang, Cunhua Pan, D. Niyato, and O. Dobre. Large language model enhanced multi-agent systems for 6g communications. IEEE wireless communications , 2023.

- Jiang et al. [2024] J Jiang, K Zhou, WX Zhao, Y Song, and C Zhu…. Kg-agent: An efficient autonomous agent framework for complex reasoning over knowledge graph. 2024. URL https://arxiv.org/abs/2402.11163 .

- Jiang et al. [20222] Jinhao Jiang, Kun Zhou, Wayne Xin Zhao, and Ji rong Wen. Unikgqa: Unified retrieval and reasoning for solving multi-hop question answering over knowledge graph. International Conference on Learning Representations , 20222.

- Jiang et al. [20232] Jinhao Jiang, Kun Zhou, Zican Dong, Keming Ye, Wayne Xin Zhao, and Ji rong Wen. Structgpt: A general framework for large language model to reason over structured data. Conference on Empirical Methods in Natural Language Processing , 20232.

- Jiang et al. [20233] Song Jiang, Zahra Shakeri, Aaron Chan, Maziar Sanjabi, Hamed Firooz, Yinglong Xia, Bugra Akyildiz, Yizhou Sun, Jinchao Li, Qifan Wang, and Asli Celikyilmaz. Resprompt: Residual connection prompting advances multi-step reasoning in large language models. North American Chapter of the Association for Computational Linguistics , 20233.

- Jiang et al. [20234] Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie Callan, and Graham Neubig. Active retrieval augmented generation. Conference on Empirical Methods in Natural Language Processing , 20234.

- Jiang et al. [20252] Zhonglin Jiang, Qian Tang, and Zequn Wang. Generative reliability-based design optimization using in-context learning capabilities of large language models, arXiv preprint arXiv:2503.22401, 20252. URL https://arxiv.org/abs/2503.22401v1 .

- Jiang et al. [20242] Zhuoxuan Jiang, Haoyuan Peng, Shanshan Feng, Fan Li, and Dongsheng Li. Llms can find mathematical reasoning mistakes by pedagogical chain-of-thought. International Joint Conference on Artificial Intelligence , 20242.

- Jimenez et al. [2024] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. Swe-bench: Can language models resolve real-world github issues?, arXiv preprint arXiv:2310.06770, 2024. URL https://arxiv.org/abs/2310.06770 .

- Jin et al. [2024] B Jin, C Xie, J Zhang, KK Roy, Y Zhang, and Z Li…. Graph chain-of-thought: Augmenting large language models by reasoning on graphs. 2024. URL https://arxiv.org/abs/2404.07103 .

- Jin et al. [2022] Bowen Jin, Yu Zhang, Qi Zhu, and Jiawei Han. Heterformer: Transformer-based deep node representation learning on heterogeneous text-rich networks. Knowledge Discovery and Data Mining , 2022.

- Jin et al. [2023] Feihu Jin, Jiajun Zhang, and Chengqing Zong. Parameter-efficient tuning for large language model without calculating its gradients. Conference on Empirical Methods in Natural Language Processing , 2023.

- Jin et al. [20242] Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, Bo Li, and Huaming Chen. From llms to llm-based agents for software engineering: A survey of current, challenges and future, arXiv preprint arXiv:2408.02479, 20242. URL https://arxiv.org/abs/2408.02479v2 .

- Jin et al. [20243] Hongye Jin, Xiaotian Han, Jingfeng Yang, Zhimeng Jiang, Zirui Liu, Chia yuan Chang, Huiyuan Chen, and Xia Hu. Llm maybe longlm: Self-extend llm context window without tuning. International Conference on Machine Learning , 20243.

- Jin et al. [20244] Jiajie Jin, Yutao Zhu, Xinyu Yang, Chenghao Zhang, and Zhicheng Dou. Flashrag: A modular toolkit for efficient retrieval-augmented generation research. The Web Conference , 20244.

- Jin et al. [20232] Qiao Jin, Yifan Yang, Qingyu Chen, and Zhiyong Lu. Genegpt: Augmenting large language models with domain tools for improved access to biomedical information. Bioinform. , 20232.

- Jin et al. [20245] Tian Jin, W. Yazar, Zifei Xu, Sayeh Sharify, and Xin Wang. Self-selected attention span for accelerating large language model inference, arXiv preprint arXiv:2404.09336, 20245. URL https://arxiv.org/abs/2404.09336v1 .

- Jin et al. [2025] Weiqiang Jin, Hongyang Du, Biao Zhao, Xingwu Tian, Bohang Shi, and Guang Yang. A comprehensive survey on multi-agent cooperative decision-making: Scenarios, approaches, challenges and perspectives. arXiv preprint, 2025.

- Jin et al. [20233] Yang Jin, Kun Xu, Kun Xu, Liwei Chen, Chao Liao, Jianchao Tan, Quzhe Huang, Bin Chen, Chenyi Lei, An Liu, Chengru Song, Xiaoqiang Lei, Di Zhang, Wenwu Ou, Kun Gai, and Yadong Mu. Unified language-vision pretraining in llm with dynamic discrete visual tokenization. International Conference on Learning Representations , 20233.

- Jin et al. [20246] Yiqiao Jin, Minje Choi, Gaurav Verma, Jindong Wang, and Srijan Kumar. Mm-soc: Benchmarking multimodal large language models in social media platforms. Annual Meeting of the Association for Computational Linguistics , 20246.

- Jin et al. [20252] Yiyang Jin, Kunzhao Xu, Hang Li, Xueting Han, Yanmin Zhou, Cheng Li, and Jing Bai. Reveal: Self-evolving code agents via iterative generation-verification, arXiv preprint arXiv:2506.11442, 20252. URL https://arxiv.org/abs/2506.11442v1 .

- Johnson et al. [2017] Jeff Johnson, Matthijs Douze, and H. Jégou. Billion-scale similarity search with gpus. IEEE Transactions on Big Data , 2017.

- Johnson and Bullock [2023] Jeff A. Johnson and Daniel H. Bullock. Fragility in ais using artificial neural networks. Communications of the ACM , 2023.

- Kaiya et al. [2023] Zhao Kaiya, Michelangelo Naim, J. Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo, Guangyu Robert Yang, and Andrew Ahn. Lyfe agents: Generative agents for low-cost real-time social interactions, arXiv preprint arXiv:2310.02172, 2023. URL https://arxiv.org/abs/2310.02172v1 .

- Kaiyrbekov et al. [2025] Kurmanbek Kaiyrbekov, Nic Dobbins, and Sean D. Mooney. Automated survey collection with llm-based conversational agents, arXiv preprint arXiv:2504.02891, 2025. URL https://arxiv.org/abs/2504.02891v1 .

- Kakas et al. [2008] A. Kakas, P. Mancarella, F. Sadri, Kostas Stathis, and Francesca Toni. Computational logic foundations of kgp agents. Journal of Artificial Intelligence Research , 2008.

- Kamra et al. [2024] Vikas Kamra, Lakshya Gupta, Dhruv Arora, and Ashwin Kumar Yadav. Enhancing document retrieval using ai and graph-based rag techniques. 2024 5th International Conference on Communication, Computing & Industry 6.0 (C2I6) , 2024.

- Kandogan et al. [2025] Eser Kandogan, Nikita Bhutani, Dan Zhang, Rafael Li Chen, Sairam Gurajada, and Estevam R. Hruschka. Orchestrating agents and data for enterprise: A blueprint architecture for compound ai, arXiv preprint arXiv:2504.08148, 2025. URL https://arxiv.org/abs/2504.08148v1 .

- Kang et al. [2024] Haoyu Kang, Yuzhou Zhu, Yukun Zhong, Ke Wang Central South University, Dalian University of Technology, Nanjing University, and Xidian University. Sakr: Enhancing retrieval-augmented generation via streaming algorithm and k-means clustering. arXiv preprint, 2024.

- Kang et al. [2025] Jiazheng Kang, Mingming Ji, Zhe Zhao, and Ting Bai. Memory os of ai agent, arXiv preprint arXiv:2506.06326, 2025. URL https://arxiv.org/abs/2506.06326v1 .

- Kang et al. [20252] Jikun Kang, Wenqi Wu, Filippos Christianos, Alex J. Chan, Fraser Greenlee, George Thomas, Marvin Purtorab, and Andy Toulis. Lm2: Large memory models, arXiv preprint arXiv:2502.06049, 20252. URL https://arxiv.org/abs/2502.06049v1 .

- Kang et al. [2023] Sungmin Kang, Gabin An, and S. Yoo. A quantitative and qualitative evaluation of llm-based explainable fault localization. Proc. ACM Softw. Eng. , 2023.

- Kaplan et al. [2024] Guy Kaplan, Matanel Oren, Yuval Reif, and Roy Schwartz. From tokens to words: On the inner lexicon of llms. International Conference on Learning Representations , 2024.

- Karpukhin et al. [2020] Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Yu Wu, Sergey Edunov, Danqi Chen, and Wen tau Yih. Dense passage retrieval for open-domain question answering. Conference on Empirical Methods in Natural Language Processing , 2020.

- Kasner and Dusek [2024] Zdeněk Kasner and Ondrej Dusek. Beyond traditional benchmarks: Analyzing behaviors of open llms on data-to-text generation. Annual Meeting of the Association for Computational Linguistics , 2024.

- Kate et al. [2025] Kiran Kate, Tejaswini Pedapati, Kinjal Basu, Yara Rizk, Vijil Chenthamarakshan, Subhajit Chaudhury, Mayank Agarwal, and Ibrahim Abdelaziz. Longfunceval: Measuring the effectiveness of long context models for function calling, arXiv preprint arXiv:2505.10570, 2025. URL https://arxiv.org/abs/2505.10570v1 .

- Katharopoulos et al. [2020] Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Franccois Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention. International Conference on Machine Learning , 2020.

- Katrix et al. [2025] Richard Katrix, Quentin Carroway, Rowan Hawkesbury, and Matthias Heathfield. Context-aware semantic recomposition mechanism for large language models, arXiv preprint arXiv:2501.17386, 2025. URL https://arxiv.org/abs/2501.17386v2 .

- Kazemnejad et al. [2023] Amirhossein Kazemnejad, Inkit Padhi, K. Ramamurthy, Payel Das, and Siva Reddy. The impact of positional encoding on length generalization in transformers. Neural Information Processing Systems , 2023.

- Kelley et al. [2018] T. Kelley, R. Thomson, and Jonathan Milton. Standard model of mind: Episodic memory. Biologically Inspired Cognitive Architectures , 2018.

- Kepel and Valogianni [2024] Daan Kepel and Konstantina Valogianni. Autonomous prompt engineering in large language models, arXiv preprint arXiv:2407.11000, 2024. URL https://arxiv.org/abs/2407.11000v1 .

- Kesner [2013] R. Kesner. Neurobiological foundations of an attribute model of memory. arXiv preprint, 2013.

- Khan et al. [2024] A. Khan, Md Toufique Hasan, Kai-Kristian Kemell, Jussi Rasku, and Pekka Abrahamsson. Developing retrieval augmented generation (rag) based llm systems from pdfs: An experience report, arXiv preprint arXiv:2410.15944, 2024. URL https://arxiv.org/abs/2410.15944v1 .

- Khan et al. [20242] Muhammad Tayyab Khan, Lequn Chen, Ye Han Ng, Wenhe Feng, Nicholas Yew Jin Tan, and Seung Ki Moon. Leveraging vision-language models for manufacturing feature recognition in cad designs, arXiv preprint arXiv:2411.02810, 20242. URL https://arxiv.org/abs/2411.02810v1 .

- Khandelwal et al. [2019] Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke Zettlemoyer, and M. Lewis. Generalization through memorization: Nearest neighbor language models. International Conference on Learning Representations , 2019.

- Khatibi et al. [2025] Elahe Khatibi, Ziyu Wang, and Amir M. Rahmani. Cdf-rag: Causal dynamic feedback for adaptive retrieval-augmented generation. arXiv preprint, 2025.

- Khosla et al. [2020] Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, and Dilip Krishnan. Supervised contrastive learning. Neural Information Processing Systems , 2020.

- Khot et al. [2022] Tushar Khot, H. Trivedi, Matthew Finlayson, Yao Fu, Kyle Richardson, Peter Clark, and Ashish Sabharwal. Decomposed prompting: A modular approach for solving complex tasks. International Conference on Learning Representations , 2022.

- Khurana et al. [2024] Sambhav Khurana, Xiner Li, Shurui Gui, and Shuiwang Ji. A hierarchical language model for interpretable graph reasoning, arXiv preprint arXiv:2410.22372, 2024. URL https://arxiv.org/abs/2410.22372v1 .

- Kim et al. [2024] Daehee Kim, Deokhyung Kang, Sangwon Ryu, and Gary Geunbae Lee. Ontology-free general-domain knowledge graph-to-text generation dataset synthesis using large language model, arXiv preprint arXiv:2409.07088, 2024. URL https://arxiv.org/abs/2409.07088v1 .

- Kim et al. [2023] Geunwoo Kim, P. Baldi, and S. McAleer. Language models can solve computer tasks. Neural Information Processing Systems , 2023.

- Kim et al. [20242] Jaeyeon Kim, Injune Hwang, and Kyogu Lee. Learning semantic information from raw audio signal using both contextual and phonetic representations. IEEE International Conference on Acoustics, Speech, and Signal Processing , 20242.

- Kim et al. [20232] Jang-Hyun Kim, Junyoung Yeom, Sangdoo Yun, and Hyun Oh Song. Compressed context memory for online language model interaction. International Conference on Learning Representations , 20232.

- Kim et al. [20233] Jiho Kim, Yeonsu Kwon, Yohan Jo, and Edward Choi. Kg-gpt: A general framework for reasoning on knowledge graphs using large language models. Conference on Empirical Methods in Natural Language Processing , 20233.

- Kim et al. [2025] Jiin Kim, Byeongjun Shin, Jinha Chung, and Minsoo Rhu. The cost of dynamic reasoning: Demystifying ai agents and test-time scaling from an ai infrastructure perspective, arXiv preprint arXiv:2506.04301, 2025. URL https://arxiv.org/abs/2506.04301v1 .

- Kim et al. [20234] Sehoon Kim, Suhong Moon, Ryan Tabrizi, Nicholas Lee, Michael W. Mahoney, Kurt Keutzer, and A. Gholami. An llm compiler for parallel function calling. International Conference on Machine Learning , 20234.

- Kim et al. [20235] Taewoon Kim, Michael Cochez, Vincent Francois-Lavet, Mark Neerincx, and Piek Vossen. A machine with short-term, episodic, and semantic memory systems. Proceedings of the AAAI Conference on Artificial Intelligence , 37(1):48–56, 20235. ISSN 2159-5399. 10.1609/aaai.v37i1.25075 . URL http://dx.doi.org/10.1609/aaai.v37i1.25075 .

- Kirchdorfer et al. [2025] Lukas Kirchdorfer, Robert Blümel, T. Kampik, Han van der Aa, and Heiner Stuckenschmidt. Discovering multi-agent systems for resource-centric business process simulation. Process Science , 2025.

- Kirkpatrick et al. [2016] J. Kirkpatrick, Razvan Pascanu, Neil C. Rabinowitz, J. Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, A. Grabska-Barwinska, D. Hassabis, C. Clopath, D. Kumaran, and R. Hadsell. Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences of the United States of America , 2016.

- Kirsch et al. [2022] Louis Kirsch, James Harrison, Jascha Narain Sohl-Dickstein, and Luke Metz. General-purpose in-context learning by meta-learning transformers, arXiv preprint arXiv:2212.04458, 2022. URL https://arxiv.org/abs/2212.04458v2 .

- Kirstain et al. [2021] Yuval Kirstain, Patrick Lewis, Sebastian Riedel, and Omer Levy. A few more examples may be worth billions of parameters. Conference on Empirical Methods in Natural Language Processing , 2021.

- Kiruluta et al. [2025] Andrew Kiruluta, Preethi Raju, and Priscilla Burity. Breaking quadratic barriers: A non-attention llm for ultra-long context horizons, arXiv preprint arXiv:2506.01963, 2025. URL https://arxiv.org/abs/2506.01963v1 .

- Kitaev et al. [2020] Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. International Conference on Learning Representations , 2020.

- Koc et al. [2025] Vincent Koc, Jacques Verre, Douglas Blank, and Abigail Morgan. Mind the metrics: Patterns for telemetry-aware in-ide ai application development using the model context protocol (mcp), arXiv preprint arXiv:2506.11019, 2025. URL https://arxiv.org/abs/2506.11019v1 .

- Kociský et al. [2017] Tomás Kociský, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gábor Melis, and Edward Grefenstette. The narrativeqa reading comprehension challenge. Transactions of the Association for Computational Linguistics , 2017.

- Koh et al. [2023] Jing Yu Koh, R. Salakhutdinov, and Daniel Fried. Grounding language models to images for multimodal inputs and outputs. International Conference on Machine Learning , 2023.

- Koh et al. [2024] Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, and Daniel Fried. Visualwebarena: Evaluating multimodal agents on realistic visual web tasks, arXiv preprint arXiv:2401.13649, 2024. URL https://arxiv.org/abs/2401.13649v2 .

- Kojima et al. [2022] Takeshi Kojima, S. Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. Neural Information Processing Systems , 2022.

- Kong et al. [2023] Yilun Kong, Jingqing Ruan, Yihong Chen, Bin Zhang, Tianpeng Bao, Shiwei Shi, Guoqing Du, Xiaoru Hu, Hangyu Mao, Ziyue Li, Xingyu Zeng, and Rui Zhao. Tptu-v2: Boosting task planning and tool usage of large language model-based agents in real-world systems, arXiv preprint arXiv:2311.11315, 2023. URL https://arxiv.org/abs/2311.11315 .

- Korzyński et al. [2023] P. Korzyński, G. Mazurek, Pamela Krzypkowska, and Artur Kurasiński. Artificial intelligence prompt engineering as a new digital competence: Analysis of generative ai technologies such as chatgpt. Entrepreneurial Business and Economics Review , 2023.

- Kramer [2025] Oliver Kramer. Cognitive prompts using guilford’s structure of intellect model. arXiv preprint, 2025.

- Kramer [20252] Oliver Kramer. Conceptual metaphor theory as a prompting paradigm for large language models, arXiv preprint arXiv:2502.01901, 20252. URL https://arxiv.org/abs/2502.01901v1 .

- Kramer and Baumann [2024] Oliver Kramer and Jill Baumann. Unlocking structured thinking in language models with cognitive prompting. ESANN 2025 proceesdings , 2024.

- Kravari and Bassiliades [2015] K. Kravari and Nick Bassiliades. A survey of agent platforms. Journal of Artificial Societies and Social Simulation , 2015.

- Krishnan et al. [2023] Prashant Krishnan, Zilong Wang, Yangkun Wang, and Jingbo Shang. Towards few-shot entity recognition in document images: A graph neural network approach robust to image manipulation. International Conference on Language Resources and Evaluation , 2023.

- Kruijne et al. [2019] W. Kruijne, S. Bohté, P. Roelfsema, and C. Olivers. Flexible working memory through selective gating and attentional tagging. bioRxiv , 2019.

- Krupp et al. [2025] L. Krupp, Daniel Geissler, P. Lukowicz, and Jakob Karolus. Towards sustainable web agents: A plea for transparency and dedicated metrics for energy consumption, arXiv preprint arXiv:2502.17903, 2025. URL https://arxiv.org/abs/2502.17903v1 .

- Kuhail et al. [2024] M. Kuhail, Jose Berengueres, Fatma Taher, Sana Z. Khan, and Ansah Siddiqui. Designing a haptic boot for space with prompt engineering: Process, insights, and implications. IEEE Access , 2024.

- Kumar et al. [2024] Amandeep Kumar, Muzammal Naseer, Sanath Narayan, R. Anwer, Salman H. Khan, and Hisham Cholakkal. Multi-modal generation via cross-modal in-context learning, arXiv preprint arXiv:2405.18304v1, 2024. URL https://arxiv.org/abs/2405.18304v1 .

- Kumar et al. [2025] Rajeev Kumar, Harishankar Kumar, and Kumari Shalini. Detecting and mitigating bias in llms through knowledge graph-augmented training. 2025 International Conference on Artificial Intelligence and Data Engineering (AIDE) , 2025.

- Kwon et al. [2025] Taeyoon Kwon, Dongwook Choi, Sunghwan Kim, Hyojun Kim, Seungjun Moon, Beong woo Kwak, Kuan-Hao Huang, and Jinyoung Yeo. Embodied agents meet personalization: Exploring memory utilization for personalized assistance, arXiv preprint arXiv:2505.16348, 2025. URL https://arxiv.org/abs/2505.16348v1 .

- Kwon et al. [2023] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Haotong Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. Symposium on Operating Systems Principles , 2023.

- Lai et al. [2019] T. Lai, Quan Hung Tran, Trung Bui, and D. Kihara. A gated self-attention memory network for answer selection. Conference on Empirical Methods in Natural Language Processing , 2019.

- Lamba [2024] Divya Lamba. The role of prompt engineering in improving language understanding and generation. International Journal For Multidisciplinary Research , 2024.

- Lan et al. [2025] Xiaochong Lan, Jie Feng, Jia Lei, Xinlei Shi, and Yong Li. Benchmarking and advancing large language models for local life services, arXiv preprint arXiv:2506.02720, 2025. URL https://arxiv.org/abs/2506.02720v1 .

- LangChain Team [2025] LangChain Team. Memory in langgraph. https://langchain-ai.github.io/langgraph/concepts/memory/ , 2025. Accessed: 2025-07-17.

- Langlois et al. [2020] Samuel T. Langlois, Oghenetekevwe Akoroda, Estefany Carrillo, J. Herrmann, S. Azarm, Huan Xu, and Michael W. Otte. Metareasoning structures, problems, and modes for multiagent systems: A survey. IEEE Access , 2020.

- Lattimer et al. [2024] B. Lattimer, Varun Gangal, Ryan McDonald, and Yi Yang. Sparse rewards can self-train dialogue agents, arXiv preprint arXiv:2409.04617, 2024. URL https://arxiv.org/abs/2409.04617v2 .

- Lau and McManus [2024] Pak Kin Lau and Stuart Michael McManus. Mining asymmetric intertextuality, arXiv preprint arXiv:2410.15145, 2024. URL https://arxiv.org/abs/2410.15145v1 .

- Le et al. [2020] Hung Le, T. Tran, and S. Venkatesh. Self-attentive associative memory. International Conference on Machine Learning , 2020.

- Lee et al. [2025] Dohyun Lee, Seungil Chad Lee, Chanwoo Yang, Yujin Baek, and Jaegul Choo. Exploring in-context example generation for machine translation, arXiv preprint arXiv:2506.00507, 2025. URL https://arxiv.org/abs/2506.00507v1 .

- Lee et al. [2024] Dongyub Lee, Eunhwan Park, Hodong Lee, and Heuiseok Lim. Ask, assess, and refine: Rectifying factual consistency and hallucination in llms with metric-guided feedback learning. Conference of the European Chapter of the Association for Computational Linguistics , 2024.

- Lee [2024] Eunhae Lee. Towards ethical personal ai applications: Practical considerations for ai assistants with long-term memory, arXiv preprint arXiv:2409.11192, 2024. URL https://arxiv.org/abs/2409.11192v1 .

- Lee et al. [2023] Gibbeum Lee, Volker Hartmann, Jongho Park, Dimitris Papailiopoulos, and Kangwook Lee. Prompted llms as chatbot modules for long open-domain conversation. In Findings of the Association for Computational Linguistics: ACL 2023 . Association for Computational Linguistics, 2023. 10.18653/v1/2023.findings-acl.277 . URL http://dx.doi.org/10.18653/v1/2023.findings-acl.277 .

- Lee et al. [20242] Heejun Lee, Geon Park, Youngwan Lee, Jina Kim, Wonyoung Jeong, Myeongjae Jeon, and Sung Ju Hwang. A training-free sub-quadratic cost transformer model serving framework with hierarchically pruned attention, arXiv preprint arXiv:2406.09827, 20242. URL https://arxiv.org/abs/2406.09827v3 .

- Lee et al. [20252] Ho-Jun Lee, Junho Kim, Hyunjun Kim, and Yonghyun Ro. Refocus: Reinforcement-guided frame optimization for contextual understanding, arXiv preprint arXiv:2506.01274v1, 20252. URL https://arxiv.org/abs/2506.01274v1 .

- Lee et al. [20232] Jonathan Lee, Annie Xie, Aldo Pacchiano, Yash Chandak, Chelsea Finn, Ofir Nachum, and E. Brunskill. Supervised pretraining can learn in-context reinforcement learning. Neural Information Processing Systems , 20232.

- Lee et al. [20253] Namkyeong Lee, E. Brouwer, Ehsan Hajiramezanali, Chanyoung Park, and Gabriele Scalia. Rag-enhanced collaborative llm agents for drug discovery, arXiv preprint arXiv:2502.17506, 20253. URL https://arxiv.org/abs/2502.17506v2 .

- Lee et al. [20243] Shinbok Lee, Gaeun Seo, Daniel Lee, Byeongil Ko, Sunghee Jung, and M. Shin. Functionchat-bench: Comprehensive evaluation of language models’ generative capabilities in korean tool-use dialogs. arXiv preprint, 20243.

- Lee et al. [20244] Younghun Lee, Sungchul Kim, Ryan A. Rossi, Tong Yu, and Xiang Chen. Learning to reduce: Towards improving performance of large language models on structured data, arXiv preprint arXiv:2407.02750, 20244. URL https://arxiv.org/abs/2407.02750v1 .

- Lee et al. [20245] Younghun Lee, Sungchul Kim, Tong Yu, Ryan A. Rossi, and Xiang Chen. Learning to reduce: Optimal representations of structured data in prompting large language models, arXiv preprint arXiv:2402.14195, 20245. URL https://arxiv.org/abs/2402.14195v1 .

- Lee et al. [20254] Yu-Ting Lee, Hui-Ying Shih, Fu-Chieh Chang, and Pei-Yuan Wu. An explanation of intrinsic self-correction via linear representations and latent concepts, arXiv preprint arXiv:2505.11924, 20254. URL https://arxiv.org/abs/2505.11924v1 .

- Lehman and Malmberg [2013] Melissa Lehman and Kenneth J. Malmberg. A buffer model of memory encoding and temporal correlations in retrieval. Psychology Review , 2013.

- Lei et al. [2025] Yiming Lei, Zhizheng Yang, Zeming Liu, Haitao Leng, Shaoguo Liu, Tingting Gao, Qingjie Liu, and Yunhong Wang. Contextqformer: A new context modeling method for multi-turn multi-modal conversations, arXiv preprint arXiv:2505.23121v1, 2025. URL https://arxiv.org/abs/2505.23121v1 .

- Lester et al. [2021] Brian Lester, Rami Al-Rfou, and Noah Constant. The power of scale for parameter-efficient prompt tuning. Conference on Empirical Methods in Natural Language Processing , 2021.

- Lewis et al. [2020] Patrick Lewis, Ethan Perez, Aleksandara Piktus, F. Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, M. Lewis, Wen tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. Retrieval-augmented generation for knowledge-intensive nlp tasks. Neural Information Processing Systems , 2020.

- Li et al. [2021] Bohan Li, Yutai Hou, and Wanxiang Che. Data augmentation approaches in natural language processing: A survey. AI Open , 2021.

- Li et al. [20212] Chaozhuo Li, Bochen Pang, Yuming Liu, Hao Sun, Zheng Liu, Xing Xie, Tianqi Yang, Yanling Cui, Liangjie Zhang, and Qi Zhang. Adsgnn: Behavior-graph augmented relevance modeling in sponsored search. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 20212.

- Li et al. [2025] Chengpeng Li, Zhengyang Tang, Ziniu Li, Mingfeng Xue, Keqin Bao, Tian Ding, Ruoyu Sun, Benyou Wang, Xiang Wang, Junyang Lin, and Dayiheng Liu. Cort: Code-integrated reasoning within thinking, arXiv preprint arXiv:2506.09820, 2025. URL https://arxiv.org/abs/2506.09820v2 .

- Li et al. [2023] Chengshu Li, Jacky Liang, Andy Zeng, Xinyun Chen, Karol Hausman, Dorsa Sadigh, Sergey Levine, Fei-Fei Li, Fei Xia, and Brian Ichter. Chain of code: Reasoning with a language model-augmented code emulator. International Conference on Machine Learning , 2023.

- Li et al. [2024] Chuanhao Li, Runhan Yang, Tiankai Li, Milad Bafarassat, Kourosh Sharifi, Dirk Bergemann, and Zhuoran Yang. Stride: A tool-assisted llm agent framework for strategic and interactive decision-making, arXiv preprint arXiv:2405.16376, 2024. URL https://arxiv.org/abs/2405.16376v2 .

- Li et al. [2022] Daliang Li, Ankit Singh Rawat, Manzil Zaheer, Xin Wang, Michal Lukasik, Andreas Veit, Felix Yu, and Sanjiv Kumar. Large language models with controllable working memory, arXiv preprint arXiv:2211.05110, 2022. URL https://arxiv.org/abs/2211.05110 .

- Li and Murr [2024] Daniel Li and Lincoln Murr. Humaneval on latest gpt models - 2024. arXiv preprint, 2024.

- Li et al. [20242] Fu Li, Xueying Wang, Bin Li, Yunlong Wu, Yanzhen Wang, and Xiaodong Yi. A study on training and developing large language models for behavior tree generation, arXiv preprint arXiv:2401.08089, 20242. URL https://arxiv.org/abs/2401.08089v1 .

- Li et al. [20232] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. Camel: Communicative agents for "mind" exploration of large language model society. In Thirty-seventh Conference on Neural Information Processing Systems , 20232.

- Li et al. [20243] Guozheng Li, Peng Wang, Jiajun Liu, Yikai Guo, Ke Ji, Ziyu Shang, and Zijie Xu. Meta in-context learning makes large language models better zero and few-shot relation extractors. International Joint Conference on Artificial Intelligence , 20243.

- Li et al. [20233] Haoyang Li, Jing Zhang, Cuiping Li, and Hong Chen. Resdsql: Decoupling schema linking and skeleton parsing for text-to-sql. AAAI Conference on Artificial Intelligence , 20233.

- Li et al. [20234] Jia Li, Ge Li, Yongming Li, and Zhi Jin. Structured chain-of-thought prompting for code generation. ACM Transactions on Software Engineering and Methodology , 20234.

- Li et al. [20244] Jia Li, Xiangguo Sun, Yuhan Li, Zhixun Li, Hong Cheng, and Jeffrey Xu Yu. Graph intelligence with large language models and prompt learning. Knowledge Discovery and Data Mining , 20244.

- Li et al. [20245] Jiahao Nick Li, Yan Xu, Tovi Grossman, Stephanie Santosa, and Michelle Li. Omniactions: Predicting digital actions in response to real-world multimodal sensory inputs with llms. International Conference on Human Factors in Computing Systems , 20245.

- Li et al. [20246] Jiarui Li, Ye Yuan, and Zehua Zhang. Enhancing llm factual accuracy with rag to counter hallucinations: A case study on domain-specific queries in private knowledge-bases, arXiv preprint arXiv:2403.10446, 20246. URL https://arxiv.org/abs/2403.10446v1 .

- Li et al. [20235] Juncheng Li, Kaihang Pan, Zhiqi Ge, Minghe Gao, Hanwang Zhang, Wei Ji, Wenqiao Zhang, Tat seng Chua, Siliang Tang, and Yueting Zhuang. Fine-tuning multimodal llms to follow zero-shot demonstrative instructions. International Conference on Learning Representations , 20235.

- Li et al. [20213] Junnan Li, Ramprasaath R. Selvaraju, Akhilesh Deepak Gotmare, Shafiq R. Joty, Caiming Xiong, and S. Hoi. Align before fuse: Vision and language representation learning with momentum distillation. Neural Information Processing Systems , 20213.

- Li et al. [20236] Junnan Li, Dongxu Li, S. Savarese, and Steven C. H. Hoi. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. International Conference on Machine Learning , 20236.

- Li et al. [20252] Kun Li, Tianhua Zhang, Yunxiang Li, Hongyin Luo, Abdalla Moustafa, Xixin Wu, James Glass, and Helen M. Meng. Generate, discriminate, evolve: Enhancing context faithfulness via fine-grained sentence-level self-evolution, arXiv preprint arXiv:2503.01695, 20252. URL https://arxiv.org/abs/2503.01695v1 .

- Li et al. [20237] Kunchang Li, Yinan He, Yi Wang, Yizhuo Li, Wen Wang, Ping Luo, Yali Wang, Limin Wang, and Yu Qiao. Videochat: Chat-centric video understanding, arXiv preprint arXiv:2305.06355v2, 20237. URL https://arxiv.org/abs/2305.06355v2 .

- Li et al. [20238] M Li, Y Zhao, B Yu, F Song, H Li, H Yu, and Z Li…. Api-bank: A comprehensive benchmark for tool-augmented llms. 20238. URL https://arxiv.org/abs/2304.08244 .

- Li et al. [20253] Michelle M. Li, Ben Y. Reis, Adam Rodman, Tianxi Cai, Noa Dagan, Ran D. Balicer, Joseph Loscalzo, Isaac S. Kohane, and M. Zitnik. One patient, many contexts: Scaling medical ai through contextual intelligence, arXiv preprint arXiv:2506.10157, 20253. URL https://arxiv.org/abs/2506.10157v1 .

- Li et al. [20247] Ming Li, Keyu Chen, Ziqian Bi, Ming Liu, Benji Peng, Qian Niu, Junyu Liu, Jinlang Wang, Sen Zhang, Xuanhe Pan, Jiawei Xu, and Pohsun Feng. Surveying the mllm landscape: A meta-review of current surveys, arXiv preprint arXiv:2409.18991, 20247. URL https://arxiv.org/abs/2409.18991v1 .

- Li et al. [20239] Minghao Li, Feifan Song, Yu Bowen, Haiyang Yu, Zhoujun Li, Fei Huang, and Yongbin Li. Api-bank: A comprehensive benchmark for tool-augmented llms. Conference on Empirical Methods in Natural Language Processing , 20239.

- Li and Xie [2025] Qiaomu Li and Ying Xie. From glue-code to protocols: A critical analysis of a2a and mcp integration for scalable agent systems, arXiv preprint arXiv:2505.03864, 2025. URL https://arxiv.org/abs/2505.03864v1 .

- Li et al. [20248] Rongsheng Li, Jin Xu, Zhixiong Cao, Hai-Tao Zheng, and Hong-Gee Kim. Extending context window in large language models with segmented base adjustment for rotary position embeddings. Applied Sciences , 20248.

- Li et al. [20254] Shuaike Li, Kai Zhang, Qi Liu, and Enhong Chen. Mindbridge: Scalable and cross-model knowledge editing via memory-augmented modality, arXiv preprint arXiv:2503.02701v1, 20254. URL https://arxiv.org/abs/2503.02701v1 .

- Li et al. [20255] Shuaiyi Li, Zhisong Zhang, Yang Deng, Chenlong Deng, Tianqing Fang, Hongming Zhang, Haitao Mi, Dong Yu, and Wai Lam. Incomes: Integrating compression and selection mechanisms into llms for efficient model editing, arXiv preprint arXiv:2505.22156, 20255. URL https://arxiv.org/abs/2505.22156v1 .

- Li et al. [20249] Siheng Li, Cheng Yang, Zesen Cheng, Lemao Liu, Mo Yu, Yujiu Yang, and Wai Lam. Large language models can self-improve in long-context reasoning, arXiv preprint arXiv:2411.08147, 20249. URL https://arxiv.org/abs/2411.08147v1 .

- Li et al. [20256] X Li, H Zou, and P Liu. Torl: Scaling tool-integrated rl. 20256. URL https://arxiv.org/abs/2503.23383 .

- Li et al. [20257] Xiaopeng Li, Pengyue Jia, Derong Xu, Yi Wen, Yingyi Zhang, Wenlin Zhang, Wanyu Wang, Yichao Wang, Zhaochen Du, Xiangyang Li, Yong Liu, Huifeng Guo, Ruiming Tang, and Xiangyu Zhao. A survey of personalization: From rag to agent, arXiv preprint arXiv:2504.10147, 20257. URL https://arxiv.org/abs/2504.10147v1 .

- Li et al. [20258] Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yutao Zhu, Yongkang Wu, Ji-Rong Wen, and Zhicheng Dou. Webthinker: Empowering large reasoning models with deep research capability, arXiv preprint arXiv:2504.21776, 20258. URL https://arxiv.org/abs/2504.21776v1 .

- Li et al. [202410] Xin Li, Qizhi Chu, Yubin Chen, Yang Liu, Yaoqi Liu, Zekai Yu, Weize Chen, Cheng Qian, Chuan Shi, and Cheng Yang. Graphteam: Facilitating large language model-based graph analysis via multi-agent collaboration, arXiv preprint arXiv:2410.18032v4, 202410. URL https://arxiv.org/abs/2410.18032v4 .

- Li et al. [202411] Xinyi Li, Sai Wang, Siqi Zeng, Yu Wu, and Yi Yang. A survey on llm-based multi-agent systems: workflow, infrastructure, and challenges. Vicinagearth , 202411.

- Li et al. [202310] Xinze Li, Zhenghao Liu, Chenyan Xiong, Shi Yu, Yu Gu, Zhiyuan Liu, and Ge Yu. Structure-aware language model pretraining improves dense retrieval on structured data. Annual Meeting of the Association for Computational Linguistics , 202310.

- Li et al. [2020] Yang Li, Jiacong He, Xiaoxia Zhou, Yuan Zhang, and Jason Baldridge. Mapping natural language instructions to mobile ui action sequences. Annual Meeting of the Association for Computational Linguistics , 2020.

- Li et al. [202412] Yinghao Li, R. Ramprasad, and Chao Zhang. A simple but effective approach to improve structured language model output for information extraction. Conference on Empirical Methods in Natural Language Processing , 202412.

- Li et al. [202311] Yuan Li, Yixuan Zhang, and Lichao Sun. Metaagents: Simulating interactions of human behaviors for llm-based task-oriented coordination via collaborative generative agents, arXiv preprint arXiv:2310.06500, 202311. URL https://arxiv.org/abs/2310.06500 .

- Li [2023] Yucheng Li. Unlocking context constraints of llms: Enhancing context efficiency of llms with self-information-based content filtering, arXiv preprint arXiv:2304.12102, 2023. URL https://arxiv.org/abs/2304.12102v1 .

- Li et al. [202312] Yucheng Li, Bo Dong, Chenghua Lin, and Frank Guerin. Compressing context to enhance inference efficiency of large language models. Conference on Empirical Methods in Natural Language Processing , 202312.

- Li et al. [20259] Zhaoxin Li, Xiaoming Zhang, Haifeng Zhang, and Chengxiang Liu. Refining interactions: Enhancing anisotropy in graph neural networks with language semantics, arXiv preprint arXiv:2504.01429, 20259. URL https://arxiv.org/abs/2504.01429v1 .

- Li et al. [202413] Zhecheng Li, Yiwei Wang, Bryan Hooi, Yujun Cai, Naifan Cheung, Nanyun Peng, and Kai-Wei Chang. Think carefully and check again! meta-generation unlocking llms for low-resource cross-lingual summarization. 202413.

- Li et al. [202414] Zhecheng Li, Yiwei Wang, Bryan Hooi, Yujun Cai, Nanyun Peng, and Kai-Wei Chang. Drs: Deep question reformulation with structured output. In Association for Computational Linguistics ACL, 2025. , 202414.

- Li et al. [202415] Zhecheng Li, Yiwei Wang, Bryan Hooi, Yujun Cai, Zhen Xiong, Nanyun Peng, and Kai-Wei Chang. Vulnerability of llms to vertically aligned text manipulations. In Association for Computational Linguistics ACL, 2025. , 202415.

- Li et al. [202510] Zhecheng Li, Guoxian Song, Yujun Cai, Zhen Xiong, Junsong Yuan, and Yiwei Wang. Texture or semantics? vision-language models get lost in font recognition. In Conference on Language Modeling COLM, 2025. , 202510.

- Li et al. [202511] Zhiyu Li, Shichao Song, Hanyu Wang, Simin Niu, Ding Chen, Jiawei Yang, Chenyang Xi, Huayi Lai, Jihao Zhao, Yezhaohui Wang, Junpeng Ren, Zehao Lin, Jiahao Huo, Tianyi Chen, Kai Chen, Ke-Rong Li, Zhiqiang Yin, Qingchen Yu, Bo Tang, Hongkang Yang, Zhiyang Xu, and Feiyu Xiong. Memos: An operating system for memory-augmented generation (mag) in large language models, arXiv preprint arXiv:2505.22101, 202511. URL https://arxiv.org/abs/2505.22101v1 .

- Li et al. [202313] Zhong-Zhi Li, Ming-Liang Zhang, Fei Yin, and Cheng-Lin Liu. Lans: A layout-aware neural solver for plane geometry problem. 202313.

- Li et al. [202416] Zhong-Zhi Li, Ming-Liang Zhang, Fei Yin, Zhi-Long Ji, Jin-Feng Bai, Zhen-Ru Pan, Fan-Hu Zeng, Jian Xu, Jia-Xin Zhang, and Cheng-Lin Liu. Cmmath: A chinese multi-modal math skill evaluation benchmark for foundation models. 202416.

- Li et al. [202512] Zhong-Zhi Li, Duzhen Zhang, Ming-Liang Zhang, Jiaxin Zhang, Zengyan Liu, Yuxuan Yao, Haotian Xu, Junhao Zheng, Pei-Jie Wang, Xiuyi Chen, et al. From system 1 to system 2: A survey of reasoning large language models. 202512.

- Li et al. [202417] Zhuoqun Li, Xuanang Chen, Haiyang Yu, Hongyu Lin, Yaojie Lu, Qiaoyu Tang, Fei Huang, Xianpei Han, Le Sun, and Yongbin Li. Structrag: Boosting knowledge intensive reasoning of llms via inference-time hybrid information structurization. International Conference on Learning Representations , 202417.

- Li et al. [202513] Zinuo Li, Xian Zhang, Yongxin Guo, Mohammed Bennamoun, F. Boussaid, Girish Dwivedi, Luqi Gong, and Qiuhong Ke. Watch and listen: Understanding audio-visual-speech moments with multimodal llm, arXiv preprint arXiv:2505.18110v2, 202513. URL https://arxiv.org/abs/2505.18110v2 .

- Li et al. [202418] Zixuan Li, Jing Xiong, Fanghua Ye, Chuanyang Zheng, Xun Wu, Jianqiao Lu, Zhongwei Wan, Xiaodan Liang, Chengming Li, Zhenan Sun, Lingpeng Kong, and Ngai Wong. Uncertaintyrag: Span-level uncertainty enhanced long-context modeling for retrieval-augmented generation, arXiv preprint arXiv:2410.02719, 202418. URL https://arxiv.org/abs/2410.02719v1 .

- Li et al. [20222] Zonglin Li, Ruiqi Guo, and Surinder Kumar. Decoupled context processing for context augmented language modeling. Neural Information Processing Systems , 20222.

- Li et al. [202419] Zongqian Li, Yinhong Liu, Yixuan Su, and Nigel Collier. Prompt compression for large language models: A survey. North American Chapter of the Association for Computational Linguistics , 202419.

- li Yu and Zhao [2023] Wen li Yu and Junfeng Zhao. Quantum multi-agent reinforcement learning as an emerging ai technology: A survey and future directions. International Conferences on Computing Advancements , 2023.

- Liang and Tong [2025] Guannan Liang and Qianqian Tong. Llm-powered ai agent systems and their applications in industry, arXiv preprint arXiv:2505.16120, 2025. URL https://arxiv.org/abs/2505.16120v1 .

- Liang et al. [2025] Jintao Liang, Gang Su, Huifeng Lin, You Wu, Rui Zhao, and Ziyue Li. Reasoning rag via system 1 or system 2: A survey on reasoning agentic retrieval-augmented generation for industry challenges, arXiv preprint arXiv:2506.10408, 2025. URL https://arxiv.org/abs/2506.10408v1 .

- Liang et al. [2023] Xinnian Liang, Bing Wang, Huijia Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, and Zhoujun Li. Scm: Enhancing large language model with self-controlled memory framework, arXiv preprint arXiv:2304.13343, 2023. URL https://arxiv.org/abs/2304.13343v4 .

- Liang et al. [2024] Xuechen Liang, Meiling Tao, Yinghui Xia, Tianyu Shi, Jun Wang, and Jingsong Yang. Self-evolving agents with reflective and memory-augmented abilities, arXiv preprint arXiv:2409.00872, 2024. URL https://arxiv.org/abs/2409.00872v2 .

- Liang et al. [20252] Xuechen Liang, Meiling Tao, Yinghui Xia, Jianhui Wang, Kun Li, Yijin Wang, Jingsong Yang, Tianyu Shi, Yuantao Wang, Miao Zhang, and Xueqian Wang. Mars: Memory-enhanced agents with reflective self-improvement, arXiv preprint arXiv:2503.19271, 20252. URL https://arxiv.org/abs/2503.19271v2 .

- Liang et al. [20253] Yanbiao Liang, Huihong Shi, Haikuo Shao, and Zhongfeng Wang. Accllm: Accelerating long-context llm inference via algorithm-hardware co-design, arXiv preprint arXiv:2505.03745, 20253. URL https://arxiv.org/abs/2505.03745v1 .

- Liang et al. [20232] Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu, Yan Xia, Yu Liu, Yangyiwen Ou, Shuai Lu, Lei Ji, Shaoguang Mao, Yun Wang, Linjun Shou, Ming Gong, and Nan Duan. Taskmatrix.ai: Completing tasks by connecting foundation models with millions of apis. Intelligent Computing , 20232.

- Liang et al. [20242] Yiming Liang, Ge Zhang, Xingwei Qu, Tianyu Zheng, Jiawei Guo, Xinrun Du, Zhenzhu Yang, Jiaheng Liu, Chenghua Lin, Lei Ma, Wenhao Huang, and Jiajun Zhang. I-sheep: Self-alignment of llm from scratch through an iterative self-enhancement paradigm. arXiv preprint, 20242.

- Liao and Vargas [2024] Bingli Liao and Danilo Vasconcellos Vargas. Beyond kv caching: Shared attention for efficient llms. Neurocomputing , 2024.

- Liao et al. [2025] Xiaoxuan Liao, Binrong Zhu, Jacky He, Guiran Liu, Hongye Zheng, and Jia Gao. A fine-tuning approach for t5 using knowledge graphs to address complex tasks, arXiv preprint arXiv:2502.16484, 2025. URL https://arxiv.org/abs/2502.16484v1 .

- Lillis [2017] David Lillis. Internalising interaction protocols as first-class programming elements in multi agent systems, arXiv preprint arXiv:1711.02634, 2017. URL https://arxiv.org/abs/1711.02634v1 .

- Lin et al. [2019] Bill Yuchen Lin, Xinyue Chen, Jamin Chen, and Xiang Ren. Kagnet: Knowledge-aware graph networks for commonsense reasoning. Conference on Empirical Methods in Natural Language Processing , 2019.

- Lin et al. [2021] Bill Yuchen Lin, Seyeon Lee, Xiaoyang Qiao, and Xiang Ren. Common sense beyond english: Evaluating and improving multilingual language models for commonsense reasoning. Annual Meeting of the Association for Computational Linguistics , 2021.

- Lin et al. [2024] Bin Lin, Chen Zhang, Tao Peng, Hanyu Zhao, Wencong Xiao, Minmin Sun, Anmin Liu, Zhipeng Zhang, Lanbo Li, Xiafei Qiu, Shen Li, Zhigang Ji, Tao Xie, Yong Li, and Wei Lin. Infinite-llm: Efficient llm service for long context with distattention and distributed kvcache, arXiv preprint arXiv:2401.02669, 2024. URL https://arxiv.org/abs/2401.02669 .

- Lin et al. [2025] Jianhao Lin, Lexuan Sun, and Yixin Yan. Simulating macroeconomic expectations using llm agents, arXiv preprint arXiv:2505.17648, 2025. URL https://arxiv.org/abs/2505.17648v2 .

- Lin et al. [2023] Lei Lin, Jiayi Fu, Pengli Liu, Qingyang Li, Yan Gong, Junchen Wan, Fuzheng Zhang, Zhongyuan Wang, Di Zhang, and Kun Gai. Just ask one more time! self-agreement improves reasoning of language models in (almost) all scenarios. Annual Meeting of the Association for Computational Linguistics , 2023.

- Lin et al. [20242] Matthieu Lin, Jenny Sheng, Andrew Zhao, Shenzhi Wang, Yang Yue, Yiran Wu, Huan Liu, Jun Liu, Gao Huang, and Yong-Jin Liu. Training of scaffolded language models with language supervision: A survey, arXiv preprint arXiv:2410.16392, 20242. URL https://arxiv.org/abs/2410.16392v2 .

- Lin et al. [20243] Qiqiang Lin, Muning Wen, Qiuying Peng, Guanyu Nie, Junwei Liao, Jun Wang, Xiaoyun Mo, Jiamu Zhou, Cheng Cheng, Yin Zhao, and Weinan Zhang. Hammer: Robust function-calling for on-device language models via function masking, arXiv preprint arXiv:2410.04587, 20243. URL https://arxiv.org/abs/2410.04587v2 .

- Lin et al. [20232] Yu-Chen Lin, Akhilesh Kumar, Norman Chang, Wen-Liang Zhang, Muhammad Zakir, Rucha Apte, Haiyang He, Chao Wang, and Jyh-Shing Roger Jang. Novel preprocessing technique for data embedding in engineering code generation using large language model. 2024 IEEE LLM Aided Design Workshop (LAD) , 20232.

- Lin et al. [20252] Yu-Hsuan Lin, Qian-Hui Chen, Yi-Jie Cheng, Jia-Ren Zhang, Yi-Hung Liu, Liang-Yu Hsia, and Yun-Nung Chen. Llm inference enhanced by external knowledge: A survey, arXiv preprint arXiv:2505.24377, 20252. URL https://arxiv.org/abs/2505.24377v1 .

- Lindsey and Litwin-Kumar [2024] Jack W Lindsey and Ashok Litwin-Kumar. Selective consolidation of learning and memory via recall-gated plasticity. bioRxiv , 2024.

- Linzen et al. [2016] Tal Linzen, Emmanuel Dupoux, and Yoav Goldberg. Assessing the ability of lstms to learn syntax-sensitive dependencies. Transactions of the Association for Computational Linguistics , 2016.

- Lior et al. [2024] Gili Lior, Yuval Shalev, Gabriel Stanovsky, and Ariel Goldstein. Computation or weight adaptation? rethinking the role of plasticity in learning. bioRxiv , 2024.

- Liu et al. [2024] Bingyang Liu, Haoyi Zhang, Xiaohan Gao, Zichen Kong, Xiyuan Tang, Yibo Lin, Runsheng Wang, and Ru Huang. Layoutcopilot: An llm-powered multi-agent collaborative framework for interactive analog layout design. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems , 2024.

- Liu et al. [2018] E. Liu, Kelvin Guu, Panupong Pasupat, Tianlin Shi, and Percy Liang. Reinforcement learning on web interfaces using workflow-guided exploration. International Conference on Learning Representations , 2018.

- Liu et al. [20242] Guang-Da Liu, Haitao Mao, Bochuan Cao, Zhiyu Xue, K. Johnson, Jiliang Tang, and Rongrong Wang. On the intrinsic self-correction capability of llms: Uncertainty and latent concept, arXiv preprint arXiv:2406.02378, 20242. URL https://arxiv.org/abs/2406.02378v2 .

- Liu et al. [20243] Guangyi Liu, Yongqi Zhang, Yong Li, and Quanming Yao. Dual reasoning: A gnn-llm collaborative framework for knowledge graph question answering, arXiv preprint arXiv:2406.01145, 20243. URL https://arxiv.org/abs/2406.01145v2 .

- Liu et al. [2025] Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Guanjing Xiong, Yong Liu, and Hongsheng Li. Llm-powered gui agents in phone automation: Surveying progress and prospects, arXiv preprint arXiv:2504.19838, 2025. URL https://arxiv.org/abs/2504.19838v2 .

- Liu et al. [20252] Hanchao Liu, Rong-Zhi Li, Weimin Xiong, Ziyu Zhou, and Wei Peng. Workteam: Constructing workflows from natural language with multi-agents. North American Chapter of the Association for Computational Linguistics , 20252.

- Liu et al. [2023] Hao Liu, Matei Zaharia, and Pieter Abbeel. Ring attention with blockwise transformers for near-infinite context. International Conference on Learning Representations , 2023.

- Liu et al. [20232] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. Neural Information Processing Systems , 20232.

- Liu et al. [20244] Jie Liu, Pan Zhou, Yingjun Du, Ah-Hwee Tan, Cees G. M. Snoek, J. Sonke, and E. Gavves. Capo: Cooperative plan optimization for efficient embodied multi-agent cooperation. International Conference on Learning Representations , 20244.

- Liu et al. [20253] Jun Liu, Ke Yu, Keliang Chen, Ke Li, Yuxinyue Qian, Xiaolian Guo, Haozhe Song, and Yinming Li. Acps: Agent collaboration protocols for the internet of agents, arXiv preprint arXiv:2505.13523, 20253. URL https://arxiv.org/abs/2505.13523v1 .

- Liu et al. [20245] Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng, Zhenpeng Chen, Lingming Zhang, and Yiling Lou. Large language model-based agents for software engineering: A survey, arXiv preprint arXiv:2409.02977, 20245. URL https://arxiv.org/abs/2409.02977v1 .

- Liu et al. [20246] Kai Liu, Zhihang Fu, Chao Chen, Wei Zhang, Rongxin Jiang, Fan Zhou, Yao-Shen Chen, Yue Wu, and Jieping Ye. Enhancing llm’s cognition via structurization. Neural Information Processing Systems , 20246.

- Liu et al. [20233] Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, and Guannan Zhang. Think-in-memory: Recalling and post-thinking enable llms with long-term memory. arXiv preprint, 20233.

- Liu et al. [20234] Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, and Guannan Zhang. Think-in-memory: Recalling and post-thinking enable llms with long-term memory, arXiv preprint arXiv:2311.08719, 20234. URL https://arxiv.org/abs/2311.08719 .

- Liu et al. [20247] Na Liu, Liangyu Chen, Xiaoyu Tian, Wei Zou, Kaijiang Chen, and Ming Cui. From llm to conversational agent: A memory enhanced architecture with fine-tuning of large language models, arXiv preprint arXiv:2401.02777, 20247. URL https://arxiv.org/abs/2401.02777v2 .

- Liu et al. [20235] Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, F. Petroni, and Percy Liang. Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics , 20235.

- Liu et al. [20254] Pei Liu, Xin Liu, Ruoyu Yao, Junming Liu, Siyuan Meng, Ding Wang, and Jun Ma. Hm-rag: Hierarchical multi-agent multimodal retrieval augmented generation. arXiv preprint, 20254.

- Liu et al. [20236] Shicheng Liu, Jialiang Xu, Wesley Tjangnaka, Sina J. Semnani, Chen Jie Yu, Gui D’avid, and Monica S. Lam. Suql: Conversational search over structured and unstructured data with large language models. NAACL-HLT , 20236.

- Liu et al. [20255] Shiyu Liu, Yucheng Han, Peng Xing, Fukun Yin, Rui Wang, Wei Cheng, Jiaqi Liao, Yingming Wang, Honghao Fu, Chunrui Han, et al. Step1x-edit: A practical framework for general image editing. 20255.

- Liu et al. [20248] W Liu, X Huang, X Zeng, X Hao, S Yu, and D Li…. Toolace: Winning the points of llm function calling. 20248. URL https://arxiv.org/abs/2409.00920 .

- Liu et al. [2019] Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Qi Ju, Haotang Deng, and Ping Wang. K-bert: Enabling language representation with knowledge graph. AAAI Conference on Artificial Intelligence , 2019.

- Liu et al. [20249] Weiwen Liu, Xu Huang, Xingshan Zeng, Xinlong Hao, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Zhengying Liu, Yuanqing Yu, Zezhong Wang, Yuxian Wang, Wu Ning, Yutai Hou, Bin Wang, Chuhan Wu, Xinzhi Wang, Yong Liu, Yasheng Wang, Duyu Tang, Dandan Tu, Lifeng Shang, Xin Jiang, Ruiming Tang, Defu Lian, Qun Liu, and Enhong Chen. Toolace: Winning the points of llm function calling, arXiv preprint arXiv:2409.00920, 20249. URL https://arxiv.org/abs/2409.00920v1 .

- Liu et al. [20256] Weiwen Liu, Jiarui Qin, Xu Huang, Xingshan Zeng, Yunjia Xi, Jianghao Lin, Chuhan Wu, Yasheng Wang, Lifeng Shang, Ruiming Tang, Defu Lian, Yong Yu, and Weinan Zhang. The real barrier to llm agent usability is agentic roi, arXiv preprint arXiv:2505.17767, 20256. URL https://arxiv.org/abs/2505.17767v1 .

- Liu et al. [20237] Wentao Liu, Hanglei Hu, Jie Zhou, Yuyang Ding, Junsong Li, Jiayi Zeng, Mengliang He, Qin Chen, Bo Jiang, Aimin Zhou, and Liang He. Mathematical language models: A survey, arXiv preprint arXiv:2312.07622, 20237. URL https://arxiv.org/abs/2312.07622v4 .

- Liu et al. [20257] Wentao Liu, Ruohua Zhang, Aimin Zhou, Feng Gao, and JiaLi Liu. Echo: A large language model with temporal episodic memory, arXiv preprint arXiv:2502.16090, 20257. URL https://arxiv.org/abs/2502.16090v1 .

- Liu et al. [2012] Xu Liu, S. Ramirez, Petti T. Pang, C. Puryear, A. Govindarajan, K. Deisseroth, and S. Tonegawa. Optogenetic stimulation of a hippocampal engram activates fear memory recall. Nature , 2012.

- Liu et al. [202410] Yang Liu, Xiaobin Tian, Zequn Sun, and Wei Hu. Finetuning generative large language models with discrimination instructions for knowledge graph completion. In International Semantic Web Conference , 202410.

- Liu et al. [20258] Yue Liu, Jiaying Wu, Yufei He, Hongcheng Gao, Hongyu Chen, Baolong Bi, Jiaheng Zhang, Zhiqi Huang, and Bryan Hooi. Efficient inference for large reasoning models: A survey, arXiv preprint arXiv:2503.23077, 20258. URL https://arxiv.org/abs/2503.23077v2 .

- Liu et al. [20238] Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, and Diyi Yang. A dynamic llm-powered agent network for task-oriented agent collaboration, arXiv preprint arXiv:2310.02170, 20238. URL https://arxiv.org/abs/2310.02170v2 .

- Liu et al. [20259] Zijun Liu, Zhennan Wan, Peng Li, Ming Yan, Ji Zhang, Fei Huang, and Yang Liu. Scaling external knowledge input beyond context windows of llms via multi-agent collaboration, arXiv preprint arXiv:2505.21471, 20259. URL https://arxiv.org/abs/2505.21471v1 .

- Liu et al. [202510] Zinan Liu, Haoran Li, Jingyi Lu, Gaoyuan Ma, Xu Hong, Giovanni Iacca, Arvind Kumar, Shaojun Tang, and Lin Wang. Nature’s insight: A novel framework and comprehensive analysis of agentic reasoning through the lens of neuroscience. arXiv preprint, 202510.

- Liu et al. [202411] Zuxin Liu, Thai Hoang, Jianguo Zhang, Ming Zhu, Tian Lan, Shirley Kokane, Juntao Tan, Weiran Yao, Zhiwei Liu, Yihao Feng, Rithesh Murthy, Liangwei Yang, Silvio Savarese, Juan Carlos Niebles, Huan Wang, Shelby Heinecke, and Caiming Xiong. Apigen: Automated pipeline for generating verifiable and diverse function-calling datasets. Neural Information Processing Systems , 202411.

- Lo [2023] Leo S. Lo. The art and science of prompt engineering: A new literacy in the information age. Internet Reference Services Quarterly , 2023.

- Loffredo and Yun [2025] Joseph R. Loffredo and Suyeol Yun. Agent-enhanced large language models for researching political institutions, arXiv preprint arXiv:2503.13524, 2025. URL https://arxiv.org/abs/2503.13524v1 .

- Lu et al. [2023] Jianqiao Lu, Wanjun Zhong, Wenyong Huang, Yufei Wang, Fei Mi, Baojun Wang, Weichao Wang, Lifeng Shang, and Qun Liu. Self: Self-evolution with language feedback, arXiv preprint arXiv:2310.00533, 2023. URL https://arxiv.org/abs/2310.00533v4 .

- Lu et al. [20232] Junru Lu, Siyu An, Mingbao Lin, Gabriele Pergola, Yulan He, Di Yin, Xing Sun, and Yunsheng Wu. Memochat: Tuning llms to use memos for consistent long-range open-domain conversation, arXiv preprint arXiv:2308.08239, 20232. URL https://arxiv.org/abs/2308.08239 .

- Lu et al. [2025] Junting Lu, Zhiyang Zhang, Fangkai Yang, Jue Zhang, Lu Wang, Chao Du, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, and Qi Zhang. Axis: Efficient human-agent-computer interaction with api-first llm-based agents, arXiv preprint arXiv:2409.17140, 2025. URL https://arxiv.org/abs/2409.17140 .

- Lu et al. [2024] Keer Lu, Xiaonan Nie, Zheng Liang, Da Pan, Shusen Zhang, Keshi Zhao, Weipeng Chen, Zenan Zhou, Guosheng Dong, Bin Cui, and Wentao Zhang. Datasculpt: Crafting data landscapes for long-context llms through multi-objective partitioning, arXiv preprint arXiv:2409.00997, 2024. URL https://arxiv.org/abs/2409.00997v2 .

- Lu et al. [2021] Liqiang Lu, Yicheng Jin, Hangrui Bi, Zizhang Luo, Peng Li, Tao Wang, and Yun Liang. Sanger: A co-design framework for enabling sparse attention using reconfigurable architecture. Micro , 2021.

- Lu et al. [20233] Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Y. Wu, Song-Chun Zhu, and Jianfeng Gao. Chameleon: Plug-and-play compositional reasoning with large language models. Neural Information Processing Systems , 20233.

- Lu et al. [20234] Y Lu, H Yu, and D Khashabi. Gear: Augmenting language models with generalizable and efficient tool resolution. 20234. URL https://arxiv.org/abs/2307.08775 .

- Lu et al. [20212] Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp. Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity. Annual Meeting of the Association for Computational Linguistics , 20212.

- Lu et al. [20213] Yinquan Lu, H. Lu, Guirong Fu, and Qun Liu. Kelm: Knowledge enhanced pre-trained language representations with message passing on hierarchical relational graphs, arXiv preprint arXiv:2109.04223, 20213. URL https://arxiv.org/abs/2109.04223v2 .

- Lumer et al. [2025] Elias Lumer, Anmol Gulati, V. K. Subbiah, Pradeep Honaganahalli Basavaraju, and James A. Burke. Scalemcp: Dynamic and auto-synchronizing model context protocol tools for llm agents, arXiv preprint arXiv:2505.06416, 2025. URL https://arxiv.org/abs/2505.06416v1 .

- Luo et al. [2024] Cheng Luo, Jiawei Zhao, Zhuoming Chen, Beidi Chen, and Anima Anandkumar. Mini-sequence transformer: Optimizing intermediate memory for long sequences training, arXiv preprint arXiv:2407.15892, 2024. URL https://arxiv.org/abs/2407.15892v4 .

- Luo et al. [2025] Feng Luo, Yu-Neng Chuang, Guanchu Wang, Hoang Anh Duy Le, Shaochen Zhong, Hongyi Liu, Jiayi Yuan, Yang Sui, Vladimir Braverman, Vipin Chaudhary, and Xia Hu. Autol2s: Auto long-short reasoning for efficient large language models, arXiv preprint arXiv:2505.22662, 2025. URL https://arxiv.org/abs/2505.22662v1 .

- Luo et al. [20242] Haitong Luo, Xuying Meng, Suhang Wang, Tianxiang Zhao, Fali Wang, Hanyun Cao, and Yujun Zhang. Enhance graph alignment for large language models, arXiv preprint arXiv:2410.11370v1, 20242. URL https://arxiv.org/abs/2410.11370v1 .

- Luo et al. [20252] Haoran Luo, E. Haihong, Guanting Chen, Yandan Zheng, Xiaobao Wu, Yikai Guo, Qika Lin, Yu Feng, Zemin Kuang, Meina Song, Yifan Zhu, and Anh Tuan Luu. Hypergraphrag: Retrieval-augmented generation with hypergraph-structured knowledge representation. arXiv preprint, 20252.

- Luo et al. [20253] Haotian Luo, Li Shen, Haiying He, Yibo Wang, Shiwei Liu, Wei Li, Naiqiang Tan, Xiaochun Cao, and Dacheng Tao. O1-pruner: Length-harmonizing fine-tuning for o1-like reasoning pruning. arXiv preprint, 20253.

- Luo et al. [20254] Junyu Luo, Weizhi Zhang, Ye Yuan, Yusheng Zhao, Junwei Yang, Yiyang Gu, Bohan Wu, Binqi Chen, Ziyue Qiao, Qingqing Long, Rongcheng Tu, Xiaoming Luo, Wei Ju, Zhiping Xiao, Yifan Wang, Mengxue Xiao, Chenwu Liu, Jingyang Yuan, Shichang Zhang, Yiqiao Jin, Fan Zhang, Xianhong Wu, Hanqing Zhao, Dacheng Tao, Philip S. Yu, and Ming Zhang. Large language model agent: A survey on methodology, applications and challenges, arXiv preprint arXiv:2503.21460, 20254. URL https://arxiv.org/abs/2503.21460v1 .

- Luo et al. [2023] Linhao Luo, Yuan-Fang Li, Gholamreza Haffari, and Shirui Pan. Reasoning on graphs: Faithful and interpretable large language model reasoning. International Conference on Learning Representations , 2023.

- Luo et al. [20255] Renjie Luo, Jiaxi Li, Chen Huang, and Wei Lu. Through the valley: Path to effective long cot training for small language models, arXiv preprint arXiv:2506.07712, 20255. URL https://arxiv.org/abs/2506.07712v1 .

- Luo et al. [20243] Xindi Luo, Zequn Sun, Jing Zhao, Zhe Zhao, and Wei Hu. Knowla: Enhancing parameter-efficient finetuning with knowledgeable adaptation. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics , 20243.

- Luo et al. [20232] Yifan Luo, Yiming Tang, Chengfeng Shen, Zhennan Zhou, and Bin Dong. Prompt engineering through the lens of optimal control. Journal of Machine Learning , 20232.

- Lymperopoulos and Sarathy [2025] Panagiotis Lymperopoulos and Vasanth Sarathy. Tools in the loop: Quantifying uncertainty of llm question answering systems that use tools, arXiv preprint arXiv:2505.16113, 2025. URL https://arxiv.org/abs/2505.16113v1 .

- Lyu et al. [2025] Yougang Lyu, Xiaoyu Zhang, Lingyong Yan, M. D. Rijke, Zhaochun Ren, and Xiuying Chen. Deepshop: A benchmark for deep research shopping agents, arXiv preprint arXiv:2506.02839, 2025. URL https://arxiv.org/abs/2506.02839v1 .

- Ma [2024] Jianxiang Ma. Research on the role of llm in multi-agent systems: A survey. Applied and Computational Engineering , 2024.

- Ma et al. [2024] Jie Ma, Zhitao Gao, Qianyi Chai, Wangchun Sun, Pinghui Wang, Hongbin Pei, Jing Tao, Lingyun Song, Jun Liu, Chen Zhang, and Li zhen Cui. Debate on graph: a flexible and reliable reasoning framework for large language models, arXiv preprint arXiv:2409.03155, 2024. URL https://arxiv.org/abs/2409.03155v1 .

- Ma et al. [20242] Qun Ma, Xiao Xue, Deyu Zhou, Xiangning Yu, Donghua Liu, Xuwen Zhang, Zihan Zhao, Yifan Shen, Peilin Ji, Juanjuan Li, Gang Wang, and Wanpeng Ma. Computational experiments meet large language model based agents: A survey and perspective, arXiv preprint arXiv:2402.00262, 20242. URL https://arxiv.org/abs/2402.00262v1 .

- Ma et al. [20243] Xin Ma, Yang Liu, Jingjing Liu, and Xiaoxu Ma. Mesa-extrapolation: A weave position encoding method for enhanced extrapolation in llms. Neural Information Processing Systems , 20243.

- Ma et al. [2023] Xinbei Ma, Yeyun Gong, Pengcheng He, Hai Zhao, and Nan Duan. Query rewriting for retrieval-augmented large language models, arXiv preprint arXiv:2305.14283, 2023. URL https://arxiv.org/abs/2305.14283v3 .

- Ma et al. [20244] Xuezhe Ma, Xiaomeng Yang, Wenhan Xiong, Beidi Chen, Lili Yu, Hao Zhang, Jonathan May, Luke S. Zettlemoyer, Omer Levy, and Chunting Zhou. Megalodon: Efficient llm pretraining and inference with unlimited context length. Neural Information Processing Systems , 20244.

- Ma et al. [20245] Y Ma, Z Gou, J Hao, R Xu, S Wang, and L Pan…. Sciagent: Tool-augmented language models for scientific reasoning. 20245. URL https://arxiv.org/abs/2402.11451 .

- Ma et al. [2025] Zhiyuan Ma, Zhenya Huang, Jiayu Liu, Minmao Wang, Hongke Zhao, and Xin Li. Automated creation of reusable and diverse toolsets for enhancing llm reasoning. AAAI Conference on Artificial Intelligence , 2025.

- Madaan et al. [2022] Aman Madaan, Niket Tandon, Peter Clark, and Yiming Yang. Memory-assisted prompt editing to improve gpt-3 after deployment. Conference on Empirical Methods in Natural Language Processing , 2022.

- Madaan et al. [2023] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, S. Welleck, Bodhisattwa Prasad Majumder, Shashank Gupta, A. Yazdanbakhsh, and Peter Clark. Self-refine: Iterative refinement with self-feedback. Neural Information Processing Systems , 2023.

- Mai et al. [2025] Xinji Mai, Haotian Xu, W. Xing, Weinong Wang, Yingying Zhang, and Wenqiang Zhang. Agent rl scaling law: Agent rl with spontaneous code execution for mathematical problem solving, arXiv preprint arXiv:2505.07773, 2025. URL https://arxiv.org/abs/2505.07773v2 .

- Majid et al. [2021] Amjad Yousef Majid, Serge Saaybi, Tomas van Rietbergen, Vincent François-Lavet, R. V. Prasad, and Chris Verhoeven. Deep reinforcement learning versus evolution strategies: A comparative survey. IEEE Transactions on Neural Networks and Learning Systems , 2021.

- Maldonado et al. [2024] D. Maldonado, Edison Cruz, Jackeline Abad Torres, P. Cruz, and Silvana del Pilar Gamboa Benitez. Multi-agent systems: A survey about its components, framework and workflow. IEEE Access , 2024.

- Mandi et al. [2023] Zhao Mandi, Shreeya Jain, and Shuran Song. Roco: Dialectic multi-robot collaboration with large language models. IEEE International Conference on Robotics and Automation , 2023.

- Manning et al. [2011] Jeremy R. Manning, Sean M. Polyn, G. Baltuch, B. Litt, and M. Kahana. Oscillatory patterns in temporal lobe reveal context reinstatement during memory search. Proceedings of the National Academy of Sciences of the United States of America , 2011.

- Mao et al. [2024] Qiheng Mao, Zemin Liu, Chenghao Liu, Zhuo Li, and Jianling Sun. Advancing graph representation learning with large language models: A comprehensive survey of techniques, arXiv preprint arXiv:2402.05952v1, 2024. URL https://arxiv.org/abs/2402.05952v1 .

- Marani et al. [2024] Amin Hosseiny Marani, Ulie Schnaithmann, Youngseo Son, Akil Iyer, Manas Paldhe, and Arushi Raghuvanshi. Graph integrated language transformers for next action prediction in complex phone calls. North American Chapter of the Association for Computational Linguistics , 2024.

- Maria [2025] Sophia Maria. Compass-v2 technical report, arXiv preprint arXiv:2504.15527, 2025. URL https://arxiv.org/abs/2504.15527v1 .

- Marian and Neisser [2000] Viorica Marian and U. Neisser. Language-dependent recall of autobiographical memories. Journal of experimental psychology. General , 2000.

- Mariani and Omicini [2019] S. Mariani and Andrea Omicini. Special issue “multi-agent systems”: Editorial. Applied Sciences , 2019.

- Markovic et al. [2025] Vasilije Markovic, Lazar Obradović, L’aszl’o Hajdu, and Jovan Pavlović. Optimizing the interface between knowledge graphs and llms for complex reasoning, arXiv preprint arXiv:2505.24478, 2025. URL https://arxiv.org/abs/2505.24478v1 .

- Marreed et al. [2025] Sami Marreed, Alon Oved, Avi Yaeli, Segev Shlomov, Ido Levy, Offer Akrabi, Aviad Sela, Asaf Adi, and Nir Mashkif. Towards enterprise-ready computer using generalist agent. 2025.

- Masterman et al. [2024] Tula Masterman, Sandi Besen, Mason Sawtell, and Alex Chao. The landscape of emerging ai agent architectures for reasoning, planning, and tool calling: A survey, arXiv preprint arXiv:2404.11584, 2024. URL https://arxiv.org/abs/2404.11584v1 .

- Matsumoto et al. [2024] Nicholas Matsumoto, Jay Moran, Hyunjun Choi, Miguel E. Hernandez, Mythreye Venkatesan, Paul Wang, and Jason H. Moore. Kragen: a knowledge graph-enhanced rag framework for biomedical problem solving using large language models. Bioinformatics , 2024.

- Matsuo et al. [2024] Ryoga Matsuo, Stefan Uhlich, Arun Venkitaraman, Andrea Bonetti, Chia-Yu Hsieh, Ali Momeni, Lukas Mauch, Augusto Capone, Eisaku Ohbuchi, and Lorenzo Servadei. Schemato - an llm for netlist-to-schematic conversion. arXiv preprint, 2024.

- Mavromatis et al. [2023] Costas Mavromatis, V. Ioannidis, Shen Wang, Da Zheng, Soji Adeshina, Jun Ma, Han Zhao, C. Faloutsos, and G. Karypis. Train your own gnn teacher: Graph-aware distillation on textual graphs. ECML/PKDD , 2023.

- McClelland et al. [1995] James L. McClelland, B. McNaughton, and R. O’Reilly. Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychology Review , 1995.

- McCoy et al. [2019] R. Thomas McCoy, Ellie Pavlick, and Tal Linzen. Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. Annual Meeting of the Association for Computational Linguistics , 2019.

- McDuff et al. [2023] Daniel McDuff, M. Schaekermann, Tao Tu, Anil Palepu, Amy Wang, Jake Garrison, Karan Singhal, Yash Sharma, Shekoofeh Azizi, Kavita Kulkarni, Le Hou, Yong Cheng, Yun Liu, S. Mahdavi, Sushant Prakash, Anupam Pathak, Christopher Semturs, Shwetak N. Patel, D. Webster, Ewa Dominowska, Juraj Gottweis, Joelle Barral, Katherine Chou, G. Corrado, Yossi Matias, Jacob Sunshine, A. Karthikesalingam, and Vivek Natarajan. Towards accurate differential diagnosis with large language models. Nature , 2023.

- [755] AD McNaughton, G Ramalaxmi, A Kruel, and CR Knutson…. Cactus: Chemistry agent connecting tool-usage to science, arxiv, 2024.

- Mehta et al. [2025] Sushant Mehta, R. Dandekar, R. Dandekar, and S. Panat. Latent multi-head attention for small language models, arXiv preprint arXiv:2506.09342, 2025. URL https://arxiv.org/abs/2506.09342v2 .

- Mei et al. [2024] Kai Mei, Zelong Li, Shuyuan Xu, Ruosong Ye, Yingqiang Ge, and Yongfeng Zhang. Aios: Llm agent operating system, arXiv preprint arXiv:2403.16971, 2024. URL https://arxiv.org/abs/2403.16971v4 .

- Mei et al. [20242] Lingrui Mei, Shenghua Liu, Yiwei Wang, Baolong Bi, and Xueqi Cheng. Slang: New concept comprehension of large language models. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing , page 12558–12575. Association for Computational Linguistics, 20242. 10.18653/v1/2024.emnlp-main.698 . URL http://dx.doi.org/10.18653/v1/2024.emnlp-main.698 .

- Mei et al. [20243] Lingrui Mei, Shenghua Liu, Yiwei Wang, Baolong Bi, Ruibin Yuan, and Xueqi Cheng. Hiddenguard: Fine-grained safe generation with specialized representation router, arXiv preprint arXiv:2410.02684, 20243. URL https://arxiv.org/abs/2410.02684 .

- Mei et al. [2025] Lingrui Mei, Shenghua Liu, Yiwei Wang, Baolong Bi, Yuyao Ge, Jun Wan, Yurong Wu, and Xueqi Cheng. a1: Steep test-time scaling law via environment augmented generation, arXiv preprint arXiv:2504.14597, 2025. URL https://arxiv.org/abs/2504.14597 .

- Mei et al. [20252] Lingrui Mei, Shenghua Liu, Yiwei Wang, Baolong Bi, Jiayi Mao, and Xueqi Cheng. "not aligned" is not "malicious": Being careful about hallucinations of large language models’ jailbreak, arXiv preprint arXiv:2406.11668, 20252. URL https://arxiv.org/abs/2406.11668 .

- Meiser and Bröder [2002] T. Meiser and A. Bröder. Memory for multidimensional source information. Journal of Experimental Psychology. Learning, Memory and Cognition , 2002.

- Melis et al. [2017] Gábor Melis, Chris Dyer, and Phil Blunsom. On the state of the art of evaluation in neural language models. International Conference on Learning Representations , 2017.

- Meng et al. [2022] Kevin Meng, David Bau, A. Andonian, and Yonatan Belinkov. Locating and editing factual associations in gpt. Neural Information Processing Systems , 2022.

- Meng et al. [2021] Yuxian Meng, Shi Zong, Xiaoya Li, Xiaofei Sun, Tianwei Zhang, Fei Wu, and Jiwei Li. Gnn-lm: Language modeling based on global contexts via gnn. International Conference on Learning Representations , 2021.

- Mensfelt et al. [2024] Agnieszka Mensfelt, Kostas Stathis, and Vince Trencsenyi. Towards logically sound natural language reasoning with logic-enhanced language model agents, arXiv preprint arXiv:2408.16081, 2024. URL https://arxiv.org/abs/2408.16081v2 .

- Mensink and Raaijmakers [1988] G. M. Mensink and J. Raaijmakers. A model for interference and forgetting. arXiv preprint, 1988.

- Merth et al. [2024] Thomas Merth, Qichen Fu, Mohammad Rastegari, and Mahyar Najibi. Superposition prompting: Improving and accelerating retrieval-augmented generation. International Conference on Machine Learning , 2024.

- Meskó [2023] B. Meskó. Prompt engineering as an important emerging skill for medical professionals: Tutorial. Journal of Medical Internet Research , 2023.

- Mi et al. [2025] Yapeng Mi, Zhi Gao, Xiaojian Ma, and Qing Li. Building llm agents by incorporating insights from computer systems, arXiv preprint arXiv:2504.04485, 2025. URL https://arxiv.org/abs/2504.04485v1 .

- Mialon et al. [2023] G. Mialon, Roberto Dessì, M. Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, R. Raileanu, Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu, Asli Celikyilmaz, Edouard Grave, Yann LeCun, and Thomas Scialom. Augmented language models: a survey. Trans. Mach. Learn. Res. , 2023.

- Mialon et al. [20232] G. Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. Gaia: a benchmark for general ai assistants, arXiv preprint arXiv:2311.12983, 20232. URL https://arxiv.org/abs/2311.12983v1 .

- Miao et al. [2023] Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Xinhao Cheng, Hongyi Jin, Tianqi Chen, and Zhihao Jia. Towards efficient generative large language model serving: A survey from algorithms to systems, arXiv preprint arXiv:2312.15234, 2023. URL https://arxiv.org/abs/2312.15234v1 .

- Miller et al. [2020] Jacob Miller, Guillaume Rabusseau, and John Terilla. Tensor networks for language modeling. arXiv preprint, 2020.

- ming Guo et al. [2024] Xing ming Guo, Darioush Keivan, U. Syed, Lianhui Qin, Huan Zhang, G. Dullerud, Peter J. Seiler, and Bin Hu. Controlagent: Automating control system design via novel integration of llm agents and domain expertise, arXiv preprint arXiv:2410.19811, 2024. URL https://arxiv.org/abs/2410.19811v1 .

- Mirjalili et al. [2021] Soroush Mirjalili, Patrick S. Powell, Jonathan Strunk, Taylor A James, and Audrey Duarte. Context memory encoding and retrieval temporal dynamics are modulated by attention across the adult lifespan. eNeuro , 2021.

- Misra and Maaten [2019] Ishan Misra and L. Maaten. Self-supervised learning of pretext-invariant representations. Computer Vision and Pattern Recognition , 2019.

- Modarressi et al. [2024] Ali Modarressi, Ayyoob Imani, Mohsen Fayyaz, and Hinrich Schütze. Ret-llm: Towards a general read-write memory for large language models, arXiv preprint arXiv:2305.14322, 2024. URL https://arxiv.org/abs/2305.14322 .

- Modarressi et al. [20242] Ali Modarressi, Abdullatif Köksal, Ayyoob Imani, Mohsen Fayyaz, and Hinrich Schutze. Memllm: Finetuning llms to use an explicit read-write memory. Trans. Mach. Learn. Res. , 20242.

- Mohammadi [2025] Behnam Mohammadi. Pel, a programming language for orchestrating ai agents, arXiv preprint arXiv:2505.13453, 2025. URL https://arxiv.org/abs/2505.13453v2 .

- Mohtashami and Jaggi [2023] Amirkeivan Mohtashami and Martin Jaggi. Landmark attention: Random-access infinite context length for transformers. Neural Information Processing Systems , 2023.

- Moiseev et al. [2022] Fedor Moiseev, Zhe Dong, Enrique Alfonseca, and Martin Jaggi. Skill: Structured knowledge infusion for large language models. North American Chapter of the Association for Computational Linguistics , 2022.

- Mollo and Milliere [2023] Dimitri Coelho Mollo and Raphael Milliere. The vector grounding problem, arXiv preprint arXiv:2304.01481, 2023. URL https://arxiv.org/abs/2304.01481v2 .

- Montes et al. [2022] Nieves Montes, N. Osman, and C. Sierra. Combining theory of mind and abduction for cooperation under imperfect information. European Workshop on Multi-Agent Systems , 2022.

- Moon et al. [2024] Suhong Moon, Siddharth Jha, Lutfi Eren Erdogan, Sehoon Kim, Woosang Lim, Kurt Keutzer, and A. Gholami. Efficient and scalable estimation of tool representations in vector space, arXiv preprint arXiv:2409.02141, 2024. URL https://arxiv.org/abs/2409.02141v1 .

- Mori [2002] Shinsuke Mori. A stochastic parser based on an slm with arboreal context trees. International Conference on Computational Linguistics , 2002.

- Morris [2024] Meredith Ringel Morris. Prompting considered harmful. Communications of the ACM , 2024.

- Mosbach et al. [2023] Marius Mosbach, Tiago Pimentel, Shauli Ravfogel, D. Klakow, and Yanai Elazar. Few-shot fine-tuning vs. in-context learning: A fair comparison and evaluation. Annual Meeting of the Association for Computational Linguistics , 2023.

- Mousavi et al. [2023] Sajad Mousavi, Ricardo Luna Guti’errez, Desik Rengarajan, Vineet Gundecha, Ashwin Ramesh Babu, Avisek Naug, Antonio Guillen-Perez, and S. Sarkar. N-critics: Self-refinement of large language models with ensemble of critics. arXiv preprint, 2023.

- Mukherjee et al. [2025] Manisha Mukherjee, Sungchul Kim, Xiang Chen, Dan Luo, Tong Yu, and Tung Mai. From documents to dialogue: Building kg-rag enhanced ai assistants, arXiv preprint arXiv:2502.15237, 2025. URL https://arxiv.org/abs/2502.15237v1 .

- Munkhbat et al. [2025] Tergel Munkhbat, Namgyu Ho, Seohyun Kim, Yongjin Yang, Yujin Kim, and Se young Yun. Self-training elicits concise reasoning in large language models, arXiv preprint arXiv:2502.20122, 2025. URL https://arxiv.org/abs/2502.20122v3 .

- Munkhdalai et al. [2024] Tsendsuren Munkhdalai, Manaal Faruqui, and Siddharth Gopal. Leave no context behind: Efficient infinite context transformers with infini-attention, arXiv preprint arXiv:2404.07143, 2024. URL https://arxiv.org/abs/2404.07143v2 .

- Nachmani et al. [2023] Eliya Nachmani, Alon Levkovitch, Julián Salazar, Chulayutsh Asawaroengchai, Soroosh Mariooryad, R. Skerry-Ryan, and Michelle Tadmor Ramanovich. Spoken question answering and speech continuation using spectrogram-powered llm. International Conference on Learning Representations , 2023.

- Nadel et al. [2002] L. Nadel, Jessica D. Payne, and W. J. Jacobs. The relationship between episodic memory and context: clues from memory errors made while under stress. Physiological Research , 2002.

- Nakano et al. [2022] Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, and John Schulman. Webgpt: Browser-assisted question-answering with human feedback, arXiv preprint arXiv:2112.09332, 2022. URL https://arxiv.org/abs/2112.09332 .

- Namekata et al. [2024] Koichi Namekata, Amirmojtaba Sabour, Sanja Fidler, and Seung Wook Kim. Emerdiff: Emerging pixel-level semantic knowledge in diffusion models, arXiv preprint arXiv:2401.11739, 2024. URL https://arxiv.org/abs/2401.11739 .

- Narayanan and Vishwakarma [2024] Sundaraparipurnan Narayanan and Sandeep Vishwakarma. Guard-d-llm: An llm-based risk assessment engine for the downstream uses of llms. arXiv preprint, 2024.

- Naseem et al. [2023] Usman Naseem, Surendrabikram Thapa, Qi Zhang, Liang Hu, Anum Masood, and Mehwish Nasim. Reducing knowledge noise for improved semantic analysis in biomedical natural language processing applications. Clinical Natural Language Processing Workshop , 2023.

- Nathani et al. [2023] Deepak Nathani, David Wang, Liangming Pan, and W. Wang. Maf: Multi-aspect feedback for improving reasoning in large language models. Conference on Empirical Methods in Natural Language Processing , 2023.

- Nema et al. [2025] Aashutosh Nema, Samaksh Gulati, Evangelos Giakoumakis, and Bipana Thapaliya. Modp: Multi objective directional prompting, arXiv preprint arXiv:2504.18722, 2025. URL https://arxiv.org/abs/2504.18722v1 .

- Newman et al. [2019] Christian D. Newman, Anthony S Peruma, and Reem S. Alsuhaibani. Modeling the relationship between identifier name and behavior. IEEE International Conference on Software Maintenance and Evolution , 2019.

- Nieznański et al. [2015] M. Nieznański, Michał Obidziński, Emilia Zyskowska, and Daria Niedziałkowska. Executive resources and item-context binding: Exploring the influence of concurrent inhibition, updating, and shifting tasks on context memory. Advances in Cognitive Psychology , 2015.

- Nieznański et al. [2023] M. Nieznański, Michał Obidziński, and Daria Ford. Does context recollection depend on the base-rate of contextual features? Cognitive Processing , 2023.

- Nourani and Eklund [2017] C. Nourani and P. Eklund. Concepts ontology algebras and role descriptions. Conference on Computer Science and Information Systems , 2017.

- Ocker et al. [2024] Felix Ocker, Daniel Tanneberg, Julian Eggert, and Michael Gienger. Tulip agent - enabling llm-based agents to solve tasks using large tool libraries. arXiv preprint, 2024.

- Ocker et al. [2025] Felix Ocker, J. Deigmöller, Pavel Smirnov, and Julian Eggert. A grounded memory system for smart personal assistants, arXiv preprint arXiv:2505.06328, 2025. URL https://arxiv.org/abs/2505.06328v1 .

- OpenAI [2025] OpenAI. Computer-using agent, 2025. URL https://openai.com/index/computer-using-agent/ . OpenAI Technical Report.

- OpenAI [2025] OpenAI. Swarm: Educational framework exploring ergonomic, lightweight multi-agent orchestration. https://github.com/openai/swarm , 2025. [Online; accessed 17-July-2025].

- Oppenlaender [2025] Jonas Oppenlaender. Dangermaps: Personalized safety advice for travel in urban environments using a retrieval-augmented language model, arXiv preprint arXiv:2503.14103, 2025. URL https://arxiv.org/abs/2503.14103v3 .

- Orhan [2023] A. Orhan. Recognition, recall, and retention of few-shot memories in large language models, arXiv preprint arXiv:2303.17557, 2023. URL https://arxiv.org/abs/2303.17557v1 .

- Ortiz-Hernández et al. [2022] Gustavo Ortiz-Hernández, Alejandro Guerra-Hernández, J. Hübner, and W. A. Luna-Ramírez. Modularization in belief-desire-intention agent programming and artifact-based environments. PeerJ Computer Science , 2022.

- Ouédraogo et al. [2024] Wendkûuni C. Ouédraogo, A. Kaboré, Haoye Tian, Yewei Song, Anil Koyuncu, Jacques Klein, David Lo, and Tegawend’e F. Bissyand’e. Large-scale, independent and comprehensive study of the power of llms for test case generation. arXiv preprint, 2024.

- Packer et al. [2023] Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, and Joseph Gonzalez. Memgpt: Towards llms as operating systems, arXiv preprint arXiv:2310.08560, 2023. URL https://arxiv.org/abs/2310.08560v2 .

- Packer et al. [2024] Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and Joseph E. Gonzalez. Memgpt: Towards llms as operating systems, arXiv preprint arXiv:2310.08560, 2024. URL https://arxiv.org/abs/2310.08560 .

- Pal et al. [2020] Constantin-Valentin Pal, F. Leon, M. Paprzycki, and M. Ganzha. A review of platforms for the development of agent systems. Inf. , 2020.

- Pan et al. [2025] Qianjun Pan, Wenkai Ji, Yuyang Ding, Junsong Li, Shilian Chen, Junyi Wang, Jie Zhou, Qin Chen, Min Zhang, Yulan Wu, and Liang He. A survey of slow thinking-based reasoning llms using reinforced learning and inference-time scaling law, arXiv preprint arXiv:2505.02665, 2025. URL https://arxiv.org/abs/2505.02665v2 .

- Pan et al. [2023] Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, and Xindong Wu. Unifying large language models and knowledge graphs: A roadmap. IEEE Transactions on Knowledge and Data Engineering , 2023.

- Pan et al. [20252] Xu Pan, Ely Hahami, Zechen Zhang, and H. Sompolinsky. Memorization and knowledge injection in gated llms, arXiv preprint arXiv:2504.21239, 20252. URL https://arxiv.org/abs/2504.21239v1 .

- Pang et al. [2025] Bo Pang, Hanze Dong, Jiacheng Xu, Silvio Savarese, Yingbo Zhou, and Caiming Xiong. Bolt: Bootstrap long chain-of-thought in language models without distillation, arXiv preprint arXiv:2502.03860, 2025. URL https://arxiv.org/abs/2502.03860v1 .

- Pang et al. [2024] Jianhui Pang, Fanghua Ye, Derek F. Wong, and Longyue Wang. Anchor-based large language models. Annual Meeting of the Association for Computational Linguistics , 2024.

- Paranjape et al. [2023] Bhargavi Paranjape, Scott M. Lundberg, Sameer Singh, Hannaneh Hajishirzi, Luke Zettlemoyer, and Marco Tulio Ribeiro. Art: Automatic multi-step reasoning and tool-use for large language models, arXiv preprint arXiv:2303.09014, 2023. URL https://arxiv.org/abs/2303.09014v1 .

- Parisi et al. [2022] A Parisi, Y Zhao, and N Fiedel. Talm: Tool augmented language models. 2022. URL https://arxiv.org/abs/2205.12255 .

- Park and Ahn [2019] Dongju Park and Chang Wook Ahn. Self-supervised contextual data augmentation for natural language processing. Symmetry , 2019.

- Park et al. [2022] J. Park, Lindsay Popowski, Carrie J. Cai, M. Morris, Percy Liang, and Michael S. Bernstein. Social simulacra: Creating populated prototypes for social computing systems. ACM Symposium on User Interface Software and Technology , 2022.

- Park et al. [2023] J. Park, Joseph C. O’Brien, Carrie J. Cai, M. Morris, Percy Liang, and Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. ACM Symposium on User Interface Software and Technology , 2023.

- Park et al. [2025] Soya Park, J. Zamfirescu-Pereira, and Chinmay Kulkarni. Model behavior specification by leveraging llm self-playing and self-improving, arXiv preprint arXiv:2503.03967, 2025. URL https://arxiv.org/abs/2503.03967v1 .

- Patil and Gudivada [2024] Rajvardhan Patil and Venkat Gudivada. A review of current trends, techniques, and challenges in large language models (llms). Applied Sciences , 2024.

- Patil et al. [2023] Shishir G. Patil, Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez. Gorilla: Large language model connected with massive apis, arXiv preprint arXiv:2305.15334, 2023. URL https://arxiv.org/abs/2305.15334 .

- Patil et al. [2025] Shishir G. Patil, Huanzhi Mao, Charlie Cheng-Jie Ji, Fanjia Yan, Vishnu Suresh, Ion Stoica, and Joseph E. Gonzalez. The berkeley function calling leaderboard (bfcl): From tool use to agentic evaluation of large language models. In Forty-second International Conference on Machine Learning , 2025.

- Paul et al. [2025] Shuva Paul, Farhad Alemi, and Richard Macwan. Llm-assisted proactive threat intelligence for automated reasoning, arXiv preprint arXiv:2504.00428, 2025. URL https://arxiv.org/abs/2504.00428v1 .

- Pawar et al. [2024] Saurav Pawar, S. Tonmoy, S. M. M. Zaman, Vinija Jain, Aman Chadha, and Amitava Das. The what, why, and how of context length extension techniques in large language models - a detailed survey. arXiv preprint, 2024.

- Peng et al. [2024] Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang, and Siliang Tang. Graph retrieval-augmented generation: A survey. ArXiv , abs/2408.08921, 2024. URL https://api.semanticscholar.org/CorpusID:271903170 .

- Peng et al. [2023] Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models. International Conference on Learning Representations , 2023.

- Peng et al. [2020] Hao Peng, Tianyu Gao, Xu Han, Yankai Lin, Peng Li, Zhiyuan Liu, Maosong Sun, and Jie Zhou. Learning from context or names? an empirical study on neural relation extraction. Conference on Empirical Methods in Natural Language Processing , 2020.

- Peng et al. [20242] Ji-Lun Peng, Sijia Cheng, Egil Diau, Yung-Yu Shih, Po-Heng Chen, Yen-Ting Lin, and Yun-Nung Chen. A survey of useful llm evaluation, arXiv preprint arXiv:2406.00936, 20242. URL https://arxiv.org/abs/2406.00936v1 .

- Perozzi et al. [2024] Bryan Perozzi, Bahare Fatemi, Dustin Zelle, Anton Tsitsulin, Mehran Kazemi, Rami Al-Rfou, and Jonathan J. Halcrow. Let your graph do the talking: Encoding structured data for llms, arXiv preprint arXiv:2402.05862, 2024. URL https://arxiv.org/abs/2402.05862v1 .

- Pesce and Montana [2019] E. Pesce and G. Montana. Improving coordination in small-scale multi-agent deep reinforcement learning through memory-driven communication. Machine-mediated learning , 2019.

- Petroni et al. [2020] F. Petroni, Patrick Lewis, Aleksandra Piktus, Tim Rocktäschel, Yuxiang Wu, Alexander H. Miller, and Sebastian Riedel. How context affects language models’ factual predictions. Conference on Automated Knowledge Base Construction , 2020.

- Pi et al. [2024] Yue Pi, Wang Zhang, Yong Zhang, Hairong Huang, Baoquan Rao, Yulong Ding, and Shuanghua Yang. Applications of multi-agent deep reinforcement learning communication in network management: A survey, arXiv preprint arXiv:2407.17030, 2024. URL https://arxiv.org/abs/2407.17030v1 .

- Piazza and Behzadan [2023] Nancirose Piazza and Vahid Behzadan. A theory of mind approach as test-time mitigation against emergent adversarial communication. Adaptive Agents and Multi-Agent Systems , 2023.

- Pink et al. [2024] Mathis Pink, Vy A. Vo, Qinyuan Wu, Jianing Mu, Javier S. Turek, Uri Hasson, Kenneth A. Norman, Sebastian Michelmann, Alexander Huth, and Mariya Toneva. Assessing episodic memory in llms with sequence order recall tasks, arXiv preprint arXiv:2410.08133, 2024. URL https://arxiv.org/abs/2410.08133v1 .

- Piya and Beheshti [2025] Fahmida Liza Piya and Rahmatollah Beheshti. Advancing feature extraction in healthcare through the integration of knowledge graphs and large language models. AAAI Conference on Artificial Intelligence , 2025.

- Plaat et al. [2025] A. Plaat, M. V. Duijn, N. V. Stein, Mike Preuss, P. V. D. Putten, and K. Batenburg. Agentic large language models, a survey, arXiv preprint arXiv:2503.23037, 2025. URL https://arxiv.org/abs/2503.23037v2 .

- Plenz and Frank [2024] Moritz Plenz and Anette Frank. Graph language models. Annual Meeting of the Association for Computational Linguistics , 2024.

- Polyn et al. [2009] Sean M. Polyn, K. Norman, and M. Kahana. A context maintenance and retrieval model of organizational processes in free recall. Psychology Review , 2009.

- Pond and Fujinaga [2025] Liam Pond and Ichiro Fujinaga. Teaching llms music theory with in-context learning and chain-of-thought prompting: Pedagogical strategies for machines. International Conference on Computer Supported Education , 2025.

- Porcu [2024] V Porcu. The role of memory in llms: Persistent context for smarter conversations. Int. J. Sci. Res. Manag.(IJSRM) , 12:1673–1691, 2024.

- Press et al. [2021] Ofir Press, Noah A. Smith, and M. Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. International Conference on Learning Representations , 2021.

- Puig et al. [2018] Xavier Puig, K. Ra, Marko Boben, Jiaman Li, Tingwu Wang, S. Fidler, and A. Torralba. Virtualhome: Simulating household activities via programs. 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition , 2018.

- Putta et al. [2024] Pranav Putta, Edmund Mills, Naman Garg, S. Motwani, Chelsea Finn, Divyansh Garg, and Rafael Rafailov. Agent q: Advanced reasoning and learning for autonomous ai agents, arXiv preprint arXiv:2408.07199, 2024. URL https://arxiv.org/abs/2408.07199v1 .

- Qasim et al. [2019] S. Qasim, Hassan Mahmood, and F. Shafait. Rethinking table recognition using graph neural networks. IEEE International Conference on Document Analysis and Recognition , 2019.

- Qi et al. [2020] Peng Qi, Haejun Lee, OghenetegiriTGSido, and Christopher D. Manning. Answering open-domain questions of varying reasoning steps from text. Conference on Empirical Methods in Natural Language Processing , 2020.

- Qi et al. [2024] Yong Qi, Gabriel Kyebambo, Siyuan Xie, Wei Shen, Shenghui Wang, Bitao Xie, Bin He, Zhipeng Wang, and Shuo Jiang. Safety control of service robots with llms and embodied knowledge graphs, arXiv preprint arXiv:2405.17846, 2024. URL https://arxiv.org/abs/2405.17846v1 .

- Qi et al. [20242] Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Xinyue Yang, Jiadai Sun, Yu Yang, Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, and Yuxiao Dong. Webrl: Training llm web agents via self-evolving online curriculum reinforcement learning, arXiv preprint arXiv:2411.02337, 20242. URL https://arxiv.org/abs/2411.02337v3 .

- Qian et al. [2024] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. Chatdev: Communicative agents for software development, arXiv preprint arXiv:2307.07924, 2024. URL https://arxiv.org/abs/2307.07924 .

- Qian et al. [2023] Cheng Qian, Chi Han, Y. Fung, Yujia Qin, Zhiyuan Liu, and Heng Ji. Creator: Tool creation for disentangling abstract and concrete reasoning of large language models. Conference on Empirical Methods in Natural Language Processing , 2023.

- Qian et al. [20242] Cheng Qian, Jiahao Li, Yufan Dang, Wei Liu, Yifei Wang, Zihao Xie, Weize Chen, Cheng Yang, Yingli Zhang, Zhiyuan Liu, and Maosong Sun. Iterative experience refinement of software-developing agents, arXiv preprint arXiv:2405.04219, 20242. URL https://arxiv.org/abs/2405.04219v1 .

- Qian et al. [2025] Cheng Qian, Emre Can Acikgoz, Qi He, Hongru Wang, Xiusi Chen, Dilek Hakkani-Tur, Gokhan Tur, and Heng Ji. Toolrl: Reward is all tool learning needs, arXiv preprint arXiv:2504.13958, 2025. URL https://arxiv.org/abs/2504.13958v1 .

- Qian et al. [20243] Hongjin Qian, Zheng Liu, Peitian Zhang, Zhicheng Dou, and Defu Lian. Boosting long-context management via query-guided activation refilling, arXiv preprint arXiv:2412.12486, 20243. URL https://arxiv.org/abs/2412.12486v3 .

- Qian et al. [20252] Hongjin Qian, Zheng Liu, Peitian Zhang, Kelong Mao, Defu Lian, Zhicheng Dou, and Tiejun Huang. Memorag: Boosting long context processing with global memory-enhanced retrieval augmentation, arXiv preprint arXiv:2409.05591, 20252. URL https://arxiv.org/abs/2409.05591 .

- Qian et al. [20253] Kangan Qian, Sicong Jiang, Yang Zhong, Ziang Luo, Zilin Huang, Tianze Zhu, Kun Jiang, Mengmeng Yang, Zheng Fu, Jinyu Miao, Yining Shi, He Zhe Lim, Li Liu, Tianbao Zhou, Hongyi Wang, Huang Yu, Yifei Hu, Guang Li, Guangyao Chen, Hao Ye, Lijun Sun, and Diange Yang. Agentthink: A unified framework for tool-augmented chain-of-thought reasoning in vision-language models for autonomous driving, arXiv preprint arXiv:2505.15298, 20253. URL https://arxiv.org/abs/2505.15298v3 .

- Qiao and Lu [2025] Changze Qiao and Mingming Lu. Efficiently enhancing general agents with hierarchical-categorical memory, arXiv preprint arXiv:2505.22006, 2025. URL https://arxiv.org/abs/2505.22006v1 .

- Qiao et al. [2023] S Qiao, H Gui, C Lv, Q Jia, H Chen, and N Zhang. Making language models better tool learners with execution feedback. 2023. URL https://arxiv.org/abs/2305.13068 .

- Qin et al. [2022] Binjie Qin, Haohao Mao, Ruipeng Zhang, Y. Zhu, Song Ding, and Xu Chen. Working memory inspired hierarchical video decomposition with transformative representations, arXiv preprint arXiv:2204.10105, 2022. URL https://arxiv.org/abs/2204.10105v3 .

- Qin et al. [20222] Bowen Qin, Binyuan Hui, Lihan Wang, Min Yang, Jinyang Li, Binhua Li, Ruiying Geng, Rongyu Cao, Jian Sun, Luo Si, Fei Huang, and Yongbin Li. A survey on text-to-sql parsing: Concepts, methods, and future directions, arXiv preprint arXiv:2208.13629, 20222. URL https://arxiv.org/abs/2208.13629v1 .

- Qin et al. [2023] Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang, Chaojun Xiao, Chi Han, Y. Fung, Yusheng Su, Huadong Wang, Cheng Qian, Runchu Tian, Kunlun Zhu, Shi Liang, Xingyu Shen, Bokai Xu, Zhen Zhang, Yining Ye, Bo Li, Ziwei Tang, Jing Yi, Yu Zhu, Zhenning Dai, Lan Yan, Xin Cong, Ya-Ting Lu, Weilin Zhao, Yuxiang Huang, Junxi Yan, Xu Han, Xian Sun, Dahai Li, Jason Phang, Cheng Yang, Tongshuang Wu, Heng Ji, Zhiyuan Liu, and Maosong Sun. Tool learning with foundation models. ACM Computing Surveys , 2023.

- Qin et al. [20232] Yujia Qin, Shi Liang, Yining Ye, Kunlun Zhu, Lan Yan, Ya-Ting Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Runchu Tian, Ruobing Xie, Jie Zhou, Marc H. Gerstein, Dahai Li, Zhiyuan Liu, and Maosong Sun. Toolllm: Facilitating large language models to master 16000+ real-world apis. International Conference on Learning Representations , 20232.

- Qin and Zhong [2023] Zhen Qin and Yiran Zhong. Accelerating toeplitz neural network with constant-time inference complexity. Conference on Empirical Methods in Natural Language Processing , 2023.

- Qin et al. [20233] Zhen Qin, Xiaodong Han, Weixuan Sun, Bowen He, Dong Li, Dongxu Li, Yuchao Dai, Lingpeng Kong, and Yiran Zhong. Toeplitz neural network for sequence modeling. International Conference on Learning Representations , 20233.

- Qin et al. [2024] Zhen Qin, Weigao Sun, Dong Li, Xuyang Shen, Weixuan Sun, and Yiran Zhong. Lightning attention-2: A free lunch for handling unlimited sequence lengths in large language models. arXiv preprint, 2024.

- Qiu et al. [2025] Jiahao Qiu, Xinzhe Juan, Yiming Wang, Ling Yang, Xuan Qi, Tongcheng Zhang, Jiacheng Guo, Yifu Lu, Zixin Yao, Hongru Wang, Shilong Liu, Xun Jiang, Liu Leqi, and Mengdi Wang. Agentdistill: Training-free agent distillation with generalizable mcp boxes, arXiv preprint arXiv:2506.14728, 2025. URL https://arxiv.org/abs/2506.14728v1 .

- Qiu et al. [20252] Jiahao Qiu, Fulian Xiao, Yiming Wang, Yuchen Mao, Yijia Chen, Xinzhe Juan, Siran Wang, Xuan Qi, Tongcheng Zhang, Zixin Yao, Jiacheng Guo, Yifu Lu, Charles Argon, Jundi Cui, Daixin Chen, Junran Zhou, Shuyao Zhou, Zhanpeng Zhou, Ling Yang, Shilong Liu, Hongru Wang, Kaixuan Huang, Xun Jiang, Yuming Cao, Yue Chen, Yunfei Chen, Zhengyi Chen, Ruowei Dai, Mengqiu Deng, Jiye Fu, Yu Gu, Zijie Guan, Zirui Huang, Xiaoyan Ji, Yumeng Jiang, Delong Kong, Haolong Li, Jiaqi Li, Ruipeng Li, Tianze Li, Zhuo-Yang Li, Haixia Lian, Meng Lin, Xudong Liu, Jiayi Lu, Jinghan Lu, Wanyu Luo, Ziyue Luo, Zihao Pu, Zhi Qiao, Rui-Fang Ren, Liang Wan, Ruixiang Wang, Tianhui Wang, Yang Wang, Zeyu Wang, Zihua Wang, Yujia Wu, Zhaoyi Wu, Hao Xin, Weiao Xing, Ruojun Xiong, Weijie Xu, Yao Shu, Xiao Yao, Xiaorui Yang, Yuchen Yang, Nan Yi, Jiadong Yu, Yang Yu, Huiting Zeng, Danni Zhang, Yunjie Zhang, Zhaoyu Zhang, Zhiheng Zhang, Xiaofeng Zheng, Peirong Zhou, Li-Ying Zhong, Xiaoyin Zong, Ying Zhao, Zhen Chen, Lin Ding, Xiaoyu Gao, Bingbing Gong,
Yichao Li, Yang Liao, Guang Ma, Tianyuan Ma, Xinrui Sun, Tianyi Wang, Han Xia, Ruobing Xian, Gen Ye, Tengfei Yu, Wentao Zhang, Yuxi Wang, Xi Gao, and Mengdi Wang. On path to multimodal historical reasoning: Histbench and histagent, arXiv preprint arXiv:2505.20246, 20252. URL https://arxiv.org/abs/2505.20246v3 .

- Qiu et al. [2024] Ruidi Qiu, Grace Li Zhang, Rolf Drechsler, Ulf Schlichtmann, and Bing Li. Autobench: Automatic testbench generation and evaluation using llms for hdl design. Workshop on Machine Learning for CAD , 2024.

- Qu et al. [2024] Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Jirong Wen. Tool learning with large language models: A survey. Frontiers Comput. Sci. , 2024.

- Qu et al. [2025] Xiaoye Qu, Yafu Li, Zhao yu Su, Weigao Sun, Jianhao Yan, Dongrui Liu, Ganqu Cui, Daizong Liu, Shuxian Liang, Junxian He, Peng Li, Wei Wei, Jing Shao, Chaochao Lu, Yue Zhang, Xian-Sheng Hua, Bowen Zhou, and Yu Cheng. A survey of efficient reasoning for large reasoning models: Language, multimodality, and beyond, arXiv preprint arXiv:2503.21614, 2025. URL https://arxiv.org/abs/2503.21614v1 .

- Quintanar-Zilinskas [2019] Victor Quintanar-Zilinskas. A neuromimetic approach to the serial acquisition, long-term storage, and selective utilization of overlapping memory engrams. bioRxiv , 2019.

- Raaijmakers et al. [2024] Stephan Raaijmakers, Roos Bakker, Anita Cremers, Roy de Kleijn, Tom Kouwenhoven, and Tessa Verhoef. Memory-augmented generative adversarial transformers, arXiv preprint arXiv:2402.19218, 2024. URL https://arxiv.org/abs/2402.19218 .

- Rabinovich and Anaby-Tavor [2025] Ella Rabinovich and Ateret Anaby-Tavor. On the robustness of agentic function calling. Proceedings of the 5th Workshop on Trustworthy NLP (TrustNLP 2025) , 2025.

- Rabinowitz et al. [2018] Neil C. Rabinowitz, Frank Perbet, H. F. Song, Chiyuan Zhang, S. Eslami, and M. Botvinick. Machine theory of mind. International Conference on Machine Learning , 2018.

- Rackauckas [2024] Zackary Rackauckas. Rag-fusion: a new take on retrieval-augmented generation. International Journal on Natural Language Computing , 2024.

- Radford et al. [2021] Alec Radford, Jong Wook Kim, Chris Hallacy, A. Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and I. Sutskever. Learning transferable visual models from natural language supervision. International Conference on Machine Learning , 2021.

- Raffel et al. [2019] Colin Raffel, Noam M. Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research , 2019.

- Raiaan et al. [2024] Mohaimenul Azam Khan Raiaan, Md. Saddam Hossain Mukta, Kaniz Fatema, Nur Mohammad Fahad, S. Sakib, Most. Marufatul Jannat Mim, Jubaer Ahmad, Mohammed Eunus Ali, and Sami Azam. A review on large language models: Architectures, applications, taxonomies, open issues and challenges. IEEE Access , 2024.

- Ramji et al. [2024] Keshav Ramji, Young-Suk Lee, R. Astudillo, M. Sultan, Tahira Naseem, Asim Munawar, Radu Florian, and S. Roukos. Self-refinement of language models from external proxy metrics feedback, arXiv preprint arXiv:2403.00827, 2024. URL https://arxiv.org/abs/2403.00827v1 .

- Rasal [2024] Sumedh Rasal. An artificial neuron for enhanced problem solving in large language models, arXiv preprint arXiv:2404.14222, 2024. URL https://arxiv.org/abs/2404.14222v1 .

- Raza et al. [2025] Shaina Raza, Ranjan Sapkota, Manoj Karkee, and Christos Emmanouilidis. Trism for agentic ai: A review of trust, risk, and security management in llm-based agentic multi-agent systems, arXiv preprint arXiv:2506.04133, 2025. URL https://arxiv.org/abs/2506.04133v2 .

- Ren and Xia [2024] Jing Ren and Feng Xia. Brain-inspired artificial intelligence: A comprehensive review, arXiv preprint arXiv:2408.14811, 2024. URL https://arxiv.org/abs/2408.14811v1 .

- Ren et al. [2025] Shuo Ren, Pu Jian, Zhenjiang Ren, Chunlin Leng, Can Xie, and Jiajun Zhang. Towards scientific intelligence: A survey of llm-based scientific agents, arXiv preprint arXiv:2503.24047, 2025. URL https://arxiv.org/abs/2503.24047v2 .

- Ren et al. [2024] Xubin Ren, Jiabin Tang, Dawei Yin, Nitesh V. Chawla, and Chao Huang. A survey of large language models for graphs. Knowledge Discovery and Data Mining , 2024.

- Ren et al. [20242] Yi Ren, Shangmin Guo, Linlu Qiu, Bailin Wang, and Danica J. Sutherland. Bias amplification in language model evolution: An iterated learning perspective. Neural Information Processing Systems , 20242.

- Rezazadeh et al. [2024] Alireza Rezazadeh, Zichao Li, Wei Wei, and Yujia Bao. From isolated conversations to hierarchical schemas: Dynamic tree memory representation for llms. International Conference on Learning Representations , 2024.

- Ribeiro et al. [2019] Marco Tulio Ribeiro, Carlos Guestrin, and Sameer Singh. Are red roses red? evaluating consistency of question-answering models. Annual Meeting of the Association for Computational Linguistics , 2019.

- Rizk et al. [2020] Yara Rizk, Abhishek Bhandwalder, S. Boag, Tathagata Chakraborti, Vatche Isahagian, Y. Khazaeni, Falk Pollock, and Merve Unuvar. A unified conversational assistant framework for business process automation, arXiv preprint arXiv:2001.03543, 2020. URL https://arxiv.org/abs/2001.03543v1 .

- Rizk et al. [20202] Yara Rizk, Vatche Isahagian, S. Boag, Y. Khazaeni, Merve Unuvar, Vinod Muthusamy, and Rania Y. Khalaf. A conversational digital assistant for intelligent process automation. International Conference on Business Process Management , 20202.

- Rizvi et al. [2022] S. Rizvi, Nazreen Pallikkavaliyaveetil, David Zhang, Zhuoyang Lyu, Nhi Nguyen, Haoran Lyu, B. Christensen, J. O. Caro, Antonio H. O. Fonseca, E. Zappala, Maryam Bagherian, Christopher Averill, C. Abdallah, Amin Karbasi, Rex Ying, M. Brbic, R. M. Dhodapkar, and David van Dijk. Fimp: Foundation model-informed message passing for graph neural networks, arXiv preprint arXiv:2210.09475v5, 2022. URL https://arxiv.org/abs/2210.09475v5 .

- Robinson et al. [2022] Joshua Robinson, Christopher Rytting, and D. Wingate. Leveraging large language models for multiple choice question answering. International Conference on Learning Representations , 2022.

- Rocco et al. [2024] Juri Di Rocco, D. D. Ruscio, Claudio Di Sipio, P. T. Nguyen, and Riccardo Rubei. On the use of large language models in model-driven engineering. Journal of Software and Systems Modeling , 2024.

- Rodriguez et al. [2025] Juan David Salazar Rodriguez, Sam Conrad Joyce, and Julfendi Julfendi. Using customized gpt to develop prompting proficiency in architectural ai-generated images, arXiv preprint arXiv:2504.13948, 2025. URL https://arxiv.org/abs/2504.13948v2 .

- Roethel et al. [2023] Albert Roethel, M. Ganzha, and Anna Wr’oblewska. Enriching language models with graph-based context information to better understand textual data. Electronics , 2023.

- Rolim et al. [2018] Reudismam Rolim, Gustavo Soares, Rohit Gheyi, and Loris D’antoni. Learning quick fixes from code repositories. Brazilian Symposium on Software Engineering , 2018.

- Rombach et al. [2021] Robin Rombach, A. Blattmann, Dominik Lorenz, Patrick Esser, and B. Ommer. High-resolution image synthesis with latent diffusion models. Computer Vision and Pattern Recognition , 2021.

- Ross et al. [2025] Hayley Ross, A. Mahabaleshwarkar, and Yoshi Suhara. When2call: When (not) to call tools. North American Chapter of the Association for Computational Linguistics , 2025.

- Rosser and Foerster [2025] J. Rosser and Jakob N. Foerster. Agentbreeder: Mitigating the ai safety impact of multi-agent scaffolds, arXiv preprint arXiv:2502.00757, 2025. URL https://arxiv.org/abs/2502.00757v3 .

- Rossi et al. [2018] Federico Rossi, Saptarshi Bandyopadhyay, Michael T. Wolf, and M. Pavone. Review of multi-agent algorithms for collective behavior: a structural taxonomy, arXiv preprint arXiv:1803.05464, 2018. URL https://arxiv.org/abs/1803.05464v1 .

- Rossi et al. [2021] Federico Rossi, Saptarshi Bandyopadhyay, Michael T. Wolf, and M. Pavone. Multi-agent algorithms for collective behavior: A structural and application-focused atlas, arXiv preprint arXiv:2103.11067, 2021. URL https://arxiv.org/abs/2103.11067v1 .

- Roxin and Fusi [2013] Alex Roxin and Stefano Fusi. Efficient partitioning of memory systems and its importance for memory consolidation. PLoS Comput. Biol. , 2013.

- Roy et al. [2023] Kaushik Roy, Yuxin Zi, Vignesh Narayanan, Manas Gaur, and Amit P. Sheth. Knowledge-infused self attention transformers, arXiv preprint arXiv:2306.13501, 2023. URL https://arxiv.org/abs/2306.13501v1 .

- Ru et al. [2024] Dongyu Ru, Lin Qiu, Xiangkun Hu, Tianhang Zhang, Peng Shi, Shuaichen Chang, Jiayang Cheng, Cunxiang Wang, Shichao Sun, Huanyu Li, Zizhao Zhang, Binjie Wang, Jiarong Jiang, Tong He, Zhiguo Wang, Pengfei Liu, Yue Zhang, and Zheng Zhang. Ragchecker: A fine-grained framework for diagnosing retrieval-augmented generation. Neural Information Processing Systems , 2024.

- Ruan et al. [2023] Jingqing Ruan, Yihong Chen, Bin Zhang, Zhiwei Xu, Tianpeng Bao, Guoqing Du, Shiwei Shi, Hangyu Mao, Ziyue Li, Xingyu Zeng, and Rui Zhao. Tptu: Large language model-based ai agents for task planning and tool usage, arXiv preprint arXiv:2308.03427, 2023. URL https://arxiv.org/abs/2308.03427 .

- Russak et al. [2024] M. Russak, Umar Jamil, Christopher Bryant, Kiran Kamble, Axel Magnuson, Mateusz Russak, and Waseem Alshikh. Writing in the margins: Better inference pattern for long context retrieval, arXiv preprint arXiv:2408.14906, 2024. URL https://arxiv.org/abs/2408.14906v1 .

- Ryu and Kim [2024] Hyun Ryu and Eric Kim. Closer look at efficient inference methods: A survey of speculative decoding, arXiv preprint arXiv:2411.13157, 2024. URL https://arxiv.org/abs/2411.13157v2 .

- Saberi and Fard [2024] Iman Saberi and Fatemeh Fard. Context-augmented code generation using programming knowledge graphs, arXiv preprint arXiv:2410.18251, 2024. URL https://arxiv.org/abs/2410.18251v2 .

- Safa and Sahin [2024] Abdulfattah Safa and Gözde Gül Sahin. A zero-shot open-vocabulary pipeline for dialogue understanding. North American Chapter of the Association for Computational Linguistics , 2024.

- Safaei et al. [2024] Alireza Akhavan Safaei, Pegah Saboori, Reza Ramezani, and Mohammadali Nematbakhsh. Kglm-qa: A novel approach for knowledge graph-enhanced large language models for question answering. Conference on Information and Knowledge Technology , 2024.

- Saha et al. [2024] Avirup Saha, Lakshmi Mandal, Balaji Ganesan, Sambit Ghosh, Renuka Sindhgatta, Carlos Eberhardt, Dan Debrunner, and Sameep Mehta. Sequential api function calling using graphql schema. Conference on Empirical Methods in Natural Language Processing , 2024.

- Sahoo et al. [2024] Pranab Sahoo, Ayush Kumar Singh, Sriparna Saha, Vinija Jain, S. Mondal, and Aman Chadha. A systematic survey of prompt engineering in large language models: Techniques and applications, arXiv preprint arXiv:2402.07927, 2024. URL https://arxiv.org/abs/2402.07927v2 .

- Salama et al. [2025] Rana Salama, Jason Cai, Michelle Yuan, Anna Currey, Monica Sunkara, Yi Zhang, and Yassine Benajiba. Meminsight: Autonomous memory augmentation for llm agents, arXiv preprint arXiv:2503.21760, 2025. URL https://arxiv.org/abs/2503.21760 .

- Salan et al. [2024] Jefferson Salan, Devyn E Smith, Erica S Shafer, and Rachel A Diana. Variation in encoding context benefits item recognition. Memory & Cognition , 2024.

- Saleh et al. [2025] Alaa Saleh, Sasu Tarkoma, Praveen Kumar Donta, Naser Hossein Motlagh, S. Dustdar, Susanna Pirttikangas, and Lauri Lov’en. Usercentrix: An agentic memory-augmented ai framework for smart spaces, arXiv preprint arXiv:2505.00472, 2025. URL https://arxiv.org/abs/2505.00472v1 .

- Salewski et al. [2023] Leonard Salewski, Stephan Alaniz, Isabel Rio-Torto, Eric Schulz, and Zeynep Akata. In-context impersonation reveals large language models’ strengths and biases. Neural Information Processing Systems , 2023.

- Samsonovich [2010] A. Samsonovich. Toward a unified catalog of implemented cognitive architectures. Biologically Inspired Cognitive Architectures , 2010.

- Sanikommu [2025] Narendra Reddy Sanikommu. Model context protocol: Enhancing llm performance for observability and analytics. European journal of computer science and information technology , 2025.

- Santhanam [2020] S. Santhanam. Context based text-generation using lstm networks, arXiv preprint arXiv:2005.00048, 2020. URL https://arxiv.org/abs/2005.00048v1 .

- Santos et al. [2025] G. Santos, Rita Maria Silva Julia, and Marcelo Zanchetta do Nascimento. Diverse prompts: Illuminating the prompt space of large language models with map-elites. IEEE Congress on Evolutionary Computation , 2025.

- Sapkota et al. [2025] Ranjan Sapkota, Konstantinos I. Roumeliotis, and Manoj Karkee. Ai agents vs. agentic ai: A conceptual taxonomy, applications and challenges, arXiv preprint arXiv:2505.10468, 2025. URL https://arxiv.org/abs/2505.10468v4 .

- Sarkar and Sarkar [2025] Anjana Sarkar and Soumyendu Sarkar. Survey of llm agent communication with mcp: A software design pattern centric review, arXiv preprint arXiv:2506.05364, 2025. URL https://arxiv.org/abs/2506.05364v1 .

- Sarkar and Lausen [2023] Soumajyoti Sarkar and Leonard Lausen. Testing the limits of unified sequence to sequence llm pretraining on diverse table data tasks, arXiv preprint arXiv:2310.00789, 2023. URL https://arxiv.org/abs/2310.00789v1 .

- Sarthi et al. [2024] Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, and Christopher D. Manning. Raptor: Recursive abstractive processing for tree-organized retrieval. International Conference on Learning Representations , 2024.

- Sarti [2020] Gabriele Sarti. Umberto-mtsa @ accompl-it: Improving complexity and acceptability prediction with multi-task learning on self-supervised annotations (short paper). International Workshop on Evaluation of Natural Language and Speech Tools for Italian , 2020.

- Saxena et al. [2022] Apoorv Saxena, Adrian Kochsiek, and Rainer Gemulla. Sequence-to-sequence knowledge graph completion and question answering. Annual Meeting of the Association for Computational Linguistics , 2022.

- Schick et al. [2023] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, R. Raileanu, M. Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. Neural Information Processing Systems , 2023.

- Schillaci et al. [2021] Guido Schillaci, Uwe Schmidt, and Luis Miranda. Prediction error-driven memory consolidation for continual learning: On the case of adaptive greenhouse models. KI - Künstliche Intelligenz , 35(1):71–80, 2021. ISSN 1610-1987. 10.1007/s13218-020-00700-8 . URL http://dx.doi.org/10.1007/s13218-020-00700-8 .

- Schneider et al. [2025] Florian Schneider, Narges Baba Ahmadi, Niloufar Baba Ahmadi, Iris Vogel, Martin Semmann, and Christian Biemann. Collex - a multimodal agentic rag system enabling interactive exploration of scientific collections. arXiv preprint, 2025.

- Schoepp et al. [2025] Sheila Schoepp, Masoud Jafaripour, Yingyue Cao, Tianpei Yang, Fatemeh Abdollahi, Shadan Golestan, Zahin Sufiyan, Osmar R. Zaiane, and Matthew E. Taylor. The evolving landscape of llm- and vlm-integrated reinforcement learning. arXiv preprint, 2025.

- Shan et al. [2025] Lianlei Shan, Shixian Luo, Zezhou Zhu, Yu Yuan, and Yong Wu. Cognitive memory in large language models, arXiv preprint arXiv:2504.02441, 2025. URL https://arxiv.org/abs/2504.02441v2 .

- Shang and Huang [2024] Wenbo Shang and Xin Huang. A survey of large language models on generative graph analytics: Query, learning, and applications, arXiv preprint arXiv:2404.14809v2, 2024. URL https://arxiv.org/abs/2404.14809v2 .

- Shao et al. [2023] Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng Qiu. Character-llm: A trainable agent for role-playing, arXiv preprint arXiv:2310.10158, 2023. URL https://arxiv.org/abs/2310.10158 .

- Shao and Nakashole [2024] Yutong Shao and N. Nakashole. On linearizing structured data in encoder-decoder language models: Insights from text-to-sql. North American Chapter of the Association for Computational Linguistics , 2024.

- Shao et al. [20232] Zhihong Shao, Yeyun Gong, Yelong Shen, Minlie Huang, Nan Duan, and Weizhu Chen. Synthetic prompting: Generating chain-of-thought demonstrations for large language models. International Conference on Machine Learning , 20232.

- Shaw et al. [2023] Peter Shaw, Mandar Joshi, James Cohan, Jonathan Berant, Panupong Pasupat, Hexiang Hu, Urvashi Khandelwal, Kenton Lee, and Kristina Toutanova. From pixels to ui actions: Learning to follow instructions via graphical user interfaces. Neural Information Processing Systems , 2023.

- Shen et al. [2017] Jonathan Shen, Ruoming Pang, Ron J. Weiss, M. Schuster, N. Jaitly, Zongheng Yang, Z. Chen, Yu Zhang, Yuxuan Wang, R. Skerry-Ryan, R. Saurous, Yannis Agiomyrgiannakis, and Yonghui Wu. Natural tts synthesis by conditioning wavenet on mel spectrogram predictions. IEEE International Conference on Acoustics, Speech, and Signal Processing , 2017.

- Shen et al. [2024] Junhong Shen, Atishay Jain, Zedian Xiao, Ishan Amlekar, Mouad Hadji, Aaron Podolny, and Ameet Talwalkar. Scribeagent: Towards specialized web agents using production-scale workflow data. 2024.

- Shen et al. [2025] Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang, Tong Zhang, Ameet Talwalkar, and Aviral Kumar. Thinking vs. doing: Agents that reason by scaling test-time interaction, arXiv preprint arXiv:2506.07976, 2025. URL https://arxiv.org/abs/2506.07976 .

- Shen et al. [20252] Weizhou Shen, Chenliang Li, Fanqi Wan, Shengyi Liao, Shaopeng Lai, Bo Zhang, Yingcheng Shi, Yuning Wu, Gang Fu, Zhansheng Li, Bin Yang, Ji Zhang, Fei Huang, Jingren Zhou, and Ming Yan. Qwenlong-cprs: Towards ∞ \infty ∞ -llms with dynamic context optimization. arXiv preprint, 20252.

- Shen et al. [2023] Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Y. Zhuang. Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging face. Neural Information Processing Systems , 2023.

- Shen [2024] Zhuocheng Shen. Llm with tools: A survey, arXiv preprint arXiv:2409.18807, 2024. URL https://arxiv.org/abs/2409.18807v1 .

- Sheng et al. [2023] Ying Sheng, Lianmin Zheng, Binhang Yuan, Zhuohan Li, Max Ryabinin, Daniel Y. Fu, Zhiqiang Xie, Beidi Chen, Clark W. Barrett, Joseph Gonzalez, Percy Liang, Christopher Ré, Ion Stoica, and Ce Zhang. High-throughput generative inference of large language models with a single gpu. International Conference on Machine Learning , 2023.

- Shi et al. [2025] Dingfeng Shi, Jingyi Cao, Qianben Chen, Weichen Sun, Weizhen Li, Hongxuan Lu, Fangchen Dong, Tianrui Qin, King Zhu, Minghao Liu, Jian Yang, Ge Zhang, Jiaheng Liu, Changwang Zhang, Jun Wang, Y. Jiang, and Wangchunshu Zhou. Taskcraft: Automated generation of agentic tasks, arXiv preprint arXiv:2506.10055, 2025. URL https://arxiv.org/abs/2506.10055v2 .

- Shi et al. [2021] Han Shi, Jiahui Gao, Xiaozhe Ren, Hang Xu, Xiaodan Liang, Zhenguo Li, and J. Kwok. Sparsebert: Rethinking the importance analysis in self-attention. International Conference on Machine Learning , 2021.

- Shi et al. [2020] Peng Shi, Patrick Ng, Zhiguo Wang, Henghui Zhu, Alexander Hanbo Li, Jun Wang, C. D. Santos, and Bing Xiang. Learning contextual representations for semantic parsing with generation-augmented pre-training. AAAI Conference on Artificial Intelligence , 2020.

- Shi et al. [2023] Weijia Shi, Xiaochuang Han, M. Lewis, Yulia Tsvetkov, Luke Zettlemoyer, and S. Yih. Trusting your evidence: Hallucinate less with context-aware decoding. North American Chapter of the Association for Computational Linguistics , 2023.

- Shi et al. [2024] Zhengliang Shi, Shen Gao, Xiuyi Chen, Yue Feng, Lingyong Yan, Haibo Shi, Dawei Yin, Zhumin Chen, Suzan Verberne, and Zhaochun Ren. Tool learning in the wild: Empowering language models as automatic tool agents. The Web Conference , 2024.

- Shim et al. [2024] Jay Shim, Grant Kruttschnitt, Alyssa Ma, Daniel Kim, Benjamin Chek, Athul Anand, Kevin Zhu, and Sean O’Brien. Chain-of-thought augmentation with logit contrast for enhanced reasoning in language models, arXiv preprint arXiv:2407.03600, 2024. URL https://arxiv.org/abs/2407.03600v2 .

- Shin et al. [2024] Jiho Shin, Reem Aleithan, Hadi Hemmati, and Song Wang. Retrieval-augmented test generation: How far are we?, arXiv preprint arXiv:2409.12682, 2024. URL https://arxiv.org/abs/2409.12682v1 .

- Shin et al. [2022] Seongjin Shin, Sang-Woo Lee, Hwijeen Ahn, Sungdong Kim, Hyoungseok Kim, Boseop Kim, Kyunghyun Cho, Gichang Lee, W. Park, Jung-Woo Ha, and Nako Sung. On the effect of pretraining corpora on in-context learning by a large-scale language model. North American Chapter of the Association for Computational Linguistics , 2022.

- Shinn et al. [2023] Noah Shinn, Federico Cassano, Beck Labash, A. Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: language agents with verbal reinforcement learning. Neural Information Processing Systems , 2023.

- Shiri et al. [2024] Fatemeh Shiri, Xiao-Yu Guo, Mona Far, Xin Yu, Reza Haf, and Yuan-Fang Li. An empirical analysis on spatial reasoning capabilities of large multimodal models. Conference on Empirical Methods in Natural Language Processing , 2024.

- Shokrnezhad et al. [2024] Masoud Shokrnezhad, Hao Yu, T. Taleb, Renwei Li, Kyunghan Lee, Jaeseung Song, and Cedric Westphal. Toward a dynamic future with adaptable computing and network convergence (acnc). IEEE Network , 2024.

- Shorten et al. [2021] Connor Shorten, T. Khoshgoftaar, and B. Furht. Text data augmentation for deep learning. Journal of Big Data , 2021.

- Shridhar et al. [2019] Mohit Shridhar, Jesse Thomason, Daniel Gordon, Yonatan Bisk, Winson Han, Roozbeh Mottaghi, Luke Zettlemoyer, and D. Fox. Alfred: A benchmark for interpreting grounded instructions for everyday tasks. Computer Vision and Pattern Recognition , 2019.

- Shukurlu [2025] Altun Shukurlu. Improving deep knowledge tracing via gated architectures and adaptive optimization, arXiv preprint arXiv:2504.20070, 2025. URL https://arxiv.org/abs/2504.20070v1 .

- Siegel and Kahana [2014] Lynn L Siegel and M. Kahana. A retrieved context account of spacing and repetition effects in free recall. Journal of Experimental Psychology. Learning, Memory and Cognition , 2014.

- Singh et al. [2024] Aditi Singh, Abul Ehtesham, Gaurav Kumar Gupta, Nikhil Kumar Chatta, Saket Kumar, and T. T. Khoei. Exploring prompt engineering: A systematic review with swot analysis, arXiv preprint arXiv:2410.12843, 2024. URL https://arxiv.org/abs/2410.12843v1 .

- Singh and Diao [2024] Anmolika Singh and Yuhang Diao. Leveraging large language models for optimized item categorization using unspsc taxonomy. International Journal on Cybernetics & Informatics , 2024.

- Singh et al. [2025] Joykirat Singh, Raghav Magazine, Yash Pandya, and A. Nambi. Agentic reasoning and tool integration for llms via reinforcement learning, arXiv preprint arXiv:2505.01441, 2025. URL https://arxiv.org/abs/2505.01441v1 .

- Singh et al. [20242] Krishnakant Singh, Thanush Navaratnam, Jannik Holmer, Simone Schaub-Meyer, and Stefan Roth. Is synthetic data all we need? benchmarking the robustness of models trained with synthetic images. 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW) , 20242.

- Singh et al. [20252] Ramneet Singh, Sathvik Joel, Abhav Mehrotra, Nalin Wadhwa, Ramakrishna Bairi, Aditya Kanade, and Nagarajan Natarajan. Code researcher: Deep research agent for large systems code and commit history, arXiv preprint arXiv:2506.11060, 20252. URL https://arxiv.org/abs/2506.11060v1 .

- Sinha and Omkumar [2025] Aarush Sinha and CU Omkumar. Gmlm: Bridging graph neural networks and language models for heterophilic node classification, arXiv preprint arXiv:2503.05763, 2025. URL https://arxiv.org/abs/2503.05763v3 .

- Sinha et al. [2024] Sanchit Sinha, Yuguang Yue, Victor Soto, Mayank Kulkarni, Jianhua Lu, and Aidong Zhang. Maml-en-llm: Model agnostic meta-training of llms for improved in-context learning. Knowledge Discovery and Data Mining , 2024.

- Sisate et al. [2025] Colin Sisate, Alistair Goldfinch, Vincent Waterstone, Sebastian Kingsley, and Mariana Blackthorn. Contextually entangled gradient mapping for optimized llm comprehension, arXiv preprint arXiv:2502.00048, 2025. URL https://arxiv.org/abs/2502.00048v1 .

- Sodhi et al. [2024] Paloma Sodhi, S. R. K. Branavan, Yoav Artzi, and Ryan McDonald. Step: Stacked llm policies for web actions, arXiv preprint arXiv:2310.03720, 2024. URL https://arxiv.org/abs/2310.03720 .

- Solanki [2025] Manthankumar Solanki. Efficient document retrieval with g-retriever. arXiv preprint, 2025.

- Soman et al. [2023] Karthik Soman, Peter W Rose, John H Morris, Rabia E Akbas, Brett Smith, Braian Peetoom, Catalina Villouta-Reyes, G. Cerono, Yongmei Shi, Angela Rizk-Jackson, Sharat Israni, Charlotte A. Nelson, Sui Huang, and Sergio Baranzini. Biomedical knowledge graph-optimized prompt generation for large language models. Bioinformatics , 2023.

- Some et al. [2025] Lilian Some, Wenli Yang, Michael Bain, and Byeong Kang. A comprehensive survey on integrating large language models with knowledge-based methods. Knowledge-Based Systems , 2025.

- Song et al. [2022] Chan Hee Song, Jiaman Wu, Clay Washington, Brian M. Sadler, Wei-Lun Chao, and Yu Su. Llm-planner: Few-shot grounded planning for embodied agents with large language models. IEEE International Conference on Computer Vision , 2022.

- Song et al. [2025] Huatong Song, Jinhao Jiang, Yingqian Min, Jie Chen, Zhipeng Chen, Wayne Xin Zhao, Lei Fang, and Ji-Rong Wen. R1-searcher: Incentivizing the search capability in llms via reinforcement learning. arXiv preprint, 2025.

- Song et al. [2024] Woomin Song, Seunghyuk Oh, Sangwoo Mo, Jaehyung Kim, Sukmin Yun, Jung-Woo Ha, and Jinwoo Shin. Hierarchical context merging: Better long context understanding for pre-trained llms. International Conference on Learning Representations , 2024.

- Song et al. [20252] Woomin Song, Sai Muralidhar Jayanthi, S. Ronanki, Kanthashree Mysore Sathyendra, Jinwoo Shin, A. Galstyan, Shubham Katiyar, and S. Bodapati. Compress, gather, and recompute: Reforming long-context processing in transformers, arXiv preprint arXiv:2506.01215, 20252. URL https://arxiv.org/abs/2506.01215v1 .

- Song et al. [20253] Yewei Song, Xunzhu Tang, Cedric Lothritz, Saad Ezzini, Jacques Klein, Tegawend’e F. Bissyand’e, A. Boytsov, Ulrick Ble, and Anne Goujon. Callnavi, a challenge and empirical study on llm function calling and routing, arXiv preprint arXiv:2501.05255, 20253. URL https://arxiv.org/abs/2501.05255v2 .

- Song et al. [20254] Yueqi Song, Frank Xu, Shuyan Zhou, and Graham Neubig. Beyond browsing: Api-based web agents, arXiv preprint arXiv:2410.16464, 20254. URL https://arxiv.org/abs/2410.16464 .

- Srinivasa and Deshmukh [2021] S. Srinivasa and Jayati Deshmukh. Paradigms of computational agency. Novel Approaches to Information Systems Design , 2021.

- Staresina et al. [2012] B. Staresina, R. Henson, N. Kriegeskorte, and Arjen Alink. Episodic reinstatement in the medial temporal lobe. Journal of Neuroscience , 2012.

- Staudigl et al. [2015] T. Staudigl, C. Vollmar, S. Noachtar, and S. Hanslmayr. Temporal-pattern similarity analysis reveals the beneficial and detrimental effects of context reinstatement on human memory. Journal of Neuroscience , 2015.

- Stechly et al. [2024] Kaya Stechly, Karthik Valmeekam, and Subbarao Kambhampati. Chain of thoughtlessness? an analysis of cot in planning. Neural Information Processing Systems , 2024.

- Sterken and Kirkpatrick [2025] R. Sterken and James Ravi Kirkpatrick. Conversational alignment with artificial intelligence in context. Philosophical Perspectives , 2025.

- Stoewer et al. [2023] Paul Stoewer, Achim Schilling, Andreas K. Maier, and Patrick Krauss. Multi-modal cognitive maps based on neural networks trained on successor representations, arXiv preprint arXiv:2401.01364, 2023. URL https://arxiv.org/abs/2401.01364v1 .

- Styles et al. [2024] Olly Styles, Sam Miller, Patricio Cerda-Mardini, T. Guha, Victor Sanchez, and Bertie Vidgen. Workbench: a benchmark dataset for agents in a realistic workplace setting, arXiv preprint arXiv:2405.00823, 2024. URL https://arxiv.org/abs/2405.00823v2 .

- Su et al. [2024] Guangxin Su, Yifan Zhu, Wenjie Zhang, Hanchen Wang, and Ying Zhang. Bridging large language models and graph structure learning models for robust representation learning, arXiv preprint arXiv:2410.12096, 2024. URL https://arxiv.org/abs/2410.12096v1 .

- Su et al. [2008] Hong Su, Elke A. Rundensteiner, and Murali Mani. Automaton in or out: run-time plan optimization for xml stream processing. International Symposium on Signal Processing Systems , 2008.

- Su et al. [2025] Hongjin Su, Ruoxi Sun, Jinsung Yoon, Pengcheng Yin, Tao Yu, and Sercan Ö. Arık. Learn-by-interact: A data-centric framework for self-adaptive agents in realistic environments. 2025.

- Su et al. [20252] Jinyan Su, Jennifer Healey, Preslav Nakov, and Claire Cardie. Between underthinking and overthinking: An empirical study of reasoning length and correctness in llms, arXiv preprint arXiv:2505.00127, 20252. URL https://arxiv.org/abs/2505.00127v1 .

- Su et al. [20242] Weihang Su, Yichen Tang, Qingyao Ai, Zhijing Wu, and Yiqun Liu. Dragin: Dynamic retrieval augmented generation based on the real-time information needs of large language models. Annual Meeting of the Association for Computational Linguistics , 20242.

- Su et al. [20243] Xin Su, Man Luo, Kris W Pan, Tien Pei Chou, Vasudev Lal, and Phillip Howard. Sk-vqa: Synthetic knowledge generation at scale for training context-augmented multimodal llms. arXiv preprint, 20243.

- Subagdja and Tan [2015] Budhitama Subagdja and A. Tan. Neural modeling of sequential inferences and learning over episodic memory. Neurocomputing , 2015.

- Sui et al. [2025] Yang Sui, Yu-Neng Chuang, Guanchu Wang, Jiamu Zhang, Tianyi Zhang, Jiayi Yuan, Hongyi Liu, Andrew Wen, Shaochen Zhong, Hanjie Chen, and Xia Hu. Stop overthinking: A survey on efficient reasoning for large language models, arXiv preprint arXiv:2503.16419, 2025. URL https://arxiv.org/abs/2503.16419v3 .

- Sun et al. [2024] Chuanneng Sun, Songjun Huang, and D. Pompili. Llm-based multi-agent reinforcement learning: Current and future directions, arXiv preprint arXiv:2405.11106, 2024. URL https://arxiv.org/abs/2405.11106v1 .

- Sun et al. [20242] Hanshi Sun, Zhuoming Chen, Xinyu Yang, Yuandong Tian, and Beidi Chen. Triforce: Lossless acceleration of long sequence generation with hierarchical speculative decoding, arXiv preprint arXiv:2404.11912, 20242. URL https://arxiv.org/abs/2404.11912v3 .

- Sun et al. [2023] Haotian Sun, Yuchen Zhuang, Lingkai Kong, Bo Dai, and Chao Zhang. Adaplanner: Adaptive planning from feedback with language models. Neural Information Processing Systems , 2023.

- Sun et al. [20232] Jiankai Sun, Chuanyang Zheng, E. Xie, Zhengying Liu, Ruihang Chu, Jianing Qiu, Jiaqi Xu, Mingyu Ding, Hongyang Li, Mengzhe Geng, Yue Wu, Wenhai Wang, Junsong Chen, Zhangyue Yin, Xiaozhe Ren, Jie Fu, Junxian He, Wu Yuan, Qi Liu, Xihui Liu, Yu Li, Hao Dong, Yu Cheng, Ming Zhang, P. Heng, Jifeng Dai, Ping Luo, Jingdong Wang, Jingwei Wen, Xipeng Qiu, Yi-Chen Guo, Hui Xiong, Qun Liu, and Zhenguo Li. A survey of reasoning with foundation models: Concepts, methodologies, and outlook. ACM Computing Surveys , 20232.

- Sun et al. [20233] Jiashuo Sun, Chengjin Xu, Lumingyuan Tang, Sai Wang, Chen Lin, Yeyun Gong, H. Shum, and Jian Guo. Think-on-graph: Deep and responsible reasoning of large language model with knowledge graph. arXiv preprint, 20233.

- Sun et al. [20243] Lei Sun, Zhengwei Tao, Youdi Li, and Hiroshi Arakawa. Oda: Observation-driven agent for integrating llms and knowledge graphs, arXiv preprint arXiv:2404.07677, 20243. URL https://arxiv.org/abs/2404.07677 .

- Sun et al. [20244] Lei Sun, Xinchen Wang, and Youdi Li. Pyramid-driven alignment: Pyramid principle guided integration of large language models and knowledge graphs, arXiv preprint arXiv:2410.12298, 20244. URL https://arxiv.org/abs/2410.12298v2 .

- Sun et al. [2022] Liangtai Sun, Xingyu Chen, Lu Chen, Tianle Dai, Zichen Zhu, and Kai Yu. Meta-gui: Towards multi-modal conversational agents on mobile gui. Conference on Empirical Methods in Natural Language Processing , 2022.

- Sun et al. [2025] Lijun Sun, Yijun Yang, Qiqi Duan, Yuhui Shi, Chao Lyu, Yu-Cheng Chang, Chin-Teng Lin, and Yang Shen. Multi-agent coordination across diverse applications: A survey, arXiv preprint arXiv:2502.14743, 2025. URL https://arxiv.org/abs/2502.14743v2 .

- Sun et al. [2018] Qianru Sun, Yaoyao Liu, Tat-Seng Chua, and B. Schiele. Meta-transfer learning for few-shot learning. Computer Vision and Pattern Recognition , 2018.

- Sun et al. [2019] Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Hao Tian, Hua Wu, and Haifeng Wang. Ernie 2.0: A continual pre-training framework for language understanding. AAAI Conference on Artificial Intelligence , 2019.

- Surapaneni et al. [2025] Rao Surapaneni, Miku Jha, Michael Vakoc, and Todd Segal. Announcing the agent2agent protocol (a2a). https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ , April 2025. [Online; accessed 17-July-2025].

- Szeider [2024] Stefan Szeider. Mcp-solver: Integrating language models with constraint programming systems. arXiv preprint, 2024.

- Szelogowski [2025] Daniel Szelogowski. Engram memory encoding and retrieval: A neurocomputational perspective, arXiv preprint arXiv:2506.01659, 2025. URL https://arxiv.org/abs/2506.01659v1 .

- Taatgen et al. [2008] N. Taatgen, David Huss, D. Dickison, and John R. Anderson. The acquisition of robust and flexible cognitive skills. Journal of experimental psychology. General , 2008.

- Tack et al. [2024] Jihoon Tack, Jaehyung Kim, Eric Mitchell, Jinwoo Shin, Yee Whye Teh, and Jonathan Richard Schwarz. Online adaptation of language models with a memory of amortized contexts. Neural Information Processing Systems , 2024.

- Tai et al. [2023] Yan Tai, Weichen Fan, Zhao Zhang, Feng Zhu, Rui Zhao, and Ziwei Liu. Link-context learning for multimodal llms. Computer Vision and Pattern Recognition , 2023.

- Tajwar et al. [2025] Fahim Tajwar, Yiding Jiang, Abitha Thankaraj, Sumaita Sadia Rahman, J. Z. Kolter, Jeff Schneider, and Ruslan Salakhutdinov. Training a generally curious agent, arXiv preprint arXiv:2502.17543, 2025. URL https://arxiv.org/abs/2502.17543v3 .

- Tallam [2025] K. Tallam. From autonomous agents to integrated systems, a new paradigm: Orchestrated distributed intelligence, arXiv preprint arXiv:2503.13754, 2025. URL https://arxiv.org/abs/2503.13754v2 .

- Tan et al. [2019] A. Tan, Budhitama Subagdja, Di Wang, and Lei Meng. Self-organizing neural networks for universal learning and multimodal memory encoding. Neural Networks , 2019.

- Tan et al. [2023] Chuanyuan Tan, Yuehe Chen, Wenbiao Shao, and Wenliang Chen. Make a choice! knowledge base question answering with in-context learning, arXiv preprint arXiv:2305.13972, 2023. URL https://arxiv.org/abs/2305.13972v1 .

- Tan et al. [2024] Sijun Tan, Xiuyu Li, Shishir G. Patil, Ziyang Wu, Tianjun Zhang, Kurt Keutzer, Joseph E. Gonzalez, and Raluca A. Popa. Lloco: Learning long contexts offline. Conference on Empirical Methods in Natural Language Processing , 2024.

- Tan et al. [20242] Xiaoyu Tan, Haoyu Wang, Xihe Qiu, Yuan Cheng, Yinghui Xu, Wei Chu, and Yuan Qi. Struct-x: Enhancing large language models reasoning with structured data. arXiv preprint, 20242.

- Tan and Jiang [2023] Zhaoxuan Tan and Meng Jiang. User modeling in the era of large language models: Current research and future directions. IEEE Data Engineering Bulletin , 2023.

- Tan et al. [20243] Zhijie Tan, Xu Chu, Weiping Li, and Tong Mo. Order matters: Exploring order sensitivity in multimodal large language models, arXiv preprint arXiv:2410.16983v1, 20243. URL https://arxiv.org/abs/2410.16983v1 .

- Tancik et al. [2020] Matthew Tancik, Pratul P. Srinivasan, B. Mildenhall, Sara Fridovich-Keil, N. Raghavan, Utkarsh Singhal, R. Ramamoorthi, J. Barron, and Ren Ng. Fourier features let networks learn high frequency functions in low dimensional domains. Neural Information Processing Systems , 2020.

- Tang et al. [2025] Fei Tang, Haolei Xu, Hang Zhang, Siqi Chen, Xingyu Wu, Yongliang Shen, Wenqi Zhang, Guiyang Hou, Zeqi Tan, Yuchen Yan, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, and Yueting Zhuang. A survey on (m)llm-based gui agents, arXiv preprint arXiv:2504.13865, 2025. URL https://arxiv.org/abs/2504.13865v2 .

- Tang et al. [2023] Jiabin Tang, Yuhao Yang, Wei Wei, Lei Shi, Lixin Su, Suqi Cheng, Dawei Yin, and Chao Huang. Graphgpt: Graph instruction tuning for large language models. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 2023.

- Tang et al. [2024] Jiabin Tang, Yuhao Yang, Wei Wei, Lei Shi, Lixin Su, Suqi Cheng, Dawei Yin, and Chao Huang. Graphgpt: Graph instruction tuning for large language models. In Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval , pages 491–500, 2024.

- Tang et al. [20242] Jianheng Tang, Qifan Zhang, Yuhan Li, Nuo Chen, and Jia Li. Grapharena: Evaluating and exploring large language models on graph computation. arXiv preprint arXiv:2407.00379 , 20242.

- Tang et al. [20243] Xiangru Tang, Yiming Zong, Jason Phang, Yilun Zhao, Wangchunshu Zhou, Arman Cohan, and Mark Gerstein. Struc-bench: Are large language models good at generating complex structured tabular data? North American Chapter of the Association for Computational Linguistics , 20243.

- Tang et al. [20252] Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, Arman Cohan, and Mark Gerstein. Chemagent: Self-updating library in large language models improves chemical reasoning, arXiv preprint arXiv:2501.06590, 20252. URL https://arxiv.org/abs/2501.06590v1 .

- Tang et al. [2022] Xuemei Tang, Jun Wang, and Q. Su. Chinese word segmentation with heterogeneous graph neural network, arXiv preprint arXiv:2201.08975, 2022. URL https://arxiv.org/abs/2201.08975v1 .

- Tang et al. [20244] Yiqing Tang, Xingyuan Dai, Chengchong Zhao, Qi Cheng, and Yisheng Lv. Large language model-driven urban traffic signal control. Australian and New Zealand Control Conference , 20244.

- Tang et al. [20245] Yongjian Tang, Rakebul Hasan, and Thomas Runkler. Fsponer: Few-shot prompt optimization for named entity recognition in domain-specific scenarios. European Conference on Artificial Intelligence , 20245.

- Tang et al. [20246] Yunlong Tang, Daiki Shimada, Jing Bi, Hang Hua, and Chenliang Xu. Empowering llms with pseudo-untrimmed videos for audio-visual temporal understanding. AAAI Conference on Artificial Intelligence , 20246.

- Tao et al. [2025] Yao Tao, Yehui Tang, Yun Wang, Mingjian Zhu, Hailin Hu, and Yunhe Wang. Saliency-driven dynamic token pruning for large language models, arXiv preprint arXiv:2504.04514, 2025. URL https://arxiv.org/abs/2504.04514v2 .

- Tarasov and Shridhar [2024] Denis Tarasov and Kumar Shridhar. Distilling llms’ decomposition abilities into compact language models, arXiv preprint arXiv:2402.01812, 2024. URL https://arxiv.org/abs/2402.01812v1 .

- Taveekitworachai et al. [2025] Pittawat Taveekitworachai, Potsawee Manakul, Kasima Tharnpipitchai, and Kunat Pipatanakul. Typhoon t1: An open thai reasoning model, arXiv preprint arXiv:2502.09042, 2025. URL https://arxiv.org/abs/2502.09042v2 .

- Tay et al. [2017] Yi Tay, Anh Tuan Luu, Minh C. Phan, and S. Hui. Multi-task neural network for non-discrete attribute prediction in knowledge graphs. International Conference on Information and Knowledge Management , 2017.

- Team [2025] 36Kr Editorial Team. The future of ai: From parameter scaling to context scaling. Online, 2025. URL https://36kr.com/p/3337269379328264 . Chinese business and technology media publication discussing context scaling in large language models.

- Tian et al. [2024] Junfeng Tian, Da Zheng, Yang Cheng, Rui Wang, Colin Zhang, and Debing Zhang. Untie the knots: An efficient data augmentation strategy for long-context pre-training in language models, arXiv preprint arXiv:2409.04774, 2024. URL https://arxiv.org/abs/2409.04774v1 .

- Tian et al. [2025] S Tian, R Wang, H Guo, P Wu, Y Dong, and X Wang…. Ego-r1: Chain-of-tool-thought for ultra-long egocentric video reasoning. 2025. URL https://arxiv.org/abs/2506.13654 .

- Tian et al. [20252] Shulin Tian, Ruiqi Wang, Hongming Guo, Penghao Wu, Yuhao Dong, Xiuying Wang, Jingkang Yang, Hao Zhang, Hongyuan Zhu, and Ziwei Liu. Ego-r1: Chain-of-tool-thought for ultra-long egocentric video reasoning. arXiv preprint, 20252.

- Tinati et al. [2015] Ramine Tinati, Xin Wang, Ian C. Brown, T. Tiropanis, and W. Hall. A streaming real-time web observatory architecture for monitoring the health of social machines. The Web Conference , 2015.

- Tirumala et al. [2022] Kushal Tirumala, Aram H. Markosyan, Luke Zettlemoyer, and Armen Aghajanyan. Memorization without overfitting: Analyzing the training dynamics of large language models. Neural Information Processing Systems , 2022.

- Tomkou et al. [2025] Despina Tomkou, George Fatouros, Andreas Andreou, Georgios Makridis, F. Liarokapis, Dimitrios Dardanis, Athanasios Kiourtis, John Soldatos, and D. Kyriazis. Bridging industrial expertise and xr with llm-powered conversational agents, arXiv preprint arXiv:2504.05527, 2025. URL https://arxiv.org/abs/2504.05527v1 .

- Toro et al. [2023] Sabrina Toro, A. V. Anagnostopoulos, Sue Bello, Kai Blumberg, Rhiannon Cameron, Leigh Carmody, A. Diehl, Damion M. Dooley, William Duncan, P. Fey, Pascale Gaudet, Nomi L. Harris, marcin p. joachimiak, Leila Kiani, Tiago Lubiana, M. Munoz-Torres, Shawn T. O’Neil, David Osumi-Sutherland, Aleix Puig, Justin Reese, L. Reiser, Sofia M C Robb, Troy Ruemping, James Seager, Eric Sid, Ray Stefancsik, Magalie Weber, Valerie Wood, M. Haendel, and Christopher J. Mungall. Dynamic retrieval augmented generation of ontologies using artificial intelligence (dragon-ai). Journal of Biomedical Semantics , 2023.

- Torre et al. [2023] Fernanda M De La Torre, Cathy Mengying Fang, Han Huang, Andrzej Banburski-Fahey, Judith Amores Fernandez, and Jaron Lanier. Llmr: Real-time prompting of interactive worlds using large language models. International Conference on Human Factors in Computing Systems , 2023.

- Toshevska and Gievska [2025] Martina Toshevska and Sonja Gievska. Llm-based text style transfer: Have we taken a step forward? IEEE Access , 2025.

- Trad and Chehab [2024] Fouad Trad and Ali Chehab. Evaluating the efficacy of prompt-engineered large multimodal models versus fine-tuned vision transformers in image-based security applications. ACM Transactions on Intelligent Systems and Technology , 2024.

- Tran et al. [2025] Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O’Sullivan, and Hoang D. Nguyen. Multi-agent collaboration mechanisms: A survey of llms, arXiv preprint arXiv:2501.06322, 2025. URL https://arxiv.org/abs/2501.06322v1 .

- Triedman et al. [2025] Harold Triedman, Rishi Jha, and Vitaly Shmatikov. Multi-agent systems execute arbitrary malicious code, arXiv preprint arXiv:2503.12188, 2025. URL https://arxiv.org/abs/2503.12188v1 .

- Trivedi et al. [2024] H. Trivedi, Tushar Khot, Mareike Hartmann, R. Manku, Vinty Dong, Edward Li, Shashank Gupta, Ashish Sabharwal, and Niranjan Balasubramanian. Appworld: A controllable world of apps and people for benchmarking interactive coding agents. Annual Meeting of the Association for Computational Linguistics , 2024.

- Tsai et al. [2024] Yun-Da Tsai, Ting-Yu Yen, Pei-Fu Guo, Zhe-Yan Li, and Shou-De Lin. Text-centric alignment for multi-modality learning, arXiv preprint arXiv:2402.08086v2, 2024. URL https://arxiv.org/abs/2402.08086v2 .

- Tu et al. [2025] Tao Tu, M. Schaekermann, Anil Palepu, Khaled Saab, Jan Freyberg, Ryutaro Tanno, Amy Wang, Brenna Li, Mohamed Amin, Yong Cheng, Elahe Vedadi, Nenad Tomašev, Shekoofeh Azizi, Karan Singhal, Le Hou, Albert Webson, Kavita Kulkarni, S. Mahdavi, Christopher Semturs, Juraj Gottweis, Joelle Barral, Katherine Chou, Greg S. Corrado, Yossi Matias, A. Karthikesalingam, and Vivek Natarajan. Towards conversational diagnostic artificial intelligence. Nature , 2025.

- Tulchinskii et al. [2024] Eduard Tulchinskii, Laida Kushnareva, Kristian Kuznetsov, Anastasia Voznyuk, Andrei Andriiainen, Irina Piontkovskaya, Evgeny Burnaev, and Serguei Barannikov. Listening to the wise few: Select-and-copy attention heads for multiple-choice qa, arXiv preprint arXiv:2410.02343, 2024. URL https://arxiv.org/abs/2410.02343v1 .

- Udeshi et al. [2025] Meet Udeshi, Minghao Shao, Haoran Xi, Nanda Rani, Kimberly Milner, Venkata Sai Charan Putrevu, Brendan Dolan-Gavitt, S. K. Shukla, P. Krishnamurthy, F. Khorrami, Ramesh Karri, and Muhammad Shafique. D-cipher: Dynamic collaborative intelligent multi-agent system with planner and heterogeneous executors for offensive security. arXiv preprint, 2025.

- Ursino et al. [2022] M. Ursino, Nicole Cesaretti, and G. Pirazzini. A model of working memory for encoding multiple items and ordered sequences exploiting the theta-gamma code. Cognitive Neurodynamics , 2022.

- Uytsel et al. [2001] D. H. V. Uytsel, Filip Van Aelten, and Dirk Van Compernolle. A structured language model based on context-sensitive probabilistic left-corner parsing. North American Chapter of the Association for Computational Linguistics , 2001.

- Vaghefi et al. [2025] Saeid Ario Vaghefi, Aymane Hachcham, Veronica Grasso, Jiska Manicus, Nakiete Msemo, C. Senni, and Markus Leippold. Ai for climate finance: Agentic retrieval and multi-step reasoning for early warning system investments, arXiv preprint arXiv:2504.05104, 2025. URL https://arxiv.org/abs/2504.05104v2 .

- Vaithilingam et al. [2022] Priyan Vaithilingam, Tianyi Zhang, and Elena L. Glassman. Expectation vs. experience: Evaluating the usability of code generation tools powered by large language models. CHI Extended Abstracts , 2022.

- Van et al. [2024] Phuc Phan Van, Dat Nguyen Minh, An Dinh Ngoc, and Huy-Phan Thanh. Rx strategist: Prescription verification using llm agents system, arXiv preprint arXiv:2409.03440, 2024. URL https://arxiv.org/abs/2409.03440v1 .

- Vaswani et al. [2017] Ashish Vaswani, Noam M. Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and I. Polosukhin. Attention is all you need. Neural Information Processing Systems , 2017.

- Velásquez-Henao et al. [2023] J. D. Velásquez-Henao, Carlos Jaime Franco-Cardona, and Lorena Cadavid-Higuita. Prompt engineering: a methodology for optimizing interactions with ai-language models in the field of engineering. DYNA , 2023.

- Verma et al. [2024] Gaurav Verma, Rachneet Kaur, Nishan Srishankar, Zhen Zeng, T. Balch, and Manuela Veloso. Adaptagent: Adapting multimodal web agents with few-shot learning from human demonstrations, arXiv preprint arXiv:2411.13451, 2024. URL https://arxiv.org/abs/2411.13451v1 .

- Vertsel and Rumiantsau [2024] Aliaksei Vertsel and Mikhail Rumiantsau. Hybrid llm/rule-based approaches to business insights generation from structured data, arXiv preprint arXiv:2404.15604, 2024. URL https://arxiv.org/abs/2404.15604v1 .

- Vijayan [2023] Aishwarya Vijayan. A prompt engineering approach for structured data extraction from unstructured text using conversational llms. International Conference on Advances in Computing and Artificial Intelligence , 2023.

- Vladika et al. [2023] Juraj Vladika, Alexander Fichtl, and Florian Matthes. Diversifying knowledge enhancement of biomedical language models using adapter modules and knowledge graphs. International Conference on Agents and Artificial Intelligence , 2023.

- Vo [2024] James Vo. Sparseaccelerate: Efficient long-context inference for mid-range gpus, arXiv preprint arXiv:2412.06198, 2024. URL https://arxiv.org/abs/2412.06198v1 .

- vSkrlj et al. [2025] Blavz vSkrlj, Boshko Koloski, S. Pollak, and Nada Lavravc. From symbolic to neural and back: Exploring knowledge graph-large language model synergies. arXiv preprint, 2025.

- Völker et al. [2024] Tom Völker, Jan Pfister, Tobias Koopmann, and Andreas Hotho. From chat to publication management: Organizing your related work using bibsonomy & llms. Conference on Human Information Interaction and Retrieval , 2024.

- Walton [2020] D. Walton. Using argumentation schemes to find motives and intentions of a rational agent. Argument Comput. , 2020.

- Wan et al. [2024] Hanlong Wan, Jian Zhang, Yan Chen, Weili Xu, and Fan Feng. Generative ai application for building industry. Building Simulation , 2024.

- Wan and Mei [2025] Jun Wan and Lingrui Mei. Large language models as computable approximations to solomonoff induction, arXiv preprint arXiv:2505.15784, 2025. URL https://arxiv.org/abs/2505.15784 .

- Wan and Ma [2025] Luanbo Wan and Weizhi Ma. Storybench: A dynamic benchmark for evaluating long-term memory with multi turns, arXiv preprint arXiv:2506.13356, 2025. URL https://arxiv.org/abs/2506.13356v1 .

- Wang et al. [2021] Bernie Wang, Si ting Xu, K. Keutzer, Yang Gao, and Bichen Wu. Improving context-based meta-reinforcement learning with self-supervised trajectory contrastive learning, arXiv preprint arXiv:2103.06386, 2021. URL https://arxiv.org/abs/2103.06386v1 .

- Wang et al. [2025] Bing Wang, Xinnian Liang, Jian Yang, Hui Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, and Zhoujun Li. Scm: Enhancing large language model with self-controlled memory framework, arXiv preprint arXiv:2304.13343, 2025. URL https://arxiv.org/abs/2304.13343 .

- Wang et al. [2024] Cangqing Wang, Yutian Yang, Ruisi Li, Dan Sun, Ruicong Cai, Yuzhu Zhang, and Chengqian Fu. Adapting llms for efficient context processing through soft prompt compression. Proceedings of the International Conference on Modeling, Natural Language Processing and Machine Learning , 2024.

- Wang et al. [2023] Chaozheng Wang, Yuanhang Yang, Cuiyun Gao, Yun Peng, Hongyu Zhang, and Michael R. Lyu. Prompt tuning in code intelligence: An experimental evaluation. IEEE Transactions on Software Engineering , 2023.

- Wang et al. [20232] Dongsheng Wang, Zhiqiang Ma, Armineh Nourbakhsh, Kang Gu, and Sameena Shah. Docgraphlm: Documental graph language model for information extraction. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 20232.

- Wang et al. [20242] Fan Wang, Chuan Lin, Yang Cao, and Yu Kang. Benchmarking general purpose in-context learning, arXiv preprint arXiv:2405.17234, 20242. URL https://arxiv.org/abs/2405.17234v6 .

- Wang et al. [20233] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models, arXiv preprint arXiv:2305.16291, 20233. URL https://arxiv.org/abs/2305.16291 .

- Wang et al. [20243] Guoqing Wang, Zeyu Sun, Zhihao Gong, Sixiang Ye, Yizhou Chen, Yifan Zhao, Qing-Lin Liang, and Dan Hao. Do advanced language models eliminate the need for prompt engineering in software engineering?, arXiv preprint arXiv:2411.02093, 20243. URL https://arxiv.org/abs/2411.02093v1 .

- Wang et al. [20244] Hanlin Wang, Zhan Tong, Kecheng Zheng, Yujun Shen, and Limin Wang. Contextual ad narration with interleaved multimodal sequence. Computer Vision and Pattern Recognition , 20244.

- Wang et al. [2020] Hanrui Wang, Zhekai Zhang, and Song Han. Spatten: Efficient sparse attention architecture with cascade token and head pruning. International Symposium on High-Performance Computer Architecture , 2020.

- Wang et al. [20252] Haochen Wang, Xiangtai Li, Zilong Huang, Anran Wang, Jiacong Wang, Tao Zhang, Jiani Zheng, Sule Bai, Zijian Kang, Jiashi Feng, et al. Traceable evidence enhanced visual grounded reasoning: Evaluation and methodology. arXiv preprint arXiv:2507.07999 , 20252.

- Wang et al. [20234] Haochun Wang, Chi Liu, Nuwa Xi, Zewen Qiang, Sendong Zhao, Bing Qin, and Ting Liu. Huatuo: Tuning llama model with chinese medical knowledge, arXiv preprint arXiv:2304.06975, 20234. URL https://arxiv.org/abs/2304.06975 .

- Wang et al. [20253] Haoyu Wang, Tong Teng, Tianyu Guo, An Xiao, Duyu Tang, Hanting Chen, and Yunhe Wang. Unshackling context length: An efficient selective attention approach through query-key compression, arXiv preprint arXiv:2502.14477, 20253. URL https://arxiv.org/abs/2502.14477v1 .

- Wang et al. [20235] Heng Wang, Shangbin Feng, Tianxing He, Zhaoxuan Tan, Xiaochuang Han, and Yulia Tsvetkov. Can language models solve graph problems in natural language? Neural Information Processing Systems , 20235.

- Wang et al. [20245] Hengyi Wang, Haizhou Shi, Shiwei Tan, Weiyi Qin, Wenyuan Wang, Tunyu Zhang, A. Nambi, T. Ganu, and Hao Wang. Multimodal needle in a haystack: Benchmarking long-context capability of multimodal large language models. North American Chapter of the Association for Computational Linguistics , 20245.

- Wang et al. [20254] Hongru Wang, Cheng Qian, Manling Li, Jiahao Qiu, Boyang Xue, Mengdi Wang, Heng Ji, and Kam-Fai Wong. Toward a theory of agents as tool-use decision-makers, arXiv preprint arXiv:2506.00886, 20254. URL https://arxiv.org/abs/2506.00886v1 .

- Wang [2025] Jingjin Wang. Proprag: Guiding retrieval with beam search over proposition paths, arXiv preprint arXiv:2504.18070, 2025. URL https://arxiv.org/abs/2504.18070v1 .

- Wang et al. [20246] Jingyu Wang, Lu Zhang, Xueqing Li, Huazhong Yang, and Yongpan Liu. Ulseq-ta: Ultra-long sequence attention fusion transformer accelerator supporting grouped sparse softmax and dual-path sparse layernorm. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems , 20246.

- Wang et al. [20247] Jize Wang, Zerun Ma, Yining Li, Songyang Zhang, Cailian Chen, Kai Chen, and Xinyi Le. Gta: A benchmark for general tool agents. Neural Information Processing Systems , 20247.

- Wang et al. [20236] Lei Wang, Chengbang Ma, Xueyang Feng, Zeyu Zhang, Hao ran Yang, Jingsen Zhang, Zhi-Yang Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, and Ji rong Wen. A survey on large language model based autonomous agents. Frontiers Comput. Sci. , 20236.

- Wang et al. [20237] Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim. Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning by large language models. Annual Meeting of the Association for Computational Linguistics , 20237.

- Wang et al. [20238] Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Ruihua Song, Wayne Xin Zhao, et al. When large language model based agent meets user behavior analysis: A novel user simulation paradigm. 20238.

- Wang [20252] Libo Wang. Towards humanoid robot autonomy: A dynamic architecture integrating continuous thought machines (ctm) and model context protocol (mcp), arXiv preprint arXiv:2505.19339, 20252. URL https://arxiv.org/abs/2505.19339v1 .

- Wang et al. [20239] Liya Wang, Jason Chou, Xin Zhou, A. Tien, and Diane M. Baumgartner. Aviationgpt: A large language model for the aviation domain, arXiv preprint arXiv:2311.17686, 20239. URL https://arxiv.org/abs/2311.17686v1 .

- Wang et al. [20202] Liyuan Wang, Bo Lei, Qian Li, Hang Su, Jun Zhu, and Yi Zhong. Triple-memory networks: A brain-inspired method for continual learning. IEEE Transactions on Neural Networks and Learning Systems , 20202.

- Wang et al. [20255] Lu Wang, Fangkai Yang, Chaoyun Zhang, Junting Lu, Jiaxu Qian, Shilin He, Pu Zhao, Bo Qiao, Ray Huang, Si Qin, Qisheng Su, Jiayi Ye, Yudi Zhang, Jian-Guang Lou, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, and Qi Zhang. Large action models: From inception to implementation, arXiv preprint arXiv:2412.10047, 20255. URL https://arxiv.org/abs/2412.10047 .

- Wang et al. [20256] Peijie Wang, Zhong-Zhi Li, Fei Yin, Xin Yang, Dekang Ran, and Cheng-Lin Liu. Mv-math: Evaluating multimodal math reasoning in multi-visual contexts. 20256.

- Wang et al. [202310] Qineng Wang, Zihao Wang, Ying Su, and Yangqiu Song. On the discussion of large language models: Symmetry of agents and interplay with prompts, arXiv preprint arXiv:2311.07076, 202310. URL https://arxiv.org/abs/2311.07076v1 .

- Wang et al. [20248] Rongzheng Wang, Shuang Liang, Qizhi Chen, Jiasheng Zhang, and Ke Qin. Graphtool-instruction: Revolutionizing graph reasoning in llms through decomposed subtask instruction. Knowledge Discovery and Data Mining , 20248.

- Wang et al. [20249] Shengnan Wang, Youhui Bai, Lin Zhang, Pingyi Zhou, Shixiong Zhao, Gong Zhang, Sen Wang, Renhai Chen, Hua Xu, and Hongwei Sun. Xl3m: A training-free framework for llm length extension based on segment-wise inference, arXiv preprint arXiv:2405.17755, 20249. URL https://arxiv.org/abs/2405.17755v1 .

- Wang et al. [202311] Song Wang, Yaochen Zhu, Haochen Liu, Zaiyi Zheng, Chen Chen, and Jundong Li. Knowledge editing for large language models: A survey. ACM Computing Surveys , 202311.

- Wang et al. [20257] Song Wang, Junhong Lin, Xiaojie Guo, Julian Shun, Jundong Li, and Yada Zhu. Reasoning of large language models over knowledge graphs with super-relations. International Conference on Learning Representations , 20257.

- Wang et al. [202410] Tiannan Wang, Jiamin Chen, Qingrui Jia, Shuai Wang, Ruoyu Fang, Huilin Wang, Zhaowei Gao, Chunzhao Xie, Chuou Xu, Jihong Dai, Yibin Liu, Jialong Wu, Shengwei Ding, Long Li, Zhiwei Huang, Xinle Deng, Teng Yu, Gangan Ma, Han Xiao, Z. Chen, Danjun Xiang, Yunxia Wang, Yuanyuan Zhu, Yichen Xiao, Jing Wang, Yiru Wang, Siran Ding, Jiayang Huang, Jiayi Xu, Yilihamujiang Tayier, Zhenyu Hu, Yuan Gao, Chengfeng Zheng, Yu-Jie Ye, Yihan Li, Lei Wan, Xinyue Jiang, Yujie Wang, Siyuan Cheng, Zhule Song, Xiangru Tang, Xiaohua Xu, Ningyu Zhang, Huajun Chen, Y. Jiang, and Wangchunshu Zhou. Weaver: Foundation models for creative writing, arXiv preprint arXiv:2401.17268, 202410. URL https://arxiv.org/abs/2401.17268v1 .

- Wang et al. [2022] Weizhi Wang, Li Dong, Hao Cheng, Haoyu Song, Xiaodong Liu, Xifeng Yan, Jianfeng Gao, and Furu Wei. Visually-augmented language modeling. International Conference on Learning Representations , 2022.

- Wang et al. [20212] Xiang Wang, Tinglin Huang, Dingxian Wang, Yancheng Yuan, Zhenguang Liu, Xiangnan He, and Tat seng Chua. Learning intents behind interactions with knowledge graph for recommendation. The Web Conference , 20212.

- Wang et al. [202312] Xiao Wang, Isaac Lyngaas, A. Tsaris, Peng Chen, Sajal Dash, Mayanka Chandra Shekar, Tao Luo, Hong-Jun Yoon, M. Wahib, and J. Gounley. Ultra-long sequence distributed transformer, arXiv preprint arXiv:2311.02382, 202312. URL https://arxiv.org/abs/2311.02382v2 .

- Wang et al. [202411] Xiaohan Wang, Yuhui Zhang, Orr Zohar, and S. Yeung-Levy. Videoagent: Long-form video understanding with large language model as agent. European Conference on Computer Vision , 202411.

- Wang et al. [20258] Xiaolong Wang, Zhaolu Kang, Wangyuxuan Zhai, Xinyue Lou, Yunghwei Lai, Ziyue Wang, Yawen Wang, Kaiyu Huang, Yile Wang, Peng Li, and Yang Liu. Mucar: Benchmarking multilingual cross-modal ambiguity resolution for multimodal large language models, arXiv preprint arXiv:2506.17046v1, 20258. URL https://arxiv.org/abs/2506.17046v1 .

- Wang et al. [20259] Xiaoqiang Wang, Suyuchen Wang, Yun Zhu, and Bang Liu. R3mem: Bridging memory retention and retrieval via reversible compression. arXiv preprint, 20259.

- Wang et al. [2018] Xiaoyang Wang, Pavan Kapanipathi, Ryan Musa, Mo Yu, Kartik Talamadupula, I. Abdelaziz, Maria Chang, Achille Fokoue, B. Makni, Nicholas Mattei, and M. Witbrock. Improving natural language inference using external knowledge in the science questions domain. AAAI Conference on Artificial Intelligence , 2018.

- Wang et al. [202412] Xindi Wang, Mahsa Salmani, Parsa Omidi, Xiangyu Ren, Mehdi Rezagholizadeh, and A. Eshaghi. Beyond the limits: A survey of techniques to extend the context length in large language models. International Joint Conference on Artificial Intelligence , 202412.

- Wang et al. [202413] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. Executable code actions elicit better llm agents. International Conference on Machine Learning , 202413.

- Wang et al. [20222] Xuezhi Wang, Jason Wei, D. Schuurmans, Quoc Le, Ed H. Chi, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. International Conference on Learning Representations , 20222.

- Wang et al. [202414] Yancheng Wang, Ziyan Jiang, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, and Yingzhen Yang. Recmind: Large language model powered agent for recommendation, arXiv preprint arXiv:2308.14296, 202414. URL https://arxiv.org/abs/2308.14296 .

- Wang [2024] Yani Wang. Application of large language models based on knowledge graphs in question-answering systems: A review. Applied and Computational Engineering , 2024.

- Wang et al. [202415] Yanlin Wang, Wanjun Zhong, Yanxian Huang, Ensheng Shi, Min Yang, Jiachi Chen, Hui Li, Yuchi Ma, Qianxiang Wang, and Zibin Zheng. Agents in software engineering: Survey, landscape, and vision, arXiv preprint arXiv:2409.09030, 202415. URL https://arxiv.org/abs/2409.09030v2 .

- Wang and Xu [2024] Yaqi Wang and Haipei Xu. Srsa: A cost-efficient strategy-router search agent for real-world human-machine interactions. 2024 IEEE International Conference on Data Mining Workshops (ICDMW) , 2024.

- Wang et al. [202510] Yi Wang, Xinhao Li, Ziang Yan, Yinan He, Jiashuo Yu, Xiangyun Zeng, Chenting Wang, Changlian Ma, Haian Huang, Jianfei Gao, Min Dou, Kaiming Chen, Wenhai Wang, Yu Qiao, Yali Wang, and Limin Wang. Internvideo2.5: Empowering video mllms with long and rich context modeling. arXiv preprint, 202510.

- Wang et al. [202313] Yiming Wang, Zhuosheng Zhang, and Rui Wang. Element-aware summarization with large language models: Expert-aligned evaluation and chain-of-thought method. Annual Meeting of the Association for Computational Linguistics , 202313.

- Wang and Atanasova [2025] Yingming Wang and Pepa Atanasova. Self-critique and refinement for faithful natural language explanations, arXiv preprint arXiv:2505.22823, 2025. URL https://arxiv.org/abs/2505.22823v1 .

- Wang et al. [20213] Yiwei Wang, Wei Wang, Yuxuan Liang, Yujun Cai, and Bryan Hooi. Mixup for node and graph classification. In Proceedings of the Web Conference 2021 , pages 3663–3674, 20213.

- Wang et al. [202416] Yu Wang, Yifan Gao, Xiusi Chen, Haoming Jiang, Shiyang Li, Jingfeng Yang, Qingyu Yin, Zheng Li, Xian Li, Bing Yin, Jingbo Shang, and Julian McAuley. Memoryllm: Towards self-updatable large language models, arXiv preprint arXiv:2402.04624, 202416. URL https://arxiv.org/abs/2402.04624 .

- Wang et al. [202511] Yu Wang, Dmitry Krotov, Yuanzhe Hu, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogério Feris, and Zexue He. M+: Extending memoryllm with scalable long-term memory. arXiv preprint, 202511.

- Wang et al. [202417] Yubin Wang, Xinyang Jiang, De Cheng, Wenli Sun, Dongsheng Li, and Cairong Zhao. Hpt++: Hierarchically prompting vision-language models with multi-granularity knowledge generation and improved structure modeling. arXiv preprint, 202417.

- Wang et al. [202418] Yujie Wang, Shiju Wang, Shenhan Zhu, Fangcheng Fu, Xinyi Liu, Xuefeng Xiao, Huixia Li, Jiashi Li, Faming Wu, and Bin Cui. Flexsp: Accelerating large language model training via flexible sequence parallelism. International Conference on Architectural Support for Programming Languages and Operating Systems , 202418.

- Wang et al. [202419] Yuntao Wang, Yanghe Pan, Zhou Su, Yi Deng, Quan Zhao, L. Du, Tom H. Luan, Jiawen Kang, and D. Niyato. Large model based agents: State-of-the-art, cooperation paradigms, security and privacy, and future trends. IEEE Communications Surveys & Tutorials , 202419.

- Wang et al. [202512] Yuntao Wang, Shaolong Guo, Yanghe Pan, Zhou Su, Fahao Chen, Tom H. Luan, Peng Li, Jiawen Kang, and Dusit Niyato. Internet of agents: Fundamentals, applications, and challenges, arXiv preprint arXiv:2505.07176, 202512. URL https://arxiv.org/abs/2505.07176v1 .

- Wang et al. [202513] Yuxiang Wang, Xinnan Dai, Wenqi Fan, and Yao Ma. Exploring graph tasks with pure llms: A comprehensive benchmark and investigation, arXiv preprint arXiv:2502.18771v1, 202513. URL https://arxiv.org/abs/2502.18771v1 .

- Wang et al. [202420] Z. Wang, King Zhu, Chunpu Xu, Wangchunshu Zhou, Jiaheng Liu, Yibo Zhang, Jiashuo Wang, Ning Shi, Siyu Li, Yizhi Li, Haoran Que, Zhaoxiang Zhang, Yuanxing Zhang, Ge Zhang, Ke Xu, Jie Fu, and Wenhao Huang. Mio: A foundation model on multimodal tokens, arXiv preprint arXiv:2409.17692v3, 202420. URL https://arxiv.org/abs/2409.17692v3 .

- Wang et al. [202421] Zheng Wang, Shu Xian Teo, Jieer Ouyang, Yongjun Xu, and Wei Shi. M-rag: Reinforcing large language model performance through retrieval-augmented generation with multiple partitions. Annual Meeting of the Association for Computational Linguistics , 202421.

- Wang et al. [202422] Zhiruo Wang, Zhoujun Cheng, Hao Zhu, Daniel Fried, and Graham Neubig. What are tools anyway? a survey from the language model perspective, arXiv preprint arXiv:2403.15452, 202422. URL https://arxiv.org/abs/2403.15452v1 .

- Wang et al. [202423] Ziyang Wang, Jianzhou You, Haining Wang, Tianwei Yuan, Shichao Lv, Yang Wang, and Limin Sun. Honeygpt: Breaking the trilemma in terminal honeypots with large language model, arXiv preprint arXiv:2406.01882, 202423. URL https://arxiv.org/abs/2406.01882v2 .

- Wang et al. [202424] Ziyue Wang, Chi Chen, Yiqi Zhu, Fuwen Luo, Peng Li, Ming Yan, Ji Zhang, Fei Huang, Maosong Sun, and Yang Liu. Browse and concentrate: Comprehending multimodal content via prior-llm context fusion. Annual Meeting of the Association for Computational Linguistics , 202424.

- Wang et al. [202425] Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig. Agent workflow memory, arXiv preprint arXiv:2409.07429, 202425. URL https://arxiv.org/abs/2409.07429 .

- Weber [2024] Irene Weber. Large language models are pattern matchers: Editing semi-structured and structured documents with chatgpt. AKWI Jahrestagung , 2024.

- Wei et al. [2023] Hui Wei, Chenyue Feng, and Jianning Zhang. Modeling of memory mechanisms in cerebral cortex and simulation of storage performance, arXiv preprint arXiv:2401.00381, 2023. URL https://arxiv.org/abs/2401.00381v2 .

- Wei et al. [2022] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed H. Chi, F. Xia, Quoc Le, and Denny Zhou. Chain of thought prompting elicits reasoning in large language models. Neural Information Processing Systems , 2022.

- Wei et al. [20232] Jerry W. Wei, Le Hou, Andrew Kyle Lampinen, Xiangning Chen, Da Huang, Yi Tay, Xinyun Chen, Yifeng Lu, Denny Zhou, Tengyu Ma, and Quoc V. Le. Symbol tuning improves in-context learning in language models. Conference on Empirical Methods in Natural Language Processing , 20232.

- Wei et al. [20222] Shaopeng Wei, Yu Zhao, Xingyan Chen, Qing Li, Fuzhen Zhuang, Ji Liu, and Gang Kou. Graph learning and its advancements on large language models: A holistic survey, arXiv preprint arXiv:2212.08966, 20222. URL https://arxiv.org/abs/2212.08966v5 .

- Wei et al. [2025] Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, and Lihong Li. Webagent-r1: Training web agents via end-to-end multi-turn reinforcement learning. arXiv preprint, 2025.

- Wei et al. [2024] Zhiyuan Wei, Jing Sun, Zijian Zhang, and Xianhao Zhang. Llm-smartaudit: Advanced smart contract vulnerability detection. arXiv preprint, 2024.

- Westhäußer et al. [2025] Rebecca Westhäußer, Frederik Berenz, Wolfgang Minker, and Sebastian Zepf. Caim: Development and evaluation of a cognitive ai memory framework for long-term interaction with intelligent agents. arXiv preprint, 2025.

- Weyns and Oquendo [2019] Danny Weyns and F. Oquendo. An architectural style for self-adaptive multi-agent systems, arXiv preprint arXiv:1909.03475, 2019. URL https://arxiv.org/abs/1909.03475v1 .

- Wijmans et al. [2024] Erik Wijmans, Brody Huval, Alexander Hertzberg, V. Koltun, and Philipp Krähenbühl. Cut your losses in large-vocabulary language models. International Conference on Learning Representations , 2024.

- Wikipedia contributors [2025] Wikipedia contributors. Agent communications language — Wikipedia, the free encyclopedia, 2025. URL https://en.wikipedia.org/wiki/Agent_Communications_Language . [Online; accessed 17-July-2025].

- Winata et al. [2023] Genta Indra Winata, Lingjue Xie, Karthik Radhakrishnan, Shijie Wu, Xisen Jin, Pengxiang Cheng, Mayank Kulkarni, and Daniel Preotiuc-Pietro. Overcoming catastrophic forgetting in massively multilingual continual learning, arXiv preprint arXiv:2305.16252, 2023. URL https://arxiv.org/abs/2305.16252 .

- woo Kwak et al. [2025] Beong woo Kwak, Minju Kim, Dongha Lim, Hyungjoo Chae, Dongjin Kang, Sunghwan Kim, Dongil Yang, and Jinyoung Yeo. Toolhaystack: Stress-testing tool-augmented language models in realistic long-term interactions, arXiv preprint arXiv:2505.23662, 2025. URL https://arxiv.org/abs/2505.23662v1 .

- Wu et al. [2024] Biao Wu, Yanda Li, Meng Fang, Zirui Song, Zhiwei Zhang, Yunchao Wei, and Ling Chen. Foundations and recent trends in multimodal mobile agents: A survey, arXiv preprint arXiv:2411.02006, 2024. URL https://arxiv.org/abs/2411.02006v2 .

- Wu et al. [20242] Cheng-Kuang Wu, Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, and Hung yi Lee. Streambench: Towards benchmarking continuous improvement of language agents. Neural Information Processing Systems , 20242.

- Wu et al. [2025] Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou. Webdancer: Towards autonomous information seeking agency, arXiv preprint arXiv:2505.22648, 2025. URL https://arxiv.org/abs/2505.22648v2 .

- Wu et al. [20252] Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Deyu Zhou, Pengjun Xie, and Fei Huang. Webwalker: Benchmarking llms in web traversal, arXiv preprint arXiv:2501.07572, 20252. URL https://arxiv.org/abs/2501.07572v2 .

- Wu et al. [20253] Junde Wu, Jiayuan Zhu, and Yuyuan Liu. Agentic reasoning: Reasoning llms with tools for the deep research, arXiv preprint arXiv:2502.04644, 20253. URL https://arxiv.org/abs/2502.04644v1 .

- Wu et al. [2023] Likang Wu, Zhilan Zheng, Zhaopeng Qiu, Hao Wang, Hongchao Gu, Tingjia Shen, Chuan Qin, Chen Zhu, Hengshu Zhu, Qi Liu, Hui Xiong, and Enhong Chen. A survey on large language models for recommendation. World wide web (Bussum) , 2023.

- Wu et al. [20254] M Wu, J Yang, J Jiang, M Li, K Yan, and H Yu…. Vtool-r1: Vlms learn to think with images via reinforcement learning on multimodal tool use. 20254. URL https://arxiv.org/abs/2505.19255 .

- Wu et al. [20243] Mengsong Wu, Tong Zhu, Han Han, Chuanyuan Tan, Xiang Zhang, and Wenliang Chen. Seal-tools: Self-instruct tool learning dataset for agent tuning and detailed benchmark. Natural Language Processing and Chinese Computing , 20243.

- Wu et al. [20255] Panlong Wu, Ting Wang, Yifei Zhong, Haoqi Zhang, Zitong Wang, and Fangxin Wang. Deepform: Reasoning large language model for communication system formulation, arXiv preprint arXiv:2506.08551, 20255. URL https://arxiv.org/abs/2506.08551v2 .

- Wu et al. [20232] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, A. Awadallah, Ryen W. White, Doug Burger, and Chi Wang. Autogen: Enabling next-gen llm applications via multi-agent conversation, arXiv preprint arXiv:2308.08155, 20232. URL https://arxiv.org/abs/2308.08155v2 .

- Wu et al. [20256] Ruofan Wu, Youngwon Lee, Fan Shu, Danmei Xu, Seung won Hwang, Zhewei Yao, Yuxiong He, and Feng Yan. Composerag: A modular and composable rag for corpus-grounded multi-hop question answering, arXiv preprint arXiv:2506.00232, 20256. URL https://arxiv.org/abs/2506.00232v1 .

- Wu et al. [20244] Shangyu Wu, Ying Xiong, Yufei Cui, Haolun Wu, Can Chen, Ye Yuan, Lianming Huang, Xue Liu, Tei-Wei Kuo, Nan Guan, and C. Xue. Retrieval-augmented generation for natural language processing: A survey, arXiv preprint arXiv:2407.13193, 20244. URL https://arxiv.org/abs/2407.13193v3 .

- Wu et al. [20245] Shirley Wu, Shiyu Zhao, Qian Huang, Kexin Huang, Michihiro Yasunaga, V. Ioannidis, Karthik Subbian, J. Leskovec, and James Zou. Avatar: Optimizing llm agents for tool usage via contrastive reasoning. Neural Information Processing Systems , 20245.

- Wu et al. [20233] Suhang Wu, Minlong Peng, Yue Chen, Jinsong Su, and Mingming Sun. Eva-kellm: A new benchmark for evaluating knowledge editing of llms, arXiv preprint arXiv:2308.09954, 20233. URL https://arxiv.org/abs/2308.09954 .

- Wu et al. [20246] Tianhao Wu, Weizhe Yuan, Olga Golovneva, Jing Xu, Yuandong Tian, Jiantao Jiao, Jason E Weston, and Sainbayar Sukhbaatar. Meta-rewarding language models: Self-improving alignment with llm-as-a-meta-judge. arXiv preprint, 20246.

- Wu et al. [20257] Tong Wu, Chong Xiang, Jiachen T. Wang, and Prateek Mittal. Effectively controlling reasoning models through thinking intervention, arXiv preprint arXiv:2503.24370, 20257. URL https://arxiv.org/abs/2503.24370v3 .

- Wu and Varshney [2023] Xinbo Wu and L. Varshney. A meta-learning perspective on transformers for causal language modeling. Annual Meeting of the Association for Computational Linguistics , 2023.

- Wu and Tsioutsiouliklis [2024] Xue Wu and Kostas Tsioutsiouliklis. Thinking with knowledge graphs: Enhancing llm reasoning through structured data, arXiv preprint arXiv:2412.10654, 2024. URL https://arxiv.org/abs/2412.10654v1 .

- Wu et al. [20258] Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, and Yong Liu. From human memory to ai memory: A survey on memory mechanisms in the era of llms, arXiv preprint arXiv:2504.15965, 20258. URL https://arxiv.org/abs/2504.15965v2 .

- Wu and Ito [2025] Zengqing Wu and Takayuki Ito. The hidden strength of disagreement: Unraveling the consensus-diversity tradeoff in adaptive multi-agent systems, arXiv preprint arXiv:2502.16565, 2025. URL https://arxiv.org/abs/2502.16565v2 .

- Wu et al. [20234] Zihao Wu, Lu Zhang, Chao-Yang Cao, Xiao-Xing Yu, Haixing Dai, Chong-Yi Ma, Zheng Liu, Lin Zhao, Gang Li, Wei Liu, Quanzheng Li, Dinggang Shen, Xiang Li, Dajiang Zhu, and Tianming Liu. Exploring the trade-offs: Unified large language models vs local fine-tuned models for highly-specific radiology nli task. IEEE Transactions on Big Data , 20234.

- Xi et al. [2023] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, Rui Zheng, Xiaoran Fan, Xiao Wang, Limao Xiong, Qin Liu, Yuhao Zhou, Weiran Wang, Changhao Jiang, Yicheng Zou, Xiangyang Liu, Zhangyue Yin, Shihan Dou, Rongxiang Weng, Wensen Cheng, Qi Zhang, Wenjuan Qin, Yongyan Zheng, Xipeng Qiu, Xuanjing Huan, and Tao Gui. The rise and potential of large language model based agents: A survey, arXiv preprint arXiv:2309.07864, 2023. URL https://arxiv.org/abs/2309.07864v3 .

- Xia et al. [2025] Menglin Xia, Victor Ruehle, Saravan Rajmohan, and Reza Shokri. Minerva: A programmable memory test benchmark for language models, arXiv preprint arXiv:2502.03358, 2025. URL https://arxiv.org/abs/2502.03358v2 .

- Xia et al. [2023] Yuchen Xia, Manthan Shenoy, N. Jazdi, and M. Weyrich. Towards autonomous system: flexible modular production system enhanced with large language model agents. IEEE International Conference on Emerging Technologies and Factory Automation , 2023.

- Xia et al. [20252] Yutong Xia, Ao Qu, Yunhan Zheng, Yihong Tang, Dingyi Zhuang, Yuxuan Liang, Cathy Wu, Roger Zimmermann, and Jinhua Zhao. Reimagining urban science: Scaling causal inference with large language models, arXiv preprint arXiv:2504.12345v3, 20252. URL https://arxiv.org/abs/2504.12345v3 .

- Xiang et al. [2025] Zhishang Xiang, Chuanjie Wu, Qinggang Zhang, Shengyuan Chen, Zijin Hong, Xiao Huang, and Jinsong Su. When to use graphs in rag: A comprehensive analysis for graph retrieval-augmented generation, arXiv preprint arXiv:2506.05690, 2025. URL https://arxiv.org/abs/2506.05690v1 .

- Xiao et al. [2024] Chaojun Xiao, Pengle Zhang, Xu Han, Guangxuan Xiao, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, Song Han, and Maosong Sun. Infllm: Training-free long-context extrapolation for llms with an efficient context memory. Neural Information Processing Systems , 2024.

- Xiao et al. [2023] Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks. International Conference on Learning Representations , 2023.

- Xiao et al. [2025] MiniCPM Team Chaojun Xiao, Yuxuan Li, Xu Han, Yuzhuo Bai, Jie Cai, Haotian Chen, Wentong Chen, Xin Cong, Ganqu Cui, Ning Ding, Shengda Fan, Yewei Fang, Zixuan Fu, Wenyu Guan, Yitong Guan, Junshao Guo, Yu-Xuan Han, Bingxiang He, Yuxian Huang, Cunliang Kong, Qiu-Tong Li, Siyuan Li, Wenhao Li, Yanghao Li, Yishan Li, Zhen Li, Dan Liu, Biyuan Lin, Yankai Lin, Xiang Long, Quanyu Lu, Ya-Ting Lu, Pei Luo, Hongya Lyu, Litu Ou, Yinxu Pan, Zekai Qu, Qundong Shi, Zijun Song, Jiayu Su, Zhou Su, Ao Sun, Xiang ping Sun, Peijun Tang, Fang-Ming Wang, Feng Wang, Shuo Wang, Yudong Wang, Yesai Wu, Zhenyu Xiao, Jie Xie, Zi-Kang Xie, Yukun Yan, Jia-Li Yuan, Kai Zhang, Lei Zhang, Linyu Zhang, Xueren Zhang, Yudi Zhang, Hengyu Zhao, Weilin Zhao, Weilun Zhao, Yuanqian Zhao, Zhijun Zheng, Ge Zhou, Jie Zhou, Wei Zhou, Zihan Zhou, Zi-An Zhou, Zhiyuan Liu, Guoyang Zeng, Chaochao Jia, Dahai Li, and Maosong Sun. Minicpm4: Ultra-efficient llms on end devices, arXiv preprint arXiv:2506.07900, 2025. URL https://arxiv.org/abs/2506.07900v1 .

- Xiao et al. [20252] Yang Xiao, Jiashuo Wang, Ruifeng Yuan, Chunpu Xu, Kaishuai Xu, Wenjie Li, and Pengfei Liu. Limopro: Reasoning refinement for efficient and effective test-time scaling, arXiv preprint arXiv:2505.19187, 20252. URL https://arxiv.org/abs/2505.19187v1 .

- Xiao et al. [20253] Yilin Xiao, Chuang Zhou, Qinggang Zhang, Bo Li, Qing Li, and Xiao Huang. Reliable reasoning path: Distilling effective guidance for llm reasoning with knowledge graphs, arXiv preprint arXiv:2506.10508, 20253. URL https://arxiv.org/abs/2506.10508v1 .

- Xie et al. [2024] Jian Xie, Kai Zhang, Jiangjie Chen, Tinghui Zhu, Renze Lou, Yuandong Tian, Yanghua Xiao, and Yu Su. Travelplanner: A benchmark for real-world planning with language agents. International Conference on Machine Learning , 2024.

- Xie et al. [20242] Yuxi Xie, Anirudh Goyal, Xiaobao Wu, Xunjian Yin, Xiao Xu, Min-Yen Kan, Liangming Pan, and William Yang Wang. Coral: Order-agnostic language modeling for efficient iterative refinement, arXiv preprint arXiv:2410.09675, 20242. URL https://arxiv.org/abs/2410.09675v1 .

- Xing et al. [2025] Yue Xing, Tao Yang, Yijiashun Qi, Minggu Wei, Yu Cheng, and Honghui Xin. Structured memory mechanisms for stable context representation in large language models, arXiv preprint arXiv:2505.22921, 2025. URL https://arxiv.org/abs/2505.22921v1 .

- Xiong et al. [2025] Guangzhi Xiong, Qiao Jin, Xiao Wang, Yin Fang, Haolin Liu, Yifan Yang, Fangyuan Chen, Zhixing Song, Dengyu Wang, Minjia Zhang, Zhiyong Lu, and Aidong Zhang. Rag-gym: Systematic optimization of language agents for retrieval-augmented generation. arXiv preprint, 2025.

- Xiong et al. [2024] Haoyi Xiong, Zhiyuan Wang, Xuhong Li, Jiang Bian, Zeke Xie, Shahid Mumtaz, and Laura E. Barnes. Converging paradigms: The synergy of symbolic and connectionist ai in llm-empowered autonomous agents, arXiv preprint arXiv:2407.08516, 2024. URL https://arxiv.org/abs/2407.08516v5 .

- Xiong et al. [20252] Junjie Xiong, Changjia Zhu, Shuhang Lin, Chong Zhang, Yongfeng Zhang, Yao Liu, and Lingyao Li. Invisible prompts, visible threats: Malicious font injection in external resources for large language models, arXiv preprint arXiv:2505.16957, 20252. URL https://arxiv.org/abs/2505.16957v1 .

- Xiong et al. [20253] Zhen Xiong, Yujun Cai, Bryan Hooi, Nanyun Peng, Zhecheng Li, and Yiwei Wang. Enhancing llm character-level manipulation via divide and conquer. 20253.

- Xiong et al. [20254] Zhen Xiong, Yujun Cai, Zhecheng Li, and Yiwei Wang. Mapping the minds of llms: A graph-based analysis of reasoning llm. 20254.

- Xiong et al. [20255] Zhen Xiong, Yujun Cai, Zhecheng Li, and Yiwei Wang. Unveiling the potential of diffusion large language model in controllable generation. 20255.

- Xiong et al. [20256] Zidi Xiong, Yuping Lin, Wenya Xie, Pengfei He, Jiliang Tang, Himabindu Lakkaraju, and Zhen Xiang. How memory management impacts llm agents: An empirical study of experience-following behavior, arXiv preprint arXiv:2505.16067, 20256. URL https://arxiv.org/abs/2505.16067v1 .

- Xu et al. [2021] Chunmei Xu, Shengheng Liu, Cheng Zhang, Yongming Huang, Zhaohua Lu, and Luxi Yang. Multi-agent reinforcement learning based distributed transmission in collaborative cloud-edge systems. IEEE Transactions on Vehicular Technology , 2021.

- Xu et al. [2025] Haotian Xu, Xing Wu, Weinong Wang, Zhongzhi Li, Da Zheng, Boyuan Chen, Yi Hu, Shijia Kang, Jiaming Ji, Yingying Zhang, et al. Redstar: Does scaling long-cot data unlock better slow-reasoning systems? 2025.

- Xu et al. [2024] Hongshen Xu, Su Zhu, Zihan Wang, Hang Zheng, Da Ma, Ruisheng Cao, Shuai Fan, Lu Chen, and Kai Yu. Reducing tool hallucination via reliability alignment, arXiv preprint arXiv:2412.04141, 2024. URL https://arxiv.org/abs/2412.04141v3 .

- Xu et al. [20212] Hu Xu, Gargi Ghosh, Po-Yao (Bernie) Huang, Dmytro Okhonko, Armen Aghajanyan, and Florian Metze Luke Zettlemoyer Christoph Feichtenhofer. Videoclip: Contrastive pre-training for zero-shot video-text understanding. Conference on Empirical Methods in Natural Language Processing , 20212.

- Xu [2020] Mengjia Xu. Understanding graph embedding methods and their applications. SIAM Review , 2020.

- Xu et al. [2023] Minrui Xu, Hongyang Du, Dusist Niyato, Jiawen Kang, Zehui Xiong, Shiwen Mao, Zhu Han, A. Jamalipour, Dong In Kim, X. Shen, Victor C. M. Leung, and H. Poor. Unleashing the power of edge-cloud generative ai in mobile networks: A survey of aigc services. IEEE Communications Surveys and Tutorials , 2023.

- Xu et al. [20252] Minrui Xu, D. Niyato, and Christopher G. Brinton. Serving long-context llms at the mobile edge: Test-time reinforcement learning-based model caching and inference offloading, arXiv preprint arXiv:2501.14205, 20252. URL https://arxiv.org/abs/2501.14205v1 .

- Xu et al. [20242] Nan Xu, Fei Wang, Sheng Zhang, Hoifung Poon, and Muhao Chen. From introspection to best practices: Principled analysis of demonstrations in multimodal in-context learning. North American Chapter of the Association for Computational Linguistics , 20242.

- Xu and Zhong [2025] Shuhang Xu and Fangwei Zhong. Comet: Metaphor-driven covert communication for multi-agent language games, arXiv preprint arXiv:2505.18218, 2025. URL https://arxiv.org/abs/2505.18218v1 .

- Xu et al. [20253] Tianyang Xu, Haojie Zheng, Chengze Li, Haoxiang Chen, Yixin Liu, Ruoxi Chen, and Lichao Sun. Noderag: Structuring graph-based rag with heterogeneous nodes, arXiv preprint arXiv:2504.11544, 20253. URL https://arxiv.org/abs/2504.11544v1 .

- Xu et al. [20243] Wenda Xu, Guanglei Zhu, Xuandong Zhao, Liangming Pan, Lei Li, and W. Wang. Pride and prejudice: Llm amplifies self-bias in self-refinement. Annual Meeting of the Association for Computational Linguistics , 20243.

- Xu and Parhi [2025] Wenrui Xu and Keshab K. Parhi. A survey of attacks on large language models, arXiv preprint arXiv:2505.12567, 2025. URL https://arxiv.org/abs/2505.12567v1 .

- Xu et al. [20254] Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. A-mem: Agentic memory for llm agents. arXiv preprint, 20254.

- Xu et al. [20255] Wujiang Xu, Kai Mei, Hang Gao, Juntao Tan, Zujie Liang, and Yongfeng Zhang. A-mem: Agentic memory for llm agents, arXiv preprint arXiv:2502.12110, 20255. URL https://arxiv.org/abs/2502.12110 .

- Xu et al. [20213] Yifei Xu, Jingqiao Zhang, Ru He, Liangzhu Ge, Chao Yang, Cheng Yang, and Ying Wu. Sas: Self-augmentation strategy for language model pre-training. AAAI Conference on Artificial Intelligence , 20213.

- Xu et al. [20256] Zhe Xu, Daoyuan Chen, Zhenqing Ling, Yaliang Li, and Ying Shen. Mindgym: What matters in question synthesis for thinking-centric fine-tuning?, arXiv preprint arXiv:2503.09499, 20256. URL https://arxiv.org/abs/2503.09499v2 .

- Xu et al. [20244] Zhentao Xu, Mark Jerome Cruz, Matthew Guevara, Tie Wang, Manasi Deshpande, Xiaofeng Wang, and Zheng Li. Retrieval-augmented generation with knowledge graphs for customer service question answering. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 20244.

- Xue et al. [2025] Eric Xue, Ke Chen, Zeyi Huang, Yuyang Ji, Yong Jae Lee, and Haohan Wang. Improve: Iterative model pipeline refinement and optimization leveraging llm experts, arXiv preprint arXiv:2502.18530, 2025. URL https://arxiv.org/abs/2502.18530v2 .

- Xue and Aletras [2023] Huiyin Xue and Nikolaos Aletras. Pit one against many: Leveraging attention-head embeddings for parameter-efficient multi-head attention. Conference on Empirical Methods in Natural Language Processing , 2023.

- Xue et al. [2024] Xiangyuan Xue, Zeyu Lu, Di Huang, Zidong Wang, Wanli Ouyang, and Lei Bai. Comfybench: Benchmarking llm-based agents in comfyui for autonomously designing collaborative ai systems, arXiv preprint arXiv:2409.01392, 2024. URL https://arxiv.org/abs/2409.01392v2 .

- Yan et al. [2025] Bingyu Yan, Xiaoming Zhang, Litian Zhang, Lian Zhang, Ziyi Zhou, Dezhuang Miao, and Chaozhuo Li. Beyond self-talk: A communication-centric survey of llm-based multi-agent systems. arXiv preprint, 2025.

- Yan and Xu [2023] Tianqiang Yan and Tiansheng Xu. Refining the responses of llms by themselves, arXiv preprint arXiv:2305.04039, 2023. URL https://arxiv.org/abs/2305.04039v1 .

- Yan et al. [2024] Xu Yan, Junliang Du, Lun Wang, Yingbin Liang, Jiacheng Hu, and Bingxing Wang. The synergistic role of deep learning and neural architecture search in advancing artificial intelligence. 2024 International Conference on Electronics and Devices, Computational Science (ICEDCS) , 2024.

- Yan et al. [2023] Yibo Yan, Haomin Wen, Siru Zhong, Wei Chen, Haodong Chen, Qingsong Wen, Roger Zimmermann, and Yuxuan Liang. Urbanclip: Learning text-enhanced urban region profiling with contrastive language-image pretraining from the web. The Web Conference , 2023.

- Yan et al. [20252] Yuchen Yan, Yongliang Shen, Yang Liu, Jin Jiang, Mengdi Zhang, Jian Shao, and Yueting Zhuang. Inftythink: Breaking the length limits of long-context reasoning in large language models, arXiv preprint arXiv:2503.06692, 20252. URL https://arxiv.org/abs/2503.06692v3 .

- Yang et al. [2023] Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, and Xinyun Chen. Large language models as optimizers. International Conference on Learning Representations , 2023.

- Yang et al. [2024] Hongkang Yang, Zehao Lin, Wenjin Wang, Hao Wu, Zhiyu Li, Bo Tang, Wenqiang Wei, Jinbo Wang, Zeyun Tang, Shichao Song, Chenyang Xi, Yu Yu, Kai Chen, Feiyu Xiong, Linpeng Tang, and E. Weinan. Memory3: Language modeling with explicit memory. Journal of Machine Learning , 2024.

- Yang [2023] Jianxin Yang. Longqlora: Efficient and effective method to extend context length of large language models, arXiv preprint arXiv:2311.04879, 2023. URL https://arxiv.org/abs/2311.04879v2 .

- Yang et al. [20232] Jinghan Yang, Shuming Ma, and Furu Wei. Auto-icl: In-context learning without human supervision. arXiv preprint, 20232.

- Yang et al. [20233] Jingkang Yang, Yuhao Dong, Shuai Liu, Bo Li, Ziyue Wang, Chencheng Jiang, Haoran Tan, Jiamu Kang, Yuanhan Zhang, Kaiyang Zhou, and Ziwei Liu. Octopus: Embodied vision-language programmer from environmental feedback. European Conference on Computer Vision , 20233.

- Yang et al. [20242] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Adriano Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. Swe-agent: Agent-computer interfaces enable automated software engineering. Neural Information Processing Systems , 20242.

- Yang et al. [2021] Junhan Yang, Zheng Liu, Shitao Xiao, Chaozhuo Li, Defu Lian, Sanjay Agrawal, Amit Singh, Guangzhong Sun, and Xing Xie. Graphformers: Gnn-nested transformers for representation learning on textual graph. Neural Information Processing Systems , 2021.

- Yang et al. [20243] Ke Yang, Yao Liu, Sapana Chaudhary, Rasool Fakoor, Pratik Chaudhari, George Karypis, and Huzefa Rangwala. Agentoccam: A simple yet strong baseline for llm-based web agents. 20243.

- Yang et al. [20234] Lin F. Yang, Hongyang Chen, Zhao Li, Xiao Ding, and Xindong Wu. Give us the facts: Enhancing large language models with knowledge graphs for fact-aware language modeling. IEEE Transactions on Knowledge and Data Engineering , 20234.

- Yang et al. [2025] Ling Yang, Ye Tian, Bowen Li, Xinchen Zhang, Ke Shen, Yunhai Tong, and Mengdi Wang. Mmada: Multimodal large diffusion language models, arXiv preprint arXiv:2505.15809v1, 2025. URL https://arxiv.org/abs/2505.15809v1 .

- Yang et al. [20235] R Yang, L Song, Y Li, S Zhao, and Y Ge…. Gpt4tools: Teaching large language model to use tools via self-instruction. 20235. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash/e393677793767624f2821cec8bdd02f1-Abstract-Conference.html?utm_campaign=Artificial%2BIntelligence%2BWeekly&utm_medium=email&utm_source=Artificial_Intelligence_Weekly_411 .

- Yang et al. [20236] Rui Yang, Lin Song, Yanwei Li, Sijie Zhao, Yixiao Ge, Xiu Li, and Ying Shan. Gpt4tools: Teaching large language model to use tools via self-instruction. Neural Information Processing Systems , 20236.

- Yang et al. [20252] Shang Yang, Junxian Guo, Haotian Tang, Qinghao Hu, Guangxuan Xiao, Jiaming Tang, Yujun Lin, Zhijian Liu, Yao Lu, and Song Han. Lserve: Efficient long-sequence llm serving with unified sparse attention, arXiv preprint arXiv:2502.14866, 20252. URL https://arxiv.org/abs/2502.14866v2 .

- Yang et al. [20244] Shanglong Yang, Zhipeng Yuan, Shunbao Li, Ruoling Peng, Kang Liu, and Po Yang. Gpt-4 as evaluator: Evaluating large language models on pest management in agriculture. arXiv preprint, 20244.

- Yang et al. [20253] Wang Yang, Zirui Liu, Hongye Jin, Qingyu Yin, Vipin Chaudhary, and Xiaotian Han. Longer context, deeper thinking: Uncovering the role of long-context ability in reasoning, arXiv preprint arXiv:2505.17315, 20253. URL https://arxiv.org/abs/2505.17315v1 .

- Yang et al. [20245] Wen Yang, Kai Fan, and Minpeng Liao. Markov chain of thought for efficient mathematical reasoning. North American Chapter of the Association for Computational Linguistics , 20245.

- Yang et al. [2020] Yaodong Yang, Chengdong Ma, Zihan Ding, S. McAleer, Chi Jin, and Jun Wang. Game-theoretic multiagent reinforcement learning, arXiv preprint arXiv:2011.00583, 2020. URL https://arxiv.org/abs/2011.00583v4 .

- Yang et al. [20246] Yazheng Yang, Yuqi Wang, Sankalok Sen, Lei Li, and Qi Liu. Unleashing the potential of large language models for predictive tabular tasks in data science, arXiv preprint arXiv:2403.20208, 20246. URL https://arxiv.org/abs/2403.20208v7 .

- Yang et al. [20237] Yi Yang, Yixuan Tang, and Kar Yan Tam. Investlm: A large language model for investment using financial domain instruction tuning, arXiv preprint arXiv:2309.13064, 20237. URL https://arxiv.org/abs/2309.13064 .

- Yang et al. [20202] Yiben Yang, Chaitanya Malaviya, Jared Fernandez, Swabha Swayamdipta, Ronan Le Bras, Ji ping Wang, Chandra Bhagavatula, Yejin Choi, and Doug Downey. G-daug: Generative data augmentation for commonsense reasoning. Findings , 20202.

- Yang et al. [20254] Yingxuan Yang, Huacan Chai, Yuanyi Song, Siyuan Qi, Muning Wen, Ning Li, Junwei Liao, Haoyi Hu, Jianghao Lin, Gaowei Chang, Weiwen Liu, Ying Wen, Yong Yu, and Weinan Zhang. A survey of ai agent protocols, arXiv preprint arXiv:2504.16736, 20254. URL https://arxiv.org/abs/2504.16736v3 .

- Yang et al. [20247] Yuan Yang, Siheng Xiong, Ehsan Shareghi, and F. Fekri. The compressor-retriever architecture for language model os, arXiv preprint arXiv:2409.01495, 20247. URL https://arxiv.org/abs/2409.01495v1 .

- Yang et al. [20255] Yuxin Yang, Haoyang Wu, Tao Wang, Jia Yang, Hao Ma, and Guojie Luo. Pseudo-knowledge graph: Meta-path guided retrieval and in-graph text for rag-equipped llm, arXiv preprint arXiv:2503.00309, 20255. URL https://arxiv.org/abs/2503.00309v1 .

- Yang et al. [20248] Zhen Yang, Fang Liu, Zhongxing Yu, J. Keung, Jia Li, Shuo Liu, Yifan Hong, Xiaoxue Ma, Zhi Jin, and Ge Li. Exploring and unleashing the power of large language models in automated code translation. Proc. ACM Softw. Eng. , 20248.

- Yao and Fujita [2024] Chengyuan Yao and Satoshi Fujita. Adaptive control of retrieval-augmented generation for large language models through reflective tags. Electronics , 2024.

- Yao et al. [2024] Huaiyuan Yao, Longchao Da, Vishnu Nandam, J. Turnau, Zhiwei Liu, Linsey Pang, and Hua Wei. Comal: Collaborative multi-agent large language models for mixed-autonomy traffic, arXiv preprint arXiv:2410.14368, 2024. URL https://arxiv.org/abs/2410.14368v2 .

- Yao et al. [2025] Jiayu Yao, Shenghua Liu, Yiwei Wang, Lingrui Mei, Baolong Bi, Yuyao Ge, Zhecheng Li, and Xueqi Cheng. Who is in the spotlight: The hidden bias undermining multimodal retrieval-augmented generation. 2025.

- Yao et al. [20242] Jinghan Yao, Sam Ade Jacobs, Masahiro Tanaka, Olatunji Ruwase, A. Shafi, H. Subramoni, and Dhabaleswar K. Panda. Training ultra long context language model with fully pipelined distributed transformer, arXiv preprint arXiv:2408.16978, 20242. URL https://arxiv.org/abs/2408.16978v2 .

- Yao et al. [2018] Liang Yao, Chengsheng Mao, and Yuan Luo. Graph convolutional networks for text classification. AAAI Conference on Artificial Intelligence , 2018.

- Yao et al. [2022] Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable real-world web interaction with grounded language agents. Neural Information Processing Systems , 2022.

- Yao et al. [20222] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. International Conference on Learning Representations , 20222.

- Yao et al. [2023] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, T. Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. Neural Information Processing Systems , 2023.

- Yao et al. [20232] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models, arXiv preprint arXiv:2210.03629, 20232. URL https://arxiv.org/abs/2210.03629 .

- Yao et al. [20243] Shunyu Yao, Noah Shinn, P. Razavi, and Karthik Narasimhan. τ 𝜏 \tau italic_τ -bench: A benchmark for tool-agent-user interaction in real-world domains. arXiv preprint, 20243.

- Yao et al. [20244] Weiran Yao, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Yihao Feng, Le Xue, Rithesh Murthy, Zeyuan Chen, Jianguo Zhang, Devansh Arpit, Ran Xu, Phil Mui, Huan Wang, Caiming Xiong, and Silvio Savarese. Retroformer: Retrospective large language agents with policy gradient optimization, arXiv preprint arXiv:2308.02151, 20244. URL https://arxiv.org/abs/2308.02151 .

- Yasunaga et al. [2021] Michihiro Yasunaga, Hongyu Ren, Antoine Bosselut, Percy Liang, and J. Leskovec. Qa-gnn: Reasoning with language models and knowledge graphs for question answering. North American Chapter of the Association for Computational Linguistics , 2021.

- Yasunaga et al. [2022] Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D. Manning, Percy Liang, and J. Leskovec. Deep bidirectional language-knowledge graph pretraining. Neural Information Processing Systems , 2022.

- Yazin et al. [2021] Fahd Yazin, Moumita Das, A. Banerjee, and Dipanjan Roy. Contextual prediction errors reorganize naturalistic episodic memories in time. Scientific Reports , 2021.

- Ye et al. [2024] J Ye, G Li, S Gao, C Huang, Y Wu, S Li, and X Fan…. Tooleyes: Fine-grained evaluation for tool learning capabilities of large language models in real-world scenarios. 2024. URL https://arxiv.org/abs/2401.00741 .

- Ye et al. [20242] J Ye, S Li, G Li, C Huang, S Gao, and Y Wu…. Toolsword: Unveiling safety issues of large language models in tool learning across three stages. 20242. URL https://arxiv.org/abs/2402.10753 .

- Ye et al. [2025] Junjie Ye, Zhengyin Du, Xuesong Yao, Weijian Lin, Yufei Xu, Zehui Chen, Zaiyuan Wang, Sining Zhu, Zhiheng Xi, Siyu Yuan, Tao Gui, Qi Zhang, Xuanjing Huang, and Jiechao Chen. Toolhop: A query-driven benchmark for evaluating large language models in multi-hop tool use, arXiv preprint arXiv:2501.02506, 2025. URL https://arxiv.org/abs/2501.02506v4 .

- Ye et al. [2023] Qinyuan Ye, Maxamed Axmed, Reid Pryzant, and Fereshte Khani. Prompt engineering a prompt engineer. Annual Meeting of the Association for Computational Linguistics , 2023.

- Ye et al. [20252] Sixiang Ye, Zeyu Sun, Guoqing Wang, Liwei Guo, Qing-Lin Liang, Zheng Li, and Yong Liu. Prompt alchemy: Automatic prompt refinement for enhancing code generation, arXiv preprint arXiv:2503.11085, 20252. URL https://arxiv.org/abs/2503.11085v1 .

- Ye et al. [20253] Zhifan Ye, Kejing Xia, Yonggan Fu, Xin Dong, Jihoon Hong, Xiangchi Yuan, Shizhe Diao, Jan Kautz, Pavlo Molchanov, and Y. Lin. Longmamba: Enhancing mamba’s long-context capabilities via training-free receptive field enlargement. International Conference on Learning Representations , 20253.

- Yehudai et al. [2025] Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan, and Michal Shmueli-Scheuer. Survey on evaluation of llm-based agents, arXiv preprint arXiv:2503.16416, 2025. URL https://arxiv.org/abs/2503.16416v1 .

- Yi and Xia [2025] Peiling Yi and Yuhan Xia. Irony detection, reasoning and understanding in zero-shot learning. IEEE Transactions on Artificial Intelligence , 2025.

- Yin et al. [2023] Da Yin, Faeze Brahman, Abhilasha Ravichander, Khyathi Raghavi Chandu, Kai-Wei Chang, Yejin Choi, and Bill Yuchen Lin. Agent lumos: Unified and modular training for open-source language agents. Annual Meeting of the Association for Computational Linguistics , 2023.

- Yin et al. [2025] Fan Yin, Zifeng Wang, I-Hung Hsu, Jun Yan, Ke Jiang, Yanfei Chen, Jindong Gu, Long T. Le, Kai-Wei Chang, Chen-Yu Lee, Hamid Palangi, and Tomas Pfister. Magnet: Multi-turn tool-use data synthesis and distillation via graph translation, arXiv preprint arXiv:2503.07826, 2025. URL https://arxiv.org/abs/2503.07826v1 .

- Yin et al. [2024] Guoli Yin, Haoping Bai, Shuang Ma, Feng Nan, Yanchao Sun, Zhaoyang Xu, Shen Ma, Jiarui Lu, Xiang Kong, Aonan Zhang, Dian Ang Yap, Yizhe Zhang, K. Ahnert, Vik Kamath, Mathias Berglund, Dominic Walsh, Tobias Gindele, Juergen Wiest, Zhengfeng Lai, Xiaoming Wang, Jiulong Shan, Meng Cao, Ruoming Pang, and Zirui Wang. Mmau: A holistic benchmark of agent capabilities across diverse domains. North American Chapter of the Association for Computational Linguistics , 2024.

- Yin et al. [2020] Pengcheng Yin, Graham Neubig, Wen tau Yih, and Sebastian Riedel. Tabert: Pretraining for joint understanding of textual and tabular data. Annual Meeting of the Association for Computational Linguistics , 2020.

- Yin et al. [20242] S Yin, W You, Z Ji, G Zhong, and J Bai. Mumath-code: Combining tool-use large language models with multi-perspective data augmentation for mathematical reasoning. 20242. URL https://arxiv.org/abs/2405.07551 .

- Yong et al. [2022] Gunwoo Yong, Kahyun Jeon, Daeyoung Gil, and Ghang Lee. Prompt engineering for zero-shot and few-shot defect detection and classification using a visual-language pretrained model. Comput. Aided Civ. Infrastructure Eng. , 2022.

- Yoo and Collins [2021] Aspen H. Yoo and A. Collins. How working memory and reinforcement learning are intertwined: A cognitive, neural, and computational perspective. Journal of Cognitive Neuroscience , 2021.

- Yoon et al. [2024] Chanwoong Yoon, Taewhoo Lee, Hyeon Hwang, Minbyul Jeong, and Jaewoo Kang. Compact: Compressing retrieved documents actively for question answering. Conference on Empirical Methods in Natural Language Processing , 2024.

- You et al. [2024] Jiaxuan You, Mingjie Liu, Shrimai Prabhumoye, M. Patwary, M. Shoeybi, and Bryan Catanzaro. Llm-evolve: Evaluation for llm’s evolving capability on benchmarks. Conference on Empirical Methods in Natural Language Processing , 2024.

- You et al. [20242] Yuxin You, Zhen Liu, Xiangchao Wen, Yongtao Zhang, and Wei Ai. Large language models meet graph neural networks: A perspective of graph mining. Mathematics , 20242.

- Yu et al. [2024] Dian Yu, Yuheng Zhang, Jiahao Xu, Tian Liang, Linfeng Song, Zhaopeng Tu, Haitao Mi, and Dong Yu. Teaching llms to refine with tools, arXiv preprint arXiv:2412.16871, 2024. URL https://arxiv.org/abs/2412.16871v1 .

- Yu et al. [2025] Miao Yu, Fanci Meng, Xinyun Zhou, Shilong Wang, Junyuan Mao, Linsey Pang, Tianlong Chen, Kun Wang, Xinfeng Li, Yongfeng Zhang, Bo An, and Qingsong Wen. A survey on trustworthy llm agents: Threats and countermeasures, arXiv preprint arXiv:2503.09648, 2025. URL https://arxiv.org/abs/2503.09648v1 .

- Yu et al. [20252] Ye Yu, Yaoning Yu, and Haohan Wang. Premise: Scalable and strategic prompt optimization for efficient mathematical reasoning in large models, arXiv preprint arXiv:2506.10716, 20252. URL https://arxiv.org/abs/2506.10716v1 .

- Yu and Ananiadou [2024] Zeping Yu and Sophia Ananiadou. Understanding multimodal llms: the mechanistic interpretability of llava in visual question answering, arXiv preprint arXiv:2411.10950v2, 2024. URL https://arxiv.org/abs/2411.10950v2 .

- Yu et al. [20253] Zishun Yu, Tengyu Xu, Di Jin, Karthik Abinav Sankararaman, Yun He, Wenxuan Zhou, Zhouhao Zeng, Eryk Helenowski, Chen Zhu, Si-Yuan Wang, Hao Ma, and Han Fang. Think smarter not harder: Adaptive reasoning with inference aware optimization, arXiv preprint arXiv:2501.17974, 20253. URL https://arxiv.org/abs/2501.17974v2 .

- yu Su et al. [2025] Zhao yu Su, Linjie Li, Mingyang Song, Yunzhuo Hao, Zhengyuan Yang, Jun Zhang, Guanjie Chen, Jiawei Gu, Juntao Li, Xiaoye Qu, and Yu Cheng. Openthinkimg: Learning to think with images via visual tool reinforcement learning, arXiv preprint arXiv:2505.08617, 2025. URL https://arxiv.org/abs/2505.08617v1 .

- Yuan et al. [2025] Siyu Yuan, Zehui Chen, Zhiheng Xi, Junjie Ye, Zhengyin Du, and Jiecao Chen. Agent-r: Training language model agents to reflect via iterative self-training. arXiv preprint, 2025.

- Yuan et al. [2024] Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Sainbayar Sukhbaatar, Jing Xu, and Jason E Weston. Self-rewarding language models. International Conference on Machine Learning , 2024.

- Yuan et al. [20252] Xiaowei Yuan, Zhao Yang, Ziyang Huang, Yequan Wang, Siqi Fan, Yiming Ju, Jun Zhao, and Kang Liu. Exploiting contextual knowledge in llms through v-usable information based layer enhancement. arXiv preprint, 20252.

- Yuan et al. [20253] Xinbin Yuan, Jian Zhang, Kaixin Li, Zhuoxuan Cai, Lujian Yao, Jie Chen, Enguang Wang, Qibin Hou, Jinwei Chen, Peng-Tao Jiang, and Bo Li. Enhancing visual grounding for gui agents via self-evolutionary reinforcement learning, arXiv preprint arXiv:2505.12370, 20253. URL https://arxiv.org/abs/2505.12370v2 .

- Yue [2025] Murong Yue. A survey of large language model agents for question answering, arXiv preprint arXiv:2503.19213, 2025. URL https://arxiv.org/abs/2503.19213v1 .

- Yue et al. [2024] Xihang Yue, Linchao Zhu, and Yi Yang. Fragrel: Exploiting fragment-level relations in the external memory of large language models. Annual Meeting of the Association for Computational Linguistics , 2024.

- Yun et al. [2019] Seongjun Yun, Minbyul Jeong, Raehyun Kim, Jaewoo Kang, and Hyunwoo J. Kim. Graph transformer networks. Neural Information Processing Systems , 2019.

- Yuyao et al. [2022] Ge Yuyao, Cheng Yiting, Wang Jia, Zhou Hanlin, and Chen Lizhe. Vision transformer based on knowledge distillation in tcm image classification. In 2022 IEEE 5th International Conference on Computer and Communication Engineering Technology (CCET) , pages 120–125. IEEE, 2022.

- Zaheer et al. [2020] M. Zaheer, Guru Guruganesh, Kumar Avinava Dubey, J. Ainslie, Chris Alberti, Santiago Ontañón, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. Big bird: Transformers for longer sequences. Neural Information Processing Systems , 2020.

- Zang et al. [2023] Yuhang Zang, Wei Li, Jun Han, Kaiyang Zhou, and Chen Change Loy. Contextual object detection with multimodal large language models. International Journal of Computer Vision , 2023.

- Zelikman et al. [2022] E. Zelikman, Yuhuai Wu, and Noah D. Goodman. Star: Bootstrapping reasoning with reasoning, arXiv preprint arXiv:2203.14465, 2022. URL https://arxiv.org/abs/2203.14465v2 .

- Zelikman et al. [2023] E. Zelikman, Eliana Lorch, Lester Mackey, and A. Kalai. Self-taught optimizer (stop): Recursively self-improving code generation, arXiv preprint arXiv:2310.02304, 2023. URL https://arxiv.org/abs/2310.02304v3 .

- Zeng et al. [2024] Pai Zeng, Zhenyu Ning, Jieru Zhao, Weihao Cui, Mengwei Xu, Liwei Guo, XuSheng Chen, and Yizhou Shan. The cap principle for llm serving: A survey of long-context large language model serving, arXiv preprint arXiv:2405.11299, 2024. URL https://arxiv.org/abs/2405.11299v2 .

- Zeng et al. [20242] Ruihong Zeng, Jinyuan Fang, Siwei Liu, and Zaiqiao Meng. On the structural memory of llm agents, arXiv preprint arXiv:2412.15266, 20242. URL https://arxiv.org/abs/2412.15266v1 .

- Zeng et al. [2025] Yirong Zeng, Xiao Ding, Yuxian Wang, Weiwen Liu, Wu Ning, Yutai Hou, Xu Huang, Bing Qin, and Ting Liu. itool: Reinforced fine-tuning with dynamic deficiency calibration for advanced tool use, arXiv preprint arXiv:2501.09766, 2025. URL https://arxiv.org/abs/2501.09766v4 .

- Zeng et al. [20252] Yongcheng Zeng, Xinyu Cui, Xuanfa Jin, Guoqing Liu, Zexu Sun, Dong Li, Ning Yang, Jianye Hao, Haifeng Zhang, and Jun Wang. Evolving llms’ self-refinement capability via iterative preference optimization, arXiv preprint arXiv:2502.05605, 20252. URL https://arxiv.org/abs/2502.05605v3 .

- Zhang et al. [2023] An Zhang, Leheng Sheng, Yuxin Chen, Hao Li, Yang Deng, Xiang Wang, and Tat-Seng Chua. On generative agents in recommendation. Annual International ACM SIGIR Conference on Research and Development in Information Retrieval , 2023.

- Zhang et al. [20232] B Zhang, K Zhou, X Wei, and X Zhao…. Evaluating and improving tool-augmented computation-intensive math reasoning. 20232. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash/4a47dd69242d5af908cdd5d51c971cbf-Abstract-Datasets_and_Benchmarks.html .

- Zhang et al. [2024] Chao Zhang, Haoxin Zhang, Shiwei Wu, Di Wu, Tong Xu, Xiangyu Zhao, Yan Gao, Yao Hu, and Enhong Chen. Notellm-2: Multimodal large representation models for recommendation. Knowledge Discovery and Data Mining , 2024.

- Zhang et al. [2025] Chaoyun Zhang, He Huang, Chiming Ni, Jian Mu, Si Qin, Shilin He, Lu Wang, Fangkai Yang, Pu Zhao, Chao Du, et al. Ufo2: The desktop agentos. arXiv preprint arXiv:2504.14603 , 2025.

- Zhang et al. [2020] Chi Zhang, Yujun Cai, Guosheng Lin, and Chunhua Shen. Deepemd: Few-shot image classification with differentiable earth mover’s distance and structured classifiers. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pages 12203–12213, 2020.

- Zhang et al. [2021] Dan Zhang, G. Feng, Yang Shi, and D. Srinivasan. Physical safety and cyber security analysis of multi-agent systems: A survey of recent advances. IEEE/CAA Journal of Automatica Sinica , 2021.

- Zhang et al. [20233] Danyang Zhang, Lu Chen, Situo Zhang, Hongshen Xu, Zihan Zhao, and Kai Yu. Large language models are semi-parametric reinforcement learning agents. Neural Information Processing Systems , 20233.

- Zhang et al. [20242] Daoan Zhang, Weitong Zhang, Bing He, Jiang Zhang, Chenchen Qin, and Jianhua Yao. Dnagpt: A generalized pre-trained tool for multiple dna sequence analysis tasks. bioRxiv , 20242.

- Zhang et al. [20243] Duzhen Zhang, Yahan Yu, Jiahua Dong, Chenxing Li, Dan Su, Chenhui Chu, and Dong Yu. Mm-llms: Recent advances in multimodal large language models. In Findings of the Association for Computational Linguistics ACL 2024 , pages 12401–12430, 20243.

- Zhang et al. [20252] Duzhen Zhang, Yong Ren, Zhong-Zhi Li, Yahan Yu, Jiahua Dong, Chenxing Li, Zhilong Ji, and Jinfeng Bai. Enhancing multimodal continual instruction tuning with branchlora. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , 20252.

- Zhang et al. [20253] Han Zhang, Langshi Zhou, and Hanfang Yang. Learning to retrieve and reason on knowledge graph through active self-reflection, arXiv preprint arXiv:2502.14932, 20253. URL https://arxiv.org/abs/2502.14932v1 .

- Zhang [2024] Hengyu Zhang. Sinklora: Enhanced efficiency and chat capabilities for long-context large language models, arXiv preprint arXiv:2406.05678, 2024. URL https://arxiv.org/abs/2406.05678v1 .

- Zhang et al. [20244] Jiaxin Zhang, Zhongzhi Li, Mingliang Zhang, Fei Yin, Chenglin Liu, and Yashar Moshfeghi. Geoeval: benchmark for evaluating llms and multi-modal models on geometry problem-solving. 20244.

- Zhang et al. [2022] Jing Zhang, Xiaokang Zhang, Jifan Yu, Jian Tang, Jie Tang, Cuiping Li, and Hong Chen. Subgraph retrieval enhanced model for multi-hop knowledge base question answering. Annual Meeting of the Association for Computational Linguistics , 2022.

- Zhang et al. [20234] Kai Zhang, Fubang Zhao, Yangyang Kang, and Xiaozhong Liu. Llm-based medical assistant personalization with short- and long-term memory coordination. North American Chapter of the Association for Computational Linguistics , 20234.

- Zhang et al. [20254] Kai Zhang, Yejin Kim, and Xiaozhong Liu. Personalized llm response generation with parameterized memory injection, arXiv preprint arXiv:2404.03565, 20254. URL https://arxiv.org/abs/2404.03565 .

- Zhang et al. [20235] Kechi Zhang, Zhuo Li, Jia Li, Ge Li, and Zhi Jin. Self-edit: Fault-aware code editor for code generation. Annual Meeting of the Association for Computational Linguistics , 20235.

- Zhang et al. [20245] Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. Codeagent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. Annual Meeting of the Association for Computational Linguistics , 20245.

- Zhang et al. [20255] Kechi Zhang, Ge Li, Jia Li, Huangzhao Zhang, Jingjing Xu, Hao Zhu, Lecheng Wang, Yihong Dong, Jing Mai, Bin Gu, and Zhi Jin. Computational thinking reasoning in large language models, arXiv preprint arXiv:2506.02658, 20255. URL https://arxiv.org/abs/2506.02658v2 .

- Zhang et al. [20246] Ming-Liang Zhang, Zhong-Zhi Li, Fei Yin, Liang Lin, and Cheng-Lin Liu. Fuse, reason and verify: Geometry problem solving with parsed clauses from diagram. 20246.

- Zhang et al. [20256] Qiyuan Zhang, Fuyuan Lyu, Zexu Sun, Lei Wang, Weixu Zhang, Zhihan Guo, Yufei Wang, Irwin King, Xue Liu, and Chen Ma. A survey on test-time scaling in large language models: What, how, where, and how well?, arXiv preprint arXiv:2503.24235, 20256. URL https://arxiv.org/abs/2503.24235v3 .

- Zhang et al. [20257] Ruichen Zhang, Mufan Qiu, Zhen Tan, Mohan Zhang, Vincent Lu, Jie Peng, Kaidi Xu, Leandro Z. Agudelo, Peter Qian, and Tianlong Chen. Symbiotic cooperation for web agents: Harnessing complementary strengths of large and small llms, arXiv preprint arXiv:2502.07942, 20257. URL https://arxiv.org/abs/2502.07942v2 .

- Zhang et al. [20258] Tengchao Zhang, Yonglin Tian, Fei Lin, Jun Huang, Patrik P. Süli, Rui Qin, and Fei-Yue Wang. Coordfield: Coordination field for agentic uav task allocation in low-altitude urban scenarios, arXiv preprint arXiv:2505.00091, 20258. URL https://arxiv.org/abs/2505.00091v3 .

- Zhang et al. [20259] Weizhi Zhang, Xinyang Zhang, Chenwei Zhang, Liangwei Yang, Jingbo Shang, Zhepei Wei, Henry Peng Zou, Zijie Huang, Zhengyang Wang, Yifan Gao, Xiaoman Pan, Lian Xiong, Jingguo Liu, Philip S. Yu, and Xian Li. Personaagent: When large language model agents meet personalization at test time, arXiv preprint arXiv:2506.06254, 20259. URL https://arxiv.org/abs/2506.06254v1 .

- Zhang et al. [20247] Wen Zhang, Long Jin, Yushan Zhu, Jiaoyan Chen, Zhiwei Huang, Junjie Wang, Yin Hua, Lei Liang, and Hua zeng Chen. Trustuqa: A trustful framework for unified structured data question answering. AAAI Conference on Artificial Intelligence , 20247.

- Zhang et al. [202510] Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi Zhang, Derong Xu, Zhaochen Du, Huifeng Guo, Ruiming Tang, and Xiangyu Zhao. Process vs. outcome reward: Which is better for agentic rag reinforcement learning, arXiv preprint arXiv:2505.14069, 202510. URL https://arxiv.org/abs/2505.14069v2 .

- Zhang et al. [202511] Wentao Zhang, Ce Cui, Yilei Zhao, Rui Hu, Yang Liu, Yahui Zhou, and Bo An. Agentorchestra: A hierarchical multi-agent framework for general-purpose task solving, arXiv preprint arXiv:2506.12508, 202511. URL https://arxiv.org/abs/2506.12508v2 .

- Zhang et al. [202512] Xiaoyi Zhang, Zhaoyang Jia, Zongyu Guo, Jiahao Li, Bin Li, Houqiang Li, and Yan Lu. Deep video discovery: Agentic search with tool use for long-form video understanding, arXiv preprint arXiv:2505.18079, 202512. URL https://arxiv.org/abs/2505.18079v2 .

- Zhang et al. [20222] Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D. Manning, and J. Leskovec. Greaselm: Graph reasoning enhanced language models for question answering. International Conference on Learning Representations , 20222.

- Zhang et al. [20248] Yao Zhang, Zijian Ma, Yunpu Ma, Zhen Han, Yu Wu, and Volker Tresp. Webpilot: A versatile and autonomous multi-agent system for web task execution with strategic exploration, arXiv preprint arXiv:2408.15978, 20248. URL https://arxiv.org/abs/2408.15978 .

- Zhang et al. [20236] Yinger Zhang, Hui Cai, Yicheng Chen, Rui Sun, and Jing Zheng. Reverse chain: A generic-rule for llms to master multi-api planning, arXiv preprint arXiv:2310.04474, 20236. URL https://arxiv.org/abs/2310.04474v3 .

- Zhang et al. [20212] Youjia Zhang, Jin Wang, Liang-Chih Yu, and Xuejie Zhang. Ma-bert: Learning representation by incorporating multi-attribute knowledge in transformers. Findings , 20212.

- Zhang et al. [202513] Yu Zhang, Jinlong Ma, Yongshuai Hou, Xuefeng Bai, Kehai Chen, Yang Xiang, Jun Yu, and Min Zhang. Evaluating and steering modality preferences in multimodal large language model, arXiv preprint arXiv:2505.20977v1, 202513. URL https://arxiv.org/abs/2505.20977v1 .

- Zhang et al. [20249] Yunyi Zhang, Ming Zhong, Siru Ouyang, Yizhu Jiao, Sizhe Zhou, Linyi Ding, and Jiawei Han. Automated mining of structured knowledge from text in the era of large language models. Knowledge Discovery and Data Mining , 20249.

- Zhang et al. [202410] Yusen Zhang, Ruoxi Sun, Yanfei Chen, Tomas Pfister, Rui Zhang, and Sercan Ö. Arik. Chain of agents: Large language models collaborating on long-context tasks. Neural Information Processing Systems , 202410.

- Zhang et al. [202514] Yuxiang Zhang, Yuqi Yang, Jiangming Shu, Xinyan Wen, and Jitao Sang. Agent models: Internalizing chain-of-action generation into reasoning models, arXiv preprint arXiv:2503.06580, 202514. URL https://arxiv.org/abs/2503.06580v1 .

- Zhang et al. [202411] Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, and Ji-Rong Wen. A survey on the memory mechanism of large language model based agents, arXiv preprint arXiv:2404.13501, 202411. URL https://arxiv.org/abs/2404.13501v1 .

- Zhang et al. [202412] Zeyu Zhang, Quanyu Dai, Luyu Chen, Zeren Jiang, Rui Li, Jieming Zhu, Xu Chen, Yi Xie, Zhenhua Dong, and Ji-Rong Wen. Memsim: A bayesian simulator for evaluating memory of llm-based personal assistants, arXiv preprint arXiv:2409.20163, 202412. URL https://arxiv.org/abs/2409.20163v1 .

- Zhang et al. [202515] Zeyu Zhang, Quanyu Dai, Xu Chen, Rui Li, Zhongyang Li, and Zhenhua Dong. Memengine: A unified and modular library for developing advanced memory of llm-based agents. The Web Conference , 202515.

- Zhang et al. [20223] Zheng Zhang, Liang Ding, Dazhao Cheng, Xuebo Liu, Min Zhang, and Dacheng Tao. Bliss: Robust sequence-to-sequence learning via self-supervised input representation, arXiv preprint arXiv:2204.07837, 20223. URL https://arxiv.org/abs/2204.07837v2 .

- Zhang et al. [20237] Zhenyu (Allen) Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark W. Barrett, Zhangyang Wang, and Beidi Chen. H2o: Heavy-hitter oracle for efficient generative inference of large language models. Neural Information Processing Systems , 20237.

- Zhang et al. [202413] Zhihan Zhang, Zhenwen Liang, Wenhao Yu, Dian Yu, Mengzhao Jia, Dong Yu, and Meng Jiang. Learn beyond the answer: Training language models with reflection for mathematical reasoning. Conference on Empirical Methods in Natural Language Processing , 202413.

- Zhang and Zhang [2023] Zhuosheng Zhang and Aston Zhang. You only look at screens: Multimodal chain-of-action agents. Annual Meeting of the Association for Computational Linguistics , 2023.

- Zhao et al. [2023] Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Y. Liu, and Gao Huang. Expel: Llm agents are experiential learners. AAAI Conference on Artificial Intelligence , 2023.

- Zhao et al. [2024] Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. Expel: Llm agents are experiential learners, arXiv preprint arXiv:2308.10144, 2024. URL https://arxiv.org/abs/2308.10144 .

- Zhao et al. [2022] Jianan Zhao, Meng Qu, Chaozhuo Li, Hao Yan, Qian Liu, Rui Li, Xing Xie, and Jian Tang. Learning on large-scale text-attributed graphs via variational inference. International Conference on Learning Representations , 2022.

- Zhao et al. [20242] Penghao Zhao, Hailin Zhang, Qinhan Yu, Zhengren Wang, Yunteng Geng, Fangcheng Fu, Ling Yang, Wentao Zhang, and Bin Cui. Retrieval-augmented generation for ai-generated content: A survey, arXiv preprint arXiv:2402.19473, 20242. URL https://arxiv.org/abs/2402.19473v6 .

- Zhao et al. [20232] Pengyu Zhao, Zijian Jin, and Ning Cheng. An in-depth survey of large language model-based artificial intelligence agents, arXiv preprint arXiv:2309.14365, 20232. URL https://arxiv.org/abs/2309.14365v1 .

- Zhao et al. [20243] Pu Zhao, Xuan Shen, Zhenglun Kong, Yixin Shen, Sung-En Chang, Timothy Rupprecht, Lei Lu, Enfu Nan, Changdi Yang, Yumei He, Xingchen Xu, Yu Huang, Wei Wang, Yue Chen, Yongchun He, and Yanzhi Wang. 7b fully open source moxin-llm/vlm – from pretraining to grpo-based reinforcement learning enhancement. arXiv preprint, 20243.

- Zhao et al. [2025] Qi Zhao, Hongyu Yang, Qi Song, Xinwei Yao, and Xiangyang Li. Knowpath: Knowledge-enhanced reasoning via llm-generated inference paths over knowledge graphs, arXiv preprint arXiv:2502.12029, 2025. URL https://arxiv.org/abs/2502.12029v3 .

- Zhao et al. [20233] Qifang Zhao, Weidong Ren, Tianyu Li, Xiaoxiao Xu, and Hong Liu. Graphgpt: Generative pre-trained graph eulerian transformer, arXiv preprint arXiv:2401.00529v3, 20233. URL https://arxiv.org/abs/2401.00529v3 .

- Zhao et al. [20244] Ruilin Zhao, Feng Zhao, Long Wang, Xianzhi Wang, and Guandong Xu. Kg-cot: Chain-of-thought prompting of large language models over knowledge graphs for knowledge-aware question answering. International Joint Conference on Artificial Intelligence , 20244.

- Zhao et al. [20252] Shangziqi Zhao, Jiahao Yuan, Guisong Yang, and Usman Naseem. Can pruning improve reasoning? revisiting long-cot compression with capability in mind for better reasoning, arXiv preprint arXiv:2505.14582, 20252. URL https://arxiv.org/abs/2505.14582v1 .

- Zhao et al. [20234] Shitian Zhao, Zhuowan Li, Yadong Lu, Alan L. Yuille, and Yan Wang. Causal-cog: A causal-effect look at context generation for boosting multi-modal language models. Computer Vision and Pattern Recognition , 20234.

- Zhao et al. [2021] Tony Zhao, Eric Wallace, Shi Feng, D. Klein, and Sameer Singh. Calibrate before use: Improving few-shot performance of language models. International Conference on Machine Learning , 2021.

- Zhao et al. [20253] Weixiang Zhao, Xingyu Sui, Jiahe Guo, Yulin Hu, Yang Deng, Yanyan Zhao, Bing Qin, Wanxiang Che, Tat-Seng Chua, and Ting Liu. Trade-offs in large reasoning models: An empirical analysis of deliberative and adaptive reasoning over foundational capabilities, arXiv preprint arXiv:2503.17979, 20253. URL https://arxiv.org/abs/2503.17979v1 .

- Zhao et al. [20254] Yibo Zhao, Jiapeng Zhu, Ye Guo, Kangkang He, and Xiang Li. E 2 graphrag: Streamlining graph-based rag for high efficiency and effectiveness. arXiv preprint, 20254.

- Zheng et al. [2024] Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, and Yu Su. Gpt-4v(ision) is a generalist web agent, if grounded. International Conference on Machine Learning , 2024.

- Zheng et al. [20242] Changmeng Zheng, Dayong Liang, Wengyu Zhang, Xiao Wei, Tat seng Chua, and Qing Li. A picture is worth a graph: A blueprint debate paradigm for multimodal reasoning. ACM Multimedia , 20242.

- Zheng et al. [20243] Chuanyang Zheng, Yihang Gao, Han Shi, Minbin Huang, Jingyao Li, Jing Xiong, Xiaozhe Ren, Michael Ng, Xin Jiang, Zhenguo Li, and Yu Li. Dape: Data-adaptive positional encoding for length extrapolation. Neural Information Processing Systems , 20243.

- Zheng et al. [2023] Chunmo Zheng, Saika Wong, Xing Su, Yinqiu Tang, Ahsan Nawaz, and Mohamad Kassem. Automating construction contract review using knowledge graph-enhanced large language models. Automation in Construction , 2023.

- Zheng et al. [20244] Junhao Zheng, Shengjie Qiu, Chengming Shi, and Qianli Ma. Towards lifelong learning of large language models: A survey. ACM Computing Surveys , 20244.

- Zheng et al. [2025] Junhao Zheng, Xidi Cai, Qiuke Li, Duzhen Zhang, Zhongzhi Li, Yingying Zhang, Le Song, and Qianli Ma. Lifelongagentbench: Evaluating llm agents as lifelong learners, arXiv preprint arXiv:2505.11942, 2025. URL https://arxiv.org/abs/2505.11942v3 .

- Zheng et al. [20232] Longtao Zheng, R. Wang, and Bo An. Synapse: Trajectory-as-exemplar prompting with memory for computer control. International Conference on Learning Representations , 20232.

- Zheng et al. [20245] Longtao Zheng, Rundong Wang, Xinrun Wang, and Bo An. Synapse: Trajectory-as-exemplar prompting with memory for computer control, arXiv preprint arXiv:2306.07863, 20245. URL https://arxiv.org/abs/2306.07863 .

- Zheng et al. [20252] Xu Zheng, Chenfei Liao, Yuqian Fu, Kaiyu Lei, Yuanhuiyi Lyu, Lutao Jiang, Bin Ren, Jialei Chen, Jiawen Wang, Chengxin Li, Linfeng Zhang, D. Paudel, Xuanjing Huang, Yu-Gang Jiang, N. Sebe, Dacheng Tao, L. V. Gool, and Xuming Hu. Mllms are deeply affected by modality bias, arXiv preprint arXiv:2505.18657v1, 20252. URL https://arxiv.org/abs/2505.18657v1 .

- Zheng et al. [20253] Yuxiang Zheng, Dayuan Fu, Xiangkun Hu, Xiaojie Cai, Lyumanshan Ye, Pengrui Lu, and Pengfei Liu. Deepresearcher: Scaling deep research via reinforcement learning in real-world environments, arXiv preprint arXiv:2504.03160, 20253. URL https://arxiv.org/abs/2504.03160v4 .

- Zhong et al. [2024] Li Zhong, Zilong Wang, and Jingbo Shang. Debug like a human: A large language model debugger via verifying runtime execution step by step. Annual Meeting of the Association for Computational Linguistics , 2024.

- Zhong et al. [20242] Rui Zhong, Yang Cao, Jun Yu, and M. Munetomo. Large language model assisted adversarial robustness neural architecture search. 2024 6th International Conference on Data-driven Optimization of Complex Systems (DOCS) , 20242.

- Zhong et al. [2023] Wanjun Zhong, Lianghong Guo, Qi-Fei Gao, He Ye, and Yanlin Wang. Memorybank: Enhancing large language models with long-term memory. AAAI Conference on Artificial Intelligence , 2023.

- Zhong et al. [20232] Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. Memorybank: Enhancing large language models with long-term memory, arXiv preprint arXiv:2305.10250, 20232. URL https://arxiv.org/abs/2305.10250 .

- Zhou et al. [2023] Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang. Language agent tree search unifies reasoning acting and planning in language models. International Conference on Machine Learning , 2023.

- Zhou et al. [2022] Bin Zhou, Xingwang Shen, Yuqian Lu, Xinyu Li, B. Hua, Tianyuan Liu, and Jinsong Bao. Semantic-aware event link reasoning over industrial knowledge graph embedding time series data. International Journal of Production Research , 2022.

- Zhou et al. [20222] Denny Zhou, Nathanael Scharli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, D. Schuurmans, O. Bousquet, Quoc Le, and Ed H. Chi. Least-to-most prompting enables complex reasoning in large language models. International Conference on Learning Representations , 20222.

- Zhou et al. [2025] Huichi Zhou, Kin-Hei Lee, Zhonghao Zhan, Yue Chen, Zhenhao Li, Zhaoyang Wang, Hamed Haddadi, and Emine Yilmaz. Trustrag: Enhancing robustness and trustworthiness in rag, arXiv preprint arXiv:2501.00879, 2025. URL https://arxiv.org/abs/2501.00879 .

- Zhou et al. [20232] Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig. Webarena: A realistic web environment for building autonomous agents. International Conference on Learning Representations , 20232.

- Zhou et al. [20233] Wangchunshu Zhou, Y. Jiang, Long Li, Jialong Wu, Tiannan Wang, Shi Qiu, Jintian Zhang, Jing Chen, Ruipu Wu, Shuai Wang, Shiding Zhu, Jiyu Chen, Wentao Zhang, Xiangru Tang, Ningyu Zhang, Huajun Chen, Peng Cui, and Mrinmaya Sachan. Agents: An open-source framework for autonomous language agents, arXiv preprint arXiv:2309.07870, 20233. URL https://arxiv.org/abs/2309.07870v3 .

- Zhou et al. [20252] Yingli Zhou, Yaodong Su, Youran Sun, Shu Wang, Taotao Wang, Runyuan He, Yongwei Zhang, Sicong Liang, Xilin Liu, Yuchi Ma, and Yixiang Fang. In-depth analysis of graph-based rag in a unified framework, arXiv preprint arXiv:2503.04338, 20252. URL https://arxiv.org/abs/2503.04338v1 .

- Zhou and Ai [2024] Yuhang Zhou and Wei Ai. Teaching-assistant-in-the-loop: Improving knowledge distillation from imperfect teacher models in low-budget scenarios. Annual Meeting of the Association for Computational Linguistics , 2024.

- Zhou et al. [2024] Yujia Zhou, Yan Liu, Xiaoxi Li, Jiajie Jin, Hongjin Qian, Zheng Liu, Chaozhuo Li, Zhicheng Dou, Tsung-Yi Ho, and Philip S. Yu. Trustworthiness in retrieval-augmented generation systems: A survey, arXiv preprint arXiv:2409.10102, 2024. URL https://arxiv.org/abs/2409.10102v1 .

- Zhou et al. [20234] Zhehua Zhou, Jiayang Song, Kunpeng Yao, Zhan Shu, and Lei Ma. Isr-llm: Iterative self-refined large language model for long-horizon sequential task planning. IEEE International Conference on Robotics and Automation , 20234.

- Zhou et al. [20242] Zihan Zhou, Chong Li, Xinyi Chen, Shuo Wang, Yu Chao, Zhili Li, Haoyu Wang, Rongqiao An, Qi Shi, Zhixing Tan, Xu Han, Xiaodong Shi, Zhiyuan Liu, and Maosong Sun. Llm × \times × mapreduce: Simplified long-sequence processing using large language models, arXiv preprint arXiv:2410.09342, 20242. URL https://arxiv.org/abs/2410.09342v1 .

- Zhou et al. [20253] Zijian Zhou, Ao Qu, Zhaoxuan Wu, Sunghwan Kim, Alok Prakash, Daniela Rus, Jinhua Zhao, B. Low, and P. Liang. Mem1: Learning to synergize memory and reasoning for efficient long-horizon agents, arXiv preprint arXiv:2506.15841, 20253. URL https://arxiv.org/abs/2506.15841v1 .

- Zhu et al. [2024] Andrew Zhu, Liam Dugan, and Christopher Callison-Burch. Redel: A toolkit for llm-powered recursive multi-agent systems. Conference on Empirical Methods in Natural Language Processing , 2024.

- Zhu et al. [2023] Dawei Zhu, Nan Yang, Liang Wang, Yifan Song, Wenhao Wu, Furu Wei, and Sujian Li. Pose: Efficient context window extension of llms via positional skip-wise training. International Conference on Learning Representations , 2023.

- Zhu [2023] Hongyin Zhu. Metaaid 2.5: A secure framework for developing metaverse applications via large language models. arXiv preprint, 2023.

- Zhu et al. [2021] Jason Zhu, Yanling Cui, Yuming Liu, Hao Sun, Xue Li, Markus Pelger, Liangjie Zhang, Tianqi Yan, Ruofei Zhang, and Huasha Zhao. Textgnn: Improving text encoder via graph neural network in sponsored search. The Web Conference , 2021.

- Zhu et al. [2025] Jiachen Zhu, Menghui Zhu, Renting Rui, Rong Shan, Congmin Zheng, Bo Chen, Yunjia Xi, Jianghao Lin, Weiwen Liu, Ruiming Tang, Yong Yu, and Weinan Zhang. Evolutionary perspectives on the evaluation of llm-based ai agents: A comprehensive survey, arXiv preprint arXiv:2506.11102, 2025. URL https://arxiv.org/abs/2506.11102v1 .

- Zhu et al. [20252] Jinguo Zhu, Weiyun Wang, Zhe Chen, Zhaoyang Liu, Shenglong Ye, Lixin Gu, Yuchen Duan, Hao Tian, Weijie Su, Jie Shao, Zhangwei Gao, Erfei Cui, Yue Cao, Yangzhou Liu, Haomin Wang, Weiye Xu, Hao Li, Jiahao Wang, Han Lv, Dengnian Chen, Songze Li, Yinan He, Tan Jiang, Jiapeng Luo, Yi Wang, Cong He, Botian Shi, Xingcheng Zhang, Wenqi Shao, Junjun He, Ying Xiong, Wenwen Qu, Peng Sun, Penglong Jiao, Lijun Wu, Kai Zhang, Hui Deng, Jiaye Ge, Kaiming Chen, Limin Wang, Min Dou, Lewei Lu, Xizhou Zhu, Tong Lu, Dahua Lin, Yu Qiao, Jifeng Dai, and Wenhai Wang. Internvl3: Exploring advanced training and test-time recipes for open-source multimodal models, arXiv preprint arXiv:2504.10479v3, 20252. URL https://arxiv.org/abs/2504.10479v3 .

- Zhu et al. [20232] Mingwei Zhu, Leigang Sha, Yu Shu, Kangjia Zhao, Tiancheng Zhao, and Jianwei Yin. Benchmarking sequential visual input reasoning and prediction in multimodal large language models, arXiv preprint arXiv:2310.13473v1, 20232. URL https://arxiv.org/abs/2310.13473v1 .

- Zhu et al. [20253] Rongzhi Zhu, Xiangyu Liu, Zequn Sun, Yiwei Wang, and Wei Hu. Mitigating lost-in-retrieval problems in retrieval augmented multi-hop question answering. 20253.

- Zhu et al. [20254] Rongzhi Zhu, Yi Liu, Zequn Sun, Yiwei Wang, and Wei Hu. When can large reasoning models save thinking? mechanistic analysis of behavioral divergence in reasoning. 20254.

- Zhu et al. [20255] Runchuan Zhu, Zinco Jiang, Jiang Wu, Zhipeng Ma, Jiahe Song, Fengshuo Bai, Dahua Lin, Lijun Wu, and Conghui He. Grait: Gradient-driven refusal-aware instruction tuning for effective hallucination mitigation. 20255.

- Zhu et al. [20256] Runchuan Zhu, Zhipeng Ma, Jiang Wu, Junyuan Gao, Jiaqi Wang, Dahua Lin, and Conghui He. Utilize the flow before stepping into the same river twice: Certainty represented knowledge flow for refusal-aware instruction tuning. In Proceedings of the AAAI Conference on Artificial Intelligence , volume 39, pages 26157–26165, 20256.

- Zhu et al. [20242] Tongyao Zhu, Qian Liu, L. Pang, Zhengbao Jiang, Min-Yen Kan, and Min Lin. Beyond memorization: The challenge of random memory access in language models. Annual Meeting of the Association for Computational Linguistics , 20242.

- Zhu et al. [20233] Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei Lu, Xiaogang Wang, Yu Qiao, Zhaoxiang Zhang, and Jifeng Dai. Ghost in the minecraft: Generally capable agents for open-world environments via large language models with text-based knowledge and memory, arXiv preprint arXiv:2305.17144, 20233. URL https://arxiv.org/abs/2305.17144 .

- Zhu et al. [20257] Yue Zhu, Hao Yu, Chen Wang, Zhuoran Liu, and Eun Kyung Lee. Towards efficient key-value cache management for prefix prefilling in llm inference, arXiv preprint arXiv:2505.21919, 20257. URL https://arxiv.org/abs/2505.21919v1 .

- Zhu et al. [20243] Zhengqiu Zhu, Yong Zhao, Bin Chen, S. Qiu, Kai Xu, Quanjun Yin, Jin-Yu Huang, Zhong Liu, and Fei Wang. Conversational crowdsensing: A parallel intelligence powered novel sensing approach, arXiv preprint arXiv:2402.06654, 20243. URL https://arxiv.org/abs/2402.06654v1 .

- Zhu et al. [20258] Zulun Zhu, Tiancheng Huang, Kai Wang, Junda Ye, Xinghe Chen, and Siqiang Luo. Graph-based approaches and functionalities in retrieval-augmented generation: A comprehensive survey, arXiv preprint arXiv:2504.10499, 20258. URL https://arxiv.org/abs/2504.10499v1 .

- Zhuang et al. [2024] Alex Zhuang, Ge Zhang, Tianyu Zheng, Xinrun Du, Junjie Wang, Weiming Ren, Stephen W. Huang, Jie Fu, Xiang Yue, and Wenhu Chen. Structlm: Towards building generalist models for structured knowledge grounding, arXiv preprint arXiv:2402.16671, 2024. URL https://arxiv.org/abs/2402.16671v7 .

- Zhuang et al. [2023] Yuchen Zhuang, Yue Yu, Kuan Wang, Haotian Sun, and Chao Zhang. Toolqa: A dataset for llm question answering with external tools. Neural Information Processing Systems , 2023.

- Zhuang et al. [2025] Zhixiong Zhuang, Maria-Irina Nicolae, Hui-Po Wang, and Mario Fritz. Proxyprompt: Securing system prompts against prompt extraction attacks, arXiv preprint arXiv:2505.11459, 2025. URL https://arxiv.org/abs/2505.11459v1 .

- Zhuang et al. [20242] Ziyuan Zhuang, Zhiyang Zhang, Sitao Cheng, Fangkai Yang, Jia Liu, Shujian Huang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, and Qi Zhang. Efficientrag: Efficient retriever for multi-hop question answering. In In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing , pages 3392–3411, 20242.

- Zong et al. [2024] Chang Zong, Yuchen Yan, Weiming Lu, Eliot Huang, Jian Shao, and Y. Zhuang. Triad: A framework leveraging a multi-role llm-based agent to solve knowledge base question answering. Conference on Empirical Methods in Natural Language Processing , 2024.

- Zong et al. [20242] Yongshuo Zong, Ondrej Bohdal, and Timothy M. Hospedales. Vl-icl bench: The devil in the details of benchmarking multimodal in-context learning. arXiv preprint, 20242.

- Zong et al. [20243] Yongshuo Zong, Ondrej Bohdal, and Timothy M. Hospedales. Vl-icl bench: The devil in the details of multimodal in-context learning. International Conference on Learning Representations , 20243.

- Zou et al. [2025] Henry Peng Zou, Wei-Chieh Huang, Yaozu Wu, Yankai Chen, Chunyu Miao, Hoang Nguyen, Yue Zhou, Weizhi Zhang, Liancheng Fang, Langzhou He, Yangning Li, Yuwei Cao, Dongyuan Li, Renhe Jiang, and Philip S. Yu. A survey on large language model based human-agent systems. arXiv preprint, 2025.

- Zou et al. [2023] Tao Zou, Le Yu, Yifei Huang, Leilei Sun, and Bo Du. Pretraining language models with text-attributed heterogeneous graphs. Conference on Empirical Methods in Natural Language Processing , 2023.

- Zweiger et al. [2025] Adam Zweiger, Jyothish Pari, Han Guo, Ekin Akyürek, Yoon Kim, and Pulkit Agrawal. Self-adapting language models, arXiv preprint arXiv:2506.10943, 2025. URL https://arxiv.org/abs/2506.10943v1 .
