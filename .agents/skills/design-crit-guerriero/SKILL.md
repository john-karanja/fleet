---
name: design-crit-guerriero
description: >
  Apply Sebastiano Guerriero's design thinking to evaluate and improve CVFMS screens.
  Use this skill when reviewing any desktop or mobile frame, writing a critique, or
  deciding how to refactor a layout to be clearer, denser, and more intentional.
  The reference screenshots in /references show the exact Before-After standard to aim for.
---

# Design Crit: The Guerriero Standard

## Who is Sebastiano Guerriero?

Sebastiano Guerriero (@guerriero_se) is a senior product designer known for precise,
content-first UI work. His design approach is grounded in one core principle:

> "Most of the job is about refactoring the content so you can deliver more
> information within the same space."

This is not about making things prettier. It is about making things **clearer and denser**
without adding noise. The reference screenshots in this skill's /references/ folder show
his Before vs After on a Workshop Job Calendar — a domain nearly identical to CVFMS's
FRAME-03 (Peter's Workshop Job Card Board).

---

## The Reference Screenshots

| File | What it shows |
|---|---|
| `guerriero_before.webp` | Before: flat label/value drawer, no icons, no checklist, no photo, no inline actions. Lots of whitespace, low information density. |
| `guerriero_after.webp` | After: same content refactored — icon-per-row details, live struck-through checklist, vehicle photo thumbnail, inline Call/Message links, compact calendar with avatar chips. |
| `guerriero_card_anatomy.png` | Annotated diagram: card color = job type; icon = job status; technician avatar; "show more details as the card becomes bigger" (progressive disclosure). |

When evaluating a CVFMS screen, open these references and ask:
"Could Guerriero draw a red arrow from our current state to a better one?"
If yes, the screen is not done.

---

## The 7 Guerriero Principles Applied to CVFMS

### 1. Refactor Content, Do Not Add Decoration

What he does: Removes whitespace inflation and label-only rows. Every pixel either
carries information or separates two pieces of information clearly.

CVFMS test: If a detail panel has 6+ rows of "Label: Value" text with no icons and
no visual grouping, it has not been refactored — it has been transcribed. Flat
label/value stacks are the Before state, not the finished state.

---

### 2. Icon Equals Semantic Signal, Not Decoration

What he does: Every icon in the detail drawer carries a specific, non-redundant meaning:
- Calendar icon: date/time
- Clock icon: time remaining
- Bay/location icon: work location
- Person icon: assignment/technician

The icon is NOT a bullet point. It is NOT generic. It tells you the type of information
before you read the text.

CVFMS test: If an icon could be swapped for any other icon with no loss of meaning,
it is decoration. Replace it with a meaningful one or remove it. Outline SVG icons only
(Heroicons or Lucide), 1.5px stroke, never emoji.

---

### 3. Color Equals Job or Status Type, Not Aesthetics

What he does: Card background color encodes job type. The color does real semantic work
— you can scan the calendar and immediately see the distribution of job types without
reading.

CVFMS test: Every use of color must answer "what decision does this color change?"
If it cannot answer that question, the color is decoration. Status colors in CVFMS
are reserved: Green = Active/Pass, Amber = Warning/Pending, Red = Critical/Fail.
Never introduce a color without a locked semantic meaning.

---

### 4. Progressive Disclosure — Show More as the Container Grows

What he shows (card anatomy diagram): Small cards show only the essential
(vehicle name + time). Taller cards reveal more (technician name, client). The content
adapts to the available space — it does not truncate with an ellipsis, it expands.

CVFMS test: Any card or panel that truncates content with "..." instead of using
available space differently is a progressive disclosure failure. Either show the content
or give it a deliberate "View Details" affordance that leads somewhere real.

---

### 5. Live Checklists with Struck-Through Completion

What he does: Completed checklist items are struck-through in muted grey.
In-progress items are bold/dark. Upcoming items are muted/inactive. This gives
the status of the entire job at a glance — no need to count or read.

CVFMS test: Any checklist in CVFMS (FRAME-03 QA release gate, FRAME-07
walkaround inspection, FRAME-02 Dispatch Gate) should use this pattern:
Done = struck-through and muted. Pending = full opacity. Upcoming = greyed-out.

---

### 6. Inline Actions Close to Their Subject

What he does: "Call" and "Message" appear on the same line as the client name —
not in a separate Actions section, not in a footer button row. The action lives
exactly where you learn you need it.

CVFMS test: If an action (Override / Approve / Reassign / Dispatch) requires the
user to scroll away from the relevant context to find the button, the layout has
failed this principle. Scope every action to its context row or panel section.

---

### 7. Vehicle Photo as Identity, Not Decoration

What he does: A small vehicle thumbnail sits inline next to the client name and
vehicle line. It is not a hero image. It is not optional. It makes the record
immediately identifiable without reading.

CVFMS test: Any screen where a vehicle is the subject (job card, dispatch detail,
trip detail, vehicle registry row) should carry a vehicle thumbnail. No photo means
a grey placeholder with the registration plate, never a generic car icon. This is
already a locked CVFMS rule (03_MASTER_DESIGN_SYSTEM.md section 1, third pass).

---

## How to Run a Guerriero Critique on a CVFMS Screen

When asked to review a frame, work through this checklist and report any failures:

GUERRIERO CRITIQUE — [Frame Name]

1. CONTENT DENSITY: Are there flat label/value rows that could carry semantic icons?
   Pass or Fail — describe what rows need icon prefixes

2. ICON SEMANTICS: Does every icon have a unique, non-swappable meaning?
   Pass or Fail — list any generic or decorative icons

3. COLOR SEMANTICS: Does every use of color answer "what decision does this change?"
   Pass or Fail — list any color used for aesthetics only

4. PROGRESSIVE DISCLOSURE: Does truncated content have a deliberate expand affordance?
   Pass or Fail — list any "..." truncation without a View Details path

5. CHECKLIST PATTERN: Are completion states visually differentiated (struck/muted/full)?
   Pass or Fail — applies to dispatch gate, walkaround, QA release, any checklist

6. ACTION PROXIMITY: Are actions placed inline with their subject, not in a remote footer?
   Pass or Fail — list any actions separated from their context

7. VEHICLE IDENTITY: Does every vehicle-subject screen show a photo or plate placeholder?
   Pass or Fail — list screens missing vehicle visual identity

Output format: A pass/fail table followed by exact, prioritised fixes written as
Figma AI prompt fragments ready to be pasted and run.

---

## The Bar

The After screenshot in /references/guerriero_after.webp is the minimum acceptable
standard for any detail drawer, job card, or checklist screen in CVFMS. If a rendered
screen looks closer to the Before than the After, it is not done — regardless of
whether it is technically correct per the spec.

The spec defines what information appears.
Guerriero's standard defines how clearly that information is delivered.
