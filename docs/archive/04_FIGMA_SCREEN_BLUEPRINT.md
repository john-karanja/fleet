# CVFMS: Figma Screen Blueprint & Frame Directory

**Document ID:** `DOC-CVFMS-004`
**Version:** 1.0.0 (Generation-Ready Standard)
**Depends on:** `01_USER_PERSONAS.md`, `02_USER_FLOWS.md`, `03_MASTER_DESIGN_SYSTEM.md`
**Purpose:** This is the doc `figma-generate-design` / `use_figma` should be pointed at. It enumerates exact frames, dimensions, and per-component specs so generation doesn't drift from the token system.

---

## 1. Master Frame Directory (Desktop, 1440 × 1024px)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              CVFMS DESKTOP FRAME DIRECTORY (Wave 1)                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. [FRAME-01] Fleet Command Dashboard (Grace — Fleet Manager)  ◄── FLAGSHIP SCREEN (see §2A v2.3) │
│    • FINAL 5-component list (closed Round 15/16, do not add/remove without updating §2A first):    │
│      KPI row (plain, no chart) → [Needs Attention ~60-65% width + Coming Up ~35-40% width] side by │
│      side → Fleet Map (bounded preview, full width, own row) → Recent Activity. NO Vehicle Status  │
│      Board panel, NO standalone Utilization Gap/Critical Mismatch card.                            │
│                                                                                                      │
│ 2. [FRAME-02] Dispatch & Requisition Queue (Daniel — Transport Officer)                            │
│    • Left: Requisition Queue List (status: Pending Approval / Approved / Ready to Dispatch)        │
│    • Right: Dispatch Gate Checklist Panel (BR-001–BR-005 pass/fail) + Authorize/Override           │
│                                                                                                      │
│ 3. [FRAME-03] Workshop Job Card Board (Peter — Workshop Manager)                                   │
│    • 5-column Kanban: Diagnosis / In Repair / Awaiting Parts / QA / Ready for Release              │
│    • Job Card Detail Drawer (parts requested + stock status, QA checklist, release button)         │
│                                                                                                      │
│ 4. [FRAME-04] Executive Briefing Dashboard (Sarah — County Executive)                              │
│    • Large KPI tiles: Availability %, Total Expenditure vs Budget, Utilization, Accident Summary   │
│    • Trend sparkline per tile + single-level drill-down (department breakdown)                     │
│    • Read-only — no primary action buttons on this screen                                          │
│                                                                                                      │
│ 5. [FRAME-05] Finance & Cost Dashboard (Miriam — Finance Officer)                                  │
│    • Budget vs. Actual bars by department/cost-center                                              │
│    • Fuel/Maintenance Anomaly Review Queue (flagged transactions, clear/escalate actions)          │
│    • Export controls (PDF / Excel / CSV) gated by role permission                                  │
│                                                                                                      │
│ 6. [FRAME-06] Live Fleet Map (Grace — Fleet Manager, in-page tab of "Fleet")  ◄── ADDED v1.5        │
│    • Full-bleed GIS map, real-time vehicle position markers (SRS 5.16 GPS & Telematics)             │
│    • Geofence overlays, speed-violation/after-hours alert pins                                      │
│    • Reached via [Overview] [Live Map] tabs at the top of the Fleet page — NOT a home-screen widget │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Shared shell (top nav + left rail, per `03_MASTER_DESIGN_SYSTEM.md` Component 1) wraps all 6 frames — build it once as a reusable Figma component, not per-frame.

**Note on FRAME-06 sequencing:** the SRS tiers GPS/Telematics as Phase 5 (Digital Intelligence) — after Foundation, Operations, Cost Management, and Compliance & Risk are built. Design-wise it's included here as a documented destination (so Grace's navigation structure is decided now, not bolted on later), but it should be the last of the 6 frames actually generated, after FRAME-02 through FRAME-05.

---

## 2. FRAME-01 Detail: Fleet Command Dashboard (build this one first)

## 2A. CURRENT AUTHORITATIVE SPEC — Version 2.3 — FINAL COMPONENT LIST (read this section; everything below is version history)

**Change from v2.2 — Round 16: Needs Attention narrowed, paired with Coming Up.** User flagged that a full-width Needs Attention card was wasteful — on a typical day it holds only 2-4 short rows (a tag, one line, a button), and stretching that content across the full ~1160px content width either left dead space or forced an uncomfortably large gap between each row's description and its action button. Full-width had been a proxy for "dominance" (Round 9), but dominance comes from elevation, position, and being the first thing on the page — not specifically from occupying the entire row. **Fix:** Needs Attention narrows to ~60-65% of the content width; Coming Up moves up from its previous position (below Fleet Map) to fill the remaining ~35-40% beside it. This pairing was chosen deliberately, not arbitrarily: both are list/urgency-shaped content, and seeing "what's urgent now" beside "what's coming later" is a genuinely useful comparison for Grace — not filler, and not a repeat of content already shown elsewhere (checked against the same redundancy test that removed Critical Mismatch and merged Compliance Countdown; Coming Up's content is disjoint from Needs Attention's, just related in shape/purpose). Needs Attention remains visually dominant via its elevation and top position, not its width.

