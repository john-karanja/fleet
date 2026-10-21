# Swiftfleet (CVFMS): Design → Code Handover

**Written:** 2026-10-21. **Audience:** a Claude Code session (or developer) in the *code* folder who will build the app from this design workspace. This workspace has no application code. It holds the spec, the design system and the Figma file.

Read this first, then follow the links. It does not repeat the full history in `08_PROJECT_HANDOVER.md` (2,480 lines, partly stale; §29 is the current summary).

---

## 1. What is being built

- **Product:** **Swiftfleet** (one word, capital S), a Swiftcent product sold to Kenyan county governments. "CVFMS" is the SRS's generic name only.
- **What it does:** vehicle requests and approvals, dispatch, driver trips, workshop job cards, fuel anomaly detection, compliance, finance, audit.
- **Source of truth for requirements:** `Kenya_County_Government_Vehicle_Fleet_Management_System_SRS.pdf` and `CVFMS_Architecture_and_Implementation_Summary.md`.
- **Target stack (per SRS):** Next.js 15, TypeScript, Tailwind, shadcn/ui, PostgreSQL.
- **Surfaces:** desktop web (1440px, 12 roles) and a driver mobile PWA (offline-first).
- **Theme:** light enterprise theme, Civic Green `#006837` as the only accent. Not a dark cockpit.

## 2. Where everything lives

| What | Where |
|---|---|
| Figma file | `bnxWZCzNtbjM0ulb886hXo`, https://www.figma.com/design/bnxWZCzNtbjM0ulb886hXo (account: SwiftGroup). Local export: `CVFMS Fleet Management Design System.fig` (Sep 16, older than the live file). |
| Git remote | https://github.com/john-karanja/fleet (`main`). Credentials and live-app screenshots are gitignored. |
| Tokens (authoritative) | `docs/03_MASTER_DESIGN_SYSTEM.md` §2 (color, type, spacing, radius, elevation) and mirrored in `.agents/rules/master-design-system.md` |
| Personas / roles | `docs/01_USER_PERSONAS.md` (16 SRS roles); `Test Login Accounts.docx` lists 13 roles (confidential, do not commit) |
| Flows and state machines | `docs/02_USER_FLOWS.md` |
| Page templates T1–T9, patterns P0–P17, page register, object model, decisions D1–D11 | `docs/13_SYSTEM_MAP.md` |
| Per-screen layout specs | `docs/04_FIGMA_SCREEN_BLUEPRINT.md` |
| Prompt fragments for patterns | `docs/09_PATTERN_LIBRARY.md` |
| Desktop redesign log | `docs/12_DESKTOP_REDESIGN.md` |
| Brand / logo | `brand/swift-fleet/world-class/` (primary kit), `brand/swift-fleet/BRIEF.md` |

## 3. Figma file inventory (checked live 2026-10-21)

**Pages:** `Page 1` (11 nodes, early frames), **`Refined`** (53 nodes, the working page), `drafts` (12).

**Variables (3 collections, all single-mode):**
- `CVFMS Colors`: 19 variables, mode Light. Matches the color tokens in doc 03 §2A.
- `CVFMS Spacing`: 8 variables.
- `CVFMS Radius`: 4 variables (6 / 8 / 12 and one more).
- **Styles:** 9 text styles, 3 effect styles, 0 paint styles.

**Components on `Refined`** (these map to React components):

| Figma component | Variants | Suggested code component |
|---|---|---|
| Layout/Page Shell, Page Shell / Landing, Page Shell / Standard | — | `AppShell` layout |
| Navigation/Sidebar | 8 | `Sidebar` (role-aware nav items) |
| Sidebar/Collapsed | — | `Sidebar` collapsed state |
| Top Bar, Top Bar / Global Utility | — | `TopBar` |
| Page Header / Landing, Page Header / Standard | — | `PageHeader` (P0: breadcrumb, greeting, scope, freshness stamp) |
| Status Pill | 5 (Available, On Trip, Grounded, Due Soon, Disposed) | `StatusPill`, always icon + text, never color alone |
| KPI Tile | — | `KpiTile` (analytics only, not on T1 landing) |
| Checklist Row | 2 (Pass/Fail) | `ChecklistRow` (Warning variant still to add) |
| Data Display/Status Row | 4 | `StatusRow` |
| Data Display/Status Breakdown Bar | — | `StatusBreakdownBar` (to be rebuilt as bar + cells, P7) |
| Data Display/Section Card | — | `SectionCard` (title · context · link) |
| Data Display/Summary Field Grid | — | `SummaryFieldGrid` (read-only facts only) |
| Data Display/Alert Card | 3 | `AlertRow` (to be rebuilt as a row, not a tinted box, P5) |
| Navigation/Tab Item | 2 | `Tabs` |
| Controls/Filter Dropdown | — | `FilterDropdown` |
| Data Display/Table Header Cell, Table Data Cell | — | `DataTable` (36px rows) |

