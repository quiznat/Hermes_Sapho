---
version: source-capture.v1
article_id: art-2026-03-06-015
ticket_id: ticket-import-art-2026-03-06-015
source_url: https://arxiv.org/html/2601.15195v1
canonical_url: https://arxiv.org/abs/2601.15195
source_title: arXiv 2601.15195
capture_kind: runtime-import
http_status: 200
content_type: text/markdown
captured_at_utc: '2026-03-07T19:27:22Z'
---
# Source Capture

## Title

arXiv 2601.15195

## Body

# arXiv 2601.15195

Source: https://arxiv.org/html/2601.15195v1

Generated: 2026-03-01 17:54 UTC

> Note: Generated from arXiv HTML full text as an LLM-friendly fallback where native PDF extraction tools are unavailable on this VM.

Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub 

- 1 Introduction 

- 2 Methodology 

- 3 Results 

- 4 Conclusion 

Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub 

Ramtin Ehsani 0000-0003-1517-7135 Drexel University Philadelphia PA USA ramtin.ehsani@drexel.edu , Sakshi Pathak Drexel University Philadelphia PA USA sp3856@drexel.edu , Shriya Rawal Drexel University Philadelphia PA USA sr3728@drexel.edu , Abdullah Al Mujahid Missouri University of Science and Technology Rolla MO USA amgzc@mst.edu , Mia Mohammad Imran Missouri University of Science and Technology Rolla MO USA imranm@mst.edu and Preetha Chatterjee Drexel University Philadelphia PA USA preetha.chatterjee@drexel.edu 

(2018) 

Abstract. 

AI coding agents are now submitting pull requests (PRs) to software projects, acting not just as assistants but as autonomous contributors. As these agentic contributions are rapidly increasing across real repositories, little is known about how they behave in practice and why many of them fail to be merged.
In this paper, we conduct a large-scale study of 33k agent-authored PRs made by five coding agents across GitHub. (RQ1) We first quantitatively characterize merged and not-merged PRs along four broad dimensions: 1) merge
outcomes across task types, 2) code changes, 3) CI build results, and 4) review dynamics. We observe that tasks related to documentation , CI , and build update achieve the highest merge success, whereas performance and bug-fix tasks perform the worst. Not-merged PRs tend to involve larger code changes, touch more files, and often do not pass the project’s CI/CD pipeline validation. (RQ2) To further investigate why some agentic PRs are not merged, we qualitatively analyze 600 PRs to derive a hierarchical taxonomy of rejection patterns.
This analysis complements the quantitative findings in RQ1 by uncovering rejection reasons not captured by quantitative metrics, including lack of meaningful reviewer engagement , duplicate PRs , unwanted feature implementations , and a gent misalignment . Together, our findings highlight key socio-technical and human-AI collaboration factors that are critical to improving the success of future agentic workflows. 

Agents, Large language models, Agentic pull request, AIDev 
† † copyright: acmlicensed † † journalyear: 2018 † † doi: XXXXXXX.XXXXXXX † † conference: MSR ’26: Proceedings of the 23rd International Conference on Mining Software Repositories; April 2026; Rio de Janeiro, Brazil † † isbn: 978-1-4503-XXXX-X/2018/06 † † ccs: Software and its engineering Software creation and management † † ccs: Computing methodologies Intelligent agents 

1. Introduction 

AI coding agents such as GitHub Copilot and OpenAI Codex are rapidly becoming active contributors to open-source repositories, often assisting with or directly authoring new pull requests (PRs). Beyond offering inline code suggestions, these tools now generate code changes, respond to reviewer feedback, and participate in the software lifecycle as autonomous agents (Li et al. , 2025 ; Chen, 2021 ; Barke et al. , 2023 ; Yang et al. , 2024b ; Ehsani et al. , 2025b ) .
As agent-authored PRs are becoming more prevalent, it is critical to understand how they are evaluated and accepted in practice. 

