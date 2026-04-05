---
version: source-capture.v1
article_id: art-2026-03-10-077
ticket_id: ticket-import-art-2026-03-10-077
source_url: https://arxiv.org/html/2601.17627v1
canonical_url: https://arxiv.org/abs/2601.17627
source_title: 'Code Change Characteristics and Description Alignment: A Comparative
  Study of Agentic versus Human Pull Requests'
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-05T16:11:16Z'
linked_paper_urls: []
---
# Source Capture

## Title

Code Change Characteristics and Description Alignment: A Comparative Study of Agentic versus Human Pull Requests

## Body

Code Change Characteristics and Description Alignment: A Comparative Study of Agentic versus Human Pull Requests

Dung Pham Department of Computer Science Trent University Peterborough Ontario Canada dungpham290198@gmail.com and Taher A. Ghaleb 0000-0001-9336-7298 Department of Computer Science Trent University Peterborough Ontario Canada taherghaleb@trentu.ca

(2026)

Abstract.

AI coding agents can autonomously generate pull requests (PRs), yet little is known about how their contributions compare to those of humans. We analyze 33,596 agent-generated PRs (APRs) and 6,618 human PRs (HPRs) to compare code-change characteristics and message quality.
We observe that APR-introduced symbols (functions and classes) are removed much sooner than those in HPRs (median time to removal 3 vs. 34 days) and are also removed more often (symbol churn 7.33% vs. 4.10%), reflecting a focus on other tasks like documentation and test updates.
Agents generate stronger commit-level messages (semantic similarity 0.72 vs. 0.68) but lag humans at PR-level summarization (PR–commit similarity 0.86 vs. 0.88). Commit message length is the best predictor of description quality, indicating reliance on individual commits over full-PR reasoning.
These findings highlight a gap between agents’ micro-level precision and macro-level communication, suggesting opportunities to improve agent-driven development workflows.

Pull requests, Code changes, Agentic software development, Commit messages, Mining software repositories 
† † journalyear: 2026 † † conference: 23rd International Conference on Mining Software Repositories; April 13–14, 2026; Rio de Janeiro, Brazil † † booktitle: 23rd International Conference on Mining Software Repositories, April 13–14, 2026, Rio de Janeiro, Brazil † † ccs: Software and its engineering Software version control † † ccs: Software and its engineering Development frameworks and environments

1. Introduction

Large language models are increasingly used for software development
tasks such as code generation and pull request (PR) creation ( Mo et al. , ; Watanabe et al. , 2025 ; Cotroneo et al. , 2025 ) . Recent agentic systems extend these capabilities through multi-step contributions (Wang et al. , 2025 ) ,
motivating an examination of how agent-generated pull requests differ from human ones in code change patterns and communication quality, which
directly affect reliability, maintainability, and security (Cotroneo et al. , 2025 ) . PRs communicate changes through descriptions
and commit messages. Automated commit message generation still exhibits
poor generalization ability (Wu et al. , 2025 ) . Since PRs often span
multiple commits, generating PR-level descriptions requires additional
effort (Sakib et al. , 2024 ) . This challenge underscores the need to
understand whether agent-generated PRs (APRs) differ from human PRs (HPRs) in their
communication effectiveness.

In this paper, we address two research questions: (RQ1) How do APRs and HPRs differ in code change characteristics (files changed, code churn, lines added/removed, and change purposes)? (RQ2) How well do APR descriptions and commit messages align with code changes? To do this, we introduce three alignment metrics: PR–commit similarity, patch–message similarity, and an LLM-based consistency score, and build a classification model to identify the factors that predict strong agent-generated PR descriptions.
Our results reveal that APRs consistently make smaller, more focused changes and excel at describing them at the commit level, but they perform worse than humans when articulating the broader, PR-level narrative.

Paper organization. Section 2 describes our data collection. Sections 2.3 and 2.4 analyze code change characteristics (RQ1) and description alignment (RQ2). Section 3 discusses the implications, Section 4 discusses threats to validity, Section 5 reviews related work, and Section 6 concludes and outlines future work.

