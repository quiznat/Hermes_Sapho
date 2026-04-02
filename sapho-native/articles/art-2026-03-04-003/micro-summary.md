# arXiv 2510.21413

## Core Thesis

AI configuration files were still a minority practice in the repositories this study examined, but where they appeared they already showed recognizable structure: adoption remained sparse, TypeScript-heavy projects were most represented, file formats differed materially in size and variability, and AGENTS.md maintenance was usually light, with the more active documents evolving mainly through instruction edits rather than broad rewrites.

## Why It Matters for Sapho

This matters because it pushes Sapho away from treating repository-level AI instructions as a mature, standardized control layer. The study instead suggests an early, uneven governance surface: low visible adoption, tool-scope fragmentation, and document behavior that looks more like targeted operational guidance than stable institutional specification. For Sapho, that means evaluation doctrine should treat these files as useful but partial signals about workflow discipline, not as reliable proxies for full agent governance maturity.

## Key Findings

- Only 466 scanned repositories, or 5%, had at least one of the studied AI configuration file formats, indicating that visible adoption in this measured tool set was still limited.
- That 5% figure is explicitly bounded: the study covered four commercial tools and excluded other ecosystems such as Cline and OpenCode, so it does not measure the whole landscape of AI configuration practice.
- Within repositories that did use these files, TypeScript led with 135 repositories, while Go and Python each appeared in 58 and C# in 56, forming a clear second cluster below TypeScript.
- The language distribution continued with 36 Java, 34 JavaScript, 32 C++, 29 Rust, 19 PHP, and 9 C, showing adoption spread across several mainstream development stacks rather than a single niche.
- The configuration formats differed in size behavior: Copilot instruction files were longest on average at 310 lines, while AGENTS.md averaged 142 lines but had the highest variation, with a standard deviation of 231 lines.
- AGENTS.md often stayed stable after creation: among 155 files, 77 never changed again, 36 changed once, and 32 changed between two and seven times.
- In the higher-activity subset, change was usually narrow rather than comprehensive: 111 of 169 annotated commits, or 66%, involved only one change category, and the most common actions were adding instructions (78 instances) and modifying instructions (59).

## Evidence and Findings

- The study found only 466 adopting repositories out of the scanned set, yielding a 5% adoption rate for the formats it tracked. This supports the conclusion that AI configuration files were not yet a default repository practice in the observed ecosystem, which matters because any governance or quality inference built on their presence will miss most repositories.
- That headline adoption figure is materially bounded by scope: the analysis covered four commercial tools and excluded named alternatives such as Cline and OpenCode. This supports a narrower conclusion than “AI config adoption is 5% overall”; what it actually shows is that adoption of these particular formats was low, which matters because ecosystem fragmentation can make apparent sparsity partly a measurement artifact.
- Among repositories with configuration files, TypeScript appeared in 135 cases, while Go and Python each appeared in 58 and C# in 56. This supports the conclusion that adoption clustered most strongly in TypeScript-heavy development contexts, which matters because any emerging conventions in these files may first reflect the norms of web and application engineering rather than software repositories broadly.
- File-size behavior differed sharply by format: Copilot instruction files averaged 310 lines, while AGENTS.md averaged 142 lines but varied far more, with a standard deviation of 231. This supports the conclusion that these formats are not interchangeable document shells; some appear to invite longer standardized instruction blocks, while AGENTS.md behaves more like a flexible container with highly uneven elaboration.
- AGENTS.md histories suggest low routine churn at the file level: 77 of 155 files never changed after creation, 36 changed once, and 32 changed between two and seven times. This supports the conclusion that many teams treat these files as relatively stable guidance artifacts rather than continuously tuned operational playbooks, which matters because static guidance can age quickly when tooling or workflow changes.
- The closer look at 10 high-activity AGENTS.md files covered 169 commits, representing 37% of the 453 collected commits, and showed that 66% of annotated commits involved only one change category. With add-instruction and modify-instruction actions dominating at 78 and 59 instances, the study supports a bounded conclusion that when active maintenance does occur, it is usually instruction-centric and incremental rather than a broad restructuring of document purpose.

## Contradictions and Tensions

- The strongest tension is between the clean 5% adoption figure and the study’s tool boundary. The result is useful, but it measures only the formats attached to four commercial tools, so the finding can support “low adoption in this defined slice” more confidently than “low adoption of AI configuration files in general.”
- The language counts make TypeScript the clear leader, but they are counts inside the adopting subset, not a baseline-adjusted comparison against GitHub-wide repository language prevalence. That means the observed concentration may reflect broader platform composition as much as a special affinity between TypeScript projects and AI configuration practices.
- AGENTS.md appears simultaneously stable and actively curated depending on the unit of analysis. At the file-history level, many documents barely changed after creation; at the commit-analysis level, the most active files show repeated instruction updates. The tension is that “usually stable” and “frequently edited” are both true, but for different slices of the sample.
- Structural interpretation of AGENTS.md is narrowed by exclusions: the heading analysis removed 15 files created before January 1, 2025 and 5 files with no heading structure. That improves comparability for convention-era, structured documents, but it also means the reported heading patterns do not cleanly describe all AGENTS.md usage.
- The size comparison also carries an interpretive tension: Copilot files were longest on average, but AGENTS.md was far more variable. This suggests format-level differences in how constrained or open-ended the documents are, but the study does not show whether that variation reflects repository complexity, team maturity, or simply inconsistent authoring norms.

## Mechanism or Bounds

The strongest bounded explanation is that these files function as an emerging repository-level instruction layer whose uptake is still selective, fragmented by tool ecosystem, and shaped by document affordances. The evidence supports comparative observations about where the files appear, how large they are, and how AGENTS.md changes over time, but it does not establish why TypeScript repositories lead, why Copilot files are longer on average, or why many AGENTS.md files remain static after creation. The maintenance evidence supports a narrower operational reading: when teams do revisit AGENTS.md in the active subset, they usually refine instructions rather than overhaul multiple governance categories at once. All of these conclusions remain bounded to the studied formats, the sampled repositories, and in some analyses a filtered subset of structured or high-activity files.

## Limits

The study does not provide a full map of AI configuration adoption across all tool ecosystems, so the 5% figure should not be generalized beyond the included formats without caution.
It does not establish causal reasons for language concentration, file length differences, or maintenance behavior.
Several analyses depend on narrowed subsets, including structured AGENTS.md files and a 10-file high-activity sample, so some of the sharper pattern claims rest on concentrated rather than universal evidence.
The evidence is strongest on observed distribution and maintenance patterns, weaker on organizational mechanism, governance quality, or downstream effects on developer or agent behavior.
