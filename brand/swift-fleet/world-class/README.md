# Swiftfleet logo: Lexend world-class pass (2 Oct 2026)

A refined build of the Lexend kit. **`../final/` and `../final-lexend/` are untouched.**
Open `index.html` (or `board.png`) for the before/after, construction, small sizes and usage guide.

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
