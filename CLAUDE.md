# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Marketing website repo for [getpacerai.com](https://getpacerai.com). WordPress.com hosted site deployed via the WordPress REST API. No local dev server — content is authored as standalone HTML files and pushed to WordPress as Pages.

**Target:** PE-backed SaaS operators (Operating Partners, CFOs, RevOps leaders at $50M-$1B ARR companies).

## Stack

- **CMS:** WordPress.com (hosted, no SSH/WP-CLI access)
- **Theme:** Twenty Twenty-Four (WordPress default — fully overridden by inline CSS)
- **Deploy method:** WordPress REST API + Application Password (Python `requests` library)
- **No build tools** — no npm, no bundler, no framework. Pure HTML/CSS, vanilla JS for mobile nav only.
- **Font loading:** Google Fonts loaded by WordPress — no `<link>` tags needed in page HTML.

## WordPress Page Registry

All pages are deployed as WordPress Pages via REST API. Each page's HTML source file is the source of truth.

| Page | WP ID | Slug | Parent | Source File |
|------|-------|------|--------|-------------|
| **Home** | 25 | `no-title` | — | `src/homepage/index-build.html` |
| **Blog** | 230 | `blog` | — | `src/blog/index-build.html` |
| Platform (parent) | 362 | `platform` | — | *(placeholder — no content)* |
| **Platform Overview** | 371 | `overview` | 362 | `src/platform/overview.html` |
| Solutions (parent) | 364 | `solutions` | — | *(placeholder — no content)* |
| **ARR Snowball** | 372 | `arr-snowball-board-reporting` | 364 | `src/solutions/arr-snowball.html` |
| **Customer Data Cube** | 373 | `customer-data-cube` | 364 | `src/solutions/customer-data-cube.html` |
| Company (parent) | 366 | `company` | — | *(placeholder — no content)* |
| **About** | 374 | `about` | 366 | `src/company/about.html` |
| **Contact** | 375 | `contact` | 366 | `src/company/contact.html` |
| Pricing | 111 | `pricing` | — | *(legacy — not managed by this repo)* |
| Login | 134 | `login` | — | *(legacy — not managed by this repo)* |

**Live URLs:**
- https://getpacerai.com/
- https://getpacerai.com/blog/
- https://getpacerai.com/platform/overview/
- https://getpacerai.com/solutions/arr-snowball-board-reporting/
- https://getpacerai.com/solutions/customer-data-cube/
- https://getpacerai.com/company/about/
- https://getpacerai.com/company/contact/

## Environment Variables (Required for REST API deploys)

```bash
WP_BASE_URL=https://getpacerai.com
WP_USER=willsullivan5e7f50183a
WP_APP_PASSWORD=[set in shell — ask Will]
```

Verify: `source ~/.zshrc && echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...`

## Repository Structure

```
src/
├── homepage/
│   └── index-build.html                # Homepage (WP ID 25)
├── blog/
│   ├── index-build.html                # Blog index (WP ID 230)
│   ├── post-template.html              # Blog post template
│   └── posts/                          # Individual blog post build files
├── platform/
│   └── overview.html                   # Platform Overview (WP ID 371)
├── solutions/
│   ├── arr-snowball.html               # ARR Snowball (WP ID 372)
│   └── customer-data-cube.html         # Customer Data Cube (WP ID 373)
└── company/
    ├── about.html                      # About (WP ID 374)
    └── contact.html                    # Contact (WP ID 375)

docs/
├── plan/
│   ├── overview.md                     # Project goals, scope, success criteria
│   ├── prd.md                          # Product requirements document
│   └── site-tree-and-build-prompts.md  # Full site tree + build prompts for every page
├── design/
│   ├── pacerai-homepage_by_Claude_030526_1522.html   # Original v1 design mockup
│   └── pacerai-homepage-v2_2026-03-09.html           # v2 design (current)
├── build/
│   └── architecture.md                 # Technical decisions, deploy methods, page structure
├── review/
│   ├── checklist.md                    # QA checklist
│   ├── Issues.md                       # Known issues
│   └── pre-deploy-backup-*.json        # Backups before each deploy
├── document/
│   ├── changelog.md                    # Deploy log
│   └── Internal_Documentation.md       # Messaging, positioning, site tree, SEO strategy
└── deploy/
    └── runbook.md                      # Deploy instructions
```

## Key Workflows

### Deploying a single page
```python
import requests, os

base_url = os.environ['WP_BASE_URL']
auth = (os.environ['WP_USER'], os.environ['WP_APP_PASSWORD'])

with open('src/platform/overview.html') as f:
    html = f.read()

content = f"<!-- wp:html -->{html}<!-- /wp:html -->"
resp = requests.post(f"{base_url}/wp-json/wp/v2/pages/371", json={"content": content}, auth=auth)
print(f"{'OK' if resp.status_code == 200 else 'FAILED'} — HTTP {resp.status_code}")
```

