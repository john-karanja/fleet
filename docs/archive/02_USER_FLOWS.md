# CVFMS Core User Flows & State Logic

**Document ID:** `DOC-CVFMS-002`
**Source:** SRS Section 5 (Functional Requirements), Section 18 (Business Rules), Section 26 (Recommended County Fleet Operating Workflow)

---

## 1. Master Vehicle Lifecycle State Machine (SRS 5.1)

```
[Awaiting Delivery] → [Active/Available] ⇄ [Assigned] ⇄ [On Trip]
                              │                              │
                              ├──────────► [Under Maintenance] ◄──┘
                              │
                              ├──────────► [Grounded] (fails a dispatch gate)
                              │
                              ├──────────► [Accident] → [Under Maintenance] or [Awaiting Disposal]
                              │
                              └──────────► [Impounded] / [Lost/Stolen]

[Awaiting Disposal] → [Disposed] / [Written Off]   (terminal — BR-010: no longer allocatable)
```

Every transition is written to the immutable audit log (SRS Section 8): user, role, timestamp, previous state, new state.

---

## 2. Fleet Manager Monitor-to-Action Flow (Grace's primary flow)

*Added after correcting an earlier draft that scoped Grace as monitor-only — see correction note in `01_USER_PERSONAS.md`. Her flow is not a single linear procedure like Daniel's or Peter's; it is a hub-and-spoke pattern: she starts every session on one screen and branches into one of four actions depending on what the dashboard surfaces, then returns.*

*Note on scope: the Fleet Command Dashboard's documented job is exactly the four things in the box below (KPI row / status board / compliance countdown / utilization gap alert) — an aggregation/triage task. A live GPS map (SRS 5.16, Phase 5: Digital Intelligence) is a spatial/exploration task and deliberately does NOT live inside this box: mixing an aggregation screen with an exploration tool weakens both, and a map small enough to fit alongside 4 other sections would be too small to be useful. Resolution: the Fleet page carries two in-page tabs — "Overview" (this dashboard, the default landing tab) and "Live Map" (a full-screen map view, one click away, not nested deeper in the nav). See `04_FIGMA_SCREEN_BLUEPRINT.md` FRAME-06 for the map's own spec.*

```
                              ┌─────────────────────────────┐
                              │ Fleet Command Dashboard      │  (landing screen, every session —
                              │ [Overview] [Live Map] tabs   │   "Overview" tab selected by default)
                              │  KPI row / status board /    │
                              │  compliance countdown /      │
                              │  utilization gap alert       │
                              └───────────────┬───────────────┘
                                               │
              ┌────────────────┬──────────────┼──────────────┬────────────────┐
              ▼                ▼              ▼              ▼                ▼
    ┌──────────────────┐ ┌──────────┐ ┌───────────────┐ ┌────────────┐ ┌─────────────┐
    │ A. Registry Edit  │ │ B. Real- │ │ C. Dispatch    │ │ D. Mainten-│ │ (no action   │
    │ (5.1)             │ │ locate   │ │ Override (5.6) │ │ ance       │ │ needed —     │
    │                   │ │ Idle     │ │                │ │ Approval   │ │ dashboard    │
    │ Click a vehicle    │ │ Vehicle  │ │ Daniel escal-  │ │ (5.9)      │ │ closed)      │
    │ row → edit master  │ │ (5.3,    │ │ ates a blocked │ │            │ │              │
    │ record (status,    │ │ 5.17)    │ │ dispatch she   │ │ Reviews a  │ │              │
    │ station, custodian)│ │          │ │ cannot clear   │ │ pending    │ │              │
    │ → save → audit log │ │ Click the│ │ herself →      │ │ maintenance│ │              │
    │                    │ │ Utiliz-  │ │ reviews the    │ │ cost/sched-│ │              │
    │                    │ │ ation Gap│ │ same 5-row gate│ │ ule request│ │              │
    │                    │ │ banner → │ │ checklist →    │ │ → approve/ │ │              │
    │                    │ │ assign   │ │ enters mandat- │ │ reject with│ │              │
    │                    │ │ idle     │ │ ory justific-  │ │ comment    │ │              │
    │                    │ │ vehicle  │ │ ation →        │ │            │ │              │
    │                    │ │ to a     │ │ authorizes     │ │            │ │              │
    │                    │ │ pending  │ │ override       │ │            │ │              │
    │                    │ │ request  │ │ (logged)       │ │            │ │              │
    └────────┬──────────┘ └────┬─────┘ └───────┬────────┘ └─────┬──────┘ └──────────────┘
             │                 │               │                │
             └─────────────────┴───────────────┴────────────────┘
                                       │
                                       ▼
                          Return to Fleet Command Dashboard
                          (state reflects the action just taken)
```

**Design implication:** Grace's dashboard is not read-only. Every panel that surfaces a finding — a status board row, the compliance countdown, the utilization gap banner — needs an entry point into the matching action (edit, reallocate, override, approve), not just a passive display or a link that hands off to someone else's screen. The override path (C) reuses the same 5-row Dispatch Gate Checklist component Daniel sees (Component 4), since she is reviewing the identical gate — the only difference is she is the one authorized to override it and Daniel escalates to her instead of resolving it himself.

---

## 3. End-to-End Requisition → Dispatch → Trip Flow (Daniel's primary flow)

