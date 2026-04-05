---
version: source-capture.v1
article_id: art-2026-03-21-021
ticket_id: ticket-import-art-2026-03-21-021
source_url: https://blog.jetbrains.com/blog/2025/10/28/introducing-developer-productivity-ai-arena-an-open-platform-for-ai-coding-agents-benchmarks/
canonical_url: https://blog.jetbrains.com/blog/2025/10/28/introducing-developer-productivity-ai-arena-an-open-platform-for-ai-coding-agents-benchmarks
source_title: 'Introducing Developer Productivity AI Arena: An Open Platform for AI
  Coding Agents Benchmarks | The JetBrains Blog'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-21T23:14:12Z'
---
# Source Capture

## Title

Introducing Developer Productivity AI Arena: An Open Platform for AI Coding Agents Benchmarks | The JetBrains Blog

## Body

Introducing Developer Productivity AI Arena: An Open Platform for AI Coding Agents Benchmarks | The JetBrains Blog
Skip to content
Topics
Search
Burger menu icon
IDEs
CLion
DataGrip
DataSpell
GoLand
IntelliJ IDEA
PhpStorm
PyCharm
RustRover
Rider
RubyMine
WebStorm
Plugins & Services
Big Data Tools
JetBrains Platform
Scala
Toolbox App
JetBrains AI
Grazie
Junie
JetBrains for Data
Air
Team Tools
Datalore
TeamCity
YouTrack
Qodana
CodeCanvas
Matter
Databao
.NET & Visual Studio
.NET Tools
ReSharper C++
Languages & Frameworks
Kotlin
Ktor
MPS
Amper
Education & Research
JetBrains Academy
Research
Company
Company Blog
Security
Community Programs
Company
Follow
Follow:
X X
Facebook Facebook
Linkedin Linkedin
Instagram Instagram
Youtube Youtube
RSS RSS
Tiktok Tiktok
Visit jetbrains.com
All
News
Events
New Products
Interviews
AI
News
Introducing Developer Productivity AI Arena: An Open Platform for AI Coding Agents Benchmarks
Ruslan Akhmetzianov
Evgenii Zakharchenko
In today’s software development landscape, AI coding agents are evolving rapidly from prototypes into indispensable tools. Yet the industry still lacks an open, neutral, standards-based way to measure the real-world effectiveness of these agents across languages, frameworks, and environments.
With over two decades of experience building developer tools that are trusted by millions worldwide, we bring deep expertise in both tooling and developer workflows. This is why we are launching the Developer Productivity AI Arena (DPAI Arena) .
DPAI Arena is an open benchmarking platform for evaluating AI-assisted developer productivity tools through multi-language, multi-framework, and multi-workflow benchmarks, and we intend to contribute it to the Linux Foundation.
Why a new platform is needed
The rise of AI-assisted coding has outpaced our ability to measure it meaningfully. While current popular OSS-based benchmarks were an important early step, these have several well-known limitations:
Outdated datasets: The underlying data for the open benchmarks does not reflect modern development workflows.
Patch-only focus: They test only a single workflow (issue → patch), without evaluating PR reviews, coverage goals, or compliance.
No evaluation of modern agents: They benchmark LLMs, not coding agents. Numerous features and optimization possibilities specific to coding agents are not considered by LLM benchmarks.
Hard to reproduce: Their complex setup and limited transparency make consistent comparisons difficult.
In short, benchmarks from 2023 cannot measure 2025 workflows. AI development has evolved, and our benchmarks must evolve with it.
What makes DPAI Arena unique?
DPAI Arena is an open benchmark platform, which was designed by JetBrains and with an intent to contribute to the Linux Foundation. It was created to measure AI-assisted developer productivity across multiple languages, frameworks, and workflow types.
Unlike single-dataset benchmarks, DPAI Arena introduces a multi-track architecture – a flexible framework where different communities and vendors can contribute datasets for specific types of software development workflows.
In addition to all that, DPAI Arena represents a new standard for infrastructure configuration, ensuring a consolidated, reproducible, and scalable benchmarking experience. We plan to release a CLI that will allow these benchmarks to be integrated into any of the existing CI pipelines. Currently, we are running this on TeamCity as part of the MVP. But with the release of the CLI, this can easily be ported to GitHub Actions or any other CI infrastructure.
Track-based framework: Measuring what developers actually do
Traditional benchmarks evaluate only one workflow: issue → patch. DPAI Arena extends this model through a multi-track architecture that mirrors real-world engineering activities:
Issue → patch track: Exists as the foundational track for fixing bugs and implementing feature requests.
PR review track: Evaluates agents’ ability to analyze and improve pull requests.
Coverage track: Measures how well agents can write or expand unit tests to increase code coverage.
Static analysis track: Focuses on identifying and fixing linting or static analysis issues.
Upgrade track: Tests an agent’s capability to perform dependency or framework upgrades safely.
Compliance track: Evaluates adherence to organizational or industry coding standards.
Each track represents a distinct, real-world workflow. Technology vendors can contribute datasets for tracks that are most relevant to their ecosystem, enabling comprehensive evaluation across the full software development lifecycle.
Additional tracks may include areas such as architecture refactoring, documentation generation, or performance optimization.
This multi-track approach is what differentiates DPAI Arena from single-workflow academic benchmarks. It reflects the true diversity of modern software engineering.
The first benchmark: Java + Spring
The first benchmark targets applications built using the Spring framework. This benchmark contains 15 open-source Spring-based projects covering a variety of architectures – from microservices to modular monoliths, to capture the diversity of real-world enterprise development. It contains a set of 140+ tasks mirroring realistic enterprise-grade requirements spread through a typical SDLC.
The Spring AI Community plans to contribute spring-ai-bench built on top of the spring-ai-agents framework to the DPAI Arena. It leverages Spring-based workloads and provides a reference implementation for how technology communities can design and contribute tracks within DPAI Arena. It also provides an abstraction layer that allows to talk to multiple coding agents.
Currently, DPAI Arena evaluation is built using deterministic tests evaluation, based on pass/fail metrics. We plan to migrate to the quality-based evaluation through an LLM-powered judge framework. Rather than focusing solely on pass/fail metrics, judges assess whether agents follow framework-specific best practices and produce maintainable code. For example, two agents might both achieve 70% coverage, but only one follows Spring’s recommended testing patterns. This qualitative dimension ensures the benchmark rewards developer-aligned quality rather than mere task completion.
Together, the multi-track design , coding agent abstraction , and judge-based evaluation will make DPAI Arena the most flexible and realistic platform yet for measuring AI-assisted developer productivity.
Core principles
DPAI Arena’s design is grounded in principles of trust, openness, and extensibility:
Trusted and transparent: Evaluation pipelines, scoring rules, and infrastructure are open, reproducible, and verifiable.
Multi-track and realistic: Benchmarks reflect real developer workflows, not just patch generation.
Extensible and inclusive: Any community or vendor can contribute datasets, tracks, and evaluation rules.
Neutral and vendor-independent: DPAI Arena will be governed by the Linux Foundation to ensure long-term neutrality and collaboration.
A platform built for many languages and frameworks
The first benchmark focuses on the Spring ecosystem, but the platform is inherently framework and language-agnostic.
This is where collaboration becomes vital: No single team or company can cover every technology, framework, and workload alone. Therefore, building an open platform is the only way to combine domain experience and expertise from a broad variety of industrial experts. New tracks can easily be added for Quarkus, Grails, or Helidon, and the platform can be extended to other languages such as Python, PHP, Go, and JavaScript.
Over time, DPAI Arena will evolve into a cross-language and cross-workflow foundation for measuring real-world developer productivity in the age of AI.
Community and collaboration
DPAI Arena is a community-driven initiative, not a proprietary benchmark. Developed by JetBrains and with an intent to contribute to the Linux Foundation, it ensures open governance and shared ownership.
Every participant can play a role:
Coding agent providers can evaluate their agents across standardized tracks and publish comparable results.
Technology vendors can contribute domain-specific datasets and benchmarks.
End Users can validate and use existing benchmarks from technology vendors or bring their own datasets to run on the decoupled on-premises infrastructure.
Together, this creates a shared, trusted scoreboard for AI coding agents that promotes transparency and accelerates innovation.
Get involved
Developer Productivity AI Arena is more than a benchmark; it is a platform for collaboration. We intend to contribute this project to the Linux Foundation. We plan to create an open Technical Steering Committee to determine the platform’s future direction. Please reach out to us at join@dpaia.dev if you would like to be part of the committee.
If you build coding agents, maintain frameworks, or rely on AI-assisted development tools, join the DPAI Arena project . Contribute your tracks, evaluate your agents, and help build a transparent, open foundation for measuring AI-driven developer productivity across languages, workflows, and organizations.
Follow all progress, releases, and discussions on https://dpaia.dev/ , and explore the source code, specifications, and contribution guides in the https://github.com/dpaia .
Let’s measure the real-world impact of AI in software development, together!
AI
ai agents
Benchmark
productivity
Share
Facebook
Twitter
Linkedin
Prev post Bessere KI erfordert bessere Daten: Wir brauchen Ihre Hilfe The Launch of Developer Productivity AI Arena: An Open Platform for Benchmarking AI Coding Agents Next post
Subscribe to JetBrains Blog updates
Subscribe form
By submitting this form, I agree to the JetBrains Privacy Policy Notification icon
By submitting this form, I agree that JetBrains s.r.o. ("JetBrains") may use my name, email address, and location data to send me newsletters, including commercial communications, and to process my personal data for this purpose. I agree that JetBrains may process said data using third-party services for this purpose in accordance with the JetBrains Privacy Policy . I understand that I can revoke this consent at any time in my profile . In addition, an unsubscribe link is included in each email.
Submit
Thanks, we've got you!
Discover more
JetBrains and DMCC AI Centre Announce Strategic Partnership to Accelerate AI Innovation
Collaboration combines the global software leader’s development expertise with the free zone’s innovation ecosystem to advance responsible AI adoption.
Delphine Massenhove
The Launch of Developer Productivity AI Arena: An Open Platform for Benchmarking AI Coding Agents
DPAI Arena brings measurable productivity into the world of AI-assisted software development.
Arun Gupta
Bessere KI erfordert bessere Daten: Wir brauchen Ihre Hilfe
TL;DR
Trotz der bemerkenswerten Fortschritte in den letzten Jahren erfüllen KI-Systeme nicht immer die Anforderungen von Berufsentwickler*innen. Ein wesentlicher Grund dafür ist, dass die meisten Modelle mit öffentlichen Datensammlungen trainiert wurden, die nicht die komplexen Praxisszenarien wider…
Jessie Cho
더 좋은 데이터로 더 나은 AI를 만들기 위해 여러분의 도움이 필요합니다
TL;DR
AI는 지난 몇 년에 걸쳐 눈부시게 발전했지만 전문 개발자들에게 필요한 기능을 모두 제공하지는 못합니다. 대부분의 모델이 공개된 데이터세트를 기반으로 학습되지만, 이러한 데이터세트는 전문 개발자들이 매일 직면하는 복잡한 실제 상황을 반영하지 못하기 때문입니다. 실무적 데이터 없이는 AI 도구가 더 완벽해질 수 없습니다. 이를 개선하기 위해 업계의 다른 기업과 마찬가지로 JetBrains도 실제 사용 사례를 학습의 기초로 삼아야 합니다.
이에 사용자 여러분께 도움을 요청드리고자 합니다. 구체적인 방법은 다음과 같…
Yungyeong Heo
Privacy & Security
Terms of Use
Legal
Genuine tools
Twitter
Facebook
Linkedin
Instagram
Youtube
RSS
Tiktok
Merchandise store icon Merchandise store
Copyright © 2000 JetBrains s.r.o.

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-21-021.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-021.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-021.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