**Updated final component list, v2.3:** KPI row (4 plain cards, full width) → [Needs Attention (~60-65% width) + Coming Up (~35-40% width)] side by side → Fleet Map (bounded preview, full width, own row) → Recent Activity Feed (full width, lowest priority). Five components total, same set as v2.2 — this round changed sizing/pairing, not the component list itself. As with Round 15: any future change to this arrangement must be written here first, not discovered after a build.

**Current top-to-bottom layout (v2.3, supersedes the v2.2 diagram below):**

```
Top Nav (56px) + Left Rail (240px, dark #0F172A)
Page Title: "Fleet Command Dashboard"
[ Overview ] [ Live Map ]  ← tabs, Overview active

KPI ROW — 4 tiles, plain, no sparkline: Fleet Size 247, Availability 89%, Grounded 6, Alerts Due 14.

HERO ROW — two panels side by side:
  LEFT (~60-65% width): NEEDS ATTENTION — dominant via elevation/position, NOT via full width.
        Tightened scope: Overdue + This Week only (2-4 rows typical day). Row treatment per
        Component 3C v1.9 (plain rows, colored dot, section headers, dismiss icon). Header:
        "View all compliance →" link. UTILIZATION row(s): "View allocation table →" link to
        Component 3G.
  RIGHT (~35-40% width): COMING UP — date-grouped, calm, no urgency color-coding, per Component 3F.
        Paired here deliberately (Round 16) — both list/urgency-shaped, useful side-by-side
        comparison of "urgent now" vs. "coming later," not redundant with each other's content.

FLEET MAP — full width, own row, bounded/card-contained treatment per Component 3E (map area +
  adjacent status/count list), "Full map →" and "All Vehicles →" links.

RECENT ACTIVITY FEED — full width, lowest visual priority, 5 rows.
```

[No standalone Utilization Gap / Critical Mismatch card — removed Round 14. No standalone Vehicle Status Board panel — removed Round 15. No full-width Needs Attention — narrowed and paired with Coming Up, Round 16. None of these should be re-added or re-widened without updating this section first.]

---

## 2A-prior. Version 2.2 — FINAL COMPONENT LIST (superseded by v2.3 above — kept for the Round 15 reasoning, which still applies)

**CLOSED DECISION, Round 15 — Vehicle Status Board is REMOVED from FRAME-01 Overview, permanently, not by accident.** A build correctly implemented v2.1 but Fleet Map ended up occupying the secondary row alone, with Vehicle Status Board simply absent — nobody had deliberately decided this, it just happened, which the user rightly called out as "going round in circles, removing and adding the same things." This entry exists to stop that pattern: **the reasoning is now final and written down once.** Vehicle Status Board's justification (Round 9) was being Needs Attention's "companion, same subject two views." That's no longer true: Fleet Map already shows per-status vehicle counts (Available/On Trip/Grounded/Maintenance) beside a spatial view, and Needs Attention already surfaces the specific vehicles needing action. A condensed 3-4 row Vehicle Status Board would show arbitrary additional vehicles with no specific reason to be those ones — weaker justification than either component already on the page. Fleet Map's "All Vehicles →" link is the sufficient path to the full table. **Do not re-add Vehicle Status Board to Overview without a new, specific justification distinct from what's already reasoned here — and if it comes up again, update this section directly instead of silently changing the layout.**

**The full, final Overview component list as of v2.2 (nothing else, nothing missing):** KPI row (4 plain cards) → Needs Attention (hero, full width) → Fleet Map (bounded preview, full width on its own — not paired with anything) → Coming Up + Recent Activity. Five components total. Any future addition or removal must be written into this section before it's built, not discovered afterward.

**Change from v2.0 — Round 14: Critical Mismatch (Utilization Gap) removed as a standalone card.** Its content duplicated Needs Attention's own "UTILIZATION" row at a different level of detail — the same redundancy pattern already fixed once (Round 8, Compliance Countdown merge). Its full-detail content (idle vehicles matched against pending requests) becomes a linked table destination (Component 3G, Vehicle Allocation Table) reached via a link from Needs Attention's UTILIZATION row, not a permanent Overview card. See `03_MASTER_DESIGN_SYSTEM.md` Component 3D's removal note for the full reasoning and references. Also reverted the KPI sparkline addition from Round 11 (see Component 3's Round 14 note) — 3-of-4 cards having one and one not created a ragged, unbalanced row; rather than force artificial consistency, no KPI cards carry a sparkline as of this version.

