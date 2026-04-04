# Website 2.0 GitHub Pages Implementation Plan

> For Hermes: use subagent-driven-development discipline if executing this plan later, but keep commits as small explicit slices.

Goal: stand up Website 2.0 on GitHub Pages using the current public site's style, layout, and viewer flow as the carry-forward baseline, while deferring RSS/feed work until after the site stabilizes.

Architecture: keep the site static and file-native. Reuse the existing `render_site.py` pipeline as the core renderer, but separate site generation from the old OpenClaw/Vercel/live-website assumptions. Formal publication authority should remain the source of what is eligible to appear. Website 2.0 should become a GitHub Pages-native static output target with a clean deployment path.

Tech stack: Python static site generation, existing HTML/CSS/JS viewer assets, GitHub Pages static hosting, repo-based deployment.

---

## Current audit summary

### Current assets worth preserving
- Homepage:
  - `sapho-native/public/site/index.html`
- Viewer shell:
  - `sapho-native/public/site/viewer.html`
- Main theme CSS:
  - `sapho-native/public/site/assets/style.css`
- Render pipeline:
  - `sapho-native/scripts/render_site.py`

### Current deployment assumptions to unwind
- `render_site.py` hardcodes:
  - `BASE_URL = "https://research.quiznat.com"`
  - `DEFAULT_PUBLIC_SEED_DIR = /home/openclaw/.openclaw/workspace/website`
  - `RUNTIME_CHARTER` and some ops inputs under `/home/openclaw/...`
- `deploy_live_site.py` syncs rendered output into the old OpenClaw live repo/website tree and commits there.
- Validation currently requires exact seed-file equality for homepage/viewer/charter wrapper, which is too rigid for a controlled Website 2.0 evolution.

### Current feed coupling that should be deferred
- Homepage currently links `artifacts.xml` directly.
- Render validation currently requires:
  - `rss.xml`
  - `artifacts.xml`
  - `daily.xml`
- Artifact/daily rendering still treats RSS/feed generation as part of the required surface set.

### Key migration implication
Website 2.0 should be implemented as a static-site migration and render-pipeline cleanup, not a redesign. The current visual baseline should be preserved while feed surfaces are removed from the launch-critical validation path.

---

## Build sequence

1. Introduce a GitHub Pages-oriented site config surface.
2. Decouple rendering from old OpenClaw seed/deploy paths.
3. Preserve homepage/viewer/layout look while allowing controlled Website 2.0 edits.
4. Remove RSS/feed surfaces from required validation for Website 2.0 launch.
5. Add a GitHub Pages output/deploy path.
6. Verify locally with generated static output.
7. Only after Website 2.0 stabilizes, create a separate RSS/feed slice.

---

## Task 1: Add explicit site-target configuration

Objective: make the renderer choose between legacy/live assumptions and Website 2.0 GitHub Pages assumptions without hardcoded path surgery.

Files:
- Modify: `sapho-native/scripts/render_site.py`
- Modify: `sapho-native/scripts/common.py` if shared helpers are needed
- Test: create `sapho-native/tests/test_render_site_config.py`

Step 1: Add a small site-target config layer in `render_site.py`
- Introduce env-driven settings such as:
  - `SAPHO_SITE_BASE_URL`
  - `SAPHO_SITE_MODE` with values like `legacy` / `github-pages`
  - `SAPHO_PUBLIC_SEED_DIR`
- Default to current behavior unless explicitly switched.

Step 2: Replace hardcoded `BASE_URL` usages with config access
- Keep one canonical resolver function, e.g. `site_base_url()`.
- All generated absolute URLs should use that resolver.

Step 3: Write tests
- Verify default mode preserves current base URL behavior.
- Verify GitHub Pages mode can produce a different base URL.

Step 4: Run tests
- Run: `python -m pytest tests/test_render_site_config.py -q`

Step 5: Commit
- Commit message:
  - `sapho: add configurable site target for Website 2.0`

---

## Task 2: Separate static rendering from old live-seed equality requirements

Objective: preserve visual/layout carryover without requiring byte-for-byte equality with the old seed site.

Files:
- Modify: `sapho-native/scripts/render_site.py`
- Test: extend/add `sapho-native/tests/test_render_site_validation.py`

