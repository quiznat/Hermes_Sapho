---
version: source-capture.v1
article_id: art-2026-03-01-025
ticket_id: ticket-import-art-2026-03-01-025
source_url: https://github.com/agno-agi/dash
canonical_url: https://github.com/agno-agi/dash
source_title: "GitHub - agno-agi/dash: Self-learning data agent that grounds its answers\
  \ in 6 layers of context. Inspired by OpenAI's in-house implementation. \xB7 GitHub"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

GitHub - agno-agi/dash: Self-learning data agent that grounds its answers in 6 layers of context. Inspired by OpenAI's in-house implementation. · GitHub

## Body

GitHub - agno-agi/dash: Self-learning data agent that grounds its answers in 6 layers of context. Inspired by OpenAI's in-house implementation. · GitHub
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
agno-agi
/
dash
Public
Notifications
You must be signed in to change notification settings
Fork
199
Star
1.8k
Code
Issues
4
Pull requests
4
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
agno-agi/dash
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
39 Commits
39 Commits
.github/ workflows
.github/ workflows
app
app
dash
dash
db
db
scripts
scripts
.dockerignore
.dockerignore
.gitignore
.gitignore
CLAUDE.md
CLAUDE.md
Dockerfile
Dockerfile
LICENSE
LICENSE
README.md
README.md
compose.yaml
compose.yaml
example.env
example.env
pyproject.toml
pyproject.toml
railway.json
railway.json
requirements.txt
requirements.txt
View all files
Repository files navigation
README
Apache-2.0 license
Dash
Dash is a self-learning data agent that grounds its answers in 6 layers of context and improves with every run.
Inspired by OpenAI's in-house data agent .
Get Started
# Clone the repo
git clone https://github.com/agno-agi/dash.git && cd dash
# Add OPENAI_API_KEY
cp example.env .env
# Edit .env and add your key
# Start the application
docker compose up -d --build
# Load sample data and knowledge
docker exec -it dash-api python -m dash.scripts.load_data
docker exec -it dash-api python -m dash.scripts.load_knowledge
Confirm dash is running at http://localhost:8000/docs .
Connect to the Web UI
Open os.agno.com and login
Add OS → Local → http://localhost:8000
Click "Connect"
Try it (sample F1 dataset):
Who won the most F1 World Championships?
How many races has Lewis Hamilton won?
Compare Ferrari vs Mercedes points 2015-2020
Why Text-to-SQL Breaks in Practice
Our goal is simple: ask a question in english, get a correct, meaningful answer. But raw LLMs writing SQL hit a wall fast:
Schemas lack meaning.
Types are misleading.
Tribal knowledge is missing.
No way to learn from mistakes.
Results generally lack interpretation.
The root cause is missing context and missing memory.
Dash solves this with 6 layers of grounded context , a self-learning loop that improves with every query, and a focus on understanding your question to deliver insights you can act on.
The Six Layers of Context
Layer
Purpose
Source
Table Usage
Schema, columns, relationships
knowledge/tables/*.json
Human Annotations
Metrics, definitions, and business rules
knowledge/business/*.json
Query Patterns
SQL that is known to work
knowledge/queries/*.sql
Institutional Knowledge
Docs, wikis, external references
MCP (optional)
Learnings
Error patterns and discovered fixes
Agno Learning Machine
Runtime Context
Live schema changes
introspect_schema tool
The agent retrieves relevant context at query time via hybrid search, then generates SQL grounded in patterns that already work.
The Self-Learning Loop
Dash improves without retraining or fine-tuning. We call this gpu-poor continuous learning.
It learns through two complementary systems:
System
Stores
How It Evolves
Knowledge
Validated queries and business context
Curated by you + dash
Learnings
Error patterns and fixes
Managed by Learning Machine automatically
User Question
↓
Retrieve Knowledge + Learnings
↓
Reason about intent
↓
Generate grounded SQL
↓
Execute and interpret
↓
┌────┴────┐
↓ ↓
Success Error
↓ ↓
↓ Diagnose → Fix → Save Learning
↓ (never repeated)
↓
Return insight
↓
Optionally save as Knowledge
Knowledge is curated—validated queries and business context you want the agent to build on.
Learnings is discovered—patterns the agent finds through trial and error. When a query fails because position is TEXT not INTEGER, the agent saves that gotcha. Next time, it knows.
Insights, Not Just Rows
Dash reasons about what makes an answer useful, not just technically correct.
Question:
Who won the most races in 2019?
Typical SQL Agent
Dash
Hamilton: 11
Lewis Hamilton dominated 2019 with 11 wins out of 21 races , more than double Bottas’s 4 wins. This performance secured his sixth world championship.
Deploy to Railway
railway login
./scripts/railway_up.sh
Production Operations
Load data and knowledge:
railway run python -m dash.scripts.load_data
railway run python -m dash.scripts.load_knowledge
View logs:
railway logs --service dash
Run commands in production:
railway run python -m dash # CLI mode
Redeploy after changes:
railway up --service dash -d
Open dashboard:
railway open
Adding Knowledge
Dash works best when it understands how your organization talks about data.
knowledge/
├── tables/ # Table meaning and caveats
├── queries/ # Proven SQL patterns
└── business/ # Metrics and language
Table Metadata
{
"table_name": "orders",
"table_description": "Customer orders with denormalized line items",
"use_cases": ["Revenue reporting", "Customer analytics"],
"data_quality_notes": [
"created_at is UTC",
"status values: pending, completed, refunded",
"amount stored in cents"
]
}
Query Patterns
-- <query name>monthly_revenue</query name>
-- <query description>
-- Monthly revenue calculation.
-- Converts cents to dollars.
-- Excludes refunded orders.
-- </query description>
-- <query>
SELECT
DATE_TRUNC('month', created_at) AS month,
SUM(amount) / 100.0 AS revenue_dollars
FROM orders
WHERE status = 'completed'
GROUP BY 1
ORDER BY 1 DESC
-- </query>
Business Rules
{
"metrics": [
{
"name": "MRR",
"definition": "Sum of active subscriptions excluding trials"
}
],
"common_gotchas": [
{
"issue": "Revenue double counting",
"solution": "Filter to completed orders only"
}
]
}
Load Knowledge
python -m dash.scripts.load_knowledge # Upsert changes
python -m dash.scripts.load_knowledge --recreate # Fresh start
Local Development
./scripts/venv_setup.sh && source .venv/bin/activate
docker compose up -d dash-db
python -m dash.scripts.load_data
python -m dash # CLI mode
Environment Variables
Variable
Required
Description
OPENAI_API_KEY
Yes
OpenAI API key
EXA_API_KEY
No
Web search for external knowledge
DB_*
No
Database config (defaults to localhost)
Learn More
OpenAI's In-House Data Agent — the inspiration
Self-Improving SQL Agent — deep dive on an earlier architecture
Agno Docs
Discord
About
Self-learning data agent that grounds its answers in 6 layers of context. Inspired by OpenAI's in-house implementation.
Resources
Readme
License
Apache-2.0 license
Uh oh!
There was an error while loading. Please reload this page .
Activity
Custom properties
Stars
1.8k
stars
Watchers
18
watching
Forks
199
forks
Report repository
Releases
No releases published
Packages
0
Uh oh!
There was an error while loading. Please reload this page .
Contributors
2
ashpreetbedi
Ashpreet
claude
Claude
Languages
Python
82.0%
Shell
17.0%
Dockerfile
1.0%
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
- runtime_article_bundle_path: research/articles/art-2026-03-01-025.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-025.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-025.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
