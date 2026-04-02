---
version: source-capture.v1
article_id: art-2026-03-04-007
ticket_id: ticket-import-art-2026-03-04-007
source_url: https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/
canonical_url: https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps
source_title: 'Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic
  AI Apps | Microsoft Foundry Blog'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-07T19:27:15Z'
---
# Source Capture

## Title

Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps | Microsoft Foundry Blog

## Body

Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps | Microsoft Foundry Blog
Skip to main content
Microsoft
Dev Blogs
Dev Blogs
Dev Blogs
Home
Developer
Microsoft for Developers
Visual Studio
Visual Studio Code
Develop from the cloud
All things Azure
Xcode
DevOps
Windows Developer
ISE Developer
Azure SDK
Command Line
Aspire
Technology
DirectX
Semantic Kernel
Languages
C++
C#
F#
TypeScript
PowerShell Team
Python
Java
Java Blog in Chinese
Go
.NET
All .NET posts
.NET Aspire
.NET MAUI
AI
ASP.NET Core
Blazor
Entity Framework
NuGet
Servicing
.NET Blog in Chinese
Platform Development
#ifdef Windows
Microsoft Foundry
Azure Government
Azure VM Runtime Team
Bing Dev Center
Microsoft Edge Dev
Microsoft Azure
Microsoft 365 Developer
Microsoft Entra Identity Developer
Old New Thing
Power Platform
Data Development
Azure Cosmos DB
Azure Data Studio
Azure SQL
OData
Revolutions R
Unified Data Model (IDEAs)
Microsoft Entra PowerShell
More
Search
Search
No results
Cancel
Dev Blogs
Microsoft Foundry Blog
Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps
October 1st, 2025
19 reactions
Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps
Takuto
,
Shawn
,
Elijah
Show more
Create the future
Securely design, customize, and manage AI applications and agents at scale with Microsoft Foundry.
Get started
Why agents need a new foundation
Over the last year, developers have been experimenting with AI agents in every imaginable form. Agents are not just chatbots or copilots — they are autonomous software components that can reason about goals, call tools and APIs, collaborate with other agents, and adapt dynamically. Whether it’s a retrieval agent for research, a coding agent embedded in a dev workflow, or a compliance agent ensuring policy enforcement, agents are becoming the next layer of application logic.
Yet despite the excitement, the path from prototype to production has been fraught with obstacles . Many of the most popular open-source frameworks are fragmented, each with their own APIs and abstractions. Local development rarely maps cleanly to cloud deployments. And most importantly, enterprise readiness is missing : observability, compliance hooks, security, and long-running durability are table stakes in OSS frameworks.
At Microsoft, we’ve had a front-row seat to this problem. With Semantic Kernel , we gave developers a stable SDK with connectors into enterprise systems, content moderation, and telemetry. With AutoGen , pioneered in Microsoft Research, we opened the door to experimental multi-agent orchestration patterns that inspired the community. Both had passionate users — but each had gaps.
Developers asked us: why can’t we have both — the innovation of AutoGen and the trust and stability of Semantic Kernel — in one unified framework?
That’s exactly why we built the Microsoft Agent Framework .
Introducing Microsoft Agent Framework
Microsoft Agent Framework is an open-source SDK and runtime designed to let developers build, deploy, and manage sophisticated multi-agent systems with ease. It unifies the enterprise-ready foundations of Semantic Kernel with the innovative orchestration of AutoGen , so teams no longer have to choose between experimentation and production.
Semantic Kernel
AutoGen
Microsoft Agent Framework
Focus
Stable SDK with enterprise connectors, workflows, and observability
Experimental multi-agent orchestration from research
Unified SDK combining innovation + enterprise readiness
Interop
Plugins, connectors, and support for MCP, A2A, OpenAPI
Tool integration supported; lacks standardized cross-runtime protocols
Built-in connectors, MCP + A2A + OpenAPI
Memory
Multiple vector store connectors and memory store abstraction (e.g. Azure SQL Elasticsearch, MongoDB)
Support for in-memory / buffer history + external vector store memory options (ChromaDB, Mem0, etc)
Pluggable memory across stores (first-party and third-party), persistent & adaptive memory stored with retrieval, hybrid appraoches
Orchestration
Deterministic + dynamic orchestration (Agent Framework, Process Framework)
Dynamic LLM orchestration (debate, reflection, facilitator/worker, group chat)
Deterministic + dynamic orchestration (Agent Orchestration, Workflow Orchestration)
Enterprise readiness
Telemetry, observability, compliance hooks
Minimal
Observability, approvals, CI/CD, long-running durability, hydration
With Microsoft Agent Framework, you get:
Open standards & interoperability — MCP, A2A, and OpenAPI ensure agents are portable and vendor-neutral.
Pipeline for research-to-production — bleeding-edge orchestration patterns from Microsoft Research are now ready for enterprise use.
Community-driven extensibility — modular by design, with connectors, pluggable memory, and declarative agent definitions.
Enterprise readiness — built-in observability, approvals, security, and long-running durability.
Microsoft Agent Framework doesn’t replace Semantic Kernel and AutoGen — it builds on them. By consolidating their strengths, it gives developers one foundation to move from experimentation to enterprise deployment without compromise. Microsoft Agent Framework supports both Agent Orchestration (LLM-driven, creative reasoning and decision-making) and Workflow Orchestration (business-logic driven, deterministic multi-agent workflows). Together, they allow teams to choose the right approach for the problem: flexible collaboration for open-ended tasks, or structured workflows for repeatable enterprise processes.
Looking ahead, Microsoft Agent Framework further advances integrations across Microsoft’s agent development stack, including the integration with the Microsoft 365 Agents SDK and a shared runtime with Azure AI Foundry Agent Service . The Microsoft 365 Agents SDK is the pro-code toolkit that lets developers build full-stack, multi-channel agents and publish them across Microsoft 365 Copilot, Teams, web, and other surfaces, with deep interoperability into Copilot Studio’s low-code connectors and Microsoft 365 Copilot custom engine agents. By converging this SDK with Microsoft Agent Framework—and aligning it with the shared runtime used in Foundry Agent Service—developers will gain one unified set of abstractions to create, run, scale, and publish agents. This means you can prototype locally, debug with consistent telemetry, and then seamlessly move into scaled hosting with enterprise-grade observability, compliance, and security—all without rewriting your agents—and then publish them into any communication channels of choice where you want to surface your agents.
The Four Pillars of Agent Framework
Open Standards & Interoperability
Agents don’t exist in isolation — they need to connect to data, tools, and each other. Microsoft Agent Framework was built with open standards at its core, so developers can choose their integrations and ensure their systems remain portable across frameworks and clouds.
MCP (Model Context Protocol): Agents can dynamically discover and invoke external tools or data servers exposed over MCP. Microsoft Agent Framework makes it easy to connect to a growing ecosystem of MCP-compliant services without custom glue code.
Agent-to-Agent (A2A): Agents can collaborate across runtimes using structured, protocol-driven messaging. A2A support allows developers to create workflows where one agent retrieves data, another analyzes it, and a third validates results — even if they’re running in different frameworks or environments.
OpenAPI-first design: Any REST API with an OpenAPI specification can be imported as a callable tool instantly. Microsoft Agent Framework handles schema parsing, tool definition, and secure invocation so developers can leverage thousands of enterprise APIs without building wrappers by hand.
Cloud-agnostic runtime: Agents can run in containers, on-premises, or across multiple clouds, making them portable across environments. Developers can spin up a single agent with their preferred SDK (Azure OpenAI, OpenAI, etc.), add tools by wrapping existing methods as AIFunctions, and immediately connect to external APIs.
The latest update to the VS Code AI Toolkit brings a streamlined experience for building with the Microsoft Agent Framework , enabling developers to locally create, run, and visualize multi-agent workflows. These enhancements simplify the inner dev loop, making it easier to build, debug, and iterate on multi-agent systems within the familiar VS Code environment.
Pipeline for Research
Microsoft Agent Framework is designed to be the bridge between research innovation and enterprise-ready production . Many of the most exciting breakthroughs in multi-agent orchestration patterns come out of Microsoft Research in AutoGen, and the new framework makes those ideas usable in real-world systems without sacrificing durability, governance, or performance.
The framework supports:
Sequential orchestration for step-by-step workflows.
Concurrent orchestration where agents work in parallel.
Group chat orchestration where agents brainstorm collaboratively.
Handoff orchestration where responsibility moves between agents as context evolves.
Magentic orchestration where a manager agent builds and refines a dynamic task ledger, coordinating specialized agents (and sometimes humans) for complex, open-ended problems.
To serve both innovators and production-minded developers, Microsoft Agent Framework also provides an extension package for experimental features — a clearly labeled incubation channel where advanced users can try out cutting-edge capabilities from Microsoft Research and the open-source community. These features are transparent about their experimental status, while successful innovations graduate naturally into the stable framework.
These patterns — once prototypes — now run with durability, auditability, and enterprise controls. It’s the best of research innovation, matured for real-world use.
Extensible by Design & Community-Driven
Microsoft Agent Framework is 100% open source and designed to grow with the community. Its modular design makes it easy to extend, customize, and contribute.
Connectors to enterprise systems: Agent Framework inherits a broad set of built-in connectors (Azure AI Foundry, Microsoft Graph, Microsoft Fabric, SharePoint, Oracle, Amazon Bedrock, MongoDB, and a various SaaS system through Azure Logic Apps) so agents can work with enterprise data from day one.
Pluggable memory modules: Developers can choose Redis , Pinecone, Qdrant, Weaviate, Elasticsearch, Postgres, or their own store for conversational memory. Agent Framework provides the abstraction; you decide the backend.
Declarative agents : YAML or JSON definitions allow developers to specify prompts, roles, and tools declaratively. These files can be version-controlled, templatized, and shared across teams.
Community innovation: Agent Framework is designed to absorb community-driven orchestration strategies, new connectors, and best practices.
This means Microsoft Agent Framework is not a fixed product — it’s a living ecosystem , continuously shaped by contributions from Microsoft Research and the global OSS community.
Ready for Production
Microsoft Agent Framework isn’t just for experimentation — it was built for enterprise-grade deployment from the very beginning. It delivers the end-to-end tooling and runtime features needed to confidently move from prototype to scale, while integrating deeply with the Azure AI Foundry ecosystem.
Observability: OpenTelemetry can instrument and visualize every agent action, tool invocation, and orchestration step, making it easy to trace reasoning flows and monitor performance through Azure AI Foundry dashboards.
Secure Cloud Hosting: Agents will run natively on Azure AI Foundry with enterprise controls like virtual network integration, role-based access, private data handling, and built-in content safety.
Security & compliance: Azure AI Content Safety integration, Entra ID authentication, and structured logging mean Agent Framework agents can run in regulated industries.
Long-running durability: Agent threads and workflows can pause, resume, and recover from interruptions, with retry and error-handling logic ensuring long-running processes remain reliable at scale.
Human in the loop: For scenarios that require governance, tools can be marked as requiring human approval. Agent Framework automatically emits a pending approval request that can be routed to a UI or queue, then continues or denies execution accordingly. This works across local tools or remote service calls, ensuring sensitive operations remain under control.
CI/CD integration: The framework integrates directly into GitHub Actions and Azure DevOps pipelines, with telemetry flowing into Azure Monitor and Application Insights for enterprise-grade deployment and root-cause analysis.
With these capabilities, Microsoft Agent Framework makes it seamless to prototype locally, debug with rich telemetry, and then scale securely into production with the enterprise readiness that modern AI systems demand.
Customer Momentum
Enterprises across industries are already testing Microsoft Agent Framework in real-world scenarios:
KPMG is building Clara AI , a multi-agent system that automates audit testing and documentation. “Foundry Agent Service and Microsoft Agent Framework connect our agents to data and each other, and the governance and observability in Azure AI Foundry provide what KPMG firms need to be successful in a regulated industry” – Sebastian Stöckle, Global Head of Audit Innovation and AI, KPMG International
Commerzbank is piloting Microsoft Agent Framework to power avatar-driven customer support, enabling more natural, accessible, and compliant customer interactions. “The new Microsoft Agent Framework simplifies coding, reduces efforts and fully supports MCP for agentic solutions. We are really looking forward to the productive usage of container-based Azure AI Foundry agents, which significantly reduces workload in IT operations” – Gerald Ertl, Managing Director/Head of Digital Banking Solutions, Commerzbank AG
BMW: BMW is using Microsoft Agent Framework and Foundry Agent Service to orchestrate multi-agent systems that analyze terabytes of vehicle telemetry in near real time, enabling engineers to accelerate design cycles and spot issues earlier in testing. “Durability and observability are key for our operations. With multi-agent systems powered by Microsoft Agent Framework and Foundry Agent Service, engineers don’t just access data — they get insights they can act on immediately, cutting analysis from days to minutes.” – Christof Gebhart, Manager, Advanced Vehicle Measurement Technology, BMW
Fujitsu is embedding Microsoft Agent Framework into its integration services, enabling customers to safely adopt advanced orchestration strategies such as group chat and debate. “I believe it enables us to build multi-agent systems that emphasize coexistence between humans and AI and can truly accelerate our AI transformation” – Hirotaka Ito, Lead engineer of AI, Corporate Digital Unit, Fujitsu.
Citrix: Citrix is exploring how they can use agentic AI within VDI environments to improve enterprise productivity and efficiency . “We are excited about the Microsoft Agent Framework, which brings a modern, developer-first approach to building single- and multi-agent workflows. With support of key APIs and languages, and native adoption of emerging protocols for tool calling and observability, it enables intuitive development of agents on Azure AI Foundry, without compromising developer control. We are eager to leverage the framework to deliver enterprise-scale, production-ready AI solutions to our customers.” — George Tsolis, Distinguished Engineer, Citrix
Fractal: Fractal’s Cogentiq is an agentic AI platform that uses Microsoft Agent Framework to orchestrate and scale enterprise AI agents and workflows across industries. “Cogentiq leverages Microsoft Agent Framework to orchestrate and scale AI agents and workflows. Microsoft Agent framework’s ease of use, flexible agent development and deployment options and support for building complex multi-agentic workflows enables us to rapidly build, deploy, and manage multi-agent solutions across industries and functions. The Agent Framework allows both technical and business teams to innovate quickly, integrate with enterprise systems, and deliver value at scale through production-ready tools and access to industry-leading AI models. It takes care of the heavy lifting around model access, deployment, scaling, security, networking helping Fractal focus on solving our client’s industry and function specific business problems.” — Himanshu Nautiyal, Chief Product Officer, Fractal
TCS: Tata Consultancy Services is actively building a multi-agent practice on the Microsoft Agent Framework, with several initiatives underway that showcase their strategic investment and technical depth including agentic solutions for finance, IT operations, and retail. “Adopting Microsoft Agent Framework is not just a technological advancement, but a bold step towards reimagining industry value chains. By harnessing Agentic AI and Frontier models, we enable our teams to build flexible, scalable, enterprise-grade solutions that transform workflows and deliver value across platforms. True leadership is about empowering innovation, embracing change, and fostering an environment where agility and collaboration drive excellence.” – Girish Phadke, Head, Microsoft Azure Practice, TCS
Sitecore: Sitecore is building a solution to help marketers interact more seamlessly with the Sitecore platform by automating tasks across content supply chain, from creating and managing web experiences to digital assets, using intelligent agents. “By partnering with Microsoft to leverage its new Microsoft Agent Framework, Sitecore can bring together the best of both worlds: the flexibility to power fully non-deterministic agentic orchestrations and the reliability to run more deterministic, repeatable agents. At the same time, we benefit from Microsoft’s enterprise-grade observability and telemetry, ensuring that these orchestrations are not only powerful but also secure, measurable, and production-ready.” – Mo Cherif, VP of AI, Sitecore.
NTT DATA: Agentic AI value includes a complete ecosystem of solutions, services, and partners. NTT DATA is adopting the Microsoft Agent Framework in alignment with efforts to standardize its R&D approach for multi-agent management, enabling the company to deploy, manage, and optimize AI solutions across industries. This will help accelerate deployments, support complex process workflows that can be customized and replicated and make it easier to connect and orchestrate sophisticated models on behalf of clients. “By adopting the Microsoft Agent Framework, NTT DATA is not only further standardizing how we develop and manage multi-agent systems, but also accelerating how our clients realize value from AI. This initiative allows us to deliver faster, more scalable, and more governed AI solutions, while staying closely in step with Microsoft’s engineering roadmap.”- Charlie Doubek, Global VP, Agentic AI Services Leader, Cloud and Security, NTT DATA
MTech Systems: MTech Systems will use the new Agent Framework to orchestrate transactional data anomaly sweeps, human-in-the-loop approvals, and automated fixes – agent patterns that previously required extensive glue code. “The framework gives us a batteries-included developer experience and makes agent workflows far easier to build and run. Features like checkpointing and declarative YAML workflows will save us time and let us scale changes across hundreds of customer applications without redeploys ” – Barry Schulz, CTO, MTech Systems
TeamViewer : TeamViewer is embedding agentic AI into its IT support stack so that remote support agents can get real-time diagnostics, automated summarization, and contextual recommendations during sessions. “The framework strikes the right balance between technical depth and usability. Its intuitive design and modular structure make it easy for our teams to adopt quickly, while providing the scalability and flexibility we need for complex projects. That combination allows us to deliver value faster today and positions us well to take advantage of the enhancements still to come.” – Mei Dent, Chief Product and Technology Officer TeamViewer
Weights & Biases : Weights & Biases is collaborating with Microsoft to ensure developers can seamlessly train, track, and operationalize AI agents at scale. “The new Microsoft Agentic Framework makes building production-ready agents dramatically easier. With flexible orchestration, checkpointing to save time and compute, and built-in human-in-the-loop support, it tackles the real challenges teams face when moving from prototype to production “ – Phil Gurbacki, VP of Product, Weights & Biases
Elastic : Elasticsearch supports a native connector to Microsoft Agent Framework, enabling developers to seamlessly integrate enterprise data into intelligent agents and workflows. “Elasticsearch is the context engineering platform and vector database of choice for organizations to store and search their most valuable operational and business data. With the new Microsoft Agent Framework connector, developers can now bring the most relevant organizational context directly into intelligent agents and multi-agent workflows. This makes it easier than ever to build production-ready AI solutions that combine the reasoning power of agents with the speed and scale of Elasticsearch.” — Steve Kearns, General Manager Search Solutions, Elastic
These early stories highlight the dual promise of Microsoft Agent Framework: innovative enough to inspire new approaches, stable enough to deploy in production.
Path to Microsoft Agent Framework
Many customers are already using Semantic Kernel or AutoGen in production today. Both projects will remain supported but most investment is now focused on Microsoft Agent Framework. Developers using Semantic Kernel or AutoGen will find the transition straightforward:
For Semantic Kernel users:
Migration is straightforward: replace Kernel and plugin patterns with the Agent and Tool abstractions.
.NET developers move from Microsoft.SemanticKernel.* to the new Microsoft.Extensions.AI.* namespaces, with agents created directly from providers instead of requiring Kernel coupling.
Python developers can install the full package (pip install agent-framework) or just the components they need (e.g., agent-framework-azure-ai, agent-framework-redis).
Agents now manage threads natively, simplify invocation with RunAsync / RunStreamingAsync, and register tools inline without attributes or plugin wrappers.
Existing vector store integrations (Azure AI Search, Postgres, Cosmos DB, Redis, Elasticsearch, etc.) continue to work through connectors.
Plugins like Bing, Google, OpenAPI, and Microsoft Graph port directly as tools, often exposed via MCP or OpenAPI.
The net result: less boilerplate, simplified memory management, and alignment with open standards.
For AutoGen users:
AutoGen pioneered many orchestration patterns (GroupChat, GraphFlow, event-driven runtimes), which are now unified in Agent Framework under the Workflow abstraction.
The AssistantAgent maps directly to the new ChatAgent, which is multi-turn by default and continues tool invocation until a result is ready.
FunctionTool wrappers migrate to the @ai_function decorator, with automatic schema inference and support for hosted tools like code interpreter or web search.
Messaging is simplified: multiple message classes are replaced with a unified ChatMessage type, with explicit roles (USER, ASSISTANT, TOOL, SYSTEM).
Orchestration shifts from event-driven models to a typed, graph-based Workflow API that supports checkpointing, pause/resume, and human-in-the-loop flows.
Observability is richer and simpler, with OpenTelemetry support out of the box.
Most single-agent migrations require only light refactoring; multi-agent migrations benefit from the new Workflow model with stronger composability and durability.
This continuity means developers can preserve their existing investments while unlocking new capabilities. Microsoft Agent Framework is not a replacement for what came before — it is the natural evolution that unites innovation and stability. For more information about migration, see the documentation .
Get Started with Microsoft Agent Framework Today
Agents are fast becoming the next layer of application logic — reasoning about goals, calling tools, collaborating with each other, and adapting dynamically. With Microsoft Agent Framework, developers now have a single, open-source foundation that carries the best of research innovation into production with the durability, observability, and enterprise readiness required to scale.
This is the natural evolution of the journey that began with Semantic Kernel and AutoGen — and it’s only the beginning. By building in the open and co-creating with the developer community, Microsoft Agent Framework will continue to evolve as the foundation for next-generation multi-agent systems.
Download the SDK: aka.ms/AgentFramework
Explore documentation for more details: https://aka.ms/AgentFramework/Docs
See it in action: Watch demos on AI Show and Open at Microsoft
Learn step by step : Microsoft Learn modules for Agent Framework and AI Agents for Beginners
Join the Azure AI Foundry Discord to connect with developers and product groups, sharpen your AI skills, and stay inspired through real-time community. Join us for an AMA Tuesday 7 th October 9am PST: https://aka.ms/foundry/discord
19
3
87
Share on Facebook
Share on X
Share on Linkedin
Copy Link
-->
Category
A2A AIAgent MCP Microsoft Foundry
Topics
agents AI Development AI Tools ai-agents azure-openai Microsoft Foundry semantic-kernel
Share
Author
Takuto Higuchi
Sr Product Marketing Manager
Sr Product Marketing Manager
Shawn Henry
Principal Group Product Manager
Principal Group Product Manager
Elijah Straight
Product Manager for Microsoft Agent Framework
3 comments
Discussion is closed. Login to edit/delete existing comments.
Code of Conduct
Sort by :
Newest
Newest
Popular
Oldest
José Luis Latorre Millás -->
José Luis Latorre Millás
-->
October 8, 2025
2
-->
Collapse this comment
-->
Copy link
-->
-->
-->
-->
Hi,
The latest update to the VS Code AI Toolkit does not seem to bring any workflow visualizer... is that in a private preview? I have explored the toolkit documentation, tried to explore it but nothing seems to point to a workflow visualizer... so it is not yet in apparently - or I cannot seem to find it..
https://code.visualstudio.com/docs/intelligentapps/faq
There is a cool package called devui ( see https://github.com/microsoft/agent-framework/blob/main/python/packages/devui) but seems only for python so far...any intention to port it to .NET? or maybe it can also host a .NET workflow somehow? - have to dig into this...)
Thanks,
José
Read more Hi,
The latest update to the VS Code AI Toolkit does not seem to bring any workflow visualizer… is that in a private preview? I have explored the toolkit documentation, tried to explore it but nothing seems to point to a workflow visualizer… so it is not yet in apparently – or I cannot seem to find it..
https://code.visualstudio.com/docs/intelligentapps/faq
There is a cool package called devui ( see https://github.com/microsoft/agent-framework/blob/main/python/packages/devui ) but seems only for python so far…any intention to port it to .NET? or maybe it can also host a .NET workflow somehow? – have to dig into this…)
Thanks,
José
Read less
José Luis Latorre Millás -->
José Luis Latorre Millás
-->
October 9, 2025
1
-->
Collapse this comment
-->
Copy link
-->
-->
-->
-->
And I reply to myself after attending the Office Hours and asking directly to the team 😉
– VS Code AI Toolkit seems in “private preview” – me want please… can I have it?
– DevUi is only available in Python so far, will come to .NET but… not clear when…
Looks like I have to unrust my Python skills 😉
Thanks Elijah!!
Anbu -->
Anbu
-->
October 2, 2025
0
-->
Collapse this comment
-->
Copy link
-->
-->
-->
-->
is there a plan to support Java as well?
Read next
October 7, 2025
What’s new in Azure AI Foundry | September 2025
Nick Brady
October 14, 2025
The Developer’s Guide to Smarter Fine-tuning: Unlock custom AI for every business challenge
Malena,
Jacques
Stay informed
Get notified when new posts are published.
Email *
Country/Region *
Select... United States Afghanistan Åland Islands Albania Algeria American Samoa Andorra Angola Anguilla Antarctica Antigua and Barbuda Argentina Armenia Aruba Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bermuda Bhutan Bolivia Bonaire Bosnia and Herzegovina Botswana Bouvet Island Brazil British Indian Ocean Territory British Virgin Islands Brunei Bulgaria Burkina Faso Burundi Cabo Verde Cambodia Cameroon Canada Cayman Islands Central African Republic Chad Chile China Christmas Island Cocos (Keeling) Islands Colombia Comoros Congo Congo (DRC) Cook Islands Costa Rica Côte dIvoire Croatia Curaçao Cyprus Czechia Denmark Djibouti Dominica Dominican Republic Ecuador Egypt El Salvador Equatorial Guinea Eritrea Estonia Eswatini Ethiopia Falkland Islands Faroe Islands Fiji Finland France French Guiana French Polynesia French Southern Territories Gabon Gambia Georgia Germany Ghana Gibraltar Greece Greenland Grenada Guadeloupe Guam Guatemala Guernsey Guinea Guinea-Bissau Guyana Haiti Heard Island and McDonald Islands Honduras Hong Kong SAR Hungary Iceland India Indonesia Iraq Ireland Isle of Man Israel Italy Jamaica Jan Mayen Japan Jersey Jordan Kazakhstan Kenya Kiribati Korea Kosovo Kuwait Kyrgyzstan Laos Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macau SAR Madagascar Malawi Malaysia Maldives Mali Malta Marshall Islands Martinique Mauritania Mauritius Mayotte Mexico Micronesia Moldova Monaco Mongolia Montenegro Montserrat Morocco Mozambique Myanmar Namibia Nauru Nepal Netherlands New Caledonia New Zealand Nicaragua Niger Nigeria Niue Norfolk Island North Macedonia Northern Mariana Islands Norway Oman Pakistan Palau Palestinian Authority Panama Papua New Guinea Paraguay Peru Philippines Pitcairn Islands Poland Portugal Puerto Rico Qatar Réunion Romania Rwanda Saba Saint Barthélemy Saint Kitts and Nevis Saint Lucia Saint Martin Saint Pierre and Miquelon Saint Vincent and the Grenadines Samoa San Marino São Tomé and Príncipe Saudi Arabia Senegal Serbia Seychelles Sierra Leone Singapore Sint Eustatius Sint Maarten Slovakia Slovenia Solomon Islands Somalia South Africa South Georgia and South Sandwich Islands South Sudan Spain Sri Lanka St Helena Ascension Tristan da Cunha Suriname Svalbard Sweden Switzerland Taiwan Tajikistan Tanzania Thailand Timor-Leste Togo Tokelau Tonga Trinidad and Tobago Tunisia Turkey Turkmenistan Turks and Caicos Islands Tuvalu U.S. Outlying Islands U.S. Virgin Islands Uganda Ukraine United Arab Emirates United Kingdom Uruguay Uzbekistan Vanuatu Vatican City Venezuela Vietnam Wallis and Futuna Yemen Zambia Zimbabwe
I would like to receive the Microsoft Foundry Blog Newsletter. Privacy Statement.
Subscribe
Follow this blog
Are you sure you wish to delete this
comment?
× -->
OK
Cancel
Sign in
Theme
Insert/edit link
Close
Enter the destination URL
URL
Link Text
Open link in a new tab
Or link to existing content
Search
No search term specified. Showing recent items.
Search or use up and down arrow keys to select an item.
Cancel
Code Block
×
Paste your code snippet
Ok
Cancel
What's new
Surface Pro
Surface Laptop
Surface Laptop Studio 2
Copilot for organizations
Copilot for personal use
AI in Windows
Explore Microsoft products
Windows 11 apps
Microsoft Store
Account profile
Download Center
Microsoft Store support
Returns
Order tracking
Certified Refurbished
Microsoft Store Promise
Flexible Payments
Education
Microsoft in education
Devices for education
Microsoft Teams for Education
Microsoft 365 Education
How to buy for your school
Educator training and development
Deals for students and parents
AI for education
Business
Microsoft AI
Microsoft Security
Dynamics 365
Microsoft 365
Microsoft Power Platform
Microsoft Teams
Microsoft 365 Copilot
Small Business
Developer & IT
Azure
Microsoft Developer
Microsoft Learn
Support for AI marketplace apps
Microsoft Tech Community
Microsoft Marketplace
Marketplace Rewards
Visual Studio
Company
Careers
About Microsoft
Company news
Privacy at Microsoft
Investors
Diversity and inclusion
Accessibility
Sustainability
Your Privacy Choices
Consumer Health Privacy
Sitemap
Contact Microsoft
Privacy
Manage cookies
Terms of use
Trademarks
Safety & eco
Recycling
About our ads
© Microsoft 2026

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-04-007.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-04-007.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-04-007.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
