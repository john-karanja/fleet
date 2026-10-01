# Visual Design Instructions

Follow these instructions whenever you build, style, or revise a user interface. They apply to layouts, components, pages, and design tokens.

Project tokens always override these defaults. If the project defines a color, type scale, spacing scale, radius, or component, use it and do not invent a parallel one.

## 0. Project Tokens

* **Accent color:** `#006837` (Nairobi Civic Green) / `#DC2626` (Emergency Life-Safety Red)
* **Neutral scale:** `#FFFFFF` (Card Surface), `#F8FAFC` / `#F2F2F7` (App Background), `#E2E8F0` / `#CBD5E1` (Borders), `#0F172A` (Primary Text), `#64748B` / `#475569` (Secondary Text)
* **Typeface:** Inter / SF Pro Text
* **Type scale:** 11px (Meta), 12px (Body Compact), 14px (Body/Headlines Compact), 16px (Body Standard / Headings), 20px (Section Titles), 26px+ (Hero Titles)
* **Spacing scale:** 4, 8, 12, 16, 24, 32, 48, 64
* **Corner radius:** 8px (Pills/Buttons), 16px (Standard Cards), 24px (Bottom Sheets & Modals)
* **Shadow:** `0 2px 8px rgba(0,0,0,0.03)`
* **Icon library:** Lucide / Standard SVG Icons
* **Component library or directory:** `components/` and `css/design-system.css`

## 1. Color

Color carries meaning. Use as little of it as possible so the meaning stays legible.

* Use one accent color. It marks the primary action and active states, nothing else.
* Everything else is a neutral scale: one background, one surface, one border, two text colors (primary and secondary).
* Semantic colors (success, warning, error) exist only for status and validation. Never use them decoratively.
* Text contrast is at least 4.5:1 against its background. Large text and icons are at least 3:1.
* Never convey state with color alone. Pair it with text, an icon, or a shape.
* Define every color once as a token. No hard-coded hex values in components.
* Support light and dark themes through tokens, not through duplicated styles.

## 2. Typography

Type is most of the interface. Get the scale right and most hierarchy problems disappear.

* Use one typeface family for the interface. A second family is allowed only for code, or for a deliberate editorial contrast defined in the project tokens.
* Use a single modular type scale with a ratio of at least 1.25. Default: 14, 16, 20, 25, 31, 39.
* Body text is 16px or larger. Small labels are never below 12px.
* The page's top heading is at least twice the body size.
* Use at most three font weights: regular, medium, bold.
* Body line height is 1.5 or more. Heading line height is 1.1 to 1.25.
* Reading text has a maximum measure of 65 to 75 characters.
* Left-align interface text. Center text only for short standalone lines such as an empty state or a hero heading.
* Use sentence case for labels, buttons, and headings unless the project specifies otherwise.
* Uppercase is for micro-labels only, at 12 to 13px with letter-spacing of 0.05em or more.

## 3. Spacing and Grid

Consistent spacing is the difference between one object and a pile of parts.

* Every margin, padding, gap, and size is a multiple of 8px. 4px is allowed inside compact components.
* Use one spacing scale: 4, 8, 16, 24, 32, 48, 64, 96. No other values.
* Related elements sit closer together than unrelated ones. The gap between groups is at least twice the gap within a group.
* Whitespace increases with hierarchy. Section gaps are larger than block gaps, which are larger than element gaps.
* Align everything to a shared left edge. Ragged left edges read as mistakes.
* Vertical rhythm follows the spacing scale. Do not eyeball it.

## 4. Layout and Width

Width is a readability decision, not a screen decision.

* Constrain content width. Default maximum for reading layouts is 720px. Default maximum for application layouts is 1280px.
* Use a 12-column grid for page layouts and CSS grid or flexbox for components. Do not mix ad hoc pixel positioning with either.
* Build one responsive layout with breakpoints. Do not build separate mobile and desktop versions.
* Default breakpoints: 640, 768, 1024, 1280.
* Content reflows at breakpoints. Nothing is hidden on mobile that the user needs to complete the task.
* Sticky elements are limited to one header and, at most, one action bar.

## 5. Hierarchy

The user should know what matters most within one second.

* Each view has one visually dominant element. Usually the heading or the primary action.
* Establish hierarchy with size and weight first, then space, then color. Decoration is last and usually unnecessary.
* Use at most three levels of visual hierarchy on a single view.
* Secondary information uses the secondary text color and a smaller size, not a lighter weight of the same size.
* De-emphasize before you emphasize. Quieting everything else is cheaper than making one thing louder.

## 6. Containers, Borders, Shadows, and Radii

Containers are for grouping, not decoration.

* Separate groups with space first. Add a border or background only when space alone leaves the grouping ambiguous.
* Do not wrap every section in a card. A card is for a repeated, self-contained unit such as a list item or a product.
* Never nest a card inside a card.
* Use one corner radius token for components and at most one larger token for containers and modals.
* Use one shadow token, or none. If the project's aesthetic is flat or brutalist, use borders and no shadows.
* Borders are 1px and use the border token. Never use borders thicker than 2px for grouping.
* Dividers replace neither spacing nor headings. Use them only in dense lists and tables.

## 7. Buttons and Actions

One view, one primary action.

