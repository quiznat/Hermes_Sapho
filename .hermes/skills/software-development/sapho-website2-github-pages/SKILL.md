---
name: sapho-website2-github-pages
description: Migrate Sapho Website 2.0 to GitHub Pages while preserving the current static site style/layout, keeping the same custom domain, and deferring RSS/feed surfaces until later stabilization.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [sapho, website, github-pages, static-site, custom-domain, rss, deployment]
    project: sapho-native
---

# Sapho Website 2.0 on GitHub Pages

## When to use

Use this in `/home/hermes/sapho-native` when:
- the next Sapho slice is Website 2.0
- hosting is moving from the old Vercel/OpenClaw website path to GitHub Pages
- the public URL should stay the same (for example `research.quiznat.com`)
- the current visual style/layout should carry over
- RSS/feed work should be explicitly deferred until after site stabilization

## Core rule

Do not redesign first.
Treat the current static site as the visual and structural baseline.
The first goal is hosting/runtime migration plus validation cleanup, not a fresh aesthetic system.

## Strong findings from rollout

### 1. The current site is already static-site shaped

The important baseline surfaces were already under:
- `public/site/index.html`
- `public/site/viewer.html`
- `public/site/assets/style.css`

The main renderer was:
- `scripts/render_site.py`

This means the migration is mostly a render/deploy-path cleanup, not a dynamic-site rewrite.

### 2. Keep the same public domain if possible

If the plan is to keep the same public URL and just repoint DNS/CNAME to GitHub Pages:
- leave the canonical site base URL as `https://research.quiznat.com`
- add or preserve a `CNAME` file in the rendered output
- focus on hosting migration, not public URL transition

A good Website 2.0 setup includes env-driven config such as:
- `SAPHO_SITE_MODE=github-pages`
- `SAPHO_SITE_BASE_URL=https://research.quiznat.com`
- `SAPHO_SITE_CUSTOM_DOMAIN=research.quiznat.com`

### 3. RSS/feed surfaces should be removed from launch-critical validation when deferred

A major blocker in the current renderer was feed coupling:
- homepage linked `artifacts.xml`
- render validation required `rss.xml`, `artifacts.xml`, and `daily.xml`

If RSS is intentionally deferred, fail closed in presentation too:
- remove the homepage RSS card
- remove the RSS `<link rel="alternate">` tag from Website 2.0 homepage mode
- stop requiring feed files in Website 2.0 validation mode
- keep feed generation code present if useful, but make it non-required for launch

This prevents false readiness.

### 4. Exact seed equality is too rigid for migration mode

The old renderer used strict checks like:
- homepage must exactly equal seed
- viewer must exactly equal seed
- charter wrapper must exactly equal seed

That is useful for frozen parity, but too rigid for a controlled Website 2.0 migration.

A better approach is to split validation modes:
- `legacy` mode: exact-seed parity checks
- `github-pages` / Website 2.0 mode: structural checks

Good Website 2.0 structural checks:
- homepage still contains institute heading and primary surfaces
- homepage still links charter / archive / kept-links / viewer surfaces
- viewer still contains the markdown-render shell and scripts it needs
- charter wrapper still redirects to the canonical viewer path
- `CNAME` exists and matches the intended domain

### 5. Do not depend on old OpenClaw live-site sync in Website 2.0 mode

The old render/deploy path contained assumptions like:
- default public seed from `/home/openclaw/.openclaw/workspace/website`
- deploy script syncing into the old live website tree
- runtime charter and ops surfaces under `/home/openclaw/...`

For Website 2.0 mode:
- do not require rsync from the old live site tree
- treat the repo’s committed `public/site` baseline as the seed surface
- preserve required baseline files locally, for example:
  - `index.html`
  - `viewer.html`
  - `charter.html`
  - `assets/style.css`
  - `assets/sapho-seal.png`

This makes GitHub Pages rendering reproducible from the repo itself.

### 6. Public ops validation may need to loosen in Website 2.0 mode

A real Website 2.0 render initially failed on:
- `public_ops_checkin_stale`

Cause:
- legacy validation required public ops checkin content to exactly match the runtime checkin under old paths

For Website 2.0 mode, a safer transitional rule is:
- require the public ops surfaces to exist
- validate their pointer structure
- do not require exact byte-for-byte equality with old runtime paths during the migration slice

