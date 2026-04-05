---
version: source-capture.v1
article_id: art-2026-03-09-005
ticket_id: ticket-import-art-2026-03-09-005
source_url: https://arxiv.org/html/2601.17581
canonical_url: https://arxiv.org/abs/2601.17581
source_title: 'How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull
  Requests'
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-05T14:13:06Z'
linked_paper_urls: []
---
# Source Capture

## Title

How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests

## Body

How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests

Daniel Ogenrwot 0000-0002-0133-8164 University of Nevada Las Vegas Las Vegas Nevada USA ogenrwot@unlv.nevada.edu and John Businge 0000-0003-3206-7085 University of Nevada Las Vegas Las Vegas Nevada USA john.businge@unlv.edu

(5 June 2009)

Abstract.

AI coding agents are increasingly acting as autonomous contributors by generating and submitting pull requests (PRs). However, we lack empirical evidence on how these agent-generated PRs differ from human contributions, particularly in how they modify code and describe their changes. Understanding these differences is essential for assessing their reliability and impact on development workflows. Using the MSR 2026 Mining Challenge version of the AIDev dataset, we analyze 24,014 merged Agentic PRs (440,295 commits) and 5,081 merged Human PRs (23,242 commits). We examine additions, deletions, commits, and files touched, and evaluate the consistency between PR descriptions and their diffs using lexical and semantic similarity. Agentic PRs differ substantially from Human PRs in commit count (Cliff’s δ = 0.5429 \delta=0.5429 ) and show moderate differences in files touched and deleted lines. They also exhibit slightly higher description-to-diff similarity across all measures. These findings provide a large-scale empirical characterization of how AI coding agents contribute to open source development.

AI coding agents, Agentic AI, LLMs, Pull Requests, Code patches 
† † copyright: acmlicensed † † journalyear: 2026 † † doi: XXXXXXX.XXXXXXX † † conference: MSR ’26: Proceedings of the 23rd International Conference on Mining Software Repositories; April 2026; Rio de Janeiro, Brazil † † ccs: Software and its engineering Collaboration in software development † † ccs: Computing methodologies Artificial intelligence

1. Introduction

Artificial intelligence (AI) coding agents are rapidly transforming software development. Tools such as GitHub Copilot (GitHub Copilot, 2025 ) , OpenAI Codex (OpenAI, 2025 ) , Claude Code (Anthropic, 2025 ) , Cursor (Cursor, 2025 ) , and Devin (Devin AI, 2025 ) can now autonomously generate code, fix bugs, and submit pull requests (PRs). These systems are evolving from assistive tools into active collaborators, a transition towards Software Engineering 3.0 (Hassan et al. , 2025 , 2024 ) . Prior work has examined how developers interact with AI-generated suggestions and how such tools affect productivity and code quality (Chen et al. , 2021 ; Vaithilingam et al. , 2022 ; Li et al. , 2025 ; Barke et al. , 2023 ; Hasan et al. , 2025 ; Vaithilingam et al. , 2023 ; Ogenrwot and Businge, 2025 ) , highlighting both opportunities and challenges for human–AI collaboration.

Despite this growing adoption, we still lack empirical evidence about how AI-generated PRs differ from human-authored ones in real-world repositories. In particular, little is known about how coding agents modify source code or how accurately their PR descriptions reflect the associated edits. These gaps limit our ability to assess their reliability, maintainability impact, and communicative clarity during code review. While existing research focuses primarily on usage patterns and developer interactions (Barke et al. , 2023 ; Vaithilingam et al. , 2023 ; Jin et al. , 2024 ) , large-scale analyses of autonomous AI-authored PRs remain scarce.

The MSR 2026 Mining Challenge dataset (Li et al. , 2025 ) enables this study by providing thousands of merged Agentic and Human PRs with commit histories and diff information. We therefore examine two research questions: RQ1: How do the structural characteristics of Agentic PRs, such as additions, deletions, files touched, and commit count, compare to Human-authored PRs? RQ2: How does the alignment between PR descriptions and code edits differ between Agentic and Human PRs?

These questions help reveal how AI agents behave as contributors and how effectively they communicate intent through natural language, both of which are critical for trust and collaboration in software engineering workflows.

