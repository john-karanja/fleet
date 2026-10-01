# CVFMS: Design Quality Process

**Document ID:** `DOC-CVFMS-006`
**Revision:** 2.0 — full restart. The process rules below are re-derived from the same root causes the archived v1.x process doc (`docs/archive/06_DESIGN_QUALITY_PROCESS.md`) identified — a real, repeated First Draft fidelity gap, and a real silent-layout-drift incident — kept because the *causes* are structural to this tool/workflow combination, not because the old document said so. If a future round finds either rule stops applying, update this doc directly rather than silently ignoring it.

---

## §0. Figma-First vs. Code-First Decision

Figma's First Draft (text-to-design) has a measurable, repeated gap between a precise prompt and the rendered output, especially for information-dense enterprise layouts (multi-panel dashboards, tables with many columns, conditional states like a disabled button).

**Mitigation rules:**
1. **One issue per correction prompt, never batched.** A prompt asking First Draft to fix three unrelated things produces a render that fixes one, partially fixes another, and silently reverts the third. Isolate each correction.
2. **Escalation rule:** if the same specific issue fails to land after two focused correction attempts, stop prompting and fix it directly via `use_figma` (the Plugin API), which has proven reliable for precise structural changes. Don't keep re-prompting past two failures — it wastes rounds without improving odds.
3. Before writing the first prompt for any frame, run the pre-generation checklist in §1 below. Reactive fixing (discovering an issue after a bad render) is more expensive than front-loading the same check before generation — this was the single largest source of rework in the prior version of this project.

---

## §1. Mandatory Pre-Generation Checklist (run BEFORE the first prompt for any frame)

