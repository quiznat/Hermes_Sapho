# Historical Remediation Playbook

## Operating pattern
- Process `legacy_quarantined` articles in explicit small batches.
- Commit each successful slice promptly.
- Include GitHub links for commit, remediation report, article package, article, validation, and policy surfaces in operator-facing updates.

## Durable implementation facts
- Main runner: `scripts/remediate_historical_imports.py`
- Reports live under `sapho-native/state/reports/`
- Task-run receipts live under `sapho-native/state/receipts/task-runs/`

## Replay/debugging findings worth preserving
1. Large Hermes argv payloads should use temp-file prompt transport rather than oversized CLI arguments.
2. Extractor evidence prompts should emit evidence blocks first and declare `evidence_count` last to avoid count mismatches.
3. Use small explicit batches rather than widening carelessly when replay/path quality is still being hardened.

## Note
- Procedural details like this should generally live in skills or vault notes, not active memory.
