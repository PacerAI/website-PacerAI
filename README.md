# website-PacerAI

Homepage refresh for [getpacerai.com](https://getpacerai.com) — AI-native build using the PDBRDD lifecycle.

## Project Overview

This repo manages the design, development, and deployment of the Pacer AI marketing website. The primary goal of this sprint is to deploy a refreshed homepage targeting Operating Partners, PE Portfolio Ops, CFOs, and RevOps leaders at $50M–$1B ARR SaaS companies.

**Tagline:** Turn operational data into agent intelligence.

---

## Stack

| Layer | Tool |
|---|---|
| CMS | WordPress.com (hosted) |
| Deploy | WordPress REST API + Application Password |
| Dev Environment | Claude Code (Anthropic) |
| Version Control | GitHub (`pacerai/website-PacerAI`) |
| SEO | Yoast SEO (active plugin) |
| Design Source | HTML mockup (docs/design/) |

---

## PDBRDD Lifecycle

```
docs/
├── plan/
│   ├── overview.md        # Project goals, scope, success criteria
│   └── prd.md             # Product requirements document
├── design/
│   └── pacerai-homepage_by_Claude_030526_1522.html   # Approved design mockup
├── build/
│   └── architecture.md    # Technical decisions, API approach, file map
├── review/
│   └── checklist.md       # QA, Lighthouse, SEO, mobile checks
├── document/
│   └── changelog.md       # What changed, why, and when
└── deploy/
    └── runbook.md         # Step-by-step deploy instructions for Claude Code
```

---

## Quick Start for Claude Code

1. Confirm env vars are set: `WP_BASE_URL`, `WP_USER`, `WP_APP_PASSWORD`
2. Read `AGENTS.md` for full operating instructions
3. Read `docs/deploy/runbook.md` before touching any live page
4. Design source of truth: `docs/design/pacerai-homepage_by_Claude_030526_1522.html`

---

## Agents & Skills

- **AGENTS.md** — Claude Code instructions for this repo
- **MCP Servers in use:** Slack (notifications), Gmail (stakeholder comms), Notion (project tracking)
- **Relevant Claude Skills:** `frontend-design`, `docx` (for PRD/spec docs)

---

## Key Constraints

- Only modify the homepage — no other pages
- Preserve all Yoast SEO metadata
- Brand: Georgia serif, white background, minimal — financial-professional aesthetic
- No gradients, no playful UI elements