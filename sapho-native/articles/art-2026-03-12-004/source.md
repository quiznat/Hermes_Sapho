---
version: source-capture.v1
article_id: art-2026-03-12-004
ticket_id: ticket-import-art-2026-03-12-004
source_url: https://arxiv.org/html/2601.06112v1
canonical_url: https://arxiv.org/abs/2601.06112
source_title: '[2601.06112] ReliabilityBench: Evaluating LLM Agent Reliability Under
  Production-Like Stress Conditions'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-12T22:18:39Z'
---
# Source Capture

## Title

[2601.06112] ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions

## Body

[2601.06112] ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions
Support arXiv on Cornell Giving Day!
We're celebrating 35 years of open science - with YOUR support! Your generosity has helped arXiv thrive for three and a half decades. Give today to help keep science open for ALL for many years to come.
Donate!
Skip to main content
We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors.
Donate
> cs > arXiv:2601.06112
Help | Advanced Search
All fields
Title
Author
Abstract
Comments
Journal reference
ACM classification
MSC classification
Report number
arXiv identifier
DOI
ORCID
arXiv author ID
Help pages
Full text
Search
GO
quick links
Login
Help Pages
About
-->
Computer Science > Artificial Intelligence
arXiv:2601.06112 (cs)
[Submitted on 3 Jan 2026]
Title: ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions
Authors: Aayush Gupta
View a PDF of the paper titled ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions, by Aayush Gupta
View PDF
HTML (experimental)
Abstract: Existing benchmarks for tool-using LLM agents primarily report single-run success rates and miss reliability properties required in production. We introduce \textbf{ReliabilityBench}, a benchmark for evaluating agent reliability across three dimensions: (i) consistency under repeated execution using $\mathrm{pass}^k$, (ii) robustness to semantically equivalent task perturbations at intensity $\epsilon$, and (iii) fault tolerance under controlled tool/API failures at intensity $\lambda$. ReliabilityBench contributes a unified reliability surface $R(k,\epsilon,\lambda)$, \textit{action metamorphic relations} that define correctness via end-state equivalence rather than text similarity, and a chaos-engineering-style fault injection framework (timeouts, rate limits, partial responses, schema drift). We evaluate two models (Gemini 2.0 Flash, GPT-4o) and two agent architectures (ReAct, Reflexion) across four domains (scheduling, travel, customer support, e-commerce) over 1,280 episodes. Perturbations alone reduce success from 96.9% at $\epsilon=0$ to 88.1% at $\epsilon=0.2$. Rate limiting is the most damaging fault in ablations. ReAct is more robust than Reflexion under combined stress, and Gemini 2.0 Flash achieves comparable reliability to GPT-4o at much lower cost. ReliabilityBench provides a systematic framework for assessing production readiness of LLM agents.
Comments:
18 pages, 5 figures, 8 tables. Evaluates ReAct vs Reflexion across four tool-using domains with perturbation (epsilon) and fault-injection (lambda) stress testing; 1,280 total episodes
Subjects:
Artificial Intelligence (cs.AI)
MSC classes:
68T50, 68T05, 68M15
ACM classes:
I.2.7; D.2.5; C.4
Cite as:
arXiv:2601.06112 [cs.AI]
(or
arXiv:2601.06112v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.06112
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Aayush Gupta [ view email ]
[v1]
Sat, 3 Jan 2026 13:41:33 UTC (16 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions, by Aayush Gupta
View PDF
HTML (experimental)
TeX Source
view license
Current browse context: cs.AI
< prev
|
next >
new
|
recent
| 2026-01
Change to browse by:
cs
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer ( What is the Explorer? )
Connected Papers Toggle
Connected Papers ( What is Connected Papers? )
Litmaps Toggle
Litmaps ( What is Litmaps? )
scite.ai Toggle
scite Smart Citations ( What are Smart Citations? )
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv ( What is alphaXiv? )
Links to Code Toggle
CatalyzeX Code Finder for Papers ( What is CatalyzeX? )
DagsHub Toggle
DagsHub ( What is DagsHub? )
GotitPub Toggle
Gotit.pub ( What is GotitPub? )
Huggingface Toggle
Hugging Face ( What is Huggingface? )
Links to Code Toggle
Papers with Code ( What is Papers with Code? )
ScienceCast Toggle
ScienceCast ( What is ScienceCast? )
Demos
Demos
Replicate Toggle
Replicate ( What is Replicate? )
Spaces Toggle
Hugging Face Spaces ( What is Spaces? )
Spaces Toggle
TXYZ.AI ( What is TXYZ.AI? )
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower ( What are Influence Flowers? )
Core recommender toggle
CORE Recommender ( What is CORE? )
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .
Which authors of this paper are endorsers? |
Disable MathJax ( What is MathJax? )
About
Help
Contact
Subscribe
Copyright
Privacy Policy
Web Accessibility Assistance
arXiv Operational Status

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-12-004.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-12-004.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-12-004.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
