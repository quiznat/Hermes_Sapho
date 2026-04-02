# SWE-agent: Agent-Computer Interfaces Unlock Automated Software Engineering

## Core Thesis

SWE-agent argues that autonomous software engineering depends not just on stronger language models but on a purpose-built agent-computer interface. By redesigning the commands, feedback, and guardrails around coding work, the paper shows that interface design itself is a major performance lever for software-engineering agents.

## Why It Matters

The paper shifts the center of gravity from raw model capability to execution environment design. That matters because it suggests there is a tractable systems path to better coding agents: improve how models search repositories, edit files, and receive structured feedback, rather than waiting only for bigger models.

## Key Findings

- With GPT-4 Turbo as the base model, SWE-agent resolves 12.47% of the full 2,294-task SWE-bench test set, substantially above the paper's cited non-interactive baseline.
- On the 300-task SWE-bench Lite split, the paper reports a 10.7 percentage point gain over a baseline agent that uses the default Linux shell without the custom interface.
- The interface transfer is not limited to one model family: the paper reports that a Claude 3 Opus variant still solves 10.5% of benchmark tasks.
- The paper also reports strong HumanEvalFix results, supporting the claim that the agent-computer interface improves short-horizon debugging as well as broader repository work.

## Limits

This is still a benchmark paper, not proof of reliable general-purpose autonomous software engineering in production. Absolute solve rates remain low, costs are meaningful, and the system's gains depend on a carefully designed interface and evaluation setup rather than a turnkey ability to handle arbitrary engineering work.
