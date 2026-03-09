# Architecture — Homepage Refresh v1

**Date:** March 2026  
**Approach:** WordPress REST API (no SSH/theme file access required)

---

## Deployment Architecture

```
Claude Code (local)
    │
    ├── reads  → docs/design/pacerai-homepage_by_Claude_030526_1522.html
    ├── writes → src/homepage/index-build.html  (working copy)
    │
    └── deploys via WordPress REST API
            │
            └── POST /wp-json/wp/v2/pages/[HOMEPAGE_ID]
                    │
                    └── getpacerai.com (WordPress.com hosted)
                            └── Yoast SEO (active)
                            └── Active theme (to be confirmed)
```

---

## API Endpoints Used

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/wp-json/wp/v2/settings` | Get `page_on_front` ID |
| GET | `/wp-json/wp/v2/pages/[ID]` | Read current homepage content |
| POST | `/wp-json/wp/v2/pages/[ID]` | Update homepage content |
| GET | `/wp-json/wp/v2/pages` | List all pages (audit) |

---

## Authentication

- Method: HTTP Basic Auth with Application Password
- Variables: `WP_USER`, `WP_APP_PASSWORD`, `WP_BASE_URL`
- Scope: Edit Pages (minimum required permission)
- Key name in WP admin: `claude-code`

---

## Content Strategy

WordPress.com REST API accepts **HTML content** in the `content` field. The page template and `<head>` are managed by WordPress — we only control the `<body>` content block.

**Extraction approach:**
1. Parse `docs/design/pacerai-homepage_by_Claude_030526_1522.html`
2. Extract everything between `<body>` and `</body>`
3. Strip any `<script>` tags that reference localhost or relative paths
4. Replace relative image `src` paths with absolute WP CDN URLs
5. Submit as `content` field in REST API PATCH request

---

## Asset Handling

Images in the design mockup must map to one of:
- Existing uploads at `https://getpacerai.com/wp-content/uploads/`
- Inline SVG (preferred for icons and simple graphics)
- Placeholder with note for manual upload

**Do not:** reference external CDNs, localhost paths, or data URIs for large images.

---

## Known Constraints

| Constraint | Impact |
|---|---|
| WordPress.com (no SSH) | Cannot edit theme PHP files — content-only updates |
| No WP-CLI access | Cannot flush object cache programmatically |
| Yoast SEO active | Must preserve `yoast_head` — do not overwrite meta fields |
| REST API content field | Gutenberg blocks may conflict with raw HTML — test first |

---

## Gutenberg Block Consideration

WordPress.com uses the Gutenberg block editor. Posting raw HTML via the REST API may be wrapped in a Classic Block (`<!-- wp:html -->`). To avoid this:

Option A — Use `content.raw` with block markup (preferred if Gutenberg is active):
```json
{"content": "<!-- wp:html --><div>...</div><!-- /wp:html -->"}
```

Option B — Disable Gutenberg on the homepage page and post raw HTML (requires plugin access — may not be available on WordPress.com).

**Claude Code should test Option A first and report the rendered output.**

---

## File Map

```
src/homepage/
└── index-build.html        # Extracted body content, ready for API push

docs/design/
└── pacerai-homepage_by_Claude_030526_1522.html   # Source of truth

docs/review/
└── pre-deploy-backup-[DATE].json    # Backup of current live content

docs/document/
└── changelog.md            # Running deploy log
```