This allows the website migration to proceed without pretending the old deploy topology is still canonical.

### 7. GitHub Pages cannot point at an arbitrary nested site folder

Important platform limitation discovered in practice:
- GitHub Pages cannot be told to serve an arbitrary nested directory like:
  - `sapho-native/public/site/index.html`
- it only supports:
  - branch root
  - `/docs` on a branch
  - or a GitHub Actions artifact deploy

Practical implication:
- do not tell the operator to "just point Pages at index.html"
- if the site lives under `sapho-native/public/site`, either:
  - deploy with GitHub Actions, or
  - restructure the published output into `/docs`

For this Sapho Website 2.0 path, GitHub Actions is the least disruptive option because it avoids repo-wide restructuring.

### 8. When using a custom workflow, Pages source should be `GitHub Actions`, not `main/root`

A key operational finding from rollout:
- if the repo uses a workflow that renders `sapho-native/public/site` and uploads that folder as the Pages artifact,
- GitHub Pages must be configured with source:
  - `GitHub Actions`
- not:
  - `Deploy from branch: main / root`

If Pages stays on `main/root`, GitHub will try to serve the repository root instead of the rendered site artifact.

### 9. GitHub's suggested static workflow is wrong if it uploads the whole repo

A common trap during Pages setup:
- GitHub may suggest a generic static-content workflow using:
  - `path: '.'`
- that uploads the entire repository, not the actual rendered site

For Sapho Website 2.0 the workflow should instead:
1. install the minimal render dependency (`pyyaml`)
2. run:
   - `python scripts/render_site.py`
   with:
   - `SAPHO_SITE_MODE=github-pages`
   - `SAPHO_SITE_CUSTOM_DOMAIN=research.quiznat.com`
   - `SAPHO_SITE_BASE_URL=https://research.quiznat.com`
3. upload exactly:
   - `sapho-native/public/site`

A good workflow can remain simple, but it must publish the rendered site folder, not the repository root.

### 10. GitHub workflow pushes can fail even when normal git push works

Important deployment gotcha discovered in practice:
- creating/updating `.github/workflows/*.yml` can be rejected by GitHub if the current PAT lacks `workflow` scope
- normal code pushes may still succeed

Observed failure looked like:
- remote rejected workflow update because token lacked `workflow` scope

Good operational response:
- commit and push the Website 2.0 code/render changes separately
- leave the workflow file local if credentials cannot push it
- do not block the whole migration slice on workflow-scope credentials

This is especially useful on headless VPS setups where the agent is pushing through an existing PAT.

### 11. For Website 2.0, the shell carries over — not the old content inventory

A critical correction from real rollout:
- the user wanted the old site's shell/style/layout only
- they explicitly did NOT want the old site's content, daily surfaces, longform surfaces, or old artifact inventory carried over

Approved Website 2.0 surfaces were narrowed to:
- Charter
- kept artifacts

Explicitly not approved for Website 2.0:
- Daily surfaces
- longform surfaces
- RSS/feed surfaces

Operational rule:
- do not lightly edit the old homepage seed and leave its content blocks intact
- in Website 2.0 mode, rebuild the homepage content from scratch while preserving the visual shell

A good Website 2.0 homepage should therefore render only:
- institute hero / shell
- Charter card
- Kept Artifact Index card
- recent kept artifacts pulled from the new lawful corpus

### 12. In Website 2.0 mode, do not merge kept-links with the old payload

A major real-world bug source was this pattern:
- renderer loaded the old `data/kept-links.json`
- inserted new lawful items into it
- kept all the old retained items too
- result: Website 2.0 still showed the old artifact corpus even after the homepage shell was partially fixed

Correct behavior in Website 2.0 mode:
- rebuild kept-links from scratch from the current lawful corpus
- do not merge with the old payload
- set counts (`keptCount`, `decisionedCount`, lane counts) from the rebuilt lawful item set only

This is essential when the old site is only a shell reference and not the content source of truth.

### 13. In Website 2.0 mode, artifact selection must come from the new lawful ready corpus only

Another important rollout finding:
- selecting both `published` and `ready-for-daily` artifacts in Website 2.0 mode can accidentally pull the old already-published corpus back into the new site

Correct Website 2.0 selection rule:
- include only articles where:
  - `publication_status == ready-for-daily`
  - article publication authority verdict is `pass`
- do not include legacy `published` corpus items in Website 2.0 mode just because they were previously public

