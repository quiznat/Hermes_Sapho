# When AGENTS.md Backfires: What a New Study Says About Context Files and Coding Agents

## Core Thesis

A February 2026 study by ETH Zurich researchers delivers an unexpected verdict on AGENTS.md: LLM-generated context files harm task success rates while driving up inference costs by 20%, challenging the rationale behind a format that has proliferated to over 60,000 public repositories since OpenAI introduced it in mid-2025.

## Why It Matters

Developers adopted AGENTS.md to escape the burden of maintaining parallel configuration artifacts, and the format quickly became a de facto standard—evidenced by 88 files in OpenAI's monorepo alone. This empirical evaluation questions whether widespread adoption outpaced validation, suggesting that machine-readable convenience may trade away performance developers assumed they were gaining.

## Key Findings

- LLM-generated context files reduce task success rates compared to handling configuration without them
- Inference costs increase by 20% when these automated context files are used
- AGENTS.md spread rapidly after OpenAI launched Codex in mid-2025, yet the empirical record now undercuts its core value proposition

## Limits

This synthesis draws from a partial excerpt; the full methodology, detailed results, and additional researcher caveats from the original ETH Zurich paper may qualify or extend these conclusions.
