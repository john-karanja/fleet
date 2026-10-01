# CVFMS: System Map — Templates, Patterns, Components, Connections

**Document ID:** `DOC-CVFMS-013`
**Started:** 2026-09-24 (desktop chat)
**Purpose:** stop designing page by page. Every screen is an instance of a small set of **page
templates**, assembled from shared **patterns**, built from library **components**, and linked to
other screens through a known **connection map**. A new page means picking a template, filling
its slots and checking its links. It never means inventing a layout.

**How this relates to other docs:**
- `09_PATTERN_LIBRARY.md` holds the proven prompt fragments from the first 7 screens. Several of
  its patterns are superseded by this map (see §7). Reconcile 09 against this doc once the
  templates are locked.
- `12_DESKTOP_REDESIGN.md` holds the working log: audits, prompts, render checks.
- `05` holds the references behind each pattern.
- This doc is the structure everything hangs on.

**Two standing goals (user, 2026-09-24) that every proposal is checked against before it's shown:**
1. **Best for the user:** the page opens with what *this* person must act on; reference data sits below.
2. **Reuse first:** every section is an existing template, pattern or component from this map. A new
   element must be justified as a future shared pattern, never a one-off.

---

## 1. The four layers

```
TEMPLATES (9)  → page skeletons with named slots      e.g. T1 Role Home
PATTERNS (~16) → reusable sections that fill slots    e.g. P6 Exception group list
COMPONENTS     → Figma library parts inside patterns  e.g. Status Pill, Tab Item
CONNECTIONS    → every link: from pattern → to template (with filter applied)
```

Rule of the system: **a pattern can only be used in the slots its template allows**, and **every
link a pattern shows must resolve to a template in §5**. A dead link is a design bug.

---

## 2. Page templates

| # | Template | Job it serves | Slots (top → bottom) | Budget (§7 of doc 12) |
|---|---|---|---|---|
| **T1** | **Role Home** ("Today" / "Overview") | Know state, act on exceptions | Greeting + scope switcher + freshness stamp → Live strip (conditional) → State band + 1 money/secondary card → Exception list ∥ Oversight → Watch list | ≤ 5 blocks + live strip |
| **T2** | **Work Queue** (list + detail pane) | Clear items one by one, fast | Title + filter row → status chips → compact list (left) ∥ detail pane with gate/decision (right) | ≤ 3 blocks |
| **T3** | **Registry** (table) | Find, compare and bulk-act on many records | Title + filter row + saved views → summary band (optional) → table → pagination; row click → T7 or drawer | table + ≤ 1 band |
| **T4** | **Board** (Kanban) | Move work through stages | Title + filter row → columns with cards; card click → drawer | columns ≤ 6 |
| **T5** | **Analytics** | Understand trends, compare, export | Title + purpose line + filter row (period + comparison) → metric band → 2 charts → drill-down table | ≤ 4 blocks |
| **T6** | **Map** | See where things are | Map full-bleed + collapsible side list; marker click → drawer | — |
| **T7** | **Record Detail** | Everything about one vehicle/driver/request/job | Identity header (photo, ID, status, primary action) → tabs (Overview · History · Documents · …) → section cards | 1 primary action |
| **T8** | **Action Drawer / Modal** | Decide or act on one item without leaving the page | Title + context → facts → checks (if gated) → justification (if required) → primary + secondary action | 1 primary action |
| **T9** | **Form / Wizard** | Create or change a record | Title → steps (if > 1) → fields (single column, per memory rule) → review → submit | 1 column for inputs |

Mobile has its own template set (Home list, Detail, Checklist, Trip stage, Report flow). That's
owned by the mobile chat. §6 links both sets where they share data.

---

## 3. Shared patterns (built once, reused everywhere)