This keeps Website 2.0 aligned with the new lawful corpus rather than the old public archive.

### 14. If Website 2.0 still looks old, inspect the homepage and kept-links generation path first

Useful debugging lesson from rollout:
- if the rendered site still looks like the old site, the likely causes are:
  1. homepage still being seed-preserved instead of rebuilt
  2. kept-links JSON/cards still merging against old payload data
  3. artifact selection still including old `published` items
  4. browser/CDN cache masking a real fix

A fast verification pattern is:
- render in Website 2.0 mode locally
- inspect `public/site/index.html`
- inspect `public/site/data/kept-links.json`
- confirm:
  - no Daily section
  - no longform section
  - only lawful ready corpus items in kept payload

### 15. Website 2.0 artifact bodies should use the canonical article body, not a simplified public rewrite

A major rollout correction clarified the right artifact surface for Website 2.0:
- do not publish a simplified rewritten public summary format
- do not collapse the article into ad hoc sections like `Source metadata`, `Core thesis`, `Why it matters`, etc. if the canonical article already exists
- public artifact markdown should use the canonical `article.md` body itself, with frontmatter stripped

Correct pattern:
- read `article.md`
- strip frontmatter
- publish the remaining canonical article body as the public artifact body

Why this matters:
- it preserves the actual new Sapho artifact style
- it avoids quietly regressing to an older summary-only public shape
- it keeps Website 2.0 aligned with the real article artifact contract

### 16. Canonical artifact pages still need a lightweight traceability panel above the body

Another user correction from rollout:
- publishing only the stripped canonical article body removed too much provenance context
- the desired public artifact page should keep the canonical article body AND restore a small traceability surface above it

A good Website 2.0 pattern is:
- prepend a collapsible traceability block to the canonical article body
- keep the body itself unchanged after frontmatter stripping

Useful fields to surface in the traceability panel:
- source link
- intake queued time
- source captured time
- curated time
- artifact finalized time
- artifact published time when available

Good implementation shape:
- wrap it in a `<details class="traceability-panel">`
- use the existing CSS hooks in `public/site/assets/style.css` when present:
  - `.traceability-panel`
  - `.traceability-body`
- then append the canonical article body below it

This preserves both:
- the new canonical article style
- the minimal provenance surface the user still expects on public artifacts

A major rollout correction:
- the first Website 2.0 artifact pass still published a rewritten artifact shape like:
  - `Source metadata`
  - `Core thesis`
  - `Why it matters`
  - `Key findings`
  - `Evidence base`
  - `Limits`
- that was not the desired new artifact style
- the user wanted the canonical new article artifact itself

Correct Website 2.0 behavior:
- public artifact markdown should use the canonical `article.md` body with frontmatter stripped
- do not re-summarize or remap sections into an older public-summary schema

A good implementation pattern is:
- in `build_public_artifact_markdown(...)`, start from `strip_frontmatter(body)`
- emit that canonical body directly
- only add small surrounding public metadata if explicitly requested

Verification:
- open one generated artifact under `public/site/artifacts/kb/queue/`
- confirm it starts with the canonical article title and sections like:
  - `## Core Thesis`
  - `## Why It Matters for Sapho`
  - `## Key Findings`
  - `## Evidence and Findings`
  - `## Contradictions and Tensions`
  - `## Mechanism or Bounds`
  - `## Limits`

### 16. Restore traceability as a compact accordion above the canonical artifact body

Another important user correction from rollout:
- even when the canonical article body is used, the public artifact should still expose a compact traceability surface
- the right shape is not the full raw frontmatter dump
- the right shape is a focused accordion/details block carrying key provenance fields

A strong Website 2.0 traceability block includes:
- source link
- intake queued timestamp
- source captured timestamp
- curated timestamp
- artifact finalized timestamp
- artifact published timestamp when available

Implementation pattern that worked:
- prepend a `<details class="traceability-panel">` block to the public artifact markdown/HTML payload
- keep the canonical article body below it unchanged
- reuse the existing CSS hooks already present in `public/site/assets/style.css`:
  - `.traceability-panel`
  - `.traceability-body`
  - `.traceability-subhead`

Practical rule:
- restore traceability, but do not dump the entire article frontmatter verbatim
- preserve readability by surfacing only the provenance fields the operator actually cares about