Prior work shows that PR acceptance depends on factors such as technical correctness, problem scope, and contributor reputation (Lenarduzzi et al. , 2021 ; Soares et al. , 2015 ; Zhang et al. , 2023 ) .
PRs are more likely to be merged when they pass tests and CI pipelines, address high-priority or well-scoped problems, and introduce localized and incremental code changes rather than broad or invasive modifications (van der Veen et al. , 2015 ; Zampetti et al. , 2019 ; Zhao et al. , 2017 ) . While these factors characterize the success of human-authored PRs, their relevance and applicability to agent-authored PRs are not yet well understood. 

Coding agents have been extensively benchmarked across a range of tasks, from code generation (Chen and et al., 2021 ; Sajadi et al. , 2025 ) , testing (Kang et al. , 2024 ; Yang et al. , 2024a ; Pangas et al. , 2025 ) , to automated program repair (Jimenez et al. , 2024 ; Ehsani et al. , 2025a ; Nashid et al. , 2025 ) . Other studies have analyzed agent-driven code refactoring, reporting that these refactorings tend to be small, localized improvements that produce modest but statistically significant gains in code quality (Horikawa et al. , 2025 ; Shinn et al. , 2023 ) . More recent work has focused on agent reasoning and execution behaviors, including
traceability, decision-making, and workflow strategies in complex software engineering tasks (Ceka et al. , 2025 ; Majgaonkar et al. , 2025 ) .
While prior work evaluates agents in isolated tasks, we lack a systematic assessment of how agents perform when integrated into real development workflows involving CI validation, code review, and iterative revision. 

In this paper, we conduct a large-scale empirical study on agent-authored pull requests using the AIDev-pop dataset (Li et al. , 2025 ) , which comprises over 33k PRs submitted by five major coding agents across GitHub projects with more than 100 stars.
We characterize the types of contributions agents attempt, their acceptance rates, reviewer interactions, and, most importantly, where and why their contributions fail.
Specifically, we investigate two RQs: 

RQ1: How do merged and not-merged agent-authored PRs differ in task types, code changes, CI outcomes, and review interactions? We find that agentic PRs involving documentation , CI , and build update tasks are merged at higher rates, while performance and bug-fix contributions show the lowest acceptance. Not-merged PRs tend to involve larger code changes, touch more files, receive more reviewer revisions, and frequently fail project CI checks. 

RQ2: What patterns lead to agent-authored PRs not being merged in real-world software repositories? The most frequent rejection pattern is reviewer abandonment, where agent-authored PRs receive little or no human engagement before being closed. Among PRs that do undergo active review, duplicate PRs, build failures, and unwanted features account for the majority of rejections. 

Overall, our results suggest that agentic PR failures stem from misalignment with repository workflows (e.g., CI/CD failures), developer expectations (e.g., unwanted or incorrect features), and a lack of project coordination (e.g., reviewer abandonment). 

2. Methodology 

RQ1: How do merged and not-merged agent-authored PRs differ in task types, code changes, CI outcomes, and review interactions? 

We perform a quantitative characterization of agent-authored pull requests along four dimensions: 1) merge outcomes across task types, 2) code changes, 3) CI build results, and 4) review dynamics.
These characteristics are grounded in prior work on factors that influence pull request acceptance (Zhang et al. , 2023 ; Zampetti et al. , 2019 ; Lenarduzzi et al. , 2021 ) . 

