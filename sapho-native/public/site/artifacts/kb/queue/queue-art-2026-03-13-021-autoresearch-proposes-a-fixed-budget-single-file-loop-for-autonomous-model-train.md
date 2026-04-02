# Queue Item Processing — art-2026-03-13-021

## Source metadata
- URL: https://github.com/karpathy/autoresearch
- Source type: user-direct
- Lane tags: `agent-factory, agent-factory`
- Curated at (UTC): 2026-03-14T02:02:08Z
- Finalized at (UTC): 2026-03-14T02:39:31Z

## Source custody
- Source snapshot: `research/evidence/source-material/2026-03-13/art-2026-03-13-021.json`
- Clean text path: `research/evidence/source-material/2026-03-13/art-2026-03-13-021.txt`

## Core thesis
Autoresearch frames autonomous research as an agent repeatedly modifying a single training file under a fixed five-minute training budget, using validation bits per byte as the comparison metric while humans steer the process through a Markdown instruction file rather than direct code edits.

## Mechanism summary
The README defines a minimal setup with three main files: prepare.py for one-time data preparation and runtime utilities, train.py as the only file the agent edits, and program.md as the human-authored instruction layer. Each run trains for a fixed wall-clock budget, evaluates with val_bpb, and the surrounding workflow is designed for repeated overnight experimentation on a single NVIDIA GPU.

## Why it matters for Sapho
This matters as a concrete practitioner pattern for autonomous research workflows because it narrows the agent’s edit surface, fixes the experimental budget, and makes acceptance criteria explicit through a single validation metric. The design is significant less as proof of superior results than as an operational template for making agent-driven experimentation tractable, auditable, and cheap enough to run repeatedly on modest hardware. It also makes the human role legible: guidance lives in an instruction file, while the agent owns bounded code changes inside a controlled loop.

## Confidence
medium

Justification: The rating is medium because the source is a primary repository README, so the workflow description and stated design choices are directly attributable to the authors. Confidence is limited because the evidence is mostly procedural and aspirational, with no extractable benchmark-style results or comparative performance data demonstrating that the workflow works better than alternatives.
