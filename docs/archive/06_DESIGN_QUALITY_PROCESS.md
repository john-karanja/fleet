# CVFMS: Design Quality Process

**Document ID:** `DOC-CVFMS-006`
**Purpose:** The standing process to run before every new frame's first Figma prompt is written, and before any frame is considered done. Formalizes what was previously done reactively (see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` Rounds 1-3 for FRAME-01, which were fix-ups after the fact) into steps that happen up front.

## 0. Figma-First vs. Code-First — decision on record

After FRAME-01 required 6 benchmark rounds and two consecutive whole-page correction prompts that failed to land (canvas contrast, icon color restraint, composition-bar proportions — see Round 6), the option of switching to a Next.js/Tailwind coded prototype (matching the SRS's actual specified stack) was raised and considered directly. **Decision: stay Figma-first**, to preserve the component library already built (Status Pill, KPI Tile, tokens, text/effect styles — all proven to propagate correctly when fixed at the source, per the pill-correction test in Figma) and keep Figma as the artifact for eventual stakeholder/county review. Trade-off accepted knowingly: First Draft has a real, repeated fidelity gap between a precise text prompt and the rendered output, especially for compound instructions (multiple simultaneous fixes in one prompt). Mitigation, effective immediately: **one issue per correction prompt, not batched fixes** — see §1B below. If a single issue still fails to render correctly after two focused attempts, re-open the code-first question rather than continuing to iterate blindly.

## 0B. Spec Leads Build — no silent layout drift (added after Round 15)

Round 15 caught a real process failure: Vehicle Status Board disappeared from FRAME-01's Overview page without anyone deciding that — a correction prompt targeting something else left a gap, First Draft rendered something plausible to fill it (Fleet Map expanding to a full row), and nobody registered that as a decision until reviewing the output. This is a different failure mode than a prompt simply not rendering correctly (§0's concern) — here the render was *self-consistent*, just not something anyone had chosen.

