---
version: source-capture.v1
article_id: art-2026-03-10-061
ticket_id: ticket-import-art-2026-03-10-061
source_url: https://www.arxiv.org/pdf/2601.18749
canonical_url: https://arxiv.org/abs/2601.18749
source_title: "Let\u2019s Make Every Pull Request Meaningful: An Empirical Analysis\
  \ of Developer and Agentic Pull Requests"
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-05T16:04:21Z'
linked_paper_urls: []
---
# Source Capture

## Title

Let’s Make Every Pull Request Meaningful: An Empirical Analysis of Developer and Agentic Pull Requests

## Body

\setcctype

by

Let’s Make Every Pull Request Meaningful: An Empirical Analysis of Developer and Agentic Pull Requests

Haruhiko Yoshioka 0009-0004-2353-1397 , Takahiro Monno 0009-0001-4669-8411 Nara Institute of Science and Technology Ikoma Nara Japan yoshioka.haruhiko.yi4@naist.ac.jp monno.takahiro.mv3@naist.ac.jp , Haruka Tokumasu 0009-0006-5463-6305 , Taiki Wakamatsu 0009-0000-4237-106X Kyushu University Fukuoka Fukuoka Japan tokumasu@posl.ait.kyushu-u.ac.jp wakamatsu.taiki.448@s.kyushu-u.ac.jp , Yuki Ota 0009-0001-3657-161X Ritsumeikan University Ibaraki Osaka Japan is0607ih@ed.ritsumei.ac.jp , Nimmi Weeraddana 0009-0002-6550-4181 University of Calgary Calgary Alberta Canada nimmi.weeraddana@ucalgary.ca and Kenichi Matsumoto 0000-0002-7418-9323 Nara Institute of Science and Technology Ikoma Nara Japan matumoto@is.naist.jp

(2026)

Abstract.

The automatic generation of pull requests (PRs) using AI agents has become increasingly common.
Although AI-generated PRs are fast and easy to create, their merge rates have been reported to be lower than those created by humans.
In this study, we conduct a large-scale empirical analysis of 40,214 PRs collected from the AIDev dataset.
We extract 64 features across six families and fit statistical regression models to compare PR merge outcomes for human and agentic PRs, as well as across three AI agents.
Our results show that submitter attributes dominate merge outcomes for both groups, while review-related features exhibit contrasting effects between human and agentic PRs.
The findings of this study provide insights into improving PR quality through human–AI collaboration.

Pull Request, AI Agent, Empirical Study, Software Engineering, Human-AI Collaboration 
† † journalyear: 2026 † † copyright: cc † † conference: 23rd International Conference on Mining Software Repositories; April 13–14, 2026; Rio de Janeiro, Brazil † † booktitle: 23rd International Conference on Mining Software Repositories (MSR ’26), April 13–14, 2026, Rio de Janeiro, Brazil † † doi: 10.1145/3793302.3793567 † † isbn: 979-8-4007-2474-9/2026/04 † † ccs: Software and its engineering Collaboration in software development † † ccs: Software and its engineering Software creation and management

1. Introduction

In software development, creating pull requests (PRs) requires substantial effort from developers (Gousios et al. , 2016 ) . Beyond implementing code changes, developers must also provide contextual information, such as clear statements of intent, references to related issues, and responses to peer-reviewer feedback.
Existing literature (Gousios et al. , 2014 ; Tsay et al. , 2014 ; Zhang et al. , 2023 ; Iyer et al. , 2021 ; Meijer et al. , 2025 ; Alami et al. , 2022 ) has extensively analyzed the factors influencing the acceptance or rejection of developer-authored PRs.
For example, Gousios et al. (Gousios et al. , 2014 ) have revealed that PR acceptance is influenced by change size, file activity, project scale, contributor’s track record, and the review process.
Furthermore, others have shown that the richness of descriptions, the nature of discussions, and the presence of tests (Tsay et al. , 2014 ) impact the acceptance of developers’ PRs.

