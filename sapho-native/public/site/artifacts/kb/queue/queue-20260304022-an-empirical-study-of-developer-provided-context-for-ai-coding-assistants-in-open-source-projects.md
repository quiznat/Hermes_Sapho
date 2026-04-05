<details class="traceability-panel">
<summary>Traceability</summary>
<div class="traceability-body">
<ul>
  <li><strong>Source:</strong> <a href="https://arxiv.org/abs/2512.18925" target="_blank" rel="noopener">https://arxiv.org/abs/2512.18925</a></li>
  <li><strong>Intake queued:</strong> 2026-03-04T03:59:01Z</li>
  <li><strong>Source captured:</strong> 2026-03-30T17:55:40Z</li>
  <li><strong>Curated:</strong> 2026-04-02T21:16:25Z</li>
  <li><strong>Artifact finalized:</strong> 2026-04-02T21:18:55Z</li>
  <li><strong>Artifact published:</strong> 2026-03-30T17:58:57Z</li>
</ul>
</div>
</details>

# An Empirical Study of Developer-Provided Context for AI Coding Assistants in Open-Source Projects

## Core Thesis

Developer-supplied context for AI coding assistants in open-source repositories is not a narrow set of prompts but a structured operating layer: across 401 cleaned repositories, maintainers most often supplied guidelines, project information, and conventions, usually in combination, while explicit assistant-directed instructions were less universal. The result is a useful empirical map of what developers think assistants need, but the map is methodologically bounded because large-scale thematic coding depended on repeated LLM labeling with only moderate agreement against human raters.

## Why It Matters for Sapho

This matters because it pushes Sapho away from treating AI-assistant context as simple prompt engineering. In practice, developers appear to externalize a mixed governance bundle: how the project works, how code should be written, and how work should be done. That supports a stronger evaluation doctrine for Sapho: assess context systems as operational policy surfaces, not just instruction text. At the same time, the study also warns against over-reading neat taxonomies from LLM-coded corpora. Frequency patterns are informative, but they are not ground truth without visible reliability bounds.

## Key Findings

- The analyzed corpus covered 401 open-source repositories with cursor rules after manual cleaning reduced an initial 487 fetched repositories, showing that the reported landscape is already filtered by nontrivial exclusion decisions.
- The study organized developer-provided context into five themes: Conventions, Guidelines, Project Information, LLM Directives, and Examples.
- Guidelines appeared in 89% of repositories, Project Information in 85%, Conventions in 84%, and LLM Directives in 50%, indicating that repositories more often emphasize project norms and operating context than direct model-facing instruction.
- Multi-category context was common: 37.16% of repositories included four categories, while only 24.69% included all five, so broad coverage existed but complete coverage was a minority pattern.
- The repository set contained 1,876 .mdc files, averaging 4.68 files per repository; 93.27% of repositories placed them in the recommended root .cursor directory.
- Rule files were often substantial rather than trivial, averaging 462.67 lines, with the longest reaching 11,076 lines.
- The full-dataset coding pipeline used gemini-2.5-flash-preview-09-2025 at temperature 0.0 with three repeated labeling passes and majority vote per line.
- That pipeline is useful but bounded: human coders reached Cohen’s Kappa of 0.71 on the initial sample, while LLM-assisted coding reached 0.64 and 0.65 against the two human raters; 2.1% of all lines still produced three different LLM labels and were forced into “No Code,” and 28.70% of all lines were duplicates.

## Evidence and Findings