Replication Package: Our data,
scripts, notebooks, prompts and results can be found in our replication package (Pham and Ghaleb, 2026 )

2. Empirical Analysis and Results

2.1. Data collection

In this study, we use the AIDev-pop subset of the AIDev dataset (Oct 28, 2025 update) (Li et al. , 2025 ) , which contains 33,596 curated agentic PRs (APRs) from five major autonomous coding agents:
OpenAI Codex (21,799 PRs), Devin (4,827 PRs), GitHub Copilot (4,970 PRs), Cursor (1,541 PRs), and Claude Code (459 PRs). We also use a dataset of 6,618 human PRs (HPRs), and because detailed commit information was not provided, we constructed a complementary dataset by retrieving commit IDs, changed files, change types, patch diffs (added and removed lines of code), and commit messages via the GitHub API. The APRs span 2024-12 to 2025-07 and the HPRs 2025-01 to 2025-06, covering comparable periods.
We further computed benchmark metrics (RQ2) from samples of the two datasets, by randomly sampling 663 instances (corresponding to a 99% confidence level with a ± \pm 5% margin of error) from the cleaned training set (138,895 records) of Tire et al. (Tire et al. , 2025 ) and 664 instances from the 249,688 test samples of the CommitBench dataset (Schall et al. , 2024 ) .

2.2. Terminologies

We define agentic PRs as APRs and human PRs as HPRs . The Merged PR ratio is computed over all PRs with a close date: PRs with a merge date are considered successful, others are not. Task type refers PR purpose, e.g., feature ( feat ) or bug fix ( fix ) as in Hao Li et al. (Li et al. , 2025 ) . A Directory is the immediate parent folder of a changed file. Symbols are functions or classes extracted from patch diffs. Symbol churn refers to symbols that are introduced in a commit and subsequently removed in a later commit. We measure PR–Commit Similarity (semantic alignment between PR description and commit messages) and Patch–Commit Similarity (alignment between diff and messages). The LLM-based Consistency Score is a GPT-4o rating of the quality of the commit message.

2.3. Code Change Characteristics

It is important to understand how agentic code changes differ from human changes, to help teams identify tasks agents handle well, where they fall short, and what needs extra review before merging.

RQ1.1: Do agents and humans differ in the footprint of their code modifications?

Approach. We compute the merge rate and four median per-PR change metrics (commits, changed files, directories, and lines) for 31,268 closed APRs and compare them with 6,135 closed HPRs. We model merge outcomes using multivariate logistic regression with footprint metrics (commits, files, directories) to assess their relation to merge success. We model PR task types with Poisson regression on the footprint, chosen for interpretability and to quantify effect sizes via odds ratios (OR) or incidence rate ratios (IRR), with statistical significance tested using p p -values. Poisson regression is appropriate for non-negative, often non-normal and positively skewed count data (Hutchinson and Holtman, 2005 ) . We assess statistical differences between APRs and HPRs in these metrics are evaluated using the Mann–Whitney U test (Mann and Whitney, 1947 ) and proportional z-test (Agresti and Kateri, 2011 ) , with α = 0.05 \alpha=0.05 .

Results. APRs show lower merge rates and smaller change footprints, and a higher number of commits in a PR is associated with reduced merge success. Table 1 shows that APRs have a lower merge rate than HPRs (76.80% vs. 82.82%, p < 0.001 p<0.001 ) and smaller footprints: fewer commits (median 1 vs. 2, p < 0.001 p<0.001 ), files (median 3 vs. 4, p < 0.001 p<0.001 ), and directories (median 1 vs. 2, p < 0.001 p<0.001 ). The number of changed lines does not differ significantly ( p = 0.131 p=0.131 ). Logistic regression indicates that the number of commits is a strong negative predictor of merging (OR = 0.95, p < 0.001 p<0.001 ), with each additional commit reducing merge odds by about 5%; the numbers of files and directories changed have no significant association ( p > 0.01 p>0.01 ).

