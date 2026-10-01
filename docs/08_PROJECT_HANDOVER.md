# CVFMS: Project Handover

**Document ID:** `DOC-CVFMS-008`
**Revision:** 2.7 (2026-09-18) — reconciliation pass: added a "Fast orientation" note up top flagging that §6 is stale (superseded by §12) and that the 16-persona model (`01_USER_PERSONAS.md`) and the newer 11-profile model (§11/§12, from `CVFMS Primary profiles.docx`) were never reconciled into one source of truth — this is a real open item, not resolved by this pass, just made visible. §3's blueprint entry corrected to reflect FRAME-07/08/09 now existing in `04_FIGMA_SCREEN_BLUEPRINT.md` (9 frames, not 6). 2.6 (2026-09-18) added §12 (Current Status, Screen Progress & Next Agent Action Plan): FRAME-01 re-rendered and verified (active Operations pillar, vehicle IDs restored in Recent Activity, 1px card borders); FRAME-02 (Daniel / Dispatch) prompt finalized with role titles under profile names and humanized Dispatch Readiness checklist; FRAME-07 (Driver Mobile PWA) fully specced using M3 component anatomy with CVFMS tokens, including deep home screen anatomy ("Today's Job" card, 3 dynamic shift states); next agent roadmap locked in. 2.5 (2026-09-18) added §11: Formal adoption of `CVFMS Primary profiles.docx` (11 primary user profiles + Approver as permission overlay), 6-stage demo lifecycle path, Auditor vs Administrator separation, and Driver trip bookends.
**Purpose:** Entry point for anyone picking up this project. Read this first.
**If you are actively building a new screen under time pressure, skip straight to `09_PATTERN_LIBRARY.md`** — it has copy-paste prompt fragments for every proven pattern and a pre-flight checklist. Come back to docs 01-07 only for the "why" behind a decision, not as the first stop for "how."
**Fast orientation (2026-09-18) — this doc has grown faster than it's been reconciled; read §12 first for actual current state, not §6** (§6's "Current State" header is stale — it predates FRAME-07/08/09 and the 11-profile model). Two real, unresolved contradictions to know about before trusting anything below at face value: (1) `01_USER_PERSONAS.md` v3.0 documents **16 separate SRS-role personas**, but §11/§12 below describe a newer **11 Primary Operational Profiles** model (source: `CVFMS Primary profiles.docx`, in the repo root) as "locked" — these were never reconciled into one source of truth, and `04_FIGMA_SCREEN_BLUEPRINT.md`'s new FRAME-08/09 sections cite both naming schemes interchangeably. (2) §8's "Driver Management" web-registry screen (184 drivers, licence/expiry columns) is a **still-open, unresolved gap**, distinct from FRAME-07 (the Driver Mobile App in §12) — don't assume the new driver work in §11/§12 closes it.

**Desktop work (since 2026-09-24) runs in a separate chat from mobile. For desktop, read §25 at the end of this doc, then `13_SYSTEM_MAP.md` and `12_DESKTOP_REDESIGN.md` §2.**

---

## 1. What This Project Is

CVFMS (County Government Vehicle Fleet Management System) is enterprise software for Kenyan county government fleet operations — approval workflows, compliance tracking, dispatch, maintenance, finance. It shares a design lineage and visual identity (Civic Green `#006837` accent) with a sibling project, `el-nino`, but is a light-theme daytime back-office tool, not el-nino's dark 12-hour EOC cockpit.

**Current phase:** UX/Figma design only. No application code exists. Target eventual stack per the SRS: Next.js 15, TypeScript, Tailwind, shadcn/ui, PostgreSQL.

**Where the design lives:** Figma file `bnxWZCzNtbjM0ulb886hXo` (https://www.figma.com/design/bnxWZCzNtbjM0ulb886hXo). **Update (2026-09-14/15): the v2.0 blueprint has since been built out.** All 7 screens in the demo set exist in the file — FRAME-01 (Grace, node `133:28`), FRAME-02 (Daniel, `141:52`), FRAME-05 (Miriam, `146:83`), FRAME-03 (Peter, `147:124`), FRAME-04 (Sarah, `159:278`), All Vehicles (`161:391`), FRAME-06 (`164:476`). Node IDs have shifted between sessions in past checks — the file is actively edited (by the user and/or their Figma agent) between calls, so re-verify a node ID against a fresh `get_metadata`/screenshot before trusting it, rather than assume a previously-recorded ID is still current.

---

## 2. Why This Restart Happened

The project had an existing, working doc set (01-08) built up over 16 rounds of iteration on FRAME-01 alone. On 2026-09-13, the user installed the `ui-ux-pro-max` skill and asked to redo the research "from the very beginning," explicitly checking the source PDF, and — after being asked to confirm scope given the destructive, hard-to-reverse nature of the request — chose a **full restart of both docs and Figma**, with the old docs **archived, not merged**. The full original doc set (v1.x) is preserved at `docs/archive/` for reference; nothing in it was treated as ground truth for the new version, though several conclusions independently reappeared (see §6 below).

---

## 3. Read the Docs in This Order

1. **`01_USER_PERSONAS.md`** (v3.0, 2026-09-16) — all 16 SRS roles now documented. Wave 1: the original 5 flagship personas (Grace/Fleet Manager, Daniel/Transport Officer, Peter/Workshop Manager, Sarah/Executive, Miriam/Finance), the only ones with Figma screens built. Wave 2: 11 additional personas (System Administrator, Fleet Officer, Driver, Mechanic, Fuel Officer, Storekeeper, Procurement Officer, HR Officer, Auditor, Department User, Approving Officer) documented to the same method but not yet built as screens — see §8 below.
2. **`02_USER_FLOWS.md`** (v2.0) — state machines re-derived from SRS §5 functional requirements and §18/§23 business rules/fraud controls, including the resolved Recent Activity question (see §5 below, no longer open).
3. **`03_MASTER_DESIGN_SYSTEM.md`** (v2.0) — **the single most important doc.** Tokens and components re-derived from a fresh `ui-ux-pro-max` research pass (documented in its own §0), not carried over from the archived version. Notable changes from v1.x: typography is now Lexend/Source Sans 3 (was a different pairing); color hex values were independently re-derived (same green/navy family, different exact values — treat v2.0 as authoritative); the "never color alone" accessibility rule and the bar/line-only chart policy both survived the restart because the fresh research independently re-confirmed them, not because they were assumed correct.
4. **`04_FIGMA_SCREEN_BLUEPRINT.md`** — originally 6 frames (v2.0, re-derived fresh from each persona's core goal). **Expanded 2026-09-18 to 9 frames**, adding FRAME-07 (Driver Mobile App), FRAME-08 (Requester Portal & Approver Review), FRAME-09 (Statutory Audit Trail) — see §11/§12 below. The doc's own revision line at the top has not been updated to reflect this addition; don't trust it, trust the actual section list (`grep "^## " docs/04_FIGMA_SCREEN_BLUEPRINT.md`).
5. **`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`** (v2.0) — restructured from chronological "Rounds" (tied to old build iterations) to **per-component** benchmarks, since the round history no longer applies. Adopts the project's own late-stage insight — per-component search beats whole-page search — from the start this time.
6. **`06_DESIGN_QUALITY_PROCESS.md`** (v2.0) — same two hard-won process rules as before (§0 First Draft escalation, §0B no silent layout drift), kept because their root causes are structural to this tool/workflow, not because the old doc said so. Added: a token-value verification section (§2) and an explicit worked-examples section for the decorative-element test (§4).
7. **`07_FIRST_DRAFT_CONTEXT_CARD.md`** (v3.0, 2026-09-16) — rewritten from a full paste-every-prompt token block into a standing-context summary (read once, applies going forward), matching the shift to reference-based prompting. Covers the current simplicity direction (plain KPI tiles by default, one accent color, no default loading/error states) and the reduced-token prompting format.
8. **`09_PATTERN_LIBRARY.md`** (new, 2026-09-14) — fast-reference companion to all of the above, added under real timeline pressure. Every proven, confirmed-working pattern from the 7 screens built so far (App Shell, two-pane work surfaces, KPI rows, status/action lists, Kanban, data tables, drill-downs, breadcrumb scope) as copy-paste prompt fragments, plus a component-sourcing section covering the Untitled UI base kit (buttons/badges/inputs only — it has no composed patterns, those remain CVFMS-original) and a pre-flight checklist. **Read this before writing a new screen prompt** — it's the "how," while docs 01-07 remain the "why."

Source specs (unchanged, root directory): `Kenya_County_Government_Vehicle_Fleet_Management_System_SRS.pdf`, `CVFMS_Architecture_and_Implementation_Summary.md`.

**Archived v1.x docs:** `docs/archive/01_USER_PERSONAS.md` through `08_PROJECT_HANDOVER.md` — kept for reference only, not authoritative. Useful if you want to see the reasoning trail behind FRAME-01's 16 rounds, but do not treat anything in `archive/` as current.

---

## 4. Design System Baseline (locked this session)

Confirmed with the user before writing docs, via the `ui-ux-pro-max` research pass:
- **Style:** Data-Dense Dashboard + Accessible & Ethical (WCAG AAA target).
- **Palette:** Civic Green `#006837` as the sole brand accent; Navy/Slate (`#0F172A` / `#334155`) as structural neutrals; standard success/warning/critical status tokens.
- **Typography:** Lexend (headings) + Source Sans 3 (body) — the "Corporate Trust" pairing, chosen over Inter/Minimal Swiss specifically for its reading-accessibility design intent, given the WCAG AAA target and a varied-literacy public-sector user base.
- **Charts:** bar (category comparison) and line (trend) only — no radar/gauge/donut/heatmap anywhere in the system.

Full reasoning and rejected alternatives are in `03_MASTER_DESIGN_SYSTEM.md` §0.

---

## 5. Recent Activity — Resolved (was open in the prior handover)

The archived handover left this open with three options on the table. This restart resolves it: **Recent Activity stays on FRAME-01's Overview, narrowed to override/exception events only** (option 2 from the old list), not removed and not left as a full routine-action feed. Reasoning is in `04_FIGMA_SCREEN_BLUEPRINT.md` §2.

---

## 6. Current State (updated 2026-09-15) — All 7 Screens Built, Iterating on Fixes — **STALE, see §12 for actual current state (2026-09-18)**

**Workflow in use:** the user runs their own Figma agent against prompts I write (not `use_figma` calls from this session). Per screen: I run the mandatory pre-generation Mobbin check (`06_DESIGN_QUALITY_PROCESS.md` §1), write a structure-and-content-only prompt (no styling — user's explicit standing preference, see §7 below), the user runs it and shares a screenshot, I check it against spec (and, where useful, directly inspect the actual Figma node via `get_metadata`/`get_screenshot` rather than trust the screenshot alone), then write a single-issue or small-combined-issue fix prompt.

**7-screen demo set, all built, all through at least one fix round:**
1. **FRAME-01** (Grace, Fleet Operations Overview) — 3 tabs: Overview / Live Map / All Vehicles. Multiple fix rounds: Jobber-style simplification (greeting header replacing page title, merged KPI+urgency "Fleet Status Row"), per-section Needs Attention counts, map legend, Recent Activity actor field, nav-label regressions (recurring — see §7).
2. **FRAME-02** (Daniel, Dispatch & Requisition Queue) — fixed two-pane (not a drawer — deliberate, see §7), Dispatch Gate Checklist with BR-001–005. Fixed: pane width ratio drift, detail-panel elevation/spacing, Override button clarity.
3. **FRAME-05** (Miriam, Finance & Cost Dashboard, Anomaly Review tab) — true overlay drawer (deliberate, opposite of FRAME-02 — see §7), 3-way decision (Confirm Fraud / False Positive / Escalate).
4. **FRAME-03** (Peter, Workshop Job Card Board) — 5-column Kanban, QA-gated release. Fixed: nav regression, context label, cost-breakdown reconciliation, stalled-column tint.
5. **FRAME-04** (Sarah, Executive Briefing) — KPI-against-target, twin trend charts, inline departmental drill-down. Fixed: dual-nav-highlight bug, orphaned chart data point.
6. **All Vehicles tab** — full Fleet Registry table (Component 6), closes a real gap (the "Fleet Registry" nav item and "All vehicles →" link had no destination before this).
7. **FRAME-06** (Live Fleet Map) — full-bleed map + collapsible side panel, prompted but not yet confirmed built/checked.

**Recurring defects worth knowing about before checking any new screen** (see `09_PATTERN_LIBRARY.md` §11 for the full pre-flight list): icon-only/unlabeled sidebar (happened twice), KPI delta shown as a bare colored dot with no text/icon (happened twice, on two different screens), duplicate page-title blocks. Always check these specifically, don't assume a screen that passed once won't regress.
**New mobile-specific recurring defect (found 2026-09-21, FRAME-07):** the Figma agent reuses one generic icon (a car/taxi silhouette) across every icon slot on a screen — found on FRAME 7A across all 3 Quick Action chips AND all 3 bottom tab items (6 slots, 1 icon). Always check that action/nav icons are actually distinct and meaningful per item, not just present — a screen can pass a "does it have icons" check while still being generic if every icon is the same shape. Check this specifically on 7B, 7C, and 7D before treating them as done.

**Personalization added to FRAME-07 (2026-09-21), per direct user request.** Asked "have we included personalization?" — checked and confirmed the answer was no: the SRS never mentions language/localization at all, and the bottom tab bar's "Profile" tab had no screen behind it. User confirmed scope: (1) a real Driver Profile screen (**new FRAME 7D**, `04_FIGMA_SCREEN_BLUEPRINT.md` §8) — identity card, licence class/expiry (the same data BR-003 checks at Daniel's dispatch gate, now visible to the driver too), a language toggle, sign-out; (2) an **English/Kiswahili language toggle**, scoped to the mobile app only for now; (3) a **home-screen greeting** ("Good morning, Joseph") on FRAME 7A. The greeting is a deliberate, reasoned extension of a previously FRAME-01-only pattern — documented in `03_MASTER_DESIGN_SYSTEM.md` Component 1 as a second instance of the same "once-per-session daily landing screen" usage pattern, not a blanket loosening of the rule. **Open, wider question not resolved by this addition:** should the desktop system also get localization? Not asked about or decided — flag to the user before assuming either way if a future screen's language scope comes up.

**Quick Actions row removed from FRAME 7A (2026-09-21), traced against the persona's own journey table.** User asked directly whether the Home screen's Quick Actions (SOS/Log Fuel/Report Defect) were actually needed there. Checked `01_USER_PERSONAS.md` §8's journey table: Log Fuel and Report Defect belong to Stage 4 ("During trip"), not Stage 1 ("Login & view assignment") — they were on Home because FRAME 7C never specced a during-trip screen state, not because Home was the right place for them. **Fix, not just a removal:** added a new **State 1.5 (Active Trip)** to FRAME 7C, between Start Journey and End Journey, where Log Fuel and Report Breakdown/Defect now live as contextual actions. Emergency SOS is different — not tied to one stage — so it's **promoted to a persistent header icon on all 4 FRAME-07 sub-screens**, reachable regardless of which screen the driver is on when something goes wrong. **The FRAME 7A fix prompt given earlier in this session (icons, SOS distinction, action-priority reorder) is now partially stale** — it still assumed Quick Actions stays on Home in some form. Don't run that prompt as-is; a corrected one is needed before the next Figma pass on 7A, and the still-unbuilt Active Trip state needs its own prompt.

**SOS grounding corrected (2026-09-21).** It had no basis in the SRS — traced back to an unstated assumption from earlier in this project's history, then compounded by promoting it to a persistent header element before ever checking where it came from. Asked the user directly: confirmed **keep**, justified by SRS §11's offline-first/rural-connectivity rationale (a real emergency scenario with no signal), not by the SRS naming "SOS" explicitly. **Still open: what SOS actually does when tapped** (call a number, alert dispatch, etc.) — not decided, needs a follow-up before this is buildable end-to-end.

**Trip Card action reconsidered (2026-09-21) — a real course-correction, not just an answer.** Initially reasoned "one linear task, nothing to triage, so no card-level actions needed" (beyond the call icon). User pushed back ("a card without any actions does seem a bit strange here") and that reasoning turned out to be too narrow: a single card can still need actions if it's hiding content, independent of whether there's anything to choose between. Concrete evidence: the already-rendered build truncates the requester line ("...3 Pass..."), meaning real SRS §5.4 fields (full passenger count, purpose, special requirements) are being lost, not just hidden-but-reachable. **Added a "View Details →" action to the Trip Card** (`04_FIGMA_SCREEN_BLUEPRINT.md` §8, FRAME 7A). Vehicle Card was deliberately NOT given an equivalent action — its content is already fully visible with nothing truncated, so adding one would be symmetry for its own sake, not a real need. **Lesson: "is there a decision to make" isn't the only test for whether a card needs an action — "is content being cut off" is a separate, independently sufficient reason.**

**Inspection cadence — reasoning revised twice (2026-09-21), not yet fully locked.** User asked directly "is the car inspection per trip or when exactly?" — SRS genuinely doesn't say; it uses "inspection" for two different things (the statutory roadworthiness record BR-004 checks vs. the driver's own physical walkaround) and never states the walkaround's frequency. **First pass:** "once per shift, per vehicle" (commercial-trucking convention), confirmed with the user. **User then asked "is this practical for county or national governments?"** — good challenge: CVFMS is a pooled-vehicle, per-request dispatch model (Daniel's Dispatch Queue, BR-005), not one driver keeping one vehicle all day, so "already inspected this shift" doesn't hold once the vehicle can change hands mid-day. Proposed the stricter opposite (per-dispatch, matching the system's accountability-heavy governance culture) — **user pushed back: "isn't this too much?"**, correctly — a full walkaround before every single trip in a multi-trip day risks becoming exactly the rubber-stamping failure the persona's own design implication warns about. **Landed on a custody-based rule instead:** skip re-inspection only across back-to-back dispatches in the same vehicle with the same driver and no return to the pool in between; require a fresh check whenever the vehicle returns to the yard/pool between dispatches. **Not a final locked decision** — flagged as the recommended direction for whoever builds multi-trip-per-shift next, since current FRAME 7A/7B/7C remain single-trip-only in scope and this hasn't been road-tested. See `04_FIGMA_SCREEN_BLUEPRINT.md` §8 for the full reasoning trail — worth reading in full before treating either the trucking convention or the per-dispatch rule as settled, since both were tried and rejected in this same conversation.

**Real driver function gap found and closed (2026-09-21): "Accept" was missing entirely.** User proposed drivers should see a list of incoming assignments, in order, with Confirm/Deny(reason)/Transfer/Delay actions — not just today's single trip. Checked the SRS directly: line 405's driver function list literally separates "Accept/start/end trip" — three distinct steps, but this spec only ever built "start" and "end," treating every assignment as pre-committed with no acceptance gate. **Transfer specifically raised a governance concern** (a driver reassigning their own trip would bypass Daniel's dispatch authority, cutting against the maker-checker model enforced everywhere else in this system) — confirmed with the user: **replaced with "Decline (with reason)," which routes back to Daniel's Dispatch Queue for reassignment**, keeping dispatch as the sole reassignment authority. "Delay" has no SRS grounding and wasn't added. **Result: FRAME-07 now has 6 sub-frames, not 4** — added **7A/State 0** (Accept/Decline an incoming assignment, precedes the existing Home content which is now State 1) and **7E** (Trips tab: the ordered incoming-assignments list, closing a second empty tab alongside 7D's Profile). Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8. This also quietly resolves an earlier open item — whether the Home screen could show a future-dated trip — since future assignments now live in the 7E list until accepted.

**"Offline Sync Ready • 100%" header badge removed (2026-09-21) — same failure mode as the SOS-grounding mistake.** User asked directly why this text was there; it turned out to have been carried forward unscrutinized from the original draft spec through every consolidation pass this session, never actually reconsidered. Two problems: "100%" is meaningless jargon (100% of what?), and it violates the content-type rule (below) — default/working states shouldn't get a permanent badge, only something needing attention should, matching why delta chips are opt-in and there's no stats row. The phone's OS status bar already shows connectivity. Removed entirely; a plain-language warning can appear only if sync genuinely fails. **Lesson, worth repeating: original-draft spec text isn't automatically correct just because it's been there since the start** — check it the same way anything newly-proposed gets checked, don't grandfather it in.

**First real render of FRAME 7A (both states) checked (2026-09-21) — mostly correct, 3 fixes needed.** The content-type rule, Accept/Decline hierarchy, wheelchair-strip styling, distinct tab icons, and the removed sync badge all landed correctly — real progress. Three issues found: (1) the SOS icon rendered as a generic warning triangle, not recognizable as "emergency" specifically — needs a more explicit emergency signifier; (2) States 0 and 1 looked nearly identical, distinguished only by small label text — added a thin green top border to State 0 so "this needs a decision" is unmistakable at a glance, not something to notice only by reading carefully; (3) the wheelchair-access flag only appeared in State 1 (after acceptance) — backwards, since it's more useful before a driver commits than after; now shown on both states. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**FRAME 7A rebuilt as a list, replacing the single-card two-state model (2026-09-21) — a real architectural correction, not a patch.** User pushed back hard: Home needs to show multiple assignments ordered by urgency, not one dominant card; questioned why a call icon existed at all; said "Next Step" belongs to a work card, not the page; asked for Grab-style inline accept/deny actions. Asked directly what a senior product designer would think. **Answer: the user was right, and the fix was to reuse a pattern this project already has** — Grace's Needs Attention list (`09_PATTERN_LIBRARY.md` §4: urgency-ordered rows, each with its own scoped action, vary the verb, never one generic button) — rather than the bespoke single-card-with-page-level-CTA pattern Home had been built as. **Call icon removed entirely on reconsideration**: it was imported from Grab/Shopee, where live call is essential because driver and passenger are actively locating each other — CVFMS's driver-requester relationship is a pre-arranged government trip with a fixed time/place, not a live coordination problem. Same category of mistake as the earlier map/route creep. **Result:** Home is now an ordered list — in-progress trip (top, own "Start Pre-Trip Inspection" button on the card) → pending assignment (Accept/Decline buttons on the card) → scheduled-for-later (informational only). No page-level "NEXT STEP" or sticky footer anymore, since different cards need different next steps. This also resolves the earlier open question about future-dated trips for free — a scheduled card just shows its own real date. **New open item this creates:** FRAME 7E (Trips tab) now needs reconciling against Home's list — not yet decided what's left for it specifically (likely full history + far-future scheduling). Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**Root cause of the recurring mobile "generic" feeling — found, then corrected a second time (2026-09-21).** User asked about adopting a real external mobile design system (Wise, Uber considered) — neither is actually installable as a genuine Figma library, and checking Wise's real screens directly corrected an assumption: it's dark-themed and promotional, not the restrained single-accent match its reputation suggests. Found that **Material 3 Design Kit is already installed in the main Figma file**, with real, correctly-built components — first recommendation was to use these real M3 components instead of hand-described M3-style shapes. **User corrected this too: "we are already using material and my issue is all the generic stuff."** Right call — real M3 components fix structural/accessibility correctness, but if M3's own visual defaults (shadows, corner radii, shape language) are left untouched, a technically-correct M3 screen still reads as a generic Android app, because M3's whole design philosophy (expressive, tonally-elevated, bouncy) is close to the opposite of CVFMS's own deliberate flat/restrained identity (`03_MASTER_DESIGN_SYSTEM.md`: `radius.lg` 12px, hairline borders, a shadow explicitly documented as "never decorative"). **Corrected standing rule: use M3 for structure/accessibility only, override every visual default (radius, shadow, icon weight) with CVFMS's own already-established tokens — recoloring M3's stock shadows/radii to green doesn't remove the shadows/radii.** The card's left-edge accent-bar pattern (a genuine CVFMS invention, not stock M3) should be leaned into as a signature element, not diluted back toward M3 conventions. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**5 scannability refinements applied to the assignment cards (2026-09-21)**, from general UI-scannability principles the user shared (anchoring to edges, differentiating content, showing not telling, managing emphasis via neighbors, simplifying layouts) — checked honestly against the current design rather than applied wholesale. Two real gaps found and fixed: (1) three cards for three different requesters were only differentiable by reading the name — added a small initials avatar per requester; (2) status labels were text-only — added a small universal icon per status (play/bell/clock), strengthening the existing never-color-alone rule, which matters more here given the low-literacy design concern already established for this app. Two more: (3) the "Scheduled" card should be visually quieted (muted text) rather than the urgent cards being made louder — emphasis via contrast with neighbors, not added decoration; (4) the internal reference ID ("TRIP · REQ-2024-0851") was leading every card before the destination — demoted to secondary/muted text since a driver scans for destination, not an internal number. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**First header render checked (2026-09-22) — mostly correct, two confirmed additions, one still missing.** Greeting/name weight split, background photo + overlay, and notification bell + badge all landed correctly. Two unprompted additions confirmed as keepers: a settings gear icon beside the notification bell, and a real/representative avatar photo instead of the neutral placeholder originally specced (both loosened as standing rules). A small green "on duty" status dot also appeared and was kept as a reasonable, low-risk addition. **Still missing: the county emblem/crest icon** — the landscape photo covers "landmark" but the separate small emblem hasn't appeared in any build yet, needs a follow-up prompt. Also noted: the same render's assignment cards are still the un-fixed version from the previous round (READY label, gray Accept button, solid colored dots) — the card fix prompt hasn't been run yet, just the header changes layered on top.

