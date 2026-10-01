# Master Design System: County Vehicle Fleet Management System (CVFMS)

**Document ID:** `DOC-CVFMS-003`
**Revision:** 2.0 — full restart. Tokens below are derived from (a) the SRS/architecture summary's functional requirements and (b) a fresh `ui-ux-pro-max` research pass (product, style, color, typography, chart, and shadcn-stack domains), evaluated for fit rather than used to confirm the prior v1.x system (archived in `docs/archive/03_MASTER_DESIGN_SYSTEM.md`).
**Target Viewport:** Desktop enterprise (`1440×900px+`), responsive down to `1280px` and `1024px`, mobile-safe per SRS §10 ("responsive web interface... mobile-friendly screens") and §11 (dedicated PWA for drivers, out of scope for this doc).
**Authority:** Single source of truth for tokens and components across all 5 flagship persona screens.
**Relationship to el-nino:** Shares the Civic Green accent (`#006837`) for cross-platform Kenyan county government identity, but is a light enterprise theme throughout — CVFMS is daytime back-office software, not el-nino's 12-hour EOC cockpit. No dark-mode cockpit variant exists here.

---

## 0. Research Basis

Ran `ui-ux-pro-max --design-system` plus targeted domain searches (`product`, `style`, `color`, `typography`, `chart`, `ux`, `shadcn` stack) against the query profile: enterprise government fleet dashboard, light theme, back-office daytime use, five operational/executive personas, Next.js/Tailwind/shadcn stack, Civic Green brand constraint.

**Convergent findings adopted:**
- **Style:** *Data-Dense Dashboard* (BI/Analytics category — KPI cards, sortable tables, minimal padding, grid layout) blended with *Accessible & Ethical* (government/public-sector category — WCAG AAA target, high contrast, 16px+ text, visible focus states). Both independently recommended for this product type; neither is decorative.
- **Rejected styles, with reason:** Dark Mode (OLED) and Cyberpunk — wrong mood (night-mode/gaming), and this is explicitly a daytime tool per the project brief. Neumorphism and Glassmorphism — flagged by the tool itself as low-contrast / WCAG-risk, directly conflicting with the Accessible & Ethical requirement this system needs (approval workflows, audit trails, government users of varied literacy and eyesight).
- **Color:** The tool's literal "Government/Public Service" palette result is navy/blue (`#0F172A` / `#0369A1`) with no green — it doesn't know about the Civic Green brand constraint. Its "Hyperlocal Services" and "E-commerce" results independently landed on the same green family we need (`#059669` primary, `#ECFDF5` background, `#064E3B` text) validating that a saturated, mid-dark green reads as trustworthy/positive in this tool's model generally, not just as an arbitrary brand pick. We combine: Civic Green as the single brand/primary accent (per project mandate) + the Government palette's navy/slate as the neutral and structural color, not as a competing accent.
- **Typography:** *Corporate Trust* (Lexend headings + Source Sans 3 body) was the top match for "enterprise, government, healthcare, finance, accessibility-focused" — chosen over *Minimal Swiss* (Inter/Inter) because Lexend is purpose-designed to improve reading performance, which matters more here given the WCAG AAA target and a user base of varied literacy/eyesight across county government offices, not just general-purpose neutrality.
- **Charts:** Bar (category comparison — cost by department, utilization by station) and Line (trend over time — fuel spend, availability rate) are the only chart types this domain's data actually calls for. Radar/spider, gauge, and heatmap were considered and rejected — no metric in the SRS's KPI list (§19) or dashboard content (§6) is multi-axis, single-point, or matrix-shaped enough to need them. This mirrors, independently, the standing project rule against decorative charts (see `06_DESIGN_QUALITY_PROCESS.md`).
- **Accessibility finding carried into components directly:** "Don't convey information by color alone" (severity: High) — directly binding on the Status Pill (§3B below), which must always pair color with an icon or text label, never color alone.
- **Stack guidance (shadcn):** use `Table`/`DataTable` (TanStack Table) for all tabular views, not div-grids; use `Form` + `react-hook-form` + `zodResolver` for all the action modals in §4 below; include one `<Toaster />` in the root layout for the Confirmation Toast pattern (§4B).

---

## 1. Design Philosophy

CVFMS is a dense, transactional, audit-sensitive enterprise system serving five personas with different jobs but one shared standard. Priority order:

1. **Legibility of state** — a vehicle's status, a dispatch gate's pass/fail, a budget's variance must be readable at a glance, never requiring hover or click to disambiguate.
2. **Trust and auditability** — every consequential action (override, approval, release) must look deliberately different from a passive view (Von Restorff effect), because the SRS treats the audit trail as load-bearing, not incidental (§8, BR-009).
3. **Density without noise** — one accent color, a small type scale, and a strict spacing scale are what let five different dense screens (a queue, a board, a reconciliation view, a briefing, an operational hub) feel like one product.
4. **Accessible by default, not by retrofit** — WCAG AAA contrast and never color-only signaling are binding constraints from the first draft, not a pass applied at the end, because this is public-sector software serving users the SRS itself does not assume are technically sophisticated (§10: "simple navigation... mobile-friendly").

**"Simple" is not "sterile" — corrected 2026-09-23, checked against real apps rather than assumed.**
This project's own minimalism discipline (dissolve unnecessary containers, cut icons that don't
pass a differentiation test, one accent color, closed color list) was applied correctly on its own
terms across FRAME-07, but the cumulative effect had gone further than intended: a direct
"the app is now boring" critique was raised and checked against 10+ real reference apps rather than
dismissed. Two research passes — one on dashboard-style apps (Squarespace, Jobber, Wise, Mercury,
monday.com), one on **Turo specifically, chosen because it's genuinely information-dense
(bookings, dates, mileage, protection plans, license verification) and still doesn't read as
sterile** — found a consistent, specific set of techniques that add warmth without reopening the
closed color list or abandoning restraint. **Three now locked as standing rules, not just
observations:**
1. **Real photos are ordinary, recurring content, not a rare "identity moment."** Turo shows a
   small rounded-corner photo of the actual car on every single booking screen — not reserved for
   1-3 special screens. CVFMS previously restricted real photography to Home/Profile/Login's county
   landmark image, treating it as a deliberate, scarce exception. **That scarcity was the wrong
   call.** Vehicle photos should now appear wherever a vehicle is the subject of the screen —
   Component 11 (Trip Details), Component 17 (Trip Start/Active/End), Component 18 (Report an
   Issue), Component 19 (Maintenance Request) — see each component's updated spec below. The
   county-landmark photo policy on Home/Profile/Login is unchanged; this is an addition, not a
   replacement.
2. **Tinted info cards for contextual notices, not plain gray text.** Turo's protection-plan notice
   uses a soft, brand-tinted card background (not a plain white/gray block) with a small icon and a
   link. CVFMS already has the exact token for this without inventing a new color — `color.brand.
   primary-subtle` `#E6F2EB`, already used for Component 9's "Ready" status treatment. Reused here
   for the same purpose: a card background, `1px solid` a slightly darker tint of the same color
   (not `color.neutral.border`, which would look like an ordinary card, not a tinted one), 12px
   corner radius, 12px padding, small icon at 16-18px in `color.brand.primary`, body text in
   `color.neutral.ink` at the standard body size. Applied to contextual/informational notices that
   previously sat as plain muted text — e.g. Component 17's GPS-logging microcopy on Trip Start.
   Not applied to status values (those stay the existing colored-text-no-container treatment,
   unchanged) — this is specifically for *notices*, a different content type.
3. **Small, purposeful icons are back**, reversing Component 11's "no icons on static rows" rule
   from 2026-09-22. That rule was correct on its own narrow logic (a generic person/vehicle icon
   next to an already-labeled section duplicates the label) but the cumulative effect across the
   whole app — checklist rows, detail rows, form fields all icon-free — reads as flatter than
   intended. Turo pairs small icons (shield, car, pin) with informational content throughout, not
   only where strictly necessary for differentiation. **Corrected: a small icon (18-20px,
   `color.neutral.slate-muted` for neutral content, `color.brand.primary` inside a tinted info
   card) is now permitted on informational rows and notices for warmth, not gated behind the
   differentiation test alone.** The differentiation test still governs *navigational* icon use
   (chevron-terminated action lists, per the American Airlines/Fly Delta precedent already cited)
   — this reversal is specifically about static, informational content.

**What did not change:** the "one main CTA" per-decision scoping (Component 9's resolution stays as
originally locked — considered loosening this against Turo's multiple-bold-buttons-per-flow
pattern, but decided against it; CVFMS's existing hierarchy discipline here was a deliberate,
reasoned choice, not an accident of over-restraint, and stays as-is). The closed color list stays
closed — `color.brand.primary-subtle` is an existing token, not a new color introduced for this.

**Second pass, 2026-09-23 — "smart information categorizing and smart color use," not more
graphics.** Direct follow-up: not heavier visuals, better use of grouping and color on what's
already there. Checked Navan, Rivian, and Check specifically for this (in addition to Turo, above).
Two concrete additions:

