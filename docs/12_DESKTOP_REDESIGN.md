# CVFMS: Desktop Redesign — Bringing the 9 Desktop Screens up to the Refined Design Language

**Document ID:** `DOC-CVFMS-012`
**Started:** 2026-09-24
**Why a separate doc:** desktop and mobile are now being worked in two parallel chats. Keeping desktop
prompts and render checks here avoids edit collisions in `08_PROJECT_HANDOVER.md`. Fold a summary
back into the handover once the redesign pass is complete.

**Figma file:** `bnxWZCzNtbjM0ulb886hXo`, page **"Refined"** (`302:456`) — not "Page 1". Page 1 holds
older copies; all current work (desktop screens, desktop component library, refined mobile screens)
lives on "Refined".

**Method (user decision, 2026-09-24):** Figma AI agent prompts (same workflow as mobile), run on
**duplicates** of the current screens placed in a new "Desktop v2" row. Originals stay untouched for
side-by-side comparison and rollback.

**NEXT AGENT, START HERE (2026-09-24):**
- Read `13_SYSTEM_MAP.md` first (templates, patterns, components, connections, audit method).
- Then read §2 below for status, and the latest sections (§8i Today, §10 Requests) for where work
  stopped.
- Handover summary: `08_PROJECT_HANDOVER.md` §25.

---

## 1. Audit of the current desktop screens (2026-09-24)

Screens on "Refined" (all 1776px wide, built on `Layout/Page Shell` = `Navigation/Sidebar` + `Top Bar`):

| Node | Screen | Notes |
|---|---|---|
| `338:5039` | fleet-operations-overview (FRAME-01, Grace) | Map preview still has AI artifact text ("Avaliable / fleet on trips") |
| `338:5212` | dispatch-requisition-queue (FRAME-02, Daniel) | Gate logic defect (below) |
| `338:5368` | finance-cost-dashboard (FRAME-05, Miriam) | |
| `338:5504` | workshop-job-card-board (FRAME-03, Peter) | |
| `338:5811` | executive-briefing (FRAME-04, Sarah) | Placeholder identity; chart points float off lines |
| `338:5981` | fleet-all-vehicles | |
| `338:6173` | fleet-live-map (FRAME-06) | Never render-checked |
| `338:6386` | dispatch-override-review (Grace modal 2C.1) | |
| `338:7511` | driver-management-registry | Loosest build: 22% of fills token-bound, Roboto mixed in, duplicate nav item |

Desktop component library on the same page: `Layout/Page Shell`, `Navigation/Sidebar` (8 variants),
`Top Bar`, `KPI Tile`, `Status Pill` (5), `Data Display/Status Row` (4), `Data Display/Alert Card` (3),
`Data Display/Section Card`, `Data Display/Summary Field Grid`, `Data Display/Status Breakdown Bar`,
`Navigation/Tab Item`, `Controls/Filter Dropdown`, `Data Display/Table Header Cell`,
`Data Display/Table Data Cell`, `Checklist Row` (Pass/Fail). Variables: CVFMS Colors (19),
Spacing (8), Radius (4). Text styles: 9, all Inter.

**Gaps, ranked:**
1. **Typography.** Every desktop screen and every text style is Inter. The spec
   (`03_MASTER_DESIGN_SYSTEM.md` §2 type table) is Lexend (headings, metrics) + Source Sans 3 (body,
   labels) — and the refined mobile screens already use it. Biggest single visual gap.
2. **The "simple is not sterile" corrections (handover §21–22) never reached desktop:** vehicle
   photos as ordinary content, tinted info cards for contextual notices, small purposeful icons on
   informational rows, Stat Tiles for genuine fact clusters.
3. **Placeholder / wrong content:** "Date label" and "User / Fleet Manager" on Executive Briefing
   and Driver Management (breaks the locked name + role-title rule); Driver Management sidebar lists
   "Driver Management" twice, first with a truck icon; FRAME-01 map artifact text.
4. **Behavior defects:** Dispatch Queue shows Vehicle Availability FAIL while "Authorize Dispatch"
   is still an enabled green button, and the override field + red "Force Dispatch" are always
   visible — contradicts the blueprint (any fail → Authorize disabled; override field only opens
   from Request Override). Executive Briefing chart dots don't sit on their lines.
5. **Weak component discipline on Driver Management** (see table).

**Known side effect of Prompt 0:** updating fonts on the shared components (Sidebar, Top Bar, KPI
Tile, Status Pill, etc.) also changes their instances inside the *original* screens. That's
intended — the originals still preserve old layouts for comparison; only the type updates everywhere.

---

## 2. Execution order and status (updated 2026-09-24, end of first desktop session)

| # | Item | Status | Where |
|---|---|---|---|
| 0 | Foundation: v2 row + Lexend/Source Sans 3 on styles/components | Written; not confirmed run. v3 renders already show the new fonts | §3 |
| 1 | Dispatch Queue v2 (FRAME-02) | Old prompt §4 **superseded**. Old render audited (§4a, §9). **§9a prompt on hold**: waiting for the user's updated Dispatch render; trim §9a to what's still wrong | §9 |
| 2 | **Today / Fleet overview (T1)** | **Near-locked.** Frame `v3 / fleet-operations-overview` (+ `/group-expanded`). Last render (§8i) needs the §8i polish prompt + 2 direct `use_figma` fixes (fuel anomaly icon → flag; stray divider under "2 anomalies") | §8–8i |
| 3 | **Vehicle requests (T3)** | Live-app page audited (§10); simplified structure (§10b); **prompt ready (§10c)**, not yet run | §10 |
| 4 | Dispatch Override Review (T8) | Not started | — |
| 5 | Executive (FRAME-04), Finance (FRAME-05), Workshop (FRAME-03), All Vehicles + Driver Mgmt (T3), Live Map (T6) | Not started. Audit each with `13` §7 as the user shares live-app pages | — |
| 6 | Missing destinations: Compliance, Fuel Management, Vehicle detail (T7), Audit Trail, Live alerts queue, GPS events register, Renew-insurance drawer | Not designed | `13` §5, §6b |
| 7 | Build new Figma components (Pipeline Segment, Exception Group Row, Approval Row, Watch Line, Pace Bar, Scope Switcher, Freshness Stamp, Vehicle Row, Decision Footer) directly via `use_figma` | Not started; **needs Figma MCP re-auth (`/mcp`)** | `13` §4 |

---|---|---|
| 0 | Foundation: Desktop v2 row + Lexend/Source Sans 3 on text styles and components | Ready |
| 1 | FRAME-02 Dispatch Queue v2 (2 states: gate blocked / override open) | Ready |
| 2 | FRAME-01 Fleet Overview v2 | Not written |
| 3 | Dispatch Override Review v2 | Not written |
| 4 | Executive Briefing v2 | Not written |
| 5 | Finance v2 | Not written |
| 6 | Workshop v2 | Not written |
| 7 | All Vehicles + Driver Management v2 | Not written |
| 8 | Live Map v2 | Not written |

FRAME-02 goes first: it's the center of the 6-stage demo (Requester → Approver → **Transport Ops** →
Driver → Fleet Ops → Auditor) and has the most real defects.

---

## 3. Prompt 0 — Foundation

```
On the page named "Refined", do the following. Do not change any layout, spacing, color, or
content — this is a typography and file-organization pass only.

1. CREATE A "DESKTOP V2" ROW.
   Duplicate these 9 desktop screen frames: fleet-operations-overview, dispatch-requisition-queue,
   finance-cost-dashboard, workshop-job-card-board, executive-briefing, fleet-all-vehicles,
   fleet-live-map, dispatch-override-review, driver-management-registry. Place the copies in one
   horizontal row directly BELOW all existing content on the page (leave at least 400px clear
   space above the row), same left-to-right order, 120px gap between frames. Rename each copy with
   a "v2 / " prefix, e.g. "v2 / dispatch-requisition-queue". Add a text label "DESKTOP V2" (24px,
   bold) 80px above the first frame. Do not modify the original frames.

2. UPDATE THE TEXT STYLES to the CVFMS type pairing — Lexend for headings and numbers, Source Sans 3
   for everything else. Keep each style's existing size, line height and weight unless listed:
   - Page Title → Lexend, 24px / 32px line height, weight 600 (SemiBold)
   - Section Header → Lexend, 18px / 26px, weight 600
   - Metric Large → Lexend, 28px / 34px, weight 700
   - Metric Medium → Lexend, 24px / 30px, weight 600
   - Metric Small → Lexend, keep size, weight 600
   - Body Primary → Source Sans 3, 14px / 22px, weight 400
   - Body Secondary → Source Sans 3, keep size, weight 400
   - Meta Badge → Source Sans 3, 12px / 16px, weight 600, uppercase, letter spacing +2%
   - Micro Eyebrow → Source Sans 3, 12px / 16px, weight 600, uppercase, letter spacing +4%

3. UPDATE THE COMPONENTS so every text layer inside them uses Lexend (for titles, KPI values and
   the CVFMS wordmark) or Source Sans 3 (for everything else — nav labels, body, pills, table
   text, buttons, captions). Components: Navigation/Sidebar (all 8 variants), Sidebar/Collapsed,
   Top Bar, KPI Tile, Status Pill (all 5), Data Display/Status Row, Data Display/Alert Card,
   Data Display/Section Card, Data Display/Summary Field Grid, Data Display/Status Breakdown Bar,
   Navigation/Tab Item, Controls/Filter Dropdown, Data Display/Table Header Cell,
   Data Display/Table Data Cell, Checklist Row. Where a text layer can use one of the text styles
   above, apply the style rather than setting the font directly.

4. In all 9 "v2 / " frames only, replace any remaining Inter or Roboto text that is NOT inside a
   component instance with the same rule: Lexend for page titles, card/section titles and big
   numbers; Source Sans 3 for everything else. Apply the matching text style where one fits.

5. Update the "Type Scale — CVFMS" specimen frame so its rows show the new fonts, and change its
   subtitle from "Inter · 7 sizes · 4 weights · 17 styles" to "Lexend + Source Sans 3".
```

**Check after render:** (a) originals untouched apart from fonts inside component instances;
(b) no text overflow/clipping — Source Sans 3 runs slightly narrower than Inter, Lexend slightly
wider, so watch KPI values, sidebar labels and the Top Bar identity pill; (c) zero Inter/Roboto left
in the v2 row.

---

## 4. Prompt 1 — FRAME-02 Dispatch Queue v2

Grounding: blueprint FRAME-02 (`04_FIGMA_SCREEN_BLUEPRINT.md` §3); handover §11 (human-readable
checks, no raw BR codes) and §21–22 (vehicle photo, tinted notice card, purposeful icons, stat
tiles). Demo data: `REQ-2024-0851`, Mary Akinyi / Public Works → Nakuru Sub-County Office, vehicle
KBZ 442A Toyota Land Cruiser, driver Joseph Mutua.

```
Work on the frame "v2 / dispatch-requisition-queue" on the "Refined" page. Keep the app shell
(Navigation/Sidebar instance with Operations expanded and "Dispatch Management" active, Top Bar
instance), the two-pane layout (queue left ~58%, detail pane right ~42%, 24px gap, both panes
white cards with 1px #E2E8F0 border, 12px corner radius, on the #F8FAFC page background) and all
existing requisition data. Fonts: Lexend for titles and numbers, Source Sans 3 for everything else.
Colors only from: #006837 (primary green), #00522C (green hover), #E6F2EB (green tint), #0F172A,
#334155, #64748B, #E2E8F0, #F8FAFC, #FFFFFF, #059669/#ECFDF5 (success), #B45309/#FFFBEB (warning),
#B91C1C/#FEF2F2 (critical).

HEADER: Title "Dispatch & Requisition Queue" (Lexend 24px/600, #0F172A). Subtitle below:
"Transport Operations: Daniel Otieno • 6 requests awaiting dispatch" (Source Sans 3 14px, #64748B).
Remove the green "online" dot. Top Bar identity must read "Daniel Otieno" with
"Transport Operations Officer" beneath it.

LEFT PANE — INCOMING REQUISITIONS
- Card title "Incoming Requisitions" (Lexend 18px/600) with a count to its right: "6" in a small
  neutral pill (#F8FAFC bg, #334155 text, 12px/600). Keep the three Filter Dropdowns
  (Department, Status, Date) below the title.
- Table columns: REQUEST (requester name 14px/600 #0F172A, beneath it "Public Works ·
  REQ-2024-0851" 12px #64748B), DESTINATION, REQUESTED (date), STATUS (Status Pill, right aligned).
  Header cells 12px/600 uppercase #64748B on #F8FAFC. Row height 64px, 1px #E2E8F0 dividers.
- Status pills must be tinted chips with a leading icon, not text alone: Approved = check icon,
  #059669 text on #ECFDF5; Pending = clock icon, #B45309 on #FFFBEB; Ready = arrow-right icon,
  #006837 on #E6F2EB. 6px radius, 12px/600 text, sentence case ("Approved", not "APPROVED").
- Selected row (Mary Akinyi, REQ-2024-0851): #E6F2EB background plus a 3px #006837 bar on the
  row's left edge. Only this row is selected.

RIGHT PANE — REQUEST DETAIL (top to bottom, 24px padding, 24px between sections)
1. Context label "Dispatch Management → Request Detail" (12px/600 uppercase, #64748B), then title
   "REQ-2024-0851" (Lexend 18px/600 #0F172A) with "Approved" status pill on the same line, right.
2. VEHICLE CARD: a 1px #E2E8F0 bordered row, 12px radius, 12px padding. Left: a 72×56px photo of a
   Toyota Land Cruiser (reuse the same vehicle photo already used on the mobile "Start Journey"
   screen on this page), 8px radius. Right of it: "Toyota Land Cruiser" (Lexend 16px/600 #0F172A),
   beneath it "KBZ 442A · Nakuru HQ Yard, Bay 4" (14px #64748B). Far right: Status Pill
   "Grounded" (alert-triangle icon, #B91C1C on #FEF2F2).
3. TRIP FACTS as plain label/value rows (label 13px #64748B on the left, value 14px/600 #0F172A on
   the right, 12px between rows): Requester — Mary Akinyi · Public Works; Destination — Nakuru
   Sub-County Office; Departure — Today, 10:30 AM; Driver — Joseph Mutua. Put a small 16px icon
   (#64748B) before each label: user, map-pin, clock, steering-wheel/id-card.
4. DISPATCH READINESS: section label "DISPATCH READINESS" (12px/600 uppercase #64748B) and on the
   same line, right: "4 of 5 checks passed" (13px/600 #B45309). Below, the 5 checks as Checklist
   Row instances, each with an icon + text result (never color alone):
   Insurance Policy Active — Pass; Driver Licensed & On Duty — Pass; Driver Licence Class Valid
   (Class A, B, C1) — Pass; Vehicle Availability — Fail; Approved Requisition Linked — Pass.
   Pass = green check icon + "Pass" chip (#059669 on #ECFDF5). Fail = red x icon + "Fail" chip
   (#B91C1C on #FEF2F2), and under the Vehicle Availability label the reason in 13px #B91C1C:
   "KBZ 442A is grounded for maintenance (brake pads) since Sep 11".
5. BLOCKED NOTICE: a tinted card, #FEF2F2 background, 1px #FECACA border, 8px radius, 12px padding,
   alert-triangle icon #B91C1C on the left, text 14px #334155: "Dispatch is blocked until every
   check passes. You can request an override — it will be logged to the audit trail."
6. ACTIONS pinned to the bottom of the pane, full width, 12px apart:
   - "Authorize Dispatch" primary button — DISABLED state: #E2E8F0 background, #64748B text,
     no shadow, 44px tall, 8px radius, Source Sans 3 15px/600.
   - "Request Override" secondary button — enabled: white background, 1px #006837 border,
     #006837 text, same size.
   REMOVE the always-visible override justification field and the red "Force Dispatch" button
   from this state.

SECOND STATE — duplicate the finished frame, place it 120px to the right, name it
"v2 / dispatch-requisition-queue / override-open". In the copy only, replace the ACTIONS block
with an expanded override panel (it appears after Daniel clicks Request Override):
- Panel: white, 1px #E2E8F0 border, 12px radius, 16px padding.
- Label "Override justification" (14px/600 #0F172A) with "Required · logged to audit trail"
  (12px #64748B) beside it.
- Multi-line text field, 96px tall, 1px #334155 border (focused), 8px radius, containing:
  "Urgent medical supply delivery — maintenance rescheduled to tomorrow, brake pads replaced
  yesterday."
- Below the field, a small line 12px #64748B: "Requires approval from Grace M., County Fleet
  Manager. You cannot approve your own override."
- Buttons side by side, right aligned: "Cancel" (text-only, #334155) and "Submit for Approval"
  (primary, #006837 background, white text). No red "Force Dispatch" button anywhere.
- "Authorize Dispatch" stays visible above the panel, still disabled.
```

**Check after render:** Authorize Dispatch visibly disabled in state 1; no override field or red
button in state 1; vehicle photo present and not stretched; exactly one selected row; pills
sentence-case with icons; Top Bar identity = Daniel Otieno / Transport Operations Officer;
"Submit for Approval" (not self-authorizing) in state 2 — the maker-checker rule from handover §11.

**Design decision recorded:** the override now routes to Grace for approval instead of Daniel
force-dispatching directly. This follows the locked "strictly no self-approval" rule (handover §11,
PFM Act 2012), and it connects FRAME-02 to the existing `dispatch-override-review` screen (Grace's
modal 2C.1), which is exactly where that approval lands.


### 4a. Render check — Dispatch Queue (2026-09-24)

The render doesn't follow Prompt 1's layout: the queue is stacked cards, not a table, and the demo
data is different (REQ-2024-0892, Mombasa → Kilifi, KCB 456K). It's reviewed on its own merits.

**Landed well:**
- Identity is Daniel Otieno.
- Status filter chips: All / Pending / Approved / Ready to Dispatch / Flagged.
- Approval provenance line: "Approved by James Mwangi (HOD) on 24 Sep".
- Assigned vehicle and driver have "Change" actions.
- Confirm Dispatch is disabled, with an explanation.
- The override field is no longer always visible, and there's no red Force Dispatch button.

**Findings:**
1. **Gate logic is wrong (highest).** The only non-pass check is a WARNING (insurance expires in 4
   days, and the trip is tomorrow), yet dispatch is blocked. A warning should inform, not block.
   There are also 6 checks where the spec has 5, because insurance appears twice ("Insurance
   Policy Active" PASS + "Insurance Certificate — expires in 4 days" WARNING).
2. **The queue is cards, not rows.** Each request takes a ~150px card, so 5 of 14 are visible.
   Daniel's goal is throughput across a high-volume queue, so he needs compact rows he can scan
   and compare.
3. **Density breaches (§7):**
   - Every card carries two chip systems: status plus a "Routine" priority chip. "Routine" on
     every card is noise; show only "Urgent".
   - Pass checks carry both a green icon and a PASS chip.
   - The blocked state is said twice: the amber banner and the red sentence above the buttons.
   - The right pane has ~9 blocks.
4. **Action hierarchy:** Reject (red outline), Request Override (green outline) and Confirm
   (disabled) are three equal-width buttons, with the destructive one sitting beside the primary.
   It's also unclear whether a Transport Officer may reject an HOD-approved request, or should
   "Return" it instead.
5. **Status vocabulary:** "Pending Dispatch" vs "Approved" in Daniel's queue — both mean approved
   and waiting for him.
6. **Demo data drift:**
   - Coastal places (Mombasa, Kilifi, Kwale) instead of the Nakuru-area story.
   - The lifecycle request REQ-2024-0851 (Mary Akinyi, KBZ 442A, Joseph Mutua) is missing.
   - "Grace Njeri" collides with Grace, the Fleet Manager persona.
7. **Small:**
   - Sidebar shows "Vehicle Request" bold/white as well as the active "Dispatch Management" chip
     (two active states).
   - Role reads "Transport Officer"; the locked title is "Transport Operations Officer".
   - Pagination says 1–6 but 5 cards are visible.

---

## 5. Live app "Today" screen (Fleet Manager) — analysis and holistic fixes (2026-09-24)

Source: screenshot of the running web app shared by the user (Fleet Manager "Today" page,
3420×5924 full-page capture). This is the live implementation of what FRAME-01 designs. The goal is
to redesign it in Figma using the CVFMS components, so fixes below are stated as design decisions,
with the few that are really backend/data bugs called out separately.

### 5.1 What the page is trying to be vs. what it is

FRAME-01's job (blueprint §2): Grace's once-per-session landing — *know fleet state, then act on
exceptions*. The live page tries to be three pages at once: a fleet KPI board (11 tiles), an
exception inbox (Needs Attention), and Daniel's full transactional dispatch work surface (a 25-row
Transport Queue + gate-check detail pane). Result: ~2,000px of scroll, and the dispatch table (the
biggest thing on the page) is someone else's job.