**"One main green CTA" scoped explicitly (2026-09-22) — a real question, resolved with reasoning on record.** User asked whether keeping Accept as filled green violates a one-primary-CTA-per-screen discipline, given Card 1's button is also filled green. Resolved: scoped per-decision, not per-screen — each card is an independent choice, not a competitor for the same decision, and the list's urgency ordering already signals relative priority without needing to mute color elsewhere. Initial fallback proposal (cap/hide overflow cards) was correctly refined by a follow-up response: hiding a pending assignment risks a driver missing one they needed to see, a real discoverability cost. **Adopted instead: max 2 visible filled-green CTAs in the viewport** (current 3-card layout already satisfies this), with overflow handled by showing the single highest-priority pending card plus a plain "View N more pending →" row — nothing hidden, everything still reachable.

**Recurring defect flagged as a known, named issue (2026-09-22): "Accept" keeps rendering as a plain gray button instead of filled Civic Green.** This is roughly the 4th time button hierarchy has failed to render correctly across all the render checks this session, despite explicit, repeated instructions ("filled #006837, white text, clearly dominant"). Also found in this same render: Card 1's status chip says "READY" instead of "IN PROGRESS" (wrong label), and the journey dots reverted to solid blue/green fill colors instead of the locked hollow-origin/filled-destination neutral treatment (enforcing an already-made decision, not re-litigating it). Given how often the Accept-button defect specifically recurs, worth considering — if it happens again — whether the Figma agent is reusing an existing button component with the wrong variant/property set by default, rather than building the button fresh each time; a generic "make it green" instruction clearly isn't sufficient on its own anymore.

**County branding added to the header — a deliberate, acknowledged exception to this project's minimalism discipline (2026-09-22).** User pushed back on stripping everything down for its own sake ("functionality doesn't mean it needs to be boring") and asked for both a county landmark background image and a county emblem, since CVFMS may deploy per-county. Agreed and specced properly rather than just dropped in decoratively: applies to the **expanded header state only** (collapsed stays solid navy, sidestepping the accessibility risk at compact size), with a mandatory dark overlay (`#0F172A` 75-85% opacity) that must guarantee WCAG contrast regardless of which county's photo loads — not a per-photo judgment call. Flagged the real operational dependency this creates: every county needs a sourced, rights-cleared, consistently-cropped photo and emblem before it can ship for that county, with a plain-gradient fallback for any county not yet configured (must never render as a broken image). This is explicitly logged as a one-off philosophy exception — nowhere else in the app carries a photographic/decorative element, and that stays true everywhere except this one header.

**SOS removed entirely, replaced with a notification icon (2026-09-22).** User: don't need SOS, but want a notification icon like IKEA's. Good trade — SOS was always the weaker element here, an unstated assumption that needed after-the-fact justification (SRS §11's offline-first rationale) rather than an actual named requirement. A notification icon is directly grounded in SRS §5.23 ("Notification and Alert Management") — a real requirement already referenced elsewhere in this project (flagged as needed for the Approving Officer persona, never built) but never implemented anywhere until now. Same position and neutral treatment as SOS had; added an unread-badge spec (small red dot, `color.status.critical`, shown only when something's unread) as the one new, deliberate color exception to the otherwise-closed list — caught and fixed a contradiction where an earlier line claimed "no exceptions left" right before this one was added. All historical SOS reasoning in `03_MASTER_DESIGN_SYSTEM.md`/`04_FIGMA_SCREEN_BLUEPRINT.md` is left in place as a reasoning trail but explicitly marked superseded, not deleted.

**Collapsing header added (2026-09-22)** — user proposed a bigger header that shrinks on scroll, like IKEA's. This is genuinely the native iOS/Android "Large Title" pattern, not a novel idea, and makes sense now that Home has real scrollable length (3 cards). Specified as two closed states in `03_MASTER_DESIGN_SYSTEM.md`: expanded (avatar visible, name at 20px, subtitle visible, 20px padding) and collapsed (avatar and subtitle dropped, name alone at the standard 16px, 12px padding) — SOS icon stays visible and unchanged in both states, since it must remain persistent regardless of scroll position. Explicit guardrail added: the expanded state must not become a place to add new content (a stats count, search bar, etc.) just to fill the extra height — it's purely more breathing room and larger type on what's already there, given how much of this session was spent removing exactly that kind of unjustified addition elsewhere on this screen.

**Render checked (2026-09-22) — one real inconsistency, one genuine improvement kept, two regressions fixed.** User asked what the best card hierarchy actually is, since a new render showed a nicer journey visual but the cards didn't agree with each other. Found: Card 1 correctly kept time small/secondary with destination as the one bold hero; Cards 2 and 3 instead promoted time to its own bold headline, giving those two cards two competing dominant elements — a direct violation of §B2 (exactly one dominant element per card). **Resolved: Card 1's treatment is now mandatory for all cards.** Kept and formalized a genuine improvement from the same render: a vertical dot-connector-dot journey timeline (hollow origin dot → line → filled destination dot) replacing the flat "🔵 From X" line — clearer, and it let the route-dot color exception (`#3B82F6`) be retired entirely, since shape now carries the origin/destination distinction instead of color, tightening the closed color list further. Fixed two regressions: Card 1 was missing its chevron (every card needs one), and the button text had drifted from "Start Pre-Trip Inspection →" to a vague "Continue assignment" — reverted, with the exact-action-naming rule restated directly on the component since it drifted once already. Also checked Mobbin for header references — no strong structural match existed (most results were full dark-mode consumer apps, not our dark-header/light-body pattern), but [IKEA's header](https://mobbin.com/screens/236972df-1152-4b5a-9bd2-2ed6aa872220) gave one real, usable idea: split the greeting phrase from the driver's name in weight, name bolder — applied. Full detail in `03_MASTER_DESIGN_SYSTEM.md` Component 9 and `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**Follow-up audit caught a real self-contradiction (2026-09-21).** After closing the weight/color table, re-read the rest of Component 9 and found its own closing "What this replaces" section still said "the person/car icons are dropped" — flatly contradicting the confirmed decision to keep them, sitting at the very end of the component where it could be read as the final word. Fixed, with an explicit warning not to trust earlier statements in the doc over the current color table. Also closed three colors that had never been specified at all: the chevron (`slate-muted`, doesn't shift per card state), the header avatar/SOS icon (neutral placeholder colors), and the bottom tab bar (inactive icons `slate-muted` on navy, active icon white on the existing `#173829` desktop active-chip token — not a new mobile-only color). All icons across the whole screen — status, route dot, detail-block, chevron, header, tab bar — now follow one closed icon-color rule with no chrome-element exceptions.

**Every weight/color value closed, no ambiguity left (2026-09-21).** User asked for clarity on weights and colors specifically. Auditing Component 9 found real gaps: chip text colors were referenced by token name without exact hex per status, the "Scheduled" card's muted text had no pinned value (just "lighter shade"), icon colors were never stated at all, and an earlier rule wrongly demanded AAA contrast for the muted state when this system's own existing muted-text token (`slate-muted`, `#64748B`) is documented as AA, not AAA — corrected to match what's actually achievable with existing tokens rather than overclaim. Added a full per-state color table (chip bg/text, body text, icons, route dot) for all 3 card states, and closed the route-dot ambiguity: it mutes to gray on the Scheduled card rather than staying bright blue, since a persistently bright dot would become the one loud element specifically because its neighbors went quiet — the opposite of the emphasis-via-relationship rule. Also locked a system-wide icon style rule (one icon set, one stroke weight, icon color always matches adjacent text) closing the "icons look inconsistent" complaint from several turns back, which had been flagged but never turned into an actual rule.

**Destination headline size corrected — 20px was a reasoning error, rolled back to 16px (2026-09-21).** User: "our font system is too big." Reconsidering the earlier bump to 20px (done to match inDrive's price prominence) surfaced a real error: inDrive's price is a genuine page-level hero appearing once on the whole screen; our destination text repeats three times, once per card — a row-level title, not a singular hero, and shouldn't borrow hero-scale sizing. Checked real per-row titles (Airtasker, CVS Health, Jira) — all sit at 15-17px, not 20px+, matching iOS's own type-scale distinction between a one-time Title and a repeated list-row Headline. Locked at 16px. Rest of the scale (12px chip, 14px body/route/time, 15px button) checked and confirmed within normal bounds — the headline was the one actual offender.

**"In Progress" chip semantics corrected against Atlassian's Lozenge component (2026-09-21).** User asked why we weren't checking established enterprise design systems (Atlassian, Shopify, GitHub, Salesforce, Microsoft) instead of consumer apps — a fair critique, since CVFMS is enterprise/government software, not a consumer app, and Atlassian's design system was already a trusted source for desktop token verification (`06_DESIGN_QUALITY_PROCESS.md`) that had simply never been extended to mobile. Checked Atlassian's Lozenge documentation directly: it classifies "in progress" as an **Information** state (neutral, ongoing), reserving **Success** for "completed, approved, resolved" — a real semantic distinction. Cross-checked against CVFMS's own desktop rule and found it already makes this exact distinction (Component 3's Status Pill: "On Trip/Assigned → `color.brand.primary-subtle`, informational, not a judgment" vs. full `color.status.success`) — mobile's "In Progress" chip had been using success-green this whole time, semantically wrong by CVFMS's own existing rule, not just by Atlassian's. Fixed: "In Progress" now uses `color.brand.primary-subtle` (`#E6F2EB`/`#006837`), a third distinct shade in the green family. Also added a chip max-width/truncation rule from the same reference. (Note: Uber's Base design-language page was also checked per the user's link, but it's a JS-rendered SPA that returned no usable content via fetch — flagged honestly rather than guessed at.)

**Mobile research pass finally run (2026-09-21) — user correctly pointed out mobile never got what desktop got.** Desktop's design system was built on a deliberate, upfront `ui-ux-pro-max` research pass (§0) before any screen was built; every FRAME-07 decision since has been reactive instead — fixing one complaint or borrowing one screenshot pattern at a time. Ran the equivalent pass for mobile via `ui-ux-pro-max`'s CLI tool. Confirmed independently: Corporate Trust (Lexend + Source Sans 3) is still the top typography match for a fresh "government/accessible" query, and Flat Design/Minimalism & Swiss Style both match the existing flat-card direction. **New, corrective finding: no emoji as icons, anywhere.** Flagged twice in the source material as a common unprofessional-UI mistake. Every FRAME-07 prompt written this session has used emoji (🔵🟢👤🚗🔔🕐🆘) as icon placeholders — if the Figma agent rendered these literally rather than resolving to proper SVG icons, this is a likely real contributor to the "inconsistent icons" and "not world class" feedback across every render reviewed. Added as a standing rule in `03_MASTER_DESIGN_SYSTEM.md` §B4: prompts must say "use an SVG icon depicting X, not emoji" explicitly going forward. Also added a formal 8px minimum gap rule between adjacent touch targets (Accept/Decline pair), found via this same research pass, not previously stated anywhere. **Clarified for the record: CVFMS never actually adopted Uber's design system as a base** — earlier work borrowed individual patterns from Uber-family apps (Grab, DoorDash, inDrive) via Mobbin, one at a time, which is a different thing from adopting a formal base system; this research pass is the closer equivalent to what desktop actually had.

**Chip sizing and hierarchy contrast fixed (2026-09-21), checked against inDrive's Order screen.** User: icons are fine now (reversing the earlier "remove them" rule), but chips are too big and overall hierarchy is weaker than inDrive's. Checked directly: inDrive's price is dramatically larger than its supporting chips/rows, and its chips are small and text-hugging. Fixed: status chip now reuses the desktop Status Pill's exact sizing (20px height, 8px padding, `radius.sm`) instead of an unspecified/oversized chip; destination headline bumped from 18px to 20px to widen the gap against 14px body text. Also noted inDrive differentiates its two location dots by shape (solid vs. ringed), not just color — worth applying if a destination dot is ever reintroduced. Full detail in `03_MASTER_DESIGN_SYSTEM.md` Component 9.

**Render of the locked Component 9 checked (2026-09-21) — one critical regression, plus real fixes.** Good news: the render independently arrived at destination-as-headline with time as a secondary right-rail value, which is actually better than Component 9's original hero-time rule and got adopted as the new locked spec (it also resolved a contradiction this doc never caught — an older section already said "destination is the dominant identifier," which the hero-time rule had silently overridden). **Critical problem: Card 2 replaced its Accept/Decline buttons with a "Tap to respond" text link** — this undoes the entire reason Home was rebuilt as a list (actions visible on the card, not behind a tap). Also found: the person/vehicle icons Component 9 said to remove were still present; an unrequested divider line appeared, contradicting the "no dividers, whitespace only" principle already adopted; and the "Scheduled" card's contrast looked low enough to risk failing this project's own AAA target. All four now written into Component 9 as explicit, named rules (not just described in a screen-specific note) so they don't recur. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**Root cause finally addressed: a locked "Mobile Assignment Card" component, not another round of element-by-element patching (2026-09-21).** User named the actual pattern: "our biggest issue is hierarchy, font sizes, weights, spacing, color, buttons" — all still having problems despite many individually-correct fixes. Root cause: every fix (dot markers, chips, hero time, status badges, differentiation icons) solved a real problem in isolation, but nothing ever governed all of them together, so the cumulative result kept drifting. **Fix: added `03_MASTER_DESIGN_SYSTEM.md` Component 9 — a fully locked mobile card spec** with exactly 4 structural groups, 4 type sizes total, 3 spacing values total, a closed color list, and exactly 2 button states — no line item left as agent discretion. This required cutting several earlier additions that were each individually justified but collectively added back the visual variety the fix needed to eliminate: the passenger-count chip (folded into plain detail-block text), the person/vehicle differentiation icons, and the status icon's circular badge. `04_FIGMA_SCREEN_BLUEPRINT.md` §8's FRAME 7A layout rebuilt to match Component 9 exactly. This is the most significant structural correction in the FRAME-07 work so far — everything before it was patching symptoms.

**Status treatment reversed (2026-09-21) — left-edge accent bar replaced with a tinted chip, after checking real best-in-class execution.** User said the build still wasn't "world class" despite being structurally correct. Checked [CVS Health's Visit Checklist](https://mobbin.com/screens/5367bf1b-68be-434d-825e-33fa368bfd42) and [Jira Cloud's task list](https://mobbin.com/screens/f206f339-e758-44fe-828e-a5c8644da613) directly — both use a tinted status chip (colored background + text), not a left-edge bar, and it reads as more polished on direct comparison. **Reversed the earlier call to keep the left-edge bar as a "CVFMS signature element"** — that reasoning was sound at the time, but concrete comparison against real execution outweighs defending a prior decision. Also fixed: the status icon now sits in a soft tinted circular badge (likely the real fix for the earlier "icons look inconsistent" complaint — icons floating loose at different implicit sizes read as less considered than uniformly-contained ones); the passenger-count chip now matches this same tinted style instead of a bare outline (the card was mixing two chip languages); the vehicle icon was flagged as unclear (looked like a steering wheel, not a car) and needs a clearer glyph. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**3 elements borrowed from inDrive and Airtasker (2026-09-21)**, after the user said the build still wasn't satisfying: (1) colored dot markers (blue/green) for origin/destination, replacing the "→" arrow — an established ride-hailing convention, doesn't reopen the no-navigation-app decision since nothing is computed; (2) a new "hero time" treatment — time is now the single most visually prominent element on the card (new `type.hero-mobile` token, 22px/700, added to `03_MASTER_DESIGN_SYSTEM.md` §B3), the equivalent of Airtasker's bold price; (3) a headcount fact-chip ("[ 3 passengers ]"), fully worded, borrowed from inDrive's compact-fact chip style. Vehicle info stays a plain text line, not a chip — chips suit single short values, not a compound one like model+reg-plate. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**First render of the type/spacing-scale rebuild checked (2026-09-21) — 2 defects, one significant.** (1) Accept and Decline rendered as two visually identical outline buttons, undoing the earlier hierarchy fix — Accept must be filled/dominant, Decline outline/secondary. (2) **Vehicle assignment info (reg plate, model) was missing from every card entirely** — a real functional gap traced back to the Home-as-list rebuild: the old design had a separate Vehicle card, and when Home was consolidated into a compact list, nobody explicitly decided where vehicle identity should live — it just silently disappeared, unnoticed until this render surfaced it. Fixed: added a compact "Vehicle: [Model] · [Reg Plate]" line to every card, including pending ones (a driver needs to know which vehicle they'd be responsible for before deciding to accept, not just after). Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**Mobile type/spacing scale defined for the first time (2026-09-21) — user: "ours seem big and with no system."** Root cause: no explicit mobile type/spacing scale had ever existed; FRAME-07 prompts described sizes qualitatively ("bold," "small") without pinned values, so renders defaulted toward Material 3's own generous type scale — same category of issue as the earlier "generic M3" finding (that time it was shadows/radii, this time size). **Fixed by adding `03_MASTER_DESIGN_SYSTEM.md` §B3**: a real mobile type scale reusing desktop tokens wherever they fit (`type.label`, `type.body`, `type.caption` unchanged) plus two new mobile-specific tokens (`type.card-title-mobile` 16px/600, `type.button-mobile` 15px/600) — deliberately smaller than M3 defaults. Spacing reuses the existing 8pt scale exactly (16px card padding, 8px internal gaps, 12px between cards, `radius.lg` 12px corners) with one new hard rule: **buttons are 48px tall, treated as a ceiling as well as a floor** — the accessibility minimum already satisfies the touch-target requirement, so taller buttons were just adding to the "big" problem, not adding accessibility value. Synced to `.agents/rules/master-design-system.md`.

**3 more clarity fixes on the assignment cards (2026-09-21).** User caught three remaining ambiguities: (1) SOS was rendered as literal "SOS" text in a circle, which defeats the point of an icon — it still requires reading/decoding an acronym; fixed to a real emergency pictogram. (2) The headcount icon+bare-number ("👥 3") relies on the viewer already knowing that specific convention, which isn't a safe assumption for this audience; spelled out as "3 passengers" instead. (3) The requester name+department had no role label at all — genuinely unclear whether that person is the requester, a passenger, or someone else; fixed to "Requester: [Name] · [Department]". All three point the same direction: compactness only helps if it's still unambiguous. **Follow-up correction: the header's top-left slot (beside the greeting) should be the driver's own avatar, not SOS** — that position naturally reads as "who am I," reinforcing the personalization already built for this screen (greeting, Profile, language toggle), and SOS was occupying it instead. Moved SOS to the top-right corner (empty since the sync badge was removed earlier) — still persistent across every FRAME-07 screen, just not displacing personal identity. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**First render of the new list-based Home checked (2026-09-21) — structurally correct, 4 polish fixes.** The architecture itself (urgency-ordered cards, per-card actions, no call icon) rendered correctly. Found: (1) card status labels missing the letter-spacing already defined in `03_MASTER_DESIGN_SYSTEM.md`'s `type.label` token — an existing spec being skipped, not a new rule; (2) left-edge accent bars have hard corners clashing with the card's rounded corners; (3) the "Scheduled" card has zero accent treatment, reading as unfinished next to two color-coded cards, rather than intentionally neutral; (4) Accept/Decline buttons unevenly proportioned in a way that looks accidental. Full detail and fix prompt in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**Content-type visual rule established for FRAME-07 (2026-09-21) — the real fix behind "the cards are confusing."** User flagged that it was unclear what's actually important/actionable on the driver screens. Audit: only 3 elements on FRAME 7A are genuinely actionable (View Details chevron, call icon, primary CTA), yet nearly every informational row also carried a leading icon with similar visual weight — nothing distinguished "tap me" from "here's a fact." **Standing rule, applies to all 4 FRAME-07 sub-screens:** actionable elements are the only things in Civic Green/circular treatment; status (pills/badges) keeps its own distinct treatment; flagged/warning content (special requirements) gets its own visually distinct strip, not a bulleted row; plain informational content drops decorative icons entirely — muted text only, nothing implying tappability. Applied to FRAME 7A's layout in `04_FIGMA_SCREEN_BLUEPRINT.md` §8 — check this rule against 7B/7C/7D as they're built or revisited, since the same over-iconing risk applies there too.

**Trip Card given a deliberate IA pass (2026-09-21), replacing reactive field-adding.** User pushed to properly consider "what goes on this card" after several rounds of one-off additions (destination, time, call icon, View Details, text wrap) — the pattern itself was a symptom: fields like "Purpose: Drainage Inspection" had shown up in a render without ever being a deliberate decision. Pulled the actual SRS §5.4 field list and tiered every field explicitly (card face / behind View Details / not shown), full table in `04_FIGMA_SCREEN_BLUEPRINT.md` §8. **Two real gaps closed:** "expected return" and "special requirements" were never specced anywhere before this pass despite being named fields in §5.4. Special requirements now conditionally promoted to the card face (only rendered when a request actually has one, same opt-in principle as delta chips) since burying something like a wheelchair-access need behind a tap is a real operational risk, not just an IA nicety.

- **Vehicle Allocation Table**, **Grace's 4 action modals**, and the **`status_reason_code` schema note** — still open, unchanged since the original restart.
- **Vehicle-detail view** (reached from a row click on the All Vehicles table) — flagged as a follow-on gap, not yet specced or built.
- **New doc: `10_DASHBOARD_DESIGN_KNOWLEDGE.md` (2026-09-16)**, synthesized from 3 external dashboard-UX articles (UX Collective, Pencil & Paper, Aufait UX — full citations in the doc), read in full and diffed against CVFMS's existing decisions rather than treated as a generic checklist. Most principles confirmed things CVFMS already does independently (good signal the underlying method was sound). A sharper five-second-test procedure (show 5s, hide, ask what they recall — failure if they recall layout/color before the actual metric) folded into `06_DESIGN_QUALITY_PROCESS.md` §1; **saved views** (a named filter/view configuration a user can return to) flagged as a candidate enhancement for FRAME-02 and FRAME-05's filter rows, not yet committed. One alternative explicitly considered and rejected: a blue/orange status palette instead of red/amber/green for financial metrics — kept red/amber/green system-wide for one consistent status language across all 5 personas, reasoning recorded in the new doc §2.8 so it isn't re-litigated.
- **New doc: `11_COMPONENT_REBUILD_INSTRUCTIONS.md` (2026-09-16) — applies to a SEPARATE Figma file, `YdYyvLxyN07dERN7bn66MS`, not the main CVFMS file (`bnxWZCzNtbjM0ulb886hXo`) all other docs reference.** The user shared a detailed component-quality audit (Sidebar, Top Bar, Status Pill, KPI Tile, Checklist Row all lacking proper component properties — e.g. Status Pill has no text-override property, Sidebar has zero properties despite being used on every screen). This session was given Viewer-only access to that file (to avoid consuming a paid Editor seat) and independently verified several claims directly via `get_design_context`/`use_figma` before hitting the View seat's low MCP tool-call rate limit mid-investigation. **Real complication found and documented:** the Sidebar situation is worse than "one component needs properties" — there are 8+ distinct sidebar frames/instances scattered across the file (some may not share a common master component) plus 10+ more one-off duplicates on a "drafts" page, meaning consolidation has to happen before property-adding makes sense. **Important process note for future work on this file:** an earlier pass of this same investigation was mistakenly run against the WRONG file entirely and produced confident-looking but incorrect specific numbers (a KPI Tile padding/sizing claim). `11_COMPONENT_REBUILD_INSTRUCTIONS.md` labels every finding [VERIFIED] or [FROM AUDIT] specifically because of that near-miss — maintain that discipline on any follow-up work here. Whoever continues this needs Editor access (or a higher-rate-limit seat) to finish verifying KPI Tile and Checklist Row, which the View-seat rate limit prevented from being checked this session.
- **REVERSED (2026-09-16): loading/empty/error states (skeleton screens etc.) are NOT wanted.** The doc above initially flagged missing loading/empty/error states as a gap to fix; the user has since explicitly said to keep designs simple and avoid adding things like skeleton states. `09_PATTERN_LIBRARY.md` §11 and its pre-flight checklist item 9 have been updated to reflect this — don't add loading/empty/error-state specs to new prompts unless the user asks for one explicitly on a specific screen. The Dispatch Override Review prompt (below) was rewritten without it for this reason.
- **KPI Tile delta chips changed from default to opt-in (2026-09-16), following a token-efficiency question that led to a real design-direction correction.** User asked how to build more efficiently (fewer tokens per Figma prompt) and separately pointed at Airwallex/Uxcel/User Interviews dashboards as the simplicity bar to aim for. Checked both Airwallex's and Uxcel's actual dashboards directly (not from memory) — both converge on one accent color total, plain black KPI numbers with zero default decoration, flat cards, minimal chrome. Our prior spec mandated a colored delta chip on every KPI tile by default — genuinely more decoration than either reference uses. **`03_MASTER_DESIGN_SYSTEM.md` Component 2 and `09_PATTERN_LIBRARY.md` §3 updated: delta chips are now opt-in, named explicitly only when a number's meaning depends on a comparison (Sarah's target-comparison case), not assumed automatically.** Does not retroactively change FRAME-01/FRAME-04's already-built chips. This is also a direct token-efficiency win: the KPI row prompt fragment is shorter now that "delta as text next to a dot" isn't spelled out by default.
- **Token-efficiency findings for prompting the Figma agent (2026-09-16):** (1) reference-based prompting (`09_PATTERN_LIBRARY.md`'s header note) roughly halves prompt length — confirmed on the Dispatch Override Review prompt (2436 → 1105 characters) by saying "reuse FRAME-02's drawer/checklist pattern" instead of re-describing it. (2) **Untested idea, not yet adopted:** since the agent can resolve pattern references by name, the mandatory full-verbatim-nav-every-prompt rule (`06_DESIGN_QUALITY_PROCESS.md` §0C) could potentially be relaxed to a shorthand reference too ("same sidebar as FRAME-01") — but this rule exists specifically because the nav regressed twice from being referenced by shorthand before. **Do not relax this rule without testing it carefully first and confirming the render is fully correct** — a 3rd nav regression would cost more than the tokens saved. (3) Batching 2+ small related deltas (e.g. two similar modals) into one prompt, still under the 2000-character limit, may be more efficient than one prompt per screen — not yet tried, worth testing on the remaining 3 action modals (Maintenance Approval, Reallocate, Registry Edit).
- **Figma AI generation credits expired (2026-09-16), resolved by adding a new account as Editor on the same file** (`bnxWZCzNtbjM0ulb886hXo`) — no file/screen loss, same node IDs remain valid. Separately confirmed: this session's own `use_figma` Plugin API connection is independent of the user's Figma agent/generation credits — direct structural/style fixes can be made from this session even when generation credits are down. Used directly to fix a real, confirmed sidebar node (**"Sidebar-v2", node `229:895`**) that already existed in the file with most of the grouped-nav spec correctly built (8 pillars, connector line, chevron), but had two precise defects fixed directly via `use_figma`: (1) the connector line was misaligned ~8.5px left of the pillar icon's center; (2) the active sub-item chip ("Fleet Registry") stretched edge-to-edge instead of having inset padding. Both fixed with exact pixel values (not guessed) — see the session's `use_figma` calls for the precise before/after node properties. **This "Sidebar-v2" node is a further-advanced version of the sidebar than what earlier fix-prompt rounds targeted — check its current state directly before writing another sidebar prompt, since it may already have more of the spec correctly implemented than assumed.** This "Sidebar-v2" node turned out to belong to node `159:278`, the **Executive Briefing frame (Sarah)**, not FRAME-01 — found via direct inspection, not assumption. That frame also had two real regressions against settled decisions, both fixed directly via `use_figma`: (1) it had a Grace-style greeting header ("Good morning, Sarah") — the greeting pattern is explicitly reserved for FRAME-01 only (`03_MASTER_DESIGN_SYSTEM.md` Component 1) — replaced with the standard plain title ("Executive Briefing") + status subtitle ("County Executive: Sarah N. • Executive Dashboard Live") pattern used on every other work-surface screen; (2) the sidebar had "Fleet Registry" active under Vehicle Management instead of "Reporting & BI" under Fleet Analytics — fixed by cloning the Vehicle Management group's expand/sub-item structure onto Fleet Analytics (which had no expanded sub-items built at all), trimming it to the 2 real sub-items (Reporting & BI, Vehicle Expenses), and collapsing Vehicle Management back down. Confirmed via screenshot after the fix — both issues resolved, rest of the screen (KPI row, twin trend charts with the 85% target line, departmental drill-down) unaffected and matches spec.

**Root-cause finding (2026-09-16): 6 of 7 screens share one real Figma component, and its DEFAULT state was wrong.** Checking Grace's FRAME-01 directly (not assumed fixed) revealed its sidebar showed Fleet Analytics/Reporting & BI active — the exact same wrong state found on Sarah's screen, but this time via a shared component, not a copy-paste. Traced to the master component **`Sidebar-v2`, node `170:888`** — used as an INSTANCE by 6 screens: `fleet-operations-overview` (Grace), `dispatch-requisition-queue` (Daniel), `finance-cost-dashboard` (Miriam), `workshop-job-card-board` (Peter), `fleet-all-vehicles`, `fleet-live-map`. Only `executive-briefing` (Sarah) is a **detached, standalone frame**, not an instance of this component — which is why it needed the earlier by-hand connector-line/chip fix separately and won't receive future master-component fixes automatically. **Fixed at the master component level** (propagates to all 6 instances at once): collapsed Fleet Analytics back to its default closed state, expanded Vehicle Management with its real 4 sub-items (Fleet Registry active, Insurance/Compliance/Disposal plain), added the dark-green active-chip tint (`#173829`) and a correctly-positioned absolute connector line (avoided two failed attempts: an auto-layout-participating rectangle broke the flow, `layoutPositioning = 'ABSOLUTE'` set after `appendChild` fixed it). **Any per-screen active-item override still needs to be applied per-instance** (e.g. Daniel's screen should show Operations/Dispatch Management active, not the new Vehicle Management/Fleet Registry default) — the master fix corrects the *shared default*, it does not retroactively set the correct per-screen override on each of the 6 instances. **Next step: check each of the 5 remaining instance-based screens (Daniel, Miriam, Peter, All Vehicles, Live Map) directly and apply their correct per-screen active pillar/item as an instance override, per the table in `09_PATTERN_LIBRARY.md` §1.**
- **3 new template gaps identified (2026-09-15), not yet defined:** a plain **Form Drawer** (create/edit fields, no decision/checklist buttons — needed for Registry Edit), a **Picker-in-Drawer** sub-pattern (search/select a pending request — needed for Reallocate), and an undecided **Vehicle Detail** layout (drawer vs. full page — content volume may not fit a drawer). None of the existing `09_PATTERN_LIBRARY.md` templates cover these three; define them before writing prompts for the corresponding modals, per the same lesson learned from the fixed-pane-vs-drawer decision (define the pattern once, deliberately, rather than discover the gap mid-prompt).