To help developers create PRs, Artificial Intelligence (AI) agents are used to automatically create change sets and submit PRs (Li et al. , 2025 ) .
However, AI-generated PRs (i.e., Agentic PRs ) are not without their limitations (Cotroneo et al. , 2025 ; Bukhari et al. , 2023 ; Chouchen et al. , 2024 ; Cihan et al. , 2025 ; Li et al. , 2025 ) .
In fact, AI-generated code has been reported to be structurally simple and repetitive, prone to containing vulnerabilities (Cotroneo et al. , 2025 ) , and identifiable by specific lexical and syntactic features (Bukhari et al. , 2023 ) .
Besides, PRs that include at least one ChatGPT shared link take longer to be closed (merged or abandoned) (Chouchen et al. , 2024 ) .
Then, Li et al. (Li et al. , 2025 ) demonstrated that the acceptance rate of Agentic PRs
(i.e., the proportion of Agentic-PRs that are successfully merged) in AIDev dataset
is significantly lower than that of humans.
However, little is known about the quality and acceptability of such PRs compared to those authored by humans (Li et al. , 2025 ; Cotroneo et al. , 2025 ) .

The primary goal of this study is to enhance PR quality by leveraging the complementary strengths of humans and GenAI.
To compare the factors that characterize the accepted PRs that were created by humans and agents, we first extract 64 features across 6 families from a dataset of 6,618 human-authored PRs and 33,596 agentic PRs from the AIDev dataset (Li et al. , 2025 ) .
These features include change set size, number of files added/deleted/changed, task types, external links, and AI agent type (e.g., OpenAI Codex, Copilot).
For humans and each of the AI models in AIDev dataset, we fit and analyze regression models to uncover the features of PRs that make them difficult for GenAI agents to get their PR merged but easy for humans (and vice versa).
By gaining insights into such features, we provide actionable evidence regarding the behavior of AI agents in real-world projects, offering guidelines for developers and project managers to optimize development processes where AI and humans collaborate (Li et al. , 2025 ) .
This study addresses the following three research questions (RQs):

RQ1: To what extent can statistical regression models determine whether a PR created by a human or an AI agent will be merged? As a foundation for our comparative analysis between humans and AI agents, we analyze the extent to which the constructed regression models can perform on real-world PRs.

RQ2: How do the features contributing to merge probability differ between PRs created by humans and those created by AI agents? This RQ aims to uncover the respective strengths and weaknesses of humans and agents in getting their PRs merged. We investigate the explanatory power of each feature family in our statistical models to identify which ones contribute most to PR merging, providing insights into which aspects are most critical for humans versus agents.

RQ3: How do the features contributing to merge probability differ across PRs generated by different AI agents? In this RQ, we compare the importance of feature families in predicting the merge outcomes of agent-authored PRs across different AI agents, with the goal of providing insights into which AI agents are better suited for specific development contexts.

Our key findings reveal that: (1) submitter attributes dominate merge outcomes for both human and agentic PRs; (2) increased review activity is associated with higher merge likelihood for human PRs but lower for agentic PRs; and (3) AI agents show distinct merge patterns.

Figure 1. An overview of our study design

2. Study Design 
Table 1. Families of Features

Family # Features

PR Change Size & Commit Characteristics 18

PR Description 8

Submitter Attributes 6

Repository Attributes 3

Issue Linkage & Surrounding Context 3

Reviews & Discussion 26

Total number of features 64

In this section, we describe our method for data preparation (Section 2.1 ) and the model creation (Section 2.2 ). Figure 1 overviews our study design.

2.1. Data Preparation

Collect metadata from AIDev dataset. We begin with the AIDev dataset (Nov. 2025) released by Li et al. (Li et al. , 2025 ) , which consists of 932,791 Agentic PRs created by five major autonomous AI agents.
Of these, 33,596 include rich metadata such as comments, issues, reviews, commits, repositories, timelines, and user information.

Collect metadata for human-authored PRs. For comparison purposes, the AIDev dataset contains 6,618 human-authored PRs created by 2,515 developers (hereafter referred to as human PRs ) across 818 repositories. However, for these human PRs, the AIDev dataset provides only repository-level information and task type, and does not include other metadata such as comments, reviews, or commits.
To enable a fair comparison between agentic PRs and human PRs, it is necessary to use the same set of features for both. Therefore, we collect the same set of metadata for human PRs as those available for agentic PRs by using the same GitHub API endpoints as Li et al. when constructing the AIDev dataset (Li et al. , 2025 ) .