**Not yet built in Figma** (listed in `13_SYSTEM_MAP.md` §4): Pipeline Segment, Exception Group Row, Approval Row, Watch Line, Pace Bar, Scope Switcher, Freshness Stamp, Vehicle Row, Decision Footer. Build these with `use_figma` (not AI prompts: prompting repeatedly failed on structural precision).

**Libraries attached** (community, structure only): Material 3 Design Kit, Simple Design System, iOS 18/26/27, macOS 26/27, watchOS 26, visionOS 26. Rule: use M3 for structure and accessibility only. Override every visual default (radius, shadow, icon weight) with CVFMS tokens.

**Mobile components:** the driver app (FRAME-07, sub-frames 7A–7G) has Components 9–19 specced in `03_MASTER_DESIGN_SYSTEM.md` §3. They are *specs*, not yet confirmed as Figma components in this file. Verify before relying on them.

## 4. Design tokens to put in `tailwind.config` / CSS variables

```
color.brand.primary        #006837   color.brand.primary-hover  #00522C
color.brand.primary-subtle #E6F2EB   (dark rail variant #173829)
color.neutral.ink #0F172A   slate #334155   slate-muted #64748B (≥14px only)
color.neutral.border #E2E8F0   surface #FFFFFF   bg #F8FAFC
color.status.success #059669 / subtle #ECFDF5
color.status.warning #B45309 / subtle #FFFBEB
color.status.critical #B91C1C / subtle #FEF2F2
color.status.neutral #475569
radius: sm 6 (pills) · md 8 (buttons, inputs) · lg 12 (cards)
spacing: 8pt scale 0/4/8/12/16/20/24/32/40/48/64; table row 36px; grid gap 16
shadow.card 0 1px 2px rgba(15,23,42,.06), 0 1px 3px rgba(15,23,42,.08) (never decorative)
fonts: Lexend (headings, metrics) + Source Sans 3 (body); sizes in doc 03 §2B
mobile: buttons 44px tall (ceiling), card padding 20px, 8px min gap between touch targets
icons: one set (Lucide or Heroicons), outline, 1.5px stroke, never emoji
```

Hard rules: WCAG AA minimum (AAA target), color never the only carrier of status, charts are bar and line only, one accent color.

## 5. Settled product decisions that affect code

- **Status vocabulary is one model across web and mobile** (`13_SYSTEM_MAP.md` §6a).
- **Request/Trip is the spine** of the object model (§10). Pages are views of objects.
- **D1–D11** (`13` §11), made user-first and checked against the SRS. Key ones:
  - Only a **Fail** blocks dispatch.
  - Transport officers *return* a request; approvers *reject*.
  - Pool allocation (SRS §5.3) is different from request allocation.
  - "Requests & trips" merges Vehicle Request, Dispatch and Journey.
  - Layout is set by role (no toggle).
  - One request-detail component with a role-aware footer.
  - **Stage order:** … Needs vehicle → Needs driver → Driver check-in → Ready → On trip. This puts the pre-trip inspection *before* dispatch.
- **Business rules BR-001–005** gate dispatch (BR-003 licence validity, BR-004 statutory inspection, BR-005 pooled dispatch); see doc 02.
- **Maker-checker everywhere:** no self-approval. The live test app does not enforce this server-side, so enforce it in the new backend.
- **Driver "Decline (with reason)"** routes back to the dispatch queue. Drivers cannot transfer trips.
- **Offline-first driver app** (SRS §11).
- **Brand inside county products:** the county leads (name, emblem, Civic Green UI) and Swiftfleet appears once as a one-colour "Powered by".
- All decisions marked "validate with PO" are **unvalidated with the product owner**.

