# Architecture — Homepage v2

**Date:** March 2026 (updated 2026-03-09)
**Approach:** Dual-channel WordPress deployment — REST API (curl/Python) + AI Engine MCP

---

## Deployment Architecture

```
Claude Code (local)
    │
    ├── reads  → docs/design/pacerai-homepage_by_Claude_030526_1522.html
    ├── writes → src/homepage/index-build.html  (working copy)
    │
    ├── deploys via WordPress REST API (curl / Python urllib)
    │       │
    │       └── POST /wp-json/wp/v2/pages/25
    │
    └── deploys via AI Engine MCP (Claude Code tool)
            │
            ├── wp_get_post       — read page content
            ├── wp_update_post    — full content replacement
            ├── wp_alter_post     — surgical search-and-replace
            ├── wp_get_option     — read WP settings (show_on_front, etc.)
            ├── wp_upload_media   — upload images
            └── wp_get_post_snapshot — full page data in one call
                    │
                    └── getpacerai.com (WordPress.com hosted)
                            ├── Theme: Twenty Twenty-Four (default)
                            ├── Yoast SEO (active — manages <head> meta)
                            └── AI Engine plugin (provides MCP server)
```

---

## Two Deploy Methods

### Method 1: REST API (curl / Python)
Used for full content pushes. Requires shell env vars.

```bash
export WP_BASE_URL=https://getpacerai.com
export WP_USER=willsullivan5e7f50183a
export WP_APP_PASSWORD=[app password]
```

Deploy script (Python):
```python
content = open('src/homepage/index-build.html').read()
wrapped = "<!-- wp:html -->" + content + "<!-- /wp:html -->"
# POST to /wp-json/wp/v2/pages/25 with Basic Auth
```

### Method 2: AI Engine MCP (Claude Code tools)
Used for reads, surgical edits, and metadata operations. No env vars needed — credentials managed by MCP server config.

| Tool | Use Case |
|------|----------|
| `wp_get_post` | Read page content/status |
| `wp_update_post` | Full content replacement |
| `wp_alter_post` | Search-and-replace within content (caution: can mangle newlines in replacements) |
| `wp_get_option` | Check `page_on_front`, `show_on_front` settings |
| `wp_get_post_snapshot` | Full page data + meta + terms in one call |
| `wp_list_plugins` | Audit active plugins |

**Known MCP limitation:** `wp_alter_post` with `\n` in replacement strings stores literal `n` characters instead of newlines. Use REST API for full content pushes.

---

## Page Structure

The homepage (page ID 25) is a single `<!-- wp:html -->` Gutenberg block containing:

```
<style>
  ├── TT4 theme overrides (hide header/footer, dark bg, full-width)
  ├── CSS variables (:root)
  ├── Component styles (nav, hero, sections, footer)
  ├── Mobile responsive (@media max-width: 768px)
  └── Tablet responsive (@media max-width: 1024px)
</style>

<div id="pacerai-homepage">
  ├── <nav>           — Fixed top nav with logo, dropdown menus, CTA buttons
  │                     Mobile: hamburger menu with full-screen overlay
  ├── .hero           — Hero section with headline, CTAs, stats, badges
  ├── .preview-section — Dashboard preview (ARR waterfall mockup)
  ├── .logo-strip     — Social proof / partner logos
  ├── .section (use cases) — Use case menu strip + card grid
  ├── .how-section    — 4-step "How It Works"
  ├── .section (pillars) — 3-column platform pillars
  ├── .empathy-section — Problem/solution with expert card
  ├── .quote-section  — Testimonial
  ├── .cta-section    — Bottom CTA
  └── <footer>        — 5-column footer with legal bar
</div>

<script>
  └── Mobile nav: hamburger toggle + dropdown expand/collapse
</script>
```

### Header (Nav)
- Fixed position, semi-transparent background (desktop), solid dark (mobile)
- Desktop: logo + 6 nav items with hover dropdowns + Log In / Request Demo
- Mobile: logo + Request Demo + hamburger → full-screen slide-down menu
- Dropdowns use CSS `:hover` with invisible `::before` bridge to prevent hover gap
- Mobile dropdowns expand inline on tap via JS `mobile-expanded` class

### Footer
- 5-column grid: Brand, Platform, Use Cases, Comparisons, Company
- Bottom bar: copyright + legal links
- Mobile: 2-column grid, brand spans full width

---

## Theme: Twenty Twenty-Four

Switched from Beaver Builder (removed 2026-03-09) to WordPress default theme.

**TT4 overrides in content CSS:**
- Hide theme header/footer (`.wp-site-blocks > header/footer`)
- Force dark background on `html, body, .wp-site-blocks` (#080E1C)
- Remove content container constraints (`.is-layout-constrained`, `.has-global-padding`)
- Mobile: disable `backdrop-filter` on nav (it creates a containing block that traps fixed-position children)

**Why TT4:** Minimal, respects static front page setting, WordPress core team maintained. Our content is fully self-contained with inline CSS — theme only provides the shell.

---

## API Endpoints Used

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/wp-json/wp/v2/settings` | Get `page_on_front` ID |
| GET | `/wp-json/wp/v2/pages/25` | Read current homepage content |
| POST | `/wp-json/wp/v2/pages/25` | Update homepage content |
| GET | `/wp-json/wp/v2/pages` | List all pages (audit) |

---

## Authentication

- **REST API:** HTTP Basic Auth with Application Password
  - Variables: `WP_USER`, `WP_APP_PASSWORD`, `WP_BASE_URL`
  - Key name in WP admin: `claude-code`
- **MCP:** Credentials managed by AI Engine plugin configuration

---

## Asset Handling

Images must map to one of:
- Existing uploads at `https://getpacerai.com/wp-content/uploads/`
- Inline SVG (preferred for icons — logo, chevrons, decorative elements)
- Upload via `wp_upload_media` MCP tool for new assets

**Do not:** reference external CDNs, localhost paths, or data URIs for large images.

---

## Known Constraints

| Constraint | Impact |
|---|---|
| WordPress.com (no SSH) | Cannot edit theme PHP files — content-only updates |
| No WP-CLI access | Cannot flush object cache programmatically |
| Yoast SEO active | Must preserve `yoast_head` — do not overwrite meta fields |
| TT4 theme | Overrides needed to hide chrome and go full-width |
| MCP `wp_alter_post` | Mangles `\n` in replacements — use REST API for full pushes |
| `backdrop-filter` | Creates containing block — disabled on mobile nav |

---

## File Map

```
src/homepage/
└── index-build.html            # Complete page content (style + HTML + script), ready for API push

docs/design/
└── pacerai-homepage_by_Claude_030526_1522.html   # Original design mockup

docs/review/
├── pre-deploy-backup-*.json    # Backups before each deploy
├── checklist.md                # QA checklist
└── Issues.md                   # Known issues

docs/document/
└── changelog.md                # Running deploy log
```
