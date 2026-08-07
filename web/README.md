# Case study cards + modal (GoHighLevel embed)

`ghl-case-study-cards.html` is a single self-contained block — HTML, CSS and JS
in one file, no build step, no external dependencies. It renders two states:
the card as it sits in the grid, and the full case study that opens when the
card is clicked.

Currently loaded with twelve cards:

1. **Ronnie**, laid off at Accenture to a $90K fully-remote job in 30 days.
2. **Thomas J.**, "just trust me" to a six-figure offer in 3 months.
3. **Jose M.**, 15 years in sales to Senior Business Analyst, offered in 4 days.
4. **Will K.**, 100s of rejections to an offer off a single LinkedIn message.
5. **Hakeem L.**, sales to Senior Analytics Consultant at phData, built in
   public.
6. **LaRita W.**, laid-off teacher to Sr. People Analyst at Roku, 5 offers.
7. **Caitlin U.**, math teacher to finance analyst without ever applying.
8. **Tanya C.**, beginner to a $20K internal promotion in 4 months.
9. **Elleni T.**, accounting to government data analyst at the DC OCFO in
   5 months.
10. **Robby**, experienced analyst stuck at a 1 to 2 percent response rate to an
    offer.
11. **Amanda L.**, teacher to academic research analyst, staying inside
    education.
12. **Jacinda L.**, CDL A truck driver to a Data Analyst profile in 90 days.

## Install in GHL

