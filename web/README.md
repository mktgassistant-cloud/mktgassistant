# GoHighLevel embed blocks

Two independent paste-into-GHL blocks live here:

- `ghl-case-study-cards.html`, the student case study grid and modals.
- `ghl-cards-first-6.html`, the same engine with a mount for cards 1 to 6
  already in it, so it drops into one GHL element and renders those 6 on the
  spot. Use this OR `ghl-case-study-cards.html`, never both, and add
  mount-only lines for every other placement.
- `ghl-cards-next-9.html`, the same idea for cards 7 to 15. Only for a
  DIFFERENT page from the first 6, since it carries its own copy of the
  engine. On the same page, use a mount line instead.
- `ghl-clarity-call-checklist.html`, the "On this call we'll:" checklist.
  Pure HTML and CSS, no JavaScript, so it renders inside the builder canvas
  straight away. Edit the `<li>` lines and nothing else. Add `is-light` to the
  wrapper for a white section; `--cc-check` recolors the ticks.

# Case study cards + modal

`ghl-case-study-cards.html` is a single self-contained block — HTML, CSS and JS
in one file, no build step, no external dependencies. It renders two states:
the card as it sits in the grid, and the full case study that opens when the
card is clicked.

Currently loaded with fifteen cards, ordered strongest testimonial first. The
order lives in the `CASE_STUDIES` array and nothing else depends on it, so
resequencing is a matter of moving one object.

1. **LaRita W.**, laid-off teacher already self-teaching and still stuck. Exact
   ICP, 5 offers, Roku, student to mentor, complete and verifiable.
2. **Caitlin U.**, zero applications, recruiter found her. Publicly checkable
   profile, post, and reaction counts.
3. **Catherine L.**, 27 days, fastest placement on record, told in her own
   voice throughout.
4. **Jose M.**, dated Slack screenshots proving 4 days from application to
   offer. Hardest evidence on the grid.
5. **Jacinda L.**, truck driver to data analyst in 90 days. Best hook by
   distance travelled. Analyst employer still unverified.
6. **Shantel W.**, no degree to Microsoft. Biggest brand. Held back by the SWE
   mismatch and the consent question.
7. **Ronnie**, the only hard salary figure and a clean 30 days. Wrong ICP caps
   it.
8. **Thomas Y.**, "just trust me" to a six-figure offer in 3 months. Has a
   video and a timeline, but no title, employer, or exact figure. Placement is
   an estimate, not from the ranked list.
9. **Hakeem L.**, externally auditable, clearest demonstration of the challenge
   library. No timeline.
10. **Rachel**, weakest numbers, highest strategic value.
11. **Will K.**, only recent-grad coverage and a complete causal chain, but no
    title, employer, salary, or hard outcome number.
12. **Elleni T.**, strong skills-get-tested angle and an ignored market. Thin
    evidence, no quote.
13. **Amanda L.**, good lesson, no timeline, employer, or salary.
14. **Robby**, weak arrow, and reads as risky next to the beginners.
15. **Tanya C.**, unique strategy, hollow middle.

## Install in GHL

Paste `ghl-case-study-cards.html` **once**, not once per group of cards.
Either a **Custom Code** element at the bottom of the page, or
**Settings → Tracking Code → Footer**.

Then place a mount wherever cards should appear. One line each, as many as
you want:

```html
<div class="cs-mount" data-cs="larita,caitlin,katherine"></div>
<div class="cs-mount" data-cs="jose,jacinda,shantel"></div>
```

`data-cs` is a comma separated list of ids, rendered in the order written.
Omit it and that mount renders all fifteen. Unknown ids are skipped rather
than rendering a blank card. Mounts can sit above or below the block, since
rendering waits for the document and sweeps again on load.

Nothing appears until a mount exists, which is what lets the block live in
the footer without dumping fifteen cards down there.

The modal arrows walk the group you clicked into, not the whole set: a mount
of 3 cycles those 3, and a mount of 1 hides the arrows. Deep links open a
card inside whichever group holds it. Pasting the block twice is harmless,
the second copy stands down rather than fighting over element ids.

If your account's code element strips `<script>`, put the `<style>` + modal
markup in the code element and paste the `<script>` block into
**Settings → Tracking Code → Footer** instead. Nothing else changes.

## Adding the next student

Everything renders from the `CASE_STUDIES` array near the top of the `<script>`.
Card and full case study come from the same object, so they can't drift apart.
Copy any existing block, change the values, give it a new `id`. Position in the
array is position on the page, so insert it where its strength puts it. The comment block
at the top of the file documents every field.

The layout adjusts to the count on its own, no CSS edits:

| Cards | Desktop | Tablet | Phone |
|---|---|---|---|
| 1 | centered, 400px | centered | full width |
| 2 | centered pair | 2 columns | 1 column |
| 3+ | 3 columns | 2 columns | 1 column |

Rows are 3 across. At the current 15 cards all 5 rows are full.

The modal's ‹ › arrows and arrow-key navigation appear automatically once there
is more than one card.

## Still TODO

- `CONFIG.ctaUTM` is `false`. Flip it to `true` to tag each Book a Free Call
  link with `utm_content=<card id>`, so the analytics say which case study
  produced the booking. Check the utm_source / medium / campaign values match
  your taxonomy first.
