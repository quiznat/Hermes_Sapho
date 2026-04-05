---
version: source-capture.v1
article_id: art-2026-03-08-002
ticket_id: ticket-import-art-2026-03-08-002
source_url: https://arxiv.org/abs/2603.02473
canonical_url: https://arxiv.org/abs/2603.02473
source_title: '[2603.02473] Diagnosing Retrieval vs. Utilization Bottlenecks in LLM
  Agent Memory'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-08T08:30:59Z'
---
# Source Capture

## Title

[2603.02473] Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory

## Body

[2603.02473] Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
Skip to main content
We gratefully acknowledge support from the Simons Foundation, member institutions , and all contributors.
Donate
> cs > arXiv:2603.02473
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
arXiv:2603.02473 (cs)
[Submitted on 2 Mar 2026]
Title: Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory
Authors: Boqin Yuan , Yue Su , Kun Yao
View a PDF of the paper titled Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory, by Boqin Yuan and 2 other authors
View PDF
HTML (experimental)
Abstract: Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval methods (cosine, BM25, hybrid reranking). On LoCoMo, retrieval method is the dominant factor: average accuracy spans 20 points across retrieval methods (57.1% to 77.2%) but only 3-8 points across write strategies. Raw chunked storage, which requires zero LLM calls, matches or outperforms expensive lossy alternatives, suggesting that current memory pipelines may discard useful context that downstream retrieval mechanisms fail to compensate for. Failure analysis shows that performance breakdowns most often manifest at the retrieval stage rather than at utilization. We argue that, under current retrieval practices, improving retrieval quality yields larger gains than increasing write-time sophistication. Code is publicly available at this https URL .
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2603.02473 [cs.AI]
(or
arXiv:2603.02473v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2603.02473
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Boqin Yuan [ view email ]
[v1]
Mon, 2 Mar 2026 23:47:23 UTC (3,599 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory, by Boqin Yuan and 2 other authors
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
| 2026-03
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
- runtime_article_bundle_path: research/articles/art-2026-03-08-002.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-08-002.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-08-002.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
- refreshed_live_source: false