Verification:
- render Website 2.0 locally
- inspect one generated artifact file
- confirm the traceability accordion appears above the canonical article title/body and includes the key dates plus source URL

### 17. In Website 2.0 mode, routine artifact publication should rebuild the lawful kept-artifact site state, not patch old incremental surfaces

Another important operational finding from rollout:
- `run_micro_artifact_publish.py` originally still behaved like the old incremental artifact publisher
- it staged and patched old artifact surfaces (`kept-links`, RSS, alias redirects) one article at a time
- this was fragile in Website 2.0 mode because the new site treats the lawful ready corpus as the source of truth and should not depend on old live-site incremental state

Correct Website 2.0 behavior:
- first update the article metadata with:
  - `artifact_publication_alias`
  - `artifact_publication_status=published`
  - `artifact_publication_minted_at_utc`
  - `artifact_publication_published_at_utc`
- then rebuild the Website 2.0 kept-artifact site state through the clean renderer path
- do not treat old staged live surfaces as authoritative in GitHub Pages mode

A good implementation pattern is:
- in `run_micro_artifact_publish.py`, branch on `site_mode()`
- for `github-pages` mode:
  - skip `stage_live_artifact_surfaces()`
  - write artifact publication metadata to the article first
  - call `render_artifact_site()` to regenerate the lawful kept-artifact output set
- for legacy mode:
  - preserve the old incremental patch/update path if still needed

Important operational detail discovered in practice:
- when invoking `run_micro_artifact_publish.py` manually on the VPS, explicitly set Website 2.0 env vars, for example:
  - `SAPHO_SITE_MODE=github-pages`
  - `SAPHO_SITE_BASE_URL=https://research.quiznat.com`
  - `SAPHO_SITE_CUSTOM_DOMAIN=research.quiznat.com`
- otherwise the script can fall back to legacy live-site staging and try to touch old OpenClaw paths like `/home/openclaw/.openclaw/workspace/website/...`, which fails or is the wrong deploy target in Website 2.0 mode

Why this matters:
- routine kept-artifact publication becomes reproducible and clean
- the site stays aligned with the lawful current corpus instead of whatever old surface snapshot happened to be staged
- adding one new artifact does not risk half-mutating unrelated site content

### 18. Preserve artifact aliases during clean Website 2.0 rebuilds

A follow-on rollout finding:
- once `run_micro_artifact_publish.py` assigns an alias, the clean Website 2.0 rebuild must reuse it
- otherwise the renderer may generate a new alias and the just-published artifact can appear to vanish or move

Correct pattern:
- in `render_site.collect_current_articles(...)`, if no registry item exists for the source but the article frontmatter already has `artifact_publication_alias`, use that configured alias directly before generating a new one

Verification:
- publish a kept article in Website 2.0 mode
- rerender the site cleanly
- confirm:
  - the article still appears
  - the alias path stays stable
  - the kept-links payload includes the new article under the expected alias

### 19. If RSS is deferred, keep feed files physically absent — not merely unlinked

A later rollout correction made the intended Website 2.0 rule stricter:
- it is not enough to hide RSS/feed links from the homepage
- feed files like `rss.xml`, `artifacts.xml`, `daily.xml`, and `data/artifacts-feed.json` must remain absent in Website 2.0 mode until the feed slice is intentionally re-enabled

Why this matters:
- a lingering committed feed file can still trigger readers, crawlers, or operator confusion even if the homepage no longer advertises it
- “offline” should mean absent, not merely de-emphasized

Correct pattern:
- add a cleanup step in Website 2.0 mode, for example `cleanup_disabled_feed_surfaces()`
- remove these files whenever feeds are disabled:
  - `public/site/rss.xml`
  - `public/site/artifacts.xml`
  - `public/site/daily.xml`
  - `public/site/data/artifacts-feed.json`
- call that cleanup during artifact-only renders, daily renders, and full site renders in Website 2.0 mode

Verification:
- run a Website 2.0 render locally
- confirm all four feed paths are absent on disk
- confirm validation still passes without them

### 20. Website 2.0 kept surfaces should be rebuilt from the lawful ready corpus in explicit batches

A useful operational lesson from backlog processing:
- when importing and processing old runtime backlog items, Website 2.0 should surface only the newly lawful corpus
- the safest pattern is to process pending imports in explicit batches (for example batches of 6), then artifact-publish newly kept items into the site after each batch