Extract features from human PRs and agentic PRs, covering distinct families of features. We use our dataset of metadata to extract 64 features across six families (while consulting prior work (Zhang et al. , 2023 ; Soares et al. , 2015 ; Tsay et al. , 2014 ) ) to represent different dimensions of a PR, ranging from code changes to social interactions.
Table 1 shows these families of features.
For example, the family that covers PR Change Size & Commit Characteristics (Zhang et al. , 2023 ) includes 18 features, such as commit count, unique committers , and average changes per commit . Similarly, the family that covers PR Description contains eight features, including message token count, message character count , and average line count of messages .
Then, the family of Submitter Attributes (Zhang et al. , 2023 ) contains features, such as the number of prior reviews made by the PR submitter, social distance (i.e., whether the submitter follows the user who closes the pull request), and the submitter’s follower count .
The full list of 64 features is available in our online appendix. 1 1 1 https://zenodo.org/records/18373332 After encoding all the categorical features with one-hot encoding, our dataset expanded to 106 model terms.

Label PRs with merge status. To be able to analyze differences in families of features that contribute to merge status, we determine the merge status of each PR by checking if the merged_at field of a PR is NULL (Li et al. , 2025 ) . If so, the PR is considered not merged; otherwise, it is regarded as merged.
Note that this labelling process is applied to both agentic PRs and human PRs.

2.2. Model Creation

Our goal is to study what characterizes merged PRs created by humans and agents.
Therefore, we select a statistical regression modelling approach which, unlike many other classification techniques, emphasizes interpretability. Such models (e.g., logistic regression) provide clear insights into how different factors influence outcomes, making them suited for nuanced analysis. Below, we discuss how we create these models.

Eliminate collinearity and multicollinearity. Collinear terms distort importance estimates (Hastie et al. , 2009 ) .
We use Variance Inflation Factor (VIF) (Montgomery et al. , 2021 ) to detect multicollinearity in our regression models, as VIF captures higher-order dependencies that pairwise correlation coefficients may fail to identify.
Applying the commonly used threshold of VIF < 10 <10 (O’brien, 2007 ) , we eliminate ten model terms (two due to perfect collinearity and eight with VIF > 10 >10 ), reducing the number of model terms across the feature families from 106 to 96.

Fit the models. We fit logistic regression models using the set of 96 model terms that remained after the collinearity elimination step.
First, we train two main models using the full datasets: one on all human PRs and one on all agentic PRs.
Note that our dataset contains Agentic PRs created by five AI agents: OpenAI Codex ( N = 21 , 799 N=21,799 ), GitHub Copilot ( N = 4 , 970 N=4,970 ), Cursor ( N = 1 , 541 N=1,541 ), Devin ( N = 4 , 827 N=4,827 ), and Claude Code ( N = 459 N=459 ).
Therefore, we further fit five additional models by partitioning the Agentic PR dataset by agent name and fitting a separate logistic regression model for each agent.
Our dataset and replication package is available online. 1

To answer RQ1, we analyze model fitness, which is a prerequisite to ensure that our models provide reliable insights. We then compare the explanatory power across different feature families in the human-PR model and all-agentic model to answer RQ2, and examine agent-specific PR models to address RQ3.

3. Study Results

In this section, we present the approach and results for our RQs.

Table 2. Prediction Performance

Metric Human All-agentic OpenAI Copilot Cursor Devin Claude

Codex Code

AUC 0.878 0.960 0.997 0.775 0.969 0.810 0.904

Precision 0.859 0.939 0.994 0.690 0.958 0.744 0.963

Recall 0.911 0.909 0.984 0.582 0.904 0.809 0.768

F1 0.884 0.923 0.989 0.631 0.930 0.775 0.850

Brier Score 0.119 0.073 0.014 0.193 0.063 0.176 0.113

Table 3. Feature Family Importance: Human vs Agentic PRs

Human PRs Agentic PRs

Family χ 2 \chi^{2} df p χ 2 \chi^{2} df p

Submitter Attributes 1,969.19 6 * 19,440.85 6 *

Reviews & Discussion 202.03 22 * 1,195.76 22 *

PR Change Size & Commit 118.55 17 * 1,078.55 17 *

Repository Attributes 189.54 37 * 633.78 40 *

Issue Linkage & Context 4.00 3 ∘ \circ 250.65 3 *

PR Description 17.99 4 * 93.21 4 *

Entire model 2,853.86 96 * 25,528.61 96 *

* p < 0.001 p<0.001 ∘ \circ Not Significant ( p = 0.262 p=0.262 )

3.1. RQ1: To what extent can statistical regression models determine whether a PR created by a human or an AI agent will be merged?

Approach. We evaluate the discriminatory power of our models using AUC (0.5 = random, 1 = perfect), precision, recall, and F1 score (0 = worst, 1 = best), and calibration using the Brier score (0 = best, 1 = worst), via five-fold cross-validation.