1. **3-reference Mobbin check.** Pull at least 3 real-world reference screens for the frame's dominant, novel component (see `05_MOBBIN_BENCHMARK_AND_ALIGNMENT.md` for the target search per component). Record borrow/reject findings there before writing the prompt.
2. **NN/g dashboard heuristics pass.** Check the planned layout against: visibility of system status, match between system and real-world terms (use the county's own vocabulary — "requisition," "dispatch," "workshop," not generic SaaS terms), user control (can Grace back out of an action drawer without committing?), consistency with the rest of the system's components, error prevention (is a destructive/consequential action gated the way §3's disabled-until-valid pattern requires?).
3. **Five-second rule — sharpened test procedure (2026-09-16, per `10_DASHBOARD_DESIGN_KNOWLEDGE.md` §2.4).** Could the target persona look at the finished frame for five seconds and correctly state what it's for and what the single most important thing on it is? The specific test: show the render for five seconds, take it away, ask what they remember. **The failure signal is not just "they couldn't say" — it's if what they recall FIRST is the layout, colors, or visual style rather than the actual metric or action item.** Recalling "it was green and had a big number" before recalling what the number was or meant is the same failure as not remembering at all — the hierarchy is prioritizing visual style over the content it's supposed to carry. If either failure mode shows up, the layout's hierarchy is wrong before a single pixel is generated — fix the plan, not the render.
4. **Component enumeration (§0B below) is written and current** for the frame being built.
5. **Decorative-element test (§4 below)** has been run against every chart, sparkline, or visual flourish planned for the frame — not just the ones that feel decorative at a glance.
6. **Token-value spot check (§2 below)** — confirm the specific tokens this frame will use (colors, type sizes) are the current values in `03_MASTER_DESIGN_SYSTEM.md`, not a memorized or previously-used value that may have since changed.

Only after all six pass does the first prompt get written.

---

## §0C. Always Re-State the Full Left Nav List, Every Prompt, No Exceptions

**Root cause this rule exists for:** the full 20-item SRS §2 module nav (`03_MASTER_DESIGN_SYSTEM.md` Component 1) silently shrank to 8 items on two consecutive screen generations (FRAME-02, then FRAME-03), even though each prompt only asked to change the *active* nav item, not the list itself — First Draft cannot be trusted to remember or infer the full list from a prior screen or from "same shell as before" instructions.

**Rule:** every single screen-generation prompt from here forward must include the complete, verbatim 20-item nav list (Fleet Registry through Audit, in SRS §2 order), even when the prompt is describing a screen whose shell should look identical to one built moments ago. Never reference the nav by shorthand ("same left sidebar as the other screens") without also pasting the full list inline. This applies to every remaining frame (FRAME-04, All Vehicles, FRAME-06) and to every future correction/fix prompt that touches or re-renders the app shell.

## §0B. Spec Leads Build — No Silent Layout Drift

**Root cause this rule exists for:** in the prior version of this project, a component (Vehicle Status Board) disappeared from a page without anyone deciding that — a correction prompt left a gap that First Draft filled plausibly, and nobody noticed until a later review. The failure wasn't the disappearance itself; it was that no one could tell, after the fact, whether it was a deliberate removal or an accident.

**Rule:** every frame's component list must be:
1. Explicitly enumerated in its blueprint section (`04_FIGMA_SCREEN_BLUEPRINT.md`) as a numbered or named list, not just implied by a diagram.
2. Updated *before* any prompt that changes it — the blueprint is the plan, the render is the output; the plan changes first.
3. Checked item-by-item against the actual render immediately after generation. If a component from the list is missing, that's a defect to fix, not a fait accompli to accept because "it looks fine without it."

---

## §2. Token Value Verification

Token *values* (not just layout/process) must be checked against a real, load-bearing source before being treated as final — a plausible-looking hex code or spacing value that was never actually verified against anything is a liability in an audit-sensitive enterprise system. For this restart, the verification source is the `ui-ux-pro-max` skill's research databases (color/typography/style domains), cross-checked for WCAG contrast ratios directly (see `03_MASTER_DESIGN_SYSTEM.md` §2A for the computed contrast values). If a future revision wants to additionally verify against a specific published design system's real component source (as the prior version did with Atlassian's `@atlaskit/lozenge` package), record that as a new changelog entry in the design system doc, the same way — component-by-component, not as a blanket claim.

---

## §3. Interaction Pattern Standard: Gated Actions

Recurring pattern across this system (Dispatch Gate, Workshop Release, Override justification): a consequential primary action is **disabled by default** and only enables once its prerequisite condition is verifiably satisfied — never a silent background validation that fails invisibly. This is not a per-frame decision; it's a system-wide interaction standard because the same underlying risk (an action taken before its precondition is actually true) recurs in dispatch, maintenance release, and financial anomaly resolution alike. Any new gated action added to this system should follow the same shape: visible checklist → visibly disabled primary action → either all-pass unlock or an explicit override path with mandatory justification.

---

## §4. Decorative-Element Test

Before adding any chart, sparkline, icon flourish, or visual embellishment anywhere in this system, name the specific decision it would change for the viewing persona. If no such decision exists, don't add it.

**Worked examples from this restart:**
- KPI sparklines on FRAME-01 (Grace): rejected — her KPI row communicates absolute current state (Fleet Size, Availability now), and a trend arrow doesn't change what she'd do differently right now; the trend information Sarah needs lives correctly on FRAME-04 instead, where it does change a decision (is this quarter's spike new or seasonal).
- Trend charts on FRAME-04 (Sarah): kept — she explicitly cannot tell a cost spike from a seasonal pattern without one, and that ambiguity changes whether she'd flag it in a budget hearing.
- Radar/gauge/heatmap charts anywhere: rejected system-wide — no metric in the SRS's KPI list is multi-axis, single-point, or matrix-shaped enough to need one (see `03_MASTER_DESIGN_SYSTEM.md` Component 8).

---

## §5. Accessibility Is a Pre-Generation Gate, Not a Post-Hoc Audit

Per the `ui-ux-pro-max` research basis in `03_MASTER_DESIGN_SYSTEM.md` §0, this system targets WCAG AAA contrast and never conveys status by color alone. These are binding constraints checked in §1's pre-generation checklist (item 2, error prevention / consistency) — not a pass applied after a frame is otherwise "done." A frame that fails an accessibility check post-generation should be treated as an incomplete build, not a polish item.
