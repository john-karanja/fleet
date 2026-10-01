# CVFMS: Figma Screen Blueprint & Frame Directory

**Document ID:** `DOC-CVFMS-004`
**Revision:** 2.1 — reference update only. `01_USER_PERSONAS.md` and `02_USER_FLOWS.md` were revised to v2.1 (journey-stage/friction-point structure per the `ui-ux-expert` method) after this blueprint was first written; checked against that revision and confirmed no frame, component, or layout decision below changes as a result — the underlying facts (roles, goals, friction points) are the same, only their organizing frame changed. Section references below updated accordingly. Originally re-derived from `01_USER_PERSONAS.md` v2.0, `02_USER_FLOWS.md` v2.0, and `03_MASTER_DESIGN_SYSTEM.md` v2.0 as a full restart — the archived v1.x blueprint (`docs/archive/04_FIGMA_SCREEN_BLUEPRINT.md`) went through 16 rounds of revision on FRAME-01 alone, none of which is inherited here.
**Depends on:** `01_USER_PERSONAS.md`, `02_USER_FLOWS.md`, `03_MASTER_DESIGN_SYSTEM.md`.
**Purpose:** The doc `figma-generate-design` / `use_figma` should be pointed at. Enumerates exact frames, dimensions, and per-component specs.

---

## 1. Master Frame Directory (Desktop, 1440 × 1024px)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              CVFMS DESKTOP FRAME DIRECTORY (Wave 1)                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. [FRAME-01] Fleet Operations Overview (Grace — Fleet Manager)   ◄── build first, see §2          │
│ 2. [FRAME-02] Dispatch & Requisition Queue (Daniel — Transport Officer)  — see §3                  │
│ 3. [FRAME-03] Workshop Job Card Board (Peter — Workshop Manager)  — see §4                          │
│ 4. [FRAME-04] Executive Briefing Dashboard (Sarah — County Executive)  — see §5                    │
│ 5. [FRAME-05] Finance & Cost Dashboard (Miriam — Finance Officer)  — see §6                         │
│ 6. [FRAME-06] Live Fleet Map (Grace — in-page tab of Fleet Operations)  — see §7, build last        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Shared shell (top nav + left rail, Component 1) wraps all 6 frames — build once as a reusable Figma component.

**Generation sequence:** FRAME-01 → FRAME-02 → FRAME-03 → FRAME-04 → FRAME-05 → FRAME-06. FRAME-06 is last because the SRS tiers GPS/Telematics as Phase 5 (architecture summary §8), after Foundation/Operations/Cost/Compliance — the design sequence mirrors the build sequence so Grace's navigation structure is decided now without forcing the spatial-map capability to be designed before its data dependencies (live GPS feed) exist.

**Product-owner demo sequence (2026-09-13) — distinct from the generation sequence above:** the user asked for at least 5 screens to show the product owner. Rather than default to the first 5 frames in build order, the demo set was chosen to maximize persona coverage and substance-per-screen: **FRAME-01 (Grace) → FRAME-02 (Daniel) → FRAME-05 (Miriam) → FRAME-03 (Peter) → FRAME-04 (Sarah)**, covering all 5 flagship personas and deliberately excluding FRAME-06 (Live Map) — not because it's unimportant, but because it's the weakest standalone story for a product owner review (mostly a map with markers, and the SRS itself sequences its underlying data dependency, GPS/Telematics, as Phase 5, last). Reasoning per screen: FRAME-01 establishes the product premise (state + urgency + direct action); FRAME-02 demonstrates the SRS's fraud-prevention business rules (BR-001–005) as a tangible, visible gate — the strongest credibility builder for a government audit context; FRAME-05 (specifically its Anomaly Review tab) shows the fraud-detection logic becoming a reviewable queue, the clearest "this system pays for itself" story; FRAME-03 proves the system handles a fundamentally different interaction pattern (a physical/floor-based Kanban board, not just office approvals); FRAME-04 closes as the "so what" executive summary, most persuasive once the underlying operational rigor has already been seen. This does not change the underlying generation sequence used for build dependency reasons (§27 above) — FRAME-06 will still be designed last regardless of demo order, once GPS data dependencies exist.

**Demo set expanded to 7 screens (2026-09-13):** the user asked to add the All Vehicles tab content and FRAME-06 (Live Map) as two more screens in the demo set, despite both being flagged above as lower-priority (All Vehicles visually repeats a Data Table pattern already shown twice; Live Map's build sequencing places its data dependency last). Accepted — for a design mockup (no application code exists yet), designing Live Map ahead of its natural data-maturity sequence carries none of the risk it would in an actual build order (there's no GPS ingestion service to be missing), so the SRS-phasing rationale that governs *build* order doesn't block *design* order. **Final 7-screen demo set, in generation order:** FRAME-01 (Grace) → FRAME-02 (Daniel) → FRAME-05 (Miriam) → FRAME-03 (Peter) → FRAME-04 (Sarah) → All Vehicles (full registry table, content for the FRAME-01 tab, prompted as its own standalone screen since its content is substantial enough to warrant one) → FRAME-06 (Live Map, still generated last within this set, consistent with its position in the underlying generation sequence in §27).

---

## 2. FRAME-01: Fleet Operations Overview (Grace — Fleet Manager)

**Derivation:** Grace's core goal (`01_USER_PERSONAS.md` §1) is two jobs — know fleet state, act before problems compound. Her journey map (§1's stage table) identifies stages 3-4 (Decide the action → Take the action) as the dominant friction — a finding without a direct path to the fix. Her stated dashboard content per SRS §6/§7.1: real-time status breakdown, active requisitions awaiting allocation, vehicles due for return, preventive maintenance countdowns, GPS/speeding alerts (the last deferred to FRAME-06, §7). The layout leads with an action-oriented list, not a passive status summary, because that's where her journey's friction actually concentrates.

