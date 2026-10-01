# Swiftfleet — logo brief and decisions

Drafted 2 Oct 2026 from the project docs. Items marked ⚠ are assumptions; please confirm or correct.

1. **Name and what it does:** Swift Fleet: one system for a county government to request, approve,
   dispatch, track, maintain and account for every county vehicle.
2. **Who uses it:**
   - County fleet managers, transport officers, approvers, auditors (web).
   - Drivers (mobile app).
   - **Buyers:** county governments.
3. **Family:** a separate brand, a product of **Swiftcent** (endorsed: "Swift Fleet by Swiftcent").
   Not part of the TaifaPay family.
   - ⚠ How close to Swiftcent should it look: shared colours only, or a shared shape?
4. **One idea or moment to carry:** ⚠ *proposed*: **"every vehicle accounted for"** (identity,
   custody, return). Alternatives tried: "cleared to go" (dispatch gate), "the trip closed"
   (odometer).
5. **Avoid:**
   - The Swiftcent orbit as-is; map pins; road S; arrow S (Subway owns it); steering wheels.
   - Crescent shapes (moon reading); price-tag shapes (retail); dot rings (loading spinner).
   - Gradients as a crutch.
   - The county emblem and flags. The county's identity leads inside the app.
6. **Where it appears first:**
   - ⚠ Driver app icon.
   - "Powered by Swift Fleet" on county web login and sidebar.
   - Vehicle stickers on county vehicles.
   - Proposals and decks.

