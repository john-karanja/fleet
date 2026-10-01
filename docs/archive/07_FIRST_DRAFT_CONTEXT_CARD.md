# CVFMS: First Draft Context Card

**Document ID:** `DOC-CVFMS-007`
**Purpose:** Figma's First Draft has no memory or file access between prompts — it only sees what's pasted into the box, fresh, every time. This card is a stable, short summary of context that rarely changes, meant to be pasted at the **top of every First Draft prompt**, before the screen-specific instructions for whatever you're generating that time. Keep this card itself short — its whole value is that it's cheap to paste every time; the full reasoning behind it lives in `01-06`.

Copy everything below the line into the top of your prompt, then add your specific screen instructions after it.

---

```
PROJECT CONTEXT: This is CVFMS, a County Government Vehicle Fleet Management System for Kenya — enterprise software for county staff (not a consumer or citizen-facing app), dense/audit-sensitive/approval-heavy, light theme.

DESIGN TOKENS (always use these exact values, never invent new ones):
- Font: Inter throughout.
- Type scale: Page title 26px bold · Section header 20px semibold · Body/table primary 14px medium · Body secondary 13px regular · Meta/badge 12px semibold · Micro-eyebrow 11px bold uppercase · Metric numbers (KPI values) 24px bold — visually distinct from headings, plain text delta beneath, NO sparkline on any KPI card (tried twice, removed twice — a partial sparkline row looks broken/unbalanced, and no sparkline in this system has been tied to a specific decision Grace would make differently).
- Colors: canvas #F8FAFC (page background, must look visibly different from white cards) · surface #FFFFFF (cards) · border #E2E8F0 · primary accent civic green #006837 · success #10B981 · critical red #DC2626 · warning amber #D97706 · info blue #2563EB · text primary #0F172A · text secondary #64748B · text muted #94A3B8.
- Dark sidebar: #0F172A background, inactive nav items #94A3B8, active item white text + 3px green left border + subtle low-opacity green tint (not the light-mode green tint elsewhere).
- Radius: 12px cards/panels · 6px pills · 8px buttons/inputs/chips/thumbnails.
- Spacing: 8px grid — 16px card padding, 24px gaps between major sections.
- Every card needs BOTH a 1px border AND a soft drop shadow (0 1px 3px rgba(0,0,0,0.06)) — cards must look elevated above the gray canvas, never flush/flat white-on-white.

TYPE HIERARCHY RULE (apply to every row/list — this is the most commonly missed rule): exactly ONE dominant text element per row (14px medium, dark) — everything else (tags, timestamps, metadata) drops to 11-12px, muted gray, uppercase with letter-spacing where it's a label. Never more than 2 distinct text sizes visible in one row. Color reinforces this hierarchy, it does not replace it — a colored tag must still be small/light even though it's colored.

COLOR DISCIPLINE: color only appears where it signals status/severity/urgency (pills, dots, accent borders). Everything decorative (icons, dividers, chrome) stays neutral gray. Never fill a whole row/box with color as the primary treatment — prefer a small colored dot or a thin accent border over a full tinted background.

ACTIVE PERSONA: Grace Wanjiru, County Fleet Manager. Her two jobs: (1) know the real-time state of the fleet, (2) act before small problems become expensive/dangerous — job 2 dominates; a fact she can't act on is lower priority than one she can. She has real write authority (edit registry, reallocate vehicles, approve maintenance, override blocked dispatches) — she is not a passive monitor, every screen for her needs a clear path to action, not just display.

STANDING RULE: before adding any chart, sparkline, or decorative visual element, name the specific decision it would change for the user. If you can't name one, it's decoration — leave it out. This project has had decorative elements removed multiple times for failing this test.

CRAFT TARGET: enterprise SaaS polish comparable to Airwallex, Vercel, Linear, or incident.io — not a generic AI-generated dashboard look. No illustrations, no gradients, no emoji-as-icons.
```

---

## When to update this card

Update this file (and re-copy it into your next prompt) whenever a *standing* rule changes — a token value, a persona correction, a new system-wide pattern (like the List Row Hierarchy rule). Do **not** add screen-specific content here (e.g. "Needs Attention has 3 rows about KCA 902B") — that belongs in the per-screen prompt you write after pasting this card, not in the reusable card itself. If this card grows past what's comfortable to paste every time, that's a signal something in it should move to a project rule file instead (`.agents/rules/`) rather than being repeated per-prompt.