We examine merge outcomes across task types , using the task labels provided in the dataset. These tasks consist of 11 categories: feature, fix, performance, refactoring, style, documentation, test, chore, build, CI, and other (ConventionalCommits, 2025 ; Li et al. , 2025 ) . This allows us to assess whether certain categories of agent-generated contributions are more or less likely to be merged.
We analyze the magnitude of proposed code changes by measuring a) the total number of added and removed lines of code ( #LOC Changes ), and b) the number of files modified by each PR ( #File Changes ). These two characteristics serve as quantitative indicators of the PR’s complexity and potential review burden (Zampetti et al. , 2019 ; Lenarduzzi et al. , 2021 ; Zhang et al. , 2023 ) .
We inspect CI build results for each PR by querying the GitHub API for the status of the last commit in the PR. For every PR, we extract the number of failed check-runs ( #Failed CI Checks ) and record the overall commit status reported by GitHub (success or failure). This provides a proxy for whether the agent-generated changes break tests, violate linting rules, or fail other repository-specific validation pipelines. This metric allows us to capture automated quality signals that may influence maintainers’ decisions (Zampetti et al. , 2019 ; Maipradit et al. , 2023 ) .
We examine review interactions associated with each PR (Zampetti et al. , 2019 ) . Specifically, we compute a) the number of review comments in a PR ( #Review Comments ), and b) the number of review revisions each PR receives ( #Review Revisions ). Review revisions are the total number of additions and deletions by the developers during review cycles of the PRs. These measures reflect how much developer attention and iteration an agent-generated PR demands. 

Because of the dataset size (¿ 33k), standard statistical significance testing by itself is not informative because all comparisons might yield statistically significant values even when the differences are negligible (Sullivan and Feinn, 2012 ) . Instead, following best practices in large-scale empirical studies (Hofmann, 2015 ; Kitchenham et al. , 2017 ) , we rely on effect size measures, using Cliff’s delta ( δ \delta ) to quantify the magnitude of difference between merged and not-merged PR distributions. To complement effect-size analysis, we use kernel density estimates (Hofmann, 2015 ; Kitchenham et al. , 2017 ) to visualize distribution shapes. Unlike simple summaries, kernel density plots give a smooth, continuous view of the data’s distribution, making it easier to see shifts and spread in the data (Kitchenham et al. , 2017 ; Thrun et al. , 2020 ) . In addition, we use logistic regression modeling (Kitchenham et al. , 2017 ) to see how effective these characteristics are in predicting the outcome of agent-authored PRs. Together, these analyses allow us to assess whether meaningful differences exist between merged and not-merged agentic PRs. 

RQ2: What patterns lead to agent-authored PRs not being merged in real-world software repositories? 

We randomly select a subset of 600 rejected PRs for qualitative analysis, stratified across the five coding agents to ensure balanced coverage, and sufficient statistical power to estimate rejection prevalence with 95% confidence and a ±5% margin of error (Cochran, 1977 ) . 

We start with a sample of 100 rejected PRs.
Following open coding (Azungah, 2018 ) , two authors independently label each PR with its primary reason for rejection. During the first round of coding (50 PRs), the annotators identified recurring patterns such as build failures, licensing or contribution policy violations, redundant or unwanted changes, and logical or semantic errors in the proposed code. These patterns were iteratively discussed to derive an initial hierarchical taxonomy spanning three levels: Code , Pull Request , and Reviewer level.
We assess inter-rater reliability using Cohen’s kappa (McHugh, 2012 ) . After the first round, the agreement was 0.55, indicating moderate alignment. All disagreements were then discussed and resolved through group discussions, during which the taxonomy was refined, and an additional Agentic level was introduced.
The refined taxonomy was applied to a second set of 50 PRs, resulting in a final Cohen’s kappa of 0.91 across all 100 PRs, reflecting strong agreement (McHugh, 2012 ) . Using this taxonomy, the annotators independently labeled 250 more PRs each (500 in total), bringing the size of the manually annotated dataset to 600 PRs. The detailed annotation instructions and codebook are available in the replication package. 

Our iterative manual coding resulted in a hierarchical taxonomy of agentic-PR rejection patterns , consisting of four high-level categories as described in Table 2 .
1) Reviewer level reflects PRs that close without meaningful developer engagement, often due to inactivity or abandonment.
2) Pull Request level capture cases where the PR is unsuitable for project integration, such as unwanted features, duplicate submissions, or changes submitted to the wrong branch.
3) Code level failures happen when the proposed implementation is incomplete, incorrect, or breaks CI/test pipelines.
4) Agentic failures capture behaviors such as licensing violations with the project or misalignment with reviewer instructions. 

3. Results 

RQ1: How do merged and not-merged agent-authored PRs differ in task types, code changes, CI outcomes, and review interactions? 