Contributions.

- •

We conduct a large-scale empirical comparison of the structural code changes of Agentic and Human PRs using the MSR 2026 Mining Challenge dataset.

- •

We assess description-to-diff alignment to evaluate how well PR descriptions capture the underlying code modifications.

- •

We release a replication package containing curated data and analysis scripts to support reproducibility (Ogenrwot and Businge, 2026 ) .

2. Method

Figure 1 summarizes our four-step process: dataset collection, extension of Human PRs with commit-level data, filtering of merged PRs with valid patches, and computation of structural and similarity metrics for analysis.

Figure 1 . Four-step workflow: dataset collection, commit-data extension, PR filtering, and structural and similarity analysis. Four-step workflow: dataset collection, commit-data extension, PR filtering, and structural and similarity analysis.

Step 1: Dataset Collection. We use the AIDev dataset (Li et al. , 2025 ) provided for the MSR 2026 Mining Challenge (retrieved November 1, 2025). The dataset contains 932,791 Agentic PRs and 6,618 Human PRs across 116,211 repositories, along with a curated subset enriched with comments, reviews, and issue links. We use the Agentic PR set for structural analysis and reconstruct commit-level details for the Human PRs to enable consistent comparison.

Step 2: Extracting Human-PRs Commit Details. Unlike Agentic PRs, the Human PRs in the AIDev dataset lack commit-level information. To enable consistent comparison, we retrieved commit metadata and file-level patches for all Human PRs using the GitHub REST API (GitHub, 2025 ) . For each PR, we collected its commits and their associated details, including modified files, additions, deletions, and the unified diff when available. This reconstruction yields a commit-level structure matching that of the Agentic PRs. The number of files touched is computed as the set of unique file paths modified across all commits, ensuring repeated edits to the same file are counted once. File renames reported by GitHub are treated as single-file modifications.

Step 3: PRs Filtering Criteria. We focus on merged PRs, which provide complete commit histories. For Agentic PRs, we removed entries lacking patch text, required for computing structural and similarity metrics. A commit was considered to have a valid patch if the GitHub API returned a non-empty unified diff for all modified files. For Human PRs, we excluded cases with missing repositories, unavailable commit data, or incomplete patches retrieved from the GitHub API. After filtering, the analysis set contains 24,014 Agentic PRs (440,295 commits with valid patches) and 5,081 Human PRs (23,242 commits with valid patches). These datasets form the basis of all analyses in RQ1 and RQ2. Agentic PRs are also grouped by agent type for stratified analyses in the results.

Step 4: Data Analysis. For RQ1, we computed code-change metrics for each PR, including the number of commits, total lines added and deleted, and files touched.
Commit-level additions and deletions were summed across all commits in a PR, which avoids double-counting because GitHub reports per-file statistics.
We summarized the distributions of these metrics for Agentic and Human PRs. Normality assumptions were violated for all metrics, motivating the use of the Mann–Whitney U U test (McKnight and Najab, 2010 ; Mann and Whitney, 1947 ) to assess differences between the two groups. Effect sizes were quantified with Cliff’s delta ( δ \delta ) using standard interpretation thresholds (Long et al. , 2003 ; Romano et al. , 2006 ) .

For RQ2, we evaluate description–diff alignment along two dimensions. The first is lexical similarity , which measures surface-level overlap between the PR description and the code diff. We compute Term Frequency–Inverse Document Frequency (TF–IDF) cosine similarity and Okapi BM25, two standard information retrieval baselines widely used in software engineering tasks, particularly in bug report similarity and localization (Salton and Buckley, 1988 ; Robertson and Zaragoza, 2009 ; Yang et al. , 2016 ; Samir and Rahman, 2025 ) . PR titles and descriptions are concatenated and normalized. For all lexical and semantic analyses, code diffs are lowercased and stripped of diff metadata (file headers +++ / --- , hunk headers @@ , and leading + / - ), retaining only added and deleted lines with normalized whitespace.

Both PR description and code diff are then tokenized using a simple word-based tokenizer (Bird et al. , 2009 ) . Let d d denote the normalized description and c c the cleaned diff; TF–IDF cosine similarity is computed between vectors 𝐯 d \mathbf{v}_{d} and 𝐯 c \mathbf{v}_{c} , treating c c as the query to capture whether tokens introduced or modified by the patch are reflected in the description.