This lower number-of-commits pattern is associated with PR task types. The Poisson regression shows that task type is significantly associated with commit count. We use feature development ( feat ) as the reference group, since it is most common and represents a typical PR. Documentation (IRR = 0.74, p < 0.001 p<0.001 ), test (IRR = 0.72, p < 0.001 p<0.001 ), and style (IRR = 0.64, p < 0.001 p<0.001 ) PRs involve about 26%, 28%, and 36% fewer commits than feature PRs. In contrast, chore (IRR = 1.13, p < 0.001 p<0.001 ) and refactoring (IRR = 1.15, p < 0.001 p<0.001 ) PRs involve about 13% and 15% more commits, respectively, compared to the reference group. Table 2 shows that feature (feat) and bug fix (fix) tasks are the two most common task types for both groups, but the third and fourth most frequent tasks differ: APRs focus more on documentation and test tasks, whereas HPRs handle more build and chore tasks. This helps explain why APRs have fewer commits per PR than HPRs. Future research should further investigate possible causes, such as task selection bias, agent prompting strategies, or autonomy levels, to derive more actionable guidance.

Table 1. Agentic PRs (APR) vs. Human PRs (HPR) Metrics.

Metric APR HPR

# of PRs 31,268 6,135

Merge Rate 76.80% 82.82%

Median # of Commits 1 2

Median # of Files Changed 3 4

Median # of Directories Changed 1 2

Median # of Lines Changed 90 88 
Table 2. Top Task Types for APR and HPR

Rank APR: Top Tasks HPR: Top Tasks

Top 1 Feat (42.79%) Feat (28.48%)

Top 2 Fix (23.59%) fix (27.19%)

Top 3 Docs (11.95%) Chore (13.32%)

Top 4 Test (7.22%) Build (9.60%)

RQ1.2: Do agents and humans differ in symbol churn and the timing of subsequent modifications?

Approach. We evaluate PR quality using two metrics: (1) time to next modification and (2) symbol churn. For time to next modification, we track when each file is first added and merged, then compute the number of days until its next modification in a later PR. For symbol churn, we extract functions and classes from patch diffs for the top three languages in the AIDev-Pop dataset (TypeScript, Python, and Go) (Li et al. , 2025 ) using regular-expression patterns, then measure the days from symbol introduction to first removal. Differences between APRs and HPRs are assessed with the Mann–Whitney U test for days to modification and churn, and a proportional z-test for modification and symbol-churn ratios (all at α = 0.05 \alpha=0.05 ).

Results. Files and symbols introduced by APRs change more frequently and much sooner than those in HPRs. Table 3 summarizes the key findings on time to next modification and symbol churn. APRs show a higher file-modification ratio than HPRs (14.36% vs. 3.36%, p < 0.001 p<0.001 ) and are modified far earlier (median 0.88 days vs. 23 days, p < 0.001 p<0.001 ). For symbol-level changes, the pattern is similar: among 7,338 APR symbols and 8,089 HPR symbols, APRs exhibit a higher churn rate (7.33% vs. 4.10%, p < 0.001 p<0.001 ) and their symbols are removed much sooner (median 3 days vs. 34 days, p < 0.001 p<0.001 ).
This early churn can be explained with the task-type distribution observed in RQ1.1: For APRs, documentation and tests are among the top categories of work (table 2 ), areas that naturally evolve quickly. For example, in one documentation-related PR 1 1 1 https://github.com/Azure/azure-sdk-for-python/pull/41463 , the function send_with_run_in_executor was introduced and then removed just two days later in a subsequent PR 2 2 2 https://github.com/Azure/azure-sdk-for-python/pull/41352 .

Table 3. Time to Next Modification and Code Churn Comparison between APR and HPR

Time to Next Modification Code Churn

Type #New Added Files % Modification Median #Days #New Functions/Classes %Churn Rate Median #Days

APR 87,277 14.36% 0.88 7,338 7.33% 3