**Role coverage — 5 of 16 SRS roles have Figma screens; all 16 are now documented as personas (updated 2026-09-16, see §9 below — this paragraph originally said 11 roles were "not yet even specced," which is now out of date for documentation, though still true for screens).** The SRS/architecture summary define 16 discrete functional roles (architecture summary §3). **Screens** exist only for the 5 flagship personas (Fleet Manager/Grace, Transport Officer/Daniel, Workshop Manager/Peter, Executive/Sarah, Finance Officer/Miriam) — chosen in the original persona doc as "the first design wave." **Documentation** (as of `01_USER_PERSONAS.md` v3.0) now covers all 16 roles — see §9 for the 11 newly-added Wave 2 personas (System Administrator, Fleet Officer, Driver, Mechanic, Fuel Officer, Storekeeper, Procurement Officer, HR Officer, Auditor, Department User, Approving Officer) and their design implications. **Do not conflate the two:** a role having a documented persona does not mean it has a screen queued next — the 5-flagship-first build order is unchanged. **This build-order scoping is a confirmed, deliberate decision as of 2026-09-15 (user: "keep building out the 5 flagship personas fully first, treat the other 11 as a known future phase"), not an oversight — but it has never been put to the product owner (Patrick Swift) directly.** Given Patrick is already actively directing scope (the pillar/menu regrouping instruction), whoever next has a chance to check in with him should confirm this deferral is actually correct, rather than assume the original 5-persona build scoping still matches his current priorities.

---

## 7. Practical Notes for Continuing This Work

- **Prompts to the user's Figma agent are structure-and-content only, no styling** — the user's explicit standing preference (2026-09-13): describe what components exist, their order, and their content, but not colors/type/spacing. The design system doc's tokens exist for whoever/whatever applies visual styling downstream, not to be pasted into every screen prompt.
- **Full 20-item nav list must be pasted verbatim into every single screen prompt** — never referenced by shorthand ("same sidebar as before"). This has already caused two real regressions (icon-only sidebar, sidebar dropping from 20 to 8 items) from being referenced by shorthand instead of restated. See `06_DESIGN_QUALITY_PROCESS.md` §0C and `09_PATTERN_LIBRARY.md` §1.
- **Two-pane screens: fixed pane vs. true overlay drawer is a deliberate per-persona decision, not a style choice.** High-volume/rapid-triage personas (Daniel) get a fixed pane so they keep queue visibility; low-volume/focused-investigation personas (Miriam) get a true dimmed drawer. Don't apply one pattern to both without checking the persona's actual job shape — see `09_PATTERN_LIBRARY.md` §2.
- **Page title slot: greeting block is reserved for FRAME-01 only** (the one true once-per-session landing screen); every other screen keeps a plain title + status subtitle. Don't extend the greeting pattern elsewhere without a fresh justification. See `03_MASTER_DESIGN_SYSTEM.md` Component 1.
- **Breadcrumbs are scoped to genuine drill-down detail views only** (e.g. "Dispatch Management → Request Detail" above a selected-item detail panel) — this system's nav is flat (20 top-level modules, no nested groups), so a breadcrumb anywhere else would be circular or imply structure that doesn't exist. See `09_PATTERN_LIBRARY.md` §10.
- **Untitled UI (a separate Figma file, "❖ Untitled UI – PRO STYLES v6.0") was investigated (2026-09-14) as a possible source of pre-built components to speed up remaining work.** Confirmed: it's a generic base-primitives + marketing-page kit (Badges, Buttons, Inputs, Tooltips, Icons, blog/content page blocks) — no dashboard, table, sidebar, or KPI-card patterns found in the pages/searches checked so far. The user pushed back, saying it "has everything" — this was not fully resolved before the session ended; **whoever picks this up next should ask the user for a specific node URL or page name showing the dashboard/table components they're referring to**, rather than repeat the same page-list/search-based check that already came back empty twice. If it does have those patterns, the plan is to restyle them with CVFMS tokens rather than rebuild from scratch; if it doesn't, continue treating composed patterns (App Shell, Data Table, Kanban, etc.) as CVFMS-original per `09_PATTERN_LIBRARY.md` §0.
- **Mirror every design system change** to `.agents/rules/master-design-system.md` (verify it stays a `cp` mirror of `docs/03_MASTER_DESIGN_SYSTEM.md`, not edited independently).
- **Before generating any frame**, run the full pre-generation checklist in `06_DESIGN_QUALITY_PROCESS.md` §1 — Mobbin references, NN/g heuristics, five-second rule, component enumeration, decorative-element test, token spot-check — all before the first prompt, not after a bad render.
- **When First Draft correction prompts don't land after two focused attempts**, switch to `use_figma` directly per `06_DESIGN_QUALITY_PROCESS.md` §0.
- **The Figma file is actively edited between sessions/calls** (by the user and/or their Figma agent) — node IDs recorded in a past conversation or doc may no longer resolve, or may point to different content. Always re-fetch (`get_metadata` or `get_screenshot`) immediately before acting on a node ID rather than trusting a previously-recorded one.
- **This workspace has no git repository.** The `docs/archive/` copy is the only safety net for the prior doc version — if anything here needs to be reverted, that's where to look; there is no other undo mechanism.

---

## 8. Card/Table Separation Defect Found and Fixed at the Spec Level (2026-09-16)

The user flagged, from rendered screenshots (Driver Management, All Vehicles), that KPI tiles and data tables had no clear visual separation from the page background — comparable Mobbin dashboards don't have this problem. Root cause: `color.neutral.surface` (`#FFFFFF`) vs `color.neutral.bg` (`#F8FAFC`) is a real, correct token pair on paper, but only ~3% apart in lightness — far too subtle to read as a distinct surface once rendered, especially with the system's flat-card-no-shadow direction and no border previously specified. The KPI Tile (Component 2) and Data Table (Component 6) specs never actually mandated a border or any other separation treatment — an omission, not a wrong value.

**Fix, applied at the spec level so it doesn't recur:** `03_MASTER_DESIGN_SYSTEM.md` Components 2 and 6 now mandate a visible `1px solid color.neutral.border` on every card-shaped surface (KPI tiles, table containers, filter controls), synced to `.agents/rules/master-design-system.md`. `09_PATTERN_LIBRARY.md` §3 and §6 prompt fragments updated to include the border explicitly, and pre-flight checklist item 10 added so this is checked before generation, not caught after a bad render. **Both already-rendered screens (Driver Management, All Vehicles) still need a fix prompt run against them** — this was a spec-level fix, not yet applied to existing frames.

**Correction (2026-09-18):** the initial spec text cited "comparable Mobbin references" for the border rule without having actually re-checked one in that session — an unverified claim presented as if benchmarked, caught when the user directly asked "which mobbin reference have you checked?" **Fix:** searched Mobbin and confirmed directly against [Airwallex's own dashboard screen](https://mobbin.com/screens/f0165978-3117-45a7-88f0-1a8a97007275) (the same app already used for this project's KPI delta-chip decision) — every stat tile and section card there does have a visible thin gray border on white fill against a light-gray page background, matching the fix as specced. `03_MASTER_DESIGN_SYSTEM.md` Component 2 updated to cite this real, checked reference instead of the earlier vague "comparable Mobbin references (Airwallex, Linear-style dashboards)" phrasing. **Lesson: don't cite "benchmarked against X" unless X was actually re-opened and checked in that session** — a plausible-sounding reference is not the same as a verified one, and the user caught this by asking directly rather than taking the citation on faith.

**Open gap surfaced while writing this section, not yet resolved (2026-09-18): "Driver Management" is an 8th rendered screen with no blueprint entry.** The two screenshots the user shared to report this defect were labeled **Driver Management** (a Driver Registry table under the Driver Management pillar — 184 drivers, licence class/expiry columns, HR Liaison status line) and **Fleet Registry/All Vehicles** (the latter matches an already-specced screen — `04_FIGMA_SCREEN_BLUEPRINT.md` §2 confirms "Fleet Registry" is the All Vehicles tab on FRAME-01, not a separate frame). **Driver Management does not appear anywhere in `04_FIGMA_SCREEN_BLUEPRINT.md`'s 7-frame demo set (§6 above) or its frame directory** — it exists in Figma (someone built/prompted it) but was never specced through this doc set's normal pre-generation process (`06_DESIGN_QUALITY_PROCESS.md` §1), and its own detail (an "HR Liaison: Alice Njoroge" status line, tabs/sub-items under the Driver Management pillar) was never reasoned from a persona goal the way the other 7 screens were. **This needs to be resolved, not just patched:** either (a) retroactively write a blueprint entry for it now that it exists, tracing it to a persona (Grace's Driver Management sub-item, or a stand-in for the not-yet-built Fleet Officer/HR Officer Wave 2 personas — see §9), or (b) ask the user directly where this screen came from and whether more untracked screens like it exist. Don't assume it's "fine because it's already built" — the same missing-spec pattern is exactly what caused the card/border defect in the first place (a component built without its separation rule ever being written down).

## 9. Personas Expanded to All 16 SRS Roles (2026-09-16)

The user pasted the SRS §4 role table in full and asked whether Driver and other roles were missing from `01_USER_PERSONAS.md`. They were — the doc covered only the 5 flagship roles by deliberate original scoping (named dashboard tier or high-frequency workflow). Asked whether to add just Driver or keep the deferral, the user's answer was broader than either option: **"add to our document all personas."**

`01_USER_PERSONAS.md` is now v3.0: all 16 SRS roles have a documented persona, using the same `ui-ux-expert` journey-mapped method as the original 5 (SRS-cited Goals & Motivations, a Journey table, a Design Implication). The 11 new "Wave 2" personas are: System Administrator, Fleet Officer, Driver, Mechanic, Fuel Officer, Storekeeper, Procurement Officer, HR Officer, Auditor, Department User, Approving Officer. The Persona Comparison Matrix now has all 16 rows.

**Important distinction — documentation coverage vs. build queue:** this does NOT change which personas have Figma screens. The 5 flagship personas remain the only ones built (`04_FIGMA_SCREEN_BLUEPRINT.md`, the 7-screen demo set). The Wave 2 personas are documented so the full picture exists and design implications are traceable, but none has a screen yet. Notably, the **Driver persona explicitly flags that it should NOT be designed as a scaled-down web screen** — SRS §11 puts Driver on a separate mobile/PWA-first application, offline-capable, which is a materially different design problem from every desktop-oriented frame built so far. If/when Driver screens are prioritized, expect a new blueprint section, not an extension of `04_FIGMA_SCREEN_BLUEPRINT.md`'s existing frame format.

A few Wave 2 personas surfaced real, previously-implicit cross-persona dependencies worth remembering:
- **HR Officer → Daniel (Transport Officer):** HR Officer's employment/licence data lag directly feeds BR-002/BR-003 (driver active & employed, licence valid) at Daniel's dispatch gate. If HR data goes stale, Daniel's gate check can pass on inaccurate assumptions.
- **Storekeeper → Peter/Mechanic:** the parts-visibility gap already identified in Peter's Wave 1 persona (`09_PATTERN_LIBRARY.md`'s Kanban stock-status pill) has its upstream root in the Storekeeper's own inventory accuracy — this is one problem seen from two personas, not two separate problems.
- **Department User → Daniel/Miriam:** the "no visibility into a multi-step approval workflow" friction, previously only described from Daniel's and Miriam's side, actually originates at the Department User's request-submission stage. If a "my requests" status view is ever built, it closes this gap at the source rather than downstream.

## 10. Component Rebuild Instructions — Separate Figma File (2026-09-16)

The user provided a detailed manual audit of 5 base Figma components (Sidebar, Top Bar, Status Pill, KPI Tile, Checklist Row) — missing properties, hardcoded values, missing icons — and asked for rebuild instructions so these are "well built, accessible, and very good design wise." **This audit is against a different Figma file than the one used throughout docs 01-09**: `YdYyvLxyN07dERN7bn66MS`, not the main `bnxWZCzNtbjM0ulb886hXo`. Both files are confusingly named the same ("CVFMS Fleet Management Design System") — **always confirm which file a claim is about before trusting specific numbers.** An earlier verification pass in this session was mistakenly run against the wrong file and produced a confident but incorrect contradiction of the audit's KPI Tile findings; this is why `11_COMPONENT_REBUILD_INSTRUCTIONS.md` labels every finding **[VERIFIED]** or **[FROM AUDIT]** rather than presenting everything as equally confirmed.

Access to this second file required a cost tradeoff: the user asked how to verify without paying for another Editor seat, so this session used **Viewer access** instead (usually free, but with a much lower MCP tool-call rate limit — hit mid-investigation). Result: Sidebar and Status Pill were independently verified; Top Bar's existence was confirmed but its properties were not; KPI Tile and Checklist Row rely entirely on the user's audit, unverified. Full findings, priority order (Sidebar → Top Bar → Status Pill → KPI Tile → Checklist Row), and the open question of whether 6+ scattered "Sidebar-v2" instances share one true master component are in `11_COMPONENT_REBUILD_INSTRUCTIONS.md`. **Whoever picks this up next should have Editor access on `YdYyvLxyN07dERN7bn66MS`** to finish verification and apply fixes.

## 11. Primary Profiles, 6-Stage Lifecycle & Demo Architecture (2026-09-18)

Following a comprehensive audit of `CVFMS Primary profiles.docx` against the SRS and rendered Figma designs, the project formally adopted the **11 Primary User Profiles** architecture and locked in key governance rules:

1. **The 11 Primary Operational Profiles + Permission Modifier Model:**
   - Instead of 16 unconstrained roles, the system consolidates into 11 distinct operational workspaces: **Executive/Management, Fleet Manager, Transport Operations, Fleet Operations, Requester, Driver, Workshop Manager, Mechanic, Finance, Audit, Administrator**.
   - **Approver is modeled as a permission overlay, not a standalone profile.** Approvers are Department Heads, Sub-County Admins, or Fleet Leads with an assigned approval limit and workflow scope. Crucial maker-checker rule: **strictly no self-approval** (PFM Act 2012 internal controls).
   - The 4 remaining SRS roles are explicitly mapped: Fuel Officer (under Fleet Operations/Finance), Storekeeper (under Workshop Operations), HR Officer and Procurement Officer (as integrated support modules feeding driver eligibility and asset acquisitions).

2. **The 6-Stage Closed-Loop Demo Lifecycle:**
   - Rather than presenting disconnected screens, the upcoming demo will trace one continuous operational lifecycle using shared data (`REQ-2024-0851`, vehicle `KBZ 442A`, driver `Joseph Mutua`, starting odometer `142,850 km`):
     $$\text{Requester (Mary)} \longrightarrow \text{Approver (Director)} \longrightarrow \text{Transport Ops (Daniel)} \longrightarrow \text{Driver Mobile (Joseph)} \longrightarrow \text{Fleet Ops / Map (Grace)} \longrightarrow \text{Auditor (Immutable Log)}$$

3. **Standing UI & Governance Decisions (Locked 2026-09-18):**
   - **Auditor vs. Administrator Strict Separation:** The Auditor is an independent, read-only evidence and forensic review profile (cannot make business or configuration changes). The Administrator configures users, roles, organizational hierarchy, and workflows (has no operational transaction/dispatch buttons). These must never be merged into a single surface.
   - **Hide Raw `BR-001–005` IDs from the UI:** End-user screens must display clear, human-readable labels (e.g. "Dispatch Readiness: 4 of 5 checks passed", "Insurance Policy Active", "Vehicle Availability") rather than raw specification codes.
   - **Configurable Approval Wording:** Approval workflows must not assume every requisition checks financial budget. Routine departmental pool travel is an "Operational/Administrative Authorization", while specialized field trips with per diems/activity votes carry "Budget Commitment" sign-off.
   - **Driver Journey Bookending (Start + End Trip):** The mobile driver journey must bookend both beginning and completion of a job:
     - **Trip Start:** Pre-trip walkaround inspection checklist + Initial odometer capture (`142,850 km`) + "Start Journey" (activates GPS).
     - **Trip End:** Closing odometer capture (`142,914 km`) for automated net distance calculation + defect note + "Complete Trip" (releases vehicle back to available pool).

---

## 12. Current Status, Screen Progress & Next Agent Action Plan (2026-09-18)

### Current Screen Status (Session Exit State):
1. **FRAME-01 (Grace / Operations Overview) — [RE-RENDERED & VERIFIED]:**
   - **Status:** Gold-standard finish achieved.
   - **Landed Fixes:** Operations pillar is expanded with the dark green active chip (`#173829`) on "Fleet Overview"; missing vehicle registration IDs (`KBZ 442A`, `KCB 119B`, `KDA 330C`, `KCE 558A`) restored in Recent Activity; 1px card borders cleanly applied.
   - **Minor Polish Queue (Non-blocking):** Clean up map preview AI artifact text ("Fls Aveliable / Fleet on trips"), deduplicate Card 2 subtitle, replace bottom-left initials "PM" with "GM", equalize container heights with Coming Up.

2. **FRAME-02 (Daniel / Transport Operations — Dispatch Queue) — [PROMPT READY]:**
   - **Status:** Prompt finalized in conversation and ready to execute.
   - **Key Inclusions:** Top-right profile pill includes role title under name (`Daniel Otieno / Transport Operations Officer`); left rail has Operations expanded with `Dispatch Management` active; right-hand gate checklist uses human-readable labels ("Dispatch Readiness: 4/5 Checks Passed", "Insurance Policy Active", "Driver Licensed & On Duty", "Vehicle Availability"); fixed split-pane layout preserved.

3. **FRAME-07 (Joseph Mutua / Driver Mobile App — 3 Frames) — [PROMPT READY]:**
   - **Status:** Prompt finalized in conversation and ready to execute.
   - **Component Architecture:** Uses **Material 3 (M3) Component Anatomy** (M3 Outlined Cards, M3 Small Top App Bar, M3 Two-Line List Items, M3 Bottom Action Bar) skinned with **CVFMS Design Tokens** (Civic Green `#006837`, Lexend + Source Sans 3, pure white surface, 1px `#E2E8F0` borders, 48px+ touch targets).
   - **Home Screen Anatomy:** Tailored to the driver's mental model ("Today's Job" card, requester Mary Akinyi contact, assigned vehicle KBZ 442A in Bay 4, 52px CTA `Start Pre-Trip Inspection`, quick utility chips for Fuel/Breakdown/SOS, 3 dynamic shift states).
   - **3 Frames:** Frame 7A (Home & Assigned Trip), Frame 7B (60s Walkaround Checklist), Frame 7C (Start Trip `142,850 km` + End Trip `142,914 km` bookends).

4. **System-wide Profile & Role Labeling Rule — [LOCKED]:**
   - All user identity pills across top bars must include the user's formal role title directly beneath their name (e.g., `Grace M. / County Fleet Manager`, `Daniel Otieno / Transport Operations Officer`, `Joseph Mutua / County Driver`, `Miriam Chebet / Finance Officer`, `Sarah N. / County Executive`).

---

### Immediate Action Plan for the Next Agent:

1. **Step 1:** Run the finalized structure-and-content prompt for **FRAME-02 (Transport Operations — Daniel)** in Figma. Check render against the human-readable checklist and active sidebar spec.
2. **Step 2:** Run the finalized 3-frame prompt for **FRAME-07 (Driver Mobile PWA — Joseph)** in Figma. Verify 390px viewport, M3 card layout, and Start/End odometer bookends.
3. **Step 3:** Draft and run the prompt for **FRAME-08 (Requester Portal & Approver Review)**:
   - Mary Akinyi submitting `REQ-2024-0851` for Public Works.
   - Department Supervisor's inline approval drawer (with configurable operational clearance wording and no-self-approval rule).
