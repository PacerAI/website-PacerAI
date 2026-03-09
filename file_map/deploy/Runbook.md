# Deploy Runbook — Homepage Refresh v1

**READ THIS BEFORE TOUCHING THE LIVE SITE.**

This runbook is executed by Claude Code. Every step must be completed in order. Do not skip steps.

---

## Pre-Flight Checks

### 1. Verify environment variables
```bash
echo "URL: $WP_BASE_URL"
echo "USER: $WP_USER"
echo "PASS: ${WP_APP_PASSWORD:0:4}..."
```
All three must be non-empty. Stop if any are missing.

### 2. Confirm homepage page ID
```bash
curl -s -u "$WP_USER:$WP_APP_PASSWORD" \
  "$WP_BASE_URL/wp-json/wp/v2/settings" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('Homepage ID:', d.get('page_on_front'))"
```
Record the ID. If `page_on_front` is 0 or empty, **stop and alert Will** — no static homepage is set.

### 3. Backup current homepage
```bash
HOMEPAGE_ID=[ID from step 2]
DATE=$(date +%Y%m%d-%H%M)

curl -s -u "$WP_USER:$WP_APP_PASSWORD" \
  "$WP_BASE_URL/wp-json/wp/v2/pages/$HOMEPAGE_ID" \
  > docs/review/pre-deploy-backup-$DATE.json

echo "Backup saved: docs/review/pre-deploy-backup-$DATE.json"
```
Confirm the file is non-empty before proceeding.

### 4. Confirm review checklist is complete
Read `docs/review/checklist.md`. Every item must be checked. If any are unchecked, stop.

---

## Deploy

### 5. Prepare content payload
The build file is `src/homepage/index-build.html`. This file must contain only the `<body>` content — no `<html>`, `<head>`, or `<body>` tags.

Wrap in Gutenberg HTML block:
```
<!-- wp:html -->
[CONTENT FROM src/homepage/index-build.html]
<!-- /wp:html -->
```

### 6. Push to WordPress
```bash
HOMEPAGE_ID=[confirmed ID]
CONTENT=$(cat src/homepage/index-build.html)

curl -s -X POST \
  -u "$WP_USER:$WP_APP_PASSWORD" \
  -H "Content-Type: application/json" \
  -d "{\"content\": \"<!-- wp:html -->$CONTENT<!-- /wp:html -->\"}" \
  "$WP_BASE_URL/wp-json/wp/v2/pages/$HOMEPAGE_ID" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('Status:', d.get('status'), '| Modified:', d.get('modified'))"
```

Expected output: `Status: publish | Modified: [current timestamp]`

If status is not `publish` or the call returns an error, **stop and report**.

---

## Post-Deploy Verification

### 7. Fetch live page and verify
```bash
curl -s "https://getpacerai.com/" | grep -i "turn operational data" | head -3
```
Should return the hero headline. If empty, content did not deploy correctly.

### 8. Visual check
Open `https://getpacerai.com` in browser and confirm:
- Hero headline visible
- Navigation renders correctly
- CTA button present
- No broken layout or missing images

### 9. Log the deploy
Append to `docs/document/changelog.md`:
```markdown
## [DATE] — Homepage Refresh v1
- **Page ID:** [ID]
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Content size:** [before chars] → [after chars]
- **Changes:** Full homepage redesign — new hero, ARR Snowball section, updated nav/footer
- **Issues:** [none / describe any]
- **Live URL:** https://getpacerai.com
```

---

## Rollback Procedure

If anything is wrong after deploy, restore from backup immediately:

```bash
HOMEPAGE_ID=[ID]
BACKUP_FILE=docs/review/pre-deploy-backup-[DATE].json

ORIGINAL_CONTENT=$(python3 -c "
import json, sys
d = json.load(open('$BACKUP_FILE'))
print(d['content']['raw'])
")

curl -s -X POST \
  -u "$WP_USER:$WP_APP_PASSWORD" \
  -H "Content-Type: application/json" \
  -d "{\"content\": \"$ORIGINAL_CONTENT\"}" \
  "$WP_BASE_URL/wp-json/wp/v2/pages/$HOMEPAGE_ID"

echo "Rollback complete. Verify at https://getpacerai.com"
```