HPR 23,989 3.36% 29.2 8,089 4.10% 34

2.4. Description Alignment

It is important to examine how well agents’ PR descriptions reflect the underlying code changes. Understanding description quality and its drivers helps reveal where agents fall short and how to improve PR clarity and reliability.

RQ2.1: How well do PR descriptions and commit messages align with code changes?

Approach. We address this RQ using three alignment metrics: (1) PR–Commit Similarity: We measure the semantic similarity between PR descriptions and commit messages by using GistEmbed (Solatorio, 2024 ) , the top-performing model in prior benchmarks (Sutriawan et al. , 2025 ) , by computing embeddings for both texts and then calculating cosine similarity. (2) Patch–Commit Similarity: We use a fine-tuned CodeT5-Without-History model (Eliseeva et al. , 2023 ) to generate commit messages from patch diffs, as it is recognized as a state-of-the-art model for commit message generation (Zhang et al. , 2024 ) and is widely used as a baseline in prior work (Shi et al. , 2022 ; Wu et al. , 2025 ) . Using the history-free variant isolates patch-level semantic alignment and avoids stylistic or project-specific confounds. We then embed both generated and actual messages with GistEmbed and compute cosine similarity. (3) LLM Consistency Score: We use GPT-4o to evaluate the metric based on established criteria for good commit messages (Tian et al. , 2022 ) , as it aligns well with human judgments, outperforms traditional lexical metrics ( liu2023g ) , and has been widely adopted as a judge model in LLM-as-a-Judge frameworks (Huang et al. , 2025 ; Wei et al. , 2024 ; Mohammadkhani and Beigy, 2025 ) . Full prompt is in our replication package (Pham and Ghaleb, 2026 ) . This RQ focuses on assessing description alignment, so deleted symbols are retained to preserve generalizability.

We filter PR text for English, as it constitutes the vast majority of the dataset ( ≈ \approx 98%), and to ensure linguistic consistency, using the XLM-R model (Papluca, 2022 ) with a confidence threshold > 0.7 >0.7 . XLM-R has strong performance on language identification tasks (Conneau et al. , 2020 ) , yielding 22,633 APRs and 4,009 HPRs. From these, we sample 647 APRs and 571 HPRs (99% confidence level, 5% margin of error).
Due to the lack of ground-truth labels for PR–code alignment, we use high-quality datasets from prior work as benchmarks: 663 PR–commit instances from Tire et al. (Tire et al. , 2025 ) and 664 patch–commit instances from CommitBench (Schall et al. , 2024 ) . Statistical significance is assessed using the Kruskal–Wallis test (Kruskal and Wallis, 1952 ) followed by Dunn’s post-hoc test (Dunn, 1964 ) . We report effect sizes using epsilon-squared ( ε 2 \varepsilon^{2} ).

Results. Agents are better at describing individual commits, while humans are better at summarizing PR-level changes. As shown in Figure 1 , APRs achieve higher commit-level alignment than HPRs both in semantic similarity (median 0.72 vs. 0.68, p < 0.001 p<0.001 ) and in LLM-as-a-judge scores (median 4/10 vs. 2/10), with p < 0.001 p<0.001 and effect sizes of ε 2 ≈ 0.12 \varepsilon^{2}\approx 0.12 and 0.17 0.17 , respectively. In contrast, at the PR level, APRs score lower than humans in PR–commit similarity (0.86 vs. 0.88, p < 0.001 p<0.001 ), but with an effect size of ε 2 ≈ 0.04 \varepsilon^{2}\approx 0.04 . All differences are statistically significant under the Kruskal–Wallis test with Dunn’s post-hoc correction ( α = 0.05 \alpha=0.05 ).

Figure 1. Distribution of PR-commit similarity score, Patch-commit similarity score and LLM-based consistency score. Three boxplots comparing Agentic PRs (APR) and Human PRs (HPR). 1) PR-Commit Similarity: HPR median is slightly higher than APR. 2) Patch-Commit Similarity: APR median is higher than HPR. 3) LLM Score: APR median is higher (4) compared to HPR (2).