- The paper shows that the observed ecosystem is sizeable but curated: 487 repositories were initially fetched, then reduced to 401 after removing deleted files, non-rule uses of .mdc, non-English files, duplicates, and template or example repositories. That supports the conclusion that the taxonomy rests on a substantial corpus, while also making clear that its representativeness is bounded by manual exclusion decisions.
- The source identifies five recurring context themes—Conventions, Guidelines, Project Information, LLM Directives, and Examples—and reports repository-level prevalence of 89% for Guidelines, 85% for Project Information, 84% for Conventions, and 50% for LLM Directives. This supports the conclusion that developers more often encode workflow, project knowledge, and coding norms than narrow model-facing commands, which matters because assistant performance may depend as much on institutionalized project context as on explicit instructions.
- Repositories commonly layered several context types together rather than relying on a single instruction mode: 37.16% of repositories included four categories, while 24.69% included all five. That supports the conclusion that mixed-context bundles are normal, but fully saturated context systems are not. For Sapho, this matters because evaluation should expect partial but composite context architectures rather than idealized complete ones.
- The corpus also shows that developer context is physically substantial. Across 401 repositories, the authors collected 1,876 .mdc files, averaging 4.68 files per repository, with average file length of 462.67 lines and a maximum of 11,076 lines. This supports the conclusion that these repositories are maintaining durable context infrastructure, not just short prompt fragments, which matters for any system that must reason about maintainability, retrieval, and instruction overload.
- The coding pipeline stabilizes large-scale classification operationally but does not eliminate interpretive uncertainty. The authors used three LLM labeling passes with majority vote, yet LLM-human agreement on the initial sample was only 0.64 and 0.65, below the 0.71 agreement between human coders. This supports the conclusion that the theme frequencies are useful measured patterns, not exact semantic truth, which matters because downstream synthesis should treat the taxonomy as directional evidence rather than a definitive ontology.
- Residual uncertainty remained visible even after repeated labeling: 2.1% of all lines received three different LLM labels and were assigned “No Code,” which the authors say should be treated as a lower bound, and 19,917 lines—28.70% of all lines—were duplicates. That supports the conclusion that ambiguity and repetition could materially shape reported distributions, which matters because repeated phrasing may amplify certain themes while unresolved disagreement hides some true category uncertainty.

## Contradictions and Tensions

- The paper presents a large empirical map, but that map narrows materially during cleaning: the shift from 487 fetched repositories to 401 analyzed repositories means the visible ecosystem is not the same as the raw discovered one.
- The thematic story is internally uneven. Guidelines, Project Information, and Conventions are each present in roughly four-fifths of repositories, while LLM Directives appear in only 50%. That cuts against any simple claim that developer context is mainly about directly instructing the model.
- Multi-category context is common, but full thematic coverage is not. Repositories often combine several context types, yet only 24.69% include all five categories, so “rich context” should not be confused with comprehensive context.
- The study relies on an LLM-assisted coding pipeline to describe what developers wrote for LLMs. That is operationally efficient but interpretively tense: human-human agreement was stronger than LLM-human agreement, and some lines never converged under repeated model labeling.
- Duplicate text is a major dataset feature, not a footnote: 28.70% of all lines were duplicates. That raises the risk that common boilerplate or copied phrasing can make some thematic patterns look more stable or more prevalent than they would in a de-duplicated semantic analysis.

## Mechanism or Bounds

The strongest supported mechanism is organizational rather than behavioral: developers appear to use cursor rules as a repository-level context layer that packages project information, coding conventions, and procedural guidance into reusable files, usually in the repository root .cursor directory and often across multiple substantial documents. The study supports that these artifacts are structured governance surfaces for assistants and collaborators alike.

But the paper does not establish how those context bundles change coding-assistant performance, nor why some themes are more prevalent than others. Its contribution is a bounded descriptive mechanism: it shows how developers are externalizing context, not whether the resulting context improves outcomes. Because the full corpus was coded through repeated LLM labeling with majority vote, the reported category frequencies should be read as measured distributions within this cleaned dataset, not as exact ground truth or causal evidence.

## Limits

- The study is descriptive, not outcome-evaluative; it does not show whether these context patterns improve assistant quality, reliability, or project performance.
- Representativeness is bounded by the cleaning pipeline and by the fact that only repositories with cursor rules entered the analysis.
- The five-theme taxonomy is supported within this corpus, but the evidence provided here does not prove it is exhaustive beyond the sampled ecosystem.
- Coding reliability is good enough to inform synthesis but not strong enough to erase uncertainty: LLM-human agreement is only moderate, some line-level disagreement remained unresolved, and the “No Code” rate is explicitly a lower bound.
- Heavy duplication means repeated wording may disproportionately shape the measured thematic landscape.
- File size and prevalence show that developers are investing in context infrastructure, but the evidence here does not establish the optimal amount, format, or mix of context for real assistant performance.