4. **Step 4:** Draft and run the prompt for **FRAME-09 (Statutory Audit Explorer)**:
   - Immutable read-only table displaying the full custody chain of `REQ-2024-0851` (submission $\rightarrow$ approval $\rightarrow$ dispatch override $\rightarrow$ driver trip execution) with SHA256 hashes and Auditor-General export.
5. **Step 5 (Final Polish):** Wire Figma prototype hotspot links connecting the 6 stages for an unbroken, interactive demo walkthrough.

---

## 13. FRAME-07 Home Screen (Mobile) Rebuilt as a Locked Component — Component 9 (2026-09-21 to 2026-09-22)

**§12 above is stale on FRAME-07 specifically** — the M3-card single-"Today's Job"-card model it
describes was replaced entirely. Home is now an urgency-ordered **list** (in-progress → needs
response → scheduled), each card with its own scoped action(s), matching the same list pattern
already proven for Grace's Needs Attention (`09_PATTERN_LIBRARY.md` §4). Full spec:
**Component 9 — Mobile Assignment Card** in `03_MASTER_DESIGN_SYSTEM.md` (mirrored to
`.agents/rules/master-design-system.md`), plus the matching ASCII mockup in
`04_FIGMA_SCREEN_BLUEPRINT.md` §8, FRAME 7A.

**Why the rebuild happened:** repeated render rounds kept failing on hierarchy, spacing, button
sizing, and color even after individually-justified fixes — because no single rule governed all of
them together. Component 9 is the fix: one closed, exact spec (4 structural groups, 4 type sizes,
3 spacing values, a closed color list, 2 button states) instead of ongoing ad hoc patching.

**Notable resolved decisions, all detailed with Mobbin citations in Component 9 itself:**
- SOS removed entirely (no SRS grounding) → replaced with a notification bell (SRS §5.23), badge
  uses `color.status.critical` as the one deliberate color exception.
- Route visual is a dot-connector-dot timeline. **Reversed twice on origin/destination
  differentiation — see §13e below for the final, current call (colored dots, not shape-only).**
- "One main green CTA" is scoped **per-card**, not per-screen (each card is an independent
  decision); guardrail is max 2 visible filled-green CTAs at once, with a "View N more pending →"
  row for overflow — never hiding a pending card.
- Collapsing header on scroll (native Large Title pattern): expanded state adds only breathing
  room/type size, never new content; collapsed state drops to just the name at 16px/700.
- County branding (landmark photo + emblem in the expanded header) is an explicit, acknowledged
  exception to this project's minimalism — real per-county asset-sourcing dependency flagged, with
  a plain-gradient fallback required for any unconfigured county. **Emblem/crest still not rendered
  in any build as of 2026-09-22** — needs its own follow-up Figma prompt.

**Known, named recurring defect — appears fixed as of the 2026-09-22 render (§13d), but watch for
recurrence:** the Accept button had rendered as flat gray instead of filled `#006837` across
roughly 4 separate render rounds despite explicit fix instructions each time. Possible cause:
Figma-agent component reuse defaulting to the wrong variant. The render checked in §13d finally
shows it filled green — treat this as resolved but not proven stable until it survives one more
render round untouched.

### 13a. Three follow-up fixes, 2026-09-22 (buttons, status chip, page title)

User asked to re-check three specific things against Mobbin rather than patch them blind:

1. **Buttons were sized like a rare high-stakes confirmation, not a routine list decision.**
   Checked against American Airlines' Review screen (compact, pill-shaped, content-hugging
   Undo/Change buttons) vs. UNIQLO's Delete Account screen (correctly big, full-width — but a rare,
   once-ever action). **Fixed:** height stays at 44px (the actual accessibility touch-target
   minimum, corrected down from an earlier incorrect 48px), but shape/width now depends on context —
   **solo primary** (nothing paired against it, e.g. "Start Pre-Trip Inspection") stays full-width/
   `radius.md`; **paired primary + secondary** (Accept/Decline) is now pill-shaped and
   content-hugging, not stretched to a fixed % of card width.
2. **Status chip container dropped entirely.** Checked real apps and found the split is genuine —
   some use small chips (Alan, SHEIN), just as many use plain colored text with no container at all
   (OKX's "Pending release," Yami's "Cancelled"). The chip's background tint was never doing the
   "never color alone" accessibility job — the text label alone already satisfies that. **Fixed:**
   status is now plain colored, uppercase, tracked (+0.02em) text, no background/border/padding.
3. **"Assignments" page title was too big, competing with "Joseph" for dominance.** Same "two
   competing headlines" problem already solved inside individual cards, recurring one level up at
   the page. **Fixed:** "Assignments" now renders at `type.section-title` (18px/600), one clear
   step down from the header's name, functioning as a plain list-section label.

All three are now closed in Component 9 and mirrored to `.agents/rules/master-design-system.md`;
the FRAME 7A ASCII mockup in `04_FIGMA_SCREEN_BLUEPRINT.md` has been updated to match. A
consolidated Figma re-render prompt covering all three fixes together is the next thing to hand to
whoever runs the next render.

### 13b. Still open for FRAME-07
- County emblem/crest icon: still missing from every render so far, needs its own prompt.
- Page title ("Assignments") still needs the size fix — see §13d, not yet applied as of the last
  render check.

### 13c. Consolidated re-render prompt sent for buttons + chip removal + page title (2026-09-22)
Superseded by the render check in §13d below — kept here only as a record of what was asked for.
The prompt covered all 3 of §13a's fixes at once (button resize/reshape, chip-container removal,
page-title shrink); the render that came back only landed 2 of the 3 (see §13d).

### 13d. Render check after the §13c prompt (2026-09-22) — 2 of 3 fixes landed, 1 new defect found
- **Status label (chip removal): done.** "IN PROGRESS" and "NEEDS YOUR RESPONSE" both render as
  plain colored text, no box.
- **Buttons: done — and the long-standing Accept-gray defect (§ above, ~4 prior rounds) finally
  cleared.** Accept/Decline are pill-shaped, content-hugging, and Accept renders filled `#006837`.
- **Page title: NOT done.** "Assignments" still renders at roughly the same large/bold weight as
  before, still competing with "Joseph" in the header. Needs another pass — see §13f prompt below.
- **New regression, unrelated to the 3 asks:** the render reintroduced solid blue+green journey
  dots, which at the time contradicted the then-current shape-only/neutral-color spec. **This is no
  longer a defect — see §13e, the spec itself was reversed to match what this render already
  shows.** Left in this log for the reasoning trail; do not "fix" the dots back to neutral.

### 13e. Journey dot color reversed back (2026-09-22) — user pushback led to fresh research
User asked directly: "is the journey dots decision truly better than what we have now?" — a fair
challenge, since the shape-only/neutral-color rule (from 2026-09-21, see above) was about to be
enforced against a render that looked fine. Checked real apps fresh rather than defend the existing
call: Tesla Robotaxi and BlaBlaCar do use shape-only (hollow→filled, one neutral color), but
**inDrive — already flagged earlier this session as a liked reference for this exact screen** —
uses colored (blue origin / green destination) dots for precisely this pattern, and Grab Driver
color-codes pickup vs. drop-off too. Real practice is genuinely split. The original shape-only rule
had been motivated by tightening the closed color list (a hygiene goal), not a usability problem
color was causing — weaker grounds than the defect-driven fixes elsewhere in this component.
**Reversed: colored dots are correct.** Locked in Component 9: origin `#3B82F6` (blue, one new
closed-list exception), destination `color.brand.primary` `#006837` (reuses the existing token).
The Scheduled card keeps its dots muted gray (not the fixed blue/green) since that whole card is
deliberately quieted — not a new exception, just not applying the color one to that specific card.
**Visual match, not pixel-verified — revised 2026-09-22.** The prior note said "no re-render
needed" based on the render *looking* consistent with the locked spec, but the exact hex was never
pixel-checked against the screenshot. A generic green a Figma agent picks on its own could drift
from the locked `#006837` on the next pass without an explicit instruction. Folded an exact-color
lock into the §13f prompt below rather than leaving it to hold by assumption.

### 13f. Remaining re-render prompt — page title + exact dot-color lock

```
Two corrections to the FRAME-07 Home screen:

1. PAGE TITLE: "Assignments" (the heading above the card list, below the header) is still
   rendering too large/bold. Shrink it to 18px, weight 600, color #0F172A. It should read as a
   smaller section label sitting under the header, not compete with "Joseph" in the header above
   it for visual weight.

2. JOURNEY DOTS — lock exact colors so they don't drift: origin dot (top, e.g. "Nakuru HQ") must
   be exactly #3B82F6. Destination dot (bottom, bold destination name) must be exactly #006837 —
   the same Civic Green used on the "Start Pre-Trip Inspection" button, not a different or
   generic green. Both dots stay solid/filled circles. On the Scheduled card only, both dots stay
   muted gray (#E2E8F0 origin, #64748B destination) instead of the fixed blue/green, since that
   card is deliberately the quietest one on the screen.

Keep everything else on this screen exactly as currently built — card structure, buttons, status
labels, detail block, header, and bottom tab bar are all correct as-is and should not change.
```

### 13g. Accept/Decline had no SRS grounding — checked and resolved, not removed (2026-09-22)

User asked directly whether "mandatory work" cards should even have Accept/Decline. Checked the
actual SRS-derived flow rather than assume the existing pattern was fine: **`02_USER_FLOWS.md` §3's
Dispatch Gate diagram and `01_USER_PERSONAS.md` §8's driver journey (both built directly from SRS
§5.4/§5.6/§11) put the assignment decision with Daniel (Transport Officer), not the driver** — the
driver's SRS-grounded journey just says they "see their assigned vehicle for the day." Accept/
Decline had been pattern-matched from the ride-hailing references (Uber/Grab/inDrive) used
throughout this screen's design without ever being checked against this project's own dispatch
model — the same category of ungrounded import as SOS, just affecting a whole card type instead of
one icon.

**Resolved, not removed:** user confirmed the real intent — drivers need to confirm they've seen a
dispatched assignment, and flag genuine inability to fulfill it (illness, a known prior conflict),
not shop between assignments. So Accept/Decline stays, reframed:
- **Accept = confirm/acknowledge**, not "I choose this job."
- **Decline is gated by a mandatory reason field** (matching the system's existing justification
  pattern — BR-009's override justification, §5.24's rejection/return-for-correction) and **routes
  back to Daniel's Dispatch Queue for reassignment** — never a driver-to-driver handoff, which would
  bypass Daniel's dispatch authority and break the maker-checker model this system enforces
  everywhere else.

This mechanism (mandatory reason, routes to Daniel) already existed in `04_FIGMA_SCREEN_BLUEPRINT.md`'s
per-card notes and was well-designed — what was missing was connecting it back to the canonical flow
docs, which made it look ungrounded when it was actually just undocumented there. Now recorded in
all three places: `02_USER_FLOWS.md` §3 (new "Driver Confirmation" step + note), `01_USER_PERSONAS.md`
§8 (stage 1 footnote), and `03_MASTER_DESIGN_SYSTEM.md` Component 9 (new grounding note before the
button spec). No UI/visual change — the button spec, labels, and colors already built are unaffected;
only the documented meaning behind them changed.

### 13h. "In Progress" card renamed to "Ready" (2026-09-22) — closes the earlier flagged contradiction

Direct follow-up question: "is the logical step still Accept → Start Inspection?" Tracing it
through revealed the sequence isn't adjacent — there's a date gate in between. **Full corrected
state chain: Needs Your Response → (Accept) → Scheduled → (trip date arrives) → Ready → (Start
Pre-Trip Inspection tapped) → hands off to FRAME 7B/7C (a separate screen, not a Home card state).**

This closes the "In Progress" label contradiction flagged earlier in §13: the card previously
called "In Progress" (Mary Akinyi's trip, today, "Start Pre-Trip Inspection" button) is actually
**confirmed + today + not yet started** — nothing is "in progress" about it. The ordering rationale
in `04_FIGMA_SCREEN_BLUEPRINT.md` had described it as "mid-inspection, mid-drive," which
contradicted its own "Start" (not "Continue") button. **Relabeled to "Ready."** Updated in
`03_MASTER_DESIGN_SYSTEM.md` Component 9 (state-naming correction note + color table), the FRAME 7A
ASCII mockup, and the ordering rationale in `04_FIGMA_SCREEN_BLUEPRINT.md` §8.

**Still open, not built:** a genuinely mid-trip "In Progress" Home-list state (for a driver who
backgrounds the app mid-checklist or mid-drive and needs a way back in, with a "Continue Trip"
button rather than "Start Pre-Trip Inspection") — conceptually distinct from "Ready," lives
logically alongside FRAME 7C's Active Trip screen, not yet designed or confirmed as needed. Flag
before assuming Home's 3 card types are exhaustive.

### 13i. Re-render prompt — status label rename only

```
One text change to the FRAME-07 Home screen:

Rename the status label on the first card (today's confirmed assignment — Mary Akinyi / Nakuru
Sub-County Office, button "Start Pre-Trip Inspection") from "IN PROGRESS" to "READY". Keep the
exact same color (#006837), same plain-text-no-chip treatment, same position and size as before.
This card represents a confirmed assignment for today that hasn't been started yet — "Ready" is
accurate, "In Progress" was not.

Do not change anything else — the other two cards (Needs Your Response, Scheduled), buttons,
journey dot colors, page title, header, and bottom tab bar are all correct as-is.
```

## 14. FRAME 7B (Walkaround Checklist) locked as Component 10 (2026-09-22)

Moved on from FRAME 7A to FRAME 7B — the screen "Start Pre-Trip Inspection" leads into. It existed
only as a rough content sketch (no exact type/spacing/color values, single Pass checkbox) before
this pass; now locked the same way Component 9 was for Home.

**Fixed a real compliance gap in the rough draft:** a single Pass checkbox conflates "not yet
inspected" with "passed" — risky for a checklist BR-004 and the Dispatch Gate depend on. Replaced
with a real two-state Pass/Fail segmented toggle (neither selected by default), reusing Component
9's pill-button geometry rather than inventing a new control. Camera icon per-row-on-Fail (not a
blanket action) was already correctly speced, confirmed via Turo/Lime references cited earlier in
`05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`.