These results show that agents produce precise commit-level messages, but struggle to combine multiple commits into a coherent PR-level summary, which humans perform better. Benchmark results also show that both APRs and HPRs still lag behind high-quality references, leaving room for improvement at both levels.

RQ2.2: What factors predict APR description quality?

Approach. To study what distinguishes strong agent-generated PR descriptions from weak ones, we frame the problem as a binary classification task. A description is labeled “good” if its PR–commit similarity score is ≥ 0.9 \geq 0.9 . Following prior work (Ortiz Martes et al. , 2025 ) , which notes that semantic-similarity thresholds should be tuned to application goals, we select 0.9 based on the distribution of PR–commit similarity scores of (Figure 1 ), where it roughly corresponds to the 75th percentile and thus marks the cutoff for the top 25% highest-scoring descriptions.
We then model this classification task using Random Forest (RF), k-Nearest Neighbors (KNN), Light Gradient Boosting Machine (LightGBM), and Extreme Gradient Boosting (XGBoost) classifiers. We also perform a sensitivity analysis to examine the impact of varying the threshold from the median to the 75th percentile (0.85–0.9 in increments of 0.01) on feature importance.
We construct three categories of features: (1) Descriptive attributes: title length, body length, task type, template score, code-snippet flag; (2) Development activity: related-issue count, commit count, average commit-message length; and (3) Code changes: number of files changed, additions, deletions, total changes, change-status distribution, directories changed.
We split the data into 80% training ( 17 , 728 17,728 PRs) and 20% testing ( 4 , 433 4,433 PRs). Last, we apply SHAP to identify the strongest features to predict high-quality descriptions.

Results. Commit message length is the strongest predictor of a good APR description (max SHAP: 0.57) , followed by PR title and PR body length (max SHAP: 0.21 and 0.20, respectively). As shown in Figure 2, high-quality APR descriptions are strongly associated with commit messages ≥ \geq 13 words, PR titles ≥ \geq 7 words, and PR bodies ≥ \geq 80 words.
We observe that RF outperformed other classifiers across all metrics (Accuracy: 86.22%, AUC: 79.86%, Precision: 72.8%, Recall: 31.9%, F1-score: 44.40%) and was therefore selected for SHAP analysis. The relatively low F1-score results from the strict PR–commit similarity threshold ( ≥ 0.9 \geq 0.9 ) defining high-quality descriptions, creating strong class imbalance and favoring precision over recall. Threshold sensitivity analysis (0.85–0.9) shows F1-score decreasing from ≈ \approx 71% to 44% as the cutoff increases, while AUC rises from ≈ \approx 73% to 79%. As our goal is feature attribution rather than deployment-ready classification, RF is sufficient to identify the dominant predictors of high-quality descriptions.

Figure 2. SHAP values of the top 3 features that contributes to defining a good PR description SHAP dependence plots for the top three features. 1) Average Commit Message Length shows positive SHAP values (positive impact) when the length exceeds approximately 13 words. 2) PR Title Length shows a positive impact starting at around 7 words. 3) PR Body Length shows a positive contribution when the word count is above 80 words.

3. Implications

Our findings offer the following implications:

Project maintainers. Assign AI agents narrowly scoped tasks to avoid unnecessary rework and prevent the merge-rate drop seen with larger changes. Carefully review newly introduced symbols, which are prone to high churn, and use length-based heuristics to flag brief or low-quality PR descriptions for extra review.

AI Agent builders. Move beyond simply aggregating commit messages and train agents to reason over the full changeset, enabling the generation of more coherent and holistic PR descriptions that better capture the intent, scope, and rationale of changes.

Researchers. Investigate methods to better evaluate PR quality and agent behavior, including developing metrics that capture semantic alignment, reviewing agent-specific differences, and exploring cross-language generalization of code change patterns.

4. Threats to validity