The second dimension is semantic similarity , which evaluates whether the meaning expressed in the PR description aligns with the underlying code edits. Embeddings are computed for both texts using CodeBERT (Feng et al. , 2020 ) and GraphCodeBERT (Guo et al. , 2021 ) , and similarity is measured using cosine similarity, a standard choice for comparing embedding vectors in semantic similarity settings (Reimers and Gurevych, 2019 ) . We include both CodeBERT and GraphCodeBERT to capture semantic similarity under distinct model architectures: a masked language model and a data-flow–aware encoder. RQ2 is evaluated on the subset of PRs that contain complete description text and valid diff data after filtering in Step 3.

TF–IDF and embedding cosine scores are bounded (typically in [ 0 , 1 ] [0,1] ), with larger values indicating stronger alignment. Okapi BM25, in contrast, is an unbounded relevance score whose magnitude depends on token frequencies and document length; long and token-heavy diffs can therefore produce very large positive or negative values. Negative Okapi BM25 values arise when very common tokens receive low inverse document frequency weights, which can reduce the summed relevance score for long diffs. As a result, Okapi BM25 should be interpreted only as a relative lexical signal rather than a calibrated similarity measure (Robertson and Zaragoza, 2009 ; Lv and Zhai, 2012 ) . Because absolute cutoffs are task-dependent, interpretation relies on the score distributions (e.g., medians and quartiles).

3. Results

RQ 1: How do the structural characteristics of Agentic PRs, such as additions, deletions, files touched, and commit count, compare to Human-authored PRs?

Figure 2 . Distribution of LOC added and deleted in agentic vs. human PRs. Distribution of LOC added and deleted in agentic vs. human PRs.

Figure 2 shows that Human PRs exhibit the largest and most variable code changes, with substantially higher medians and long upper tails for both additions and deletions. Agentic PRs tend to introduce smaller and more localized edits. Within the Agentic group, Claude Code and OpenAI Codex display somewhat greater variability in their additions, whereas Devin, Cursor, and especially Copilot produce more consistently small and localized changes.

Key takeaway: Agentic PRs tend to introduce smaller and more localized changes than Human PRs, though some agents (e.g. Claude Code and OpenAI Codex) show broader variability than others.

Figure 3 . Distribution of commits and files touched across agents and human PRs. Distribution of commits and files touched across agents and human PRs.

Figure 3 shows that Human PRs touch more files and often involve more commits than Agentic PRs, indicating broader and more distributed modifications. Claude Code and OpenAI Codex again show a wider spread than other agents, while Devin, Cursor, and Copilot exhibit narrow distributions that reflect highly localized edits. Human contributions consistently span more files and commit steps, matching the large effect size observed for commit count.

Key takeaway: Agentic PRs are not uniform; some tools generate highly compact, single-focus contributions, while others produce broader edits that overlap more closely with the lower range of Human PRs.

Table 1. Cliff’s δ \delta Effect Sizes - agentic vs. human PRs

Metric Cliff’s δ \delta Effect Size

Commits 0.5429 Large

Files Touched 0.4487 Medium

Additions 0.2836 Small

Deletions 0.4462 Medium

Line Changes (add + + delete) 0.3158 Small

Table 1 shows that the largest practical difference between Agentic and Human PRs is the number of commits ( δ = 0.54 \delta=0.54 , large effect), indicating distinct contribution patterns in how changes are structured. Medium effects for files touched and deletions suggest that Human PRs modify codebases more broadly and remove more code. In contrast, additions and total line changes show only small effects, suggesting that the overall quantity of code introduced is closer between the two groups than the structure of the edits. Overall, the result of the Mann–Whitney U U test shows that the differences are statistically significant ( p ≤ 0.001 p\leq 0.001 ).

Key takeaway: The most distinctive characteristics of Agentic PRs are not simply how many lines they change, but how they organize and distribute changes across commits and files.

RQ 2: How does the alignment between PR descriptions and code edits differ between Agentic and Human PRs?

