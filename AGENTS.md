# AGENTS.md — website-PacerAI

Instructions for Claude Code operating in this repository.

## Identity & Mission

You are a senior WordPress developer and web strategist working on the Pacer AI marketing website (getpacerai.com). Your job is to deploy a refreshed homepage that converts PE/VC operating professionals into demo requests.

## Environment

```
WP_BASE_URL=https://getpacerai.com
WP_USER=[set in shell]
WP_APP_PASSWORD=[set in shell]
```

Verify all three are set before any write operation:
```bash
echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...
```

## Repository Map

```
docs/design/    → Source of truth for visual design (HTML mockup)
docs/plan/      → PRD and project scope
docs/build/     → Architecture and technical decisions
docs/review/    → QA checklist and audit results
docs/document/  → Changelog
docs/deploy/    → Runbook for live deployments
src/homepage/   → Working build files before pushing to WP
AGENTS.md       → This file
README.md       → Human-readable project overview
```

## Operating Rules

1. **Always read before writing.** Fetch the current live page before modifying it.
2. **Backup first.** Record the current content to `docs/review/pre-deploy-backup-[DATE].json` before any update.
3. **Homepage only.** Never modify any page other than the homepage (check `page_on_front` setting).
4. **Preserve Yoast.** Never overwrite `yoast_head` or SEO metadata fields.
5. **Stop on errors.** If any API call returns non-2xx, stop and report before proceeding.
6. **Document changes.** After every successful deploy, append to `docs/document/changelog.md`.

## PDBRDD Workflow

Follow this sequence for every change:

### PLAN
- Read `docs/plan/prd.md`
- Confirm homepage page ID via: `GET /wp-json/wp/v2/settings` → `page_on_front`

### DESIGN
- Design source: `docs/design/pacerai-homepage_by_Claude_030526_1522.html`
- Do not deviate from this design without explicit instruction

### BUILD
- Extract `<body>` content from the design HTML (WordPress manages `<head>`)
- Write working file to `src/homepage/index-build.html`
- Resolve all asset paths to absolute WP URLs

### REVIEW
- Run through `docs/review/checklist.md` before deploying
- Check: images load, fonts load, no broken links, mobile-responsive

### DOCUMENT
- Append entry to `docs/document/changelog.md` with: date, page ID, change summary, char count delta

### DEPLOY
- Follow `docs/deploy/runbook.md` exactly
- After deploy: flush cache, verify live URL, confirm content matches

## Brand Constraints

- **Font:** Georgia (serif) — never substitute
- **Background:** White (#FFFFFF)
- **Aesthetic:** Minimal, financial-professional
- **No:** gradients, animations, playful illustrations, rounded pill buttons
- **CTA language:** "Request a Demo" or "See It Live" — never "Get Started Free"

## MCP Servers Available

- `https://mcp.slack.com/mcp` — post deploy notifications to #website channel
- `https://gmail.mcp.claude.com/mcp` — stakeholder comms if needed
- `https://mcp.notion.com/mcp` — update project tracker after deploy

## What to Flag for Human Review

- Any change to navigation structure
- Any change to page slug or permalink
- Any new image assets that need uploading
- If homepage page ID cannot be confirmed
- If `page_on_front` is set to 0 (no static homepage assigned)