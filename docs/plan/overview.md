# Project Overview — Pacer AI Homepage

**Sprint:** Website Refresh v2
**Date:** March 2026 (updated 2026-03-09)
**Owner:** Will Sullivan, Founder — Pacer AI
**Status:** Live — Ongoing Optimization

---

## Goal

Deploy and maintain a production homepage for getpacerai.com that clearly communicates Pacer AI's value proposition to PE-backed SaaS operators and converts visitors into demo requests.

## Problem Statement

The original homepage did not reflect Pacer AI's positioning as a board-level ARR intelligence platform. It lacked the financial-professional aesthetic and specific use case clarity needed to resonate with Operating Partners, CFOs, and RevOps leaders evaluating operational data tools.

## What Was Done (v1 → v2)

### v1 (2026-03-09)
- Full homepage redesign deployed via WordPress REST API
- New hero, ARR Snowball section, platform pillars, use cases, testimonial, CTA
- Beaver Builder override CSS included to fight BB container constraints

### v2 (2026-03-09)
- Removed Beaver Builder entirely (plugins + theme)
- Switched to Twenty Twenty-Four theme with clean overrides
- Added nav and footer HTML from design mockup
- Full mobile responsive implementation (hamburger nav, stacked layouts)
- Fixed dropdown hover gap, backdrop-filter containing block issue
- Established dual deploy workflow: REST API + AI Engine MCP

## Success Criteria

- [x] Redesigned homepage live at getpacerai.com
- [x] Primary CTA ("Request a Demo") above the fold
- [x] ARR Snowball use case clearly featured as primary product story
- [x] Navigation with dropdowns (Platform, Solutions, Resources, Partners, Case Studies, Company)
- [x] Full footer with Platform, Use Cases, Comparisons, Company columns
- [x] Mobile-responsive with hamburger nav on phone viewports
- [x] Beaver Builder removed — clean Twenty Twenty-Four theme
- [x] Dual deploy workflow operational (REST API + MCP)
- [ ] Lighthouse Performance score >= 85
- [ ] Lighthouse SEO score >= 90
- [ ] Yoast SEO metadata set (page title + meta description)
- [ ] SEO/AEO audit agent built

## Scope — In

- Homepage only (`/`)
- Navigation menu structure (header + mobile hamburger)
- Footer structure (Platform, Use Cases, Comparisons, Company)
- Mobile responsive design
- Deploy infrastructure (REST API + MCP)
- SEO/AEO optimization (planned)

## Scope — Out

- Blog, product pages, or any other existing pages
- WordPress theme customization beyond CSS overrides
- Server-side changes (no SSH access on WordPress.com)

## Target Audience

| Persona | Title | Company Stage |
|---|---|---|
| Primary | Operating Partner | PE firm, 3–15 portfolio companies |
| Primary | CFO / VP Finance | $50M–$500M ARR SaaS |
| Secondary | Head of RevOps | $50M–$500M ARR SaaS |
| Secondary | CRO | Growth-stage SaaS |

## Design References

- Design mockup (source of truth): `docs/design/pacerai-homepage_by_Claude_030526_1522.html`
- Live build file: `src/homepage/index-build.html`

## Timeline

| Phase | Owner | Status |
|---|---|---|
| Plan | Will | Done |
| Design | Claude (claude.ai) | Done — mockup approved |
| Build | Claude Code | Done — v2 live |
| Review | Will | Done — visual review complete |
| Document | Claude Code | Done — docs updated |
| Deploy | Claude Code | Done — live at getpacerai.com |
| Optimize | Claude Code | Next — SEO/AEO agent, Lighthouse audit |