Figure 4 . Kernel density estimates comparing lexical and semantic similarity distributions. Kernel density estimates comparing lexical and semantic similarity distributions Figure 5 . Distribution of similarity scores across lexical and semantic metrics for both Agentic and Human PRs. Distribution of similarity scores across lexical and semantic metrics for both Agentic and Human PRs. Table 2. Descriptive statistics for lexical and semantic similarity metrics, grouped by PR Type.

Statistic Agentic PRs Human PRs

Lexical Semantic Lexical Semantic

TF–IDF Okapi BM25 CodeBERT GraphCodeBERT TF–IDF Okapi BM25 CodeBERT GraphCodeBERT

Mean 0.1245 2.8455 0.9356 0.8254 0.1007 0.1739 0.9285 0.7815

Std. 0.1104 466.2787 0.0331 0.0654 0.1054 23.1437 0.0423 0.1016

Min 0.0000 -13776.6311 0.7243 0.4183 0.0000 -1271.3196 0.6259 0.2875

25% 0.0479 -0.3836 0.9141 0.7889 0.02413 -0.2380 0.9042 0.7254

50% 0.0937 1.0169 0.9375 0.8302 0.0680 0.0000 0.9347 0.8067

75% 0.1655 1.4011 0.9605 0.8708 0.1465 1.1236 0.9617 0.8563

Max 0.9535 68947.5283 0.9974 0.9807 0.9266 585.4945 0.9939 0.9788

We first examine the distribution of lexical and semantic similarity scores for Human and Agentic PRs. Figure 4 shows a clear separation between lexical and semantic similarity. Lexical scores for both Agentic and Human PRs cluster near zero, indicating very limited surface-level vocabulary overlap between descriptions and diffs. In contrast, semantic similarity scores form tight peaks between 0.9 and 1.0, suggesting that both description types capture the underlying meaning of their patches even when exact wording differs.

Figure 5 presents distributional comparisons across all four metrics. Agentic PRs show a slight right-shift relative to Human PRs across both lexical and semantic measures, although the difference is small in absolute terms and both groups show high semantic alignment. The lexical measures remain heavily skewed, while the semantic models produce consistently high similarity scores, with Agentic PRs displaying tighter clustering. Okapi BM25 exhibits extremely high variance and large positive or negative values, particularly for Agentic PRs, reflecting the unbounded nature of the score and its sensitivity to tokenization. As a result, Okapi BM25 should be interpreted only as a coarse lexical indicator rather than a calibrated similarity measure.

Table 2 shows that Agentic PRs have slightly higher central tendency across all four metrics. The differences are modest, but they suggest that agent-generated descriptions align at least as well, and in some cases slightly better, with the content of their edits compared to human descriptions.

Key takeaway: Agentic PR descriptions exhibit description-to-diff consistency that is comparable to, and in some metrics slightly higher than, Human PRs, with the clearest differences appearing in the semantic similarity measures.

4. Implications

RQ1 shows that differences between Agentic and Human PRs arise not only in the amount of code changed, but in how changes are structured and distributed. Review processes and triage heuristics may therefore benefit from using commit count and files touched as early indicators of an Agentic PR’s scope, rather than relying solely on LOC-based measures. Deletion-heavy or wide-scope Agentic PRs may warrant closer review, although further work is needed to link these structural patterns to concrete risks. Variability across agent types further suggests that Agentic PR behavior is not uniform, and that modeling agent identity and task context may be important when studying downstream outcomes such as review effort, latency, or defect likelihood.

For RQ2, the consistently high semantic alignment between descriptions and diffs suggests that agent-authored PR description is generally coherent with the code edits it describes. This level of consistency may support downstream tasks that depend on accurate summaries, such as release-note generation, change-log construction, or reviewer routing. Automated checks could further highlight cases where description–diff alignment is unusually low, enabling developers to intervene when an Agentic PR is potentially ambiguous or misleading.

5. Related Work

Research on AI-assisted programming has examined models such as Codex and GitHub Copilot, focusing on code completion, developer productivity, and interaction patterns (Chen et al. , 2021 ; Vaithilingam et al. , 2022 , 2023 ; Barke et al. , 2023 ; Ogenrwot and Businge, 2024 , 2025 ) . Most of this work investigates snippet-level behavior rather than project-scale contributions such as pull requests.

