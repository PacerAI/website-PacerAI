# Deploy Runbook — getpacerai.com

**READ THIS BEFORE DEPLOYING TO THE LIVE SITE.**

This runbook is executed by Claude Code. Every step must be completed in order.

---

## Deploy Method: REST API via Python

All deploys use the WordPress REST API with Basic Auth. The `requests` library is preferred.

### Required Environment Variables

```bash
# Set in ~/.zshrc
export WP_BASE_URL=https://getpacerai.com
export WP_USER=willsullivan5e7f50183a
export WP_APP_PASSWORD=[app password from WP admin]
```

Verify: `source ~/.zshrc && echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...`

---

## Page Registry

Always reference `CLAUDE.md` for the authoritative page registry. Key pages:

| Page | WP ID | Source File |
|------|-------|-------------|
| Home | 25 | `src/homepage/index-build.html` |
| Blog | 230 | `src/blog/index-build.html` |
| Platform Overview | 371 | `src/platform/overview.html` |
| ARR Snowball | 372 | `src/solutions/arr-snowball.html` |
| Customer Data Cube | 373 | `src/solutions/customer-data-cube.html` |
| About | 374 | `src/company/about.html` |
| Contact | 375 | `src/company/contact.html` |

Parent placeholder pages (no content): Platform (362), Solutions (364), Company (366).

---

## Pre-Flight Checks

### 1. Verify environment
```bash
source ~/.zshrc
echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...
```

### 2. Backup current page (for major changes)
```bash
source ~/.zshrc
DATE=$(date +%Y%m%d-%H%M)
curl -s -u "$WP_USER:$WP_APP_PASSWORD" \
  "$WP_BASE_URL/wp-json/wp/v2/pages/25?context=edit" \
  > docs/review/pre-deploy-backup-$DATE.json
```

### 3. Confirm review checklist is complete
Read `docs/review/checklist.md`. Critical items must be checked.

---

## Deploy: Single Page

```python
import requests, os

base_url = os.environ['WP_BASE_URL']
auth = (os.environ['WP_USER'], os.environ['WP_APP_PASSWORD'])

with open('src/platform/overview.html') as f:
    html = f.read()

content = f"<!-- wp:html -->{html}<!-- /wp:html -->"
resp = requests.post(f"{base_url}/wp-json/wp/v2/pages/371", json={"content": content}, auth=auth)

if resp.status_code == 200:
    print(f"OK — {resp.json()['link']}")
else:
    print(f"FAILED — HTTP {resp.status_code}: {resp.text[:300]}")
```

## Deploy: All Pages (Batch)

Use this when shared elements (nav, footer, base CSS) have changed.

```python
import requests, os

base_url = os.environ['WP_BASE_URL']
auth = (os.environ['WP_USER'], os.environ['WP_APP_PASSWORD'])
api = f"{base_url}/wp-json/wp/v2/pages"
src = "src"  # relative to repo root

pages = [
    {"id": 25,  "title": "Home",               "file": f"{src}/homepage/index-build.html"},
    {"id": 230, "title": "Blog",               "file": f"{src}/blog/index-build.html"},
    {"id": 371, "title": "Platform Overview",   "file": f"{src}/platform/overview.html"},
    {"id": 372, "title": "ARR Snowball",        "file": f"{src}/solutions/arr-snowball.html"},
    {"id": 373, "title": "Customer Data Cube",  "file": f"{src}/solutions/customer-data-cube.html"},
    {"id": 374, "title": "About",               "file": f"{src}/company/about.html"},
    {"id": 375, "title": "Contact",             "file": f"{src}/company/contact.html"},
]

for p in pages:
    with open(p['file']) as f:
        html = f.read()
    content = f"<!-- wp:html -->{html}<!-- /wp:html -->"
    resp = requests.post(f"{api}/{p['id']}", json={"content": content}, auth=auth)
    status = "OK" if resp.status_code == 200 else f"FAIL ({resp.status_code})"
    print(f"  {status} — {p['title']} (ID {p['id']})")
```

## Deploy: New Page (First Time)

```python
# 1. Create the HTML source file in src/
# 2. Create the WordPress page:
resp = requests.post(f"{base_url}/wp-json/wp/v2/pages", json={
    "title": "Page Title",
    "slug": "page-slug",
    "parent": 364,  # Parent page ID (Platform=362, Solutions=364, Company=366)
    "status": "publish",
    "content": f"<!-- wp:html -->{html}<!-- /wp:html -->"
}, auth=auth)
new_id = resp.json()['id']
print(f"Created page ID {new_id} at {resp.json()['link']}")
# 3. IMPORTANT: Update CLAUDE.md page registry with the new ID
```

---

## Deploy: Blog Post

See **[Blog Post Guide](blog-post-guide.md)** for the complete workflow — writing content, building from template, deploying, and updating the blog listing.

Quick version: ask Claude Code to "write a blog post about [topic] and publish it."

---

## Post-Deploy Verification

```bash
# Verify all pages return HTTP 200
source ~/.zshrc
for url in \
  "https://getpacerai.com/" \
  "https://getpacerai.com/blog/" \
  "https://getpacerai.com/platform/overview/" \
  "https://getpacerai.com/solutions/arr-snowball-board-reporting/" \
  "https://getpacerai.com/solutions/customer-data-cube/" \
  "https://getpacerai.com/company/about/" \
  "https://getpacerai.com/company/contact/"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  echo "$code  $url"
done
```

### Log the deploy
Append to `docs/document/changelog.md` with date, page IDs, changes, and backup reference.

### Lighthouse audit (optional)
```bash
npx lighthouse https://getpacerai.com --output=json --output-path=docs/review/lighthouse-$(date +%Y%m%d).json
```

---

## Rollback Procedure

Restore from backup:
```python
import json, requests, os

backup = json.load(open('docs/review/pre-deploy-backup-[DATE].json'))
content = backup['content']['raw']

resp = requests.post(
    f"{os.environ['WP_BASE_URL']}/wp-json/wp/v2/pages/25",
    json={"content": content},
    auth=(os.environ['WP_USER'], os.environ['WP_APP_PASSWORD'])
)
print(f"Rollback {'OK' if resp.status_code == 200 else 'FAILED'}")
```

---

## Content Format

Every page source file follows this structure:

```html
<style>
  /* TT4 overrides: hide theme chrome, force dark bg, remove constraints */
  /* .wp-block-post-title, .wp-block-spacer { display: none !important; } */
  /* CSS variables, component styles, responsive breakpoints */
</style>
<div id="pacerai-homepage">
  <nav><!-- Shared nav --></nav>
  <!-- Page-specific content -->
  <footer><!-- Shared footer --></footer>
</div>
<script>/* Mobile nav JS */</script>
```

- No `<html>`, `<head>`, or `<body>` tags — WordPress manages the document shell
- Content is wrapped in `<!-- wp:html -->...<!-- /wp:html -->` during deploy
- Google Fonts loaded by WordPress — no `<link>` tags needed
- All CSS scoped under `#pacerai-homepage`