Current problem:
- `validate_render()` currently raises if:
  - homepage is not exact seed
  - viewer is not exact seed
  - charter wrapper is not exact seed
- That is useful for frozen parity, but too strict for Website 2.0.

Step 1: Introduce validation modes
- `legacy-parity` mode: preserve current exact-seed checks
- `website2` mode: require structural/semantic checks instead of exact file identity

Step 2: Replace exact-seed checks with structural checks in Website 2.0 mode
Homepage checks should assert presence of:
- institute heading
- primary surfaces section
- kept-links/archive/viewer links
- stylesheet and seal assets

Viewer checks should assert presence of:
- stylesheet link
- `marked`, `dompurify`, `mermaid` script hooks if still used
- back/home navigation
- `viewer.html?file=` behavior scaffolding

Step 3: Keep exact-seed parity checks available only for legacy mode

Step 4: Add tests
- one test for legacy-parity mode exactness
- one test for website2 mode structural validation acceptance

Step 5: Run tests
- Run: `python -m pytest tests/test_render_site_validation.py -q`

Step 6: Commit
- Commit message:
  - `sapho: relax site validation for Website 2.0 structural carryover`

---

## Task 3: Remove RSS/feed surfaces from Website 2.0 launch-critical validation

Objective: make Website 2.0 stand up cleanly before RSS is rebuilt.

Files:
- Modify: `sapho-native/scripts/render_site.py`
- Modify: `sapho-native/public/site/index.html` or generated homepage template area in renderer if homepage is regenerated there
- Test: add `sapho-native/tests/test_render_site_website2_no_rss.py`

Current coupling to remove from launch-critical path:
- `validate_artifact_render()` requires `rss.xml` and `artifacts.xml`
- `validate_daily_briefing_render()` requires `daily.xml`
- homepage surfaces advertise RSS directly

Step 1: Introduce feed mode flag
- Example:
  - `SAPHO_ENABLE_FEEDS=1` for later slice
  - default false in Website 2.0 mode

Step 2: In Website 2.0 mode, stop requiring feed files in validation
- Artifact/daily page validation should pass without feed files when feeds are disabled.

Step 3: Remove or de-emphasize homepage RSS links for Website 2.0
- Prefer removing “Artifacts RSS” from the critical homepage surface rather than pointing to a not-yet-supported target.
- Fail-closed principle: do not advertise feed readiness before it exists.

Step 4: Keep feed generation code present but non-required
- This makes the later RSS slice additive rather than entangled.

Step 5: Add tests
- Assert Website 2.0 render validation passes with feeds disabled.
- Assert no homepage RSS primary-surface requirement remains in Website 2.0 mode.

Step 6: Run tests
- Run: `python -m pytest tests/test_render_site_website2_no_rss.py -q`

Step 7: Commit
- Commit message:
  - `sapho: defer rss from Website 2.0 launch path`

---

## Task 4: Create a GitHub Pages output/deploy target

Objective: publish the rendered site to a GitHub Pages-compatible location instead of the old OpenClaw website repo path.

Files:
- Modify: `sapho-native/scripts/deploy_live_site.py`
- Possibly create: `sapho-native/scripts/deploy_github_pages_site.py`
- Possibly create: `.github/workflows/website2-pages.yml` in `/home/hermes`
- Test: add deployment-path tests if feasible

Recommended implementation approach:
- Do not overload the old deploy script too far.
- Prefer a new deploy path for clarity, e.g.:
  - render into `sapho-native/public/site/`
  - sync/copy into a GitHub Pages publish directory such as:
    - `/home/hermes/docs/site2/` or
    - `/home/hermes/gh-pages/` staging branch workflow

Preferred repo strategy (simple version):
- keep source and generation in the main repo
- publish GitHub Pages from a dedicated branch or from `/docs` if that proves cleaner
- choose one canonical approach and document it explicitly

Step 1: Decide publish strategy
- Option A: GitHub Pages from `docs/`
- Option B: GitHub Pages from dedicated `gh-pages` branch

Recommendation:
- Prefer dedicated `gh-pages` branch if generated output is large and should stay separate.
- Prefer `/docs` only if the generated site is modest and keeping it on `main` aids review.

Step 2: Implement a dedicated deployment script for Website 2.0
- Script should:
  - run render
  - stage the GitHub Pages output target
  - avoid old `/home/openclaw/...` live repo assumptions
  - emit a deployment receipt or summary