Construct Validity. We use semantic similarity and LLM-based scores as proxies for PR-description quality, which may not fully capture factual correctness and may reflect LLM self-preference bias. We mitigate this by combining multiple alignment metrics and manually verifying a small sample. We also use CodeT5-generated commit messages as a proxy for patch semantics; while not ideal, this remains a reasonable approximation given the benchmark group’s high similarity scores and the use of an LLM-as-a-judge metric. The “good” description threshold ( ≥ 0.9 \geq 0.9 ) is heuristic, but feature importance remained consistent across sensitivity tests. The model’s 31.9% recall shows it misses most good descriptions, indicating that, despite its feature-attribution intent, the identified predictors do not fully capture what makes a description good.

Internal Validity. Our symbol-churn analysis (RQ1.2) uses regular expressions (regex) to extract function and class definitions for TypeScript, Python, and Go. We rely on regex rather than AST-based methods like Tree-sitter (Developers, 2018 ) because patches contain limited code context (Xiong et al. , 2025 ) , though the code is expected to be syntactically valid (Gong et al. , 2024 ) . To enhance reliability, we focus on the three languages with clearly recognizable tokens ( def , function , func , class ). Regex may miss symbols or capture false positives, e.g., commented or nested code, so we restrict the analysis to languages where extraction is most reliable. Manual inspection of a small sample further supports this choice, showing minimal false positives.

External Validity. Agent capabilities evolve rapidly, so our results represent a snapshot of current model performance and may change as agents improve reasoning and long-context understanding. Additionally, our churn analysis focuses on dynamic languages and may not generalize to statically typed ecosystems, e.g., Java and C++, where type constraints, annotations, generics, and other language-specific constructs complicate symbol extraction from partial diffs, preventing reliable regex-based parsing.

5. Related works

The closest prior work is Watanabe et al. (Watanabe et al. , 2025 ) , who compared HPRs and APRs of one agent (Claude Code). We study five agents and add measures such as symbol churn and time to next modification. Unlike Watanabe et al., who report APRs introduce more code, we find no significant difference in lines changed. Both studies find feature development ( feat ) and bug fixes ( fix ) dominate, with documentation and tests more frequent in APRs.
Zi et al. (Zi et al. , 2025 ) introduced the AgentPack dataset, showing that co-authored changes are narrowly scoped and that LLM-generated commit messages capture intent well. However, they do not assess merge success or symbol stability and use only message length as a quality metric; our work fills these gaps with multiple quality metrics.

Prior PR-description research has focused on generating descriptions (Sakib et al. , 2024 ; Tire et al. , 2025 ) or commit messages (Eliseeva et al. , 2023 ) , not alignment with code changes. We introduce metrics quantifying consistency between descriptions and code modifications for humans and agents, and model predictors of high-quality descriptions. Related work on commit message faithfulness (Liu et al. , 2025 ) shows high hallucination in code-review generation ( 50%) but lower in commit messages ( 20%), proposing detection metrics. Unlike these studies, we systematically measure alignment at both commit and PR levels, revealing agents are precise locally but struggle with PR-level summarization.

6. Conclusion

In this paper, we compare agentic pull requests (APRs) and human pull requests (HPRs) to understand differences in code changes and PR-level communication. Analyzing 33,596 APRs and 6,618 HPRs, we find that agent-introduced symbols are removed sooner (median 3 vs. 34 days) and churn more (7.33% vs. 4.10%), indicating a focus on narrow tasks. Agents produce stronger commit-level messages (semantic similarity 0.72 vs. 0.68) but lag in PR-level summarization (PR–commit similarity 0.86 vs. 0.88), highlighting limited full-PR reasoning. These insights guide task assignment, review practices, and agent training for more reliable agent-assisted development.

Future work. Several opportunities remain for future work, including expanding symbol-churn analysis to additional languages using parser-based techniques, refining the labels and features used to characterize high-quality PR descriptions, and examining agent-specific behaviors to uncover differences beyond aggregate trends.

Acknowledgment

