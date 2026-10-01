# CVFMS: Mobbin Benchmark & Alignment

**Document ID:** `DOC-CVFMS-005`
**Purpose:** World-class reference screens from Mobbin, mapped to each Wave 1 frame, with specific patterns to borrow and specific patterns to reject (because they don't fit a government audit-sensitive context). This grounds `04_FIGMA_SCREEN_BLUEPRINT.md` in real, proven enterprise UI rather than invented layout.

---

## FRAME-01 Round 16: Needs Attention narrowed — dominance ≠ full width

*User flagged that a full-width Needs Attention card wastes space: on a typical day it holds only 2-4 short rows, and stretching that content across the full page width either left dead space after each row's button or forced an uncomfortably wide gap between a row's description and its action.*

**Reasoning:** Round 9 made Needs Attention full-width as the mechanism for "dominant element on the page." But dominance is a function of elevation, position (first thing seen), and content weight — not literally occupying the entire row. Conflating "dominant" with "wide" was the actual mistake, not the width choice in isolation.

**Fix:** narrowed Needs Attention to ~60-65% of content width. Rather than leave the freed space empty (which trades one waste for another) or duplicate existing content there (which would repeat the Critical Mismatch/Compliance Countdown redundancy mistake), paired it with **Coming Up**, moved up from its prior position below Fleet Map. This pairing was chosen deliberately: both are list/urgency-shaped content, and "what's urgent now" beside "what's coming later" is a genuine, non-redundant comparison — checked against the same redundancy test used to remove Critical Mismatch (their actual content doesn't overlap, only their shape/purpose is related, which is exactly why the pairing works rather than being wasteful).

**Process note:** per the Round 15 "spec leads build" rule, this change was written into `04_FIGMA_SCREEN_BLUEPRINT.md` §2A (now v2.3, with a corrected current diagram) before any prompt was issued — not discovered after a render.

---

## FRAME-01 Round 15: Closing the loop — Vehicle Status Board's disappearance, and a standing "no silent layout drift" rule

*The Round 14 correction landed correctly, but Vehicle Status Board vanished from the page without anyone deciding that — Fleet Map simply expanded to fill its row. User called this out directly: "we keep removing and adding the same things," a fair process complaint, not a design one. This is the second time a component changed without a documented decision (the first being the sparkline row inconsistency in Round 14 itself, where the fix was at least deliberate even if the original addition wasn't fully thought through).*

**Root cause:** components were being added/removed via prompt instructions without always updating the authoritative spec first, so "what should be on the page" and "what's actually on the page" drifted independently across rounds — First Draft would render *something* plausible for an underspecified gap (like Fleet Map quietly taking a whole row), and nobody caught it as a decision until reviewing the result.

**Resolution — closed permanently, not re-opened:** Vehicle Status Board is formally removed from FRAME-01 Overview. Its original justification (Round 9 — "companion to Needs Attention, same subject two views") no longer holds now that Fleet Map already shows per-status vehicle counts and Needs Attention already surfaces the specific vehicles needing action; a condensed extra table would show arbitrary additional vehicles with no specific reason to be those ones. Fleet Map's "All Vehicles →" link is the sufficient path to the full table.

**Process fix, not just a content fix:** `04_FIGMA_SCREEN_BLUEPRINT.md` §2A now states the FULL, FINAL 5-component list for Overview explicitly (KPI row, Needs Attention, Fleet Map, Coming Up, Recent Activity) and instructs that any future add/remove must update that section first — the spec leads the build, the build should never be reverse-engineered into the spec after the fact.

---

## FRAME-01 Round 14: Two build defects escalate into real content decisions (sparkline consistency, Critical Mismatch redundancy)

*A build applying the Round 11-13 correction prompts showed two of three fixes landing (sparklines, Fleet Map) but revealed real problems on inspection: 3-of-4 KPI cards having a sparkline read as a ragged, unbalanced row, and Critical Mismatch's button fix hadn't rendered at all. Rather than issue a fourth correction-prompt cycle on the same card, the user asked the same first-principles question already used successfully in Rounds 6 and 9: does Grace need this, or is it decoration/redundancy?*

**Sparkline finding:** applying "does the trend change a decision" honestly across all 4 KPIs — only Grounded clearly qualifies (a climbing count over days is a real pattern), Availability is borderline, Fleet Size and Alerts Due don't. Building 3-of-4 with a sparkline and one without wasn't a fair test of that finding, it just looked broken. Rather than force artificial consistency (sparklines on cards with no real case) or reserve blank space (fixes layout, not the underlying honesty problem), reverted to zero sparklines on any KPI card — see `03_MASTER_DESIGN_SYSTEM.md` Component 3.

**Critical Mismatch finding:** stepping back from "what should this card look like" to "does Grace need this as its own thing" revealed the card duplicates Needs Attention's existing UTILIZATION row — same fact, two levels of detail, same redundancy pattern already fixed once before (Round 8's Compliance Countdown merge). Checked [Google Ads Recommendations](https://mobbin.com/screens/7f77aab3-3a8e-430d-8f9b-9c4b864c1f06) and [Salesforce Recommended Actions](https://mobbin.com/screens/02576646-fdbb-4d74-888b-1552861baa0f) — both show well-designed recommendations presented as normal list rows, not separately-styled cards, reinforcing the case for dissolving rather than restyling.

**Decision — where should the full detail live?** User proposed a real data-grid table (like a Wrike/ClickUp/Airtable workspace table) instead of prose-in-a-card. Checked [Wrike's Creative Team table](https://mobbin.com/screens/9705c335-9e80-449f-a3c4-9f7b9ce057d3), [ClickUp](https://mobbin.com/screens/e9639493-e0a6-46c9-93d1-d3189cbdc3c7), [Airtable](https://mobbin.com/screens/1ccf6613-4abd-420f-9d18-ac7b40a04848) — confirmed this is the standard pattern for matching two related entity types (idle vehicles, pending requests) as rows with a type column. Then weighed whether this table belongs permanently on Overview or as a linked destination: chose **linked destination**, consistent with the Round 9 principle that Overview should stay scoped to short-list triage while full tools (Vehicle Status Board, Fleet Map, and now this table) live one click away. Component 3D removed; Component 3G (Vehicle Allocation Table) added as its replacement, reached via a new link on Needs Attention's UTILIZATION row.

---

## FRAME-01 Round 13: Deeper Fleet Map benchmark — preview vs. full-tool treatment split

*Continuing the per-component deep-dive requested in Round 12, now applied to Fleet Map. Two more searches surfaced a distinction the single Round-11 Felt reference didn't capture.*

- [Uber Eats tracking view](https://mobbin.com/screens/fbbc20da-52f8-4211-b0ea-a0bedf3fd0f6) — confirms real-street-basemap-with-colored-pins is mainstream and correct, reinforcing the Round 10 build's upgrade from an abstract dot-scatter.
- [Google Analytics "Active users by Country"](https://mobbin.com/screens/b5e7543e-5eed-44a1-9fcf-2322d64a2b7e), [Chatbase "Chats by country"](https://mobbin.com/screens/48d5b7dd-5c10-44aa-a88f-95faaa1155a3) — both show a map as a *bounded, card-contained widget* with an adjacent compact data list, rather than full-bleed with a legend beneath.

**Finding:** the Round 11 spec applied Felt's full-bleed treatment identically to both the FRAME-01 preview and the FRAME-06 full tool, just at different sizes. GA/Chatbase suggest a preview widget and a full spatial tool are different *kinds* of things, not the same thing scaled down — a preview should look boundedly like a preview.

**Decision:** split the treatment. Component 3E (FRAME-01 preview) now specs a bounded map area (rounded corners inside the card's own padding) paired with a compact adjacent status+count list, per GA/Chatbase. FRAME-06 (the full Live Map) keeps the Felt/Uber Eats full-bleed treatment unchanged — noted explicitly in `04_FIGMA_SCREEN_BLUEPRINT.md` §2B so the two don't get conflated again.

---

## FRAME-01 Round 12: Deeper Critical Mismatch benchmark (user requested more references — one wasn't enough)

*User correctly pushed back that Round 11's single Zillow reference wasn't sufficient to confidently spec a genuinely unusual content shape (two unrelated lists compared side-by-side with an implied action). Ran three more targeted searches specifically for this pattern.*

- [Programa Procurement Hub](https://mobbin.com/screens/079d676e-8012-4f1d-b29a-a20bfb05a015) — Overdue/This Week sections distinguished by a restrained background-tint wash on rows, not a heavy border or boxed card — a concrete model for "how tinted should this actually be," reinforcing Round 10's direction with an example instead of just an instruction.
- [Rox Recommended Actions](https://mobbin.com/screens/3f692f59-31ca-4254-8d47-1112661613a1) — finding + supporting context + a real, clearly labeled action button. This challenged the existing spec: Critical Mismatch's action was a bare text link ("Review pending requests →"), but a concrete/specific recommendation (reallocate this vehicle to that request) reads more confidently as a button than a link.

**Decision:** changed the action element from a text link to an outlined button (not filled/primary — filled stays reserved for Needs Attention, per the Round 10 visual-weight cap, which an outline button does not violate). Confirmed the Round 10 "tone it down" direction was correct rather than overcorrected, now with a concrete reference model (Programa) rather than only an instruction.

---

## FRAME-01 Round 11: Individual component benchmark — all 5 cards checked separately (Metric Cards, Needs Attention, Critical Mismatch, Fleet Map, Coming Up)

*User asked to check Mobbin specifically for each of the 5 card types on the page individually, rather than continuing whole-page or single-issue reviews — the same per-element discipline as Round 6, applied to the current, more mature version of the page.*

- Metric cards: [Whop KPI row](https://mobbin.com/screens/0bb8b25f-0c3d-47c3-b20a-1447e7dbab9e) — thin, minimal embedded sparkline (no axis/fill/labels), quiet enough to stay secondary to the number
- Needs Attention: already resolved in Round 8 (Todoist/GitHub) — no change from this round
- Critical Mismatch: [Zillow property map panel](https://mobbin.com/screens/13d32017-f704-4bb5-995d-a2059063795b) — confirms the Round 10 direction (calm, restrained, one clear action) rather than a loud alert box
- Fleet Map: [Felt operations map](https://mobbin.com/screens/c8b96c23-975f-472b-acca-279dede6555c) — real fleet/driver-status map with floating controls and a status legend on a genuine basemap; adopted as the canonical reference for both this preview card and FRAME-06's full map
- Coming Up: [Circle Events list](https://mobbin.com/screens/bbb7b785-2793-4264-9123-5a7a24f8191b), [Luma Events list](https://mobbin.com/screens/1932af9e-e821-4bd7-b13d-fcb0cb3f2524) — date-grouped, calm, no urgency color-coding (correctly, since these are deliberately non-urgent items)

**Decisions:**
1. **Reinstated a KPI sparkline** — but explicitly distinct from the Round 6 version that was removed. Round 6 removed a *prominent, decorative* sparkline with no tied decision. Whop's version is a near-invisible hairline with no fill/axis/labels, staying genuinely secondary to the number — permitted under a narrower rule (see `03_MASTER_DESIGN_SYSTEM.md` Component 3), and only for KPIs where the trend actually carries an early-warning signal (Availability, Grounded, Alerts Due — not Fleet Size, which barely moves).
2. **Formally numbered two previously prose-only components**: Component 3E (Fleet Map Preview Card) and Component 3F (Coming Up List), both of which existed only as blueprint prose before this round, with real dimensions/anatomy specs now written for each.
3. **Critical Mismatch and Needs Attention received no new changes this round** — both were checked against fresh references and confirmed already on the right track from prior rounds.

---

## FRAME-01 Round 10: v2.0 build review — hero dominance check

*User shared a new build reflecting v1.9 row treatment + v2.0 reprioritization (Needs Attention tightened to Overdue/This Week, Vehicle Status Board replaced by a real-basemap "Fleet Map," deprioritized compliance items surfaced as a "Coming Up" list). Overall a strong, largely correct implementation of everything decided through Round 9. One issue found: the "Critical Mismatch" card (renamed Utilization Gap) rendered with a bolder/more saturated yellow-orange accent border than Needs Attention above it, risking a second competing hero on the page.*

**Finding:** visual weight discipline needs to be checked not just within a component but *between* components — a correctly-designed secondary card can still accidentally out-compete the hero if its accent color/border is more saturated, even without any other structural error.

**Decision:** added Component 3D to `03_MASTER_DESIGN_SYSTEM.md` (previously prose-only, never formally numbered) with an explicit visual-weight cap: its accent border/fill must be visibly lighter/thinner than Needs Attention's, checked as a hard constraint, not just "make it look secondary" as a vague instruction.

**What else landed correctly, not re-litigated:** Needs Attention's plain-row/dot/section-header treatment (Round 8), the type hierarchy between category tag and description (Round 7), the tightened Overdue/This-Week-only scope with a working "View all compliance →" link (Round 9), and a real-basemap Fleet Map replacing the abstract dot-scatter (an upgrade beyond what was specified — good unprompted addition, worth carrying into FRAME-06's eventual full map spec).

---

## FRAME-01 Round 9: Page reprioritized around "what does Grace actually need to see to act" (no new Mobbin search — first-principles reasoning against her documented persona)

*After several rounds of styling refinement to Needs Attention, user pushed past "how should it look" to the more fundamental question: what exactly is important for Grace to see so she can take action? Rather than another visual iteration, this required re-deriving the page's information priority from her Core Goal and Pain Points directly.*

**Reasoning:** Grace's two jobs (know the fleet's state, act before problems compound) are not equal — acting is the one that matters, since knowing without acting achieves nothing per her own stated pain point about finding out too late. This means the dashboard's job is to surface a short, genuinely urgent list — not a comprehensive one. The existing Needs Attention (7-8 items spanning Overdue through "due in 22 days") was diluting its own value by including non-urgent items alongside urgent ones.

**Decision — three changes, not a styling pass:**
1. Needs Attention tightened to Overdue + This Week only (~2-4 rows typical) — every remaining row should be something actionable today.
2. Deprioritized "this month" items get a real destination: the "Compliance" sidebar nav item, previously empty with no screen behind it, now serves this purpose via a "View all compliance →" link.
3. Vehicle Status Board and Fleet Pulse demoted from primary hero-row real estate to smaller secondary panels — both are legitimate tools Grace reaches for when she needs them, not facts that need to be surfaced unprompted on every login. Needs Attention becomes the page's unambiguous dominant element with nothing else competing for "look here first."

This changes `04_FIGMA_SCREEN_BLUEPRINT.md` from v1.9 to v2.0 — see that doc for the full updated layout. Also creates an open item: the Compliance nav destination now needs an actual screen designed (a fuller compliance list view), not yet scoped as its own frame.

---

## FRAME-01 Round 8: Needs Attention row treatment redesigned — tinted boxes replaced with plain rows + dot + section headers

*User asked directly "what are we doing with the Needs Attention card" and, after narrowing down, identified that the tinted-row-per-item pattern itself (not just its type sizing) felt too visually busy for a list used daily. This is a real redesign, not a refinement of Round 7's fix — the full-tint treatment from v1.8 is replaced, not adjusted.*

- [Todoist "Today" list](https://mobbin.com/screens/8514ba3e-5372-4b61-ab79-e11ef6ea7121) — priority communicated by a small colored dot only, plain white rows, no fill
- [GitHub issues "By priority" view](https://mobbin.com/screens/231c5ed2-c43c-47e3-82bf-5acdb0f0af82) — grouped by Urgent / No Priority section headers, plain rows throughout

**Finding:** a stack of 7-8 fully-tinted colored boxes (v1.8's treatment) is busier than how real daily-use priority tools handle the same problem — Todoist and GitHub both keep every row visually calm (plain white background) and put the entire urgency signal into either a single small dot or a section-header grouping, never a full-row fill.

**Decision:** Component 3C redesigned in `03_MASTER_DESIGN_SYSTEM.md` v1.9 — dropped per-row background tint entirely. New treatment: plain rows with a hairline bottom divider (no per-row card/box shape), an 8px colored dot as the only color accent per row, and rows grouped under urgency section headers ("OVERDUE" / "THIS WEEK" / "THIS MONTH") which now carry the primary urgency signal instead of row color. Category tag and description text hierarchy (Round 7's §B2 fix) carries forward unchanged into the new row shape. Dismiss (×) icon — already present in the user's live Figma build but never documented — written into the component spec for the first time.

---

## FRAME-01 Round 7: Repeatable type hierarchy system (Needs Attention as proving ground)

*User's own Figma work (not a First Draft prompt this time) had already fixed the Utilization Gap and Recent Activity issues from Round 6 organically, and added genuinely good unspecified patterns (Fleet Pulse mini-map, notification bell, sidebar section grouping, dismiss icons). User then asked to establish a repeatable spacing/typography/hierarchy system, using Needs Attention (still weak) as the proving ground, rather than treating this as a one-off fix.*

- [incident.io Incidents list](https://mobbin.com/screens/aaf20282-34ea-403b-9ef8-36eb3907feaa) — priority tag, status tag, title, metadata all in restrained relative sizes
- [Linear issue list](https://mobbin.com/screens/0ac97560-1aef-4907-a356-8c18c749437b) — same principle: one dominant text element (title), everything else recedes

**Finding:** Needs Attention has the right structural pieces (tint, accent border, icon, category tag) but still reads flat because every text element in a row is close to the same size/weight — color alone was carrying all the differentiation, with no real type hierarchy behind it. Both references use exactly two text weights per row: one dominant (the subject/title) and everything else clearly smaller/lighter, never competing.

**Decision — new repeatable rule, not a one-off fix:** added `03_MASTER_DESIGN_SYSTEM.md` §B2 "List Row Hierarchy Pattern," a system-wide rule (applies to Needs Attention, Recent Activity, Vehicle Status Board, Kanban cards): exactly one dominant Body-Primary-sized text element per row, everything else (tags, timestamps, metadata) drops to Meta/Badge or Micro-Eyebrow size, never more than 2 distinct sizes visible in one row, and color reinforces this hierarchy rather than substituting for it. This is meant to be reused for every future frame's list/row components, not re-derived per frame.

---

## FRAME-01 Round 6: Per-element benchmark (not whole-page) after two failed correction attempts

*Two consecutive correction prompts (canvas contrast, icon restraint, composition bar proportions) were sent to First Draft and none of the three landed in the rendered output — user correctly stopped patching the whole page and asked to benchmark each individual piece of information separately before re-arranging anything. This is a methodology correction: whole-page correction prompts are unreliable for fixing specific small defects; per-element research first, then a single clean regeneration, is more reliable than iterative patching.*

- KPI counters: [Substack post stats](https://mobbin.com/screens/c0a7799c-9de5-4cbe-82a9-1a6c8eaa33c5), [Later social overview](https://mobbin.com/screens/fd51fa4e-8aef-48c0-ab92-21a0436f41d7), [Threads weekly recap](https://mobbin.com/screens/8d2857fc-e9b0-4baf-a6d8-7354806f8b47)
- Priority/action list: [Remote "Things to do"](https://mobbin.com/screens/1a5a8ac8-49f2-467c-ad4f-5e36c2e86936), [15Five "My Actions"](https://mobbin.com/screens/7fd1f60c-2643-498a-b019-2c1305dbe96e)
- Proportional breakdown: [Zoho CRM stacked bars](https://mobbin.com/screens/678fc8d5-9394-45a8-a8c3-cabafb7f7aed), [Xero Explorer stacked column](https://mobbin.com/screens/b207a4f3-7f09-4645-bc33-beaf135c186b), [YNAB spending stream](https://mobbin.com/screens/53c0ef3d-cf2a-4821-b048-cab663e1d119)

**Finding 1 — KPI sparklines have no real precedent at this density and are removed.** Substack, Later, and Threads all present KPI-style counters as plain "eyebrow label / large number / small delta or nothing" with zero embedded charts. The v1.4 sparkline addition (justified at the time by Shopify's KPI cards) does not hold up against this wider sample — most real references skip it. Combined with the earlier finding that the sparklines don't drive any specific decision (see v1.6 correction note), sparklines are removed from Component 3 (KPI Tile) entirely, reverting to a plain text delta.

**Finding 2 — the Needs Attention list needs a real card treatment, borrowed from Remote/15Five, not just plain rows.** Remote's "Things to do" and 15Five's "My Actions" both use a left accent border plus a subtle background tint to visually mark priority items — this is the exact mechanism our Needs Attention component is missing. As built, it renders as plain black text with no card presence, indistinguishable in visual weight from Recent Activity at the bottom of the page, despite being the documented hero. Component 3C is revised to require this treatment explicitly (see `03_MASTER_DESIGN_SYSTEM.md`).

**Finding 3 — the Fleet Composition Bar is removed, not fixed.** Searched specifically for "proportional segmented bar with in-segment labels" and found no strong real-world precedent for that exact pattern — real dashboards doing category breakdowns use grouped/stacked column charts (Zoho, Xero) or stream/area charts (YNAB) instead of a single full-width labeled bar. Combined with (a) two consecutive failed attempts to get its proportions rendered correctly, and (b) it being informationally redundant with the KPI row (Fleet Size, Availability, Grounded are already on screen as numbers), the component is removed from FRAME-01 entirely rather than attempted a third time. If a proportional breakdown is wanted later, a small donut/ring (Zillow/Indeed-style) is the better-precedented alternative — not attempted in this pass since removal is simpler and the numbers already exist elsewhere on the page.

---

## FRAME-01 Round 5: Information architecture restructure (ui-ux-pro-max + user references)

*User provided screenshots of Shopify Analytics, GA4 (x2), Grok usage dashboard, and Perplexity Health as reference dashboards, correctly judging that our IA "does not do a good job" of arranging actionable data compared to them, and asked to run the `ui-ux-pro-max` skill to fix it. Ran the skill's design-system search (confirmed "Data-Dense Dashboard" as the right style category, though its color/font suggestions don't apply since our tokens are locked) plus targeted chart-domain and ux-domain searches.*

- Shopify Analytics dashboard (user-provided screenshot, not a Mobbin link)
- Google Analytics 4 Realtime Overview and Home (user-provided screenshots)
- Grok usage dashboard (user-provided screenshot)

**Borrow:**
- **Hero chart + companion breakdown, not equal-weight panels.** Shopify's "Total sales over time" (large line chart) sits beside "Total sales breakdown" (same subject, tabular view) — one hero, one detail, same topic. GA4's Home does the same with its Active Users trend chart plus a smaller Realtime panel beside it. Our dashboard had no hero at all — composition bar, status table, and compliance panel were all equal size, so nothing told Grace where to look first.
- **Embedded sparklines in KPI cards.** Every Shopify KPI tile (Gross sales, Returning customer rate, Orders fulfilled, Orders) carries a small inline trend line, not just a text caption. The `ui-ux-pro-max` chart-domain search independently confirmed this: "Trend Over Time" data (which is what a KPI's month-over-month delta actually is) belongs in a Line Chart even in compact contexts — a sparkline is that chart's compact form.
- **`ui-ux-pro-max` UX-domain search flagged a real, checkable violation** in the existing Fleet Composition Bar: color-only encoding (segments identified only by a separate legend, not labeled in place), which the tool's own guideline lists as **High severity** ("Don't convey information by color alone... Red/green only for error/success").

**Reject:**
- The skill's `--design-system` command's own color/typography/pattern suggestions (gold/purple palette, dark background, Fira Code, "Enterprise Gateway" marketing-site pattern) — these are generic defaults for an unstyled dashboard project and do not apply here; CVFMS already has a locked, source-verified token system (Civic Green, Inter, light theme) that takes precedence. Only the structural/chart/UX guidance was adopted, not the visual-identity suggestions.

**Decision:** Fleet Availability Trend (30-day line/area chart) becomes the new hero visual, replacing the Fleet Composition Bar in that role — the bar survives as a smaller, now-labeled supporting element rather than being removed, since it still answers a real question (current-state proportion) the trend chart doesn't. KPI tiles gain embedded sparklines. Vehicle Status Board becomes the hero chart's companion (same subject: fleet status), decoupling it from the unrelated Compliance Countdown panel it was arbitrarily paired with before. Full detail in `04_FIGMA_SCREEN_BLUEPRINT.md` v1.4.

---

## FRAME-01 Round 4: Full Airwallex visual-approach teardown (user-requested)

*User pushed back that the built dashboard "does not resemble the Mobbin references" and specifically asked for a breakdown of Airwallex's UI approach. Pulled a broader set of Airwallex screens beyond the single approval modal found in Round-2-era FRAME-02 research: dashboard, settings, spend-requests list, approval flow (list → drawer → confirmation toast), workflow/rule builder, card creation.*

- [Airwallex Dashboard](https://mobbin.com/screens/cb9c2e5d-d90d-46ee-9ec7-761d63805a4d)
- [Airwallex Spend Requests List](https://mobbin.com/screens/9885871f-0e1c-4e39-b5d8-1d1094e79b5c)
- [Airwallex Approval Drawer](https://mobbin.com/screens/defdb85a-2fa6-4d65-93f1-bdd3e991dbe5)
- [Airwallex Confirmation Toast](https://mobbin.com/screens/89c96631-be20-4176-be78-d24175e013ed)
- [Airwallex Workflow/Rule Builder](https://mobbin.com/screens/c50ee9ac-db63-4688-b0c4-fc2b1c759bc4)

**Borrow:**
- **Dark left rail.** Airwallex's near-black sidebar creates real separation from the white content area without extra borders — reads as more considered than our flat light-on-light rail. Adopted with scoped new color tokens (`--color-nav-dark`, etc.) — see `03_MASTER_DESIGN_SYSTEM.md` v1.2.0, Component 1.
- **Multi-stat cards.** Dashboard groups 2-3 related numbers per card (e.g. "Pending approval / To pay / Overdue") instead of one number per tile — denser, and shows the numbers' relationship. Adopted as new Component 3B, used where numbers are genuinely related stages of one thing (compliance countdown buckets), while single-stat KPI Tiles remain for standalone headline metrics (Fleet Size, Availability %).
- **Slide-in approval drawer over a dimmed, still-visible list**, not a static side panel and not a full-page navigation. Adopted — Component 4 (Dispatch Gate Checklist) renamed and restructured from "Card" to "Drawer."
- **2-column label/value metadata grid** inside the drawer (Start/end date, Requested for, Category) before the actual checklist/approval content — adopted into Component 4's new metadata-grid section.
- **Comments + Attachments built into the approval drawer** — real product thinking for the "wait, can you clarify" moment. Adopted as an available (not mandatory) pattern, most relevant to Grace's Maintenance Approval modal.
- **Post-action confirmation toast** ("Spend request approved — The request will now be forwarded to the finance admin for card creation") stating what happened AND what happens next. This exposed a real gap: no feedback/toast pattern existed anywhere in our design system despite our own `ux-design-instructions.md` requiring one (Doherty Threshold: "never leave users wondering whether their action registered"). Adopted as new Component 4B, now required after every state-changing action system-wide.
- **Filter chip row above tables** (Category / Requested by / Status as pill-shaped dropdown buttons). Our design system's prose already claimed tables were "filterable by department/station/status" but never specified an actual filter component — this was a real, previously undetected spec gap, not a new idea. Added to Component 6.

**Reject:**
- Nothing rejected outright from this teardown — Airwallex's patterns are close enough to our actual needs (approval/audit-heavy admin software) that everything reviewed was adoptable in some form, unlike the Round-1/Round-3 teardowns which had clearer domain mismatches to reject (dark cockpit theme, Uber-style map markers).

**Why this wasn't caught earlier:** Rounds 1-3 benchmarked *layout/structure* (KPI row shape, table columns, kanban card content) and correctly validated those. This round exposed that visual *craft* — depth, real feedback loops, interaction affordances like drawers and filter chips — was never benchmarked at all, because the earlier prompts described structure in enough detail to get structure right, but never specified things like "what happens after you click Approve" or "how does the sidebar create visual separation," so those details were filled in with the flattest possible default (flat colors, no toast, a static panel) rather than a deliberately considered choice.

---

## FRAME-01 Round 2 (post-build review): benchmarked against Deel, Employment Hero, GoDaddy

*Triggered by reviewing the actual built dashboard against fresh Mobbin references, after correcting Grace's persona from monitor-only to having real write actions (see `01_USER_PERSONAS.md` correction note).*

- [Deel Assets Dashboard](https://mobbin.com/screens/966dd7a5-28c6-4144-8a9d-a32e7e1f24fd)
- [Employment Hero Asset Register](https://mobbin.com/screens/1f9118fd-a85f-4aea-951b-dc0a84b1295b)
- [GoDaddy Renewals Notification Panel](https://mobbin.com/screens/ff55e54f-687d-46eb-8503-8d4c6a3303c2)

**Borrow:**
- Deel's asset dashboard leads with a **horizontal stacked distribution bar** (by asset state) sitting above its data table — proportional composition at a glance, which our KPI row (four disconnected numbers) doesn't provide. Adopted as the new "Fleet Composition Bar" in `04_FIGMA_SCREEN_BLUEPRINT.md` §2.
- Employment Hero's Asset Register — same domain shape as ours (asset code, category, status pill, assigned-to) — includes a **row-level "Actions" affordance** we were missing entirely. Our table had no way to act on a row, which was inconsistent with Grace's corrected persona (she has real edit/reallocate/override actions). Adopted as a new Actions column with a "•••" menu per row.
- GoDaddy's renewal panel puts a **"Renew All" bulk action in the panel header**, not just per-row. Our Compliance Countdown forced one-at-a-time handling. Adopted as "Review All →" in the Compliance Countdown header.

**Reject:**
- Deel's colored donut/ring chart elsewhere on the same page — a stacked bar communicates proportion better than a ring for exactly 4 categories; don't add a second chart type for the same data.

**Other finding (not from a specific reference, but surfaced by comparing our screenshot at full frame height):** the built dashboard left roughly the bottom third of the 1024px frame empty, which reads as unfinished rather than minimalist — none of the three benchmarks above leave that much dead space on a primary dashboard. Fixed by adding a Recent Activity Feed panel.

---

## FRAME-01 Round 3: Row thumbnails — Uber/Grab/Lyft instinct, tested against Mobbin

*User asked whether the Vehicle Status Board should use vehicle illustrations like Uber/Grab/Lyft. Initial answer (illustrations belong on a map/single-vehicle view, not a dense multi-row table) was directionally right but too narrow — checked Mobbin for car-dealership/marketplace dashboards and general catalog tables before finalizing.*

- [Shopify Products table](https://mobbin.com/screens/e8786dbf-4443-40f1-91f1-c45d3560aa80)
- [Square Items table](https://mobbin.com/screens/c914fb7a-3274-4fd2-9fa7-508a7af9274a)
- [Klaviyo Products table](https://mobbin.com/screens/e91c22a1-7988-4edf-a5c2-97e35a45d0bd)
- [Squarespace Products table](https://mobbin.com/screens/dd9e833f-3677-4b5d-be37-241d0ed07bf7)
- Rejected reference: [Turo individual car listing](https://mobbin.com/screens/4fcd69f8-4bc4-4c4e-86ed-a4b1d237edb0) — full photo hero card, correct for a single-item consumer listing, wrong shape for a 200+ row operational table.

**Finding:** a small square thumbnail (~32-40px, rounded corners) to the left of the item name in a dense data table is a standard, proven enterprise catalog pattern — not a consumer-only affectation. Shopify, Square, Klaviyo, and Squarespace all use it in their products/items tables, which are structurally the same shape as our Vehicle Status Board (name + type + status + numeric columns).

**Decision:** adopt a small 32px vehicle-type thumbnail per row in the Vehicle Status Board — a generic type icon (sedan/pickup/ambulance/grader silhouette, flat single-color style matching the icon library, not a photo) placed to the left of the registration number, in the same slot and size Shopify/Square use for product photos. This is deliberately narrower than Uber/Grab/Lyft's live per-vehicle map markers (rejected — no map context here) and narrower than Turo's full per-listing photo (rejected — no real per-vehicle photos exist, and a hero photo is too heavy for a 48px table row). Added to `04_FIGMA_SCREEN_BLUEPRINT.md` §2.

---

## FRAME-01 Round 1: Fleet Command Dashboard → benchmarked against Vercel, Sentry, Better Stack

- [Vercel Observability Overview](https://mobbin.com/screens/38a44719-a4b0-482b-bb40-283eec56ebd4)
- [Sentry Base Dashboard](https://mobbin.com/screens/54bac74a-aa92-47cf-a64b-b5f551241eb6)
- [Better Stack Telemetry Dashboards](https://mobbin.com/screens/c2435ccb-ffdf-4103-ad68-3f014403d81e)

**Borrow:**
- Vercel and Sentry both lead with a **compact horizontal row of plain-number KPI tiles** (no heavy chart, just label + big number + optional small trend) before any table or chart — exactly the pattern for Grace's "Fleet Size / Availability % / Grounded / Alerts Due" row. Note how restrained the tiles are: no icons competing for attention, one number is always dominant.
- Sentry's session-health table (label left, right-aligned count) is the correct model for the Vehicle Status Board rows — not decorative, just clean left-label/right-value density.
- Left rail in both stays static and icon-first with labels, collapsing to icon-only — matches our Component 1 (Application Shell).

**Reject:**
- Sentry and Better Stack's **dark theme** — CVFMS is light enterprise per the design system; do not carry over dark surfaces even though the layout logic is right.
- Sentry's donut/pie charts (seen in the Posh example too) — avoid decorative charts for compliance-critical counts; a number and a status pill communicate faster than a chart slice for "6 grounded vehicles."

---

## FRAME-02: Dispatch & Requisition Queue → benchmarked against Airwallex, Reddit Mod Queue, Qatalog

- [Airwallex Spend Request Approval](https://mobbin.com/screens/defdb85a-2fa6-4d65-93f1-bdd3e991dbe5)
- [Reddit Moderation Queue](https://mobbin.com/screens/9e81dbcf-db79-45ef-8347-08e81e1b5b77)
- [Qatalog Request Thread](https://mobbin.com/screens/17b2ec6d-a9e3-4eb7-9bd7-1837150964f2)

**Borrow:**
- Airwallex is the closest real-world analog to our exact need: a **list-left, detail-right** layout where the detail panel shows structured request metadata (amount, dates, category) and ends in a **sticky footer with `[Reject]` and a primary filled action** (`Create card` there = `Authorize Dispatch` for us). This is precisely Component 4's structure — validates the blueprint as-is.
- Reddit's mod queue shows the same list-left/detail-right pattern but with a visible **reason/context trail** in the detail pane before any action — reinforces that our Dispatch Gate Checklist should read top-to-bottom as a trail of facts before the action buttons, not action-first.
- Note Airwallex keeps the destructive/secondary action (`Reject`) as an outline button to the *left* of the primary filled action, both bottom-right — adopt this exact placement for `[Request Override]` / `[Authorize Dispatch]`.

**Reject:**
- Reddit's queue list uses vote counts/emoji reactions — irrelevant, drop entirely; our queue rows need status pill + department + requester, not social metadata.

---

## FRAME-03: Workshop Job Card Board → benchmarked against Plane, Height, Linear-style boards

- [Plane Kanban Board](https://mobbin.com/screens/0a016723-4f5b-4f5b-a418-4c14b1aebef7)
- [Height Kanban with Column Config](https://mobbin.com/screens/913e271b-5104-454a-96aa-56b7c255c167)

**Borrow:**
- Plane's column header format — **column name + count badge + a thin colored dot per status** — is the exact pattern for our 5 columns (Diagnosis / In Repair / Awaiting Parts / QA / Ready for Release). Keep columns fixed-width with clean whitespace, not the noisy colored-column-background style seen in some Trello examples.
- Card content stays minimal: title, small metadata row (assignee avatar, date). Our cards should resist the urge to cram parts-status and QA-status onto the card face — that detail belongs in the drawer (per blueprint), keeping the board itself scannable.
- Plane's "+ New work item" affordance pinned at the bottom of each column (not just top) — adopt for high-volume columns like "In Repair."

**Reject:**
- Trello's colored-background board style (dark navy with photo backdrop) — too decorative for an audit-sensitive government tool; stay on the light `--color-canvas` background from our design system.

---

## Summary: Blueprint Changes Triggered by This Benchmark

1. **FRAME-01 KPI row:** confirmed as plain number tiles (no charts/icons) per Vercel/Sentry — no change needed to `04_FIGMA_SCREEN_BLUEPRINT.md`, benchmark validates the existing spec.
2. **FRAME-02 action button placement:** adopt Airwallex's exact footer order — outline `[Request Override]` immediately left of primary filled `[Authorize Dispatch]`, both bottom-right of the panel (already specified; benchmark confirms it's the right convention, not just a made-up guess).
3. **FRAME-03 column headers:** add a count badge next to each column name (e.g. "In Repair · 4") — this was implicit in the original blueprint's kanban description but should be made explicit as a required element.
4. **FRAME-03 card face:** explicitly keep cards minimal (title + defect summary + assignee + one status pill) and push parts/QA detail to the drawer only — avoids the temptation to overload cards during generation.

These four points should be treated as binding refinements to `04_FIGMA_SCREEN_BLUEPRINT.md` when generation begins.