Software engineering studies on human-authored patches have analyzed patch size, structure, and review effort (Gousios et al. , 2014 ; Kononenko et al. , 2016 ; Wang et al. , 2025 ; Watanabe et al. , 2025 ) and their relationships to maintainability and defect risk (Rahman et al. , 2013 ; Chen and Jiang, 2025 ) . Empirical analyses of AI-generated patches remain limited, though early work reports refactoring (Horikawa et al. , 2025 ) , stylistic repetition, boilerplate generation, and occasional inconsistencies between descriptions and code changes (Tambon et al. , 2025 ; Horikawa et al. , 2025 ; Wu et al. , 2025 ) .
The AIDev dataset (Li et al. , 2025 ) enables the first large-scale, PR-level analysis of how AI agents author and describe code changes in real-world repositories, addressing a gap in existing literature.

6. Threats to Validity

Internal validity. Our results depend on the completeness of the AIDev dataset and the reconstructed Human-PR commit data. Missing or truncated patches may bias the distributions, although PRs lacking patch text were excluded. GitHub API retrieval for Human PRs may introduce gaps due to rate limits, deleted repositories, or rewritten histories. Additionally, it may truncate diffs for very large changes, which can reduce patch completeness and may affect similarity metrics computed from diff text.

Construct validity. Our structural metrics (additions, deletions, commits, files touched) approximate PR scope but do not capture intent or correctness. Lexical and semantic similarity measure description–diff alignment, but not code quality or reviewer understanding. Okapi BM25 is unbounded and sensitive to tokenization, so it should be interpreted only as a relative lexical indicator.

External validity. Findings generalize to open-source GitHub projects represented in the AIDev dataset and to the agent versions included in it. Results may differ in private or industrial settings, with different review cultures, or as coding agents evolve.

7. Conclusion

We conducted a large-scale empirical comparison of Agentic and Human PRs in the AIDev dataset. Agentic PRs differ most clearly in commit structure and the breadth of modified files, while differences in added or changed lines are relatively small. For RQ2, both PR types show high semantic alignment between descriptions and code, with Agentic PRs exhibiting slightly stronger consistency. These findings suggest that AI-generated PRs are structurally distinct yet generally coherent in how they describe their edits. Future work should examine how these patterns relate to review effort, defect risk, and maintainability as coding agents and development workflows continue to evolve.

Acknowledgements. 
This research was supported by NSF Grant Award No. AWD-02-00002782. We also acknowledge NSF MRI (#2117941) for GPU Cluster support.

References

- Anthropic (2025) Claude.ai . Note: https://claude.ai/ Accessed: 2025-12-14 Cited by: §1 .

- S. Barke, S. Bansal, and N. Polikarpova (2023) Grounded copilot: how programmers interact with code-generating models . In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems , USA , pp. 1–13 . Cited by: §1 , §1 , §5 .

- S. Bird, E. Klein, and E. Loper (2009) Natural language processing with python . 1st edition , O’Reilly Media, Inc. , USA . External Links: ISBN 0596516495 Cited by: §2 .

- M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, G. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. Such, D. Cummings, M. Plappert, F. Chantzis, M. Barnes, A. Herbert-Voss, W. Guss, A. Nichol, C. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, I. Sutskever, and D. Amodei (2021) Evaluating large language models trained on code . In Proceedings of the NeurIPS 2021 Datasets and Benchmarks Track , USA . Cited by: §1 , §5 .

- Z. Chen and L. Jiang (2025) Evaluating software development agents: patch patterns, code quality, and issue complexity in real-world github scenarios . In 2025 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER) , Vol. , pp. 657–668 . External Links: Document Cited by: §5 .

- Cursor (2025) Cursor: ai code editor . Note: https://cursor.com/ Accessed: 2025-12-14 Cited by: §1 .

- Devin AI (2025) Devin ai — ai coding assistant . Note: https://app.devin.ai/ Accessed: 2025-12-14 Cited by: §1 .

