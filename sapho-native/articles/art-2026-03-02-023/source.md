---
version: source-capture.v1
article_id: art-2026-03-02-023
ticket_id: ticket-import-art-2026-03-02-023
source_url: https://github.com/a2aproject/A2A
canonical_url: https://github.com/a2aproject/A2A
source_title: "GitHub - a2aproject/A2A: Agent2Agent (A2A) is an open protocol enabling\
  \ communication and interoperability between opaque agentic applications. \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-07T19:27:12Z'
---
# Source Capture

## Title

GitHub - a2aproject/A2A: Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications. · GitHub

## Body

GitHub - a2aproject/A2A: Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications. · GitHub
Skip to content
Navigation Menu
Toggle navigation
Sign in
Appearance settings
Platform AI CODE CREATION GitHub Copilot Write better code with AI
GitHub Spark Build and deploy intelligent apps
GitHub Models Manage and compare prompts
MCP Registry New Integrate external tools
DEVELOPER WORKFLOWS Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE Why GitHub
Documentation
Blog
Changelog
Marketplace
View all features
Solutions BY COMPANY SIZE Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY Healthcare
Financial services
Manufacturing
Government
View all industries
View all solutions
Resources EXPLORE BY TOPIC AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES Documentation
Customer support
Community forum
Trust center
Partners
View all resources
Open Source COMMUNITY GitHub Sponsors Fund open source developers
PROGRAMS Security Lab
Maintainer Community
Accelerator
Archive Program
REPOSITORIES Topics
Trending
Collections
Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
-->
Search
Clear
Search syntax tips
Provide feedback
-->
We read every piece of feedback, and take your input very seriously.
Include my email address so I can be contacted
Cancel
Submit feedback
Saved searches
Use saved searches to filter your results more quickly
-->
Name
Query
To see all available qualifiers, see our documentation .
Cancel
Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session.
You signed out in another tab or window. Reload to refresh your session.
You switched accounts on another tab or window. Reload to refresh your session.
Dismiss alert
{{ message }}
a2aproject
/
A2A
Public
Notifications
You must be signed in to change notification settings
Fork
2.3k
Star
22.3k
Code
Issues
172
Pull requests
25
Discussions
Actions
Projects
Security
0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Projects
Security
Insights
a2aproject/A2A
main
Branches Tags
Go to file
Code Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
History
521 Commits
521 Commits
.devcontainer
.devcontainer
.gemini
.gemini
.github
.github
.mkdocs
.mkdocs
.vscode
.vscode
adrs
adrs
docs
docs
scripts
scripts
specification
specification
.editorconfig
.editorconfig
.git-blame-ignore-revs
.git-blame-ignore-revs
.gitattributes
.gitattributes
.gitignore
.gitignore
.gitvote.yml
.gitvote.yml
.prettierrc
.prettierrc
.ruff.toml
.ruff.toml
CHANGELOG.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTING.md
GOVERNANCE.md
GOVERNANCE.md
LICENSE
LICENSE
MAINTAINERS.md
MAINTAINERS.md
README.md
README.md
SECURITY.md
SECURITY.md
lychee.toml
lychee.toml
mkdocs.yml
mkdocs.yml
requirements-docs.txt
requirements-docs.txt
View all files
Repository files navigation
README
Code of conduct
Contributing
Apache-2.0 license
Security
Agent2Agent (A2A) Protocol
🌐 Language
English
| 简体中文
| 繁體中文
| 日本語
| 한국어
| हिन्दी
| ไทย
| Français
| Deutsch
| Español
| Italiano
| Русский
| Português
| Nederlands
| Polski
| العربية
| فارسی
| Türkçe
| Tiếng Việt
| Bahasa Indonesia
| অসমীয়া
Agent2Agent (A2A) Protocol
An open protocol enabling communication and interoperability between opaque agentic applications.
The Agent2Agent (A2A) protocol addresses a critical challenge in the AI landscape: enabling gen AI agents, built on diverse frameworks by different companies running on separate servers, to communicate and collaborate effectively - as agents, not just as tools. A2A aims to provide a common language for agents, fostering a more interconnected, powerful, and innovative AI ecosystem.
With A2A, agents can:
Discover each other's capabilities.
Negotiate interaction modalities (text, forms, media).
Securely collaborate on long-running tasks.
Operate without exposing their internal state, memory, or tools.
DeepLearning.AI Course
Join this short course on A2A: The Agent2Agent Protocol , built in partnership with Google Cloud and IBM Research, and taught by Holt Skinner , Ivan Nardini , and Sandi Besen .
What you'll learn:
Make agents A2A-compliant: Expose agents built with frameworks like Google ADK, LangGraph, or BeeAI as A2A servers.
Connect agents: Create A2A clients from scratch or using integrations to connect to A2A-compliant agents.
Orchestrate workflows: Build sequential and hierarchical workflows of A2A-compliant agents.
Multi-agent systems: Build a healthcare multi-agent system using different frameworks and see how A2A enables collaboration.
A2A and MCP: Learn how A2A complements MCP by enabling agents to collaborate with each other.
Why A2A?
As AI agents become more prevalent, their ability to interoperate is crucial for building complex, multi-functional applications. A2A aims to:
Break Down Silos: Connect agents across different ecosystems.
Enable Complex Collaboration: Allow specialized agents to work together on tasks that a single agent cannot handle alone.
Promote Open Standards: Foster a community-driven approach to agent communication, encouraging innovation and broad adoption.
Preserve Opacity: Allow agents to collaborate without needing to share internal memory, proprietary logic, or specific tool implementations, enhancing security and protecting intellectual property.
Key Features
Standardized Communication: JSON-RPC 2.0 over HTTP(S).
Agent Discovery: Via "Agent Cards" detailing capabilities and connection info.
Flexible Interaction: Supports synchronous request/response, streaming (SSE), and asynchronous push notifications.
Rich Data Exchange: Handles text, files, and structured JSON data.
Enterprise-Ready: Designed with security, authentication, and observability in mind.
Getting Started
📚 Explore the Documentation: Visit the Agent2Agent Protocol Documentation Site for a complete overview, the full protocol specification, tutorials, and guides.
📝 View the Specification: A2A Protocol Specification
Use the SDKs:
🐍 A2A Python SDK pip install a2a-sdk
🐿️ A2A Go SDK go get github.com/a2aproject/a2a-go
🧑‍💻 A2A JS SDK npm install @a2a-js/sdk
☕️ A2A Java SDK using maven
🔷 A2A .NET SDK using NuGet dotnet add package A2A
🎬 Use our samples to see A2A in action
Contributing
We welcome community contributions to enhance and evolve the A2A protocol!
Questions & Discussions: Join our GitHub Discussions .
Issues & Feedback: Report issues or suggest improvements via GitHub Issues .
Contribution Guide: See our CONTRIBUTING.md for details on how to contribute.
Private Feedback: Use this Google Form .
Partner Program: Google Cloud customers can join our partner program via this form .
What's next
Protocol Enhancements
Agent Discovery:
Formalize inclusion of authorization schemes and optional credentials directly within the AgentCard .
Agent Collaboration:
Investigate a QuerySkill() method for dynamically checking unsupported or unanticipated skills.
Task Lifecycle & UX:
Support for dynamic UX negotiation within a task (e.g., agent adding audio/video mid-conversation).
Client Methods & Transport:
Explore extending support to client-initiated methods (beyond task management).
Improvements to streaming reliability and push notification mechanisms.
About
The A2A Protocol is an open source project under the Linux Foundation, contributed by Google. It is licensed under the Apache License 2.0 and is open to contributions from the community.
About
Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications.
a2a-protocol.org/
Topics
agents
linux-foundation
a2a
generative-ai
a2a-protocol
a2a-mcp
a2a-server
Resources
Readme
License
Apache-2.0 license
Code of conduct
Code of conduct
Contributing
Contributing
Security policy
Security policy
Uh oh!
There was an error while loading. Please reload this page .
Activity
Custom properties
Stars
22.3k
stars
Watchers
223
watching
Forks
2.3k
forks
Report repository
Releases
9
v0.3.0
Latest
Jul 30, 2025
+ 8 releases
Uh oh!
There was an error while loading. Please reload this page .
Contributors
143
+ 129 contributors
Languages
Shell
100.0%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can’t perform that action at this time.

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-02-023.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-02-023.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-02-023.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
