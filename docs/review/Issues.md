# Issues — Homepage Refresh v1

Identified during PLAN phase (2026-03-09). Must be addressed before or during DEPLOY.

---

## 1. Slug is `no-title`

- **Impact:** SEO — the page slug should ideally be `/` or a meaningful slug, not `no-title`
- **Action:** Flag for Will. Changing the slug would alter the permalink. Must be done in WP admin.
- **Status:** Pending human review

## 2. Yoast meta description is missing

- **Impact:** SEO — Yoast head includes the admin notice: "this page does not show a meta description because it does not have one."
- **PRD specifies:** "Pacer AI turns CRM, ERP, and HRIS data into board-ready ARR Snowball reports and AI agent intelligence. Built for Operating Partners and SaaS CFOs."
- **Action:** Set via MCP `wp_update_post_meta` with `_yoast_wpseo_metadesc` key.
- **Status:** RESOLVED (2026-03-10) — Meta descriptions set on all 18 published pages via MCP.

## 3. Page title is generic ("Home")

- **Impact:** SEO — current `<title>` renders as "Home - Get Pacer AI"
- **PRD specifies:** "Pacer AI — ARR Intelligence for PE-Backed SaaS"
- **Action:** Set via MCP `wp_update_post_meta` with `_yoast_wpseo_title` key.
- **Status:** RESOLVED (2026-03-10) — Title set to "Pacer AI — ARR Intelligence for PE-Backed SaaS" via MCP.

## 4. CTA says "Learn more" instead of "Request a Demo"

- **Impact:** Conversion — PRD requires "Request a Demo" as primary CTA
- **Action:** Will be fixed in BUILD phase when new design is applied.
- **Status:** Will be resolved in build

## 5. Current content is long-form prose (16,117 chars)

- **Impact:** The entire page content will be replaced by the approved design mockup.
- **Action:** Current content saved to `docs/old_content.md` for reference. Pre-deploy backup will also be created per runbook.
- **Status:** Archived

## 6. Featured image (media 433) rendering above page content

- **Impact:** TT4 theme renders the WordPress featured image above page content. The Pacer AI OG image (media ID 433) was set as featured image on all 18 pages, causing a large logo graphic to display above the nav on every page.
- **Action:** Removed featured images from all pages via REST API (`featured_media: 0`). Our pages use inline CSS for all visuals — no WordPress featured images needed.
- **Status:** RESOLVED (2026-03-10)
- **Note:** Do not set featured images on Pacer AI pages. The OG image for social sharing is handled by Yoast (`_yoast_wpseo_opengraph-image`) and does not require a featured image.
