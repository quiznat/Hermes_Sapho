---
name: headless-browser-setup
description: Repair Hermes browser tool access on headless Ubuntu/Debian servers by installing Playwright Chromium, required OS libraries, and verifying direct-link reading for sites like X.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [browser, playwright, chromium, headless, ubuntu, debugging]
    related_skills: [systematic-debugging, hermes-agent-setup]
---

# Headless Browser Setup for Hermes

Use this when Hermes browser tools fail on a headless Ubuntu/Debian VPS with errors like:
- `Executable doesn't exist at ... chrome-headless-shell`
- `Please run: npx playwright install`
- `error while loading shared libraries: libatk-1.0.so.0`
- browser navigation works in principle but public sites like X cannot be opened from Hermes

This is the standard recovery flow for restoring local browser fallback.

## When to use

- `browser_navigate` fails before page load
- Playwright/Chromium is missing
- Chromium is installed but launch fails on shared-library errors
- You need Hermes to open public links directly on a headless server

## Root causes this skill addresses

There are two common failure layers:

1. Browser binary missing
   - Symptom: Playwright says executable does not exist and recommends `npx playwright install`

2. OS libraries missing
   - Symptom: Chromium launches then exits with errors like `libatk-1.0.so.0: cannot open shared object file`
   - Cause: the VPS lacks GUI/runtime packages that headless Chromium still needs

## Step 1: Verify environment

From the Hermes repo:

```bash
source venv/bin/activate
which python
python --version
which node
node --version
which npx
npx --version
```

Confirm you are in the Hermes repo before installing browser components.

## Step 2: Install Playwright Chromium

```bash
source venv/bin/activate
npx playwright install chromium
```

This downloads:
- Chromium
- Chrome headless shell
- ffmpeg helper assets

If the original error was "Executable doesn't exist", this usually clears that layer.

## Step 3: If launch now fails on shared libraries, inspect the exact missing package

Typical error:

```text
error while loading shared libraries: libatk-1.0.so.0
```

That means Chromium is present but the OS packages are not.

## Step 4: Get the exact OS dependency command

Run:

```bash
source venv/bin/activate
npx playwright install-deps --dry-run chromium
```

On Ubuntu/Debian this prints the apt command Playwright wants. Example output seen in practice:

```bash
sudo -- sh -c "apt-get update&& apt-get install -y --no-install-recommends libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libatspi2.0-0t64 libcairo2 libcups2t64 libdbus-1-3 libdrm2 libgbm1 libglib2.0-0t64 libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xvfb fonts-noto-color-emoji fonts-unifont libfontconfig1 libfreetype6 xfonts-cyrillic xfonts-scalable fonts-liberation fonts-ipafont-gothic fonts-wqy-zenhei fonts-tlwg-loma-otf fonts-freefont-ttf"
```

## Step 5: Install OS dependencies as a privileged user

If the Hermes user is non-root, `npx playwright install-deps chromium` may fail because it invokes sudo interactively.

In that case, run the printed apt command yourself as root, or equivalent:

```bash
apt-get update
apt-get install -y --no-install-recommends \
  libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libatspi2.0-0t64 \
  libcairo2 libcups2t64 libdbus-1-3 libdrm2 libgbm1 libglib2.0-0t64 \
  libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 \
  libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xvfb \
  fonts-noto-color-emoji fonts-unifont libfontconfig1 libfreetype6 \
  xfonts-cyrillic xfonts-scalable fonts-liberation fonts-ipafont-gothic \
  fonts-wqy-zenhei fonts-tlwg-loma-otf fonts-freefont-ttf
```

## Step 6: Re-test Hermes browser access

After installing deps, retry the exact URL via Hermes browser tools.

For direct CLI verification, re-run the original Hermes/browser action that failed.

## Practical notes for X links

- Public X links often cannot be scraped with generic web extractors
- Hermes browser fallback is therefore especially valuable for reading X links directly
- If browser access is still unavailable, use an official X API workflow as the primary path and keep browser reading as secondary backup

## Complementary official-X setup

If you also want reliable structured X access, install `x-cli` and point it at Hermes secrets:

```bash
uv tool install git+https://github.com/Infatoshi/x-cli.git
mkdir -p ~/.config/x-cli
ln -sfn ~/.hermes/.env ~/.config/x-cli/.env
```

Then ensure these vars exist in `~/.hermes/.env`:
- `X_API_KEY`
- `X_API_SECRET`
- `X_BEARER_TOKEN`
- `X_ACCESS_TOKEN`
- `X_ACCESS_TOKEN_SECRET`

Quick check:

```bash
export PATH="$HOME/.local/bin:$PATH"
x-cli tweet get https://x.com/karpathy/status/2039805659525644595
```

If credentials are missing, `x-cli` reports the exact missing env vars.

## Pitfalls

- Installing Chromium alone is not enough on a minimal VPS
- `install-deps` often requires root and fails from non-interactive sudo sessions
- The first missing shared library in the error output is usually a signal of a larger package set missing, not just one file
- For X specifically, generic scraping may fail even when the link is public; keep the official API path available when possible

## Success criteria

You are done when:
- `npx playwright install chromium` succeeds
- required apt packages are installed
- Hermes browser tool can open previously failing public URLs
- optional: `x-cli` is installed and can read tweets with configured credentials