| # | Pattern | Used in | Reference | Status |
|---|---|---|---|---|
| P0 | **Page header** (same on every template, see §3a) | all desktop templates | Amplitude, Asana, Wix | Proposed |
| P1 | **Title row**: title · context/time window · one exit link | every card, every template | Wix, Okta | Proven (v3) |
| P2 | **Scope switcher** ("All stations ▾") in the date line | T1, T3, T5 | Shopify locations | New (§8e) |
| P3 | **Filter row**: icon dropdowns + Reset + freshness right-aligned | T2, T3, T4, T5 (not T1) | Airwallex | Proven (v3) |
| P4 | **Freshness stamp**: "Live · Updated 10:42 · 44 trackers offline" | T1, T5, T6 | Okta | New |
| P5 | **Live strip**: 1 sentence + ≤ 3 calm rows; collapses to "All clear" | T1 | OpenAI, Okta | Pending render |
| P6 | **Exception group list**: problem types with counts, collapsible to records, in-card tabs. On full-width pages, split into two internal columns (actions | follow-ups) instead of stretching rows | T1, T7 (per-record issues) | Okta Tasks, Apollo | Proven (v3) |
| P7 | **Status band**: cells that sum to a total, color only on the exception cell, optional stacked bar | T1, T3, T5 | Xero, Apollo | Proven (v3) |
| P8 | **Pipeline strip**: arrow segments with counts, bottleneck tinted, each segment links to a filtered T2 | T1, T2 header | Jobber, QuickBooks | Pending render |
| P9 | **Approval rows**: title, reason, requester, age, "Review" → T8 | T1 (approver/manager), T2 | Airwallex | Proven (v3) |
| P10 | **Watch line**: module · time window · one exception · link | T1 | Fresha | Proven (v3) |
| P11 | **Pace card**: one number + budget + pace bar with "today" marker | T1, T5 | — | Pending render |
| P12 | **Gate checklist**: Pass / **Warning** / Fail / **Not yet assigned** (neutral) rows; only Fail blocks; passes collapse to "4 passed" | T2, T8, mobile checklist | Doc 03 Component 4 | **Needs rule fix** (warning semantics, §8) |
| P13 | **Vehicle row**: photo thumb · reg · model · reason · action | T1 (expanded), T2, T3, T8 | Turo | Proven |
| P14 | **Decision footer**: primary + secondary + (destructive as text link) | T2, T8, T9 | — | Needs definition (§8) |
| P15 | **Empty / all-clear line**: sections shrink to one line when there's nothing to show | all | OpenAI | Rule only |
| P17 | **Lifecycle stepper (labeled)**: steps named in the §6a vocabulary, current step as text; unlabeled dots are banned. **Usage:** full stepper where someone tracks progress (requester, approver, drawer); a compact "Step X of 7" line in work queues | T7, T8, requester list | — | New (doc 12 §10) |
| P16 | **Problems move up**: a module's off-normal state becomes a P6 row on T1 | T1 | — | Rule (§8d of doc 12) |


### 3a. P0 Page header: where the page title and breadcrumbs live

**Rule:** the **top bar is global** (search · notifications · account) and looks identical on
every page. **Everything about the current page lives in the page header** in the content area,
built from the same 3 rows on every template:

```
Row 1  breadcrumb   13px #64748B      Operations / Fleet overview
Row 2  H1 title  ─────────────────   right side: scope switcher │ freshness stamp  (or page actions)
Row 3  tabs (only if the page has views)
```

| Template | Row 1 breadcrumb | Row 2 H1 | Right side of row 2 |
|---|---|---|---|
| T1 Role Home | `Operations / Fleet overview` | Greeting ("Good afternoon, Grace") | Scope ▾ · freshness stamp (with date) |
| T2 Work Queue | `Operations / Dispatch management` | "Dispatch & Requisition Queue" | Primary page action (if any) |
| T3 Registry | `Vehicle management / Fleet registry` | "Fleet registry" | "Add vehicle", export |
| T4 Board | `Maintenance / Workshop` | "Workshop board" | "New job card" |
| T5 Analytics | `Fleet analytics / Reporting` | "Executive briefing" | Export |
| T6 Map | `Tracking & telematics / Live map` | "Live map" | Freshness stamp |
| T7 Record Detail | `Vehicle management / Fleet registry / KBZ 442A` (**clickable** except the last segment) | Record identity ("KBZ 442A · Toyota Land Cruiser") | Primary record action |
| T8 Drawer | none; the drawer shows a context label ("Dispatch override · REQ-2024-0851") | Drawer title | Close |

- **Breadcrumb segments** are pillar / page / record.
  - The pillar segment isn't clickable: it's a menu group, not a page.
  - Page and record segments are clickable when they aren't the current page.
  - The breadcrumb follows the site hierarchy, not the click history; browser Back covers history.
- **This revises the 2026-09-13 breadcrumb decision** (`04` §2 correction: breadcrumbs only on
  drill-downs, as a non-clickable label). That decision was made when the nav was a flat 20-item
  list. Since 2026-09-15 the nav is grouped into 8 pillars, so real hierarchy exists. A one-line
  breadcrumb on every page now does two jobs: it names the page (so a T1 greeting can be the H1
  without the page losing its name) and it's the way back up from T7 detail pages.


### 3b. Live alerts inside the exception list (P5 → P6), and how it scales

Decision under review (2026-09-24): live alerts become the first group ("LIVE NOW") of the
Needs-attention list instead of their own card. Scaling rules:

1. **Tight definition.** A live alert is *possible misuse happening now and not yet picked up*:
   ghost trip, unauthorised or after-hours movement, geofence exit. Speeding, idling and
   harsh-braking are **GPS events** and go to the events register ("82 unreviewed →"), not here.
2. **It leaves the group once picked up.** When someone opens and acknowledges an alert (assigns
   it, or marks it under review), it drops out of LIVE NOW. The count is always unhandled alerts only.
