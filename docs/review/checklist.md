# Review Checklist — Homepage Refresh v1

Run this checklist after BUILD and before DEPLOY. Claude Code should work through each item and record pass/fail with notes.

**Date:** 2026-03-09
**Reviewer:** Claude Code
**Build file:** `src/homepage/index-build.html`

---

## 1. Content Integrity

- [x] Hero headline: "Your ARR Snowball Report. Automated. Board-Ready." (matches design mockup — differs from PRD, design is source of truth per AGENTS.md)
- [x] Primary CTA present: "Request Demo"
- [x] ARR Snowball section present and accurate
- [x] Navigation structure matches PRD (Platform, Solutions, Resources, Customers, Company)
- [x] Footer structure matches PRD
- [x] No placeholder text (lorem ipsum, [TBD], etc.)
- [x] No references to localhost, staging URLs, or relative paths

---

## 2. Visual / Brand

- [x] Font: DM Sans (body) + Cormorant Garamond (headings) — approved by Will over Georgia (2026-03-09)
- [x] Background: White (#FFFFFF) on main content areas
- [x] Gradients: subtle hero background gradients present from approved design — not playful/purple. Accepted.
- [x] CTA buttons: consistent style, correct label ("Request Demo")
- [x] Logo present (inline SVG three-chevron mark)
- [x] All images load — data URI replaced with WP CDN URL (media ID 327)

---

## 3. SEO

- [ ] Page `<title>` — pending: must be set via Yoast in WP admin (see Issues.md #3)
- [ ] Meta description — pending: must be set via Yoast in WP admin (see Issues.md #2)
- [x] H1 present and unique on page (1 H1)
- [x] H2s follow logical hierarchy (1 H1, 5 H2, 5 H3)
- [x] No duplicate H1s
- [x] Canonical URL — managed by Yoast (confirmed present in yoast_head)
- [x] OG tags intact (verified via Yoast yoast_head field — 4,570 chars)

---

## 4. Technical

- [x] HTML validates (no unclosed tags, no `<html>/<head>/<body>` wrappers)
- [x] No inline `<script>` blocks with external dependencies
- [x] No `<iframe>` embeds from unapproved sources
- [x] Mobile viewport meta tag — managed by WordPress `<head>`
- [ ] No JavaScript errors in browser console — requires manual check
- [ ] Page loads under 3 seconds on fast 3G — requires post-deploy test

---

## 5. Lighthouse Audit

Run after deploy: `npx lighthouse https://getpacerai.com --output=json --output-path=docs/review/lighthouse-20260309.json`

| Category | Target | Actual | Pass? |
|---|---|---|---|
| Performance | ≥ 85 | pending | |
| Accessibility | ≥ 90 | pending | |
| Best Practices | ≥ 90 | pending | |
| SEO | ≥ 90 | pending | |

---

## 6. Cross-Browser / Device

- [ ] Chrome (desktop) — page open for Will's manual review
- [ ] Safari (desktop)
- [ ] Mobile Safari (iPhone 14 viewport: 390px)
- [ ] Chrome Mobile (Android)
- [ ] iPad Pro (1024px viewport)

---

## 7. Known Issues (see `docs/review/Issues.md`)

- [ ] Slug `no-title` reviewed — confirm with Will whether to change
- [ ] Yoast meta description set in WP admin
- [ ] Yoast page title set in WP admin: "Pacer AI — ARR Intelligence for PE-Backed SaaS"

---

## 8. Pre-Deploy Backup

- [ ] Current live homepage content saved to `docs/review/pre-deploy-backup-[DATE].json`
- [ ] Backup includes: page ID, title, content, modified date, yoast_head

---

## Sign-off

| Item | Status | Notes |
|---|---|---|
| Content | PASS | Design mockup headline accepted over PRD |
| Brand | PASS | DM Sans + Cormorant approved by Will. Subtle gradients accepted. |
| SEO | PARTIAL | Yoast title + meta description pending WP admin action |
| Technical | PASS | Clean HTML, no scripts/iframes, inline style block |
| Lighthouse | PENDING | Post-deploy |
| Cross-browser | PENDING | Manual testing |
| Backup | PENDING | Will be created during deploy |

**Ready to deploy:** YES (pending pre-deploy backup)
**Approved by:** Will Sullivan (2026-03-09)

---

## 9. GitHub Integration — Claude Code CI/CD

This repo uses GitHub-integrated Claude Code for automated PR review and issue handling.
Reference: [Anthropic Skilljar — Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action/303240)

### Workflow Files

#### `.github/workflows/claude.yml` — @claude Mentions
Triggers when someone mentions `@claude` in a GitHub issue or PR comment.

**What it does:**
- Claude reads the issue/PR context and responds with analysis, suggestions, or code
- Can be used to ask Claude to investigate bugs, suggest implementations, or review changes
- Responds directly in the GitHub comment thread

**Usage in issues:**
```
@claude Can you review the current homepage CSS and suggest performance improvements?
@claude What would it take to add a blog sidebar component?
```

**Usage in PRs:**
```
@claude Review this PR for accessibility issues
@claude Does this change break mobile responsiveness?
```

#### `.github/workflows/claude-code-review.yml` — Automated PR Review
Triggers automatically on pull request creation or update.

**What it does:**
- Claude reviews the full diff of the PR
- Posts a review comment with:
  - Summary of changes
  - Potential issues (bugs, security, performance)
  - Suggestions for improvement
  - Approval or request for changes
- Follows the project's CLAUDE.md rules and brand constraints

### Setup Requirements

1. **GitHub Actions enabled** on the repository
2. **Anthropic API key** stored as a GitHub secret (`ANTHROPIC_API_KEY`)
3. **Workflow files** in `.github/workflows/`:
   - `claude.yml` — for @claude mentions
   - `claude-code-review.yml` — for automated PR review

### Configuration

Both workflows should reference this repo's `CLAUDE.md` for context, ensuring Claude:
- Only reviews homepage-related changes
- Checks brand constraints (fonts, colors, CTA language)
- Validates technical requirements (no external CDNs, inline CSS, Gutenberg compatibility)
- Flags SEO issues (missing alt text, heading hierarchy, keyword usage)
- Checks mobile responsiveness of CSS changes

### Review Checklist for PRs

When Claude reviews a PR to this repo, it should verify:

- [ ] Changes only affect homepage (page 25) or planned new pages
- [ ] No Yoast SEO metadata overwritten
- [ ] Brand constraints maintained (DM Sans/Cormorant, dark theme, CTA language)
- [ ] Mobile responsive — no fixed widths > 768px without media query
- [ ] No external CDN dependencies, localhost references, or data URIs
- [ ] Images use getpacerai.com CDN URLs or inline SVG
- [ ] `<!-- wp:html -->` wrapper preserved
- [ ] No JavaScript frameworks — vanilla JS only
- [ ] Deploy backup documented in changelog
- [ ] Build file (`src/homepage/index-build.html`) matches what's deployed

### Integrating with PDBRDD Workflow

```
Plan (docs/plan/)
  ↓
Design (docs/design/)
  ↓
Build (src/) ← Claude Code writes code
  ↓
Review ← GitHub PR + Claude automated review + manual review
  ↓
Document (docs/document/) ← changelog updated
  ↓
Deploy (docs/deploy/) ← runbook followed, live verified
```

GitHub PRs serve as the **Review gate** in the PDBRDD lifecycle:
1. Developer (Claude Code or human) creates branch and PR
2. `claude-code-review.yml` auto-reviews the diff
3. Will reviews and approves
4. Merge triggers deploy (or deploy is manual per runbook)
