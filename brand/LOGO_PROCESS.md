# Logo process (from the TaifaPay family handover, 1 Oct 2026, @John; world-class pass added 2 Oct 2026)

This is the method for every new brand or product. The source is the TaifaPay handover; Swift Fleet
is a **separate brand** (Swiftcent), so it runs **all eight steps**.

1. **Brief:** product, users, the one idea the logo carries, the rules already in force.
2. **Taste mood board:** ~24 real logos from Mobbin; the owner marks each number as loved or
   disliked. Read the pattern, not single picks. **Do this before drawing anything.**
3. **Directions:** 2–3, each with a one-line story, judged against the mood board before showing.
4. **Compare with what you have:** does any new direction beat the current system? If not, refine.
5. **Refine the winner:** exact geometry (one stroke, one gap, built on the font's metrics);
   outlined wordmark, not live text.
6. **Build the family:** one shared element; candidates side by side as mark, app icon, 24px,
   16px and lockup; recommend one.
7. **Show it in use:** on real things (vehicle sticker, uniform, app icons, site). Decide on these,
   never on bare marks.
8. **Decide and hand off:** record each decision with the date; update brand files only after
   approval; write the handover.
9. **World-class pass:** run this after the direction is chosen and before the final handover.
   TaifaPay stopped at step 8; Swiftfleet added this pass. See below.

**Rules of thumb:**
- One geometry for everything.
- The 16px test decides.
- Holes are real holes.
- One meaning per element.
- Family rule: change one thing.
- Check the lookalike (what else does this shape look like?).
- Colour carries no warnings.
- App icons centre by weight.

**Working habits:**
- Decisions go on tap cards with one recommended option.
- Every result goes onto the board; nothing lives only in chat.

---

## Step 9: the world-class pass (added 2 Oct 2026, from Swiftfleet)

Steps 1–8 give you the right idea. Step 9 makes it look **drawn, not typed**. Swiftfleet reference:
`brand/swift-fleet/world-class/`. Read its `README.md`, open `index.html`, and rebuild everything with
`python3 kit.py && python3 board.py`.

**Rules for the pass:**
- **Never replace a kit.** Build the refined version in its own folder next to the old ones, so the owner
  can compare and roll back.
- **Look at every change.** Render it and inspect it at zoom. Most first attempts left slivers, double
  facets or collisions that only showed up in the render.

### A. Letter craft (on the outlines, with fontTools and skia-pathops)
1. **Measure first.** Extract the real outlines and list every straight segment, crossbar height and
   terminal. Don't guess coordinates.
2. **One terminal angle.** Recut every free stroke end to a single angle. For a slanted wordmark, cut
   vertically in the upright drawing; after the slant, every end runs parallel to the stems.
   - Put the cut line through the **inner end** of the old diagonal; otherwise a two-facet stub remains.
3. **Align shared metrics.** Letters that should share a height must share it exactly. In Lexend, the f
   and t crossbars differed by 8–17 units.
4. **Draw the special element upright.** Build the dash (or any device) in the upright drawing, so its
   ends match the stems after the slant.
   - Size it from a real metric (here, the i-dot height).
   - Align its edges to construction lines (here, the i stem and the s's top cut).
5. **Optical spacing.** Space pairs from measured left/right profiles across the full height
   (descender to ascender, including crossbars), plus a minimum gap. Measuring only the x-height band
   misses crossbars and lets f, t and f collide.
6. **One version.** Study variants (such as the f–t–f join), then retire them. A second geometry breaks
   "one geometry for everything".

### B. Versions for real conditions
7. **Reversed cut.** Thin light-on-dark artwork about 5–8% (merge overlapping contours first, then inset
   with a stroke-and-subtract) so it doesn't glow heavier than the light version.
8. **Small-size cuts.**
   - Small wordmark: heavier weight, looser spacing, thicker accent.
   - Small symbol: thicker, shorter accent and a wider gap.
   - Set the switch points (here: wordmark 24px tall, symbol 48px).
9. **Contrast check on every brand colour against white and dark.** Below 3:1, a colour fails for
   graphics; below 4.5:1, it fails at text size. Add a deeper shade for small use (Teal #1FA3A9 at 3.06:1
   → Teal deep #147B80 at 5.0:1).

### C. Proof
10. **Automated audit:** `svg_audit.py`. Explain every warning; deliberate angles are fine.
11. **Test sheet:** `preview_sheet.py`. Size ladder, 16/32/48px pixel test, squint blur, mirror,
    rotate 180°, one colour, greyscale, backgrounds.
12. **Peer and shelf test:** put the mark next to 3–4 exemplary library marks at equal size
    (`search_library.py --exemplary`). It must look equally finished.
    - Name the nearest cliché honestly (here, Go's speed lines) and the rule that keeps you clear of it.
13. **Construction sheet:** draw the guide lines over the mark (shared heights and cut lines), then
    zoom in to check that they really land on the terminals.
14. **In-use sheet:** every real surface: host app ("Powered by"), own sign-in, home-screen icon,
    splash, vehicle decal, badge, email signature, browser tab.
    - This catches size rules the bare mark hides. Here, "by Swiftcent" was unreadable below 220px wide.

### D. Hand-off
15. **Lockups rebuilt** from the refined letters. Align the endorsement to a real edge (here, the end
    of the t).
16. **Motion:** one movement, under one second, with reduced-motion support.
17. **Web kit:** `export_variants.py --web-icons --favicon-source <small symbol>`.
18. **Usage guide:**
    - clear space and minimum sizes
    - colours with contrast notes
    - when to switch to the small cuts
    - the host-brand rule (the county leads)
    - "don't" examples
19. **Figma prompts:** under 2000 characters each, one per surface. Turn logos into components and
    colours into styles, and never let the agent redraw vectors (it can't read local files, so import
    the SVGs by hand).
20. **Honest limits, written down:**
    - what needs a specialist (a true drawn italic from a type designer)
    - trademark search
    - the parent brand's official files
    - a real recall test with users

**Added rules of thumb:**
- Measure, don't guess.
- One angle for every cut.
- Draw devices upright, then slant.
- Thin the reversed version.
- Small sizes get their own drawing and their own colour.
- An element that needs a size rule gets one in the guide.
- Retire study variants.
