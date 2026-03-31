# Fixture Packs

Canonical evaluation data is organized by `persona + job`:

- `curator/admission`
- `extractor/evidence`
- `synthesist/article`
- `synthesist/daily`
- `conclave/gate`

Each canonical pack contains ten cases.

The legacy flat packs still exist as compatibility data for the current harness, but they are not the canonical layout anymore. The `synthesist-article` and `synthesist-daily` names are retired compatibility aliases, not separate personas.

Current loaders still point at the legacy flat roots, so they will need a path update to read the canonical persona/job tree.

The Daily certification scope for this refactor is intentionally narrow:

- `Curator` handles admission
- `Extractor` handles evidence
- `Synthesist` handles both article and Daily jobs
- `Conclave` remains the gate

`piter-heartbeat` is intentionally left out of this refactor.
