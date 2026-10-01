---
name: figma-skill-cvfms-mobile
description: >
  Contains the exact text to paste into the Figma AI "Add skill" Instructions box
  for CVFMS mobile driver app screen generation (390px). Use this skill to get the
  correct Figma skill name, description, and instructions whenever setting up or
  updating the Figma AI mobile skill. Source of truth is docs/03_MASTER_DESIGN_SYSTEM.md
  (Components 9-19) and docs/04_FIGMA_SCREEN_BLUEPRINT.md §8 — update there first.
---

# Figma AI Skill: CVFMS Mobile Driver App

Paste the three blocks below into Figma AI > Skills > Add skill.

---

## Skill name

```
cvfms-mobile-system
```

---

## Description

```
Design and refine CVFMS mobile driver app screens (390px PWA) using the dark collapsing header, urgency-ordered assignment cards, struck-through inspection checklists, and trip lifecycle bookends. Governs Joseph's FRAME-07 series on the Refined page.
```

---

## Instructions

```
You are designing the CVFMS mobile Driver App (Joseph, FRAME-07 series, 390px width)
on page "Refined" (Figma file: bnxWZCzNtbjM0ulb886hXo).

================================================================================
1. VIEWPORT, SHELL & HEADER
================================================================================
- Viewport: 390px x 844px (iPhone 15 / Android PWA).
- Canvas Background: Light neutral grey #F8FAFC. Cards sit on this surface.
- Header (Dark Navy #0F141C / #0F172A):
  Expanded State: Greeting ("Good morning, Joseph"), driver avatar (40px circle),
  County Crest/Emblem, notification bell with red unread dot.
  Collapsed State (on scroll): Compact title and notification icon only.
- Bottom Navigation Bar (56px, dark navy base):
  3 tabs: Home, Trips, Profile.
  Active Tab: White icon on #173829 chip (radius.md).
  Inactive Tabs: #64748B.

================================================================================
2. SURFACE TOKENS
================================================================================
- Card Fill: #FFFFFF, 12px radius, 1px solid #DFE5EB border, 20px internal padding.
- Gap between cards: 12px. Gap between elements within card: 8px.
- Page Canvas: #F8FAFC.
- Primary Accent: #006837 (Civic Green).
- Status Green: #10B981 | Amber: #F59E0B | Red: #EF4444.
- Never color alone — always pair with an icon or text label.

================================================================================
3. ASSIGNMENT CARDS & HOME LIST (FRAME 7A)
================================================================================
Urgency-ordered vertical card list. Never a single-card takeover.

Card order:
  1. In-Progress Trip (top)
  2. Pending Assignment (Needs Response)
  3. Scheduled for later (quiet/informational)

Card anatomy:
- Requester initials avatar (32px) + Destination Headline (16px Lexend 600).
- Departure time and reference ID: secondary/muted (12px–14px Source Sans 3).
- Journey Visual: Vertical timeline — hollow origin dot (○) → 1px line → filled destination dot (●).

Card CTAs (max 2 visible filled-green CTAs in the viewport):
- In-Progress: "Start Pre-Trip Inspection →" filled #006837, 44px height.
- Pending: Inline pair — "Accept" (filled #006837) + "Decline" (outline 1px #DFE5EB).
  Minimum 8px gap between the two buttons.
- Scheduled: Muted text only. No action button.

================================================================================
4. DETAIL ROWS — SEMANTIC ICONS
================================================================================
Every label/value row in any detail drawer or card must carry a contextual SVG icon:
- Calendar icon → date / scheduled time
- Clock icon → duration or time remaining
- Location pin → destination or work location
- Person silhouette → assigned driver or requester
- Car icon → vehicle identity
- Wrench icon → service or maintenance type
- Document icon → attached files or reports
All icons: Heroicons or Lucide outline, 1.5px stroke, 18px. Never emoji.

================================================================================
5. CHECKLISTS (Walkaround Inspection FRAME 7B, any checklist)
================================================================================
Three visual states — differentiated without color alone:
- Done: struck-through text (line-through), #64748B muted, filled checkmark icon.
- Pending/Current: full opacity #0F172A, empty circle icon.
- Upcoming: #64748B muted, empty grey circle.

Defect photo capture: camera icon revealed per row when that row is marked Fail.
NOT a blanket "Attach photos" button at the bottom.

================================================================================
6. TRIP LIFECYCLE BOOKENDS (FRAME 7C)
================================================================================
- Start State: Starting Odometer + [Photo Verified] pill + Fuel Gauge pill +
  "Start Journey Now" CTA (filled #006837, 44px).
- Active Trip (Stage 2 of 3): Stage indicator, two outline chips
  ("Log Fuel Stop", "Report Breakdown"), persistent "Complete Trip" CTA.
- End State: Closing Odometer → auto-calculated distance + Defect check +
  "Finalize & Close Trip" CTA.

================================================================================
7. PHOTO AS IDENTITY
================================================================================
Use real images wherever they make a record immediately identifiable:
- Vehicles: full-width thumbnail (140px height, 12px radius, object-fit cover).
- Drivers: 40px circular avatar; initials monogram as fallback.
- Damage/defects: full-width or grid, the photo IS the content.
Missing asset: neutral placeholder (plate text / initials / camera-outline icon).
Never a broken image, never a generic silhouette.

================================================================================
8. ERGONOMICS & ACCESSIBILITY
================================================================================
- Minimum touch target: 44px height. Buttons: 44px–48px height.
- Icon style: Heroicons or Lucide outline, 1.5px stroke. Never emoji.
- Typography: Lexend for headings/hero labels. Source Sans 3 for body/meta.
- Primary text #0F172A. Muted text #64748B.
- Status Green (#10B981) for Active/Ready. Amber (#F59E0B) for Pending.
  Red (#EF4444) for Defect/Critical. Never color alone.

Always bind to existing Figma variables (CVFMS Colors, Spacing, Radius) and reuse
master components from the "Refined" page.
```
