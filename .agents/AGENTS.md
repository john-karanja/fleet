

---

## Automated Testing Philosophy (Playwright)

**Use Playwright ONLY for complex, multi-step stateful flows.**

Playwright spins up a real browser and is slow (~10–60s per run). It is the wrong tool for verifying layouts, static text, or component visibility. Those are trivially validated by opening the dev server in a browser.

### When to use Playwright ✅
- Multi-step flows that mutate state across components (e.g. Change Group → verify drawer reflects new group)
- Modal confirmation flows where the outcome must be validated in a different UI area (e.g. Add Role → verify in Access tab)
- Lifecycle state transitions (e.g. Suspend → verify status pill changes)
- Anything where the result is invisible until a sequence of actions completes

### When NOT to use Playwright ❌
- "Does this route render?" → open the browser
- "Is this text/button/column visible?" → open the browser
- "Does the table have an actions column?" → open the browser
- Navigation checks, `waitForSelector('text=...')` for static labels → open the browser

### Test structure rules
- No trivial `waitForSelector` assertions for static text
- Every test must assert a **state change** (`if (!content.includes(X)) throw new Error(...)`)
- Always scope dialog locators to `.MuiDialog-root` (or equivalent) to avoid ambiguity with same-named buttons in the page
- MUI `startIcon` content is NOT part of button text — `button:has-text("+ Add Role")` will never match; use `button:has-text("Add Role")`
- Wrap `Tooltip`-covered `IconButton`s with `{ force: true }` if click times out

