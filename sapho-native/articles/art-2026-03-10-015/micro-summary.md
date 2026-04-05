# SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

## Core Thesis

SWE-Bench Pro argues that current agent evaluation has been too concentrated on lighter bug-fix settings and introduces a larger benchmark aimed at materially longer-horizon software engineering work: 1,865 problems from 41 actively maintained repositories, with tasks that often span multiple files, require nontrivial patch sizes, and still yield low reported solve rates even for top models.

## Why It Matters for Sapho

This matters because it sharpens a doctrine Sapho should already be moving toward: strong performance on public coding benchmarks does not yet justify broad confidence in autonomous long-horizon engineering. The paper contributes not just another scorecard, but a benchmark design and result pattern that make three points legible at once: longer-horizon tasks are structurally harder, unreleased evaluation slices matter if overfitting is a concern, and even frontier agents remain far from reliable on realistic multi-file repository work. For Sapho, that supports stricter skepticism toward smooth “AI engineer” narratives and stronger emphasis on benchmark construction, split design, and failure-mode visibility.

## Key Findings

- The benchmark contains 1,865 problems drawn from 41 actively maintained repositories, making it substantially larger than a toy or single-repo evaluation frame.
- SWE-Bench Pro is split into 11 public repositories, 12 held-out repositories, and 18 proprietary commercial repositories, with 731 public instances released, 858 held-out problems retained for future overfitting checks, and 276 commercial problems kept private while aggregate results are still reported.
- The tasks are explicitly framed as long-horizon engineering work that may take professional software engineers hours to days rather than minutes.
- Typical solution scope is materially extended: reference solutions average 107.4 lines of code across 4.1 files.
- Every task requires at least 10 lines of change, and more than 100 tasks require over 100 lines of modification, reinforcing that this is not just a thin benchmark of tiny edits.
- Reported agent performance remains low overall, and the best commercial-set result is lower than the best public-set result: 23.3% on the public set versus 17.8% on the commercial set.
- The paper also exposes concrete failure modes rather than treating failure as a single bucket: for one model, wrong solutions account for 35.9% of failures and syntax errors for 24.2%; for another, context overflow accounts for 35.6% and endless file reading for 17.0%.

## Evidence and Findings

- The paper establishes scale and composition directly: 1,865 problems across 41 actively maintained repositories. That supports the conclusion that this is a deliberately broad benchmark build rather than a narrow demo set, which matters because claims about agent competence become more credible when they are tested across many live repositories instead of a small curated slice.
- The split design is central to the benchmark’s argument: 731 public instances are released, 858 held-out problems are reserved for future overfitting checks, and 276 commercial problems remain private while reported publicly in aggregate. That supports the conclusion that the benchmark is trying to preserve harder-to-game evaluation surfaces, which matters because public-only benchmarks are vulnerable to saturation, memorization, and benchmark-specific optimization.
- The benchmark’s “long-horizon” label is backed by task properties, not just rhetoric: tasks may take engineers hours to days, reference solutions average 107.4 lines across 4.1 files, every task requires at least 10 changed lines, and more than 100 tasks require over 100 lines of modification. That supports the conclusion that SWE-Bench Pro is targeting materially extended repository work, which matters because many optimistic agent narratives still rest on much smaller edit regimes.
- Reported performance remains weak even at the frontier. The top public-set resolve rate is 23.3%, while the top commercial-set resolve rate is 17.8%. That supports the conclusion that current agents solve only a minority of these tasks and perform worse on the commercial slice, which matters because benchmarked competence is still far from operational reliability in harder or less exposed codebases.
- The evaluation stack itself includes controls for instability: each test set is run three times and tests that do not pass consistently are filtered out. That supports the conclusion that the authors are actively bounding test flakiness rather than ignoring it, which matters because unreliable harnesses can inflate both false success and false failure and distort the meaning of benchmark scores.
- The failure analysis adds operational detail beyond headline percentages. One model’s failures skew toward wrong solutions and syntax errors, while another loses heavily to context overflow and endless file reading. That supports the conclusion that agent limits are not just about “reasoning quality” in the abstract but also about workflow control, context management, and code-edit execution discipline, which matters for any serious evaluation doctrine.

## Contradictions and Tensions

- The benchmark is explicitly designed to limit overfitting by keeping held-out and commercial subsets private, but that same privacy creates an inspection asymmetry: outside users can see results on unreleased tasks without being able to directly audit the underlying instances. That improves benchmark control while weakening external interpretability.
- The benchmark argues for broader realism, yet its own language coverage remains limited, with Java, C++, and Rust underrepresented. That means the benchmark can support claims about harder long-horizon engineering within its sampled distribution, but not strong claims about software engineering in general.
- The commercial split appears harder than the public split on reported top-line results, but the mechanism is not pinned down. The gap could reflect repository type, task mix, private-set difficulty, or enterprise-code characteristics; the score difference alone does not isolate which factor is doing the work.
- The paper tries to reduce harness instability by running tests three times and filtering inconsistent tests, which is sensible, but it also reveals that raw evaluation conditions are unstable enough to need correction. That is a strength in transparency and a reminder that benchmark scores remain partly contingent on harness curation.

## Mechanism or Bounds

The strongest supported mechanism is structural rather than causal: harder performance appears to arise from tasks that demand larger, multi-file, longer-duration edits inside repository-specific environments, combined with agent failure modes that reflect practical execution limits such as context overflow, endless file reading, syntax breakage, and incorrect patches. The benchmark’s private/public partitioning plausibly helps preserve harder-to-game evaluation surfaces by separating released tasks from unreleased reporting sets, but the paper does not demonstrate that this fully prevents leakage or benchmark gaming. More broadly, the evidence supports a bounded claim about this benchmark’s task distribution and observed performance patterns, not a universal claim about all software engineering work.

## Limits

The paper supports strong claims about benchmark construction and weak-to-moderate claims about broader field capability.
The public-versus-commercial performance gap is real in the reported results, but its cause is not identified cleanly.
Private held-out and commercial subsets improve anti-overfitting posture but reduce outside auditability.
Language coverage is incomplete, with underrepresentation in major languages that matter for real-world engineering.
Task difficulty is supported by task properties and low solve rates, but not by a direct head-to-head comparison against every competing benchmark class.
Even the evaluation pipeline shows bounded instability, since inconsistent tests had to be filtered before final use.