3. **≤ 3 alerts → one row each** (vehicle, place, time, "Review trace").
4. **> 3 alerts → rows grouped by alert type with a count**, collapsible like every other P6 group:
   "Possible ghost trip · 6 vehicles · Review all →". Opening a group shows its 3 most recent
   vehicles, then "+ N more →".
5. **The overflow goes to a dedicated Live alerts queue** (T2: list + map trace in the detail
   pane), which is added to the page register as a destination.
6. **The station scope applies.** A station-scoped user only sees their station's alerts.
7. **The "Live (N)" tab** filters the list to live alerts only.

---

## 4. Component inventory (Figma "Refined" page)

| Component | Exists? | Serves | Action |
|---|---|---|---|
| Layout/Page Shell, Navigation/Sidebar (8), Top Bar | ✅ | all | Fonts → Lexend/Source Sans 3 (Prompt 0); Top Bar right padding |
| Status Pill (5 variants) | ✅ | everywhere | Align vocabulary to §6; add icon to every variant |
| Checklist Row (Pass/Fail) | ✅ | P12 | **Add `Warning` variant** |
| KPI Tile | ✅ | T5 only now | Remove from T1; keep for analytics |
| Data Display/Status Breakdown Bar | ✅ | P7 | Rebuild as bar + cells (P7), drop legend |
| Data Display/Alert Card (3) | ✅ | P5 | **Rebuild as a row** (no tinted box) |
| Data Display/Section Card | ✅ | P1 wrapper | Update header to title · context · link |
| Summary Field Grid, Status Row (4) | ✅ | T7, T8 | Keep |
| Navigation/Tab Item, Controls/Filter Dropdown | ✅ | P3, P6 tabs, T7 | Add leading-icon variant for P3 |
| Table Header Cell, Table Data Cell | ✅ | T3 | Keep; add thumbnail cell variant (P13) |
| **Pipeline Segment** | ❌ | P8 | New: first / middle / last, default + bottleneck |
| **Exception Group Row** | ❌ | P6 | New: collapsed / expanded, severity group label |
| **Approval Row** | ❌ | P9 | New |
| **Watch Line** | ❌ | P10 | New |
| **Pace Bar** | ❌ | P11 | New: on pace / ahead (amber) |
| **Scope Switcher**, **Freshness Stamp** | ❌ | P2, P4 | New (small) |
| **Vehicle Row** | ❌ | P13 | New: compact / with action |
| **Decision Footer** | ❌ | P14 | New: blocked / ready / override-open |

**Build approach:** components are built directly in Figma via `use_figma`, not through AI prompts.
Structural precision is exactly where prompting has failed repeatedly (alert boxes, rings,
buttons). Screens are then *assembled* from instances, via prompts or directly. The Figma MCP
connection must be re-authorized (`/mcp`) first.

---

## 5. Page register — every screen, its template, its status

Roles and landings are from `Test Login Accounts.docx` (13 roles).

| Role | Landing (template) | Other pages (template) | Built? |
|---|---|---|---|
| Fleet Manager (Grace) | **Today** (T1): reference frame `v3 / fleet-operations-overview`, **lock pending polish (doc 12 §8i)** | Live Map (T6), All Vehicles (T3), Vehicle detail (T7), Compliance (T3), Override review (T8) | T1 v3 in progress; T6, T3 v1; Compliance ❌; Vehicle detail ❌; T8 v1 |
| Transport Ops (Daniel) | **Today** (T1) | Dispatch & Requisition Queue (T2), Active trips (T3/T6) | T1 ❌; T2 v1 (+ a new render, doc 12 §4a) |
| Fleet Operations | **Today** (T1) | Registry (T3), Vehicle detail (T7), Register vehicle (T9), Inspections/Documents (T3) | ❌ all |
| Approver | **Today, approvals first** (T1) | Approval queue (T2), Review (T8) | ❌ |
| Executive / Director (Sarah) | **Overview** (T5-flavoured T1) | Reports (T5), drill-downs (T3) | FRAME-04 v1 |
| Finance (Miriam) | **Overview — Finance** (T5) | Anomaly review (T2), Cost by vehicle (T3) | FRAME-05 v1 |
| Workshop Manager (Peter) | **Workshop Board** (T4) | Job card (T7/T8) | FRAME-03 v1 |
| Mechanic | **My Jobs** (mobile/T2) | Job card | ❌ |
| Requester (Mary) | **Requests** (T3 own requests) | New request (T9), Request detail (T7) | FRAME-08 specced, ❌ |
| Auditor | **Overview — Audit** (T1 read-only) | Audit Trail (T3), Evidence (T7) | FRAME-09 specced, ❌ |
| Administrator | **Admin** (T3 set) | Users, Roles, Workflows (T3/T9) | ❌ |
| Driver (Joseph) | **My Trip** (mobile) | Checklist, Trip stages, Report | Mobile chat |
| — | — | Driver Management registry (T3) + Behaviour tab | v1 (loosest build) |
| — | — | Fuel Management: Log (T3) + Anomalies (T2) | ❌ |