This work is funded by the Natural Sciences and Engineering Research Council of Canada (NSERC): RGPIN-2025-05897.

References

- A. Agresti and M. Kateri (2011) Categorical data analysis . In International encyclopedia of statistical science , pp. 206–208 . Cited by: §2.3 .

- A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek, F. Guzmán, E. Grave, M. Ott, L. Zettlemoyer, and V. Stoyanov (2020) Unsupervised cross-lingual representation learning at scale . In Proceedings of the 58th annual meeting of the association for computational linguistics , pp. 8440–8451 . Cited by: §2.4 .

- D. Cotroneo, C. Improta, and P. Liguori (2025) Human-written vs. AI-generated code: a large-scale study of defects, vulnerabilities, and complexity . In 2025 IEEE 36th International Symposium on Software Reliability Engineering (ISSRE) , pp. 252–263 . Cited by: §1 .

- T. Developers (2018) Tree-sitter: an incremental parsing system for programming tools . Note: https://github.com/tree-sitter/tree-sitter Accessed: 2025-12-14 Cited by: §4 .

- O. J. Dunn (1964) Multiple comparisons using rank sums . Technometrics 6 ( 3 ), pp. 241–252 . Cited by: §2.4 .

- A. Eliseeva, Y. Sokolov, E. Bogomolov, Y. Golubev, D. Dig, and T. Bryksin (2023) From commit message generation to history-aware commit message completion . In 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE) , pp. 723–735 . Cited by: §2.4 , §5 .

- L. Gong, M. Elhoushi, and A. Cheung (2024) AST-T5: structure-aware pretraining for code generation and understanding . In Proceedings of the 41st International Conference on Machine Learning , Cited by: §4 .

- H. Huang, Y. Qu, X. Bu, H. Zhou, J. Liu, M. Yang, B. Xu, and T. Zhao (2025) An empirical study of LLM-as-a-Judge for LLM evaluation: fine-tuned judge model is not a general substitute for GPT-4 . In Findings of the Association for Computational Linguistics , pp. 5880–5895 . Cited by: §2.4 .

- M. K. Hutchinson and M. C. Holtman (2005) Analysis of count data using poisson regression . Research in nursing & health 28 ( 5 ), pp. 408–418 . Cited by: §2.3 .

- W. H. Kruskal and W. A. Wallis (1952) Use of ranks in one-criterion variance analysis . Journal of the American statistical Association 47 ( 260 ), pp. 583–621 . Cited by: §2.4 .

- H. Li, H. Zhang, and A. E. Hassan (2025) The rise of AI teammates in software engineering (se) 3.0: how autonomous coding agents are reshaping software engineering . arXiv preprint arXiv:2507.15003 . Cited by: §2.1 , §2.2 , §2.3 .

- C. Liu, H. Y. Lin, and P. Thongtanunam (2025) Hallucinations in code change to natural language generation: prevalence and evaluation of detection metrics . In Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics , pp. 2538–2560 . Cited by: §5 .

- H. B. Mann and D. R. Whitney (1947) On a test of whether one of two random variables is stochastically larger than the other . The annals of mathematical statistics , pp. 50–60 . Cited by: §2.3 .

- [14] M. Mo, Y. Luo, J. Gao, and X. Tang AutoPR: automatically pull request generation for fix issued bugs of codebase . Cited by: §1 .

- M. G. Mohammadkhani and H. Beigy (2025) Checklist engineering empowers multilingual LLM judges . In Proceedings of the Workshop on Beyond English: Natural Language Processing for all Languages in an Era of Large Language Models , pp. 190–196 . Cited by: §2.4 .

- D. Ortiz Martes, E. Gunderson, C. Neuman, and N. N. Kachouie (2025) Transformer models for paraphrase detection: a comprehensive semantic similarity study . Computers 14 ( 9 ), pp. 385 . Cited by: §2.4 .