This is the CVFMS equivalent of el-nino's 90-second triage loop — the single flow every dispatch screen must optimize for.

```
1. Department User submits Vehicle Request
   (requester, department, purpose, destination, date/time, expected return, passengers, vehicle type preference)
        │
        ▼
2. Supervisor Approval  ──────► [Reject] → returned to requester with reason (recoverable, not a dead end)
        │ (Approve)
        ▼
3. Transport Review & Vehicle Allocation
   (Transport Officer selects candidate vehicle + driver)
        │
        ▼
4. MANDATORY DISPATCH GATE (BR-001 to BR-005) — evaluated automatically, shown as pass/fail before dispatch is even attempted
   ┌────────────────────────────────────────────────────────┐
   │ ✓ / ✗  Insurance valid (not expired)                    │
   │ ✓ / ✗  Driver active & employed                         │
   │ ✓ / ✗  Driver licence valid (not expired)               │
   │ ✓ / ✗  Vehicle not grounded / in maintenance            │
   │ ✓ / ✗  Approved request linked                          │
   └────────────────────────────────────────────────────────┘
        │
        ├── All pass ──────────────────────► 5. Dispatch Authorized
        │
        └── Any fail ──► [Blocked] ──► Authorized Executive Override
                                        (mandatory justification field, logged to audit trail)
                                        │
                                        └──► 5. Dispatch Authorized (flagged as override)
        ▼
6. Trip Initiated
   (starting odometer captured, driver + vehicle + passengers locked to trip record)
        │
        ▼
7. Utilization Phase
   (fuel transactions logged against trip, GPS breadcrumbs recorded if device fitted)
        │
        ▼
8. Trip Closure
   (ending odometer captured — must be ≥ starting odometer per BR-007 —
    distance auto-calculated, trip marked COMPLETED)
```

**Design implication:** The dispatch gate must never be a silent validation — every gate row is visible with its pass/fail state before the Transport Officer can act, per Postel's Law ("prevent errors proactively") and to give Daniel confidence he isn't one click from an audit finding.

---

## 4. Workshop Job Card Flow (Peter's primary flow)

```
[Defect Reported / PM Due] → [Job Card Created]
        │
        ▼
[Diagnosis] ──► Parts identified ──► [Spare Parts Requisition]
        │                                    │
        │                          ┌─────────┴─────────┐
        │                          │ In stock: issued   │ Out of stock: reorder
        │                          └─────────┬─────────┘
        ▼                                    ▼
[In Repair] (mechanic assigned, labour tracked) ◄──── parts arrive
        │
        ▼
[Quality Inspection] ──► Fails checklist ──► back to [In Repair]
        │ Passes
        ▼
[Vehicle Release Authorized] ──► Vehicle status returns to [Active/Available]
        │
        ▼
[Maintenance History Updated] (cost, parts consumed, labour, warranty status)
```

**Design implication:** Release must be gated behind a completed QA checklist — a single "Release" button with no structured checklist behind it recreates the rubber-stamp problem Peter already has on paper.

---

## 5. Fuel Transaction & Anomaly Flow (feeds Miriam's reconciliation queue)

```
[Fuel Transaction Logged]
   (vehicle, driver, trip, station, quantity, price/litre, odometer, payment method)
        │
        ▼
Automated checks:
   • Quantity ≤ tank capacity × 1.05          → else: ANOMALY (over-capacity)
   • No duplicate within 4hr window           → else: ANOMALY (duplicate/rapid refuel)
   • Efficiency within ±25% of class baseline → else: ANOMALY (consumption outlier)
   • Linked to an active trip/reference       → else: BLOCKED (ghost trip prevention, BR-006)
        │
        ├── Clean ──► Posted to Fuel Ledger ──► available for Finance reconciliation
        │
        └── Anomaly ──► Flagged, routed to Finance Officer's Anomaly Review Queue
                         (not silently logged — someone must clear or escalate it)
```

---

## 6. Persona-to-Flow Ownership Map

| Flow | Primary Owner | Screen(s) |
| :--- | :--- | :--- |
| Monitor-to-action (registry edit, reallocation, dispatch override, maintenance approval) | Grace (Fleet Manager) | Fleet Command Dashboard + action surfaces (registry edit, override checklist, approval panel — not yet built as separate screens, see note below) |
| Requisition → Dispatch Gate → Trip | Daniel (Transport Officer) | Dispatch & Requisition Queue |
| Job Card → QA → Release | Peter (Workshop Manager) | Workshop Job Card Board |
| Executive KPI review | Sarah (Executive) | Executive Briefing Dashboard |
| Fuel/cost reconciliation & anomaly review | Miriam (Finance Officer) | Finance & Cost Dashboard |

Grace's dashboard is still the aggregation point where every other persona's flow becomes visible as a state change — that part of the original description was correct. What was wrong was treating her as having no actions of her own. **Open item:** FRAME-01 as built only covers her monitoring view; the four action surfaces in her flow (§2 above: Registry Edit, Reallocate Idle Vehicle, Dispatch Override, Maintenance Approval) are not yet designed as screens/modals. These should be scoped and built before Grace's persona is considered complete — likely as modals/drawers launched from the dashboard rather than full new frames, to preserve the "act without leaving her workspace" principle from her Success Looks Like statement.