- Jose's employer is still not stated anywhere, including his own post.
- Thomas's salary figure. "Six figure" is his own wording and nothing
  corroborates a number.
- `images[].src` still empty: Jose's two Slack screenshots, LaRita's and
  Hakeem's LinkedIn profile screenshots. Those are separate artifacts from the
  posts already wired, so their slots stay empty and render nothing.
- Jacinda has no proof screenshot, because none exists. Her LinkedIn work
  history is not updated either, so her "Verify on LinkedIn" link points at a
  profile that does not corroborate the case study. Consider dropping her
  `linkedin` line until it is.
- Jose's positioning-statement writeup, flagged in a code comment: it needs to
  read as DIM IP rather than as a feature bullet.
- `wistia` for LaRita, Caitlin, Shantel, Hakeem, Rachel, Elleni, Amanda and
  Tanya, if clips exist. Wired: LaRita none, Catherine `p6g63rj9rj`, Jose
  `udpai65364`, Ronnie `e2jdcz4o5w`, Thomas `ukjdvqw75m`, Will `5qmf872wnj`,
  Robby `k88ct0murh`. Jacinda uses a Loom through `modal.video`.
- Will has a second Wistia ID, `8y3xgnmmzu`. `5qmf872wnj` is still wired.
  Only one can show.
- Tanya's post announces joining Clario through the WCG eCOA acquisition. It
  does not evidence the $20K promotion her card claims, so it sits under a
  claim it does not support.
- Amanda's write-up reaches for a school district example, but she landed at
  the Institute for Humane Studies, a higher-ed research nonprofit.
- LaRita, Tanya, Elleni, Amanda, Shantel and Jacinda have no pull quote in
  their source copy, so their modals have no quote block.
- `accent` / `accent2` are DIM blue `#0038FF` and coral `#FF6240` on every
  card, which together draw the top bar gradient. Vary per card if you want
  them to read differently.

## Facts the screenshots confirmed

These came out of the LinkedIn assets and are not yet written into any copy.
Titles and employers are now verifiable, so the write-ups can use them:

| Card | Employer | Title |
|---|---|---|
| Catherine L. | Kootenai Health | Healthcare Data Analyst |
| Thomas Y. | HITT Contracting Inc. | Data Analyst, now Data Analyst Manager |
| Rachel | Essentia Health | Business Intelligence Analyst |
| Will K. | USI Insurance Services | Employee Benefits Analyst, Bloomington MN |
| Elleni T. | Office of the Chief Financial Officer | Financial Data Analyst |
| Amanda L. | Institute for Humane Studies | Academic Research Analyst |
| Robby | HUB International | Business Intelligence Analyst, Commercial Lines |
| Caitlin U. | Mustang Cat | CMD Finance Analyst |

Two of these are strong enough to quote directly. Hakeem's post thanks
"Kedeisha Bryan and Data In Motion for the fantastic career consulting and
interview prep" by name, and Roku published its own post about LaRita rather
than her announcing it herself.

## Fields a case study can use

Card: `id`, `name`, `category`, `avatar`, `accent`, `accent2`, `stat`,
`statLabel` (optional), `summary`.

Modal: `name` and `category` (optional overrides), `headline`, `subhead`
(optional), `stats`, `quote` (above the write-up), `closingQuote` (below it),
`images` (proof screenshots, above the video), `wistia` (media ID) or `video`
(embed URL), `sections`, `cta`, `disclaimer`. Anything omitted renders nothing.

`cta` is `{ text }` only. The URL comes from `CONFIG.ctaHref`, currently
`https://datacareerblueprint.com/apply-page`, so changing where the button
goes is one edit rather than fifteen. A card can still override it with its
own `cta.href`.

### Book a Free Call: popup or redirect

`CONFIG.ctaTypeform` holds a Typeform live id. Set (currently
`01KVR57XYKKAFZQRAV9RB47MM8`), the button opens that form as a full screen
popup over the page, with no navigation, so page level tracking keeps
running. Set it to `""` and the button falls back to a plain redirect to
`ctaHref`, which is what a second page wanting different behaviour would do.

Details worth knowing:

- The anchor keeps `ctaHref` as its real `href`, so a middle click still
  opens the apply page in a tab, and if `embed.js` has not loaded the click
  simply follows the link. The button is never dead.
- `embed.js` loads when a case study first opens, not on page load, so it
  costs nothing to visitors who never open a card.
- Opening the form closes the case study first. The Typeform popup is full
  screen, and leaving the dialog open underneath means two scroll locks and
  our focus trap fighting the form's iframe for the keyboard.
- The popup is built once and reused across clicks.

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

- Every card carries `avatar` (the round photo beside the name) and `linkedin`
  (a "Verify on LinkedIn" link under the category line, new tab, noopener).
  Fourteen carry a proof screenshot in `images`.
- Proof screenshots are capped at 440px tall and anchored to the top, because
  LinkedIn screenshots run past 1200px and would bury the video and the CTA.
  What gets cropped is the decorative graphic at the bottom of a post, never
  the author line or the announcement.

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
