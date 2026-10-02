# Swiftfleet logo: Lexend world-class pass (2 Oct 2026)

**Primary kit since 2 Oct 2026** (decided user-first; validate with the owner). The join variant is retired.

A refined build of the Lexend kit. **`../final/` and `../final-lexend/` are untouched.**
Open `index.html` (or `board.png`) for the before/after, construction, small sizes and usage guide.

**Review pack for the bosses (2 Oct 2026):**
- `Swiftfleet-logo-options.jpg`: the two finalists side by side. Option 1 "Forward lean" (Lexend, recommended) and Option 2 "Swiftcent letters" (family), each on white, on dark, as the app icon and with "by Swiftcent".
- `Swiftfleet-logo-review.jpg`: the recommended option in six views.
- Deck (12 slides: the ask, the story, the evidence, decisions, next steps with costs to fill in): https://claude.ai/artifact/J3iP7JjzyS3uSLeeGC5sCR
- Logo sheet (every background, icons, lockups, colours): https://claude.ai/artifact/AQK9RQMWTSmvX6BkK4rMpc, source `logo-sheet.html` / `sheet.py`.
- Full board (decisions, construction, usage guide): https://claude.ai/artifact/BY8V3vdTwJwXRJFqhBhMwu, source `index.html`.
- All links are private until they're shared from each page's Share menu. Fill in the deck's `[KES __]` costs (trademark search, type designer) before presenting.

## What changed

- **Signature cut:** the s, e and f stroke endings are recut vertically in the upright drawing. After the 12° slant, every
  stroke end, stem and both dash ends run on one angle.
- **Dash:** drawn upright, so its ends are parallel to the stems. It is the i-dot's height, and its right end continues
  the i stem.
- **Crossbars:** the t crossbar was rebuilt to the f's height (367–516 units).
- **Spacing:** pairs are spaced from measured letter profiles, with a minimum gap of 34 units.
- **Dark cut:** inset by 6 units (about 8% less ink) to offset the glow of light-on-dark.
- **Small sizes:**
  - The small wordmark uses weight 900, looser spacing, a thicker dash and Teal deep `#147B80` (5.0:1 on white).
  - The small icon cut has a thicker, shorter dash and a wider gap.
- **Icon:** the dash's right end continues the s's top cut line.
- **Motion:** the same movement as before, retimed to a 0.2 s fade followed by a 0.6 s arrival.

## Files

| Path | Use |
|---|---|
| `out/A-/B-wordmark-light/dark.svg` | Main wordmarks (A: all navy; B: navy + teal) |
| `out/A-/B-wordmark-small.svg` | Under 24 px tall |
| `out/A-/B-wordmark-join-light.svg` | Optional f–t–f join study (large display only) |
| `out/wordmark-mono-navy/white.svg` | One colour, "Powered by" |
| `out/symbol*.svg`, `out/app-icon*.svg` | Symbol and icons, regular and small cuts |
| `kit/` | favicon.ico/svg, PNG icons, maskable, manifest, head snippet, mono/black/white symbols |
| `out/A-/B-lockup-endorsed-light/dark.svg` | “Swiftfleet by Swiftcent”: right-aligned to the t; minimum 220 px wide |
| `in-use.html` / `in-use.png` | The logo on real surfaces |
| `FIGMA_PROMPTS.md` | 5 prompts for the Figma agent (components, sidebar, splash, icons, CVFMS text) |
| `motion/index.html` | Logo, splash, dispatch animation |
| `build.py`, `wordmark.py`, `kit.py`, `board.py` | Rebuild everything: `python3 kit.py && python3 board.py` (needs fontTools and skia-pathops; Lexend in `../refine/lettering/`) |

## Tests run

- svg_audit: scores 91–92/100. The angle warnings are the deliberate 12° slant and Lexend's own w diagonals.
- Size ladder: the wordmark holds to 24 px tall; below that, use the small cuts.
- Squint, mirror, rotate and one-colour checks: the shape stays clear in all of them.
- Peer and shelf test against Adyen, Go, Next.js and Wire: the mark looks just as resolved.

## Limits

- This is still a sheared Lexend, not a drawn italic. A type designer should rebalance the curves if it becomes primary.
- No trademark search has been done yet.
