# Queue Item Processing — art-2026-03-13-040

## Source metadata
- URL: https://arxiv.org/html/2509.16941
- Source type: firehose-brave
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-13T10:02:20Z
- Finalized at (UTC): 2026-03-13T20:05:57Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-040.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-040.txt`

## Core thesis
Existing coding agents that perform strongly on prior benchmarks still struggle on contamination-resistant, multi-file, enterprise-relevant issue-resolution tasks.

## Mechanism summary
SWE-Bench Pro introduces a human-augmented benchmark with 1,865 problems across public, commercial, and held-out splits drawn from 41 repositories, combining reproducible containerized environments, reviewed fail2pass and pass2pass tests, and augmented task specifications under a unified SWE-Agent scaffold. The benchmark filters out trivial edits and yields reference solutions averaging 107.4 lines across 4.1 files. Reported results show public-set resolve rates remain below 45%, with Claude Sonnet 4.5 at 43.6% and OpenAI GPT-5 (high) at 41.8%, while commercial-set performance drops further, with the top reported score at 17.8% and other leading models below that level.

## Why it matters for Sapho
This matters because it tightens the benchmark around the conditions that matter for professional software work: larger multi-file changes, contamination resistance, and harder enterprise-like codebases. Its significance is that strong performance on earlier public benchmarks does not imply readiness for real commercial development settings, and the large gap between public and commercial subsets suggests current agents are still materially limited when tasks become more realistic, private, and long-horizon.

<!-- canonical-empirical-findings -->

## Empirical Findings (Data Snapshot)

| Novel finding | Quantitative result | Experimental setup/sample | Metric/outcome | Caveat/limit |
|---|---|---|---|---|
| SWE-Bench Pro is structured to combine scale, diversity, and contamination resistance through three access-controlled subsets. | The benchmark contains 1,865 problems from 41 repositories: public 731 problems (11 repositories), commercial 276 problems (18 repositories), and held-out 858 problems (12 repositories). | Problems are sourced from actively maintained repositories, with public and held-out drawn from copyleft-licensed repos and commercial tasks drawn from private startup codebases. | The split design supports open benchmarking while reserving private data for overfitting checks and enterprise realism. | Underlying codebases for commercial and held-out subsets are not publicly accessible. |
| Task construction explicitly filters out trivial edits and yields substantially larger multi-file changes. | Reference solutions average 107.4 lines of code across 4.1 files; every problem has at least 10 lines of change; more than 100 tasks require over 100 lines of modification. | During curation, trivial edits (1–10 LOC) are excluded and tasks are retained for substantial, multi-file modifications. | The resulting instances are positioned as long-horizon and industrially realistic compared with simpler issue-fix tasks. | Complexity statistics describe benchmark reference patches, not model-generated patches. |
| Under a unified scaffold and non-ambiguous task specification, frontier model performance on the public set remains below 45%. | Public set (N=731) resolve rates: Claude Sonnet 4.5 = 43.6%, Claude Sonnet 4 = 42.7%, OpenAI GPT-5 (high) = 41.8%, Claude Haiku 4.5 = 39.5%, Kimi K2 Instruct = 27.7%, OpenAI GPT-OSS 120B = 16.2%. | Models are evaluated with SWE-Agent, up to 50 turns, with augmented prompt fields (problem statement, requirements, interface) provided. | Even leading models do not surpass the mid-40% range on this benchmark’s public split. | Results are scaffold- and setting-dependent (SWE-Agent prompting and tool-use configuration). |
| Performance drops sharply on the commercial subset, indicating materially harder enterprise codebase conditions. | Commercial set (N=276) resolve rates: Claude Opus 4.1 = 17.8%, OpenAI GPT-5 (high) = 15.7%, OpenAI GPT-5 (medium) = 14.9%, Gemini 2.5 Pro Preview = 10.1%, Claude Sonnet 4 = 9.1%, OpenAI GPT-4o = 3.6%. | Commercial problems are sourced from startup repositories and evaluated with the same benchmark framework while codebases remain private. | Best commercial-set performance is below 20%, substantially lower than public-set top scores. | Commercial instances are private, so independent external reproduction on raw tasks is constrained. |

## Confidence
high

Justification: The source is a primary arXiv benchmark paper with explicit split design, large benchmark scale, reproducible evaluation setup, and clear reported model results across public and commercial subsets. Confidence is high because the evidence is directly quantitative and benchmark-specific, with the main caveat being that commercial and held-out subsets are private, which limits independent reproduction on the raw underlying tasks.
