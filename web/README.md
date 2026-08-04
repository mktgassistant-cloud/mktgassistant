# Case study cards + modal (GoHighLevel embed)

`ghl-case-study-cards.html` is a single self-contained block — HTML, CSS and JS
in one file, no build step, no external dependencies — that renders the
clickable case-study card grid and the full case-study modal.

**Currently loaded with one card (Tyler R. / TJR) so the first one can be
dialed in before the rest go live.** The other 7 case-study objects are parked
in `remaining-case-studies.js`; paste them into the `CASE_STUDIES` array when
card #1 is approved. The layout adapts on its own — 1 card renders centered at
400px, 2 or 3 stay centered, 4+ becomes the 4-column grid — and the modal's
prev/next arrows and "Case study 1 of 8" line appear only once there is more
than one.

## Install in GHL

1. Funnel/page builder → add an **element** → **Custom Code** (in some
   accounts it's called *Code*). Put it in a full-width section/row.
2. Paste the entire contents of `ghl-case-study-cards.html` into the code box.
3. Save, then **preview the live page** — the builder canvas often refuses to
   run `<script>`, so cards can look missing inside the editor while working
   perfectly on the published page.

If your account's code element strips `<script>`, put the `<style>`+HTML in the
code element and paste the `<script>` block into
**Settings → Tracking Code → Footer** instead. Nothing else changes.

## Editing content

Everything renders from the `CASE_STUDIES` array near the top of the `<script>`.
Cards and their modals are generated from the same object, so they can't drift
apart. Each entry documents itself in the comment block at the top of the file;
search for `TODO` to find every field still needing real copy:

- avatar URLs (upload to the GHL media library, paste the URL into `avatar` —
  an empty string falls back to the person's initials)
- `modal.quote` for the 7 case studies that don't have one yet
- `modal.sections[].html` bodies — an empty section is skipped, so partially
  filled case studies still look finished
- `modal.video` — omit the key entirely and no player is rendered
- `modal.cta.href` — currently `#book`; point it at your booking section/URL

Only the stats already visible on the live site's cards are pre-filled, plus
Tyler's quote and first two modal sections. Nothing else was invented.

## Preview locally

Open `ghl-case-study-cards.html` directly in a browser — it renders standalone.
For a dark page background matching the live site, wrap it in a scratch file
with `body{background:#0d0c0f}`.

## What differs from a stock ChatGPT version

- One data array drives cards **and** modals (no duplicated markup to keep in
  sync; adding a 9th case study is one object).
- The modal is relocated to `<body>` at runtime. GHL sections routinely use
  `overflow:hidden` and CSS transforms, which clip or trap a `position:fixed`
  modal — this is the single most common reason DIY GHL modals appear cut off
  or stuck behind the header.
- Real dialog semantics: `aria-modal`, labelled by the headline, Esc to close,
  focus trapped inside while open and returned to the originating card on
  close, scroll lock that compensates for the scrollbar so the page doesn't
  shift.
- ‹ › buttons and ←/→ keys move between case studies without closing.
- Per-card two-tone accent gradient, initials avatar fallback, automatic
  font-size step-down for long values like `3× → 5.6× ROAS`.
- Optional pieces are truly optional: missing video, quote, CTA or section body
  render nothing instead of an empty black iframe or a dangling heading.
- `#case=<id>` deep links open a specific case study on page load.
- All selectors namespaced `cs-*`, design tokens in one CSS variable block, JS
  wrapped in an IIFE with no globals.