Strong pattern that worked:
1. import stale pending items from the old runtime into local `queue/` and `articles/`
2. process them through `run_micro_article_lane.py` in explicit 6-item batches
3. for each batch, identify items that ended as:
   - `publication_status: ready-for-daily`
   - `historical-policy.json -> current_law_compliant`
4. artifact-publish those kept items
5. rerender Website 2.0 in `github-pages` mode
6. review on-site before continuing the next batch

This keeps pace higher without widening into an unreviewable blob and preserves the user’s preference for reviewing on the actual site rather than only in GitHub.

### 21. Approved Website 2.0 surfaces are strictly limited to Charter and kept artifacts

A critical product constraint reaffirmed during rollout:
- Website 2.0 is not approved to show daily surfaces
- Website 2.0 is not approved to show longform/canon surfaces
- RSS must remain offline until intentionally restored later

Practical rule:
- if any render path leaks old daily content, longform sections, or old artifact inventory, treat it as a bug and rebuild from the approved corpus/surfaces only
- the shell/style/layout may carry over, but the content model must be limited to Charter + kept artifacts

### 22. Review flow preference: publish newly kept artifacts to the site promptly so the user can review on-site

A durable operator preference from rollout:
- once a batch produces new lawful kept artifacts, artifact-publish them and rerender Website 2.0 promptly
- the user prefers reviewing new articles on the live site rather than primarily through GitHub blobs

This means batch cadence should usually be:
1. process batch
2. artifact-publish newly kept items
3. rerender/deploy Website 2.0
4. let the user review on-site
5. continue to the next batch

### 23. After a GitHub Pages push, verify the live site and expect propagation lag

Another useful rollout finding:
- after committing and pushing Website 2.0 changes, the repo state can be correct while `research.quiznat.com` still serves the older Pages build for a while
- this can look like the push failed even when the generated `public/site` contents and pushed commit are correct

Good verification pattern:
1. verify local rendered output under `public/site/` contains the new aliases / artifact files
2. verify the push succeeded on `origin/main`
3. probe the live site directly (for example `https://research.quiznat.com/` and `https://research.quiznat.com/kept-links.html`)
4. if the live site still shows the older kept count or older top-of-homepage artifacts, wait and poll again rather than immediately assuming render/publish failure

Practical rule:
- distinguish "repo/render state is correct" from "Pages edge has updated"
- when reporting to the operator, it is useful to say explicitly whether:
  - the commit is pushed
  - the local rendered site contains the new artifacts
  - the public domain has or has not caught up yet

## Recommended implementation order

1. Add env-driven site config to `scripts/render_site.py`
   - mode
   - base URL
   - custom domain
   - feed enable/disable

2. Add Website 2.0 surface overrides
   - remove homepage RSS card
   - remove homepage RSS alternate tag
   - preserve style/layout otherwise
   - write `CNAME`

3. Split validation behavior by mode
   - legacy exact parity
   - Website 2.0 structural checks

4. Remove feed files from required validation in Website 2.0 mode

5. Loosen ops-surface equality checks in Website 2.0 mode to existence/shape checks where appropriate

6. Add tests for Website 2.0 mode
   - mode detection
   - feeds disabled by default
   - custom domain handling
   - homepage override behavior
   - baseline seed requirement behavior

7. Run a real local render in Website 2.0 mode
   - example:
     - `SAPHO_SITE_MODE=github-pages SAPHO_SITE_CUSTOM_DOMAIN=research.quiznat.com python scripts/render_site.py`

8. Only then add GitHub Pages deployment workflow or publishing path
   - if workflow-scope credentials are unavailable, keep the code slice separate from the workflow push

## Verification checklist

- `render_site.py` supports a GitHub Pages / Website 2.0 mode
- same public base URL still works
- `public/site/CNAME` is rendered correctly
- homepage style/layout remains recognizably the current Sapho site
- viewer still works as the canonical reading surface
- RSS/feed files are not required for Website 2.0 launch validation
- local Website 2.0 render succeeds
- tests covering Website 2.0 behavior pass

## What not to do

- Do not start with a redesign.
- Do not keep RSS as a hard requirement if the user explicitly deferred it.
- Do not leave GitHub Pages migration blocked on workflow PAT scope if the code path itself can still be completed and pushed.
- Do not preserve old OpenClaw deploy assumptions as if they are still the desired long-term hosting model.