**The big win:** 5 roles land on a **T1 Role Home** (Fleet Manager, Transport Ops, Fleet Ops,
Approver, Auditor). Lock T1 once on Grace's page, and the other four are the same template with
different slot content. Mostly that's a table of which pattern goes in which slot per role (§5a).

### 5a. T1 slot content per role

| Slot | Fleet Manager | Transport Ops | Fleet Operations | Approver | Auditor (read-only) |
|---|---|---|---|---|---|
| Live strip | Misuse alerts | Trips running late / off-route | — | — | New exceptions since last visit |
| State band | Vehicle status (sum 1,056) | Today's trips by stage | Vehicle records by document status | My queue by age | Transactions by type |
| Secondary card | Fuel pace | Driver availability | Custody transfers pending | Budget used by my approvals | Overrides this month |
| Exception list | Blocking dispatch / due this week | Requests stuck > 1 day | Expired documents / inspections | Awaiting my approval (first) | Flagged transactions |
| Oversight | Dispatch pipeline + my approvals | Dispatch pipeline (actionable) | Registration pipeline | Approval pipeline | — |
| Watch list | Workshop, Drivers | Vehicles returning today | Disposals | Returned requests | Evidence requests |

---

## 6. Connection map (where every link goes)

### 6a. Shared vocabulary — one status model, web + mobile

- **Vehicle status (a partition that must sum to fleet size):** Available · Allocated · On trip ·
  In workshop · Grounded · Pending disposal.
- **Request/trip lifecycle:** Submitted → Approved → Transport review → Driver assigned (Needs
  driver) → Ready → Dispatched (awaiting driver) → Pre-trip → On trip → Closed. Side exits:
  Returned, Rejected, Recalled.
- **Chip color meaning:** grey = waiting on someone else · amber = waiting on *you* · green tint =
  ready/done · red = blocked.
- **Canonical demo dataset:**
  - REQ-2024-0851 · Mary Akinyi · Public Works · KBZ 442A Toyota Land Cruiser · Joseph Mutua ·
    Nakuru HQ → Nakuru Sub-County Office · odometer 142,850 → 142,914.
  - Fleet 1,056 (812 / 31 / 118 / 64 / 23 / 8).
  - Stations: Nakuru HQ, Molo, Njoro, Naivasha.
  - People: Grace Wanjiru, Daniel Otieno, Peter Kamau, Miriam Chebet, Sarah N., Alice Njoroge.
  - No other names reuse these first names.

### 6b. Links from Grace's Today (T1)

| From (pattern) | Link | To (template, filter applied) |
|---|---|---|
| P4 stamp | "44 trackers offline" | Live Map (T6), filter = offline |
| P5 live strip | "Review trace" | Live Map (T6) focused on vehicle + trip trace drawer (T8) |
| P5 | "82 unreviewed GPS events →" | GPS events register (T3) ❌ not designed |
| P7 fleet band | a cell (e.g. Grounded) | All Vehicles (T3), filter = that status |
| P11 fuel | "Fuel log →" / "2 anomalies" | Fuel Management (T3 log / T2 anomalies) ❌ |
| P6 exceptions | quick links Compliance · Workshop · Drivers | Compliance (T3) ❌ · Workshop Board (T4) · Driver Mgmt (T3) |
| P6 | "Renew all →" / per-vehicle "Renew" | Renew insurance drawer (T8) ❌ |
| P6 | "View job card →" | Job card (T7/T8 in Workshop) |
| P8 pipeline | a segment | Dispatch Queue (T2), status chip = that stage |
| P9 approvals | "Review" | Dispatch Override Review (T8) ✅ v1 |
| P10 watch | Workshop / Drivers | Workshop Board (T4) filter = past promised date · Driver Mgmt (T3) filter = licence expiring |

**Unresolved destinations (to design):** GPS events register, Fuel Management, Compliance, Renew
insurance drawer, Vehicle detail (T7), Trip trace drawer.

### 6c. The demo spine (6-stage lifecycle), across templates

Requester **T9 New request** → Approver **T1/T8 approve** → Transport **T2 dispatch gate** (fails:
KBZ 442A grounded → override → Grace **T8**) → Driver **mobile** checklist/trip → Fleet Manager
**T1 / T6** sees it on trip → Auditor **T3 audit trail** shows the chain.

---

## 7. Audit method — run on every page, same order

1. **Job:** whose page, which journey stage, what one question it answers.
2. **Template fit:** which T#; does the page follow its slots? If not, why?
3. **Tiering:** every item tagged Tier 1/2/3 (doc 12 §7.1); Tier 3 items leave the page.
4. **Density:** blocks, tiles, rows, repeated numbers against the budget (doc 12 §7.2).
5. **Pattern and component reuse:** which P# and components it uses; anything bespoke has to justify
   itself or become a pattern.
