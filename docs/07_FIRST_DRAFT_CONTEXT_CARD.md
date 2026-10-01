# CVFMS: Figma Agent Standing Context

**Document ID:** `DOC-CVFMS-007`
**Revision:** 3.0 (2026-09-16) — rewritten. The prior version (a full token/type/spacing block meant to be pasted into every prompt) is now obsolete: the project moved to reference-based prompting specifically to reduce per-prompt length under the Figma agent's 2000-character limit, so re-pasting a full context block every time defeats that. This version is a **standing-context summary** — read it once, keep applying it, don't paste it verbatim into every prompt.
**Depends on:** `03_MASTER_DESIGN_SYSTEM.md` (tokens, authoritative if this card ever disagrees), `09_PATTERN_LIBRARY.md` (reusable component patterns and the reference-prompting format).

---

## Standing Rules (apply to every screen, don't restate these in each prompt)

**Simplicity direction (2026-09-16, benchmarked against Airwallex and Uxcel dashboards):**
- KPI tiles are **plain by default** — label + number, nothing else. No colored dot, delta chip, or icon unless a prompt explicitly names one because that specific number needs a comparison to make sense (e.g. a target).
- **One accent color** (`#006837` Civic Green) — buttons, active-nav state, links only. Don't add color to KPI tiles or passive/informational content for visual interest.
- Status colors (red/amber/green pills) are function, not decoration — only where they gate a real decision (a dispatch check, a stock-status tag), always paired with an icon or text label, never color alone.
- Flat cards: whitespace and hairline borders over heavy shadows/elevation.
- **No loading skeletons, empty states, or error states by default** — only add if a prompt explicitly asks for one on that specific screen.
- Charts: bar (comparison) or line (trend) only. No radar/gauge/donut/heatmap, no sparklines unless a prompt specifies one.

**Structure:**
- Dark left rail (`#0F172A`, 240px), grouped into 8 collapsible pillars — see `09_PATTERN_LIBRARY.md` §1 for the full list and which one to expand per screen. **Paste this nav list in full on every nav-related prompt — do not shorten or reference it by name yet** (it has regressed twice when abbreviated).
- Light top bar (56px), light page surface (`#F8FAFC`) with white cards — the dark rail is the only dark surface anywhere.
- Page title: greeting block on Grace's Overview only; plain title + status subtitle everywhere else.
- Typography: Lexend (headings) + Source Sans 3 (body). WCAG AAA contrast target throughout.

**Prompting format (2026-09-16):**
Reference an existing built screen's pattern by name and describe only the delta — e.g. "Reuse the drawer/checklist pattern from FRAME-02, with these changes: [list]" — rather than re-describing full structure each time. Roughly halves prompt length. Full self-contained prompts only for a genuinely new pattern with nothing yet to reference.

---

## Notes

- If this card ever disagrees with `03_MASTER_DESIGN_SYSTEM.md`, the design system doc is authoritative — update this card to match, not the other way around.
- Update this file whenever a standing rule changes; it should always reflect current practice, not history.