**Revision (2026-09-13) — simplified per user request, benchmarked against Jobber's dashboard:** the user explicitly liked Jobber's dashboard simplicity (referenced: [Jobber Home](https://mobbin.com/screens/56a6ce1c-8d71-4c1a-89cb-1d07f075424a)) and asked to push FRAME-01 toward it on two fronts: (1) a human greeting line replacing the generic page title, and (2) merging the KPI row and Needs Attention's urgency counts into one combined pipeline-style row, matching Jobber's "Workflow" block (each stat card shows a count plus its own urgent sub-breakdown, one row doing double duty instead of two separate panels). This is a genuine structural change to how Grace's two jobs (know state / act) are laid out — checked against her journey stages 3-4 (`01_USER_PERSONAS.md` §1) below to confirm it doesn't lose the "direct path to the fix" the original two-panel split existed to guarantee.

**Correction (2026-09-13) — greeting header lost real information, ordering re-benchmarked, and breadcrumb scope decided.** Two follow-on issues surfaced once the greeting change actually rendered: (1) the original header's "Manager: Grace Wanjiru • Live Command Active" line was dropped entirely when replaced by the greeting — but "Live Command Active" is real system-state information (is the fleet-monitoring pipeline actually running), not decorative chrome, and Daniel's FRAME-02 header kept an equivalent status line ("Gate Check System Online"). Jobber/Buffer don't have this line because those products have no equivalent backend-system-liveness concept to signal — the simplification precedent doesn't actually cover dropping it. **Fixed: the status line is restored as a small line under the greeting**, not reintroduced as part of a redundant title/subtitle. (2) Checked [Buffer's home screen](https://mobbin.com/screens/6a20adec-611b-4f90-84c4-bd72ec3d05a9) and [ElevenLabs' home screen](https://mobbin.com/screens/dca603f3-4beb-4a71-8e63-42baaef3584d) for greeting/date ordering — both put the greeting first (large) and the date second (small), the reverse of the initial fix prompt's ordering. **Adopted Buffer's ordering.** (3) User asked about adding breadcrumbs (referencing [folk's "Recruitment pipeline / All applicants" pattern](https://mobbin.com/screens/aac9827e-b12f-4fe5-908a-2efd0acfcc11)) — folk's breadcrumb reflects real nested navigation (a group containing multiple named views) that this system's flat 20-module nav doesn't have; a breadcrumb on Overview's own tabs would be circular. **Decided: breadcrumbs are scoped only to genuine drill-down detail views** — a plain, non-interactive context label (not a clickable nested breadcrumb, since there's no folder structure to click back into) on FRAME-02's Request Details panel (e.g. "Dispatch Management → Request Detail") and on the future vehicle-detail view reached from the All Vehicles tab (e.g. "All Vehicles → Vehicle Detail"). No breadcrumb anywhere else.

**Component list (five components, top to bottom):**

```
Top Nav (56px) + Left Rail (240px, dark #0F172A, full 20-item SRS §2 module list per Component 1's
  product-owner-corrected spec — scrollable within the rail, not compressed or truncated)
Greeting line (replaces generic page title, per Jobber/Buffer reference — see revision note below
  on ordering): "Good [morning/afternoon/evening], Grace" as the large primary line, with the
  current date as a small line directly beneath it (Buffer's ordering — greeting first, date
  second, not the reverse). Directly under that: a small status line, "● Live Command Active" —
  restored per the 2026-09-13 correction below, not dropped as part of the Jobber-style
  simplification.
[ Overview ] [ Live Map ] [ All Vehicles ]  ← tabs, Overview active, Live Map → FRAME-06,
  All Vehicles → Fleet Registry tab (see below)

FLEET STATUS ROW (merged KPI + urgency row, replaces the old separate KPI Row — Component 2
  variant, per Jobber's "Workflow" block pattern): 4 cards, each with a single thin colored top
  border (not a full-color card) as the only saturated color per card — restrained, matching
  Jobber's near-zero-color approach:
    - Fleet Size: 247 · sub-line: "247 registered"
    - Availability: 89% · sub-line: "6 grounded" (links to the grounded rows below)
    - Compliance: 14 due · sub-line: "2 overdue · 12 this week" (links to Needs Attention below)
    - Requests: [count] · sub-line: "[n] pending allocation" (links to the allocation-pending rows)
  Each card's sub-line is a live count of items that also appear in Needs Attention below it — the
  card is both a KPI (Job 2: know state) and an entry point into the specific urgent rows behind
  that count (Job 1: act) — this is the Jobber-style merge, kept honest to Grace's journey stages
  3-4 by making sure the "direct path to the fix" survives the merge: clicking a card's sub-line
  scrolls to/filters the matching Needs Attention rows, it does not just display a number in
  isolation.

HERO ROW — two panels side by side (unchanged from before the merge):
  LEFT (~60% width): NEEDS ATTENTION (Component 3C) — Overdue + Due This Week only, scoped tightly
        per the design system's binding rule that every row must be something Grace could act on
        today. Each row: vehicle/request identifier (dominant), Status Pill (Component 3), one-line
        reason, direct action button (Reallocate / Registry Edit / Override / Approve, opening
        Component 4 Action Drawer per its persona-authorized action). Header link: "View all
        compliance →" to a full Compliance list destination (nav item, not built this wave).
        Per the queued post-render refinement (`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`), each
        section shows its own row count next to its label ("Overdue (2)", "This Week (2)").
  RIGHT (~40% width): COMING UP (Component 3B or 3C variant) — date-grouped, calm, non-urgent items
        (services due in 2-4 weeks, allocations expiring later). Deliberately not color-coded for
        urgency — this list's entire purpose is to be the calm counterpart to Needs Attention, so
        using the same warning/critical treatment here would blur that distinction. Matches
        Jobber's restrained-color principle by default (it was never color-coded to begin with).

FLEET STATUS SUMMARY — full width, own row. A bounded/card-contained status breakdown (counts per
  status: Available / On Trip / Grounded / Maintenance) with a small preview map thumbnail, NOT a
  full interactive map (full map lives in FRAME-06). Links: "Full map →" (FRAME-06), "All vehicles →"
  (Fleet Registry tab, see below). Per the queued post-render refinement, the map preview
  carries its own small on-map legend so it's decodable without reading the status list beside it.

RECENT ACTIVITY — full width, lowest priority, narrowed to override/exception events only (not
  routine trip starts/ends). Justification: SRS §8 treats the audit trail as the authoritative,
  complete record of every action — Overview does not need to duplicate that in full; it only needs
  the subset with real audit/exception value that a passing glance might surface a problem from
  (an override, a rejected approval, an anomaly flag). A full chronological feed of routine actions
  fails the same "does Grace need this to act" test everything else on this page is held to, so it
  is deliberately excluded rather than included as a default. Per the queued post-render refinement,
  each row carries a distinct actor field (who performed the action), not folded into prose.
```

**What did NOT change, and why:** Needs Attention, Coming Up, Fleet Status Summary, and Recent Activity keep their existing content and scope — Jobber's simplicity comes from a small-business tool with far lower compliance/audit stakes than a county government fleet system (SRS §8, BR-009 both require durable, structured audit content this system cannot simplify away). The merge is scoped to where Jobber's actual technique (one row doing double duty) transfers cleanly — the KPI/urgency-count row — not applied as a blanket "remove panels" instruction.

**Gap closed (2026-09-13): the full Fleet Registry had no destination.** "Fleet Registry" is the first item in the 20-item nav list and "All vehicles →" is a link from Fleet Status Summary, but no frame ever specced what either actually leads to — a genuine gap, not a previously-deferred item (the deferred item, Vehicle Allocation Table, is a different, narrower thing — see `03_MASTER_DESIGN_SYSTEM.md` Component 3G). Resolved as a **third tab on this same page**, not a separate frame, consistent with how Live Map already works as a tab rather than its own nav destination:

```
[ Overview ] [ Live Map ] [ All Vehicles ]  ← All Vehicles tab

ALL VEHICLES TAB — full-width Data Table (Component 6), one row per vehicle in the fleet:
  Columns: Registration Number, Make/Model, Department/Station, Status (Status Pill), Insurance
  Expiry, Inspection Expiry, Current Odometer. Sortable columns, filter-chip row above (department,
  status, station), search field, pagination (247 vehicles — not all on one page). Row click opens
  a vehicle detail view (not specced this wave — flagged as a follow-on gap, same as Grace's 4
  action modals).
```

**Considered and rejected: a small registry-summary panel on the Overview tab itself** (e.g. beside Recent Activity, showing a handful of recently-updated vehicles). Rejected because Fleet Status Summary already serves as Overview's registry summary — it shows the registry's aggregate state (counts per status) and links directly to the full table. A second summary panel would either duplicate that same aggregate information in a different shape, or introduce a new, unrequested slice of data ("recently updated vehicles") that doesn't trace to any stated need in Grace's journey (`01_USER_PERSONAS.md` §1). This is the same redundancy/decorative-element test that removed the old Vehicle Status Board from Overview during the original design work — reapplied here rather than reopened without new justification.

---

## 2C. Grace's 4 Action Modals (new, 2026-09-16)

Reached from Needs Attention row clicks on FRAME-01 (`04_FIGMA_SCREEN_BLUEPRINT.md` §2). Per `01_USER_PERSONAS.md` §1's journey table, these are stage 3→4 (decide the action → take the action) — each modal is a single specific item Grace is resolving, not a queue she's working through, which matters for the fixed-pane-vs-drawer decision below.

### 2C.1 Dispatch Override Review — first of the 4, pure template reuse

**Mechanic decision:** true overlay drawer, NOT a fixed pane. Reasoning, per the same decision rule used for FRAME-02 vs. FRAME-05 (`09_PATTERN_LIBRARY.md` §2): Grace reaches this from a single Needs Attention row, not a queue she's triaging in volume — the same low-volume, deliberate-investigation shape as Miriam's Anomaly Review (FRAME-05), not Daniel's high-volume dispatch queue (FRAME-02). A fixed pane would cost nothing here (there's no adjacent queue to keep visible), so the true drawer's decision-focus benefit is free to take.

**Content — reuses FRAME-02's Dispatch Gate Checklist structure directly, viewed by Grace:**
```
TRUE OVERLAY DRAWER — background (the Needs Attention list / whichever screen she came from) dims,
drawer slides in from the right, close (X) button top-right.

Context label: "Fleet Registry → Dispatch Override Review" (per the breadcrumb-scope rule,
09_PATTERN_LIBRARY.md §10).

Request summary: requester, destination, vehicle assigned, driver assigned — same fields as
Daniel's version.

BR-001–BR-005 checklist, each a pass/fail Status Pill (icon + text, never color alone): Insurance
valid · Driver active & employed · Driver licence valid · Vehicle not grounded · Linked approved
request exists. At least one shows FAIL, with the specific reason shown inline (matching the
pattern already proven on FRAME-02's render — a reason line under the failed check, not just a
pass/fail label).

Since Grace is here specifically because Daniel already found this blocked and escalated it:
a small note showing WHO escalated it and WHEN (e.g. "Escalated by Daniel Otieno — 10:42 AM,
citing urgent medical supply delivery") — this is new content Daniel's version doesn't need,
since Daniel IS the one hitting the block, not receiving an escalation from someone else.

Override justification field (required) — pre-filled with Daniel's original justification if he
provided one, editable by Grace, since she may add her own reasoning as the approving authority.

Bottom-anchored decision buttons: "Deny Override" (secondary) and "Authorize Override" (primary,
Civic Green) — both write to the audit trail (BR-009) with Grace's name as the authorizing officer,
distinct from Daniel's original escalation record.
```

**Confirmation:** Confirmation Toast (Component 4B) on either decision, drawer closes, Needs Attention row updates status.

### 2C.2 Remaining 3 modals — not yet specced this pass
- **Maintenance Approval** — pure reuse of the true-drawer decision pattern (same mechanic as 2C.1), content not yet detailed.
- **Reallocate Vehicle** — needs the Picker-in-Drawer sub-pattern (search/select a pending request), not yet defined (`08_PROJECT_HANDOVER.md` template-gap list).
- **Registry Edit** — needs the Form Drawer sub-pattern (create/edit fields, no decision buttons), not yet defined.

**Resolved open question (carried from `docs/archive/08_PROJECT_HANDOVER.md` §5):** the prior project left Recent Activity's scope unresolved between three options — remove entirely, narrow to exceptions only, or find new justification. This restart resolves it as **narrow to exceptions only** (option 2): a fully-removed activity feed would leave override/exception events with no low-effort passive-glance surface at all, and Grace's persona pain points don't support removing all retrospective visibility, only removing the *routine, non-actionable* portion of it.

---

## 3. FRAME-02: Dispatch & Requisition Queue (Daniel — Transport Officer)

**Derivation:** Daniel's flow (`02_USER_FLOWS.md` §3) is linear — Transport Review/Allocation → Dispatch Gate → Trip Initiated. His journey map (`01_USER_PERSONAS.md` §2's stage table) identifies stage 3 (Gate check) as the dominant friction — a check historically discovered as a failure only after commitment. His core goal is speed without breaking a mandatory gate. The layout is a two-pane work surface, not a dashboard: a queue to triage on the left, a gate-check detail on the right, because his job is fundamentally "pick the next item, clear it, move on," not "survey a summary."

```
Top Nav + Left Rail
Page Title: "Dispatch & Requisition Queue"

LEFT PANE (~55% width): REQUISITION QUEUE (Data Table, Component 6)
  Columns: Request ID, Requester/Department, Destination, Requested Date, Status (Pending Approval /
  Approved / Ready to Dispatch — Status Pill). Sortable, filter-chip row (department, status, date
  range) above. Row click loads that request into the right pane.

RIGHT PANE (~45% width): DISPATCH GATE CHECKLIST (Component 4, Action Drawer pattern rendered inline
  when a row is selected, or as a drawer on narrower viewports)

  **Confirmed (2026-09-13) as a FIXED pane, not a true overlay drawer, after benchmarking against
  Airwallex's Spend Requests drawer** (`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`): Airwallex's true
  drawer (dimmed background, slide-in, close button) trades away background-list visibility for
  decision focus — the right tradeoff for a low-volume, deliberate-review context like Airwallex's
  own spend approvals. Daniel's stated core goal (`01_USER_PERSONAS.md` §2) is speed across a
  high-volume queue, and his journey's dominant friction is the gate check itself (stage 3), not
  decision-focus — a true drawer would cost him the ability to glance at the next 2-3 pending rows
  while resolving the current one, a real throughput cost for his specific job. **Kept as a fixed,
  always-visible pane; Airwallex's spacing/button polish is borrowed without borrowing its drawer
  mechanic** (see spacing/button notes below).

  - Small, non-interactive context label above the panel title: "Dispatch Management → Request
    Detail" — per the breadcrumb-scope decision (`04_FIGMA_SCREEN_BLUEPRINT.md` §2 correction note):
    this is the one genuine drill-down in the system so far, so a plain label (not a clickable
    nested breadcrumb, since there's no folder structure behind it to click back into) is warranted
    here even though the rest of the system's flat nav doesn't need one.
  - Selected request summary: requester, destination, vehicle assigned, driver assigned. Give each
    field generous vertical spacing (per Airwallex's field-layout polish — Requested amount /
    Start-end date / Requested for / Category each visually separated, not packed tightly).
  - Dispatch Readiness Checklist (5 required checks, each a pass/fail Status Pill with icon + text, never color alone). Standing rule (2026-09-18): DO NOT show raw "BR-001–BR-005" codes in the UI. Display human-readable checks:
    1. "Insurance Policy Active" (SRS BR-001)
    2. "Driver Licensed & On Duty" (SRS BR-002)
    3. "Driver License Class Valid (Class A, B, C1)" (SRS BR-003)
    4. "Vehicle Availability (Vehicle not grounded)" (SRS BR-004)
    5. "Approved Requisition Linked" (SRS BR-005)
    If a check fails, display the reason inline (e.g. "Vehicle KBZ 442A is currently grounded for maintenance").
  - All pass → [Authorize Dispatch] primary button (Civic Green).
  - Any fail → [Authorize Dispatch] disabled, [Request Override] secondary button opens the
    override justification field (mandatory, per BR-009) → [Confirm Override] logs to audit trail
    and enables dispatch.
  - On confirm (either path): Confirmation Toast (Component 4B), row updates status in the queue,
    pane clears for the next selection.
```

No KPI row on this screen — Daniel's job is transactional throughput, not situational awareness; a KPI row here would be decorative relative to his actual task (per the design system's decorative-element test).

---

## 4. FRAME-03: Workshop Job Card Board (Peter — Workshop Manager)

**Derivation:** Peter's flow (`02_USER_FLOWS.md` §4) is a state machine with a re-entrant state (Awaiting Parts) and a mandatory gate before release (Quality Inspection). His journey map (`01_USER_PERSONAS.md` §3's stage table) identifies stages 2 and 4 (parts request; quality inspection) as the dominant friction points. A Kanban board is the direct visual match for a card moving through discrete, mechanic-visible stages — it's the pattern the flow itself already implies, not a stylistic choice.

```
Top Nav + Left Rail
Page Title: "Workshop Job Card Board"
Filter row: department, mechanic, date range (chip filters, consistent with Component 6's filter row)

FIVE-COLUMN KANBAN (Component 5):
  Diagnosis | In Repair | Awaiting Parts | Quality Inspection | Ready for Release

  Each card: vehicle reg (dominant, type.body-strong), assigned mechanic (secondary text), linked
  spare-parts request with live stock Status Pill (In Stock / Backordered / Requested), age-in-column
  indicator (e.g., "3 days" in type.caption — a signal for jobs stalling, not a decoration).

  Ready for Release column: the release action on each card is disabled until that card's QA
  checklist sub-component (opened via card click → Component 4 drawer) is marked complete — this is
  a hard gate, mirroring the Dispatch Gate's disabled-until-clear pattern in FRAME-02, because both
  are the same underlying UX problem: don't let a consequential action be taken before its
  prerequisite is verifiably satisfied.
```

**Job Card Detail Drawer (Component 4):** opened from any card. Shows full work order (diagnosis, parts requested + stock status, labour, estimated/actual cost, warranty note) and, only in the Ready-for-Release column, the QA checklist gating the Release button.

---

## 5. FRAME-04: Executive Briefing Dashboard (Sarah — County Executive)

**Derivation:** Sarah's persona is explicitly read-only, low-frequency, and needs an answer in under a minute (`01_USER_PERSONAS.md` §4). Her journey map identifies stages 2-3 (assessing a figure; wanting to know why) as the dominant friction — no trend context and no drill path. The design system's KPI Tile at `type.metric-large` exists specifically for this screen. No action buttons anywhere on this frame — that's a binding constraint, not an oversight, because the SRS gives this role no write function in §5 and her journey has no transactional stage at all.

