# Synthesist Article Contradiction Review Job

Current job:
review one article package for contradiction visibility.

Echo the exact `article_id` from Mission context unchanged.
Do not invent contradictions.
Do not smooth away unresolved tension.
If no contradiction is visible in the provided material, say so plainly.
If a tension exists but cannot be resolved, disclose it rather than hiding it.

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
contradictions:
  - contradiction_text: <one concrete tension or contradiction>
    related_claim_texts:
      - <claim or finding text>
    related_fact_refs:
      - fact-001
    disposition: unresolved|bounded|resolved
    disclosure: <what must stay visible>
    confidence: low|medium|high
```

If there are no visible contradictions, return:

```yaml
summary: <one short plain-English summary>
review_confidence: low|medium|high
contradictions: []
```
