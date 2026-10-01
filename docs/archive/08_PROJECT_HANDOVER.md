# CVFMS: Project Handover

**Document ID:** `DOC-CVFMS-008`
**Purpose:** Entry point for a designer or engineer picking up this project. Read this first — it tells you what exists, what's decided, what's open, and where to find the reasoning behind every decision so you don't have to re-derive it or accidentally undo it.

---

## 1. What This Project Is

CVFMS (County Government Vehicle Fleet Management System) is enterprise software for Kenyan county government fleet operations — approval workflows, compliance tracking, dispatch, maintenance, finance. It shares a design lineage and visual identity (Civic Green `#006837` accent) with a sibling project, `el-nino` (Nairobi El Niño Response System), but is a light-theme daytime back-office tool, not el-nino's dark 12-hour EOC cockpit.

**Current phase:** UX/Figma design only. No application code exists yet. The target eventual stack (per the SRS) is Next.js 15, TypeScript, Tailwind, shadcn/ui, PostgreSQL — but nothing has been built in code; this is purely design artifacts.

**Where the design lives:** a real Figma file, `bnxWZCzNtbjM0ulb886hXo` (https://www.figma.com/design/bnxWZCzNtbjM0ulb886hXo), built via a mix of Figma's First Draft (text-to-design) and direct Plugin API manipulation (`use_figma`). Real components exist there: Status Pill, KPI Tile, color/spacing/radius variables, text/effect styles — all propagate correctly to instances when fixed at the source (proven multiple times).

---

## 2. Read the Docs in This Order

1. **`01_USER_PERSONAS.md`** — 5 flagship personas: Grace Wanjiru (Fleet Manager, the flagship/primary persona), Daniel Otieno (Transport Officer), Peter Mwangi (Workshop Manager), Sarah (Executive), Miriam (Finance Officer). **Important correction embedded in this doc**: an early draft wrongly scoped Grace as a passive monitor with no real actions — this was corrected; she has real write authority (edit fleet registry, allocate vehicles, override blocked dispatches, approve maintenance). Read the correction note in her section before assuming anything about her scope.
2. **`02_USER_FLOWS.md`** — state machines and flows: vehicle lifecycle, Grace's monitor-to-action hub-and-spoke flow, Daniel's requisition→dispatch-gate→trip flow, Peter's job-card flow, the fuel anomaly flow. Also documents *why* a live map is a separate destination (in-page tab), not part of the main dashboard — an aggregation/triage screen and a spatial exploration tool are different cognitive tasks and shouldn't compete for the same space.
3. **`03_MASTER_DESIGN_SYSTEM.md`** — **the single most important doc**. Canonical tokens (color, type, spacing, radius, shadow) and numbered components (3, 3B, 3C, 3D [removed], 3E, 3F, 3G, 4, 4B, 5, 6, 7...). Every component has a version history explaining *why* it looks the way it does, with Mobbin reference links. **Do not change a token or component spec without reading its existing history first** — several "obvious" changes (adding a sparkline, making a card full-width) were already tried, found wanting, and reverted; the reasoning is written inline so it isn't repeated.
4. **`04_FIGMA_SCREEN_BLUEPRINT.md`** — exact frame directory (6 frames) and per-frame layout specs. **FRAME-01's spec has been through 16 rounds of revision.** Section 2A always contains the CURRENT authoritative version at the top (currently v2.3) — everything below it in that document is version history, kept for traceability, not a build target. Always check the version number at the top of §2A before building anything.
5. **`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`** — the real-world reference screens (Mobbin links) behind every design decision, organized as numbered "Rounds" in reverse chronological order (newest first). If you're wondering "why does this look like this," search this doc for the component name.
6. **`06_DESIGN_QUALITY_PROCESS.md`** — the standing process rules. Contains two hard-won process fixes worth internalizing before you touch anything:
   - **§0: Figma-first vs. code-first decision** — Figma's First Draft has a real, repeated fidelity gap between a precise prompt and the rendered output. Mitigation: one issue per correction prompt, never batched. If one issue fails twice, stop prompting and either fix it directly via `use_figma` (proven reliable) or reconsider the tool choice.
   - **§0B: Spec leads build, no silent layout drift** — a component (Vehicle Status Board) once disappeared from a page without anyone deciding that, because a correction prompt left a gap that First Draft filled plausibly. Rule: every frame's component list must be explicitly enumerated in its blueprint section, updated *before* any prompt that changes it, and checked item-by-item against the actual render afterward.
7. **`07_FIRST_DRAFT_CONTEXT_CARD.md`** — a copy-pasteable block (tokens, active persona, standing rules) to paste at the top of every First Draft prompt, since First Draft has no memory or file access between prompts. Keep this file in sync whenever a standing rule changes.

Source specs: `Kenya_County_Government_Vehicle_Fleet_Management_System_SRS.pdf` and `CVFMS_Architecture_and_Implementation_Summary.md` (project root, not in `docs/`).

---

## 3. Current State of FRAME-01 (Fleet Command Dashboard) — the only frame built so far

**Status: mature, close to done, one open question remains (§5 below).**

Current final layout (v2.3 — see `04_FIGMA_SCREEN_BLUEPRINT.md` §2A for the authoritative version and full reasoning):

```
Top Nav + Left Rail (dark #0F172A)
Page Title + [Overview] [Live Map] tabs

KPI Row — 4 plain cards (Fleet Size, Availability, Grounded, Alerts Due), no sparklines

[Needs Attention ~60-65% width] + [Coming Up ~35-40% width] — side by side

Fleet Map — full width, bounded/card-contained (map + adjacent status list, NOT full-bleed)

Recent Activity Feed — full width, lowest priority
```

**Key decisions that took multiple rounds to reach — do not casually reopen these:**
- **Needs Attention is the hero.** Originally a trend chart was tried (Round 4-6) and removed for being decorative, not actionable — it didn't answer any question Grace actually has. Needs Attention (a synthesized, urgency-ranked action list, merged from what were once 3 separate components: the original Needs Attention, Compliance Countdown, and Critical Mismatch/Utilization Gap) replaced it because every row is a decision, not a data point.
- **Needs Attention is scoped tightly** — Overdue + This Week only, not a comprehensive list. Deprioritized items go to a "Compliance" nav destination (linked, not shown) and a "Coming Up" panel (date-grouped, calm, non-urgent).
- **Vehicle Status Board and Critical Mismatch were both removed as standalone Overview components** (Rounds 14-15) after being found redundant with content already in Needs Attention / Fleet Map. Their full detail lives in linked destinations instead (a Vehicle Allocation Table for the idle-vehicle/pending-request detail, "All Vehicles →" on Fleet Map for the full fleet table).
- **Dominance comes from elevation and position, not width** (Round 16) — Needs Attention was briefly full-width as a proxy for "most important," found to waste space on short content, and narrowed with Coming Up brought up to fill the freed space deliberately (not arbitrarily — both are list/urgency-shaped, non-redundant with each other).
- **Row-level type hierarchy is a system-wide rule**, not specific to one component (`03_MASTER_DESIGN_SYSTEM.md` §B2): exactly one dominant text element per row, everything else drops at least one size/weight level, never more than 2 distinct sizes per row, color reinforces hierarchy rather than replacing it. Apply this to every future list/row component.

---

## 4. What's NOT Started

- **FRAME-02** (Dispatch & Requisition Queue, Daniel) — spec exists in `04_FIGMA_SCREEN_BLUEPRINT.md` §3, not yet built in Figma.
- **FRAME-03** (Workshop Job Card Board, Peter) — spec exists §4, not built.
- **FRAME-04** (Executive Briefing Dashboard, Sarah) — spec exists §5, not built.
- **FRAME-05** (Finance & Cost Dashboard, Miriam) — spec exists §6, not built.
- **FRAME-06** (Live Fleet Map, full-bleed) — spec exists §2B, explicitly sequenced last (SRS tiers GPS/Telematics as Phase 5, after Foundation/Operations/Cost/Compliance).
- **Vehicle Allocation Table** (`03_MASTER_DESIGN_SYSTEM.md` Component 3G) — specced as a concept, not yet assigned to a frame or built. Decide whether it's a modal/drawer or a dedicated view when you get to it.
- **Grace's 4 action modals** (Registry Edit, Reallocate, Dispatch Override, Maintenance Approval) — referenced throughout `02_USER_FLOWS.md` §2 as destinations from Needs Attention's action buttons, never actually designed as screens.
- **A `status_reason_code` field** was identified as a required schema addition (`04_FIGMA_SCREEN_BLUEPRINT.md`, old v1.3 Gap 1 note) and added to the ERD in `CVFMS_Architecture_and_Implementation_Summary.md` — flagged for whoever picks up engineering, not yet actioned beyond the doc update.

**Recommended next step:** FRAME-02, following the Generation Sequence in `04_FIGMA_SCREEN_BLUEPRINT.md` §7 — but first read `06_DESIGN_QUALITY_PROCESS.md` §1 in full and run its 3-reference-Mobbin-check + Finish Pass steps *before* writing the first prompt, not after seeing a bad render (this is what slowed FRAME-01 down — most of its 16 rounds were reactive fixes that could have been front-loaded).

---

## 5. Open Question — Recent Activity

Not yet resolved. Recent Activity (a chronological feed of actions by all users — trip starts, overrides, approvals) has survived every prior round without being tested against the same "does Grace need this to act" bar everything else on the page has been held to. Initial analysis: it's retrospective, not actionable, and doesn't clearly serve either of Grace's two core jobs (know state / act on problems). Three options were on the table when this handover was written, none chosen yet:
1. Remove it entirely from Overview.
2. Keep it, but narrow its content to override/exception events only (real audit value) rather than routine actions.
3. Find a justification not yet articulated and keep it as-is.

Resolve this before considering FRAME-01 fully closed.

---

## 6. Practical Notes for Continuing This Work

- **Every design system/blueprint change gets mirrored** to `.agents/rules/master-design-system.md` — this file is a copy of `docs/03_MASTER_DESIGN_SYSTEM.md`, kept in sync via `cp`. Don't edit the `.agents/rules/` copy directly; edit the canonical doc and re-copy.
- **When First Draft correction prompts don't land**, check `06_DESIGN_QUALITY_PROCESS.md` §0's escalation rule: two failed focused attempts on the same issue means switch to fixing it directly via `use_figma`, don't keep re-prompting.
- **Before adding any chart, sparkline, or decorative element anywhere in this system**, name the specific decision it would change for the user first. This project has removed decorative elements (a hero trend chart, KPI sparklines twice) for failing this test — it's a real, enforced standard, not a suggestion.
- **Mobbin benchmarking should be per-component, not per-page** when refining something specific — whole-page searches were less useful than targeted searches for "what does a well-designed X look like" once the project matured past its first draft.
