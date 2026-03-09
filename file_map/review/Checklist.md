# Review Checklist — Homepage Refresh v1

Run this checklist after BUILD and before DEPLOY. Claude Code should work through each item and record pass/fail with notes.

**Date:** _______________  
**Reviewer:** _______________  
**Build file:** `src/homepage/index-build.html`

---

## 1. Content Integrity

- [ ] Hero headline matches PRD: "Turn operational data into agent intelligence."
- [ ] Primary CTA present: "Request a Demo"
- [ ] ARR Snowball section present and accurate
- [ ] Navigation structure matches PRD (Platform, Solutions, Resources, Customers, Company)
- [ ] Footer structure matches PRD
- [ ] No placeholder text (lorem ipsum, [TBD], etc.)
- [ ] No references to localhost, staging URLs, or relative paths

---

## 2. Visual / Brand

- [ ] Font: Georgia serif (check CSS `font-family` declarations)
- [ ] Background: White (#FFFFFF) on main content areas
- [ ] No purple gradients or playful UI elements
- [ ] CTA buttons: consistent style, correct label ("Request a Demo")
- [ ] Logo present and resolves to correct WP CDN URL
- [ ] All images load (no broken `src` attributes)

---

## 3. SEO

- [ ] Page `<title>` set (or confirmed via Yoast): "Pacer AI — ARR Intelligence for PE-Backed SaaS"
- [ ] Meta description present (via Yoast — do not overwrite via API)
- [ ] H1 present and unique on page
- [ ] H2s follow logical hierarchy
- [ ] No duplicate H1s
- [ ] Canonical URL confirmed as `https://getpacerai.com/`
- [ ] OG tags intact (verified via Yoast `yoast_head` field in API response)

---

## 4. Technical

- [ ] HTML validates (no unclosed tags, malformed attributes)
- [ ] No inline `<script>` blocks with external dependencies
- [ ] No `<iframe>` embeds from unapproved sources
- [ ] Mobile viewport meta tag present in `<head>` (WordPress manages this — confirm not stripped)
- [ ] No JavaScript errors in browser console
- [ ] Page loads under 3 seconds on fast 3G (Chrome DevTools)

---

## 5. Lighthouse Audit

Run: `npx lighthouse https://getpacerai.com --output=json --output-path=docs/review/lighthouse-[DATE].json`

| Category | Target | Actual | Pass? |
|---|---|---|---|
| Performance | ≥ 85 | | |
| Accessibility | ≥ 90 | | |
| Best Practices | ≥ 90 | | |
| SEO | ≥ 90 | | |

---

## 6. Cross-Browser / Device

- [ ] Chrome (desktop)
- [ ] Safari (desktop)
- [ ] Mobile Safari (iPhone 14 viewport: 390px)
- [ ] Chrome Mobile (Android)
- [ ] iPad Pro (1024px viewport)

---

## 7. Pre-Deploy Backup

- [ ] Current live homepage content saved to `docs/review/pre-deploy-backup-[DATE].json`
- [ ] Backup includes: page ID, title, content, modified date, yoast_head

---

## Sign-off

| Item | Status | Notes |
|---|---|---|
| Content | | |
| Brand | | |
| SEO | | |
| Technical | | |
| Lighthouse | | |
| Cross-browser | | |
| Backup | | |

**Ready to deploy:** YES / NO  
**Approved by:** _______________