**Change from v1.9 — page reprioritized around a single question: what does Grace actually need to see to act?** After several rounds of styling refinement to Needs Attention (tinted rows → type hierarchy → plain rows/dots), the user asked the more fundamental question directly: what exactly is most important for Grace to see on this page so she can act? Answered from first principles against her Core Goal and Pain Points (`01_USER_PERSONAS.md`), not from what had already been built:

Her two jobs are **know the state of the fleet** and **act before small problems become expensive/dangerous**. The second job dominates — knowing without acting achieves nothing, per her own stated pain point ("finds out about lapsed insurance only when a vehicle is already stopped at a roadblock"). This means the single most important thing on the page is a **short, genuinely urgent problem list** — not a comprehensive one. The v1.8/v1.9 Needs Attention list (7-8 items spanning "overdue" through "due in 22 days") diluted this by including items that aren't actually urgent yet, competing for attention with the 2-4 items that are.

**Three changes from this reprioritization:**

1. **Needs Attention is tightened to only genuinely urgent items** — Overdue + This Week only, realistically 2-4 rows on a normal day, no "This Month" section on the hero anymore. Every row on this list should be something Grace could plausibly act on today; if it isn't, it doesn't belong here.
2. **Deprioritized items move to the Compliance nav destination**, not off a cliff. A "View all compliance →" link in the Needs Attention header leads to the "Compliance" sidebar item (previously an empty destination with no screen behind it — this finally gives it a real purpose: the fuller list of all compliance items regardless of urgency, including the "due in 22 days" items that don't belong on the hero).
3. **Vehicle Status Board and Fleet Pulse are demoted from "always visible on login" to "reachable when needed."** Both are legitimate tools (a searchable inventory, a spatial view) but neither is a *fact Grace needs surfaced unprompted* — she doesn't need the full 247-vehicle table or a map preview every time she opens the dashboard, she needs them when she's specifically looking something up. They move out of the primary hero row and become secondary/lower on the page, sized smaller, so the tightened Needs Attention list is unambiguously the dominant element with nothing else competing for "what should I look at first."

Top-to-bottom layout:

```
Top Nav (56px) + Left Rail (240px, dark #0F172A, now including a real "Compliance" destination)
Page Title: "Fleet Command Dashboard"
[ Overview ] [ Live Map ]  ← tabs, Overview active

KPI ROW — 4 tiles, plain, no sparkline (reverted Round 14 after a 3-of-4 sparkline row rendered
  unbalanced — see Component 3): Fleet Size 247, Availability 89%, Grounded 6, Alerts Due 14.

NEEDS ATTENTION — full width, THE dominant element on the page, nothing else competes with it in
  size or visual weight. Tightened scope: Overdue + This Week sections only (2-4 rows typical day).
  Row treatment per Component 3C v1.9 (plain rows, colored dot, section headers, dismiss icon).
  Header includes a "View all compliance →" link to the Compliance nav destination for deprioritized
  compliance items. Its UTILIZATION row(s) include a "View allocation table →" link to Component 3G
  (Vehicle Allocation Table) for the full idle-vehicle/pending-request detail — added Round 14,
  replacing the standalone Utilization Gap card.

FLEET MAP — full width on its own row (NOT paired with Vehicle Status Board — see Round 15 closed
  decision above for why that pairing was permanently dropped), clearly subordinate in size/weight
  to Needs Attention above. Bounded/card-contained treatment per Component 3E v1.9 (Round 13): map
  area (~60-65% width) + adjacent status/count list (~35-40% width), "Full map →" and "All Vehicles →"
  links in the footer — the latter is Overview's only path to the full vehicle table, replacing the
  condensed Vehicle Status Board panel.

[No standalone Utilization Gap / Critical Mismatch card — removed Round 14. No standalone Vehicle
 Status Board panel — removed Round 15. Neither should be re-added without updating the Round 14/15
 decisions above first, not by silently changing the layout.]

Recent Activity Feed — full-width, lowest visual priority, 5 rows.
```

**Page-level visual requirements (unchanged):** page canvas visibly `#F8FAFC`, cards `#FFFFFF` with both border and Level 1 shadow. Color reserved for status/severity signals only.

Component specs: Needs Attention = Component 3C (v1.9 row treatment + v2.0 tightened scope + Round 14 utilization-link addition), KPI Tile = Component 3 (no sparkline), Fleet Map = Component 3E, Vehicle Allocation Table = Component 3G — all in `03_MASTER_DESIGN_SYSTEM.md`.

---

## 2B. Version History (older, superseded — kept for traceability, do not build from these)

**Version 1.6 — correction: the v1.4 hero chart was decorative, not actionable.** User's standing instruction is that every element must be useful/actionable data, expertly designed — not just a component that resembles what a polished reference dashboard has. Audited v1.4/v1.5 against that bar directly and the Fleet Availability Trend hero chart failed it: it was added because Shopify/GA4 have a hero trend chart, not because anything in Grace's documented goals or pain points (`01_USER_PERSONAS.md`) asks a historical-trend question. Her stated need is point-in-time ("know the real-time state... at a glance") and forward-looking ("intervene before it becomes a failure") — a 30-day line chart of a slowly-moving percentage doesn't change what she does today. Same critique applies, to a lesser extent, to the KPI sparklines added in v1.4 Change 2 (kept — see below — but demoted in importance).

**Fix — replace the hero chart with a "Needs Attention" ranked action list.** Instead of a chart, the hero slot is now a synthesized, priority-ordered list that pulls the single most urgent item from each of the dashboard's other data sources into one place: a grounded vehicle with the most severe reason, the most overdue compliance item, and the request/idle-vehicle mismatch with the most idle days — each shown as one row with a severity indicator, a one-line reason, and a direct action button, ranked most-urgent first. This is the correct hero because it is literally the synthesis of everything else on the page into "here is what to do right now," which is a closer match to her Success Looks Like criterion ("every finding has a direct path to the action... without leaving her own workspace") than a chart of any kind. Vehicle Status Board remains this hero's companion/detail panel beside it, since "here's what's urgent" and "here's the full status list it was drawn from" are still the same subject at two zoom levels — that part of the v1.4 pairing logic was correct and is kept.

**KPI sparklines — kept but demoted in rationale.** Not removed, since a sparkline costs little space and a sharply worsening shape (e.g. Grounded count climbing steadily) is a legitimate early-warning signal even if the current single number is still low. But they are explicitly secondary, ambient context — not a claim that they are, by themselves, the reason this dashboard is well designed. Do not add further chart/sparkline elements to this page without first naming the specific decision they'd change, per the standing "useful and actionable, not just nice-looking" instruction — this is now a required test for any future addition to this frame.

---

**Version 1.4 — hierarchy restructure (ui-ux-pro-max + user reference screens: Shopify Analytics, GA4, Grok usage dashboard).** User correctly identified that despite v1.1-1.3 fixing individual components, the overall information *hierarchy* was still flat — every panel (composition bar, status table, compliance panel) carried roughly equal visual weight, so nothing told Grace where to look first. Real dashboards in this class (Shopify Analytics, Google Analytics 4) share one structural trait ours lacked: **one dominant hero trend chart**, with everything else positioned as smaller, clearly secondary detail around it — never a wall of equal-weight panels.

**Change 1 — Fleet Availability Trend replaces the Fleet Composition Bar as the dashboard's hero visual.** The flat composition bar answered "what's the fleet's state right now" but gave no sense of *trend* — is availability improving or declining — which is the more actionable question for a manager who checks this daily. New hero element: a large line/area chart (per the `ui-ux-pro-max` chart-domain recommendation for "Trend Over Time" data — Line Chart, area fill at ~20% opacity, civic green) plotting Fleet Availability % over the last 30 days, positioned directly below the KPI row at roughly 2x the vertical height of any other panel on the page — matching Shopify's "Total sales over time" and GA4's "Active users" trend chart, both of which anchor their dashboards this way. The Vehicle Status Board becomes this chart's companion breakdown, positioned immediately beside/below it (same subject — fleet status — two views: trend and detail), not paired arbitrarily with the unrelated Compliance Countdown panel as in v1.1-1.3.

**Change 2 — KPI tiles gain embedded sparklines, replacing the bare trend-delta caption.** Per the chart-domain guidance ("Trend Over Time" data belongs in a Line Chart even in compact/KPI contexts — a sparkline is the compact form), each of the 4 KPI tiles (Fleet Size, Availability, Grounded, Alerts Due) now shows a small inline sparkline (last 7-14 data points, no axis labels, ~40px wide x 20px tall) beside or below the hero number, replacing the plain text-only trend caption ("+3 vs last month"). This matches Shopify's KPI cards, which all carry an embedded mini-chart rather than a caption alone.

**Change 3 — fix the composition bar's color-only violation, and demote it to a smaller supporting element.** The `ui-ux-pro-max` UX-domain search flagged our composition bar directly: "Don't convey information by color alone... Red/green only for error/success" is a High severity issue, and the bar had no in-context labels, only a separate legend row. Since it's no longer the hero, it survives as a smaller supporting strip (not removed — it still answers "current state" at a glance, which the trend chart doesn't) but must now show each segment's count directly on or immediately touching its segment (not only in a detached legend), and should be visually subordinate in size/position to the new hero trend chart.

**Resulting top-to-bottom order:** KPI row (with sparklines) → Fleet Availability Trend (hero chart) + Vehicle Status Board (companion breakdown, side by side or stacked depending on space) → Fleet Composition Bar (now a smaller supporting strip, labeled) → Compliance Countdown + Utilization Gap → Recent Activity Feed. This is a reordering and re-weighting of existing elements, not new content — every component from v1.1-1.3 (grounded-reason text, urgency-grouped compliance, concrete gap preview, row actions, filter chips, dark rail, thumbnails) remains and is unaffected by this hierarchy change.

---

**Version 1.3 — information architecture revision.** Before continuing any visual polish pass, Grace's stated goal (`01_USER_PERSONAS.md` Core Goal & Mental Model, Pain Points, Success Looks Like) was re-decomposed to check whether the *information* on the dashboard actually serves it, independent of how it looks. Three gaps found and fixed here; visual craft (icons, shadows, imagery) remains a separate, still-open pass — closing an information gap and improving visual polish are not substitutes for each other, both are needed.

**Gap 1 — "grounded... and why" was never answered.** Grace's core goal explicitly says she needs to know what's grounded *and why*, but the Vehicle Status Board only ever showed the status pill with no reason. **Data model correction required:** `CVFMS_Architecture_and_Implementation_Summary.md` §5 documents `VEHICLE.status` as an enum (`ACTIVE, ON_TRIP, MAINTENANCE, GROUNDED, DISPOSED`) with no reason field — this doc's ERD should be treated as needing a `status_reason` (string) or `grounded_reason_code` (enum: FAILED_INSPECTION, ACCIDENT, AWAITING_PARTS, INSURANCE_LAPSED, OTHER) field added before engineering picks this up; flagging here as a design-driven schema requirement, not fixing the architecture doc itself in this pass. **Screen fix:** the Vehicle Status Board's Status column shows the reason as small secondary text directly under the pill for any non-Available/On-Trip state (e.g. pill "GROUNDED" with "Failed NTSA inspection" in 12px gray beneath it) — this is a two-line cell for flagged rows only, not a full extra table column, keeping density intact for the common case.

**Gap 2 — Compliance Countdown had no urgency ranking, only color.** All 4 rows read as equally weighted except pill color; her pain point ("finds out too late") is about timing, not just category. **Fix:** the panel is restructured into two visually distinct groups, not one flat list — an "Overdue / Due within 7 days" group at the top (red pills, slightly bolder card treatment) and a "Due within 30 days" group below (amber pills, standard treatment), with a small group-divider label between them. This makes "needs action today" structurally separate from "worth knowing," not just a different color in an undifferentiated list.

**Gap 3 — the Utilization Gap Banner stated a mismatch but showed no data.** "6 vehicles idle 3+ days while 4 requests are pending allocation" is a sentence Grace can't act on without a blind click-through, contradicting her Success Looks Like criterion ("direct path to the action... without leaving her own workspace"). **Fix:** the banner expands into a compact two-column preview *inside itself* (still one card, not a new full panel) — left side lists up to 3 idle vehicle regs, right side lists up to 3 pending request summaries (department + purpose), with the "Review pending requests →" link remaining as the path to the full reallocation flow (Frame per `02_USER_FLOWS.md` §2, path B) for anything beyond the 3-item preview.

---

**Version 1.1 — revised after Mobbin benchmark review** (Deel Assets, Employment Hero Asset Register, GoDaddy renewals panel). v1.0 was monitor-only, consistent with the now-corrected error described in `01_USER_PERSONAS.md` (Grace was wrongly scoped as having no actions of her own) and left the bottom third of the 1024px frame empty. v1.1 fixes both.

**Layout Archetype:** A (Command Dashboard)

```
┌─ Top Nav (56px) ─────────────────────────────────────────────────────────────┐
├─ Left Rail (240px) ─┬──────────────────────────────────────────────────────────┤
│                      │  Page Title: "Fleet Command Dashboard"        [Filters ▾]│
│                      │  ┌────────┬────────┬────────┬────────┐                 │
│                      │  │ 247    │ 89%    │ 6      │ 14     │  ◄── KPI row    │
│                      │  │ Fleet  │ Avail. │Grounded│ Alerts │      (4 tiles)  │
│                      │  │ Size   │        │        │ Due    │                 │
│                      │  └────────┴────────┴────────┴────────┘                 │
│                      │  ┌───────────────────────────────────────────────────┐│
│                      │  │ Fleet Composition Bar (NEW, per Deel Assets)      ││
│                      │  │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▓                       ││
│                      │  │ ● Available 178  ● On Trip 41  ● Grounded 6  ● Maint 22 │
│                      │  └───────────────────────────────────────────────────┘│
│                      │  ┌───────────────────────────┬────────────────────────┐│
│                      │  │ Vehicle Status Board       │ Compliance Countdown  ││
│                      │  │ (table, sortable/filterable│ header row now has    ││
│                      │  │  by dept/station/status)   │ "Review All →" link   ││
│                      │  │  Reg | Dept | Status |     │ (NEW, per GoDaddy)    ││
│                      │  │  Odometer | Last Service |  │ list sorted by       ││
│                      │  │  Actions ◄── NEW column,   │ days-remaining,       ││
│                      │  │  "•••" per row (per         │ color-coded 30/14/7  ││
│                      │  │  Employment Hero) opening    │                       ││
│                      │  │  Edit / Reallocate / Override│                      ││
│                      │  └───────────────────────────┴────────────────────────┘│
│                      │  ┌───────────────────────────────────────────────────┐│
│                      │  │ Utilization Gap Alert Banner                       ││
│                      │  │ "6 vehicles idle 3+ days while 4 requests pending" ││
│                      │  │ [Review Pending Requests →]                        ││
│                      │  └───────────────────────────────────────────────────┘│
│                      │  ┌───────────────────────────────────────────────────┐│
│                      │  │ Recent Activity Feed (NEW — fills empty space,     ││
│                      │  │ shows the last 5 audit-logged actions: overrides,  ││
│                      │  │ reallocations, registry edits, maintenance approvals)││
│                      │  │ each row: timestamp, actor, action, vehicle reg    ││
│                      │  └───────────────────────────────────────────────────┘│
└──────────────────────┴──────────────────────────────────────────────────────┘
```

**Component call-outs:**
* KPI row uses Component 3 (KPI Tile) — exactly 4 tiles, each with a one-word eyebrow, the number as hero value, and a trend delta.
* **Fleet Composition Bar (new):** a single horizontal stacked bar, full width, ~32px tall, segments proportional to count in each status (Available = success green, On Trip = info blue, Grounded = critical red, Maintenance = amber), with a legend row below showing swatch + label + count per segment. This is the "at a glance" proportional view the KPI row alone can't give — directly serves Grace's stated goal of knowing fleet-wide state instantly.
* Vehicle Status Board uses Component 6 (Data Table) with Status Pill (Component 2) in the Status column — never a bare colored cell. **New vehicle-type thumbnail:** a 32×32px rounded-corner square icon (flat single-color vehicle-type silhouette — sedan/pickup/ambulance/grader — matching the icon library, not a photo) placed immediately left of the registration number in each row, mirroring the product-thumbnail slot used by Shopify/Square/Klaviyo catalog tables (see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` Round 3). This is a type icon, not a per-vehicle photo or a map marker — rejected the Uber/Grab/Lyft live-marker treatment and Turo's full listing-photo treatment as wrong shape for a dense 200+ row table. **New Actions column:** a "•••" icon button per row (32×32px hit area, right-aligned, last column) opening a menu with "Edit Record" / "Reallocate" / "Request Override" — these route to the three Grace action modals defined in `02_USER_FLOWS.md` §2. This closes the gap where the table was previously a dead end inconsistent with Grace's corrected persona.
* Compliance Countdown Panel: each row is a compact card, amber pill for 14–30 days, red pill for <14 days, per the design system's semantic color rule. **New:** panel header now includes a "Review All →" text link (12px semibold, civic green) to the right of the "Compliance Countdown" title, giving a bulk entry point per the GoDaddy renewals-panel pattern, instead of forcing one-at-a-time review.
* Utilization Gap banner uses Component 7-adjacent treatment: a single-row alert card with one primary text link action, not a button — this is a nudge, not a transaction.
* **Recent Activity Feed (new):** a full-width panel below the alert banner, same card styling as other panels (white surface, 1px border, 12px radius), listing the 5 most recent audit-logged actions system-wide (not just Grace's own) in a simple timestamp/actor/action/vehicle row format. Fills the previously-empty bottom third of the 1024px frame and gives Grace visibility into what Daniel/Peter/Miriam have been doing without leaving her dashboard.

**Page-level tab structure (added v1.5):** the entire FRAME-01 layout above lives under an "Overview" tab. Directly below the page title "Fleet Command Dashboard," add two in-page tabs: `[Overview]` (selected/active by default — this is everything described above) and `[Live Map]` (leads to FRAME-06). This keeps the aggregation dashboard and the spatial map view under one shared "Fleet" sidebar destination without merging their content — see `02_USER_FLOWS.md` §2 note on why a live map does not belong inside the Overview tab's own hierarchy.

---

## 2B. FRAME-06 Detail: Live Fleet Map (Grace's "Live Map" tab)

**Layout Archetype:** New — "Spatial Map Cockpit," adapted from el-nino's Archetype A (Spatial Cockpit) pattern (`docs/MASTER_DESIGN_SYSTEM.md` in the el-nino project), the only archetype in either project actually built for a full-bleed map canvas. CVFMS stays light-theme (no cockpit dark mode), but reuses the *structural* idea: map bleeds full width/height, controls float above it rather than living in a fixed sidebar-and-content layout.

**Note (Round 13):** this full-bleed treatment is exclusive to this frame. FRAME-01's Fleet Map preview (Component 3E) deliberately uses a *different*, card-contained treatment (bounded map + adjacent list, per Google Analytics/Chatbase) rather than a smaller version of this same full-bleed style — see Component 3E in `03_MASTER_DESIGN_SYSTEM.md` for why. Do not apply this frame's full-bleed pattern to the Overview tab's preview card.

```
┌─ Top Nav (56px) ───────────────────────────────────────────────────────────────┐
├─ Left Rail (240px) ─┬────────────────────────────────────────────────────────────┤
│                      │  Page Title: "Fleet Command Dashboard"                    │
│                      │  [ Overview ] [ Live Map ● active ]  ◄── same tabs as FRAME-01
│                      │  ┌─────────────────────────────────────────────────────┐│
│                      │  │  FULL-BLEED MAP CANVAS (fills remaining viewport)   ││
│                      │  │                                                       ││
│                      │  │   ┌──────────────────────────┐                       ││
│                      │  │   │ Floating filter bar        │ (top-left, over map)││
│                      │  │   │ [Department ▾] [Status ▾]  │                     ││
│                      │  │   └──────────────────────────┘                       ││
│                      │  │                                                       ││
│                      │  │        🟢 (vehicle marker, available)                ││
│                      │  │              🔵 (on trip)      🔴 (grounded)         ││
│                      │  │                                                       ││
│                      │  │   ┌─────────────────────────┐                        ││
│                      │  │   │ Selected Vehicle Card     │ (floats bottom-left  ││
│                      │  │   │ KCK 442E · Public Works   │  on marker click)    ││
│                      │  │   │ Status: On Trip           │                       ││
│                      │  │   │ Speed: 62 km/h            │                       ││
│                      │  │   │ Last ping: 12s ago         │                       ││
│                      │  │   └─────────────────────────┘                        ││
│                      │  │                                    ┌──────────────┐  ││
│                      │  │                                    │ Legend        │  ││
│                      │  │                                    │ (bottom-right)│  ││
│                      │  │                                    └──────────────┘  ││
│                      │  └─────────────────────────────────────────────────────┘│
└──────────────────────┴────────────────────────────────────────────────────────┘
```

**Component call-outs:**
* **Map canvas:** muted slate street vectors, light landmass, subtle water bodies — same restrained basemap treatment as el-nino's Component 2 (Tactical Map Canvas), minus the tactical/hazard-overlay elements that don't apply here (no flood zones, no green-corridor routing).
* **Vehicle markers:** small circular pins colored by status using the existing semantic tokens (success green = Available, info blue = On Trip, critical red = Grounded, warning amber = Maintenance) — same 4-state palette as the Fleet Composition Bar and Status Pill, so the color language is consistent between the Overview tab and the Live Map tab. Never a bare colored dot with no other differentiator — cluster count badges appear when markers overlap at a given zoom level (standard map-pin clustering, not a new pattern to invent).
* **Floating filter bar:** reuses the filter-chip component from `03_MASTER_DESIGN_SYSTEM.md` Component 6, but floats over the map canvas (white background, drop shadow, rounded corners) rather than sitting inline above a table.
* **Selected Vehicle Card:** appears when a marker is clicked — a small floating card (white, rounded, shadow) showing registration, department, status, current speed, and time since last GPS ping. Includes a "•••" action affordance consistent with the Vehicle Status Board rows, so the same Edit/Reallocate/Override actions are reachable from the map, not just the table.
* **Geofence overlays:** soft transparent polygon fills (using the amber/red semantic tokens at low opacity) for any active geofence violation, with a small label pill identifying the zone — direct application of SRS 5.16's "geofencing, after-hours movement alerts."
* **Legend:** bottom-right floating card listing the 4 marker colors and their meaning — required per the design system's "never color alone" rule, same as the Fleet Composition Bar fix in v1.4.

**Per the Finish Pass:** this is the one CVFMS screen where a full-bleed canvas is appropriate instead of the card-grid pattern used everywhere else — justified because the underlying data (vehicle position) is inherently spatial, unlike every other screen's tabular/aggregate data. Do not apply this full-bleed treatment to any other frame.

**Per the Finish Pass:** the only *primary filled buttons* on this screen live inside the row-action menu's destination modals, not on the dashboard canvas itself — the dashboard surface remains dominated by monitoring components (table, bar, feed) with text-link/icon-button affordances only, consistent with "one dominant primary action per view" since the dashboard's own dominant action is scanning, not transacting.

---

## 3. FRAME-02 Detail: Dispatch & Requisition Queue

**Layout Archetype:** B (Queue / Workflow)

```
┌─ Top Nav + Left Rail ──────────────────────────────────────────────────────────┐
│  Page Title: "Requisitions & Dispatch"                                          │
│  ┌───────────────────────────┬─────────────────────────────────────────────┐  │
│  │ Requisition Queue (list)   │  Dispatch Gate Checklist                    │  │
│  │ ○ REQ-0412  Health Dept    │  Vehicle: KCK 442E  •  Driver: J. Mutiso    │  │
│  │   Pending Approval         │  ┌────────────────────────────────────────┐│  │
│  │ ● REQ-0409  Public Works   │  │ ✓ Insurance valid (exp. 2027-01-15)    ││  │
│  │   Ready to Dispatch  ◄──── │  │ ✓ Driver active & employed              ││  │
│  │   (selected)               │  │ ✗ Driver licence — expired 2 days ago  ││  │
│  │ ○ REQ-0407  Agriculture     │  │ ✓ Vehicle not grounded                  ││  │
│  │   Approved                 │  │ ✓ Approved request linked               ││  │
│  │                             │  └────────────────────────────────────────┘│  │
│  │                             │  [Request Override]      [Authorize Dispatch]│ │
│  │                             │   (outline, enabled)      (primary, disabled)│ │
│  └───────────────────────────┴─────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Component call-outs:**
* Left queue list rows use Status Pill for queue state (Pending Approval / Approved / Ready to Dispatch), selected row gets civic-green left border per Component 6.
* Right panel is Component 4 (Dispatch Gate Checklist) exactly as specced — this is the single most important component in the whole system for fraud/audit prevention (SRS BR-001–BR-005), do not simplify it.
* When a gate fails, `[Authorize Dispatch]` is disabled (not hidden) so the officer can see what's blocking it; `[Request Override]` opens a modal with a mandatory justification textarea before enabling dispatch.
* Footer button order follows the proven pattern from [Airwallex's spend-request approval panel](https://mobbin.com/screens/defdb85a-2fa6-4d65-93f1-bdd3e991dbe5): outline secondary/destructive action immediately left of the primary filled action, both bottom-right of the panel — see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`.

---

## 4. FRAME-03 Detail: Workshop Job Card Board

**Layout Archetype:** C (Board / Table)

* Full-width 5-column kanban per Component 5. Sticky filter toolbar above (filter by station/vehicle type/mechanic).
* Each column header shows the column name plus a count badge (e.g. "In Repair · 4") — required on every column, not optional.
* Cards stay minimal: vehicle reg + defect summary (2-line clamp) + assigned mechanic avatar + exactly one status pill. Parts-request status and QA checklist detail live in the drawer only — never crowd the card face with both.
* Clicking a card opens a right-side drawer (Component per Master Design System modal/drawer radius `16px`) showing: defect description, linked parts requisitions with stock-status pills, labour log, and the QA checklist — release action is disabled until every QA checklist item is checked.
* Reference: [Plane Kanban Board](https://mobbin.com/screens/0a016723-4f5b-4f5b-a418-4c14b1aebef7) for column header format; see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`.

---

## 5. FRAME-04 Detail: Executive Briefing Dashboard

**Layout Archetype:** A (Command Dashboard), simplified

* 4 large KPI tiles (Component 3, larger variant — `min-width: 280px`): Fleet Availability %, Total Expenditure vs Budget, Utilization %, Accident Summary (count + estimated liability).
* Each tile: trend sparkline (12 months) + one-level drill-down (click reveals a breakdown by department in an inline expansion, not a new page — respects Sarah's low-frequency, meeting-context usage).
* No primary action buttons anywhere on this frame — it is intentionally read-only, reinforcing that this is a briefing view, not an operational tool.

---

## 6. FRAME-05 Detail: Finance & Cost Dashboard

**Layout Archetype:** B (Queue / Workflow)

* Top: Budget vs. Actual bars (Component 7) grouped by department, one row per department/cost-center.
* Below: Anomaly Review Queue — table (Component 6) of flagged fuel/maintenance transactions, each row showing anomaly type as a Status Pill (critical-red for duplicate/over-capacity, amber for consumption-outlier), with row actions `[Clear]` / `[Escalate]`.
* Export controls (`PDF`/`Excel`/`CSV`) as a button group in the toolbar, visible only to roles with export permission.

---

## 7. Generation Sequence

Build in this order so shared components exist before dependent frames need them:

1. Application shell (top nav + left rail) as a reusable component.
2. Shared components: Status Pill, KPI Tile, Data Table row, Status/Button states.
3. FRAME-01 (Fleet Command Dashboard) — flagship, validates the whole token system end-to-end.
4. FRAME-02 (Dispatch Queue) — introduces the Dispatch Gate Checklist component.
5. FRAME-03 (Workshop Board) — introduces the Kanban card component.
6. FRAME-04 (Executive Briefing) — reuses KPI Tile at larger scale, no new components.
7. FRAME-05 (Finance Dashboard) — introduces the Budget vs. Actual bar component.

After each frame, run the Finish Pass checklist from `03_MASTER_DESIGN_SYSTEM.md` before moving to the next.
