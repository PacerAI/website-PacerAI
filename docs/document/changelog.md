# Changelog — website-PacerAI

All deployments logged here in reverse chronological order.

---

## 2026-03-10 — New Blog Post + Yoast SEO + Featured Image Fix
- **Pages deployed:** New blog post (441), updated blog listing (230)
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Changes:**
  - Published "Why LLMs Can't Build Your ARR Snowball from Operational Data" (page 441)
  - Set Yoast meta descriptions and page titles on all 18 published pages via MCP `wp_update_post_meta`
  - Set parent placeholder pages (362, 364, 366) and Login (134) to `noindex`
  - Removed featured image (media 433) from all 18 pages — TT4 was rendering it above content
  - Created `/blog-post` skill with draft preview and two review gates
  - Updated `/blog-post` skill with content voice preferences (plain language, linking requirements)
  - Homepage JSON-LD added (Organization, WebSite, WebPage schemas)
  - Blog post FAQ schema added (FAQPage with Q&A pairs per post)
  - SEO/AEO audit run, report saved to `docs/review/seo-audit-getpacerai-20260310.md`
- **Issues resolved:** #2 (missing meta descriptions), #3 (generic page title), #6 (featured image above content)
- **New source files:**
  - `src/blog/posts/content-441.html`, `src/blog/posts/441-build.html`
  - `.claude/skills/blog-post/SKILL.md`
  - `docs/deploy/blog-post-guide.md`
  - `docs/review/seo-audit-getpacerai-20260310.md`

---

## 2026-03-10 — Blog System: JSON-LD Schema + Category Filtering + BB Cleanup
- **Pages deployed:** Blog listing (230), 5 blog posts (358, 360, 368, 376, 378)
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Changes:**
  - Added JSON-LD structured data to all blog pages (Article schema on posts, CollectionPage + ItemList on listing)
  - Added client-side category pill filtering (vanilla JS, `data-category` attributes)
  - Confirmed no Beaver Builder CSS remains in any source files
  - Only 1 BB plugin remains: "Ultimate Addons for Beaver Builder - Lite" (needs manual deactivation)
  - Created SEO/AEO audit Claude Skill at `Claude-skills/seo-aeo-audit/`
- **Schema types deployed:**
  - Blog posts: `Article` with headline, datePublished, author (Organization), publisher with logo, articleSection
  - Blog listing: `CollectionPage` + `ItemList` with 5 ListItems
- **Issues:** Will to deactivate "Ultimate Addons for BB - Lite" plugin in WP admin

---

## 2026-03-10 — P1 Site Expansion: 5 New Pages + Cross-Linking + Blog Update
- **Pages deployed:**
  - Platform Overview (ID 371) → https://getpacerai.com/platform/overview/
  - ARR Snowball Board Reporting (ID 372) → https://getpacerai.com/solutions/arr-snowball-board-reporting/
  - Customer Data Cube (ID 373) → https://getpacerai.com/solutions/customer-data-cube/
  - About (ID 374) → https://getpacerai.com/company/about/
  - Contact (ID 375) → https://getpacerai.com/company/contact/
- **Parent pages created:** Platform (362), Solutions (364), Company (366) — empty placeholders for URL hierarchy
- **Deployed by:** Claude Code
- **Approved by:** Will Sullivan
- **Changes:**
  - Built 5 P1 pages as standalone HTML files with inline CSS matching homepage design system
  - Each page follows shared pattern: TT4 overrides, CSS variables, nav, page content, footer, mobile JS
  - Cross-linked all 7 pages (homepage, blog, platform, ARR snowball, customer data cube, about, contact) at nav, footer, and content-level CTAs/links
  - Added `.wp-block-post-title, .wp-block-spacer { display: none }` to all page files to fix TT4 page title gap
  - Updated blog nav/footer links to match P1 cross-linking
  - Redeployed homepage (ID 25) and blog (ID 230) with updated cross-links
  - Fixed Solutions/Company parent page titles (were "usolutions"/"ucompany" from sed issue)
- **New source files:**
  - `src/platform/overview.html`
  - `src/solutions/arr-snowball.html`
  - `src/solutions/customer-data-cube.html`
  - `src/company/about.html`
  - `src/company/contact.html`
- **Documentation updated:** CLAUDE.md, AGENTS.md, README.md, architecture.md, runbook.md, changelog.md, Internal_Documentation.md, overview.md
- **Issues:** Yoast SEO metadata not yet set for new pages

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