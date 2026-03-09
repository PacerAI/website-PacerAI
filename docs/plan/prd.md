# Product Requirements Document — Homepage v2

**Version:** 2.0
**Date:** March 2026 (updated 2026-03-09)
**Status:** Approved — Live

---

## 1. Navigation

### Header Menu (Desktop)
```
[Logo: Pacer AI]   Platform ▾   Solutions ▾   Resources ▾   Partners   Case Studies   Company ▾   [Log In]  [Request Demo]
```

- Logo: Inline SVG three-chevron mark + "Pacer AI" wordmark (Georgia serif)
- Dropdowns appear on hover with invisible bridge to prevent hover gap
- Log In links to `https://app.getpacerai.com/.auth/login/aad`
- Request Demo links to `https://calendly.com/pacerai`

### Header Menu (Mobile)
```
[Logo: Pacer AI]   [Request Demo]   [☰ Hamburger]
```

- Hamburger opens full-screen dark overlay menu
- Nav items stack vertically, tap chevron items to expand dropdowns inline
- X button closes menu and restores scroll

### Solutions Dropdown
Two-column grid:

**Use Cases:**
- ARR Snowball Board Reporting
- Customer Data Cube
- Virtual Data Room
- Exit Readiness

**Industry:**
- B2B SaaS
- PE-Backed SaaS
- Pre-IPO SaaS

### Footer Structure
```
Brand (logo + tagline)  |  Platform       |  Use Cases                    |  Comparisons       |  Company
                        |  Overview       |  ARR Snowball Board Reporting |  vs. Manual Excel  |  About Pacer AI
                        |  Data Ingestion |  Customer Data Cube           |  vs. Mosaic Tech   |  Newsletter
                        |  MS Fabric      |  Virtual Data Room            |  vs. Vena Solutions|  Blog
                        |  Power BI       |  Exit Readiness               |  vs. Pigment       |  Partners
                        |  AI Agents      |  MBR Automation               |  vs. Causal        |  Case Studies
                        |  Excel+Copilot  |  GTM Analytics                |  vs. Cube          |  Careers
                        |  Security       |                               |                    |  Contact
                        |  Integrations   |                               |                    |

Bottom bar: © 2025 Predictive Analytics Partners LLC · getpacerai.com  |  Privacy · Terms · Cookies · LinkedIn
```

Mobile footer: 2-column grid, brand spans full width.

---

## 2. Hero Section

**Headline:** Your ARR Snowball Report. Automated. Board-Ready.
**Subheadline:** Pacer AI transforms your Revenue data — CRM, billing, and reported — into due diligence-grade ARR Snowball reports, automatically. From raw data to board quality in days, not months.
**Primary CTA:** See a Live ARR Demo →
**Secondary CTA:** How It Works
**Visual:** Subtle grid background with radial gradient, floating data lines
**Below fold:** Hero badges (Microsoft Fabric, Power BI, AI Agents)

---

## 3. Dashboard Preview

ARR Snowball waterfall mockup in a browser-frame container:
- Metric cards (4-up): Total ARR, Net New ARR, Logo Retention, Net Revenue Retention
- ARR waterfall grid: Beginning ARR → New → Expansion → Contraction → Churn → Ending ARR
- Mini sparkline bars

---

## 4. Logo Strip / Social Proof

Technology partner logos/text: Microsoft Fabric, Power BI, Azure AI, Dynamics 365, HubSpot, Salesforce

---

## 5. Use Case Section

**Menu strip** of 9 use cases (3-col grid on mobile):
ARR Snowball Board Reporting, Customer Data Cube, Expansion Enablement, Whitespace Visibility, Bottoms-Up Forecasting, Roll-Fwd Sales Planning by Cohort, Virtual Data Room, Exit Readiness Package, Investor Diligence

**Card grid** (2-col desktop, 1-col mobile):
- Primary card: ARR Snowball Board Reporting (spans full width)
- Secondary cards: Customer Data Cube, Expansion & Whitespace Visibility, Virtual Data Room, Exit Readiness