Results. Table 2 shows the performance of our logistic regression models.
Accordingly, all the models surpass the baseline performance of a random guesser in terms of AUC when predicting whether a PR will be merged across all cases.
For example, the model for human PRs shows an AUC of 0.878, while the All-Agentic model achieves a higher AUC of 0.960.
Besides, the precision, recall, and F1-scores of our models are also closer to 1, demonstrating robust performance under class imbalance.
In terms of the Brier score, all models achieved values close to zero, indicating well-calibrated probability estimates in their predicted merge probabilities. Overall, our models are strong, suggesting that the observations derived from these models are meaningful and suitable for comparative analyses in upcoming RQs: RQ2 & RQ3.

3.2. RQ2: How do the features contributing to merge probability differ between PRs created by humans and those created by AI agents?

Approach. In this RQ, we identify differences in strengths between humans and AI agents in contributing to PR merges. To this end, we use the human-PR model and the all-agentic-PR model to analyze which feature families are most important for predicting merge probabilities for human PRs and agentic PRs.

Figure 2. Feature family importance: human vs agentic PRs

We use Likelihood Ratio (LR) χ 2 \chi^{2} chunk tests (Harrell, 2015 ) to estimate feature family importance.
A larger LR χ 2 \chi^{2} value indicates greater loss of explanatory power when a family is removed, signifying higher importance in explaining merge outcomes.
We compare relative importance ( χ 2 ​ value of the family χ 2 ​ value of the entire model × 100 % \frac{\chi^{2}\text{value of the family}}{\chi^{2}\text{value of the entire model}}\times 100\% ) between human and agentic PRs using radar charts.

Results. Table 3 compares the importance of feature families between human PRs and agentic PRs.
The χ 2 \chi^{2} column reports the LR χ 2 \chi^{2} statistic from chunk tests, ranking feature families by explanatory power. The df column indicates model terms per feature family after collinearity elimination. For comparison purposes, Figure 2 visualizes the relative importance of each feature family as a percentage of the total LR χ 2 \chi^{2} in the human-PR model and all-agentic-PR model.

Table 3 and Figure 2 show that submitter attributes dominate merge outcomes for both human PRs and agentic PRs, with relative importance of 1 , 969.19 2 , 853.86 \frac{1,969.19}{2,853.86} × \times 100=69.00% and 19 , 440.85 25 , 528.61 \frac{19,440.85}{25,528.61} × \times 100=76.15%, respectively.
A feature-level analysis of this family reveals that when the contributor is also the integrator of a PR (i.e., when the value of same_user feature is one), the odds of merging a PR increase by approximately 219 times for human PRs and by 5,419 times for agentic PRs, compared to cases where the contributor and integrator are different individuals.
We find that 57.63% of merged human PRs have same_user =1, compared to 77.51% of merged agentic PRs. This difference is also statistically significant (two-proportion z-test: z = − 29.38 z=-29.38 , p < 0.001 p<0.001 ), confirming that agentic PRs are substantially more likely than human PRs to be merged by the submitter of that PR.

Implication 1. This finding provides insights into a potential risk: allowing the same entity (especially an AI agent) to both author and merge PRs may limit independent oversight.
Project maintainers may investigate such cases further and enforce third-party approval for PRs when deploying AI agents in development workflows.

For both human PRs and agentic PRs, reviews and discussion attributes form the second most important feature family, with a relative importance of 202.03 2 , 853.86 \frac{202.03}{2,853.86} × \times 100=7.08% and 1 , 195.76 25 , 528.61 \frac{1,195.76}{25,528.61} × \times 100=4.68%, respectively.
However, feature-level analysis shows that these signals carry different meanings across the two PR types.
For instance, each additional reviewer comment increases merge odds by 2.7% for human PRs, but decreases merge odds by 2.8% for agentic PRs.
In fact, 3.7% of merged agentic PRs have more than three reviewers, whereas a higher percentage (i.e., 5.8%) of unmerged agentic PRs have more than three reviewers.

Implication 2. Our finding provides insights into another potential issue: extensive review activity around agentic PRs may signal the amount of correction required before merging. We encourage project maintainers to break down code changes into smaller, more manageable tasks for agents, enabling easier integration and code review.

3.3. RQ3: How do the features contributing to merge probability differ across PRs generated by different AI agents?