Of the 33,596 agentic pull requests, the majority originate from OpenAI Codex (21,799), exceeding the output of any other agent by more than a factor of four. Copilot and Devin follow with 4,970 and 4,827 PRs, while Cursor contributes 1,541, and Claude Code represents the smallest share with 459 PRs.
Across all agents, 71.48% of PRs (24,014) are successfully merged. Despite handling the largest volume of contributions, OpenAI Codex achieves the highest merge rate, with 82.59% (18,004) of its PRs being accepted. Cursor follows with a 65.22% merge rate (1,005), then Claude Code at 59.04% (271), and Devin at 53.76% (2,595). Copilot exhibits the lowest merge rate, with only 43.04% (2,139) of its PRs being merged. 

Figure 1 . Merge-rate per Task Type Across Agentic PRs. 

Figure 1 shows the merge rates for each agent across all task categories , along with the number of PRs in each cell. The distribution of success varies across task types and agents. Codex shows the highest merge rates overall, exceeding 80% in categories including documentations (0.92), CI (0.86), build (0.87), chore (0.84), test (0.84), fix (0.82), feature (0.81), and refactoring (0.80). Its lowest category is performance (0.68).
Cursor also performs strongly on maintenance-oriented tasks, with high merge rates in CI (0.94), documentations (0.74), chore (0.74), and style (0.72). Its lowest rates occur in build (0.57) and performance (0.46). Claude Code’s highest merge rates appear in build (0.88), documentations (0.75), and CI (0.57), with lower rates for test (0.50) and refactoring (0.50). Devin shows moderate values across most categories, with higher merge rates in documentations (0.71), style (0.68), and CI (0.61), and lower rates in performance (0.35) and fix (0.43). Copilot displays the lowest merge rates among the agents, with its highest values in CI (0.63) and documentations (0.61), and its lowest in feature (0.38), test (0.37), and performance (0.27).
Across agents, tasks with consistently higher merge rates include documentations (84%), CI (79%), and build (74%).
In contrast, performance (55%) and fix (64%) display the lowest merge rates overall.
These results indicate that tasks involving documentation, CI, and build changes tend to merge more easily in repositories, whereas categories requiring more complex or subjective changes show lower merge rates. 

(a) Changed Files (log10) 

(b) Changed LOC (log10) 

(c) CI Fails 

Figure 2 . Differences in Merged vs. Not-merged PRs. 

Figures 2(a) and 2(b) show the differences in code changes between merged and not-merged PRs, in terms of #LOC Changes and #File Changes . Not merged PRs tend to introduce larger modifications in the number of files and LOC than merged ones. Based on Cliff’s δ \delta (Table 1 ), the difference in total lines of code changes is 17%, and the difference in the number of changed files is 10%, both indicating a small-to-medium effect size that not-merged PRs skew toward larger changes. Figures 2(a) and 2(b) also show kernel density estimates of these two metrics. Because changes span several orders of magnitude, the distributions for these plots are shown on a log10 scale, where each unit corresponds to a ten-fold increase in size. Higher density toward the right side of the plots reflects larger PRs. In both subfigures, the distribution for not-merged PRs is shifted slightly rightward relative to merged PRs, visualizing the same trend captured by Cliff’s δ \delta . 

Figure 2(c) reports the distribution of CI failures for merged and not-merged agentic PRs. Not-merged PRs show a noticeably heavier tail, with many PRs accumulating multiple failing check runs. In contrast, merged PRs cluster sharply near zero, indicating that most merged contributions pass their checks with little or no failure. Cliff’s δ \delta of 24% indicates a moderate effect size, showing that not-merged PRs tend to experience more CI failures. 

Table 1 . Logistic Regression and Effect Size (* p p ¡0.05) 

Characteristic Coef p p -value Odds Ratio δ \delta 

#LOC Changes -2.8e-06 ∼ \sim 1% ∗ 99% -0.17 

#File Changes -0.0011 ∼ \sim 1% ∗ 99% -0.10 

#Failed CI Checks -0.1579 ∼ \sim 1% ∗ 85% -0.24 