---

## 6. How It Works

4 steps (4-col desktop, 1-col mobile):
1. Connect Your Data (CRM, billing, ERP)
2. Pacer Builds Your Foundation (Microsoft Fabric semantic model)
3. Intelligence Goes Live (Power BI dashboards, AI agents)
4. Board-Ready in Days (ARR Snowball report)

---

## 7. Platform Pillars

3 columns (1-col mobile):
1. Microsoft Fabric Foundation (data lakehouse, semantic models)
2. Power BI Intelligence Layer (dashboards, embedded analytics)
3. AI Agent Activation (Claude, GPT, Copilot ready)

---

## 8. Empathy / Guide Section

**Left column:** "What goes wrong" mistake list (4 items about ARR Snowball challenges)
**Right column:** Expert card with founder quote and credentials

---

## 9. Testimonial / Quote

Blockquote from B2B SaaS CFO with attribution.

---

## 10. CTA Section (Bottom)

**Headline:** See Your ARR Snowball. Live.
**Body:** Description of live demo offer
**Primary CTA:** Request a Live Demo
**Secondary CTA:** Talk to a RevOps Expert

---

## 11. SEO Requirements

| Field | Value |
|---|---|
| Page Title | Pacer AI — ARR Intelligence for PE-Backed SaaS |
| Meta Description | Pacer AI turns CRM, ERP, and HRIS data into board-ready ARR Snowball reports and AI agent intelligence. Built for Operating Partners and SaaS CFOs. |
| Primary Keyword | ARR Snowball reporting |
| Secondary Keywords | PE portfolio reporting, SaaS board reporting, operational data platform |
| Schema Type | Organization + SoftwareApplication |

**Status:** Page title and meta description must be set via Yoast in WP admin.

---

## 12. Technical Requirements

- **CMS:** WordPress.com hosted, Twenty Twenty-Four theme
- **Deploy:** WordPress REST API (Python) + AI Engine MCP (Claude Code tools)
- **Content format:** Single `<!-- wp:html -->` Gutenberg block with inline CSS
- **Fonts:** DM Sans (body) + Cormorant Garamond (headings) via Google Fonts
- **No JavaScript frameworks** — vanilla JS for mobile nav toggle only
- **Images:** Hosted on getpacerai.com CDN, inline SVG for icons
- **Mobile responsive:** Breakpoints at 768px (mobile) and 1024px (tablet)
- **Lighthouse targets:** Performance >= 85, SEO >= 90, Accessibility >= 90, Best Practices >= 90

### Removed (v2)
- ~~Beaver Builder Lite, Starter, Themer, Ultimate Addons~~ — deactivated and deleted
- ~~Beaver Builder theme~~ — replaced with Twenty Twenty-Four
- ~~Classic Editor plugin~~ — no longer needed
- ~~BB override CSS~~ (`.fl-post-header`, `.fl-post-content`, `#fl-main-content`) — removed from content

### Added (v2)
- AI Engine MCP plugin — provides WordPress MCP server for Claude Code tool access
- Twenty Twenty-Four theme overrides — hide theme chrome, force dark background
- Mobile hamburger nav with full-screen menu overlay
- Tablet responsive breakpoint (769–1024px)
- Nav dropdown hover bridge (CSS `::before` pseudo-element)

---

## 13. Deploy Infrastructure

### AI Engine MCP
The AI Engine WordPress plugin provides an MCP (Model Context Protocol) server that Claude Code connects to as a tool provider. This enables direct WordPress CRUD operations from Claude Code without shell env vars.

**Key capabilities:**
- Read/write posts and pages
- Upload media
- Read/update options and settings
- Search-replace within content (with caveats)
- List plugins, terms, users

**Limitation:** `wp_alter_post` mangles newlines in replacement strings. Full content pushes should use the REST API via Python.

See `docs/deploy/runbook.md` for the full tool reference.
