# CVFMS: Dashboard Design Knowledge Base

**Document ID:** `DOC-CVFMS-010`
**Purpose:** Synthesized from 3 external articles on B2B/enterprise dashboard UX (full citations below), read in full and cross-checked against CVFMS's existing decisions rather than treated as a standalone checklist. Every principle below is marked as either **(confirmed)** — independently matches something CVFMS already does, evidence it was the right call — or **(gap)** — a real, actionable thing CVFMS has not yet addressed. This distinction is the point of the document: it's not a re-summary of 3 articles, it's a diff against our actual state.
**Source articles (read in full, 2026-09-15/16):**
1. Rucha Abhyankar, ["6 steps to design thoughtful dashboards for B2B SaaS products"](https://uxdesign.cc/design-thoughtful-dashboards-for-b2b-saas-ff484385960d), UX Collective, Jul 2025.
2. Fanny Vassilatos & Ceara Crawshaw, "Dashboard Design UX Patterns," Pencil & Paper, Aug 2026.
3. Vijesh TV, "Best Dashboard UI UX Design Principles You Must Know in 2026," Aufait UX, 2026.

**Note on images:** all 3 articles rely heavily on screenshots, hand-drawn diagrams, and named-client dashboard examples to make their points. WebFetch/pasted text captured captions and surrounding descriptions, not the actual images — anywhere below that references a specific visual example, treat it as a *described* reference, not a verified one. Where a principle's value depends on seeing the actual visual craft (not just the described pattern), that's noted.

---

## 1. Confirmed — CVFMS Already Does This (evidence the original design system reasoning was sound)

| Principle (source) | CVFMS's existing implementation |
| :--- | :--- |
| Start with the decision, not the widget (Vijesh TV §1; Abhyankar §2) | Our entire persona → journey-stage-friction → component chain (`01_USER_PERSONAS.md`, `02_USER_FLOWS.md`) already does exactly this — every component on every frame traces back to a specific friction point in a specific persona's stated journey, not a generic "what data do we have" pass. |
| Design around who's using it, not a generic audience (Vijesh TV §2; Abhyankar §1) | The 5 flagship personas were chosen specifically because their needs diverge enough to warrant distinct screens (Grace's triage hub vs. Daniel's throughput queue vs. Sarah's read-only briefing) — matches the articles' "find the overlaps and divergences" guidance almost exactly. |
| F-pattern scanning, most important content top-left (all 3 articles) | FRAME-01's Needs Attention is deliberately dominant via position (not full width) — same reasoning already documented in `04_FIGMA_SCREEN_BLUEPRINT.md` §2. |
| 3-5 KPIs above the fold, not a data dump (Vijesh TV §4; Abhyankar mistake list) | Every frame's KPI row is capped at 3-4 tiles; the "decorative-element test" in `06_DESIGN_QUALITY_PROCESS.md` §4 already enforces "don't show it just because you have the data." |
| Never color alone — pair with icon/text (Pencil & Paper "Colour-coding mishaps"; Vijesh TV) | Binding rule since the original `ui-ux-pro-max` research pass, enforced on every Status Pill, KPI delta, and chart. |
| Deltas need context — comparison, target, direction indicator (all 3 articles) | Our KPI Tile's delta chip (`03_MASTER_DESIGN_SYSTEM.md` Component 2) and Sarah's KPI-against-target pattern already do this — confirmed via the Steep/Jobber Mobbin benchmarks independently of these articles. |
| Progressive disclosure over showing everything (all 3 articles) | Needs Attention's tight Overdue/This-Week scope with a "View all compliance →" escape hatch is exactly this pattern, reasoned independently in `04_FIGMA_SCREEN_BLUEPRINT.md`. |
| Drill-down expands inline, doesn't navigate away, for low-frequency users (Pencil & Paper "Drilling into information"; Abhyankar) | Sarah's departmental breakdown (FRAME-04) already does this — confirmed via the Twenty CRM Mobbin benchmark before these articles were read. |
| 5-second rule (all 3 articles, most explicit in Vijesh TV §9) | Already our own standing rule (`06_DESIGN_QUALITY_PROCESS.md` §1) — Vijesh TV's version adds a sharper operational test (see §3 below, a real refinement, not just confirmation). |