```
Top Nav + Left Rail
Page Title: "Executive Briefing"
Period selector (This Month / This Quarter / This Year) — the only interactive control besides
  drill-down, since Sarah's own pain point is not being able to tell a spike from a seasonal pattern.

KPI ROW — 3-4 large tiles (type.metric-large), above the fold, no action buttons:
  Fleet Availability % (target ≥85% per architecture summary §7.1, shown against target),
  Total Expenditure vs Budget (fuel + repairs + insurance + tyres, per SRS §7.1),
  Fleet Utilization %, Accident Summary / Liability Exposure count.

TREND ROW — two charts side by side (Component 8, line charts only): Expenditure trend (6-12 months),
  Availability trend (6-12 months). No sparklines on the KPI tiles themselves (redundant with these
  two full trend charts directly below — showing the same trend twice at different sizes fails the
  decorative-element test).

DEPARTMENTAL BREAKDOWN — one level of drill-down only (per persona's stated need, not a full
  multi-level analytics tool): a bar chart (Component 8) of utilization or expenditure by department,
  clicking a bar reveals that department's contributing figures inline (expand, not navigate away —
  Sarah should never leave this single screen).
```

---

## 6. FRAME-05: Finance & Cost Dashboard (Miriam — Finance Officer)

**Derivation:** Miriam's core goal is reconciliation before close, plus catching anomalies before Audit does (`01_USER_PERSONAS.md` §5). Her journey map identifies stages 2-3 (reconcile; review anomalies) as the dominant friction, and they're distinct enough to need separate destinations, not one merged view. Unlike Grace's triage hub or Daniel's throughput queue, Miriam's screen needs two coequal destinations — budget reconciliation and anomaly review — because the SRS treats these as related but distinct Finance Dashboard content (§6, §23).

```
Top Nav + Left Rail
Page Title: "Finance & Cost Dashboard"
[ Budget & Cost ] [ Anomaly Review ]  ← tabs

── Budget & Cost tab ──
BUDGET VS ACTUAL — Budget Bar (Component 7) per department/cost-center, sorted by variance
  (largest overrun first — the thing Miriam needs to see first before month-end close).
COST BREAKDOWN — bar chart (Component 8) of cost by category (fuel, maintenance, insurance, tyres)
  per department, supporting the drill Miriam's pain points call for.
EXPORT CONTROLS — PDF / Excel / CSV, gated by role permission per SRS §7 ("Reports shall support
  PDF, Excel and CSV export, subject to role permissions").

── Anomaly Review tab ──
ANOMALY QUEUE (Data Table, Component 6) — system-flagged transactions only (from the fuel anomaly
  flow, 02_USER_FLOWS.md §5): columns for transaction, vehicle, flag reason (duplicate / tank-capacity
  exceeded / odometer rollback / efficiency outlier), flagged date, status (Needs Review / Confirmed /
  False Positive). Row action: review drawer (Component 4) with the flagged transaction's full detail
  and a decision control (Confirm Fraud / Mark False Positive / Escalate to Investigation) — every
  decision writes to the audit trail (BR-009).

  **Confirmed (2026-09-13) as a TRUE overlay drawer (dimmed background, slides in from the right,
  visible close button), matching Airwallex's Spend Requests drawer pattern directly** — unlike
  Daniel's fixed pane on FRAME-02, Miriam's anomaly review is closer to Airwallex's own use case:
  a focused, deliberate investigation of one flagged transaction at a time, not a high-volume
  glance-ahead queue. The decision-focus a true drawer provides (background dimmed, full attention
  on the one transaction) is a net benefit here rather than a throughput cost. Borrow Airwallex's
  full drawer treatment: dimmed/scrimmed background, slide-in from the right, close (×) button
  top-right, generously spaced fields (transaction amount/detail as a large standalone figure,
  supporting fields in a clean row below), and bottom-anchored decision buttons — extended from
  Airwallex's two-button Reject/Approve to this system's required three-way decision (Confirm
  Fraud / Mark False Positive / Escalate to Investigation).
```

---

## 7. FRAME-06: Live Fleet Map (Grace, in-page tab — build last)

**Derivation:** Full-bleed GIS view per SRS §5.16 (GPS and Telematics). Deliberately excluded from FRAME-01's Overview (see `02_USER_FLOWS.md` §2) because it is a spatial exploration tool, not an aggregation/triage screen — the two compete for the same space but serve different cognitive tasks.

```
Top Nav + Left Rail
Page Title: "Fleet Operations Overview"
[ Overview ] [ Live Map ]  ← tabs, Live Map active

FULL-BLEED MAP — real-time vehicle position markers, color-coded by status (using the same
  Status Pill color tokens, never color-only — markers carry a label/icon on hover or selection).
  Geofence overlays. Speed-violation and after-hours-movement alert pins (distinct marker style,
  not just a color difference, per the design system's binding accessibility rule).

SIDE PANEL (collapsible): vehicle list matching current map viewport/filter, click-to-center-map.
```

Do not build this frame before FRAME-02 through FRAME-05 — it depends on a live GPS feed the architecture summary sequences as Phase 5, after Operations/Cost/Compliance are functional (§8).

---

## 8. FRAME-07: Driver Mobile Application (Joseph Mutua — County Driver)

