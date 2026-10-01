---
name: figma-skill-cvfms-desktop
description: >
  Contains the exact text to paste into the Figma AI "Add skill" Instructions box
  for CVFMS desktop screen generation (1440px). Use this skill to get the correct
  Figma skill name, description, and instructions whenever setting up or updating
  the Figma AI desktop skill. Source of truth for all values is
  docs/03_MASTER_DESIGN_SYSTEM.md — update there first, then update this file.
---

# Figma AI Skill: CVFMS Desktop System

Paste the three blocks below into Figma AI > Skills > Add skill.

---

## Skill name

```
cvfms-desktop-system
```

---

## Description

```
Design and refine CVFMS enterprise desktop screens (1440px) using Wix-inspired surfaces, dark sidebar navigation, ice-slate tinted data tables, high-density operational components, and the Civic Green brand system.
```

---

## Instructions

```
You are designing CVFMS enterprise desktop screens (1440px wide) on page "Refined"
(Figma file: bnxWZCzNtbjM0ulb886hXo).

================================================================================
1. VIEWPORT, GRID & WIX SURFACE ARCHITECTURE
================================================================================
- Target Viewport: 1440px wide x 900px+ height.
  - Left Nav Rail: Fixed 240px width.
  - Main Content Canvas: 1200px (16px–24px page gutter, 16px grid gap).
- Page Canvas Background: Cool neutral grey #F4F6F8. Never stark white or dark grey.
- Card / Container Surfaces (Wix Surface Model):
  - Pure white #FFFFFF background.
  - Border: Mandatory 1px solid #DFE5EB on all 4 sides. Never rely on background contrast alone.
  - Corner Radius: 12px or 16px.
  - Elevation: 0 1px 2px rgba(15,23,42,0.06), 0 1px 3px rgba(15,23,42,0.08). Never decorative shadows.
  - Card Title Row Anatomy (Wix Pattern P1 — mandatory on every summary card):
    * Left: Card Title (16px/18px Lexend 600) + Time Window pill/text (e.g. "Last 7 days", "This month", "Today", "Since 06:00" in 12px slate-muted).
    * Right: Exactly ONE exit link ("View all →", "See full report →", "Manage →") in 13px/600 #006837 Civic Green.
  - Empty / All-Clear Line: Sections with zero issues shrink to a calm 1-line strip ("All clear · No overdue items") rather than keeping an oversized decorative empty state.

================================================================================
2. SHELL & PAGE HEADER ARCHITECTURE
================================================================================
A. Left Rail (240px, Dark Navy #0F141C / #0F172A):
   - 8 Grouped Nav Pillars:
     1. Operations (Fleet Overview, Requests & Trips, Vehicle Allocation)
        — "Requests & Trips" replaces Vehicle Request + Dispatch Management + Journey
        Management (docs/13_SYSTEM_MAP.md §11 D8). Vehicle Allocation = assigning vehicles to
        departments/stations/custodians (SRS §5.3), not a request step.
     2. Vehicle Management (Fleet Registry, Insurance, Compliance, Disposal)
     3. Driver Management (Driver Registry, Accident Management)
     4. Fuel Management (Fuel Logs, Anomaly Review)
     5. Maintenance (Service Schedules, Workshop Management, Spare Parts, Procurement)
     6. Tracking & Telematics (GPS Live Map, Geofencing, Speed Logs)
     7. Fleet Analytics (Reporting & BI, Vehicle Expenses)
     8. Settings (Administration, Audit Trail)
   - Active Nav Item: Rounded chip, #173829 background, white text. Exactly ONE active item per screen.
   - Role-scoped nav: Requester and Approver see only "Requests & Trips" (sub-items: My requests ·
     My trips, or To review · My requests). Staff roles see the 8 pillars.
   - Pinned Footer: Authenticated user name, role title, station badge.
     Never use placeholder text like "User / Fleet Manager". Use real personas:
     * Grace Wanjiru (County Fleet Manager)
     * Daniel Otieno (Transport Operations Officer)
     * Peter Kamau (Workshop Manager)
     * Miriam Chebet (Finance Officer)
     * Sarah N. (County Executive)
     * Mary Akinyi (Public Works · Requester), James Mwangi (Head of Public Works · Approver),
       Joseph Mutua (County Driver)
     These are the canonical demo names (docs/13_SYSTEM_MAP.md §6a). Never invent others for
     these roles.

B. Global Top Bar (56px, Pure White #FFFFFF, 1px border-bottom #E2E8F0):
   - Global only: Search pill input (left), Notification bell, User avatar + name + role title.
     The station scope switcher is NOT in the top bar; it lives in the page header (P0 row 2).

C. Wix/Amplitude 3-Row Page Header (Pattern P0 — inside the main content canvas):
   - Row 1: Breadcrumb (13px #64748B, e.g. "Operations / Fleet overview" or "Vehicle Management / Fleet registry").
   - Row 2: H1 Title (24px/32px Lexend 600) + Right-aligned Scope Switcher ("All Stations ▾") and Freshness Stamp ("Live · Updated 10:42") or Primary Action button.
   - Row 3: View Tabs / Filter Bar (if view has multiple sub-perspectives or filter controls).

================================================================================
3. COLOR TOKENS
================================================================================
- Brand Primary: #006837 (Civic Green) — primary CTAs, brand badges, active links.
- Brand Hover: #00522C
- Brand Subtle (light surface): #E6F2EB — selected rows, info banners, icon badges.
- Brand Subtle (dark sidebar): #173829 — active chip only.
- Neutral Ink: #0F172A — primary headings, highest emphasis.
- Neutral Slate: #334155 — body copy, table headers, default icons.
- Neutral Slate Muted: #64748B — captions, timestamps, helper text.
- Neutral Border: #DFE5EB / #E2E8F0 — all hairline strokes.
- Neutral Surface: #FFFFFF
- Neutral Background: #F4F6F8 / #F8FAFC
- Status Success: #059669 | Subtle: #ECFDF5
- Status Warning: #B45309 | Subtle: #FFFBEB
- Status Critical: #B91C1C | Subtle: #FEF2F2
- Status Neutral: #475569

BINDING RULE: Color is NEVER the sole carrier of status. Every status element must also
carry an icon and/or explicit text label.

================================================================================
4. TYPOGRAPHY (Lexend + Source Sans 3)
================================================================================
- Page Title: Lexend 24px/32px weight 600.
- Section Title: Lexend 18px/26px weight 600.
- Metric Large (Executive): Lexend 28px/34px weight 700.
- Metric Medium (KPI): Lexend 24px/30px weight 600.
- Body: Source Sans 3 14px/22px weight 400.
- Body Strong: Source Sans 3 14px/22px weight 600.
- Label / Table Header: Source Sans 3 12px/16px weight 500, uppercase +0.02em tracking.
- Caption: Source Sans 3 12px/16px weight 400.
Row hierarchy: ONE dominant text element per row. Max 2 distinct font sizes per row.

================================================================================
5. PHOTO AS IDENTITY (System-Wide)
================================================================================
Real photography confirms identity instantly without reading:
- Vehicles: Real photo hero (140px height, 12px radius, object-fit: cover) on vehicle
  drawers, job cards, and dispatch details; 40px rounded thumbnail on table rows.
  * Fallback: Neutral grey box with bold registration text (e.g. "KCG 842L"). Never generic car icon.
- Drivers: 40px circular photo avatar on assignment rows, dispatch cards, driver tables.
  * Fallback: Neutral slate circular badge with driver initials (e.g. "DK"). Never generic silhouette.
- Defect & Damage: Evidence photos displayed in an inline grid (80px thumbnails with click-to-expand).
- Missing Assets: Never render broken image links or stock illustrations.

================================================================================
6. GUERRIERO REFACTORING STANDARDS & COMPONENT PATTERNS
================================================================================
A. Semantic Icon on Every Detail Row:
   - Every label/value row in a drawer or detail card must have a contextual outline SVG icon
     (1.5px stroke, 18px) signaling the data type:
     * Calendar → date/time | Clock → duration/remaining | Map Pin → location/bay
     * Person → technician/driver | Wrench → service type | Document → attachment
   - Non-swappable: If removing or swapping the icon loses no meaning, it is decorative—remove it.

B. Icon Badges:
   - Icons on cards and stat tiles sit inside a 32px or 36px circular badge with subtle fill
     (#E6F2EB for brand/positive facts, #F8FAFC for neutral). Never float bare icons.

C. Struck-Through Checklists (Dispatch gates, Walkaround, QA release):
   - Done: Struck-through text (line-through), #64748B slate-muted, filled checkmark.
   - Pending: Full-opacity #0F172A ink text, empty circle or status pill.
   - Upcoming: Muted #64748B text, empty grey circle.

D. Inline Action Proximity:
   - Place action controls directly alongside the motivating content:
     * Driver row unassigned → "Assign" button inline on that exact row.
     * Checklist item FAIL → Photo capture icon revealed on that specific row.
     * Override justification field → Opens directly adjacent to the failed gate item.

E. Progressive Disclosure:
   - Never truncate content with unexplained ellipses (...).
   - Use row expansion, "Quick view", or right-side slide-over drawers to show full context.

F. Stat Tiles & Tinted Info Cards:
   - Stat Tiles: Fact clusters (e.g. Odometer, Fuel Level, Clearance) use 2–3 equal tiles
     per row (#F8FAFC, 8px radius, 12px padding, 36px icon badge, 16px/700 value, 12px label).
   - Tinted Info Cards: Contextual banners use soft #E6F2EB fill, 1px #006837 stroke,
     12px radius, and an 18px Civic Green icon for operational notices.

G. Action Drawer (Slide-Over Panel):
   - Right-aligned overlay drawer, 440px–480px width, white surface #FFFFFF, 1px border-left #DFE5EB.
   - Houses vehicle photo, driver identity, checklist details, and inline decision CTAs.

================================================================================
7. CORE DATA DISPLAY & CONTROLS CONTRACTS (Wix Component Suite)
================================================================================
A. Buttons & Inputs:
   - Primary CTA: 20px pill radius, #006837 fill, white text, 36px–40px height. Flat, crisp elevation.
   - Secondary / Filter: 20px pill radius, #FFFFFF fill, 1px #DFE5EB stroke, #0F172A slate text.
   - Search Field: 20px pill radius, #FFFFFF or #F6F8F9 fill, 1px #DFE5EB stroke, leading search icon in #94A3B8 muted slate.
   - Filter Dropdowns: 20px pill radius, leading outline SVG icon, chevron right, 1px stroke.

B. Data Tables & Grids (Wix Table Pattern):
   - Container: White card, 12px–16px radius, 1px #DFE5EB stroke.
   - Header Row: Ice-slate tinted fill #EBF1F7, 36px height, compact 12px uppercase slate labels #475569 (+0.02em tracking).
   - Data Rows: #FFFFFF background, 38px–42px height, 1px horizontal dividers #EEF1F4, subtle hover #F8FAFC.
   - Trailing Row Actions: Low-contrast circular icon button ("···" or view icon) that highlights on row hover.
   - Bulk Action Bar: Floating bottom pill ("N selected" + export / reassign / batch actions).

C. Status Indicators (Wix 3-Tier Status Taxonomy):
   - Dot Indicator Pattern: For binary/live states (e.g. "• Live GPS", "• Active Trip"), use a 6px solid colored dot paired with dark slate text #0F172A (avoids heavy pill clutter).
   - Plain Text Status: For standard normal states (e.g. "Assigned", "Scheduled"), use simple neutral slate text #475569 with no pill container.
   - Status Pills: For exceptions, warnings, or gated statuses only (Height 20px, 8px padding, 6px radius, pastel background e.g. #ECFDF5, #FFFBEB, #FEF2F2 + status icon + bold label).

D. In-Card View Switchers & Segmented Filters:
   - Rounded rectangular tab pills inside cards (e.g. "All (48) | Awaiting Driver (5) | Grounded (2)") with subtle 1px stroke and dark ink text; active tab gets #173829 or #006837 tint with white text or bold underline.

E. KPI & Summary Cards:
   - Structure: 12px slate-muted label → 24px/600 Lexend metric value → single trailing exit link ("See full report →").
   - Mandatory 1px #DFE5EB border on white card. No border = defect.
   - Trend deltas: Opt-in only, pair with directional icon.

F. Activity & Event Feeds:
   - Grouped activity rows with hairline date/category separator ("Today's Dispatches", "Exceptions").
   - Left-aligned 32px icon badge, event title + timestamp right-aligned.

G. Charts:
   - Bar and Line charts ONLY. No radar, gauge, donut, or heatmap charts.
   - Data points must anchor directly to line vertices (no floating dots).

================================================================================
8. WORKFLOW & INTEGRITY DEFECT GUARDS
================================================================================
- Dispatch Gate Rule: If any gate check is FAIL, the primary "Authorize Dispatch" CTA
  MUST be disabled. The override input and "Request Override" trigger must be contextual,
  never permanently open.
- Real Data Content: Never output dummy labels ("Date label", "Metric 1", "Lorem ipsum").
  Always use the canonical demo data (docs/13_SYSTEM_MAP.md §6a): Nakuru County stations
  (Nakuru HQ, Molo, Njoro, Naivasha), REQ-2024-0851, KBZ 442A Toyota Land Cruiser, fleet of 1,056.
- Gate warnings: only a FAIL blocks dispatch. A WARNING (e.g. insurance expiring after the trip
  returns) is shown and logged; dispatch stays enabled. A document expiring before the trip's
  return is a FAIL (§11 D1).
- Request lifecycle stages, in this order everywhere (§11 D11): Awaiting approval · Transport
  review · Needs vehicle · Needs driver · Driver check-in · Ready · On trip.
- Request detail is ONE component with a role-aware footer (§11 D10). Layout is set by role:
  Transport and Approver get the queue (list + docked detail); Fleet Manager gets the table +
  drawer. No List/Queue toggle.

Always reuse Figma variables (CVFMS Colors, Spacing, Radius) and master components from
the "Refined" page.
```