Approach. In this RQ, we aim to understand the characteristics of specific AI agents to provide insights into selecting the most suitable agent.
We apply LR χ 2 \chi^{2} chunk tests to agent-specific models (Section 2.2 ) to assess feature family importance.
Note that we exclude the logistic regression models for Cursor and Claude Code because they exceed the degrees-of-freedom budget defined as # PRs in minority class 15 \frac{\text{\# PRs in minority class}}{15} (Harrell Jr et al. , 1984 , 1985 ) .
We then visualize χ 2 \chi^{2} statistics using radar charts, 1 and identify the feature families that have the highest explanatory power in the remaining three models.

Results. Figure 3 , the radar charts, shows that different agents’ PR merge likelihood is correlated with different feature families.
In fact, OpenAI Codex’s most important feature family is submitter features, consistent with the RQ2 models, whereas Copilot is primarily driven by PR change size and commit features, and Devin by review and discussion features.

Such distinctions are reflected in the feature-level coefficients of our models as well. For example, within the PR change size and commit family, a unit increase in the number of commits linked to a PR increases merge likelihood by 2.11 times for Copilot and 1.57 times for OpenAI Codex, but is associated with an approximately 7% decrease in merge odds for Devin. Similarly, a higher volume of submitter-reviewer interaction increases the odds of merging for OpenAI Codex-authored PRs, compared to others.

Figure 3. Feature family importance across AI agents

Implication 3. Project maintainers may select agents based on the specific characteristics of their development workflows. Consequently, researchers should investigate how to design PR review workflows that better leverage these varying agent characteristics.

4. Threats to Validity

PRs with NULL merged_at values include both closed and open PRs; the latter may introduce noise, though the large sample size mitigates this effect.
Our models identify correlations, not causal relationships.
The AIDev dataset naturally excludes repositories that prohibit AI-generated PRs.
Additionally, Cursor and Claude Code were excluded from RQ3 due to small sample sizes ( N N =1,541 and N N =459), limiting generalizability of our results for these agents.

5. Discussion and Future Work

Our findings reveal both shared and distinct factors influencing the merge outcomes of human-authored and agent-authored PRs, suggesting that uniform PR creation and review workflows may not be optimal for both.
For instance, Khare et al. (Khare et al. , 2025 ) show that hybrid code review workflows—where AI handles routine checks and humans focus on higher-level judgment—better leverage complementary strengths.
For human-AI collaboration, Hassan et al. (Hassan et al. , 2024 ) advocate a shift from task-first approaches to an approach where humans and AI discuss and refine goals through dialogues.
Future work may explore collaborative development that delineates human and AI roles, leveraging AI for PR generation while preserving human contributions in reviews.

Acknowledgments

This work was supported by JST SPRING Grant Number JPMJSP2140.

References

- A. Alami, R. Pardo, M. L. Cohn, and A. Wąsowski (2022) Pull request governance in open source communities . IEEE Transactions on Software Engineering 48 ( 12 ), pp. 4838–4856 . External Links: Document Cited by: §1 .

- S. Bukhari, B. Tan, and L. De Carli (2023) Distinguishing ai- and human-generated code: a case study . In Proceedings of the 2023 Workshop on Software Supply Chain Offensive Research and Ecosystem Defenses , SCORED ’23 , New York, NY, USA , pp. 17–25 . External Links: ISBN 9798400702631 , Link , Document Cited by: §1 .

- M. Chouchen, N. Bessghaier, M. Begoug, A. Ouni, E. A. AlOmar, and M. Wiem Mkaouer (2024) How do software developers use chatgpt? an exploratory study on github pull requests . In 2024 IEEE/ACM 21st International Conference on Mining Software Repositories (MSR) , Vol. , pp. 212–216 . External Links: Document Cited by: §1 .

- U. Cihan, V. Haratian, A. İçöz, M. K. Gül, Ö. Devran, E. F. Bayendur, B. M. Uçar, and E. Tüzün (2025) Automated code review in practice . In 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP) , Vol. , pp. 425–436 . External Links: Document Cited by: §1 .

- D. Cotroneo, C. Improta, and P. Liguori (2025) Human-written vs. ai-generated code: a large-scale study of defects, vulnerabilities, and complexity . In 2025 IEEE 36th International Symposium on Software Reliability Engineering (ISSRE) , Vol. , pp. 252–263 . External Links: Document Cited by: §1 .