**Derivation:** Derived directly from SRS §11 (Mobile Application) and the Driver persona (`01_USER_PERSONAS.md` §8). Unlike all other desktop back-office screens, this is an **offline-first Mobile PWA (390×844)** designed for high glare, outdoor use, and one-handed operation (48px+ minimum touch targets). Bookends both beginning and completion of an assigned trip to enable statutory distance calculation ($Ending - Starting$). **6 sub-frames as of 2026-09-21** (7A Home — rebuilt as an urgency-ordered assignment list, not a single two-state card, reusing the Needs Attention list pattern from `09_PATTERN_LIBRARY.md` §4 — 7B Walkaround Checklist, 7C Trip Start/End + Active Trip, 7D Profile, 7E Trips tab — 7D and 7E added to close the previously-empty "Profile" and "Trips" tabs; 7A rebuilt after finding SRS §11 separates "Accept" from "start trip" and after direct user feedback that a single-card model couldn't represent multiple simultaneous assignments).

**Process fix (2026-09-21) — corrected twice in the same conversation.** User asked about adopting an external mobile design system (Wise, Uber considered — neither is a real installable library; Wise's actual screens turned out to be dark/promotional, not the restrained match assumed). First correction: found **Material 3 Design Kit is already installed** in this Figma file, with real, correctly-built components (proper "List item" variants, dedicated "List" containers) — recommended using these real components instead of hand-described M3-style shapes. **User corrected this too, and was right: "we are already using material and my issue is all the generic stuff."** Using real M3 *components* is necessary but insufficient — if M3's other *defaults* (shadows, corner radii, shape language) are left untouched, a correctly-wired M3 screen still reads as a generic Android app, because M3's whole design philosophy (Google's expressive, bouncy, tonally-elevated "Material You" language) is close to the opposite of CVFMS's own deliberate, already-established visual identity (flat cards, hairline borders, near-invisible shadow — `03_MASTER_DESIGN_SYSTEM.md` §D: `radius.lg` 12px cards, `1px solid color.neutral.border`, `shadow.card` explicitly "never decorative"). Recoloring M3's stock shadows/radii to Civic Green doesn't remove M3's shadows/radii.

**Corrected standing rule for all FRAME-07 prompts: use M3 components for structure and accessibility only (touch targets, list-item anatomy, interaction states) — override every visual default with CVFMS's own already-established tokens, not just its colors:**
- Corner radius: `radius.lg` (12px) on cards, matching desktop exactly — not M3's stock rounding.
- Shadow: `shadow.card` (barely-there) or a plain 1px border, never M3's more pronounced default
  elevation/tonal-surface treatment.
- Icon weight/style: should read as deliberately chosen, not default M3 icon-set icons left as-is.
- **Superseded (2026-09-21):** this originally recommended a left-edge accent bar as a CVFMS
  signature element. Reversed after comparing directly against CVS Health's and Jira Cloud's real
  execution — a tinted status chip (colored background + text) reads as more polished. See the
  "Status treatment reconsidered" note further down this section for the full reasoning.
- Header/tab-bar dark navy must match desktop's exact `color.neutral.ink` (#0F172A) value, not an
  M3 default dark tone, for genuine cross-platform consistency, not just a similar-looking dark.

```
VIEWPORT: Native Mobile 390×844 (iPhone 15 / Android PWA)
HEADER (2026-09-21, greeting pattern extended here — see `03_MASTER_DESIGN_SYSTEM.md` Component 1):
  "Good morning, Joseph" (time-of-day greeting, same mechanic as Grace's FRAME-01), small line
  beneath: "County Driver • On Duty".
- **Correction (2026-09-21): removed the persistent "Offline Sync Ready • 100%" badge.** This text
  was carried forward unscrutinized from the original draft spec through every later consolidation
  pass — the same failure mode as the earlier SOS-grounding mistake. Two problems: "100%" is
  meaningless jargon to an ordinary user (100% of what?), and it contradicts the content-type rule
  established below (§8, State 1) — default/fine states shouldn't get a permanent badge, only
  something needing attention should (the same reasoning already used to justify opt-in delta
  chips and no stats row). The phone's own OS status bar already shows signal/connectivity a few
  pixels above this. **Replaced with: no persistent badge at all.** If sync genuinely fails, a
  small, plain-language warning can appear then ("Not synced — will update when back online"),
  but nothing should be shown for the default/working state.

PERSISTENT ELEMENT — EMERGENCY SOS (2026-09-21, corrected — see note): a small, always-visible SOS
  icon lives in the header/top app bar on every FRAME-07 sub-screen (7A, 7B, 7C, 7D) — not just
  the Home screen. **Correction on grounding: this feature has no basis in the SRS** — it first
  appeared in an earlier part of this project's history as an unstated assumption, not a
  requirement, and was carried forward and given more prominence (persistent header) before its
  basis was ever checked. Directly asked the user whether to keep it; **confirmed keep, justified
  by SRS §11's own offline-first/rural-low-connectivity rationale** for the mobile app generally —
  a genuine emergency (breakdown, accident, personal safety) with no phone signal is a real
  scenario in that context, even though the SRS never names "SOS" explicitly. Reasoning for
  placement: an emergency isn't tied to one stage of the trip, so it must be reachable regardless
  of which screen the driver is currently on. Neutral palette icon (no red), but visually distinct
  enough to find quickly under stress. **Still undecided: what SOS actually does when tapped**
  (call a specific number, alert dispatch directly, or something else) — not yet specced, needs a
  follow-up decision before this is buildable end-to-end, not just a header icon.

FRAME 7-PRE — SPLASH, LOGIN, FIRST-RUN SETUP (added 2026-09-22, locked to Components 14-16 in
`03_MASTER_DESIGN_SYSTEM.md` — this section gives content only. Closes a real gap: nothing built
before this got a driver from opening the app to Home. Grounded in SRS §9's authentication
requirements and §11's "Driver login and assigned vehicle view" as the mobile app's first named
function — not invented. Onboarding carousel explicitly rejected as unrequested consumer-app
complexity; kept only a minimal functional first-run step instead.)

- **Splash, hierarchy corrected 2026-09-22:** full-bleed Civic Green (#006837), no photo. **County
  identity leads, CVFMS is a footer attribution, not the headline** — corrected from an earlier
  version that centered "CVFMS" as the primary brand mark, backwards for a platform deployed
  per-county. Centered: county crest/logo (image, flagged as a per-county asset dependency), "
  Baringo County" (bold, white), "Vehicle Fleet Management System" (smaller, muted white) beneath
  it. Near the bottom, small and quiet: "Powered by CVFMS". Brief, checks cached auth state
  (offline-first) — auto-advances to Login (no session) or straight to Home (valid cached session).
- **Login** (form checked against [DocuSign](https://mobbin.com/screens/38b0081f-b0a6-4213-af88-cd4ca9e8c2c7)
  and [Upwork](https://mobbin.com/screens/ad035e48-ef44-4eb3-aa99-529aaca9cf14) — plain single-screen
  form, not a multi-step tenant-lookup flow, doesn't apply since CVFMS is one county system).
  **County photo banner added 2026-09-22** (user's proposal) — checked
  [Peacock's](https://mobbin.com/screens/cb9736f7-aecd-4b43-a981-81dadd209d92) full-bleed-plus-
  floating-card pattern against
  [Grill'd](https://mobbin.com/screens/261e6bbf-785c-4c59-97eb-d80ec7c5b823)/[Taco Bell](https://mobbin.com/screens/57aa091c-6caf-45c4-b2be-2ab2671fb081)'s
  top-banner-then-white-form; chose the banner pattern since Home and Profile already both use it —
  keeps one consistent rule across all three, not a fourth distinct treatment. County photo is now
  a recurring pattern across 3 screens, not the single exception it started as — tracked explicitly
  in Component 15. **Header text corrected to match Splash's hierarchy fix — "Baringo County," not
  "CVFMS," centered on the banner.** No "CVFMS" text on this screen; that attribution lives on
  Splash only. White content below: plain heading "Sign In", Staff Number field (SRS §5.22, same
  identifier already used on Profile), Password field with show/hide toggle, "Sign In" primary
  button (Component 9's solo-button spec), "Forgot password?" plain link. **No SSO button** — SRS
  §9's SSO is conditional ("where approved and technically available"), not confirmed for this
  rollout; flagged for later, not built speculatively.
- **First-Run Setup**, shown once after first login only (checked against
  [Wispr Flow's language-confirm screen](https://mobbin.com/screens/bf00197d-a10e-4333-bbaf-2816a04115eb)
  for tone — deliberately plainer than the mostly-consumer, illustration-heavy results the same
  search returned): plain heading "Quick Setup", Language toggle (English/Kiswahili, reuses
  Component 12/10's exact segmented-toggle geometry), a short plain sentence on notifications +
  "Enable Notifications" button (leads into the native OS permission dialog, doesn't replicate it)
  + "Skip for now" link, "Continue" primary button → Home.

FRAME 7A — HOME: ASSIGNMENT LIST (rebuilt 2026-09-21 — replaces the earlier two-state single-card
model entirely, per direct user feedback)

**Why this changed:** the previous design showed one dominant card representing either an incoming
decision (State 0) or the active trip (State 1), with a page-level "NEXT STEP" + sticky-footer CTA.
User pushback, and it was correct: (1) real drivers can have more than one relevant thing at once
(an active trip AND a new pending assignment), which a single-card model can't represent; (2) this
project already has a proven pattern for exactly this — Grace's Needs Attention list
(`09_PATTERN_LIBRARY.md` §4: urgency-ordered rows, each with its own scoped action, vary the verb,
never one generic button) — and Home was built as a bespoke single-card pattern instead of reusing
it. **Fixed: Home is now an urgency-ordered LIST. Each card carries its own action(s) — there is no
page-level CTA or "NEXT STEP" label anymore, because different cards need different next steps.**

**Ordering (most urgent first), corrected 2026-09-22 — see `03_MASTER_DESIGN_SYSTEM.md` Component
9's "state name corrected" note for the full reasoning:** 1) **Ready** — confirmed (Accept already
happened) and scheduled for *today*, not yet started; shows "Start Pre-Trip Inspection." This card
type was originally mislabeled "In Progress," which wrongly implied the inspection/drive had
already begun — it hasn't; a genuinely mid-trip state is a separate screen (FRAME 7C's Active Trip),
not a Home-list card, and isn't built yet. 2) a pending assignment awaiting Accept/Decline (a
decision is owed). 3) an already-accepted assignment scheduled for a future date (informational,
lowest urgency). This also resolves an earlier open question for free — "what if a trip isn't
today" no longer needs a special case, since a scheduled-for-later card just shows its own real
date, and the **full state chain is: Needs Your Response → (Accept) → Scheduled → (date arrives) →
Ready → (Start Pre-Trip Inspection tapped) → hands off to FRAME 7B/7C.**

**Consolidated layout (2026-09-21) — folds in all 5 scannability refinements above, replacing the
earlier draft that only described them in prose:**

**Rebuilt to exactly match Component 9 — Mobile Assignment Card (`03_MASTER_DESIGN_SYSTEM.md`),
2026-09-21.** Every earlier addition that didn't survive the locked-component pass is gone:
the passenger chip, the person/vehicle differentiation icons, and the status icon's circular badge
are all dropped — not because they were individually wrong, but because their cumulative effect
was the actual problem (see Component 9's "why this exists" note). What's left is deliberately
narrow: 4 groups per card, 4 type sizes total, 3 spacing values total, a closed color list, 2
button states. Nothing on this card may deviate from Component 9's exact values.

**Revised a third time (2026-09-21)** after a render introduced a genuinely better journey visual
(a vertical dot-connector-dot timeline, origin above destination) but applied the card hierarchy
inconsistently between cards — Card 1 kept time small/secondary with destination as the one bold
hero, Cards 2 and 3 instead promoted time to its own bold headline above the journey, giving those
two cards two competing dominant elements (violates §B2: exactly one dominant element, never more
than 2 sizes per row). **Resolved: Card 1's treatment is correct and now applies to all 3 cards** —
one hero (destination), time always visible but consistently secondary, never promoted to its own
headline. Two more defects fixed: Card 1 was missing its chevron (every card gets one, no
exceptions); the button text had drifted to a generic "Continue assignment" — reverted to naming
the exact next action, matching the established rule that a button always says what happens next,
never a vague verb. **Journey visual kept and formalized:** a small origin dot (muted, `#3B82F6`)
above a short vertical connector line above a destination dot+headline — clearer than the earlier
flat "🔵 From X" single line, and still just two colored markers with no computed route, so it
doesn't reopen the no-navigation-app decision. Header also revised: the greeting phrase and the
driver's name now carry different weight (checked against
[IKEA's header](https://mobbin.com/screens/236972df-1152-4b5a-9bd2-2ed6aa872220), which splits a
small greeting from a large bold name) — "Good morning," stays smaller/lighter, "Joseph" becomes
the larger, bolder element, since the personalization moment is about the name, not the phrase.

┌═══════════════════════════════════════════════┐  ← EXPANDED state only: county
║ [landmark photo, dark overlay for legibility]  ║     landmark photo + dark
║ (JM)  Good morning,           [crest]     (🔔) ║     overlay (Component 9's
║       Joseph                                   ║     county-branding note) —
║       County Driver • On Duty                  ║     collapsed state stays
╚═══════════════════════════════════════════════╝     solid #0F172A, no photo
├───────────────────────────────────────────────┤
│ Assignments                                     │  ← list section title, 18px/600
│                                                  │     (`type.section-title`) — one step
│                                                  │     down from header's "Joseph" so it
│                                                  │     doesn't compete for dominance
│ ┌─────────────────────────────────────────┐    │     (Component 9, 2026-09-22)
│ │ READY                         Today,     ›│  ← relabeled from "IN PROGRESS"
│ │                              10:30 AM    │     (2026-09-22) — confirmed +
│ │                                           │     today, not yet started; plain
│ │                                           │     colored text, no chip box; time
│ │  ○ Nakuru HQ                             │     stays small/secondary,
│ │  ┆                                       │     never promoted to headline
│ │  ● Nakuru Sub-County Office              │  ← thin vertical connector
│ │                                           │  ← destination: the ONE hero,
│ │ Mary Akinyi · Public Works · 3 passengers │     bold, dark — origin dot is
│ │ Toyota Land Cruiser · KBZ 442A            │     #3B82F6 blue, destination dot
│ │                                           │     is #006837 green (colored,
│ │ ╭──────────────────────────────────────╮ │     reversed back 2026-09-22 —
│ │ │    Start Pre-Trip Inspection  →      │ │  ← solo primary: full-width,
│ │ ╰──────────────────────────────────────╯ │     `radius.md` (8px corners),
│ └─────────────────────────────────────────┘    │     44px height (unchanged shape,
│                                                  │     this is the "solo" case)
│ ┌─────────────────────────────────────────┐    │
│ │ NEEDS YOUR RESPONSE          Tomorrow,  ›│  ← plain colored text, no chip box
│ │                                8:00 AM   │     SAME small/secondary
│ │  ○ Nakuru HQ                             │     treatment as Card 1 — not
│ │  ┆                                       │     its own bold headline
│ │  ● Molo Sub-County Office                │
│ │                                           │
│ │ James Kariuki · Agriculture · 2 passengers│
│ │ Nissan Patrol · KAX 215A                  │
│ │                                           │
│ │  ╭───────────╮  ╭───────────╮            │  ← paired buttons, resized
│ │  │ Accept →  │  │  Decline  │            │     2026-09-22: pill-shaped,
│ │  ╰───────────╯  ╰───────────╯            │     content-hugging width (NOT
│ └─────────────────────────────────────────┘    │     stretched), 44px height,
│                                                  │     filled #006837 / outline —
│ ┌─────────────────────────────────────────┐    │     see Component 9 button spec
│ │ SCHEDULED                 Thu, Sep 24,  ›│  ← muted throughout, same
│ │                                9:00 am   │     small/secondary time
│ │  ○ Nakuru HQ                              │     treatment as the other 2
│ │  ┆                                       │
│ │  ● Naivasha Sub-County Office             │
│ │                                           │
│ │ Grace Wanjiru · Fleet Office · 1 passenger│
│ │ Toyota Hiace · KBZ 104D                   │
│ └─────────────────────────────────────────┘    │
├───────────────────────────────────────────────┤
│   🏠 Home        📋 Trips        👤 Profile     │
└───────────────────────────────────────────────┘

**Per-card rules, matching `09_PATTERN_LIBRARY.md` §4 exactly (same pattern as Grace's Needs
Attention list, just applied to mobile):**
- Each card = one dominant identifier (destination), one line of context (time, requester),
  a status label distinguishable by more than color alone (a tinted chip pairing color + text,
  never color alone — see "Status treatment reconsidered" below for why this replaced an earlier
  left-edge-bar approach), and an action button scoped to what that specific card needs — never
  one generic button repeated across card types.
- **Call icon removed entirely** (reconsidered directly per user challenge). It was borrowed from
  Grab/Shopee, where a live call is essential because the driver and passenger are actively
  locating each other in real time. CVFMS's driver-requester relationship isn't that — it's a
  pre-arranged government trip with a fixed destination and time, not a live coordination problem.
  Importing that gig-economy assumption didn't fit, the same category of mistake as the earlier
  map/route creep. If a genuine "need to reach the requester" case exists, it lives inside View
  Details as a rare action, not permanent card-face real estate.
- **Special requirements** (e.g. wheelchair access) still conditional (only rendered if the
  specific assignment has one) and still shown regardless of card type — including on a pending
  "Needs Your Response" card, since it's more useful before accepting than after.
- **Content-type rule still applies per card**, reframed for the list: only actionable buttons get
  Civic Green fill; status is carried by a tinted chip (never color alone); plain informational
  text (destination, time, requester, vehicle detail) has no leading icons of its own — the
  person/vehicle icons are a deliberate, justified exception (see the differentiation-test note
  below), not a reversal of this rule.

**5 scannability refinements (2026-09-21), from general UI-scannability principles the user shared
— checked against the current card design honestly, not applied wholesale:**
1. **Anchoring to edges** — already mostly true (destination/time/requester share one left edge);
   made an explicit rule now so a future render doesn't reintroduce internal divider lines the way
   the earlier single-card drafts did. No internal dividers inside a card — consistent left
   alignment does the grouping work instead.
2. **Differentiate via a requester avatar, not just name text.** Real gap found: three cards for
   three different requesters (Mary Akinyi, James Kariuki, Grace Wanjiru) were differentiated only
   by *reading* the name. Add a small initials-avatar (e.g. "MA") beside the requester line on each
   card — a genuine scannability aid tied to a specific differentiating field, not decoration, so it
   doesn't conflict with the content-type rule above (that rule targets icons implying false
   tappability on plain facts, not differentiation aids like this).
3. **Show status via icon, not text alone.** Real gap: the three status labels were text-only. Add
   a small universal icon paired with each label — a play/arrow for "In Progress," a bell for
   "Needs Your Response," a clock for "Scheduled" — so status registers before the words are read.
   This strengthens, not just adds to, the existing never-color-alone accessibility rule, and
   matters more here than usual given the standing low-literacy design concern for this app.
4. **Manage emphasis by quieting the low-priority card, not just decorating the urgent ones.** Real
   gap: the "Scheduled" card currently lacks a colored accent bar but its text is exactly as bold
   and high-contrast as the urgent cards above it. Fix: mute its text slightly (lighter gray, maybe
   a faint background tint) so the hierarchy comes from contrast between neighbors, not only from
   what's added to the important cards.
