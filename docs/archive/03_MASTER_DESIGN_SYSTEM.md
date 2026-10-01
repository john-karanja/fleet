# Master Design System: County Vehicle Fleet Management System (CVFMS)

**Document ID:** `DOC-CVFMS-003`
**Version:** 1.2.0 — Airwallex visual-approach teardown incorporated (see changelog)
**Target Viewport:** Desktop enterprise (`1440 × 900px+`), with responsive collapse to `1280px` and `1024px` for smaller office monitors.
**Authority:** Single source of truth for all UI, Figma prompts, components, and tokens across the 5 flagship persona screens.
**Relationship to el-nino:** Shares the Civic Green accent (`#006837`) for cross-platform Kenyan county government identity, but uses a light enterprise theme throughout — CVFMS is daytime back-office software, not a 12-hour shift command cockpit, so there is no dark-mode cockpit variant here.

**v1.1.0 Changelog (Atlassian audit):** Atlassian was chosen as the primary anchor for auditing our token *values* (not just process) because CVFMS is an approval/audit/RBAC-heavy enterprise system, the same category Atlassian's own products (Jira, Confluence) serve — a closer match than commerce-oriented systems like Shopify Polaris. Atlassian's public docs site (atlassian.design) doesn't expose exact pixel values in static HTML (client-rendered examples), so values below were verified against the actual compiled source of `@atlaskit/lozenge` v15.4.1 (pulled from the npm registry) and Atlassian's published spacing/typography token documentation. Changes: (1) Status Pill height 24→20px, padding 10px→4/8px, radius 8→6px, matching Atlassian's real Lozenge/Badge dimensions; (2) added a distinct Metric type token family (28/24/16px bold) separate from headings, matching Atlassian's `font.metric.*` tokens, and moved KPI Tile values onto it (26px Page-Title-adjacent → 24px Metric Medium); (3) confirmed our 8pt spacing scale is a correct subset of Atlassian's real scale (0/2/4/6/8/12/16/20/24/32/40/48/64/80) — no change needed there. Component 4 (Dispatch Gate Checklist), Component 5 (Kanban), Component 6 (Data Table), and Component 7 (Budget Bar) were not re-audited in this pass — their specs remain design-instruction-derived, not source-verified, and should be treated as lower-confidence until checked the same way.

**v1.2.0 Changelog (Airwallex visual teardown):** User flagged that the built FRAME-01 looked "very basic" and didn't resemble the Mobbin references despite matching them structurally — root cause was visual craft (depth, feedback patterns, real interaction affordances), not layout. Did a screen-by-screen teardown of Airwallex (dashboard, spend-requests list, approval drawer, confirmation toast, workflow builder — see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` FRAME-01 Round 4) and adopted four patterns: (1) dark left nav rail (`#0F172A`) replacing the flat light rail — new scoped color tokens added, rest of app remains light-surface; (2) Dispatch Gate Checklist converted from a static side-panel card to a true slide-in drawer with scrim, matching Airwallex's approval pattern — renamed Component 4; (3) added Component 4B Confirmation Toast — no feedback pattern existed anywhere in this system before, despite our own UX instructions doc requiring one (Doherty Threshold rule); (4) added Component 3B Multi-Stat Card and a filter-chip-row spec for Component 6 — both were implied by earlier prose ("filterable by...") but never actually specified as components until now.

---

## 1. Design Philosophy

CVFMS is a dense, transactional, audit-sensitive enterprise system. The design priority order is:

1. **Legibility of state** — a vehicle's status, a gate check's pass/fail, a budget's variance must be readable at a glance without hover or click.
2. **Trust and auditability** — every action that matters (override, approval, release) must look deliberately different from a passive view, per the Von Restorff effect.
3. **Density without noise** — five personas each need dense tables/boards, so the token discipline (one accent, few font sizes, strict spacing scale) is what keeps five different dense screens feeling like one product.

---

## 2. Canonical Token Dictionary

### A. Color Tokens