- Z. Feng, D. Guo, D. Tang, N. Duan, X. Feng, M. Gong, L. Shou, B. Qin, T. Liu, D. Jiang, and M. Zhou (2020) CodeBERT: a pre-trained model for programming and natural languages . External Links: 2002.08155 , Link Cited by: §2 .

- GitHub Copilot (2025) GitHub copilot . Note: https://github.com/copilot Accessed: 2025-12-14 Cited by: §1 .

- GitHub (2025) GitHub rest api documentation . Note: https://docs.github.com/en/rest?apiVersion=2022-11-28 Accessed: 2025-12-14 Cited by: §2 .

- G. Gousios, M. Pinzger, and A. v. Deursen (2014) An exploratory study of the pull-based software development model . In Proceedings of the 36th International Conference on Software Engineering (ICSE) , USA , pp. 345–355 . Cited by: §5 .

- D. Guo, S. Ren, S. Lu, Z. Feng, D. Tang, S. Liu, L. Zhou, N. Duan, A. Svyatkovskiy, S. Fu, M. Tufano, S. K. Deng, C. Clement, D. Drain, N. Sundaresan, J. Yin, D. Jiang, and M. Zhou (2021) GraphCodeBERT: pre-training code representations with data flow . External Links: 2009.08366 , Link Cited by: §2 .

- M. M. Hasan, H. Li, E. Fallahzadeh, G. K. Rajbahadur, B. Adams, and A. E. Hassan (2025) An empirical study of testing practices in open source ai agent frameworks and agentic applications . External Links: 2509.19185 , Link Cited by: §1 .

- A. E. Hassan, H. Li, D. Lin, B. Adams, T. Chen, Y. Kashiwa, and D. Qiu (2025) Agentic software engineering: foundational pillars and a research roadmap . External Links: 2509.06216 , Link Cited by: §1 .

- A. E. Hassan, G. A. Oliva, D. Lin, B. Chen, Z. Ming, and Jiang (2024) Towards ai-native software engineering (se 3.0): a vision and a challenge roadmap . External Links: 2410.06107 , Link Cited by: §1 .

- K. Horikawa, H. Li, Y. Kashiwa, B. Adams, H. Iida, and A. E. Hassan (2025) Agentic refactoring: an empirical study of ai coding agents . arXiv preprint arXiv:2511.04824 . Cited by: §5 .

- H. Jin, S. Lee, H. Shin, and J. Kim (2024) Teach ai how to code: using large language models as teachable agents for programming education . In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems , CHI ’24 , New York, NY, USA . External Links: ISBN 9798400703300 , Link , Document Cited by: §1 .

- O. Kononenko, O. Baysal, and M. W. Godfrey (2016) Code review quality: how developers see it . In Proceedings of the 38th International Conference on Software Engineering , ICSE ’16 , New York, NY, USA , pp. 1028–1038 . External Links: ISBN 9781450339001 , Link , Document Cited by: §5 .

- H. Li, H. Zhang, and A. E. Hassan (2025) The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering . arXiv preprint arXiv:2507.15003 . Cited by: §1 , §1 , §2 , §5 .

- J. D. Long, D. Feng, and N. Cliff (2003) Ordinal analysis of behavioral data . Handbook of psychology , pp. 635–661 . Cited by: §2 .

- Y. Lv and C. Zhai (2012) A log-logistic model-based interpretation of tf normalization of bm25 . In Advances in Information Retrieval , R. Baeza-Yates, A. P. de Vries, H. Zaragoza, B. B. Cambazoglu, V. Murdock, R. Lempel, and F. Silvestri (Eds.) , Berlin, Heidelberg , pp. 244–255 . External Links: ISBN 978-3-642-28997-2 Cited by: §2 .

- H. B. Mann and D. R. Whitney (1947) On a test of whether one of two random variables is stochastically larger than the other . The Annals of Mathematical Statistics 18 ( 1 ), pp. 50–60 . External Links: ISSN 00034851 , Link Cited by: §2 .

- P. E. McKnight and J. Najab (2010) Mann-whitney u test . In The Corsini Encyclopedia of Psychology , pp. 1–1 . External Links: ISBN 9780470479216 , Document , Link , https://onlinelibrary.wiley.com/doi/pdf/10.1002/9780470479216.corpsy0524 Cited by: §2 .

