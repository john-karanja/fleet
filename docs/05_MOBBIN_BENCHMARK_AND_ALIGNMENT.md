# CVFMS: Mobbin Benchmark & Alignment

**Document ID:** `DOC-CVFMS-005`
**Revision:** 2.0 — full restart. Prior version (`docs/archive/05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`) organized findings as chronological "Rounds" tied to specific build iterations of the old FRAME-01. Since that build history no longer applies, this version organizes by **component**, per the practical-notes guidance the old handover itself arrived at ("Mobbin benchmarking should be per-component, not per-page... once the project matured past its first draft") — starting there directly instead of re-discovering it.
**Depends on:** `03_MASTER_DESIGN_SYSTEM.md`, `04_FIGMA_SCREEN_BLUEPRINT.md`.
**Purpose:** Real-world reference screens (via Mobbin) mapped to each CVFMS component, with concrete patterns to borrow or reject. Use `mcp__claude_ai_Mobbin__search_screens` / `search_flows` / `search_sections` when refining a specific component — search for the component's function ("approval drawer," "kanban job board," "budget variance bar"), not the whole page.

---

## 1. How to Use This Document

Per `06_DESIGN_QUALITY_PROCESS.md`'s mandatory pre-generation check: before writing the first Figma First Draft prompt for any frame, pull at least 3 reference screens for its dominant, novel component (not for generic nav/KPI-tile patterns already settled by the design system) and record the finding here — pattern to borrow, pattern to reject, and why — before generation starts, not after a bad render.

---

## 2. Component-by-Component Benchmark Targets

### Status Pill / State Indicator
**What to search:** approval status badges, shipment/order status chips in operations dashboards.
**What to borrow:** icon + text pairing inside the pill (never a bare color dot) — this is also a binding accessibility rule in the design system (§0/§A), so any reference that uses color-only status should be rejected outright regardless of how clean it looks.
**What to reject:** oversized pills that compete with row text for dominance — per the design system's row-hierarchy rule (§B2), the pill is never the dominant element in a row.