| Role | Token Name | Hex Value | WCAG Contrast | Usage Rule |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Brand / Action** | `--color-civic-green` | `#006837` | 6.8:1 on white | Primary buttons, active nav state, "Dispatch Authorized" / "Release" confirmations. |
| **Critical / Blocked** | `--color-critical-red` | `#DC2626` | 4.8:1 on white | Failed dispatch gate rows, grounded vehicles, expired compliance, anomaly flags. |
| **Warning / Due Soon** | `--color-amber-warning` | `#D97706` | 4.5:1 on white | Insurance/inspection expiring in 30/14/7 days, low stock parts, near-budget-limit. |
| **Informational** | `--color-blue-info` | `#2563EB` | 5.2:1 on white | In-progress states (On Trip, In Repair), links, informational badges. |
| **Success / Cleared** | `--color-success-green` | `#10B981` | High on white | Passed gate checks, completed trips, cleared anomalies. Distinct from brand green to separate "passive success" from "primary action." |
| **Surface / Card Background** | `--color-surface` | `#FFFFFF` | — | Cards, tables, panels, modals. |
| **Canvas / App Background** | `--color-canvas` | `#F8FAFC` | — | Page background behind cards. |
| **Border** | `--color-border` | `#E2E8F0` | — | 1px card/table/input borders. |
| **Border Subtle** | `--color-border-subtle` | `#CBD5E1` | — | Outline buttons, secondary strokes. |
| **Primary Text** | `--color-text-primary` | `#0F172A` | 14.2:1 on white | Headings, table primary values, KPI numbers. |
| **Secondary Text** | `--color-text-secondary` | `#64748B` | 4.6:1 on white | Descriptions, subtitles, table secondary values. |
| **Muted Text** | `--color-text-muted` | `#94A3B8` | 3.1:1 on white | Timestamps, metadata. |
| **Nav Rail Surface** *(new — Airwallex teardown)* | `--color-nav-dark` | `#0F172A` | — | Left navigation rail background only. Reuses our existing `text-primary` slate as a dark surface rather than inventing a new near-black — keeps the palette from growing. |
| **Nav Rail Text (inactive)** | `--color-nav-text-muted` | `#94A3B8` | 4.6:1 on `#0F172A` | Inactive nav item labels/icons on the dark rail. |
| **Nav Rail Text (active)** | `--color-nav-text-active` | `#FFFFFF` | 15.8:1 on `#0F172A` | Active nav item label/icon, paired with a civic-green indicator (see Component 1). |

**Rule:** Exactly one primary accent (`#006837`) plus four semantic colors (critical/warning/info/success) — never used decoratively, only to carry status meaning, always paired with text or an icon (never color alone). The three new Nav Rail tokens are a scoped exception used only inside Component 1 — the rest of the application remains strictly light-surface per the original design philosophy; this is not a shift to a dark theme.

---

### B. Typography Scale (Inter)

Ratio: 1.25 modular scale, consistent with `VISUAL_DESIGN_INSTRUCTIONS.md` project defaults.

| Level | Size | Weight | Line Height | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Page Title** | `26px` | Bold (700) | `32px` | Screen root titles ("Fleet Command Dashboard"). |
| **Section Header** | `20px` | SemiBold (600) | `26px` | Card/panel section titles. |
| **Body / Table Primary** | `14px` | Medium (500) | `20px` | Table cell primary values, form labels, card titles. |
| **Body Secondary** | `13px` | Regular (400) | `18px` | Descriptions, table secondary line. |
| **Meta / Badge** | `12px` | SemiBold (600) | `16px` | Status pills, timestamps, KPI captions. |
| **Micro-Eyebrow** | `11px` | Bold (700) | `14px` | Uppercase section dividers, table column headers. |