**Standing rule:** the component list for any frame's primary view must be stated explicitly and completely in that frame's blueprint section (e.g. `04_FIGMA_SCREEN_BLUEPRINT.md` §2A's "final component list" for FRAME-01) — a plain enumeration, not just implied by a diagram. Before sending any prompt that adds, removes, or resizes a component, **update that explicit list first**, then write the prompt from the updated list. After a build comes back, check the render against the list item-by-item — not just "does this look good" but "is everything on the list present, and is nothing extra here that isn't." If a component appears or disappears that the list didn't call for, that is a defect to fix (either the render or the list, deliberately), never something to accept silently because it happens to look fine.

## 1. Required Steps Before Writing a Frame's First Prompt

For every new frame (FRAME-02 onward), complete all three before drafting the First Draft prompt:

### Step A: Mandatory 3-Reference Mobbin Check

Search Mobbin for exactly three categories of reference, not just one broad query:

1. **Domain analog** — a product in the *same domain* if one exists (asset/inventory management → Shopify, Deel, Employment Hero; approval workflows → Airwallex, Xero; kanban/work orders → Plane, Height, Linear-style boards).
2. **Structural analog** — a product with the *same UI shape* regardless of domain (a KPI-row dashboard → Vercel, Sentry; a list-left/detail-right approval panel → Airwallex, Salesforce; a stacked distribution bar → Deel Assets).
3. **A deliberate reject case** — one reference that looks superficially similar but whose pattern is wrong for this context, documented as "reject" with the reason (e.g. Uber/Grab/Lyft live map markers rejected for a dense multi-row table; Turo's full-photo listing card rejected for a 48px table row).

Document all three (borrow + reject) in `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` under that frame's heading before writing the prompt, not after.

### Step B: NN/g Dashboard Heuristics Pass

Applies specifically to Layout Archetype A (Command Dashboard) frames — FRAME-01, FRAME-04. For queue/board archetypes (B, C), use judgment on which items apply.

1. **Most important metric has the most visual weight.** Check: on this frame, is the single most business-critical number (e.g. Grounded count, a failed gate) larger/bolder/more prominent than secondary metrics — not just present.
2. **Every anomaly has a "what do I do about this" path.** Check: for every red/amber flagged item on the screen, is there a specific, visible next action (a link, a button, a row action) — never a flag with no path forward.
3. **Data density matches decision frequency.** Check: information the user acts on daily (vehicle status) gets persistent table space; information checked weekly/monthly (e.g. lifecycle cost trends) can be one level deeper, not on the primary view.
4. **The Five-Second Rule.** Show the frame's screenshot to yourself cold (or literally ask: "if I saw only this for 5 seconds, what's the one fact I'd walk away with?"). If the answer isn't the persona's primary goal statement from `01_USER_PERSONAS.md`, the hierarchy is wrong — fix before finalizing the prompt, not after.

### Step C: Finish Pass Checklist (Pre-Check, Not Post-Check)

Run the 10-point checklist from `03_MASTER_DESIGN_SYSTEM.md` §5 **against the planned layout/prompt draft**, before generation — not only after seeing the rendered result. Write a pass/fail line for each of the 10 points into the frame's blueprint section. A prompt should not be sent to First Draft with a known Finish Pass failure already visible on paper.

### Step D: One-Issue-Per-Correction-Prompt Rule (added after Round 6)

When reviewing a rendered frame and issuing a correction (not a first-generation prompt — this applies specifically to fixing an already-generated screen):

1. **Fix exactly one visual/structural defect per correction prompt.** Two consecutive batched correction prompts for FRAME-01 (each bundling 2-3 fixes: canvas contrast + icon restraint + composition-bar math) resulted in *none* of the fixes landing in the rendered output. A single, narrowly-scoped correction is far more likely to actually render than a compound one — First Draft's fidelity degrades with instruction complexity in ways that are hard to predict in advance.
2. **After sending a single-issue correction, verify it landed before sending the next one.** Do not queue up multiple sequential single-issue prompts without checking the result of each — if issue 1's fix didn't render, sending issue 2's prompt next just compounds the confusion about what state the design is actually in.
3. **If the same single issue fails to render correctly after 2 focused attempts**, stop iterating on it via prompt corrections. Options at that point: (a) accept the current state and note the known gap, (b) attempt the fix directly via `use_figma` on the live file (proven reliable — see the Status Pill/KPI Tile token corrections earlier in this project, which propagated correctly to every instance), or (c) re-open the code-first question from §0.
4. **A full page regeneration (not a correction) is exempt from the one-issue rule** — when enough has changed that a clean regeneration is warranted (e.g. the v1.8 consolidation), write the complete, comprehensive prompt as usual. The one-issue rule applies only to *patching* an existing render, not to *replacing* it.

---

## 2. Required Steps After Generation (Unchanged, Now Formalized)

1. Screenshot/review the actual rendered output.
2. Re-run the Finish Pass checklist against what was *actually generated* (prompts don't always render exactly as written) — this is the existing post-check, kept as a second pass, not a replacement for Step C.
3. Log any gap found as a new benchmark round in `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md`, following the existing Round format (finding → reference → decision), and fold the fix into the blueprint doc (`04_FIGMA_SCREEN_BLUEPRINT.md`) so the correction is durable, not just a one-off prompt patch.

---

## 3. Token/Component Value Verification (Separate from Layout Benchmarking)

Distinct from Mobbin visual benchmarking (which validates *layout patterns*), this validates the *literal pixel/color values* in `03_MASTER_DESIGN_SYSTEM.md` itself.

**Anchor system:** Two co-primary anchors, used for different value categories — pull from whichever has a real documented/source-verifiable value for the component in question:

- **Atlassian Design System** — for approval workflows, permissions/RBAC UI, audit-trail patterns, and general type/spacing tokens. Chosen because CVFMS is an approval/audit/RBAC-heavy enterprise system, the same category Atlassian's own products (Jira, Confluence) serve.
- **IBM Carbon Design System** — for data table specs (row height, header treatment, density modes) and accessibility verification. Chosen because Carbon was purpose-built for dense enterprise data products, publishes a fully open specification (the `carbon-components`/`@carbon/*` packages), and has more rigorous documented accessibility conventions than Atlassian — which matters more here given CVFMS's public-sector compliance mandate.

Shopify Polaris remains a **tertiary/situational reference**, used only for catalog/data-table row patterns like product thumbnails (see the vehicle-thumbnail decision in `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` Round 3) — not a primary anchor.

GOV.UK Design System was considered and explicitly **not** adopted as an anchor: it has the strongest public-sector precedent and legally-grounded accessibility patterns, but is built for citizen-facing content/forms (GOV.UK services), not dense internal ops dashboards — wrong shape for Grace's cockpit or Peter's kanban board. Revisit GOV.UK specifically if/when CVFMS ever needs a citizen- or external-facing screen (unlikely in current scope — all 5 flagship personas are internal county staff).

When Atlassian and Carbon disagree on a value (e.g. different row heights), default to Carbon for anything inside a data table, and Atlassian for anything inside an approval/workflow panel or the application shell — matching each system's actual area of purpose-built strength rather than picking one arbitrarily.

**How to verify a value (learned from the v1.1.0 audit):**
- Atlassian's docs site (atlassian.design) renders exact pixel/color specs client-side — static page fetches will not return them. Do not guess values from a partial page read and present them as verified.
- Instead, pull the real npm package for the component in question (`registry.npmjs.org/@atlaskit/<component>`) and inspect the compiled CSS/JS source directly for exact values (padding, radius, height, color tokens). This is what produced the confirmed Status Pill correction in v1.1.0 (24px→20px height, 8px→6px radius).
- Their real GitHub-facing bug tracker is on Bitbucket (`atlassian-frontend-mirror`), not a public GitHub monorepo named "design-system" — don't guess GitHub URLs for their source; verify via the npm registry metadata first (`registry.npmjs.org/@atlaskit/<name>/latest`), which gives the real repo/homepage links.

**Status of the token dictionary as of v1.1.0:** Spacing scale and Status Pill (Component 2) are source-verified against real Atlassian values. KPI Tile (Component 3) hero value type is source-verified (Metric token family). Components 1, 4, 5, 6, 7 remain design-instruction-derived only — not yet checked against a real reference implementation. Audit these the same way (pull the real npm package, inspect compiled CSS) before treating their exact pixel values as anything more than a reasonable placeholder.

**Applying corrections to the live Figma file:** when a token/component value is corrected in this doc, also push the fix into the actual Figma file (`bnxWZCzNtbjM0ulb886hXo`) via `use_figma` — don't let the docs and the file drift. Since our components (Status Pill, KPI Tile, etc.) are real Figma component sets, a single fix to the main component/variant propagates automatically to every instance already placed on any frame — this was confirmed when the Status Pill height/radius fix (24→20px, 8→6px) instantly updated every pill already placed across FRAME-01's Vehicle Status Board and Compliance Countdown panel without touching those instances directly.

**Attempted and rejected: importing Atlassian/Carbon as real Figma libraries.** Checked via `get_libraries` on the working file — `libraries_available_to_add` returned empty, and direct `search_design_system` queries for "Atlassian Design System" and "Carbon Design System" returned no components/variables/styles. Atlassian does not appear to publish an official first-party Figma Community file at all (only unofficial third-party recreations exist, which we chose not to trust as a source of truth); IBM Carbon's official Community file may exist but isn't discoverable through this MCP connection's library listing. **Decision:** don't re-attempt this via the API. If a real import is ever wanted, a human needs to manually add the library inside the Figma desktop/web app first (Community tab → search → "Add to file"), after which `get_libraries` should be able to see it. Until then, continue the npm-source-verification method (pull the real package from `registry.npmjs.org/@atlaskit/<name>` or `@carbon/<name>`, inspect compiled CSS/JS) as the working, proven way to get real values — this is what produced the confirmed Status Pill and Metric-token corrections in v1.1.0.