#Review Comments -0.0028 ∼ \sim 48% 99% -0.05 

#Review Revisions -1.6e-05 ∼ \sim 67% 99% -0.03 

Figure 3 shows the differences in review interactions . Not-merged PRs tend to receive more reviewer revisions than merged ones. Based on Cliff’s δ \delta (Table 1 ), developers make approximately 5% more review comments and 3% more revisions on not-merged PRs compared to merged PRs, although the effect sizes for both are small. The density distributions follow a similar overall pattern. However, the curves widen for not-merged PRs as the number of comments (Figure 3(a) ) or revisions (Figure 3(b) ) increases, indicating that not-merged PRs often undergo extensive reviewer discussion and iterative refinement until a final decision is made to leave them open or mark them as rejected. 

(a) Comments in PRs (log10) 

(b) Revisions in PRs (log10) 

Figure 3 . Reviews of Merged vs. Not-merged PRs. 

The logistic regression results in Table 1 show that all model coefficients are negative, indicating that increases in these metrics are associated with lower odds of a PR being merged. Based on the p p -values, all variables except # review comments and # review revisions are significant (threshold at 0.05 0.05 ). Odds ratios quantify the practical effect of each metric. For example, a one-unit increase in # LOC changes decreases the odds of a merge by approximately 1%, which can accumulate meaningfully given that code modifications span several orders of magnitude in size. Similar patterns hold for # file changes , # review comments , and # revision cycles , although with smaller magnitudes. Notably, each additional failed CI check decreases the odds of a merge by about 15%. 

Across all agentic PRs, documentation , CI , and build tasks exhibit the highest success, while performance and fix see the lowest. Not-merged PRs tend to introduce larger code changes, touch more files, fail more CI checks, and receive slightly more review comments and revisions. 

RQ2: What patterns lead to agent-authored PRs not being merged in real-world software repositories? 

Table 2 summarizes the distribution of rejection patterns for the 600 manually annotated rejected agentic pull requests. We note that 38 PRs were no longer accessible at the time of analysis due to deletion or archival, leaving a total of 562 PRs for categorization. 

Reviewer -level abandonment is the most frequent rejection pattern, accounting for 228 PRs (38%). These PRs were left without any meaningful human reviewer interaction, often after prolonged inactivity or automated closure, indicating that a substantial fraction of agentic PRs fail before entering active review. 

Pull request -level reasons form the second-largest group, comprising 188 PRs (31%). Within this level, duplicate PRs are the most common pattern, affecting 142 PRs (23%), where maintainers explicitly reference an existing PR that already implements the same change. For example, one PR was closed with the comment: “Superseded by PR #715 which consolidates all GFQL code changes into a single PR” (GitHub, 2025i ) . Unwanted features account for 24 PRs (4%), where maintainers state that the contribution is misaligned with project goals or introduces excessive or unnecessary changes. Examples include: “Too old already superseded by more recent pushes ” (GitHub, 2025j ) and “This is a LOT to review, would really prefer smaller granular PRs” (GitHub, 2025h ) .
Less frequent patterns include non-functional PRs (13; 2%), which often consist of only setup or configuration tests. For example, PRs explicitly titled “testing DO NOT MERGE” (GitHub, 2025b ) . Wrong task descriptions account for 7 PRs (1%), where the PR description provides little to no meaningful context. Maintainers often respond with comments such as “Sorry, I don’t know what this is, but it doesn’t look like it belongs in our repo” (GitHub, 2025c ) . Finally, wrong branch submissions (2; ¡1%) occur when PRs are opened on incorrect branches, prompting maintainers to make comments such as “PR is opened against main. You probably want to open it against develop” (GitHub, 2025d ) . 

Code -level reasons represent the third most frequent category, affecting 133 PRs (22%). The dominant pattern in this category is CI/test failure, observed in 99 PRs (17%), where automated builds or tests fail due to the submitted changes. At times, reviewers even explicitly point out these failures, for example: “@copilot fix the merge conflicts; if you cannot fix these then close the PR” (GitHub, 2025g ) .
Incorrect implementations (19; 3%) and incomplete implementations (15; 2%) comprise the remaining code-level failures. Reviewers often highlight technical inaccuracies or missing logic with comments such as: “The changes made to the billing.test.ts file are entirely wrong” (GitHub, 2025f ) . 