**Evidence model corrected a second time, same pass (2026-09-22) — user asked directly how Pass
items get evidence, since only Fail had a camera icon.** Checked real DVIR (Driver Vehicle
Inspection Report) industry practice rather than guess: "failed items require a description and,
critically, a photograph" — so the Fail camera icon is now **mandatory, paired with a required
reason**, not just available. For Pass items, the real industry mechanism isn't per-item photos
(which would fight this screen's "60-second" framing and prove little for a routine, fine item) —
it's **automatic GPS + timestamp capture at inspection start and submission**, verifying physical
presence at the vehicle. Added a small, silent "Location & time verified" caption at the bottom of
the screen for this.

**Third correction, same day — the Fail "description" interaction itself was wrong.** First draft
used a free-text "What's wrong?" field. Caught before any render: typing a full description
one-handed, outdoors, in glare is exactly the friction this whole screen (and Accept/Decline, and
Pass/Fail itself) was designed to eliminate by using taps instead of typing. **Fixed: quick-select
reason chips, scoped per checklist item** (e.g. Tyres — Worn Tread / Flat or Damaged / Missing
Spare / Low Pressure), multi-select, reusing the same interaction already cited for this screen —
[Turo's "Physical damage" checklist](https://mobbin.com/screens/c9fbb23e-0b26-4958-924a-ef9c171ae8a6),
a multi-select list of specific damage types — not a new pattern invented from scratch. A row is
complete with photo + at least one chip; an optional "+ Add more detail" text area exists for
anything the presets don't cover, but is never required. See Component 10's updated notes for full
citations and the per-item chip sets.

**Bigger finding: a Fail blocks departure — this is SRS-grounded, not a UI judgment call.** Checked
directly: SRS §5.6 (Dispatch Management) reads *"verify... tyres, lights, brakes and safety
equipment. Prevent dispatch where mandatory conditions are not met, subject to authorized
override"* — the exact same 4 checklist items, the exact same block-plus-override pattern already
used for the Dispatch Gate's BR-001–005. **Any Fail now blocks "Confirm Inspection & Proceed"
entirely; the button slot instead becomes "Request Override — Report to Transport Office," which
routes to Daniel's Dispatch Queue for authorization — not a self-override**, matching this system's
own standing pattern (BR-009's override is granted by Daniel, never self-served by the person being
blocked; same channel already locked for a Home-screen Decline).

Full spec: **Component 10 — Mobile Pre-Trip Inspection Row** in `03_MASTER_DESIGN_SYSTEM.md`
(mirrored to `.agents/rules/master-design-system.md`), content updated to match in
`04_FIGMA_SCREEN_BLUEPRINT.md` §8 FRAME 7B. Also fixed: `09_PATTERN_LIBRARY.md` §13 had a stale
pre-rebuild driver-flow fragment (old single-card Home, SOS present, 48px touch targets) that would
have misled a future agent copy-pasting from it — marked superseded, pointed to the current docs.

**Fourth revision, same day — layout, app bar, and Fail interaction all reworked after a render
check (2026-09-22).** User flagged 4 real issues at once: no back navigation on the app bar, long
labels ("Headlights, Brake Lights & Indicators") wrapping into the Pass/Fail buttons, whether the
buttons were sized right, and whether Fail detail should be a dropdown or a drawer.
- **App bar:** added a proper M3 small top app bar — leading back arrow, left-aligned title,
  trailing progress pill. Tried to pull the exact current M3 spec from `m3.material.io/components/
  app-bars/specs` directly; it's a JS-rendered page and returned no usable content (same failure
  mode as the earlier Uber Base/Polaris attempts) — used stable, well-established M3 conventions
  instead of a freshly-verified pull, and said so explicitly in Component 10 rather than presenting
  it as verified-today.
- **Row crowding:** root cause wasn't button size — it was a single-line layout that only worked
  for short labels. Fixed by stacking each row into two lines (icon+label on line 1, Pass/Fail
  toggle on line 2), so a wrapped label can never crowd the buttons regardless of length. Button
  height stays 44px, unchanged — that's this project's own accessibility floor, not something to
  shrink to solve a layout bug.
- **Fail interaction — dropdown vs. drawer, resolved as a modal bottom sheet.** Asked directly;
  recommended and confirmed a bottom sheet over inline expansion, since several rows failing at
  once would otherwise compound into a tall, reflowing list. Tapping Fail now opens a sheet (photo +
  reason chips + optional detail + its own Save button); on save the row collapses to a compact
  one-line summary with an Edit affordance, keeping the main list height stable regardless of how
  many items fail.

**Fifth correction, same day — button size, prompted by a direct comparison against Perplexity's
compact action pills.** User pointed out Perplexity's buttons look visibly shorter than CVFMS's
Pass/Fail toggle. Checked rather than dismissed: the likely explanation is that 44px governs the
*tappable zone*, not the *rendered box* — both Apple HIG and Material Design allow a visually
smaller pill with invisible padding making up the real touch-target minimum, which is very likely
what Perplexity is doing, not a touch-target violation. **Fixed: tappable zone stays 44px
(unchanged — this driver context is more demanding than average, not less), but the visible pill
now renders at 36px**, with padding making up the difference. Applied consistently to both
Component 9's Accept/Decline (paired buttons only, not the solo full-width button) and Component
10's Pass/Fail toggle — the same distinction, not two separate fixes.

**Sixth revision, same day — text-wrap rule locked explicitly, and the bottom sheet rebuilt using
the reference screens more carefully.** User re-confirmed the wrap rule (text wraps, buttons never
do) and asked for a genuinely better sheet than a generic chips+photo+button form.
- **Locked explicitly:** the checklist label is the only element in this component allowed to wrap
  to a second line — the Pass/Fail toggle and every button/chip elsewhere stay fixed-height,
  single-line. This was already true structurally but hadn't been stated as a hard rule.
- **Sheet header added**, borrowed from Flighty's "Report Data Issue" sheet: an item-specific
  question at the top ("What's wrong with the Tyres & Spare Wheel?") instead of an unlabeled form.
- **Sheet reordered** to match Lime's reference (location, then reason, then photo) rather than
  photo-icon-first.
- **Real gap found and fixed: added a "which one?" chip tier.** Every checklist row bundles more
  than one physical item under one label (Tyres *and* Spare Wheel; Headlights *and* Brake Lights
  *and* Indicators; Oil *and* Coolant; Extinguisher *and* First Aid Kit) — re-examining Lime's
  reference (which pairs its reason chips with a labeled diagram specifically to *locate* an issue,
  not just categorize it) surfaced that CVFMS's chips had the same "locate, not just categorize"
  need but no way to answer it. The full diagram stays rejected as overkill (already decided,
  `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`), but a lightweight chip tier closes the same gap without
  it — confirmed with the user before locking in, since it's a content-model change, not a style
  tweak. Sheet order is now: which-one chips → reason chips → photo → optional detail → Save.

**Still open, not built:** (1) the driver's wait state between requesting an override and Daniel
authorizing it has no screen yet; (2) whether the app bar's back arrow discards or preserves
in-progress checklist state if tapped mid-inspection. Both need their own design pass before
FRAME 7B→7C is fully closed.

### 14a. Figma prompts — FRAME 7B, Walkaround Checklist (split into 2, condensed 2026-09-22)

**Split into 2 sequential prompts to fit the Figma agent's ~2000-character limit**
(`09_PATTERN_LIBRARY.md`'s standing rule). One combined prompt ran ~5,975 characters — even a
single condensed pass stayed ~2,811, still over. Given how much of this screen's content is
genuinely new (two-tier chip sets across 4 items, each needing exact labels), further compression
risked the Figma agent guessing at details rather than actually having them — splitting is more
reliable than cramming. **Run Prompt 1 first, review the render, then run Prompt 2** (which adds
the bottom sheet on top of the base screen Prompt 1 builds).

**Prompt 1 — base screen (app bar, rows, banner, CTA, offline fallback):**
```
Build FRAME 7B, the Walkaround Checklist a driver reaches after "Start Pre-Trip Inspection" on
Home. Same 390px viewport, light theme, Lexend/Source Sans 3, Civic Green (#006837) as FRAME-07.
Reuse FRAME 7A's exact button geometry, pill styling, and color tokens throughout (don't restate
them) — the elements below are only what's new to this screen.

APP BAR (M3 small top app bar, 56px, white): back arrow (leading) → title "Pre-Trip Inspection •
KBZ 442A" (left-aligned, not centered) → trailing progress pill "0/4 Checked".

4 CHECKLIST ROWS, 1px divider between each, TWO STACKED LINES per row (not one — long labels must
never sit beside the buttons): Line 1 = category icon + item label (wraps freely to 2 lines).
Line 2, 8px below = Pass/Fail toggle, left-aligned (same pill styling as FRAME 7A's Accept/Decline,
visible height 36px/tappable zone 44px). Items: Tyres & Spare Wheel / Headlights, Brake Lights &
Indicators / Engine Oil & Coolant Levels / Fire Extinguisher & First Aid Kit. For now, tapping
"Fail" just fills the toggle red — the detail sheet is a separate follow-up prompt.

Small caption near the bottom: "Location & time verified" (auto, silent, no interaction).

COMPLETION BANNER once all 4 rows are marked: all-Pass → one line, informational green, "No
defects logged. You are cleared for departure." (no separate heading). Any Fail → one line,
critical red, "X defect(s) found — departure blocked pending authorization." (no duplicate count).

PRIMARY BUTTON: all-Pass → "Confirm Inspection & Proceed →" filled green. Any Fail → same slot
becomes "Request Override — Report to Transport Office" filled critical red. Disabled/grayed before
all 4 rows are marked.

If Fail is active AND device has no data connection, show a secondary outline button below:
"No connection — Call Transport Office" (tap-to-call the county dispatch number).

Same bottom tab bar as Home, "Home" no longer highlighted (this is a sub-screen).
```

**Prompt 2 — Fail bottom sheet (run after Prompt 1 renders):**
```
On FRAME 7B's Walkaround Checklist, change what happens when a row's "Fail" toggle is tapped: it
should no longer just fill red in place. Instead, open a MODAL BOTTOM SHEET sliding up from the
bottom, in this order: (1) header question, "What's wrong with the [item]?"; (2) "Which one?"
chips (small label above them) — per item: Tyres & Spare Wheel→Front-Left/Front-Right/Rear-Left/
Rear-Right/Spare Wheel; Headlights, Brake Lights & Indicators→Headlights/Brake Lights/Indicators;
Engine Oil & Coolant Levels→Engine Oil/Coolant; Fire Extinguisher & First Aid Kit→Fire
Extinguisher/First Aid Kit; (3) "What's wrong?" chips (same chip styling, own small label) — Tyres
& Spare Wheel→Worn Tread/Flat or Damaged/Missing Spare/Low Pressure; Headlights, Brake Lights &
Indicators→Not Working/Cracked Lens/Dim or Flickering; Engine Oil & Coolant Levels→Low Level/
Leaking/Discoloured; Fire Extinguisher & First Aid Kit→Missing/Expired/Damaged; (4) mandatory photo
capture (camera icon + "Add Photo"); (5) optional "+ Add more detail" text link, expands a text
area, never required; (6) "Save" button, filled Civic Green, disabled until a which-one chip, a
what's-wrong chip, and a photo are all present. On Save, the sheet closes and that row's toggle
line is replaced by a compact one-line summary, e.g. "Front-Left, Worn Tread · Photo attached" in
critical red, with a small "Edit" link to reopen the sheet. Also update the primary button logic:
"Request Override" now stays disabled until every Fail row has been saved via its sheet, not just
toggled red.
```

### 14b. Offline override fallback added (2026-09-22) — Baringo/low-connectivity gap

Direct question: what happens when a driver has a failed inspection and no connectivity to reach
Daniel at all? Real gap — this system already commits to offline-first
(`CVFMS_Architecture_and_Implementation_Summary.md`: checklists log locally, "syncing when
connection restores"), and several county sub-counties (Baringo named directly) genuinely have poor
connectivity. GPS/timestamp and photo/description entry all work offline fine — but the digital
"Request Override" action needs to actually reach Daniel, which fails outright with zero signal. As
first speced, a driver in that situation would simply be stuck.

**Resolved: three-tier escalation**, confirmed with the user rather than assumed:
1. Digital override request (as already speced) when connectivity allows.
2. Data fails, voice/SMS may still work (common — cellular voice often survives where data
   doesn't): a "No connection — Call Transport Office" fallback button (included in the prompt
   above) opens the device dialer; returning to the app requires a logged "Verbally authorized by
   [name/role]" confirmation — not yet added to the first-build prompt above since it's a secondary
   screen/dialog, not part of the initial checklist layout; needs its own follow-up prompt once the
   base screen renders.
3. No signal at all — genuine last resort: an offline provisional override behind an explicit
   acknowledgment dialog (deliberately not a casual button tap), logged locally and flagged
   "Offline provisional — pending review," synced and surfaced to Daniel/audit once connectivity
   restores. Also not yet in the first-build prompt — same reason.

**Why this matters beyond FRAME 7B:** all three authorization types (digital, verbal, offline-
provisional) must stay distinguishable in the record — this is a direct dependency for FRAME-09
(Statutory Audit Trail), which needs to show *how* a departure was authorized, not just that it
was. Recorded in `03_MASTER_DESIGN_SYSTEM.md` Component 10, `02_USER_FLOWS.md` §3 (new note after
the Driver Confirmation section), and `04_FIGMA_SCREEN_BLUEPRINT.md` §8 FRAME 7B.

### 14c. Render check after Prompts 1 & 2 (2026-09-22) — most structural fixes landed

Real progress: stacked two-line rows work exactly as specced (no more label/button crowding), the
bottom sheet replaced inline expansion, the collapse-to-summary-on-save behavior works correctly
("Worn Tread · Photo attached · Edit"), and both banner copy fixes from the prior round held (no
"SUCCESS" heading, no duplicated defect-count text).

**App bar decision:** the render split the title and vehicle-plate/progress-pill onto two rows
(app bar = title only; a separate content row below carries "KBZ 442A" + the progress pill) rather
than one combined title string as originally speced. Asked directly — **kept as-is**, it reads
cleanly and separates navigation chrome from status content. Component 10 updated to match what
was actually built rather than forcing a revert to the original spec.

**2 real issues found, not yet fixed:**
1. A Figma inspector/sizing overlay ("390 Fill × 546") leaked into the 0/4-Checked frame's export —
   needs a clean re-export, not a design fix.
2. **The "Which one?" chip tier is missing from the sheet entirely** — only the "What's wrong?"
   chips rendered (Worn Tread, Flat or Damaged, Missing Spare, Low Pressure); the location chips
   (Front-Left/Front-Right/Rear-Left/Rear-Right/Spare Wheel) confirmed earlier didn't make it in.
   Also, photo capture rendered *before* the reason chips instead of after — spec order is
   which-one → what's-wrong → photo.

### 14d. Fix prompt — add the missing "Which one?" chip tier and correct sheet order

```
On FRAME 7B's Fail bottom sheet, two corrections:

1. Add a "Which one?" chip section ABOVE the existing "What's wrong?" chips (same chip styling —
   unselected white/outline, selected filled critical red). Small label "Which one?" above this
   new row. Per item: Tyres & Spare Wheel→Front-Left/Front-Right/Rear-Left/Rear-Right/Spare Wheel;
   Headlights, Brake Lights & Indicators→Headlights/Brake Lights/Indicators; Engine Oil & Coolant
   Levels→Engine Oil/Coolant; Fire Extinguisher & First Aid Kit→Fire Extinguisher/First Aid Kit.

2. Reorder the sheet to: header question → "Which one?" chips (new) → "What's wrong?" chips
   (existing) → "Add Photo" button → "+ Add more detail" link → Save. Currently "Add Photo" renders
   before the chips — move it to after both chip sections instead.

The Save button should stay disabled until a "Which one?" chip, a "What's wrong?" chip, AND a
photo are all present — not just the existing two conditions.

Also: please re-export the 0/4-Checked (empty) state — it currently has a stray blue "390 Fill x
546" label box floating in the middle of the screen that shouldn't be part of the design.
```

### 14e. Bottom-of-screen crowding — caption removed, banner un-boxed (2026-09-22)

User flagged the bottom area directly: "the messages and the buttons are conflicting... do we need
the messages styled as buttons?" Two real problems, both fixed in Component 10:
- **"Location & time verified" caption removed from the visible UI entirely.** It was never for the
  driver — it's the system reassuring itself that GPS/timestamp capture happened. The capture is
  unchanged and still happens automatically; it just no longer needs a visible line of text.
- **Completion banner un-boxed.** It was a filled/bordered box sitting directly above the primary
  button at similar width and shape — reading as a second (or third, with the offline-fallback
  button) button rather than a status message. Fixed: plain icon + text, no background/border. Only
  actual buttons keep a box treatment now, so there's no ambiguity about what's tappable. Same fix
  already applied to FRAME 7A's status label for the identical reason.

Folded into the same fix prompt as §14d below, since neither has been re-rendered yet.

### 14f. Combined fix prompt — chip tier + sheet order + bottom-of-screen declutter

```
Three corrections to FRAME 7B:

1. FAIL SHEET: Add a "Which one?" chip section ABOVE the existing "What's wrong?" chips (same chip
   styling — unselected white/outline, selected filled critical red). Small label "Which one?"
   above this new row. Per item: Tyres & Spare Wheel→Front-Left/Front-Right/Rear-Left/Rear-Right/
   Spare Wheel; Headlights, Brake Lights & Indicators→Headlights/Brake Lights/Indicators; Engine
   Oil & Coolant Levels→Engine Oil/Coolant; Fire Extinguisher & First Aid Kit→Fire Extinguisher/
   First Aid Kit. Reorder the sheet to: header question → "Which one?" chips (new) → "What's
   wrong?" chips → "Add Photo" (move this after the chips, not before) → "+ Add more detail" →
   Save. Save stays disabled until a "Which one?" chip, a "What's wrong?" chip, AND a photo are
   all present.

2. BOTTOM OF SCREEN: Remove the "Location & time verified" caption entirely — it should not appear
   anywhere on screen. Change the completion banner (the green "cleared for departure" / red
   "departure blocked" message) from a filled colored box to plain text with a small icon — no
   background fill, no border, no rounded-box container. Only the actual buttons below it should
   look like buttons.

3. Please re-export the 0/4-Checked (empty) state — it currently has a stray blue "390 Fill x 546"
   label box floating in the middle of the screen that shouldn't be part of the design.
```

### 14g. Render check after §14f (2026-09-22) — all 3 fixes landed

All three corrections confirmed in the render: "Affected item(s)" chips (Front-Left/Front-Right/
Rear-Left/Rear-Right/Spare Wheel) now appear above "What's wrong?" chips, with "Add Photo" moved
after both chip groups as requested; the "Location & time verified" caption is gone; both
completion banners now render as plain icon + text with no box, clearly distinct from the real
buttons below them; the stray Figma export artifact is gone. The collapsed row summary also
improved on its own — now includes the affected-item info too ("Front-Left · Worn Tread · Photo
attached"), not just the reason.

**Two small polish items found, resolved:**
- Sheet title rendered as "Report tyre issue" instead of the originally-drafted question format.
  **Confirmed as the new standard** — shorter, reads naturally, kept consistent across all 4 items
  ("Report [item] issue"). Component 10 and the FRAME 7B blueprint updated to match.
- Buttons use a plain hyphen ("Request Override - Report to Transport Office") instead of the
  specced em dash. Cosmetic only — not worth its own prompt; fold into any future render pass on
  this screen if one happens anyway.

**FRAME 7B's core checklist + Fail flow is now effectively closed.** Remaining open items, neither
blocking: (1) whether the app bar's back arrow discards or preserves in-progress state; (2) the
driver's wait-state screen between requesting override and Daniel's authorization. Next natural
step is either resolving those two, or moving to FRAME 7C (Trip Start/Active Trip/Trip End) or
View Details (the chevron target from FRAME 7A, still unbuilt).

### 14h. Bottom-area hierarchy/spacing rebalanced (2026-09-22)

User flagged the bottom of the last two states directly: hierarchy and spacing not balanced, even
after the caption removal and banner un-boxing. Two real causes found:
- **Spacing was inconsistent between states**, not just present. The banner sat at the end of the
  scrolling checklist content while the button was pinned separately to the viewport bottom (sticky
  footer) — so the gap between them varied with how much content filled the space above (large gap
  on All-Pass, almost no gap on Fail). **Fixed: banner + button(s) are now one fixed, non-scrolling
  action zone anchored to the bottom of the screen**, guaranteeing the same 12px gap in every state.
- **Two full-width buttons stacked (Request Override + the offline fallback) read as equal-weight
  choices, not a primary action with a rare exception underneath.** **Fixed: the offline fallback
  ("No connection — Call Transport Office") is now a plain centered text link, not a full-width
  outline button** — matches how this project already treats other rare/exception actions (e.g.
  Home's "View N more pending" overflow link) rather than giving an edge case the same visual
  authority as the main path.

Both fixed in Component 10, `04_FIGMA_SCREEN_BLUEPRINT.md` §8 FRAME 7B.

```
Two corrections to the bottom of FRAME 7B's checklist screen:

1. Make the banner and button(s) below it into one fixed group anchored to the bottom of the
   screen — not the banner scrolling with the checklist content while the button stays pinned
   separately. The checklist rows should scroll independently above this fixed bottom group. This
   should give a consistent, small gap (about 12px) between the banner and the button in every
   state, instead of a large gap when all items pass and almost no gap when one fails.

2. Change "No connection — Call Transport Office" from a full-width outline button into a plain
   centered text link (no border, no fill, no button shape) sitting just below the primary
   "Request Override" button. It's a rare fallback, not a co-equal action, and shouldn't look like
   a second full-width button stacked under the first one.
```

## 15. View Details built as Component 11 (2026-09-22)

Closed a gap referenced constantly since FRAME 7A was first built — every Home card has a chevron,
and both Component 9 and this blueprint kept saying "the rest lives behind the chevron" without
that screen ever actually being specced. Field list grounded directly in SRS §5.4/§5.5, not
guessed: purpose, expected return, full passenger breakdown, project/activity, and supporting
documents are the fields that had nowhere else to live once the Home card face was locked down.

**Resolved a question left open since Component 9 was written:** View Details supplements the
card-face Accept/Decline and "Start Pre-Trip Inspection" buttons, it doesn't replace them — a
driver can still decide directly from Home without an extra screen transition; View Details is for
a driver who wants the full picture first. Considered and rejected moving the buttons off the card
face entirely, since that would add a forced extra tap to the single most common interaction on
Home for every driver, on every assignment.

Structurally, almost nothing on this screen is new — it reuses FRAME 7B's app bar, Component 9's
journey visual and button specs, and Component 10's fixed/anchored action-zone treatment. The only
genuinely new content is the SRS fields themselves. Full spec: **Component 11 — Assignment Detail /
"View Details"** in `03_MASTER_DESIGN_SYSTEM.md` (mirrored), content in
`04_FIGMA_SCREEN_BLUEPRINT.md` §8, new **FRAME 7A.1**.

### 15a. Figma prompt — FRAME 7A.1, View Details (revised 2026-09-22 with exact hierarchy/spacing)

**Locked as a full page, not a drawer** — checked directly rather than defaulted to consistency
with FRAME 7B's sheet pattern: every real reference cited for this screen (BlaBlaCar, inDrive's
Order screen, inDrive's receipt, Grab Driver) is itself a full page, content volume is well beyond
a sheet's comfortable range, and the chevron trigger + page-to-page forward navigation (into FRAME
7B) both point the same direction. See Component 11 for the standing rule this sets: drawer for a
small nested task, page for a genuinely deeper view.

```
Build a new screen, "Trip Details" — reached by tapping the chevron on any Home-screen assignment
card. Same 390px viewport, light theme, Lexend/Source Sans 3, Civic Green (#006837). Reuse FRAME
7A's exact journey visual and FRAME 7B's exact app bar and fixed bottom action-zone — don't
restate their styling, just reuse it.

APP BAR (56px, white): back arrow → title "Trip Details" (plain, not a greeting), 16px/700.

16px below the app bar: reference ID "REQ-2024-0851", 12px/400, #64748B.

24px below that, JOURNEY block: same dot-connector-dot visual as Home — "Nakuru HQ" (origin,
#3B82F6 dot) to "Nakuru Sub-County Office" (destination, bold hero, #006837 dot, 16px/700 #0F172A).

24px below the journey, "TRIP INFO" section label (12px/600, uppercase, +0.02em tracking, #64748B
— same treatment as the status label on Home cards, just neutral-colored here). Rows below it, 8px
apart, each a label (14px/400, #334155) + value (14px/600, #0F172A) pair: "Departure — Today,
10:30 AM", "Expected Return — Today, 3:00 PM", "Purpose — Site inspection, Public Works quarterly
review".

24px below Trip Info, "REQUESTER" section label (same style). Rows: "Mary Akinyi · Public Works",
then full passenger list "Mary Akinyi, John Otieno, Grace Wambui — 3 passengers" (not just a
count).

24px below Requester, "VEHICLE" section label (same style). Rows: "Toyota Land Cruiser · KBZ
442A", "Nakuru HQ Yard · Bay 4", "Fuel: 75%", "Dispatch Clearance: Passed".

No divider lines anywhere on this page — the 24px gaps and section labels do the grouping.
16px side padding throughout.

FIXED BOTTOM ACTION ZONE (anchored to the viewport bottom, not scrolling with the content above —
same treatment as FRAME 7B): Accept (filled #006837) / Decline (outline) side by side, same pill
button spec as FRAME 7A's paired buttons — since this version is opened from a "Needs Your
Response" assignment.

Bottom tab bar not shown on this screen — it's a detail view, not a tab destination.
```

### 15b. Render check (2026-09-22) — 4 real fixes, plus icons confirmed correct with evidence

Render came back structurally solid (spacing, section labels, journey visual all landed), but with
3 real defects plus one genuine content ambiguity worth resolving:
1. **Reference ID rendered too large/bold** — was competing with the destination headline for
   dominance, exactly what it's specced not to do (12px/400 muted). Corrected in Component 11.
2. **"Dispatch Clearance: Passed" needs status color** — was plain black, indistinguishable from
   neutral facts around it (fuel level). Fixed: value renders in `#006837` (or critical red if
   blocked), no container — same un-boxed status treatment as FRAME 7B's banners.
3. **Label "Officer" → "Requester"** — didn't match SRS §5.4's own term or this app's vocabulary
   elsewhere.
4. **Requester/passenger overlap resolved:** Mary Akinyi appeared as both "Officer" and in the
   passenger list with no stated relationship — genuinely ambiguous (duplication bug vs. she's
   really traveling). Resolved: requesters often do travel on their own trip; when she's among the
   passengers, tag her explicitly — "Mary Akinyi (Requester), John Otieno, Grace Wambui."

**Icons — asked "why aren't we using them," checked properly rather than defended by reasoning
alone.** Researched 10 real detail/booking screens (Turo, BlaBlaCar, American Airlines, Viator,
Agoda, Grab, Waymo, Fly Delta, Tripadvisor, Lyft). Waymo's Trip Details screen is the closest real
match to this component and uses zero icons on its equivalent rows. Consistent pattern across all
10: icons only appear on tappable navigation-list rows (differentiating one clickable destination
from an identical neighbor) or specific universal glyphs (phone, payment card) — never generic
person/vehicle icons next to an already-labeled section. **Confirms the original no-icons call was
right, now backed by evidence rather than just reasoning** — Component 11 updated with the full
citation trail so this doesn't need re-litigating later.

### 15c. UI fundamentals check (2026-09-22) — 3 more real gaps, none rendered yet

Asked directly whether the underlying craft (not just content/copy) could improve. Found 3 real
gaps in the spec itself, none of them content fixes:
1. **No locked label-column alignment** — each row's value started wherever its own label ended,
   so values would drift out of alignment depending on label length. Fixed: a fixed 110px label
   column, value column takes the rest and wraps within it. Every value now sits at the same
   x-position — matches how Waymo's reference screen aligns its own rows.
2. **Section-label-to-first-row spacing was ambiguous** — 24px was locked between sections, but
   nothing distinguished that from the gap between a label and its own first row, risking a label
   reading as floating equidistant between two sections instead of clearly attached to one. Fixed:
   8px between a label and its own first row (same rhythm as rows within a section); 24px stays
   reserved for the gap between one section's last row and the next section's label.
3. **Documents row had no touch-target size** — the one genuinely tappable row on the page, missed
   when the section was first drafted. Fixed: 44px minimum height, matching this project's
   established floor everywhere else.

Considered and rejected changing: the app bar title and destination headline are both 16px/700.
Deliberate, not a missed type-scale opportunity — the destination reuses Component 9's exact token
so a driver recognizes the same journey from Home; the two sit in clearly separate visual zones
(fixed chrome vs. scrolling body), so it doesn't reopen the "two competing headlines" problem fixed
elsewhere (that was about two same-zone elements stacked directly on each other).

### 15d. Combined fix prompt — 7 corrections to View Details (content + fundamentals, none rendered yet)

```
Seven corrections to the Trip Details screen:

1. Shrink "REQ-2024-0851" to 12px, weight 400, color #64748B — it's currently rendering too large
   and bold, competing with "Nakuru Sub-County Office" for visual dominance.

2. Change "Dispatch Clearance: Passed" so only the value "Passed" renders in green (#006837) —
   keep the label "Dispatch Clearance" in normal muted gray.

3. Change the section label from "Officer" to "Requester".

4. Change the passenger list to "Mary Akinyi (Requester), John Otieno, Grace Wambui — 3
   passengers" — tag her role explicitly since she's both the requester and a traveler.

5. Align all label/value rows to a fixed label column, about 110px wide (enough to fit "Expected
   Return" without wrapping) — every value across the whole page should start at the same
   horizontal position, not wherever its own label happens to end.

6. Tighten the gap between each section label ("TRIP INFO," "REQUESTER," "VEHICLE") and its own
   first row to about 8px — the same tight spacing already used between rows within a section. Keep
   the larger ~24px gap only between one section's last row and the next section's label, so each
   label clearly reads as attached to the content below it.

7. Give the Documents row (if shown) a minimum tap height of 44px.

Do not add icons to any of the section rows (Requester, Vehicle, etc.) — confirmed this should
stay text-only, matching Waymo's Trip Details screen as the closest real reference.
```

### 15e. Figma prompt — View Details, "Ready" and "Scheduled" variants

The two remaining card-type variants, using the same example data already established for those
card types on Home (FRAME 7A). Reference-based — reuses the already-built page, describes only the
content and action-zone deltas per Component 11's rule (mirrors whichever card this was opened
from).

```
On the Trip Details screen already built (the "Needs Your Response" version with Accept/Decline),
create two more variants — same exact layout, spacing, section structure, and all 7 fixes just
applied. Only the content and the bottom action zone change per variant.

VARIANT 1 — opened from a "Ready" card (Mary Akinyi's assignment, already accepted, today):
Content: REQ-2024-0850. Journey: Nakuru HQ → Nakuru Sub-County Office. Trip Info: Departure Today,
10:30 AM; Expected Return Today, 3:00 PM; Purpose: Site inspection, Public Works quarterly review.
Requester: Mary Akinyi (Requester), Public Works; Passengers: Mary Akinyi (Requester), John
Otieno, Grace Wambui — 3 passengers. Vehicle: Toyota Land Cruiser · KBZ 442A; Nakuru HQ Yard · Bay
4; Fuel 75%; Dispatch Clearance: Passed (green).
Action zone: a SINGLE full-width button, "Start Pre-Trip Inspection →", filled #006837, 8px corner
radius (not pill-shaped — this is a solo action, same spec as FRAME 7A's solo button). No second
button.

VARIANT 2 — opened from a "Scheduled" card (Grace Wanjiru's assignment, future date):
Content: REQ-2024-0852. Journey: Nakuru HQ → Naivasha Sub-County Office. Trip Info: Departure Thu,
Sep 24, 9:00 AM; Expected Return Thu, Sep 24, 1:00 PM; Purpose: Fleet inspection, quarterly
maintenance review. Requester: Grace Wanjiru, Fleet Office; Passengers: Grace Wanjiru (Requester)
— 1 passenger. Vehicle: Toyota Hiace · KBZ 104D; Nakuru HQ Yard · Bay 2; Fuel 60%; Dispatch
Clearance: Passed (green).
Action zone: NONE — no button of any kind. The page ends after the Vehicle section with normal
bottom padding; this variant is purely informational since nothing needs deciding yet.
```

## 16. FRAME 7D (Profile) and 7E (Trips tab) locked as Components 12/13 (2026-09-22)

Closed the other two bottom-tab destinations. Both reuse existing patterns rather than inventing
new ones — Profile reuses Component 11's section-label/label-value pattern, Trips reuses Component
9's row anatomy directly.

**Real scope question resolved before locking Trips tab, not assumed:** if Home already shows
Ready/Needs-Response/Scheduled items, what does a separate Trips tab add? Resolved: Home is the
urgency-ordered *execution* view (only what's current/actionable today); Trips is the complete
*intake ledger* (every assignment not yet completed, chronological order, including far-out items
Home doesn't surface to avoid clutter). Different jobs, not a duplicate list.

**One real correction found while building Trips tab:** an earlier draft said tapping an unanswered
row opens "FRAME 7A/State 0" — a reference to a state that no longer exists since the Home rebuild.
Fixed: every row now opens Component 11 (View Details), whichever variant fits.

**Licence expiry urgency, grounded rather than invented:** reuses SRS §5.23's own 30/14/7-day
compliance-alert cadence (already established for insurance/inspection warnings) for the driver's
own licence expiry, instead of picking a new threshold for this one field.

Full specs: **Component 12 — Driver Profile** and **Component 13 — Trips Tab** in
`03_MASTER_DESIGN_SYSTEM.md` (mirrored), content in `04_FIGMA_SCREEN_BLUEPRINT.md` §8 FRAME 7D/7E.

**Checked against real references before finalizing prompts, per direct request — one real fix
found.** Researched 8 profile screens and 8 trip/booking-list screens rather than build purely from
reused patterns.
- **Sign Out was wrong as plain text.** Majority of real profile screens (Mercedes-Benz, Panera
  Bread, Crypto.com, 5 Minute Journal) give this an outline button, not bare text — Mercedes-Benz
  in particular uses a two-tier system (Log Out = outline button, Delete Account = plain text
  below it, an even rarer/more severe action). Fixed: Sign Out now reuses Component 9's exact
  Secondary/outline button style (same as Decline).
- **Trips tab confirmed correct as speced.** [Navan](https://mobbin.com/screens/dc0200de-0819-491e-b2dd-ce7b3d9d81d2)
  (closest domain match — corporate travel) validates the two-state urgent/muted color split;
  [Zomato](https://mobbin.com/screens/b2da1a7b-4031-4299-88e6-4942956cd1bc) confirms uppercase
  section labels and plain colored status text with no chip. One addition flagged for later, not
  built now: [Qantas](https://mobbin.com/screens/8f6f9d0f-d3fb-448f-837b-4ff90ad8ef82) groups rows
  under date headers, worth adopting once this list grows past 2-3 items.

### 16a. Figma prompt — FRAME 7D, Driver Profile (revised 2026-09-22 with overflowing-avatar header)

```
Build FRAME 7D, "Profile" (bottom tab bar, no back arrow, same as Home). Reuse FRAME 7A.1's exact
section-label style (12px/600 uppercase tracked #64748B), label-column row pattern, and 24px/8px
spacing — don't restate, just reuse.

HEADER: same county landmark photo + dark overlay (75-85%) as Home's header, reused exactly, but
shorter (photo only, no greeting text). APP BAR on top of the photo: plain title "Profile", no
back arrow, translucent circular backing.

AVATAR: 88px circular photo (same driver photo as Home), white ring border 3-4px, centered,
straddling the photo/white boundary — about half the circle on the photo, half on white below.

Below it, centered: "Joseph Mutua" at 20px/700 (same size as "Joseph" on Home's expanded header).
Directly below: "County Driver" at 12px, #64748B (same as Home's subtitle treatment).

"IDENTITY" section, 24px below: "Staff Number — [ID]", "Station — Nakuru HQ Transport Pool". Do
NOT repeat "Role" — already shown under the avatar.

"LICENCE" section, 24px below: "Class — Class A, B, C1", "Expiry — 15 Mar 2027" (normal dark text,
no urgency needed).

"PREFERENCES" section, 24px below: "Language" label, two-option segmented toggle "English /
Kiswahili" — same pill toggle as FRAME 7B's Pass/Fail control, English selected (filled #006837).

32px below (double gap): "Sign Out" as an outline button (white fill, 1px #E2E8F0 border, #334155
text) — same style as FRAME 7A's Decline, content-hugging, centered, not full-width.

Same bottom tab bar, "Profile" highlighted as active.
```

### 16b. Figma prompt — FRAME 7E, Trips Tab (first build)

```
Build FRAME 7E, the "Trips" screen reached via the bottom tab bar (no back arrow, tab root). Reuse
FRAME 7A's exact assignment-card row style (icon-free, plain colored status text, no chip
container, dot-connector-dot journey) — don't restate, just reuse the same row component.

APP BAR: plain title "Trips", subtitle below it "2 upcoming" (14px, #64748B, plain text, no pill).

LIST, ordered by date ascending, two rows:
1. Status "AWAITING YOUR RESPONSE" (warning amber, plain text), "Tomorrow, 8:00 AM", journey
   Nakuru HQ → Molo Sub-County Office, "James Kariuki · Agriculture".
2. Status "ACCEPTED" (plain neutral gray, #64748B), "Thu, Sep 24, 9:00 AM", journey Nakuru HQ →
   Naivasha Sub-County Office, "Grace Wanjiru · Fleet Office".

Both rows tappable (chevron on the right, same as Home's cards) — tapping either opens the Trip
Details screen already built (FRAME 7A.1), matching whichever variant fits its status.

Keep the same bottom tab bar (Home / Trips / Profile), "Trips" highlighted as active this time.
```

## 17. Splash, Login, First-Run Setup — the pre-auth flow (2026-09-22)

Real gap, not scope creep: nothing built so far got a driver from opening the app to seeing Home.
Checked the SRS directly before building anything — §9 (Security Requirements) requires "Username/
password authentication," "Single Sign-On where available," "Role-Based Access Control"; §11
(Mobile Application) lists "Driver login and assigned vehicle view" as its *first* named function.

**Onboarding carousel considered and explicitly rejected**, not just skipped. A multi-slide
feature-tour is a consumer-app pattern for building trust with someone who chose to download an
app — Joseph is handed a county-issued device with this app pre-installed for work, he doesn't
need convincing. Would have been the same category of unrequested complexity already cut elsewhere
(SOS, chat icons, decorative loading states). **Kept instead: one minimal, functional first-run
step** — language + notification permission, the two real one-time choices, no illustration or
marketing copy.

Checked real references for each: [DocuSign](https://mobbin.com/screens/38b0081f-b0a6-4213-af88-cd4ca9e8c2c7)
and [Upwork](https://mobbin.com/screens/ad035e48-ef44-4eb3-aa99-529aaca9cf14) validate a plain
single-screen login (not the multi-step email-then-password flow B2B SaaS apps use to resolve
company tenancy — doesn't apply, CVFMS is one county system). [Wispr Flow's](https://mobbin.com/screens/bf00197d-a10e-4333-bbaf-2816a04115eb)
language-confirm screen set the tone for First-Run Setup — deliberately plainer than the mostly
consumer, illustration-heavy results (Duolingo, Etsy, Hinge) the same search returned.

**No SSO button built** — SRS's SSO is conditional ("where approved and technically available"),
unconfirmed for this rollout; a speculative button for an unconfirmed integration isn't grounded.
Flagged for later, not built now.

Full specs: **Components 14-16** in `03_MASTER_DESIGN_SYSTEM.md` (mirrored), content in
`04_FIGMA_SCREEN_BLUEPRINT.md` §8, new **FRAME 7-PRE**.

**Splash/Login hierarchy corrected, 2026-09-22 — user caught a real branding error before any
render.** Original spec centered "CVFMS" as the primary brand mark on both Splash and Login's
banner. Backwards: CVFMS is the underlying platform, deployed per county — the county is the
organization a driver actually works for, so its identity should lead, with CVFMS demoted to a
quiet "Powered by" attribution. This is the standard pattern for white-labeled enterprise/
government software (deploying organization's brand leads, platform name becomes a footer credit).
**Fixed on both screens:** Splash now leads with the county crest, "Baringo County" (bold), and
"Vehicle Fleet Management System" beneath it, with "Powered by CVFMS" demoted to small, quiet text
near the bottom. Login's banner now shows "Baringo County," not "CVFMS" — the platform name doesn't
repeat on every screen, it appears once, on Splash only.

### 17a. Figma prompt — Splash, Login, First-Run Setup (fully detailed, 2026-09-22 — no longer trimmed to a 2000-char limit, see `09_PATTERN_LIBRARY.md` for why)

```
Build 3 screens for FRAME-07's pre-auth flow, in this order: Splash → Login → First-Run Setup →
Home. 390×844 mobile viewport throughout. Type: Lexend for headings/buttons, Source Sans 3 for
body/labels. Civic Green #006837 is the one accent color; everything else is white, the neutral
ink/slate/border scale already established (#0F172A ink, #334155 slate, #64748B slate-muted,
#E2E8F0 border, #F8FAFC bg), or the county landmark photo + dark overlay already used on Home and
Profile. No new colors, no new type sizes beyond what's listed below.

────────────────────────────────────────
SCREEN 1 — SPLASH
────────────────────────────────────────
Full-bleed background, solid #006837, no photo, no gradient. Status bar content in white (light
mode) — the whole screen is dark enough to need it.

**Hierarchy: the county's own identity leads, CVFMS is a quiet footer attribution, not the
headline.** CVFMS is the underlying platform, deployed per county — it isn't the organization a
driver works for, the county is, so the county's own branding gets the primary moment here, the
same way a white-labeled enterprise product typically defers to the deploying organization's brand
and demotes the platform name to a small "Powered by" line.

Centered both horizontally and vertically as one block:
- County crest/logo (Baringo County's official crest), image asset, roughly 64px tall. (This is a
  real per-county asset sourcing dependency, same as the emblem already flagged for Home's header —
  if this specific asset isn't available yet, leave the space empty rather than substitute a
  generic or wrong icon; an absent crest is honest, a wrong one isn't.)
- 16px gap below the crest.
- "Baringo County" — Lexend, weight 700, 24px, white, letter-spacing +0.01em. This is the primary
  text on the screen — the organizational identity, not the software name.
- 4px below that: "Vehicle Fleet Management System" — Source Sans 3, weight 400, 14px, white at
  reduced opacity (around 80%) — describes what this specific app is, secondary to the county name
  above it.

Near the bottom of the screen (roughly 48px above the safe-area bottom edge), centered, small and
quiet: "Powered by CVFMS" — Source Sans 3, weight 400, 12px, white at reduced opacity (around 60%).
This is the platform attribution, deliberately the least prominent text on the screen — not a
second brand competing with the county's own identity above.

Nothing else on this screen. No spinner, no loading percentage, no tagline beyond what's listed
above — this is a brief transitional screen, not a designed moment to linger on.

────────────────────────────────────────
SCREEN 2 — LOGIN
────────────────────────────────────────
HEADER BANNER: 200px height, full width. Same county landmark photo already used for Home's and
Profile's headers (reuse the identical image asset), with a dark overlay on top — #0F172A at
75-85% opacity, applied as a flat scrim or a gradient (transparent at the very top of the banner,
fading to near-solid navy by the bottom edge) — same overlay logic already locked for Home's
header, guaranteeing white text stays legible regardless of the source photo's brightness.
Status bar content in white over this banner.

On top of the banner, vertically centered: "Baringo County" — Lexend, weight 700, 18px, white
(same hierarchy logic as Splash: the county's identity, not "CVFMS," is what belongs here). No
"CVFMS" text appears on this screen at all — that platform attribution lives on Splash only, once,
not repeated on every screen a driver sees.

BELOW THE BANNER, white background (#FFFFFF), 16px side padding throughout:

24px below the banner: heading "Sign In", Lexend, weight 700, 16px, #0F172A (reuses
`type.card-title-mobile`, the same token used for card-face destination headlines elsewhere in
this app — not a new size invented for this screen).

24px below the heading, first field:
- Label "Staff Number", Source Sans 3, weight 600, 12px, uppercase, +0.02em letter-spacing, #64748B
  (reuses the same section-label treatment already locked for Trip Details/Profile).
- 4px below the label: input box, 44px height, white fill, 1px solid #E2E8F0 border, 8px corner
  radius, 14px Source Sans 3 input text in #0F172A, placeholder text (if empty) in #94A3B8.

16px below the Staff Number field, second field:
- Label "Password", same label style as above.
- 4px below: input box, same 44px/border/radius spec, masked input (dots, not visible characters
  by default), with a show/hide eye icon inside the field, right-aligned, 20px, #64748B, vertically
  centered in the field — tapping it toggles the mask.

24px below the Password field: primary button, full width, 44px height, filled #006837, white
text "Sign In", Lexend weight 600, 15px, 8px corner radius (reuses Component 9's solo-primary
button spec exactly — same height, same corner radius, same fill).

12px below the button, centered: "Forgot password?" as plain text, Source Sans 3, weight 600,
14px, #334155, no underline, no button/border styling — a quiet, low-emphasis link, not a second
button competing with "Sign In".

No SSO button, no "Create account" link, no social login icons — this app has one authentication
path for now (username/password), and nothing else is confirmed or should be implied as available.

────────────────────────────────────────
SCREEN 3 — FIRST-RUN SETUP
────────────────────────────────────────
White background throughout, no header photo, no app bar, no back arrow — this is a linear
step in the sequence, not a place a driver navigates back from. 16px side padding.

24px from the top safe area: heading "Quick Setup", Lexend, weight 700, 16px, #0F172A. No
illustration, no icon, no subtitle beneath it — the heading alone is enough context.

32px below the heading: "LANGUAGE" section label, Source Sans 3, weight 600, 12px, uppercase,
+0.02em, #64748B.

8px below the label: a two-option segmented toggle, "English" and "Kiswahili", pill-shaped,
side by side, content-hugging width (not full-width/not stretched). Reuses the exact same toggle
geometry as FRAME 7B's Pass/Fail control and FRAME 7D's language toggle: visible pill height 36px,
real tappable zone 44px (invisible padding makes up the difference — do not shrink the actual tap
target). "English" selected by default: filled #006837, white text. "Kiswahili" unselected: white
fill, 1px solid #E2E8F0 border, #334155 text.

24px below the toggle: "NOTIFICATIONS" section label, same style as "LANGUAGE" above.

8px below that label: one sentence, Source Sans 3, weight 400, 14px, #334155: "Get notified about
new assignments and updates." No icon beside it.

12px below that sentence: button "Enable Notifications", outline style — white fill, 1px solid
#E2E8F0 border, #334155 text, 44px height, content-hugging width, centered (same Secondary button
style already used for Decline and for Profile's Sign Out — not filled, this is priming a native
OS permission prompt, not the main action of this screen). Tapping this is expected to trigger the
device's native notification-permission dialog — that dialog is OS system UI, not something to
design here.

12px below that button, centered: "Skip for now" as plain text, Source Sans 3, weight 600, 14px,
#64748B, no button styling — same low-emphasis treatment as Login's "Forgot password?" link.

Pinned near the bottom of the screen (not scrolling away, matching the fixed-action-zone pattern
already used on FRAME 7B and Trip Details): primary button, full width, 44px height, filled
#006837, white text "Continue", Lexend weight 600, 15px, 8px corner radius — advances to Home.

────────────────────────────────────────
GENERAL
────────────────────────────────────────
No back arrows and no bottom tab bar on any of these three screens — this is a linear, one-way
pre-auth sequence (Splash → Login → First-Run Setup → Home), not part of the app's main tabbed
navigation, and a driver shouldn't be able to navigate backward into it once past Login.
```

## 18. FRAME 7C — Trip Start / Active Trip / Trip End locked as Component 17 (2026-09-22)

Checked FRAME-07's coverage against the full SRS §11 function list directly (user provided it):
Driver login ✅, assigned vehicle view ✅, inspection checklist ✅, Accept trip ✅ — but start/end
trip and odometer/fuel capture were only ever a rough sketch, never locked like everything else
this session. This closes that gap. Two more real SRS-named gaps remain after this (Report
Breakdown/Accident, Submit Maintenance Request) — sequenced as the next two pieces of work, not
silently dropped.

**Three real corrections made while locking this, not just a copy-paste of the old sketch:**
1. **Button height was 52px** — a leftover from before this project corrected its touch-target
   minimum to 44px. Fixed to match every other button in this app.
2. **"Camera Verified" badge on the starting odometer, dropped.** Checked Turo's odometer/fuel
   confirmation screen — the closest real analog — and found the odometer is a plain, pre-filled
   number to confirm there, not something requiring photo proof; Turo's actual photo-capture step
   is separate, optional, and about general vehicle condition, not the odometer specifically. A
   photo badge here would also have duplicated evidence Component 10's checklist already gathers
   before a driver ever reaches this screen. Fixed: Starting Odometer is now pre-filled from the
   vehicle's last recorded system reading, shown as an editable value to confirm — not blind entry,
   not photo-gated.
3. **"Does this need a distinct 'Arrived at Destination' state?" — resolved, not left open** since
   2026-09-21. A CVFMS driver has one destination per trip (any return leg is already metadata, not
   a separate step) — unlike Grab Driver's multi-stop reference, which is where this question came
   from. No "Arrived" step added; one continuous Active Trip state is sufficient.

Also fixed: the two contextual mid-trip actions ("Log Fuel Stop," "Report Breakdown/Defect") were
loosely described as "chips" — now explicitly reuse Component 9's Secondary/outline button style,
and the "TRIP SUMMARY" grouping now explicitly reuses Component 11's section-label style instead of
an undefined treatment.

Full spec: **Component 17 — Trip Start / Active Trip / Trip End** in `03_MASTER_DESIGN_SYSTEM.md`
(mirrored), content in `04_FIGMA_SCREEN_BLUEPRINT.md` §8 FRAME 7C.

### 18a. Figma prompt — FRAME 7C, Trip Start / Active Trip / Trip End (fully detailed)

```
Build 3 states for FRAME 7C, the trip lifecycle a driver goes through after a passed pre-trip
inspection. 390×844 viewport. Lexend for headings/buttons, Source Sans 3 for body/labels. Reuse
FRAME 7A's solo and paired button specs and FRAME 7A.1's section-label style exactly — don't
restate their values, just apply them.

────────────────────────────────────────
STATE 1 — START JOURNEY
────────────────────────────────────────
No back arrow (forward-only, same as the pre-auth sequence — a driver shouldn't navigate back to
"undo" starting a trip once past inspection). Plain title "Start Journey" at the top, 16px/700,
#0F172A, no app bar icons.

24px below the title: "Starting Odometer" section label (12px/600 uppercase tracked #64748B).
Below it, a large editable value, "142,850 km" — Lexend, weight 700, 28px, #0F172A — pre-filled
from the vehicle's last recorded reading in the system, not blank. No camera icon, no "verified"
badge next to it — this is a confirmable number, not something requiring photo proof.

24px below that: "Fuel Level" section label, same style. Below it: a segmented pill showing
"75% (3/4 Tank)" — light gray background (#F8FAFC), #334155 text, 12px/600, fully rounded,
non-interactive display only (not a toggle).

24px below that: one line of muted microcopy, 12px, #64748B: "Starting this trip enables
continuous GPS location logging to county dispatch."

Pinned near the bottom: primary button, full width, 44px height, filled #006837, white text
"Start Journey Now", Lexend weight 600, 15px, 8px corner radius.

────────────────────────────────────────
STATE 1.5 — ACTIVE TRIP
────────────────────────────────────────
No back arrow. At the top: a small stage indicator, "Stage 2 of 3 · In Transit" — 12px/600,
#64748B, left-aligned.

Below it, a persistent banner (no box/container, plain text — same un-boxed treatment already
used for FRAME 7B's completion banners): "In Transit to Nakuru Sub-County Office · Started
10:32 AM" — 14px/600, #0F172A.

24px below the banner: two outline buttons side by side, content-hugging width, 44px tappable/36px
visible height (same tappable-vs-visible distinction as FRAME 7B and 7A's buttons) — "Log Fuel
Stop" and "Report Breakdown / Defect", both white fill, 1px #E2E8F0 border, #334155 text, 15px
weight 600. Neither is required to proceed; tapping "Report Breakdown / Defect" would lead to a
separate reporting screen not built in this pass — for now, just make it tappable with no
destination screen yet.

Pinned near the bottom, always visible regardless of scroll: primary button, full width, 44px
height, filled #006837, white text "Complete Trip & Record Closing Odometer", Lexend weight 600,
15px, 8px corner radius.

────────────────────────────────────────
STATE 2 — END JOURNEY & CLOSURE
────────────────────────────────────────
No back arrow. Same persistent banner as State 1.5 at the top: "In Transit to Nakuru Sub-County
Office · Started 10:32 AM".

24px below the banner: "TRIP SUMMARY" section label (12px/600 uppercase tracked #64748B — same
style as FRAME 7A.1's section labels). Rows below it, 8px apart, label (14px/400, #334155) + value
(14px/600, #0F172A) pairs, aligned to a fixed label column same as FRAME 7A.1:
- "Starting Odometer" — "142,850 km" (read-only, carried over from State 1)
- "Closing Odometer" — an editable input field, placeholder "Enter reading", 44px height, 1px
  #E2E8F0 border, 8px corner radius
- "Distance Travelled" — auto-calculated once Closing Odometer is entered, "64 km traveled",
  read-only, updates live as the driver types

24px below the summary rows: "Any mechanical defects during this trip?" (14px, #334155), then two
options side by side — "None" (filled #006837 when selected) and "Report" (outline, leads to a
defect-report flow not built in this pass, same as "Report Breakdown/Defect" above).

Pinned near the bottom: primary button, full width, 44px height, filled #006837, white text
"Finalize & Close Trip", Lexend weight 600, 15px, 8px corner radius — disabled until Closing
Odometer has a value.

────────────────────────────────────────
GENERAL
────────────────────────────────────────
No bottom tab bar on any of these three states — a driver is mid-task, not browsing the app's main
sections. No back arrow anywhere in this flow, matching the same forward-only logic already used
for the pre-auth sequence.
```

### 18b. Render check (2026-09-23) — confirmed working, no real defects

First actual render of FRAME 7C since it was locked — resolves the earlier concern that this
screen set had never been verified. Strong result, no real defects found. Two positive deviations
from the original spec, both locked in as the new standard rather than reverted:
- **Stage indicator extended to all 3 states** ("Stage 1 of 3 · Ready to Start," "Stage 3 of 3 ·
  Trip Closure"), not just Active Trip as originally specced — gives the driver a complete sense of
  progress throughout, kept.
- **Starting Odometer rendered as a bordered/boxed editable field**, matching Closing Odometer's
  already-boxed treatment in State 2 — reads correctly as editable and keeps the two odometer
  fields visually consistent with each other. Kept, locked as 28px/700/#0F172A inside a bordered
  box.

One thing flagged to watch, not to fix: Active Trip (State 1.5) has a lot of empty space between
its two outline buttons and the pinned bottom button — likely fine, since this is a glanceable
mid-drive screen a driver checks briefly while stopped, not something meant to be content-dense.

Both confirmed improvements are now locked in Component 17.

## 19. FRAME 7F — Report an Issue: Breakdown/Accident locked as Component 18 (2026-09-23)

Second of the three real SRS §11 gaps found by checking against the full function list. Grounded
directly in §5.15's field list rather than guessed, and scoped honestly: §5.15 names cost/insurance
claim/investigation/liability/corrective-action fields too, but those are Grace's/Finance's/an
investigator's job filled in after intake — not something to put in front of a driver at the scene.
The driver form only includes what a person on-site can actually observe and report.

**One branching flow, not two, confirmed with the user first.** Picks a type ("Mechanical
Breakdown" or "Accident / Collision") then shows only the relevant fields — checked against Temu's
and eBay's report flows, both validate this over building two near-duplicate screens.

**Two real distinctions built in, not treated as one generic form:**
- **Breakdown path: photo is recommended, not mandatory** — deliberately different from Component
  10's Fail photo (mandatory there). A driver dealing with a live breakdown, possibly blocking
  traffic, shouldn't be gated on taking a photo before they can report it and get help.
- **Accident path triggers an immediate notification on submit**, not just a queued entry to
  Daniel — SRS §5.23 explicitly names "accident" as a notification-triggering event, a real
  severity distinction from the lower-urgency breakdown path.

Both paths reuse the offline call-fallback pattern already locked in Component 10 rather than
inventing a new one.

Full spec: **Component 18** in `03_MASTER_DESIGN_SYSTEM.md` (mirrored), content in
`04_FIGMA_SCREEN_BLUEPRINT.md` §8, new **FRAME 7F**.

### 19a. Figma prompt — FRAME 7F, Report an Issue (fully detailed)

```
Build FRAME 7F, "Report an Issue" — reached from the "Report Breakdown / Defect" button on the
Active Trip screen (FRAME 7C, State 1.5). 390×844 viewport. Lexend for headings/buttons, Source
Sans 3 for body/labels/inputs. Reuse this app's existing tokens throughout: #006837 accent,
#0F172A/#334155/#64748B/#E2E8F0/#F8FAFC neutral scale, #B91C1C for critical/required-warning
states. Reuse Component 10's exact chip geometry (unselected: white fill, 1px #E2E8F0 border,
#334155 text; selected: filled #B91C1C, white text; 32px height, content-hugging) and Component
9's exact button specs (solo-primary: filled #006837, 44px, 8px radius, full width; secondary/
outline: white fill, 1px #E2E8F0 border, #334155 text) — don't restate their values, just apply
them.

────────────────────────────────────────
SCREEN 1 — TYPE SELECTOR
────────────────────────────────────────
App bar: back arrow (returns to Active Trip), plain title "Report an Issue", 16px/700, #0F172A.

24px below the app bar: heading "What happened?", Lexend, weight 700, 16px, #0F172A.

16px below: two full-width tappable cards, stacked, 16px gap between them, each 72px tall, white
fill, 1px solid #E2E8F0 border, 8px corner radius, 16px internal padding:
- Card 1: "Mechanical Breakdown" (15px, weight 600, #0F172A) with a smaller subtitle beneath it,
  "Engine, brakes, tyres, or other mechanical issue" (13px, #64748B).
- Card 2: "Accident / Collision" (15px, weight 600, #0F172A) with subtitle "Any collision, however
  minor" (13px, #64748B).
Tapping either card advances to that path's screen below.

────────────────────────────────────────
SCREEN 2 — BREAKDOWN PATH
────────────────────────────────────────
App bar: back arrow (returns to Screen 1), title "Mechanical Breakdown".

24px below: a read-only context row, label "Vehicle" (12px/600 uppercase tracked #64748B) + value
"Toyota Land Cruiser · KBZ 442A" (14px/600 #0F172A) — auto-filled, not editable.

24px below that: "What's wrong?" section label, same style. Below it, quick-select reason chips,
multi-select: "Engine" · "Brakes" · "Tyres" · "Electrical" · "Other". At least one required to
enable Submit.

24px below the chips: "Photo (recommended)" section label — note "(recommended)" explicitly in the
label text, not implied. Below it, a camera icon + "Add Photo" outline button, same Secondary
button style, NOT required to enable Submit.

24px below: "Notes (optional)" section label, then a multi-line text area, 1px #E2E8F0 border, 8px
radius, placeholder "Anything else the Transport Office should know?" — optional.

Pinned near the bottom: primary button, full width, 44px, filled #006837, white text "Submit
Report", disabled/grayed until at least one reason chip is selected. Below it, centered, plain text
link (not a button): "No connection — Call Transport Office", 14px/600, #334155.

────────────────────────────────────────
SCREEN 3 — ACCIDENT / COLLISION PATH
────────────────────────────────────────
App bar: back arrow (returns to Screen 1), title "Accident / Collision".

24px below: two read-only context rows, same label/value style as the Breakdown path: "Vehicle" —
"Toyota Land Cruiser · KBZ 442A", "Date & Time" — auto-filled current timestamp.

16px below: "Location" row — auto-captured GPS coordinates or nearest address, shown as an
editable field (in case GPS is unavailable and the driver needs to enter it manually), 44px
height, 1px #E2E8F0 border, 8px radius.

24px below: "Description" section label, required, multi-line text area, same style as the
Breakdown path's Notes field but required, not optional — a small red asterisk after the label to
mark it required.

24px below: "Conditions" section label, quick-select chips (same geometry as the reason chips
above): "Clear" · "Rain" · "Night" · "Poor Visibility" · "Other".

24px below: "Other parties involved?" (14px, #334155) with a Yes/No segmented toggle beside it
(same pill toggle geometry as the Language toggle on FRAME 7D/First-Run Setup). If "Yes" is
selected, reveal a repeatable block beneath it: "Party name" field, "Contact" field, "Vehicle
registration" field, each 44px/1px border/8px radius, plus a plain text link "+ Add another party"
below the block.

24px below: "Police Reference (optional)" section label, single-line text field.

24px below: "Witnesses (optional)" section label, repeatable "Name" + "Contact" field pairs, plus
a plain text link "+ Add witness".

24px below: "Photos (recommended)" section label, same camera + "Add Photo" outline button as the
Breakdown path, not required.

Pinned near the bottom: primary button, full width, 44px, filled #006837, white text "Submit
Report", disabled/grayed until Description has content. Below it, same "No connection — Call
Transport Office" plain text link as the Breakdown path.

────────────────────────────────────────
GENERAL
────────────────────────────────────────
No bottom tab bar on any of these three screens — this is a task flow reached mid-trip, not one of
the app's main tabbed sections.
```

### 19b. Render check (2026-09-23) — 2 real fixes, otherwise a strong first render

Chips, buttons, disabled-state logic, and the offline fallback link all landed correctly on first
try. Two real issues found:
1. **Literal placeholder bracket text leaked into the design** — "[Auto-filled date & time]" and
   "[Captured location]" rendered as visible text instead of realistic example content.
2. **"Other parties involved?" defaulted to "No" pre-selected** — a real compliance risk, not a
   style nitpick: same category of problem already fixed for Component 10's Pass/Fail toggle,
   which deliberately starts with neither option selected so an unreviewed default can never be
   mistaken for a real answer. Fixed in Component 18: neither Yes nor No selected by default.

```
Two corrections to the Accident/Collision screen:

1. Replace the literal placeholder text "[Auto-filled date & time]" and "[Captured location]" with
   realistic example content — e.g. "Today, 2:15 PM" for Date & Time, and a real-looking location
   string (e.g. "Along B4, near Nakuru–Nairobi Highway") for Location.

2. Change "Other parties involved?" so that neither "Yes" nor "No" is selected by default — both
   should render in the unselected/outline state until the driver taps one. Currently "No" comes
   pre-selected (filled green), which risks a report going out with an unreviewed default answer to
   a factual, liability-relevant question. Matches the same no-default-state rule already used for
   the Pass/Fail toggle on the Walkaround Checklist screen.
```

## 20. FRAME 7G — Submit Maintenance Request locked as Component 19 (2026-09-23)

Third and last of the three real SRS §11 gaps found by checking against the full function list.
FRAME-07's driver-facing coverage is now complete: login, assigned vehicle view, inspection
checklist, accept/start/end trip, odometer/fuel capture, report breakdowns and accidents, and
maintenance requests.

**Odometer scope corrected after a direct question.** §5.9's work-order fields (diagnosis, parts,
labour, supplier, cost, approvals) are Workshop-only, filled in after intake — but odometer isn't:
it's a point-in-time fact the driver naturally has at hand when filing the request, same reasoning
as FRAME 7C's Starting Odometer. **Confirmed as one shared data source, not three independent
values** — the vehicle's last known odometer reading is written whenever a trip closes and read by
Trip Start, Trip End, and this screen alike.

**Routing resolved: Daniel's Dispatch Queue, same channel as every other driver-initiated
exception** (Decline, Fail-override, FRAME 7F's reports) — considered routing straight to Peter's
Workshop board since maintenance is literally Workshop's domain, but kept consistent with the
established maker-checker pattern rather than introducing a special-case path for one request type.

**Entry point:** a plain text link, "Request Maintenance," added to FRAME 7A.1 (View Details)'s
Vehicle section — a driver noticing something wrong with the vehicle they're already looking at
can act on it directly, rather than hunting for a separate location in the app.

Checked against [Rivian's "Vehicle maintenance" screen](https://mobbin.com/screens/56bd4a31-4b7f-4bd9-828d-f7098b65171a),
the closest real match — mileage as the visual centerpiece, not a minor field among many.

Full spec: **Component 19** in `03_MASTER_DESIGN_SYSTEM.md` (mirrored), content in
`04_FIGMA_SCREEN_BLUEPRINT.md` §8, new **FRAME 7G**. Also updated: Component 11's Vehicle section
now includes the "Request Maintenance" entry link.

### 20a. Figma prompt — FRAME 7G, Submit Maintenance Request (fully detailed)

```
Build FRAME 7G, "Request Maintenance" — reached by tapping the "Request Maintenance" link at the
bottom of the Trip Details screen's Vehicle section. 390×844 viewport. Lexend for headings/
buttons, Source Sans 3 for body/labels. Reuse this app's existing tokens: #006837 accent,
#0F172A/#334155/#64748B/#E2E8F0/#F8FAFC neutral scale, #B91C1C for critical states. Reuse the
exact chip geometry, button specs, and section-label style already established on FRAME 7F — don't
restate their values, just apply them.

APP BAR: back arrow (returns to Trip Details), plain title "Request Maintenance", 16px/700,
#0F172A.

24px below the app bar: a read-only context row, label "Vehicle" (12px/600 uppercase tracked
#64748B) + value "Toyota Land Cruiser · KBZ 442A" (14px/600 #0F172A) — auto-filled, not editable.

24px below that: "CURRENT ODOMETER READING" section label, same style. Below it, a large editable
value, "142,850 km" — Lexend, weight 700, 28px, #0F172A, inside a bordered box (1px #E2E8F0
border, 8px corner radius) — same treatment as the Starting Odometer field on the Start Journey
screen, pre-filled from the vehicle's last recorded reading, not blank.

24px below: "WHAT NEEDS ATTENTION?" section label. Below it, quick-select reason chips, multi-
select, same geometry as FRAME 7F's chips: "Routine Service" · "Brakes" · "Tyres" · "Engine" ·
"Electrical" · "Other". At least one required to enable Submit.

24px below the chips: "URGENCY" section label. Below it, a two-option segmented toggle, "Routine"
and "Urgent", same pill geometry as the Language toggle elsewhere in this app — neither option
selected by default; selecting "Routine" fills it #006837 white text, selecting "Urgent" fills it
#B91C1C white text (urgent is a warning-weight choice, not the standard brand green).

24px below: "DESCRIPTION (OPTIONAL)" section label, multi-line text area, 1px #E2E8F0 border, 8px
radius, placeholder "Describe what you've noticed".

24px below: "PHOTO (OPTIONAL)" section label, camera icon + "Add Photo" outline button, same
Secondary button style used throughout this app.

Pinned near the bottom: primary button, full width, 44px height, filled #006837, white text
"Submit Request", disabled/grayed until at least one "What needs attention?" chip is selected.
Below it, centered, plain text link (not a button): "No connection — Call Transport Office",
14px/600, #334155.

No bottom tab bar — this is a task flow reached from a detail screen, not one of the app's main
tabbed sections.
```

## 21. "Simple is not sterile" — a real design-language correction (2026-09-23)

Direct critique: the app had become plain to the point of boring, not just simple. Checked against
real apps rather than dismissed or fixed by feel — two research passes, one on dashboard apps
(Squarespace, Jobber, Wise, Mercury, monday.com), one on **Turo specifically**, chosen because it's
genuinely information-dense (bookings, dates, mileage, protection plans, license checks) and still
doesn't read as sterile. Found a consistent, specific set of techniques, not vague "add more
personality." **Three adopted, one considered and rejected:**

1. **Real vehicle photos are now ordinary, recurring content**, not a rare "identity moment."
   Turo shows a small photo of the actual car on every booking screen. Added to Components 11
   (Trip Details), 17 (Trip Start/Active/End), 18 (Report an Issue), and 19 (Maintenance Request) —
   64×64px, 8px corner radius, real photo per vehicle (a genuine asset-sourcing dependency, same
   category as the county emblem). The Home/Profile/Login county-photo policy is unchanged; this is
   additive.
2. **Tinted info cards for contextual notices.** Reuses an existing token (`color.brand.primary-
   subtle` `#E6F2EB`, already used for Component 9's "Ready" status) rather than inventing a new
   color. Applied to Component 17's GPS-logging notice on Trip Start as the first instance.
3. **Small, purposeful icons are back** on informational rows, reversing Component 11's "no icons"
   rule from the day before. That rule was correct on its narrow logic (a generic icon next to an
   already-labeled section duplicates the label) but the cumulative effect app-wide read as flatter
   than intended. Navigational icon use (chevron lists) is unaffected — still gated by the
   differentiation test.
4. **Considered and rejected: loosening the "one main CTA per screen" rule.** Turo uses multiple
   bold-filled buttons across one flow, each at its own contextual moment. Checked directly against
   this — **kept CVFMS's existing per-card CTA discipline as-is**, a deliberate choice already
   reasoned through earlier (Component 9's "one main green CTA" resolution), not an accident of
   over-restraint like the other three.

Full principle recorded in `03_MASTER_DESIGN_SYSTEM.md` §1 (Design Philosophy), with per-component
updates in Components 11, 17, 18, 19. Mirrored, and `04_FIGMA_SCREEN_BLUEPRINT.md` updated with
pointer notes.

### 21a. Fix prompts — apply the correction to already-rendered screens

Three screens were already built and confirmed working before this correction landed. Rather than
redo full prompts, these are scoped, additive follow-ups.

**Trip Details (FRAME 7A.1):**
```
Two additions to the Trip Details screen:

1. Add a small photo of the actual vehicle (64x64px, 8px corner radius) at the top of the
   "VEHICLE" section, beside the model/registration text.

2. Add small icons (18-20px, #64748B) before the label on each informational row across the page
   (Trip Info, Requester, Vehicle sections) — for visual warmth, not because the section labels
   need help identifying what each row is about. Keep the section labels exactly as they are; this
   is additive, not a replacement for them.
```

**FRAME 7C, all 3 states (Start Journey / Active Trip / Trip Closure):**
```
Apply these additions across all three states of the trip lifecycle screen:

1. Add a small photo of the actual vehicle (64x64px, 8px corner radius) near the top of each of
   the 3 states:
   - State 1 (Start Journey): above the Starting Odometer section.
   - State 1.5 (Active Trip): below the stage indicator/banner, above the two outline buttons —
     this state currently has a lot of empty space below the buttons, so the photo also gives that
     area real content instead of leaving it blank.
   - State 2 (End Journey & Closure): below the stage indicator/banner, above the Trip Summary
     section.

2. On State 1 only, change the GPS-logging notice ("Starting this trip enables continuous GPS
   location logging to county dispatch") from plain gray text into a soft tinted card: light green
   background (#E6F2EB), a thin border in a slightly darker green, 12px corner radius, 12px
   padding, with a small location-pin icon (16-18px, #006837) beside the text. Keep the wording
   exactly the same.

Keep everything else on all three states exactly as currently built — stage indicators, banners,
buttons, and the Trip Summary fields are all correct as-is.
```

**Report an Issue (FRAME 7F, both paths):**
```
One addition to both the Mechanical Breakdown and Accident/Collision screens:

Add a small photo of the actual vehicle (64x64px, 8px corner radius) beside the "Vehicle" context
row at the top of each screen, next to the vehicle model/registration text.
```

### 21b. Note on the Maintenance Request prompt (§20a) — not yet run, update before using

The FRAME 7G prompt above (§20a) predates this correction and doesn't include the vehicle photo.
Before running it, add this line after the "Vehicle" context row instruction: *"Add a small photo
of the actual vehicle (64×64px, 8px corner radius) beside this row — especially relevant here since
the request is specifically about the vehicle's condition."*

## 22. Second pass — "smart information categorizing and smart color use" (2026-09-23)

Direct follow-up to §21: not more graphics, better use of grouping and color on what's already
there. Two additions, checked against Navan, Rivian, and Check specifically:

1. **Stat Tile pattern** — for fact clusters that were flat rows but are actually scanned together
   (Fuel Level + Dispatch Clearance on Trip Details/Vehicle screens; Starting/Closing
   Odometer/Distance on Trip Closure). Checked against [Check's vehicle screen](https://mobbin.com/screens/9eb57d2f-f370-4af6-95c8-0280802461fe).
   Not a blanket replacement for every label/value row — sequential facts (Departure, Purpose, bay
   location) stay plain rows; only genuine clusters convert to tiles.
2. **Visual stage-stepper** for Component 17's 3-stage flow — 3 small dots beside the existing
   "Stage X of Y" text, filled for completed/current, outline for upcoming. Checked against
   [Navan's numbered checkout steps](https://mobbin.com/screens/d656dceb-9a9d-4e4a-926f-eb4614b2423b).

Full specs in `03_MASTER_DESIGN_SYSTEM.md` §1, Component 11 (Vehicle section), and Component 17
(Trip Summary + stepper). Mirrored, `04_FIGMA_SCREEN_BLUEPRINT.md` updated with pointer notes.

### 22a. Fix prompts — apply to the two already-rendered, already-photo-updated screens

These fold in on top of §21a's photo/icon additions — run together if §21a hasn't been applied yet,
or as a follow-up pass if it has.

**Trip Details (FRAME 7A.1) — Vehicle section:**
```
On the "Trip Details" screen (the page reached by tapping the chevron on a Home assignment card,
with sections labeled TRIP INFO / REQUESTER / VEHICLE), change the VEHICLE section specifically:
keep the vehicle model, registration plate, and bay location as plain text rows. But combine "Fuel
Level" and "Dispatch Clearance" into two side-by-side tiles instead of separate rows — equal width,
light gray background (#F8FAFC), 8px corner radius, 12px padding, no border needed. Each tile: a
small icon at the top, the value in bold below it (16px), and the label below that in smaller muted
text (12px). Fuel Level's icon and value stay neutral gray (#64748B) — it's not a pass/fail.
Dispatch Clearance's icon and value are green (#006837) since it shows "Passed" (would be red
#B91C1C if it were ever blocked). Do not change the Trip Info or Requester sections.
```

**FRAME 7C — the three trip-lifecycle screens (Start Journey / Active Trip / Trip Closure) — stage stepper on all three:**
```
This applies to the three screens in the driver's trip lifecycle flow, reached in this order after
a passed vehicle inspection: (1) "Start Journey" — the screen with the Starting Odometer field and
"Start Journey Now" button; (2) "Active Trip" — the screen with "Log Fuel Stop" and "Report
Breakdown / Defect" buttons and "Complete Trip & Record Closing Odometer"; (3) "Trip Closure" — the
screen with the Trip Summary section and "Finalize & Close Trip" button.

On all three of these screens, add a small visual step indicator next to the existing "Stage X of
Y" text at the top: 3 small circles (8px diameter) in a row, connected by a thin line. The
completed/current stage's circle is filled green (#006837); upcoming stages are just an outline
(#E2E8F0). On the "Start Journey" screen, only the first circle is filled. On the "Active Trip"
screen, the first two are filled. On the "Trip Closure" screen, all three are filled. Keep the
"Stage X of Y · [Label]" text exactly as it is now on each screen — this is additive, sitting
beside the text, not replacing it.
```

**FRAME 7C — the "Trip Closure" screen only (the third of the three trip-lifecycle screens, with the Trip Summary section) — Trip Summary tiles:**
```
On the "Trip Closure" screen specifically (the last screen in the trip lifecycle flow, the one with
"Finalize & Close Trip" as its bottom button), change the Trip Summary section: instead of three
stacked rows (Starting Odometer, Closing Odometer, Distance Travelled), show them as three
equal-width tiles side by side — same tile style as the Vehicle section tiles on the Trip Details
screen (light gray background #F8FAFC, 8px radius, 12px padding, small neutral-gray icon at the top
of each, bold value below, muted label below that). Closing Odometer's tile keeps its editable
input behavior — same bordered field for entering a reading, just presented inside the tile's
layout instead of a plain row. Distance still auto-calculates and updates once Closing Odometer has
a value. Do not change the "Start Journey" or "Active Trip" screens.
```

### 22b. Render check (2026-09-23) — stepper landed, three fixes from the same batch did not

Reviewed three renders of the FRAME 7C screens after the §22a prompts were run. The stage stepper
rendered correctly on all three (1/3, 2/3, 3/3 fill matching spec exactly). Three others from the
same round did not land: Trip Closure's Trip Summary was still three stacked rows, not tiles; Start
Journey's GPS notice was still plain gray text, not a tinted card; the vehicle photo (§21a) was
absent from all three screens. A regression was also spotted: Start Journey's Fuel Level lost its
segmented-pill background, rendering as plain text. These are folded into §23's consolidated
prompts below rather than re-issued separately, since §23 also changes the photo spec itself
(64×64px → full-width hero) — no point running the old photo prompt twice.

## 23. Third pass — closing the visual-polish gap against Turo/Wealthfront/Check (2026-09-23)

Direct critique, this time not about missing content but about execution confidence: current
renders (Trip Closure, Trip Details) are structurally correct but visibly flatter than Wealthfront's
"Transfer money" screen and Check's vehicle screen shown side by side. Checked against those two
plus a further Mobbin pass — [pliability](https://mobbin.com/screens/92c29d97-80f0-442c-97f6-f150fd07bd2a)
and [Alan](https://mobbin.com/screens/e2d2c425-dcb8-4974-80fa-d2773066c6f0) for icon-badge
treatment; [CRED](https://mobbin.com/screens/7e383067-74f6-4097-95bc-de0f445effd3),
[Lloyds Mobile Banking](https://mobbin.com/screens/01aa813d-d698-4466-8548-a1116253bb55), and
[Booking.com](https://mobbin.com/screens/a9bc7b70-344d-485c-8e5f-d33aa27d2972) for vehicle-detail
hierarchy. User selected all four fixes found. Full specs now in `03_MASTER_DESIGN_SYSTEM.md` §1
(third pass) and §2B3/§2C (spacing) — mirrored to `.agents/rules/master-design-system.md`.

1. **Icon Badge** (new component) — every Stat Tile icon and informational-row icon now sits in a
   32-36px tinted circle, not bare. Supersedes the second pass's bare-icon wording.
2. **Hero type contrast** — `type.hero-mobile` (22px/700), previously only used for Home's card
   time, is now applied to the one genuine focal identifier per screen. Trip Details' and Trip
   Closure/Active Trip's destination name upgrades from 16px/600 to 22px/700.
3. **Spacing bump** — new token `space.section-gap` = 32px, replacing the 24px inter-section gap
   used everywhere in §3. Mobile card padding floor raised 16px → 20px.
4. **Vehicle photo upgraded to a full-width hero** — 64×64px thumbnail superseded by full-width,
   140px height, 12px corner radius, `object-fit: cover`. Supersedes every "64×64px" reference in
   §3 (Components 11, 17, 18, 19).

### 23a. Fix prompts — Trip Details and Trip Closure (the two screens under direct critique)

These supersede §21a/§22a's photo-sizing instructions (64×64px is now wrong) and fold in the §22b
regressions (Fuel Level pill, GPS tinted card) that never landed. Run these instead of the older
photo/GPS/pill prompts, not in addition to them.

**Trip Details (the page reached by tapping the chevron on a Home assignment card, sections
labeled TRIP INFO / REQUESTER / VEHICLE):**
```
Four changes to the "Trip Details" screen:

1. Add a full-width photo of the actual vehicle at the top of the VEHICLE section, above the model/
   plate text — full card width, 140px tall, 12px corner radius, image cropped to fill (not
   letterboxed).

2. In the VEHICLE section's Fuel Level and Dispatch Clearance tiles (the two side-by-side gray
   tiles), change the icon at the top of each into a small tinted circle badge: 36px circle,
   light gray background (#F8FAFC) with a neutral gray icon (#64748B) for Fuel Level, light green
   background (#E6F2EB) with a green icon (#006837) for Dispatch Clearance (since it reads
   "Passed"). Currently the icons are bare with no circle behind them.

3. Make the destination name ("Nakuru Sub-County Office") noticeably bigger than it is now — 22px,
   bold (700) — so it's the clear single focal point of the top of the screen, bigger than the
   reference number and route line above it.

4. Increase the vertical gap between the TRIP INFO, REQUESTER, and VEHICLE section labels from the
   current spacing to 32px (currently tighter, around 24px). Keep the spacing between a section's
   own label and its first row tight and unchanged — only the gap between one section's last row
   and the next section's label grows.
```

**FRAME 7C — all three trip-lifecycle screens (Start Journey / Active Trip / Trip Closure):**
```
Changes across the three trip-lifecycle screens (Start Journey, with the Starting Odometer field;
Active Trip, with "Log Fuel Stop"/"Report Breakdown"; Trip Closure, with "Finalize & Close Trip"):

1. Add a full-width photo of the actual vehicle to each screen — full card width, 140px tall, 12px
   corner radius, cropped to fill. Position: above the Starting Odometer section on Start Journey;
   below the stage indicator/banner on Active Trip and Trip Closure.

2. On Start Journey: restore the Fuel Level pill — "75% (3/4 Tank)" should sit inside a light gray
   rounded pill (#F8FAFC background, fully rounded corners), not render as plain text with no
   container.

3. On Start Journey: change the GPS notice ("Starting this trip enables continuous GPS location
   logging to county dispatch") from plain gray text into a tinted card — light green background
   (#E6F2EB), thin border in a slightly darker green, 12px corner radius, 12px padding, with a small
   location-pin icon (16-18px, #006837) beside the text.

4. On Trip Closure: change the Trip Summary section from three stacked rows (Starting Odometer,
   Closing Odometer, Distance Travelled) into three equal-width tiles side by side — light gray
   background (#F8FAFC), 8px corner radius, 12px padding. Each tile: a small icon at the top inside
   a 36px tinted gray circle badge (#F8FAFC circle, #64748B icon — these are neutral facts, not
   pass/fail), bold value below (16px), muted label below that (12px). Closing Odometer's tile keeps
   its editable input field. Distance still auto-calculates once Closing Odometer has a value.

5. On Active Trip and Trip Closure: make the destination name in the banner ("Nakuru Sub-County
   Office") 22px bold (700) — bigger and bolder than the "Started 10:32 AM" text beside it, so it
   reads as the clear focal point of the banner.

Do not change the stage stepper dots on any of the three screens — those are correct as rendered.
```

### 23b. Render checks (2026-09-23) — photo and hero type landed, tiles failed three times

First render of the "Trip Closure"-only prompt (§23a, isolated to one screen): hero-sized
destination name landed correctly. Photo and tiles did not — reissued each as its own single-change
prompt. Second render: vehicle photo landed (as a floating product-style shot on a plain
background, matching how Booking.com/CRED/Rivian actually present their vehicle photos — better
than the literal "cropped to fill 140px" spec, kept as-is, spec not changed). **Tiles still did not
land — third consecutive miss**, despite increasingly explicit, isolated, before/after-framed
prompts.

**Root cause suspected, 2026-09-23: the prompts never specified how the Closing Odometer input
field behaves inside a ~112px-wide tile** — a real, unresolved fit problem (an inline "km" suffix
next to a 6-digit number doesn't fit that width), not just a style ambiguity. The Figma agent may
have been silently declining the whole layout change rather than guessing at an interaction it
wasn't told how to handle. **Resolved and locked in `03_MASTER_DESIGN_SYSTEM.md`, Component 17,
State 2:** drop the inline "km" suffix from the value line, move the unit into the label instead
("Closing Odometer (km)"); tapping the tile opens the device's native numeric keyboard exactly as
the original row did — no new sheet or modal. Checked against [Polarsteps](https://mobbin.com/screens/c332355f-4903-474a-96cf-f584f23dfc46)
and [MacroFactor](https://mobbin.com/screens/4eda9454-5bfc-4104-bd26-5abf50beccd8), both confirming
compact-field-triggers-native-keypad as standard, though neither shows a field this narrow with an
inline unit — the unit-in-label move is this project's own resolution to that specific fit problem.

**Fourth attempt — Trip Summary tiles only, "Trip Closure," now with the input interaction fully specified:**
```
On the "Trip Closure" screen, under the "TRIP SUMMARY" label, replace the three stacked rows with
three equal-width tiles side by side in one horizontal row. Each tile: light gray background
(#F8FAFC), 8px corner radius, 12px padding. Inside each tile, top to bottom: a small icon centered
inside a 36px circle badge (circle background #F8FAFC, icon color #64748B), then a value line, then
a label line below in muted 12px text.

Tile 1 — label "Starting Odometer (km)", value "142,850" (number only, no "km" suffix on this line
— the unit lives in the label instead, since there's no room for both in this width).

Tile 2 — label "Closing Odometer (km)", value area is a tappable input: at rest it shows placeholder
text "Enter" in muted gray; when tapped, the tile gets a green border (#006837) and the device's
native numeric keyboard opens from the bottom of the screen, exactly like a normal number field —
no popup, sheet, or dialog, just the standard keyboard; once a number is typed, the tile shows it in
bold, e.g. "142,914" (again, number only, no inline "km").

Tile 3 — label "Distance Travelled (km)", value shows "—" until tile 2 has a number in it, then
auto-calculates and displays the result, e.g. "64" (number only).

Do not add a separate popup or bottom sheet for entering the Closing Odometer value — it must behave
like a normal inline text field that happens to live inside a tile, using the system keyboard.
```

### 23c. Reverted, 2026-09-23 — both the Trip Summary tiles and the State 1.5/2 vehicle photo

Direct user pushback after the fourth tile attempt: "the three columns simply does not work and i
also dont get the purpose of having the car image." Both re-examined rather than defended, and both
turned out to be genuinely wrong calls, not just execution failures:

- **Trip Summary tiles.** The four failed render attempts (§23a-23b) turned out to be a real signal,
  not bad luck — Closing Odometer is an *active input field*, structurally unlike Vehicle section's
  two read-only facts (Fuel Level, Dispatch Clearance) that compress into tiles fine. An input wants
  a full-width label and room to be read/tapped; a third-width tile fights that. **Reverted to plain
  stacked rows — the original, working treatment.** The Stat Tile pattern itself stays correct for
  genuinely static fact clusters (Vehicle section, unchanged); this was the wrong content for it,
  not a flaw in the pattern.
- **Vehicle photo on Active Trip / Trip Closure.** The Turo precedent it was based on (§21, second
  pass) doesn't actually transfer: Turo's driver browses many different cars across many different
  bookings, so a repeated photo re-confirms identity each time in a genuinely multi-vehicle context.
  A CVFMS driver is on one continuous trip with one vehicle across three sequential screens — by
  Active Trip and Trip Closure they've already seen it twice. Repeating it a third time is
  decorative, not functional. **Reverted — photo now appears on Start Journey only**, paired with
  the pre-trip odometer/fuel checks, where it has a genuine identity-confirmation purpose before the
  trip begins. Component 11 (Trip Details), Component 18 (Report an Issue), and Component 19
  (Maintenance Request) are unaffected — each of those has its own separate justification for the
  photo (first sight of the assigned vehicle, or documentation for whoever reviews the report) that
  doesn't share Active Trip/Trip Closure's "already seen it twice" problem.

Full reasoning and updated spec in `03_MASTER_DESIGN_SYSTEM.md`, Component 17 (§1 third-pass
"applies to" scoping also corrected) — mirrored to `.agents/rules/master-design-system.md`.
`04_FIGMA_SCREEN_BLUEPRINT.md`'s FRAME 7C section updated to match.

**Cleanup prompt — reverts both, "Active Trip" and "Trip Closure" screens:**
```
Two changes, reverting recent additions that didn't work out:

1. On "Active Trip" and "Trip Closure": remove the vehicle photo from both screens entirely. Do not
   replace it with anything — the space above the content simply closes up, so the stage
   indicator/banner is followed directly by the next section as it was before the photo was added.
   (The vehicle photo on "Start Journey" stays — do not touch that screen.)

2. On "Trip Closure" only: change the TRIP SUMMARY section back from the 3-tile grid to three plain
   stacked rows, same as this screen originally had — "Starting Odometer" with value "142,850 km"
   on one line, "Closing Odometer" with its editable input field ("Enter reading" placeholder, "km"
   suffix) on the next line, "Distance Travelled" with value "—" (auto-calculating once Closing
   Odometer has a value) on the last line. Remove the gray tile backgrounds, icon badges, and
   side-by-side layout entirely — back to simple vertical rows with a label above each value.

Do not change the stage stepper dots or the hero-sized destination name in the banner on either
screen — both are correct as rendered.
```

### 23d. Start Journey confirmed correct, 2026-09-24 — and a genuine improvement found in the render

Reviewed the latest "Start Journey" render: stage stepper correct, Fuel Level pill regression from
§22b is fixed, GPS tinted card correct, Starting Odometer boxed field correct. The vehicle photo
landed as something better than what was actually specced — a render paired it directly with the
vehicle's model and plate in one horizontal identity card (photo left, "Toyota Land Cruiser" /
"KBZ 442A" right, light gray card background) instead of a bare photo floating above Starting
Odometer.

**This also directly answers a question raised the same day ("does it make sense with the car
image?") — pairing the photo with model + plate is what makes it functional rather than decorative:**
it lets the driver visually spot-check that the vehicle in front of them matches the assigned
model/plate, which a bare photo or plate-text-alone don't do as clearly together. Locked as the
standard in `03_MASTER_DESIGN_SYSTEM.md`, Component 17 State 1 (mirrored to
`.agents/rules/master-design-system.md`); `04_FIGMA_SCREEN_BLUEPRINT.md` updated to match. No
further prompt needed for this screen — it's done.

**Still outstanding from §23c:** confirmation that the "Active Trip"/"Trip Closure" photo removal
and the Trip Summary plain-row revert actually landed — not yet reviewed as of this entry.

## 24. Fuel Level moved from Start Journey into the FRAME 7B checklist (2026-09-24)

Direct question: why does Fuel Level appear on Start Journey, and how is the reading obtained?
Checked against the SRS rather than assumed — two exact citations:

- **§5.6 (Dispatch Management):** *"Before dispatch verify vehicle availability, driver assignment,
  licence, insurance, inspection, service status, **fuel level**, odometer, tyres, lights, brakes
  and safety equipment. Prevent dispatch where mandatory conditions are not met, subject to
  authorized override."* Fuel level is named as a mandatory pre-dispatch gate condition, in the same
  sentence as FRAME 7B's four existing checklist items (tyres, lights, brakes, safety equipment) —
  the same category, not something separate.
- **§5.16 (GPS and Telematics):** lists exactly what the vehicle-integration layer provides —
  location, trip history, distance, speed, geofencing, route deviation, idling, engine status,
  mileage. **Fuel is absent**, even though "engine status" and "mileage" are included — there's no
  sensor/telematics fuel source anywhere in this SRS. The reading is self-reported: the driver looks
  at the gauge, same as the other four checklist rows are the driver's own physical inspection.

**Real gap this surfaced:** Fuel Level on Start Journey was a passive pill with no pass/fail and no
blocking consequence, while the SRS treats it as a mandatory gate condition that can prevent
dispatch. User confirmed the fix: **move it into FRAME 7B's checklist as a 5th Pass/Fail row**, same
override/escalation treatment as tyres/lights/brakes/safety equipment, and remove the now-redundant
pill from Start Journey (by the time a driver reaches that screen, fuel level has already been
checked and, if inadequate, blocked).

Full spec in `03_MASTER_DESIGN_SYSTEM.md`, Component 10 (all "4" counts updated to "5": progress
pill, completion banner condition, primary CTA disabled-state condition) and Component 17 State 1
(pill removed). Mirrored to `.agents/rules/master-design-system.md`. `04_FIGMA_SCREEN_BLUEPRINT.md`
updated to match in both FRAME 7B and FRAME 7C sections.

**Fix prompt — FRAME 7B (Pre-Trip Inspection checklist), add the 5th row:**
```
On the "Pre-Trip Inspection" screen (the checklist with Tyres & Spare Wheel, Headlights/Brake
Lights & Indicators, Engine Oil & Coolant Levels, and Fire Extinguisher & First Aid Kit as its four
rows), make two changes:

1. Update the progress pill in the header from "0/4 Checked" to "0/5 Checked" (or whatever count
   reflects how many rows are currently marked).

2. Add a 5th row, "Fuel Level," below Fire Extinguisher & First Aid Kit, using the exact same row
   structure as the other four: a fuel-pump icon and the label "Fuel Level" on the first line, with
   one difference — add a small rounded pill showing "75% (3/4 Tank)" at the end of this same first
   line, right-aligned (light gray background, this is just an informational reading, not a button).
   Below that, on the second line, the same Pass/Fail two-button toggle as every other row, neither
   button selected by default.

   If this row is marked "Fail," it opens the same kind of bottom sheet as the other rows, titled
   "Report fuel level issue," but skip the "Affected item(s)" step that the other rows have (that
   step doesn't apply here) — go straight to reason chips: "Below 1/4 Tank," "Empty or Near-Empty,"
   "Fuel Gauge Malfunction," "Other." Then the same mandatory photo capture and optional detail field
   as the other rows, then Save.

Do not change anything else about the checklist — same completion banner logic, same primary button
behavior, just now counting 5 rows instead of 4.
```

**Fix prompt — "Start Journey" (FRAME 7C), remove the Fuel Level pill:**
```
On the "Start Journey" screen, remove the "FUEL LEVEL" label and its "75% (3/4 Tank)" pill entirely
— this has moved to the Pre-Trip Inspection checklist screen instead. The screen should now flow
directly from the "STARTING ODOMETER" boxed field to the GPS notice card, with nothing in between.
Do not change the vehicle identity card, Starting Odometer, GPS notice, or "Start Journey Now"
button — all correct as they are.
```


---

## 25. Desktop redesign stream: handover (2026-09-24, separate chat from mobile)

Since 2026-09-24, desktop and mobile run in **two parallel chats**. This section covers desktop
only; §13–24 are mobile. Desktop working detail lives in its own docs to avoid edit collisions:

- **`docs/13_SYSTEM_MAP.md` (read first):**
  - 9 page templates (T1 Role Home … T9 Form).
  - 18 shared patterns (P0 Page header … P17 Lifecycle stepper).
  - Component inventory: what exists in Figma vs. what to build.
  - Page register for all 13 roles.
  - Connection map: where every link goes.
  - The 9-step audit method.
- **`docs/12_DESKTOP_REDESIGN.md`:** the working log (audits, prompts, render checks). The status
  table is in §2.
- **`docs/05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`:** new entries for FRAME-01 v2, information-heavy
  pages (user picks: OpenAI, Okta, Apollo, Fresha, Wix, Xero, Airwallex, Jobber, QuickBooks),
  and page header / live-alert layout.

**Figma file facts:**
- File `bnxWZCzNtbjM0ulb886hXo`. All current work is on the page **"Refined"** (`302:456`), not
  "Page 1".
- Desktop frames are 1776px wide.
- "Refined" holds the desktop component library (Page Shell, Sidebar ×8, Top Bar, KPI Tile,
  Status Pill, Checklist Row, Alert Card, Section Card, Table cells, Tab Item, Filter Dropdown…)
  and 3 variable collections.

**Where desktop stands:**
1. **Today / Fleet overview (T1 reference):** frame `v3 / fleet-operations-overview` is
   near-locked. Its structure:
   - Page header: breadcrumb, greeting, scope switcher, freshness stamp with date.
   - Fleet state band (5 cells summing to 1,056) beside a Fuel pace card.
   - Needs attention: LIVE NOW (photos) / Blocking / This week, with groups collapsible.
   - Dispatch oversight: arrow pipeline + approvals.
   - Watch list.

   Remaining: the §8i polish prompt, plus two direct `use_figma` fixes.
2. **Vehicle requests:** the live-app page was audited (a ~21,000px page stacking 3 jobs). It's
   redesigned as a T3 registry reusing Today's parts; the prompt in doc 12 §10c is ready.
3. **Dispatch Queue:** the old render is audited (doc 12 §9). The §9a prompt is on hold until the
   user shares the updated render.
4. The user is now **sharing live-app pages one by one** for audit. Audit each with `13` §7, and
   map fixes to shared patterns.

**Standing rules added this session (all in docs + memory):**
- **Information budget** (doc 12 §7): landing ≤ 5 blocks, ≤ 4 KPI tiles, ≤ 5–6 rows per overview
  list, no number shown twice.
  - Proactively flag overload.
  - "Problems move up": modules show quiet states low on the page, and off-normal states
    promote into Needs attention.
- **User-first + reuse** (`13` top): every proposal opens with the viewer's next action and is
  built from existing templates/patterns/components. Self-check before presenting.
- **Color marks only the exception**: amber = waiting on you, red = blocked, grey = waiting on
  others. No boxes inside cards. A row about one vehicle shows its photo; a row about a group
  shows an icon.
- **Page header (P0)**: the top bar is global; breadcrumb + title live in the page header. This
  revises the 2026-09-13 "breadcrumbs only on drill-downs" decision, because the nav is now grouped.
- **Escalation** (doc 06 §0 rule 2): after 2 failed prompts on the same item, fix it directly via
  `use_figma`.
- **Mobbin** is available as an MCP server (`mcp__mobbin__search_screens`). Use it for the
  3-reference check before new patterns.

**Open decisions (need the user; proposed defaults in `13` §8):**
1. Gate Warning doesn't block dispatch; only Fail blocks.
2. Transport Officer can "Return to requester", not "Reject".
3. One insurance check with 3 states.
4. The Executive landing uses the T1 skeleton.

Added this session: gate checks get a 4th neutral state, "Not yet assigned".

**Blockers:**
- **The Figma MCP needs re-auth (`/mcp`).** Direct edits and component building depend on it.
- **Dev-side bugs** found in the live app, to pass to the dev team (doc 12 §5 and §10):
  - KPI tiles that don't reconcile or read 0.
  - A request dispatched with failing checks.
  - "Linked approved request" failing on an approved request.
  - Checks marked FAIL before assignment.
  - Stale requests never expire.
  - Pagination not applied.
  - Two ID formats.
  - Test data visible.
  - Self-approval needs a server-side check.

---

## 26. Comprehensive Project Handover (2026-10-01)

### 26.1 System State & Ground Truth
- **Figma File:** `bnxWZCzNtbjM0ulb886hXo` | Active Page: **"Refined"** (`302:456`). All production work (desktop screens, mobile driver app, component library, variable collections) lives here. Legacy copies remain on "Page 1".
- **Master Tokens & Specs:** `docs/03_MASTER_DESIGN_SYSTEM.md` (Authority).
- **Desktop Redesign Log & Prompts:** `docs/12_DESKTOP_REDESIGN.md`.
- **System Architecture & Navigation:** `docs/13_SYSTEM_MAP.md` (9 Templates T1–T9, 18 Shared Patterns P0–P17, 8 Pillar Nav).
- **Pattern Library & Auditing:** `docs/09_PATTERN_LIBRARY.md` and `docs/06_DESIGN_QUALITY_PROCESS.md`.

---

### 26.2 Key Architectural & Design Upgrades Locked (2026-09-24 to 2026-10-01)

1. **Wix Surface Architecture & Component Suite (Locked in `03` & Desktop Skill):**
   - **Canvas & Card:** Cool grey `#F4F6F8` canvas, pure white `#FFFFFF` cards, mandatory hairline `1px solid #DFE5EB` on all 4 sides, `12px/16px` radius, subtle elevation `0 1px 2px rgba(15,23,42,0.06)`.
   - **Pattern P0 (3-Row Page Header):** Row 1 Breadcrumb (`13px #64748B`) → Row 2 H1 Title (`24px/32px` Lexend 600) + Scope Switcher (`"All Stations ▾"`) & Freshness Stamp (`"Live · Updated 10:42"`) → Row 3 View Tabs / Filters.
   - **Pattern P1 (Wix Card Title Row):** Card Title (`16px/18px` Lexend 600) + explicit Time Window tag (`"Last 7 days"`, `"This month"`) + exactly ONE exit link (`"View all →"`).
   - **Calm Empty States:** Sections with 0 issues collapse into a calm single-line strip (`"All clear · No overdue items"`).
   - **3-Tier Status Taxonomy:** Dot Indicator (`• Live`) for binary/active states; plain text for normal states; soft pastel pills (`#ECFDF5`, `#FFFBEB`, `#FEF2F2`) for exceptions/warnings.
   - **Controls:** Pill buttons (`20px` radius, `#006837` primary CTA), ice-slate tinted table headers (`#EBF1F7`), trailing row action icons (`···`), and floating bottom bulk-action bars.

2. **Guerriero Structural Refactoring Standards (`03` §1.4 & `.agents/skills/design-crit-guerriero`):**
   - *Core principle:* "Refactor content to deliver more information in the same space without noise."
   - **Semantic outline SVG icon on every detail row** (Calendar, Clock, Map Pin, Person, Wrench, Document). Non-swappable.
   - **Struck-through checklists:** Done = line-through + filled checkmark; Pending = dark ink text + empty circle; Upcoming = muted grey text.
   - **Inline Action Proximity:** Action controls sit directly adjacent to the motivating data (e.g. "Assign" inline on unassigned driver row; photo icon on failed gate check).
   - **Progressive Disclosure:** No arbitrary `...` truncation; content expands via drawers, row expansion, or quick-view popovers.

3. **Photo as Identity (System-Wide Rule):**
   - Real photos confirm identity instantly without reading:
     - Vehicles: Real photo hero (`140px` height, 12px radius) in drawers/cards; 40px thumbnails in tables. Fallback = neutral licence-plate rect.
     - Drivers: `40px` circular avatar with initials fallback. Never a generic silhouette.
     - Defect/Damage: Photos are primary content, arranged in an 80px grid with click-to-expand.

4. **Desktop Viewport Correction:**
   - Standardized to **1440px wide** (240px dark navy nav rail + 1200px main content canvas). Legacy 1776px frames to be phased out via the "Desktop v2" row.

---

### 26.3 The 3 Figma AI Skills & 1 AGY Skill (All Saved to Disk)

| Skill Name | Path | Where Used | Instructions Content |
|---|---|---|---|
| `cvfms-desktop-system` | `.agents/skills/figma-skill-cvfms-desktop/SKILL.md` | Figma AI > Add skill | 1440px viewport, 8 nav pillars, Wix surface suite, Lexend/Source Sans 3, Photo as Identity, Guerriero standards, Stat Tiles, Action Drawers, AI defect guards. |
| `cvfms-mobile-system` | `.agents/skills/figma-skill-cvfms-mobile/SKILL.md` | Figma AI > Add skill | 390px PWA, collapsing navy header, 3-tab bottom nav, urgency-ordered cards, 44px buttons, walkaround checklist, lifecycle stages. |
| `cvfms-quality-audit` | `.agents/skills/figma-skill-cvfms-quality-audit/SKILL.md` | Figma AI > Add skill | 12-point defect auditor for checking rendered frames against system standards. |
| `design-crit-guerriero` | `.agents/skills/design-crit-guerriero/SKILL.md` | AGY internal skill | Guerriero design critique thinking, 7-point checklist, Before/After image references in `/references/`. |

---

### 26.4 Screen-by-Screen Status Across Streams

#### Desktop Screens (Page "Refined")
1. **FRAME-01 / T1 Fleet Operations Overview (Today):**
   - Frame `v3 / fleet-operations-overview` near-locked.
   - Structure: 3-row header, 5-cell Fleet state band + Fuel pace card, 3-tier Needs Attention list, Dispatch pipeline, and Watch list.
   - Pending: Run polish prompt (`12` §8i) and fix fuel anomaly icon + divider via direct edit.
2. **FRAME-02 / T2 Dispatch & Requisition Queue:**
   - Audited (`12` §9). Gate logic defect documented (Authorize Dispatch must disable on FAIL; override fields must hide until toggled).
   - Prompt `12` §9a ready to run.
3. **T3 Vehicle Requests:**
   - Simplified from legacy 21,000px mega-page into a standard T3 Registry with P0 header, filter row, and action drawer.
   - Prompt `12` §10c ready to run.
4. **FRAME-03 Workshop Job Board, FRAME-04 Executive Briefing, FRAME-05 Finance Dashboard, FRAME-06 Live Map:**
   - Audited; ready for Desktop v2 duplicate and redesign passes.

#### Mobile Driver App (FRAME-07 Series)
- Refined screens on page "Refined" (Home, Trip Details, Pre-Trip Checklist, Trip Start/Active/End, Defect Report).
- Type tokens, 20px card padding, 44px button height, and photo-as-identity rules fully synchronized.

---

### 26.5 Blockers & Dev Bug Backlog
1. **Figma MCP Re-Authentication:**
   - Tool `use_figma` / MCP server requires re-authentication (`/mcp` command) to execute direct canvas manipulations.
2. **Dev-Side Live Application Defects (to hand off to Dev Team):**
   - KPI metrics showing 0 or failing to reconcile.
   - Dispatch gate allowing authorization with failing checks.
   - Inconsistent identifier formats (`REQ-001` vs `VR-2024-001`).
   - Missing request expiration for stale records.
   - Lack of server-side validation against self-approval.

---

### 26.6 Immediate Next Actions for the Incoming Agent
1. **Confirm Figma AI Skill Installation:** Ensure `cvfms-desktop-system`, `cvfms-mobile-system`, and `cvfms-quality-audit` are active in Figma AI.
2. **Execute Desktop Foundation Pass (Prompt 0):** Run `docs/12_DESKTOP_REDESIGN.md §3` to create the horizontal "Desktop v2" row and apply Lexend + Source Sans 3 across all component text layers.
3. **Run Prompt 1 on FRAME-02 Dispatch Queue:** Apply the updated prompt (`docs/12_DESKTOP_REDESIGN.md §9a`) to fix the gate logic and introduce the right-hand slide-over Action Drawer.
4. **Run Vehicle Requests T3 Prompt:** Apply `docs/12_DESKTOP_REDESIGN.md §10c` to replace the bloated live-app page with the refined registry layout.

### 26.7 Corrections to §26 (desktop chat, 2026-10-01): read before acting on §26.6

§26 was written by another session and missed the desktop chat's work from 2026-09-25. The Wix
direction it describes is **confirmed by the user as the standard**, now formalised in
`03_MASTER_DESIGN_SYSTEM.md` §1.5. Corrections:

1. **Don't run §26.6 steps 2–4 as written:**
   - Prompt 0 (`12` §3): the v2/v3 frames already exist with the new fonts. Re-running it makes
     duplicates.
   - `12` §9a (Dispatch Queue): superseded. Daniel's queue is now the Requests & trips queue
     view; the current prompt is `12` §11a.
   - `12` §10c (Vehicle requests v1): already built and superseded by `12` §10g + the four role
     views (§10h → §10k, rendered).
2. **Missing from §26: decisions D1–D11** (`13_SYSTEM_MAP.md` §11, SRS-checked in §11a):
   - Only Fail blocks dispatch.
   - Transport returns, approvers reject.
   - One check per document, 3 states.
   - Executive on the T1 home.
   - Needs vehicle → Needs driver.
   - Grace reallocates *pool* allocation (§5.3) by escalation.
   - **Requests & trips** replaces Vehicle Request + Dispatch + Journey.
   - Layout set by role (no toggle).
   - One request-detail component with a role footer.
   - **Stage order: … Needs driver → Driver check-in → Ready → On trip.** ⚠ This affects the
     mobile flow: the pre-trip inspection moves *before* dispatch (SRS §5.6).
3. **Desktop skill corrected** (`.agents/skills/figma-skill-cvfms-desktop/SKILL.md`):
   - It had invented persona names ("Grace Ochieng", "Daniel Kiprop"…); restored the canonical
     Grace Wanjiru, Daniel Otieno, Peter Kamau, Miriam Chebet, Sarah N., Mary Akinyi,
     James Mwangi, Joseph Mutua.
   - Operations nav updated per D8.
   - Scope switcher moved from the top bar to the P0 header.
   - Demo data set to Nakuru County.
   - D1/D10/D11 rules added.
   **Re-upload this skill in Figma AI.**
4. **§26.2 said the Wix tokens were "locked in 03"**; they weren't until `03` §1.5 was added today.

**Current desktop next actions (replace §26.6 for desktop):**
1. Re-upload the corrected desktop skill to Figma AI.
2. Run `12` §11a (Daniel's queue: Wix + strip pass, resized to 1440).
3. Apply the same pass to the approver queue and Grace's drawer, then My requests and the form.
4. Today (T1): run the `12` §8i polish, then resize to 1440 with Wix surfaces, and lock.
5. Re-authorize the Figma MCP (`/mcp`) and build the shared components (stage strip, stepper,
   request detail, chips, pill buttons) as real Figma components to stop drift.
6. Tell the mobile chat about the D11 stage order.

---

## 27. Session handover (desktop chat, 2026-10-01 → 2026-10-02)

**Read with:** §25 (desktop stream), §26 + §26.7 (Wix direction + corrections), `13_SYSTEM_MAP.md`
(structure + decisions D1–D11), `12_DESKTOP_REDESIGN.md` §2 (status table) and §11 (Wix alignment).

### 27.1 What happened this session
1. **Visual direction settled: Wix approach** (user-confirmed).
   - Formalised in `03_MASTER_DESIGN_SYSTEM.md` §1.5 (desktop authority): 1440px, canvas #F4F6F8,
     cards with 1px #DFE5EB, pill buttons (20px radius), ice-slate table headers #EBF1F7, 3-tier
     status, semantic row icons, 140px vehicle hero in detail views.
2. **Desktop Figma skill corrected** (`.agents/skills/figma-skill-cvfms-desktop/SKILL.md`):
   - Canonical persona names restored (it had invented "Grace Ochieng", "Daniel Kiprop"…).
   - Operations nav per D8.
   - Scope switcher moved out of the top bar.
   - Nakuru demo data.
   - D1/D10/D11 rules added.
   **It must be re-uploaded in Figma AI.**
3. **Requests & trips work:**
   - Four role views rendered (Daniel's queue, approver queue, Mary's My requests, New request form).
   - Per-page fix prompts in `12` §10k.
   - The strip pass and Wix conversion for Daniel's queue are in `12` §11a (supersedes §10l).
   - The List/Queue toggle was removed (D9 revised in `13` §11).
4. **Logo exploration** (logo-design plugin installed, user scope): three greyscale concepts for a
   CVFMS mark in `brand/logo/`:
   - A Convoy
   - B Closed loop
   - C Yard bays (recommended, needs a small-size cut)

   Overview: `brand/logo/concepts.png`. **Waiting on the user to pick a direction** before building
   the kit (colour, CVFMS wordmark + lockups, favicon/app icons, presentation board, usage guide).
   No trademark search done.
5. **Git repository created** and pushed to `https://github.com/john-karanja/fleet.git`.
   **Deliberately excluded** (`.gitignore`):
   - `Test Login Accounts.docx` and the whole `deesktop app screenshots/` folder: they contain
     live-app login credentials and the live server's IP.
   - `.DS_Store`.

   Keep credentials out of the repo going forward.

### 27.2 Next actions (desktop)
1. Re-upload the corrected desktop skill to Figma AI.
2. Run `12` §11a (Daniel's queue, Wix + strip, resized to 1440); then the same pass on the approver
   queue, Grace's drawer, My requests and the New request form.
3. Today (T1): run the `12` §8i polish, then the Wix + 1440 conversion, and lock.
4. Re-authorize the Figma MCP (`/mcp`), then build the shared components (stage strip, stepper,
   request detail, chips, pill buttons) as real components.
5. Tell the mobile chat about the D11 stage order (pre-trip inspection *before* dispatch).
6. Logo: once the user picks a direction, build the kit with the logo-design skill (Phase 7).
