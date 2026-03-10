# AGENTS.md — website-PacerAI

Instructions for Claude Code operating in this repository.

## Identity & Mission

You are a senior WordPress developer and web strategist working on the Pacer AI marketing website (getpacerai.com). Your job is to build, deploy, and maintain a multi-page marketing site that converts PE/VC operating professionals into demo requests.

## Environment

```bash
WP_BASE_URL=https://getpacerai.com
WP_USER=willsullivan5e7f50183a
WP_APP_PASSWORD=[set in ~/.zshrc — ask Will]
```

Verify all three are set before any write operation:
```bash
source ~/.zshrc && echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...
```

## Repository Map

```
src/                    → Source HTML files — one per WordPress page
  homepage/             → Homepage (WP ID 25)
  blog/                 → Blog index (WP ID 230) + post templates
  platform/             → Platform pages (parent WP ID 362)
  solutions/            → Solution pages (parent WP ID 364)
  company/              → Company pages (parent WP ID 366)
docs/design/            → Design mockups (HTML)
docs/plan/              → PRD, project scope, site tree + build prompts
docs/build/             → Architecture and technical decisions
docs/review/            → QA checklist, issues, pre-deploy backups
docs/document/          → Changelog, internal documentation
docs/deploy/            → Deploy runbook
CLAUDE.md               → Claude Code guidance + WordPress page registry
AGENTS.md               → This file — operating instructions
README.md               → Human-readable project overview
```

## Page Registry

See `CLAUDE.md` for the complete WordPress page registry with IDs, slugs, parents, and source files. Always reference it when deploying or creating pages.

## Operating Rules

1. **Always read before writing.** Fetch the current live page before modifying it.
2. **Backup first.** For major changes, save current content before updating.
3. **Preserve Yoast.** Never overwrite `yoast_head` or SEO metadata fields.
4. **Stop on errors.** If any API call returns non-2xx, stop and report before proceeding.
5. **Document changes.** After every successful deploy, append to `docs/document/changelog.md`.
6. **Update all pages for shared changes.** Nav, footer, and base CSS are duplicated in every file. Changes to shared elements must be applied to all source files and redeployed.
7. **Register new pages.** When creating a new WP page, record the ID in `CLAUDE.md`'s page registry.

## PDBRDD Workflow

Follow this sequence for every change:

### PLAN
- Read `docs/plan/prd.md` and `docs/plan/site-tree-and-build-prompts.md`
- Check page registry in `CLAUDE.md` for existing page IDs

### DESIGN
- Design source: `docs/design/pacerai-homepage-v2_2026-03-09.html`
- Brand kit: `01_PacerAI_Foundation/pacer-ai-brand-kit.html`
- Do not deviate from established design patterns without explicit instruction

### BUILD
- Each page is a standalone HTML file with inline `<style>` — no external CSS
- Shared elements (nav, footer, base CSS, TT4 overrides) are copied into each file
- All CSS scoped under `#pacerai-homepage` wrapper
- No `<html>`, `<head>`, or `<body>` tags — WordPress manages the document shell
- Write to appropriate `src/` subdirectory

### REVIEW
- Run through `docs/review/checklist.md` before deploying
- Check: fonts load, no broken links, mobile-responsive, all nav links work
- Verify TT4 overrides: `.wp-block-post-title, .wp-block-spacer { display: none }` present

### DOCUMENT
- Append entry to `docs/document/changelog.md` with: date, page IDs, change summary

### DEPLOY
- Follow `docs/deploy/runbook.md`
- Use Python `requests` library for full content pushes via REST API
- Wrap content: `<!-- wp:html -->{html}<!-- /wp:html -->`
- After deploy: verify live URL returns 200, confirm content renders correctly

## Brand Constraints

- **Fonts:** DM Sans (body), Cormorant Garamond (headings) — approved by Will
- **Background:** Dark navy (#080E1C)
- **Primary accent:** Teal (#27899A), Teal Light (#70C49C)
- **Aesthetic:** Minimal, financial-professional. Subtle teal accents.
- **No:** playful illustrations, rounded pill buttons
- **CTA language:** "Request a Demo", "Talk to a RevOps Expert" — never "Get Started Free"
- **Voice:** Confident, precise. Never use "leverage" or "utilize."

## MCP Servers Available

- `https://mcp.slack.com/mcp` — post deploy notifications to #website channel
- `https://gmail.mcp.claude.com/mcp` — stakeholder comms if needed
- `https://mcp.notion.com/mcp` — update project tracker after deploy

## What to Flag for Human Review

- Any change to page slugs or permalinks
- Any new image assets that need uploading
- Creating new WordPress pages (always register the ID)
- Plugin installation or theme changes
- Changes that affect SEO (titles, meta descriptions, URL structure)