### 5.2 Findings, by region

**Header / shell**
- H1. "Good afternoon, **Fleet**" and identity "FM · Fleet" — account username, not a person. No
  role title (breaks the locked name + role rule, handover §12.4). Sidebar footer repeats
  "Fleet Manager / Fleet Manager".
- H2. "Sign out" is a standalone top-bar button — belongs in the avatar menu.
- H3. Search placeholder "Search inventory…" — wrong domain word; there is no inventory here.
- H4. Nav is flat (Today, Requests, Dispatch, Vehicle Mgmt…, Incidents) — doesn't match the
  8-pillar grouped nav (pattern library §1). "Incidents" isn't in our nav; the SRS home for it is
  Driver Management → Accident Management. Sidebar background stops at ~665px on a long page (not
  full-height/sticky).

**KPI tiles (11 tiles, 2 rows)**
- K1. **The numbers don't reconcile.** Available 1023 + On Trip 0 + In Workshop 0 + Grounded 2 =
  1,025, not 1,056. 31 vehicles are in no bucket. (The Transport Queue also shows 31 items — may be
  coincidence, but it hints that allocated/dispatched-but-not-departed vehicles have no status
  bucket. Needs a dev check.)
- K2. "Available 1023 · Ready to dispatch" while Needs Attention lists vehicles with expired
  insurance — available ≠ dispatchable. The label overclaims.
