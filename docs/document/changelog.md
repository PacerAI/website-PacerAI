# Changelog — website-PacerAI

All homepage deployments logged here in reverse chronological order.

Format per entry:
```
## [DATE] — [DESCRIPTION]
- **Page ID:** 
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Content size:** [before] → [after] characters
- **Changes:** 
- **Issues:** 
- **Live URL:** https://getpacerai.com
```

---

## 2026-03-09 — Mobile Responsive + Clean Theme Migration (v3)
- **Page ID:** 25
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Changes:**
  - Switched theme from Beaver Builder to Twenty Twenty-Four
  - Added TT4 override CSS (hide theme header/footer, force dark background, remove container constraints)
  - Added nav HTML (with hamburger menu for mobile) and footer HTML from design mockup
  - Fixed nav dropdown hover gap with invisible bridge pseudo-element
  - Full mobile responsive overhaul: nav hamburger menu, stacked hero CTAs, single-column grids for use cases/steps/pillars/empathy, 3-col use case menu strip, 2-col footer, tablet breakpoint
  - Fixed backdrop-filter containing block issue that trapped mobile menu inside 56px nav
- **Issues:** Will to deactivate/delete BB plugins and BB theme in WP admin
- **Backup:** docs/review/pre-deploy-backup-20260309-v2.json
- **Live URL:** https://getpacerai.com

---

## 2026-03-09 — Remove Beaver Builder CSS Hacks (v2)
- **Page ID:** 25
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Content size:** 52,349 → 50,238 characters
- **Changes:** Removed 30 lines of Beaver Builder override CSS (.fl-post-header hide, #pacerai-homepage breakout hack, .fl-post-content/fl-content-full/fl-page-content overrides). All design CSS and HTML preserved — only BB fight code removed. Prepares for BB plugin deactivation.
- **Issues:** Will needs to deactivate BB plugins in WP admin: Beaver Builder Lite, Beaver Builder Starter, Beaver Themer, Ultimate Addons for BB. Optionally deactivate Classic Editor.
- **Backup:** docs/review/pre-deploy-backup-20260309-v2.json
- **Live URL:** https://getpacerai.com

---

## 2026-03-09 — Homepage Refresh v1
- **Page ID:** 25
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Content size:** 16,117 → 52,349 characters
- **Changes:** Full homepage redesign from approved design mockup. New hero ("Your ARR Snowball Report. Automated. Board-Ready."), nav (Platform, Solutions, Resources, Partners, Customers, Company), ARR Snowball section, platform pillars, use cases, how-it-works steps, testimonial, founder section, CTA, and full footer. Replaced base64 data URI with WP CDN image (media ID 327). Log In button linked to app.getpacerai.com auth. DM Sans + Cormorant Garamond fonts. Inline CSS included.
- **Issues:** Yoast page title and meta description still need to be set in WP admin (see docs/review/Issues.md)
- **Backup:** docs/review/pre-deploy-backup-20260309.json
- **Live URL:** https://getpacerai.com