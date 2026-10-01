# CVFMS User Personas

**Document ID:** `DOC-CVFMS-001`
**Source:** SRS Section 3 (Stakeholders) & Section 4 (User Roles and Access Control)
**Scope:** Of the 16 SRS-defined roles, this first design wave covers 5 flagship personas spanning operations, maintenance, executive oversight, and finance. Remaining roles (System Administrator, Mechanic, Storekeeper, HR Officer, Auditor, Department User, Approving Officer, Procurement Officer, Driver) are deferred to later waves — their screens should reuse the component library and tokens defined here.

---

## 1. Grace Wanjiru — County Fleet Manager (Flagship Persona)

**Role & Location:** Overall fleet management, County Transport Directorate HQ.
**Primary Device & Hardware:** Dual-monitor office desktop, wired LAN, standard 9am–5pm shift with occasional after-hours alert response.
**Core Goal & Mental Model:** Know the real-time state of every vehicle in the fleet at a glance — what's available, what's on trip, what's grounded and why — and intervene before small problems (an expiring insurance policy, an overdue service) become compliance failures or breakdowns.

**Responsibilities (SRS 5.1, 5.3, 5.6, 5.9, 5.17) — corrected scope:** Grace is not a passive monitor. She holds real write authority:
- **Fleet Registry (5.1):** creates and edits vehicle master records — registration, VIN, engine number, status changes.
- **Vehicle Allocation (5.3):** assigns vehicles to departments, directorates, sub-counties, and stations — an action she performs, not just reviews.
- **Dispatch Override Authority (5.6):** the SRS calls out an "authorized executive override" for blocked dispatches (BR-001–005) — Grace, as the senior fleet role above Daniel (Transport Officer), is the plausible holder of that override authority for exceptions Daniel cannot clear himself.
- **Maintenance Approval (5.9):** approves maintenance scheduling and cost oversight, not just watches counters tick down.
- **Utilization Management (5.17):** reviews utilization metrics and acts on idle-asset findings — e.g. reallocating an idle vehicle to a pending request herself.

*Correction note: an earlier version of this document compressed Grace into a pure "aggregation point / monitor-only" persona whose only screen was the dashboard. That was a simplification made for the sake of a dramatic flagship screen, not something grounded in the SRS. The SRS gives her real allocation, registry-edit, override, and approval functions — her journey below reflects that.*

**Pain Points:**
- Vehicle status is scattered across spreadsheets and phone calls from station custodians.
- Finds out about lapsed insurance or overdue inspection only when a vehicle is already stopped at a roadblock.
- No single view of which vehicles are sitting idle while requests pile up elsewhere.
- Has to leave her monitoring view and hunt for a separate tool every time she needs to actually reallocate a vehicle, edit a registry record, or approve a maintenance override.

**Success Looks Like:** A cockpit screen where fleet-wide status, compliance countdowns, and utilization gaps are visible without switching tabs — and where every finding has a direct path to the action she's authorized to take (reallocate, edit, override, approve) without leaving her own workspace for someone else's screen.

---

## 2. Daniel Otieno — Transport Officer

**Role & Location:** Requisitions, allocation and dispatch; Transport Directorate front office.
**Primary Device & Hardware:** Single-monitor desktop, shared office with 3 other transport officers, phone line for urgent requests.
**Core Goal & Mental Model:** Move a vehicle request from "submitted" to "dispatched" as fast as possible without breaking a mandatory gate (BR-001 to BR-005) — insurance, driver licensing, roadworthiness, grounded status, linked request.

**Responsibilities (SRS 5.4, 5.5, 5.6):** Reviewing incoming requisitions, allocating vehicles and drivers, running dispatch gate checks, authorizing override with justification when an executive needs an exception.

**Pain Points:**
- Approving a request only to discover at dispatch that the assigned vehicle's insurance lapsed yesterday.
- No queue view — requests arrive by email/paper and get triaged manually by memory.
- Overrides happen verbally with no audit trail, which Internal Audit flags every quarter.

**Success Looks Like:** A prioritized requisition queue where every gate check (insurance/license/roadworthiness/grounded/linked-request) is pre-validated and visibly pass/fail before he can even attempt dispatch, with overrides forced through a justification field that's automatically logged.

---

## 3. Peter Mwangi — Workshop Manager