**Metric token family (added — verified against Atlassian's real `font.metric.*` tokens):** Atlassian's type system treats dashboard hero numbers as a distinct semantic category from headings, not just "a big heading." Their scale is `font.metric.large` (28px bold), `.medium` (24px bold), `.small` (16px bold). We adopt the same split:

| Level | Size | Weight | Line Height | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Metric Large** | `28px` | Bold (700) | `32px` | Primary hero numbers in a single-metric context (e.g. a large standalone stat). |
| **Metric Medium** | `24px` | Bold (700) | `28px` | KPI Tile hero values (Component 3) — was previously using Page Title's 26px; now has its own token so KPI numbers can evolve independently of page titles. |
| **Metric Small** | `16px` | Bold (700) | `20px` | Compact inline metrics (e.g. a count badge inside a denser card). |

Eight sizes total across headings + metrics, per the revised Finish Pass rule below (was five/six — the metric family is additive because it serves a different semantic purpose than headings, not decorative proliferation).

---

### B2. List Row Hierarchy Pattern *(new — repeatable rule, derived from incident.io and Linear teardown)*

**The problem this fixes:** components like Needs Attention had the right structural pieces (tint, border, icon, tag) but still read as flat, because every text element inside a row was close to the same size/weight — color was doing all the differentiation work, with no type hierarchy backing it up. Checked against incident.io's Incidents list and Linear's issue list: both use exactly **two** text weights per row, never three or more competing sizes.

**The rule — applies to every list/row component in this system (Needs Attention, Recent Activity, Vehicle Status Board, Kanban cards):**

1. **Exactly one dominant text element per row.** This is the *subject* — the thing the row is about (e.g. "KCA 902B grounded — failed NTSA inspection, 2 days ago" in Needs Attention; a vehicle reg in the Status Board; an actor's name in Recent Activity). Use **Body Primary (`14px` Medium)**, always `--color-text-primary`, never a lighter shade. This is the only element in the row a viewer's eye should catch first.
2. **Everything else drops at least one full level down**, using **Meta/Badge (`12px`)** or **Micro-Eyebrow (`11px`)**, in `--color-text-secondary` or `--color-text-muted` — never the same size as the dominant element, even if bolded or colored. This includes: category tags, timestamps, metadata (assignee, station, odometer captions), and helper/secondary description lines.
3. **Color reinforces the hierarchy, it does not replace it.** A category tag or severity icon is still small/muted per rule 2, even though it's also colored — color alone was the exact mistake this pattern corrects. A red-tinted row with a same-size, same-weight category label as its subject text is still flat, regardless of the tint.
4. **Never more than 2 distinct text sizes visible in a single row.** If a row seems to need a 3rd size, that's a signal the row is trying to show too much — move the extra detail to a detail view/drawer instead of adding another type level to the row.

**Applied correction to Component 3C (Needs Attention):** the category tag ("GROUNDED", "INSURANCE") must render at Micro-Eyebrow size (`11px`) in `--color-text-muted`, clearly smaller/lighter than the row's Body Primary description text — not the same visual weight as the description, which is the specific defect in the build reviewed in Round 7 (see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`).

---

### C. Spacing Scale (Strict 8pt Rhythm)

```
4px (Micro) · 8px (Compact) · 12px (Standard Gap) · 16px (Container Pad) · 24px (Section Gap) · 32px (Block) · 48px (Touch Target) · 64px (Nav Height)
```

---

### D. Corner Radii

* **Small (`8px`):** Buttons, pills, badges, inputs.
* **Medium (`12px`):** Cards, panels, dropdown menus.
* **Large (`16px`):** Modals, drawers, bottom sheets.

---

### E. Shadows & Elevation

* **Level 0 (Flat):** Table rows, inline cards — `border: 1px solid #E2E8F0`, no shadow.
* **Level 1 (Cards):** `0 1px 3px 0 rgba(0,0,0,0.05)`.
* **Level 2 (Sticky header/toolbar, dropdowns):** `0 4px 14px -2px rgba(0,0,0,0.08), 0 2px 6px -1px rgba(0,0,0,0.04)`.
* **Level 3 (Modals, drawers):** `0 -10px 25px -5px rgba(0,0,0,0.10)` (drawers) / `0 20px 40px -8px rgba(0,0,0,0.15)` (modals).

---

## 3. Core Component Specifications

### Component 1: Application Shell — Top Nav + Left Rail

**Revised — Airwallex teardown (see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` FRAME-01 Round 4).** Original spec used a flat white/light-gray rail matching the canvas, which read as unfinished next to real fintech/enterprise references. Airwallex's dark rail creates separation without extra borders and reads as more considered — adopted, scoped to this one component only (see color token note above).

* **Top Bar:** `Height: 56px`, `bg: #FFFFFF`, `border-bottom: 1px solid #E2E8F0`. Left: county crest + "CVFMS" wordmark. Center: global search (vehicle reg/trip number/driver). Right: notification bell (badge count), role-based profile menu.
* **Left Nav Rail (revised):** `Width: 240px` (expanded) / `64px` (collapsed icon-only), `bg: --color-nav-dark (#0F172A)` — was `#F8FAFC`. No right border needed (the color contrast against the white canvas already separates it — remove the `1px #E2E8F0` border-right from the original spec). Sections grouped by module family (Fleet, Dispatch, Workshop, Finance, Compliance, Reports). Inactive items: icon + label in `--color-nav-text-muted (#94A3B8)`. Active item: icon + label in `--color-nav-text-active (#FFFFFF)`, with a `3px` left border in `--color-civic-green` and a subtle tinted background using civic-green at low opacity (`rgba(0,104,55,0.16)`, not the light-mode `#E8F5E9` tint, which would look chalky against the dark surface).

### Component 2: Status Pill (used everywhere — vehicle status, gate checks, anomaly flags)

* **Dimensions (revised — verified against `@atlaskit/lozenge` v15.4.1 compiled source, npm registry, checked directly since Atlassian's docs site doesn't expose pixel values in static HTML):** `Height: 20px` (was 24px — Atlassian's current Lozenge/Badge is `1.25rem`), `padding: 4px 8px` (was 10px — Atlassian uses `space-050` = 4px both axes), `radius: 6px` (was 8px — Atlassian's own component uses 3-6px, a sharper "label" shape than a soft pill; 6px = their "medium" radius token, chosen over their 3-4px "small" token since our light theme benefits from slightly more softness, but 8px was confirmed too far from any real reference).
* **Variants (always icon + text, never color alone):**
  * Active/Available: `bg: #DCFCE7`, `text: #006837`, `● icon`.
  * On Trip / In Repair: `bg: #DBEAFE`, `text: #2563EB`.
  * Grounded / Blocked / Failed: `bg: #FEE2E2`, `text: #DC2626`.
  * Due Soon / Warning: `bg: #FEF3C7`, `text: #D97706`.
  * Disposed / Inactive: `bg: #F1F5F9`, `text: #64748B`.
* **Note on our color choices vs. Atlassian's:** our tints (`#DCFCE7`, `#FEE2E2`, `#FEF3C7`, `#DBEAFE`) are close in hue to Atlassian's real subtle-background tokens (`#d3f1a7` success, `#ffd5d2` danger, `#fce4a6` warning, `#cfe1fd` information) but are not required to match exactly — Atlassian's palette is tuned to their brand, ours is tuned to Civic Green; the point of this cross-check was structural (radius, height, padding), not palette-copying.

### Component 3: KPI Tile (Executive Dashboard, Fleet Manager summary row)

* **Dimensions:** `Min-width: 220px`, `padding: 20px`, `radius: 12px`, `border: 1px solid #E2E8F0`, `bg: #FFFFFF`.
* **Anatomy (reverted in Round 14 — see below):** Eyebrow label (`11px` uppercase, `--color-text-muted`) → large value (`24px` bold, **Metric Medium token**, `--color-text-primary`) → plain text delta (`12px`, e.g. "+3 vs last month", colored by direction using semantic tokens, never bare color). No sparkline.
* **Sparkline history — added Round 11, reverted Round 14.** Round 11 reinstated a thin hairline sparkline (per [Whop's KPI cards](https://mobbin.com/screens/0bb8b25f-0c3d-47c3-b20a-1447e7dbab9e)) but only on KPIs where trend carried real decision value — which, applying the anti-decoration rule honestly, was really only Grounded (a climbing grounded-count over consecutive days is a pattern worth investigating differently than a one-off blip); Availability was borderline; Fleet Size and Alerts Due had no real case. Built as 3 of 4 cards having a sparkline and one not, which rendered as a ragged, unbalanced row — the empty space under Fleet Size's delta made it look unfinished next to its siblings. Rather than force artificial consistency (adding sparklines to cards with no real decision value just to fill the row) or reserve blank space (which fixes the layout but not the honesty problem), reverted to no sparklines on any KPI card — the simplest fix that doesn't paper over a content decision with a layout compromise. If a genuinely decision-driving trend need resurfaces later (e.g. Grounded), it should be solved with a component that can hold that asymmetry without looking broken (e.g. a distinct "trending" indicator, not a sparkline matched to a row of otherwise-plain cards) — not by re-adding this exact pattern.

### Component 3C: Needs Attention List *(new — replaces the v1.4 hero trend chart, see `04_FIGMA_SCREEN_BLUEPRINT.md` v1.6; merged with Compliance Countdown in v1.8; row treatment redesigned in v1.9 — see below)*

A synthesized, priority-ranked list pulling every urgent item across the dashboard's data domains into one place — the dashboard's hero element for Grace, chosen specifically because it is actionable (a decision-ready list) rather than decorative (a trend chart with no corresponding decision).

**v1.9 redesign — tinted-row treatment replaced with plain-row + dot + section-header treatment.** The full-tint-per-row pattern (each row its own colored box) was judged too visually busy for a list Grace scans daily — a stack of 7-8 colored boxes competes with itself rather than reading calmly. Checked against Todoist's priority-dot pattern and GitHub's Urgent/No-Priority grouped issue view: both handle urgency **without any per-row background fill** — a small colored dot is the only accent, rows stay plain white, and urgency is communicated primarily through grouping under section headers rather than through row color. Adopted this pattern in place of the v1.8 tinted-row treatment.

* **Container elevation (unchanged from Round 6 Finding 2):** `Width: 100%` of its hero slot, `radius: 12px`, `border: 1px solid #E2E8F0`, `bg: #FFFFFF`, `padding: 16px`, plus Level 1 shadow (Shadows & Elevation §E) — this component must be visibly elevated above the page canvas, not flush with it, since it is the documented hero and must carry more visual weight than every other card on the page.
* **Header:** `"Needs Attention"` (`20px` semibold) with a count badge (e.g. a small pill showing "7").
* **Section headers (new — GitHub-style grouping):** rows are grouped under small uppercase section labels by urgency band — e.g. `"OVERDUE"`, `"THIS WEEK"`, `"THIS MONTH"` — each label at Micro-Eyebrow size (`11px`, `--color-text-muted`, uppercase, letter-spacing), `8px` bottom margin before its group's rows begin. This is the primary urgency signal now, replacing what per-row tint used to communicate.
* **Row anatomy (redesigned — Todoist/GitHub treatment, replaces v1.8's tinted sub-container):** plain row, `bg: transparent` (no fill, no tint), `1px solid #E2E8F0` bottom divider only (no border on other sides, no per-row card shape), `12px` vertical padding, full width. Inside, left-to-right: a small colored dot (`8px` diameter, color = severity — critical red or warning amber, this is the ONLY color in the row) → category tag (`11px` uppercase muted gray, per the List Row Hierarchy Pattern §B2 — small and light, never competing with the description) stacked above or inline before the description → one-line description combining subject + reason (`14px` medium, dark — this is the row's one dominant element per §B2) → a single right-aligned action button (outline, `32px` height, e.g. "Reallocate", "Review", "Override") → a small dismiss (`×`) icon furthest right (muted gray, `16px`, click to acknowledge/clear without taking the primary action — matches the dismiss affordance already present in the current Figma build, not previously documented).
* **Ranking rule:** within each urgency-band section, rows are sorted by severity/days — sections themselves are ordered Overdue → This Week → This Month. A grounded vehicle, an overdue insurance policy, a maintenance approval, and an idle-vehicle mismatch can all appear in the same section if they share an urgency band — grouping is by urgency, not by data source or category.
* **Row count:** up to ~7-8 rows across all sections combined (this list fully absorbed the former Compliance Countdown component as of v1.8 — do not build Compliance Countdown as a separate card).
* **Empty state (per section):** if a section has no items, omit that section header entirely rather than showing it empty. If the whole list is empty, show a single calm row — a success-green check icon + "No urgent items — fleet is operating normally."
* **Anti-pattern warning:** do not add a chart, sparkline, or any purely visual element to this component. Do not reintroduce full per-row background tints — that was the specific pattern this redesign replaced; the dot + section header combination is the required treatment, not an optional lighter alternative to keep alongside it.

### Component 3D: Utilization Gap / "Critical Mismatch" Card — REMOVED in Round 14 (was Rounds 10/12; see below for replacement)

*History: this component went through three rounds of surface refinement (visual-weight cap in Round 10, action-button change in Round 12) before the user asked the more fundamental question — same discipline applied earlier to the v1.4 hero chart and the v1.8 Needs Attention/Compliance merge: does Grace need this as its own thing, or is it redundant with something else already on the page?*

**Round 14 finding:** this card's entire content (idle vehicles vs. pending requests) duplicates Needs Attention's own "UTILIZATION" row at a different level of detail — both describe the same underlying mismatch (Component 3C already carries a row like "KBZ 204D idle 5 days while Agriculture dept request is pending — Reallocate"). This is the same redundancy pattern already fixed once before (Round 8, merging the standalone Compliance Countdown card into Needs Attention for an identical reason). Checked references for "well-designed recommendation" patterns — [Google Ads' Recommendations](https://mobbin.com/screens/7f77aab3-3a8e-430d-8f9b-9c4b864c1f06) and [Salesforce's Recommended Actions](https://mobbin.com/screens/02576646-fdbb-4d74-888b-1552861baa0f) — both show that a well-designed recommendation is presented as a normal row in an existing list, not a separately-styled special card. Reinforced the case for dissolving this component rather than continuing to restyle it.

**Decision:** Component 3D is removed as a standalone Overview card. Its full-detail content (matching every idle vehicle against every pending request) becomes a **linked table destination** instead — see Component 3G below — reached via a link from Needs Attention's UTILIZATION row, not shown permanently on Overview. This keeps Overview scoped to short-list triage (per the Round 9 decision) while still making the full picture available on demand, one click away — consistent with how Vehicle Status Board and Fleet Map are already treated (condensed/preview on Overview, full detail one click away).

### Component 3G: Vehicle Allocation Table *(new — Round 14, replaces Component 3D's on-page content as a linked destination)*

A real data-grid table matching idle vehicles against pending requests — reached from Needs Attention's UTILIZATION row link (e.g. "View allocation table →"), not shown on the Overview page itself.

* **References:** [Wrike's Creative Team table](https://mobbin.com/screens/9705c335-9e80-449f-a3c4-9f7b9ce057d3) — real columns, status pills, grouped rows; [ClickUp's task table](https://mobbin.com/screens/e9639493-e0a6-46c9-93d1-d3189cbdc3c7) and [Airtable](https://mobbin.com/screens/1ccf6613-4abd-420f-9d18-ac7b40a04848) confirm the same pattern as the mainstream way to present this shape of relational data.
* **Structure:** a single flat table (per Component 6, Data Table) with a `TYPE` column distinguishing row kind ("Idle Vehicle" / "Pending Request" as status-pill-style tags), then shared columns where applicable: `VEHICLE / DEPARTMENT`, `STATUS` (idle duration or request urgency), `DETAIL` (purpose, for requests), and an `ACTION` column ("Reallocate" button on idle-vehicle rows, "Assign Vehicle" on pending-request rows). Sortable/filterable like any other data table in this system.
* **Not yet assigned to a frame** — this is a destination, not part of FRAME-01. It should be scoped as either a modal/drawer launched from Needs Attention (fastest to reach, matches Component 4's drawer pattern) or a dedicated view under a nav item — decide when this is actually built, not speculatively now.

### Component 3E: Fleet Map Preview Card *(newly numbered — Round 11, was described only as "Fleet Pulse"/"Fleet Map" in `04_FIGMA_SCREEN_BLUEPRINT.md` prose; treatment split from FRAME-06 in Round 13)*

The compact, secondary-panel version of the map that sits on the Overview tab. **As of Round 13, this deliberately uses a different visual treatment than FRAME-06's full Live Map** — a bounded, card-contained widget, not a scaled-down full-bleed map. Full-bleed is reserved for the real tool (FRAME-06); a preview card should look like a preview, not an undersized version of the main event.

* **References (Round 13 revision):** [Google Analytics "Active users by Country"](https://mobbin.com/screens/b5e7543e-5eed-44a1-9fcf-2322d64a2b7e) and [Chatbase "Chats by country"](https://mobbin.com/screens/48d5b7dd-5c10-44aa-a88f-95faaa1155a3) — both present a map as a bounded widget *inside* a dashboard card, paired with a compact adjacent data list, rather than full-bleed with a legend beneath. This is the model for this component. [Felt's operations map](https://mobbin.com/screens/c8b96c23-975f-472b-acca-279dede6555c) and [Uber Eats' tracking view](https://mobbin.com/screens/fbbc20da-52f8-4211-b0ea-a0bedf3fd0f6) remain the reference for FRAME-06 (the full, real map tool) — see that section, not this one.
* **Dimensions:** `Width: 100%` of its panel slot, `radius: 12px`, `border: 1px solid #E2E8F0`, `bg: #FFFFFF`, `padding: 16px` — the map sits *inside* this padded card area with its own rounded corners (`8px`, smaller than the card's own radius), not edge-to-edge with the card. Header: `"Fleet Map"` title + a `"View full map →"` link routing to the `[Live Map]` tab (FRAME-06).
* **Layout:** map area on one side (roughly 60-65% of the card width), a compact adjacent list on the other (35-40%) — status + count pairs (e.g. "Available · 178", "On Trip · 41", "Grounded · 6", "Maintenance · 22"), matching GA/Chatbase's map-plus-sidelist pattern instead of a legend row beneath a full-width map.
* **Map content:** a real street-level basemap (muted/desaturated so colored dots stand out), bounded within the widget's rounded corners — this is a windowed view onto the map, not the map itself.
* **Markers:** small colored dots using the same 4-state semantic tokens as Status Pill (success/info/critical/warning = Available/On Trip/Grounded/Maintenance) — consistent color language across this preview, the KPI row, and the full Live Map.
* **Interactivity:** static preview, not pannable/zoomable (that's FRAME-06's job) — clicking anywhere in the card routes to the full Live Map tab.

### Component 3F: Coming Up List *(newly numbered — Round 11, was prose-only as the "Coming Up" deprioritized-compliance destination)*

The destination for compliance items tightened out of Needs Attention's hero scope (v2.0) — a calmer, date-grouped list rather than an urgency-dot list, since these items are explicitly *not* urgent yet.

* **References:** [Circle's Events list](https://mobbin.com/screens/bbb7b785-2793-4264-9123-5a7a24f8191b) and [Luma's Events list](https://mobbin.com/screens/1932af9e-e821-4bd7-b13d-fcb0cb3f2524) — both group upcoming items by date with a consistent date-badge treatment, clean single-line rows, no urgency color-coding (appropriate here, since these items are deliberately non-urgent).
* **Dimensions:** `Width: 100%` of its panel slot, `radius: 12px`, `border: 1px solid #E2E8F0`, `bg: #FFFFFF`, header `"Coming Up"` with a `"Next 14 days →"` or similar scope label and a link to the full Compliance nav destination.
* **Row anatomy:** a small date badge/label on the left (e.g. "Sep 11", `12px`, muted gray — not a full calendar-square graphic, a compact text badge is sufficient at this density) → item title (`14px` medium, dark — the row's one dominant element per §B2) → vehicle reg as a smaller trailing detail (`12px`, muted, right-aligned). No colored dots or severity accents here — deliberately calmer than Needs Attention, since urgency-coding non-urgent items would be a false signal.
* **Sort order:** strictly chronological (soonest first), never re-sorted by category or severity — this list's entire value is "what's coming, in order," distinct from Needs Attention's urgency-first sort.

### Component 3B: Multi-Stat Card *(new — Airwallex teardown)*

Airwallex groups 2-3 related numbers inside one bordered card with a header + "View all" link, rather than one number per tile — denser and shows the numbers' relationship (e.g. "pending / to pay / overdue" as stages of the same thing) instead of presenting them as unrelated facts side by side.

* **Dimensions:** `Min-width: 260px`, `padding: 16px`, `radius: 12px`, `border: 1px solid #E2E8F0`, `bg: #FFFFFF`.
* **Header row:** section label (`14px` semibold, `--color-text-primary`) left, `"View all →"` text link (`12px` semibold, civic green) right.
* **Stat groups:** 2-3 stacked rows inside the card body, each a label/value pair — label (`12px`, `--color-text-secondary`) left, value (`16px` bold, **Metric Small token**) right, on the same line. A thin `1px` divider between stat groups only when there are 3+ (2 groups can rely on spacing alone per the design system's "space before border" rule).
* **Usage:** use this instead of single-stat KPI Tiles (Component 3) whenever 2-3 numbers are genuinely related stages/facets of the same thing (e.g. a compliance panel's "Overdue / Due this week / Due this month" counts). Keep single-stat KPI Tiles for standalone headline metrics like Fleet Size or Availability % that don't have natural siblings.

### Component 4: Dispatch Gate Checklist Drawer *(revised — Airwallex teardown, was "Card")*

Originally specified as a static side panel sitting next to the requisition list. Airwallex's approval pattern uses a true right-side slide-in drawer that overlays a dimmed background while keeping the list visible behind it — adopted, since it better matches "reviewing one item pulled out of a list" than a permanently-visible split panel.

* **Dimensions:** `Width: 480px` (was "100% within a 420px side panel"), full viewport height, `bg: #FFFFFF`, `radius: 16px 0 0 16px` (rounded only on the left/leading edge, since the right edge meets the viewport boundary), Level 3 shadow (drawer variant, see Shadows & Elevation).
* **Scrim:** the list behind it dims to `rgba(15, 23, 42, 0.4)` and becomes non-interactive while the drawer is open — clicking the scrim or a close icon (top-right of the drawer) dismisses it.
* **Entry animation:** slides in from the right, `250ms ease-out`, per the design system's Motion rule (UI feedback transitions 100-200ms, layout transitions 200-300ms — this is a layout transition).
* **Header:** title (`20px` semibold) + subtitle metadata line (`13px` secondary, e.g. "Vehicle: KCA 902B · Driver: J. Mutiso") + close icon top-right.
* **Metadata grid (new):** above the checklist, a 2-column grid of label/value pairs (label `11px` uppercase muted above, value `14px` medium below — same pattern as Airwallex's "Start and end date / Requested for / Category" grid) for any request-level context (requester, department, purpose, dates) before the gate checklist itself.
* **Checklist body:** icon (✓ in success green / ✗ in critical red) + label (`14px` medium) + right-aligned detail text (`12px` secondary, e.g. "Expired 2 days ago"). Failing rows get `bg: #FEF2F2` row tint.
* **Comments/Attachments section (new):** below the checklist, an optional comment textarea + file drop zone, matching Airwallex's pattern of building in the "wait, can you clarify" moment rather than assuming every approval is a single yes/no click. Not mandatory for CVFMS's simpler gate checks (unlike Airwallex's spend requests) but available as a pattern for any future approval screen that needs it — Grace's Maintenance Approval modal (see `02_USER_FLOWS.md` §2 path D) is the clearest candidate.
* **Footer:** sticky at the bottom of the drawer. If any gate fails — `[Request Override]` (outline button, opens justification modal, mandatory text field, logs to audit trail) sits beside the disabled primary `[Authorize Dispatch]` button. If all pass, only `[Authorize Dispatch]` (primary, filled green) is shown.
* **On confirm:** dismiss the drawer and trigger Component 4B (Confirmation Toast) — never leave the user without feedback that the action registered.

### Component 4B: Confirmation Toast *(new — Airwallex teardown)*

No feedback pattern previously existed anywhere in this design system despite the UX instructions doc's own Doherty Threshold rule ("never leave users wondering whether their action registered"). Airwallex's post-approval toast is the reference: confirms what happened AND states what happens next.

* **Dimensions:** `Min-width: 320px`, `max-width: 480px`, `padding: 12px 16px`, `radius: 8px`, positioned bottom-center or bottom-left of the viewport (not top — avoid colliding with the top nav bar), `8px` margin from viewport edge.
* **Variants:** Success (`bg: #DCFCE7` background OR a solid dark surface with a green check icon — use the solid-surface treatment for stronger visibility against busy dashboard backgrounds: `bg: #0F172A`, icon in success green, text `#FFFFFF`), Error (same solid-surface pattern, icon/accent in critical red).
* **Anatomy:** icon (16px, left) + message text (`14px` medium) + optional single text-link action (e.g. "View" or "Undo") right-aligned, + close icon.
* **Message pattern:** always two clauses — what happened, then what happens next. E.g. "Dispatch authorized — KCA 902B is now on trip." or "Override approved — This has been logged to the audit trail." Never a bare confirmation like "Success" with no context.
* **Timing:** enters `250ms ease-out` from bottom, auto-dismisses after `4000ms` unless the user hovers (pause on hover), or is manually dismissed via the close icon.
* **Usage:** trigger after every state-changing action in the system — Authorize Dispatch, Request Override, Approve/Reject Maintenance, Reallocate Vehicle, Save Registry Edit. This is now a required part of every action flow's spec, not optional polish.

### Component 5: Kanban Work Order Board (Workshop)

* **Columns:** Diagnosis / In Repair / Awaiting Parts / QA / Ready for Release — fixed-width `280px` columns, `gap: 16px`, horizontal scroll on overflow rather than wrapping.
* **Card:** `radius: 12px`, `padding: 12px`, `border: 1px solid #E2E8F0`. Shows vehicle reg (`14px` bold), defect summary (`12px` secondary, 2-line clamp), assigned mechanic avatar + name, linked parts request status pill, days-in-column indicator.

### Component 6: Data Table (Fleet Registry, Trip Log, Fuel Ledger, Reports)

* **Filter chip row (new — Airwallex teardown):** a horizontal row of pill-shaped filter buttons directly above the table, `height: 32px`, `radius: 8px` (rounded rectangle, not full pill — matches Airwallex's chip shape), `border: 1px solid #E2E8F0`, `bg: #FFFFFF`, each showing a filter dimension name + chevron (e.g. "Department ▾", "Status ▾"), opening a dropdown/checklist on click. An active filter shows its selected value in the chip itself (e.g. "Status: Grounded ✕") with a small `✕` to clear. This was previously only implied by the design system's text ("filterable by department/station/status") without an actual component spec — now required wherever that text appears (Vehicle Status Board, Dispatch Queue, Fleet Registry, Trip Log).
* **Row height:** `48px` standard, `40px` compact (toggle available for high-density review).
* **Header:** `bg: #F8FAFC`, `11px` uppercase bold, sticky on scroll, sort icon on hover/active.
* **Numbers:** right-aligned, tabular figures. Text: left-aligned.
* **Row hover:** `bg: #F8FAFC`. Selected row: `bg: #E8F5E9` with left `3px` civic-green border.
* **Empty state:** icon + one sentence + one action button, never a blank grid.

### Component 7: Budget vs. Actual Bar (Finance Dashboard)

* **Dimensions:** `Height: 32px` per row, horizontal stacked bar — actual spend as filled bar in `--color-civic-green` (or `--color-critical-red` if over budget), budget line as a vertical marker.
* **Label:** department/cost-center name left, actual/budget figures right, percentage variance as a status pill.

---

## 4. Layout Archetypes

Every CVFMS screen belongs to one of three archetypes:

| Archetype | Screens | Structure |
| :--- | :--- | :--- |
| **A. Command Dashboard** | Fleet Command Dashboard, Executive Briefing | KPI tile row (top) → multi-panel grid below (status breakdown, alerts feed, map/list) |
| **B. Queue / Workflow** | Dispatch & Requisition Queue, Finance Anomaly Review | Left: filterable list/queue. Right: detail/action panel (gate checklist, reconciliation detail) |
| **C. Board / Table** | Workshop Job Card Board, Fleet Registry, Trip Log | Full-width kanban board or data table with sticky filter toolbar above |

---

## 5. Finish Pass Checklist

Before any CVFMS screen or Figma prompt is approved:

1. **Accent colors:** Exactly one primary accent (`#006837`) plus the four fixed semantic tokens — no ad-hoc colors.
2. **Font sizes:** Eight or fewer, drawn only from the defined heading scale (`26, 20, 14, 13, 12, 11`) plus the Metric family (`28, 24, 16`) — never an ad-hoc size, and never use a heading token where a Metric token is semantically correct (e.g. KPI values).
3. **Primary buttons:** Exactly one dominant filled primary button per view/panel.
4. **Spacing:** Every value is on the 8pt scale (`4, 8, 12, 16, 24, 32, 48, 64`).
5. **Status is never color-only:** every pill/indicator pairs color with text or icon.
6. **Tables:** row height consistent, numbers right-aligned tabular, empty states designed.
7. **Gate/approval actions:** visually distinct from passive display — never the same button style as a "View" link.
8. **Override/destructive actions:** always require a justification field and are visibly logged.
9. **Touch/click targets:** minimum 40×40px interactive area even on a dense desktop table (row action icons excepted only via a min 32px hit area).
10. **Resize check:** layout collapses gracefully at 1280px and 1024px without losing access to primary actions.
