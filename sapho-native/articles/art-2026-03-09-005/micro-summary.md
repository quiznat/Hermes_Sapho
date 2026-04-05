# How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests

## Core Thesis

In this filtered comparison, pull requests produced by AI coding agents are not just marginal variants of human pull requests. They differ across every reported structural metric, with the sharpest separation in commit count, and they also show higher average description-to-diff similarity under TF-IDF, CodeBERT, and GraphCodeBERT. The result is a real distributional distinction between agentic and human code-change artifacts, but one established on a filtered and partially reconstructed dataset rather than a full raw-corpus apples-to-apples view.

## Why It Matters for Sapho

This matters because it pushes Sapho away from treating agent output as interchangeable with ordinary developer output. If agentic pull requests have a distinct structural signature and somewhat tighter alignment between descriptions and diffs, then evaluation doctrine should assume that agent-written software work leaves detectable artifact patterns. But the paper also shows why governance must stay careful: the comparison depends on heavy filtering, reconstruction of the human side through GitHub API retrieval, and similarity measures with known interpretive limits. The field signal is real, but the measurement stack is not clean enough to support broad causal stories.

## Key Findings

- The study begins from a very large AIDev corpus of 932,791 agentic pull requests and 6,618 human pull requests across 116,211 repositories, but the final structural analysis uses a much smaller retained subset with valid patches: 24,014 agentic pull requests covering 440,295 commits and 5,081 human pull requests covering 23,242 commits.
- Across all reported structural metrics, agentic and human pull requests differ at p ≤ 0.001 under Mann-Whitney U testing, with effect sizes reported using Cliff's delta because the metric distributions violate normality assumptions.
- Commit count is the strongest separator between the two groups, with Cliff's delta = 0.5429, labeled large.
- Files touched and deletions also separate meaningfully, with Cliff's delta = 0.4487 and 0.4462 respectively, both labeled medium.
- Additions and total line changes differ as well, but more weakly, with Cliff's delta = 0.2836 for additions and 0.3158 for total line changes, both labeled small.
- Pull request descriptions from the agentic side score higher on average against their diffs under all three reported similarity measures: TF-IDF 0.1245 versus 0.1007, CodeBERT 0.9356 versus 0.9285, and GraphCodeBERT 0.8254 versus 0.7815.
- The human comparison set was not ready-made in the source dataset: the authors had to retrieve commit metadata and file-level patches through the GitHub REST API, then reconstruct files touched from unique modified paths across commits, treating renames as single-file modifications.

## Evidence and Findings

- The paper does not rest on anecdote or a tiny sample. It starts from 932,791 agentic pull requests and 6,618 human pull requests across 116,211 repositories, then narrows to 24,014 agentic and 5,081 human pull requests with valid patches for the actual analysis. That supports the conclusion that the reported differences are drawn from substantial observed activity, while also making clear that the claims apply to a retained subset rather than the full corpus.
- The structural comparison is statistically disciplined: because the metric distributions failed normality tests, the authors used Mann-Whitney U and Cliff's delta instead of parametric summaries. On that basis, every reported structural metric differs at p ≤ 0.001, supporting the conclusion that agentic and human pull requests have distinct distributional profiles rather than isolated mean differences.
- The strongest empirical separator is commit count, with Cliff's delta = 0.5429, a large effect. Files touched at 0.4487 and deletions at 0.4462 are medium effects, while additions at 0.2836 and total line changes at 0.3158 are small. This matters because the difference is not uniform: agentic pull requests appear especially distinguishable in how work is partitioned into commits, less so in raw code volume.
- Description-to-diff alignment is consistently higher on the agentic side under three different similarity systems: TF-IDF rises from 0.1007 to 0.1245, CodeBERT from 0.9285 to 0.9356, and GraphCodeBERT from 0.7815 to 0.8254. That supports a bounded conclusion that agentic pull request descriptions track the associated code changes more closely on average within this study's measurement frame.
- The human side required additional reconstruction before comparison. Commit metadata and file-level patches were retrieved via the GitHub REST API, and files touched were computed from unique modified paths across commits, with renames counted once. That supports the conclusion that the comparison is analytically usable but not methodologically symmetric, which matters because some observed differences may partly reflect reconstruction choices or retrieval incompleteness.
- The paper itself flags measurement fragility. BM25-style lexical similarity is explicitly unbounded and should be read only as a relative signal, and the authors warn that missing or truncated patches, GitHub API retrieval gaps, and large-diff truncation may bias distributions and similarity scores. This supports a careful reading: the results show structured differences, but not a cleanly calibrated or fully bias-resistant measurement of agent quality or intent.

## Contradictions and Tensions

- The paper's headline scale is enormous, but the decisive analysis is not run on the full raw corpus. The starting dataset contains 932,791 agentic pull requests, yet the filtered analysis uses 24,014 agentic pull requests with valid patches. That creates a real scope tension between the impression of comprehensive coverage and the narrower population actually measured.
- The structural differences are universal in statistical significance, but not uniform in magnitude. Commit count shows a large effect, files touched and deletions show medium effects, and additions plus total line changes are only small. That cuts against any simplified claim that agentic pull requests are categorically larger or categorically more expansive in every structural sense.
- The description-to-diff advantage for agentic pull requests appears across all three reported measures, but the measures do not carry the same interpretive weight. TF-IDF and BM25-style lexical signals are relative and unstable across long, token-heavy diffs, while even embedding-based similarity can be affected by patch truncation. The signal is directionally consistent, but the meaning of the score gap is not fully settled.
- The comparison depends on asymmetric data preparation. Human pull requests needed post hoc GitHub API retrieval and file-level reconstruction, while the agentic side came from the existing corpus structure. That creates a comparability tension: the study may be capturing real behavioral differences, but it is also operating across differently assembled records.

## Mechanism or Bounds

The strongest supported explanation is operational rather than causal: within the retained set of pull requests with valid patches, agentic work products exhibit a distinct artifact profile, especially in commit partitioning, and their written descriptions align more closely on average with the resulting diffs under the study's chosen similarity measures. The paper does not establish why agents differ this way. It does not isolate whether the pattern comes from agent planning behavior, tool defaults, repository selection, task type, or differences introduced by data reconstruction and filtering. The findings are therefore bounded to comparative distributions in a filtered dataset, not a causal mechanism for how or why AI coding agents modify code differently.

## Limits

- The reported results apply to a filtered subset with valid patches, not the entire original corpus.
- The human comparison set required additional GitHub API retrieval and reconstruction, introducing possible incompleteness and asymmetry.
- Missing or truncated patches may bias both structural distributions and similarity measurements.
- Very large diffs may distort lexical similarity signals and affect embedding-based estimates through truncation.
- The paper shows distributional difference, not causal explanation.
- The study does not establish that higher description-to-diff similarity means better code, better reasoning, or better reviewability.