- L. Papluca (2022) Xlm-roberta-base-language-detection . Note: Fine-tuned version of XLM-RoBERTa for language identification (Accessed: 2025-11-22) External Links: Link Cited by: §2.4 .

- D. Pham and T. A. Ghaleb (2026) Code change characteristics and description alignment: a comparative study of agentic versus human pull requests (replication package) . Note: https://github.com/Taher-Ghaleb/AIAgentsAlignment-MSR2026 Cited by: §1 , §2.4 .

- M. N. Sakib, M. A. Islam, and M. M. Arifin (2024) Automatic pull request description generation using LLMs: a T5 model approach . In 2024 2nd International Conference on Artificial Intelligence, Blockchain, and Internet of Things (AIBThings) , pp. 1–5 . Cited by: §1 , §5 .

- M. Schall, T. Czinczoll, and G. De Melo (2024) CommitBench: a benchmark for commit message generation . In 2024 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER) , pp. 728–739 . Cited by: §2.1 , §2.4 .

- E. Shi, Y. Wang, W. Tao, L. Du, H. Zhang, S. Han, D. Zhang, and H. Sun (2022) RACE: retrieval-augmented commit message generation . In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing , pp. 5520–5530 . Cited by: §2.4 .

- A. V. Solatorio (2024) GISTEmbed: guided in-sample selection of training negatives for text embedding fine-tuning . arXiv preprint arXiv:2402.16829 . External Links: Link Cited by: §2.4 .

- S. Sutriawan, W. Sasoko, and Z. Alamin (2025) Ritzkal,“benchmarking text embedding models for multi-dataset semantic textual similarity: a machine learning-based evaluation framework,” . Acadlore Trans. Mach. Learn 4 ( 2 ), pp. 82–96 . Cited by: §2.4 .

- Y. Tian, Y. Zhang, K. Stol, L. Jiang, and H. Liu (2022) What makes a good commit message? . In Proceedings of the 44th International Conference on Software Engineering , pp. 2389–2401 . Cited by: §2.4 .

- K. Tire, B. Çakar, and E. Tüzün (2025) Evaluating the impact of data cleaning on the quality of generated pull request descriptions . arXiv preprint arXiv:2505.01120 . Cited by: §2.1 , §2.4 , §5 .

- H. Wang, J. Gong, H. Zhang, J. Xu, and Z. Wang (2025) AI agentic programming: a survey of techniques, challenges, and opportunities . arXiv preprint arXiv:2508.11126 . Cited by: §1 .

- M. Watanabe, H. Li, Y. Kashiwa, B. Reid, H. Iida, and A. E. Hassan (2025) On the use of agentic coding: an empirical study of pull requests on GitHub . arXiv preprint arXiv:2509.14745 . Cited by: §1 , §5 .

- H. Wei, S. He, T. Xia, F. Liu, A. Wong, J. Lin, and M. Han (2024) Systematic evaluation of LLM-as-a-Judge in LLM alignment tasks: explainable metrics and diverse prompt templates . arXiv preprint arXiv:2408.13006 . Cited by: §2.4 .

- Y. Wu, Y. Wang, Y. Li, W. Tao, S. Yu, H. Yang, W. Jiang, and J. Li (2025) An empirical study on commit message generation using LLMs via in-context learning . In Proceedings of the IEEE/ACM 47th International Conference on Software Engineering , pp. 553–565 . Cited by: §1 , §2.4 .

- B. Xiong, L. Zhang, C. Wang, and P. Liang (2025) Contextual code retrieval for commit message generation: a preliminary study . arXiv preprint arXiv:2507.17690 . Cited by: §4 .

- L. Zhang, H. Zhang, C. Wang, and P. Liang (2024) RAG-enhanced commit message generation . arXiv preprint arXiv:2406.05514 . Cited by: §2.4 .

- Y. Zi, Z. Wu, A. Boruch-Gruszecki, J. Bell, and A. Guha (2025) AgentPack: a dataset of code changes, co-authored by agents and humans . arXiv preprint arXiv:2509.21891 . Cited by: §5 .