1. Funnel/page builder → add an **element** → **Custom Code** (in some
   accounts it's called *Code*). Put it in a full-width section/row.
2. Paste the entire contents of `ghl-case-study-cards.html` into the code box.
3. Save, then **preview the live page** — the builder canvas often refuses to
   run `<script>`, so the card can look missing inside the editor while working
   perfectly on the published page.

If your account's code element strips `<script>`, put the `<style>` + HTML in
the code element and paste the `<script>` block into
**Settings → Tracking Code → Footer** instead. Nothing else changes.

## Adding the next student

Everything renders from the `CASE_STUDIES` array near the top of the `<script>`.
Card and full case study come from the same object, so they can't drift apart.
Copy the Ronnie block, change the values, give it a new `id`. The comment block
at the top of the file documents every field.

The layout adjusts to the count on its own, no CSS edits:

| Cards | Desktop | Tablet | Phone |
|---|---|---|---|
| 1 | centered, 400px | centered | full width |
| 2 | centered pair | 2 columns | 1 column |
| 3+ | 3 columns | 2 columns | 1 column |

Rows are 3 across. At the current 12 cards all 4 rows are full.

The modal's ‹ › arrows and arrow-key navigation appear automatically once there
is more than one card.

## Still TODO

- `avatar` on all twelve cards — photo URLs from the GHL media library. Empty
  falls back to the person's initials in a blue ring.
- `modal.cta.href` — `#book` on all twelve, needs the real booking link.
- `images[].src` uploads: Jose's two Slack screenshots, Hakeem's LinkedIn
  profile screenshot, LaRita's LinkedIn profile screenshot. An entry with an
  empty `src` is skipped, so nothing broken renders until they are uploaded.
- Jose's employer, and Thomas's job title, employer, and actual salary figure.
  None are in their transcripts, so none were invented.
- Jose's positioning-statement writeup, flagged in a code comment: it needs to
  read as DIM IP rather than as a feature bullet.
- `wistia` for Hakeem, LaRita, Caitlin, Tanya, Elleni, Robby, Amanda, and
  Jacinda, if there are clips. Wired: Ronnie `e2jdcz4o5w`, Thomas
  `ukjdvqw75m`, Jose `udpai65364`, Will `5qmf872wnj`.
- Hakeem, Tanya, Elleni, Amanda, and Jacinda have no pull quote in their source
  copy, so their modals have no quote block.
- Amanda's LinkedIn profile screenshot, if you want proof of the headline and
  Featured section the write-up describes. Same for Jacinda's profile, where a
  before and after of the FedEx bullet would carry the whole point.
- Jacinda's location: the copy has her in Troy, Alabama and driving out of
  Brooklyn. Both are kept as written, flagged in a code comment.
- `accent` / `accent2` — all set to DIM blue `#0038FF` and coral `#FF6240`,
  which together draw the top bar gradient. Vary per card if you want them to
  read differently.

## Fields a case study can use

Card: `id`, `name`, `category`, `avatar`, `accent`, `accent2`, `stat`,
`statLabel` (optional), `summary`.

Modal: `name` and `category` (optional overrides), `headline`, `subhead`
(optional), `stats`, `quote` (above the write-up), `closingQuote` (below it),
`images` (proof screenshots, above the video), `wistia` (media ID) or `video`
(embed URL), `sections`, `cta`, `disclaimer`. Anything omitted renders nothing.

Modal order: headline, subhead, stat tiles, opening quote, write-up, closing
quote, proof images, video, CTA, disclaimer.

## Brand

Font is Inter, loaded from the same Google Fonts URL the site itself requests
(`wght@300..900`), so it resolves from cache. `--cs-font` at the top of the
stylesheet overrides it.

Palette is lifted from datacareerblueprint.com's own CSS variables:

| Token | Value | Role |
|---|---|---|
| `--cs-blue` | `#0038FF` | primary, CTA button |
| `--cs-blue-lift` | `#4D7BFF` | blue that stays legible as text on navy |
| `--cs-coral` | `#FF6240` | section labels, "Full case study" link |
| `--cs-card-bg` / `--cs-card-bg-2` | `#0D1336` / `#0A0E29` | card gradient |
| `--cs-modal-bg` | `#080C26` | dialog surface |
| `--cs-tile-bg` | `#131A3C` | stat tiles, quote block |
| `--cs-text` / `--cs-body` / `--cs-muted` | `#F6F6FF` / `#C9D8E0` / `#8893A8` | type |

The page background is `#000321`, so every surface sits just above it. The big
card number is `color-mix(--cs-a 58%, white)` because raw `#0038FF` is too dark
to read as text on navy; the same lift is applied to the quote rules. Restyle
the whole block by editing that one token list.

## Copy conventions baked in

- **No em dashes anywhere.** Verified zero in the file, including the code
  comments.
- **Numerals, not words**: 30 days, not thirty days. 8 to 10, not eight to ten.
  Applied inside quotes too, where a spoken number becomes a numeral.
- `statLabel` is optional; omit it and the headline gets its own spacing before
  the summary.
- A `( ... )` parenthetical inside a card headline renders smaller and lighter
  than the claim itself, so qualifiers can sit in the headline without
  competing with it.
- The big card line uses a real arrow (`\u2192` in the data) rather than "to",
  e.g. `Laid Off \u2192 $90K Fully-Remote Job in 30 Days`. Font size steps down
  in 3 tiers as the line gets longer, so long headlines stay to 2 lines. The quote attribution renders as a plain line with no leading dash,
  and the only place an em dash could have appeared (an unused headline
  fallback) now uses a colon.
- Section headings render uppercase from sentence case in the data, so write
  `"Their path before DIM"` and the page shows `THEIR PATH BEFORE DIM`.
- Short quotes inside body copy use `<p class="cs-pull">` for the indented
  italic treatment. Use `&ldquo;` `&rdquo;` `&rsquo;` for curly punctuation.
- `modal.disclaimer` renders the small grey results disclaimer under the CTA.

## Preview locally

Open `ghl-case-study-cards.html` directly in a browser — it renders standalone.
For the dark page background, wrap it in a scratch file with
`body{background:#0d0c0f}`.

## Implementation notes

- One data object drives card + modal, so numbers can't disagree between them.
- The modal is relocated to `<body>` at runtime. GHL sections routinely use
  `overflow:hidden` and CSS transforms, which clip or trap a `position:fixed`
  modal — the most common reason DIY GHL modals appear cut off or stuck behind
  the header.
- Real dialog semantics: `aria-modal`, labelled by the headline, Esc to close,
  focus trapped while open and returned to the card on close, scroll lock that
  compensates for scrollbar width so the page doesn't shift.
- Optional pieces are truly optional: missing video, quote, CTA, disclaimer or
  section body renders nothing rather than an empty box or dangling heading.
- Long card headlines step down in two tiers so text values like
  "Laid Off to $90K Remote" stay on one line.
- `#case=ronnie` deep links open the case study on page load.
- Selectors namespaced `cs-*`, design tokens in one CSS variable block, JS in
  an IIFE with no globals.