5. **Simplify: demote the internal reference ID.** Real gap: every card currently leads with
   "TRIP · REQ-2024-0851" *before* the destination — but a driver scans for where they're going,
   not an internal reference number. Shrink it to small, muted, secondary text (or drop it from the
   card face entirely, keeping it only in View Details) so destination is unambiguously the first
   thing read on every card.

**Icon-for-density pass (2026-09-21), then corrected the same session against a sharper breakdown
of the same source material.** First pass added icons broadly (clock on time, tag on reference ID,
icons on every button, person-icon for headcount) — reasoned through field-by-field, but still
erred toward "add an icon" as the default density fix. **A more detailed breakdown of the same
video's 5 principles (Dual-Rail alignment, dissolving unnecessary containers, emphasis as
relationship, hunting vs. reading, edge structure) prompted a real self-check**, since actual
receipts — the reference case for all 5 principles — get density and clarity from *alignment and
structure*, not from icons; the "universal glyphs" principle explicitly lists them as one tool
alongside telegraphic copy and tabular alignment, not a replacement for either. Reversed part of
the first pass as a result:
- **Applied Dual-Rail (new):** time and headcount are now on the same row, time left-aligned,
  headcount right-aligned — like a receipt's item-vs-quantity split — instead of headcount buried
  inline at the end of the requester line.
- **Applied "dissolving containers":** the reference ID no longer gets its own dedicated line on
  the card face at all (a stronger move than the earlier "just shrink it" fix) — it's already one
  tap away via the chevron, so it doesn't need to invent its own row. Still available in View
  Details.
- **Walked back:** the clock icon and the button icons (checkmark/X/checklist), added in the first
  pass. Honest reconsideration: "10:30 AM" and "Accept" are already as fast to read as an icon
  would be to recognize, so those icons were decoration riding on the "add icons" instruction, not
  functional density reduction — and piling more small glyphns onto an already-detailed card risks
  the "cognitive saturation" the emphasis-as-relationship principle warns about directly.
- **Kept:** the person/group icon for headcount, specifically because it now functions as a
  receipt-style "quantity column" value in the right rail — position + a well-established glyph
  convention (headcount icon + number, used across booking/reservation apps generally) together
  carry meaning here, unlike the icons that were walked back.
- **Still rejected, unchanged from the first pass:** icon-only for department name (no universal
  icon exists) and icon-only for special requirements (must stay icon+text per the binding
  accessibility rule — precision matters more than density for a compliance-relevant flag).
- **Edge structure applied to special requirements:** stays an edge-anchored accent strip matching
  the card's own left-edge-bar language, never its own separately-bordered nested box.

**3 more clarity fixes (2026-09-21), all pointing the same direction: an icon or shorthand only
helps if it's actually unambiguous, not just compact.**
1. **SOS was rendered as literal text ("SOS") inside a circle — wrong.** Spelling out an acronym
   defeats the point of using an icon at all: it still requires reading and decoding, exactly what
   an icon should let a driver skip, especially given the standing low-literacy design concern for
   this screen. Fixed: a real emergency pictogram (not letters) — e.g. an alert/exclamation glyph
   distinct from ordinary warning-triangle "caution" icons (the earlier defect this was originally
   meant to fix), sourced as an actual icon asset, not text-in-a-shape.
2. **Headcount icon+bare-number ("👥 3") is genuinely ambiguous, reconsidered.** It relies on the
   viewer already knowing this exact app convention (person-icon + number = passenger count) —
   a reasonable assumption for a frequent rideshare-app user, a much weaker one for this specific
   audience. Bare icon+number could be misread as almost anything with no way to check. **Fixed:
   spelled out as "3 passengers"** (still right-aligned in the dual-rail position) — the icon
   wasn't earning its ambiguity-risk given how little space "passengers" actually costs.
3. **Requester name + department had no role label — genuinely unclear who this person is.**
   "Mary Akinyi · Public Works" alone doesn't say whether she's the requester, a passenger, a
   supervisor, or someone else entirely. **Fixed: "Requester: [Name] · [Department]"** — the same
   discipline already applied to every other field on this card (status is labeled, the FROM→TO
   line is unambiguous), just not consistently carried through to this one until now.

**Header identity slot corrected (2026-09-21): that position should be the driver's own avatar,
not SOS.** The top-left slot beside the greeting is naturally read as "who am I" — pairing the
driver's own photo/avatar with "Good morning, Joseph" reinforces personal identity, consistent with
the personalization work already done for this screen (greeting, Profile screen, language toggle).
SOS doesn't belong there; it was occupying the identity anchor instead of an actual identity
element. **Moved SOS to the opposite corner (top-right)** — already empty since the jargon-y
"Offline Sync Ready" badge was removed from that spot earlier — where it stays just as persistent
and reachable across every FRAME-07 sub-screen, without competing with or displacing personal
identity.

**3 elements borrowed from inDrive and Airtasker (2026-09-21), after user said the build still
wasn't satisfying and asked to check real references again:**
1. **Colored dot markers for origin/destination**, replacing the "→" arrow — confirmed via
   [inDrive's "My requests" screen](https://mobbin.com/screens/de59f6e9-ae7a-46e0-9909-8987040046bb),
   which uses a blue dot for pickup and a green dot for drop-off next to each address. A
   well-established ride-hailing convention, instantly recognizable, and doesn't reopen the
   no-navigation-app decision — it's two colored markers next to plain text, nothing computed or
   routed.
2. **A "hero" time treatment** — time is now visually the most prominent element on the card
   (large, bold), the equivalent of how [Airtasker's task cards](https://mobbin.com/screens/56f72678-2dc0-4be8-a8a7-b508e0fc12b3)
   make the price the unmistakably dominant number. Reasoning carries over from the earlier
   decision to elevate time's visual weight (a missed departure has an immediate, visible
   consequence) — this pushes that same reasoning further, all the way to "clearly the most
   prominent thing on the card," not just "as bold as everything else."
3. **Fact chips for headcount** — "[ 3 passengers ]" as a contained pill, not a plain inline text
   fragment — confirmed via inDrive's "Pay with SPEI" / "Movers" chip treatment. Fully worded (no
   ambiguity, keeping the earlier fix that reversed icon+bare-number), but visually distinct as a
   quick-scan fact rather than blended into a longer text line.
**Not borrowed:** Airtasker's requester photo — CVFMS already uses initials-avatar treatment
elsewhere in this system; no reason to switch to a full photo just because Airtasker does it.
Vehicle info (reg plate + model) stays a plain "Vehicle:" line, not a chip — chips suit short,
single-value facts (a headcount), not a compound value like "Toyota Land Cruiser · KBZ 442A."