6. **Connections:** every link resolves to a T# with a filter; no dead ends; every inbound link
   from §6 lands correctly.
7. **Vocabulary and data:** §6a statuses, chip colors, canonical demo data, no raw codes, human
   dates.
8. **Rules:** gate semantics, one primary action, no self-approval, name + role in the top bar.
9. **References:** at least 3 Mobbin references for any new pattern (doc 06 §1).

Output per page: a findings table (severity-ranked) + a fix list mapped to templates/patterns,
so a fix to a *pattern* is made once and flows to every page using it.

**Superseded patterns in `09_PATTERN_LIBRARY.md`:**
- The KPI Row as a landing pattern (now P7 band + P11).
- The flat Needs Attention list (now P6).
- The always-visible override field (now T8/P14 override-open state).
- The two page-title forms still stand.

---

## 8. Open system decisions (need answers before templates lock)

1. **Gate warning semantics (P12):** does a Warning (e.g. insurance expires in 4 days, after the
   trip) block dispatch? Proposed: **no**. A Warning informs and is logged; only a Fail blocks.
   The render in doc 12 §4a blocked on a warning.
2. **Decision footer (P14):** Transport Officer on an HOD-approved request: "Reject" or "Return"?
   Proposed: "Return to requester" (text link, needs a reason). Rejecting is the approver's power.
3. **Duplicate checks:** one insurance check with three states (valid / expiring / expired), not
   two separate rows.
4. **Executive landing:** T5 analytics or a T1 home with analytics slots? Proposed: T1 skeleton,
   with the band and secondary cards showing KPIs against target.

---

## 9. Execution order

1. **Lock rules:** answer §8.
2. **Build components:** the 8 new ones + 3 updates in §4, directly with `use_figma` (needs Figma
   re-auth).
3. **Lock T1:** finish Grace's Today v3 from instances. Then T1 for Transport Ops and Approver are
   slot swaps (§5a).
4. **Lock T2 + T8:** Dispatch Queue + Override Review, the demo spine's core.
5. **Audit existing pages with §7:** All Vehicles and Driver Mgmt (T3), Workshop (T4), Finance and
   Executive (T5), Live Map (T6).
6. **Design missing destinations:** Compliance, Fuel Management, Vehicle detail, Audit Trail,
   Requester (FRAME-08).
7. **Reconcile 09:** update it to point at this map; delete superseded fragments.


---

## 10. The object model: how pages fit together (senior-designer pass, 2026-09-24)

**The core insight:** CVFMS is not a set of modules. It's a handful of **objects** that move
through **lifecycles**, and **roles** act on them at specific steps. Every page is either a
*role's view of work waiting at their step*, a *browse view of an object*, or *the object itself*.
The Requests-page confusion (doc 12 §10f) came from designing a module page before defining the
object's lifecycle and who acts where.

### 10a. Core objects and how they connect

```
            requested by                allocated               assigned
Requester ─────────────► REQUEST / TRIP ◄──────── VEHICLE ◄──── ... DRIVER
                           │   (one ID, one lifecycle, web + mobile)
                           │ blocked by                ▲ grounded by
                           ▼                           │
                     EXCEPTION / ALERT ──raises──► JOB CARD (workshop)
                           │                           │
                    APPROVAL (override, transfer)   FUEL TXN · DOCUMENT (insurance, inspection)
                           │
                     AUDIT EVENT (every action on every object)
```

**Objects:**
- **Request/Trip** is the spine: one object, one ID (`REQ-2024-0851`) from submission to closure.
  The driver's mobile trip is the same object in its later stages, not a separate one.
- **Vehicle, Driver, Job card, Document, Fuel transaction** each have their own lifecycle, and
  they block or unblock requests.
- **Approval** is a small object, attached to whatever it approves.
- **Audit event** is written by every action on every object.

**The rule that follows:** each object gets **one detail view (T7/T8), reused everywhere**. The
footer shows only the actions *the viewer's role* can take at *the current step*. Each role gets
**queues** (T2) filtered to the steps they act on, and **browse views** (T3) of the whole set.

### 10b. Request/Trip lifecycle × role: who acts at each step

Sources: `02` §3 (SRS §5.4 workflow + dispatch gate), the profiles doc, and the test accounts.
**"?" = unconfirmed; ask the product owner / dev team.** This table decides every request page.

| Step | Requester | Approver | Transport Ops | Fleet Manager | Fleet Ops | Driver | Auditor |
|---|---|---|---|---|---|---|---|
| Draft / Submitted | create, edit, submit, cancel | — | — | view | — | — | view |
| Awaiting approval | cancel | **approve / reject / return** | view | view (approves only if granted) | — | — | view |
| Returned | **correct & resubmit** | — | — | view | — | — | view |
| Transport review | view | — | **review / return** | view | — | — | view |
| Needs vehicle | view | — | **allocate** | **?** allocate / reallocate | **?** (custody) | — | view |
| Needs driver | view | — | **assign driver** | **?** | — | — | view |
| Ready (dispatch gate) | view | — | **dispatch**, or request override | view | — | — | view |
| Override requested | — | — | view | **approve / deny** (no self-approval) | — | — | view |
| Dispatched · awaiting driver | view | — | reassign if declined | view | — | **accept / decline** | view |
| Pre-trip | view | — | view | view | — | **checklist, start** | view |
| On trip | view | — | monitor | **monitor; act on live alerts** | — | **end trip, report issue** | view |
| Closed | view | — | — | view | — | — | **review evidence** |