- G. Gousios, M. Pinzger, and A. v. Deursen (2014) An exploratory study of the pull-based software development model . In Proceedings of the 36th International Conference on Software Engineering , ICSE 2014 , New York, NY, USA , pp. 345–355 . External Links: ISBN 9781450327565 , Link , Document Cited by: §1 .

- G. Gousios, M. Storey, and A. Bacchelli (2016) Work practices and challenges in pull-based development: the contributor’s perspective . In Proceedings of the 38th International Conference on Software Engineering , ICSE ’16 , New York, NY, USA , pp. 285–296 . External Links: ISBN 9781450339001 , Link , Document Cited by: §1 .

- F. E. Harrell (2015) Regression modeling strategies: with applications to linear models, logistic and ordinal regression, and survival analysis . Second edition , Springer Cham . External Links: Document , ISBN 978-3-319-33039-6 Cited by: §3.2 .

- F. E. Harrell Jr, K. L. Lee, R. M. Califf, D. B. Pryor, and R. A. Rosati (1984) Regression modelling strategies for improved prognostic prediction . Statistics in medicine 3 ( 2 ), pp. 143–152 . Cited by: §3.3 .

- F. E. Harrell Jr, K. L. Lee, D. B. Matchar, and T. A. Reichert (1985) Regression models for prognostic prediction: advantages, problems, and suggested solutions. . Cancer treatment reports 69 ( 10 ), pp. 1071–1077 . Cited by: §3.3 .

- A. E. Hassan, G. A. Oliva, D. Lin, B. Chen, and Z. M. (. Jiang (2024) Rethinking software engineering in the foundation model era: from task-driven ai copilots to goal-driven ai pair programmers . External Links: 2404.10225 , Link Cited by: §5 .

- T. Hastie, R. Tibshirani, and J. Friedman (2009) The elements of statistical learning: data mining, inference, and prediction . Second edition , Springer , New York, NY, USA . External Links: Document , Link , ISBN 978-0-387-84857-0 Cited by: §2.2 .

- R. N. Iyer, S. A. Yun, M. Nagappan, and J. Hoey (2021) Effects of personality traits on pull request acceptance . IEEE Transactions on Software Engineering 47 ( 11 ), pp. 2632–2643 . External Links: Document Cited by: §1 .

- V. Khare, V. Saini, D. Sharma, A. Kumar, A. Rana, and A. Yadav (2025) DeputyDev – ai powered developer assistant: breaking the code review logjam through contextual ai to boost developer productivity . External Links: 2508.09676 , Link Cited by: §5 .

- H. Li, H. Zhang, and A. E. Hassan (2025) The rise of ai teammates in software engineering (se) 3.0: how autonomous coding agents are reshaping software engineering . External Links: 2507.15003 , Link Cited by: §1 , §1 , §2.1 , §2.1 , §2.1 .

- W. Meijer, M. Riveni, and A. Rastogi (2025) Ecosystem-wide influences on pull request decisions: insights from npm . Empirical Softw. Engg. 30 ( 6 ). External Links: ISSN 1382-3256 , Link , Document Cited by: §1 .

- D. C. Montgomery, E. A. Peck, and G. G. Vining (2021) Introduction to linear regression analysis . 6th edition , John Wiley & Sons , Hoboken, NJ, USA . External Links: ISBN 978-1-119-57872-7 , Link Cited by: §2.2 .

- R. M. O’brien (2007) A caution regarding rules of thumb for variance inflation factors . Quality & Quantity 41 ( 5 ), pp. 673–690 . External Links: ISSN 1573-7845 , Document , Link Cited by: §2.2 .

- D. M. Soares, M. L. de Lima Júnior, L. Murta, and A. Plastino (2015) Acceptance factors of pull requests in open-source projects . In Proceedings of the 30th Annual ACM Symposium on Applied Computing , SAC ’15 , New York, NY, USA , pp. 1541–1546 . External Links: ISBN 9781450331968 , Link , Document Cited by: §2.1 .

- J. Tsay, L. Dabbish, and J. Herbsleb (2014) Influence of social and technical factors for evaluating contribution in github . In Proceedings of the 36th International Conference on Software Engineering , ICSE 2014 , New York, NY, USA , pp. 356–366 . External Links: ISBN 9781450327565 , Link , Document Cited by: §1 , §2.1 .

- X. Zhang, Y. Yu, G. Gousios, and A. Rastogi (2023) Pull request decisions explained: an empirical overview . IEEE Transactions on Software Engineering 49 ( 2 ), pp. 849–871 . External Links: Document Cited by: §1 , §2.1 .