**The Stat Tile pattern — for dense fact clusters that currently render as flat rows.** Checked
against [Check's vehicle screen](https://mobbin.com/screens/9eb57d2f-f370-4af6-95c8-0280802461fe),
which breaks up several related facts (mileage, seats, charging card, carplay) into small
individual tiles rather than a stacked list — genuinely improves scannability of dense info without
adding visual weight. **Locked spec:** 2-3 tiles per row, equal width, `color.neutral.bg` `#F8FAFC`
background (no border needed — the tonal shift from the white page is enough separation), 8px
corner radius, 12px padding. Each tile: a small icon (18-20px) at the top, `color.brand.primary` if
the fact is positive/normal, `color.status.warning` or `color.status.critical` if it's a genuine
attention-worthy state (reuses the exact status-color logic already established, not a new rule) —
then the value below it, 16px/700 `color.neutral.ink`, then the label below that, 12px/400
`color.neutral.slate-muted`. **Where it applies:** replaces flat label/value rows specifically
where 2-3 related facts sit adjacent to each other and would benefit from visual grouping — not a
blanket replacement for every label/value row in the app (Trip Info's Departure/Purpose fields, for
example, stay as plain rows; they're not a "cluster," they're sequential facts). Applied to
Component 11's Vehicle section (Fuel Level, Dispatch Clearance) and Component 17's Trip Summary
(Starting Odometer, Closing Odometer, Distance) — see each component below.

**Visual stage-stepper, replacing plain "Stage X of 3" text.** Checked against [Navan's checkout
flow](https://mobbin.com/screens/d656dceb-9a9d-4e4a-926f-eb4614b2423b), which uses a numbered
circle per step rather than a text label alone. Component 17's 3-stage trip flow (Start → Active →
Closure) already has the right underlying concept but rendered it as text only. **Locked: 3 small
circles in a row, 8px diameter, connected by a thin 1px line** — completed/current stage filled
`color.brand.primary`, upcoming stages `color.neutral.border` — sitting beside (not replacing) the
"Stage X of Y · [Label]" text, giving progress a genuine visual read instead of requiring the text
to be parsed. Applied to Component 17, all three states.

**Independently reinforced, not new:** [Booking.com's confirmation-number treatment](https://mobbin.com/screens/87f6d903-a02e-4b01-80a4-c254c429cb01)
(a reference number sitting in a light-tinted box with an icon) is a second, independent real-app
confirmation of the tinted-card technique already adopted from Turo — not applied to CVFMS's own
reference-ID field, which was deliberately de-emphasized earlier specifically so it wouldn't
compete with the destination headline; that fix stays as-is, this is just corroborating evidence
the tinted-card technique generally is sound practice.

**Third pass, 2026-09-23 — visual polish, not information architecture.** Direct critique against
rendered Trip Closure and Trip Details screens: correct content, correct structure, but visibly
less polished than Turo, Wealthfront, and Check side by side. This is a different failure mode from
the first two passes (those were about *what content appears*; this is about *how confidently it's
executed*) — checked against Wealthfront's "Transfer money" screen and Check's vehicle screen
directly, plus a further Mobbin pass ([pliability](https://mobbin.com/screens/92c29d97-80f0-442c-97f6-f150fd07bd2a)
and [Alan](https://mobbin.com/screens/e2d2c425-dcb8-4974-80fa-d2773066c6f0) for icon treatment;
[CRED](https://mobbin.com/screens/7e383067-74f6-4097-95bc-de0f445effd3),
[Lloyds Mobile Banking](https://mobbin.com/screens/01aa813d-d698-4466-8548-a1116253bb55), and
[Booking.com](https://mobbin.com/screens/a9bc7b70-344d-485c-8e5f-d33aa27d2972) for vehicle-detail
hierarchy). Four specific, mechanical gaps found — not vague "make it nicer" — all four adopted:

1. **Icon badges — icons sit inside a tinted circle, never bare.** Wealthfront, Alan, and
   pliability all wrap every icon this way; CVFMS's stat-tile and informational-row icons (added in
   the second pass, above) are flat/bare, which alone reads as unfinished next to these references.
   **Locked spec — new component, `Icon Badge`:** 32px circle (36px in stat tiles specifically, to
   match their larger padding), background `color.brand.primary-subtle` `#E6F2EB` when the icon sits
   on brand/positive content, `color.neutral.bg` `#F8FAFC` when it's neutral/informational content
   (reuses the Stat Tile's own neutral-vs-status color logic, not a new rule); icon itself centered,
   18-20px, `color.brand.primary` on the tinted-green badge or `color.neutral.slate-muted` on the
   neutral-gray badge. **Applies to:** every Stat Tile icon (Component 11's Vehicle tiles —
   supersedes the second pass's "small icon at the top" wording, which didn't specify a badge) and
   every informational-row icon added in the second pass above. Does not apply to navigational
   chevron-list icons (still governed by the differentiation test) or to status pills (already have
   their own established treatment). **Component 17's Trip Summary is no longer a Stat Tile row as
   of 2026-09-23 (reverted, see Component 17 State 2 below) — this doesn't apply there.**
2. **One hero focal element per screen, genuinely oversized.** CRED's vehicle name, Check's "IRIS",
   Lloyds' "Your profile is 50% complete" are each sized 2-3× the surrounding text — CVFMS's screens
   are flatter, with headline and body sizes sitting closer together, so nothing anchors the first
   glance. `type.hero-mobile` (22px/700, §2B3) already exists but has only ever been applied to
   Home's card time — **generalized, 2026-09-23: apply `type.hero-mobile` to the one genuine focal
   identifier of any screen**, not just card time. Concretely: Trip Details' destination name
   upgrades from `type.card-title-mobile` (16px/600) to `type.hero-mobile` (22px/700); Trip Closure
   and Active Trip's banner destination name gets the same upgrade. This is a targeted exception,
   not license to enlarge multiple elements per screen — the "exactly one dominant element per row"
   rule (§B2) still governs everything below the hero.
3. **More generous spacing.** Lloyds' tiles and Wealthfront's list rows carry noticeably more
   internal padding and inter-section air than CVFMS's current renders. **New token,
   `space.section-gap` = 32px, replacing the 24px figure used throughout §3 below** (every "24px
   between sections" reference in Components 11 through 19 is superseded by this value — the
   sections themselves and their 8px label-to-first-row rhythm are unchanged, only the gap between
   sections grows). Mobile card internal padding also grows, `space.card-padding` mobile floor 16px
   → **20px** (§2B3).
4. **Photo as Identity — generalized 2026-09-26 (was vehicle-only).** The original rule
   (vehicle photo as inline content, Booking.com/CRED/Rivian references) was correct but scoped
   too narrowly. The underlying principle is broader: **use a real image wherever it makes a
   record immediately identifiable or confirms a state without requiring the user to read.**
   This applies to:
   - **Vehicles** (job card, dispatch detail, trip detail, vehicle registry row) — full-width
     hero image, 140px height, `radius.lg` (12px) corner radius, `object-fit: cover`. Every
     "64×64px/8px-radius" reference in §3 below is superseded by this treatment. Component 17
     exception remains: photo on State 1 (Start Journey) only, not repeated across States 1.5
     and 2 of a continuous trip (see Component 17's note).
   - **Drivers** (assignment card, driver registry row, dispatch detail panel) — small circular
     avatar (40px), sourced from driver profile; initials monogram as fallback, never a generic
     person silhouette.
   - **Damage / Defect evidence** (accident report, breakdown report, defect log, Component 18)
     — the photo IS the content, not decoration. Full-width or grid layout depending on count.
   - **County branding** (mobile home screen expanded header) — already locked, unchanged.
   - **Workshop job cards** (FRAME-03) — vehicle thumbnail inline in the job detail drawer
     confirms the vehicle in the bay matches the job before work starts.
   **What it is NOT for:** maps, charts, data visualisations, stock illustrations, or making
   a screen feel less sparse. The purpose is always identity confirmation, never decoration.
   **Missing-asset rule (system-wide):** render a neutral placeholder appropriate to the
   entity type — licence plate text on a grey rect for vehicles, initials monogram for
   drivers, a camera-outline icon for damage photos not yet uploaded. Never a broken image,
   never a generic silhouette icon.

---

## 2. Canonical Token Dictionary

### A. Color Tokens

| Role | Token Name | Hex Value | WCAG Contrast (on white `#FFFFFF`) | Usage Rule |
| :--- | :--- | :--- | :--- | :--- |
| Brand / Primary Accent | `color.brand.primary` | `#006837` (Civic Green) | 7.7:1 (AAA) | Primary buttons, active nav state, links, brand marks. The *only* saturated accent in the system — do not introduce a second brand color. |
| Brand / Primary Hover | `color.brand.primary-hover` | `#00522C` | 9.9:1 (AAA) | Hover/pressed state for primary actions only. |
| Brand / Primary Subtle | `color.brand.primary-subtle` | `#E6F2EB` | — (background use) | Selected-row backgrounds, subtle badges, chart fill at low opacity. **Light-surface use only** — do not apply to the dark sidebar (see `color.brand.primary-subtle-dark` below). |
| Brand / Primary Subtle (dark surface) | `color.brand.primary-subtle-dark` | `#173829` | — (background use, on `#0F172A`) | **New (2026-09-15)**, added specifically for the sidebar's active-item chip (see Component 1 below) — `#E6F2EB` is a light-surface tint and reads as a jarring bright rectangle against the dark `#0F172A` rail. This is a desaturated, dark-context equivalent: a muted green-black blend, subtle enough to read as "selected" without competing with the rail's own darkness, verified to keep the active item's white/light text at AAA contrast on top of it. |
| Neutral / Ink (dark nav, headers) | `color.neutral.ink` | `#0F172A` | 17.9:1 (AAA) | Left nav rail background, top nav background, highest-emphasis headings on light surfaces. |
| Neutral / Slate (secondary text, borders) | `color.neutral.slate` | `#334155` | 9.6:1 (AAA) | Secondary/body text, table headers, icon default color. |
| Neutral / Slate Muted | `color.neutral.slate-muted` | `#64748B` | 4.8:1 (AA, use ≥14px) | Tertiary text (timestamps, helper text) — never body copy below 14px. |
| Neutral / Border | `color.neutral.border` | `#E2E8F0` | — (non-text) | All hairline borders, table row dividers, card outlines. |
| Neutral / Surface | `color.neutral.surface` | `#FFFFFF` | — | Card and modal backgrounds. |
| Neutral / Page Background | `color.neutral.bg` | `#F8FAFC` | — | App canvas background behind cards. |
| Status / Success | `color.status.success` | `#059669` | 4.6:1 (AA) | Positive state fills — pair with a checkmark icon, never color alone. |
| Status / Success Subtle | `color.status.success-subtle` | `#ECFDF5` | — | Success pill/badge background. |
| Status / Warning | `color.status.warning` | `#B45309` | 5.2:1 (AA) | Approaching-deadline / needs-attention-soon states — pair with a clock/warning icon. |
| Status / Warning Subtle | `color.status.warning-subtle` | `#FFFBEB` | — | Warning pill/badge background. |
| Status / Critical | `color.status.critical` | `#B91C1C` | 6.1:1 (AA) | Overdue, blocked, failed-gate states — pair with an alert-triangle/x icon. |
| Status / Critical Subtle | `color.status.critical-subtle` | `#FEF2F2` | — | Critical pill/badge background. |
| Status / Neutral (inactive/disposed) | `color.status.neutral` | `#475569` | 8.3:1 (AAA) | Disposed, written-off, or otherwise inactive states. |

**Binding rule (from research, §0 above):** color is never the sole carrier of status information. Every status pill, table cell, or KPI delta that uses a status color must also carry an icon and/or text label legible without color (severity: High per `ui-ux-pro-max` UX guideline "Color Only").

### B. Typography Tokens

**Pairing:** *Corporate Trust* — Lexend (headings) + Source Sans 3 (body), per §0 research.

```css
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap');
```

| Token | Font | Size / Line-height | Weight | Usage |
| :--- | :--- | :--- | :--- | :--- |
| `type.page-title` | Lexend | 24px / 32px | 600 | Page-level heading (one per screen). |
| `type.section-title` | Lexend | 18px / 26px | 600 | Panel/card group headings (e.g. "Needs Attention"). |
| `type.metric-large` | Lexend | 28px / 34px | 700 | Hero KPI values (Executive dashboard only). |
| `type.metric-medium` | Lexend | 24px / 30px | 600 | Standard KPI tile values. |
| `type.body` | Source Sans 3 | 14px / 22px | 400 | Default body/table text. |
| `type.body-strong` | Source Sans 3 | 14px / 22px | 600 | Row-dominant text per the row-hierarchy rule (§B2 below). |
| `type.label` | Source Sans 3 | 12px / 16px | 500 | Pill text, table headers (uppercase, +0.02em tracking), form labels. |
| `type.caption` | Source Sans 3 | 12px / 16px | 400 | Timestamps, helper text, secondary metadata. |

**§B3 — Mobile type & spacing scale (added 2026-09-21, FRAME-07).** No explicit mobile scale existed
before this — FRAME-07 prompts described sizes qualitatively ("bold," "small," "muted") without
pinning values, and renders came out feeling oversized and inconsistent (user: "ours seem big and
with no system"). Root cause: without pinned values, renders defaulted toward Material 3's own type
scale, which runs larger by design (M3's whole philosophy favors generous, high-legibility type) —
the same category of problem as the earlier "generic M3" finding (shadows/radii), just showing up
as size this time. **Reuses desktop tokens wherever they fit — mobile is not a license to invent a
separate, bigger scale:**

| Element | Token | Size / Line-height | Weight |
| :--- | :--- | :--- | :--- |
| Hero time (added 2026-09-21, borrowed from Airtasker's price prominence) | `type.hero-mobile` (new) | 22px / 28px | 700 (Lexend) |
| Card dominant identifier (destination) | `type.card-title-mobile` (new) | 16px / 22px | 600 (Lexend) |
| Status label (small caps) | `type.label` (reused, unchanged) | 12px / 16px | 500, uppercase +0.02em |
| Body/context lines (requester, vehicle) | `type.body` (reused, unchanged) | 14px / 22px | 400 (Source Sans 3) |
| Muted/secondary text | `type.caption` (reused, unchanged) | 12px / 16px | 400 |
| Button label | `type.button-mobile` (new) | 15px / 20px | 600 (Source Sans 3) |

**Note on `type.hero-mobile`:** the one deliberate exception to "reuse desktop tokens, don't invent
a bigger scale" (§B3 above) — earned specifically because it's the single most prominent element on
the card by design, the mobile equivalent of Airtasker's bold price treatment. Used for time only;
does not license bumping any other element to this size.

**Mobile spacing — same 8pt scale as desktop, no new values invented:**
- Card internal padding: **20px, raised from 16px (2026-09-23, §1 third pass** — checked against
  Lloyds Mobile Banking and Wealthfront, whose tiles/rows carry more internal air than CVFMS's
  original 16px floor) (`space.card-padding` lower bound).
- Gap between elements within a card: 8px.
- Gap between cards: 12px.
- Card corner radius: `radius.lg` (12px) — exactly matching desktop, not M3's stock rounding.
- **Button height: 44px exactly (revised 2026-09-22, was 48px)** — this project's own touch-target
  research established 44×44px as the actual accessibility minimum (Apple HIG), not 48px; 44px is
  correct and still fully compliant. Treated as a ceiling too — do not let a button render taller,
  on the assumption "bigger is more accessible." See Component 9's button spec for the fuller
  fix (width/shape, not just height, was the real source of the "too big" complaint).
- **Minimum 8px gap between adjacent touch targets** (e.g. the Accept/Decline button pair) — a
  formal touch-interaction rule, not a style choice; found via a dedicated `ui-ux-pro-max` research
  pass (2026-09-21, see below), not something this doc had explicitly stated before.

**§B4 — Mobile research pass (2026-09-21).** Every FRAME-07 decision up to this point was reactive
— fixing a specific complaint or borrowing a pattern from one screenshot at a time — unlike the
desktop system, which got a deliberate, upfront `ui-ux-pro-max` research pass before any screen was
built (§0). Ran the equivalent pass for mobile. Two outcomes:
- **Confirmed, independently:** querying fresh for "clean readable professional government
  accessible" still returns *Corporate Trust* (Lexend + Source Sans 3) as the top match — the
  existing typography choice holds up from a mobile-specific angle too, not just carried over
  from desktop by assumption. *Flat Design* and *Minimalism & Swiss Style* both independently
  matched this project's existing flat-card, no-shadow, single-accent direction.
- **New, corrective finding: no emoji as icons, anywhere in this system.** Source material flags
  this twice as a common "unprofessional UI" mistake — real icons must come from a proper SVG set
  (Heroicons, Lucide, or equivalent), never emoji characters. **Every FRAME-07 prompt written so
  far has used emoji (🔵🟢👤🚗🔔🕐🆘) as icon placeholders in the prompt text** — if the Figma
  agent has been rendering these literally as emoji rather than resolving them to proper icons,
  this is a likely, previously-unidentified contributor to the inconsistent, unprofessional icon
  feel across every render reviewed so far. **Standing rule from this point on: prompts must say
  "use an SVG icon depicting [X], not an emoji character" explicitly, and any emoji already
  embedded in a spec (this doc included) is a placeholder for what the icon should depict, never
  an instruction to render the emoji glyph itself.** *Flat Design*'s "icon-heavy" classification
  also confirms keeping the person/vehicle icons was the right call — the earlier back-and-forth
  on whether to include them was really about execution (emoji vs. real icon), not about whether
  icons belonged there at all.
- **Icon style, locked (2026-09-21), closing the "icons look inconsistent" gap flagged earlier but
  never turned into an actual rule.** One icon set, one stroke weight, system-wide: outline-style
  icons (not filled/solid), 1.5px stroke, from a single set (Heroicons or Lucide — pick one and use
  it exclusively, never mix sets within a screen). Icon color always matches its adjacent text
  color exactly (see the per-state color table above) — an icon never introduces a color its own
  row's text doesn't already have. This applies to every icon on every FRAME-07 screen: status
  icons, route dots, person/vehicle icons, SOS, tab bar icons — one visual language, not five.

**Icon Badge (new component, 2026-09-23 — §1 third pass).** A tinted circle wrapper around an
icon, used wherever an icon needs more visual presence than the plain "icon matches adjacent text
color" rule above provides — Stat Tile icons and informational-row icons specifically, not every
icon in the system. 32px circle (36px inside Stat Tiles, to match their larger internal padding);
background `color.brand.primary-subtle` `#E6F2EB` for brand/positive content, `color.neutral.bg`
`#F8FAFC` for neutral/informational content; icon centered, 18-20px, `color.brand.primary` on the
green badge or `color.neutral.slate-muted` on the gray badge. Does not apply to navigational
chevron-list icons or status pills, both of which keep their existing, separate treatments.

**§B2 — Row-level type hierarchy (system-wide rule, applies to every list/row/card component):**
- Exactly one dominant text element per row (`type.body-strong` or larger).
- Everything else in that row drops at least one size/weight level below the dominant element.
- Never more than 2 distinct type sizes visible in a single row.
- Color reinforces hierarchy (e.g., a status color on the dominant element); it never substitutes for it.

### C. Spacing & Radius Tokens

8pt base scale: `0 / 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64px`. Data-dense contexts (tables, dense lists) use the 8–12px band for internal padding per the Data-Dense Dashboard style guidance (§0); card-level and page-level spacing uses 16–32px.

| Token | Value | Usage |
| :--- | :--- | :--- |
| `radius.sm` | 6px | Status pills, small badges. |
| `radius.md` | 8px | Buttons, inputs, table cells. |
| `radius.lg` | 12px | Cards, modals, panels. |
| `space.table-row` | 36px row height | Dense tables (Vehicle Registry, Fuel Log). |
| `space.card-padding` | 16–20px (mobile floor raised to 20px, 2026-09-23 — see §2B3) | Standard card interior padding. |
| `space.grid-gap` | 16px | Grid/flex gaps between cards and panels. |
| `space.section-gap` | 32px (raised from 24px, 2026-09-23 — see §1, third pass) | Gap between labeled sections on a mobile detail screen (Trip Info / Requester / Vehicle, etc.); the 8px section-label-to-first-row rhythm is unchanged. |

### D. Elevation & Motion

| Token | Value | Usage |
| :--- | :--- | :--- |
| `shadow.card` | `0 1px 2px rgba(15,23,42,0.06), 0 1px 3px rgba(15,23,42,0.08)` | Resting card elevation — subtle, never decorative drop-shadow. |
| `shadow.modal` | `0 10px 15px rgba(15,23,42,0.12), 0 4px 6px rgba(15,23,42,0.08)` | Modals, drawers, popovers. |
| `motion.micro` | 150–200ms ease-out | Hover, focus, pill state changes. |
| `motion.transition` | 250–300ms ease-in-out | Drawer slide-in, drill-down expand, toast entry. |
| `motion.reduced` | Respect `prefers-reduced-motion` | All of the above degrade to opacity-only or instant when set. |

---

## 3. Core Components

**Component index — added 2026-09-23 to solve navigability, not to split this file.** This file
covers both desktop (Components 1-8) and mobile (Components 9-19) — considered splitting into
separate desktop/mobile files when the size became a real problem, and decided against it (shared
token dictionary, this project's own "single source of truth" framing in CLAUDE.md, and the long
citation trail throughout `08_PROJECT_HANDOVER.md` all made a split riskier than it's worth right
now). This index is the lighter fix: jump to any component directly instead of scrolling.

| # | Component | Platform | Screen/Frame | Render status (as of 2026-09-23) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [App Shell (Top Nav + Left Rail)](#component-1--app-shell-top-nav--left-rail) | Desktop | All desktop screens | Pre-existing, not touched this session |
| 2 | [KPI Tile](#component-2--kpi-tile) | Desktop | Dashboards | Pre-existing, not touched this session |
| 3 | [Status Pill](#component-3--status-pill) | Desktop | System-wide | Pre-existing, not touched this session |
| 3B | [Multi-Stat Card](#component-3b--multi-stat-card) | Desktop | Dashboards | Pre-existing, not touched this session |
| 3C | [Needs Attention / Action List](#component-3c--needs-attention--action-list) | Desktop | FRAME-01 (Grace) | Pre-existing, not touched this session |
| 4 | [Action Drawer](#component-4--action-drawer-modal-alternative-for-approvalsoverrides) | Desktop | FRAME-02 (Daniel) | Pre-existing, not touched this session |
| 4B | [Confirmation Toast](#component-4b--confirmation-toast) | Desktop | System-wide | Pre-existing, not touched this session |
| 5 | [Work Order Board (Kanban)](#component-5--work-order-board-kanban) | Desktop | FRAME-03 (Peter) | Pre-existing, not touched this session |
| 6 | [Data Table](#component-6--data-table) | Desktop | System-wide | Pre-existing, not touched this session |
| 7 | [Budget Bar](#component-7--budget-bar) | Desktop | FRAME-05 (Miriam) | Pre-existing, not touched this session |
| 8 | [Trend / Comparison Chart](#component-8--trend--comparison-chart) | Desktop | Dashboards | Pre-existing, not touched this session |
| 9 | [Mobile Assignment Card](#component-9--mobile-assignment-card-added-2026-09-21) | Mobile | FRAME 7A (Home) | ✅ Rendered, multiple fix rounds confirmed |
| 10 | [Mobile Pre-Trip Inspection Row](#component-10--mobile-pre-trip-inspection-row-added-2026-09-22-frame-7b) | Mobile | FRAME 7B | ✅ Rendered, multiple fix rounds confirmed |
| 11 | [Assignment Detail / "View Details"](#component-11--assignment-detail--view-details-added-2026-09-22-frame-07) | Mobile | FRAME 7A.1 | ✅ Rendered, fix rounds confirmed |
| 12 | [Driver Profile](#component-12--driver-profile-added-2026-09-22-frame-7d) | Mobile | FRAME 7D | ⚠️ Prompted, not yet rendered/confirmed |
| 13 | [Trips Tab](#component-13--trips-tab-added-2026-09-22-frame-7e) | Mobile | FRAME 7E | ⚠️ Prompted, not yet rendered/confirmed |
| 14-16 | [Splash, Login, First-Run Setup](#components-1416--splash-login-first-run-setup-added-2026-09-22-frame-07-pre-auth) | Mobile | FRAME 7-PRE | ⚠️ Prompted, not yet rendered/confirmed |
| 17 | [Trip Start / Active Trip / Trip End](#component-17--trip-start--active-trip--trip-end-added-2026-09-22-frame-7c) | Mobile | FRAME 7C | ✅ Rendered, fix rounds confirmed |
| 18 | [Report an Issue: Breakdown / Accident](#component-18--report-an-issue-breakdown--accident-added-2026-09-23-frame-7f) | Mobile | FRAME 7F | ✅ Rendered, fix round confirmed |
| 19 | [Submit Maintenance Request](#component-19--submit-maintenance-request-added-2026-09-23-frame-7g) | Mobile | FRAME 7G | ⚠️ Prompted, not yet rendered/confirmed |

**Reading the render status column:** ✅ means an actual screenshot came back and was checked
against spec in this session — treat these as verified. ⚠️ means a prompt was written and handed
off, but no render has been reviewed yet — treat these as unverified specs, not confirmed working
screens, the same distinction that prompted this whole index to begin with (see
`08_PROJECT_HANDOVER.md` for the history of that gap being found).

### Component 1 — App Shell (Top Nav + Left Rail)

**Revision note (2026-09-13, product owner feedback on first FRAME-01 render):** the nav list below was corrected from an earlier persona-scoped summary (Overview/Requisitions/Workshop/Compliance/Finance/Reports — a paraphrase, not sourced) to the SRS's own module list, verbatim, per explicit product owner instruction: *"List the modules on the left as listed in Functional section."* The nav is now a direct transcription of SRS §2 (System Scope, the Module/Major Functions table), not a curated or persona-filtered subset.

Dark left rail (`color.neutral.ink`, `#0F172A`) fixed width 240px (`--sidebar-width`), containing: county/system wordmark, primary nav, user/role indicator pinned to bottom. Top bar (`color.neutral.surface`, white) height 56px (`--header-height`), containing: page title slot, global search, notification bell, user avatar menu. Rest of the app surface is light (`color.neutral.bg`) — the dark rail is the only dark surface in the system, chosen deliberately as a wayfinding anchor, not a step toward a dark theme.

**Page title slot — greeting vs. plain title, decided per screen type (2026-09-13):** the page title slot takes one of two forms, chosen deliberately per screen, not applied uniformly:
- **Greeting block** (date + "Good [morning/afternoon/evening], [Name]" + a small system-status line) — reserved for once-per-session daily landing screens only. Originally FRAME-01 (Grace's Overview) exclusively; **extended 2026-09-21 to FRAME-07's driver home screen (7A)** on the same justification: a driver opens the mobile app once per shift to see their assignment before doing anything else, the identical once-per-session usage pattern as Grace's desktop landing page, just on a different device. Not extended to any other screen — the reasoning is usage-pattern-specific, not "any home-ish screen qualifies."
- **Plain page title + status subtitle** (e.g. "Dispatch & Requisition Queue" / "Active Handler: Daniel Otieno • Gate Check System Online") — used everywhere else (FRAME-02 through FRAME-06, FRAME-08, FRAME-09, and any future work-surface screen). These are screens a user jumps into and out of repeatedly throughout the day, not once-per-session landing pages — a repeated greeting there is chrome without a job to do, since it doesn't set context a user needs freshly on the 20th visit the way it does on the 1st visit of the day. The status subtitle (system-state info specific to that screen's function) is kept regardless of which title form is used, since it's real information, not decorative.
Do not extend the greeting pattern to any further screen without a fresh justification tied to that screen's actual usage pattern (once-per-session landing vs. repeated work surface) — this is a deliberate, narrowly-scoped exception, not an oversight to "fix" toward uniformity later.

**SUPERSEDED (2026-09-15) — see grouped nav below.** The flat 20-item list (kept here for traceability) was the product owner's first instruction ("list the modules as given in the Functional section," 2026-09-13). A follow-up product owner instruction (Patrick Swift, via a pillar diagram + direct message, 2026-09-14/15) explicitly asked to **group the menus and sub-menus** into named pillars, plus add a Settings menu — this is a real, deliberate revision of the earlier flat-list instruction, not a conflicting one to reconcile by guessing; the product owner changed their own ask.

Flat list (superseded):
1. Fleet Registry · 2. Vehicle Allocation · 3. Vehicle Request · 4. Dispatch Management · 5. Journey Management · 6. Driver Management · 7. Fuel Management · 8. Maintenance · 9. Workshop Management · 10. Insurance · 11. Compliance · 12. Accident Management · 13. GPS/Telematics · 14. Vehicle Expenses · 15. Procurement · 16. Disposal · 17. Stores/Spare Parts · 18. Reporting & BI · 19. Administration · 20. Audit

**Primary nav — grouped, per product owner pillar diagram (2026-09-15):**

The product owner supplied 6 pillars with key capabilities (Vehicle Management, Driver Management, Fuel Management, Maintenance, Tracking & Telematics, Fleet Analytics) and asked to group the existing 20 modules into pillar → sub-menu structure, plus a Settings group. Mapping every module against the 6 named pillars left 3 modules — Vehicle Allocation, Vehicle Request, Dispatch Management — with no clean home (they're operational workflows, not vehicle/driver/fuel/maintenance/tracking/analytics categories, and Dispatch Management specifically is the core of Daniel's entire persona and FRAME-02's BR-001–005 gate). **A 7th pillar, "Operations," was added to hold these three — this is an assumption made to keep moving under time pressure, not a product-owner-confirmed pillar. Flag it back to the product owner (Patrick Swift) for confirmation before treating it as settled**, the same way the RBAC-visibility question below remains open.

1. **Operations** *(assumed 7th pillar — not in the product owner's original 6, pending confirmation)*
   - Vehicle Request
   - Vehicle Allocation
   - Dispatch Management
   - Journey Management
2. **Vehicle Management**
   - Fleet Registry
   - Insurance
   - Compliance
   - Disposal
3. **Driver Management**
   - Driver Management
   - Accident Management
4. **Fuel Management**
   - Fuel Management
5. **Maintenance**
   - Maintenance
   - Workshop Management
   - Stores/Spare Parts
   - Procurement
6. **Tracking & Telematics**
   - GPS/Telematics
7. **Fleet Analytics**
   - Reporting & BI
   - Vehicle Expenses
8. **Settings** *(product owner's explicit instruction — "And Settings Menus")*
   - Administration
   - Audit

**Placement notes (so a future reviewer can check the reasoning, not just the result):** Journey Management went to Operations, not Tracking & Telematics, because it's trip/journey record-keeping (SRS §5.5), not live GPS monitoring — the pillar's own key-capabilities list ("GPS, geofencing, routes, speed, idling, trips, vehicle utilisation") does mention "trips," which is a legitimate alternate reading; flag this specific placement for product owner confirmation too if precision matters here. Vehicle Expenses went to Fleet Analytics, not its own group, because the pillar's key capabilities explicitly name "Cost/vehicle, cost/km" — a direct match. Accident Management went under Driver Management (not Vehicle Management) because accidents are logged against a driver's record/violations, matching Driver Management's "violations" capability.

**Open question — RBAC-scoped visibility vs. full list for every role (unchanged from the original flat-list version):** the SRS itself (§4) ties access to "role, department, directorate, vehicle pool, location/station, transaction type and approval authority," which implies not every role should see all pillars/sub-items (e.g. a Driver has no reason to see Procurement or Disposal). Still unresolved — FRAME-01 (Grace, the broadest operational role) should show the full grouped list; narrower roles built in later frames should confirm their subset with the product owner.

**Layout implication (updated for grouped nav):** a collapsible pillar → sub-menu structure (accordion-style, one pillar expanded at a time, or all expanded by default with individual collapse) fits a 240px rail far better than the old flat scrolling 20-item list did — grouping was in part a usability fix for exactly the scroll problem flagged in the prior version of this note. Whichever pillar contains the active screen's module should be expanded by default on load.

**Active-item indicator — rounded chip, not a left accent bar (2026-09-15, benchmarked against Airwallex, Asana, and Indeed sidebars).** All three converge on the same active-state pattern regardless of light/dark sidebar base: a soft, rounded background chip behind the active row (comfortable padding, `radius.md` corners, not edge-to-edge) — not a thin left accent bar. Adopted system-wide for the active sub-item: background `color.brand.primary-subtle-dark` (`#173829`, the dark-context equivalent added above — never the light-surface `#E6F2EB`), text in white or `color.brand.primary`-tinted light green for extra emphasis, `radius.md` rounded corners, comfortable internal padding matching the row's existing height. The sidebar's own base color (`#0F172A`) is unchanged — this is scoped to the active-item indicator only, also incorporating the tree-connector line and other details already specified above.

### Component 2 — KPI Tile

**Default (revised 2026-09-16 — see reasoning below): plain stat card, no delta chip, no sparkline.** Structure: label (`type.label`, `color.neutral.slate-muted`) → value (`type.metric-medium`), nothing else, by default. Used in a 4-up row on Grace's Overview and Miriam's Finance dashboard; Sarah's Executive dashboard uses `type.metric-large` in a 3–4 up row as the sole above-the-fold content.

**Card separation from page background — mandatory, found missing in rendered screens (2026-09-16), confirmed against a real reference on 2026-09-18.** `color.neutral.surface` (`#FFFFFF`) against `color.neutral.bg` (`#F8FAFC`) is only a ~3% lightness difference — real, correct as a token pair, but too subtle on its own to read as a distinct surface once rendered, especially with no shadow. **Checked directly against [Airwallex's own dashboard](https://mobbin.com/screens/f0165978-3117-45a7-88f0-1a8a97007275)** (the same app already used as this project's simplicity benchmark for the KPI-tile delta-chip decision above) — every stat tile and section card there has a visible thin gray border on white fill, sitting on a light-gray page background; it does not rely on background-tint alone anywhere on that screen. Every KPI Tile, and every card-shaped surface in this system, must have at minimum: `1px solid color.neutral.border` (`#E2E8F0`) on all four sides, `radius.md` corners. Do not omit the border on the assumption the background-color difference is sufficient — it is not, and this caused a real rendered defect (see `09_PATTERN_LIBRARY.md`'s pre-flight checklist).

**Delta chip is now OPT-IN, not default (2026-09-16, benchmarked against [Airwallex's dashboard](https://mobbin.com/screens/adfc8a85-a15c-4405-b9ef-7136e216adba) and [Uxcel's dashboard](https://mobbin.com/screens/51ce5df6-f6d9-49b5-a96d-f47a1c9df99b)).** Both references — chosen by the user specifically as "incredibly simple but well designed" — converge on the same discipline: one accent color total, KPI numbers as plain black text with no default decoration (no colored dot, no delta arrow, no icon-per-metric), flat cards, minimal chrome. Our prior spec mandated a colored delta chip on every KPI tile by default (e.g. "Availability 89% ↑2%") — this is genuinely more decoration than either reference actually uses, and doesn't match the simplicity direction the user has asked for. **Only add a delta chip when that specific number's meaning genuinely depends on the comparison** — e.g. Sarah's "Fleet Availability 89%, target: 85%" (Component 3, large tile), where the whole point of the number is whether it's above or below target. Name this explicitly in the prompt when it's needed; don't assume it automatically the way the prior spec did. This does not retroactively change FRAME-01/FRAME-04's already-built delta chips — applies to new screens/prompts going forward.

### Component 3 — Status Pill

Height 20px, horizontal padding 8px, radius `radius.sm` (6px), `type.label`. Always icon + text, never a bare color chip (binding accessibility rule, §0/§A). Vehicle statuses map to the SRS's own status enum (§5.1): `Active`/`Available` → success; `On Trip`/`Assigned` → brand-subtle (informational, not a judgment); `Under Maintenance`/`Grounded` → warning or critical depending on `status_reason_code` severity; `Accident`/`Impounded`/`Lost/Stolen` → critical; `Awaiting Disposal`/`Disposed`/`Written Off` → neutral.

### Component 3B — Multi-Stat Card

A card presenting 2–3 related figures grouped under one heading (e.g., a department's vehicle count + utilization % + idle count together), used where the SRS's dashboard content groups metrics by dimension (e.g., §7.1 "departmental fleet utilization benchmarks"). Internal type hierarchy follows §B2.

### Component 3C — Needs Attention / Action List

A synthesized, urgency-ranked list — not a comprehensive table. Scoped tightly (Overdue + Due This Week only; anything further out belongs in a linked Compliance destination) because the SRS's own alert model is time-boxed (30/14/7-day windows, §5.23) rather than "show everything." Each row: one dominant identifier (vehicle reg / request ID), a status pill, a one-line reason, and a direct action button scoped to the viewing persona's authority (e.g., Grace sees "Reallocate" / "Approve" / "Override"; Daniel sees "Dispatch" / "Return to Requester").

### Component 4 — Action Drawer (modal alternative for approvals/overrides)

Slide-in drawer with scrim, not a static side panel — used for Grace's four action flows (Registry Edit, Reallocate, Dispatch Override, Maintenance Approval) and Daniel's Dispatch Gate Checklist. Built with shadcn `Sheet` + `Form` + `react-hook-form` + `zodResolver` per the stack research (§0). An override action always requires a justification text field before the confirm button enables — this is a direct implementation of BR-009 (all approvals recorded in the audit trail) and the fraud-prevention framework in the architecture summary §6.

### Component 4B — Confirmation Toast

Every state-changing action (approve, override, dispatch, release) confirms via a toast (shadcn `Sonner`/`Toaster`, one instance in the root layout per stack guidance), not a silent UI update — satisfying the "Submit Feedback" UX rule (loading → success/error, never no feedback) surfaced in research (§0).

### Component 5 — Work Order Board (Kanban)

Peter's primary surface: Diagnosis → In Repair → Awaiting Parts → Quality Inspection → Ready for Release. Each card: vehicle reg (dominant), assigned mechanic, linked parts requests with live stock-status pill, and age-in-column indicator. The Ready-for-Release column's release action is disabled until the QA checklist (a required sub-component, not implied) is complete.

### Component 6 — Data Table

Built on shadcn `Table` + TanStack Table (`DataTable` pattern) per stack research — never a div-grid. Sortable columns, filter-chip row above the table for common filters (department, status, date range), sticky header, `space.table-row` (36px) row height, horizontal scroll wrapper on narrow viewports (never a page-level horizontal scroll). Used for the Fleet Registry, Fuel Log, and any full-list destination linked from a summary component.

**Table-as-card separation — mandatory, same defect as Component 2 (found 2026-09-16).** The whole table sits inside a card: `color.neutral.surface` background, `1px solid color.neutral.border` on all four sides, `radius.md` corners — do not let the table render as bare rows floating directly on the page background with only a header underline, which is indistinguishable from the page canvas at this system's actual background/surface contrast. Row dividers between data rows use the same `color.neutral.border` at 1px, header row gets a `color.neutral.bg` tint (slightly darker than the body rows) to separate it from the data without needing a heavier rule, and filter-chip controls above the table are their own bordered elements (not bare text), so the whole block reads as one clearly bounded surface, not text loose on the page.

### Component 7 — Budget Bar

A horizontal bar comparing actual vs. budgeted spend per department/cost-center, used on Miriam's Finance dashboard. Actual fill in `color.brand.primary` when under budget, `color.status.critical` when over — with the percentage explicitly labeled in text alongside the bar (never color/length alone), per the same accessibility rule as Status Pills.

### Component 8 — Trend / Comparison Chart

Line chart for trend-over-time metrics (fuel spend, availability rate over the last 6–12 months) and bar chart for category comparison (cost by department, utilization by station) — the only two chart types this system uses, per §0 research. No radar, gauge, donut, or heatmap anywhere in this system: no metric in the SRS's KPI list (§19) is multi-axis, single-point, or matrix-shaped enough to justify one, and every chart must pass the decorative-element test in `06_DESIGN_QUALITY_PROCESS.md` before it's added to any screen.

### Component 9 — Mobile Assignment Card (added 2026-09-21)

**Why this exists as a locked component, not another round of prose description.** FRAME-07's
assignment cards went through many individually-justified fixes (dot markers, chips, hero time,
status badges, differentiation icons) that each solved a real problem in isolation, but the
cumulative result kept failing on hierarchy, sizing, weight, spacing, color, and buttons anyway —
because no single rule ever governed all of them together. This component is the fix: every value
below is exact and closed, not descriptive. A Figma build that doesn't match one of these values is
wrong, full stop — there is no "close enough" or agent discretion on any line of this spec.

**Structure — exactly 4 visual groups per card, nothing else:**
1. Status row: status label text, no chip container (left) + time, small/secondary (right) + chevron — every card gets a
   chevron, no exceptions; time never grows beyond this row's secondary size anywhere in this
   component (see the hierarchy-consistency fix below — this is a hard constraint, not a style
   preference)
2. Journey block — a vertical two-point timeline, not a flat line (revised 2026-09-21, colors
   locked 2026-09-22, see below): a filled `#3B82F6` origin dot, a short vertical connector, a
   filled `color.brand.primary` destination dot beside the destination headline (the one true
   hero of the card)
3. Detail block (requester + vehicle, visually secondary, same weight as each other)
4. Action zone (button/buttons)

**Hierarchy consistency, locked (2026-09-21) — this was inconsistent across cards and that was the
actual problem, not any single card's design.** A rendered build treated Card 1 correctly (time
small and secondary, destination the one bold hero) but treated Cards 2 and 3 differently (time
promoted to its own bold headline above the journey) — giving those two cards two competing
dominant elements and directly violating §B2 (exactly one dominant element per row/card). **Card
1's treatment is the correct one and is now mandatory for all cards, no per-card variation
permitted:** time is always small/secondary, in the status row, never a headline of its own.

**Journey visual upgraded (2026-09-21) from a flat line to a vertical dot-connector-dot timeline**
— a rendered build introduced this and it's a genuine improvement, kept and formalized. Origin:
filled dot, `#3B82F6` (blue). Destination: filled dot, `color.brand.primary` `#006837`, paired
with the destination headline text. **Colors locked 2026-09-22** (see the route-dot history note
earlier in this component) — the two dots differ by *color*, not shape; both are solid/filled
circles. This isn't a never-color-alone violation the way a status label would be, since the dots
aren't the only signal of which end is which — they're paired with actual address text ("Nakuru
HQ" / "Nakuru Sub-County Office") immediately beside each one. A short vertical line connects the
two dots. This replaces the earlier flat "🔵 From [origin]" single-line treatment entirely — do
not build both.

**Revision (2026-09-21) — destination is the hero, not time.** Originally specified time as the
single oversized "hero" element. A rendered build promoted destination to the bold headline
instead, with time as a smaller right-aligned value on the same row — and on reflection this is
correct, not a defect to revert. It resolves a contradiction this doc never caught: an earlier
section (`04_FIGMA_SCREEN_BLUEPRINT.md`'s per-card rules) already said "one dominant identifier
(destination)," which this component's original hero-time rule silently overrode without
reconciling. Destination is also the more useful thing to scan three different cards apart by —
time values look visually similar to each other, place names don't. **Locked now: destination is
the headline (left rail), time is a secondary value (right rail, same row) — the receipt-style
dual-rail pattern this project adopted early in FRAME-07's design, finally applied correctly here.**

**Revision (2026-09-21) — chip sizing and hierarchy contrast, checked against [inDrive's Order
screen](https://mobbin.com/screens/ad7715b7-1700-49cc-9e1d-02df2a4e673a).** User flagged the status
chip renders too large, and that overall hierarchy contrast is weaker than inDrive's — checked
directly: inDrive's price ($650) is dramatically larger than its supporting chips/rows (a much
bigger size jump than this component had), and its chips ("Pay with SPEI," "Movers") are small and
text-hugging, not blocky. **Status chip now reuses the desktop Status Pill's exact sizing**
(`03_MASTER_DESIGN_SYSTEM.md` Component 3: 20px height, 8px horizontal padding, `radius.sm` 6px)
instead of an unspecified/oversized chip — the same discipline already proven on desktop, just
never carried over to mobile. **Person/vehicle detail-block icons are back in** — user confirmed
they're fine; the earlier "remove them" rule is retracted (see the removed-elements note below).

**Correction (2026-09-21) — the destination headline bump to 20px was a reasoning error, rolled
back to 16px.** Comparing against inDrive's price to widen the hierarchy gap conflated two
different things: inDrive's price is a genuine page-level hero, appearing **once** on the whole
screen. This card's destination text appears **three times**, once per card — a repeated row-level
title, not a singular hero. iOS's own type scale treats these as separate tiers for exactly this
reason: a one-time Title (20-28px) versus a repeated list-row Headline (17px semibold) are not
interchangeable just because both are "the bold text." Checked directly against real per-row
titles (Airtasker's task titles, CVS Health's checklist row titles, Jira's task titles) — all sit
in the 15-17px range, not 20px+, because they repeat per row rather than appearing once per screen.
**Locked at 16px** — enough weight to lead the row, without borrowing hero-scale sizing that
belongs to a genuinely singular element this screen doesn't have.

**Status chip container dropped entirely (2026-09-22) — checked whether chips were even needed.**
User asked directly whether the chip was necessary or well-implemented, given it's been a recurring
source of sizing/color problems. Checked real professional apps: some do use small chips ([Alan](https://mobbin.com/screens/6d226768-0103-4d13-a508-42de0ff39c76),
[SHEIN](https://mobbin.com/screens/48e3dd57-f299-4681-afe6-82fa3b4f7ce3)), but just as many
respected apps use **plain colored text with no chip container at all** ([OKX](https://mobbin.com/screens/48eed82e-300c-4939-8261-8330ff6fc7da)'s
"Pending release," [Yami](https://mobbin.com/screens/2ef4581c-b9d7-4aa1-a93c-dcb02e2107fc)'s
"Cancelled"). Plain colored text still satisfies "never color alone" — the word itself carries
meaning independent of color, the chip's background tint was never the part doing that job.
**Dropped the chip background/border/padding container entirely — status is now plain colored,
uppercase, tracked text, no box around it.** This removes an entire recurring problem source
(sizing, radius, padding all needed no further tuning once the container itself is gone).

**Locked type scale for this component — 4 sizes total, no fifth size permitted:**

| Element | Size / Weight | Color |
| :--- | :--- | :--- |
| Status label text (no chip container) | 12px / 600, uppercase, +0.02em | Status color (see below) |
| Destination (headline) | 16px / 700 (Lexend) | `color.neutral.ink` (#0F172A) |
| Time (secondary, right rail) | 14px / 600 (Source Sans 3) | `color.neutral.slate` (#334155) |
| Route line | 14px / 400 (Source Sans 3) | `color.neutral.slate` (#334155) |
| Detail block + button label | 14px / 400 body, 15px / 600 button | `color.neutral.slate` (#334155) body |

**Locked spacing — 3 gap values total, no other gap permitted anywhere in this component:**
- 4px: between the destination headline and its own supporting elements (same conceptual group)
- 12px: between each of the 4 structural groups (status→headline, headline→route, route→detail,
  detail→action)
- 16px: card internal padding on all four sides
- **No internal divider lines anywhere in this component.** A rendered build added a horizontal
  rule between the route line and detail block — this directly contradicts the "dissolve
  unnecessary containers, let whitespace do the grouping" principle already adopted for this
  screen (see the Kole Jain breakdown notes). Whitespace and the 12px gap above are the only
  grouping mechanism; no divider is ever added to close that gap visually.

**Locked color usage — closed list, nothing else may carry color:**
- Civic Green `#006837`: filled primary buttons only (Accept, Start Pre-Trip Inspection).
- **Status chip semantics corrected (2026-09-21), checked against [Atlassian's Lozenge
  component](https://atlassian.design/components/lozenge/examples).** Atlassian's semantic mapping
  classifies "in progress" as **Information** (a neutral, ongoing state), reserving **Success**
  specifically for "completed, approved, resolved." Checking CVFMS's own existing desktop rule
  (Component 3, Status Pill) confirms this same distinction already exists here and was simply
  never carried over to mobile: "`On Trip`/`Assigned` → `color.brand.primary-subtle` (informational,
  not a judgment)" — being mid-trip is not an achieved positive outcome, exactly the same logic.
  **Fixed: this card's status now uses `color.brand.primary-subtle` (`#E6F2EB` bg) with
  `color.brand.primary` (`#006837`) text — not `color.status.success`.** This is a third, distinct
  shade in the green family (muted brand-informational vs. saturated status-success vs. solid
  button-fill), matching the desktop system's own existing precedent instead of a new invented
  rule. "Needs Your Response" keeps `warning`/`warning-subtle` (a genuine pending-decision state,
  correctly a warning). "Scheduled" keeps `color.status.neutral`/`color.neutral.bg`. **The label
  text itself was "In Progress" at the time this note was written — relabeled to "Ready" on
  2026-09-22, see the state-naming correction below; the color reasoning above is unaffected by
  the rename.**
- **Status label max-width (superseded 2026-09-22 — no longer a chip-width concern since the
  container was dropped, but the underlying constraint still holds):** the status label is plain
  text now, not a box, so there's no chip to stretch — but it still must not wrap to a second line
  or run long enough to crowd the time/chevron on its right. Keep status words short (one or two
  words: "Ready," "Needs Your Response," "Scheduled") so this never comes up in practice.
- **State name corrected: "In Progress" → "Ready" (2026-09-22) — the label didn't match what the
  card actually represents.** Traced from a direct question about the accept→inspection sequence:
  this card shows an assignment that's confirmed (Accept already happened) and scheduled for
  *today*, but the driver hasn't tapped "Start Pre-Trip Inspection" yet — nothing is actually "in
  progress." The ordering rationale in `04_FIGMA_SCREEN_BLUEPRINT.md` had described this same card
  as "mid-inspection, mid-drive — finish what's already started," which flatly contradicts a button
  that says "Start" rather than "Continue." **"Ready" is the accurate label: confirmed, today,
  not yet started.** A genuinely mid-trip state (post-tap, mid-checklist or mid-drive) is a
  *different* state this component doesn't currently render an example of — it lives on FRAME 7C's
  "Active Trip" screen (`04_FIGMA_SCREEN_BLUEPRINT.md` §8), not as a Home-list card action. Whether
  Home needs its own true "In Progress" card (e.g., so a driver who backgrounds the app mid-trip
  sees a way back in in, with a "Continue Trip" button instead of "Start Pre-Trip Inspection") is
  flagged but not yet built or decided — see the open item in `08_PROJECT_HANDOVER.md` §13.
  **The full state chain, current and accurate:** Needs Your Response → (Accept) → Scheduled →
  (trip date arrives) → Ready → (Start Pre-Trip Inspection tapped) → hands off to FRAME 7B/7C,
  which is a separate screen, not a Home card state.
- **Route dots — reversed back to color (2026-09-22), after a render check questioned whether
  shape-only was actually the better call.** The 2026-09-21 "shape-only, color exception removed"
  decision below is superseded. Re-checked against real apps directly: Tesla Robotaxi and
  [BlaBlaCar](https://mobbin.com/screens/dc129e88-cb44-4ece-828a-a7a0ee5b5713) do use shape-only
  (hollow→filled, one neutral color) — that's what justified the original rule. But
  [inDrive](https://mobbin.com/screens/1489a9fd-f96a-4bdb-80b1-2f4ce62bc09e) — an app already
  flagged earlier in this project as a liked reference for this exact screen — uses colored
  (blue origin / green destination) dots for precisely this pattern, and
  [Grab Driver](https://mobbin.com/screens/ca866942-38fe-469f-94d9-f0541d458c02) color-codes
  pickup vs. drop-off too. It's a genuine split in real practice, not a case where color is
  clearly wrong. The original shape-only rule was motivated by tightening the closed color list
  (an internal hygiene goal), not by a usability problem color was causing — a weaker basis than
  the defect-driven fixes elsewhere in this component (SOS ambiguity, oversized buttons). **Locked:
  origin dot `#3B82F6` (blue, one new closed-list exception, reinstating the value the 2026-09-21
  pass had retired), destination dot `color.brand.primary` `#006837`** (reuses the existing Civic
  Green token rather than inventing a new green — also gives "arrival" a nice semantic tie to the
  brand color). Both dots stay filled/solid circles — shape no longer needs to carry the
  differentiation now that color does, so the hollow-vs-filled distinction is dropped along with it.
- Everything else: `color.neutral.ink`, `color.neutral.slate`, or `color.neutral.border` only.
  No other color appears on this card under any circumstance, except the two dot colors above and
  the notification unread-badge (`color.status.critical`, noted below) — **three total exceptions
  to the closed list now, not zero.** Earlier versions of this line claimed "no exceptions left" at
  different points in this doc's history; that was never true for long. Don't trust a "no
  exceptions" claim anywhere else in this document as a standing fact — this line, current as of
  2026-09-22, is the actual count.
- **Exact colors closed for every element, every card state (2026-09-21) — this was ambiguous
  before and needed to not be.** User asked for explicit clarity on weight and color; auditing the
  spec found real gaps: chip text colors were referenced by token name without exact hex, the
  "Scheduled" card's muted text had no pinned value (just "lighter shade" — exactly the kind of
  ambiguity a Figma agent renders inconsistently), icon colors were never stated, and an earlier
  version of this rule overclaimed "AAA contrast" for the muted state without checking that
  against what this system's own existing muted-text token actually provides. Closed below:

  | Card state | Status label text color (no bg/container, see 2026-09-22 removal above) | Body text | Icons | Origin dot | Destination dot |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  | Ready (renamed 2026-09-22, was "In Progress") | `#006837` (`color.brand.primary`) | `color.neutral.slate` `#334155` | `#334155` (matches body) | `#3B82F6` (blue, fixed) | `#006837` (`color.brand.primary`) |
  | Needs Your Response | `color.status.warning` `#B45309` | `#334155` | `#334155` | `#3B82F6` | `#006837` |
  | Scheduled | `color.status.neutral` `#475569` (stays AAA, 8.3:1 — this token is designed for exactly this "inactive" semantic) | `color.neutral.slate-muted` `#64748B` (this is this system's own existing tertiary-text token — **AA 4.8:1, not AAA**; the earlier version of this rule wrongly demanded AAA for muted body text when no AAA-rated muted token exists in this system. AA is correct here and matches how `slate-muted` is used everywhere else in this doc, e.g. Component 2's KPI label) | `#64748B` (matches muted body text) | `#E2E8F0` (deliberately muted, not the fixed blue — see note below) | `#64748B` (deliberately muted, not the fixed green — see note below) |

  **Scheduled card's dots stay muted gray, not the fixed blue/green (2026-09-22).** The vivid
  blue/green dot colors are a signal of an active/urgent card; the Scheduled card is deliberately
  the lowest-priority, quietest card on the screen (per the "manage emphasis by quieting the
  low-priority card" scannability rule), so its dots follow the rest of its own muted palette
  instead of picking up the new color exception. This isn't a fourth color exception — it's the
  existing neutral-muted tokens already used for everything else on that specific card.

  Destination headline text on the Scheduled card also uses `#64748B`, not `color.neutral.ink` —
  the whole card follows this one muted color, no element on it uses full-contrast ink or slate.

**Buttons resized (2026-09-22) — "generic and too big" traced to a real cause, not vague
oversizing.** Checked against [American Airlines' Review screen](https://mobbin.com/screens/aa82ca60-7521-40e7-aa4f-bec11593e779):
its "Undo"/"Change" buttons are compact, pill-shaped, and content-hugging — sitting naturally in
a trip-card row, nowhere near full card width. Compared against [UNIQLO's "Delete Account"
confirmation](https://mobbin.com/screens/03b38108-d7da-4426-8795-7613d863e0e8), which correctly
uses big, unmissable, full-width buttons — but that's a rare, high-stakes, once-ever action. Our
buttons had been sized like UNIQLO's (rare-confirmation treatment) for what is actually American
Airlines' context: a routine, frequent, in-list micro-decision. **Fixed the actual problem — width
and shape, not height.** Height stays at the accessibility minimum (44px, not reduced further —
this project's own research already established 44×44px as a hard touch-target minimum, not a
style choice to shrink past).

**Locked button spec — the only two button states this component uses:**
- **Primary, solo** (Start Pre-Trip Inspection — the only action on its card, nothing paired
  against it): filled `#006837`, white text, 44px height, `radius.md` (8px), full width. A lone
  action isn't competing with a peer for visual space, so it can stay prominent — this case is
  unaffected by the resize below.
- **Primary, paired** (Accept, when shown beside Decline): filled `#006837`, white text, 44px
  height, fully rounded/pill shape (`border-radius` = half the height), content-hugging width
  (auto-sized to text + 20px horizontal padding) — NOT stretched to a fixed % of card width.
- **Secondary** (Decline): white fill, `1px solid color.neutral.border`, `color.neutral.slate`
  text, 44px height, same pill shape and content-hugging width as paired Primary.
- Paired buttons sit side by side, compact, natural content width — never stretched to fill most
  of the card the way a rare-confirmation dialog button would.
- **Tappable zone vs. visible pill height, clarified 2026-09-22 — these are not the same
  measurement, and this spec had been conflating them.** "44px height" governs the *tappable
  area*, not necessarily the *rendered box* — both Apple HIG and Material Design allow a visually
  smaller pill with invisible padding making up the difference to the real touch-target minimum.
  Checked against a real comparison the user raised (Perplexity's compact "Search"/"Computer"
  action pills, visibly smaller than a 44px box) — that app is very likely using exactly this
  technique, not violating the touch-target rule. **For paired buttons specifically** (Accept/
  Decline, where two buttons sit close together and visual weight is more noticeable than on a
  lone full-width button): the **tappable zone stays 44px, unchanged** — this driver-facing context
  (outdoor, glare, gloves) is more demanding than average, not less, so the accessibility floor
  doesn't move. The **visible pill can render smaller** (36px), with ~4px of invisible padding
  above/below making up the rest of the real 44px tappable area. Solo, full-width buttons (Start
  Pre-Trip Inspection) are unaffected — nothing there needs to look visually lighter the way two
  adjacent pills do.
- No third button style exists. No button on this card is ever anything other than one of these.
- **Accept/Decline grounding, added 2026-09-22 — checked against the actual SRS flow after a
  direct challenge, not assumed.** These buttons were originally built by pattern-matching against
  ride-hailing references (Uber/Grab/inDrive) without checking them against this project's own
  dispatch model — where SRS §5.4/§5.6 puts the assignment decision with Daniel (Transport
  Officer) at the Dispatch Gate, not with the driver. On review, real need survives: a driver must
  be able to confirm they've seen a dispatched assignment, and flag genuine inability to fulfill it
  (illness, a known prior conflict) before execution — not shop between assignments the way a
  ride-hailing driver does. **So Accept means "confirm/acknowledge," not "I choose this job"; and
  Decline is gated by a mandatory reason field and routes back to Daniel's Dispatch Queue for
  reassignment** (matching the system's existing justification pattern — BR-009's override
  justification, §5.24's rejection/return-for-correction — never a driver-to-driver handoff, which
  would bypass Daniel's dispatch authority). Full flow grounding: `02_USER_FLOWS.md` §3's "Driver
  Confirmation" note. This doesn't change the button spec below, only its meaning — Accept still
  needs to read as the clear expected action, Decline as the deliberate exception path.
- **"One main green CTA" is scoped per-card (per decision), not per-screen — a deliberate call,
  worth recording since this button's hierarchy has come up repeatedly (2026-09-22).** User
  correctly raised whether multiple filled-green buttons visible at once (Card 1's "Start Pre-Trip
  Inspection" and Card 2's "Accept") violates a one-primary-CTA discipline. Resolved: each card is
  an *independent decision*, not a competing option for the same choice — the list's urgency
  ordering (Ready → Needs Your Response → Scheduled) already signals which decision matters
  most right now, without needing to mute color on the others. Within a single card, Accept still
  needs full green specifically to signal "the expected path" against Decline — toning it down
  would undo the button-hierarchy fix already made.
- **Guardrail refined (2026-09-22), based on a genuinely better counter-proposal.** Initially
  proposed capping/hiding pending cards if the list grows past a few simultaneous "Needs Your
  Response" items. Correctly pushed back on: silently hiding a pending assignment risks a driver
  missing one they actually needed to see — a real discoverability cost, not just a visual one.
  **Adopted instead: max 2 visible filled-green CTAs in the viewport at once** (the current 3-card
  layout already satisfies this — Card 1's button + Card 2's Accept, Card 3 has none). If pending
  cards ever exceed that, show the single highest-priority one in full (with its real buttons),
  and add a plain "View N more pending →" row instead of stacking additional green-button cards —
  nothing is hidden, everything is still reachable, the count itself signals there's more to see.
- **The action zone must contain real button(s), never a text link like "Tap to respond."** A
  rendered build replaced Card 2's Accept/Decline buttons with a "Tap to respond" link, which
  buries the single most important interaction on this entire screen behind an extra tap and
  directly undoes the reason Home was rebuilt as a list in the first place (per-card actions
  visible without navigating away). This is a hard rule, not a style preference: every card that
  has an action must show it as a real button on the card face, full stop.
- **Superseded (2026-09-21): the person/vehicle detail-block icons are back in.** This previously
  said to remove them; user confirmed they're fine after seeing them rendered. Person/car icons
  stay on the Requester/Vehicle lines, colored to match their row's body text exactly (see the
  per-state color table above: `#334155` on active cards, `#64748B` on the Scheduled card) — not a
  separate unspecified "muted-gray," per the closed icon-color rule.
- **Chevron and header/tab-bar colors, closed (2026-09-21) — the last unspecified colors in this
  screen.** Chevron (›): `color.neutral.slate-muted` (`#64748B`) on active cards, matching the
  Scheduled card's muted color there too (it's a low-emphasis affordance, never a status carrier,
  so it doesn't need to shift per card state the way body text does). **Header avatar, revised
  2026-09-22: a real/representative photo is fine, not restricted to a neutral placeholder.** The
  earlier "placeholder until a real photo exists" rule was more conservative than needed — a
  rendered build used a real-looking photo and the user confirmed keeping it, treating it as the
  intended design rather than a stand-in. **Notification icon** (see below — replaces SOS entirely):
  `color.neutral.bg`-tinted circle background with a `color.neutral.ink` icon. **Settings icon,
  added 2026-09-22**: a gear icon beside the notification bell, same neutral tinted-circle
  treatment — confirmed as a deliberate addition, a quick-access shortcut alongside the
  notification icon even though Profile (bottom tab) also reaches account/settings content; not
  redundant navigation to remove. Bottom tab
  bar icons: inactive tabs use `color.neutral.slate-muted` on the dark navy bar (enough contrast to
  read against `#0F172A`), active tab uses white icon on the `#173829` active-chip background
  (reusing the exact dark-sidebar active-chip token from desktop Component 1, not a new mobile-only
  color). All icons across the header, chevrons, and tab bar follow the same one-set/one-stroke-
  weight rule as everything else on this screen — no exceptions carved out for chrome elements.
- **Route dot history, both reversals in one place (superseded 2026-09-21, then reversed again
  2026-09-22 — see the locked rule above, this note is now purely historical).** Original rule: a
  solid blue origin dot, color as the main differentiator. 2026-09-21: switched to shape-only
  (hollow origin, filled destination, one neutral color) when the vertical dot-connector-dot
  timeline was introduced, reasoning that shape alone could do the job. 2026-09-22: reversed back
  to color (origin `#3B82F6`, destination `color.brand.primary` `#006837`, both filled) after a
  render check found real precedent — inDrive, a liked reference for this screen — uses color for
  exactly this pattern, and the shape-only rule had been a hygiene preference, not a defect fix.
  **The locked rule above is current; do not re-derive from either superseded step in this note.**
- **Header greeting/name weight split, locked (2026-09-21)**, checked against [IKEA's
  header](https://mobbin.com/screens/236972df-1152-4b5a-9bd2-2ed6aa872220), which splits a small
  greeting phrase from a large bold name rather than treating "Good morning, Joseph" as one
  uniform line. Locked: "Good morning," at `type.body` weight/size (secondary), "Joseph" at
  `type.card-title-mobile` weight/size (16px/700, the same headline weight used for destination
  text) — the personalization moment is about the name, not the phrase, so the name gets the
  bolder treatment.
- **Collapsing header on scroll (added 2026-09-22)** — the same native iOS/Android "Large Title"
  pattern IKEA's header also uses. Two states, values closed, no new content added to either:
  - **Expanded (scroll position at top):** avatar visible, "Good morning," at `type.body` (14px),
    "Joseph" at 20px/700 (Lexend) — larger than the standard 16px header-name size specifically for
    this expanded state — "County Driver • On Duty" subtitle visible beneath at `type.caption`
    (12px, muted white). Generous vertical padding: 20px top/bottom.
  - **Collapsed (scrolled past the top of the list):** avatar hidden, greeting phrase ("Good
    morning,") dropped, subtitle dropped — only "Joseph" remains, at 16px/700 (the standard
    header-name size, matching the weight-split rule above), vertically centered in a compact
    12px-padding bar. The notification icon (top-right) stays visible and unchanged in both states.
  - **What does not change between states:** background color (`#0F172A` throughout), notification
    icon position/size, and — critically — no new content is added to justify the expanded state's
    extra height. The expansion is purely more breathing room and larger type on content that's
    already there, not a place to add a stats count, search bar, or other filler. This project has
    spent this whole revision cycle removing exactly that kind of unjustified addition; a bigger
    header must not quietly reopen it.
- **"Assignments" list title sized down (2026-09-22)** — checked real apps' section/list titles:
  mixed convention found, compact centered nav-bar titles (Satispay, KOHO) versus larger
  left-aligned page headings (Zip, Uber Eats, Notion) — reasoned from this general pattern
  rather than one specific cited screen, since the deciding factor
  here isn't which convention to copy, it's that CVFMS's own header already carries a large bold
  name ("Joseph," 20px/700 expanded). A second large bold heading ("Assignments") stacked directly
  beneath it recreates the exact "two dominant elements competing" problem already fixed *inside*
  individual cards (destination vs. time), just one level up at the page. **Fixed: "Assignments"
  now renders at `type.section-title` (18px/600, Lexend)** — one clear step down from the header
  name, reading as a plain list-section label under an already-established identity heading, not a
  second hero. `color.neutral.ink`. **Locked position:** left-aligned, in the normal scrolling
  content flow (not part of the collapsing header, so it does not collapse/hide with it), 12px
  below the header and 12px above the first card — reusing the component's own existing 12px gap
  value, no new spacing value introduced for this.
- **County branding, added 2026-09-22 — a deliberate exception to this doc's own minimalism
  discipline, and worth stating as such.** Since CVFMS may deploy per-county, the user asked for a
  county landmark background image *and* a county emblem, explicitly pushing back on stripping
  everything down for its own sake ("functionality doesn't mean it needs to be boring"). This is a
  real, acknowledged philosophy exception: nowhere else in this app carries a photographic or
  decorative element, and that's intentional here too — the header is allowed to feel like it
  belongs to a specific place, everything below it stays exactly as restrained as already specced.
  - **Applies to the expanded header state only.** The collapsed state stays solid `#0F172A` with
    no image — this also sidesteps the accessibility risk of photo-behind-text at the compact,
    lower-padding size where there's no room for a strong overlay to work with.
  - **Background image**: full-bleed county landmark photo behind the expanded header, with a
    dark overlay/scrim — `#0F172A` at 75-85% opacity, or a matching gradient (transparent at the
    very top fading to near-solid navy by the text baseline) — applied on top of every photo before
    text renders. This is not optional per-photo; contrast must be verified against WCAG AA/AAA
    for white text regardless of which county's image is loaded, since landmark photos vary widely
    in local brightness and a fixed overlay strength must guarantee legibility for all of them, not
    just the one used for design/preview purposes.
  - **County emblem/coat-of-arms**: a small icon, placed beside the greeting text (not competing
    with the driver's own avatar, which stays as the primary identity anchor) — e.g. a small crest
    icon before "Good morning," or beside "County Driver • On Duty." Exact placement is a render
    decision, not locked to a single position yet — check it doesn't crowd the existing avatar/
    greeting/notification layout once built, and adjust if it does. **Still missing as of the first
    render (2026-09-22)** — the landscape background photo covers "landmark," but the separate
    small emblem/crest hasn't appeared in any build yet; needs its own follow-up prompt.
  - **"On Duty" status dot, confirmed 2026-09-22**: a small green dot before the "County Driver •
    On Duty" subtitle, matching the online/active-status-dot convention (Slack, Discord, etc.) —
    appeared in a rendered build unprompted, kept as a reasonable, low-risk addition since it's a
    real status (on duty vs. off duty), icon-adjacent rather than color-alone, and doesn't compete
    with anything else in the header.
  - **Asset pipeline, flagged as a real operational dependency, not just a design toggle**: each
    county needs a sourced, rights-cleared, consistently-cropped landmark photo and emblem before
    this can ship for that county. A sensible default/fallback (e.g., a plain Civic Green gradient,
    no photo) must exist for any county without a configured image yet — this should never render
    as a broken image or empty space.
- **Superseded (2026-09-22): SOS removed entirely, replaced with a notification icon.** Everything
  above referencing "SOS" is historical — read it for the reasoning trail on icon/placement fixes,
  but the element itself no longer exists. SOS was always a weaker fit than it looked: the SRS
  never names it, and it was carried into this design as an unstated assumption that needed
  after-the-fact justification (SRS §11's offline-first/rural-connectivity rationale) rather than a
  real requirement. **A notification icon (bell) is a better-grounded replacement** — SRS §5.23
  ("Notification and Alert Management") is an explicit, named requirement, already referenced
  elsewhere in this project (the Approving Officer persona flagged it as needed but never built).
  Same position (top-right, both header states), same neutral icon treatment (`color.neutral.bg`-
  tinted circle, `color.neutral.ink` icon glyph) — just the correct element this time, not one that
  needed retroactive justification. **Badge, if unread notifications exist:** a small filled dot,
  `color.status.critical` (`#B91C1C`) — the one closed-list color exception this adds, used only
  for this badge, never elsewhere on the card. No badge renders when there's nothing unread. What
  tapping it opens (a notification list/panel) is a reasonable, conventional assumption for this
  pattern and doesn't need further open-question flagging the way SOS's tap-behavior did.
  - Transition: standard scroll-linked collapse (matches native platform behavior, not a novel
    animation this system needs to invent or specify further).
- **Button text must always name the exact next action, never a generic verb.** A rendered build
  drifted from "Start Pre-Trip Inspection →" to "Continue assignment" — reverted. This restates a
  rule already established earlier in FRAME-07's design (borrowed from Grab's "Arrived"/"Pick
  Up"/"Drop Off" pattern) that apparently needs restating here directly on the locked component,
  since it drifted once already: every button on this card names the specific thing tapping it
  does, never a vague catch-all like "Continue" or "Proceed."

**What this replaces (corrected 2026-09-22 — this note had gone stale twice and needs to stop
drifting from the current spec):** the card previously carried a left-edge accent bar (reversed
above) and a separately-styled outline chip for passenger count (now folded into the detail block
as plain text, not a chip). At the time this was first written, the status indicator itself was
still a chip — that's no longer true either: the status chip container was dropped entirely
(2026-09-22, see above), so passenger count and status now follow the same plain-text-no-container
treatment for the same reason, not two separate decisions that happen to agree.
**The person/car icons were dropped at one point in this component's history, then confirmed back
in** (see the superseded note above) — do not trust any earlier statement in this document that
says they're removed; the color table and icon-color rule above are the current, correct source of
truth.

### Component 10 — Mobile Pre-Trip Inspection Row (added 2026-09-22, FRAME 7B)

**Fifth checklist row added, 2026-09-24 — Fuel Level, moved here from Component 17.** Direct
question raised: why does Start Journey show a Fuel Level pill, and where does the reading come
from? Checked against the SRS directly rather than assumed. Two findings: (1) §5.6 (Dispatch
Management) names fuel level explicitly, in the same sentence as this checklist's existing four
items — *"Before dispatch verify vehicle availability, driver assignment, licence, insurance,
inspection, service status, **fuel level**, odometer, tyres, lights, brakes and safety
equipment. Prevent dispatch where mandatory conditions are not met, subject to authorized
override."* Fuel level is a named mandatory gate condition, the same category as tyres/lights/
brakes — it belongs in this checklist's Pass/Fail-with-override treatment, not as a passive,
consequence-free display elsewhere. (2) §5.16 (GPS and Telematics) lists exactly what the vehicle-
integration layer provides — location, trip history, distance, speed, geofencing, route deviation,
idling, engine status, mileage — and **fuel is absent from that list**, even though "engine status"
and "mileage" are included. No sensor/telematics source is in scope anywhere in this SRS; the
reading is self-reported, the driver looks at the vehicle's own fuel gauge, same as the other four
rows are the driver's own physical inspection. **Resolved: Fuel Level becomes this checklist's 5th
row, with the same Pass/Fail-plus-override treatment as the other four — removed from Component 17
State 1, where it previously had no blocking consequence** (see Component 17 State 1's own note for
that removal).

**Why a real two-state toggle, not a single checkbox.** The rough draft this replaces described
"4 large binary tap-targets (Pass/Fail toggle)" without specifying the actual control. A single
checkbox (checked = done) is the wrong control here: it conflates "not yet inspected" with
"passed," which is a real compliance risk — BR-004 (grounded vehicles) and the Dispatch Gate depend
on Fail being a deliberate, recorded finding, not an absence of a checkmark. Checked against Tesla's
Maintenance checklist (clean row typography/spacing precedent, though dark theme) and the already-
cited Turo "Physical damage" checklist and Lime damage-report pattern (`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`,
FRAME-07 section) for the per-item photo-evidence placement. None of these is a binary pass/fail
control exactly, so the toggle itself is this project's own construction, built from the same
locked primitives as Component 9 rather than inventing new ones.

**Structure — revised 2026-09-22 to a stacked two-line row, replacing the original single-line
layout.** The original spec put icon + label + Pass/Fail toggle all on one row. Real problem found
before any further rendering: two of the four labels ("Headlights, Brake Lights & Indicators,"
"Fire Extinguisher & First Aid Kit") are long enough to wrap to 2 lines in a 390px viewport, and a
wrapped label crowds directly into the Pass/Fail buttons next to it — a layout that only works for
short labels, which isn't all four of them. **Fixed: label and toggle move to their own separate
lines within the row, not sharing horizontal space at all**, so wrapping the label can never crowd
the buttons regardless of text length. **Locked as an explicit rule, not just an emergent side
effect of the layout:** text wraps, buttons never do. The label is the only element in this
component allowed to wrap to a second line; the Pass/Fail toggle and every button/chip elsewhere in
this component stay single-line, fixed-height, content-hugging — if a button's label were ever long
enough to risk wrapping, the fix is shorter button text, not a taller/wrapped button.
1. **Line 1 — icon + label:** leading category icon (tire, lights, fluid-drop, kit, fuel-pump —
   one per row, static, never tappable), 20px, `color.neutral.slate-muted` `#64748B`, same icon
   set/stroke-weight as the rest of the app. Item label ("Tyres & Spare Wheel"), 14px/600,
   `color.neutral.ink` — same weight/size as Component 9's detail-block body text, reused not
   reinvented. **Label wraps freely to 2 lines with no length constraint or truncation** — there's
   nothing to its right on this line to crowd. **Fuel Level's row only, added 2026-09-24: a trailing
   segmented pill** ("75% (3/4 Tank)", reusing the exact pill treatment this same reading had on
   Component 17 State 1 before it moved here) **sits at the end of Line 1**, right-aligned — purely
   informational context to help the driver judge Pass/Fail, not itself an input. "Fuel Level" is
   short enough that this never risks the wrapping-into-crowding problem the stacked-line fix above
   exists to prevent; no other row gets this treatment.
2. **Line 2 — Pass/Fail segmented toggle**, 8px below line 1, left-aligned starting from the same
   indent as the label (not right-aligned/trailing anymore — this was only meaningful when sharing
   a row with the label): two pill buttons side by side, "Pass" / "Fail", **neither selected by
   default** — an unmarked row must look visibly different from a marked one, satisfying the
   compliance concern this toggle exists for in the first place.
   - Unselected state (either button, before tap): white fill, `1px solid color.neutral.border`,
     `color.neutral.slate` text.
   - Pass, selected: filled `color.brand.primary` `#006837`, white text.
   - Fail, selected: filled `color.status.critical` `#B91C1C`, white text — deliberately the
     system's critical-red token, not a muted warning color, since a failed pre-trip check is a
     real blocking finding, not a soft caution.
   - **Tappable zone unchanged at 44px — but visible pill height can be smaller, 2026-09-22
     correction.** Same distinction just locked in Component 9 (see its "tappable zone vs. visible
     pill height" note, prompted by a direct comparison against Perplexity's compact action pills):
     the 44px figure governs the *tappable area*, not the *rendered box*. **Visible pill: 36px,
     with invisible padding making up the rest of the real 44px tappable zone** — same technique,
     reused rather than re-derived. This is a genuine visual fix, not a touch-target regression:
     the crowding problem was the stacked-vs-single-line layout (fixed above), and this makes the
     buttons look lighter on top of that, not instead of it. Pill-shaped, content-hugging width,
     same geometry as Component 9's paired Accept/Decline.

**Fail detail moves to a bottom sheet, not inline expansion (corrected 2026-09-22, reversed before
any render).** Originally speced as chips/camera/description expanding directly beneath the row.
Real problem: with several rows potentially marked Fail at once, each expanding inline compounds
into a tall, reflowing list — exactly the instability this stacked-row fix (above) was just
written to avoid. **Fixed: tapping "Fail" opens a modal bottom sheet** (native M3 pattern for
exactly this — focused, secondary data entry without leaving the current screen).

**Sheet content revised 2026-09-22 — re-examined the cited references more carefully rather than
building a generic chips+photo+button sheet.** Two concrete improvements pulled from the actual
reference screens, not invented from scratch:
- **Sheet header, revised 2026-09-22 to match what actually rendered.** Originally speced as a
  question borrowed from Flighty's "Report Data Issue" sheet — "What's wrong with the [Item
  Name]?" A render used a shorter, cleaner phrasing instead: **"Report [item] issue"** (e.g.
  "Report tyre issue," "Report headlight issue"). Confirmed as the standard going forward — reads
  more naturally and stays consistent across all 4 sheets. `type.card-title-mobile` (16px/700).
  Still gives the sheet immediate context instead of opening as an unlabeled form, just more
  concisely than the original question format.
- **Content order, matching [Lime's "Report Issue" sheet](https://mobbin.com/screens/a79e71e9-c9ce-4c2d-95f5-d33ce4bd5378)
  (location first, then reason, then photo):** since every checklist row bundles more than one
  physical item under one label, the sheet asks *which* item first, *what's wrong* with it second,
  then supports both with a photo — not photo-icon-first as originally drafted.
  1. **"Affected item(s)" chips (added 2026-09-22, label finalized as rendered — was drafted as
     "Which one?") — closes a real gap found by re-examining Lime's reference**, which pairs reason
     selection with a labeled diagram specifically to locate the issue, not just categorize it.
     This project already rejected a full diagram as overkill for a 4-item checklist
     (`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`), but the underlying need — locating, not just
     categorizing — is real: a chip like "Missing" on "Fire Extinguisher & First Aid Kit" doesn't
     say which of the two is missing. Fixed with chips, not a diagram. Multi-select, same visual
     treatment as the reason chips below. Per-row sets: **Tyres & Spare Wheel** — Front-Left /
     Front-Right / Rear-Left / Rear-Right / Spare Wheel. **Headlights, Brake Lights & Indicators**
     — Headlights / Brake Lights / Indicators. **Engine Oil & Coolant Levels** — Engine Oil /
     Coolant. **Fire Extinguisher & First Aid Kit** — Fire Extinguisher / First Aid Kit. At least
     one chip mandatory. **Fuel Level skips this step, added 2026-09-24** — it's a single reading,
     not a bundle of physical items the way the other four rows are, so there's nothing to locate;
     its sheet goes straight to "What's wrong?" below.
  2. **"What's wrong?" reason chips** (multi-select, scoped per item — reuses the pattern already
     cited for this screen, [Turo's "Physical damage" checklist](https://mobbin.com/screens/c9fbb23e-0b26-4958-924a-ef9c171ae8a6)):
     unselected = white fill, `1px solid color.neutral.border`, `color.neutral.slate` text;
     selected = filled `color.status.critical`, white text; content-hugging, 32px height. At least
     one chip mandatory. Per-row sets unchanged: **Tyres & Spare Wheel** — Worn Tread / Flat or
     Damaged / Missing Spare / Low Pressure. **Headlights, Brake Lights & Indicators** — Not
     Working / Cracked Lens / Dim or Flickering. **Engine Oil & Coolant Levels** — Low Level /
     Leaking / Discoloured. **Fire Extinguisher & First Aid Kit** — Missing / Expired / Damaged.
     **Fuel Level, added 2026-09-24** — Below 1/4 Tank / Empty or Near-Empty / Fuel Gauge
     Malfunction / Other.
  3. **Photo capture** — camera icon + "Add Photo" tap target, mandatory, directly below the chips.
  4. **Optional elaboration** — a plain text link, "+ Add more detail," expands an optional
     multi-line text area only if tapped — never required, never blocks the sheet's save action.
  5. **Save** (filled `color.brand.primary` — this confirms data entry, not the blocking decision
     itself, so it stays the neutral brand-action color, not red). Disabled until at least one
     "which one" chip, at least one reason chip, and a photo are all present.
- **On save, the sheet closes and the row collapses to a compact one-line summary** in place of
  the full Fail detail — e.g. "Front-Left, Worn Tread · Photo attached" in `color.status.critical`,
  12px, with a small "Edit" affordance to reopen the sheet. **This is what keeps the main list
  stable**: no matter how many rows are marked Fail, the list's height only grows by one compact
  line per Fail, never a full expanded form per Fail.

**Row spacing:** 16px vertical padding per row, `1px solid color.neutral.border` hairline divider
between rows. **This is a deliberate exception to Component 9's no-internal-dividers rule** — that
rule was about dissolving unnecessary containers *inside a single card*; this is a conventional
divided list (matching Tesla's and Turo's own reference patterns above), not a card with
sub-groups pretending to be separate things. Different component, different structural problem,
not a contradiction.

**App bar — revised 2026-09-22 to an explicit Material 3 small top app bar, replacing a plain
title-only header.** Real gap found: the original header was just a title + trailing pill, with no
way back to Home at all — a real usability miss for a sub-screen, not a deliberate "trap the
driver" decision. **Note on sourcing:** m3.material.io's specs page is JS-rendered and didn't
return usable content on a direct fetch attempt (the same failure mode this project hit earlier
with Uber Base/Shopify Polaris) — the structure below uses stable, well-established M3 small-top-
app-bar conventions (leading nav icon, left-aligned title, trailing actions), not a freshly-pulled
exact spec; treat exact dp values as reasonable defaults, not verified-today numbers.
- **Leading:** back arrow, 24px icon in a 44px touch target (this project's own touch-target
  minimum, not the M3 default 48dp — consistency with the rest of this component wins over an
  unverified external default), `color.neutral.ink`. Returns to Home — **does this discard
  in-progress checklist state, or preserve it?** Not yet decided; flagged as an open question below,
  not assumed.
- **Title:** "Pre-Trip Inspection," left-aligned immediately after the back arrow (M3's small-top-
  app-bar convention — left-aligned, not centered; centered titles are an iOS/M2 convention this
  project isn't using here), `type.card-title-mobile` (16px/700) — reused from Component 9, not a
  new size introduced for M3 compliance's sake.
- **Content row, split from the app bar itself (revised 2026-09-22 — a render put vehicle plate +
  progress pill on their own row below the app bar rather than folding them into one combined title
  string as originally speced; kept, since it reads cleanly and separates navigation chrome from
  status content).** Below the app bar: vehicle reg plate ("KBZ 442A"), `color.neutral.slate`,
  14px/400, left-aligned — and trailing, same row: progress pill, **"X/5 Checked" (was X/4 before
  the Fuel Level row was added, 2026-09-24)** — plain pill,
  `color.neutral.bg` fill, `color.neutral.slate` text, 12px/600, fully rounded. **Must say
  "Checked," not "Passed,"** since a completed checklist may include Fail rows — "4/4 Passed" would
  misreport a checklist that's fully filled in but contains a real defect.
- **Container:** app bar 56px height — reuses this project's own existing desktop top-bar height
  token (`--header-height`, Component 1) rather than importing a separate, unverified M3 dp value
  for a bar that otherwise follows CVFMS's own type/color tokens throughout. Content row beneath it:
  standard row padding, no fixed height locked (content-driven).

**Still open:** whether the back arrow discards or preserves in-progress checklist state (marked
rows, captured photos) if tapped mid-inspection. Needs a decision before this is fully closed —
not assumed here.

**Evidence for Pass items — GPS + timestamp, not per-item photos (2026-09-22, checked against real
DVIR industry practice, not assumed).** Direct question raised: since Fail items get a mandatory
photo, what evidence backs up a Pass? Requiring a photo on every one of the 5 items (not just
failures) would fight this screen's own "60-second" speed goal, and a photo of a routine, fine
item proves little on its own. The actual industry-standard mechanism for this exact problem is
different: **the app automatically records GPS location and timestamp when the inspection starts
and when it's submitted**, verifying the driver was physically present at the vehicle for the
whole check — this is the real anti-"pencil-whipping" (industry term for filling out a check
without doing it) control, not per-item photos. No photo requirement is added for Pass items; the
GPS/timestamp binding is the evidence for the checklist as a whole, and the mandatory photo+reason
on Fail (above) is the evidence for the specific exception.

**"Location & time verified" caption removed from the visible UI (corrected 2026-09-22).** A
render check found the bottom of the screen crowded — completion banner, this caption, and 1-2
buttons all stacked tightly, and the caption's small gray text broke up the visual rhythm between
the banner and the button without adding anything the driver needs. On reflection, this caption was
never actually for the driver — it's the system reassuring itself that GPS/timestamp capture
happened, not information a driver needs to see or act on. **The capture itself is unchanged and
still happens automatically** — it just no longer needs a visible line of text to prove it's
happening. This is the same minimalism discipline already applied elsewhere in this component
(chip container removal, SOS removal): cut UI that exists to reassure the system, not the user.

**Fail blocks departure — grounded directly in SRS §5.6, not a UI judgment call (corrected
2026-09-22, citation extended 2026-09-24 to cover the 5th row).** §5.6 (Dispatch Management) names
this checklist in full: "verify... service status, **fuel level**, odometer, **tyres, lights,
brakes and safety equipment**. **Prevent dispatch where mandatory conditions are not met, subject
to authorized override.**" That's all five of this checklist's items (fuel level included, added
2026-09-24) in one sentence, and the identical block-plus-override pattern already used for the
Dispatch Gate's BR-001–005 — this isn't a separate policy question, it's the same rule applied at
the point the driver actually finds the defect rather than only earlier at Daniel's desk.

**Completion banner (conditional on all 5 rows being marked, not just visited — was 4 before Fuel
Level was added, 2026-09-24) — un-boxed 2026-09-22,
corrected from a filled/bordered box.** A render check found the boxed banner sitting directly
above the primary button — same rounded-rectangle shape, similar width, similar visual weight —
reads as a second (or third, with the offline-fallback button) button rather than a status
message, exactly the "messages and buttons are conflicting" problem flagged directly. **Fixed:
plain icon + text, no background fill, no border** — only the actual buttons below keep a filled/
bordered box treatment, so there's no ambiguity left about what's tappable. Same fix already
applied to FRAME 7A's status label for the identical reason (a box wasn't earning its visual
weight there either).
- All 5 Pass: a small check-circle icon + "No defects logged. You are cleared for departure." —
  `color.brand.primary` icon and text, no container (same informational-not-celebratory treatment
  as Component 9's "Ready" status, not `color.status.success` — matches the same Atlassian-sourced
  semantic rule already locked there: an operational go-ahead is informational, not an achievement).
- Any Fail: a small alert icon + **"X defect(s) found — departure blocked pending authorization."**
  — `color.status.critical` icon and text, no container (this is a hard block, not a soft caution,
  so it stays the critical-red family, matching the toggle's Fail state).

**Action zone — banner + button(s) anchored as one fixed unit, corrected 2026-09-22.** A render
check found spacing inconsistent between states: with all 4 Pass, a large, variable gap opened up
between the banner and the button (the banner sits at the end of the scrolling checklist content,
the button is pinned to the viewport bottom as a sticky footer — so the gap between them depends on
how much content fills the space above, not a fixed value). With a Fail, the banner sat almost
flush against the button instead. **Fixed: the banner and button(s) are no longer independently
positioned — they're one fixed, non-scrolling zone anchored to the bottom of the screen**, with the
checklist rows scrolling independently above it. This guarantees identical internal spacing (12px
between banner and button, unchanged) in every state, regardless of how much checklist content is
above. `color.neutral.surface` background for this zone, no border/shadow needed to separate it
from the scrollable content — the fixed position alone does that job.

**Primary CTA — two distinct paths depending on outcome, both reusing Component 9's solo-primary
button geometry (filled/outline, 44px height, `radius.md`, full width) so nothing new is invented:**
- **All Pass:** "Confirm Inspection & Proceed →" — filled `#006837`, white text. Disabled until
  all 5 rows have an explicit Pass or Fail (matches the standing "no silent auto-advance" rule
  already established for the Dispatch Gate Action Drawer,
  `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` — a driver must positively resolve every check, not just
  scroll past unmarked ones).
- **Any Fail:** the same button slot instead shows **"Request Override — Report to Transport
  Office"** — filled `color.status.critical`, white text. Stays disabled until every Fail row has
  its mandatory photo and at least one reason chip selected (see the camera-icon/reason-chips note
  above), not just the Fail toggle tapped. **Not a self-override** — matches this system's own standing pattern (BR-009's
  Dispatch Gate override is granted by Daniel, never self-served by the person being blocked).
  Tapping it submits the defect report and **routes to
  Daniel's Dispatch Queue for authorization**, the same reassignment/authorization channel already
  locked for a Decline on Home (`02_USER_FLOWS.md` §3) — reused, not reinvented. The driver cannot
  proceed to Start Journey until that authorization comes back; what the driver sees while waiting
  (a pending/blocked state) is a real gap, not yet designed — flagged below.

**Still open:** the waiting-for-authorization state (after a driver requests override, before
Daniel responds) has no screen yet — does the driver wait on this same checklist screen, get
returned to Home with a new "Blocked — Pending Authorization" card state, or something else? Needs
its own design pass, not assumed here.

**Offline override fallback, added 2026-09-22 — a real gap, not an edge case.** This system's own
architecture commits to offline-first (`CVFMS_Architecture_and_Implementation_Summary.md`: "local
caching... allows drivers to log pre-trip checklists... even in low-connectivity rural
sub-counties, syncing when connection restores"), and several county sub-counties (e.g. Baringo)
are known for genuinely poor connectivity. GPS/timestamp capture and photo/description entry all
work fine offline (device-local, no network needed) — but **"Request Override — Report to
Transport Office" requires actually reaching Daniel**, which is impossible with zero connectivity
by definition. As speced above, a driver with a failed brake check and no signal would simply be
stuck: blocked from departing, no way to get authorized. **Three-tier escalation, confirmed with
the user rather than assumed:**
1. **Data connectivity available (default):** the digital override request already speced above —
   submits to Daniel's Dispatch Queue, driver waits for a real response.
2. **Data fails, voice/SMS may still work (common in low-connectivity rural areas — cellular voice
   often survives where data doesn't):** the button row shows a secondary fallback action. **De-
   emphasized 2026-09-22** — originally speced as a full-width outline button, same width/weight as
   the primary "Request Override" button directly above it; a render check found two full-width
   buttons stacked reads as a flat list of equal choices, not a primary action with a rare
   exception underneath it, adding to the same hierarchy imbalance the banner fix above addressed.
   **Fixed: "No connection — Call Transport Office" is now a plain centered text link**
   (`color.neutral.slate`, 14px/600, no border/fill, no button geometry at all), 8px below the
   primary button — matches how this project already treats other rare/exception actions (e.g. the
   "View N more pending" overflow link on Home) rather than presenting an edge case with the same
   visual authority as the main path. Still opens the device's native phone dialer pre-filled with
   the county's dispatch number. After the call, the driver returns to the app and fills a short
   required confirmation: "Verbally authorized by [name/role]" (text field) — creates a distinct,
   auditable record (not indistinguishable from a normal digital override), syncs when connectivity
   returns.
3. **No signal at all, voice included — the genuine last resort:** an **offline provisional
   override**, reached only after both paths above have been attempted/are unavailable. This is
   deliberately **not a simple button tap** — a confirmation dialog with explicit acknowledgment
   text ("No connection available. Proceeding without authorization will be logged and reviewed by
   the Transport Office once connectivity is restored. Only use this if you cannot reach the
   Transport Office by any means.") and a distinct confirm action, e.g. "I Understand — Proceed
   Anyway" (filled `color.status.critical`, deliberately not styled as an easy default action).
   Logged locally, syncs and surfaces to Daniel/audit the moment connectivity restores, **flagged
   with its own distinct provenance tag ("Offline provisional — pending review") that must never be
   silently merged into the record as if it were a normal authorized override** — this matters
   directly for FRAME-09's statutory audit trail, which needs to distinguish digital, verbal, and
   offline-provisional authorizations from each other, not just log "authorized: yes."

**Not yet resolved:** whether the app can reliably auto-detect "data failed but voice might work"
vs. "truly zero signal" (a PWA can generally detect network on/offline state but not always the
underlying cellular radio's voice-vs-data distinction) — likely resolved by always offering the
call fallback first and letting the driver themselves judge whether to escalate to the offline
provisional path, rather than the app trying to auto-detect signal quality. Full flow implication
(who reviews an offline-provisional override, and how) also needs reflecting in `02_USER_FLOWS.md`'s
Dispatch Gate diagram — flagged, not yet updated there.

### Component 11 — Assignment Detail / "View Details" (added 2026-09-22, FRAME-07)

**Why this exists — closes a gap referenced constantly but never built.** Every Home-screen card
(Component 9) has had a chevron since early in this project's mobile work, and both Component 9 and
`04_FIGMA_SCREEN_BLUEPRINT.md` repeatedly say "the rest lives behind the chevron" — reference ID,
full passenger breakdown, special requirements in full, expected return — without that screen ever
actually being specced. This component is that screen.

**Locked: full page, not a bottom sheet/drawer (decided 2026-09-22, checked rather than defaulted
to).** Worth stating explicitly since Component 10 just established a strong drawer pattern for
secondary detail (the Fail sheet) — the two aren't the same situation. Deciding factors: (1) **every
real reference cited for this screen's own content — BlaBlaCar's Ride Details, inDrive's "Order"
screen, inDrive's ride receipt, Grab Driver's Route Details — is itself a full page with a back
arrow, none use a sheet**; (2) content volume is meaningfully larger than the Fail sheet's compact
2-question form (reference strip, journey, trip info, requester + full manifest, vehicle, optional
documents — 6+ distinct sections); (3) the chevron trigger itself already signals "navigate deeper,"
distinct from a tap-to-open-sheet trigger elsewhere in this app; (4) forward navigation needs to
work page-to-page (tapping "Start Pre-Trip Inspection" from here goes to FRAME 7B, which reads
oddly as a sheet dismissing into a new page opening on top of it). **Standing rule from this
decision: drawer for a small, focused task nested inside a screen you're not leaving (Fail detail);
full page for a genuinely deeper, richer view you're navigating to (View Details).** Apply this
distinction to future screens rather than re-litigating page-vs-drawer per screen.

**Field list — grounded directly in SRS §5.4 (Vehicle Request Management) and §5.5 (Trip and
Journey Management), not guessed.** §5.4's full field list: *requester, department, purpose,
destination, date/time, expected return, passengers, special requirements, preferred vehicle type,
project/activity, supporting documents.* Cross-checked against what's already on the Home card face
(Component 9: status, time, destination, requester name + department + passenger count, vehicle
model + reg plate) — everything else from §5.4 belongs here, scoped to what a **driver** specifically
needs before executing the trip (not a full admin/audit view of every system field — that's
FRAME-09's job, not this screen's).

**Locked type scale and spacing for this page — closed, same discipline as Components 9 and 10, not
descriptive:**
- **Section label** (e.g. "TRIP INFO," "REQUESTER," "VEHICLE"): 12px/600, uppercase, +0.02em
  tracking, `color.neutral.slate-muted` `#64748B` — reuses Component 9's status-label type
  treatment exactly (size/weight/tracking), but neutral-colored here since these are structural
  headers, not status carriers. One per section, never omitted, never styled as a bigger heading —
  these must stay clearly subordinate to the destination headline (the one hero on this page, same
  rule as Component 9).
- **Label/value row:** label `type.body` (14px/400) `color.neutral.slate` `#334155`, value 14px/600
  `color.neutral.ink` `#0F172A` — label lighter weight, value heavier, so the eye lands on the
  actual answer, not the question.
- **Label column, fixed width — added 2026-09-22, a real gap in the original spec.** Without this,
  each row's value starts wherever its own label happens to end ("Departure" is short, "Expected
  Return" is longer), so values drift out of alignment down the page depending on which labels are
  long or short on a given screen. **Fixed: label column is a fixed 110px wide** (sized to fit this
  page's longest label, "Expected Return," at 14px/400 with room to spare), value column takes the
  remaining width and wraps within it if needed (as "Passengers" already does). Every value on the
  page starts at the same x-position, creating one consistent vertical reading rail — this is what
  Waymo's own reference screen does structurally, just not previously locked here as an explicit
  rule.
- **Page horizontal padding:** 16px both sides — reuses Component 9's card-padding value, applied
  here as the page's own edge padding.
- **Vertical rhythm:** 8px between rows within one section (e.g. between "Departure" and "Expected
  Return"); **24px between sections** — deliberately larger than Component 9's 12px inter-group gap,
  since these are independent full sections on a scrolling page, not sub-groups inside one compact
  card; picked as this component's own closed value rather than reusing Component 9's tighter
  figure out of context. No divider lines between sections — whitespace alone does the grouping,
  same "dissolve unnecessary containers" principle already applied throughout this app.
- **Section label to its own first row: 8px, not 24px — clarified 2026-09-22, a real ambiguity in
  the original spec.** The 24px figure above governs the gap *between* sections (one section's last
  row to the next section's label); it was never stated how far a section label sits from its own
  first row, which left open the risk of both gaps rendering identically — breaking the proximity
  cue that tells the eye what's grouped with what. **Fixed: a section label sits 8px above its own
  first row (the same tight rhythm as rows within that section), while the 24px gap stays reserved
  for the space between one section's last row and the next section's label.** This makes each
  label read unambiguously as attached to the content below it, not floating equidistant between
  two sections.

**Structure, top to bottom:**
1. **App bar** — reuses FRAME 7B's now-established M3 small top app bar exactly: back arrow
   (44px touch target) + title "Trip Details" (plain, not a greeting — matches the same rule
   already locked for FRAME 7D Profile).
2. **Reference strip:** trip reference ID ("REQ-2024-0851"), `color.neutral.slate-muted` `#64748B`,
   **12px/400 exactly — a render rendered this bold and large enough to compete with the
   destination headline for dominance, correcting that here in plain terms: this field must never
   be bigger or heavier than 12px/400 under any circumstance**, since it exists purely as reference
   metadata, not something a driver needs to notice first. The one field explicitly dissolved from
   the card face earlier specifically because it needed to live exactly here. Sits directly below
   the app bar, 16px below it. **Status appended, confirmed 2026-09-23 — a render added it
   unprompted and it's kept.** For the "Needs Your Response" variant only, the strip reads "REQ-
   2024-0851 · Needs your response" — the status half in `color.status.warning` `#B45309`, same
   color already used for this exact state on Component 9's Home card, at the same 12px size as the
   reference ID (color changes, size does not — this stays subordinate to the destination headline
   just like the plain reference ID does). Gives quick context for why Accept/Decline appear at the
   bottom without adding a new section. Not applicable to the "Ready" or "Scheduled" variants, which
   have no pending decision to flag this way.
3. **Journey block**, 24px below the reference strip — reuses Component 9's exact dot-connector-dot
   visual (same colors, same shape) so a driver recognizes it as the same journey they saw on Home,
   not a redrawn one. Destination headline stays the one hero, matching Component 9's hierarchy
   rule — nothing on this page is allowed to visually outweigh it, including the section labels.
4. **"TRIP INFO" section, 24px below the journey block** (checked against
   [BlaBlaCar's Ride Details screen](https://mobbin.com/screens/3bfb96de-284d-4f5a-9e7c-b2844cc6674f),
   already cited earlier this session for exactly this journey-plus-detail shape, and
   [inDrive's ride receipt/history detail](https://mobbin.com/screens/7f7c7ccb-96f7-4e90-b3f1-1c60be362dca)
   for the same plain label/value pairing convention — checked directly since inDrive is already a
   liked reference for this project, though most of its own *live* trip-tracking screens are map-
   heavy and don't apply here, given this project's standing no-map/no-navigation-app rule):
   departure date/time, **expected return date/time** (SRS field, not shown anywhere else in this
   flow), purpose (SRS field, not shown anywhere else), project/activity if present. Plain
   label/value rows, `type.body` (14px/400), `color.neutral.slate` labels + `color.neutral.ink`
   values — same pairing already used in Component 9's detail block, reused not reinvented.
   [inDrive's "Order" screen](https://mobbin.com/screens/ad7715b7-1700-49cc-9e1d-02df2a4e673a) is
   the closer structural match overall — journey with colored dots, vehicle info, a note, and
   stacked action buttons — and reinforces the action-zone and journey-visual choices already made
   here rather than requiring any change.
5. **"REQUESTER" section, 24px below Trip Info:** label corrected to **"Requester"** (a render used
   "Officer," a term not otherwise used anywhere in this app — SRS §5.4 itself says "requester,"
   and this project's own vocabulary elsewhere is consistent; realigned here rather than letting a
   second term for the same field drift into use), full name, department, **full passenger
   breakdown** (names, not just a count — the count alone is on the card face; this is where the
   actual manifest lives). **Requester/passenger overlap, resolved 2026-09-22 — a render surfaced a
   real ambiguity:** the requester often travels on the trip they requested, so she may legitimately
   also appear in the passenger list — but showing her name in both places with no stated
   relationship reads as unclear, possibly a data-duplication bug, to anyone reviewing this later
   (Daniel, an auditor). **Fixed: when the requester is among the passengers, tag her explicitly in
   the list** — "Mary Akinyi (Requester), John Otieno, Grace Wambui — 3 passengers," not just her
   bare name repeated with no context. special requirements in full text (e.g. "Wheelchair-
   accessible vehicle required — 1 passenger"). **No call/chat icon** — already rejected earlier
   this session as a gig-economy import that doesn't fit a pre-arranged government trip; unchanged
   here.
6. **"VEHICLE" section, 24px below Requester:** model, reg plate, current bay/location — stay plain
   label/value rows (sequential identity facts, not a cluster that benefits from tiling). **Fuel
   Level and Dispatch Clearance converted to a 2-tile Stat Tile row, 2026-09-23** — these two are a
   genuine cluster (both quick-glance operational status checks, naturally scanned together), the
   exact case the Stat Tile pattern (see §1) exists for. Two tiles, equal width, side by side:
   - **Fuel Level tile:** fuel-drop icon, `color.neutral.slate-muted` (a fuel level isn't inherently
     good/bad without a threshold, so it stays neutral-colored, not status-colored), value "75%"
     (16px/700), label "Fuel Level" (12px/400, muted) beneath it.
   - **Dispatch Clearance tile, absorbing the 2026-09-22 color correction below.** Icon
     (checkmark-in-circle), `color.brand.primary` when passed / `color.status.critical` when
     blocked — same icon color as the value, not a separate rule. Value "Passed" in the matching
     color (16px/700), label "Dispatch Clearance" (12px/400, muted) beneath it. **Original
     correction preserved for context:** a render had shown this status in the same plain
     `color.neutral.ink` as neutral facts around it, when it's functionally a Pass/Fail result, not
     a fact — this system colors status everywhere else it appears (never color alone). The tile
     treatment above supersedes the earlier "plain colored text, no container" fix, since the Stat
     Tile format already gives it a container and the color now lives on the icon+value together.
   **"Request Maintenance" entry point, added 2026-09-23** — a plain text link, `color.neutral.
   slate`, 14px/600, no button styling, sitting 12px below the Vehicle section's last row. This is
   the entry point into Component 19 (Submit Maintenance Request) — a driver noticing something
   wrong with the vehicle they're looking at can act on it right from this page rather than hunting
   for a separate location. Deliberately low-emphasis (plain link, not a button) since this is a
   rare, driver-initiated action, not a primary function of this screen.
7. **"DOCUMENTS" section** (SRS field), 24px below Vehicle, if any were attached to the original
   request: a plain list of file names/icons, tap to view — conditional, not shown if none exist,
   and the 24px gap above it collapses to zero when this section is absent (the next section simply
   follows Vehicle at the normal 24px, not a doubled gap) — same "don't render empty sections"
   discipline as special requirements on Component 9. **Touch target, added 2026-09-22 — a real
   omission, not a style choice.** This is the one genuinely tappable row in the scrolling content
   (every other row on this page is read-only text), but no touch-target size had been locked for
   it. **Fixed: each document row is 44px minimum height**, matching this project's own established
   touch-target floor everywhere else — this was simply missed when the section was first drafted,
   not a deliberate exception.
8. **Action zone**, fixed to the bottom of the viewport (not part of the scrolling content above,
   scroll ends at whichever section is last) — reuses Component 10's just-fixed fixed/anchored
   bottom treatment exactly: the **same action(s) as whichever card type this was opened from**,
   not a separate action set. Opened from "Needs Your Response" → Accept/Decline (Component 9's
   exact button spec). Opened from "Ready" → "Start Pre-Trip Inspection →" (Component 9's solo
   button spec). Opened from "Scheduled" → no action zone at all, purely informational, page ends
   at the last content section with normal bottom padding instead.

**No icons on the static info rows — checked against real apps, not just this project's own
reasoning (2026-09-22).** Directly asked and researched rather than assumed. Checked 10 real detail/
booking screens (Turo, BlaBlaCar, American Airlines, Viator, Agoda, Grab, Waymo, Fly Delta,
Tripadvisor, Lyft) for the pattern. **[Waymo's Trip Details screen](https://mobbin.com/screens/f93de6a0-b730-498e-abff-28bba5945cb6)
is the closest real structural match to this component** — dot-based journey, then plain
label/value rows (License Plate, Distance, Duration), then a Cost Details section, also plain —
and uses zero icons on any static row. The consistent pattern across all ten: icons appear only on
(1) tappable/navigational list rows, where the icon differentiates one clickable destination from
an identical-looking neighbor (American Airlines' "Trip options," Fly Delta's action list — the
same logic already used for FRAME 7B's checklist icons), or (2) specific, universally-recognized
glyphs for a specific data type (a phone icon next to an actual phone number, a card-brand icon
next to a payment method). **None of the ten put a generic person/vehicle icon next to an
already-labeled static row** — this page's section labels ("REQUESTER," "VEHICLE") already do the
categorization job an icon would duplicate. Confirms rather than reverses the original reasoning —
this is a settled decision with real evidence behind it, not an open question.

**Reversed 2026-09-23 — part of the broader "simple is not sterile" correction (see §1).** The
research above was sound on its own narrow question (do static rows need a *categorization* icon
next to an already-labeled section) and that conclusion still holds. But the cumulative effect of
this rule applied everywhere in the app — combined with icons already stripped elsewhere — made the
whole product feel flatter than intended. **Small icons are now permitted on this page's
informational rows for warmth**, not for categorization (the section labels still do that job):
18-20px, `color.neutral.slate-muted`, positioned before each row's label. This doesn't reopen the
navigational-icon question (chevron-terminated action lists still follow the original
differentiation-test logic) — it's specifically about static content rows gaining a small amount of
visual texture back.

**Vehicle photo added to the Vehicle section, 2026-09-23** — part of the same correction. A small
rounded-corner photo of the actual vehicle (64×64px, 8px corner radius, real photo not a
placeholder icon) sits at the top of the "VEHICLE" section, beside the model/reg-plate text —
matches Turo's own booking-detail pattern directly (a car photo appears on every one of its trip
screens, not reserved for a rare moment). **Real per-vehicle asset dependency, same category as the
county emblem and driver photo already flagged** — each vehicle in the fleet needs a sourced photo;
render nothing (not a generic car icon) if one isn't available for a given vehicle, consistent with
this project's existing "absent is honest, wrong is not" rule for missing assets.

**Resolved: View Details does not replace the card-face buttons, it supplements them (2026-09-22)
— closes an open question flagged since Component 9 was first written.** The alternative (moving
Accept/Decline off the card face entirely, only reachable via View Details) was considered and
rejected: it would add a forced extra screen transition to the single most common interaction on
Home, for every driver, on every assignment — a real cost with no offsetting benefit for the driver
who already knows what they're looking at. Keeping both means a driver who wants to decide fast can,
and a driver who wants to review full details first also can, without either path being penalized.

**Not built from scratch — reused structure, not a new pattern:** the label/value row pairing, the
journey visual, the button specs, and the action-zone anchoring are all pulled directly from
Components 9 and 10. The only genuinely new content on this screen is the SRS fields that had
nowhere else to live (purpose, expected return, full passenger names, project/activity, supporting
documents).

### Component 12 — Driver Profile (added 2026-09-22, FRAME 7D)

**Tab root, not a drilldown — no back arrow.** Unlike Component 11 (reached via chevron, needs a
way back), this is one of the three bottom-tab destinations, same category as Home.

**Header — overflowing-avatar hero, added 2026-09-22, checked against 4 real profile screens
before locking, not eyeballed.** User proposed reusing Home's header treatment with the avatar
straddling the banner/content boundary — checked directly rather than assumed a plausible layout.
[LinkedIn](https://mobbin.com/screens/dddb4708-b756-49bc-a73a-df0096817dc2),
[Places' Enrique Olvera profile](https://mobbin.com/screens/6c86f45d-ac38-480c-b2ed-ca55ecbb2aab),
[Glassdoor](https://mobbin.com/screens/65721aa3-c6cc-44c0-8fc2-ebf864b68fd9), and
[Vivino](https://mobbin.com/screens/4948dc9f-8682-4622-a059-63b6c0cce728) all converge on the same
execution — a photo banner, a large circular avatar with a white ring border straddling the
boundary (roughly half on the photo, half on the white content below), name and role in plain text
directly beneath. Locked, translated into this project's own existing tokens rather than new ones:
- **Banner:** reuses Home's exact photo + dark-overlay treatment (`color.neutral.ink` at 75-85%
  opacity, same county landmark image) — **confirmed to reuse the same image, not a separate one**,
  since this is a small app where the repetition reads as consistent county branding, not
  redundancy. Shorter than Home's expanded header, since there's no greeting text to make room
  for — banner is photo only, no text on it.
- **Avatar:** 88px diameter (a genuine hero size, not the small in-content scale used elsewhere),
  white 3-4px ring border so it reads clearly against both the photo above and the white content
  below, horizontally centered, vertically straddling the banner/content boundary (roughly half
  above, half below) — the real driver photo already confirmed fine for use, not a placeholder.
- **Name, "Joseph Mutua":** 24px below the avatar, **reuses the 20px/700 token already locked for
  Home's expanded-header name** — the one other place in this system a name gets bigger than the
  standard 16px, and this is the same category of singular identity moment, not a new size
  invented for this screen.
- **Role subtitle, "County Driver":** directly below the name, reuses `type.caption` (12px, muted)
  — same treatment as Home's "County Driver • On Duty" subtitle.
- **Real content consequence:** Role no longer repeats as a label/value row in the IDENTITY section
  below, since it's already stated prominently here — two statements of the same fact stacked on
  one page is exactly the pattern already fixed elsewhere in this project (e.g. Component 11's
  requester/passenger overlap). IDENTITY trims to the facts not already shown in the header.

**Structure below the header, reusing Component 11's section-label + fixed-label-column pattern
exactly — this page's remaining content is the same shape (a set of facts about one entity), so it
reuses the pattern rather than inventing a "card" treatment the rest of this app doesn't otherwise
use:**
1. **App bar:** plain title "Profile", no back arrow, sits on top of the photo banner (same
   treatment as Home's header icons — translucent circular backing for contrast against varying
   photo content).
2. **"IDENTITY" section**, 24px below the role subtitle: Staff Number (SRS §5.22 HR Integration
   field), Station — "Nakuru HQ Transport Pool". Role is deliberately not repeated here (see above).
3. **"LICENCE" section:** Class — "Class A, B, C1" (same format already used on the desktop Driver
   Registry table). Expiry — **reuses the exact 30/14/7-day compliance-alert cadence SRS §5.23
   already establishes for insurance/inspection/licence warnings**, not a new threshold invented for
   this screen: plain date + `color.neutral.ink` if more than 30 days out; "Expires in N days" in
   `color.status.warning` if 8–30 days out; "Expires in N days" in `color.status.critical` if 7 or
   fewer — the same urgency-as-text-not-color-alone discipline used everywhere else in this system.
   This is the same underlying licence-validity data BR-003 checks at Daniel's Dispatch Gate,
   surfaced here so the driver can see their own status, not just have it checked invisibly.
4. **"PREFERENCES" section:** Language toggle, English / Kiswahili — a two-option segmented control
   reusing Component 10's exact Pass/Fail toggle geometry (same two-choice pill shape, 44px tappable
   zone/36px visible height), not a new control invented for one setting. Applies to this app only
   for now — the desktop system has no localization spec yet, a separate open question this doesn't
   resolve.
5. **Sign-out, corrected 2026-09-22 — checked against 8 real profile screens rather than assumed.**
   Originally speced as fully plain text with no container. Checked real apps: Setel and OKX do use
   plain text, but Mercedes-Benz, Panera Bread, Crypto.com, and 5 Minute Journal all give Sign Out
   an outlined button — a clear majority. Mercedes-Benz's pattern is the clearest signal: "Log out"
   gets a modest outline button, while "Delete account" (a genuinely rarer, more severe action) is
   demoted further to plain text below it — a two-tier system, not a flat one. **Fixed: Sign Out
   reuses Component 9's exact Secondary/outline button style** (white fill, `1px solid
   color.neutral.border`, `color.neutral.slate` text, same geometry as Decline) — not full-width,
   content-hugging, centered — rather than either plain text or inventing a third button treatment.
   32px above it (double the normal 24px section gap) to signal it's a different category of thing
   entirely, not another preference.

No fixed action zone on this page — nothing here needs a persistent decision the way Components 10
and 11 do; it's a settings-style read/adjust page, ordinary scroll to the bottom is sufficient.

### Component 13 — Trips Tab (added 2026-09-22, FRAME 7E)

**Real scope question resolved before locking this, not assumed.** Flagged since this frame was
first sketched: if Home (Component 9) already shows Ready/Needs-Response/Scheduled items, what does
a separate Trips tab add that isn't redundant? **Resolved: Home and Trips answer different
questions.** Home is the urgency-ordered *execution* view — only what's current and actionable
today (a deliberately narrow, triage-focused list, per Component 9's own "why this exists" note).
Trips is the complete *intake ledger* — every assignment given to this driver that hasn't been
completed yet, ordered chronologically (not by urgency), including trips scheduled far enough out
that Home wouldn't surface them yet (Home only shows near-term Scheduled items to avoid clutter).
A driver checks Home to know what to do right now; a driver checks Trips to know everything that's
coming, in order — genuinely different jobs, not two views of the same list.

**Structure — reuses Component 9's row anatomy exactly (same type scale, spacing, no-chip status
text), since this is structurally the same "assignment row" concept, just re-scoped and
re-ordered. Checked against 8 real trip/booking list screens (2026-09-22), not just reused from
Component 9 on assumption:**
- **[Navan's Trips screen](https://mobbin.com/screens/dc0200de-0819-491e-b2dd-ce7b3d9d81d2) is the
  closest real domain match found this session** — corporate/business travel, not leisure —
  and validates the two-state color split directly: an urgent card ("Flight Hold... Expires in:
  21h 35m 54s," warning-red) next to a muted one ("invited... Expires in 55 days," neutral gray).
  Same distinction as Awaiting-Response vs. Accepted here.
- **[Zomato's "Your bookings" screen](https://mobbin.com/screens/b2da1a7b-4031-4299-88e6-4942956cd1bc)**
  confirms both choices already made: uppercase section labels ("UPCOMING," "HISTORY" — same
  treatment as this component's own list header) and plain colored status text with no chip/pill
  container ("Booking cancelled," "Booking failed," both plain red text).
- **Scalability note, not built into the first version:** [Qantas](https://mobbin.com/screens/8f6f9d0f-d3fb-448f-837b-4ff90ad8ef82)
  groups rows under plain date headers ("Mon, 5 Jan") rather than repeating the date on every row.
  Worth adopting once this list realistically grows past 2-3 items; not necessary for the initial
  build with only a couple of assignments.
1. **App bar:** plain title "Trips", no back arrow (tab root). Subtitle beneath it, `type.body`
   muted, e.g. "2 upcoming" — a plain count, not a pill/badge (matches this app's now-consistent
   preference for plain text over containers wherever a container isn't earning its place).
2. **List, ordered by date/time ascending** (not urgency — this is the one structural difference
   from Home's ordering logic): each row reuses Component 9's card structure — destination +
   date/time, requester name, status. **Status text simplified to two states, not three, since this
   list isn't asking "is it today" the way Home is:** "Awaiting Your Response" (`color.status.
   warning`, matches Needs-Response) or "Accepted" (`color.neutral.slate`, plain — deliberately not
   reusing "Ready"/"Scheduled" language, since a driver scanning this list is asking "did I respond
   yet," not "is this today").
3. **Tap behavior, corrected 2026-09-22** — an earlier draft of this row said tapping an "Awaiting
   Your Response" row opens "FRAME 7A/State 0," a reference to a state that no longer exists post-
   rebuild. **Fixed: tapping any row opens Component 11 (View Details)** — the Needs-Response variant
   (with Accept/Decline) for an unanswered item, the Ready or Scheduled variant (read-only) for an
   accepted one — reusing the screen already built rather than inventing a second detail view.

### Components 14–16 — Splash, Login, First-Run Setup (added 2026-09-22, FRAME-07 pre-auth)

**Why these exist — a real, SRS-grounded gap, not scope creep.** Nothing built so far gets a driver
from opening the app to seeing Home. Checked the SRS directly rather than assume: §9 (Security
Requirements) requires "Username/password authentication," "Single Sign-On where available," and
"Role-Based Access Control"; §11 (Mobile Application) lists **"Driver login and assigned vehicle
view"** as its first function. This is a named requirement, not an invented one.

**Onboarding carousel explicitly rejected, not just omitted.** A multi-slide feature-tour carousel
is a consumer-app pattern — it exists to build trust and explain value to someone who *chose* to
download an app. Joseph is handed a county-issued device with this app pre-installed for work; he
doesn't need convincing. Building a tour here would be the same category of unrequested complexity
already cut elsewhere in this project (SOS, chat icons, decorative loading states). **Kept instead:
one minimal, functional first-run step** (language + notification permission) — not promotional,
just the two real one-time choices that actually need making.

**Component 14 — Splash, hierarchy corrected 2026-09-22.** Originally centered the CVFMS wordmark
as the primary brand element, with the county emblem as a secondary addition beneath it — backwards
for a platform that's deployed per-county. **CVFMS is the underlying system, not the organization a
driver works for; the county is.** Corrected to lead with the county's own identity and demote
CVFMS to a quiet "Powered by" attribution, the same pattern government/enterprise software
generally uses when a platform is white-labeled per deploying organization. Full-bleed
`color.brand.primary` `#006837` background, no photo (kept distinct from Login's photo-banner
treatment). Centered as one block: county crest/logo (image asset — flagged as a real per-county
sourcing dependency, same as the emblem already flagged for Home's header; render nothing rather
than a wrong or generic substitute if unavailable), county name ("Baringo County," bold, white,
the actual organizational identity leading), then a smaller line beneath it, "Vehicle Fleet
Management System" (white, muted opacity, describing what this specific app is). Near the bottom
of the screen, small and quiet: "Powered by CVFMS" — the platform attribution, not the headline.
No spinner needed if load is fast — this is a brief transitional screen, checking cached auth state
(offline-first architecture already established), not a designed "experience." Auto-advances to
Login (no valid session) or straight to Home (valid cached session — a driver who logged in once
shouldn't need to log in again every offline app open).

**Component 15 — Login.** Checked against
[DocuSign's](https://mobbin.com/screens/38b0081f-b0a6-4213-af88-cd4ca9e8c2c7) and
[Upwork's](https://mobbin.com/screens/ad035e48-ef44-4eb3-aa99-529aaca9cf14) login screens for the
form itself — both validate a plain, single-screen username+password form, not the multi-step
email-then-password flow B2B SaaS apps like Navan/Deel use (that pattern exists to resolve which
company tenant an email belongs to — CVFMS is one county system, that problem doesn't exist here).

**County landmark photo added to this screen, 2026-09-22 — user's proposal, checked against real
execution patterns before locking.** Since CVFMS deploys per-county, showing a county landmark
photo on Login (not just Home) makes the county identity visible from the very first meaningful
screen a driver sees, before authentication even happens. Checked two real execution patterns:
[Peacock's](https://mobbin.com/screens/cb9736f7-aecd-4b43-a981-81dadd209d92) full-bleed-photo-plus-
floating-white-card (a genuinely well-executed pattern), versus
[Grill'd's](https://mobbin.com/screens/261e6bbf-785c-4c59-97eb-d80ec7c5b823) and
[Taco Bell's](https://mobbin.com/screens/57aa091c-6caf-45c4-b2be-2ab2671fb081) top-photo-banner-
then-white-form-below. **Chose the banner pattern, not because it's objectively better, but because
Home and Profile already both use it** — reusing it a third time here keeps one consistent "how
CVFMS combines a county photo with content" rule across the app, instead of introducing a fourth
distinct treatment. **Tracking this honestly: county photo is now a recurring identity-moment
pattern across three screens (Home, Profile, Login), not the single, one-off exception it was
first introduced as — worth knowing rather than letting the framing quietly go stale.**
- **Header/banner:** same county landmark photo + dark overlay (75-85% opacity) as Home and
  Profile — reuses the exact image and overlay treatment, not a new asset. **Text on the banner
  corrected 2026-09-22 to match Component 14's hierarchy fix** — this previously said "CVFMS
  wordmark," which is backwards for the same reason it was on Splash: the county is the
  organization a driver works for, CVFMS is the underlying platform. Centered on the photo:
  county name, "Baringo County," white text (same weight/role as Splash's county name, one step
  down in size since this banner is shorter and has a form beneath it, not a full-screen moment).
  No "CVFMS" text on this screen at all — the platform attribution belongs on Splash only, not
  repeated on every screen.
- **White content area below the banner:** plain heading "Sign In," `type.card-title-mobile`
  (16px/700). Staff Number field (reuses SRS §5.22's own field, matching Component 12's Profile
  field — the same identifier a driver already knows, not inventing a separate "username").
  Password field, masked with a show/hide toggle. Primary button, "Sign In" — reuses Component 9's
  solo-primary button spec exactly (filled `#006837`, white text, 44px height, `radius.md`, full
  width). "Forgot password?" plain text link beneath, `color.neutral.slate`, low emphasis.
- **No SSO button in this first build** — SRS §9 names SSO as available "where approved and
  technically available," which isn't confirmed for this rollout; adding a button for an
  unconfirmed integration would be speculative, not grounded. Flagged as a future addition, not
  built now.

**Component 16 — First-Run Setup**, shown exactly once after a driver's first successful login,
never again. Checked against
[Wispr Flow's language-confirm screen](https://mobbin.com/screens/bf00197d-a10e-4333-bbaf-2816a04115eb)
for tone — deliberately plainer than the rest of that same search's results (Duolingo, Etsy,
Hinge, Too Good To Go, DICE, Vocabulary, Speak), which are consumer apps using illustration and
persuasive copy to earn a permission grant; that framing doesn't fit a work tool a driver is
already required to use.
- Plain heading, "Quick Setup" — `type.card-title-mobile`, no illustration.
- **Language:** English / Kiswahili — reuses the exact segmented-toggle geometry already locked for
  Component 12 (Profile) and Component 10 (Pass/Fail), not a new control invented for this screen.
- **Notifications:** one short, plain sentence explaining the real reason ("Get notified about new
  assignments and updates"), then a single button, "Enable Notifications," which triggers the
  native OS permission dialog — this screen doesn't try to replicate that dialog, just leads into
  it. A plain "Skip for now" text link beneath, `color.neutral.slate`.
- Primary button, "Continue" — reuses the same solo-primary button spec, advances to Home.

### Component 17 — Trip Start / Active Trip / Trip End (added 2026-09-22, FRAME 7C)

**Why this exists.** Closes the largest remaining SRS §11 gap: "Accept/start/end trip" and
"Capture odometer and fuel information" — Accept is done (Component 9), start/end trip and
odometer/fuel capture were only ever a rough content sketch, never locked like everything else
this session. Reached after a passed FRAME 7B inspection (or via the "Ready" card's action).

**Corrections from the original sketch, checked against real references rather than carried over
as-is:**
- **Button height was 52px — corrected to 44px**, matching this project's own established
  touch-target floor (Component 9) everywhere else. 52px predates that correction and should never
  have survived into a new component.
- **"Camera Verified" badge on the starting odometer, dropped.** Checked
  [Turo's odometer/fuel confirmation screen](https://mobbin.com/screens/fddca36b-af63-46e8-b170-e7b1ffaba2f9)
  — the closest real analog for "confirm vehicle state at trip start" — and it shows the odometer
  as a **plain, pre-filled number to confirm**, not something requiring photo proof. Turo's actual
  photo-capture step ([exterior condition photos](https://mobbin.com/screens/5b04fcaf-7d3e-4437-b40c-bea2a1431859))
  is a separate, optional, skippable step about general vehicle condition, not tied to the odometer
  specifically. A dedicated odometer photo would also duplicate evidence-gathering CVFMS's own
  Component 10 checklist already does before this screen is ever reached (defect photos + reason
  chips on Fail). **Fixed: Starting Odometer is pre-filled from the vehicle's last recorded
  reading** (system data, not blind entry), shown as an editable value the driver confirms or
  corrects if it's wrong — matches Turo's exact pattern.
- **"Does this system need a distinct 'Arrived at Destination' state?" — resolved, not left
  open.** Flagged against Grab Driver's multi-stop confirm-arrival pattern. Resolved: no — Grab's
  driver juggles multiple sequential stops where confirming arrival at each one is operationally
  meaningful; a CVFMS driver has one destination per trip (with an optional return leg already
  captured as metadata via the "expected return" field, not a separate interactive step). Nothing
  operationally happens at arrival that needs its own recorded moment. One continuous Active Trip
  state, start to finish, is sufficient — do not add an "Arrived" step.

**Structure:**
- **State 1 (Start Journey).** No back arrow — forward-only, same logic as Login→First-Run (once a
  driver has passed inspection, going back to "undo" starting the trip isn't a real path). **Stage
  indicator confirmed 2026-09-23 — extended to all 3 states, not just Active Trip.** A render added
  "Stage 1 of 3 · Ready to Start" here (and "Stage 3 of 3 · Trip Closure" on State 2) — a genuine
  improvement over the original spec, which only defined the stage indicator for State 1.5. Gives
  the driver a complete sense of progress throughout the whole flow, not just mid-trip. **Locked as
  the standard going forward. Paired with a visual stepper, added 2026-09-23** (see §1, checked
  against Navan's numbered-circle checkout steps) — 3 small circles (8px diameter) connected by a
  thin line, sitting beside the "Stage X of Y" text on all three states: completed/current stage
  filled `color.brand.primary`, upcoming stages `color.neutral.border`. Gives progress a genuine
  visual read, not just text to parse. Starting Odometer: pre-filled, editable value, **rendered as a
  bordered/boxed field (confirmed 2026-09-23)** — the original spec said only "large, legible
  display," ambiguous about container treatment; a render used a bordered box (matching Closing
  Odometer's already-boxed treatment in State 2), which reads correctly as "editable" via visual
  affordance and keeps Starting/Closing Odometer visually consistent with each other. Locked: 28px,
  weight 700, `#0F172A`, inside a 1px `#E2E8F0` bordered box, 8px corner radius. **Fuel Level pill
  removed from this screen, 2026-09-24** — moved to Component 10's checklist as its 5th Pass/Fail
  row instead (see Component 10's own note for the full reasoning: SRS §5.6 names fuel level as a
  mandatory dispatch-gate condition alongside tyres/lights/brakes, which this screen's passive,
  consequence-free pill didn't reflect; §5.16's telematics scope confirms the reading is
  self-reported, not sensor-sourced). By the time a driver reaches Start Journey, fuel level has
  already been checked and, if inadequate, blocked with the same override path as any other failed
  inspection item — showing it again here would just repeat an already-resolved fact. **Vehicle
  photo, added 2026-09-23, refined 2026-09-24 —
  genuine improvement found in a render, locked as the standard.** Rather than a bare photo floating
  above the Starting Odometer section, a render paired it directly with the vehicle's model and
  plate in one horizontal identity card: photo on the left (rounded-corner, ~72×72px within the
  card), "Toyota Land Cruiser" (bold) and "KBZ 442A" (muted, beneath it) on the right, the whole
  thing on a light gray card background (`color.neutral.bg` `#F8FAFC`, 12px radius). **This resolves
  the actual reason the photo belongs on this screen and not on States 1.5/2 (see the "photo scope
  narrowed" note further down this component): it's not decorative, it's an identity-confirmation
  card — photo plus model plus plate together let the driver visually confirm this is their assigned
  vehicle before starting the trip.** A bare photo alone doesn't carry that meaning as clearly; text
  alone (as Component 11 already had) doesn't let a driver visually spot-check against the vehicle
  in front of them. Locked: this pairing, not a standalone photo. **GPS microcopy converted to a
  tinted info card, 2026-09-23** —
  was plain muted text, now a soft card: `color.brand.primary-subtle` `#E6F2EB` background, `1px
  solid` a slightly darker tint of the same green, 12px corner radius, 12px padding, a small
  location-pin icon (16-18px, `color.brand.primary`) beside the text: "Starting this trip enables
  continuous GPS location logging to county dispatch" — same body text, now in a card instead of
  floating as plain muted text. Primary CTA: "Start Journey Now" — reuses Component 9's solo-
  primary button spec exactly (filled `#006837`, 44px, `radius.md`, full width — not 52px).
- **State 1.5 (Active Trip).** Stage indicator, "Stage 2 of 3 · In Transit" (borrowed from Grab
  Driver's numbered-stage pattern, already cited). **Vehicle photo tried 2026-09-23, reverted same
  day — see the "photo scope narrowed" note at the end of this component.** No photo on this state.
  Persistent banner: "In Transit to [destination]
  • Started [time]." Two contextual actions, equal weight, **corrected to reuse Component 9's exact
  Secondary/outline button style** (not vague "chips" as the original sketch said): "Log Fuel Stop"
  and "Report Breakdown / Defect" — content-hugging, 44px tappable/36px visible height, side by
  side. Neither is required to proceed. **"Report Breakdown / Defect" is a button here, leading to
  its own dedicated reporting flow — not yet designed, scoped as the next piece of work after this
  component.** Primary CTA stays available throughout: "Complete Trip & Record Closing Odometer."
- **State 2 (End Journey & Closure).** Stage indicator, "Stage 3 of 3 · Trip Closure" (part of the
  now-locked all-3-states stage indicator, see State 1). No vehicle photo — see note below. Same
  persistent banner as State 1.5. "TRIP SUMMARY" section
  label — reuses Component 11's exact uppercase/tracked section-label style, not an undefined
  grouping treatment (confirmed via [Mercedes-Benz's "Trip data" screen](https://mobbin.com/screens/b492b0f8-789c-4388-b298-ddfb78aff7f6),
  already cited, for the OVERVIEW/FROM START-style grouped-rows precedent). **Rows: plain stacked
  label/value, NOT a Stat Tile row — a 3-tile conversion was attempted 2026-09-23 and reverted the
  same day, see note below.** Starting Odometer "142,850 km" (read-only), Closing Odometer
  (editable, full-width bordered input, "Enter reading" placeholder, "km" suffix — the original,
  working treatment), Distance Travelled auto-calculates once Closing Odometer has a value. Post-
  trip check: "Any mechanical
  defects during trip? [None / Report]." Primary CTA: "Finalize & Close Trip" — releases the
  vehicle back to the Available pool.

  **Reverted 2026-09-23 — both the Trip Summary tiles and the State 1.5/2 vehicle photo, after
  direct user pushback ("the three columns simply does not work" / "I also don't get the purpose of
  having the car image").** Kept in the doc as a reasoning trail, not deleted, since both were
  genuine attempts with real logic behind them that turned out not to hold up:
  - **Trip Summary tiles:** failed to render correctly across four separate prompt attempts (see
    `08_PROJECT_HANDOVER.md` §23a-23b for the full history), and the underlying reason is structural,
    not a prompting problem — Closing Odometer is an *active input field*, unlike Vehicle section's
    two read-only facts (Fuel Level, Dispatch Clearance) that compress into tiles fine. An input
    wants a full-width label directly above it and room to be read/tapped comfortably; a third-width
    tile fights that. The Stat Tile pattern stays correct for genuinely static fact clusters (Vehicle
    section, unchanged) — this was simply the wrong content for it.
  - **Vehicle photo on States 1.5/2:** the Turo precedent it was based on (§1, second pass) doesn't
    actually transfer. Turo's driver browses many different cars across many different bookings, so
    a repeated photo re-confirms identity each time, in a genuinely multi-vehicle context. A CVFMS
    driver is on one continuous trip with one vehicle across three sequential screens — by Active
    Trip and Trip Closure they've already seen it twice. Repeating it a third time is decorative,
    not functional. **The photo earns its place only on State 1 (Start Journey)**, paired with the
    pre-trip odometer/fuel checks, where it genuinely serves an identity-confirmation purpose before
    the trip begins — that placement is unchanged and stays locked.

**Not built in this pass, scoped as the next piece of work:** the actual Report Breakdown/Defect
reporting screen (currently just a button here) and Submit Maintenance Request — both real,
SRS-named functions with no design yet. Flagged, not silently deferred.

### Component 18 — Report an Issue: Breakdown / Accident (added 2026-09-23, FRAME 7F)

**Grounded in SRS field lists, not guessed.** §11 names "report breakdowns and accidents" as one
combined driver function; §5.15 (Accident and Incident Management) lists the full field set:
*vehicle, driver, date/time, location, description, conditions, other parties, police reference,
witnesses, photos, damage, estimated cost, insurance claim, investigation, liability, corrective
action.* Checked which of these a driver can actually capture at the scene versus which belong to
a back-office workflow: **estimated cost, insurance claim, investigation, liability, and
corrective action are not driver-entered fields** — those are Grace's/Finance's/an investigator's
job, filled in after intake, not something to put in front of a driver on the roadside. The
driver-facing form only needs the fields a person at the scene can actually observe and report.

**One branching flow, not two separate ones — confirmed with the user rather than assumed.**
Checked against [Temu's](https://mobbin.com/screens/eb4ba5ea-f13c-4732-bd74-2e92edaf662c) type-
then-detail structure and [eBay's](https://mobbin.com/screens/9ad9a287-74a3-497b-ba7c-8f984796538a)
type-selector — both validate picking a category first, then showing only the fields relevant to
it, rather than building two near-duplicate screens that share most of the same shell.

**Structure:**
1. **Type selector** (first screen, reached from Component 17's "Report Breakdown / Defect"
   button, or an equivalent entry point during Active Trip): plain heading "What happened?", two
   large tappable option rows, "Mechanical Breakdown" and "Accident / Collision" — full-width
   cards, not a bottom sheet (this screen is already a dedicated destination, not worth a second
   layer of sheet-opening on top of it). Selecting one advances to the matching path below.
2. **Breakdown path** — checked against
   [Shell's "Report an issue" screen](https://mobbin.com/screens/92de5008-73a5-4de0-9534-b0809e004a1c),
   the closest real match: context header (vehicle, reused label/value styling, read-only, auto-
   filled — a driver isn't re-typing what the app already knows), **now paired with the vehicle's
   photo (2026-09-23, same 64×64px/8px-radius treatment as Component 11)**, then "What's wrong?"
   quick-select reason chips (Engine / Brakes / Tyres / Electrical / Other — same chip geometry as
   Component 10), then photo — **recommended, not mandatory** (deliberately different from
   Component 10's Fail photo, which is mandatory: a driver dealing with a live breakdown, possibly
   blocking traffic, shouldn't be gated on taking a photo before they can report and get help), then
   an optional Notes field, then Submit — reuses Component 9's solo-primary button spec, routes to
   Daniel's Dispatch Queue (same channel already locked for Decline and Fail-override).
3. **Accident/Collision path** — the SRS §5.15 driver-capturable subset: auto-filled vehicle/date/
   time (**paired with the vehicle photo, same as the Breakdown path above**), auto-captured GPS
   location shown for confirmation (editable if GPS is unavailable),
   required Description (free text), Conditions quick-select chips (Clear / Rain / Night / Poor
   Visibility / Other), **"Other parties involved?" Yes/No toggle — neither option selected by
   default (corrected 2026-09-23 after a render pre-selected "No")**, same no-default-state rule
   already locked for Component 10's Pass/Fail toggle: an unreviewed default answer to a factual,
   liability-relevant question is a real compliance risk, not just a style preference — revealing
   repeatable name/contact/vehicle-reg fields per party if Yes, optional Police Reference field,
   optional Witnesses
   (repeatable name/contact), Photos (recommended, same treatment as the breakdown path), Submit.
   **Submission on this path also triggers an immediate notification/alert**, not just a queued
   entry — SRS §5.23 explicitly names "accident" as a notification-triggering event, distinct from
   the lower-urgency breakdown path.
4. **Offline fallback, both paths** — reuses Component 10's exact "No connection — Call Transport
   Office" plain-text-link treatment (not a full button, per that correction), same escalation
   logic already established there. [Temu's alternate "Request a phone call to report" link](https://mobbin.com/screens/eb4ba5ea-f13c-4732-bd74-2e92edaf662c)
   independently reinforces that a phone-call fallback for report flows is standard practice, not
   a CVFMS-specific invention.

### Component 19 — Submit Maintenance Request (added 2026-09-23, FRAME 7G)

**Closes the third and last of the three real SRS §11 gaps found by checking the full function
list.** §5.9 (Maintenance Management)'s work-order fields — *diagnosis, work, parts, labour,
supplier, estimated/actual cost, approvals, completion, odometer, warranty* — mostly belong to
Workshop/mechanic execution (FRAME-03's job-card domain), filled in after intake, not something a
driver fills in. **One field is the exception, corrected after a direct question:** odometer isn't
a Workshop-only field — it's a point-in-time fact best captured by whoever's present when the
issue is noticed, the same reasoning already applied to Component 17's Starting Odometer. A driver
filing this request naturally has the current reading at hand; it shouldn't wait to be backfilled
by a mechanic days later.

**Checked against [Rivian's "Vehicle maintenance" screen](https://mobbin.com/screens/56bd4a31-4b7f-4bd9-828d-f7098b65171a),
the closest real match found** — mileage is the visual centerpiece of that screen (a large,
prominent number, not a small label/value row), with a service-interval note beneath it and a
single "Request service" action. Mirrored here rather than treating odometer as just another field
among many.

**Structure:**
1. **Entry point:** a plain text link, "Request Maintenance," at the bottom of Component 11 (View
   Details)'s Vehicle section — reuses that screen's existing low-emphasis link treatment rather
   than inventing a new navigation affordance. **This is a reasonable placement call, not
   definitively the only right one** — flagged in case a more prominent or differently-located entry
   point turns out to be needed once this is in front of real drivers.
2. **Vehicle context** (auto-filled, read-only) — same label/value treatment as Component 18's
   Breakdown path, **paired with the vehicle's photo (2026-09-23, same 64×64px/8px-radius
   treatment used throughout)** — especially relevant here, since a maintenance request is
   specifically about the vehicle's condition; seeing it reinforces what's being reported on.
3. **Current Odometer Reading** — large, prominent display (`type.card-title-mobile`-scale or
   bigger, not a small row), pre-filled from the vehicle's last recorded reading, editable —
   matches Rivian's treatment and Component 17's Starting Odometer pattern exactly. **Same shared
   data source as Component 17, not an independent value — clarified 2026-09-23 after a direct
   question.** There is one continuously-updated "vehicle's last known odometer reading" in the
   system, not separate numbers per screen: it's written whenever a trip closes (Component 17's
   Closing Odometer becomes the new baseline) and read by every screen that needs "current
   odometer" — Trip Start's Starting Odometer, Trip End's carried-over value, and this screen's
   pre-filled reading. These must never be built as three independent mock values that could drift
   out of sync; they are the same field, read in three places.
4. **"What needs attention?"** — quick-select reason chips, same geometry as Component 18:
   Routine Service / Brakes / Tyres / Engine / Electrical / Other.
5. **Urgency** — two-option segmented toggle, "Routine" / "Urgent," same pill-toggle geometry
   already used throughout (Component 10's Pass/Fail, the language toggles) — **neither selected
   by default**, same no-default-state rule just corrected on Component 18, for the same reason: an
   unreviewed default on a field that affects triage priority is a real risk, not just a style
   choice.
6. **Description** (optional), multi-line text area, same treatment as Component 18's Notes field.
7. **Photo** (optional), same camera + "Add Photo" outline button as Component 18.
8. **Submit** — reuses Component 9's solo-primary button spec. **Routing resolved 2026-09-23: to
   Daniel's Dispatch Queue, same channel as every other driver-initiated exception.** Considered
   routing directly to Peter's Workshop board (maintenance is literally Workshop's domain) but
   rejected in favor of consistency: Decline (Component 9), Fail-override (Component 10), and
   Breakdown/Accident (Component 18) all route through Daniel first — a single, consistent maker-
   checker intake point for everything a driver flags, not a special-case path just for this one
   request type. Daniel triages and forwards genuine requests to Peter's Workshop board rather than
   the board receiving unfiltered driver submissions directly.
9. **Offline fallback** — same plain-text "No connection — Call Transport Office" link as
   Component 18, unchanged.

---

## §1.4 Guerriero Execution Standards (added 2026-09-26)

**Source:** Sebastiano Guerriero (@guerriero_se) Before→After analysis of a workshop job
scheduling interface, 2026-09-25. Reference screenshots in
`.agents/skills/design-crit-guerriero/references/`. Core principle:

> *"Most of the job is about refactoring the content so you can deliver more information
> within the same space."*

This is not about aesthetics. It is about structural clarity. The five standards below are
build specifications — they govern what gets constructed in every prompt, not just how
output is evaluated after the fact. The evaluation framework (7-point checklist, Before/After
references) lives separately in the `design-crit-guerriero` skill.

### §1.4.1 — Semantic Icon on Every Detail Row

Every row in a detail drawer, job panel, or assignment detail that carries a label/value
pair must be prefixed with a contextual, non-interchangeable SVG icon that signals the
*type* of information before the user reads the text:

- Calendar icon → date / scheduled time
- Clock icon → duration or time remaining
- Location pin / bay icon → physical location or bay assignment
- Person silhouette → assigned technician or driver
- Car / vehicle icon → vehicle identity
- Wrench / tools icon → service type
- Document icon → attached files or reports

**The icon must be non-swappable:** if pulling it out and replacing it with a different icon
causes no loss of meaning, the original was decoration and must be replaced or removed.
All icons: outline style (Heroicons or Lucide, pick one per file), 1.5px stroke, 18px,
color matches adjacent text (`color.neutral.slate` for standard rows,
`color.brand.primary` inside tinted info cards). Never emoji characters.

This applies to: Component 4 (Action Drawer detail sections), Component 6 (Data Table
row-expand views), Component 11 (Assignment Detail), FRAME-03 (Job Card detail drawer),
FRAME-02 (Request Detail panel).

### §1.4.2 — Struck-Through Checklist Completion

Any checklist in this system (dispatch gate BR-001–005, walkaround inspection, QA release
gate, trip closure defect check) must visually differentiate three states without relying
on color alone:

- **Done:** struck-through text (`text-decoration: line-through`), muted slate color
  (`color.neutral.slate-muted`, `#64748B`), filled checkmark icon.
- **Current / Pending:** full-opacity text, dark ink (`color.neutral.ink`), empty circle
  or animated spinner icon.
- **Upcoming:** muted/greyed text (`color.neutral.slate-muted`), empty grey circle.

This pattern makes job completion status readable at a glance — no counting, no reading.
Applies to: FRAME-02 Dispatch Gate checklist, FRAME-07B Walkaround Inspection, FRAME-03
QA release gate, Component 10 (Pre-Trip Inspection Row).

### §1.4.3 — Progressive Disclosure (Content Expands, Does Not Truncate)

Content may not be truncated with an ellipsis (`...`) unless a deliberate, clearly
labelled expansion affordance is immediately available on the same element.

- **Calendar cards and list rows:** short cards show the essential (name + time); taller
  cards reveal secondary content (technician, client, status) as the container grows.
  This is adaptive content, not fixed truncation.
- **Tables:** truncated cell values must have a "Quick view" or row-expand interaction
  that reveals the full value inline — not a navigation to a new page.
- **Detail drawers:** all content is shown in full; scrolling within the drawer is
  acceptable, hiding content behind an unexplained ellipsis is not.

This applies system-wide. Any rendered screen with unexplained `...` truncation is
incomplete regardless of whether the spec content is technically present.

### §1.4.4 — Inline Action Proximity

Actions must live at the same visual level as the content that motivates them — not in
a remote footer, not in a separate Actions section, not requiring a scroll to reach.

- Client row with "Aisha Johnson" → "Call" and "Message" links on the same line.
- Driver row in dispatch detail → "Assign" link inline with the unassigned state label.
- Checklist row marked Fail → camera/photo capture icon revealed on that specific row,
  not a blanket "Attach photos" button below the whole list.
- Override justification field → appears adjacent to the failed gate item, not at the
  bottom of the form.

This applies to: Component 4 (Action Drawer), FRAME-02 (Dispatch Gate, Override field
placement), FRAME-07B (walkaround defect photo capture), Component 18 (Report an Issue).

---

## §1.5 Wix Surface & Controls — adopted as the desktop standard (2026-10-01)

User confirmed the desktop direction is "a Wix approach". The values below are now
authoritative for **desktop**. They supersede the desktop use of `color.neutral.bg` (#F8FAFC) and
`color.neutral.border` (#E2E8F0) in §2A. Mobile keeps its existing values unless the mobile
stream adopts these. The full build spec Figma AI reads is
`.agents/skills/figma-skill-cvfms-desktop/SKILL.md`, and it must match this section.

| Token / rule | Value |
|---|---|
| Viewport | **1440px** (240px nav rail + 1200px content). Existing 1776px frames are resized as each one is finalised |
| Page canvas | `#F4F6F8` |
| Card | `#FFFFFF`, 1px `#DFE5EB` on all 4 sides, 12–16px radius, shadow `0 1px 2px rgba(15,23,42,0.06), 0 1px 3px rgba(15,23,42,0.08)` |
| Card title row (P1) | title Lexend 16px/600 + time window 12px #64748B + exactly one exit link 13px/600 #006837 |
| Buttons | **pill, 20px radius**, 36–40px tall. Primary #006837 / white; secondary white + 1px #DFE5EB + #0F172A text |
| Search / filters | pill 20px radius, 1px #DFE5EB, leading outline icon |
| Table | header fill `#EBF1F7`, 36px, 12px uppercase #475569; rows 38–42px, dividers `#EEF1F4`, hover #F8FAFC; trailing "···" row action on hover; floating bulk-action pill when rows are selected |
| Status (3 tiers) | dot + text for live/active; plain #475569 text for normal states; pastel pill + icon only for exceptions |
| Empty state | one calm line ("All clear · …"), never an oversized empty card |
| Detail rows | semantic outline icon per §1.4.1 (non-swappable test) |
| Vehicle photo | 140px hero in drawers/detail panes; 40px thumbnail in tables |

**Still in force alongside Wix (from the desktop chat, `13_SYSTEM_MAP.md`):**
- The information budget.
- No boxes inside cards (stat tiles for read-only fact clusters excepted).
- Color marks only the exception.
- One active nav item.
- Decisions D1–D11 (`13` §11).

## 4. What Changed From v1.x (for anyone comparing against `docs/archive/`)

- Palette: navy-and-green combination is retained in spirit (green accent, navy/slate neutral) but hex values were independently re-derived from the `ui-ux-pro-max` color research rather than carried over — they land close to, but not identical to, the archived values. Treat the values in this document as authoritative.
- Typography: switched from the archived pairing to Lexend/Source Sans 3 (Corporate Trust), chosen specifically for reading-accessibility fit over general-purpose neutrality.
- Status Pill dimensions and the "never color alone" rule are retained from v1.x's Atlassian-sourced audit — that finding was independently re-confirmed by the fresh research pass (§0), so it survives the restart on its own merits, not by default.
- Chart policy (bar/line only, no decorative charts) is retained from v1.x's hard-won "decorative element" standard — again independently re-confirmed, this time by the chart domain's own data-type-matching logic rather than by project history.
