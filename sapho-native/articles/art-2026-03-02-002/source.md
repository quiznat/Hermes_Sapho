---
version: source-capture.v1
article_id: art-2026-03-02-002
ticket_id: ticket-import-art-2026-03-02-002
source_url: https://azure.microsoft.com/en-us/blog/agent-factory-the-new-era-of-agentic-ai-common-use-cases-and-design-patterns/
canonical_url: https://azure.microsoft.com/en-us/blog/agent-factory-the-new-era-of-agentic-ai-common-use-cases-and-design-patterns
source_title: "Agent Factory: The new era of agentic AI\u2014common use cases and\
  \ design patterns | Microsoft Azure Blog"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-07T19:27:07Z'
---
# Source Capture

## Title

Agent Factory: The new era of agentic AI—common use cases and design patterns | Microsoft Azure Blog

## Body

Agent Factory: The new era of agentic AI—common use cases and design patterns | Microsoft Azure Blog
Skip to content
Skip to main content
Microsoft
Azure
Azure
Azure
Home
Explore
Products
Popular
Popular
View all products (200+)
Microsoft Foundry
Foundry Agent Service
Azure Copilot
Observability in Foundry Control Plane
GitHub Copilot
Azure DevOps
Azure Kubernetes Service (AKS)
Azure Cosmos DB
Azure Database for PostgreSQL
Azure Arc​
Microsoft Foundry
Microsoft Foundry
Microsoft Foundry
Foundry Models
Foundry Agent Service
Foundry IQ
Foundry Tools
Azure OpenAI in Foundry Models
Azure Content Understanding in Foundry Tools
Observability in Foundry Control Plane
Azure Speech in Foundry Tools
Azure Machine Learning
Databases + analytics
Databases + analytics
View all databases
Azure Cosmos DB
Azure DocumentDB
Azure SQL
Azure Database for PostgreSQL
Azure Managed Redis
Microsoft Fabric
Azure Databricks
Azure Synapse Analytics
Compute
Compute
Linux virtual machines in Azure
SQL Server on Azure Virtual Machines
Windows Server
Azure Functions
Azure Virtual Machine Scale Sets
Azure Spot Virtual Machines
Azure Container Apps
Azure Compute Fleet
Containers
Containers
Azure Container Apps
Azure Kubernetes Service (AKS)
Azure Kubernetes Fleet Manager
Azure Container Registry
Azure Red Hat OpenShift
Azure Container Instances​
Azure Container Storage
Hybrid + multicloud
Hybrid + multicloud
Azure Arc​
Azure Local
Microsoft Defender for Cloud
Azure IoT Edge
Azure Monitor
Microsoft Sentinel
Azure Migrate
Azure Storage Mover
Solutions
Featured
Featured
View all solutions (40+)
Cloud solutions for small and medium businesses
Azure cloud migration and modernization center
Data analytics for AI
Azure AI Infrastructure
Adaptive cloud
Azure networking and network security
SAP on the Microsoft Cloud
Azure Databases
Azure Integration Services
AI
AI
Azure AI Apps and AI Agents
Responsible AI with Azure
Azure AI Infrastructure
Knowledge mining
Hugging Face on Azure
Machine learning operations (MLOps)
Application development
Application development
Development and testing
DevOps
DevSecOps
Integration Services
Serverless computing
Low-code application development on Azure
Cloud migration and modernization
Cloud migration and modernization
Migration and modernization center
.NET apps migration
Development and testing
SQL Server migration
Linux on Azure
SAP on the Microsoft Cloud
Oracle on Azure
Azure confidential computing
Azure storage migration solutions
Hybrid Cloud and infrastructure
Hybrid Cloud and infrastructure
Adaptive cloud
Resiliency
High-performance computing (HPC)
Business-critical applications
Quantum computing
Infrastructure as a service (IaaS)
Resources
Resources
Reference architectures
Resources for accelerating growth
Microsoft Marketplace
Azure Essentials
Azure Accelerate
Microsoft Cloud Adoption Framework for Azure
Azure Well-Architected Framework
FinOps on Azure
Pricing
How to buy
How to buy
Azure pricing
Free Azure services
Azure account
Flexible purchase options
Azure offers and benefits
Pricing tools and resources
Pricing tools and resources
Pricing calculator
Optimize your costs
FinOps on Azure
Partners
Software Development Companies
Microsoft Marketplace
Find a partner
Resources
Learning
Learning
Get started with Azure
Customer stories
Analyst reports, white papers, and e-books
Videos
Learn more about cloud computing
Technical resources
Technical resources
Documentation
Get the Azure mobile app
Developer resources
Quickstart templates
Resources for startups
Community
Community
Developer community
Students
Azure for partners
What's new
What's new
Blog
Events and Webinars
Learn
Support
Contact Sales
Get started with Azure
Sign in
More
All Microsoft
Global
Microsoft 365
Teams
Copilot
Windows
Surface
Xbox
Deals
Small Business
Support
Software
Software
Windows Apps
Outlook
OneDrive
Microsoft Teams
OneNote
Microsoft Edge
Moving from Skype to Teams
PCs & Devices
PCs & Devices
Computers
Shop Xbox
Accessories
VR & mixed reality
Certified Refurbished
Trade-in for cash
Entertainment
Entertainment
Xbox Game Pass Ultimate
PC Game Pass
Xbox games
PC games
Business
Business
Microsoft AI
Microsoft Security
Dynamics 365
Microsoft 365 for business
Microsoft Power Platform
Windows 365
Small Business
Digital Sovereignty
Developer & IT
Developer & IT
Azure
Microsoft Developer
Microsoft Learn
Support for AI marketplace apps
Microsoft Tech Community
Microsoft Marketplace
Marketplace Rewards
Visual Studio
Other
Other
Microsoft Rewards
Free downloads & security
Education
Gift cards
Licensing
Unlocked stories
View Sitemap
Search
Search Azure
No results
Cancel
Blog home
/
AI + machine learning
/
Agent Factory: The new era of agentic AI—common use cases and design patterns
Search for:
Submit search
Published Aug 13, 2025
6 min read
Agent Factory: The new era of agentic AI—common use cases and design patterns
By Yina Arenas , Corporate Vice President, Microsoft Foundry
Share
Content type
Partnerships
Thought leadership
Tag
Agent Factory
AI
Large language models (LLMs)
Audience
AI professionals
Product
Azure AI
GitHub Copilot
Microsoft Foundry
Tech Community
Connect with a community to find answers, ask questions, build skills, and accelerate your learning.
Visit the Microsoft Foundry tech community
Instead of simply delivering information, agents reason, act, and collaborate—bridging the gap between knowledge and outcomes. Read more about agentic AI in Azure AI Foundry.
This blog post is the first out of a six-part blog series called Agent Factory which will share best practices, design patterns, and tools to help guide you through adopting and building agentic AI.
Beyond knowledge: Why enterprises need agentic AI
Retrieval-augmented generation (RAG) marked a breakthrough for enterprise AI—helping teams surface insights and answer questions at unprecedented speed. For many, it was a launchpad: copilots and chatbots that streamlined support and reduced the time spent searching for information.
However, answers alone rarely drive real business impact. Most enterprise workflows demand action: submitting forms, updating records, or orchestrating multi-step processes across diverse systems. Traditional automation tools—scripts, Robotic Process Automation (RPA) bots, manual handoffs—often struggle with change and scale, leaving teams frustrated by gaps and inefficiencies.
This is where agentic AI emerges as a game-changer. Instead of simply delivering information, agents reason, act, and collaborate—bridging the gap between knowledge and outcomes and enabling a new era of enterprise automation.
Build agentic AI with Azure AI Foundry
Patterns of agentic AI: Building blocks for enterprise automation
While the shift from retrieval to real-world action often begins with agents that can use tools, enterprise needs don’t stop there. Reliable automation requires agents that reflect on their work, plan multi-step processes, collaborate across specialties, and adapt in real time—not just execute single calls.
The five patterns below are foundational building blocks seen in production today. They’re designed to be combined and together unlock transformative automation.
1. Tool use pattern—from advisor to operator
Modern agents stand out by driving real outcomes. Today’s agents interact directly with enterprise systems—retrieving data, calling Application Programming Interface (APIs), triggering workflows, and executing transactions. Agents now surface answers and also complete tasks, update records, and orchestrate workflows end-to-end.
Fujitsu transformed its sales proposal process using specialized agents for data analysis, market research, and document creation—each invoking specific APIs and tools. Instead of simply answering “what should we pitch,” agents built and assembled entire proposal packages, reducing production time by 67%.
2. Reflection pattern—self-improvement for reliability
Once agents can act, the next step is reflection—the ability to assess and improve their own outputs. Reflection lets agents catch errors and iterate for quality without always depending on humans.
In high-stakes fields like compliance and finance, a single error can be costly. With self-checks and review loops, agents can auto-correct missing details, double-check calculations, or ensure messages meet standards. Even code assistants, like GitHub Copilot , rely on internal testing and refinement before sharing outputs. This self-improving loop reduces errors and gives enterprises confidence that AI-driven processes are safe, consistent, and auditable.
3. Planning pattern—decomposing complexity for robustness
Most real business processes aren’t single steps—they’re complex journeys with dependencies and branching paths. Planning agents address this by breaking high-level goals into actionable tasks, tracking progress, and adapting as requirements shift.
ContraForce’s Agentic Security Delivery Platform (ASDP) automated its partner’s security service delivery with security service agents using planning agents that break down incidents into intake, impact assessment, playbook execution, and escalation. As each phase completes, the agent checks for next steps, ensuring nothing gets missed. The result: 80% of incident investigation and response is now automated and full incident investigation can be processed for less than $1 per incident.
Planning often combines tool use and reflection, showing how these patterns reinforce each other. A key strength is flexibility: plans can be generated dynamically by an LLM or follow a predefined sequence, whichever fits the need.
4. Multi-agent pattern—collaboration at machine speed
No single agent can do it all. Enterprises create value through teams of specialists, and the multi-agent pattern mirrors this by connecting networks of specialized agents—each focused on different workflow stages—under an orchestrator. This modular design enables agility, scalability, and easy evolution, while keeping responsibilities and governance clear.
Modern multi-agent solutions use several orchestration patterns —often in combination—to address real enterprise needs. These can be LLM-driven or deterministic: sequential orchestration (such as agents refine a document step by step), concurrent orchestration (agents run in parallel and merge results), group chat/maker-checker (agents debate and validate outputs together), dynamic handoff (real-time triage or routing), and magentic orchestration (a manager agent coordinates all subtasks until completion).
JM Family adopted this approach with business analyst/quality assurance (BAQA) Genie, deploying agents for requirements, story writing, coding, documentation, and Quality Assurance (QA). Coordinated by an orchestrator, their development cycles became standardized and automated—cutting requirements and test design from weeks to days and saving up to 60% of QA time.
5. ReAct (Reason + Act) pattern—adaptive problem solving in real time
The ReAct pattern enables agents to solve problems in real time, especially when static plans fall short. Instead of a fixed script, ReAct agents alternate between reasoning and action—taking a step, observing results, and deciding what to do next. This allows agents to adapt to ambiguity, evolving requirements, and situations where the best path forward isn’t clear.
For example, in enterprise IT support, a virtual agent powered by the ReAct pattern can diagnose issues in real time: it asks clarifying questions, checks system logs, tests possible solutions, and adjusts its strategy as new information becomes available. If the issue grows more complex or falls outside its scope, the agent can escalate the case to a human specialist with a detailed summary of what’s been attempted.
These patterns are meant to be combined. The most effective agentic solutions weave together tool use, reflection, planning, multi-agent collaboration, and adaptive reasoning—enabling automation that is faster, smarter, safer, and ready for the real world.
Why a unified agent platform is essential
Building intelligent agents goes far beyond prompting a language model. When moving from demo to real-world use, teams quickly encounter challenges:
How do I chain multiple steps together reliably?
How do I give agents access to business data—securely and responsibly?
How do I monitor, evaluate, and improve agent behavior?
How do I ensure security and identity across different agent components?
How do I scale from a single agent to a team of agents—or connect to others?
Many teams end up building custom scaffolding—DIY orchestrators, logging, tool managers, and access controls. This slows time-to-value, creates risks, and leads to fragile solutions.
This is where Azure AI Foundry comes in—not just as a set of tools, but as a cohesive platform designed to take agents from idea to enterprise-grade implementation.
Azure AI Foundry: Unified, scalable, and built for the real world
Azure AI Foundry is designed from the ground up for this new era of agentic automation. Azure AI Foundry delivers a single, end-to-end platform that meets the needs of both developers and enterprises, combining rapid innovation with robust, enterprise-grade controls.
With Azure AI Foundry, teams can:
Prototype locally, deploy at scale: Develop and test agents locally, then seamlessly move to cloud runtime—no rewrites needed. Check out how to get started with Azure AI Foundry SDK .
Flexible model choice: Choose from Azure OpenAI, xAI Grok, Mistral, Meta, and over 10,000 open-source models—all via a unified API. A Model Router and Leaderboard help select the optimal model, balancing performance, cost, and specialization. Check out the Azure AI Foundry Models catalog .
Compose modular multi-agent architectures: Connect specialized agents and workflows, reusing patterns across teams. Check out how to use connected agents in Azure AI Foundry Agent Service .
Integrate instantly with enterprise systems: Leverage over 1,400+ built-in connectors for SharePoint, Bing, SaaS, and business apps, with native security and policy support. Check out what are tools in Azure AI Foundry Agent Service .
Enable openness and interoperability: Built-in support for open protocols like Agent-to-Agent (A2A) and Model Context Protocol (MCP) lets your agents work across clouds, platforms, and partner ecosystems. Check out how to connect to a Model Context Protocol Server Endpoint in Azure AI Foundry Agent Service .
Enterprise-grade security: Every agent gets a managed Entra Agent ID, robust Role-based Access Control (RBAC), On Behalf Of authentication, and policy enforcement—ensuring only the right agents access the right resources. Check out how to use a virtual network with the Azure AI Foundry Agent Service .
Comprehensive observability: Gain deep visibility with step-level tracing, automated evaluation, and Azure Monitor integration—supporting compliance and continuous improvement at scale. Check out how to monitor Azure AI Foundry Agent Service .
Azure AI Foundry isn’t just a toolkit—it’s the foundation for orchestrating secure, scalable, and intelligent agents across the modern enterprise.
It’s how organizations move from siloed automation to true, end-to-end business transformation.
Stay tuned: In upcoming posts in our Agent Factory blog series , we’ll show you how to bring these pillars to life—demonstrating how to build secure, orchestrated, and interoperable agents with Azure AI Foundry, from local development to enterprise deployment.
Azure AI Foundry
Create adaptable AI agents that automate tasks and enhance user experiences.
Learn more >
Tech Community
Connect with a community to find answers, ask questions, build skills, and accelerate your learning.
Visit the Microsoft Foundry tech community
Related Posts
Thought leadership
Aug 20, 2025
6 min read
Agent Factory: Building your first AI agent with the tools to deliver real-world outcomes
Thought leadership
Aug 27, 2025
7 min read
Agent Factory: Top 5 agent observability best practices for reliable AI
Thought leadership
Sep 3, 2025
6 min read
Agent Factory: From prototype to production—developer tools and rapid agent development
Explore
Microsoft Foundry
The future of AI starts here. Envision your next great AI app with the latest technologies. Get started with Azure.
Learn more about Microsoft Foundry
Connect with us on social
X
YouTube
LinkedIn
Instagram
Explore Azure
What is Azure?
Get started with Azure
Global infrastructure
Datacenter regions
Trust your cloud
Azure Essentials
Customer stories
Products and pricing
Products
Azure pricing
Free Azure services
Flexible purchase options
FinOps on Azure
Optimize your costs
Solutions and support
Solutions
Resources for accelerating growth
Solution architectures
Support
Azure demo and live Q&A
Partners
Software Development Companies
Microsoft Marketplace
Find a partner
Resources
Documentation
Blog
Developer resources
Students
Events and Webinars
Analyst reports, white papers, and e-books
Videos
Cloud computing
What is cloud computing?
What is multicloud?
What is machine learning?
What is deep learning?
What is AIaaS?
What are LLMs?
What is a container?
What is RAG?
English (United States)
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
- runtime_article_bundle_path: research/articles/art-2026-03-02-002.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-02-002.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-02-002.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
