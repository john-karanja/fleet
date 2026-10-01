# CVFMS: Component Rebuild Instructions

**Document ID:** `DOC-CVFMS-011`
**File this applies to:** `YdYyvLxyN07dERN7bn66MS` ("CVFMS Fleet Management Design System") — **a different Figma file** from the one referenced in docs 01-10 (`bnxWZCzNtbjM0ulb886hXo`). Do not confuse the two; node IDs are not interchangeable between them.
**Source:** A detailed component audit provided by the user (2026-09-16), cross-checked directly against the file where possible. Findings below are labeled **[VERIFIED]** (confirmed directly via `get_design_context`/`use_figma` against the real file) or **[FROM AUDIT]** (taken from the user's audit as given — not independently re-checked, but no reason to doubt; verify on first touch when rebuilding).
**Access note:** This session has Viewer-only access to this file, which carries a low MCP tool-call rate limit (hit mid-investigation) — not every claim below could be independently verified before the limit was reached. Whoever executes these fixes should have Editor access and can verify claims as they go.

---

## Priority Order (matches the user's original audit — confirmed sound)

1. **Sidebar** — highest impact, used on every screen, worst current state.
2. **Top Bar** — second highest, used everywhere.
3. **Status Pill** — quick win.
4. **KPI Tile** — moderate effort.
5. **Checklist Row** — lowest priority, already mostly functional.

---

## 1. Sidebar — Rebuild, Don't Patch

**[VERIFIED] The situation is worse than "zero properties on one component."** Direct inspection found **at least 8 distinct sidebar frames/instances** scattered across the file, not one master component with instances cleanly deriving from it:
- `165:574`, `146:84`, `147:125`, `161:392`, `164:477`, `275:531` — all named "Sidebar-v2," `INSTANCE` type (need to confirm they share one main component — this check was in progress when the rate limit hit; **verify this first** when you have Editor access, using `getMainComponentAsync()` on each).
- `170:889` — a sidebar instance named just "Sidebar" (used on at least one screen — Daniel's).
- `229:895` — a "Sidebar-v2" that is a plain **FRAME**, not a component instance at all. This is either the original master (unlikely, since components render as `COMPONENT` type) or a **detached copy** that's drifted out of sync with everything else.
- `145:184` — "Sidebar/Collapsed," a real `COMPONENT`, separately maintained from the expanded version.
- **10+ more one-off sidebar frames on a "drafts" page** (`148:564`, `148:801`, `148:1087`, `148:1416`, `148:1674`, `148:2016`, `148:2392`, `148:2658`, `148:3234`, `148:3517` — none componentized), representing exploration history, not usable components.

**What this means practically:** before adding properties to "the" Sidebar-v2 component, first determine whether a single source-of-truth master component exists at all, or whether the 6+ "Sidebar-v2"-named instances have silently diverged (some may have per-instance overrides that never get fixed when you edit "the" master, because they're not actually all pointing to one master). **Audit this first, fix second** — adding properties to one component while 3 other divergent copies still exist elsewhere doesn't solve the underlying problem, it just adds a well-built 4th copy.

**[FROM AUDIT] Once consolidated to one real master component, it needs:**
- A `Active Item` property (or similar) — an instance-swap or variant control so each screen's instance can select its own active nav item without manually painting the highlight on one specific instance's overrides. This is the single highest-value fix — right now, per the user's audit, "every instance is a visual lie": they all look identical regardless of which screen they're actually on.
- An `Expanded Pillar` boolean/variant per pillar group (or a single "which pillar is expanded" enum) — currently no property controls whether e.g. Vehicle Management shows 4 sub-items or is collapsed; this is hand-set per instance.
- A configurable user name/avatar in the bottom row — currently hardcoded.
- The **Collapsed** variant (`145:184`) needs the same property treatment — it currently also has zero properties, and should ideally be a true variant of the same component set as the expanded version (a `Collapsed` boolean toggle), not a separate, independently-maintained component.

**Recommended approach:** Pick the most complete/correct existing sidebar frame as the reference (compare `229:895` against the "Sidebar-v2"-named instances to see which has the most correct content — nav grouping, icons, connector-line detail per `09_PATTERN_LIBRARY.md` §1 in the other CVFMS docs), rebuild it as ONE real component with the properties above, delete/archive the rest (the drafts-page duplicates especially — they serve no purpose once a real component exists and only cause exactly this kind of confusion later).

---

## 2. Top Bar

**[VERIFIED] Component exists as `277:536`, type `COMPONENT`** (confirmed present in the file — not yet checked for property definitions before the rate limit hit).

**[FROM AUDIT] Needs:**
- A real search icon (magnifying glass) — currently an empty frame.
- A real notification bell icon — currently an empty frame.
- Avatar should support an image fill, not just a flat gray rectangle — needed for any screen showing a real user photo.
- Bottom border needs a visually solid stroke (currently set but rendering too thin to read clearly).
- A boolean property to show/hide the status dot + text in the subtitle row — some screens (per the audit) don't need a status indicator there, and right now that's presumably handled by manually deleting the layer per-instance rather than a real property.

**When rebuilding:** since icons are missing rather than just wrong, source them from the Untitled UI base kit's Icons page (already established as the base-primitives source for this project — see `09_PATTERN_LIBRARY.md` §0 in the sibling CVFMS docs) rather than drawing new vector paths from scratch.

---

## 3. Status Pill — Quick Win

**[VERIFIED] Confirmed exactly as audited, via direct code-context inspection of `1:44` (Available) and `1:50` (Grounded):**
- **No text override property.** The component's only prop is `status?: "Available"` (a variant selector) — the visible label text ("AVAILABLE", "GROUNDED") is hardcoded per variant, not bound to an editable text property. You cannot currently show "GROUNDED — 3 days" or any custom string on an instance; you'd have to detach it and edit the layer directly, which defeats the point of a component.
- **The status dot is a separate exported SVG image** (`<img src=".../ellipse.svg">`), not a native shape with its own bound fill color. This works visually but is fragile: changing a status color requires re-exporting the asset, not adjusting a variable — and per the audit, alignment may drift at different text lengths since the dot and text aren't in a guaranteed-consistent auto-layout relationship (this second part wasn't independently re-verified before the rate limit, but is consistent with what the code context showed).
- **Colors ARE correctly bound as CSS variables** per variant (e.g. `--color/critical-bg`, `--color/critical-red` for Grounded) — this part of the component is well-built and shouldn't be touched.

**Fix:** add a `Label` text property (override text per instance, defaulting to the variant's status name so existing usage doesn't break) and a `Detail` text property (optional, for "— 3 days" style suffixes). Convert the dot from an exported image to a native ellipse/circle shape with its fill bound to the same color variable already used for the text, inside a proper auto-layout row with fixed gap — this fixes both the "can't retint easily" and "alignment may drift" issues in one pass.

**[FROM AUDIT, not verified]** Consider a generic/custom variant (e.g. "PENDING", "EXPIRED") for statuses outside the current 5, so edge cases don't require adding a new variant to the set every time one comes up.

---

## 4. KPI Tile

**[VERIFIED — but with an important caveat about which file/component]:** When this same audit-style check was run against the *other* CVFMS file, the equivalent "KPI Tile" master component (`2:2` in that file) had 20px padding on all sides and `HUG` sizing, not the "fixed 280px, uneven padding" described in an early draft of this same audit — that earlier check was against the wrong file entirely (this is the reason this document was split off with careful [VERIFIED]/[FROM AUDIT] labeling). **The actual KPI Tile in THIS file (`YdYyvLxyN07dERN7bn66MS`) has not yet been independently checked** — the rate limit was hit before reaching it. Verify its real width/sizing/padding directly before trusting either the audit's numbers or assuming it matches the other file's version.

**[FROM AUDIT] Needs (verify against the real component before applying):**
- Change from fixed width to `FILL` sizing so it adapts to its container (screens use ~373px; if the master is still fixed at 280px, this is a real mismatch worth fixing).
- Add a text override property structure: `Label`, `Value`, `Description` (or similar) — confirm these don't already exist as properties before assuming they need to be added; the equivalent component in the sibling file had zero properties despite looking like it should have some.
- Add a separator/divider option, since KPI tiles sit in a row with visual dividers between them in actual screen usage, and that's presumably not part of the standalone component.
- Fix padding to be consistent on all sides (audit reports 0 left/right, 16 top/bottom — "looks unfinished").

**Per the CVFMS simplification direction already adopted (`03_MASTER_DESIGN_SYSTEM.md` Component 2, `09_PATTERN_LIBRARY.md` §3, both in the sibling docs):** delta chips are now opt-in, not default. When rebuilding this component, do NOT make a colored delta/dot a mandatory part of the base component — add it as an optional child/property that's off by default, matching the plain-KPI-tile direction already decided for the rest of the project.

---

## 5. Checklist Row — Lowest Priority, Mostly Functional

**[FROM AUDIT, not independently verified — rate limit hit before reaching this component]:**
- Confirmed to exist as `277:535` (COMPONENT_SET) with `Status=Pass` (`277:520`) and `Status=Fail` (`277:526`) variants [VERIFIED, existence only].
- Icons (check mark, X) are described as "basic vector paths, not crisp icons matching the original screen's rendering" — worth swapping for the Untitled UI icon set the same way as Top Bar's icons, for consistency.
- Consider a boolean property to show/hide the "Reason" row on the Fail variant, for cases where a fail doesn't need an explanation shown.

---

## Notes on Method

This document intentionally separates verified findings from audit-reported ones because an earlier pass of this same investigation was run against the wrong Figma file entirely (`bnxWZCzNtbjM0ulb886hXo` instead of `YdYyvLxyN07dERN7bn66MS`) and produced a real, specific-looking but incorrect contradiction of the audit's KPI Tile claims. That mistake is the reason for this document's careful labeling — treat any future audit-vs-verification work on this project with the same discipline: confirm which file you're actually looking at before trusting specific numbers, even when they look precise and confident.