**Status treatment reconsidered (2026-09-21) — replaced the left-edge accent bar with a tinted
chip, a genuine reversal, not an addition.** After a render still didn't feel "world class" despite
being structurally correct, checked real best-in-class execution directly: [CVS Health's Visit
Checklist](https://mobbin.com/screens/5367bf1b-68be-434d-825e-33fa368bfd42) and [Jira Cloud's task
list](https://mobbin.com/screens/f206f339-e758-44fe-828e-a5c8644da613) both use a **tinted status
chip** (colored background + colored text, e.g. amber-tinted "Action Needed," green-tinted
"Completed") rather than a left-edge bar. Comparing directly, the chip reads as more considered and
polished. **Reversing the earlier "left-edge bar is a CVFMS signature element, keep it" decision**
— that reasoning was sound at the time (a genuine non-M3 invention worth reinforcing), but concrete
comparison against real best-in-class execution outweighs defending a prior call for its own sake.
**Fixed:**
- Status is now a tinted chip (light green bg + dark green text for "In Progress", light amber bg
  + dark amber text for "Needs Your Response", light gray bg + gray text for "Scheduled") —
  replaces the left-edge accent bar entirely, not in addition to it (having both would be two
  systems saying the same thing).
- The status icon (play/bell/clock) sits inside a small soft tinted circular badge, matching CVS
  Health's consistent icon-container treatment — likely a real contributor to the earlier
  "icons look inconsistent" problem, since icons floating loose at different implicit sizes read
  as less considered than icons uniformly contained.
- **The passenger-count chip now uses the same tinted-chip style**, not a bare outline — the card
  previously mixed two different chip languages (outline for passengers, nothing/bar for status),
  which reads as unplanned. One consistent chip treatment throughout.
- **Vehicle icon fixed** — the rendered icon looked like a steering wheel/seatbelt shape, not a
  clearly recognizable car — undermining the entire point of using it to differentiate the row.
  Needs an unambiguous car/vehicle silhouette icon.

**One more icon opportunity found (2026-09-21), applying the same differentiation test as before.**
The Requester and Vehicle lines were structurally identical ("Label: Value", "Label: Value") —
nothing distinguished "this is about a person" from "this is about a vehicle" except reading the
label word itself. Added a small person icon before Requester and a car icon before Vehicle —
this passes the same test the dot markers and chip passed (genuine differentiation between two
similar rows, not decoration): both icons are static, muted gray (not accent green), non-circular
and not button-shaped, so they read as category markers on plain text, not as tappable elements.
This is different from the earlier walked-back button icons (checkmark/X on Accept/Decline), which
failed the same test because button text was already fast enough to read — here, two visually
identical label:value rows genuinely benefit from a shape-based way to tell them apart at a glance.

**First render of the type/spacing-scale rebuild checked (2026-09-21) — real progress, 2 defects
found, one of them significant:**
1. **Accept and Decline rendered as two visually identical outline buttons** — both white/bordered
   with similar weight, undoing the hierarchy work already done earlier (Accept must be
   unmistakably the dominant/expected path — filled Civic Green — with Decline clearly secondary
   as an outline button). A driver looking at this render has no way to tell which action is the
   default one.
2. **Vehicle assignment info (reg plate, model) was missing from every card — a real functional
   gap, not a style issue.** Traced back: this silently dropped out when Home was rebuilt from the
   old two-card model (a separate Trip card + Vehicle card) into the compact list — nobody
   explicitly decided where vehicle identity should live in the new structure, so it just vanished,
   and wasn't caught until this render surfaced it. **Fixed: added a compact "Vehicle: [Model] ·
   [Reg Plate]" line to every card**, including "Needs Your Response" — a driver deciding whether
   to accept an assignment needs to know which vehicle they'd be responsible for before committing,
   not just after. Fuller vehicle detail (location, fuel level, dispatch-clearance status) stays
   in View Details — the card face only needs enough to identify the vehicle, not describe it.

**6th fix, found separately (2026-09-21): the destination line was a bare place name with no
indication it's a directional trip.** "Nakuru Sub-County Office" alone doesn't say whether it's a
destination, a pickup point, or one leg of a round trip — a real ambiguity, not a labeling nicety,
given the SRS's own "expected return" field (§5.4, already found in the IA pass above) implies
these are usually from-base-and-back journeys, not one-way drops. **Fixed: show both endpoints as
plain text, "Nakuru HQ → [destination]"** — no map, no computed route/distance, just naming the two
places (this doesn't reopen the earlier no-navigation-app decision, since nothing here is computed
or routed, only stated). The "Nakuru HQ" side reuses the same base location already shown on the
Vehicle card, but the two aren't redundant: the Vehicle card answers "where do I find the vehicle,"
this line answers "what's the shape of the journey." A full round-trip readout (out and back) isn't
needed on the card face — "expected return" specifics stay in View Details, per the existing SRS
§5.4 field tiering. Applied consistently across all 3 card types (In Progress, Needs Your Response,
Scheduled) in the layout above.

**Decline (with reason)** — tapping opens a mandatory reason field (matches the system's standing
require-justification pattern: BR-009's override justification, §5.24's workflow rejection/return-
for-correction) → submits, and the assignment **routes back to Daniel's Dispatch Queue for
reassignment**. **Explicitly not a driver-to-driver transfer** — considered and rejected directly
with the user, since a driver handing off a trip themselves would bypass Daniel's dispatch
authority, cutting against the maker-checker model this system enforces everywhere else.

**Still open, not yet resolved:**
- **Superseded (2026-09-22): SOS is removed entirely, replaced with a notification icon** (SRS
  §5.23, Notification and Alert Management — a real, named requirement, unlike SOS which needed
  after-the-fact justification). Same position and neutral treatment, plus an unread-count badge
  (`color.status.critical` red dot, only shown when something's unread). See
  `03_MASTER_DESIGN_SYSTEM.md` Component 9's header section for the full spec. Tapping it opens a
  notification list — a conventional pattern that doesn't need the same open-question flag SOS's
  tap-behavior did.
- **CTA copy** — "Start Pre-Trip Inspection" is SRS/compliance terminology; a plainer alternative
  ("Check My Vehicle →") was proposed but never signed off. Same open question, now scoped to
  whichever card carries that action.
- **View Details chevron content** — unchanged from before: purpose, full passenger breakdown,
  special requirements in full, expected return time/date (per the SRS §5.4 field tiering already
  established — destination/time/requester+status stay on the card face, the rest lives behind the
  chevron).
- **Inspection cadence (once accepted, before the "in progress" card can show "Start Pre-Trip
  Inspection")** — separately reasoned through and left as a recommendation, not a locked rule
  (custody-based: skip re-inspection only across back-to-back dispatches in the same vehicle with
  no return to the pool in between). Unaffected by this list restructure.
- **FRAME 7E (Trips tab) needs reconciling against this list.** Home now surfaces active + pending
  + near-term scheduled items directly — it's not yet decided what's left for the Trips tab
  specifically (likely: full history, plus anything scheduled far enough out that it shouldn't
  clutter Home). Not resolved in this pass — flag before building 7E further.
- **No distance/ETA/route line, no map, no stats/KPI row** — all still explicitly excluded, same
  reasoning as before (this isn't a navigation app; a driver has nothing to compare/triage that a
  stats row would serve).

**First render checked (2026-09-21) — structurally correct, 4 polish fixes needed:**
1. **Missing letter-spacing on card status labels.** The design system already defines `type.label`
   (`03_MASTER_DESIGN_SYSTEM.md`) as uppercase with +0.02em tracking for exactly this kind of small-
   caps text — the render's "IN PROGRESS" / "NEEDS YOUR RESPONSE" / "SCHEDULED" labels were tightly
   kerned with no tracking applied. Apply the existing token, don't invent new label styling.
2. **Left-edge accent bars have hard corners against the card's rounded corners** — reads as a
   rectangle laid on top of the card rather than integrated into its shape. Inset the bar and match
   its corner radius to the card's, or round just the bar's outer edge to follow the card curve.
3. **"SCHEDULED" card has zero accent bar**, which next to two clearly color-coded cards looks like
   something's missing rather than intentionally neutral. Give it its own neutral-gray accent bar
   (`color.neutral.border` or similar) so all three cards read as one consistent system that differs
   only in color meaning, not in whether they have the treatment at all.
4. **Accept/Decline buttons are unevenly proportioned in a way that reads as accidental**, not
   deliberately hierarchical. Fix the ratio to roughly 65/35 (Accept wider, clearly dominant) with
   both buttons matched in height, rather than the current uneven split with an awkward gap.

FRAME 7A.1 — VIEW DETAILS (added 2026-09-22, locked to Component 10's sibling — Component 11 in
`03_MASTER_DESIGN_SYSTEM.md`, this section gives content only). Reached via the chevron on any
Home card — referenced constantly since 7A was first built, never actually speced until now.

**Locked as a full page, not a drawer (decided 2026-09-22)** — every real reference cited below is
itself a full page, content volume is well beyond the Fail sheet's compact 2-question form, and
forward navigation (View Details → FRAME 7B) needs to work page-to-page. See Component 11 for the
standing rule this establishes: drawer for a small nested task, page for a genuinely deeper view.

**Type/spacing, exact — reused from Components 9/10, not reinvented:** section labels 12px/600
uppercase +0.02em `#64748B` (same treatment as Component 9's status label, neutral not status-
colored). Label/value rows: label 14px/400 `#334155`, value 14px/600 `#0F172A`. Page padding 16px
both sides. 8px between rows in one section, **32px between sections (raised from 24px, 2026-09-23
— see `03_MASTER_DESIGN_SYSTEM.md` §1 third pass, `space.section-gap`)**, still deliberately larger
than Component 9's 12px card-internal gap — these are full independent sections on a page, not card
sub-groups. No divider lines — whitespace only.

**Three fundamentals fixes, added 2026-09-22 (asked directly whether the underlying craft could
improve, beyond the content fixes above):**
- **Fixed 110px label column** — without this, each row's value starts wherever its own label ends,
  so values drift out of alignment depending on label length. Now every value on the page starts at
  the same x-position (matches how Waymo's reference screen aligns its own rows).
- **Section label sits 8px above its own first row, not 24px** — the 24px figure is reserved for
  the gap between one section's last row and the *next* section's label. Without this distinction,
  a label could read as floating equidistant between two sections instead of clearly belonging to
  the content beneath it.
- **Documents row: 44px minimum height** — the one genuinely tappable row on this page (every other
  row is read-only text); had no touch-target size locked before, a real omission.

- **App bar:** back arrow + plain title "Trip Details" (not a greeting).
- **Reference strip**, 16px below the app bar: "REQ-2024-0851" — the ID dissolved off the card
  face earlier lives here. **12px/400 exactly, `#64748B`** — a render rendered this bold and large
  enough to compete with the destination headline; corrected, must never outweigh it.
- **Journey block**, 32px below the reference strip: exact reuse of Component 9's dot-connector-dot
  visual (Nakuru HQ → Nakuru Sub-County Office). **Destination name upgraded to `type.hero-mobile`
  (22px/700), 2026-09-23** — the screen's one genuine focal element, per the third pass.
- **"TRIP INFO" section**, 32px below the journey block (checked against [BlaBlaCar's Ride Details screen](https://mobbin.com/screens/3bfb96de-284d-4f5a-9e7c-b2844cc6674f)
  and [inDrive's ride receipt detail](https://mobbin.com/screens/7f7c7ccb-96f7-4e90-b3f1-1c60be362dca)
  for the label/value pairing; [inDrive's "Order" screen](https://mobbin.com/screens/ad7715b7-1700-49cc-9e1d-02df2a4e673a)
  is the closer overall structural match — journey + vehicle info + note + stacked actions —
  confirmed by checking inDrive directly rather than assumed, since most of its *live* trip-
  tracking screens are map-heavy and don't apply given this project's no-map rule): "Departure:
  Today, 10:30 AM", "Expected Return: Today, 3:00 PM" (SRS field, shown nowhere else in this flow),
  "Purpose: Site inspection — Public Works quarterly review" (SRS field, shown nowhere else),
  "Project/Activity: Q3 Infrastructure Audit" if present.
- **"REQUESTER" section** (label corrected from a rendered "Officer" — SRS §5.4 and the rest of
  this app both say "Requester"), 32px below Trip Info: "Mary Akinyi · Public Works", full
  passenger manifest — **"Mary Akinyi (Requester), John Otieno, Grace Wambui — 3 passengers"**
  (tagged explicitly since she's both the requester and traveling; a render showed her name in both
  places with no stated relationship, reading as unclear or a possible duplication bug), special
  requirements in full if any (e.g. "Wheelchair-accessible vehicle required"). No call/chat icon —
  already rejected earlier.
- **"VEHICLE" section**, 32px below Requester: "Toyota Land Cruiser · KBZ 442A", "Nakuru HQ Yard ·
  Bay 4" stay plain rows. **Fuel Level + Dispatch Clearance converted to a 2-tile Stat Tile row,
  2026-09-23** (see §1 and Component 11) — "75%" / "Fuel Level" tile beside "Passed" / "Dispatch
  Clearance" tile (green if passed, red if ever blocked). **Each tile's icon now sits inside an
  Icon Badge (36px tinted circle), 2026-09-23 third pass** — gray circle/gray icon for Fuel Level,
  green circle/green icon for Dispatch Clearance — supersedes the bare-icon wording above.
- **"DOCUMENTS" section** (conditional, only if attached), 32px below Vehicle: plain file-name
  list, tap to view.
- **Action zone**, fixed to the bottom of the viewport (not part of the scrolling content), same
  anchored treatment as Component 10: mirrors whichever card this was opened from — Accept/Decline
  from a "Needs Your Response" card, "Start Pre-Trip Inspection →" from a "Ready" card, no action
  zone at all from "Scheduled" (purely informational there).
- **Icon rule reversed 2026-09-23 — see Component 11 and §1 of the design system.** The 2026-09-22
  "no icons on static rows" finding above is superseded, not deleted — kept for its reasoning trail,
  but small icons (18-20px, muted) are now permitted on this page's informational rows for warmth,
  part of a broader "simple is not sterile" correction. **Vehicle photo also added, upgraded to a
  full-width hero 2026-09-23 (third pass, supersedes the original 64×64px thumbnail size)** — a
  real photo of the vehicle, full card width, 140px tall, 12px corner radius, now sits at the top
  of the "VEHICLE" section.
- **Supplements the card-face buttons, doesn't replace them** — a driver can still decide directly
  from Home without opening this screen; View Details is for a driver who wants the full picture
  first. See Component 11 for the full reasoning on why this was resolved this way.

FRAME 7B — 60-SECOND WALKAROUND CHECKLIST (locked to Component 10, 2026-09-22 — see
`03_MASTER_DESIGN_SYSTEM.md` for the exact spec; this section gives content only)

**Superseded (2026-09-22): a single Pass checkbox is replaced by a real two-state Pass/Fail
toggle.** A checkbox (checked = done) conflates "not yet inspected" with "passed" — a real
compliance risk given BR-004 and the Dispatch Gate depend on Fail being a deliberate, recorded
finding. See Component 10's "why a real two-state toggle" note for the full reasoning.

- **App bar (M3 small top app bar, 2026-09-22):** leading back arrow (44px touch target) + title
  "Pre-Trip Inspection • KBZ 442A" (left-aligned, not centered) + trailing progress pill **"0/5
  Checked" (was 0/4 before the Fuel Level row was added, 2026-09-24)** (not "Passed" — a completed
  checklist can still contain a Fail). Full spec incl. sourcing caveat on M3 dp values: Component 10.
- **5 rows, stacked two-line layout (revised 2026-09-22, replaces the original single-line
  layout):** line 1 = category icon + label (wraps freely, up to 2 lines, no crowding); line 2,
  8px below = Pass/Fail segmented toggle, left-aligned. Fixes long labels ("Headlights, Brake
  Lights & Indicators," "Fire Extinguisher & First Aid Kit") pushing into the buttons on one line.
  **Button sizing, corrected same day after a direct comparison against Perplexity's compact
  action pills:** tappable zone stays 44px (this project's accessibility floor, unchanged), but the
  **visible pill renders at 36px**, with invisible padding making up the rest — same distinction
  now locked in Component 9 for Accept/Decline too. Not a touch-target regression, a visual-weight
  fix layered on top of the layout fix, not instead of it.
  1. Tyres & Spare Wheel
  2. Headlights, Brake Lights & Indicators
  3. Engine Oil & Coolant Levels
  4. Fire Extinguisher & First Aid Kit
  5. **Fuel Level, added 2026-09-24** — grounded in SRS §5.6, moved here from Component 17's Start
     Journey screen (see Component 10 in `03_MASTER_DESIGN_SYSTEM.md` for the full reasoning). This
     row's Line 1 also carries a trailing segmented pill ("75% (3/4 Tank)", right-aligned) showing
     the self-reported reading — informational only, not itself an input; no other row has this.
     Its Fail sheet skips the "Affected item(s)" step (a single reading, not a bundle of physical
     items) and goes straight to reason chips: Below 1/4 Tank / Empty or Near-Empty / Fuel Gauge
     Malfunction / Other.
- **Fail detail opens a bottom sheet, not inline expansion (revised 2026-09-22)** — chosen over
  inline to keep the list stable regardless of how many rows fail at once (inline expansion on
  several rows at once compounds into a tall, reflowing list). **Sheet header, confirmed as
  rendered: "Report [item] issue"** (e.g. "Report tyre issue") — shorter than the originally
  drafted question format ("What's wrong with the [Item Name]?"), kept as the standard since it
  reads more naturally. Content order, top to bottom (matches [Lime's "Report Issue" sheet](https://mobbin.com/screens/a79e71e9-c9ce-4c2d-95f5-d33ce4bd5378) —
  location, then reason, then photo):
  1. **"Affected item(s)" chips (added 2026-09-22, label confirmed as rendered)** — every row's
     label bundles more than one physical item (Tyres *and* Spare Wheel; Headlights *and* Brake
     Lights *and* Indicators; Oil *and* Coolant; Extinguisher *and* First Aid Kit), so the sheet
     first asks which is affected, closing a real gap surfaced by looking at Lime's diagram-plus-
     chips approach more carefully (the full diagram itself is still rejected as overkill — see
     Component 10). See Component 10 for the full per-item chip sets.
  2. "What's wrong?" reason chips (multi-select, scoped per item — reuses Turo's "Physical damage"
     checklist), see Component 10 for the full per-item chip sets.
  3. Mandatory camera/photo capture.
  4. Optional "+ Add more detail" text area.
  5. Sheet's own "Save" button, disabled until a "which one" chip, a reason chip, and a photo are
     all present.
  **On save, the row collapses to a compact one-line summary** ("Front-Left, Worn Tread · Photo
  attached," critical red, 12px) with an "Edit" affordance to reopen the sheet — this is what keeps
  the main list from growing unpredictably. Checked against real DVIR industry practice: "failed
  items require a description and, critically, a photograph."
- **Pass items get no per-item photo requirement — evidence instead comes from automatic GPS +
  timestamp capture at inspection start and submission**, verifying the driver was physically at
  the vehicle for the check (the real industry anti-"pencil-whipping" control). **No visible caption
  for this (removed 2026-09-22)** — a render check found the bottom of the screen crowded (banner +
  caption + 1-2 buttons stacked tightly), and the caption was never for the driver anyway, just the
  system reassuring itself; capture still happens silently. Requiring a photo on every one of the 5
  items regardless of outcome was considered and rejected: it would fight this screen's own
  "60-second" speed goal, and a photo of a routine, fine item documents little on its own.
- **Completion banner, un-boxed (corrected 2026-09-22)** — was a filled/bordered box, which sat
  directly above the primary button at similar width/shape and read as another button, not a status
  message ("messages and buttons are conflicting," flagged directly). Fixed: plain icon + text, no
  background/border — only real buttons keep a box treatment now. All-Pass: check icon + "No
  defects logged. You are cleared for departure." (informational green, no container). Any Fail:
  alert icon + **"X defect(s) found — departure blocked pending authorization."** (critical red, no
  container).
- **Action zone anchored as one fixed unit, corrected 2026-09-22** — a render check found
  inconsistent spacing between states, since the banner sat at the end of the scrolling checklist
  content while the button was pinned separately to the viewport bottom, so the gap between them
  varied with content height. Fixed: banner + button(s) are now one fixed, non-scrolling zone at
  the bottom of the screen, checklist scrolls independently above it — guarantees the same 12px
  banner-to-button gap in every state. See Component 10's "action zone" note.
- **Fail blocks departure — grounded directly in SRS §5.6** ("Prevent dispatch where mandatory
  conditions are not met, subject to authorized override" — naming this exact checklist: tyres,
  lights, brakes, safety equipment). Not a UI judgment call; corrected 2026-09-22 from an earlier,
  wrongly-non-blocking draft. See Component 10 for full reasoning.
- Primary CTA, two paths: **all Pass** → "Confirm Inspection & Proceed →" (Civic Green, disabled
  until all 4 rows are marked). **Any Fail** → same slot instead shows "Request Override — Report
  to Transport Office" (critical red) — not a self-override; routes to Daniel's Dispatch Queue for
  authorization, the same channel already locked for a Home-screen Decline (`02_USER_FLOWS.md` §3).
- **Offline override fallback (2026-09-22) — required by this system's own offline-first
  architecture and real low-connectivity sub-counties (e.g. Baringo).** Three tiers, not just the
  single digital path above: (1) digital override request when connectivity allows (above); (2) if
  data fails but voice/SMS may still work, a fallback action — **de-emphasized to a plain text
  link, not a full-width outline button**, after a render check found two stacked full-width
  buttons reading as equal-weight choices rather than a primary action with a rare exception below
  it — "No connection — Call Transport Office," opens the device dialer, then requires a logged
  "Verbally authorized by [name/role]" confirmation on return; (3) last resort, no signal at all —
  an offline provisional override behind an explicit acknowledgment dialog (not a casual tap),
  logged and flagged "pending review" until it syncs. All three stay distinguishable in the audit
  trail. Full spec: Component 10's "offline override fallback" note.
- **Still open:** no screen exists yet for the driver's wait state between requesting a digital
  override and Daniel authorizing it. Needs its own design pass before this flow is fully closed.

FRAME 7C — TRIP START & TRIP END LIFECYCLE BOOKENDS (locked to Component 17, 2026-09-22 — see
`03_MASTER_DESIGN_SYSTEM.md` for the exact spec; this section gives content only. Closes the
largest remaining SRS §11 gap: "start/end trip" and "capture odometer and fuel information.")

**Two patterns borrowed from [Grab Driver's active-trip screens](https://mobbin.com/screens/bcfa763e-74d6-4b71-9add-b54464f5453f), map/route/ETA elements explicitly excluded per the standing no-navigation-app decision:**
1. Buttons name the exact physical action at every stage, never generic "Next"/"Continue."
2. A simple stage indicator ("Stage X of 3") shows exactly where the driver is.

**"Arrived at Destination" question, resolved 2026-09-22, not left open:** a CVFMS driver has one
destination per trip, with any return leg already captured as metadata ("expected return"), not a
separate interactive step — unlike Grab's driver juggling multiple sequential stops. Nothing
operationally happens at arrival that needs its own recorded moment. One continuous Active Trip
state is sufficient; no "Arrived" step added.

- State 1 (Start Journey), no back arrow (forward-only):
  - **Starting Odometer: pre-filled from the vehicle's last recorded reading, editable, no camera
    badge** — corrected 2026-09-22. Checked [Turo's odometer/fuel screen](https://mobbin.com/screens/fddca36b-af63-46e8-b170-e7b1ffaba2f9):
    odometer is a plain confirmable number there, not photo-verified; Turo's actual photo step is
    separate, optional, and about general condition, not the odometer. A camera badge here would
    also duplicate evidence Component 10's checklist already gathers before this screen loads.
  - **Fuel Level Indicator removed from this screen, 2026-09-24** — moved to FRAME 7B's checklist as
    its 5th Pass/Fail row instead (see FRAME 7B and `03_MASTER_DESIGN_SYSTEM.md` Component 10 for
    the full reasoning: SRS §5.6 names fuel level as a mandatory dispatch-gate condition, which this
    screen's passive pill didn't reflect). The 2026-09-23 pill-background regression flagged earlier
    is now moot — the pill itself has moved screens.
  - **Vehicle photo, confirmed 2026-09-24 as a horizontal identity card, not a bare photo** (see
    `03_MASTER_DESIGN_SYSTEM.md` Component 17 State 1 for the full reasoning) — photo (~72×72px,
    rounded corners) on the left, "Toyota Land Cruiser" (bold) / "KBZ 442A" (muted) on the right,
    light gray card background (#F8FAFC, 12px radius), sitting above the Starting Odometer section.
    This is an improvement found in a render, not the original spec (which only asked for a bare
    photo) — locked as the standard because it's the pairing, not the photo alone, that makes the
    identity-confirmation purpose legible.
  - Notice microcopy: **converted to a tinted card, 2026-09-23** (§1 second pass) — light green
    background (#E6F2EB), thin darker-green border, 12px radius, 12px padding, small location-pin
    icon (16-18px, #006837) beside "Starting this trip enables continuous GPS location logging to
    county dispatch."
  - Primary CTA: "Start Journey Now" — **44px height (corrected from 52px)**, filled #006837,
    Component 9's solo-button spec exactly
- State 1.5 (Active Trip) — the screen a driver sees while actually driving:
  - Stage indicator: "Stage 2 of 3 · In Transit"
  - **No vehicle photo — tried 2026-09-23, reverted same day** (see Component 17 in
    `03_MASTER_DESIGN_SYSTEM.md` for the full reasoning: Turo's repeated-photo logic doesn't
    transfer to a single continuous trip with one vehicle across three sequential screens; the
    photo stays on State 1 only, where it has genuine identity-confirmation purpose).
  - Active Journey Banner: "In Transit to Nakuru Sub-County Office • Started 10:32 AM" (persists).
    **Destination name upgraded to `type.hero-mobile` (22px/700), 2026-09-23** — bigger/bolder than
    the "Started 10:32 AM" text beside it, the screen's one focal element.
  - Two contextual actions, **corrected to Component 9's exact Secondary/outline button style (not
    vague "chips")**: "Log Fuel Stop" · "Report Breakdown / Defect" — 44px tappable/36px visible,
    content-hugging, neither required to proceed. **"Report Breakdown / Defect" leads to its own
    dedicated reporting screen, not yet designed — scoped as the next piece of work, not built
    here.**
  - Primary CTA stays available throughout: "Complete Trip & Record Closing Odometer"
- State 2 (End Journey & Closure):
  - **No vehicle photo — same reversal as State 1.5, see above.**
  - Active Journey Banner persists. **Destination name upgraded to `type.hero-mobile` (22px/700),
    2026-09-23**, same as State 1.5.
  - "TRIP SUMMARY" section label — **reuses Component 11's exact uppercase/tracked section-label
    style** (confirmed via [Mercedes-Benz's "Trip data" screen](https://mobbin.com/screens/b492b0f8-789c-4388-b298-ddfb78aff7f6),
    already cited). **Plain stacked label/value rows — NOT a Stat Tile row.** A 3-tile conversion
    was attempted 2026-09-23 across four separate prompts and never rendered correctly; reverted
    after direct user pushback ("the three columns simply does not work"). Root cause: Closing
    Odometer is an active input field, unlike Vehicle section's two read-only facts — it needs
    full-width room, not a third-width tile. Starting Odometer "142,850 km" (read-only), Closing
    Odometer (editable, full-width bordered input, "Enter reading" placeholder, "km" suffix — the
    original working treatment), Distance Travelled auto-calculates once Closing Odometer has a
    value.
  - Visual stage-stepper (3 dots) added beside the "Stage X of Y" text on all 3 states, see §1.
  - Post-trip check: "Any mechanical defects during trip? [None / Report]"
  - Primary CTA: "Finalize & Close Trip" → releases vehicle back to 'Available' pool

**Not built in this pass:** Report Breakdown/Defect (currently just a button) and Submit
Maintenance Request — both real SRS-named gaps, flagged as the next work, not silently deferred.

FRAME 7F — REPORT AN ISSUE: BREAKDOWN / ACCIDENT (locked to Component 18, 2026-09-23 — see
`03_MASTER_DESIGN_SYSTEM.md` for the exact spec; this section gives content only. Reached from
FRAME 7C's "Report Breakdown / Defect" button. Grounded in SRS §5.15's field list, scoped to only
the fields a driver can actually capture at the scene — cost/claims/investigation/liability fields
belong to a back-office workflow, not this form.)

- **Type selector:** heading "What happened?", two full-width tappable cards — "Mechanical
  Breakdown" / "Accident / Collision" — not a bottom sheet, this screen is already a dedicated
  destination.
- **Breakdown path** (checked against [Shell's "Report an issue" screen](https://mobbin.com/screens/92de5008-73a5-4de0-9534-b0809e004a1c)):
  auto-filled vehicle context (read-only), "What's wrong?" reason chips (Engine / Brakes / Tyres /
  Electrical / Other — same chip geometry as FRAME 7B), **photo recommended, not mandatory** (a
  driver mid-breakdown, possibly blocking traffic, shouldn't be gated on a photo before reporting),
  optional Notes, Submit → routes to Daniel's Dispatch Queue.
- **Accident/Collision path** (SRS §5.15's driver-capturable subset): auto-filled vehicle/date/
  time, GPS location (confirmable/editable), required Description, Conditions chips (Clear / Rain /
  Night / Poor Visibility / Other), "Other parties involved?" Yes/No → repeatable name/contact/
  vehicle-reg fields if Yes, optional Police Reference, optional repeatable Witnesses, Photos
  (recommended), Submit. **Submission also triggers an immediate notification** (SRS §5.23 names
  "accident" as a notification-triggering event) — not just a queued entry, unlike the lower-
  urgency breakdown path.
- **Offline fallback, both paths:** reuses Component 10's plain-text "No connection — Call
  Transport Office" link (not a full button). [Temu's "Request a phone call to report" link](https://mobbin.com/screens/eb4ba5ea-f13c-4732-bd74-2e92edaf662c)
  independently confirms this is standard practice for report flows, not a CVFMS-only pattern.

FRAME 7G — SUBMIT MAINTENANCE REQUEST (locked to Component 19, 2026-09-23 — see
`03_MASTER_DESIGN_SYSTEM.md` for the exact spec; this section gives content only. Third and last
of the three real SRS §11 gaps found by checking the full function list. §5.9's work-order fields
mostly belong to Workshop execution, not the driver — except odometer, a point-in-time fact the
driver naturally has at hand, same reasoning as FRAME 7C's Starting Odometer.)

- **Entry point:** a plain text link, "Request Maintenance," at the bottom of FRAME 7A.1 (View
  Details)'s Vehicle section — reuses that screen's existing low-emphasis link treatment.
- **Vehicle context** (auto-filled, read-only), same style as FRAME 7F's Breakdown path.
- **Current Odometer Reading** — large, prominent display (checked against [Rivian's "Vehicle maintenance" screen](https://mobbin.com/screens/56bd4a31-4b7f-4bd9-828d-f7098b65171a),
  the closest real match), same bordered/boxed treatment now confirmed for FRAME 7C's Starting
  Odometer. **Same shared data source as FRAME 7C, not an independent value** — pre-filled from
  the vehicle's last recorded reading (updated whenever a trip closes), editable if wrong.
- **"What needs attention?"** — reason chips, same geometry as FRAME 7F: Routine Service / Brakes /
  Tyres / Engine / Electrical / Other.
- **Urgency** — "Routine" / "Urgent" segmented toggle, **neither selected by default** (same no-
  default-state rule as the Accident path's "Other parties involved?" toggle — an unreviewed
  default on a field that affects triage priority is a real risk, not a style choice).
- **Description** (optional), same treatment as FRAME 7F's Notes field.
- **Photo** (optional), same camera + "Add Photo" outline button as FRAME 7F.
- **Submit → routes to Daniel's Dispatch Queue** (resolved 2026-09-23, same channel as Decline,
  Fail-override, and FRAME 7F's reports — kept consistent rather than routing directly to Peter's
  Workshop board, so every driver-initiated exception goes through one triage point, not a special
  case for this one request type).
- **Offline fallback:** same plain-text "No connection — Call Transport Office" link as FRAME 7F.

FRAME 7D — DRIVER PROFILE (locked to Component 12, 2026-09-22 — see `03_MASTER_DESIGN_SYSTEM.md`
  for the exact spec; this section gives content only. Closes a real gap: the bottom tab bar's
  "Profile" tab had no screen behind it. Personalization scope confirmed directly with the user:
  profile content + a language toggle.)

**Tab root, no back arrow** — same category as Home, not a drilldown like View Details.
**Reuses Component 11's section-label + fixed-label-column pattern**, not a new "card" treatment.

**Header — overflowing-avatar hero (2026-09-22), checked against 4 real profile screens**
([LinkedIn](https://mobbin.com/screens/dddb4708-b756-49bc-a73a-df0096817dc2),
[Places/Enrique Olvera](https://mobbin.com/screens/6c86f45d-ac38-480c-b2ed-ca55ecbb2aab),
[Glassdoor](https://mobbin.com/screens/65721aa3-c6cc-44c0-8fc2-ebf864b68fd9),
[Vivino](https://mobbin.com/screens/4948dc9f-8682-4622-a059-63b6c0cce728)): same county-landmark
photo + dark overlay as Home's header (confirmed to reuse, not a separate image), 88px avatar with
a white ring border straddling the banner/content boundary, "Joseph Mutua" at 20px/700 (reuses
Home's expanded-header name size), "County Driver" subtitle below at `type.caption`.

- App bar: plain title "Profile", no back arrow, sits on the photo banner (same translucent-circle
  treatment as Home's header icons).
- "IDENTITY" section, 24px below the role subtitle: Staff Number (SRS §5.22 HR Integration field),
  Station — "Nakuru HQ Transport Pool". **Role is not repeated here** — already stated in the
  header, avoiding two statements of the same fact on one page.
- "LICENCE" section: Class — "Class A, B, C1" (matches the desktop Driver Registry format). Expiry
  — **reuses SRS §5.23's own 30/14/7-day compliance-alert cadence**, not a new threshold: plain
  date if >30 days out; "Expires in N days" in warning-amber if 8–30 days; critical-red if ≤7 days.
  Same licence-validity data BR-003 checks at Daniel's Dispatch Gate, surfaced here for the driver.
- "PREFERENCES" section: Language toggle, English / Kiswahili — reuses Component 10's exact
  Pass/Fail toggle geometry (same two-choice pill), not a new control. Mobile-only for now; desktop
  localization is a separate, unresolved question.
- **Sign-out, corrected 2026-09-22 — checked against 8 real profile screens**, not assumed: a
  majority (Mercedes-Benz, Panera Bread, Crypto.com, 5 Minute Journal) give this an outline button,
  not plain text. **Fixed: reuses Component 9's exact Secondary/outline button style** (same as
  Decline), content-hugging and centered, not full-width. 32px gap above it (double the normal
  section gap) to read as a distinct, rare action.

No fixed action zone — this is a settings-style page, not a decision screen.

**Trips tab (FRAME 7E) validated against real references, 2026-09-22:** [Navan's Trips screen](https://mobbin.com/screens/dc0200de-0819-491e-b2dd-ce7b3d9d81d2)
(closest domain match — corporate travel) confirms the two-state urgent/muted color split;
[Zomato's bookings screen](https://mobbin.com/screens/b2da1a7b-4031-4299-88e6-4942956cd1bc)
confirms the uppercase section labels and plain colored status text (no chip). See Component 13
for the full citation trail, including a Qantas-referenced date-grouping pattern flagged for later
once the list grows past a couple of items.

FRAME 7E — TRIPS TAB (locked to Component 13, 2026-09-22 — see `03_MASTER_DESIGN_SYSTEM.md` for
  the exact spec; this section gives content only. Closes a second gap: the "Trips" tab had no
  defined content.)

**Real scope question resolved, not assumed: what does this add beyond Home?** Home is the
urgency-ordered *execution* view — only what's current/actionable today. Trips is the complete
*intake ledger* — every assignment not yet completed, ordered chronologically, including far-out
scheduled items Home doesn't surface to avoid clutter. Different jobs, not a duplicate list.

- App bar: plain title "Trips", no back arrow (tab root), subtitle "2 upcoming" (plain text, not a
  pill/badge).
- List, ordered by date ascending (not urgency — the one structural difference from Home). Each row
  reuses Component 9's exact card anatomy — destination + date/time, requester, status text, no
  chip. **Two states, not three** (this list asks "did I respond," not "is it today"): "Awaiting
  Your Response" (warning-amber) or "Accepted" (plain neutral — deliberately not reusing "Ready"/
  "Scheduled" language, since that's Home's question, not this list's).
- **Tap behavior, corrected 2026-09-22** — an earlier draft pointed to "FRAME 7A/State 0," a state
  that no longer exists post-rebuild. **Fixed: every row opens Component 11 (View Details)** — the
  Needs-Response variant for an unanswered item, the read-only Ready/Scheduled variant for an
  accepted one. Reuses the screen already built, doesn't invent a second detail view.
- Past/completed trips: a separate section below, or a filter toggle — **not yet fully specced**,
  this frame's primary job is the incoming/upcoming list; history display is a follow-up detail.
```

---

## 9. FRAME-08: Requester Portal & Approver Review (Mary Akinyi & Department Supervisor)

**Derivation:** Derived from SRS §5.4 (Vehicle Request Management) and the Requester / Approver profiles in `CVFMS Primary profiles.docx`. Provides a clean self-service experience for departmental staff and an inline approval control for supervisors.

```
TOP NAV + SCOPED LEFT RAIL (Requester View — minimal, only "My Requests" and "Submit Request")
PAGE TITLE: "Vehicle Requisitions • Department of Public Works"

LEFT PANE (~50% width): NEW REQUISITION FORM
- Requester Info (Read-only): Mary Akinyi • Senior Engineer, Public Works
- Destination & Itinerary: Destination ("Nakuru Sub-County Office"), Date/Time ("Sep 12, 2024 • 10:30 AM"), Return Date ("Sep 12, 2024 • 05:00 PM")
- Travel Justification: Purpose ("Emergency culvert and drainage inspection following heavy rainfall")
- Passenger Manifest: 3 Passengers (List of staff names/departments)
- Activity / Project Code: "PW-ROADS-2024-08" (Configurable: either operational travel or project vote)
- Vehicle Preference: 4WD Utility Vehicle
- Primary Action: [Submit Vehicle Requisition] (Civic Green)

RIGHT PANE (~50% width): MY REQUESTS & LIVE APPROVAL TRACKER
- Active Request Card (REQ-2024-0851):
  - 4-Stage Visual Stepper: [1. Submitted] ──► [2. Approved] ──► [3. Dispatched] ──► [4. In Transit]
- Contextual Approver Drawer (Triggered when Supervisor logs in):
  - Title: "Requisition Authorization: REQ-2024-0851"
  - Configurable Wording Banner: "Operational Travel Authorization • Routine Pool Dispatch"
  - Maker-Checker Rule: Disabled if viewed by requester ("Self-approval prohibited under PFM Act")
  - Action Controls: [Approve Requisition] (Civic Green) · [Return for Correction] · [Reject Request]
```

---

## 10. FRAME-09: Statutory Audit Trail & Forensic Explorer (Auditor — Read-Only)

**Derivation:** Derived from SRS §8 (Audit Trail) and the Auditor profile in `CVFMS Primary profiles.docx`. Strictly read-only forensic interface designed for statutory compliance under the PFM Act 2012 and PPADA 2015.

```
TOP NAV + AUDIT RAIL (Independent Audit Profile)
PAGE TITLE: "Statutory Audit Trail • County Government of Nakuru"
SUBTITLE: "Internal & External Audit View • Immutable Ledger"

FILTER & TIME CONTROLS:
- Date Range Picker, Actor Filter, Module Filter (Dispatch, Fuel, Workshop, Compliance, System)
- Quick Exception Toggles: [Show Overrides Only] · [Show Fuel Flagged Only] · [All Events]

MAIN AUDIT TABLE (Component 6, Read-Only Data Table):
- Columns:
  1. Timestamp: "Sep 12, 2024 • 10:42:15 EAT"
  2. Event ID: "AUD-89214"
  3. Actor / Role: "Daniel Otieno (Transport Officer)"
  4. Entity / Target: "Vehicle KBZ 442A • REQ-2024-0851"
  5. Action: "Dispatch Override Authorized" (Amber pill)
  6. Detail / Justification: "Urgent medical supply delivery — maintenance rescheduled"
  7. Verification Hash: "SHA256: 7f8a...c39e" (Immutable tamper-proof indicator)
- Zero Write Affordances: Structurally NO edit, delete, or override buttons.
- Header Action: [Export Certified Audit Pack (PDF / CSV)] for Auditor-General presentation.
```

---

## 11. Notes on Method

Every frame's layout above is derived fresh from its persona's stated core goal and the SRS content assigned to that role (§6, §7.1), not carried over from the archived v1.x blueprint's 16 rounds of FRAME-01 revision. Two structural conclusions reappear from the archive regardless — Needs Attention as the dominant, tightly-scoped hero on FRAME-01, and the live map as a separate tab rather than an Overview widget — because both follow directly from Grace's persona and the SRS's own GPS-phasing, not because the prior spec's conclusion was assumed correct going in. The Recent Activity open question, left unresolved in the prior handover, is resolved here (§2) as part of this restart rather than deferred again.

**v2.1 check (this revision):** when `01_USER_PERSONAS.md` and `02_USER_FLOWS.md` were revised to v2.1 to apply the `ui-ux-expert` journey-mapping method explicitly, every frame derivation above was re-checked against the new journey-stage/friction-point language. Result: no frame, component, or layout decision changed — each frame's "dominant friction" now cited above is the same underlying fact as the old "pain point," just traceable to a specific journey stage instead of an unordered list. This is expected: the blueprint's decisions were already being justified against real friction, the v2.1 persona rewrite just made the stage-by-stage structure of that friction explicit rather than implicit.