**Role & Location:** Maintenance and workshop operations, County Central Workshop.
**Primary Device & Hardware:** Workshop-floor terminal (shared, often standing use) plus office desktop for reporting; frequently interrupted by mechanics needing sign-off.
**Core Goal & Mental Model:** Keep the job-card board moving — know which vehicles are waiting for diagnosis, which are mid-repair, which are ready for quality sign-off and release — without losing track of parts requested against each job.

**Responsibilities (SRS 5.9, 5.10, 5.11, 5.12):** Preventive/corrective maintenance scheduling, job card creation and mechanic assignment, spare parts requisition against work orders, quality inspection, vehicle release authorization, tyre lifecycle tracking.

**Pain Points:**
- Job cards live on paper clipboards; a vehicle's repair history is only as good as whoever remembered to file the card.
- No visibility into whether a requested spare part is even in stock before promising a completion date.
- Quality sign-off is a rubber stamp because there's no structured checklist forcing verification before release.

**Success Looks Like:** A kanban-style work order board (Diagnosis → In Repair → Awaiting Parts → QA → Ready for Release) where every card shows assigned mechanic, linked parts requests with stock status, and a mandatory QA checklist before the release button unlocks.

---

## 4. Hon. Sarah Kiptoo — County Executive (CECM for Transport)

**Role & Location:** County Executive Committee Member oversight; County Government HQ, infrequent system use (weekly/monthly cadence, not daily).
**Primary Device & Hardware:** Laptop, often reviewing dashboards during cabinet or budget review meetings; sometimes projected on a screen for a room.
**Core Goal & Mental Model:** Answer "is the fleet costing us too much, and is it available when departments need it" in under a minute, with defensible numbers she can cite in a budget hearing or to the media.

**Responsibilities (SRS Section 6, Executive Dashboard):** Strategic oversight of fleet size, availability rate, expenditure, utilization benchmarks, accident/liability exposure — no transactional actions.

**Pain Points:**
- Numbers she's given verbally by the Fleet Manager don't match what Finance reports at the same cabinet meeting.
- No trend view — she only ever sees a point-in-time snapshot, so she can't tell if a cost spike is new or seasonal.
- Can't drill from a headline number ("KES 4.2M fuel spend") down to which department is driving it.

**Success Looks Like:** An executive dashboard with a small number of large, unambiguous KPI tiles (availability %, total expenditure vs budget, utilization, accident summary), each with a trend sparkline and one level of drill-down, and nothing she could act on directly — this is a read-only briefing view.

---

## 5. Miriam Chebet — Finance Officer

**Role & Location:** Fleet cost centers and IFMIS reconciliation; County Treasury / Finance Directorate.
**Primary Device & Hardware:** Office desktop, dual monitor (one for CVFMS, one for IFMIS), works against month-end and quarter-end close deadlines.
**Core Goal & Mental Model:** Reconcile every shilling of fleet expenditure — fuel, maintenance, insurance — against budget and department cost centers before month-end close, and flag anomalies (BR-006 to BR-010) before they become audit findings.

**Responsibilities (SRS 5.18, 5.20, Section 6 Finance Dashboard):** Budget vs. actual tracking by department/cost center, fuel and maintenance expenditure reconciliation, workshop invoice approval, IFMIS payment sync.

**Pain Points:**
- Reconciling fuel card statements against CVFMS trip records is a manual line-by-line exercise every month.
- Anomaly flags (duplicate fueling, excess quantity) are buried in operational logs she doesn't normally see until Audit asks about them.
- Budget vs. actual by department is assembled in a spreadsheet stitched from three exports.

**Success Looks Like:** A cost dashboard with budget-vs-actual by department/cost-center as the primary view, a dedicated anomaly review queue (already flagged by the system, not self-discovered), and one-click export to formats Audit and IFMIS both accept.

---

## Persona Comparison Matrix

| Persona | Frequency | Screen Density | Primary Verb | Primary Risk if UX Fails |
| :--- | :--- | :--- | :--- | :--- |
| Grace (Fleet Manager) | Daily, continuous | Very high (cockpit) | Monitor & intervene | Vehicle breakdown/compliance lapse goes unnoticed |
| Daniel (Transport Officer) | Daily, high-volume | High (queue) | Approve & dispatch | Unauthorized dispatch, audit finding |
| Peter (Workshop Manager) | Daily, floor-based | High (board) | Track & release | Repair delay, untracked parts cost |
| Sarah (Executive) | Weekly/monthly | Low (briefing) | Review & decide | Wrong numbers cited publicly |
| Miriam (Finance Officer) | Daily/monthly close | High (reconciliation) | Reconcile & flag | Missed fraud, audit exception |