Step 3: Add GitHub Actions workflow if desired
- Build on push/manual dispatch
- Publish static output to Pages

Step 4: Verify deploy artifact structure
- Ensure `index.html`, `viewer.html`, `assets/`, `a/`, `s/`, `briefs/`, `daily/`, `kept-links.html` are all in the published tree.

Step 5: Commit
- Commit message:
  - `sapho: add GitHub Pages deployment path for Website 2.0`

---

## Task 5: Preserve current style and layout intentionally

Objective: treat the current site as the visual baseline and verify carryover instead of drifting by accident.

Files:
- Read/compare:
  - `sapho-native/public/site/index.html`
  - `sapho-native/public/site/viewer.html`
  - `sapho-native/public/site/assets/style.css`
- Add note/checklist doc if useful:
  - `sapho-docs/2026-04-04-website-2-visual-parity-checklist.md`

Required carryover surfaces:
- scholarly publication theme in `style.css`
- institute seal and heading treatment
- homepage card-grid layout
- viewer shell and markdown rendering flow
- kept-links and archive navigability

Verification checklist:
- homepage still feels like current Sapho, not a redesign
- viewer still functions as the canonical reading surface
- article alias redirects still land correctly
- daily archive remains navigable

Commit message:
- `docs: add Website 2.0 visual parity checklist`

---

## Task 6: Validate Website 2.0 against authority surfaces

Objective: ensure Website 2.0 only reflects lawfully eligible outputs.

Files:
- Modify if needed: `sapho-native/scripts/render_site.py`
- Read: `sapho-native/scripts/publication_authority.py`
- Add tests if needed: `sapho-native/tests/test_render_site_authority.py`

Step 1: Confirm render inputs are still constrained to eligible/published surfaces
- Current renderer already filters by publication state; now it should be checked against the new authority layer where appropriate.

Step 2: Ensure no blocked or ineligible package leaks into Website 2.0 primary surfaces.

Step 3: Add test fixtures proving:
- lawful article appears
- blocked/ineligible article does not

Commit message:
- `sapho: align Website 2.0 render surfaces with publication authority`

---

## Task 7: Final local proof before cutover planning

Objective: prove the static site can be rendered locally in Website 2.0 mode before any GitHub Pages cutover.

Files:
- No major new code beyond prior tasks
- Add docs note if useful: `sapho-docs/2026-04-04-website-2-proof-checklist.md`

Commands to run:
- `python scripts/render_site.py` or the equivalent Website 2.0 render entrypoint after config changes
- inspect generated output under the chosen public target
- if Pages workflow exists, run the build path locally if possible

Manual verification:
- homepage opens
- viewer opens markdown pages
- a/ alias pages redirect correctly
- daily archive and current briefing links work
- no RSS dependency is required for a valid Website 2.0 build

Commit message:
- `docs: add Website 2.0 local proof checklist`

---

## Exact implementation priorities

Priority 1
- configurable render/deploy target

Priority 2
- relax exact-seed validation into Website 2.0 structural validation

Priority 3
- remove RSS/feed from launch-critical validation and homepage emphasis

Priority 4
- GitHub Pages deployment path

Priority 5
- authority-aligned render verification

Priority 6
- local proof and then cutover planning for Vercel sunset

---

## Risks to watch

1. Absolute URL leakage
- current alias pages and viewer resolution embed `https://research.quiznat.com`
- these must be audited so GitHub Pages and preview environments work correctly

2. Hidden OpenClaw dependencies
- seed files, charter copy path, ops checkin surfaces, and deploy script still assume `/home/openclaw/...`
- Website 2.0 should remove those as required runtime assumptions

3. Feed entanglement
- render validation currently treats RSS as mandatory
- that must be explicitly severed for this slice

4. Over-redesign risk
- the assignment is carryover plus retargeting, not a new aesthetic system

---

## Definition of done for Website 2.0 slice

Website 2.0 is done enough to stabilize when:
- it renders as a static site without old OpenClaw live-site deployment assumptions
- it has a GitHub Pages publish path
- it preserves the current visual/layout baseline
- homepage/viewer/archive/kept-links all work
- it does not depend on RSS/feed surfaces to validate successfully
- it only surfaces lawfully eligible content
- Vercel shutdown can be planned without losing the public front door
