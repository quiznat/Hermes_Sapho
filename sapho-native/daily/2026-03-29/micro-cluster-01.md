## Cluster Thesis

Empirical research is displacing speculation in the discourse on AI-assisted software engineering, as studies of real developer behavior and real-world system performance reveal a consistent pattern: skilled practitioners treat AI tools as instruments requiring active configuration and oversight, while the tools themselves exhibit measurable gaps between architectural promise and operational reliability.

## Shared Signals

- Field-grounded methodology replaces synthetic benchmarks and anecdotal claims across all four studies
- Human developers exercise deliberate control through configuration patterns rather than passive acceptance of AI output
- Current AI coding systems display structural failure modes—coordination breakdowns, robustness gaps—not captured by headline accuracy metrics
- The distance between laboratory performance and production-grade software engineering remains significant and understudied

## Article Notes

- Professional Software Developers Don't Vibe, They Control: Experienced developers deploy AI agents with strategic oversight to extend control over codebases, not to surrender authorship to automation.
- Beyond the Prompt: A large-scale analysis of 401 open-source repositories yields the first taxonomy of how developers shape AI behavior through local configuration ("Cursor rules").
- SWE-bench Tests Language Models on Real-World GitHub Issues: A rigorous evaluation framework tests language models on actual bug reports from GitHub, requiring navigation of complex codebases and generation of patches that pass real test suites.
- The Planner-Coder Gap Threatens Multi-Agent Code Generation: Multi-agent code generation systems exhibit a critical robustness gap between planning and execution components, with coordination breakdowns degrading overall performance in ways standard metrics miss.