**Mismatches to resolve:**
- The live app splits "Vehicle allocated" and "Driver assigned" into separate steps; our pipeline
  shows only "Needs driver". **Adopt the live app's two steps** ("Needs vehicle", "Needs driver").
  The pipeline strip then has 6 stages up to Awaiting driver.
- Whether the Fleet Manager allocates or reallocates (the "?" cells) decides whether Grace has real
  work on the Requests page, or only oversight plus override approvals.

### 10c. What this changes: pages become views of objects

| Role | Home (T1): "Waiting on you" pulls from all objects | Their queue (T2), their steps only | Browse (T3) | Object detail |
|---|---|---|---|---|
| Requester | Returned to you · upcoming trips | — | My requests | Request detail (T7), requester actions |
| Approver | Awaiting your approval | Approval queue | All requests (scope) | same Request detail, approve/return footer |
| Transport Ops | Needs vehicle/driver · Ready · declined by driver | Dispatch queue | All requests | same Request detail, gate + dispatch footer |
| Fleet Manager | Overrides · live alerts · blocking compliance | — (or allocation, if "?" = yes) | Vehicle requests (oversight), Fleet registry | same Request detail, override footer |
| Driver (mobile) | My trip | — | — | Trip stages (mobile) |
| Auditor | New exceptions | — | Audit trail | Evidence view (read-only) |

**Consequences:**
1. **One Request detail component** (T7 page / T8 drawer) is built once, with the P17 stepper,
   trip facts, P13 resources, the P12 gate, and a **role-aware P14 decision footer**. The
   Dispatch Queue pane, the override review, the requester's view and the auditor's evidence view
   are all this one component with different footers.
2. **One pipeline strip is the shared map** of the lifecycle. On every request page, a segment
   filters to that step. Each role's default is the step they act on.
3. **"Waiting on you" is one inbox concept.** The T1 Needs-attention group, the Requests page's
   top section, and the notification bell all read the same data, filtered by role.
4. **Navigation (proposal for the product owner):** Operations currently lists Vehicle Request,
   Vehicle Allocation, Dispatch Management and Journey Management as four separate nav items. They
   are four *stages of one object*. Candidate: one "Requests & trips" item whose stage strip is
   the sub-navigation, with role-based default stage. That makes 4 nav items into 1.
   "Operations" was already flagged as a pillar the PO never confirmed (`09` §1).
5. **Related objects link both ways:**
   - The vehicle detail shows its current and next trips, open job cards and documents.
   - The request detail links to its vehicle, driver and any blocking job card.
   - "KBZ 442A grounded → blocks REQ-2024-0851" is one link, visible from both sides.

### 10d. Order of work this implies

1. **Confirm the lifecycle × role table (10b)** with the product owner; the "?" cells and the
   step split are the priority. This is the foundation for every request page.
2. **Build the Request detail as one component** with its role-aware footer.
3. **Re-derive request pages from 10c:** Requester home, Approval queue, Dispatch queue, Vehicle
   requests (oversight). Most of the §10c prompt survives; "Waiting on you" sizing follows 10b.
4. **Repeat 10a–10c for the next objects:** Vehicle (Available → Allocated → On trip →
   Workshop → Grounded → Disposal), then Job card, then Fuel transaction.

---

## 11. Decisions taken on user-first grounds (2026-09-25)

User direction: *"go with what we believe is best for the user."* The open questions in §8 and the
"?" cells in §10b are decided below, each with its reasoning. They're marked **validate with the
product owner when available**, not blocking.