### Deploying all pages (batch)
```python
pages = [
    {"id": 25,  "file": "src/homepage/index-build.html"},
    {"id": 230, "file": "src/blog/index-build.html"},
    {"id": 371, "file": "src/platform/overview.html"},
    {"id": 372, "file": "src/solutions/arr-snowball.html"},
    {"id": 373, "file": "src/solutions/customer-data-cube.html"},
    {"id": 374, "file": "src/company/about.html"},
    {"id": 375, "file": "src/company/contact.html"},
]
for p in pages:
    with open(p['file']) as f:
        html = f.read()
    content = f"<!-- wp:html -->{html}<!-- /wp:html -->"
    resp = requests.post(f"{base_url}/wp-json/wp/v2/pages/{p['id']}", json={"content": content}, auth=auth)
    print(f"  {'OK' if resp.status_code == 200 else 'FAIL'} ID {p['id']}")
```

### Creating a new page
```python
# 1. Create the HTML source file in the appropriate src/ subdirectory
# 2. Create the WP page with correct parent and slug:
resp = requests.post(f"{base_url}/wp-json/wp/v2/pages", json={
    "title": "Page Title",
    "slug": "page-slug",
    "parent": 364,  # parent page ID (e.g., Solutions)
    "status": "publish",
    "content": f"<!-- wp:html -->{html}<!-- /wp:html -->"
}, auth=auth)
# 3. Record the new page ID in this CLAUDE.md page registry
```

### Deploy sequence
1. Edit source HTML file in `src/` → 2. Push via REST API → 3. Verify live URL returns 200 → 4. Log to `docs/document/changelog.md`

See `docs/deploy/runbook.md` for full instructions.

### Reading a live page
```bash
source ~/.zshrc && curl -s -u "$WP_USER:$WP_APP_PASSWORD" \
  "$WP_BASE_URL/wp-json/wp/v2/pages/371?context=edit&_fields=id,title,slug,content,link"
```

### Lighthouse Audit
```bash
npx lighthouse https://getpacerai.com --output=json --output-path=docs/review/lighthouse-$(date +%Y%m%d).json
```
Targets: Performance >= 85, SEO >= 90, Accessibility >= 90, Best Practices >= 90.

## Critical Rules

- **Backup before deploy** — always save current content before updating
- **Preserve Yoast SEO** — never overwrite `yoast_head` or SEO metadata fields
- **Stop on API errors** — if any REST call returns non-2xx, stop and report
- **Always read before writing** — fetch current live page before modifying
- **Update all pages when changing shared elements** — nav, footer, and base CSS are duplicated across all page files. Changes to these must be applied to all files and redeployed.
- **Page registry** — when creating new WP pages, record the ID in the registry table above

## Page Architecture

Every page follows the same pattern:

```html
<!-- wp:html -->
<style>
  /* TT4 theme overrides (hide chrome, force dark bg, remove constraints) */
  /* Hide WP page title and spacer */
  .wp-block-post-title, .wp-block-spacer { display: none !important; }
  /* CSS variables, component styles, responsive breakpoints */
</style>
<div id="pacerai-homepage">
  <nav>...</nav>           <!-- Shared nav — identical across all pages -->
  <!-- Page-specific content sections -->
  <footer>...</footer>     <!-- Shared footer — identical across all pages -->
</div>
<script>/* Mobile nav JS */</script>
<!-- /wp:html -->
```

**Key CSS overrides for WordPress TT4:**
- Hide theme header/footer: `.wp-site-blocks > header, .wp-site-blocks > footer { display: none }`
- Hide WP page title: `.wp-block-post-title, .wp-block-spacer { display: none }`
- Force dark background: `html, body, .wp-site-blocks { background: #080E1C }`
- Remove container constraints: `.is-layout-constrained, .has-global-padding { max-width: none; padding: 0 }`

## Brand Constraints

- **Fonts:** DM Sans (body), Cormorant Garamond (headings) — approved by Will
- **Background:** Dark navy (#080E1C)
- **Primary accent:** Teal (#27899A), Teal Light (#70C49C)
- **Aesthetic:** Minimal, financial-professional. Subtle teal accents. No playful illustrations or rounded pill buttons.
- **CTA language:** "Request a Demo", "See a Live ARR Demo", "Talk to a RevOps Expert" — never "Get Started Free"
- **Voice:** Confident, precise. Never use "leverage" or "utilize."

## Known Issues

- **Homepage slug is `no-title`** — needs Will's review before changing (affects permalink)
- **Yoast meta description missing** — must be set in WP admin per PRD
- **Yoast page title** — should be "Pacer AI — ARR Intelligence for PE-Backed SaaS"

## Flag for Human Review

- Changes to navigation structure or page slug/permalink
- New image assets that need uploading
- Creating new WordPress pages (record ID in registry)
- Plugin installation or theme changes
