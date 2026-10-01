# CVFMS — County Vehicle Fleet Management System

This is a design/spec workspace for a Kenyan county government fleet management platform, currently in the UX/Figma design phase (no application code yet).

**Picking this project up fresh or after a break? Read [`docs/08_PROJECT_HANDOVER.md`](docs/08_PROJECT_HANDOVER.md) first** — it summarizes current state, key decisions, and open items so you don't have to reconstruct them from the full history below.

**Actively building a new screen under time pressure? Skip straight to [`docs/09_PATTERN_LIBRARY.md`](docs/09_PATTERN_LIBRARY.md)** — copy-paste prompt fragments for every proven, confirmed-working pattern (App Shell, two-pane work surfaces, KPI rows, status lists, Kanban, data tables, drill-downs) plus a pre-flight checklist. It's the "how"; docs 01-07 below remain the "why" — read them for reasoning, not as the first stop when assembling a screen fast.

## Context & Documentation

Read these before designing, building, or revising any UI or Figma screen, in this order:
1. [`docs/01_USER_PERSONAS.md`](docs/01_USER_PERSONAS.md) — all 16 SRS roles now documented (v3.0): 5 flagship personas (Fleet Manager, Transport Officer, Workshop Manager, Executive, Finance Officer) with Figma frames built, plus 11 Wave 2 personas documented but not yet built as screens.
2. [`docs/02_USER_FLOWS.md`](docs/02_USER_FLOWS.md) — core state machines and flows (vehicle lifecycle, dispatch gate, workshop job cards, fuel anomaly detection).
3. [`docs/03_MASTER_DESIGN_SYSTEM.md`](docs/03_MASTER_DESIGN_SYSTEM.md) — canonical design tokens, components, and layout archetypes. Single source of truth for colors, type, spacing, and components.
4. [`docs/04_FIGMA_SCREEN_BLUEPRINT.md`](docs/04_FIGMA_SCREEN_BLUEPRINT.md) — exact frame directory and per-screen layout specs for Figma generation. Point `figma-generate-design` / `use_figma` at this doc.
5. [`docs/05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`](docs/05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md) — real-world Mobbin reference screens (Vercel, Sentry, Airwallex, Plane, Deel, Shopify) mapped to each frame, with concrete patterns to borrow/reject.
6. [`docs/06_DESIGN_QUALITY_PROCESS.md`](docs/06_DESIGN_QUALITY_PROCESS.md) — **required process before writing any frame's first prompt**: mandatory 3-reference Mobbin check, NN/g dashboard heuristics + five-second rule, and pre-generation Finish Pass check. Also covers how token *values* (not just layout) are verified against Atlassian Design System source.
7. [`docs/07_FIRST_DRAFT_CONTEXT_CARD.md`](docs/07_FIRST_DRAFT_CONTEXT_CARD.md) — **v3.0 (2026-09-16): standing context to read once and keep applying, not a block to paste into every prompt.** Covers the current simplicity direction (plain KPI tiles, one accent color, no default loading/error states) and the reference-based prompting format used to stay under the Figma agent's 2000-character limit.
8. [`docs/08_PROJECT_HANDOVER.md`](docs/08_PROJECT_HANDOVER.md) — project handover / entry point summarizing current state, key decisions, and open items across all of the above.
9. [`docs/09_PATTERN_LIBRARY.md`](docs/09_PATTERN_LIBRARY.md) — fast-reference companion for speed under deadline pressure: every proven pattern from the 7 screens built so far, as copy-paste prompt fragments, plus component-sourcing guidance (which parts come from the Untitled UI base kit vs. which are CVFMS-original) and a pre-flight checklist.
10. [`docs/10_DASHBOARD_DESIGN_KNOWLEDGE.md`](docs/10_DASHBOARD_DESIGN_KNOWLEDGE.md) — synthesized from 3 external dashboard-UX articles, checked against CVFMS's existing decisions rather than treated as a generic checklist. Marks each principle as confirmed (CVFMS already does it) or a real gap (loading/empty/error states, saved views, a sharper five-second-test procedure).
11. [`docs/11_COMPONENT_REBUILD_INSTRUCTIONS.md`](docs/11_COMPONENT_REBUILD_INSTRUCTIONS.md) — **applies to a DIFFERENT Figma file** (`YdYyvLxyN07dERN7bn66MS`, not `bnxWZCzNtbjM0ulb886hXo`). Rebuild instructions for 5 base components (Sidebar, Top Bar, Status Pill, KPI Tile, Checklist Row) found to lack proper component properties. Findings are labeled [VERIFIED] or [FROM AUDIT] — read the file-mismatch note at the bottom before trusting any specific number.
12. [`docs/12_DESKTOP_REDESIGN.md`](docs/12_DESKTOP_REDESIGN.md) — **desktop redesign pass (started 2026-09-24), run in a separate chat from mobile.** Audit of the 9 desktop screens on the Figma "Refined" page, execution order, and Figma AI prompts bringing them up to the refined design language (Lexend/Source Sans 3, "simple is not sterile"). Desktop prompts and render checks go here, not in the handover, until the pass is done.
13. [`docs/13_SYSTEM_MAP.md`](docs/13_SYSTEM_MAP.md) — **the structure everything hangs on (2026-09-24):** 9 page templates, ~16 shared patterns, the component inventory (existing vs. to build), a register of every page by role and template, the connection map (where every link goes), and the 9-step audit method to run on every page. Start here before designing or auditing any screen.

Source specification: [`Kenya_County_Government_Vehicle_Fleet_Management_System_SRS.pdf`](Kenya_County_Government_Vehicle_Fleet_Management_System_SRS.pdf) and [`CVFMS_Architecture_and_Implementation_Summary.md`](CVFMS_Architecture_and_Implementation_Summary.md).

## Design Rules

Project-level UX and visual design rules live in [`.agents/rules/`](.agents/rules/):
- `ux-design-instructions.md` — general UX heuristics (Hick's Law, Fitts's Law, etc.), apply to every screen.
- `visual-design-instructions.md` — general visual design defaults (color, type, spacing, components).
- `master-design-system.md` — CVFMS-specific tokens (mirrors `docs/03_MASTER_DESIGN_SYSTEM.md`); project tokens here always override the generic defaults above where they conflict.

## Relationship to `el-nino` Project

This project reuses the design pipeline and visual identity established in `/Users/dragonfly/Projects/el-nino` (Nairobi El Niño Response System): same Civic Green (`#006837`) accent for shared Kenyan county government identity, same personas → flows → design tokens → Figma blueprint → generation pipeline. Unlike el-nino's dark 12-hour EOC cockpit theme, CVFMS uses a light enterprise theme suited to daytime back-office use — do not carry over the dark cockpit styling.
