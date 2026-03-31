# Parallel Sapho

This is a clean parallel rebuild of Sapho Chapterhouse Institute.

It does not salvage the old runtime.
It does not read from the old queue, old site, or old feed surfaces.
It starts from the charter and rebuilds the daily institute lane from first principles.

## Core rules

- Markdown is the only canonical internal format.
- YAML frontmatter is the only structured handoff format.
- Python does transport, capture, lint, scheduling, and publishing only.
- Agent personas do the reasoning work.
- The old runtime stays untouched.
- The default local backend is one fast isolated agent runtime; role identity lives in the persona prompt, not in a legacy backend binding.

## Daily lane

The daily lane is:

1. Intake ticket enters the queue.
2. Source is captured once into markdown.
3. Curator decides whether the article is institute-worthy.
4. Extractor emits atomic evidence files.
5. Synthesist emits atomic claim files and the canonical article artifact.
6. PM Daily Synthesist writes the day's Daily package.
7. Conclave passes, blocks, or withdraws the package.
8. Publish receipt and public surfaces are rendered deterministically.

## Tree

- `spec/` charter-derived operational spec
- `personas/` live prompt templates
- `fixtures/` eval packs
- `queue/` one markdown intake ticket per item
- `articles/` one folder per article
- `daily/` one folder per UTC day
- `public/site/` parallel site and feeds
- `scripts/` thin launchers and renderers

## Canonical artifacts

- Intake ticket
- Source capture
- Curator receipt
- Extractor receipt
- Atomic evidence files
- Atomic claim files
- Canonical article artifact
- Daily package
- Conclave dossier
- Publish receipt
- Heartbeat note

## Non-goals

- No JSON contracts.
- No shared queue ledgers.
- No issue manifests.
- No compatibility layer for the old runtime.
