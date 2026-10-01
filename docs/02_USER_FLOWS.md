# CVFMS User Flows

**Document ID:** `DOC-CVFMS-002`
**Revision:** 2.1 — flows below now correspond directly to the journey stages mapped in `01_USER_PERSONAS.md` v2.1 (per the `ui-ux-expert` skill's journey-mapping method) rather than standing as separate state-machine diagrams. Each flow's state transitions and gates are unchanged from v2.0, since they are fixed by SRS functional requirements and business rules (§5, §18, §23), not by design methodology — what changed is that each flow section below now names which persona journey stage it corresponds to and which friction point it resolves, closing the loop from "friction identified" (doc 01) to "flow designed to fix it" (this doc).
**Depends on:** `01_USER_PERSONAS.md` (roles and journey stages), `03_MASTER_DESIGN_SYSTEM.md` (component vocabulary referenced below).

---

## 1. Vehicle Lifecycle State Machine

Directly from SRS §5.1 (status enum) and §2 (lifecycle phases: Planning → Acquisition → Registration → Allocation → Dispatch → Utilization → Fuel → Maintenance → Insurance/Compliance → Accident Management → Monitoring → Valuation → Disposal).

```
Awaiting Registration → Active → Assigned → On Trip → Active (loop)
                           │         │
                           │         └──→ Grounded (safety/compliance fail) → Under Maintenance → Active
                           │
                           ├──→ Under Maintenance → Active
                           ├──→ Accident → (Under Maintenance | Grounded | Awaiting Disposal)
                           ├──→ Impounded → (Active | Awaiting Disposal)
                           ├──→ Lost/Stolen → Written Off
                           └──→ Awaiting Disposal → Disposed | Written Off
```

Every non-Active status (Grounded, Under Maintenance, Accident, Impounded) requires a `status_reason_code` (schema addition, §5 below) — a vehicle cannot sit in a blocked state with no recorded reason, since BR-004 depends on the system knowing *why* a vehicle is grounded to gate dispatch correctly.

---

## 2. Grace's Flow — Monitor-to-Action Hub

**Corresponds to:** `01_USER_PERSONAS.md` §1 journey stages 3-4 (Decide the action → Take the action) — the stages flagged there as the dominant friction point (finding a problem without a direct path to fixing it).

Grace's SRS-defined dashboard content (§6, §7.1) is inherently a hub-and-spoke pattern: one aggregation view, several write-authorized destinations.

```
[Overview Dashboard]
   │
   ├─ Needs Attention row → [Action Drawer: Reallocate]       (SRS §5.3)
   ├─ Needs Attention row → [Action Drawer: Registry Edit]    (SRS §5.1)
   ├─ Needs Attention row → [Action Drawer: Dispatch Override](SRS §5.6, BR-001–005)
   ├─ Needs Attention row → [Action Drawer: Maintenance Approval] (SRS §5.9)
   └─ "All Vehicles →"    → [Fleet Registry Data Table]        (SRS §5.1, full list)
```

Every drawer, on confirm, writes to the audit trail (SRS §8, BR-009) and returns to the Overview with a Confirmation Toast (Component 4B) — the loop always closes back to the hub, never stranding Grace on a sub-screen.

**Why the live map is a separate destination, not part of Overview:** SRS §5.16/§6 treats GPS/telematics as real-time spatial monitoring (breadcrumb history, geofencing, speed violations) — a fundamentally different cognitive task from Overview's aggregation/triage job. The architecture summary's own phasing (§8: GPS/Telematics is Phase 5, after Foundation/Operations/Cost/Compliance) reinforces that this is a distinct, later-maturity capability, not a widget bolted onto day-one triage. Conflating the two would force Overview to compete for space with a spatial exploration tool that has entirely different interaction patterns (pan/zoom vs. scan/click).

---

## 3. Daniel's Flow — Requisition → Dispatch Gate → Trip

**Corresponds to:** `01_USER_PERSONAS.md` §2 journey stage 3 (Gate check) — the stage flagged there as the dominant friction point (a gate check historically discovered as a failure only after commitment, not verified before).

Directly from SRS §5.4's stated workflow, expanded with the mandatory dispatch gate from §5.6 and BR-001–BR-005.

```
[Vehicle Request submitted by Department User]
        │
        ▼
[Supervisor Approval] ──(Reject)──► [Returned to Requester]
        │ (Approve)
        ▼
[Transport Review & Allocation] ← Daniel's queue starts here
        │
        ▼
[Vehicle + Driver Assignment]
        │
        ▼
┌───────────────────────────────────────────┐
│           DISPATCH GATE (SRS §5.6)          │
│  BR-001 Insurance valid?                    │
│  BR-002 Driver active & employed?           │
│  BR-003 Driver licence valid?               │
│  BR-004 Vehicle not grounded?               │
│  BR-005 Linked approved request exists?     │
└───────────────┬─────────────────────────────┘
        │ All pass                    │ Any fail
        ▼                              ▼
[Dispatch Authorized]         [Blocked — Override required]
        │                              │
        │                     [Justification field, mandatory]
        │                              │
        │                     [Authorized Override] → logged (BR-009)
        │                              │
        └──────────────┬───────────────┘
                        ▼
        ┌───────────────────────────────────────────┐
        │   DRIVER CONFIRMATION (operational          │
        │   addition, not literal SRS §11 text —      │
        │   see note below)                            │
        │   Confirm → proceed        Decline →         │
        │                            [Reason field,    │
        │                             mandatory]        │
        └────────┬──────────────────────┬──────────────┘
                 │                      ▼
                 │        [Routes back to Daniel's Dispatch
                 │         Queue for reassignment — NOT a
                 │         driver-to-driver transfer]
                 ▼
                 [Trip Initiated]
                        │
                        ▼
        [Odometer + Fuel + GPS capture during trip]
                        │
                        ▼
                 [Trip Closed] → distance = end odometer − start odometer (SRS §5.5)
```

The Dispatch Gate is rendered as Component 4 (Action Drawer) in the design system — a slide-in checklist, not a silent background validation, because the SRS's own framing ("prevent dispatch... subject to authorized override") implies the block and the override path must both be visible, deliberate UI states, not something that fails invisibly.

**Driver Confirmation step, added 2026-09-22 — a deliberate operational addition, not literal SRS
text, and worth recording as such.** SRS §11's driver function list and the driver persona's own
SRS-derived journey (`01_USER_PERSONAS.md` §8) describe the driver as simply "seeing their assigned
vehicle for the day" — there's no discretionary accept/decline step in the literal spec text, since
dispatch is an administrative decision made by Daniel (Transport Officer) at the Dispatch Gate
above, not something offered to the driver as a choice. A mobile-app design pass initially borrowed
an Accept/Decline pattern directly from ride-hailing references (Uber/Grab/inDrive) without
checking it against this flow — which would have been an ungrounded import, the same mistake SOS
made earlier in the same screen. **On review, the underlying need is real and distinct from a
ride-hailing "which job do I want" choice: a driver needs a way to confirm they've seen a dispatched
assignment, and to flag genuine inability to fulfill it (illness, prior conflict, a defect they
already know about) *before* execution begins** — not to shop between assignments. So this step is
kept, but reframed as **confirmation with a mandatory-reason exception path**, not open-ended
discretion:
- **Confirm**: acknowledges the driver has seen the dispatched assignment and is proceeding —
  functionally close to SRS §11's "view assignment," with an explicit confirmation tap added for
  clarity and an auditable record of when the driver actually saw it.
- **Decline**: only reachable with a mandatory reason field — matching this system's own standing
  justification pattern used elsewhere (BR-009's override justification, §5.24's workflow
  rejection/return-for-correction) — and **routes back to Daniel's Dispatch Queue for
  reassignment**, never a driver-to-driver handoff (that would bypass Daniel's dispatch authority,
  cutting against the maker-checker model this system enforces everywhere else). This keeps the
  gate's actual decision-making authority with Daniel, consistent with the diagram above — the
  driver flags a problem, Daniel re-dispatches, exactly like an override or a rejected request.

Full UI spec for this step lives in `04_FIGMA_SCREEN_BLUEPRINT.md` §8 (FRAME 7A, "Needs Your
Response" card) and `03_MASTER_DESIGN_SYSTEM.md` Component 9.

**A second, related authorization gate exists later in the same trip — the pre-trip walkaround
inspection (FRAME 7B, Component 10) — grounded directly in SRS §5.6's own text**, which names
"tyres, lights, brakes and safety equipment" explicitly and requires the same "prevent dispatch...
subject to authorized override" pattern applied here. **This gate has a three-tier authorization
path, not just the single digital request shown above, because of this system's own offline-first
commitment** (`CVFMS_Architecture_and_Implementation_Summary.md`) and real low-connectivity
sub-counties (e.g. Baringo): (1) digital override request to Daniel, same as above, when
connectivity allows; (2) a call-Daniel fallback with a logged verbal-authorization confirmation
when data fails but voice/SMS may still work; (3) a last-resort offline provisional override,
explicitly acknowledged (not a casual tap), logged and flagged for mandatory review once
connectivity restores. All three provenances must stay distinguishable in the audit trail — a
digital override, a verbal one, and an offline-provisional one are not interchangeable records for
FRAME-09's statutory audit purposes. Full spec: `03_MASTER_DESIGN_SYSTEM.md` Component 10's
"offline override fallback" note.

---

## 4. Peter's Flow — Workshop Job Card Lifecycle

**Corresponds to:** `01_USER_PERSONAS.md` §3 journey stages 2 and 4 (Diagnosis → parts request; Quality inspection) — the stages flagged there as the dominant friction points (parts stock visibility not traveling with the job, and release historically lacking a structured check).

From SRS §5.9 (Maintenance) and §5.10 (Workshop Management).

```
[Defect Report | Preventive Trigger (mileage/time/engine-hours)]
        │
        ▼
[Work Order Created] — vehicle, diagnosis, estimated cost/parts
        │
        ▼
[Diagnosis] → [In Repair] → [Awaiting Parts]* → [In Repair]
                                                      │
                                                      ▼
                                          [Quality Inspection] (SRS §5.10, explicit required step)
                                                      │
                                        (Fail QA) ────┴──── (Pass QA)
                                              │                │
                                        [Back to In Repair]  [Ready for Release]
                                                                │
                                                                ▼
                                                      [Vehicle Released] → Active
```

*Awaiting Parts is a re-entrant state: a work order can cycle back into it if a second part is needed mid-repair. Each transition is a Kanban card move (Component 5) with the linked spare-parts request status visible on the card at every stage — SRS §5.11 requires parts to be "linked to maintenance work orders," so stock visibility must travel with the card, not live in a separate stores screen Peter has to cross-reference manually.

---

## 5. Fuel Anomaly Detection Flow

**Corresponds to:** `01_USER_PERSONAS.md` §5 journey stage 3 (Review anomalies) — the stage flagged there as a dominant friction point (anomaly flags with no explicit routing to the role positioned to act on them).

From SRS §5.8 and the architecture summary §6.1 (Programmatic Anti-Fraud Controls).

```
[Fuel Transaction Logged] — vehicle, driver, quantity, cost, odometer
        │
        ▼
┌────────────────────────────────────────────────────┐
│                 AUTOMATED CHECKS                     │
│ 1. Quantity ≤ tank capacity × 1.05?                  │
│ 2. Duplicate transaction within 4-hour window?       │
│ 3. Odometer ≥ last recorded (monotonicity, BR-007)?  │
│ 4. Linked to an approved trip/request (BR-006)?      │
│ 5. Efficiency within ±25% of vehicle-class baseline? │
└───────────────┬──────────────────────────────────────┘
        │ All pass                    │ Any fail
        ▼                              ▼
  [Transaction Settled]        [Anomaly Flag Raised] → routed to Miriam's
                                 anomaly review queue (Finance Dashboard)
                                        │
                              [Reviewed: Confirmed Fraud | False Positive | Needs Investigation]
```

This flow terminates in Miriam's queue specifically because the SRS treats these anomalies as financial/audit exposure (§5.18, §23), not purely an operational fuel-desk concern — routing them only to whoever logged the transaction would let exactly the fraud pattern the SRS describes (duplicate transactions, ghost trips) go unreviewed by the role positioned to catch it.

---

## 6. Notes on Method

Every flow's state transitions and gates are built directly from an SRS section number or business rule ID, not carried over from the archived v1.x flows. Two structural decisions from v1.x reappear here — the live map as a separate destination, and the anomaly flow routing to Finance — because they follow directly from re-reading §5.16/§8 phasing and §5.18/§23 respectively, not because they were assumed correct going in.

**v2.1 addition:** each flow above now states which persona journey stage (`01_USER_PERSONAS.md` v2.1) it corresponds to, per the `ui-ux-expert` skill's journey-mapping method. This is a genuine addition, not relabeling — it makes explicit which specific friction point each flow's design decisions (a visible gate checklist, a hard-gated release action, a routed anomaly queue) are actually solving for, rather than leaving that link implicit. The underlying flow logic itself did not change, because it is fixed by the SRS's functional requirements and business rules, which a UX design methodology has no basis to alter — only the traceability from "identified friction" to "flow built to resolve it" is new.
