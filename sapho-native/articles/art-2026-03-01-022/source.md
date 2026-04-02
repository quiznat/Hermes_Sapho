---
version: source-capture.v1
article_id: art-2026-03-01-022
ticket_id: ticket-import-art-2026-03-01-022
source_url: https://github.com/virattt/dexter
canonical_url: https://github.com/virattt/dexter
source_title: "GitHub - virattt/dexter: An autonomous agent for deep financial research\
  \ \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

GitHub - virattt/dexter: An autonomous agent for deep financial research · GitHub

## Body

GitHub - virattt/dexter: An autonomous agent for deep financial research · GitHub
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
GitHub Stars
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
virattt
/
dexter
Public
Notifications
You must be signed in to change notification settings
Fork
2.2k
Star
18.2k
Code
Issues
17
Pull requests
35
Actions
Projects
Security
0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Security
Insights
virattt/dexter
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
392 Commits
392 Commits
.github/ workflows
.github/ workflows
scripts
scripts
src
src
.gitignore
.gitignore
AGENTS.md
AGENTS.md
README.md
README.md
SOUL.md
SOUL.md
bun.lock
bun.lock
env.example
env.example
jest.config.js
jest.config.js
package.json
package.json
tsconfig.json
tsconfig.json
View all files
Repository files navigation
README
Dexter 🤖
Dexter is an autonomous financial research agent that thinks, plans, and learns as it works. It performs analysis using task planning, self-reflection, and real-time market data. Think Claude Code, but built specifically for financial research.
Table of Contents
👋 Overview
✅ Prerequisites
💻 How to Install
🚀 How to Run
📊 How to Evaluate
🐛 How to Debug
📱 How to Use with WhatsApp
🤝 How to Contribute
📄 License
👋 Overview
Dexter takes complex financial questions and turns them into clear, step-by-step research plans. It runs those tasks using live market data, checks its own work, and refines the results until it has a confident, data-backed answer.
Key Capabilities:
Intelligent Task Planning : Automatically decomposes complex queries into structured research steps
Autonomous Execution : Selects and executes the right tools to gather financial data
Self-Validation : Checks its own work and iterates until tasks are complete
Real-Time Financial Data : Access to income statements, balance sheets, and cash flow statements
Safety Features : Built-in loop detection and step limits to prevent runaway execution
✅ Prerequisites
Bun runtime (v1.0 or higher)
OpenAI API key (get here )
Financial Datasets API key (get here )
Exa API key (get here ) - optional, for web search
Installing Bun
If you don't have Bun installed, you can install it using curl:
macOS/Linux:
curl -fsSL https://bun.com/install | bash
Windows:
powershell -c " irm bun.sh/install.ps1|iex "
After installation, restart your terminal and verify Bun is installed:
bun --version
💻 How to Install
Clone the repository:
git clone https://github.com/virattt/dexter.git
cd dexter
Install dependencies with Bun:
bun install
Set up your environment variables:
# Copy the example environment file
cp env.example .env
# Edit .env and add your API keys (if using cloud providers)
# OPENAI_API_KEY=your-openai-api-key
# ANTHROPIC_API_KEY=your-anthropic-api-key (optional)
# GOOGLE_API_KEY=your-google-api-key (optional)
# XAI_API_KEY=your-xai-api-key (optional)
# OPENROUTER_API_KEY=your-openrouter-api-key (optional)
# Institutional-grade market data for agents; AAPL, NVDA, MSFT are free
# FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key
# (Optional) If using Ollama locally
# OLLAMA_BASE_URL=http://127.0.0.1:11434
# Web Search (Exa preferred, Tavily fallback)
# EXASEARCH_API_KEY=your-exa-api-key
# TAVILY_API_KEY=your-tavily-api-key
🚀 How to Run
Run Dexter in interactive mode:
bun start
Or with watch mode for development:
bun dev
📊 How to Evaluate
Dexter includes an evaluation suite that tests the agent against a dataset of financial questions. Evals use LangSmith for tracking and an LLM-as-judge approach for scoring correctness.
Run on all questions:
bun run src/evals/run.ts
Run on a random sample of data:
bun run src/evals/run.ts --sample 10
The eval runner displays a real-time UI showing progress, current question, and running accuracy statistics. Results are logged to LangSmith for analysis.
🐛 How to Debug
Dexter logs all tool calls to a scratchpad file for debugging and history tracking. Each query creates a new JSONL file in .dexter/scratchpad/ .
Scratchpad location:
.dexter/scratchpad/
├── 2026-01-30-111400_9a8f10723f79.jsonl
├── 2026-01-30-143022_a1b2c3d4e5f6.jsonl
└── ...
Each file contains newline-delimited JSON entries tracking:
init : The original query
tool_result : Each tool call with arguments, raw result, and LLM summary
thinking : Agent reasoning steps
Example scratchpad entry:
{ "type" : " tool_result " , "timestamp" : " 2026-01-30T11:14:05.123Z " , "toolName" : " get_income_statements " , "args" :{ "ticker" : " AAPL " , "period" : " annual " , "limit" : 5 }, "result" :{ ... }, "llmSummary" : " Retrieved 5 years of Apple annual income statements showing revenue growth from $274B to $394B " }
This makes it easy to inspect exactly what data the agent gathered and how it interpreted results.
📱 How to Use with WhatsApp
Chat with Dexter through WhatsApp by linking your phone to the gateway. Messages you send to yourself are processed by Dexter and responses are sent back to the same chat.
Quick start:
# Link your WhatsApp account (scan QR code)
bun run gateway:login
# Start the gateway
bun run gateway
Then open WhatsApp, go to your own chat (message yourself), and ask Dexter a question.
For detailed setup instructions, configuration options, and troubleshooting, see the WhatsApp Gateway README .
🤝 How to Contribute
Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request
Important : Please keep your pull requests small and focused. This will make it easier to review and merge.
📄 License
This project is licensed under the MIT License.
About
An autonomous agent for deep financial research
Resources
Readme
Uh oh!
There was an error while loading. Please reload this page .
Activity
Stars
18.2k
stars
Watchers
118
watching
Forks
2.2k
forks
Report repository
Releases
13
Dexter 2026.3.18
Latest
Mar 18, 2026
+ 12 releases
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
20
+ 6 contributors
Languages
TypeScript
99.3%
Other
0.7%
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
- runtime_article_bundle_path: research/articles/art-2026-03-01-022.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-022.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-022.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
