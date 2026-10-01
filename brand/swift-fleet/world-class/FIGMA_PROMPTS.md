# Swiftfleet logo: Figma agent prompts (2 Oct 2026)

These prompts put the world-class Lexend logo into the Figma file `bnxWZCzNtbjM0ulb886hXo`.
Run them **one at a time, in order**, and check each render before starting the next.
Every prompt is under 2000 characters.

**Before prompt 1 (manual, about 2 minutes):** the Figma agent can't read local files.
1. In Figma, create a page called **Brand**.
2. Drag these files from `brand/swift-fleet/world-class/` onto the page:
   - `out/B-wordmark-light.svg`, `out/B-wordmark-dark.svg`, `out/A-wordmark-light.svg`, `out/A-wordmark-dark.svg`
   - `out/B-wordmark-small.svg`, `out/wordmark-mono-navy.svg`, `out/wordmark-mono-white.svg`
   - `out/symbol.svg`, `out/symbol-small.svg`, `out/symbol-mono.svg`, `out/app-icon.svg`, `out/app-icon-small.svg`
   - `out/B-lockup-endorsed-light.svg`, `out/A-lockup-endorsed-dark.svg`
3. Don't resize or ungroup anything.

---

## Prompt 1: Brand page, components and colour styles

```
On the page "Brand" there are 14 imported SVG logo files for Swiftfleet. Turn them into a clean logo library. Do not redraw, ungroup, recolour or resize any vector.

1. Wrap each imported SVG in a component, named exactly:
Logo/Wordmark/B-Light, Logo/Wordmark/B-Dark, Logo/Wordmark/A-Light, Logo/Wordmark/A-Dark, Logo/Wordmark/Small, Logo/Wordmark/Mono-Navy, Logo/Wordmark/Mono-White, Logo/Symbol/Regular, Logo/Symbol/Small, Logo/Symbol/Mono, Logo/AppIcon/Regular, Logo/AppIcon/Small, Logo/Lockup/Endorsed-Light, Logo/Lockup/Endorsed-Dark.
The source file names map one to one (B-wordmark-light -> Logo/Wordmark/B-Light, etc.).

2. Set every component to "Scale" constraints and lock its aspect ratio.

3. Lay them out in rows on an 8px grid with 48px gaps: wordmarks, symbols and icons, lockups. Put dark versions on a #10213F rectangle behind them (outside the component). Under each, add a 12px Source Sans 3 caption with its name and minimum size:
Wordmark 24px tall, Small wordmark 16-24px tall, Symbol 48px+, Small symbol under 48px, Lockup 220px wide.

4. Create colour styles (do not change any existing styles):
Brand/Navy #1E3F78, Brand/Teal #1FA3A9, Brand/Teal Deep #147B80, Brand/Teal On Dark #32BFC4, Brand/Night #10213F.

5. Add a text block at the top: "Swiftfleet logo, Lexend world-class build, 2 Oct 2026. Never re-slant, stretch, recolour or put teal on teal. Use Teal Deep below 24px."
```

**Check:** 14 components with exact names, nothing redrawn, five colour styles.

---

## Prompt 2: desktop sidebar ("Powered by" attribution)

```
On page "Refined", update the main component "Navigation/Sidebar" (all its variants) and "Sidebar/Collapsed". Only change branding; keep nav items, widths, colours and spacing exactly as they are.

Rule: the county leads, and Swiftfleet appears once, quietly, as "Powered by".

1. Top of the sidebar: if any layer reads "CVFMS" as the app or product name, replace that text with the county name ("Nakuru County", Lexend 600, 16px) and a second line, "Fleet Management" (Source Sans 3, 12px, secondary text colour). Do not add a Swiftfleet logo at the top.

2. Bottom of the sidebar, directly above the user/role block: add a horizontal auto-layout row, 8px gap, 16px side padding, 12px top and bottom padding:
- "Powered by" (Source Sans 3, 11px, secondary text colour)
- an instance of Logo/Wordmark/Mono-White if the sidebar background is dark, or Logo/Wordmark/Mono-Navy if it is light, 12px tall (lock the ratio)
Make the row 60% opacity.

3. Sidebar/Collapsed: no wordmark. Use an instance of Logo/Symbol/Mono at 20px, 60% opacity, in the same position, white on a dark sidebar.

4. Don't change any other component. All instances on existing pages update automatically.
```

**Check:** the county name is on top, "Powered by swiftfleet" is small at the bottom, and the collapsed sidebar shows only the symbol.

---

## Prompt 3: mobile splash (for the mobile chat or the mobile pages)

```
Update the mobile "Splash" frame (Component 14). Keep the county-first hierarchy: county crest, county name, "Vehicle Fleet Management System". Keep the background and layout exactly as they are.

Only change the bottom attribution: replace the text "Powered by CVFMS" with a centred horizontal auto-layout row, 6px gap, 32px above the bottom safe area:
- "Powered by" (Source Sans 3, 12px, white, 70% opacity)
- an instance of Logo/Wordmark/Mono-White, 14px tall (lock the ratio), 70% opacity

No full-colour logo, no teal, no app icon on this screen.
```

**Check:** the attribution is one quiet line, and the county still leads.

---

## Prompt 4: app icon and store presence

```
On page "Brand", create a frame "App Icon Sizes", 1200x400, background #F4F6F8.

Place instances of Logo/AppIcon/Regular at 180, 120 and 87px, and Logo/AppIcon/Small at 60, 40 and 29px, in one row, bottom-aligned, 32px gaps, each with a 12px caption showing its size. Corner radius is already in the artwork; don't add another.

Next to them, a "Home screen" mock: a 240x480 rounded rectangle (radius 32) with a dark blue-grey gradient, a 4x5 grid of 48px placeholder squares (white, 25% opacity, radius 12), and one Logo/AppIcon/Regular at 48px in the second row with the label "Swiftfleet" (11px, white) under it.
```

**Check:** the dash stays readable at 29px (the small cut); the icon doesn't look smaller than its neighbours.

---

## Prompt 5: replace remaining "CVFMS" text

```
Search every page except "Brand" for visible text layers containing "CVFMS". Do not touch layer names, page names or frame names.
- Where it is a product attribution ("Powered by CVFMS", "CVFMS v1.0", footer credits), replace "CVFMS" with "Swiftfleet".
- Where it names the county's system to its own staff (titles, headings), replace the whole phrase with "Fleet Management".
List every change you made (frame name, old text, new text) in a text block on page "Brand" titled "CVFMS text replaced, 2 Oct 2026".
```

**Check:** read the change list; undo anything that turned a county heading into a Swiftfleet heading.

---

**After running them:** record the results in `docs/12_DESKTOP_REDESIGN.md` (desktop) or tell the mobile chat
(prompt 3). If a prompt fails twice, fix it directly with `use_figma` (project rule).
