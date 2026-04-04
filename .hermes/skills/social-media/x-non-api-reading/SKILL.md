---
name: x-non-api-reading
description: Read X/Twitter without the official API. Use this when the user wants public/non-API access, direct tweet reading, or a durable browser-based fallback instead of X developer credentials.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [twitter, x, scraping, browser, public-web, non-api]
---

# X Non-API Reading

Use this skill when the user wants to read X/Twitter content but does **not** want the official X API.

## Core rule

Do **not** push the official X API path if the user has already rejected it.

The practical choices are:
1. Public no-login recovery for specific posts/accounts
2. Persistent browser session with cookies/login (more durable, still non-API)
3. Third-party scraping vendors/providers

## Decision framework

### If the user says:
- "I don't want the X API"
- "Just read this public post"
- "There has to be a public way"
- "I don't want to log in"

Then frame the situation honestly:
- Yes, some public no-login access is possible
- No, there is not a single stable, low-maintenance universal public pipe anymore
- X is a hostile public source: public for eyeballs, adversarial for machine ingest

## Recommended hierarchy

### 1. Specific tweet/post recovery (best for one-off reads)
Try in this order:
- Direct extraction (`web_extract`) — often blocked by X
- Browser open/read if browser tools work
- Search-index recovery (`web_search`) to recover title/snippets
- Ask the user for alternate mirrors/screenshots only if necessary

Be explicit when the result is partial.
Do not pretend snippet reconstruction is a full read.

### 2. Durable non-API ongoing reading (best operational answer)
Recommend a **persistent browser session** rather than the X API.

Best pattern:
- Real Chrome/Chromium browser
- Persistent `user-data-dir` / browser profile
- Hermes attached over CDP (`BROWSER_CDP_URL` or `/browser connect`)
- Log in once if the user accepts login
- Reuse cookies/session for future browsing

Why this is the grown-up non-API answer:
- Uses the real site
- Avoids official API friction
- More durable than public mirrors/Nitter-style hacks
- Supports direct link reading and repeated monitoring

### 3. Public no-login monitoring at scale
If the user insists on **no login at all**, recommend a layered recovery stack, not a single connector:
- Tier A: direct public-page scrape
- Tier B: search-index fallback
- Tier C: third-party scraper/vendor if reliability matters
- Tier D: aggressive local caching once content is seen

State clearly:
- Pure public access is possible
- Clean/simple/stable public ingest is generally not
- Nitter/RSSHub/mirrors are backups, not primary infrastructure

## Battle-tested conclusions to communicate

### Reliable truths
- Public X pages can sometimes be scraped without login
- Direct tweet URLs are much easier than broad search/timeline access
- Search/timelines are significantly harder without login
- DIY public scrapers break regularly due to token churn, internal endpoint changes, rate limits, and anti-bot heuristics
- Nitter-style public mirrors are too unreliable to be the primary system

### Strong recommendation language
Use wording like:
- "The battle-tested non-API method is a persistent logged-in browser session, not the official API."
- "For pure no-login access, use layered scraping + fallback + caching, not one magic public source."
- "X has made public machine access adversarial even when the content is public to humans."

## Hermes-specific operational notes

### Browser failure investigation checklist
If Hermes browser reading fails:
1. Try `web_extract` first for the direct X URL
2. If unsupported, try `browser_navigate`
3. If Playwright browser executable is missing, install it:
   ```bash
   npx playwright install chromium
   ```
4. If Chromium fails with missing shared libraries (e.g. `libatk-1.0.so.0`), identify OS dependency issue
5. Show the exact Playwright dependency install command if needed:
   ```bash
   npx playwright install-deps --dry-run chromium
   ```
6. If sudo/root is unavailable, explain that the blocker is OS-level, not Hermes-level

### Important VPS finding
On headless Ubuntu/Debian VPS setups, a common failure mode is:
- Playwright Chromium installs successfully
- launch still fails due to missing system libraries
- hermes user lacks sudo, so local browser cannot be fully repaired from chat alone

In that situation, recommend:
- root-level dependency install, or
- containerized browser / remote CDP browser, or
- persistent desktop Chrome via CDP

### Docker nuance
If Docker exists but the Hermes user cannot access `/var/run/docker.sock`, the containerized browser path is still operationally blocked until permissions are fixed.

## What not to do
- Do not insist on the X API after the user rejects it
- Do not claim public no-login access is easy or stable when it is not
- Do not present snippet-based reconstruction as a complete read
- Do not recommend Nitter/mirrors as the primary durable foundation

## Good outputs

### When user wants truth, not false hope
Say:
- "Yes, there are public no-login ways to pull some X data."
- "No, there is not a stable, low-maintenance, universal public pipe anymore."

### When user wants a practical framework
Say:
- "Treat X as a hostile public source. Build a recovery stack, not a connector."

## Reusable recommendation templates

### Template: user rejects X API
"Understood — I’ll treat no official X API as a hard constraint. The realistic non-API options are: public no-login recovery for direct posts, a persistent browser session for durability, or third-party scrapers."

### Template: user demands pure public access
"Pure public access is possible, but not as a clean canonical interface. The durable pattern is layered public recovery: direct scrape, search-index fallback, optional third-party provider, and immediate local caching."

### Template: user wants the least annoying serious setup
"The least annoying serious non-API setup is one long-lived browser service with a persistent profile that Hermes connects to over CDP."
