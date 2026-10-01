# CVFMS User Personas

**Document ID:** `DOC-CVFMS-001`
**Revision:** 3.0 (2026-09-16) — extended to cover all 16 SRS roles, per explicit user instruction. Wave 1 (5 flagship personas, unchanged from v2.1) restructured to apply the `ui-ux-expert` skill's stated user-centered design method explicitly: goals/motivations first, then a journey mapped stage-by-stage to surface friction points, rather than a flat responsibilities/pain-points list (v2.0 structure, still available at `docs/archive/`). Wave 2 (11 remaining roles, new in this revision) applies the identical method to close the coverage gap — see "Wave 2" section header for scoping rationale.
**Source of fact:** SRS Section 3 (Stakeholders), Section 4 (User Roles and Access Control), Section 5 (Functional Requirements, per-role sections as cited inline), Section 6 (Dashboards and BI), Section 8 (Audit Trail), Section 11 (Mobile Application), Section 14 (Configuration Management), and the RBAC role diagram in `CVFMS_Architecture_and_Implementation_Summary.md` §3. Every goal, journey stage, and friction point below is traceable to a specific SRS section or business rule — the SRS is a requirements document, not a UX research artifact, so it states *what the system must do*, not *how a user feels doing it*. Friction points are reasoned inferences from the gap between the SRS's stated objectives and its own description of the pre-CVFMS state (§15 Data Migration: "Excel/CSV, legacy fleet systems... manual registers") — flagged as inference, not fact, per the skill's own "based on real data" standard, which this project cannot fully meet without live user interviews.
**Method note:** `ui-ux-expert` does not ship a structured persona/journey template or dataset (unlike `ui-ux-pro-max`'s CSV-backed style/color/typography search domains) — it states the method as prose guidance ("create user personas based on real data," "map user journeys to identify friction points"). This document applies that method's *shape* deliberately; it cannot supply the "real data" the method calls for beyond what the SRS documents, since no user interviews or analytics exist for this pre-build project.
**Scope:** All 16 SRS-defined roles now have a documented persona (Wave 1: 5 flagship roles with a named dashboard tier or high-frequency transactional workflow, fully specced against Figma frames already built; Wave 2: the remaining 11 roles, documented to the same method but **not yet built as Figma screens** — see each Wave 2 persona's Design Implication for what a future screen would need). Documentation coverage is not the same as build-queue priority: the 5 flagship personas remain the build priority per the project's phasing decision (`08_PROJECT_HANDOVER.md`).

---

## 1. Grace Wanjiru — County Fleet Manager (Flagship Persona)

**SRS Role:** Fleet Manager (§4: "Overall fleet management").
**Goals & Motivations:** Know the real-time state of every vehicle in the fleet, and intervene before a small problem (an expiring insurance policy, an overdue service) becomes a compliance failure, a breakdown, or a stalled request. Motivated by direct accountability — she holds real write authority (registry, allocation, override, maintenance approval per SRS §5.1/§5.3/§5.6/§5.9), so a problem she misses is hers to answer for, not someone else's.

**Journey — a single recurring loop, mapped stage by stage:**

| Stage | What she does | Friction point today (inferred from SRS §15/§1.2 gap) |
| :--- | :--- | :--- |
| 1. Start of day | Tries to get a fleet-wide status picture. | Status is fragmented across spreadsheets, station phone calls, and paper logbooks — no single view. |
| 2. Spot a problem | Notices (or is told about) an expiring insurance policy, an overdue service, or an idle vehicle. | Compliance lapses surface only when a vehicle is already stopped, not with lead time — despite the SRS requiring 30/14/7-day alert windows (§5.23). |
| 3. Decide the action | Determines whether this needs a registry edit, a reallocation, a dispatch override, or a maintenance approval. | No single view connects an idle vehicle to a pending request for a different one — she has to cross-reference manually. |
| 4. Take the action | Performs the write action she's authorized for (§5.1, §5.3, §5.6, §5.9). | Historically has to leave whatever she was looking at and open a separate tool/screen to actually act — the finding and the fix live in different places. |
| 5. Confirm & return | Expects the record/state to reflect her action immediately. | No stated friction here from the SRS text — but this is the stage a UI can most easily get wrong (silent update, no confirmation) if not designed for deliberately. |

**Design Implication:** The dominant friction is stages 3-4 — finding a problem is necessary but not sufficient; every finding needs a direct, one-click path to the specific write action it calls for, without leaving the page. This is the reasoning behind FRAME-01's Needs Attention component (`04_FIGMA_SCREEN_BLUEPRINT.md` §2).

---

## 2. Daniel Otieno — Transport Officer

**SRS Role:** Transport Officer (§4: "Requests, allocation and dispatch").
**Goals & Motivations:** Move a vehicle request from submitted to dispatched as fast as possible without violating a mandatory dispatch gate (BR-001–BR-005). Motivated by throughput under a queue he doesn't control the size of — requests arrive continuously, and every one he clears wrong is a compliance/audit exposure with his name on it.

**Journey — linear, per request, mapped stage by stage (per SRS §5.4's own stated workflow):**

| Stage | What he does | Friction point today (SRS §23/BR-009 imply this stage has historically failed) |
| :--- | :--- | :--- |
| 1. Request arrives | Picks up a request that has cleared Supervisor Approval. | SRS §23 lists "ghost trips" and "unauthorized allocation" as known failure modes — implies requests were historically triaged without a systematic queue. |
| 2. Allocate | Assigns a vehicle and driver to the request. | No stated friction at this stage specifically, beyond the queue-visibility problem above. |
| 3. Gate check | Verifies insurance, driver licence/employment status, vehicle grounded-status, and a linked approved request (BR-001–BR-005). | Approving a request only to find at dispatch that the assigned vehicle's insurance lapsed — the exact failure BR-001 exists to prevent, implying this check was previously manual/unreliable. |
| 4a. All pass | Authorizes dispatch. | — |
| 4b. Any fail | Needs an authorized override with justification. | BR-009 ("all approvals shall be recorded in the audit trail") implies overrides previously happened verbally, with no record. |
| 5. Trip starts | Initiates the trip record (§5.5). | — |

**Design Implication:** Friction concentrates at stage 3 — the gate check needs to be pre-validated and visible *before* Daniel commits to a dispatch decision, not discovered as a failure after the fact. This is the reasoning behind FRAME-02's Dispatch Gate Checklist as a visible pass/fail panel, not a background validation (`04_FIGMA_SCREEN_BLUEPRINT.md` §3).

---

## 3. Peter Mwangi — Workshop Manager

**SRS Role:** Workshop Manager (§4: "Maintenance/workshop").
**Goals & Motivations:** Keep work orders moving from diagnosis through repair to quality sign-off and release, without losing track of parts requested against each job. Motivated by throughput on the shop floor plus accountability for what he signs off as roadworthy — a rubber-stamped release that fails later is traceable to him.

**Journey — a job card's lifecycle, mapped stage by stage (SRS §5.9, §5.10):**

| Stage | What he does | Friction point today |
| :--- | :--- | :--- |
| 1. Job created | Opens a work order from a defect report or a preventive-maintenance trigger. | SRS §15 confirms the starting state is manual/paper registers — a job card on a clipboard is only as complete as who remembered to file it. |
| 2. Diagnosis → parts request | Assigns a mechanic, requests parts against the job. | SRS §5.11 requiring parts to be explicitly "linked to maintenance work orders" implies this link doesn't reliably exist today — a mechanic could promise a completion date without knowing if the part is in stock. |
| 3. In repair (possibly re-entering "awaiting parts") | Tracks progress; a job can cycle back if a second part is needed. | No visibility into whether a job is stalling vs. progressing normally. |
| 4. Quality inspection | Verifies the repair before release — SRS §5.10 names this as a distinct, required step. | Naming it as distinct (not folded into "completion") implies release previously happened without a structured check. |
| 5. Release | Marks the vehicle available again. | — |

**Design Implication:** Friction concentrates at stages 2 and 4 — parts-stock visibility needs to travel with the job card (not live in a separate stores screen), and release needs to be a hard-gated action behind the QA checklist, not a rubber stamp. This is the reasoning behind FRAME-03's Kanban board with a disabled-until-verified release action (`04_FIGMA_SCREEN_BLUEPRINT.md` §4).

---

## 4. Sarah — County Executive (Governor / CECM / County Secretary)

**SRS Role:** County Executive (§3; dashboard tier named in §6).
**Goals & Motivations:** Answer, in under a minute and with defensible figures, whether the fleet is costing the county appropriately and is available when departments need it. Motivated by public accountability — these are numbers she may have to defend in a budget hearing or to the media, not just know for herself.

**Journey — infrequent, periodic, mapped stage by stage:**

| Stage | What she does | Friction point today |
| :--- | :--- | :--- |
| 1. Opens the dashboard (weekly/monthly, not daily) | Looks for a small number of headline figures. | SRS §1.1's own emphasis on a single "auditable" source of truth implies figures given verbally today don't reconcile with what Finance reports separately. |
| 2. Assesses a figure | Tries to judge whether a number (e.g. a cost spike) is normal or a problem. | No trend view — a point-in-time figure alone can't distinguish a new problem from a seasonal pattern. |
| 3. Wants to know why | Tries to find what's driving a headline number. | No drill path from a headline figure to its department-level contributor, despite the SRS scoping departmental benchmarking as executive-relevant content (§6, §7.1). |
| 4. Cites the number externally | Uses the figure in a hearing, meeting, or public statement. | If stage 1's number doesn't reconcile with Finance's separate figure, this stage is where that gap becomes a public liability. |

**Design Implication:** Friction concentrates at stages 2-3 — large, unambiguous KPI tiles alone are not enough; each needs a trend view (to resolve stage 2) and exactly one level of drill-down (to resolve stage 3), and nothing more, since her journey has no transactional stage at all. This is the reasoning behind FRAME-04 being read-only with a bounded drill depth (`04_FIGMA_SCREEN_BLUEPRINT.md` §5).

---

## 5. Miriam Chebet — Finance Officer

**SRS Role:** Finance Officer (§4: "Costs and payments"); dashboard tier named in §6.
**Goals & Motivations:** Reconcile fleet expenditure against budget and department cost centers before month-end/quarter-end close, and catch anomalies (BR-006–BR-010, §23) before Audit does. Motivated by a hard deadline (close) and a standing adversarial check (Audit) — both make unresolved discrepancies costly in a way that compounds over time if not caught early.

**Journey — recurring monthly cycle, mapped stage by stage:**

| Stage | What she does | Friction point today |
| :--- | :--- | :--- |
| 1. Gather expenditure data | Pulls fuel, maintenance, and insurance costs against budget/cost-centers. | SRS §5.20 requiring a purpose-built financial integration implies this was previously a manual, error-prone export/import exercise between systems that don't talk to each other. |
| 2. Reconcile | Matches recorded transactions against IFMIS/budget figures by department. | SRS §7 requiring 18 distinct exportable reports implies assembling budget-vs-actual today means stitching together separate exports by hand. |
| 3. Review anomalies | Looks for fraud/error signals (duplicate transactions, tank-capacity exceeded, odometer rollback, consumption outliers). | Anomaly flags generated by operational modules (fuel, maintenance) have no explicit routing to Finance in the SRS text — without a dedicated review surface, they risk staying buried in operational logs until Audit asks about them after the fact. |
| 4. Close / escalate | Confirms clean figures for close, or escalates a confirmed anomaly. | — |

**Design Implication:** Friction concentrates at stages 2-3 — a native budget-vs-actual view (resolving stage 2) and a dedicated, system-flagged anomaly queue (resolving stage 3) are both required; neither can be a byproduct of operational screens designed for someone else's job. This is the reasoning behind FRAME-05's two-tab structure (`04_FIGMA_SCREEN_BLUEPRINT.md` §6).

---

# Wave 2 — Remaining 11 SRS Roles (added 2026-09-16)

**Why these were deferred, and why they're being added now:** the SRS defines 16 discrete roles (§4). Wave 1 (above) covered the 5 with a named dashboard tier (§6) or an unambiguous, high-frequency transactional workflow — a deliberate, documented scoping decision, not an oversight (see `08_PROJECT_HANDOVER.md`). The user has since asked for all 16 roles to be documented. **This wave adds personas for the remaining 11, using the same method as Wave 1** (SRS-traced goals, journey-mapped friction, design implication) — but none of these 11 have a Figma frame built yet; that remains a separate, later decision (see the updated comparison matrix and `08_PROJECT_HANDOVER.md` for what's actually in the design/build queue vs. documented-only).

## 6. System Administrator

**SRS Role:** System Administrator (§4: "Configuration and administration").
**Goals & Motivations:** Keep the system's configuration (organizational structure, roles, workflows, thresholds, business rules) correct and current so every other role's screen behaves as expected — success is invisible (nothing breaks), failure is loud (wrong approvals route, wrong alert thresholds fire or don't).
**Journey — infrequent setup, frequent small adjustments:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Initial setup | Configure org structure, RBAC roles, approval workflows, maintenance/fuel/speed thresholds, cost centres (SRS §14). | No stated friction — this is greenfield configuration for a new system. |
| 2. Ongoing adjustment | Update a workflow, threshold, or role as county structure or policy changes. | SRS §14 requiring "configuration changes shall be audited" implies past ad-hoc config changes had no accountability trail — a real risk in a maker-checker system (§24). |
| 3. Diagnose a misconfiguration | Someone reports a workflow routing incorrectly or an alert not firing. | No dedicated diagnostic view implied anywhere in the SRS — likely means tracing the issue manually across whichever module is affected. |

**Design Implication:** A configuration/administration console is fundamentally different in shape from every Wave 1 persona's screen — it's a settings surface, not a triage or reconciliation view. Every change should write to the audit trail per §14's own requirement, and diagnosing a misconfiguration benefits from being able to see a change's downstream effect (which workflows/roles it touches) before committing it — not yet specced as a screen.

## 7. Fleet Officer

**SRS Role:** Fleet Officer (§4: "Vehicle records and operations") — distinct from the Fleet Manager (Grace): a field-operations role under her, not a duplicate.
**Goals & Motivations:** Keep vehicle master records accurate at the point of physical contact with the fleet — a field-level counterpart to Grace's registry-edit authority, closer to day-to-day station-level record-keeping than her policy/allocation-level view.
**Journey — station-based, record-keeping-driven:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Physical vehicle event | A vehicle arrives/departs a station, changes custodian, or needs a record correction. | SRS §15's confirmed manual/paper starting state means this is currently a logbook entry, not a system update. |
| 2. Update the registry | Records the change against SRS §5.1's vehicle master fields (station, custodian, status, etc.). | No stated friction distinct from the general registry gap Grace's persona already covers — this role's friction is largely about being physically at the point of the event, not remote from it. |
| 3. Flag an issue upstream | Notices something Grace or Peter needs to know (odd odometer reading, physical damage not yet logged as an accident). | No explicit escalation path named in the SRS for this specific role. |

**Design Implication:** Likely a mobile-friendly, field-usable subset of Grace's Fleet Registry (Component 6, `03_MASTER_DESIGN_SYSTEM.md`) rather than a wholly new screen — SRS §10 already requires "mobile-friendly screens" system-wide. Not yet specced as its own frame; may not need to be, if a role-scoped view of the existing registry table suffices.

## 8. Driver

**SRS Role:** Driver (§4: "Assigned vehicle/trip activities"); has a dedicated mobile application, not a web dashboard (SRS §11).
**Goals & Motivations:** Execute an assigned trip correctly and quickly — accept the trip, verify the vehicle is roadworthy, drive it, log what's needed, report anything wrong — without the app getting in the way of actually driving.
**Journey — per-trip, mobile-first, per SRS §11's explicit function list:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Login & view assignment | Opens the app, sees their assigned vehicle for the day, **confirms it or declines with a mandatory reason** (operational addition, 2026-09-22 — see `02_USER_FLOWS.md` §3's "Driver Confirmation" note; not literal SRS §11 text, but a real need distinct from ride-hailing-style job shopping — a decline routes back to Daniel's Dispatch Queue for reassignment, never a driver-to-driver handoff). | SRS §15 implies this was previously a verbal/paper assignment with no single source of truth the driver could check themselves. |
| 2. Pre-trip inspection | Completes a vehicle inspection checklist before departure. | Without a structured checklist, a pre-trip inspection is easy to skip or do superficially — exactly the gap BR-004 (grounded vehicles) and the dispatch gate (BR-001–005) exist to catch, but only if the inspection actually happens and is recorded. |
| 3. Start trip | Accepts/starts the trip, capturing starting odometer. | SRS §5.5 requires this for distance calculation — a driver-side gap here breaks the whole trip/fuel-efficiency chain downstream. |
| 4. During trip | Fuel stops (capture fuel info), possible breakdown/accident reporting with photo upload. | SRS §11 names "report breakdowns and accidents" and "upload photos/documents" as explicit driver-side functions — implies this was previously a delayed phone-call report with no photo evidence at the time. |
| 5. End trip | Ends the trip, capturing ending odometer. | Same distance-calculation dependency as stage 3. |

**Design Implication:** This is the one Wave 2 role the SRS itself explicitly separates from the web dashboard architecture (§11: "Mobile Application," offline-first per the architecture summary's PWA rationale for low-connectivity rural sub-counties). It should NOT be designed as a scaled-down web screen — it needs its own mobile-first flow, likely the single most different design problem of all 16 roles (offline capability, camera/photo capture, large touch targets for in-vehicle use). Not yet specced; would warrant its own blueprint section distinct from the desktop-oriented `04_FIGMA_SCREEN_BLUEPRINT.md` frames.

## 9. Mechanic / Technician

**SRS Role:** Mechanic (§4: "Repair/service activities") — distinct from the Workshop Manager (Peter): the person executing the repair, not managing the board.
**Goals & Motivations:** Complete an assigned repair job efficiently, with the parts they need available when they need them, and a clear record of what was done.
**Journey — per-job-card execution, the "doing" counterpart to Peter's "managing":**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Receive assignment | Gets assigned a job card by the Workshop Manager. | Covered by Peter's Kanban board (`04_FIGMA_SCREEN_BLUEPRINT.md` §4) from the manager's side — no mechanic-facing view of "my assigned jobs" specifically. |
| 2. Diagnose & request parts | Diagnoses the issue, requests spare parts against the work order. | SRS §5.11 requiring parts "linked to maintenance work orders" — from the mechanic's side, this means knowing what's in stock before promising a timeline, same friction already identified for Peter but experienced first-hand here. |
| 3. Perform repair | Does the actual repair work, logs labour/time. | No distinct friction beyond the general paper-to-system shift (SRS §15). |
| 4. Submit for QA | Hands off to quality inspection (Peter's gate, `02_USER_FLOWS.md` §4). | — |

**Design Implication:** Likely a filtered, "my jobs only" view of Peter's Kanban board (Component 5) rather than a wholly separate screen — the underlying data model and states are identical, just scoped to one mechanic's assignments. Not yet specced as its own frame.

## 10. Fuel Officer

**SRS Role:** Fuel Officer (§4: "Fuel transactions").
**Goals & Motivations:** Log fuel transactions accurately and catch anomalies at the point of transaction, before they become Miriam's reconciliation problem downstream.
**Journey — per-transaction, front-line to the fraud-prevention framework:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Log a fuel transaction | Records vehicle, driver, quantity, cost, odometer, payment method (SRS §5.8). | SRS §15's manual-register starting state implies this was previously a paper voucher system. |
| 2. System validates | The system checks tank capacity, duplicate-transaction window, odometer monotonicity (architecture summary §6.1). | If a check fails, no stated UI treatment for how the Fuel Officer sees or resolves it at the point of entry — right now this flows to Miriam's anomaly queue (FRAME-05) after the fact, not necessarily to the Fuel Officer in the moment. |
| 3. Manage station quotas | Reconciles fuel card/voucher usage against station-level quotas. | SRS role description ("Fuel Vouchers, Reconciliation, Station Quotas," architecture summary §3) implies a quota-tracking responsibility not detailed further in the functional requirements. |

**Design Implication:** The fuel anomaly detection flow (`02_USER_FLOWS.md` §5) currently only specs the system-side checks and Miriam's downstream review — it doesn't spec what the Fuel Officer sees at the moment of transaction entry if a check fails immediately (e.g. tank-capacity exceeded, caught before the transaction even completes). Worth revisiting `02_USER_FLOWS.md` §5 to add the Fuel Officer's own point-of-entry experience, not just the downstream review. Not yet specced as a screen.

## 11. Storekeeper

**SRS Role:** Storekeeper (§4: "Spare parts").
**Goals & Motivations:** Keep spare parts inventory accurate and available — issue parts against valid work orders, reorder before running out, avoid both stockouts (blocking Peter's repairs) and overstock (wasted budget).
**Journey — inventory-management cycle:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Receive stock | Logs incoming parts against supplier/purchase order (SRS §5.11). | — |
| 2. Issue parts | Issues parts against a specific maintenance work order (the same link Peter and the Mechanic depend on). | This is the supply side of the exact gap already identified in Peter's and the Mechanic's personas — parts need to show as available/issued in real time for the Kanban stock-status pill (`03_MASTER_DESIGN_SYSTEM.md` Component 5) to be trustworthy. |
| 3. Monitor reorder levels | Tracks stock against configured reorder thresholds. | SRS §5.11 names "reorder levels" as tracked data — implies a threshold-crossing alert should exist, not yet specced anywhere. |

**Design Implication:** This role is the missing upstream half of the parts-visibility problem already identified in Peter's and the Mechanic's journeys — the Kanban board's stock-status pill (In Stock/Backordered/Requested) is only as accurate as the Storekeeper's own inventory screen feeding it. A Data Table (Component 6) view scoped to parts inventory, plus a reorder-alert list (structurally similar to Grace's Needs Attention, Component 3C), is the likely shape — not yet specced as a screen.

## 12. Finance-Adjacent: Procurement Officer

**SRS Role:** Procurement Officer (§4: "Acquisition/contracts").
**Goals & Motivations:** Manage vehicle/parts acquisition and supplier contracts in compliance with county procurement rules (PPADA, per the architecture summary §1.1) — a different compliance regime from Miriam's IFMIS/financial focus, though both are Finance-adjacent.
**Journey — acquisition-cycle-driven, infrequent relative to daily operational roles:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Plan procurement | Records approved fleet requirements, procurement reference (SRS §5.2). | — |
| 2. Manage the acquisition | Tracks supplier, purchase/contract information, delivery inspection (SRS §5.2, §5.21 Procurement Integration). | SRS §5.21 requiring integration with "county procurement systems" implies this was previously managed entirely outside CVFMS, in a disconnected system — this role's biggest friction is likely the two-system reconciliation problem, similar in shape to Miriam's IFMIS friction but for procurement specifically. |
| 3. Hand off to registry | Once acquired, the vehicle needs to enter Grace's Fleet Registry as a new asset. | No explicit handoff mechanism named between procurement completion and registry creation — a manual re-entry risk. |

**Design Implication:** Likely needs its own acquisition-tracking view distinct from both Grace's registry and Miriam's cost dashboard, with a clear "acquisition complete → create registry record" handoff action to close the gap identified above. Not yet specced as a screen.

## 13. HR Officer

**SRS Role:** HR Officer (§4: "Driver employment information").
**Goals & Motivations:** Keep driver employment/licensing data current so operational systems (dispatch gate BR-002/BR-003, Driver Management §5.7) always check against accurate status — an HR Officer's data-entry lag directly causes a Transport Officer's dispatch-gate failure downstream.
**Journey — employment-lifecycle-driven:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Onboard a driver | Enters employee number, licence details, employment status (SRS §5.7, §5.22 HR Integration). | SRS §5.22 requiring HR Integration ("staff number, department, designation, employment status, driver status, transfer and exit") implies this data currently lives in a separate HR system with no live sync — a driver's status could be stale in CVFMS if HR updates lag. |
| 2. Update status | Records a transfer, licence renewal, or exit. | Same integration-lag risk — this is the exact data BR-002 ("driver active & employed") and BR-003 ("licence valid") depend on at dispatch time (`02_USER_FLOWS.md` §3). |
| 3. Respond to a compliance alert | SRS §5.7 requires the system to "generate compliance alerts" for driver licensing/fitness issues. | No stated routing for who receives this alert — presumably HR, but not explicit. |

**Design Implication:** This role's data is load-bearing for Daniel's entire dispatch-gate flow (BR-002, BR-003) — a real, direct dependency between two personas' work that's currently implicit. Worth flagging in `02_USER_FLOWS.md` §3 as a named upstream dependency, not just assuming driver data is always current. Not yet specced as a screen.

## 14. Auditor

**SRS Role:** Auditor (§4: "Read-only audit access").
**Goals & Motivations:** Verify that the system's own controls (BR-001–010, the maker-checker workflow, the immutable audit trail) actually held — this role exists specifically because of the SRS's PFM Act/PPADA compliance mandate (architecture summary §1.1), not as an operational convenience.
**Journey — periodic review, adversarial-by-design (per Miriam's persona, which already treats Audit as a standing check):**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Select a scope | Chooses a time period, department, or transaction type to review. | — |
| 2. Review the audit trail | Examines the immutable log (SRS §8: user, role, timestamp, previous/new value, approval/rejection). | SRS §8 requiring the trail to capture "permitted technical metadata" and be genuinely immutable implies this is the one screen in the system that must never allow edits, only ever display — a hard, binding constraint unlike any other role's screen. |
| 3. Flag an exception | Finds something questionable (an override without adequate justification, an anomaly Miriam already flagged). | No stated escalation mechanism from Auditor back to operational roles — presumably outside the system (a formal audit finding process), not a CVFMS workflow. |

**Design Implication:** A read-only Data Table (Component 6) view of the audit log, with the same filter/search affordances as any other table, but with every write-affordance (edit, override, action buttons) structurally absent, not just disabled — this is a genuinely different design constraint from every other role's screen, where actions are the whole point. Not yet specced as a screen.

## 15. Department User

**SRS Role:** Department User (§4: "Vehicle requests") — the actual requester who initiates the workflow Daniel (Transport Officer) later processes.
**Goals & Motivations:** Get a vehicle for an official journey with minimum friction — submit a request, know its status, don't have to chase people for updates.
**Journey — the very first stage of the flow `02_USER_FLOWS.md` §3 already documents from Daniel's side:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Submit a request | Fills in requester, department, purpose, destination, date/time, passengers, special requirements (SRS §5.4). | SRS §15's manual-register baseline implies this was previously a paper form with no status visibility once submitted. |
| 2. Wait for approval | The request goes to Supervisor Approval, then Transport Review (SRS §5.4's stated workflow). | No stated visibility into where the request currently sits in that multi-step workflow — the Department User likely has no way to check status themselves today. |
| 3. Learn the outcome | Request is approved and dispatched, or rejected/returned for correction. | If rejected, SRS gives no stated mechanism for how the Department User learns why or what to fix. |

**Design Implication:** A simple request-submission form plus a personal "my requests" status view (a scoped, single-user version of Daniel's queue table, showing only their own requests and current stage) is the direct design match — this closes the same "no visibility into a multi-step workflow" gap already identified from Daniel's and Miriam's sides, just at the point of origin. Not yet specced as a screen.

## 16. Approving Officer

**SRS Role:** Approving Officer (§4: "Workflow approvals") — the "Supervisor Approval" step named explicitly in SRS §5.4's workflow, upstream of Daniel's Transport Review stage.
**Goals & Motivations:** Approve or reject a subordinate's vehicle request quickly and appropriately — this is a maker-checker control point (SRS §24), not a rubber stamp, so the design needs to make skipping real review as hard as possible.
**Journey — per-request, likely high-frequency for a busy department:**

| Stage | What they do | Friction point today |
| :--- | :--- | :--- |
| 1. Receive a request | A Department User's request lands for their approval. | No stated notification mechanism at this specific stage, though SRS §5.23 (Notification and Alert Management) implies one should exist system-wide. |
| 2. Review & decide | Approves, rejects, or returns for correction (SRS §5.24: "delegation, escalation, rejection, return for correction"). | — |
| 3. Delegate if unavailable | SRS §5.24 explicitly supports delegation — implying this role is sometimes unavailable and the workflow shouldn't stall waiting for them. | No stated UI for setting up a delegate — purely a backend workflow capability as far as the SRS states it. |

**Design Implication:** A lightweight approval queue — likely the simplest of all 16 roles' screens, since the decision itself (approve/reject/return) is a single-item action, not a triage or reconciliation task. Could reuse the True-Drawer decision pattern (`09_PATTERN_LIBRARY.md` §2) almost directly. Not yet specced as a screen.

---

## Persona Comparison Matrix

| Persona | SRS Role | Journey Shape | Frequency | Primary Friction Stage | Primary Risk if UX Fails |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grace (Fleet Manager) | Fleet Manager | Recurring loop (spot → decide → act → confirm) | Daily, continuous | Decide/act (stages 3-4) | Compliance lapse or breakdown goes unnoticed until it's costly |
| Daniel (Transport Officer) | Transport Officer | Linear, per-request | Daily, high-volume | Gate check (stage 3) | Unauthorized dispatch, unrecorded override, audit finding |
| Peter (Workshop Manager) | Workshop Manager | Linear with re-entrant state | Daily, floor-based | Parts visibility + QA gate (stages 2, 4) | Untracked repair cost, part shortage discovered too late |
| Sarah (Executive) | County Executive | Infrequent, periodic | Weekly/monthly | Trend + drill (stages 2-3) | Wrong or unreconciled figures cited publicly |
| Miriam (Finance Officer) | Finance Officer | Recurring monthly cycle | Daily/monthly close | Reconcile + anomaly review (stages 2-3) | Missed fraud/anomaly, audit exception |
| System Administrator | System Administrator | Infrequent setup, occasional adjustment | Rare, high-impact | Diagnose misconfiguration (stage 3) | Config error silently breaks another role's workflow |
| Fleet Officer | Fleet Officer | Station-based, event-driven | Daily, field-based | Record accuracy at point of event (stage 2) | Registry drifts from physical fleet reality |
| Driver | Driver | Per-trip, mobile-first | Daily, high-volume | Pre-trip inspection completion (stage 2) | Grounded vehicle dispatched, undocumented breakdown/accident |
| Mechanic | Mechanic | Per-job-card execution | Daily, floor-based | Parts availability at diagnosis (stage 2) | Repair delay, mis-recorded work |
| Fuel Officer | Fuel Officer | Per-transaction | Daily, high-volume | Anomaly at point of entry (stage 2) | Undetected fraud until Miriam's downstream review |
| Storekeeper | Storekeeper | Inventory-management cycle | Daily/ongoing | Reorder-threshold tracking (stage 3) | Stockout blocks repairs, or silent overstock waste |
| Procurement Officer | Procurement Officer | Acquisition-cycle-driven | Infrequent, per-acquisition | Two-system reconciliation (stage 2) | Compliance breach (PPADA), untracked asset handoff to registry |
| HR Officer | HR Officer | Employment-lifecycle-driven | Occasional, per-event | HR-to-CVFMS data lag (stages 1-2) | Stale driver status causes false dispatch-gate pass |
| Auditor | Auditor | Periodic review, adversarial-by-design | Periodic (audit cycles) | Read-only trail must be genuinely immutable (stage 2) | Compliance/audit finding, undetected control failure |
| Department User | Department User | Linear, request-and-wait | Occasional, per-need | Status visibility during approval (stage 2) | Requester frustration, duplicate/off-system requests |
| Approving Officer | Approving Officer | Per-request, single decision | Daily, high-frequency | Timely review without rubber-stamping (stage 2) | Skipped review defeats maker-checker control |

---

## Notes on Method

This revision changed the organizing frame (goals → journey stages → friction points → design implication) to explicitly match `ui-ux-expert`'s stated user-centered design approach, rather than the flatter "responsibilities / pain points" structure used in v2.0 (still in `docs/archive/`, and itself already an SRS-grounded rewrite of the original v1.x doc). The underlying facts — which 5 roles, what each does, what SRS section backs each claim — are unchanged, because they are fixed by the SRS (a requirements document) and not something a design-methodology skill has any basis to alter. What changed is that each persona is now explicitly a mapped journey with named friction points and a design implication drawn from where the friction concentrates, rather than an unordered list of pain points — this makes the link from "what's wrong today" to "what FRAME-0X does about it" traceable stage-by-stage instead of asserted.