**Takeaway from this section:** none of this is coincidence. CVFMS's design system was built by tracing every decision back to a specific SRS requirement or persona friction point, which is the same rigor these three articles independently arrive at as best practice. This is a signal the underlying method was sound, not a reason to stop checking.

---

## 2. Real Gaps — Not Yet Addressed in CVFMS, Should Be

### 2.1 Loading states (skeleton screens, not spinners)
**Source:** Vijesh TV §8, FAQ 5; Pencil & Paper "Getting Oriented."
**Gap:** No CVFMS frame spec or built screen has ever specified a loading state. Vijesh TV's reasoning is specific and worth taking seriously: a skeleton screen (a structural placeholder matching the layout about to load) gives the brain spatial context immediately, while a spinner creates dead time with no information — this is a genuine perceived-performance difference, not decoration.
**Action:** Add a Loading State pattern to `09_PATTERN_LIBRARY.md` — every data-bearing component (KPI tile, table, chart, Kanban card) gets a skeleton variant matching its own shape (a gray rounded rectangle where a KPI number would be, gray bars where table rows would be), never a generic spinner.

### 2.2 Empty states with guided first-use action
**Source:** Vijesh TV §8 (Contracting Plus Umbrella Dashboard example).
**Gap:** No CVFMS screen specs what a persona sees before any data exists — e.g., Grace's Overview on day one with zero vehicles registered, or Peter's Kanban board with no job cards yet. Currently every spec assumes populated sample data.
**Action:** For each of the 7 screens, define an explicit empty state: what does it say, what single action does it prompt (not a blank chart with no explanation). This matters specifically for CVFMS because the SRS's own data migration section (§15) implies a real onboarding period where the registry is being populated incrementally, not all at once.

### 2.3 Error states with a specific next action
**Source:** Vijesh TV §8.
**Gap:** Same as above — no error-state spec exists anywhere. "Something went wrong" is explicitly called out as a failure mode; the fix is telling the user what happened and what to do (retry, adjust a filter, contact support).
**Action:** Add to `09_PATTERN_LIBRARY.md` as a small standing pattern: every data-fetch failure state names the likely cause and the recovery action, not a generic message.

### 2.4 The 5-second test's actual mechanic (recall, not just findability)
**Source:** Vijesh TV §9.
**Refinement of an existing rule, not a brand-new one, but operationally sharper:** our existing 5-second rule (`06_DESIGN_QUALITY_PROCESS.md` §1) asks "could the persona state what the screen is for and what's most important" — Vijesh TV's version is a specific test procedure: show the dashboard for 5 seconds, take it away, ask what they remember. **If they recall the layout or colors before the actual metric, the hierarchy has failed** — a sharper failure signal than our current phrasing.
**Action:** Update `06_DESIGN_QUALITY_PROCESS.md` §1's five-second rule wording to include this specific test procedure and failure signal.

### 2.5 Formal decision-map exercise as a process step
**Source:** Vijesh TV §1 ("a simple decision map... connects every KPI to the decision it supports and the person who depends on it"); Abhyankar's metrics-prioritization spreadsheet (Impact/Actionability/Clarity scoring).
**Gap:** CVFMS's actual process jumped from persona journey stages directly to component specs — sound, but implicit. Neither article's exact artifact (a KPI-to-decision-to-person table, or an Impact/Actionability/Clarity scored list) was ever produced for CVFMS explicitly, even though the underlying reasoning exists scattered across `01_USER_PERSONAS.md` and `04_FIGMA_SCREEN_BLUEPRINT.md`.
**Action:** Not urgent to retrofit onto the 7 already-built screens, but worth using explicitly for any new screen going forward (the 11 deferred SRS roles, when that phase starts) — a one-page decision map per new persona before wireframing, per this method.

### 2.6 Saved views
**Source:** Vijesh TV §6 ("Saved views that let people return to their most-used dashboard configuration").
**Gap:** Never considered for CVFMS. Miriam's Finance dashboard (filter by department/cost-center) and Daniel's Requisition Queue (filter by department/status/date) are the two screens where this would plausibly matter — a Finance Officer re-running the same department filter every week is a real, named use case in her persona (`01_USER_PERSONAS.md` §5, "recurring monthly cycle").
**Action:** Flag as a candidate enhancement for FRAME-02 and FRAME-05's filter rows, not urgent — log in `08_PROJECT_HANDOVER.md` as a considered-but-not-committed idea.