**Rules already in force:**
- One colour must work.
- 16px favicon.
- It sits next to a Civic Green (#006837) app interface without clashing.
- Swiftcent palette available: navy #1E3F78, teal #1FA3A9/#32BFC4, blues and purples.

## Status against the 8-step process
- [x] Concepts explored *before* a mood board: rounds 1–3 + Crazy 8s (see `round2/`, `round3/`,
  `crazy8/`). Per the process, treat them as **unvalidated**; re-judge them against the mood board
  at step 3.
- [x] Brief confirmed (name decided 2 Oct 2026)
- [x] Mood board scored (2 Oct 2026)
- [x] Directions judged (`directions/board.png`)
- [x] Compared: "In motion" beats the 8 client options against the owner's taste
- [x] Refined on exact geometry (stand-in letters)
- [x] 24px / 16px / one-colour tests passed
- [x] Shown in use (`refine/in-use.png`)
- [x] Decision recorded: 2 Oct 2026


## Decisions (recorded with date)

> **2 Oct 2026, later:** the owner and the designer both prefer the **Lexend slant** visually. At the owner's request, nothing was replaced: a complete **Lexend kit** was built alongside the family kit, in `final-lexend/` (schemes A all-navy and B family colours). **Which kit is primary is still to be decided.**

> **2 Oct 2026, world-class pass:** the Lexend kit was refined in `world-class/`. Changes: one cut angle for every stroke end and the dash, aligned f/t crossbars, measured spacing, a lighter dark cut, small-size cuts, and Teal deep `#147B80` for small sizes (5.0:1 on white). An optional f–t–f join study was added. `final-lexend/` is untouched. See `world-class/README.md` and `world-class/index.html`. Still open: which kit is primary, a true drawn italic by a type designer, and a trademark search.

> **2 Oct 2026, decisions (made user-first; validate with the owner):**
> - **Primary kit:** Lexend world-class (`world-class/`). The family kit (`final/`) is kept as an archive.
> - **Teal:** #1FA3A9 at 24px and up; Teal deep #147B80 below that and for text-sized use; #32BFC4 on dark.
> - **f–t–f join:** retired.
> - **Scheme:** B (navy + teal) is the default; A is for badges and one-colour-leaning uses.
> - **Lockups:** rebuilt from the refined letters. The endorsed lockup needs a minimum width of 220px.
> - **Figma:** prompts are in `world-class/FIGMA_PROMPTS.md`.


| Date | Decision |
|---|---|
| 2 Oct 2026 | **Name written as one word: "Swiftfleet"** (capital S only, like Swiftcent). Reasons: family consistency with Swiftcent; avoids the Suzuki Swift and banking-SWIFT readings of "Swift Fleet"; a coined word is easier to protect. The "ftfl" cluster is handled in the wordmark. |
| 2 Oct 2026 | Mood board scored. Loves: 1 Lyft, 6 Posh, 7 Zip, 8 Glovo, 10 Square, 15 Mesh, 22 Subway, 23 DoorDash. Dislikes: 13 Box Box Club, 24 Too Good To Go. Pattern: bold wordmark-led, one twist inside the letters, motion, single-gesture symbols, flat 1–2 colours, no gradients. |
| 2 Oct 2026 | **Direction approved: "In motion".** |
| 2 Oct 2026 | Next: **custom lettering** to replace the Nunito Black stand-in and firm up the tone for government buyers. |
| 2 Oct 2026 | **Lettering: customised Lexend ExtraBold** (the app's own heading font, OFL licence, so outlined logo use is allowed). It replaces Nunito: firmer and more credible for government, still friendly. Customisations: 12° slant; tracking −24 with pair spacing opened (f→t +46, t→f +58, f→l +34) so the f-t-f run never touches; the i-dot dash (thickness = Lexend i-dot height, 4.2× long in the wordmark). Icon rebuilt on Lexend's s. Masters in `final/`. |

| 2 Oct 2026 | **Family decision: option C, shared "Swift".** The wordmark is built entirely from Swiftcent's own letter shapes: "Swift" as is; "fleet" from the parent's f, e and t, with the l made from the parent's i stem extended to full height. "Swift" is navy/white and "fleet" teal, like the parent's "cent". Upright like the parent. **The one change from the parent is the i-dot dash trailing back** (the "In motion" idea, kept). App icon: the parent's capital S with the trailing dash. **This supersedes the Lexend lettering and the 12° slant** (kept in `final/archive-lexend/`). Lexend stays the app's interface typeface. |

**The approved direction, "In motion" (now expressed in the family lettering, see the decision above):**
- **Wordmark:** heavy, lowercase, slanted 12°.
- **The twist:** the i's dot becomes a teal dash trailing back over the "w".
- **App icon and symbol:** the slanted "s" with the same dash trailing left.
- **Colour:** navy #1E3F78 and teal #1FA3A9 (on dark: #32BFC4).
- **One-colour rule:** inside county products Swiftfleet appears in one colour only, as "Powered by"; the county leads.

**Geometry:**
- Dash thickness = the i-dot height.
- Wordmark dash = 4.6× that thickness.
- Icon dash = 2.8× it, one gap above the s.
- Tracking −18 units.

**Files:**
- `final/`: current family masters (wordmark light, dark and mono; symbol; app icon; Swiftcent light and dark), plus `family-board.png` and `final-check.png`.
- `final/archive-lexend/`: the superseded Lexend version.
- `refine/`: the earlier Nunito exploration, plus `refine/in-use.png` (Nunito version).

**Open items:**
- [x] Lettering upgraded to customised Lexend ExtraBold (2 Oct 2026). Fully bespoke letters remain an option for a type designer later.
- [ ] Endorsement lockup ("Swiftfleet by Swiftcent") as a master file. A light-background Swiftcent version was made by recolouring "Swift" white to navy; **confirm against an official Swiftcent light logo**.
- [ ] Confirm the teal: the parent uses #32BFC4; the light-background version uses #1FA3A9 for contrast (per the earlier export notes).
- [ ] Trademark search ("Swiftfleet"; also check against Suzuki Swift and SWIFT marks).
- [x] Final exports (2 Oct 2026): SVG variants, favicon and app/web icon set, endorsed lockups, motion page (`final/`, see `final/README.md`).
- [ ] One-page usage guide.
- [ ] Dash variants + recall test page; then run the test with 5 county staff and 5 drivers.
- [ ] Five-second memory test with real users (county staff, drivers).
