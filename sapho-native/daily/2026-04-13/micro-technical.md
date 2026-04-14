# Technical Executive Report

## Top-Line Judgments

- Selective memory management should be treated as a primary systems design choice, because write-time gating changed outcomes far more than downstream retrieval over an undifferentiated store.
- Aggressive admission control can improve both precision and operational focus: a 12-14 object active set achieved perfect reported task accuracy while ungated retrieval degraded badly under distractor load.
- Archival retention with lineage resolves a key tradeoff by keeping superseded or prior-state knowledge accessible without allowing stale material to dominate current retrieval.
- For Sapho, the practical implication is stricter active-memory boundaries, explicit supersession handling, and fail-closed admission rather than permissive accumulation.

## Daily Narrative

Today’s signal is narrow but important: memory quality appears to be determined upstream, at admission time, not merely downstream at retrieval time. The reported result is stark. A write-time salience gate kept the active memory set extremely small, at 12-14 objects, yet reached 100.0% ± 0.0% accuracy. By contrast, ungated retrieval from a larger mixed store fell to 13.3% ± 4.7%. That gap suggests distractor pressure is not a marginal inconvenience but a dominant failure mode.

The article also argues that stronger gating does not require destructive forgetting. Hierarchical archiving with lineage preserved access to prior states that overwrite-based memory lost. That matters because systems need both present-tense relevance and historical accountability. If old material remains fully active, it pollutes retrieval; if it is simply overwritten, temporal truth disappears. Archive-plus-lineage offers a middle path: remove stale material from the active surface while preserving traceable access to what changed and when.

For Sapho, the implication is architectural, not cosmetic. Active memory should stay intentionally narrow. Admission should be explicit and conservative. Superseded material should not linger as a coequal retrieval candidate, but neither should it vanish without record. The evidence base here is only one article, so the claim should remain bounded. Still, the mechanism is clear enough to support a disciplined design preference: fail closed on active-memory admission, preserve displaced knowledge in archive, and make lineage first-class.

## Article Ledger

# Technical Executive Report

## Top-Line Judgments

- Selective memory management should be treated as a primary systems design choice, because write-time gating changed outcomes far more than downstream retrieval over an undifferentiated store.
- Aggressive admission control can improve both precision and operational focus: a 12-14 object active set achieved perfect reported task accuracy while ungated retrieval degraded badly under distractor load.
- Archival retention with lineage resolves a key tradeoff by keeping superseded or prior-state knowledge accessible without allowing stale material to dominate current retrieval.
- For Sapho, the practical implication is stricter active-memory boundaries, explicit supersession handling, and fail-closed admission rather than permissive accumulation.

## Daily Narrative

Today’s signal is narrow but important: memory quality appears to be determined upstream, at admission time, not merely downstream at retrieval time. The reported result is stark. A write-time salience gate kept the active memory set extremely small, at 12-14 objects, yet reached 100.0% ± 0.0% accuracy. By contrast, ungated retrieval from a larger mixed store fell to 13.3% ± 4.7%. That gap suggests distractor pressure is not a marginal inconvenience but a dominant failure mode.

The article also argues that stronger gating does not require destructive forgetting. Hierarchical archiving with lineage preserved access to prior states that overwrite-based memory lost. That matters because systems need both present-tense relevance and historical accountability. If old material remains fully active, it pollutes retrieval; if it is simply overwritten, temporal truth disappears. Archive-plus-lineage offers a middle path: remove stale material from the active surface while preserving traceable access to what changed and when.

For Sapho, the implication is architectural, not cosmetic. Active memory should stay intentionally narrow. Admission should be explicit and conservative. Superseded material should not linger as a coequal retrieval candidate, but neither should it vanish without record. The evidence base here is only one article, so the claim should remain bounded. Still, the mechanism is clear enough to support a disciplined design preference: fail closed on active-memory admission, preserve displaced knowledge in archive, and make lineage first-class.

## Article Ledger

- Selective Memory for Artificial Intelligence: Write-Time Gating with Hierarchical Archiving: Write-time salience gating reduced the active set to 12-14 objects and achieved 100.0% ± 0.0% accuracy versus 13.3% ± 4.7% for ungated retrieval, while archive-plus-lineage preserved prior-state queries that overwrite-based memory lost, making the case that memory quality depends first on admission discipline and explicit historical retention.