Agentic -level issues are the least frequent category, comprising 13 PRs (2%). Misalignment is the dominant pattern at this level, appearing in 9 PRs (1%). In these cases, agents repeatedly fail to follow explicit reviewer instructions or misunderstand requested changes, even after multiple rounds of feedback. Reviewer comments often express frustration with comments such as “Devin stop being a dumb*ss, if you claim you ”deleted 200 lines” then continue to” (GitHub, 2025e ) . Licensing issues account for the remaining 4 PRs (¡1%). These PRs are rejected because agents do not comply with project-specific legal requirements, such as signing a Contributor License Agreement (CLA) or addressing ownership concerns. Maintainers explicitly reference these requirements with comments, e.g., “we ask that you sign our Contributor License Agreement before we can accept your contribution” (GitHub, 2025a ) . Together, these examples highlight legal and governance constraints that current agents cannot satisfy. 

A majority of agentic PRs are not merged due to reviewer abandonment. Among reviewed PRs, the dominant rejection patterns include duplicate PRs, CI/test failures, and large or unwanted feature implementations. 
Table 2 . Taxonomy of Rejection Patterns in Agentic PRs. 

Level Pattern Definition Freq. 

Reviewer Abandoned/Not Reviewed PR closed with no meaningful human interaction; only bots (if any) performed actions. 228 

Pull Request Duplicate PR Work already exists in another PR; maintainers explicitly reference the duplicate. 142 

Unwanted Feature Maintainers state that the feature is unnecessary, misaligned, or not intended. 24 

Non-Functional PR PR contains only setup, configuration, or scaffolding changes without functional contribution. 13 

Wrong Task Description PR description reflects misunderstanding of the task or intended change. 7 

Wrong Branch PR targets the incorrect branch and must be resubmitted to the proper one. 2 

Code CI/Test Failure PR fails automated build or deployment checks caused by its own changes. 99 

Incorrect Implementation Implementation is technically incorrect or solves the wrong problem despite a correct task description. 19 

Incomplete Implementation Contribution lacks required logic or completeness; reviewers flag missing or insufficient work. 15 

Agentic Misalignment Agent fails to follow reviewer instructions or misunderstands explicit requested edits. 9 

License Issues Reviewers flag license or ownership concerns related to agent-generated content. 4 

4. Conclusion 

Our findings indicate that not-merged PRs tend to introduce larger and more invasive code changes, attempt broader feature additions, and exhibit higher rates of CI/test failures. Rejections of agentic PRs stem from multiple reasons, such as reviewer abandonment, duplicate PRs, or implementations of unwanted features. Overall, these results highlight difficulties of agents in task selection, coordination, and alignment with repository context. Maintainer feedback frequently emphasizes that PRs should be small, focused, and limited to a single coherent change, and discourages agentic submissions that combine substantive modifications with unrelated edits. The replication package for our study is publicly available (ReplicationPackage, 2025 ) . 

Improving the success of future agentic-AI workflows would require improving agents’ ability to identify existing or ongoing work, adhere to project contribution norms, decompose tasks into localized changes, and validate submissions against CI pipelines before opening new PRs.
Failures of agentic PRs can also be socio-technical rather than purely technical. By characterizing the failure patterns of not-merged agentics PRs, our study provides empirical grounding for the design of more context-aware and collaboration-sensitive AI coding agents, and informs future research on integrating such agents into real-world software development workflows. 

References 

- T. Azungah (2018) Qualitative research: deductive and inductive approaches to data analysis . Qualitative Research Journal 18 ( 4 ), pp. 383–400 . External Links: ISSN 1443-9883 , Link , Document Cited by: §2 . 