* Each view has exactly one primary button. It uses the accent color as its fill.
* Secondary actions are outline or ghost buttons in neutral colors. Tertiary actions are text links.
* Destructive actions use the error color and never sit beside the primary action without spacing.
* Button labels are verbs. "Save changes", not "OK". "Delete project", not "Confirm".
* Button height is 40px by default, 32px in compact contexts, 48px on touch-first screens.
* Interactive elements have a minimum target of 44 by 44px, using padding if the visual is smaller.
* Do not use an icon as the only content of a button unless it has a visible label on hover and an aria-label always.

## 8. Interaction States

An element without states is a mockup.

* Every interactive element has hover, focus-visible, active, and disabled states.
* Every asynchronous element has loading, empty, error, and success states.
* Focus rings are visible, at least 2px, and use the accent color. Never remove the outline without replacing it.
* Disabled elements are visibly disabled, at reduced opacity, and are not focusable.
* Hover changes are subtle: a background shift, an underline, or a border. Do not change size or layout on hover.
* Loading states preserve layout. Use skeletons or fixed-height placeholders instead of collapsing content.
* Selected and active states are distinct from hover.

## 9. Icons

Icons support labels. They rarely replace them.

* Use one icon library for the entire product.
* One stroke weight and one size per context. Default sizes: 16px inline, 20px in buttons and inputs, 24px standalone.
* Icons align to the text baseline or center of the line they sit with.
* Icons that carry meaning have a text label or an aria-label. Decorative icons are aria-hidden.
* Do not mix filled and outlined styles from the same library in one view.
* Do not use emoji as icons in the interface.

## 10. Forms and Inputs

Forms are where most interfaces fail.

* Labels sit above inputs, left-aligned, always visible. Placeholder text is not a label.
* Input height matches button height. Default 40px.
* One column. Multi-column forms are allowed only for short related fields such as city and postal code.
* Group fields with headings and spacing. Break long forms into steps at logical boundaries.
* Show validation inline, next to the field, after the user leaves the field. Never only at the top of the form.
* Error messages say what went wrong and how to fix it, in plain language.
* Required fields are the default. Mark optional fields instead.
* The submit button sits directly below the last field, left-aligned with the inputs.

## 11. Tables and Data

Density is fine. Noise is not.

* Numbers are right-aligned and use tabular figures. Text is left-aligned.
* Use row spacing or subtle row backgrounds instead of vertical borders.
* Column headers are visually distinct through weight or case, not through a colored background.
* Keep row height consistent. Default 48px, compact 40px.
* Truncate long text with an ellipsis and show the full value on hover or focus.
* Empty tables show an empty state with a clear next action, not a blank grid.

## 12. Motion

Motion explains change. It does not decorate.

* Use motion only to show where something came from or went to, or to confirm an action.
* UI feedback transitions are 100 to 200ms. Layout transitions are 200 to 300ms. Nothing in the interface exceeds 400ms.
* Use ease-out for elements entering and ease-in for elements leaving.
* Respect prefers-reduced-motion. Reduce or remove all non-essential motion when it is set.
* Do not animate on page load. Do not animate continuously.

## 13. Imagery and Empty States

Every screen has a state where the content is missing.

* Every list, table, and dashboard has a designed empty state with one sentence and one action.
* Images have a fixed aspect ratio and a placeholder background so layout never shifts while loading.
* Do not use stock illustrations or decorative images to fill space. Space is fine.
* Avatars and thumbnails are one consistent size and radius per context.

## 14. Consistency and Components

Reuse before you create.

* Check the project's existing components before building anything. Reuse them. Extend them only when necessary.
* Similar things look the same. Different things look different. Never reuse a visual treatment for a different meaning.
* Every value in a stylesheet comes from a token. If you need a value that has no token, add the token first.
* Name components and tokens by role, not by appearance. "surface", not "light-gray". "primary-button", not "blue-button".
* One pattern per problem. If the codebase has two ways to do the same thing, use the more common one and flag the other.

## 15. Accessibility

Accessible is the baseline, not a feature.

* Use semantic HTML: headings in order, lists as lists, buttons as buttons, links as links.
* Every image has alt text or is marked decorative.
* Every input has an associated label.
* Every interactive element is reachable and operable by keyboard, in a logical order.
* Contrast, focus, target size, and motion rules above are requirements, not preferences.
* Test at 200 percent zoom. Nothing overlaps, nothing is cut off.

## Finish Pass

Before declaring any interface complete, do this review and fix what fails:

1. Count the accent colors on screen. The answer is one.
2. Count the distinct font sizes. The answer is five or fewer.
3. Count the primary buttons in the view. The answer is one.
4. Check every spacing value against the scale. Remove any that are not on it.
5. Find every card. For each one, ask whether spacing alone would have grouped it. Remove the ones where the answer is yes.
6. Find every interactive element. Confirm hover, focus-visible, active, and disabled states exist.
7. Find every asynchronous element. Confirm loading, empty, and error states exist.
8. Tab through the whole view. Confirm focus is visible and the order is logical.
9. Resize to 375px wide. Confirm nothing overflows and the primary action is still reachable.
10. Remove anything left that does not help the user complete the primary action.

When rules conflict, prioritize in this order: legibility, accessibility, the project's existing patterns, then these defaults. Do not apply these rules mechanically. Use them to make deliberate decisions for the user's context and goal.