### 2.7 Texture/pattern fills as a second accessibility layer (beyond icon+text)
**Source:** Pencil & Paper "Lines, fills and textures."
**Gap:** Our "never color alone" rule is satisfied by icon+text on Status Pills and KPI deltas, but our charts (bar/line only, per `03_MASTER_DESIGN_SYSTEM.md` Component 8) have never been checked for whether *multiple data series on the same chart* would be distinguishable without color — e.g., if FRAME-04's Expenditure Trend and Availability Trend ever needed a second line on the same chart (they currently don't — each is single-series), this would become relevant.
**Action:** Not urgent given current chart specs are all single-series, but note in Component 8: if a future chart needs 2+ series on the same axes, add distinct line-dash patterns (solid/dashed/dotted) as well as color, not color alone.

### 2.8 Blue/orange as an alternative status pairing to red/green
**Source:** Pencil & Paper "Use of colour" ("Blues to indicate positive values, and oranges for negative trends... without your UI feeling like a trading terminal").
**Considered, not adopted — reasoning recorded so it isn't re-litigated later:** CVFMS's red/amber/green status palette was chosen deliberately (`03_MASTER_DESIGN_SYSTEM.md` §0/§A) to match universal severity conventions appropriate for a government compliance/safety context (a grounded vehicle, an expired insurance policy, a failed dispatch gate are genuinely alarm-worthy, not just "a metric trending down"). The blue/orange alternative is well-suited to financial/business metrics where "down" isn't inherently alarming — it fits Sarah's and Miriam's expenditure trend charts better than it fits Grace's or Daniel's safety-gate contexts. **Decision: keep red/amber/green system-wide for consistency** (one status language across all 5 personas, per the design system's own "density without noise" philosophy) rather than split the palette by screen type — but this was a deliberate choice against a legitimate alternative, not an oversight.

---

## 3. Terminology Note — Dashboard "Types" (for internal reference, not a new decision)

Both Abhyankar and Pencil & Paper independently propose dashboard-type taxonomies (Strategic/Operational/Analytical/Tactical; Reporting/Monitoring/Exploring/Functional/Product-home). Useful for internal shorthand when discussing a new screen, mapped against our existing 5 frames:

- **FRAME-01 (Grace):** Functional/Integrated (Pencil & Paper) — "guide users toward where they need to focus," a less-urgent monitoring dashboard. Also reads as a Product Home Page (navigation + overview combined).
- **FRAME-02 (Daniel):** Operational (Abhyankar) — real-time, action-triggering, used by frontline/junior decision-makers.
- **FRAME-03 (Peter):** Operational/Tactical hybrid — department-specific (workshop), ongoing workflow tracking.
- **FRAME-04 (Sarah):** Strategic (Abhyankar) — long-term trends, senior leadership, emphasizes clarity over depth.
- **FRAME-05 (Miriam):** Analytical (Abhyankar) — medium-term, comparison-heavy, extended interaction with filters.

**Abhyankar's own caveat, worth repeating:** "you don't sit down saying 'I'm going to build an operational dashboard' — the type is a byproduct, not a prerequisite." This matches how CVFMS actually arrived at its 5 frame designs (from persona/journey friction, not from picking a dashboard type first) — the taxonomy above is descriptive, not something to design toward on the next screen.

---

## 4. What NOT to Import (checked and deliberately rejected)

- **Neither article's specific chart-selection framework (Abhyankar's "4 pillars of dataviz": Distribution/Relationship/Comparison/Composition) changes CVFMS's chart policy.** Our bar/line-only restriction (`03_MASTER_DESIGN_SYSTEM.md` Component 8) already covers every one of the SRS's actual metrics — none of our KPIs need a scatter plot (relationship) or a composition chart (stacked/pie), so this framework is useful vocabulary but doesn't add a new chart type to our system.
- **Customization/drag-and-drop widget rearrangement (Pencil & Paper "Custom personalized dashboard pattern examples," Jira example) is not adopted.** None of our 5 personas' stated needs call for this — it would be scope/complexity added without a traced requirement, failing our own decorative-element test.
- **Onboarding-embedded dashboards (Pencil & Paper's Binance example, widgets that disappear as setup completes) is not adopted for the same reason** — no CVFMS persona has a multi-step product-setup flow that a dashboard would need to scaffold.