| # | Decision | Why it's best for the user |
|---|---|---|
| D1 | **Gate: only Fail blocks.** A Warning is shown and logged; dispatch proceeds. **Exception:** a document that expires *before the trip's expected return* is a **Fail**, not a Warning | Daniel isn't forced into an override for every expiring document, so overrides stay meaningful. Safety holds: nothing drives on a document that lapses mid-trip |
| D2 | **Transport Ops can "Return to requester" (reason required), not "Reject".** Only approvers reject | Keeps approval authority where the SRS puts it; Mary gets a fixable request back instead of a dead end |
| D3 | **One insurance check, 3 states** (Valid / Expiring / Expired); the same rule for inspection and licence | One fact, one row; no contradictions like PASS + WARNING on the same policy |
| D4 | **Executive lands on the T1 Role Home skeleton,** with KPI-against-target in the band and cards | One mental model across all roles; Sarah still gets targets, and drill-downs go to analytics (T5) |
| D5 | **Two allocation steps: "Needs vehicle" → "Needs driver"** (as in the live app) | Matches how Daniel actually works, and shows *which* resource is the bottleneck |
| D6 | **The Fleet Manager reallocates by escalation, not routinely.** Daniel does routine allocation. A request escalates to Grace when it's stuck > 1 day in Needs vehicle/driver or needs a vehicle from another station/pool. Grounded in `01` §1: Grace holds allocation authority (SRS §5.3) | Grace acts where only she can (cross-station, cross-pool); Daniel keeps his throughput; nothing waits silently |
| D7 | **Grace's "Waiting on you" = overrides + transfers + escalated allocations.** Never routine queue items | Her inbox stays short and every item truly needs her |
| D8 | **Navigation:** Operations becomes **Fleet overview · Requests & trips · Live map**. "Requests & trips" replaces Vehicle Request, Vehicle Allocation, Dispatch Management and Journey Management; the 7-stage strip is its sub-navigation (Awaiting approval → Transport review → Needs vehicle → Needs driver → Ready → Awaiting driver → On trip), with Closed/Returned under "More" | Four menu items were four stages of one object; one place, one ID, one story |
| D9 | **One page, layout set by role, no toggle** (revised 2026-09-25): Transport Ops and Approvers get the *queue* layout (list + docked detail); Fleet Manager, Executive and Auditor get the *table* layout (table + drawer). The "List \| Queue" toggle is removed | Nobody needs to switch; the labels were ambiguous; one less header control |
| D10 | **Request detail is one component** (drawer or pane) with a **role-aware footer**: requester = edit/cancel/resubmit; approver = approve/return/reject; Transport = dispatch/request override/return; Fleet Manager = approve/deny override, reallocate; auditor = none (export evidence) | Built once, consistent everywhere, and every role sees only what they can do |

**§10b updates:**
- The Fleet Manager's "?" cells in Needs vehicle / Needs driver become **"reallocate (escalated)"**.
- Fleet Ops at Needs vehicle becomes **"custody/transfer only"**.
- The Today pipeline gains "Needs vehicle" as its own stage.

### 11a. SRS check of D1–D10 (2026-09-25)

Checked against the SRS text: §4 roles, §5.3–5.6, §5.24, BR-001–010, §11, §26.

| Decision | SRS says | Verdict |
|---|---|---|
| D1 Only Fail blocks | §5.6 "Prevent dispatch where mandatory conditions are not met, subject to authorized override"; BR-001 blocks when insurance "is **expired**" | **Confirmed.** "Expiring soon" isn't a failed condition. The "expires before return = Fail" extension is our policy suggestion (SRS silent); flag it to the PO |
| D2 Return, not reject | §5.24 supports "rejection, return for correction" but doesn't say who | **Plausible.** Keep, validate |
| D3 One check, 3 states | Not addressed | Design choice; keep |
| D5 Needs vehicle → Needs driver | §5.4 workflow: "Request → Supervisor Approval → Transport Review → **Vehicle Allocation → Driver Assignment** → Dispatch" | **Confirmed** |
| D6 Grace reallocates vehicles to requests | §4: **Transport Officer = "Requests, allocation and dispatch"**; Fleet Manager = "Overall fleet management". **§5.3 "Vehicle Allocation" means assigning vehicles to departments, stations, projects and custodians** (with custodian and expected return date), a *different* allocation from the request step. §26 puts Allocation *before* Vehicle Request | **Corrected, see below** |
| D8 Merge 4 nav items | "Vehicle Allocation" (§5.3) is its own object (pool/custody assignment), not a request stage | **Corrected:** merge only Vehicle Request + Dispatch + Journey |
| D9, D10 | Not addressed; the access model in §4 ("role, department, directorate, vehicle pool, location/station… approval authority") supports role-aware views and the station scope | Keep |

**Corrections:**
1. **Two different "allocations":**
   - *Request allocation* (§5.4 step: this vehicle for this trip) belongs to the **Transport
     Officer**.
   - *Pool allocation* (§5.3: which department/station/custodian holds which vehicle) is fleet
     administration, and that's **Grace's lever**. When Molo can't meet demand, she moves a vehicle
     into Molo's pool; Daniel then assigns it to the request.
   - **D6 (revised):** escalations reach Grace as **"Station short of vehicles/drivers"** with the
     action "Move a vehicle to Molo" (a §5.3 allocation change), never as "assign this vehicle
     to this request".
   - In the override drawer, the alternative becomes **"Deny and suggest KCE 558A"** (Daniel
     assigns it), not "Reallocate instead".
2. **D8 (revised) Operations nav:** Fleet overview · **Requests & trips** (Vehicle Request +
   Dispatch Management + Journey Management) · **Vehicle allocation** (§5.3: pool/custody
   assignments; a T3 registry).
