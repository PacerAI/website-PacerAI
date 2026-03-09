# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Marketing website repo for [getpacerai.com](https://getpacerai.com). WordPress.com hosted site deployed via the WordPress REST API and AI Engine MCP. No local dev server — content is authored as HTML and pushed to WordPress.

**Target:** Homepage for PE-backed SaaS operators (Operating Partners, CFOs, RevOps leaders at $50M–$1B ARR companies).

## Stack

- **CMS:** WordPress.com (hosted, no SSH/WP-CLI access)
- **Theme:** Twenty Twenty-Four (WordPress default — overridden by inline CSS)
- **Deploy methods:**
  - WordPress REST API + Application Password (for full content pushes)
  - AI Engine MCP (for reads, small edits, media uploads — Claude Code tools)
- **Design source:** `src/homepage/index-build.html` (live build file)
- **No build tools** — no npm, no bundler, no framework. Pure HTML/CSS, vanilla JS for mobile nav only.
- **Homepage page ID:** 25

## Environment Variables (Required for REST API deploys)

```bash
WP_BASE_URL=https://getpacerai.com
WP_USER=willsullivan5e7f50183a
WP_APP_PASSWORD=[set in shell — ask Will]
```

Verify: `echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...`

**Note:** MCP tools do not require env vars — credentials are in the MCP server config.

## Repository Structure

```
docs/
├── plan/
│   ├── overview.md                 # Project goals, scope, success criteria
│   └── prd.md                      # Product requirements document
├── design/
│   ├── pacerai-homepage_by_Claude_030526_1522.html   # Original v1 design mockup
│   └── pacerai-homepage-v2_2026-03-09.html           # v2 design (matches live)
├── build/
│   └── architecture.md             # Technical decisions, deploy methods, page structure
├── review/
│   ├── checklist.md                # QA checklist
│   ├── Issues.md                   # Known issues
│   └── pre-deploy-backup-*.json    # Backups before each deploy
├── document/
│   └── changelog.md                # Deploy log
└── deploy/
    └── runbook.md                  # Deploy instructions + MCP tool reference

src/homepage/
    └── index-build.html            # Live build file — source of truth for deploys
```

## Key Workflows

### Reading the Live Homepage
```
# Via MCP (preferred):
wp_get_post(ID=25)

# Via REST API:
curl -s -u "$WP_USER:$WP_APP_PASSWORD" "$WP_BASE_URL/wp-json/wp/v2/pages/25"
```

### Deploying (full content push)
```python
# Via Python (preferred for full pushes — MCP wp_alter_post mangles newlines):
content = open('src/homepage/index-build.html').read()
wrapped = "<!-- wp:html -->" + content + "<!-- /wp:html -->"
# POST to /wp-json/wp/v2/pages/25 with Basic Auth
```

### Deploy sequence
1. Backup current page → 2. Edit `src/homepage/index-build.html` → 3. Push via REST API → 4. Verify live → 5. Log to `docs/document/changelog.md`

See `docs/deploy/runbook.md` for full instructions.

### Lighthouse Audit
```bash
npx lighthouse https://getpacerai.com --output=json --output-path=docs/review/lighthouse-$(date +%Y%m%d).json
```
Targets: Performance >= 85, SEO >= 90, Accessibility >= 90, Best Practices >= 90.

## Critical Rules

- **Homepage only** — never modify any other page
- **Backup before deploy** — always save current content before updating
- **Preserve Yoast SEO** — never overwrite `yoast_head` or SEO metadata fields
- **Stop on API errors** — if any REST call returns non-2xx, stop and report
- **Always read before writing** — fetch current live page before modifying
- **MCP wp_alter_post caution** — mangles newlines in replacements. Use REST API for multi-line content changes.

## Brand Constraints

- **Fonts:** DM Sans (body), Cormorant Garamond (headings) — approved by Will
- **Background:** Dark navy (#080E1C)
- **Aesthetic:** Minimal, financial-professional. Subtle teal accents. No playful illustrations or rounded pill buttons.
- **CTA language:** "Request a Demo", "See a Live ARR Demo", "Request a Live Demo" — never "Get Started Free"

## Known Issues

- **Slug is `no-title`** — needs Will's review before changing (affects permalink)
- **Yoast meta description missing** — must be set in WP admin per PRD
- **Yoast page title** — should be "Pacer AI — ARR Intelligence for PE-Backed SaaS"

## Flag for Human Review

- Changes to navigation structure or page slug/permalink
- New image assets that need uploading
- Homepage page ID cannot be confirmed or `page_on_front` is 0
- Plugin installation or theme changes
