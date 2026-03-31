# Daily Lane Spec

## Purpose

Convert newly admitted signal into Daily Dose judgment under charter law.

## Flow

1. Intake ticket is created.
2. Source capture writes one source markdown file.
3. Curator performs the admission job and writes one markdown receipt.
4. If discarded, the article stops.
5. If kept, Extractor performs the evidence job and writes one receipt plus atomic evidence files.
6. Synthesist performs the article-claims job and writes atomic claim files plus one claims receipt.
7. Synthesist performs the article-write job and writes the canonical article artifact from approved claims plus compact context.
8. Synthesist performs the daily-synthesis job and writes the Daily package for all articles minted for the selected replay date.
9. Conclave performs the Daily gate and writes a law-by-law dossier.
10. Publish receipt is written deterministically.
11. Archive pages, Daily pages, and feeds are rendered deterministically.

## Escalations

- Mechanist may be invoked when mechanism is weak.
- Adversary may be invoked when contradiction pressure is needed.
- Piter may throttle intake or cadence when pressure threatens quality law.

## Hard rules

- No job may skip Conclave.
- No downstream role may invent missing upstream artifacts.
- No job may redefine a persona.
- No gate may be modeled as a persona.
- No role may write JSON.
- No role may rely on the old runtime.
- No publication surface may be updated without a Conclave pass.
- Replay runs must be date-addressable through an explicit replay-date control rather than manual metadata edits.