### Needs Attention / Action List (FRAME-01)
**What to search:** "approval queue," "action required" panels in enterprise ops tools (fintech back-office, logistics dispatch).
**What to borrow:** a tightly-scoped urgent-only list with a clear "see everything else" escape hatch (link to a fuller list) — this is the same pattern behind not dumping every compliance item onto the hero.
**What to reject:** dense multi-column tables disguised as an "attention" panel — if it needs column headers to be legible, it has become a data table, not an action list, and belongs in a linked destination (Component 6) instead.
**References pulled (2026-09-13, pre-generation check for FRAME-01):** [Wrike "Tasks assigned to me" panel](https://mobbin.com/screens/b453a329-6f1b-4745-ba03-5ce03c2c5307) — date-grouped (This week / Next week) collapsible sections with status pill + assignee per row, directly matching the Needs Attention / Coming Up date-grouped pattern. [ClickUp task list](https://mobbin.com/screens/27113b60-6baf-4b1e-bd2c-3deebad34c58) — status-grouped sections (Shipped/Review) with a colored pill leading each row and priority indicator trailing, confirms the "one dominant identifier + trailing pill/action" row shape. [Cofounder task panel](https://mobbin.com/screens/e1aeef97-e084-41f1-8167-2ff9c10ebcf8) — "Requires Approval" tag distinct from routine task tags, a useful precedent for visually separating an override/approval action from a routine item within the same list.

**Post-render optimization pass (2026-09-13, against the first FRAME-01 build):** re-checked the built Needs Attention panel against [Linear's "High Priority Tasks" grouped view](https://mobbin.com/screens/610d34b6-6ad8-45ab-80fb-2107b31ed01e) and [Asana's grouped task list](https://mobbin.com/screens/6dddad98-49dc-4980-98f6-866b498f3b02) — both name a per-group row count next to the group label ("In Progress 5", "Todo 7"), not just one count badge for the whole panel. Our render has a single "Needs Attention 3" badge but no per-section count under "Overdue"/"This Week." **Adopted as a refinement** — a per-section count lets Grace judge urgency mix (how many are truly overdue vs. merely due-soon) without reading every row, which is a direct answer to her journey's stage-2 friction (`01_USER_PERSONAS.md` §1: "notices... a problem"). Two further candidate refinements were identified but deferred (queued for a later single-issue prompt, per the one-issue-per-prompt rule): collapsible sections (every reference pulled — Wrike, ClickUp, Linear, Asana — makes its groups collapsible; useful once Needs Attention grows past 3-4 rows) and a leading priority icon per row in addition to the existing OVERDUE/DUE SOON pill (Linear's pattern; lower priority since the pill already satisfies the never-color-alone rule on its own).

### Fleet Status Summary + Map Preview (FRAME-01)
**What to search:** operations dashboard with KPI tiles above a bounded map preview.
**What to borrow:** [Shopify Live View](https://mobbin.com/screens/dfca7e4b-461b-49bc-9377-92575543a585) — compact 2x2 KPI tile grid directly beside/above a bounded (not full-bleed) map, exactly the "status counts + map thumbnail, not a full map" shape FRAME-01 needs; the map is clearly a secondary, contained element, not competing with the KPI tiles for primary attention.
**What to reject:** full-bleed maps at the Overview level (per `04_FIGMA_SCREEN_BLUEPRINT.md` §2, the full interactive map is FRAME-06 only).

### Dispatch Gate Checklist (FRAME-02)
**What to search:** pre-flight checklists, KYC/compliance gate UIs, "requirements to proceed" panels before a primary action unlocks.
**What to borrow:** the disabled-primary-button-until-all-pass pattern, and a visually distinct secondary path (override/exception) that requires justification input before it activates — this maps directly onto BR-001–BR-005 plus the mandatory override justification.
**What to reject:** checklist UIs that silently auto-advance without confirming each check explicitly to the user — Daniel needs to see *why* a gate failed, not just that dispatch is blocked.
**Reference pulled (2026-09-13, pre-generation check for FRAME-02):** [Airwallex Spend Requests](https://mobbin.com/screens/defdb85a-2fa6-4d65-93f1-bdd3e991dbe5) — queue list on the left (Pending approval / All requests), selected request's full detail in a right-side panel (amount, requester, category, comments, attachments), with a clear two-button decision pair at the bottom (Reject / Create card). This is the same reference the design system's approval-drawer pattern (Component 4) was originally benchmarked against, now independently reconfirmed for FRAME-02's two-pane shape specifically — borrow the list-left/detail-right split and the bottom-anchored decision buttons; reject Airwallex's single approve/reject pair as insufficient on its own, since FRAME-02 needs a third path (Request Override) that Airwallex's simpler spend-approval flow doesn't require.

**Fixed-pane references pulled (2026-09-13), specifically for the "keep the queue visible, no dimming" mechanic confirmed for Daniel:** [Superlist](https://mobbin.com/screens/d34aae12-2518-42d7-8fbe-636dc90f36d1) — the strongest match: a genuine fixed three-pane layout where the middle list stays fully visible and interactive while the right pane shows the selected item's detail, no dimming or overlay anywhere; the selected row carries a left-edge accent bar, the same treatment our own render already uses for its highlighted row. [Evernote](https://mobbin.com/screens/98d68e8c-e100-4c18-a760-78fe88af4bb2) — persistent, undimmed note list on the left beside the open note on the right; notably shows a small breadcrumb-style label ("My Notebook > Dashboard Revamp [Feature Specs]") at the top of the detail pane, directly supporting the context-label decision already specced for FRAME-02's detail pane ("Dispatch Management → Request Detail"). [Asana's task detail](https://mobbin.com/screens/65163ad4-c2b6-4d46-9c5b-623d24a3c53d) — third confirmation of the same pattern, with generously spaced fields and a comments/activity section below, reinforcing the spacing polish already borrowed from Airwallex. No new structural gaps found — these references confirm the fixed-pane decision and its existing spec (context label, spacing, selected-row highlight) rather than surfacing anything unaddressed.

**Second-round render check (2026-09-13) — 5 issues found, none matching the references above:** (1) the pane width split rendered as roughly 75-80% table / 20-25% detail panel, inverted from the specced ~55/45 (`04_FIGMA_SCREEN_BLUEPRINT.md` §3) — likely the root cause of (2); (2) the queue table's Status column (READY/APPROVED/PENDING pills) is no longer visible at all; (3) the left nav dropped from the required 20-item SRS module list to 8 items, breaking the shared-shell consistency rule (Component 1); (4) "Override Requested" still renders as a bordered/outlined treatment indistinguishable from a status label, not a clearly pressable action (the fix from the prior round didn't land); (5) the "Dispatch Management → Request Detail" context label specced for the detail pane is absent. Fixed as one combined prompt per user request (5 independent, low-collision issues — layout ratio, nav content, table column, button styling, label addition — none likely to interfere with each other).

**Post-render quality check (2026-09-13) — user flagged the first FRAME-02 render as not good enough; re-benchmarked against [Airwallex's spend request detail panel](https://mobbin.com/screens/eb0a451e-ecc1-474b-97fd-57dabeb9c8f2) and [folk's contact detail panel](https://mobbin.com/screens/06c9bc5f-7cc0-4a47-9851-4678953abb86).** Four concrete gaps found, none of them content/structure (the structure — queue left, fixed detail pane right, checklist, gated buttons — was already confirmed correct): (1) our detail panel has no visual elevation/separation from the page — both references give the detail panel its own surface treatment (shadow, tonal shift, or border) that reads as "attached to" the selected row, ours is two flat boxes with no depth cue; (2) our checklist/summary content is cramped — Airwallex spaces its fields (Requested amount, dates, category) generously, ours compresses the request summary and 5-item checklist into a tighter rhythm; (3) our "Override Requested" button, styled as a filled/bordered green state, reads more like a status label than a pressable action — Daniel can't tell if he already clicked it; (4) the queue table's Status column is clipped at the pane's right edge, visible in no reference (an unambiguous layout bug, not a style judgment call). Fix prompt issued as one combined batch (lower risk than FRAME-01's batch, since none of the 4 items could plausibly cancel another out).

### Work Order Kanban Board (FRAME-03)
**What to search:** kanban/board views in project-management and field-service tools, specifically ones with a hard release/completion gate on the final column.
**What to borrow:** age-in-column indicators (a job stalling in "Awaiting Parts" for 5 days should look different from one that just arrived) and a disabled terminal action until a sub-checklist completes.
**What to reject:** kanban boards that allow free drag-and-drop between any two columns — the workshop flow (`02_USER_FLOWS.md` §4) has a defined, non-arbitrary state machine; the UI should reflect that some transitions are illegal, not allow any card to be dropped anywhere.
**Reference pulled (2026-09-13, pre-generation check for FRAME-03):** [ClickUp Dashboard Revamp board](https://mobbin.com/screens/0c287f59-753c-4e28-92ad-9dff95fcde36) — 5 columns, each card with a clear title, tags, and a relative-time indicator ("2 days ago", "Yesterday") that directly matches the age-in-column requirement. [HoneyBook project board](https://mobbin.com/screens/f5036961-b128-458f-a143-ac2f6abc8d0d) — secondary reference for a simpler, less tag-heavy card treatment, closer to this system's restrained-color preference than ClickUp's busier card chrome — borrow ClickUp's age-indicator mechanic, borrow HoneyBook's restraint on card decoration.

**Post-render check (2026-09-13) — two findings against real references, both actioned.** (1) Checked against [Xero's bill detail panel](https://mobbin.com/screens/5c2c4985-befa-4532-b555-de989baf4281): Xero shows an itemized line-list (description, qty, price) summing visibly to a Subtotal → Total. Our render's job card detail shows "Cost Charged: KES 42,500.00" as a flat figure with no visible derivation from the Parts Replaced list or the 4.5hrs × KES 1,500/hr labour line above it — a real audit-substance gap for a system whose entire Finance persona (Miriam, FRAME-05) exists to catch exactly this kind of unreconciled figure. Fixed: added a parts + labour cost breakdown that visibly sums to the charged total. (2) Checked against [Slack's Project Tracker](https://mobbin.com/screens/1f60cc67-befa-4043-a5b0-69cdb611a1f4): Slack tints an entire column's header when it contains a blocked item, not just the individual card — a column-level signal in addition to our existing card-level one (red border + "STALLED" badge on the individual card). Adopted as a minor enhancement: the "Awaiting Parts" column header itself gets a subtle tint when it contains a stalled card, on top of (not replacing) the existing per-card signal.

### Executive KPI Tiles + Trend (FRAME-04)
**What to search:** executive/leadership dashboards in BI tools (large-number tiles, minimal chrome, one drill level).
**What to borrow:** large, unambiguous numerals with a target/benchmark shown alongside (not just the raw figure) — matches Sarah's stated need for "defensible numbers," which means context (vs. target, vs. last period), not just a bigger font.
**What to reject:** dashboards with more than one drill level or dense filter controls — Sarah's persona explicitly has no transactional need for that depth; matching a general BI tool's full interactivity here would violate her "read-only briefing" requirement.
**Reference pulled (2026-09-13, pre-generation check for FRAME-04):** [Steep](https://mobbin.com/screens/e6f2568b-7736-460a-95cf-e68a5683ca5e) — large KPI figures shown directly against a target ("Registrations 75.83K / 35K") with a small delta/trend indicator, near-exact match for the Fleet Availability % (target ≥85%) requirement. [Twenty CRM](https://mobbin.com/screens/4ed9c91a-c71a-44d6-8279-defff70a6ce3) — the "Deals by Company" donut pairs with a detail table beside it that updates in place, confirming the "expand inline, don't navigate away" requirement for the departmental breakdown drill-down.

**Post-render check (2026-09-13), direct Figma inspection of node 159:278 — 4 issues found, confirming a recurring pattern.** Content-wise the screen matches spec well: correct KPI scope (fleet-only costs per SRS §7.1), the 85% target reference line on the Availability Trend chart, and the departmental breakdown correctly scoped to fleet cost categories (fuel/maintenance/insurance/tyres), not general county department budgets. Four defects found: (1) two left-nav items appear simultaneously highlighted (Workshop Management AND Reporting & BI) — only one should ever be active; (2) KPI delta dots are still bare color-only indicators with no text/icon, the same defect already confirmed and fix-prompted on FRAME-01 — this is now a recurring, system-wide gap rather than a one-off, worth treating as a standing Component 2 checklist item rather than a per-screen catch; (3) both trend line charts have a disconnected/orphaned data point floating near "Apr", separate from the main line — a chart rendering defect, not a style choice; (4) the "Expenditure by Department" section carries permanent instructional copy ("Click a department to view sub-allocations · Public Works selected below") rather than relying on a hover/cursor affordance — flagged as a judgment call, not yet resolved either way.

### Budget Variance Bar (FRAME-05)
**What to search:** budget-vs-actual visualizations in finance/expense-management tools.
**What to borrow:** explicit percentage/currency labels alongside the bar, sorted by variance severity — never relying on bar length alone to communicate overrun, consistent with the design system's "never color/length alone" rule.
**What to reject:** stacked or 100%-normalized bars that obscure the absolute overrun amount — Miriam needs the actual shilling variance, not just a proportion.

### Anomaly Review Queue (FRAME-05)
**What to search:** fraud/dispute review queues in fintech back-office tools.
**What to borrow:** a clear three-way decision control per flagged item (confirm / dismiss / escalate) rather than a binary approve/reject — matches the fuel anomaly flow's three terminal states (`02_USER_FLOWS.md` §5).
**What to reject:** review queues that bury the flag *reason* behind a click — the reason (duplicate transaction, tank-capacity exceeded, etc.) should be visible in the queue row itself, not only in the detail drawer, since it's often the fastest signal for triage priority.
**Reference pulled (2026-09-13, pre-generation check for FRAME-05):** [Reddit Mod Queue](https://mobbin.com/screens/9e81dbcf-db79-45ef-8347-08e81e1b5b77) — queue list on the left with a "Needs Review" tab, flag reason visible directly on the row as a tag ("Self-promo removal"), selected item's full context and action history on the right. Near-exact match for our queue → reason-visible-on-row → detail drawer → decision shape. [Whop's transaction table](https://mobbin.com/screens/6472b575-afa7-4fb6-9a91-dbfaa034e121) — secondary reference for the queue table itself, showing Status, Reason, and User columns all visible without opening a row, reinforcing the "don't bury the reason" rejection above.

**Detail panel mechanic decided (2026-09-13) — Airwallex's true drawer vs. a fixed pane, benchmarked directly against [Airwallex's Spend Requests drawer](https://mobbin.com/screens/eb0a451e-ecc1-474b-97fd-57dabeb9c8f2).** User flagged Airwallex's drawer treatment (dimmed background, slide-in, close button, generously spaced fields, bottom-anchored two-button decision) as a direction worth taking seriously across both FRAME-02 and FRAME-05. Reasoned per-persona rather than applied uniformly: **Miriam (FRAME-05) gets the true drawer** — her anomaly review is a focused, one-at-a-time investigation, the same shape as Airwallex's own spend-approval use case, so the decision-focus tradeoff (background dimmed, full attention on one transaction) is a net benefit. **Daniel (FRAME-02) keeps his fixed side-by-side pane** — his stated core goal is speed across a high-volume queue (`01_USER_PERSONAS.md` §2), and a true drawer would cost him the ability to glance at upcoming queue rows while resolving the current one, a real throughput cost his journey's friction (the gate check itself, not decision-focus) doesn't justify trading away. Airwallex's spacing and button-clarity polish is borrowed on both screens regardless of which mechanic each uses.

### Fleet Status Summary map preview (FRAME-01) — post-render optimization pass (2026-09-13)
**Reference checked:** [Felt operations map](https://mobbin.com/screens/69edfc38-9b7d-4d32-8319-87ebd3cb3829) — puts a legend (color swatch + label, e.g. "active"/"inactive") directly on the map surface itself, not only in an adjacent list.
**Gap found:** our render's map preview has colored vehicle markers but no on-map legend — a viewer looking only at the map thumbnail (not the status list beside it) can't decode what the marker colors mean. This partly defeats the point of a self-contained "preview."
**Status:** queued, not yet actioned — the higher-priority Recent Activity actor-field fix goes first (see below). Follow-up prompt when picked up: "Add a small legend overlay directly on the Fleet Status Summary map preview — a color swatch and label for each status (Available/On Trip/Grounded/Maintenance) shown in a corner of the map itself, so the map is decodable on its own without reading the status list beside it."

### Recent Activity (FRAME-01) — post-render optimization pass (2026-09-13)
**Reference checked:** [1Password Activity Log](https://mobbin.com/screens/84dbef44-916b-4322-956f-154845c224a7) — every row has the actor (who performed the action) as a distinct structured field, not folded into the event description sentence.
**Gap found:** our render's rows bury "who did it" inside the description prose (e.g. "Dispatch override authorized for KBZ 442A — insurance grace period" — no separate actor field). For an audit-sensitive system where the SRS (§8) and BR-009 both treat "who" as core audit data, not incidental detail, this is a real gap, not a cosmetic one.
**Status:** actioned next (see follow-up prompt below).

### All Vehicles / Fleet Registry table (FRAME-01 tab)
**What to search:** large asset/inventory registries with status breakdown, filters, and per-row detail action.
**Reference pulled (2026-09-13, pre-generation check):** [Deel's Assets registry](https://mobbin.com/screens/27f3bda0-f620-443a-b3c6-61a87141e9c5) — near-direct match: a "Total inventory: 22 assets" summary tile, a status-breakdown bar above the table (With worker / In transit / In storage / Write off), rich filter-chip row (Worker, Stored with, Organization, Category, Location), and a "Quick view" action per row. [Employment Hero's Policies table](https://mobbin.com/screens/47d85c21-a910-407a-b9e3-c85ac7dd6430) — shows urgency as text directly in the row ("Overdue by 1 day"), confirming our Insurance/Inspection Expiry columns should show urgency framing, not just a raw date.
**What to borrow:** Deel's status-breakdown bar above the table (a quick visual gut-check before scrolling the full list) and its "Quick view" row action pattern; Employment Hero's urgency-as-text-in-row for expiry columns.
**What to reject:** Deel's category-heavy filter row (Worker, Stored with, Organization, Category, Location — 5 filters) — our spec calls for 3 (department, status, station), which is the right scope for 247 vehicles vs. Deel's more heterogeneous asset types; adding filters beyond what the data actually needs would be scope creep.

### Live Fleet Map (FRAME-06)
**What to search:** fleet/logistics live-tracking maps (delivery, ride-hailing ops dashboards).
**What to borrow:** distinct marker shapes/icons per alert type (not just color) layered over a status-colored base marker — satisfies the same never-color-alone rule for a much higher-stakes context (after-hours movement, speed violation).
**What to reject:** map-first layouts that hide the vehicle list entirely behind the map — the side panel list (§7 of the blueprint) must stay visible, since Grace's job on this screen is still to find and act on specific vehicles, not just admire the spatial view.
**Reference pulled (2026-09-13, pre-generation check for FRAME-06):** [Felt operations map](https://mobbin.com/screens/58a17ddb-ae85-48cf-96d8-aa8c632517d7) — clicking a marker opens a "Selected item" popup with driver/vehicle ID, zone, street, status, and coordinates, plus a legend distinguishing active/inactive by color — directly validates the "markers carry a label/icon on hover or selection" requirement. [DoorDash live tracking](https://mobbin.com/screens/7dd1a9a3-3e80-4ee0-8c05-a56fb85bd5d0) — persistent right-side panel with live status and detail, positioned alongside the map (not overlaying it), reinforcing the collapsible-but-present side panel requirement rather than a map-only layout.

---

### FRAME-07: Driver Mobile Application (Joseph Mutua) — pre-generation check (2026-09-18)

**What to search:** consumer driver/logistics apps with a task-card home screen, a vehicle-condition inspection flow, and a mileage/odometer capture step — the three sub-screens FRAME-07 actually needs (`04_FIGMA_SCREEN_BLUEPRINT.md` §8). No single app has all three well; borrow per-screen.

**7A (Assigned Trip & Vehicle Card):** [DoorDash Dasher's "Current dash"](https://mobbin.com/screens/5859ffb5-02a0-45ee-9065-2ea87eaf43fa) — closest structural match: one dominant current-task card (pickup/deliver, ETA) above a map, not competing panels. **Borrow:** the single-hero-card hierarchy — one Trip Card dominates, vehicle/requester info are secondary rows beneath it, not equal-weight cards. **Reject:** Dasher's live-earnings/promo content — irrelevant to a government driver's job, would read as decorative here (violates the project's own simplicity direction, `07_FIRST_DRAFT_CONTEXT_CARD.md`). [Turo's "Booked trip" detail](https://mobbin.com/screens/0e751340-72e7-44fa-a435-ac0a8e984f50) — confirms a persistent bottom tab bar even on a task-focused screen, and a full-width primary action button pinned near the bottom, both already in FRAME-07's spec.

**Content re-check (2026-09-21), prompted by the user asking whether the spec actually reflects what a driver needs, not just style.** Honest caveat first: DoorDash/Turo/Grab are consumer gig-work apps, not true B2B fleet-driver apps — Mobbin has no indexed results found for genuine fleet-driver tools (Samsara, Onfleet, Fleetio, Verizon Connect); this benchmark is the closest available, not a perfect match. Two further references pulled: [Grab Driver's Route Details](https://mobbin.com/screens/ca866942-38fe-469f-94d9-f0541d458c02) and [Jobber's mobile home screen](https://mobbin.com/screens/37434a49-440a-4f28-a9f1-ad057c39fd69) (Jobber — a genuine field-service-worker app, technicians visiting job sites — is the closest real analog to a government driver found so far).

**Three real content gaps found, not just visual ones — applied to `04_FIGMA_SCREEN_BLUEPRINT.md` §8:**
1. **No contact action for the requester.** Grab Driver puts `FREE CALL / CHAT / CANCEL` directly on the trip screen as first-class per-stop actions. **Borrowed:** a call-icon button directly on the requester info row — a CVFMS driver plausibly needs to reach the requester (rural office access, running late) more than a gig driver needs to reach a customer.
2. **Single-trip vs. multi-trip framing was never actually decided.** The header said "TODAY'S SCHEDULE" (implying multiple) but only ever showed one card, with no way to see a second. **Decided:** single-trip-per-shift, matching SRS §11's scope — header renamed "YOUR TRIP." Jobber's pattern (a completion count + "View all") is the fallback shape if multi-trip is ever needed later, but not adopted now — don't build a scrolling trip list speculatively.
3. **Route/distance line — proposed, then reversed (2026-09-21).** This section originally recommended borrowing a compact route/distance/ETA line from DoorDash's and Jobber's map-led home screens. **User correction: CVFMS is explicitly not building an Uber/DoorDash-style navigation app.** Both those apps' core value proposition is live routing and turn-by-turn navigation — the exact thing this project has no reason to build. A distance/ETA figure implies a routing engine computing live drive time, which doesn't exist in this system and shouldn't be implied by the UI. **Reversed: no map, route line, or computed distance/ETA on this screen.** The driver's own phone maps app covers turn-by-turn needs if wanted; this screen's job is trip assignment and logging, not route guidance. **Lesson: DoorDash/Grab/Turo are navigation-first products by design — borrow their card hierarchy and contact-action patterns freely, but their map-centric layout choices specifically should not be borrowed here, since that's the one thing about them this project is deliberately not building.**

**Also found on the first rendered build (not a benchmark finding, a defect): the primary CTA ("Start Pre-Trip Inspection →") was missing from the render entirely**, and off-brand colors (red/purple/blue) were used for quick-action icons and status pills with no basis in the design system's actual token set (Civic Green as sole accent, 4-color status vocabulary). Both are implementation defects against an already-correct spec, not benchmark/content issues — fixed via a direct correction prompt, not a spec change.

**Trip Card action pattern (2026-09-21) — user pushed back on "no card actions needed," correctly.** Checked [Shopee's Order Details screen](https://mobbin.com/screens/aab471e9-7b4a-4405-8c1e-321a7e517fd6): its "Take from / [restaurant] ›" row uses a trailing chevron purely to view more detail, kept entirely separate from the driver row's own phone/chat icons. [inDrive's Order screen](https://mobbin.com/screens/ad7715b7-1700-49cc-9e1d-02df2a4e673a) reinforces the same principle — call/more/share are three distinct single-purpose controls, never combined into one icon doing double duty. **Adopted:** the Trip Card gets a trailing chevron "View Details" action (separate from the requester row's call icon) to surface content that was being truncated in the render ("...3 Pass..."). **Not adopted for the Vehicle Card** — nothing on it is hidden or truncated, so it doesn't need an equivalent action; the test is "is content being cut off," not "does every card need the same treatment for consistency."

**CTA placement fixed to a sticky footer (2026-09-21), prompted by a direct user concern about tech-literacy.** The primary CTA ("Start Pre-Trip Inspection") was just the last item in scrollable content, sitting directly above the bottom tab bar with no separation — risking (1) being pushed below the fold if the cards above grow, and (2) visually blending with the tab bar rather than reading as the screen's main action. **Confirmed fix via [Taco Bell's "START ORDER" screen](https://mobbin.com/screens/9b49e33b-c849-4fe8-8eed-e43b78ebb27b)** — a sticky footer CTA, fixed to the viewport bottom regardless of scroll, with its own background band separating it from the tab bar beneath. Adopted the same structure for FRAME 7A.

**7B (60-Second Walkaround Checklist):** [Turo's "Physical damage" checklist](https://mobbin.com/screens/c9fbb23e-0b26-4958-924a-ef9c171ae8a6) — confirms the checkbox-list shape (bold question header, plain rows, large final CTA) for a pre/post-trip condition check, the same job as FRAME-07's 4-item walkaround. [Lime's numbered damage-report diagram](https://mobbin.com/screens/a79e71e9-c9ce-4c2d-95f5-d33ce4bd5378) — pairs a labeled vehicle diagram with tap-to-select component tags plus a camera icon for photo evidence; **worth borrowing the camera-icon placement directly beside the flagged item**, not as a separate step, if a check fails — FRAME-07's current spec has "Photo Proof / Defect Capture" as one generic row below all 4 checks, which is looser than Lime's per-item attachment point. **Consider tightening this in a future revision:** attach the camera affordance to whichever specific row gets marked Fail, not as a blanket bottom-of-list action. **Reject:** Lime's diagram-based body-part selection — overkill for a 4-item mechanical checklist; a plain row list (as already specced) is the right amount of structure for this content volume.

**7C (Trip Start & End Bookends):** [Turo's "Check odometer & fuel level"](https://mobbin.com/screens/1e94c88b-f942-459c-8da3-20e72201b87d) — a near-exact match for FRAME-07's Start Journey state: a simple dashboard illustration, an odometer input row, a fuel-level selector row, one primary CTA ("Next"). **Confirms the spec's existing shape is correct** (large odometer display + fuel indicator + single CTA) — no changes needed here, this is a genuine independent confirmation, not a new borrow. [Mercedes-Benz's "Trip data" screen](https://mobbin.com/screens/b492b0f8-789c-4388-b298-ddfb78aff7f6) — shows distance/consumption stats grouped under "From Start" and "From Reset" headers; **borrow the labeled-grouping pattern** for FRAME-07's End Journey state, where starting odometer, closing odometer, and calculated distance currently read as a flat stack — a small "Trip Summary" label above those 3 rows would match this reference's clarity. **Reject:** Mercedes-Benz's driving-style/consumption analytics — out of scope, FRAME-07 only needs distance, not efficiency metrics.

---

### FRAME-01 whole-page simplicity — user-requested benchmark (2026-09-13)
**Reference:** [Jobber Home dashboard](https://mobbin.com/screens/56a6ce1c-8d71-4c1a-89cb-1d07f075424a) — user explicitly named liking its simplicity.
**What's actually doing the simplicity work (named specifically, not just "clean"):** (1) a date + human greeting line instead of a generic page title; (2) one combined "Workflow" row that is simultaneously the KPI row and the pipeline/urgency view, each card showing a count plus a 1-2 line sub-breakdown, rather than separate KPI and status panels; (3) near-zero saturated color — a single thin accent border per card, not pill-heavy; (4) a genuinely short to-do list with no urgency color-coding at all.
**What was borrowed into FRAME-01 (`04_FIGMA_SCREEN_BLUEPRINT.md` §2 revision):** the greeting line and the KPI/urgency-row merge — both transfer cleanly since they don't reduce audit/compliance content, just how it's grouped.
**What was deliberately NOT borrowed:** Jobber's near-total absence of structured, exception-routed content (its Activity Feed is a flat log, not filtered to override/exception events; its To Do list has no equivalent of a mandatory-gate action). CVFMS's audit/compliance obligations (SRS §8, BR-009) are a hard constraint Jobber's small-business context doesn't share — simplicity is borrowed where it's free, not where it would cost real audit content.

---

### FRAME-01 direct Figma node inspection (2026-09-13) — 4 confirmed structural defects, then a duplicate-frame discovery
Checked the actual Figma file (`get_metadata` + `get_screenshot` on node 133:28), not just a rendered screenshot, per the user's direct request to check the file itself. Found 4 defects confirmed at the node-data level, not just a visual read:
1. **Sidebar is icon-only, 48px wide.** All 20 `nav-item` frames exist and are correctly ordered, but none contain a text node — only an icon frame each. The spec calls for a 240px labeled rail (`03_MASTER_DESIGN_SYSTEM.md` Component 1); Grace cannot read module names as built.
2. **Duplicate header content exists simultaneously in the file.** `header-left` still contains the full "Fleet Operations Overview" title + "Manager: Grace Wanjiru • Live Command Active" subtitle (y=20-49) AND a separate `greeting-header` frame with the date + "Good morning, Grace" (y=24-82) exists at the same time, both rendering. This is the exact redundancy flagged and supposedly fixed earlier — confirmed still present structurally.
3. **Recent Activity row text is truncated mid-string in the underlying data**, not just visually clipped — e.g. row-4's actual text node content is `"System - GPS offline alert cleared for"` with nothing after "for," missing the vehicle registration entirely. Same likely true of rows 1-3 given their "for - [reason]" pattern with no reg number visible between "for" and the dash.
4. **KPI delta indicators are bare `Ellipse` shapes with no sibling text node** (e.g. `availability-value` contains only "89%" text plus an 8×8 Ellipse, no delta text/icon). This is a real, structural "color alone" violation, not a rendering artifact — the design system's binding accessibility rule (§A) is violated at the file level.

**Transient duplicate frame observed, then gone (2026-09-13).** A second top-level frame — `133:303`, "fleet-operations-dashboard" — briefly appeared in one metadata pull with nearly everything fixed (labeled sidebar, clean header, complete Recent Activity text, on-map legend). A subsequent, fresh pull of the same file no longer showed `133:303` at all, and a fresh screenshot of `133:28` showed its sidebar now correctly labeled (this had NOT been true on the first pull) but the header-duplication, Recent Activity truncation, and bare-delta-ellipse issues still present. **Conclusion: the file was being actively edited between calls (by the user or their Figma agent) — do not treat any single snapshot as ground truth without re-verifying immediately before acting on it.** As of the last confirmed check, node `133:28` is the only Grace-screen frame in the file, its sidebar labeling is fixed, but the header-duplication, Recent-Activity-truncation, and bare-delta-ellipse defects remain live and unfixed.

### FRAME-01 v2 ("Today", desktop redesign) — references pulled 2026-09-24

Pulled after Prompt 2 had already rendered (`12_DESKTOP_REDESIGN.md` §6). The pre-generation check
was skipped, which breaks doc 06 §1. These references feed the §6b fix pass instead. Mobbin has no
real fleet-telematics apps (Samsara, Motive, Fleetio); a "fleet dashboard" search returned
Felt/Navan/Turo/Jobber, so the closest analogues are used.

**Live alerts strip:**
- References: [1Password home insight card](https://mobbin.com/screens/0c0e3801-36fd-47a6-bf49-d3cc9b1ef2a9),
  [OpenAI Platform service health](https://mobbin.com/screens/d605f83d-3869-4ecc-8874-b913e09e2930),
  [Okta dashboard Status card](https://mobbin.com/screens/72c7a956-c9ec-45ef-872e-c3ec74d672df),
  [Navan risk alerts](https://mobbin.com/screens/28cd77d0-1557-4e50-8e11-9ff9baa010e7).
- Borrow: all three dashboards keep alerts calm. The card stays white, color shows only in a small
  status indicator, the title is neutral dark text, and there's one link to the detail list.
  1Password pairs a big count with one sentence and "View list →". OpenAI shows a one-line status
  headline plus a compact incident list.
- Reject: Navan's red-tinted, red-titled rows with a left accent bar. That's a dedicated alerts
  page, not a dashboard strip, and it's the same over-weighting our first render showed.
- Consequence for CVFMS: confirms §6b fix 1 (white strip, color only in icon badges, titles in
  #0F172A). Add from OpenAI: a calm "All clear · no live alerts" state for when nothing is active.

**Dispatch pipeline:**
- References: [QuickBooks Customer Hub funnel](https://mobbin.com/screens/a8df8917-46aa-4226-a13b-facf6b7471a7),
  [Jobber Home "Workflow"](https://mobbin.com/screens/56a6ce1c-8d71-4c1a-89cb-1d07f075424a) (already
  the FRAME-01 simplicity reference).
- Borrow: both use the same anatomy. A small stage label on top, a big count under it, chevrons
  between stages, and Jobber adds one sub-line per stage ("Overdue (0)"). No rings or circles.
- Reject: QuickBooks' boxed stages with colored top bars. That's extra chrome inside an
  already-bordered card, the "boxes inside boxes" problem again.
- Consequence for CVFMS: §6b fix 3 changes to label on top → big count → optional sub-line, with
  stages unboxed.

**"Awaiting your approval" on a dashboard:**
- References: [Airwallex Spend requests summary](https://mobbin.com/screens/64cb7251-edd5-4bfa-ad69-8f89182ffafa),
  [Braintrust offers](https://mobbin.com/screens/c1a094dc-669d-4811-971b-efced426b82a),
  [Remote time-off requests](https://mobbin.com/screens/68c88a4c-0241-4007-928d-41f2a85f311f).
- Borrow: Airwallex summarizes as "Pending your approval · 1" and puts the decision on the
  requests page. Our 3 rows with a single "Review" entry point match that intent: an override
  needs its justification read first.
- Reject: Braintrust's inline Accept/Decline. One-click approval of a dispatch override from a
  dashboard row would skip reading the justification, which the audit trail relies on.
- Consequence for CVFMS: keep the rows with "Review" only. Never add inline Approve here.

**Requirement/status rows (for Needs attention):**
- Reference: [Turo Safety & inspections](https://mobbin.com/screens/1da7e13a-881d-4843-b2f4-ccce79fa25c7).
- Borrow: plain requirement rows with a small status pill ("Up to date", "Need 10 more trips")
  and one specific action button. The same shape as our Needs attention rows, with calm color.
- Reject: Turo wraps each requirement in its own bordered box, which works on a single-topic
  page. On our dense dashboard card it's boxes inside boxes, so we use divider rows instead.

### Information-heavy pages — user-selected references (2026-09-24)

The user picked these as models for pages that carry a lot of information without overwhelming:
OpenAI Platform (service health), Okta (admin dashboard), Fresha (home), Apollo (home), Wix
(Sales overview), QuickBooks (Customer Hub), Jobber (home), Mixpanel. Mixpanel wasn't shared as a
screen yet, so no findings are recorded for it.

| Pattern | Seen in | CVFMS use |
|---|---|---|
| **State in one sentence first** ("All systems operational"), with details collapsed underneath | OpenAI | Live alerts header reads "All clear" or "3 live alerts need review"; nothing else when clear |
| **Collapsed-by-default rows with a status icon**, expanded on demand | OpenAI (per-service accordions) | Needs attention groups can collapse; secondary detail stays one click away |
| **Group by type with counts, then open the items** (Type · Items · Description · View) | Okta Tasks | Scales Needs attention to 1,056 vehicles: "Insurance expired · 2 vehicles · Renew →" rows that expand to the vehicles |
| **Metrics in one band with dividers**, not separate tiles | Apollo "Your email stats" | Confirms the Fleet state band (§7.4 fix 1) |
| **Every card states its time window** ("Last 7 days", "Next 7 days", "This month") | Fresha, Apollo, Wix | Fuel "This month", Due "This week", alerts "Since 06:00" |
| **One hero number + at most 2 supporting facts** per card | Fresha (Recent sales, Upcoming appointments) | Budget for any summary card on an overview |
| **Freshness timestamp** ("Updated at …") | Okta | "Updated 10:42" by the scope filter; matters for live GPS data |
| **Filter tabs inside a card** (All · Call · Email · +3 more) | Apollo "Your tasks" | Answers "do we need tabs?": filter a list inside its card, not page-level tabs |
| **Every summary card ends in one exit link** ("See full report", "View all") | Wix, Okta, OpenAI | Every Today block links to its tier-3 page |
| **Page title + one-line purpose + date-range control with comparison stated** | Wix | Work surfaces and analytics pages (FRAME-04/05), not the landing page |

**Added 2026-09-24 (user picks):**

| Pattern | Seen in | CVFMS use |
|---|---|---|
| **Status band where the label carries the count and color marks only the problem cell**: "Draft (7) · Awaiting approval (0) · Awaiting payment (6) · Overdue (2)", with only "Overdue" in red | Xero Sales overview | Fleet state band and dispatch pipeline: neutral cells, and only the exception cell (e.g. "Grounded (23)", "Needs driver (5)") takes red/amber |
| **Section title with inline quick links to its sub-pages** ("Invoices and payments · Invoices · Repeating invoices · Statements") | Xero | Each Today section header links straight to its tier-3 pages (e.g. "Needs attention · Compliance · Workshop · Drivers") — the removed information stays one click away |
| **Small top-N ranking table on a dashboard** ("Customers owing the most": 4 rows, Due/Overdue columns, red only when overdue > 0) | Xero | A dashboard table is fine when it's a short ranking. Candidate: "Stations needing attention" (top 4 stations by blocked + overdue), which answers "which station is struggling?" without a By-station tab |
| **Page-level filter bar under the title**: dropdowns with a leading icon, then a "Reset" link | Airwallex Billing | Today's filter row: Scope (station) · Period · Department · Reset. Same component on every work surface and analytics page |

Rejected from the same screens: Xero's "Create new" card and large empty-state illustration;
Airwallex's promotional banner; Airwallex's KPI tiles and charts showing 0.00, which should
collapse when empty.

**Rejected, and why:**
- Okta's 56% gauge: decorative, and the same fact fits in one line of text.
- Fresha's and Wix's trend charts on a home page: Today answers "what needs me now", not trends.
  Trends belong to Executive/Finance (FRAME-04/05).
- Apollo's truncated metric labels ("# Emails S…"): a truncated KPI label is unreadable.
- Apollo's and Wix's oversized empty states: an empty section should shrink to one line, not keep
  its full card height.

### Page header (top bar + first row) and live-alert layout — 2026-09-24

**Top bar and the row directly below it:**
- References: [Amplitude](https://mobbin.com/screens/56f5ff3c-cf4c-47e0-b3cd-7040097105e5) (small
  scope selector above the page title; "Last edited…" freshness right-aligned on the title row),
  [Asana](https://mobbin.com/screens/69821f2b-6cdb-4d4f-b432-52a11b26ea4c) (page title with tabs
  directly beneath, as one compact header block),
  [Fibery](https://mobbin.com/screens/ee8fe01a-efea-4f2e-bacc-297a566c8ea7),
  [Klaviyo](https://mobbin.com/screens/00ffa911-2087-448a-8fbb-6d10592666fe),
  [Fabric](https://mobbin.com/screens/8b1dee7d-68a4-4f99-b7ef-4f3eb374983f) (greeting only, no date line).
- Borrow:
  - Greeting and page context share **one header row**: title left; scope + freshness right.
    Tabs sit directly under it.
  - The top bar stays lean: search and account only.
  - None of these apps give the date its own line. Only Jobber (already referenced) does.
- Consequence for CVFMS:
  - Drop the standalone date line; the date joins the freshness stamp ("Wed 24 Sep · Updated 10:42").
  - Scope switcher and stamp go on the right of the greeting row.
  - Search moves to the left edge of the top bar, so the bar doesn't read as empty on the left.

**Live alerts: long rows with the action at the far edge:**
- References: [Evernote home](https://mobbin.com/screens/8a1cf5b7-c30b-419c-b601-280c9cf6b1d9) (small
  side-by-side items, action link directly under each message),
  [Nextdoor alerts](https://mobbin.com/screens/4ecb2d52-8337-4786-adaf-118b1019164b) (narrow alert
  cards, actions under the text),
  [Vapi Issues](https://mobbin.com/screens/9afecd03-c74c-41b9-b1f3-a4eee7089c21) (compact severity
  summary).
- Borrow:
  - Alerts as **2–3 side-by-side columns**, each with icon, title, detail, and the action right
    under the detail. The eye never travels across the page to act.
  - The column structure is fine as long as the columns stay white (the v2 failure was the tint,
    not the columns).
- Reject: far-right actions on full-width rows. That's a table convention (Sentry, incident.io),
  and it only works when there are column headers to follow; on a 1,500px free-text row it breaks
  proximity.

### Requests & trips views (queue, approval, my requests, form) — 2026-09-25

**Approval detail:**
- References: [Aboard expense approval](https://mobbin.com/screens/d15cd548-a758-4743-8944-99c825340019)
  (right pane: status banner, details as label-over-value, a vertical "Approval flow" showing who
  approved / who is awaited, small Reject + Approve footer),
  [Airwallex spend request drawer](https://mobbin.com/screens/f13414b4-443f-4484-bd3a-4b5970db2cc3)
  (3 facts per row, comments, attachments, footer Reject ▾ + primary; the confirmation toast says
  **what happens next**: "forwarded to the finance admin").
- Borrow:
  - A confirmation toast that names the next step and person.
  - Approval-flow names (who approved, who's next) inside the stepper.
  - A quiet footer.
- Reject: none of these show the extra outlined red "Reject" button that our render used.

**Approver list:**
- Reference: [ClickUp timesheet approvals](https://mobbin.com/screens/9ce37d47-c27d-4dff-bad7-5a07fcf657a4)
  (tabs "To review (1) · Changes requested · Approved · All").
- Borrow: an approver's view is simple tabs by *their* decision states; they don't need the whole
  fleet pipeline.

**Requester list:**
- References: [Dropbox file requests](https://mobbin.com/screens/21039b6c-ca3f-4a9a-9b13-b29a79b789f8),
  [Oyster change requests](https://mobbin.com/screens/3d0b1a3d-ebd3-453f-9997-14404ab41e5d)
  (plain table, status pill, "Cancel request" in a row menu).
- Borrow: the page title is the only "My requests" title; there's no second card heading repeating it.

**Request form:**
- References: [Airwallex create request](https://mobbin.com/screens/4efbaa43-71e9-45ef-885e-b7618ee6328b)
  (focused page, sectioned: Request details / Comments / Attachments; Save draft + Submit bottom
  right), [Oyster request time off](https://mobbin.com/screens/66bcd0a0-3d24-4128-a797-c92736ccbff8)
  (live calculated summary line: "You are requesting 1 day off"),
  [Jobber request form](https://mobbin.com/screens/79fec6e5-9bd9-4452-a9e3-999c7a47688a)
  ("(optional)" labels; Cancel + Submit).
- Borrow:
  - Section headings.
  - "(optional)" markers.
  - A live summary of what will happen: approver, distance, estimated cost.
  - Cancel + Save draft + Submit.
- Reject: Oyster's and Airwallex's two-column date pairs, per our single-column rule for inputs.

**Stage filter strip (pipeline sub-navigation) — 2026-09-25:**
- Context: All Requests & trips queue views need a stage filter at the top to let Daniel jump between dispatch stages. Previous approach (arrow/chevron polygons) failed twice: Figma AI cannot reliably build custom polygon arrow shapes, producing rogue diagonal vector lines cutting through text. Reconsidered from scratch.
- References: [Xero — Quotes](https://mobbin.com/screens/1269d955-9ebd-41ca-aefa-8263328cb49d) (underline tab bar "All | Draft 1 | Sent 1 | Declined 0 | Accepted 1 | Invoiced 0" — count embedded in label, 2px active underline, full-width search below, 36px strip height, zero visual weight), [Deputy — Timesheets](https://mobbin.com/screens/40b0eeda-18ea-4067-ba0f-1b757cdbe424) (underline tabs with counts "All 13 | Pending 11 | Approved 2 | Discarded 1" — same pattern in an approval workflow, direct match for our use case).
- Rejected alternatives: [Employment Hero — Applicants](https://mobbin.com/screens/ed5db237-5d3c-4cb3-949a-f7ecfce3724a) (filled pill tabs with counts — correct shape but the solid-fill active state reads as a permanent status badge, not a clickable filter; also harder for Figma AI to width-balance across 7 stages on a 1776px canvas). Reddit Mod Queue (filled dark pill, no counts — loses the count-per-stage data essential for Daniel's triage).
- Borrow:
  - Underline-only active state: 2px `#006837` line pinned to the bottom of the tab, text `#006837` bold. No pill, no filled background.
  - Count embedded in the tab label (e.g. "Ready  9"), not a separate badge element.
  - Warning stage: amber `#B45309` text for both label and count ("Needs driver  5") — no amber background, color on text only.
  - Container: horizontal Auto Layout, 40px tall, bottom border 1px `#E2E8F0`, no card wrap.
  - Below the strip: 13px `#64748B` sub-caption ("Showing Ready · 9 of 104 total").
- Reject: any arrow/chevron polygon shape; any filled-background active pill per Employment Hero; any chip/badge element separate from the label text.
- **Recorded as P8 (Pipeline Segment) replacement in `13_SYSTEM_MAP.md`.** Apply to all queue-role frames (queue-transport, queue-approver where a stage strip is shown).

## 3. Standing Rule

Every entry above must specify what to borrow *and* what to reject — a benchmark that only says "make it look like X" without a stated reason invites the same drift the prior version's process doc (`06_DESIGN_QUALITY_PROCESS.md`) was written to prevent. When a new component is added to the system, add its benchmark entry here before writing its first generation prompt, not after.
