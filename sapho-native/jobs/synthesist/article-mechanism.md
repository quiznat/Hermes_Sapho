# Synthesist Article Mechanism Review Job

Current job:
review one article package for mechanism law.

Echo the exact `article_id` from Mission context unchanged.
Do not invent causal explanations.
A claim may pass either by carrying a real mechanism explanation or by carrying explicit bounds saying mechanism is still unknown or limited.
If the material supports only bounded non-mechanistic claims, state those bounds plainly.

Work only from the mission context:
- source title/url
- findings
- facts
- article draft

Return YAML only.
Do not return markdown.
Do not return JSON.

Required shape:

```yaml
summary: <one short plain-English summary>
review_confidence: low|medium|high
mechanisms:
  - claim_text: <claim text or short claim paraphrase>
    mechanism_text: <causal explanation>
    bounds: <remaining limit or explicit bound>
    confidence: low|medium|high
bounded_claims:
  - claim_text: <claim text or short claim paraphrase>
    bounds: <explicit bound showing mechanism is still uncertain>
```

If no explicit mechanism explanations are justified but claims are still properly bounded, `mechanisms` may be empty and `bounded_claims` should carry the relevant bounds.
