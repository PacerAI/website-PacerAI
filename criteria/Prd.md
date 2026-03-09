# Product Requirements Document — Homepage Refresh v1

**Version:** 1.0  
**Date:** March 2026  
**Status:** Approved

---

## 1. Navigation

### Header Menu (Desktop)
```
[Logo]   Platform   Solutions ▾   Resources   Customers   Company   [Request a Demo →]
```

**Solutions dropdown:**
- ARR Snowball Board Reporting
- Customer Data Cube
- Virtual Data Room
- Exit Readiness

### Footer Structure
```
Column 1: Platform        Column 2: Solutions       Column 3: Resources
- Overview                - ARR Snowball            - Blog
- Data Lake               - Customer Data Cube      - Documentation  
- Semantic Models         - Virtual Data Room       - Case Studies
- AI Agents               - Exit Readiness

Column 4: Company         Column 5: Compare
- About                   - vs. Tableau
- Careers                 - vs. PowerBI
- Contact                 - vs. Looker

Bottom bar: © 2026 Pacer AI · Privacy Policy · Terms of Service
```

---

## 2. Hero Section

**Headline:** Turn operational data into agent intelligence.  
**Subheadline:** Pacer AI connects your CRM, ERP, and HRIS data into board-ready ARR intelligence — built for PE-backed SaaS operators.  
**Primary CTA:** Request a Demo  
**Secondary CTA:** See How It Works  
**Visual:** ARR Snowball / waterfall chart visualization  

---

## 3. Social Proof Bar

Logo strip of target customer types or analyst quotes. If no logos available, use a single strong quote with attribution.

---

## 4. Primary Use Case — ARR Snowball

**Section headline:** Board-ready ARR reporting. No data team required.  
**Body:** 3–4 sentence explanation of ARR Snowball output — what it produces, who uses it, how fast.  
**Supporting visual:** Screenshot or mockup of the ARR waterfall output  
**CTA:** See the ARR Snowball →

---

## 5. Platform Section

**Section headline:** One platform. From raw data to agent-ready intelligence.  
Three columns:
1. **Ingest** — Connect CRM, ERP, HRIS, warehouse
2. **Model** — Semantic layer built for AI and dashboards
3. **Activate** — Agents, Excel CoPilot, board reporting

---

## 6. Secondary Use Cases

Cards or horizontal scroll:
- Customer Data Cube
- Virtual Data Room
- Exit Readiness

---

## 7. How It Works (Optional)

Numbered steps or timeline:
1. Connect your data sources
2. Pacer builds your semantic model
3. Agents and dashboards go live in days

---

## 8. CTA Section (Bottom)

**Headline:** Ready to turn your data into intelligence?  
**CTA:** Request a Demo  
**Subtext:** No data team required. Live in 2 weeks.

---

## 9. SEO Requirements

| Field | Value |
|---|---|
| Page Title | Pacer AI — ARR Intelligence for PE-Backed SaaS |
| Meta Description | Pacer AI turns CRM, ERP, and HRIS data into board-ready ARR Snowball reports and AI agent intelligence. Built for Operating Partners and SaaS CFOs. |
| Primary Keyword | ARR Snowball reporting |
| Secondary Keywords | PE portfolio reporting, SaaS board reporting, operational data platform |
| Schema Type | Organization + SoftwareApplication |

---

## 10. Technical Requirements

- WordPress REST API delivery (no custom theme files)
- All images must be hosted on `getpacerai.com` CDN (no external image sources)
- Georgia font loaded via CSS `font-family` stack (system serif fallback)
- No JavaScript frameworks — vanilla JS only if needed
- Must pass Lighthouse SEO ≥ 90, Performance ≥ 85
- Must render correctly on: Chrome, Safari, Firefox, mobile Safari