3. **Checks happen at different steps:**
   - BR-002 and BR-003 say a driver "shall not be **assigned**" if inactive or unlicensed. They're
     **assignment-time rules**: the system prevents the assignment instead of showing FAIL later.
   - Vehicle and document checks (BR-001, BR-004, §5.6) apply at **dispatch**.
   - So before a step is reached, its checks show "Not yet assigned"; they never show FAIL (fixes
     the live-app bug in doc 12 §10).
4. **⚠ Lifecycle order conflict (affects the mobile chat).** §5.6 requires verifying "tyres,
   lights, brakes, safety equipment, fuel level, odometer" **before dispatch**. Our lifecycle (§6a)
   and `02` §3 put the driver's pre-trip inspection **after** dispatch. The SRS order implies:
   - Driver assigned → driver accepts and does the pre-trip inspection (mobile FRAME 7B) →
     **Ready** (all checks including inspection) → **Dispatch** → driver starts the trip.

   Needs alignment with the mobile flow before either side locks the stepper.

---

## 12. Page count and build waves (2026-09-25, reflects §11 decisions)

**Unique desktop page designs: 18**, built from **9 templates**. Role variants of the same page
(e.g. Today for 6 roles) don't count as extra designs; they're content swaps in the same frame.

| # | Page | Template | Role variants | Status | Wave |
|---|---|---|---|---|---|
| 1 | **Today** (role home) | T1 | Fleet Mgr, Transport, Approver, Fleet Ops, Auditor, Executive (D4) | FM near-locked | **A** |
| 2 | **Requests & trips** | T3 List / T2 Queue | FM & Exec (List), Transport & Approver (Queue), Requester ("My requests") | FM v1 built, v2 prompt ready | **A** |
| 3 | **Request detail** (drawer/pane) | T8/T7 | role-aware footer ×5 | prompt ready (in #2) | **A** |
| 4 | **New request** form | T9 | Requester (+ anyone) | not started | **A** |
| 5 | **Live map** | T6 | FM, Transport | v1 built (unchecked) | **A** |
| 6 | **Audit trail** + evidence view | T3 + T7 | Auditor | specced (FRAME-09) | **A** |
| 7 | Fleet registry (All vehicles) | T3 | FM, Fleet Ops | v1 built | B |
| 8 | **Vehicle detail** | T7 | all | missing | B |
| 9 | Vehicle allocation (pool/custody, §5.3) | T3 + T8 | FM, Fleet Ops | missing | B |
| 10 | Compliance (documents & expiries) | T3 + T8 renew drawer | FM, Fleet Ops | missing | B |
| 11 | Alerts & GPS events (live alerts queue + events register as tabs) | T2 | FM, Transport | missing | B |
| 12 | Driver management (+ Behaviour tab) | T3 | FM, HR | v1 built (loosest) | B |
| 13 | Workshop board + job card | T4 + T7 | Workshop Mgr | v1 built | B |
| 14 | Fuel management (log + anomalies tabs) | T3 / T2 | FM, Fuel Officer, Finance | missing (Finance anomaly review exists) | B |
| 15 | Finance overview | T5 | Finance | v1 built | C |
| 16 | Executive analytics / reports | T5 | Executive | v1 built (FRAME-04) | C |
| 17 | Driver detail | T7 | FM, HR | missing | C |
| 18 | Administration (users, roles, workflows) | T3 + T9 | Admin | missing | C |

**Wave A: 6 pages, the 6-stage demo spine.** Requester creates (4) → Approver approves (1, 2, 3)
→ Transport dispatches (2 Queue, 3) → Driver (mobile chat) → Fleet Manager monitors (1, 5) →
Auditor reviews (6).

**Wave B: 8 pages,** completing the Fleet Manager's and Fleet Ops' daily work, and every
destination Today links to.

**Wave C: 4 pages,** analytics and admin.

**Merges that kept the count down:**
- Vehicle Request + Dispatch + Journey → one page (#2).
- Override review → the request-detail footer (#3).
- Live alerts queue + GPS events register → one page with tabs (#11).
- Fuel log + anomaly review → one page with tabs (#14).
- Six role homes → one T1 (#1).

**Not counted:** the driver mobile screens (other chat) and small drawers (renew insurance, trip
trace, move vehicle), which are T8 instances.

**D11 (2026-09-25, from §11a finding 4): lifecycle order follows the SRS.**
- Stages: Awaiting approval → Transport review → Needs vehicle → Needs driver → **Driver
  check-in** (driver accepts + pre-trip inspection on mobile) → **Ready** (all dispatch checks
  pass, including the inspection) → **On trip** (dispatch = trip starts) → Closed.
- "Awaiting driver" is renamed "Driver check-in" and moves before Ready.
- **Tell the mobile chat.** Their flow currently has inspection after dispatch; FRAME 7B's
  checklist becomes the "Driver check-in" step.
