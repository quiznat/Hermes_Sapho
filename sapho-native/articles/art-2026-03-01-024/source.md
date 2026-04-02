---
version: source-capture.v1
article_id: art-2026-03-01-024
ticket_id: ticket-import-art-2026-03-01-024
source_url: https://www.ashpreetbedi.com/articles/sql-agent
canonical_url: https://www.ashpreetbedi.com/articles/sql-agent
source_title: Self Improving Text2Sql Agent with Dynamic Context and Continuous Learning
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

Self Improving Text2Sql Agent with Dynamic Context and Continuous Learning

## Body

Menu
Articles
About
Self Improving Text2Sql Agent with Dynamic Context and Continuous Learning
December 15, 2025 This post shows how to build a self-improving Text-to-SQL agent using dynamic context and "poor-man's continuous learning". We'll break the problem into two parts:
Text-to-SQL Agent (Online Path): answers questions by retrieving schema + query patterns from a knowledge base (dynamic context).
Continuous Learning (Offline Path): learns from successful runs and adds new entries to the knowledge base.
When the Agent finds a successful result, it stores it in its knowledge base for future use. This gives the text-to-sql agent a self-improving feedback loop, but keeps the online path stable.
Table of Contents
Why Text-to-SQL fails in practice
What is "dynamic context"
What is "poor man's continuous learning" (and why it works)
Unified Agent Architecture
Knowledge Base Design (keep it structured)
Production Harness (deployable anywhere)
Steps to run your own Text-to-SQL Agent
1. Why Text-to-SQL fails in practice
Most Test-to-SQL agents fail in practice because they start from scratch every time, describing tables, columns, finding join keys. Repeating every mistake, every time.
Now compare this with how senior analysts or data engineers operate: do they start from scratch every time? No, they use tribal knowledge and experience and dig through past queries to find the right one. Once they find a useful query, they capture it in their knowledge base for future reference. Our text-to-sql agent works the same way.
I've found that most Text-to-SQL failures are not "model is dumb", they're "model is missing context and tribal knowledge" issues. Let's break down the common mistakes:
The model starts from scratch every time, describing tables, columns, finding join keys. Repeating every mistake, every time.
The model guesses column names, usage patterns, or doesn't know the right join keys.
The model misses domain definitions (active user, churn, ARR, etc.) or doesn't know the right business rules (eg: "status lives in orders.state, not orders.status").
The model is missing common gotchas (date in the wrong format, nulls in the wrong place, etc.).
The model re-invents queries that already exist in your organization's knowledge base.
The biggest improvement you can make to your text-to-sql agent is to provide it with the same tribal knowledge that human engineers have. This enables them to re-use queries that we know work and let the model search established usage patterns at runtime. Call it RAG, Agentic RAG, or Dynamic Context, it's the same thing: the model, at runtime, has access to the right context to generate the right SQL.
Our goal is straightforward:
Give our agent the tools to retrieve the right context at runtime (schemas, joins, past queries, metric definitions, gotchas).
Generate SQL grounded in well established usage patterns (no guessing and no re-inventing the wheel).
Validate the SQL (query is parseable, schema checks, etc.).
Run the SQL and "analyze" the results. Don't just give me the data, give me the insights.
Capture learnings so the next run is better (new join path, corrected column mapping, query template, metric definition).
Repeat.
2. What is "dynamic context"
Dynamic context is simply: the agent retrieves the relevant knowledge at query time, which enables it to generate SQL grounded in well established usage patterns . The context is dynamic because it changes based on the query, the data, and the user's intent.
Examples of what the agent can retrieve:
Table schemas and relationships
Common join keys and relationships
Known queries for common use cases
Metric definitions and business rules
Known gotchas ("status lives in orders.state, not orders.status")
If your KB contains a query for "weekly active users", your agent should retrieve it, not re-invent it.
3. What is "poor man's continuous learning" (and why it works)
By "poor man's continuous learning", I mean:
We do not update model weights.
We do update retrieval knowledge when we find a successful result.
The system improves by capturing experience as reusable artifacts.
Every good query becomes future context.
Every mistake becomes a rule.
Every clarification becomes shared knowledge.
Poor man's continuous learning works because it provides a pragmatic learning loop: stable online behavior, controlled improvements. The best part is that you can always explore the knowledge base manually and fix issues or mistakes, imaging updating model weights by hand.
4. Unified Agent Architecture
The systems is broken into 2 parts:
Text-to-SQL Agent: answers questions by retrieving schema + query patterns from a knowledge base (dynamic context).
Continuous Learning: learns from successful runs and adds new entries to the knowledge base.
Query Flow
User asks a question
Agent retrieves context from KB (hybrid search) using:
question text
detected entities (tables, columns, metrics)
optional database introspection results
This knowledge augments the input with dynamic context:
retrieved knowledge snippets
rules and constraints (read-only, limit, etc.)
This knowledge guides the generation of SQL .
Agent executes the query in a safe environment.
Agent analyzes the results and returns the answer .
If the result is successful, the agent asks the user if they want to save the query to the knowledge base.
If the user agrees, the agent stores the query in the knowledge base.
If the user disagrees, the agent revists the query, update it and try again.
There are 2 improvments you can make to the learning path:
Run the continuous learning separately after every run of the text-to-sql agent. This way, the continuous learning is always up to date with the latest queries and results.
Add a regression harness to the continuous learning. This way, you can test the knowledge base before and after updates to ensure it's still working.
5. Knowledge Base Design (keep it structured)
We want our knowledge base to store 3 kinds of information:
Table information: this includes the table schema, column metadata, query rules , common gotchas (eg: date column contains a rule: "Use the TO_DATE function when filtering by date").
Sample queries: this include common query patterns and best practices. Along with how to retrieve common metrics and KPIs. There's no need to re-invent the wheel.
Business semantics and relationships: the layer that maps how your organization talks about data to how the database is structured.
The sample codebase I'm providing contains the following files (table information and common queries):
agents/sql/knowledge/
├── constructors_championship.json
├── drivers_championship.json
├── fastest_laps.json
├── race_results.json
├── race_wins.json
└── common_queries.sql
6. Production Harness
I'm providing a production-ready harness for our system, built using:
A FastAPI application for running our agents.
A Postgres database for storing sessions, memory and knowledge.
Here's the link to the repository containing the production codebase.
Here's the structure of the repository:
.
├── agents
│ ├── __init__.py
│ ├── sql
│ │ ├── __init__.py
│ │ ├── knowledge
│ │ ├── load_f1_data.py
│ │ ├── load_sql_knowledge.py
│ │ ├── sql_agent.py
│ │ └── test_questions.txt
│ └── .. . more agents
├── app
│ ├── __init__.py
│ └── main.py
├── compose.yaml
├── db
│ └── .. . database configuration
├── Dockerfile
├── pyproject.toml
├── railway.json
├── README.md
├── requirements.txt
├── scripts
│ ├── dev_setup.sh
│ ├── entrypoint.sh
│ ├── railway_up.sh
│ ├── format.sh
│ └── validate.sh
├── teams
│ └── finance_team.py
└── workflows
└── research_workflow.py
7. Steps to run your own Text-to-SQL Agent
Clone the repo
git clone https://github.com/agno-agi/agentos-railway.git
cd agentos-railway
Configure API keys
We'll use OpenAI for the text-to-sql agent, (we also use Anthropic and Parallel Search for other agents in the service). Please export the following environment variables:
# Required
export OPENAI_API_KEY = "YOUR_API_KEY_HERE"
# Optional
export ANTHROPIC_API_KEY = "YOUR_API_KEY_HERE"
export PARALLEL_API_KEY = "YOUR_API_KEY_HERE"
You can copy the example.env file and rename it to .env to get started.
Install Docker
We'll use docker to run the application locally and deploy it to Railway. Please install Docker Desktop if needed.
Run the application locally
Run the application using docker compose:
docker compose up --build -d
This command builds the Docker image and starts the application:
The FastAPI application , running on localhost:8000 .
The PostgreSQL database for storing agent sessions, knowledge, and memories, accessible on localhost:5432 .
Once started, you can:
View the FastAPI application at localhost:8000/docs .
Load data for the SQL Agent
To load the data for the SQL Agent, run:
docker exec -it agentos-railway-agent-os-1 python -m agents.sql.load_f1_data
To populate the knowledge base, run:
docker exec -it agentos-railway-agent-os-1 python -m agents.sql.load_sql_knowledge
Connect the AgentOS UI to the FastAPI application
Open the AgentOS UI
Login and add http://localhost:8000 as a new AgentOS. You can call it Local AgentOS (or any name you prefer).
Demo
Here's a demo of the Text-to-SQL Agent in action. Notice how I add a query to the knowledge base and the agent uses it to generate the SQL when i ask the same question again.
Your browser does not support the video tag.
Stop the application
When you're done, stop the application using:
docker compose down
Deploy the application to Railway
To deploy the application to Railway, run the following commands:
Install Railway CLI:
brew install railway
Login to Railway:
railway login
Deploy the application:
./scripts/railway_up.sh
This command will:
Create a new Railway project.
Deploy a PgVector database service to your Railway project.
Build and deploy the docker image to your Railway project.
Set environment variables in your AgentOS service.
Create a new domain for your AgentOS service.
Thank you for reading! I hope you found this useful. Feel free to reach out to me on X if you have any questions or feedback
Articles About
© 2026 Ashpreet Bedi. All rights reserved.
Self Improving Text2Sql Agent with Dynamic Context and Continuous Learning

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-01-024.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-024.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-024.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