- S. Barke, M. B. James, and N. Polikarpova (2023) Grounded copilot: how programmers interact with code-generating models . Proceedings of the ACM on Programming Languages 7 ( OOPSLA1 ), pp. 85–111 . Cited by: §1 . 

- I. Ceka, S. Pujar, S. Ramji, L. Buratti, G. Kaiser, and B. Ray (2025) Understanding software engineering agents through the lens of traceability: an empirical study . External Links: 2506.08311 , Link Cited by: §1 . 

- M. Chen and J. T. et al. (2021) Evaluating large language models trained on code . External Links: 2107.03374 Cited by: §1 . 

- M. Chen (2021) Evaluating large language models trained on code . arXiv preprint arXiv:2107.03374 . Cited by: §1 . 

- W. G. Cochran (1977) Sampling techniques . 3rd edition , John Wiley & Sons , New York, NY . External Links: ISBN 978-0471162407 Cited by: §2 . 

- ConventionalCommits (2025) ( en ). External Links: Link Cited by: §2 . 

- R. Ehsani, E. Parra, S. Haiduc, and P. Chatterjee (2025a) Hierarchical knowledge injection for improving llm-based program repair . In 40th IEEE/ACM International Conference on Automated Software Engineering (ASE) , Vol. . External Links: Link Cited by: §1 . 

- R. Ehsani, S. Pathak, E. Parra, S. Haiduc, and P. Chatterjee (2025b) What characteristics make chatgpt effective for software issue resolution? an empirical study of task, project, and conversational signals in github issues . Empirical Software Engineering 31 ( 1 ). External Links: ISSN 1573-7616 , Link , Document Cited by: §1 . 

- GitHub (2025a) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025b) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025c) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025d) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025e) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025f) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025g) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025h) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025i) ( en ). External Links: Link Cited by: §3 . 

- GitHub (2025j) ( en ). External Links: Link Cited by: §3 . 

- M. A. Hofmann (2015) Searching for effects in big data: why p-values are not advised and what to use instead . In 2015 Winter Simulation Conference (WSC) , Vol. , pp. 725–736 . External Links: Document Cited by: §2 . 

- K. Horikawa, H. Li, Y. Kashiwa, B. Adams, H. Iida, and A. E. Hassan (2025) Agentic refactoring: an empirical study of ai coding agents . External Links: 2511.04824 , Link Cited by: §1 . 

- C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2024) SWE-bench: can language models resolve real-world github issues? . External Links: 2310.06770 , Link Cited by: §1 . 

- S. Kang, G. An, and S. Yoo (2024) A quantitative and qualitative evaluation of llm-based explainable fault localization . Proc. ACM Softw. Eng. 1 ( FSE ). External Links: Link , Document Cited by: §1 . 

- B. Kitchenham, L. Madeyski, D. Budgen, J. Keung, P. Brereton, S. Charters, S. Gibbs, and A. Pohthong (2017) Robust Statistical Methods for Empirical Software Engineering . Empirical Software Engineering 22 ( 2 ), pp. 579–630 ( en ). External Links: ISSN 1573-7616 , Link , Document Cited by: §2 . 

- V. Lenarduzzi, V. Nikkola, N. Saarimäki, and D. Taibi (2021) Does code quality affect pull request acceptance? An empirical study . Journal of Systems and Software 171 , pp. 110806 . External Links: ISSN 0164-1212 , Link , Document Cited by: §1 , §2 , §2 . 

- H. Li, H. Zhang, and A. E. Hassan (2025) The rise of ai teammates in software engineering (se) 3.0: how autonomous coding agents are reshaping software engineering . External Links: 2507.15003 , Link Cited by: §1 , §1 , §2 . 

- R. Maipradit, D. Wang, P. Thongtanunam, R. G. Kula, Y. Kamei, and S. McIntosh (2023) Repeated builds during code review: an empirical study of the openstack community . In 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE) , Vol. , pp. 153–165 . External Links: Document Cited by: §2 . 

- O. Majgaonkar, Z. Fei, X. Li, F. Sarro, and H. Ye (2025) Understanding code agent behaviour: an empirical study of success and failure trajectories . External Links: 2511.00197 , Link Cited by: §1 . 