- K3. Five GPS tiles, four of them effectively zero (Online 0, Moving 0, Idle 0) and Offline 6 —
  with 1,056 vehicles, "0 online / 6 offline" means telematics isn't feeding most of the fleet.
  Showing zeros as KPIs is noise, and it hides the real message ("tracking not connected for ~1,050
  vehicles").
- K4. "Open GPS events 82" is the biggest alarm number on the page, but none of those 82 are in
  Needs Attention's grouping or ranking, and there's no path to them.
- K5. "Service due 16 · Overdue schedules" — label says due, caption says overdue.
- K6. 11 tiles fails the five-second test (doc 06): our spec is 4 tiles, each linked to the rows
  behind its number.

**Needs Attention (32)**
- N1. **Duplicates.** KDA 100A appears 5 times (insurance ×2 identical, service time ×2, service
  km ×1); KDB 200B twice (two insurance records, 2025-01-01 and 2025-12-31 — the older one should
  be superseded, not listed). The list is one row per *record*, not one row per *problem*.
- N2. **Raw system codes shown to users:** `ghost_trip`, `unauthorised_allocation` (snake_case) —
  breaks the human-readable rule (handover §11.3). Those rows also have **no vehicle** — just a
  timestamp — so Grace can't tell what it's about.
- N3. Dates are ISO record dates ("Insurance 2025-01-01") instead of what matters: "expired 8
  months ago".
- N4. Generic actions (Open file / Schedule / Locate) instead of the specific fix (Renew insurance,
  Book service, Review trip trace).
- N5. No grouping or ranking — spec groups by Overdue / This Week with counts. A possible ghost
  trip happening *today* sits below year-old paperwork.
- N6. The card is ~570px tall, and the Fuel Snapshot beside it stretches to match — a mostly empty
  white card.

**Transport Queue (embedded)**
- T1. Wrong page — this is FRAME-02 (Daniel's work surface) pasted into Grace's overview. Grace
  needs the *pipeline shape* (how many are stuck where), not 25 rows.
- T2. Step vocabulary is inconsistent: "DISPATCHED" (uppercase, grey — reads as inactive although
  it's a milestone), "Ready to dispatch" (green), "Assign driver" (blue), "Transport review" (grey).
  Mixed case, and color doesn't map to meaning (action needed vs. waiting vs. done).
- T3. Filters are unstyled native browser controls (dd/mm/yyyy pickers, native select, "Filter"
  button) — not the design system's Filter Dropdown.
- T4. Unfriendly data: IDs like `REQ-40547713-80` (hard to read or say on a phone call; our format
  is `REQ-2024-0851`); mixed ID formats (`REQ-71249150`); ISO timestamps; Purpose truncated; a
  "Submitted" column Grace doesn't need; sorted by newest submitted instead of soonest departure.
- T5. Test/seed data visible: "John Officer", "Lifecycle QA" ×8, "Nanyuli tri[", "Foreign dept".

**Request detail pane**
- D1. **Logic contradiction — highest severity.** REQ-40547713-80 is DISPATCHED with every
  lifecycle step green (incl. "Request approved"), yet "Required checks (8/10)" shows 2 FAILs:
  *No assignment conflict* (driver has a conflicting trip) and *Linked approved request exists* —
  failing on a request that is itself approved. Either the gate was bypassed, or checks are being
  re-evaluated after dispatch without saying so, or the link check is buggy. On a system whose
  whole point is a mandatory dispatch gate, this is the one thing that can't look ambiguous.
- D2. The only action is "Recall dispatch" (amber outline, no explanation). The actual fix for the
  conflict (reassign driver) isn't offered.
- D3. Good and worth keeping: checks grouped into **Driver** and **Vehicle**; Trip status line
  "Awaiting driver accept · Pre-trip pending" — that's real, useful state.
- D4. The lifecycle stepper stops at "Dispatched" — but the trip continues on mobile (driver
  accepts → pre-trip → on trip → closed). The web and mobile halves of one lifecycle don't show each
  other.

### 5.3 Holistic fixes — five system-level decisions, not 30 patches

1. **One job per page.** "Today" = FRAME-01: fleet state + exceptions only. Remove the Transport
   Queue table; replace it with a compact **Dispatch pipeline** strip: stage counts (Transport
   review · Needs driver · Ready to dispatch · Awaiting driver accept · On trip), each clickable into
   the Dispatch page pre-filtered. Fixes T1, T4, T5 on this page, and answers "why is On Trip 0?"
   visually (8 dispatched, all awaiting driver accept).
2. **One status model, end to end.** Define one vehicle-status partition that must sum to fleet
   size (Available · Allocated/Dispatched · On trip · In workshop · Grounded · Disposed/other), and
   one request/trip lifecycle shared by web and mobile (Submitted → Approved → Transport review →
   Driver assigned → Ready → Dispatched/awaiting accept → Pre-trip → On trip → Closed). Every pill
   uses the same words, sentence case, and color-by-meaning: neutral = waiting on someone else,
   amber = waiting on *you*, green tint = ready/done, red = blocked. Fixes K1, K2, T2, D4.
3. **Exceptions are problems, not records.** Needs Attention becomes one row per vehicle-problem
   (deduped, superseded records dropped), grouped by severity with counts — **Blocking dispatch
   now** (expired insurance, grounded, gate conflicts) · **Investigate** (possible ghost trip,
   unauthorised allocation, GPS events — human-labeled, with vehicle + driver) · **Due this week**
   (service by date/km). Each row: vehicle photo thumb + reg + model, plain-English reason with a
   relative date, one specific action verb. Show top ~6, "View all 32 →". Fixes N1–N5, K4.
4. **Fewer, honest numbers.** One row of 4 tiles, each linked to the rows behind it: **Fleet**
   (1,056 · status breakdown bar underneath that visibly sums), **Ready to dispatch** (count that
   excludes non-compliant vehicles), **Compliance** (overdue · this week), **Requests** (awaiting
   action). Telematics collapses to one honest line/tile: "Tracking: 6 of 1,056 vehicles reporting
   · 82 unreviewed events →" (or "Not connected" if that's the truth). No zero tiles. Fixes K1–K6.
5. **Gate integrity is visible.** Wherever checks appear, show *when* they were evaluated ("Passed
   at dispatch, 12:02 · 2 new issues since"), and pair every Fail with its fix action (Reassign
   driver / Link request) and, only if needed, the override path that routes to an approver (no
   self-approval). Fixes D1, D2. **Backend follow-up for the dev team:** confirm whether dispatch
   was allowed with failing checks, and why "Linked approved request exists" fails on an approved
   request.

Plus shell hygiene (H1–H4): real name + role, sign-out in avatar menu, scoped search placeholder,
8-pillar nav, full-height sidebar; styled filter controls; human IDs and dates
("Wed 25 Sep · 12:00"); seed data cleaned before any demo.

### 5.4 Proposed "Today" layout (1440+ desktop)

```
Shell: grouped sidebar (Operations ▸ Fleet Overview active) · Top bar: search "Search vehicles,
  requests, drivers" · bell · "Grace Wanjiru / County Fleet Manager" (menu holds Sign out)
Greeting: "Good afternoon, Grace" / Wed 24 Sep 2026 / ● Live command active
Row 1 — 4 KPI tiles (Fleet · Ready to dispatch · Compliance · Requests) + status breakdown bar
Row 2 — Needs Attention (≈62%, grouped: Blocking dispatch / Investigate / Due this week, top 6)
        | right column stacked: Dispatch pipeline (stage counts) · Fuel this month (spend, litres,
          anomalies) — heights hug content, no stretched empty card
Row 3 — Coming up (next 30 days, calm) | Recent exceptions (overrides, recalls, anomaly flags, with actor)
```

### 5.5 Validation check against the source docs (2026-09-24) — corrections to §5.3

User asked whether this IA is really what the Fleet Manager needs. Checked against SRS §6
(Dashboards), `CVFMS Primary profiles.docx`, and `Test Login Accounts.docx` (expected landing per
role in the live app):
- **Supported:** the dispatch queue belongs to Transport Operations (profiles doc; `transport` has
  its own "Today"); the Fleet Manager's flows are "fleet command, exceptions, … and **oversight**".
- **Corrections:** (1) SRS §6 names **GPS alerts** as a Fleet Manager indicator and the SRS lists
  ghost trips / unauthorised allocation / unauthorised movement as core risks — §5.3's "collapse
  telematics to one line" was wrong. (2) SRS §6 also requires **driver performance** and **workshop
  workload** — missing from both the live page and §5.4. (3) "Incidents" in the nav is legitimate
  (profiles doc gives it to the Fleet Manager) — H4's flag withdrawn.
- **Still unvalidated with a real user:** all-day vs. glance usage, whether the Fleet Manager also
  dispatches, station-level thinking. The personas are SRS-inferred, not researched.

### 5.6 Agreed approach (user decisions, 2026-09-24) — supersedes §5.4

1. **Usage:** built for a morning glance, plus a compact **live-alerts strip** at the top so the page
   stays useful if left open all day.
2. **Dispatch:** the Transport Queue table is removed and replaced by a **dispatch pipeline** (stage
   counts, each linking to the pre-filtered Dispatch page) plus **"Awaiting your approval"** (override
   requests routed to the Fleet Manager — the no-self-approval chain from FRAME-02).
3. **Stations:** a page-level **"Scope: All stations ▾"** filter in the header. Same layout; scoped
   users land on their own station.
4. **SRS gaps:** **Workshop load** and **Drivers** as compact tiles in a lower row, each linking to
   its module.

Demo numbers are chosen to reconcile: 812 available + 31 allocated (awaiting departure) + 118 on
trip + 64 in workshop + 23 grounded + 8 pending disposal = **1,056**.

---

## 6. Prompt 2 — "Today" (Fleet Manager) v2

```
Work on the "Refined" page. If a frame named "v2 / fleet-operations-overview" exists, work on it;
otherwise duplicate "fleet-operations-overview", place the copy in empty space below all existing
content, and name it "v2 / fleet-operations-overview". Do not touch the original.

This is the Fleet Manager's landing page ("Today"). Rebuild the main workspace content with the
structure below. Keep the frame 1776px wide; let height hug content.

STYLE RULES (apply everywhere)
- Fonts: Lexend for page title, card titles and big numbers; Source Sans 3 for everything else.
- Colors only from: #006837 primary green, #00522C green hover, #E6F2EB green tint, #0F172A ink,
  #334155 slate, #64748B muted, #E2E8F0 border, #F8FAFC page background, #FFFFFF card,
  #059669/#ECFDF5 success, #B45309/#FFFBEB warning, #B91C1C/#FEF2F2 critical.
- Page background #F8FAFC. Every card: white, 1px #E2E8F0 border, 12px radius, 24px padding.
  32px between page sections, 24px between cards in a row.
- Status is never color alone: every status chip has an icon + sentence-case text ("Overdue",
  not "OVERDUE"). Color meaning: red = blocked, amber = needs YOUR action, green tint =
  ready/done, grey (#F8FAFC bg, #334155 text) = waiting on someone else.
- Reuse existing components on this page wherever they fit: Navigation/Sidebar, Top Bar,
  KPI Tile, Data Display/Status Breakdown Bar, Data Display/Section Card, Status Pill,
  Navigation/Tab Item, Controls/Filter Dropdown.
- Dates are human: "8 months ago", "Fri 26 Sep", "10 min ago" — never "2025-01-01".
- No raw system codes anywhere (no "ghost_trip", no snake_case, no "BR-001").

1. SHELL
- Navigation/Sidebar instance, variant with "Operations" expanded and "Fleet Overview" active.
  Sidebar fills the full frame height.
- Top Bar: search field placeholder "Search vehicles, requests, drivers"; notification bell with a
  red count badge "4"; identity: avatar + "Grace Wanjiru" with "County Fleet Manager" beneath it.
  No standalone "Sign out" button (it lives in the avatar menu).

2. HEADER (left) + SCOPE (right), same row
- Left: "Good afternoon, Grace" (Lexend 24px/600 #0F172A); beneath it "Wednesday, 24 September
  2026" (14px #64748B); beneath that a small green dot + "Live command active" (13px #334155).
- Right, aligned to the greeting's first line: a Controls/Filter Dropdown reading
  "Scope: All stations" with a chevron.
- Below the header, keep the tabs "Overview" (active) · "Live Map" · "All Vehicles".

3. LIVE ALERTS STRIP (full width, directly under the tabs)
A single white card, 16px vertical padding, with a small red pulsing-dot icon and the label
"Live alerts" (14px/600 #0F172A) on the left, then 3 alert items in a row separated by 1px
vertical dividers, then a link on the far right "82 unreviewed GPS events →" (#006837, 14px/600).
Each alert item: a 32px round icon badge (#FEF2F2 bg, #B91C1C icon), title 14px/600 #0F172A,
detail 13px #64748B, and a small text action (#006837):
- Radar icon — "Possible ghost trip" / "KCB 119B moving with no active trip · Molo · 10:24" /
  "Review trace"
- Map-pin-off icon — "Unauthorised movement" / "KDA 330C left geofence after hours · Njoro ·
  08:36" / "Review trace"
- Signal-off icon (amber: #FFFBEB bg, #B45309 icon) — "Tracking" / "1,012 of 1,056 vehicles
  reporting · 44 offline" / "View offline"

4. KPI ROW — exactly 4 KPI Tile instances, equal width, one row
- "FLEET" — "1,056" — caption "All vehicles in scope"
- "READY TO DISPATCH" — "797" — caption "of 812 available · 15 blocked by expired documents"
- "COMPLIANCE" — "38" — caption "9 overdue · 29 due this week"
- "REQUESTS" — "46" — caption "open · 3 awaiting your approval"
Label 12px/600 uppercase #64748B; value Lexend 28px/700 #0F172A; caption 13px #64748B.
Directly under the 4 tiles, full width, a Data Display/Status Breakdown Bar: one horizontal
stacked bar, 8px tall, 4px radius, segments proportional to: Available 812 (#059669), Allocated
31 (#006837 at 50% opacity), On trip 118 (#006837), In workshop 64 (#B45309), Grounded 23
(#B91C1C), Pending disposal 8 (#64748B). Beneath it a legend row: colored dot + label + count
for each segment, and at the far right "Total 1,056".

5. MAIN ROW — two columns: left ~62%, right ~38%, tops aligned, each card hugs its content
(no stretched empty space).

LEFT — "Needs attention" card
- Header: "Needs attention" (Lexend 18px/600) + count pill "38"; right side link
  "View all 38 →" (#006837).
- Group 1 label: "BLOCKING DISPATCH NOW · 9" (12px/600 uppercase #B91C1C). Then 3 rows.
- Group 2 label: "DUE THIS WEEK · 29" (12px/600 uppercase #B45309). Then 3 rows.
- Each row, 72px tall, 1px #E2E8F0 divider between rows: on the left a 56×40px vehicle photo
  thumbnail (8px radius; reuse the Toyota Land Cruiser photo already on this page for Land
  Cruisers, and a pickup/van photo for others); then registration 14px/600 #0F172A with model
  13px #64748B after a " · "; beneath it the reason 13px #334155; on the right a status chip,
  then one specific action as a text button (#006837, 14px/600). One row per vehicle problem —
  never the same vehicle + same problem twice.
  Blocking rows:
  - KBZ 442A · Toyota Land Cruiser — "Grounded since Sep 11 · brake pads · blocks REQ-2024-0851"
    — chip "Grounded" (alert-triangle, red) — action "View job card"
  - KDB 200B · Isuzu D-Max — "Insurance expired 8 months ago" — chip "Expired" (x-circle, red) —
    action "Renew insurance"
  - KDA 100A · Toyota Land Cruiser — "Insurance expired 9 months ago" — chip "Expired" — action
    "Renew insurance"
  Due-this-week rows:
  - KDA 100A · Toyota Land Cruiser — "Service overdue by 1,200 km" — chip "Overdue" (clock, amber)
    — action "Book service"
  - KCB 119B · Isuzu NQR — "Inspection due Fri 26 Sep" — chip "Due soon" (calendar, amber) —
    action "Schedule inspection"
  - KCE 558A · Nissan X-Trail — "Insurance renews Mon 29 Sep" — chip "Due soon" — action
    "Start renewal"

RIGHT — two cards stacked, 24px apart
(a) "Dispatch oversight" card
- Header "Dispatch oversight" (Lexend 18px/600); right link "Open dispatch →".
- Pipeline: 5 stages in one horizontal row joined by thin chevron separators. Each stage: count
  (Lexend 20px/600 #0F172A) over label (12px #64748B): "6 Transport review" · "5 Needs driver" ·
  "9 Ready" · "8 Awaiting driver" · "118 On trip". The "5 Needs driver" count is #B45309 (it's
  stuck on an action); the rest are #0F172A.
- Divider, then sub-heading "AWAITING YOUR APPROVAL · 3" (12px/600 uppercase #B45309).
- 3 compact rows (56px): title 14px/600 #0F172A, detail 13px #64748B, right-aligned small
  secondary button "Review" (white, 1px #006837 border, #006837 text, 32px tall, 8px radius):
  - "Dispatch override · REQ-2024-0851" / "KBZ 442A grounded · requested by Daniel Otieno ·
    10 min ago"
  - "Dispatch override · REQ-2024-0847" / "Driver licence class mismatch · requested by Daniel
    Otieno · 1 h ago"
  - "Vehicle transfer · KCE 558A" / "Health → Public Works · requested by Alice Njoroge ·
    3 h ago"

(b) "Fuel this month" card
- Header "Fuel this month" (Lexend 18px/600); right link "Fuel log →".
- Two figures side by side (no inner boxes): "KES 568K" label "Spend" and "3,169 L" label
  "53 fills" — values Lexend 22px/600 #0F172A, labels 13px #64748B.
- One line below with a small amber flag icon: "2 fuel anomalies to review →" (#B45309, 14px/600).

6. LOWER ROW — three cards in one row: Workshop 25%, Drivers 25%, Recent exceptions 50%
(a) "Workshop load" card (wrench icon in a 32px #F8FAFC circle): big "64" (Lexend 24px/600) with
    "vehicles in workshop" (13px #64748B); beneath, three plain rows: "In progress 41",
    "Awaiting parts 18", "Past promised date 5" (the last one's number in #B45309). Link
    "Workshop board →".
(b) "Drivers" card (id-card icon in a 32px #F8FAFC circle): big "184" with "active drivers";
    rows: "Licences expiring in 30 days 12" (number #B45309), "Suspended 3" (number #B91C1C),
    "Flagged for speeding this week 7". Link "Driver management →".
(c) "Recent exceptions" card: header + right link "Audit trail →". 4 rows, each: time
    (13px #64748B, 72px column), actor as its own bold field (14px/600 #0F172A), then the event
    (14px #334155):
    - "10:42" · "Grace Wanjiru" · "Approved dispatch override for KBZ 442A — insurance grace period"
    - "09:15" · "System" · "Suspended fuel card for KCB 119B — exceeded monthly limit"
    - "08:30" · "Peter Kamau" · "Logged unscheduled repair for KDA 330C — brake inspection"
    - "Yesterday" · "Daniel Otieno" · "Recalled dispatch REQ-2024-0839 — driver conflict"

Remove from this page: the Transport Queue table, the request detail / checks pane, the old
11-tile KPI rows, the old "Fleet Status Summary" map card and "Coming Up" card (their content is
now covered by the breakdown bar, Live Map tab, and the Due-this-week group).
```

**Check after render:**
- Breakdown bar segments visibly add up, and the legend total reads 1,056.
- Exactly 4 KPI tiles; no zero-value tiles.
- No duplicate vehicle + problem rows; no snake_case or raw codes; all dates are relative or human.
- Every chip has an icon; amber is used only for "needs your action".
- Right column cards hug their content, with no stretched empty space beside Needs attention.
- Identity reads Grace Wanjiru / County Fleet Manager; no Sign out button; the scope filter is present.
- No Transport Queue table anywhere on the page.

### 6a. Render check (2026-09-24) — structure landed; visual weight and nesting need a fix pass

**Landed correctly:**
- Identity reads Grace Wanjiru / County Fleet Manager; no Sign out button; scope filter present.
- Exactly 4 KPI tiles; the breakdown bar legend totals 1,056.
- Needs attention is grouped, with relative dates, specific actions and no duplicate vehicle + problem rows.
- The pipeline and approvals replace the queue; the Workshop and Drivers cards are present.
- Recent exceptions has a separate actor field; no raw codes; fonts are Lexend + Source Sans 3.

**Fix list (by impact):**
1. **Live alerts are too loud.** Each alert is a fully tinted, bordered box (~175px strip). They're
   now the heaviest thing on the page, against the agreed "compact live strip". Should be one
   white strip, with icon badges carrying the color and dividers between items.
2. **Boxes inside boxes.** Needs attention rows, approval rows and Recent exceptions rows are each
   bordered or filled cards inside a card. Should be plain rows with 1px dividers.
3. **Pipeline counts are cramped.** Numbers sit in small colored rings below tiny labels, so 118 is
   squeezed and the rings read as a stepper. Should be a big number over the label, no rings.
4. **"Review" buttons barely read as buttons.** They're near-invisible white with dark text, not
   green outline.
5. **Breakdown bar card:** the bar hugs the card's top edge, there's empty space below the legend,
   and the legend dots sit above the text baseline. Should merge into the KPI area.
6. **Top bar:** the identity text is clipped at the right edge ("County Fleet Manager" cut off),
   and the bar is ~106px with an empty left half.
7. **Lower row is split into thirds instead of 25/25/50**, so it doesn't line up with the 4-column
   KPI grid, and card heights are unequal.
8. **Small issues:**
   - Fuel card: "53 fills" is used as the label for litres.
   - The "Grounded" chip has an amber icon with red text.
   - The vehicle model is the same weight as the registration.

### 6b. Fix prompt — visual weight and nesting pass

```
On "v2 / fleet-operations-overview" (Refined page), make these fixes only. Keep all content,
data, section order and fonts exactly as they are.

1. LIVE ALERTS — make it a compact strip, not three boxes.
   Remove the tinted background fill and border from each of the three alert items. The strip is
   one white card (1px #E2E8F0 border, 12px radius), 16px vertical padding, max ~96px tall.
   Layout, all in one row: "● Live alerts" label on the left, then the three items separated
   by 1px #E2E8F0 vertical dividers, then "82 unreviewed GPS events →" on the far right.
   Each item: a 32px circular icon badge carrying the color (#FEF2F2 circle with #B91C1C icon for
   the two red alerts, #FFFBEB with #B45309 icon for Tracking); to its right, the title
   14px/600 #0F172A (not red), and beneath it, on one line, the detail 13px #64748B followed by the
   action link "Review trace" / "View offline" in #006837 13px/600. No red or amber text
   anywhere in this strip; color lives only in the icon badges.

2. REMOVE BOXES INSIDE CARDS. In "Needs attention", "Awaiting your approval" and "Recent
   exceptions", remove the border and background fill from every individual row. Rows sit
   directly on the white card, separated by a 1px #E2E8F0 divider line, 16px vertical padding
   per row. Keep all row content the same.

3. PIPELINE — numbers, not rings (per QuickBooks/Jobber references). In "Dispatch oversight",
   remove the circles/rings around the counts and any boxes around stages. Each stage, top to
   bottom: label 12px #64748B, then the count in Lexend 24px/600 #0F172A ("5" for Needs driver
   in #B45309), then one optional sub-line 12px #64748B — only on Needs driver: "longest 2 days".
   Stages evenly spaced across the card width, left aligned in their slots, with a small #64748B
   chevron between them.

4. "REVIEW" BUTTONS — make them clearly buttons: white background, 1px #006837 border, #006837
   text 13px/600, 32px tall, 12px horizontal padding, 8px radius.

5. KPI + BREAKDOWN — merge. Delete the separate card that holds the breakdown bar. Place the bar
   and its legend directly under the four KPI tiles, with no card around them: 16px below the
   tiles, bar 8px tall full width, legend 12px below the bar. Center each legend dot vertically
   with its text.

6. TOP BAR — the identity text is clipped at the right edge. Give the Top Bar 32px right padding
   so "Grace Wanjiru / County Fleet Manager" is fully visible, and set its height to 64px with
   the search, bell and identity vertically centered.

7. LOWER ROW — widths 25% / 25% / 50% (Workshop load, Drivers, Recent exceptions), matching the
   4-column KPI grid above: Workshop's edges align with the FLEET tile, Drivers with READY TO
   DISPATCH, and Recent exceptions spans COMPLIANCE + REQUESTS. All three cards stretch to the
   same height.

8. SMALL FIXES
   - Fuel card: label above "KES 568K" = "Spend"; label above "3,169 L" = "Litres"; add "53 fills"
     as a small 13px #64748B caption under 3,169 L.
   - "Grounded" chip: make the triangle icon #B91C1C to match its red text.
   - In Needs attention rows, show the model after the registration in 13px/400 #64748B, keeping
     the registration 14px/600 #0F172A.
```

---

## 7. Standing rule — information budget (user direction, 2026-09-24)

> "We need to really manage and display the information in ways it will not overwhelm the user —
> and if the information is too much, raise it and find a better way to display it."

This applies to every screen, desktop and mobile. It's a check on every prompt and every render,
not a one-off.

### 7.1 Three tiers — every piece of information is assigned one before it goes on a screen

| Tier | Question it answers | Where it lives |
|---|---|---|
| **1 — Act now** | What's wrong, and what needs *me*? | Always visible, top of page, passes the five-second test |
| **2 — Know state** | Is the fleet/queue/budget OK overall? | Visible but quiet: one line or one band, not a grid of tiles |
| **3 — Look up** | Details, history, breakdowns, secondary modules | Behind a link, tab, drawer or dedicated page — never on the landing surface by default |

### 7.2 Budgets (raise it when a screen breaks one)

- **Content blocks per screen:** landing/overview ≤ 5, work surface ≤ 3 (plus shell).
- **KPI tiles:** ≤ 4, and only numbers someone would act on or be judged by.
- **Rows per list on an overview:** ≤ 5–6, then "View all N →".
- **No number shown twice.** If a KPI and a list show the same count, one of them goes.
- **Every number passes "so what?"** It either needs action (show it) or it's context (show it
  once, quietly) or neither (drop it). Zero values and healthy values collapse into an
  "all clear" line.
- **Module summaries show the exception, not the module.** Workshop, Drivers, Fuel on an overview
  show one actionable number each (e.g. "5 past promised date"), not a mini dashboard.

### 7.3 When information is too much — display strategies, in order of preference

1. **Drop:** doesn't pass "so what?".
2. **Merge:** the same fact appears twice, so keep the one closest to its action.
3. **Summarize:** replace a list/grid with a count + one line + a link.
4. **Group and cap:** group by severity or owner, show the top N, link the rest.
5. **Collapse by state:** show it only when non-normal ("All clear" otherwise).
6. **Move down a tier:** into a tab, drawer or the module's own page.

**Process:** every render check in this doc now includes a **density check**: count content
blocks, KPI tiles, rows per list and duplicated numbers against §7.2, and flag any breach with a
proposed strategy from §7.3.

### 7.4 Density check — "Today" v2 as rendered (breaches found)

- **9 content blocks** (live alerts, KPI row, breakdown bar, Needs attention, Dispatch oversight,
  Fuel, Workshop, Drivers, Recent exceptions) against a budget of 5. **Breach.**
- **~45 visible numbers.**
- **Duplicated numbers — breach:**
  - Compliance tile "38" = Needs attention "38".
  - Requests tile "3 awaiting your approval" = the approvals list below it.
  - Ready to dispatch "of 812 available" repeats the breakdown bar.
- **Module cards are mini dashboards — breach.** Workshop shows 4 numbers and Drivers 4, where
  each needs 1.
- **Recent exceptions is tier 3** (the audit trail already exists), taking a full half-row.

**Proposed fix (awaiting user approval):**
1. **KPI row + breakdown bar → one quiet "Fleet state" band:**
   "1,056 vehicles · 797 ready to dispatch" + the status bar + legend. Compliance and Requests
   tiles are dropped (merged into Needs attention and Dispatch oversight, where the action is).
2. **Live alerts stays tier 1** but collapses to one line ("All clear · no live alerts") when
   nothing is active; max 3 items.
3. **Fuel, Workshop and Drivers merge into one "Watch list" row:** three short lines, one
   exception each, each linked — "Workshop: 5 vehicles past promised date →", "Drivers: 12 licences
   expiring in 30 days →", "Fuel: 2 anomalies to review →". The rest moves to tier 3 (module pages).
4. **Recent exceptions leaves the landing page** (tier 3, via "Audit trail →" in the page header or
   the bell), or is capped at 3 rows collapsed below the fold if the user wants it kept.

**Result:** 9 blocks → 4 (Live alerts · Fleet state · Needs attention | Dispatch oversight ·
Watch list), ~45 numbers → ~22, no number shown twice.

---

## 8. "Today" v3 — reference-driven restructure (2026-09-24)

Replaces the §6b fix prompt and the §7.4 trim. Built from the user-selected references in `05`
("Information-heavy pages"): OpenAI, Okta, Apollo, Fresha, Wix, Xero, Airwallex, Jobber/QuickBooks.

**Density check (pre-generation, per §7):**
- **Content blocks: 6** (live alerts, fleet state, needs attention, dispatch oversight, watch list,
  stations) against a budget of 5. **One over.** "Stations needing attention" is the deliberate
  trial block; if the render feels heavy, it's the first to go.
- **KPI tiles:** 0. They're replaced by one band.
- **Numbers shown twice:** 0. "On trip" left the pipeline because the band already shows it.
- **Rows per list:** ≤ 5.

**New standing pattern — page filter row (Airwallex):** directly under the page title on every
desktop work surface and analytics page: icon dropdowns (Scope, Period, plus page-specific
filters), then a "Reset" text link; data freshness ("Updated 10:42") right-aligned on the same row.

**Destination pages added to the build list:**
- Compliance: a table with type chips and saved views.
- Fuel Management: two tabs, Fuel log and Anomalies.
- Audit Trail (FRAME-09).
- Driver Management → Behaviour tab.
These are where the quick links and "View all" links go.

**Demo numbers (all reconcile):**
- **Fleet:** 812 + 31 + 118 + 64 + 23 + 8 = 1,056. Of the 812 available, 797 are ready and 15 are
  blocked by expired documents (9 insurance + 6 inspection).
- **Needs attention (45):**
  - Blocking = 16: 9 insurance, 6 inspection, and 1 grounded vehicle blocking an approved request.
  - This week = 29: 12 service, 8 inspection due, 9 insurance renewals.

### 8a. Prompt 3 — "Today" v3

```
On the "Refined" page, duplicate the frame "v2 / fleet-operations-overview", place the copy 120px
to its right, and name it "v3 / fleet-operations-overview". Work only on the v3 copy. Keep the
Navigation/Sidebar (Operations expanded, "Fleet Overview" active) and the Top Bar. Replace
everything in the main workspace below the Top Bar with the structure below.

STYLE RULES
- Fonts: Lexend for page title, card titles and big numbers; Source Sans 3 for everything else.
- Colors only: #006837 green, #E6F2EB green tint, #0F172A ink, #334155 slate, #64748B muted,
  #E2E8F0 border, #F8FAFC page bg, #FFFFFF card, #059669/#ECFDF5 success, #B45309/#FFFBEB
  warning, #B91C1C/#FEF2F2 critical.
- Cards: white, 1px #E2E8F0 border, 12px radius, 24px padding. 24px between cards, 32px between
  page sections. Page side padding 40px.
- NO boxes inside cards: rows inside a card are separated only by 1px #E2E8F0 divider lines.
- Color marks only the exception: neutral numbers are #0F172A; only a number that is a problem
  gets #B91C1C (blocked) or #B45309 (needs your action). No red or amber text elsewhere.
- Every status chip has an icon + sentence-case text. No raw codes, no ISO dates.
- Every card title row: title (Lexend 18px/600 #0F172A), then its time window in 13px #64748B
  (e.g. "· Today"), and a link on the far right in #006837 14px/600.

0. TOP BAR: 64px tall, 32px right padding so "Grace Wanjiru / County Fleet Manager" is fully
   visible; search, bell (red badge "4") and identity vertically centered.

1. HEADER
- "Good afternoon, Grace" (Lexend 24px/600), beneath it "Wednesday, 24 September 2026" (14px
  #64748B). Below the header, keep tabs "Overview" (active) · "Live Map" · "All Vehicles".
- FILTER ROW, 16px under the tabs: three dropdown buttons, each 36px tall, white, 1px #E2E8F0
  border, 8px radius, leading 16px icon (#64748B), label 14px #0F172A, chevron:
  [map-pin] "All stations"  [calendar] "Today"  [building] "All departments"
  then a text link "Reset" (#006837 14px/600). On the far right of the same row: a small green
  dot + "Live · Updated 10:42" (13px #64748B).

2. LIVE ALERTS — one white card, compact (max 120px tall)
- First line: a small red dot + "3 live alerts need review" (14px/600 #0F172A) + " · since 06:00"
  (13px #64748B); far right link "82 unreviewed GPS events →".
- Below, one row of 3 items separated by 1px vertical dividers. Each item: 32px circular icon
  badge (#FEF2F2 + #B91C1C icon; the third #FFFBEB + #B45309 icon), title 14px/600 #0F172A,
  detail 13px #64748B, then action link 13px/600 #006837:
  · radar icon — "Possible ghost trip" — "KCB 119B moving with no active trip · Molo · 10:24" —
    "Review trace"
  · map-pin-off icon — "Unauthorised movement" — "KDA 330C left geofence after hours · Njoro ·
    08:36" — "Review trace"
  · signal-off icon — "Tracking gaps" — "44 of 1,056 vehicles offline" — "View offline"

3. FLEET STATE — one white card, no tiles inside
- Title row: "Fleet state" + "· 1,056 vehicles"; link "All vehicles →".
- A horizontal stacked bar, full width, 8px tall, 4px radius, segments proportional to:
  Available 812 (#059669), Allocated 31 (#006837 at 50% opacity), On trip 118 (#006837),
  In workshop 64 (#64748B), Grounded 23 (#B91C1C), Pending disposal 8 (#E2E8F0).
- Under the bar, one row of 6 cells separated by 1px vertical dividers (Xero style). Each cell:
  label with a colored dot matching its bar segment (13px #64748B), then the number (Lexend
  24px/600):
  "Available" 812 — with a caption under it (12px #64748B): "797 ready · 15 blocked"
  "Allocated" 31 · "On trip" 118 · "In workshop" 64 ·
  "Grounded" 23 — this number and label in #B91C1C (the only colored cell) ·
  "Pending disposal" 8.

4. MAIN ROW — two columns, left 62%, right 38%, tops aligned, each card hugs its content.

LEFT — "Needs attention" card
- Title row: "Needs attention" + count "45"; then, instead of one link, inline quick links in
  14px #006837 separated by " · ": "Compliance · Workshop · Drivers".
- Filter tabs inside the card (Navigation/Tab Item): "All (45)" active · "Blocking (16)" ·
  "This week (29)". 1px divider below.
- Group label "BLOCKING DISPATCH NOW" (12px/600 uppercase #B91C1C), then 3 problem-type rows.
  Group label "DUE THIS WEEK" (12px/600 uppercase #B45309), then 3 problem-type rows.
- Each problem-type row (56px): a chevron on the left (right-pointing = collapsed), a 20px icon,
  the problem name 14px/600 #0F172A, a count chip ("9 vehicles", neutral #F8FAFC bg, #334155
  text), and on the far right one action link (#006837 14px/600).
  Blocking:
  · [chevron-down, EXPANDED] shield-x icon — "Insurance expired" — "9 vehicles" — "Renew all →"
      Expanded content, indented 32px, 3 vehicle rows (48px each, divider lines): 48×32px
      vehicle photo (6px radius), "KDB 200B" 14px/600 + " · Isuzu D-Max" 13px #64748B, reason
      "Expired 8 months ago" 13px #334155 on the right, then "Renew" link:
        KDB 200B · Isuzu D-Max — Expired 8 months ago
        KDA 100A · Toyota Land Cruiser — Expired 9 months ago
        KCD 311F · Toyota Hilux — Expired 2 weeks ago
      then "+ 6 more vehicles →" (13px #006837).
  · clipboard-x icon — "Inspection expired" — "6 vehicles" — "Schedule →"
  · alert-triangle icon — "Grounded, blocks an approved request" — "1 vehicle" — "View job card →"
  This week:
  · wrench icon — "Service overdue" — "12 vehicles" — "Book services →"
  · calendar icon — "Inspection due" — "8 vehicles" — "Schedule →"
  · shield icon — "Insurance renewal due" — "9 vehicles" — "Start renewals →"

RIGHT — "Dispatch oversight" card
- Title row: "Dispatch oversight" + " · Today"; link "Open dispatch →".
- Pipeline: 4 cells in one row, separated by small #64748B chevrons, no boxes or rings. Each cell:
  label 13px #64748B, then count Lexend 24px/600 #0F172A:
  "Transport review" 6 → "Needs driver" 5 (count and label in #B45309, sub-line 12px #B45309
  "longest 2 days") → "Ready" 9 → "Awaiting driver" 8.
- Divider, then "AWAITING YOUR APPROVAL · 3" (12px/600 uppercase #B45309).
- 3 rows (divider lines, no boxes): title 14px/600 #0F172A, detail 13px #64748B, right-aligned
  "Review" button (white, 1px #006837 border, #006837 text 13px/600, 32px tall, 8px radius):
  · "Dispatch override · REQ-2024-0851" / "KBZ 442A grounded · Daniel Otieno · 10 min ago"
  · "Dispatch override · REQ-2024-0847" / "Licence class mismatch · Daniel Otieno · 1 h ago"
  · "Vehicle transfer · KCE 558A" / "Health → Public Works · Alice Njoroge · 3 h ago"

5. LOWER ROW — two cards, left 62%, right 38%, equal height.

LEFT — "Watch list" card
- Title row: "Watch list"; no link (each line links itself).
- 3 rows, 56px each, divider lines. Each row: 32px circular icon badge (#F8FAFC bg, #334155
  icon), module name 14px/600 #0F172A, time window 13px #64748B, then the exception sentence
  14px #334155 with its number in #B45309, and a link on the far right:
  · wrench — "Workshop" · "now" — "5 vehicles past promised date" — "Workshop board →"
  · id-card — "Drivers" · "next 30 days" — "12 licences expiring" — "Driver management →"
  · fuel — "Fuel" · "this month" — "2 anomalies to review" — "Fuel log →"

RIGHT — "Stations needing attention" card
- Title row: "Stations needing attention" + " · top 4"; link "All stations →".
- A small table, 4 rows, no outer box inside the card. Header row 12px/600 uppercase #64748B on
  #F8FAFC: STATION · BLOCKED · OVERDUE · ALERTS. Rows 44px, divider lines; station 14px/600
  #0F172A; numbers 14px right-aligned, #0F172A, except any number above 0 in BLOCKED shown in
  #B91C1C:
  Nakuru HQ — 5 — 4 — 1
  Molo — 4 — 3 — 1
  Njoro — 3 — 5 — 1
  Naivasha — 2 — 2 — 0
```

**Check after render:**
- Block count is 6, and the page reads calmer than v2.
- The only red numbers are "Grounded 23", the Blocking group, and the Blocked column; the only
  amber ones are "Needs driver" and the Watch list exceptions.
- No boxes inside cards.
- "Insurance expired" is expanded; the other five groups are collapsed.
- The filter row appears with Reset and "Updated 10:42".
- No number appears twice.
- Top Bar identity isn't clipped.

### 8b. Render check — "Today" v3 (2026-09-24)

**Verdict:** the information architecture works. The page is far calmer and easier to scan than
v2: problem types instead of rows, one fleet band, a filter row, and a freshness stamp. What's
left is (a) three styling fixes that have now failed twice and (b) a handful of new issues.

**Landed:**
- Filter row with Reset and "Live · Updated 10:42".
- Live-alerts headline sentence.
- Fleet band cells, with Grounded as the only red cell.
- Needs attention grouped by type, with counts; Insurance expanded; in-card tabs and quick links.
- Pipeline without "On trip".
- Approval rows are no longer boxed.
- Watch list as one-liners.
- Stations top-4 table.
- Top Bar identity no longer clipped.

**Failed twice (v2 fix pass + v3 prompt) → escalate per doc 06 §0 rule 2: fix directly with
`use_figma`, stop re-prompting:**
1. Live-alert items are still tinted boxes with red/amber titles, and "Review trace" touches the
   box's bottom edge.
2. Pipeline counts are still inside rings.
3. "Review" buttons are still grey outline with dark text, not green outline.

**New issues:**
4. **A number is shown twice (§7 breach):** the legend line under the fleet bar repeats every
   cell below it. Delete the legend line; the cells already carry the colored dots.
5. **Severity is shown three times per row:** the colored icon, the colored count circle and the
   group label color. The count also repeats: "9" in the circle and "9 vehicles need renewal…"
   in the subtitle. Make the count circle neutral, or drop it and keep the sentence.
6. **Two arrows side by side:** the expand chevron sits right next to the "→" action link, so it's
   unclear which one expands and which one navigates. Put the chevron on the left, before the icon.
7. **Wrong icons:** "Inspection due" reuses the x-circle from "Inspection expired" (due isn't
   failed); "Service overdue" uses a sliders icon.
8. **Unbalanced columns:** the left column is ~910px tall and Dispatch oversight ~440px, leaving a
   large empty gap on the right. Stack Stations under Dispatch oversight in the right column, and
   put the Watch list under Needs attention in the left.
9. **Missing exit links:** "All vehicles →", "Open dispatch →" and "All stations →" didn't render,
   and the time windows ("· 1,056 vehicles", "· Today", "· top 4") drifted to the far right
   instead of sitting next to their titles.
10. **Small:**
    - The Allocated and On trip dots are the same dark green.
    - The Stations table has its own border inside the card, a box inside a box.

### 8c. Fix prompt — v3 new issues — **SUPERSEDED by §8e, do not run**

```
On "v3 / fleet-operations-overview" (Refined page), make only these changes. Keep all content,
numbers and fonts as they are.

1. FLEET STATE: delete the single legend line directly under the colored bar ("Available 812 ·
   Allocated 31 · …"). The six cells below already show these. In the title row, move
   "· 1,056 vehicles" to sit right after the "Fleet state" title (13px #64748B), and add a link
   "All vehicles →" (#006837 14px/600) on the far right. Make the Allocated dot and bar segment
   #6EE7B7 so they differ from On trip (#006837).

2. NEEDS ATTENTION rows:
   - Make every count circle neutral: #F8FAFC background, #334155 text. Only the group labels
     ("BLOCKING DISPATCH NOW", "DUE THIS WEEK") keep red/amber.
   - Make every row icon #64748B (grey).
   - Move the expand chevron to the far LEFT of each row, before the icon. The right side keeps
     only the count and the action link.
   - Icons: "Inspection due" = calendar-clock icon (not an x); "Service overdue" = wrench icon.

3. LAYOUT BALANCE — remove the large empty space below "Dispatch oversight". Right column =
   "Dispatch oversight" with "Stations needing attention" placed directly under it, exactly 24px
   gap. Left column = "Needs attention" with "Watch list" directly under it, exactly 24px gap.
   Both columns top-aligned. No card may stretch to fill height: every card hugs its content.

4. TITLE ROWS: in "Dispatch oversight", move "· Today" right after the title and add
   "Open dispatch →" on the far right. In "Stations needing attention", move "· top 4" right
   after the title and add "All stations →" on the far right.

5. STATIONS TABLE: remove the border around the table; the table sits directly on the card with
   only its header background and row divider lines.

6. PIPELINE — replace the four circled counts in "Dispatch oversight" with a single arrow-segment
   strip (like Jobber's "Workflow" bar). Delete the circles entirely.
   - One horizontal strip, full card width, 72px tall, split into 4 equal segments. Each segment
     is an arrow shape pointing right (chevron-notched: flat-left edge on the first, a
     triangular notch on the left and point on the right on the others), with a 2px white gap
     between segments so the arrows read as a flow from left to right.
   - Segment fill #F8FAFC; the "Needs driver" segment fill #FFFBEB (the bottleneck).
   - Inside each segment, left-aligned with 16px padding: stage label 13px #64748B on top, count
     below in Lexend 24px/600 #0F172A:
     "Transport review" 6 · "Needs driver" 5 · "Ready" 9 · "Awaiting driver" 8.
     For "Needs driver" only: label and count in #B45309, and a third line 12px #B45309
     "oldest waiting 2 days".
   - Under the strip, one caption line 13px #64748B: "28 requests in progress · tap a stage to
     open it in Dispatch".
```


### 8d. Decisions after the v3 review (user, 2026-09-24)

1. **Filters:** only the station scope survives, as a scope switcher next to the date. The Period
   filter contradicts a "Today" page whose blocks have fixed time windows; Department belongs on
   the Dispatch queue. The filter-row pattern stays standard for work surfaces and analytics pages.
2. **Live alerts:** calm list rows, with color only in the icon badges. "Tracking gaps" isn't a
   live alert (it's system health), so it moves into the freshness stamp ("44 trackers offline").
   This leaves 2 alerts. When nothing is live, the strip collapses to one line.
3. **Fuel is promoted to the top**, as its own card beside Fleet state rather than a cell in the
   vehicle band (different unit). It shows a pace bar with a "today" marker, and turns amber only
   when spend is ahead of pace.
4. **Two-column layout, same 62/38 grid top to bottom:**
   - Left (vehicles & problems): Fleet state → Needs attention.
   - Right (money & flow): Fuel → Dispatch oversight → Watch list.
   The columns are balanced by content height.
5. **Fleet band has 5 cells:** "Pending disposal 8" becomes a note in the title so the cells get
   room. The bar still has all 6 segments and totals 1,056.
6. **"Stations needing attention" card dropped:** it was the trial block; the scope switcher covers
   single-station views.
7. **New standing rule for §7, "problems move up":** a module shows its quiet state low on the
   page and gets promoted into Needs attention when it goes off-normal (e.g. fuel spend 18% ahead
   of pace).

**Density:**
- 5 content blocks + the live strip = 6 (live, fleet, fuel, needs attention, dispatch, watch
  list). Within budget once the strip counts as conditional.
- 0 numbers shown twice.

### 8e. Fix prompt — "Today" v3 consolidated fix (supersedes §8c)

```
On "v3 / fleet-operations-overview" (Refined page), restructure the main workspace as below.
Keep the Sidebar and Top Bar, fonts, colors and all numbers unless a step changes them.
Global rules: every card is white, 1px #E2E8F0 border, 12px radius, 24px padding, and HUGS its
content (never stretches to fill height). Inside cards, rows are separated only by 1px #E2E8F0
lines — no boxes or tinted fills around rows. Title rows: title Lexend 18px/600 #0F172A, then
the context text right after the title in 13px #64748B, and one link on the far right in
#006837 14px/600.

1. HEADER — delete the whole filter row (the "All stations", "Today", "All departments" buttons
   and "Reset"). Under "Good afternoon, Grace", the second line becomes:
   "Wednesday, 24 September 2026 · " followed by a text dropdown "All stations ▾" (14px/600
   #0F172A, chevron) — this is the station scope switcher.
   On the right side of the greeting block, vertically centered: green dot + "Live · Updated
   10:42 · 44 trackers offline" (13px #64748B). Keep the Overview / Live Map / All Vehicles tabs.

2. LIVE ALERTS — rebuild this card as a simple list. Delete the three tinted alert boxes.
   - Line 1: small red dot + "2 live alerts" (14px/600 #0F172A) + " · since 06:00" (13px
     #64748B); far right link "82 unreviewed GPS events →".
   - Then 2 plain rows on the white card, 48px tall, divider line between them. Each row: a 28px
     circle with #FEF2F2 fill and a #B91C1C icon; title 14px/600 #0F172A (dark, NOT red); " — "
     then detail 14px #334155; far right text link 14px/600 #006837:
     · radar icon — "Possible ghost trip" — "KCB 119B moving with no active trip · Molo · 10:24"
       — "Review trace"
     · map-pin-off icon — "Unauthorised movement" — "KDA 330C left geofence after hours · Njoro
       · 08:36" — "Review trace"
   - Remove the "Tracking gaps" alert (now in the header stamp).

3. LAYOUT — below the live alerts card, two columns: LEFT 62%, RIGHT 38%, 24px gap. Each column
   is a vertical stack of cards with exactly 24px between cards.
   LEFT column, top to bottom: Fleet state, Needs attention.
   RIGHT column, top to bottom: Fuel, Dispatch oversight, Watch list.
   Delete the "Stations needing attention" card.

4. FLEET STATE (left, top)
   - Title row: "Fleet state" + "· 1,056 vehicles · 8 pending disposal"; link "All vehicles →".
   - Keep the stacked bar with all 6 segments; change the Allocated segment to #6EE7B7.
   - Delete the legend line under the bar.
   - Cells: 5 instead of 6 — Available 812 (caption "797 ready · 15 blocked"), Allocated 31
     (dot #6EE7B7), On trip 118, In workshop 64, Grounded 23 (red). Remove the "Pending disposal"
     cell. Numbers Lexend 24px/600.

5. FUEL (right, top) — new card, same height as Fleet state.
   - Title row: "Fuel" + "· this month"; link "Fuel log →".
   - "KES 568K" in Lexend 24px/600 #0F172A (same size as the fleet numbers, not bigger), then on
     the same line "of KES 750K budget" 14px #64748B.
   - Pace bar: 6px tall, full card width, 3px radius, track #E2E8F0, fill #006837 to 76%. A thin
     vertical marker (2px wide, 14px tall, #0F172A) at 80% of the width, with the label "Today"
     (11px #64748B) above it. This bar must look different from the fleet stacked bar: one color
     plus a marker.
   - Caption 13px #64748B: "76% spent · day 24 of 30 · on pace".
   - Divider line, then a row: small flag icon #B45309 + "2 anomalies to review" 14px/600
     #B45309 + "→".

6. NEEDS ATTENTION (left, under Fleet state)
   - Count circles neutral (#F8FAFC bg, #334155 text); all row icons #64748B. Only the group
     labels keep red/amber.
   - Expand chevron at the far LEFT of each row, before the icon; right side keeps only count +
     action link.
   - Icons: "Inspection due" = calendar-clock; "Service overdue" = wrench.
   - Keep "Insurance expired" expanded but show only 2 vehicle rows (KDB 200B, KDA 100A), then
     "+ 7 more vehicles →".

7. DISPATCH OVERSIGHT (right, under Fuel)
   - Title row: "Dispatch oversight" + "· Today"; link "Open dispatch →".
   - Delete the four circled counts. Replace with one arrow-segment strip: full card width, 64px
     tall, 4 equal right-pointing chevron segments with 2px white gaps, fill #F8FAFC; the
     "Needs driver" segment fill #FFFBEB. Inside each, 12px padding, label 12px #64748B above
     count Lexend 20px/600 #0F172A: "Transport review" 6 · "Needs driver" 5 (label and count
     #B45309, plus "oldest 2 days" 11px #B45309) · "Ready" 9 · "Awaiting driver" 8.
   - Caption 13px #64748B under the strip: "28 in progress · select a stage to open it".
   - "AWAITING YOUR APPROVAL · 3" and the 3 rows stay. Each "Review" button: white fill, 1px
     #006837 border, text #006837 13px/600 (green, not grey or black), 32px tall, 12px side
     padding, 8px radius.

8. WATCH LIST (right, under Dispatch oversight)
   - Title "Watch list". Only 2 rows now (remove the Fuel row): Workshop · now — "5 vehicles
     past promised date" — "Workshop board →"; Drivers · next 30 days — "12 licences expiring" —
     "Driver management →".
```

**Check after render:**
- The two columns end within ~100px of each other, with no large empty areas.
- The fuel card is the same height as Fleet state, and its number is the same size.
- The pace bar reads differently from the stacked bar.
- Live alerts: 2 white rows, color only in the circles.
- No filter row; the scope switcher sits in the date line.
- The pipeline is an arrow strip, not circles.
- "Review" buttons are green outline.
- **Escalation:** if the live alerts or the Review buttons fail a third time, fix them directly
  via `use_figma` (doc 06 §0 rule 2), with no further prompting.

### 8f. Render check — v3 after the §8e fix (2026-09-24): near-final, candidate T1 reference

**Landed (including all three items that had failed twice):**
- Live alerts are 2 calm white rows with color only in the icon circles.
- The pipeline is an arrow strip with the bottleneck tinted.
- "Review" buttons are green outline.
- The filter row is gone; the freshness stamp reads "44 trackers offline".
- Fleet band: 5 cells, legend removed, Allocated mint, "All vehicles →" link.
- Fuel card: same height as Fleet state, pace bar with a "Today" marker.
- Needs attention: neutral counts, grey icons, chevrons on the left, 2 vehicles + "+7 more".
- Right column is Fuel → Dispatch → Watch list; columns end within ~115px of each other.

**Density:** 6 blocks (including the conditional live strip), 0 numbers shown twice. Within budget.

**Remaining fixes (small):**
1. **Two page titles (a confirmed defect per the pattern library):** "Fleet Operations Overview" in
   the Top Bar plus the "Good afternoon, Grace" greeting. The landing page uses the greeting form
   only, so remove the Top Bar title.
2. **The date line disappeared,** and the scope switcher floats as a pill at the top right. Should
   be: under the greeting, "Wednesday, 24 September 2026 · All stations ▾" as one line.
3. **Watch list card is broken at its edges:** divider lines run past the card's right border, and
   the bottom border and padding are missing, so the card looks clipped.
4. **Wrong icons, still:** "Service overdue" and the fuel anomaly row use a sliders icon (should be
   wrench / flag); "Inspection due" now uses a map-pin (should be calendar-clock).
5. **Fuel card alignment:**
   - "of KES 750K budget" sits top-aligned like a superscript; it should share the baseline of
     "KES 568K".
   - The caption is right-aligned; it should be left-aligned.
   - A stray divider line sits under "2 anomalies to review".
6. **The "45" count pill on Needs attention is red** even though 29 of the 45 aren't blocking.
   Make it neutral, like the other counts.

### 8g. Header + live alerts rework (Mobbin-backed, 2026-09-24) — supersedes items 1–2 of the §8f fixes

**Decisions:**
- **No standalone date line.** The date moves into the freshness stamp.
- **One header row:** greeting on the left; scope switcher and stamp on the right.
- **Top bar:** search on the left.
- **Live alerts:** side-by-side columns with the action directly under each message.

References are in `05` ("Page header… and live-alert layout").

```
On "v3 / fleet-operations-overview" (Refined page):

1. TOP BAR (64px): remove the page title text. Move the search field to the LEFT, starting at
   the same x as the page content (40px from the sidebar), 360px wide. Bell and "Grace Wanjiru /
   County Fleet Manager" stay on the right.

2. PAGE HEADER — 32px below the top bar:
   - Breadcrumb line first: "Operations / Fleet overview" (13px #64748B; "Fleet overview" in
     #334155). 8px below it, the header row.
   - Header row left: "Good afternoon, Grace" (Lexend 24px/600 #0F172A). No date line under it.
   - Right, vertically centered with the greeting, in this order with 16px gaps: the text
     dropdown "All stations ▾" (14px/600 #0F172A), then a 1px × 16px #E2E8F0 divider, then a
     green dot + "Wed 24 Sep · Updated 10:42 · 44 trackers offline" (13px #64748B).
   - Delete the separate "All stations" pill and any other date text.
   - The tabs Overview / Live Map / All Vehicles sit 16px below this row.

3. LIVE ALERTS — change from full-width rows to side-by-side columns:
   - Card header line: red dot + "2 live alerts" (14px/600 #0F172A) + " · since 06:00 · "
     (13px #64748B) + "82 unreviewed GPS events →" (13px/600 #006837), all on ONE line, left
     aligned. Nothing on the far right.
   - Below it, the alerts sit in equal-width columns (2 columns now; up to 3), separated by a
     1px #E2E8F0 vertical divider, 24px padding on each side of the divider. White background,
     no boxes, no tints.
   - Each column: a 28px circle (#FEF2F2 fill, #B91C1C icon) on the left; to its right, stacked:
     title 14px/600 #0F172A, then detail 13px #64748B (may wrap to 2 lines), then the action
     link "Review trace →" (13px/600 #006837) directly under the detail, left-aligned with it.
     · radar — "Possible ghost trip" — "KCB 119B moving with no active trip · Molo · 10:24"
     · map-pin-off — "Unauthorised movement" — "KDA 330C left geofence after hours · Njoro · 08:36"
   - The whole card should be about 120px tall.

4. Keep the §8f fixes 3–6 (Watch list edges, icons, fuel card alignment, neutral "45" pill) if
   not already applied.
```

### 8h. Consolidated prompt — live alerts move into Needs attention, photo rule (2026-09-24)

**Decisions:**
- The standalone Live alerts card at the top is removed. Live alerts become the first group
  ("LIVE NOW") of Needs attention (system map §3b).
- Row rule: a row about one vehicle shows its photo; a row about a group of vehicles shows an icon.
- The whole row is clickable, with no text links inside collapsed rows.
- Groups are collapsed by default. The expanded state is shown in a second frame.

This supersedes §8g item 3 and the earlier Needs-attention instructions.

```
On "v3 / fleet-operations-overview" (Refined page):

1. REMOVE THE LIVE ALERTS CARD. Delete the standalone "Live alerts" / "2 live alerts" card at
   the top of the page entirely. Live alerts now live inside "Needs attention" (step 4). The
   two-column layout (Fleet state + Fuel) starts directly under the tabs, 24px below them.

2. TOP BAR (64px): no page title text. Search field on the LEFT, starting at the page content's
   left edge, 360px wide. Bell and "Grace Wanjiru / County Fleet Manager" on the right.

3. PAGE HEADER, 32px below the top bar:
   - Breadcrumb: "Operations / Fleet overview" (13px #64748B; "Fleet overview" #334155).
   - 8px below, header row. Left: "Good afternoon, Grace" (Lexend 24px/600 #0F172A), no date
     line. Right, vertically centered: text dropdown "All stations ▾" (14px/600 #0F172A), a 1px ×
     16px #E2E8F0 divider, then a green dot + "Wed 24 Sep · Updated 10:42 · 44 trackers offline"
     (13px #64748B). Delete the separate "All stations" pill and any other date text.
   - Tabs Overview / Live Map / All Vehicles 16px below.

4. NEEDS ATTENTION:
   - Count "47". Tabs: "All (47)" active · "Live (2)" · "Blocking (16)" · "This week (29)".
   - Row rule: a row about ONE vehicle starts with a 48×32px vehicle photo (6px radius); a row
     about a GROUP of vehicles starts with a 28px icon circle (#F8FAFC fill, #64748B icon).
     All rows 56px, divider lines, no boxes, whole row clickable, a 16px ">" chevron (#64748B)
     at the far right, no text action links inside rows.
   - FIRST group "LIVE NOW · 2" (12px/600 uppercase #B91C1C):
     · [photo of a white Isuzu NQR truck] "KCB 119B · Isuzu NQR" (14px/600 #0F172A; model
       13px #64748B) — middle: a 20px #B91C1C radar icon + "Possible ghost trip" (14px/600
       #B91C1C) + " · moving with no active trip · Molo · 10:24" (13px #64748B) — >
     · [photo of a white Toyota Hilux] "KDA 330C · Toyota Hilux" — middle: #B91C1C map-pin-off
       icon + "Unauthorised movement" + " · left geofence after hours · Njoro · 08:36" — >
     Then one line 13px/600 #006837: "82 unreviewed GPS events →".
   - "BLOCKING DISPATCH NOW · 16" (#B91C1C label), rows collapsed:
     · [icon shield-x] "Insurance expired" — "9 vehicles need renewal before dispatch" — chip 9 — >
     · [icon clipboard-x] "Inspection expired" — "6 vehicles need inspection" — chip 6 — >
     · [photo of a Toyota Land Cruiser — reuse the one on this page] "KBZ 442A · Toyota Land
       Cruiser" — "Grounded · blocks REQ-2024-0851" — >
   - "DUE THIS WEEK · 29" (#B45309 label), rows collapsed:
     · [icon wrench] "Service overdue" — "12 vehicles need service this week" — chip 12 — >
     · [icon calendar-clock] "Inspection due" — "8 vehicles need inspection this week" — chip 8 — >
     · [icon shield] "Insurance renewal due" — "9 vehicles need renewal this week" — chip 9 — >
   - Group rows show a left chevron ">" before the icon (collapsed). Count chips neutral
     (#F8FAFC / #334155).

5. REMAINING FIXES: Watch list dividers stay inside the card, full border + 24px bottom padding.
   Fuel card: "of KES 750K budget" on the same baseline as "KES 568K"; caption left-aligned;
   no divider under "2 anomalies to review"; anomaly icon = flag (#B45309).

6. SECOND FRAME: duplicate the finished frame, place it 120px to the right, name it
   "v3 / fleet-operations-overview / group-expanded". In the copy only, expand "Insurance
   expired": chevron points down, and under it, indented 40px, 2 vehicle rows with photos —
   "KDB 200B · Isuzu D-Max — Expired 8 months ago — Renew" and "KDA 100A · Toyota Land Cruiser
   — Expired 9 months ago — Renew" — then "+ 7 more vehicles →" and a small secondary button
   "Renew all 9" (white, 1px #006837 border, #006837 text).
```

---

## 9. Dispatch & Requisition Queue — full audit against the system map (2026-09-24)

This is the same render as §4a, now audited with the 9-step method (`13` §7) as the **T2 Work
Queue** reference.

| # | Step | Finding | Severity |
|---|---|---|---|
| 1 | Job | Daniel, gate-check stage: "what's next, and can it go?" The layout answers it, but slowly (5 of 14 visible) | — |
| 2 | Template T2 | Skeleton correct (list ∥ detail pane). Missing P0 breadcrumb; "Gate Check System Online" is a stray status line | Low |
| 3 | Tiering | Every card carries tier-3 facts (Dept. User label, pax, "Routine"). "Routine" on every card is noise; only "Urgent" is news | Med |
| 4 | Density | Cards ~150px tall → 5 of 14 visible. Pass checks carry an icon **and** a PASS chip. The blocked state is stated twice (amber banner + red sentence). Right pane ~9 blocks | High |
| 5 | Pattern reuse | No vehicle photo on the resource (P13). Checklist has a Warning variant but uses it wrongly (P12). Three equal-weight buttons instead of the P14 decision footer | High |
| 6 | Connections | **Status chips (Pending / Approved / Ready / Flagged) don't match the Today pipeline stages** (Transport review / Needs driver / Ready / Awaiting driver), so a pipeline click from Today has nowhere to land. "Request override" doesn't say where it goes (Grace's approvals) | **Critical** |
| 7 | Vocabulary & data | "Pending Dispatch" vs "Approved" are the same state for Daniel. Coastal demo data (Mombasa, Kilifi) instead of the Nakuru-area story. The spine request REQ-2024-0851 is missing. "Grace Njeri" collides with the Fleet Manager persona. Role shows "Transport Officer" (locked title: Transport Operations Officer) | High |
| 8 | Rules | **A Warning blocks dispatch** (insurance expires 29 Sep, the trip is 25 Sep). Insurance is checked twice. "Reject" on an HOD-approved request is the approver's power. The sidebar shows two active items (Vehicle Request bold + Dispatch Management chip) | **Critical** |
| 9 | References | Airwallex spend requests (existing FRAME-02 reference), Linear list density | — |

**Assumed rules (recommended defaults from `13` §8, pending user confirmation):**
- Only a Fail blocks; a Warning informs.
- One insurance check with three states.
- The Transport Officer can "Return to requester" with a reason; "Reject" is the approver's power.

### 9a. Prompt — Dispatch Queue v2 (T2 reference), 2 frames: blocked + ready-with-warning

```
On the "Refined" page, redesign the Dispatch & Requisition Queue screen (the frame showing
"Dispatch & Requisition Queue" for Daniel Otieno). Duplicate it first, place the copy in empty
space, name it "v2 / dispatch-queue / blocked", and work on the copy.

STYLE: Lexend for titles and big numbers, Source Sans 3 for everything else. Colors only:
#006837, #E6F2EB, #0F172A, #334155, #64748B, #E2E8F0, #F8FAFC, #FFFFFF, #059669/#ECFDF5,
#B45309/#FFFBEB, #B91C1C/#FEF2F2. Cards white, 1px #E2E8F0, 12px radius. No boxes inside cards;
rows separated by 1px divider lines. Every chip has an icon + sentence-case text.

1. SHELL: sidebar shows exactly ONE active item, "Dispatch Management" (remove the bold/white
   state from "Vehicle Request"). Top Bar identity "Daniel Otieno / Transport Operations Officer".

2. PAGE HEADER: breadcrumb "Operations / Dispatch management" (13px #64748B). Title
   "Dispatch & Requisition Queue" (Lexend 24px/600). Remove "Transport Officer: Daniel Otieno ·
   Gate Check System Online".

3. STAGE TABS — replace the chips All / Pending / Approved / Ready to Dispatch / Flagged with
   tabs that match the Fleet Manager's pipeline, each with a count:
   "Transport review (6)" · "Needs driver (5)" · "Ready (9)" active · "Awaiting driver (8)" · "All (28)".
   Same row, right side: filter dropdown "All departments ▾", a search field "Search requests",
   and "Sort: Departure ↑".

4. LIST (left pane, 56% width) — compact rows instead of cards, 72px each, divider lines, no
   boxes. Row, line 1: request ID 14px/600 #0F172A + " · " + requester 14px #334155 +
   " · " + department 13px #64748B; right: departure "Today 10:30" 13px/600 #0F172A.
   Line 2: map-pin icon + route 13px #64748B; right: an "Urgent" chip (flag icon, #B91C1C on
   #FEF2F2) ONLY on urgent rows — no "Routine" chip anywhere.
   Selected row: #E6F2EB background + 3px #006837 left bar. Rows (Ready tab):
   · REQ-2024-0851 · Mary Akinyi · Public Works — Today 10:30 — Nakuru HQ → Nakuru Sub-County
     Office  [SELECTED]
   · REQ-2024-0853 · John Kamau · Health — Today 11:00 — Nakuru HQ → Naivasha District
     Hospital — Urgent
   · REQ-2024-0855 · Sarah Njeri · Agriculture — Today 13:00 — Molo Station → Gilgil Field Station
   · REQ-2024-0858 · Peter Omondi · Education — Today 14:30 — Nakuru HQ → Molo Teachers Centre
   · REQ-2024-0860 · Ruth Wambui · Finance — Tomorrow 08:00 — Nakuru HQ → County Treasury Annex
   · REQ-2024-0861 · David Kiprop · Water & Sanitation — Tomorrow 09:00 — Njoro → Rongai Borehole Site
   · REQ-2024-0864 · Faith Chelimo · Public Works — Tomorrow 10:00 — Nakuru HQ → Bahati Ward Office
   · REQ-2024-0866 · Hassan Juma · Roads — Tomorrow 11:30 — Naivasha → Mai Mahiu Road Works
   · REQ-2024-0867 · Amina Hassan · Water — Fri 26 Sep 07:30 — Nakuru HQ → Subukia Dam
   Footer: "1–9 of 9".

5. DETAIL PANE (right, 44%), 24px padding, 24px between sections:
   a. Context label "REQUEST DETAIL" (12px/600 uppercase #64748B). Title "REQ-2024-0851"
      (Lexend 20px/600) + chip "Ready" (arrow icon, #006837 on #E6F2EB).
      Line: check icon #059669 + "Approved by James Mwangi, Head of Public Works · 23 Sep"
      (13px #334155) — plain text, no green box.
   b. TRIP — read-only fact rows, label 13px #64748B left / value 14px/600 #0F172A right:
      Requester — Mary Akinyi · Public Works; Route — Nakuru HQ → Nakuru Sub-County Office;
      Departure — Today 10:30 · return 15:00; Passengers — 3 · ~64 km.
   c. ASSIGNED — two rows, divider between, each with a "Change" text link (#006837) on the
      right:
      [72×48 photo of a Toyota Land Cruiser — reuse the one on this page] "KBZ 442A · Toyota
      Land Cruiser" + beneath "Nakuru HQ Yard · Bay 4" 13px #64748B;
      [40px avatar] "Joseph Mutua" + beneath "County driver · on duty" 13px #64748B.
   d. DISPATCH READINESS — label + "4 of 5 checks passed" (13px/600 #B91C1C) on the right.
      One collapsed row: chevron ">" + check icon #059669 + "4 checks passed" (14px #334155).
      Then the failing check, expanded: x-circle #B91C1C + "Vehicle availability" (14px/600
      #0F172A) + chip "Fail" (#B91C1C on #FEF2F2); beneath: "KBZ 442A is grounded for
      maintenance (brake pads) since 11 Sep" (13px #B91C1C).
   e. "Notes for the driver (optional)" — single text field, 72px tall.
   f. DECISION FOOTER, pinned to the pane bottom, one row:
      left: text link "Return to requester" (14px/600 #334155);
      right: secondary button "Request override" (white, 1px #006837 border, #006837 text) and
      primary button "Confirm dispatch" DISABLED (#E2E8F0 fill, #64748B text).
      One helper line above the buttons, 13px #64748B: "Dispatch is blocked by 1 failed check.
      An override goes to Grace Wanjiru (Fleet Manager) for approval."
      Remove the amber banner, the red sentence and "Reject Request".

6. SECOND FRAME: duplicate the finished frame, place it 120px right, name it
   "v2 / dispatch-queue / ready-with-warning". In the copy, select REQ-2024-0853 (John Kamau,
   Health, KCE 558A · Nissan X-Trail, driver Faith Cherotich) and change only the detail pane:
   - Readiness: "5 of 5 checks passed · 1 warning" (13px/600 #B45309). Collapsed row
     "4 checks passed"; then expanded: alert-triangle #B45309 + "Insurance" + chip "Expiring"
     (#B45309 on #FFFBEB); beneath "Policy expires 29 Sep, after this trip returns. Renewal in
     progress." (13px #64748B).
   - Footer: "Return to requester" link left; only the primary "Confirm dispatch" ENABLED
     (#006837 fill, white text) on the right. No override button (nothing failed).
   - Helper line: "Warnings don't block dispatch. This one will be logged."
```

**Check after render:**
- Exactly one active sidebar item.
- Stage tabs match the Today pipeline names and counts.
- About 9 rows visible, with no "Routine" chips.
- Passed checks collapsed to one row.
- The blocked frame: Confirm disabled, override helper names Grace.
- The warning frame: Confirm enabled.
- No Reject button.
- No boxes inside cards.

### 8i. Render check after §8h (2026-09-24): T1 ready to lock after polish

**Landed:**
- Top alert card removed; LIVE NOW is the first group, with vehicle photos.
- The photo-vs-icon row rule works.
- Top bar: search on the left, no title.
- Breadcrumb "Operations / Fleet overview".
- One header row: greeting, scope ▾, and the stamp with the date.
- Fuel number and budget share a baseline; caption left-aligned.
- Neutral "47" pill.
- Watch list edges fixed.

**Density:** 5 blocks, no repeated numbers.

**Five-second read:** the eye lands on the red live-alert types, "Grounded 23", and amber "Needs
driver". These are the right priorities.

**Remaining polish:**
1. **Default state:** this frame shows "Insurance expired" expanded. The spec had it collapsed in
   the main frame and expanded only in the `/group-expanded` copy. Expanded, the left column ends
   ~160px below the right; collapsed, they balance.
2. **Group icons are inconsistent:** Insurance expired and Inspection expired share the same
   filled dark "!" circle, while the other groups use outline icons (wrench, clock, shield). All
   group icons should be outline #64748B in a #F8FAFC circle: shield-x, clipboard-x, wrench,
   calendar-clock, shield.
3. **Group spacing:** "82 unreviewed GPS events →" runs straight into "BLOCKING DISPATCH NOW"
   with no gap. Put 24px above every group label.
4. **Tab labels** in Needs attention render larger (16px) than the rest of the UI. They should be 14px.
5. **Failed twice → direct `use_figma` edit:**
   - The fuel anomaly icon is still a sliders icon; it should be a flag.
   - The stray divider line under "2 anomalies to review" is still there.

---

## 10. Live app — "Requests" page (Fleet Manager login), audit (2026-09-24)

Source: a full-page capture, 3420×21,206px (~21,000px tall at 1×). Nav item "Requests", logged in
as `fleet`.

**What's on it, top to bottom:**
1. "Action queue · 40 in workflow": a 40-row table (Request, Destination, Step), unpaginated, with
   a request-detail pane on the right.
2. Three KPI tiles: Awaiting approval 0 / Approved & upcoming 0 / Returned 0.
3. A dark "Need a vehicle?" promo card.
4. "My requests": 104 requests as cards with unlabeled 5-dot steppers; "Page 1/3", but it seems to
   render far more than one page.
5. A right rail: New transport request form, Drafts, Upcoming trips.

| # | Step | Finding | Severity |
|---|---|---|---|
| 1 | Job | Three jobs stacked on one page: an oversight queue of everyone's requests, the Fleet Manager's own requests (a Requester job), and a create form. ~21,000px of scroll | **Critical** |
| 2 | Template | Should be split: **T3 Requests registry** (oversight) + **T9 New request** (via a header button) + "Mine" as a filter, not a second page underneath | **Critical** |
| 3 | Tiering | The promo card, Drafts and Upcoming trips (for someone else's role) are tier 3 or not this persona's content | Med |
| 4 | Density | 40 unpaginated rows + ~100 cards; each card ~150px for 4 facts; "Page 1/3" while showing far more | High |
| 5 | Patterns | 5-dot steppers have **no labels**, so they can't be read. The queue has no departure column and no sort; the one fact that sets urgency is missing | High |
| 6 | Connections | "Action queue" shows items the Fleet Manager can't act on: the detail pane says "No action for your role at this step." The Today pipeline and approvals should land on a view filtered to what she oversees or acts on | High |
| 7 | Vocabulary & data | **Two vocabularies:** queue steps (Supervisor approval, Transport review, Allocate vehicle, Ready to dispatch) vs card statuses (PENDING, APPROVED, READY, COMPLETED, RETURNED, REJECTED, DISPATCHED). Neither matches the lifecycle in `13` §6a. IDs in two formats (REQ-66359814 / REQ-56697450-37); ISO dates; vague destinations ("HQ", "Yard", "Field office"); test data everywhere (QA Pass3, Authz test, Self approve, Return me, Reject me, Nowhere, John Officer, Jane Transport) | High |
| 8 | Rules | **Gate checks show FAIL for things not yet assigned** ("Driver licence valid: FAIL, no driver assigned") on a request that's still at supervisor approval. "Not assigned yet" isn't a failure. **KPI tiles say 0 / 0 / 0** while the list below shows many pending, ready and returned requests. **Stale requests:** departures on 12–13 Sep (today is 24 Sep) still "pending", with nothing flagging it. A test request named "Self approve" exists, so self-approval blocking needs verifying | **Critical** |
| 9 | Header (P0) | Same header issues as Today: "Good afternoon, Fleet" greeting on a work page, "Search inventory", standalone Sign out, no breadcrumb/title | Med |

**Dev-side issues (not design):**
- KPI tiles counting 0.
- Pagination not applied.
- Checks evaluated as FAIL before assignment.
- Stale requests not expiring.
- Two ID formats.
- Test/seed data in the environment.
- Confirm that self-approval is blocked server-side.

### 10a. Proposed structure

**Requests (Fleet Manager) = T3 Registry + T8 drawer:**
- **Page header (P0):** breadcrumb "Operations / Vehicle requests", title "Vehicle requests",
  right: primary button "New request" (opens T9).
- **Stage tabs** using the one lifecycle vocabulary, with counts: Awaiting approval · Transport
  review · Needs driver · Ready · Dispatched · On trip · Closed · Returned/Rejected · All. The
  Today pipeline segments land on these tabs.
- **Filter row (P3):** station · department · departure date · "Mine" toggle · search.
- **Table:** Request (ID + requester · department) · Route · Departure (sortable, default soonest) ·
  Stage chip · Time in stage (amber when > 1 day) · "Your action" column: shows "Approve" or
  "Allocate" only when *this* user can act. Otherwise it's empty, and rows with no action for the
  viewer are clearly passive.
- **Stale rule:** departure passed and not dispatched → chip "Departure passed" (red). These also
  count in Today's Needs attention.
- **Row click → T8 drawer:**
  - Labeled lifecycle stepper (new pattern **P17**).
  - Trip facts and assigned resources (P13 with photo).
  - Gate checks only once the request reaches allocation. Before that, each check shows the
    neutral state "Not yet assigned" (new 4th state for **P12**).
- **Paginate at 25.**

**My requests (Requester, Mary) = Requester home:** same table component filtered to the viewer's
own requests. Each card or row shows the **current stage as text** ("Step 3 of 5 · Driver
assigned"), with the labeled stepper in the drawer. Honest tiles only if they reconcile with the
list.

**New request = T9 form**, one column:
- Destination is a location picker, not free text.
- Date/time pickers from the design system, not native.
- Vehicle type as a select.
- Estimated cost is auto-calculated or removed from the requester's form.

### 10b. Simplified structure (supersedes §10a), checked against the two standing goals

**User-first:** the page opens on what's waiting on the viewer, then what's stuck, then reference.

**Reuse map (every section comes from an existing part):**

| Section | Reused from |
|---|---|
| Top bar, sidebar, page header | Today v3 (P0) |
| Stage strip | Today's Dispatch-oversight pipeline (P8), widened to 5 stages |
| Needs attention · Waiting on you | Today's approval rows (P9) |
| Stuck / Departure passed | Today's Needs-attention group rows (P6) |
| Requests table | Table Header/Data Cell components + Status Pill (T3) |
| Search/filters | Filter Dropdown (P3) |
| Row click | Action drawer (T8), existing override-review layout |

**New:** only "Time in stage" as a table column, which later registries (Compliance, Fuel) will
reuse.

**Density:** 4 blocks (header, strip, needs attention, table), 5 columns, 25 rows per page.

### 10c. Prompt — Vehicle requests (Fleet Manager) v1

```
On the "Refined" page, create a new desktop frame 1776px wide next to
"v3 / fleet-operations-overview", named "v1 / vehicle-requests". Build it by REUSING elements
from "v3 / fleet-operations-overview": copy its sidebar, top bar, page-header layout, pipeline
strip, approval rows, group rows, card style and typography exactly — do not restyle them.

1. SHELL: copy the sidebar (Operations expanded; the ONLY active item is "Vehicle Request") and
   the top bar (search left, bell, "Grace Wanjiru / County Fleet Manager").

2. PAGE HEADER (same layout as v3): breadcrumb "Operations / Vehicle requests"; title "Vehicle
   requests" (Lexend 24px/600); on the right of the title row, a primary button "+ New request"
   (#006837 fill, white text 14px/600, 40px tall, 8px radius). No tabs.

3. STAGE STRIP: copy the arrow-segment pipeline strip from v3's "Dispatch oversight" card,
   place it full width directly under the header (no card around it), with 5 segments:
   "Awaiting approval" 12 · "Transport review" 6 · "Needs driver" 5 (amber tint, "oldest 2
   days") · "Ready" 9 · "Awaiting driver" 8. Under it, 13px #64748B: "40 in progress · select a
   stage to filter the list below".

4. NEEDS ATTENTION card (same card style and group-row style as v3's Needs attention), title
   "Needs attention" + neutral count "15":
   - Group "WAITING ON YOU · 3" (#B45309 label): copy v3's three approval rows exactly
     (Dispatch override · REQ-2024-0851 / Dispatch override · REQ-2024-0847 / Vehicle transfer ·
     KCE 558A) with their green-outline "Review" buttons.
   - Group "STUCK · 5" (#B45309 label): one collapsed group row (chevron left, clock icon in a
     #F8FAFC circle): "Stuck for more than 1 day" — "5 requests, longest 3 days in Needs
     driver" — neutral chip 5 — >.
   - Group "DEPARTURE PASSED · 7" (#B91C1C label): one collapsed group row (calendar-x icon):
     "Departure date passed, never dispatched" — "7 requests to close or reschedule" — neutral
     chip 7 — >.

5. ALL REQUESTS card: title "All requests" + " · 104" (13px #64748B). On the right of the title
   row: a search field "Search requests" (240px), a Filter Dropdown "All stations ▾", and a text
   button "More filters".
   Table (Table Header Cell / Table Data Cell components), header row 12px/600 uppercase
   #64748B on #F8FAFC, rows 56px with divider lines, no boxes:
   REQUEST (ID 14px/600 #0F172A, beneath "requester · department" 13px #64748B) · ROUTE ·
   DEPARTURE (sortable, arrow ↑ shown, default soonest) · STAGE (Status Pill with icon, sentence
   case) · IN STAGE (right-aligned; amber #B45309 when over 1 day).
   Rows:
   REQ-2024-0851 · Mary Akinyi · Public Works | Nakuru HQ → Nakuru Sub-County Office | Today 10:30 | Ready | 2 h
   REQ-2024-0853 · John Kamau · Health | Nakuru HQ → Naivasha District Hospital | Today 11:00 | Ready | 5 h
   REQ-2024-0849 · Sarah Njeri · Agriculture | Molo Station → Gilgil Field Station | Today 13:00 | Needs driver | 2 days
   REQ-2024-0852 · Peter Omondi · Education | Nakuru HQ → Molo Teachers Centre | Today 14:30 | Awaiting driver | 40 min
   REQ-2024-0856 · Ruth Wambui · Finance | Nakuru HQ → County Treasury Annex | Tomorrow 08:00 | Transport review | 3 h
   REQ-2024-0857 · David Kiprop · Water & Sanitation | Njoro → Rongai Borehole Site | Tomorrow 09:00 | Awaiting approval | 1 day
   REQ-2024-0859 · Faith Chelimo · Public Works | Nakuru HQ → Bahati Ward Office | Tomorrow 10:00 | Awaiting approval | 6 h
   REQ-2024-0862 · Hassan Juma · Roads | Naivasha → Mai Mahiu Road Works | Fri 26 Sep 07:30 | Transport review | 20 min
   Footer: "1–25 of 104" and Prev / Next.
   Stage pill colors: Awaiting approval / Transport review / Awaiting driver = grey (waiting on
   someone else); Needs driver = amber; Ready = green tint.
```

**Check after render:**
- Pipeline strip, approval rows and group rows are visually identical to Today v3 (proves reuse).
- One active sidebar item.
- 4 blocks, 5 columns.
- The only amber is Needs driver and the in-stage times over 1 day; the only red is Departure passed.

### 10d. Render check — `v1 / vehicle-requests` (2026-09-24)

**Landed:**
- Page header: breadcrumb, title, "+ New request".
- Full-width pipeline strip, identical to Today's, with Needs driver amber; counts sum to 40.
- "Waiting on you" approval rows identical to Today's, with green "Review" buttons.
- Table: 5 columns, departure sorted, amber "2 days", "1–25 of 104" with Prev/Next.
- Stage pills colored by meaning.
- Density: 4 blocks. **Reuse proven**: the strip and approval rows match Today.

**Findings:**
1. **Long rows again (the same problem the user flagged on live alerts):** Needs attention is full
   width, so "Review" sits ~1,500px from its text. Fix: keep ONE card but split it inside into two
   columns: "Waiting on you" (62%) | "Follow up" (38%), with a vertical divider.
2. **A number is shown twice:** each single-row group repeats its count ("STUCK · 5" label, then
   "…5" chip in the row; same for "DEPARTURE PASSED · 7"). Fix: merge both into one group
   "FOLLOW UP · 12" with two rows, where each row carries its own count.
3. **Two searches:** the top bar changed to page-specific ("Search requests, routes, or
   requester") and the table has its own search. The top bar is global (P0), so restore "Search
   vehicles, requests, drivers" there and keep the table search.
4. **Two active sidebar items:** "Fleet Overview" renders bold/white alongside the "Vehicle
   Request" chip. Only Vehicle Request should be active.
5. **The table doesn't use the full width:** columns end at ~1,410px, leaving ~500px empty on the
   right, and rows have no "open" affordance. Fix: spread the columns across the width and add a
   ">" chevron column (the row opens the T8 drawer).
6. **Stage pills have no icons** (rule: icon + text on every chip).
7. **Controls are inconsistent:**
   - The table search is oversized and shows a clear (x) while empty.
   - "More filters" is a green-outline button, identical to "Review", so it competes with
     real actions. Make it a neutral text button.
   - A stray vertical divider sits left of "+ New request".
8. **Group icons are filled/dark again** (same as Today §8i item 2). They should be outline
   #64748B in #F8FAFC circles.

**Carries to the pattern library:** a Needs-attention card on a full-width page splits into two
internal columns (actions | follow-ups) rather than stretching rows. Add this to P6 in `13`.

### 10e. Fix prompt — vehicle requests v1

```
On "v1 / vehicle-requests" (Refined page), make only these fixes:

1. Top bar search placeholder back to the global text "Search vehicles, requests, drivers".
2. Sidebar: only "Vehicle Request" is active (green chip). "Fleet Overview" in normal weight
   #CBD5E1 like the other sub-items.
3. Remove the thin vertical divider to the left of "+ New request".
4. NEEDS ATTENTION card — keep it one card but split its content into two columns with a 1px
   #E2E8F0 vertical divider between them (24px padding each side):
   - Left column (62%): "WAITING ON YOU · 3" with the same 3 approval rows and "Review" buttons.
   - Right column (38%): one group label "FOLLOW UP · 12" (12px/600 uppercase #B45309) and two
     rows (same group-row style: left chevron, 28px #F8FAFC circle with a 20px OUTLINE #64748B
     icon, title 14px/600, detail 13px #64748B, neutral count chip, ">" at the right):
     · clock icon — "Stuck over 1 day" — "longest 3 days in Needs driver" — 5
     · calendar-x icon — "Departure passed" — "never dispatched · close or reschedule" — 7
   - Delete the separate "STUCK · 5" and "DEPARTURE PASSED · 7" labels and rows.
   - Title count stays "15".
5. ALL REQUESTS table:
   - Columns spread across the full card width: REQUEST 24% · ROUTE 30% · DEPARTURE 14% ·
     STAGE 16% · IN STAGE 10% (right-aligned) · a 40px column with a ">" chevron (#64748B) on
     every row.
   - Stage pills get a 12px icon before the text: Ready = arrow-right; Needs driver = user-x;
     Awaiting driver = clock; Transport review = eye; Awaiting approval = hourglass.
   - Search field: 36px tall, 14px placeholder, no clear icon when empty.
   - "More filters": neutral text button (#334155 14px/600, filter icon), no border.
```

### 10f. Goal check against the live page itself (2026-09-24)

Re-read of the live capture (right rail, detail pane, tile captions), to confirm what the page is
built for rather than what we assumed.

**What the page's own content says it's for:**

| Evidence on the page | Job it serves | Whose job |
|---|---|---|
| "Need a vehicle?" card + New transport request form + Save draft + Drafts | Create a request | **Requester** |
| Tiles: "Awaiting approval · With your HOD / Transport", "Approved & upcoming · Vehicle allocated", "Returned · Needs correction" | Track *my* requests, fix returned ones | **Requester** |
| "My requests" cards with 5-step progress; "Upcoming trips" | Track my requests and trips | **Requester** |
| "Action queue · 40 in workflow" + detail pane with lifecycle steps and checks; "No action for your role at this step" | See every request in the workflow and act where my role allows | **Workflow roles** (approver, transport, fleet) |

**Conclusion:**
- The live "Requests" page is primarily the **Requester's workspace**. That matches the test
  accounts, where `requester` lands on "Requests" to create, edit, submit, cancel, track, correct
  and resubmit.
- A **workflow action queue** is layered on top for staff roles.
- Logged in as Fleet Manager, Grace gets both. The requester half is mostly irrelevant to her, and
  the queue half mostly says "no action for your role".

**Confirmed goals, by role:**
- **Requester (Mary):** create a request; know where each one is; fix returned ones; see upcoming
  trips.
- **Workflow roles:** clear the steps *they* can act on; see where everything else is.
- **Fleet Manager (Grace):** oversight of the workflow + the escalations addressed to her.
  Creating her own request is occasional.

**What the page doesn't show:**
- Which lifecycle steps a Fleet Manager can act on. Allocation? Overrides only? **Open question
  for the dev team / product owner.** It decides how big "Waiting on you" is.
- "Coverage / demand vs capacity" (§10 follow-up) is **not in the live app**. It's a proposed
  addition, not a confirmed goal.

**Design consequence:** split the page by role instead of stacking.
- **Requester** → a "My requests" home (T3 filtered to mine): returned-for-correction first, then
  in progress, then upcoming trips; "+ New request" opens the form (T9).
- **Workflow roles, including Grace** → the §10c layout: "Waiting on you" first, then stuck /
  follow-up, then the table. Their own requests sit behind a "Mine" filter; "+ New request" stays
  in the header.

### 10g. Prompt — "Requests & trips" v2 (revised 2026-09-25 after the SRS check, `13` §11a) (Fleet Manager, List layout) + request detail drawer

Applies decisions D5–D10 in `13` §11. This supersedes the §10e fix prompt; the §10e fixes are
folded in here.

```
On the "Refined" page, duplicate "v1 / vehicle-requests", place the copy 120px to its right,
name it "v2 / requests-and-trips", and work on the copy. Keep all existing styles, the pipeline
strip style, approval-row style, group-row style and table components — reuse, don't restyle.

1. NAVIGATION (edit the main component "Navigation/Sidebar", variant "Active Section=Operations",
   so every screen updates): Operations sub-items become exactly three:
   "Fleet Overview" · "Requests & Trips" · "Vehicle Allocation".
   Remove "Vehicle Request", "Dispatch Management", "Journey Management" (merged into
   "Requests & Trips").
   In this frame, "Requests & Trips" is the ONLY active item.
   Top bar search placeholder: "Search vehicles, requests, drivers".

2. PAGE HEADER: breadcrumb "Operations / Requests & trips"; title "Requests & trips";
   right side of the title row: a segmented toggle "List | Queue" (List selected; 32px tall,
   #F8FAFC track, selected segment white with 1px #E2E8F0 border) and the primary button
   "+ New request". No divider line before the button.

3. STAGE STRIP: same arrow-segment strip, now 7 segments:
   "Awaiting approval" 12 · "Transport review" 6 · "Needs vehicle" 3 (amber tint) ·
   "Needs driver" 5 (amber tint, "oldest 2 days") · "Driver check-in" 8 · "Ready" 9 ·
   "On trip" 118. Caption under it: "43 before departure · 118 on trip · select a stage to
   filter". A small text link "Closed & returned →" right-aligned on the caption line.

4. NEEDS ATTENTION — one card, two internal columns separated by a 1px #E2E8F0 vertical line:
   Left (62%): "WAITING ON YOU · 4" (#B45309) — same approval-row style, green-outline buttons:
   · "Dispatch override · REQ-2024-0851" / "KBZ 442A grounded · requested by Daniel Otieno · 10 min
     ago" — [Review]
   · "Dispatch override · REQ-2024-0847" / "Licence class mismatch · Daniel Otieno · 1 h ago" — [Review]
   · "Station short of vehicles · Molo" / "2 requests waiting 2 days for a vehicle · escalated by
     Daniel Otieno" — [Move a vehicle]
   · "Vehicle transfer · KCE 558A" / "Health → Public Works · Alice Njoroge · 3 h ago" — [Review]
   Right (38%): "FOLLOW UP · 11" (#B45309), two group rows (left chevron, 28px #F8FAFC circle with
   OUTLINE #64748B icon, title, detail, neutral count, ">"):
   · hourglass — "Approval over 1 day" — "waiting on department heads" — 4
   · calendar-x — "Departure passed" — "never dispatched · close or reschedule" — 7
   Title count: "15".

5. ALL REQUESTS table (keep rows and data from v1), with fixes:
   columns across the full width: REQUEST 24% · ROUTE 30% · DEPARTURE 14% · STAGE 16% ·
   IN STAGE 10% right-aligned · 40px column with ">" on every row.
   Change REQ-2024-0849's stage to "Needs vehicle". Stage pills get a 12px icon: Awaiting
   approval = hourglass; Transport review = eye; Needs vehicle = car-off; Needs driver = user-x;
   Ready = arrow-right; Driver check-in = clock. Needs vehicle and Needs driver are amber; Ready
   green tint; the rest grey.
   Search field 36px tall, no clear icon when empty; "More filters" = neutral text button with a
   filter icon, no border.

6. SECOND FRAME — the shared request detail as a drawer. Duplicate the finished frame, place it
   120px to the right, name it "v2 / requests-and-trips / detail-drawer". In the copy, add a
   #0F172A 30% overlay over the page and a 560px white drawer from the right edge (full height,
   24px padding, 24px between sections, left border 1px #E2E8F0), showing REQ-2024-0851:
   a. Top row: "REQ-2024-0851" (Lexend 20px/600) + chip "Override requested" (#B45309 on
      #FFFBEB, alert icon); close "×" on the right. Beneath: "Mary Akinyi · Public Works ·
      approved by James Mwangi, 23 Sep" (13px #64748B).
   b. LIFECYCLE STEPPER (labeled, horizontal, 7 small steps with labels under each): Approved ✓ ·
      Transport review ✓ · Vehicle ✓ · Driver ✓ · Driver check-in ✓ · Ready (current, amber
      ring) · On trip. Completed steps #006837; upcoming #E2E8F0 with #64748B labels.
   c. TRIP facts (label left 13px #64748B / value right 14px/600 #0F172A): Route — Nakuru HQ →
      Nakuru Sub-County Office; Departure — Today 10:30 · back 15:00; Passengers — 3 · ~64 km.
   d. ASSIGNED: [72×48 Land Cruiser photo] "KBZ 442A · Toyota Land Cruiser" / "Grounded since
      11 Sep · brake pads" (13px #B91C1C); [40px avatar] "Joseph Mutua" / "County driver · on duty".
   e. DISPATCH READINESS "4 of 5 passed": collapsed row "✓ 4 checks passed"; expanded failing
      row: x-circle #B91C1C "Vehicle availability" + chip "Fail" — "Grounded for maintenance
      (brake pads) since 11 Sep".
   f. OVERRIDE REQUEST: label "Daniel Otieno's justification" (13px/600 #334155); quote text on
      #F8FAFC, 8px radius, 12px padding: "Urgent medical supply delivery — maintenance
      rescheduled to tomorrow, brake pads replaced yesterday."
   g. SUGGESTED ALTERNATIVE (a tinted notice, #E6F2EB background, 8px radius, 12px padding, car
      icon #006837): "KCE 558A · Toyota Land Cruiser is available at Nakuru HQ." + text link
      "Deny and suggest KCE 558A →" (#006837 14px/600) — sends the request back to Daniel
      Otieno with this vehicle suggested.
   h. DECISION FOOTER pinned to the drawer bottom: left text link "Deny override" (#B91C1C
      14px/600); right primary button "Approve override" (#006837). Helper above, 13px #64748B:
      "Approving is logged to the audit trail. You can't approve an override you requested."
```

**Check after render:**
- The sidebar component shows 3 Operations items on every screen that uses it.
- 7-stage strip; Needs vehicle and Needs driver are amber.
- "Waiting on you" has 4 rows including the reallocation.
- The drawer shows a labeled stepper, the grounded vehicle in red, the justification quote, the
  reallocation suggestion, and a footer with only the Fleet Manager's actions.

### 10h. The remaining Requests & trips views (frames 3–6)

Run §10g first (frames 1–2). Each prompt below starts from the frame it builds on, and reuses its
parts unchanged. Stage order everywhere is D11: Awaiting approval · Transport review · Needs
vehicle · Needs driver · Driver check-in · Ready · On trip.

**Selected-stage style (used in frames 3–5):** the selected segment of the stage strip is white
with a 2px #006837 outline, and its label and count are #006837.

#### Frame 3 — Queue, Transport Ops (Daniel)

```
On the "Refined" page, duplicate "v2 / requests-and-trips", place the copy 120px below it, name
it "v2 / requests-and-trips / queue-transport", and work on the copy. Reuse every existing style.

1. IDENTITY: Top Bar shows "Daniel Otieno / Transport Operations Officer". Sidebar: Operations
   expanded, "Requests & Trips" active.
2. HEADER: same breadcrumb and title; the "List | Queue" toggle now has "Queue" selected. Keep
   "+ New request".
3. STAGE STRIP: same 7 segments and counts; the "Ready" segment is SELECTED (selected-stage
   style). Caption: "Showing Ready · 9".
4. Replace everything below the strip with a SPLIT PANE: left list 44% width, right detail pane
   56% width, both white cards, 24px gap, top-aligned, same height (fill to the bottom of the
   frame).
5. LEFT LIST (compact rows, 72px, divider lines, no boxes):
   - Group label "RETURNED TO YOU · 1" (12px/600 uppercase #B45309), one row:
     "REQ-2024-0851 · Mary Akinyi · Public Works" (14px/600) — right "Today 10:30";
     line 2: "Override denied by Grace Wanjiru · suggested KCE 558A" (13px #B45309).
   - Group label "READY · 9" (12px/600 uppercase #64748B), rows (line 1 ID · requester ·
     department, right departure; line 2 route in 13px #64748B; an "Urgent" chip with a flag
     icon only where marked):
     REQ-2024-0853 · John Kamau · Health — Today 11:00 — Nakuru HQ → Naivasha District Hospital — Urgent  [SELECTED: #E6F2EB background + 3px #006837 left bar]
     REQ-2024-0855 · Sarah Njeri · Agriculture — Today 13:00 — Molo Station → Gilgil Field Station
     REQ-2024-0858 · Peter Omondi · Education — Today 14:30 — Nakuru HQ → Molo Teachers Centre
     REQ-2024-0860 · Ruth Wambui · Finance — Tomorrow 08:00 — Nakuru HQ → County Treasury Annex
     REQ-2024-0861 · David Kiprop · Water & Sanitation — Tomorrow 09:00 — Njoro → Rongai Borehole Site
     REQ-2024-0864 · Faith Chelimo · Public Works — Tomorrow 10:00 — Nakuru HQ → Bahati Ward Office
6. RIGHT DETAIL PANE — the SAME request-detail layout as the drawer in
   "v2 / requests-and-trips / detail-drawer" (reuse it), for REQ-2024-0853, docked (no overlay,
   no close ×):
   a. "REQ-2024-0853" + chip "Ready" (arrow icon, #006837 on #E6F2EB). Beneath: "John Kamau ·
      Health · approved by Dr. Achieng Otieno, 23 Sep".
   b. Labeled stepper: Approved ✓ · Transport review ✓ · Vehicle ✓ · Driver ✓ · Driver check-in ✓
      · Ready (current, green ring) · On trip.
   c. Trip facts: Route — Nakuru HQ → Naivasha District Hospital; Departure — Today 11:00 ·
      back 17:00; Passengers — 2 · ~92 km; Cargo — medical supplies.
   d. Assigned: [Nissan X-Trail photo] "KCE 558A · Nissan X-Trail" / "Nakuru HQ Yard · Bay 2" +
      "Change" link; [avatar] "Faith Cherotich" / "County driver · checked in 09:52" + "Change".
   e. DISPATCH READINESS: "6 of 6 passed · 1 warning" (13px/600 #B45309).
      Collapsed row "✓ 5 checks passed" (Vehicle available · Inspection certificate valid ·
      Driver active & licensed (checked at assignment) · Approved request linked · Pre-trip
      inspection completed 09:52 · fuel ¾).
      Expanded row: alert-triangle #B45309 "Insurance" + chip "Expiring" (#B45309 on #FFFBEB) —
      "Expires 29 Sep, after this trip returns. Renewal in progress."
   f. "Notes for the driver (optional)" single field, 72px.
   g. DECISION FOOTER (pinned): left text link "Return to requester" (#334155 14px/600); right
      primary "Dispatch" (#006837 fill, white). Helper above: "Warnings don't block dispatch.
      This one will be logged."
```

#### Frame 4 — Queue, Approver (Head of department)

```
Duplicate "v2 / requests-and-trips / queue-transport", place it 120px to its right, name it
"v2 / requests-and-trips / queue-approver", and change only:

1. IDENTITY: "James Mwangi / Head of Public Works · Approver". Sidebar shows only Operations →
   "Requests & Trips" (approvers see no other modules).
2. HEADER: title "Requests & trips", subtitle under the breadcrumb row 13px #64748B:
   "Public Works department". "Queue" selected. Remove "+ New request".
3. STAGE STRIP: "Awaiting approval" is SELECTED and shows 4 (this department's count); the other
   segments show this department's counts in #64748B: 2 · 1 · 0 · 1 · 2 · 9.
4. LEFT LIST: one group "AWAITING YOUR APPROVAL · 4", rows:
   REQ-2024-0859 · Faith Chelimo — Tomorrow 10:00 — Nakuru HQ → Bahati Ward Office  [SELECTED]
   REQ-2024-0863 · Samuel Korir — Tomorrow 14:00 — Nakuru HQ → Subukia Road Works
   REQ-2024-0865 · Grace Achieng — Fri 26 Sep 08:00 — Nakuru HQ → Lanet Depot
   REQ-2024-0868 · Paul Mwangi — Mon 29 Sep 09:00 — Nakuru HQ → Rongai Ward Office
   The fourth row's department line shows "same surname as you · check conflict" in 13px
   #B45309 (a maker-checker cue).
5. RIGHT PANE (same detail layout), REQ-2024-0859:
   a. "REQ-2024-0859" + chip "Awaiting approval" (hourglass, grey). Beneath: "Faith Chelimo ·
      Public Works · submitted 23 Sep, 16:10".
   b. Stepper: Approval (current) · Transport review · Vehicle · Driver · Driver check-in · Ready
      · On trip.
   c. Trip facts: Purpose — Ward office inspection, quarterly; Route — Nakuru HQ → Bahati Ward
      Office; Departure — Tomorrow 10:00 · back 14:00; Passengers — 3 · ~38 km;
      Authorization — Operational (no budget commitment).
   d. Replace "Assigned" and "Dispatch readiness" with one grey line: "Vehicle, driver and
      dispatch checks happen after your approval." (13px #64748B, info icon).
   e. "Comment (required to return or reject)" single field, 72px.
   f. DECISION FOOTER: left text link "Reject" (#B91C1C); right secondary "Return for
      correction" (white, 1px #006837 border) and primary "Approve" (#006837). Helper: "You
      can't approve a request you submitted. Your decision is logged."
```

#### Frame 5 — My requests, Requester (Mary)

```
Duplicate "v2 / requests-and-trips" (the Fleet Manager List frame), place it 120px below the
approver frame, name it "v2 / requests-and-trips / my-requests", and change it to the
requester's view:

1. IDENTITY: "Mary Akinyi / Public Works · Staff". Sidebar shows only "Requests & Trips".
2. HEADER: breadcrumb "Requests & trips"; title "My requests"; right: "+ New request" primary.
   No toggle, no stage strip.
3. NEEDS YOUR ACTION card (same group-row style), title "Needs your action" + count 1:
   one approval-style row: "Returned for correction · REQ-2024-0850" / "Transport: add the
   passengers' names and phone numbers · Daniel Otieno · 2 h ago" — green-outline button
   [Correct].
4. NEXT TRIP card (one compact row, same vehicle-row style): [Land Cruiser photo]
   "Today 10:30 · Nakuru HQ → Nakuru Sub-County Office" (14px/600) / "REQ-2024-0851 · driver
   Joseph Mutua · vehicle being confirmed" (13px #64748B) — chip "Ready · awaiting vehicle"
   (#B45309 on #FFFBEB, clock icon).
5. MY REQUESTS table (same table components): columns REQUEST (purpose 14px/600 + ID 13px
   #64748B) · ROUTE · DEPARTURE · PROGRESS · UPDATED, with ">" on each row. PROGRESS shows the
   step as text + a thin 4px bar: e.g. "Step 3 of 7 · Needs vehicle" with the bar 3/7 filled
   #006837. Rows:
   Site inspection · REQ-2024-0851 | Nakuru HQ → Nakuru Sub-County Office | Today 10:30 | Step 6 of 7 · Ready | 10 min ago
   Passenger list update · REQ-2024-0850 | Nakuru HQ → Bahati | Fri 26 Sep | Returned for correction (amber) | 2 h ago
   Road survey · REQ-2024-0869 | Nakuru HQ → Mbaruk | Tue 30 Sep | Step 1 of 7 · Awaiting approval | 1 day ago
   Quarterly review · REQ-2024-0812 | Nakuru HQ → Njoro | 18 Sep | Completed ✓ | 6 days ago
   Footer "1–4 of 4".
```

#### Frame 6 — New request form

```
Duplicate "v2 / requests-and-trips / my-requests", place it 120px to its right, name it
"v2 / requests-and-trips / new-request", and replace the content below the Top Bar:

1. HEADER: breadcrumb "Requests & trips / New request"; title "New vehicle request".
2. ONE-COLUMN FORM, 640px wide, left-aligned with the page content, in a white card (24px
   padding). Every field on its own row (never two inputs side by side). Labels 14px/600
   #0F172A, helper text 13px #64748B, inputs 44px tall, 8px radius, 1px #E2E8F0 border:
   - Purpose (text) — placeholder "e.g. Ward office inspection".
   - Destination — searchable picker with a map-pin icon, placeholder "Search county sites";
     helper "Choose a county site, or type an address".
   - Departure — date-and-time picker field "Wed 1 Oct · 09:00" with a calendar icon.
   - Expected return — date-and-time picker field "Wed 1 Oct · 15:00".
   - Passengers — number stepper "3", then a link "+ Add passenger names" (13px #006837).
   - Special requirements — three checkbox chips: "Wheelchair access" · "Cargo space" · "4×4".
   - Preferred vehicle type — select "Any suitable vehicle".
   - Project / activity — select "Quarterly ward inspections".
   - Supporting documents — dashed upload zone 96px tall: "Drop files or browse · PDF, JPG".
3. SUMMARY (read-only, #F8FAFC box inside the card is NOT allowed — use a plain divider, then
   two text lines 13px #334155): "Approval goes to James Mwangi, Head of Public Works." and
   "Estimated ~38 km · fuel about KES 1,900 (calculated, not entered)."
4. FOOTER in the card: left text button "Save draft" (#334155 14px/600); right primary
   "Submit request" (#006837).
```

**Check after all four render:**
- The detail pane in frames 3–4 is visibly the same component as the frame-2 drawer; only the
  footer and content differ.
- Each frame shows exactly one role's job, with no stacked sections from other roles.
- The stage order everywhere is Driver check-in → Ready → On trip.
- The requester's form keeps every input on its own row.

### 10i. Render check — frames 3–6 (Daniel queue, Approver queue, My requests, New request) (2026-09-25)

**Root cause of most issues:** the agent *regenerated* shared parts instead of reusing Today's.
The stage strip, chips, buttons, selected rows, stepper and sidebar all drifted between frames.
That's the case for building these as **real Figma components** (`13` §4) before more screens.

**Shared issues, found across frames (fix once):**
1. **Sidebar:**
   - The Approver and Transport frames still show the old items (Fleet Overview, Vehicle Request,
     Requests & Trips, Journey Management).
   - They show **2–3 green active items at once**.
   - The Approver sees every module.
   - The requester frame got it right: "Requests & Trips → My requests · My trips" is a good
     role-scoped nav pattern.
2. **Stage strip (breaks D11 and reuse):**
   - Flat boxes instead of Today's arrow segments.
   - Stages are wrong: an invented "Vehicle check", Ready placed *before* an extra "Awaiting driver".
   - Correct: Awaiting approval · Transport review · Needs vehicle · Needs driver · Driver check-in
     · Ready · On trip.
3. **Stepper labels differ per frame** ("Vehicle check / Driver check" vs Vehicle / Driver). The
   approver's current step shows a ✓ (done) instead of a current ring.
4. **Selected list row:**
   - The Approver frame uses a solid dark-green fill with dark text. It's **unreadable (contrast
     failure)**.
   - The Transport frame uses the correct tint + left bar.
5. **Boxes inside cards:** "Trip details" in a grey box, the "Returned to you" group in an amber
   box, the insurance warning in an amber bordered box, "5 checks passed" in a box.
6. **Chips in UPPERCASE** (READY, URGENT, RETURNED, CHECKED IN, EXPIRING); the rule is sentence case.
7. **Oversized pill buttons:** "+ New request" and "Submit request" are ~64px, fully rounded. The
   system button is 40px tall with an 8px radius.
8. **Helper text in amber** (footers); helper text is #64748B. Amber is only for "needs your action".

**Per-frame issues:**
- **Daniel's queue:**
  - The strip's selected state is a thin left line.
  - Otherwise the content is right: returned-with-suggestion row, checks summary, warning
    doesn't block, "Return to requester" as text.
- **Approver queue:**
  - The footer has three large equal buttons, with Reject as a red outlined button; spec: Reject
    as a text link.
  - The helper text is clipped at the right edge.
  - The comment field renders as a stray circle.
  - An unspecified "Urgent" chip.
  - The full 7-stage fleet strip is noise for an approver (per ClickUp: tabs by their decision
    states).
- **My requests:**
  - Good structure.
  - Group label + row title both say "Returned for correction".
  - A second "My requests" heading on the table card.
  - The table ends ~400px short of the card edge.
- **New request:**
  - Placeholders and helper text are **green** (they look like entered values).
  - All three special-requirement checkboxes are pre-checked, in **purple** (off-palette).
  - Clock icons on the date fields.
  - A 640px form beside ~900px of empty space.
  - No section headings, "(optional)" markers or Cancel.

**Decisions from the references:**
- **Approver strip → decision tabs:** "To review (4) · Returned (1) · Approved · All".
- **Form → sectioned + live summary card on the right:**
  - Sections: Trip / People & needs / Supporting documents.
  - Summary card: "Goes to James Mwangi for approval · ~38 km · est. fuel KES 1,900 · you'll be
    notified at each step".
  - This fills the empty space with something useful.
- **Every decision button shows a toast that names the next step** ("Approved · sent to
  Transport (Daniel Otieno) for vehicle allocation").

### 10j. Fix prompts — frames 3–6

**Prompt A: consistency pass (all four frames). Run first.**

```
On the "Refined" page, apply these fixes to ALL FOUR frames: "v2 / requests-and-trips /
queue-transport", "… / queue-approver", "… / my-requests", "… / new-request". The reference for
every shared element is the frame "v3 / fleet-operations-overview" and "v2 / requests-and-trips":
COPY elements from there, do not redraw them.

1. SIDEBAR — one active item only, and role-scoped:
   - queue-transport: Operations → "Fleet Overview" · "Requests & Trips" (ACTIVE) · "Vehicle
     Allocation". Delete "Vehicle Request" and "Journey Management". Other pillars stay.
   - queue-approver: only one group "Requests & Trips" with sub-items "To review" (ACTIVE) ·
     "My requests" — same pattern as the requester frame. No other pillars.
   - my-requests / new-request: keep as is ("Requests & Trips" → "My requests" active · "My trips").
   Active item = the green chip; every other item normal weight #CBD5E1, no fill.

2. STAGE STRIP (queue-transport only): delete the current flat strip and paste a copy of the
   arrow-segment strip from "v2 / requests-and-trips". Segments, in this order:
   Awaiting approval 12 · Transport review 6 · Needs vehicle 3 · Needs driver 5 (amber, "oldest
   2 days") · Driver check-in 8 · Ready 9 · On trip 118. "Ready" SELECTED: white fill, 2px
   #006837 outline, label and count #006837. Caption "Showing Ready · 9".

3. STEPPER labels, identical in every frame: Approved · Transport review · Vehicle · Driver ·
   Driver check-in · Ready · On trip. Done = green circle with ✓; current = white circle with a
   2px ring (#006837, or #B45309 if blocked) and bold label; upcoming = #E2E8F0 outline circle,
   #64748B label. The approver's REQ-2024-0859 is at step 1: "Approval" current (ring, no ✓).

4. SELECTED LIST ROW (both queues): #E6F2EB background + 3px #006837 left bar, text stays
   #0F172A / #64748B. Never a solid dark fill.

5. NO BOXES INSIDE CARDS: remove the grey box around "Trip details", the amber box around the
   "Returned to you" group, the box around "5 checks passed", and the amber bordered box around
   the insurance warning. These become plain rows separated by 1px #E2E8F0 lines. The insurance
   row keeps only a #B45309 alert icon and an "Expiring" chip (#B45309 on #FFFBEB) for color.

6. CHIPS in sentence case with a 12px icon: "Ready", "Urgent", "Returned", "Checked in 09:52",
   "Expiring", "Awaiting approval", "Completed".

7. BUTTONS: every primary button is 40px tall, 8px corner radius, #006837 fill, white 14px/600
   text ("+ New request", "Submit request", "Dispatch", "Approve"). No pill shapes.

8. Helper text in footers: 13px #64748B (not amber), on its own line above the buttons, never
   clipped.
```

**Prompt B: per-frame fixes. Run after A.**

```
1. "… / queue-approver":
   - Replace the stage strip with decision tabs (Navigation/Tab Item): "To review (4)" active ·
     "Returned (1)" · "Approved" · "All". Keep the subtitle "Public Works department".
   - Remove the "Urgent" chip from REQ-2024-0859.
   - Comment field: one 72px text area with placeholder "Add a comment (required to return or
     reject)"; remove the stray circle.
   - Footer: left text link "Reject" (#B91C1C 14px/600, no border); right secondary "Return for
     correction" (white, 1px #006837 border, #006837 text) and primary "Approve". Helper line above:
     "You can't approve a request you submitted. Your decision is logged."
   - Add, as a separate small frame beside it named "toast-approved", a toast (white card, shadow,
     green check icon): "Approved · sent to Transport (Daniel Otieno) for vehicle allocation".

2. "… / my-requests":
   - Needs your action: delete the group label "RETURNED FOR CORRECTION · 1"; the row title
     already says it.
   - Table card: remove its "My requests · 4" heading (the page title already says it); put
     search "Search my requests" and a filter "All · In progress · Completed" at the top of the card
     instead. Columns fill the full card width: REQUEST 26% · ROUTE 28% · DEPARTURE 14% ·
     PROGRESS 20% · UPDATED 8% · ">" 4%.

3. "… / new-request":
   - Page becomes two columns: the form card on the left (640px) and a SUMMARY card on the right
     (360px, sticky at the top), 24px gap.
   - Form gets 3 section headings (16px/600 #0F172A, 24px above each): "Trip" (Purpose,
     Destination, Departure, Expected return), "People & needs" (Passengers, Special
     requirements, Preferred vehicle type, Project / activity), "Supporting documents" (upload).
   - Add "(optional)" in #64748B after: Special requirements, Preferred vehicle type, Supporting
     documents.
   - Placeholder and helper text #64748B (not green). Entered values #0F172A.
   - Date fields use a calendar icon (#64748B), not a clock.
   - Special requirements: all three checkbox chips UNCHECKED, checkbox color #006837 when checked.
   - Footer: left "Cancel" text button; right secondary "Save draft" and primary "Submit request".
   - SUMMARY card content (title "Summary"), plain rows with 16px #64748B icons:
     user-check — "Approval: James Mwangi, Head of Public Works"
     route — "~38 km round trip"
     fuel — "Estimated fuel: KES 1,900"
     bell — "You'll be notified at each step"
     Then a divider and 13px #64748B: "Transport assigns a vehicle and driver after approval."
```

### 10k. Per-page fix prompts (supersede §10j A+B; one self-contained prompt per frame)

Shared reference for every prompt: COPY elements from "v3 / fleet-operations-overview" and
"v2 / requests-and-trips"; don't redraw them.

#### 10k-1. Daniel — queue-transport

```
On the "Refined" page, fix only the frame "v2 / requests-and-trips / queue-transport". Copy shared
elements (sidebar items, arrow stage strip, chips, buttons, row styles) from
"v2 / requests-and-trips" and "v3 / fleet-operations-overview" — do not redraw them.

1. SIDEBAR: Operations → "Fleet Overview" · "Requests & Trips" (the ONLY active item, green chip) ·
   "Vehicle Allocation". Delete "Vehicle Request" and "Journey Management". All other items
   normal weight #CBD5E1, no fill.
2. STAGE STRIP: delete the flat strip; paste the arrow-segment strip from "v2 / requests-and-trips"
   with these segments in this order: Awaiting approval 12 · Transport review 6 · Needs vehicle 3 ·
   Needs driver 5 (amber tint, "oldest 2 days") · Driver check-in 8 · Ready 9 · On trip 118.
   "Ready" is SELECTED: white fill, 2px #006837 outline, label and count #006837.
   Caption below: "Showing Ready · 9".
3. LEFT LIST: remove the amber box around "RETURNED TO YOU · 1"; it's a plain group label
   (12px/600 uppercase #B45309) and a plain row. The selected row (REQ-2024-0853) keeps the
   #E6F2EB tint + 3px #006837 left bar.
4. CHIPS sentence case with a 12px icon: "Ready", "Urgent", "Returned", "Checked in 09:52",
   "Expiring".
5. RIGHT PANE:
   - Stepper labels: Approved · Transport review · Vehicle · Driver · Driver check-in · Ready ·
     On trip. Done = green ✓; current (Ready) = white circle with a 2px #006837 ring and bold label;
     upcoming = #E2E8F0 outline, #64748B label.
   - Remove the grey box around "Trip details": plain label/value rows on the card.
   - Remove the box around "5 checks passed": a plain collapsible row.
   - Remove the amber bordered box around the insurance warning: a plain row with a #B45309
     alert-triangle icon, "Insurance" (14px/600 #0F172A), chip "Expiring" (#B45309 on #FFFBEB),
     and beneath "Expires 29 Sep, after this trip returns. Renewal in progress." (13px #64748B).
     Rows separated by 1px #E2E8F0 lines.
   - Footer: helper "Warnings don't block dispatch. This one will be logged." in 13px #64748B on
     its own line above the buttons. "Return to requester" stays a text link on the left;
     "Dispatch" primary on the right: 40px tall, 8px radius.
6. "+ New request" button: 40px tall, 8px radius (not a pill).
```

#### 10k-2. James — queue-approver

```
On the "Refined" page, fix only the frame "v2 / requests-and-trips / queue-approver". Copy shared
elements from "v2 / requests-and-trips / my-requests" (sidebar pattern) and
"v2 / requests-and-trips / queue-transport" (list rows, detail pane) — do not redraw them.

1. SIDEBAR (same pattern as the my-requests frame): one group "Requests & Trips" with sub-items
   "To review" (ACTIVE, green chip) · "My requests". Remove every other pillar and item.
2. Replace the stage strip with decision tabs (Navigation/Tab Item) under the title:
   "To review (4)" active · "Returned (1)" · "Approved" · "All". Keep the subtitle
   "Public Works department" next to the title. No List/Queue toggle.
3. LEFT LIST: the selected row (REQ-2024-0859) uses the #E6F2EB tint + 3px #006837 left bar, with
   text #0F172A / #64748B. Remove the solid dark-green fill. Remove the "Urgent" chip. Keep the
   amber line "same surname as you · check conflict" on REQ-2024-0868.
4. RIGHT PANE:
   - Status chip "Awaiting approval" in sentence case with an hourglass icon.
   - Stepper labels: Approval · Transport review · Vehicle · Driver · Driver check-in · Ready ·
     On trip. "Approval" is CURRENT: white circle with a 2px #006837 ring and bold label (no ✓).
     The rest upcoming.
   - Remove the grey box around "Trip details": plain label/value rows.
   - "Next steps" line stays: info icon + "Vehicle, driver and dispatch checks happen after your
     approval." (13px #64748B).
   - Comment: one 72px text area, placeholder "Add a comment (required to return or reject)".
     Remove the stray circle.
   - Footer: helper line above the buttons, 13px #64748B, not clipped: "You can't approve a request
     you submitted. Your decision is logged." Left: text link "Reject" (#B91C1C 14px/600, no
     border). Right: secondary "Return for correction" (white, 1px #006837 border, #006837 text)
     and primary "Approve" (#006837), both 40px tall, 8px radius.
5. Beside the frame, a small frame "toast-approved": white card, 12px radius, soft shadow, green
   check icon, text "Approved · sent to Transport (Daniel Otieno) for vehicle allocation", and a
   close ×.
```

#### 10k-3. Mary — my-requests

```
On the "Refined" page, fix only the frame "v2 / requests-and-trips / my-requests".

1. NEEDS YOUR ACTION card: delete the group label "RETURNED FOR CORRECTION · 1" (the row title
   already says it). Keep the row and its "Correct" button.
2. NEXT TRIP card: chip "Ready · awaiting vehicle" in sentence case with a clock icon (#B45309 on
   #FFFBEB).
3. TABLE card:
   - Remove the card heading "My requests · 4" (the page title already says it).
   - At the top of the card, one row: search field "Search my requests" (240px, 36px tall) on the
     left and segmented filter "All · In progress · Completed" (All selected) on the right.
   - Columns fill the full card width: REQUEST 26% · ROUTE 28% · DEPARTURE 14% · PROGRESS 20% ·
     UPDATED 8% · ">" 4%.
   - "Completed" chip in sentence case with a check icon.
4. "+ New request": 40px tall, 8px radius (not a pill).
```

#### 10k-4. Mary — new-request

```
On the "Refined" page, fix only the frame "v2 / requests-and-trips / new-request".

1. LAYOUT: two columns under the header. Left: the form card, 640px. Right: a new "Summary" card,
   360px wide, top-aligned with the form, 24px gap. Every input stays in a single column (never
   two inputs side by side).
2. SECTIONS in the form, each with a heading (16px/600 #0F172A, 24px space above; a 1px #E2E8F0
   divider before the 2nd and 3rd):
   "Trip" — Purpose, Destination, Departure, Expected return
   "People & needs" — Passengers, Special requirements, Preferred vehicle type, Project / activity
   "Supporting documents" — the upload zone
3. Add "(optional)" in 14px #64748B after the labels: Special requirements, Preferred vehicle
   type, Supporting documents.
4. COLORS: placeholder and helper text #64748B (not green); entered values #0F172A; field icons
   #64748B outline. Departure and Expected return use a calendar icon (not a clock).
5. SPECIAL REQUIREMENTS: all three checkbox chips UNCHECKED (white, 1px #E2E8F0 border, empty
   checkbox). A checked state would use #006837, never purple.
6. FOOTER in the form card: left "Cancel" text button (#334155); right secondary "Save draft"
   (white, 1px #E2E8F0 border, #334155 text) and primary "Submit request" (#006837), both 40px
   tall, 8px radius. Delete the old summary text lines from the form.
7. SUMMARY card (title "Summary", Lexend 16px/600), plain rows 14px #334155, each with a 16px
   outline #64748B icon, 12px between rows:
   user-check — "Approval: James Mwangi, Head of Public Works"
   route — "~38 km round trip"
   fuel — "Estimated fuel: KES 1,900"
   bell — "You'll be notified at each step"
   then a 1px divider and 13px #64748B: "Transport assigns a vehicle and driver after approval."
```

### 10l. Strip pass — queue-transport (2026-09-25; user: "don't be afraid of stripping unnecessary colors or elements")

**Landed from 10k-1:**
- One active sidebar item.
- Arrow strip with the correct D11 stages.
- Stepper labels unified.
- Most boxes removed; helper text grey; buttons 40px.

**Strip audit: everything in the pane that repeats, decorates, or doesn't change Daniel's
decision.**

| Element | Why it goes | Replace with |
|---|---|---|
| "Ready" chip next to the ID | "Ready" is already stated 3×: selected strip segment, list group "READY · 9", selected row | nothing |
| Full 7-step progress stepper | Daniel works *at* Ready; every earlier step is done by definition. Tier 3 for him | one grey line under the title: "Step 6 of 7 · approved by Dr. Achieng Otieno, 23 Sep" |
| 6 uppercase section labels (PROGRESS, TRIP DETAILS, ASSIGNED VEHICLE, ASSIGNED DRIVER, DISPATCH READINESS, NOTES…) | Labels for content that explains itself | 2 labels only: "Vehicle & driver", "Readiness" |
| Icons + uppercase labels on the 4 trip facts | Decoration | plain label/value rows |
| Bordered boxes around vehicle and driver; "Change" as buttons | Boxes inside a card; two outlined buttons compete with Dispatch | plain rows; "Change" as grey text links |
| Green "Checked in 09:52" chip | The pre-trip check already confirms it | plain grey text "checked in 09:52" |
| Amber ×5 on one warning (pill "6 of 6 passed · 1 warning", amber title, amber icon, "Expiring" chip, amber body) | One warning, five alarms | amber **icon only**; title #0F172A; text #64748B; header count plain grey "6 of 6 passed" |
| Sub-list of every passed check | Detail that belongs behind the expand | "5 checks passed ›" only |
| Notes-for-driver field (72px) | Optional and rarely used, yet takes a full block | text link "+ Add note for driver" |
| Footer helper "Warnings don't block… logged" | The warning row already explains itself | nothing |
| "Showing Ready · 9" caption | Repeats the selected segment | nothing |
| ">" chevrons on every queue row | In a split pane, selecting shows the detail; the chevron adds nothing | nothing |
| "Returned" chip on the returned row | Group label + reason line already say it | nothing (the reason line stays amber) |

**Color after the strip:**
- **Green:** primary button, selected states, the success ✓ icon.
- **Amber:** the Needs-driver segment, the returned reason, the warning icon.
- **Red:** "Urgent" only.

**This is the request-detail component, not just this page.** The same strip applies to the
approver pane (and to Grace's drawer, minus the stepper rule, which stays full in the
requester/approver/drawer views where progress is the point). Record as P17 usage rule:
**compact "Step X of 7" line in work queues; full stepper where someone is tracking progress.**

```
On the "Refined" page, simplify only the frame "v2 / requests-and-trips / queue-transport".
Goal: remove repetition and extra color. Keep all data that isn't listed for removal.

STAGE STRIP
1. Fix the selected "Ready" segment: the whole segment gets a white fill and a 2px #006837
   outline following its arrow shape; label and count #006837. The number must not overlap the
   outline. Delete the caption "Showing Ready · 9".

LEFT LIST
2. Delete the ">" chevron on every row.
3. Returned row: delete the "Returned" chip. Keep the amber line "Override denied by Grace
   Wanjiru · suggested KCE 558A".
4. Keep "Urgent" as a small chip (#B91C1C on #FEF2F2), the only red on the page.

RIGHT PANE (top to bottom, 24px between blocks, rows separated only by 1px #E2E8F0 lines)
5. Header: "REQ-2024-0853" (13px/600 #64748B) above "John Kamau · Health" (Lexend 20px/600).
   Delete the "Ready" chip. Under it one line 13px #64748B: "Step 6 of 7 · approved by
   Dr. Achieng Otieno, 23 Sep".
6. Delete the whole PROGRESS stepper and its label.
7. Trip facts: delete the "TRIP DETAILS" label and all four icons. Four plain rows, label left
   13px #64748B, value right 14px/600 #0F172A: Route · Departure · Passengers · Cargo.
8. One label "Vehicle & driver" (13px/600 #334155, sentence case). Two plain rows, no borders or
   boxes:
   [72×48 vehicle photo] "KCE 558A · Nissan X-Trail" / "Nakuru HQ Yard · Bay 2" (13px #64748B) —
   right: text link "Change" (#64748B 13px/600).
   [40px avatar] "Faith Cherotich" / "County driver · checked in 09:52" (13px #64748B, no chip) —
   right: text link "Change".
9. One label "Readiness" (13px/600 #334155) with "6 of 6 passed" (13px #64748B) on the right —
   no pill.
   Row 1: green ✓ icon + "5 checks passed" (14px #0F172A) + ">" to expand. No sub-list.
   Row 2: #B45309 alert-triangle icon + "Insurance expires 29 Sep" (14px/600 #0F172A) and beneath
   "After this trip returns · renewal in progress" (13px #64748B). No chip, no amber text.
10. Delete the "Notes for driver" field; add a text link "+ Add note for driver" (13px/600
    #006837) under the readiness rows.
11. Footer, one row: left text link "Return to requester" (#334155 14px/600); right primary
    "Dispatch" (40px, 8px radius). Delete the helper sentence.
```

### 10m. Render check & fix prompt — queue-transport (2026-09-25)

**Landed (massive improvement):**
- Layout is now a genuine, focused T2 Master-Detail work queue for Daniel Otieno.
- Clutter stripped: no redundant stepper, no uppercase badge overload, no boxes inside cards.
- Left triage list groups "RETURNED TO YOU · 1" and "READY · 9" cleanly with rejection rationale.
- Assigned vehicle (photo, bay) and driver (avatar, check-in) with lightweight "Change" links.
- Single green active sidebar chip for "Requests & Trips".

**Findings & Remaining Fixes:**
1. **Stage Strip "Ready" Glitch:** The agent drew literal diagonal vector strokes (`/` and `\`) around "Ready" and "9", slicing into the text rather than styling the chevron segment with a clean border/fill.
2. **Trip Facts Canyon:** Labels on the far left, values on the far right across ~500px of empty space. Needs a scannable 2-column or compact key-value layout.
3. **Insurance Warning Lost Color:** The warning icon rendered grey/neutral instead of `#B45309` amber alert-triangle. Per rule ("color marks only the exception"), it needs amber to signal the pending renewal.
4. **Card Height Balance:** The left list card ends abruptly midway down the canvas while the right detail card extends down. Both should align to equal bottom bounds.
5. **Top Bar Placeholder:** Still page-specific ("Search requests, routes, or requester") instead of global ("Search vehicles, requests, drivers").
6. **Selected Row Tint:** Background is currently neutral grey `#F1F5F9`; needs brand tint `#E6F2EB` to pair with the 3px green bar.

### 10n. Render check & fix prompt — queue-approver (James Mwangi) (2026-09-25)

**Landed:**
- Scoped sidebar: only "Requests & Trips" visible with "To review" active (green chip).
- Identity: "James Mwangi / Head of Public Works · Approver".
- Left triage list shows department requests, including conflict cue on Paul Mwangi ("same surname as you").
- Decision buttons present: Reject, Return for correction, Approve.

**Findings & Alignments Needed:**
1. **Critical Stepper Bug:** Step 1 is rendered as "Approved ✓" with a green checkmark! The request is *awaiting* James's approval — it cannot show approved before he approves it. Step 1 must be "Approval" in the CURRENT active state (white circle with 2px green ring, no checkmark).
2. **Breadcrumb / Sidebar Mismatch:** Breadcrumb reads "Operations / Requests & trips", but James has no "Operations" pillar in his sidebar. Breadcrumb should simply be "Requests & trips".
3. **Stage Strip Drift:** Flat boxes instead of arrow segments; labels have drifted ("Vehicle check" instead of "Needs vehicle", "Awaiting driver" instead of "On trip"). Needs D11 alignment.
4. **Selected Row Indicator:** Left list has an oversized thick green block instead of the standard 3px left accent bar. Redundant ">" chevrons on queue rows.
5. **Uppercase Shouting Headers:** "PROGRESS", "TRIP DETAILS", "NEXT STEPS", "COMMENT REQUIRED".
6. **Missing Purpose:** Trip facts omitted the purpose ("Ward office inspection, quarterly").
7. **Comment Label:** Shouts "COMMENT REQUIRED", but comments are only required when returning or rejecting (approving does not require a comment).
8. **Left Card Height:** Truncates after 4 rows (~320px), leaving half the canvas empty below it. Must match the right card's height.

### 10o. Stage strip redesign — underline tab pattern (2026-09-25)

**Decision:** Replace the arrow/chevron polygon stage strip on all Requests & trips queue frames
with an underline-tab filter bar. Benchmarked against Xero (Quotes) and Deputy (Timesheets) —
see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` §2 "Stage filter strip". Recorded as the new P8 rule.

```
On the "Refined" page, apply this change to the frame
"v2 / requests-and-trips / queue-transport".

DELETE the existing stage strip (the arrow-segment row with 7 segments). Replace it with the
following. Do NOT copy from any other frame — build from scratch with Auto Layout only.

───────────────────────────────────────────────────
STAGE TAB BAR
───────────────────────────────────────────────────
Outer container:
  - Name: "Stage / Tab Bar"
  - Layout: Auto Layout, HORIZONTAL, Gap: 0, Align: top
  - Width: Fill container (full content width, same as the cards below)
  - Height: 40px
  - Background: none (transparent)
  - Border: BOTTOM only — 1px solid #E2E8F0
  - No left/right/top border. No corner radius.

Inside this container, place 7 Tab Item frames in this exact order:
Each Tab Item:
  - Layout: Auto Layout, VERTICAL, Gap: 0, Center-align
  - Width: Fill container (so all 7 share the width equally)
  - Height: 40px
  - Padding: 0 12px
  - Background: none
  - No border (the outer container carries the bottom border)

LABEL inside each Tab Item:
  - A single text node: the stage name + two spaces + the count
  - Font: Source Sans 3, 14px
  - For all INACTIVE tabs: color #64748B, weight 400
  - For the WARNING tab ("Needs driver  5"): color #B45309, weight 400
  - For the ACTIVE tab ("Ready  9"): color #006837, weight 600 (bold)

ACTIVE INDICATOR for the "Ready  9" tab only:
  - Add a rectangle INSIDE the Tab Item, pinned to its bottom edge
  - Width: Fill container, Height: 2px, Fill: #006837
  - Name: "Active Indicator"
  - All other tabs: no active indicator rectangle

Tab items, left to right:
  1. "Awaiting approval  12" — inactive
  2. "Transport review  6"   — inactive
  3. "Needs vehicle  3"      — inactive
  4. "Needs driver  5"       — WARNING (text #B45309)
  5. "Driver check-in  8"    — inactive
  6. "Ready  9"              — ACTIVE (text #006837 bold + 2px bottom rect)
  7. "On trip  118"          — inactive

Below the tab bar (NOT inside it), add a single text node:
  "Showing Ready · 9 of 104 total"
  Font: Source Sans 3, 13px, color #64748B
  Margin top: 8px from the tab bar

───────────────────────────────────────────────────
POST-BUILD CHECK (verify before sharing the result)
───────────────────────────────────────────────────
1. The tab bar is 40px tall and spans the same width as the cards below it.
2. All 7 tabs share width equally (no tab is wider or narrower than its neighbours).
3. Only "Ready  9" has the 2px green bottom rectangle. No other tab has it.
4. There are NO diagonal lines, no polygon shapes, no vector arrows anywhere in this element.
5. "Needs driver  5" text is #B45309. All other inactive tabs are #64748B.
6. The tab bar has a bottom border only. No top, left, or right border on the container.
```

---

## 11. Wix alignment (2026-10-01)

The user confirmed the desktop direction is **the Wix approach**. That direction was written up
by another session (desktop skill + `08` §26) and is now the standard. Reconciliation done:
- **`03` §1.5:** new authority for Wix desktop tokens.
- **Desktop skill:** personas corrected to the canonical names; Operations nav per D8; scope
  switcher moved from the top bar to the page header; canonical demo data; D1/D10/D11 rules
  added. A backup of the previous skill is in the session scratchpad.
- **D9:** toggle removed.

**What changes in the pending desktop prompts:**

| Earlier rule (this chat) | Wix standard now |
|---|---|
| Buttons 40px, 8px radius, "no pills" | **Pill, 20px radius**, 36–40px |
| Canvas #F8FAFC, borders #E2E8F0 | Canvas **#F4F6F8**, borders **#DFE5EB** |
| Table header #F8FAFC | **#EBF1F7** |
| Strip pass removed icons on trip facts | **Keep** semantic icons (`03` §1.4.1, non-swappable: map-pin = route, clock = departure, users = passengers, package = cargo) |
| 72×48 vehicle photo in the pane | **140px hero** in detail panes and drawers |
| Frames 1776px | **1440px**; resize each frame as it's finalised |

**Unchanged** (Wix and the strip pass agree):
- No repeated status chip.
- Compact step line in work queues.
- Passed checks collapsed.
- One amber signal per warning.
- No notes box.
- No chevrons in the queue list.
- Plain rows inside cards.

### 11a. Prompt — queue-transport, strip + Wix (supersedes §10l)

```
On the "Refined" page, update only the frame "v2 / requests-and-trips / queue-transport".
Goal: Wix surface style + remove repetition and extra color. Keep all data not listed for removal.

FRAME & SURFACES
1. Resize the frame to 1440px wide (240px sidebar + 1200px content, 24px page gutter); reflow
   the content to fit. Page canvas #F4F6F8. Every card: white, 1px #DFE5EB border on all sides,
   12px radius, shadow 0 1px 2px rgba(15,23,42,0.06).
2. Buttons and inputs are pills (20px radius): "+ New request" and "Dispatch" primary (#006837,
   white text, 40px tall); search field pill with 1px #DFE5EB.

HEADER
3. Delete the "List | Queue" toggle. Title "Requests & trips" with "+ New request" on the right.

STAGE STRIP
4. Selected "Ready" segment: whole segment white fill with a 2px #006837 outline following its
   arrow shape; label and count #006837; the number must not touch the outline. Delete the
   caption "Showing Ready · 9".

LEFT LIST
5. Delete the ">" chevron on every row. Delete the "Returned" chip (keep the amber reason line
   "Override denied by Grace Wanjiru · suggested KCE 558A"). Keep "Urgent" (#B91C1C on #FEF2F2,
   flag icon), the only red on the page. Row dividers #EEF1F4.

RIGHT PANE (24px between blocks; rows separated only by 1px #EEF1F4 lines; no boxes)
6. Header: "REQ-2024-0853" (13px/600 #64748B) above "John Kamau · Health" (Lexend 20px/600).
   Delete the "Ready" chip. One line under it, 13px #64748B: "Step 6 of 7 · approved by
   Dr. Achieng Otieno, 23 Sep". Delete the full PROGRESS stepper and its label.
7. Vehicle hero: a 140px-tall photo of the Nissan X-Trail (12px radius, full pane width) at the
   top of the pane under the header, with "KCE 558A · Nissan X-Trail" (14px/600) and
   "Nakuru HQ Yard · Bay 2" (13px #64748B) beneath, and a "Change" text link (#64748B) at right.
8. Trip facts: delete the "TRIP DETAILS" label; four plain rows, each with an 18px outline
   #334155 icon: map-pin "Route" · clock "Departure" · users "Passengers" · package "Cargo";
   label 13px #64748B, value 14px/600 #0F172A.
9. Driver row: 40px avatar, "Faith Cherotich" / "County driver · checked in 09:52" (13px
   #64748B, no chip), "Change" text link at right.
10. "Readiness" label (13px/600 #334155) with "6 of 6 passed" (13px #64748B) at right, no pill.
    Row: green ✓ + "5 checks passed" + ">" to expand (no sub-list).
    Row: #B45309 alert-triangle + "Insurance expires 29 Sep" (14px/600 #0F172A), beneath
    "After this trip returns · renewal in progress" (13px #64748B). No chip, no amber text.
11. Delete the notes field; add "+ Add note for driver" (13px/600 #006837).
12. Footer, one row: left "Return to requester" text link (#334155); right "Dispatch" primary
    pill. Delete the helper sentence.
```
