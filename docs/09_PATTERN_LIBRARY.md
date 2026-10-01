# CVFMS: Pattern Library — Fast Reference for Screen Assembly

**Document ID:** `DOC-CVFMS-009`
**Purpose:** This project is under real time pressure. This doc exists so that building screen 8, 9, 10 means *assembling proven patterns*, not re-deriving structure, re-running Mobbin searches, or re-negotiating decisions already settled on screens 1-7. Every pattern below is confirmed working (built and checked against a real render), not theoretical. When starting a new screen, start here — not at `03_MASTER_DESIGN_SYSTEM.md` or `04_FIGMA_SCREEN_BLUEPRINT.md`. Those remain the reasoning/traceability record (why a decision was made); this doc is the "how," optimized for speed.
**Depends on:** `03_MASTER_DESIGN_SYSTEM.md` (tokens), `04_FIGMA_SCREEN_BLUEPRINT.md` (per-frame specs), `06_DESIGN_QUALITY_PROCESS.md` (process rules — still apply, this doc doesn't replace them).

**Prompt length constraint lifted (2026-09-22) — the 2000-character Figma agent limit assumed since 2026-09-16 no longer applies.** Prompts can now be fully detailed and self-contained: spell out exact type sizes, colors, spacing, and structure directly rather than compressing into "reuse X's pattern, describe only the delta" shorthand. The reference-based habit built up while the limit was assumed (citing a prior screen by name instead of restating its values) is still fine as a *clarity* tool — it's genuinely useful to say "same button geometry as FRAME 7A's Decline" so the intent is unambiguous — but it's no longer a *length-driven requirement*, and prompts should default to being as detailed and explicit as the design actually calls for, not trimmed to fit a limit that isn't real. When in doubt, favor spelling out the exact value over a bare reference.

---

## 0. Component Sourcing — What to Build vs. What to Reuse

**Base primitives (buttons, inputs, badges, icons):** sourced from the **Untitled UI — PRO STYLES v6.0** community kit already attached to the file, restyled with CVFMS tokens (§2 of `03_MASTER_DESIGN_SYSTEM.md`). Checked directly (2026-09-14): Untitled UI's own page structure is `Badges`, `Inputs`, `Buttons`, `Tooltips`, `Icons`, `Logos`, `Misc icons` — genuine base primitives, no dashboard/table/composed patterns. Use its **Badge** component as the base shape for our Status Pill (restyle: icon+text rule, our 5 status colors, `radius.sm`); its **Button** component as the base for primary/secondary/ghost actions (restyle: Civic Green primary, our type tokens); its **Input**/textarea as the base for Action Drawer form fields (override justification, comments).

**Do NOT use:** Material 3, iOS/iPadOS/watchOS/visionOS/macOS kits, or the generic "Simple Design System" — all attached to the file but irrelevant (mobile-native or too generic), and using them risks accidental drag-and-drop of a wrong-styled component into a screen. Consider removing them from the file's library list to reduce that risk.

**Composed patterns (App Shell, Data Table, Kanban, KPI Row, Needs Attention list, Action Drawer, trend charts):** these are CVFMS-original — no generic kit has them, because they encode this project's specific personas, flows, and business rules. Build once, reuse via the patterns below; never re-derive from scratch on a new screen.

---

## 1. App Shell (every screen uses this, no exceptions)

**Left rail:** 240px, dark `#0F172A`, containing the county/system wordmark, the grouped nav (below), and a user/role indicator pinned to the bottom.

**SUPERSEDED 2026-09-15 — nav is now grouped into pillars, not a flat 20-item list.** Per product owner instruction (Patrick Swift): group menus/sub-menus into named pillars, plus a Settings group. Full reasoning and the module-to-pillar mapping is in `03_MASTER_DESIGN_SYSTEM.md` Component 1 — **"Operations" is an assumed 7th pillar, not product-owner-confirmed**, flag it back to them before treating it as final.

**MANDATORY — full grouped nav structure, every single prompt, no shorthand** (per `06_DESIGN_QUALITY_PROCESS.md` §0C — the flat list regressed twice from being referenced by shorthand; the grouped version needs the same discipline):

```
1. Operations — Vehicle Request, Vehicle Allocation, Dispatch Management, Journey Management
2. Vehicle Management — Fleet Registry, Insurance, Compliance, Disposal
3. Driver Management — Driver Management, Accident Management
4. Fuel Management — Fuel Management
5. Maintenance — Maintenance, Workshop Management, Stores/Spare Parts, Procurement
6. Tracking & Telematics — GPS/Telematics
7. Fleet Analytics — Reporting & BI, Vehicle Expenses
8. Settings — Administration, Audit
```

Each pillar is a collapsible group (accordion-style); each sub-item needs a visible **text label**, not icon-only (confirmed defect, seen twice on the old flat nav — icon-only sidebars are unreadable and must never ship). The pillar containing the screen's active module should be expanded by default; others may start collapsed. Exactly one sub-item is active/highlighted at a time — never two (confirmed defect on FRAME-04).

**Benchmarked (2026-09-15) against [Airwallex](https://mobbin.com/screens/d48ac37f-a457-4c73-b481-fe4157078dff), [Deel](https://mobbin.com/screens/b6d82ee0-8694-4f55-a1d5-9f0964c8b13c), and [Squarespace's Pages panel](https://mobbin.com/screens/d657756b-5458-405e-914a-090452b57efc) — all real, polished examples of this exact icon-rail-plus-expandable-group pattern.** What makes them read as "world class" rather than a generic accordion, specifically: (1) chevron rotates/changes direction on expand vs. collapse (down = open, right = closed), not a static icon; (2) sub-items are visually indented under their parent with a consistent left edge, not just smaller text; (3) **a thin vertical connector line runs down the left edge of the sub-item group, aligned under the parent's icon** — Squarespace's "Overview" group shows this clearly (one continuous line the full height of its children, About/Contact/Portfolio, not a separate line per row) — this is the detail most likely to get built half-heartedly (a line per row instead of one continuous one), so check it specifically; (4) icons live on pillar rows only — sub-items are text-only, keeping the nested list uncluttered; (5) the active sub-item gets a treatment visibly distinct from a merely-hovered/collapsed row; (6) typically one pillar expanded at a time, not several simultaneously. Apply all 6 whenever generating or fixing this sidebar — a grouped nav that skips these still reads as amateur even though it's structurally correct.

**Active-item treatment — confirmed as a rounded chip, not a left accent bar (2026-09-15, user comparison of Airwallex/Asana/Indeed sidebars).** Checked all three side by side: Asana (light sidebar) and Airwallex/Indeed (dark sidebars, closer to our own `#0F172A`) all converge on the same active-state pattern regardless of light/dark base — a soft, rounded background chip behind the active row (comfortable padding, not edge-to-edge, rounded corners matching `radius.md`), not a thin left accent bar. **Adopted: replace the left-accent-bar spec with this rounded-chip treatment system-wide.** Uses the new `color.brand.primary-subtle-dark` (`#173829`) token, added specifically for this — the existing `color.brand.primary-subtle` (`#E6F2EB`) is a light-surface tint and would read as a jarring bright rectangle against the dark `#0F172A` rail, so don't reuse it here. The base sidebar color itself stays `#0F172A` unchanged; this is scoped to the active-item indicator only.

**Top bar:** 56px, white, search field + notification bell + user avatar/menu.

**Page title slot — pick ONE of two forms, decided by screen type, not personal preference:**

| Screen type | Use this form | Screens using it |
| :--- | :--- | :--- |
| Once-per-session landing screen | Greeting block: date (small) → "Good [morning/afternoon/evening], [Name]" (large) → system-status line (small) | FRAME-01 (Grace's Overview) only |
| Repeated work-surface screen | Plain title + role/status subtitle: `"[Screen Name]"` / `"[Role]: [Name] • [Status line]"` | FRAME-02, FRAME-03, FRAME-04, FRAME-05, and any future work-surface screen |

Never mix both forms on one screen (confirmed defect — a duplicate title+greeting both rendering simultaneously). Never extend the greeting form to a new screen without checking it's genuinely a once-per-session landing page, not a repeated work surface.

**Prompt fragment (paste verbatim, adjust only the active item, expanded pillar, and title-slot content):**
```
APP SHELL
Left sidebar navigation grouped into these 8 collapsible pillars, in this order, each containing
its exact sub-items (verbatim — do not paraphrase, merge, or shorten):
1. Operations — Vehicle Request, Vehicle Allocation, Dispatch Management, Journey Management
2. Vehicle Management — Fleet Registry, Insurance, Compliance, Disposal
3. Driver Management — Driver Management, Accident Management
4. Fuel Management — Fuel Management
5. Maintenance — Maintenance, Workshop Management, Stores/Spare Parts, Procurement
6. Tracking & Telematics — GPS/Telematics
7. Fleet Analytics — Reporting & BI, Vehicle Expenses
8. Settings — Administration, Audit
The "[PILLAR NAME]" pillar should be expanded by default, with "[ACTIVE ITEM]" as the only
active/highlighted sub-item. Other pillars can start collapsed. Every sub-item needs a visible
text label next to its icon — never icon-only.
Top bar: search field, notification icon, user avatar/menu.
[TITLE SLOT — insert greeting block OR plain title + subtitle per the table above]
```

---

## 2. Two-Pane Work Surface (queue + detail)

**Decision rule — fixed pane vs. true overlay drawer** (this is the single most reusable judgment call in the system — apply it to every future two-pane screen without re-litigating):

| Persona's job shape | Pattern | Why |
| :--- | :--- | :--- |
| High-volume, rapid triage (pick next item, clear it, move on) | **Fixed side-by-side pane**, ~55/45 split, no dimming | Losing background-queue visibility costs real throughput — confirmed via Daniel's FRAME-02 |
| Low-volume, focused, deliberate investigation | **True overlay drawer** (dimmed background, slides in, close button) | Decision-focus is a net benefit when there's no queue to glance ahead at — confirmed via Miriam's FRAME-05 Anomaly Review |

**Fixed-pane prompt fragment:**
```
LEFT PANE (~55% width): [LIST NAME]
A data table with these columns: [COLUMNS]. Sortable, filter-chip row above (by [FILTERS]),
search field. Row click loads that item into the right pane, highlighted with a left-edge accent
bar on the selected row.

RIGHT PANE (~45% width): [DETAIL NAME]
A small, non-interactive context label above the panel title: "[Nav Item] → [Detail Name]".
[DETAIL CONTENT], with generous vertical spacing between each field/section group — don't pack
tightly. Bottom-anchored primary/secondary action buttons, clearly distinct from each other —
never style a pending/requested state identically to a pressable button.
```

**True-drawer prompt fragment:**
```
Clicking a row opens a TRUE OVERLAY DRAWER: the list behind it dims, the drawer slides in from
the right covering roughly the right half of the screen, with a visible close (X) button top-right.
A small, non-interactive context label near the top: "[Nav Item] → [Detail Name]".
[Hero figure or headline value] near the top, then a clean row of smaller labeled fields, then
[supporting content], then a comments/notes field if relevant. At the very bottom of the drawer,
anchored there: [N] decision buttons, clearly distinct from each other.
```

**Confirmed defect to check every time:** the pane width ratio has drifted to 68/32 or worse on at least one screen — always verify the actual rendered ratio against the ~55/45 spec, don't trust that it "looks about right."

---

## 3. KPI / Stat Row

**DEFAULT SIMPLIFIED (2026-09-16, benchmarked against [Airwallex](https://mobbin.com/screens/adfc8a85-a15c-4405-b9ef-7136e216adba) and [Uxcel](https://mobbin.com/screens/51ce5df6-f6d9-49b5-a96d-f47a1c9df99b) — both chosen by the user as "incredibly simple but well designed"):** default KPI tile is plain — label + number, nothing else. No colored dot, no delta chip, no icon, by default. Both references use flat black numbers with a single accent color reserved for buttons/links only — our prior default (a colored delta chip on every tile) was more decoration than either reference actually uses.

**Delta chip is now opt-in, not default** — only add one when the specific number's meaning genuinely depends on a comparison (e.g. Sarah's "Fleet Availability 89%, target: 85%" — the whole point of that number is above/below target). Name it explicitly in the prompt when needed; don't assume it automatically.

**Two variants:**
1. **Plain KPI Tile** — label → value, nothing else by default. Can be used in a merged "Fleet Status Row" where each card's sub-line is a clickable link into a matching list below it (the Jobber-style merge — confirmed working on FRAME-01).
2. **Large Executive KPI Tile** — same shape, `type.metric-large`, used on FRAME-04 — this is the one case where a target/comparison is named explicitly, since the number is meaningless without it.

**Confirmed recurring defect from the old default — still worth checking if a delta IS used:** delta indicators rendered as a bare colored `Ellipse`/dot with no text or icon sibling (happened on both FRAME-01 and FRAME-04 under the old spec). If you do add an opt-in delta, it still must pair with text/icon, never color alone.

**Card separation defect (found 2026-09-16 on rendered Driver Management and All Vehicles screens):** KPI tiles and table rows blended into the page background — the `#FFFFFF` card vs `#F8FAFC` page tokens are correct but only ~3% apart, too subtle to read once rendered without a border. **Every KPI tile needs a visible 1px border (`color.neutral.border`) on all sides** — don't rely on background-color difference alone. See `03_MASTER_DESIGN_SYSTEM.md` Component 2 for the full rule, and Component 6 for the matching Data Table fix.

**Prompt fragment:**
```
KPI ROW — [N] cards, equal width, plain: label + number only, no colored dots, no delta chips,
no icons. Each card has a visible 1px border (light gray) on all sides, white fill, rounded
corners — must read as a distinct card against the page background, not just a color-tinted
rectangle. [ONLY IF a specific number needs a comparison to be understood: name that one delta/
target explicitly, e.g. "Fleet Availability — 89%, target: 85%".]
[If this is a merged Fleet-Status-style row: each card's sub-line should read as a link into the
matching rows in [LIST NAME] below it.]
```

---

## 4. Status/Action List ("Needs Attention" pattern)

Urgency-grouped list, NOT a data table (no column headers). Each section label carries its own row count (e.g. "OVERDUE (2)"), confirmed as a real scanability improvement via [Linear](https://mobbin.com/screens/610d34b6-6ad8-45ab-80fb-2107b31ed01e)/[Asana](https://mobbin.com/screens/6dddad98-49dc-4980-98f6-866b498f3b02). Each row: one dominant identifier, one line of context, a status indicator (icon+text, never color alone), a direct action button scoped to what that specific row needs (vary the verb — Reallocate/Approve/Override/Edit, not one generic "View" button repeated).

**Prompt fragment:**
```
[PANEL NAME]: a list grouped under section labels that include their own row count (e.g.
"Overdue (2)", "This Week (2)") — not a data table, no column headers. Each row: an identifier
(the main thing to read), one line of context below it, a status indicator distinguishable by
more than color alone, and an action button scoped to what that row specifically needs (vary
the action verb across rows).
```

---

## 5. Kanban Board (state-machine-driven, not freeform)

Columns represent a real, non-arbitrary sequence (never allow free drag-and-drop between any two columns — the underlying flow has illegal transitions). Each card: dominant identifier, assigned person, a relevant status tag, and an age-in-column indicator (confirmed pattern via [ClickUp](https://mobbin.com/screens/0c287f59-753c-4e28-92ad-9dff95fcde36)). The terminal column's completion action is disabled until a sub-checklist is satisfied — this is the same "gated action" pattern as the two-pane Dispatch Gate (`06_DESIGN_QUALITY_PROCESS.md` §3), reused, not reinvented.

**Prompt fragment:**
```
[N]-COLUMN KANBAN, in this exact order: [COLUMN 1] | [COLUMN 2] | ... 
Each card: [identifier] (dominant), [assigned person] (secondary), a status tag for [relevant
sub-item], and a relative age indicator (e.g. "2 days") showing how long it's been in this column.
[TERMINAL COLUMN]'s completion action is disabled by default until [GATING CONDITION] is met —
show this disabled state with a visible reason why.
```

---

## 6. Data Table (full registry / log views)

Sortable columns, filter-chip row above (2-3 filters max — match the filter count to what the data actually needs, don't add filters speculatively), search field, pagination for large datasets. A quick status-breakdown summary strip above the table is a confirmed useful addition when the dataset represents a countable inventory (e.g. "247 vehicles — 198 Available, 37 On Trip...") — via [Deel's Assets registry](https://mobbin.com/screens/27f3bda0-f620-443a-b3c6-61a87141e9c5). Show urgency as text in date/expiry columns ("Overdue by 3 days"), not just a raw date — via [Employment Hero](https://mobbin.com/screens/47d85c21-a910-407a-b9e3-c85ac7dd6430).

**Card separation defect (found 2026-09-16, same root cause as §3 above):** rendered tables (Driver Management, All Vehicles) had rows sitting directly on the page background with no visible container — the table needs its own bordered card, not just a header underline. See `03_MASTER_DESIGN_SYSTEM.md` Component 6.

**Prompt fragment:**
```
[STATUS BREAKDOWN BAR — only if the table represents a countable inventory]: a summary strip
above the table showing total count and a quick breakdown, e.g. "[N] total — [breakdown]".

FILTER ROW: [2-3 filters matching the data], plus a search field. Each filter is its own bordered
pill/dropdown control, not bare text.

[TABLE NAME] — the whole table sits inside one card: white fill, visible 1px border on all sides,
rounded corners — must read as a clearly bounded surface against the page background, not rows
floating on the page. Sortable columns: [COLUMNS]. Header row has a faint tint distinct from the
white data rows. Row dividers: thin light-gray lines between rows. For any date/expiry column,
show urgency as text where relevant ("Overdue by N days" / "Expires in N days"), plain date
otherwise. Include [N] sample rows with realistic Kenyan county data. Pagination below the table
if the real dataset is large. Each row: a "View"/"Quick view" action indicating more detail is one
click away.
```

---

## 7. Recent Activity / Audit Log

Full width, lowest visual priority on its page, scoped to **exceptions only** (overrides, anomaly flags, rejections) — never a routine chronological feed of every action. Each row: timestamp, a **distinct actor field** (who — "Grace Wanjiru" or "System," never folded into the description prose), then the description. This is audit-trail content (SRS §8, BR-009 both treat "who" as core data) — the actor field is not optional polish, it's the confirmed fix for a real defect found via [1Password's Activity Log](https://mobbin.com/screens/84dbef44-916b-4322-956f-154845c224a7).

**Prompt fragment:**
```
[LOG NAME] — full width, lowest visual priority on the page. A list of exception/override events
only (not routine activity). Each row has three distinct parts: a timestamp, an actor (who did
it — a name, or "System" for automated events), and a one-line description. No actions on these
rows — this is a passive log.
```

---

## 8. Trend / Comparison Charts

Only two chart types exist in this system: **line** (trend over time) and **bar** (category comparison). No radar/gauge/donut/heatmap, ever (`03_MASTER_DESIGN_SYSTEM.md` Component 8) — this has been independently re-confirmed twice and is not up for reconsideration per-screen. A trend chart against a target gets a visible reference line (e.g. the 85% availability target line) — this is a confirmed pattern, not decoration, per the decorative-element test (names a specific decision the line changes: "is the fleet above or below target right now").

**Confirmed recurring defect:** orphaned/disconnected data points at the start of a line chart (seen on FRAME-04's twin trend charts) — always check every point connects into one continuous line before accepting a chart render.

**Prompt fragment:**
```
[CHART NAME] — a line chart showing [metric] over [period]. [If against a target: add a
horizontal reference line at [target value] so it's visually clear when the metric is above or
below target.] Ensure every data point connects into one continuous line — no floating/
disconnected markers.
```

---

## 9. Drill-Down (inline expand, never navigate away)

For any low-frequency, read-only persona (Sarah's pattern), a drill-down expands **in place** — the same screen, the clicked element's detail appears inline below/beside it — never a navigation to a new page. Confirmed via [Twenty CRM](https://mobbin.com/screens/4ed9c91a-c71a-44d6-8279-defff70a6ce3). Prefer a visual selected-state cue (highlighted/bordered row) over permanent instructional copy explaining the interaction — instructional text as a fixed subtitle is a flagged anti-pattern, not yet fully resolved (see FRAME-04's "Click a department..." caption).

**Prompt fragment:**
```
[CHART/LIST NAME] — clicking [an item] expands its detail inline (the chart/list area itself
grows to show it), not a navigation to a different page or screen. Show one item in this expanded
state so the interaction is clear. Indicate the selected item with a visual cue (border/highlight)
rather than instructional text explaining how to interact with it.
```

---

## 10. Breadcrumb / Context Label Scope

**No breadcrumbs anywhere except genuine drill-down detail views** (queue → one selected item's detail). This system's nav is flat (20 top-level modules, no nested groups) — a breadcrumb on a top-level screen or a tab row would be circular or would falsely imply a folder structure that doesn't exist. Where it IS used: a plain, non-interactive text label (not a clickable crumb) reading `"[Nav Item] → [Detail Name]"`, placed above the detail panel's heading. Already applied to: FRAME-02's Request Details, FRAME-03's Job Card Detail, FRAME-05's Anomaly Detail. Apply the same pattern to any future detail panel without re-deciding the question each time.

---

## 11. Loading, Empty, and Error States — DEPRIORITIZED (2026-09-16, user instruction)

**User instruction (2026-09-16): keep designs simple, avoid adding things like skeleton loading states.** This section was added per `10_DASHBOARD_DESIGN_KNOWLEDGE.md` §2.1-2.3 as a recommendation from external research, not something the user asked for — the user has since directed the opposite: don't fold loading/empty/error-state specs into new prompts by default, since it adds complexity beyond what's actually been requested. **Do not include the prompt fragment below in new screen prompts going forward.** Kept here only as a reference in case the user asks for it explicitly on a specific screen later — do not treat it as a standing checklist item (§12 below has been updated to remove it from the pre-flight list).

Original reasoning (for reference only, not currently actioned): a skeleton gives spatial context a spinner doesn't; an empty state should explain + prompt one action rather than show a blank chart; an error state should name the cause and the recovery action rather than say "Something went wrong."

**Prompt fragment (add to any new screen prompt where relevant):**
```
For [COMPONENT], also specify: a loading state (a skeleton placeholder shaped like the component
itself — gray rounded blocks where the real content will appear — not a spinner), an empty state
(if there's no data yet, a short explanation plus one specific action, not a blank chart), and an
error state (if data fails to load, state what's known about the problem and one recovery action
— never a generic "Something went wrong").
```

---

## 12. Pre-Flight Checklist for Every New Screen (condensed from `06_DESIGN_QUALITY_PROCESS.md`)

Before writing a prompt for a new screen, confirm:
1. Which App Shell title-slot form applies (§1 table above) — landing vs. work-surface.
2. Full 8-pillar grouped nav structure pasted verbatim into the prompt, not referenced by shorthand — including which pillar is expanded by default for this screen.
3. If it's a two-pane screen: fixed vs. drawer decided per the persona's job-shape (§2 table).
4. Every status indicator pairs an icon/text with its color — never color alone.
5. Every KPI delta has a text/icon label, not a bare colored dot.
6. Chart type is bar or line only, and passes the decorative-element test (names a decision it changes).
7. Any drill-down expands inline; any detail view gets a context label per §10, not a full breadcrumb.
8. Recent Activity / log content is exceptions-only with a distinct actor field, if the screen has one.
9. Keep it simple — per user instruction (2026-09-16), don't add loading skeletons, empty states, or error states unless explicitly asked for on that specific screen (see §11).
10. Every card-shaped surface (KPI tile, data table, panel) has a visible 1px border — never rely on the white-card/page-background color difference alone to read as separated (found missing on rendered screens 2026-09-16; see §3, §6, `03_MASTER_DESIGN_SYSTEM.md` Components 2 and 6).
11. No raw rule identifiers in UI: Do NOT show raw spec codes (e.g. "BR-001–005") to end users. Always use clear, human-readable labels: "Dispatch Readiness (4/5 checks passed)", "Insurance Policy Active", "Driver Licensed & On Duty", "Vehicle Availability" (locked 2026-09-18).
12. Configurable approval terminology: Approval copy must not assume every requisition is a financial budget check. Distinguish between routine "Operational Authorization / Pool Dispatch" and funded "Budget Commitment / Project Vote" travel (locked 2026-09-18).
13. Driver journey bookending: Any mobile driver flow must bookend both beginning and completion of a job: initial odometer capture & inspection checklist at Start, closing odometer capture & distance calculation at End (locked 2026-09-18).

If a screen fails any of these after its first render, fix it via a single-issue follow-up prompt (or a small combined batch of independent, non-colliding issues) — don't re-derive the pattern from scratch each time it recurs.

---

## 13. Driver Mobile Flow Pattern (390px Native PWA)

**Superseded 2026-09-22 — the fragment below described the pre-rebuild single-card Home model and
is no longer accurate.** FRAME-07's Home screen (7A) was rebuilt as an urgency-ordered assignment
list (not one hero card), SOS was removed entirely (replaced with a notification icon, no SRS
grounding existed for SOS), and the touch-target minimum was corrected to 44px, not 48px. **Do not
copy-paste FRAME 1 below** — for Home, use Component 9 (`03_MASTER_DESIGN_SYSTEM.md`) and FRAME 7A
(`04_FIGMA_SCREEN_BLUEPRINT.md` §8) instead, both exact/locked and current as of 2026-09-22. FRAME 2
(Walkaround Checklist) and FRAME 3 (Start/End bookends) below are directionally still correct but
not yet locked to the same exactness as Component 9 — treat as a rough starting sketch, not a
closed spec, and check `04_FIGMA_SCREEN_BLUEPRINT.md` §8's FRAME 7B/7C sections for the latest
detail (including FRAME 7C's State 1.5 "Active Trip," missing from the sketch below) before using.

For the Driver mobile application (`04_FIGMA_SCREEN_BLUEPRINT.md` §8), use this reference fragment. Touch targets must be 44px+ minimum, layout optimized for outdoor daylight legibility and one-handed thumb interaction:

```
VIEWPORT: Mobile Native 390×844 (iPhone 15 / Android PWA). Light background, high-contrast cards.
TOP BAR: see Component 9's collapsing header spec (avatar, greeting/name, notification icon,
county branding) — not the old "Offline Ready" sync badge, which was never built.

FRAME 1 (Home): use Component 9 / FRAME 7A instead — urgency-ordered list (Needs Your Response →
Scheduled → Ready), not a single hero card. See those docs for the exact, current spec.

FRAME 2: WALKAROUND INSPECTION CHECKLIST
- 4 Large binary tap-targets (Pass/Fail toggle with green checkmark when passed):
  1. Tyres & Spare Wheel [PASS]
  2. Lights & Indicators [PASS]
  3. Engine Fluids & Coolant [PASS]
  4. Safety Kit & Fire Extinguisher [PASS]
- Defect photo capture: camera icon on each row, revealed only when that row is marked Fail (not
  one blanket photo-attach action below the list) — confirmed via Lime's damage-report pattern,
  `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`'s FRAME-07 section.
- Banner: "No pre-existing defects logged. Clear for departure."
- Primary CTA: "Confirm Inspection & Proceed →" (Civic Green).

FRAME 3: START & END TRIP LIFECYCLE BOOKENDS
- Start State:
  - Starting Odometer input: Bold text display "142,850 km" + [📸 Photo Verified] pill.
  - Fuel Gauge Pill: "75% (3/4 Tank)".
  - Disclaimer: "Starting trip enables automated GPS tracking to county dispatch."
  - Primary CTA: "Start Journey Now" (Civic Green).
- **Active Trip state (State 1.5, missing from earlier versions of this fragment)**: stage
  indicator ("Stage 2 of 3 · In Transit"), persistent banner ("In Transit to [destination] •
  Started [time]"), two equal-weight outline-chip actions (Log Fuel Stop / Report Breakdown —
  Defect), primary CTA stays "Complete Trip & Record Closing Odometer" throughout.
- End State:
  - "In Transit to Nakuru Sub-County Office".
  - Closing Odometer input: "142,914 km" -> Auto-calculated distance: "64 km traveled".
  - Defect check: "Any mechanical defects during trip? [None / Report]".
  - Primary CTA: "Finalize & Close Trip" (Releases vehicle back to available pool).
```