- M. McHugh (2012) Interrater reliability: the kappa statistic . Biochemia medica : časopis Hrvatskoga društva medicinskih biokemičara / HDMB 22 , pp. 276–82 . Cited by: §2 . 

- N. Nashid, D. Ding, K. Gallaba, A. E. Hassan, and A. Mesbah (2025) Characterizing multi-hunk patches: divergence, proximity, and llm repair challenges . External Links: 2506.04418 , Link Cited by: §1 . 

- J. Pangas, S. Mujahid, A. Abdellatif, and M. Castelluccio (2025) Using llms to bridge the gaps in qa test plans at firefox . IEEE Software ( ), pp. 1–7 . External Links: Document Cited by: §1 . 

- ReplicationPackage (2025) ( en ). External Links: Link Cited by: §4 . 

- A. Sajadi, B. Le, A. Nguyen, K. Damevski, and P. Chatterjee (2025) Do llms consider security? an empirical study on responses to programming questions . Empirical Software Engineering 30 ( 3 ), pp. 101 . Cited by: §1 . 

- N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao (2023) Reflexion: language agents with verbal reinforcement learning . Advances in Neural Information Processing Systems 36 , pp. 8634–8652 . Cited by: §1 . 

- D. M. Soares, M. L. D. L. Junior, L. Murta, and A. Plastino (2015) Rejection factors of pull requests filed by core team developers in software projects with high acceptance rates . In 2015 IEEE 14th international conference on machine learning and applications (ICMLA) , pp. 960–965 . Cited by: §1 . 

- G. M. Sullivan and R. Feinn (2012) Using Effect Size—or Why the P Value Is Not Enough . Journal of Graduate Medical Education 4 ( 3 ), pp. 279–282 . External Links: ISSN 1949-8349 , Link , Document Cited by: §2 . 

- M. C. Thrun, T. Gehlert, and A. Ultsch (2020) Analyzing the fine structure of distributions . PLOS ONE 15 ( 10 ), pp. e0238835 . External Links: ISSN 1932-6203 , Link , Document Cited by: §2 . 

- E. van der Veen, G. Gousios, and A. Zaidman (2015) Automatically prioritizing pull requests . In 2015 IEEE/ACM 12th Working Conference on Mining Software Repositories , Vol. , pp. 357–361 . External Links: Document Cited by: §1 . 

- A. Z. H. Yang, C. Le Goues, R. Martins, and V. Hellendoorn (2024a) Large language models for test-free fault localization . In Proceedings of the IEEE/ACM 46th International Conference on Software Engineering , ICSE ’24 , New York, NY, USA . External Links: ISBN 9798400702174 , Link , Document Cited by: §1 . 

- J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024b) Swe-agent: agent-computer interfaces enable automated software engineering . Advances in Neural Information Processing Systems 37 , pp. 50528–50652 . Cited by: §1 . 

- F. Zampetti, G. Bavota, G. Canfora, and M. D. Penta (2019) A study on the interplay between pull request review and continuous integration builds . In 2019 IEEE 26th International Conference on Software Analysis, Evolution and Reengineering (SANER) , Vol. , pp. 38–48 . External Links: Document Cited by: §1 , §2 , §2 . 

- X. Zhang, Y. Yu, G. Gousios, and A. Rastogi (2023) Pull request decisions explained: an empirical overview . IEEE Transactions on Software Engineering 49 ( 2 ), pp. 849–871 . External Links: Document Cited by: §1 , §2 , §2 . 

- Y. Zhao, A. Serebrenik, Y. Zhou, V. Filkov, and B. Vasilescu (2017) The impact of continuous integration on other software development practices: a large-scale empirical study . In 2017 32nd IEEE/ACM International Conference on Automated Software Engineering (ASE) , pp. 60–71 . Cited by: §1 . 

Generated on Wed Jan 21 17:04:45 2026 by L a T e XML

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-06-015.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-06-015.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-06-015.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
- refreshed_live_source: false
