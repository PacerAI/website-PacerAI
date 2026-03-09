# Deploy Runbook — Homepage v2

**READ THIS BEFORE TOUCHING THE LIVE SITE.**

This runbook is executed by Claude Code. Every step must be completed in order. Do not skip steps.

---

## Two Deploy Methods

### Method A: AI Engine MCP (Preferred for reads and small edits)
Claude Code connects to WordPress via the AI Engine MCP plugin. No env vars needed.

```
Tools available:
  wp_get_post(ID=25)           — read page content
  wp_update_post(ID=25, ...)   — full content replacement
  wp_alter_post(ID=25, ...)    — search-and-replace (caution: mangles newlines)
  wp_get_option(key=...)       — read WP settings
  wp_get_post_snapshot(ID=25)  — full page data in one call
```

**Known limitation:** `wp_alter_post` with `\n` in replacement strings stores literal `n` instead of newlines. Use Method B for full content pushes.

### Method B: REST API via Python (Preferred for full content deploys)
Requires shell environment variables:

```bash
export WP_BASE_URL=https://getpacerai.com
export WP_USER=willsullivan5e7f50183a
export WP_APP_PASSWORD=[app password from WP admin]
```

Verify: `echo $WP_BASE_URL && echo $WP_USER && echo ${WP_APP_PASSWORD:0:4}...`

---

## Pre-Flight Checks

### 1. Verify homepage page ID
```python
# Via MCP:
wp_get_option(key="page_on_front")  # Should return "25"
wp_get_option(key="show_on_front")  # Should return "page"
```
```bash
# Via REST API:
curl -s -u "$WP_USER:$WP_APP_PASSWORD" \
  "$WP_BASE_URL/wp-json/wp/v2/settings" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('Homepage ID:', d.get('page_on_front'))"
```
If `page_on_front` is 0 or empty, **stop and alert Will**.

### 2. Backup current homepage

**Via MCP:**
```
wp_get_post(ID=25)
# Save result to docs/review/pre-deploy-backup-[DATE].json
```

**Via REST API:**
```bash
DATE=$(date +%Y%m%d-%H%M)
curl -s -u "$WP_USER:$WP_APP_PASSWORD" \
  "$WP_BASE_URL/wp-json/wp/v2/pages/25" \
  > docs/review/pre-deploy-backup-$DATE.json
```
Confirm the file is non-empty before proceeding.

### 3. Confirm review checklist is complete
Read `docs/review/checklist.md`. Critical items must be checked.

---

## Deploy

### 4. Prepare content payload
The build file is `src/homepage/index-build.html`. It contains `<style>`, `<div id="pacerai-homepage">`, and `<script>` — no `<html>/<head>/<body>` wrappers.

Wrap in Gutenberg HTML block:
```
<!-- wp:html -->[CONTENT]<!-- /wp:html -->
```

### 5. Push to WordPress

**Via Python (recommended for full pushes):**
```python
import json, urllib.request, os, base64

with open('src/homepage/index-build.html') as f:
    content = f.read()

wrapped = "<!-- wp:html -->" + content + "<!-- /wp:html -->"
url = os.environ['WP_BASE_URL'] + '/wp-json/wp/v2/pages/25'
data = json.dumps({'content': wrapped}).encode('utf-8')
creds = base64.b64encode(
    f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}".encode()
).decode()

req = urllib.request.Request(url, data=data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', f'Basic {creds}')

resp = urllib.request.urlopen(req)
result = json.loads(resp.read())
print('Status:', result.get('status'), '| ID:', result.get('id'))
```

**Via MCP (for surgical edits only):**
```
wp_alter_post(ID=25, field="post_content", search="old text", replace="new text")
```

### 6. Verify deploy

**Via MCP:**
```
wp_get_post(ID=25)
# Check rendered content for expected elements
```

**Manual:**
- Open https://getpacerai.com in browser
- Confirm hero headline, nav, footer render correctly
- Test on mobile viewport

---

## Post-Deploy

### 7. Log the deploy
Append to `docs/document/changelog.md` with date, changes, content size, and backup reference.

### 8. Lighthouse audit (optional)
```bash
npx lighthouse https://getpacerai.com --output=json --output-path=docs/review/lighthouse-$(date +%Y%m%d).json
```

---

## Rollback Procedure

If anything is wrong after deploy, restore from backup:

```python
import json

backup = json.load(open('docs/review/pre-deploy-backup-[DATE].json'))
# For MCP backups (array format):
content = json.loads(backup[0]['text'])['post_content']
# For REST API backups (object format):
content = backup['content']['raw']

# Then push via REST API Method B
```

---

## AI Engine MCP Reference

The AI Engine WordPress plugin provides an MCP server that Claude Code connects to directly. Configuration is in Claude Code's MCP settings (not in this repo).

### Available Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| `wp_get_post` | Read post by ID | Returns title, content, status, dates |
| `wp_get_post_snapshot` | Full post data | Includes meta, terms, thumbnail, author |
| `wp_update_post` | Update post fields | Can set post_content, post_title, post_status |
| `wp_alter_post` | Search-replace in content | Supports regex. **Caution: mangles newlines** |
| `wp_get_option` | Read WP option | page_on_front, show_on_front, etc. |
| `wp_update_option` | Write WP option | Use carefully |
| `wp_list_plugins` | List installed plugins | Check active/inactive status |
| `wp_upload_media` | Upload image/file | Returns media ID and URL |
| `wp_get_media` | Read media item | Get URL, dimensions, alt text |
| `wp_count_posts` | Count posts by type/status | Quick audit tool |

### When to Use MCP vs REST API

| Scenario | Use |
|----------|-----|
| Read current page content | MCP `wp_get_post` |
| Check WP settings | MCP `wp_get_option` |
| Small text change (no newlines) | MCP `wp_alter_post` |
| Full content deploy | REST API (Python) |
| Upload new image | MCP `wp_upload_media` |
| Plugin audit | MCP `wp_list_plugins` |
| Backup before deploy | Either (MCP is faster) |