- D. Ogenrwot and J. Businge (2024) PatchTrack: analyzing chatgpt’s impact on software patch decision-making in pull requests . In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering , ASE ’24 , New York, NY, USA , pp. 2480–2481 . External Links: ISBN 9798400712487 , Link , Document Cited by: §5 .

- D. Ogenrwot and J. Businge (2025) PatchTrack: a comprehensive analysis of chatgpt’s influence on pull request outcomes . External Links: 2505.07700 , Link Cited by: §1 , §5 .

- D. Ogenrwot and J. Businge (2026) Replication package for how ai coding agents modify code: a large-scale study of github pull requests External Links: Document , Link Cited by: 3rd item .

- OpenAI (2025) Codex — openai . Note: https://openai.com/codex/ Accessed: 2025-12-14 Cited by: §1 .

- F. Rahman, D. Posnett, and P. Devanbu (2013) Predicting defect-prone software modules using code change metrics . Empirical Software Engineering 18 ( 5 ), pp. 875–908 . Cited by: §5 .

- N. Reimers and I. Gurevych (2019) Sentence-bert: sentence embeddings using siamese bert-networks . External Links: 1908.10084 , Link Cited by: §2 .

- S. E. Robertson and H. Zaragoza (2009) The probabilistic relevance framework: BM25 and beyond . Found. Trends Inf. Retr. 3 ( 4 ), pp. 333–389 . External Links: Link , Document Cited by: §2 , §2 .

- J. Romano, J. D. Kromrey, J. Coraggio, J. Skowronek, and L. Devine (2006) Exploring methods for evaluating group differences on the nsse and other surveys: are the t-test and cohen’sd indices the most appropriate choices . In annual meeting of the Southern Association for Institutional Research , Vol. 14 . Cited by: §2 .

- G. Salton and C. Buckley (1988) Term-weighting approaches in automatic text retrieval . Information Processing & Management 24 ( 5 ), pp. 513–523 . External Links: ISSN 0306-4573 , Document , Link Cited by: §2 .

- A. M. Samir and M. M. Rahman (2025) Improved ir-based bug localization with intelligent relevance feedback . In 2025 IEEE/ACM 33rd International Conference on Program Comprehension (ICPC) , Vol. , USA , pp. 560–571 . External Links: Document Cited by: §2 .

- F. Tambon, A. Moradi-Dakhel, A. Nikanjam, F. Khomh, M. C. Desmarais, and G. Antoniol (2025) Bugs in large language models generated code: an empirical study . Empirical Software Engineering 30 ( 3 ), pp. 65 . External Links: Document , ISBN 1573-7616 , Link Cited by: §5 .

- P. Vaithilingam, Z. Xu, and E. L. Glassman (2023) Copilot or co-author? examining the role of code generation tools in collaborative programming . In Proceedings of the 2023 IEEE Symposium on Visual Languages and Human-Centric Computing (VL/HCC) , USA . Cited by: §1 , §1 , §5 .

- P. Vaithilingam, T. Zhang, and E. L. Glassman (2022) Expectation vs. experience: evaluating the usability of code generation tools powered by large language models . In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems , USA , pp. 1–17 . Cited by: §1 , §5 .

- F. Wang, B. Do, and J. Jermier (2025) Automated vs. human security patching patterns in pull requests: evidence from the aidev dataset . Cited by: §5 .

- M. Watanabe, H. Li, Y. Kashiwa, B. Reid, H. Iida, and A. E. Hassan (2025) On the use of agentic coding: an empirical study of pull requests on github . External Links: 2509.14745 , Link Cited by: §5 .

- Y. Wu, Y. Wang, Y. Li, W. Tao, S. Yu, H. Yang, W. Jiang, and J. Li (2025) An empirical study on commit message generation using llms via in-context learning . In 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE) , Vol. , pp. 553–565 . External Links: Document Cited by: §5 .

- X. Yang, D. Lo, X. Xia, L. Bao, and J. Sun (2016) Combining word embedding with information retrieval to recommend similar bug reports . In 2016 IEEE 27th International Symposium on Software Reliability Engineering (ISSRE) , Vol. , USA , pp. 127–137 . External Links: Document Cited by: §2 .
