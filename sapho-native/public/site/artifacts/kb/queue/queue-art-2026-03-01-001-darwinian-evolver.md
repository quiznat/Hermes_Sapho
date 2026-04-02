# Queue Item Processing — art-2026-03-01-001

## Source metadata
- URL: https://imbue.com/research/2026-02-27-darwinian-evolver/
- Source type: article
- Lane tags: `agent-factory`, `agent-research`
- Processed at (UTC): 2026-03-01T19:55:40Z

## Enrichment artifacts consulted
- Primary article: Imbue, *LLM-based Evolution as a Universal Optimizer*
- Repo reference: https://github.com/imbue-ai/darwinian_evolver
- Related project reference: https://github.com/imbue-ai/vet
- Related results post: https://imbue.com/research/2026-02-27-arc-agi-2-evolution/

## Structured extraction

### Core mechanism
The article frames a Darwinian loop for code/prompt optimization where a population of candidate organisms is iteratively sampled, mutated, scored, and re-inserted. The system depends on three interfaces: initial organism, evaluator, and mutator.

### Notable optimization controls
The source emphasizes several concrete levers that matter for production factory workflows:

1. **Weighted parent sampling** with sigmoid-scaled fitness and novelty bonus.
2. **Dynamic percentile midpoint** (instead of fixed midpoint) to keep selection pressure in a useful gradient regime as population quality shifts.
3. **Batch mutations** (mini-batch style failure exposure) for efficiency at some diversity cost.
4. **Post-mutation verification** to reject likely non-improving children before expensive full evaluation.
5. **Learning log / crossover strategies** to spread useful mutations beyond direct lineage.

### Claimed outcomes
The article claims this method materially improved their own agent-verification stack (Vet) and also produced strong ARC-AGI results when adapted to reasoning tasks.

## Factory-lane interpretation
For software-factory systems, this is strong evidence for treating prompt/harness design as a search problem rather than a one-shot engineering artifact. The high-value idea is not just “mutate prompts,” but coupling mutation with explicit fitness contracts and cheap pre-verification gates to keep cost bounded.

## Decision
- Decision: **retain**
- Rationale: high direct relevance to agentic software factory design, concrete algorithmic controls, and transferable operating guidance.
- Confidence: high (primary source + linked implementation artifacts).

## Processing notes
This item should be used as a methodological anchor when comparing Ralph-loop style iterative execution versus population-based optimization in `research/software-factory-variant-memo.md` and the variant matrix.