## 6. Build status of screens

Roles and templates: `13_SYSTEM_MAP.md` §5. In short:
- **Built in Figma (v1 or later):** Fleet Manager Today (T1, near-locked, polish pending), Dispatch queue (T2), Finance dashboard, Workshop board, Executive briefing, All Vehicles, Live Map, Requests & trips (four role views), driver mobile app 7A–7G.
- **Specced, not built:** Requester portal (FRAME-08), Audit trail (FRAME-09).
- **Not designed:** Compliance, Vehicle detail, Administrator, Fuel Management, Mechanic, Fleet Operations pages, and the other T1 role variants (same template, different slot content per `13` §5a).

## 7. Suggested way to start the code project

1. Scaffold Next.js 15 + TypeScript + Tailwind + shadcn/ui. Load the tokens from §4 as CSS variables and a Tailwind theme.
2. Build the shell first: `AppShell`, `Sidebar`, `TopBar`, `PageHeader`, then `StatusPill`, `DataTable`, `SectionCard`. These exist in Figma and are stable.
3. Pull each component's exact numbers from Figma instead of guessing:
   - `get_design_context` on the node (load the `figma-design-to-code` skill first).
   - `get_variable_defs` for token values.
   - Node IDs shift between sessions, so find nodes by name through `get_metadata`, not from old notes.
4. Optional but worthwhile: run Figma Code Connect (`figma-code-connect` skill) to map each Figma component to its React file once they exist.
5. Implement one vertical slice first: **Requests & trips**, from request creation through approval and dispatch gate to the driver's accept. It exercises the object model, role-aware footer and the dispatch gate.
6. Take the SRS (§5 functional requirements, §18/§23 business rules and fraud controls) as the data-model source. Doc 13 §10 has the object model.

## 8. Setting up the other folder with Figma access

- Connect the Figma MCP in that folder (`/mcp`, authorize). It was re-authorized in this workspace on 2026-10-21 and works (`whoami` returns SwiftGroup).
- Copy or reference these into the code repo's `CLAUDE.md`: this file's §4 and §5, the Figma file key, and the rule "read the part of a file you need, not the whole 2,480-line handover".
- Bring `.agents/rules/` (UX, visual, master design system) across so generated UI follows the same rules.
- Keep this workspace as the design source of truth. Code repo should link to it, not copy docs.

## 9. Open items (carried over)

**Design:** re-upload the corrected desktop skill to Figma AI; finish Today (T1) polish and lock; run the Wix pass on the other role views of Requests; build the missing components in §3; tell the mobile stream about the D11 stage order; validate D1–D11 with the product owner.

**Brand:** bosses' review of the logo options pending (if "Option 2" wins, the family kit becomes primary); run the 5 Figma prompts in `brand/swift-fleet/world-class/FIGMA_PROMPTS.md`; trademark search for "Swiftfleet"; official light-background Swiftcent logo.

**Known defects in the live test app (for the dev team):** KPIs read 0 or don't reconcile; dispatch allowed with failing checks; FAIL shown before assignment; stale requests never expire; pagination not applied; two ID formats; test data in the environment; self-approval not checked server-side. Full list: `12_DESKTOP_REDESIGN.md` §5 and §10.

**Repo hygiene:** uncommitted logo work, `logos/Logo.svg` shown deleted (replaced by `Swift-Logo.svg`), and root-level `Swift Fleet Logo Options.html`, `SVG Logo Designer Review-handoff.zip`, `svg-logo-designer-review/` need reviewing before commit. Do not commit `Test Login Accounts.docx`.

## 10. Working conventions (from the owner)

- Lead with the user's next action; build every page from existing templates, patterns and components (doc 13).
- No multi-column layout for rows that contain editable fields. Tiles and grids are for read-only facts.
- Information budget: a landing page has at most 5 blocks and shows no number twice; flag overload proactively.
- Resolve open questions on user-first grounds, record the reasoning, mark "validate with PO", and keep moving.
- Mobbin: standard mode only, never spend credits; send research to the `researcher` subagent.
