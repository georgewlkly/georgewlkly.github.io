# georgewalkley.com — Design Specification

**Version 1.0 · 17 July 2026 · Approved wireframes v3 (homepage), v1 (book page, archive, post, endorsement pattern)**

This document is the design brief for the redevelopment of www.georgewalkley.com. It records the decisions taken during the design conversation and is intended to be read alongside `implementation-plan.md`, which sequences the build for Claude Code. Where this document says "must", the requirement is fixed; where it says "should" or "default", the implementer may propose alternatives with reasons.

---

## 1. Purpose and goals

The site is the public front-of-house for George Walkley / Outside Context Ltd: consultant, trainer and speaker on AI in media and publishing; author of *The Intelligence Multiplier* (Practical Inspiration Publishing, December 2026); writer of *Context Window*, a weekly newsletter.

Conversion priority, in order:

1. Newsletter signups (*Context Window*, via Kit)
2. Book pre-orders and, from December 2026, sales
3. Speaking bookings
4. Consulting and training enquiries

The redesign replaces a reverse-chronological blog homepage with a curated editorial front page, and modernises the visual treatment throughout, while preserving the entire archive.

## 2. Hard constraints

- **Jekyll is retained.** Current structure, plugins and analytics carry over unchanged unless listed in §9 (housekeeping).
- **Every existing URL must continue to resolve** — posts, tag pages, year pages, landing pages, feed, sitemap. No slugs change. Where a page's role changes (the homepage), the old content moves rather than disappears: the blog roll's job passes to `/posts/` ("All writing"), whose existing pagination URLs are retained.
- **Hosting remains GitHub Pages.** Moving the build to a GitHub Actions workflow (to unlock Jekyll 4.x) is permitted and recommended but not required; hosting and URLs are unaffected either way.
- **Light mode only.** No dark-mode toggle and no `prefers-color-scheme` variants. (The footer is dark by design; that is a design element, not a mode.)

## 3. Design direction

**"Editorial modern":** the typographic seriousness of a well-set literary journal combined with the spacing, scale and curation of a contemporary studio site. It should read as "publisher who understands technology". Coherence with George's existing slide template (Playfair Display Medium titles, Helvetica Neue Light body) is deliberate and extends the same identity across site, decks and book.

**A note on distinctiveness for the implementer.** Warm-cream backgrounds with a high-contrast serif display are currently a common AI-generated-design cluster. This direction was chosen from the brief, not as a default, and the elements that keep it distinctive must be executed precisely rather than drifted toward generic equivalents: the specific paper tone (§4.1, not a generic `#FAF5EE`), the oxblood accent (not terracotta/clay, and never `#D97757`), the near-black full-width footer, top-ruled writing cards, and the letterspaced kicker convention. Do not introduce gradients, drop shadows, rounded-pill buttons, emoji, or decorative icons anywhere.

## 4. Design tokens

Implement as CSS custom properties in a single tokens layer (e.g. `_sass/_tokens.scss` or `:root` block), consumed everywhere else. No raw hex values outside the tokens file.

### 4.1 Colour

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#FBF9F4` | Page background |
| `--paper-tint` | `#F1EDE2` | Tinted bands (book band, endorsements) |
| `--card` | `#FFFFFF` | Card surfaces (services, signup cards) |
| `--ink` | `#1C1B18` | Headings, primary text, dark footer background, card top-rules |
| `--body` | `#2A2822` | Long-form body text |
| `--text-2` | `#4A473F` | Supporting text, card summaries |
| `--muted` | `#6B675F` | Metadata, nav links, captions |
| `--rule` | `#E4E0D6` | Hairline borders and dividers on paper |
| `--rule-tint` | `#DDD7C8` | Hairline borders on tinted bands; image placeholders |
| `--border-mid` | `#C9C4B6` | Secondary button borders, cover frame |
| `--accent` | `#8C3226` | Oxblood: links, primary buttons, kickers, active nav item |
| `--accent-underline` | `#D8B3AC` | Link underline tint in body text |
| `--footer-text` | `#B8B3A6` | Footer column headings and emphasised footer text |
| `--footer-muted` | `#7C786D` | Footer body text |
| `--footer-rule` | `#33322D` | Footer dividers |
| `--footer-field` | `#2A2925` / border `#45443E` | Footer email input |

The accent is the **only** saturated colour on the site. It is used for interactive or signalling elements exclusively (links, buttons, kickers, active nav, filter states) — never as decoration or large fills outside buttons.

### 4.2 Typography

**Headings and display:** Playfair Display, weight 500 (Medium) as default, 600 for the masthead wordmark only, italic 500 for quotations. Load via Google Fonts (`wght@500;600` plus italic 500) with `font-display: swap` and a `serif` fallback.

**Body and UI:** Helvetica Neue system stack — no webfont:
`"Helvetica Neue", Helvetica, Arial, sans-serif`
Accepted consequence: Windows renders Arial. Do not add Inter or any substitute webfont without explicit approval.

**Scale (desktop reference; use `clamp()` for fluid sizing down to mobile):**

| Role | Face | Size | Weight | Notes |
|---|---|---|---|---|
| Hero statement | Playfair | 40–44px | 500 | line-height ≈1.25 |
| Page title (archive, static) | Playfair | 34px | 500 | |
| Post headline | Playfair | 36–38px | 500 | line-height ≈1.2 |
| Section heading | Playfair | 24px | 500 | e.g. "Recent writing", "Inside the book" |
| Card title | Playfair | 20px | 500 | |
| Book band title | Playfair | 30px | 500 | |
| Lead endorsement | Playfair italic | 26px | 500 | |
| Grid endorsement / blockquote | Playfair italic | 18px | 500 | |
| Body (posts) | Helvetica Neue | 18px | 400 | line-height 1.75, measure 65–70ch |
| Supporting text | Helvetica Neue | 15–16px | 400 | line-height ≈1.65 |
| Card summary | Helvetica Neue | 15px | 400 | |
| Metadata / kicker | Helvetica Neue | 13px | 400 | kickers uppercase, letter-spacing 0.08em |
| Nav | Helvetica Neue | 14px | 400 | letter-spacing 0.02em |
| Footer body | Helvetica Neue | 13px | 400 | line-height ≈1.7 |

Sentence case throughout. Uppercase is reserved for kickers only.

### 4.3 Spacing, radii, rules

- Spacing rhythm in rem: section padding 3–3.5rem vertical on desktop, 2rem mobile; internal card padding 1.25–1.5rem.
- Content max-width: ~1080px page container; ~68ch for post body.
- Border radius: **3px** buttons and form fields, **4px** cards and portrait, **2px** book cover, **12px** filter pills (pill shape). Nothing larger.
- Rules are 1px solid (`--rule` on paper, `--footer-rule` in the footer). Writing cards use a **2px top rule in `--ink`** — this is a signature element; keep it.

## 5. Components

**Primary button.** Filled `--accent`, text `--paper`, 3px radius, padding ≈10px 18px, 14px text. Hover: darken ~8%. At most one primary button visible per viewport-height of content.

**Secondary button.** 1px `--border-mid` outline on transparent, `--ink` text, same geometry. Used for retailer buttons other than the featured one.

**Text link.** `--accent`, underlined with `--accent-underline` in body prose; no underline in nav/metadata contexts, where colour alone signals.

**Kicker.** 13px uppercase letterspaced `--accent`, e.g. `NEW BOOK · DECEMBER 2026 · PRACTICAL INSPIRATION`. Middle-dot separators.

**Writing card.** 2px `--ink` top rule; metadata line (date · category label); Playfair title; one-line summary in `--text-2`. Whole card is the link target.

**Service card.** White card, 1px `--rule` border, 4px radius; Playfair title, short sans description. Links to landing page.

**Filter pill.** 12px-radius pill; active = filled `--ink` with `--paper` text; inactive = 1px `--border-mid` outline.

**Quotation treatment.** Playfair italic. In posts: blockquote with 1px left rule. On the book page: endorsement pattern (§6.3). One quotation voice site-wide.

**Signup form (Kit).** Email field + primary button. Instances: footer band (all pages), end-of-post card, book-page launch card, `/newsletter/` page. All post to the same Kit form endpoint unless a separate form ID is wanted for source attribution (recommended — one Kit form or tag per placement so conversion by placement is measurable). Style Kit's markup to tokens; do not use Kit's hosted CSS.

**Masthead.** Left: "George Walkley" wordmark, Playfair 600. Right: About · Book · Writing · Speaking · Training · Consulting · Newsletter. Current page (or section) in `--accent`; "Newsletter" is additionally accent-coloured at rest as a standing pointer. 1px bottom rule. On mobile: wordmark plus a plain accessible disclosure menu (no hamburger icon library; a text "Menu" button is acceptable).

**Footer (all pages).** Dark band, `--ink` background:
1. Signup row: "Context Window" (Playfair), one-line description with subscriber count ("read by 1,900+ subscribers" — count updatable in config), email field + Subscribe button. 1px `--footer-rule` divider beneath.
2. Four columns: **Impressum** (© line, company registration, VAT, registered address), **Contact** (email, phone), **Links** (LinkedIn, Bluesky, RSS, Privacy, Sitemap), **Writing** (total words and total weeks, e.g. "91,035 words / 84 weeks" — both computed at build from the post collection; the client-side streak script is retired). Columns stack on mobile.

## 6. Templates

Four templates plus shared includes (masthead, footer, signup card).

### 6.1 Homepage (`/`)

Order: masthead → hero → book band → recent writing → services → footer.

**Hero.** Two columns: statement left, portrait right. Statement: Playfair, "Helping publishers and media businesses put AI to work — strategically, practically, and on their own terms." (copy may be refined before launch). Supporting line: "Consultant, trainer and speaker. Author of *The Intelligence Multiplier*. Writer of *Context Window*, a weekly briefing on AI in media and publishing." **No button in the hero** — deliberate; conversion is carried by the nav pointer, the footer band and end-of-post cards. Revisit only if newsletter growth stalls post-launch. Portrait: warm-graded environmental/speaking photograph, ~3:3.6 ratio, 4px radius; stacks above the statement on mobile.

**Book band.** Full-width `--paper-tint` band, 1px rules top and bottom. Cover left; kicker `NEW BOOK · DECEMBER 2026 · PRACTICAL INSPIRATION`; title; one-to-two-line pitch; "Pre-order →" text link. Post-launch the kicker becomes `OUT NOW · PRACTICAL INSPIRATION` via config.

**Recent writing.** Section heading + "All writing →". Three writing cards. Population: the three most recent posts by default, with an optional `featured: true` front-matter flag that pins a post into the set (newest featured first, backfilled by recency). Card labels use the coarse category (§7), not tags.

**Services.** Three service cards: Speaking / Training / Consulting, each one line, linking to the existing landing pages.

### 6.2 Static landing template (About, Consulting, Speaking, Training, Newsletter)

Shared skeleton: masthead → Playfair page statement → prose block(s) → credibility strip (tinted band) → contact or signup call to action → footer. Fills per page:

- **Consulting:** offer description; engagement types; credibility strip (selected clients or engagement categories); contact CTA.
- **Speaking:** talk themes; recent venues/engagements; contact CTA.
- **Training:** CPD accreditation and "300+ organisations" in the credibility strip; formats; contact CTA.
- **Newsletter:** description; subscriber count; links to recent issues; full-size signup form as the primary element.
- **About:** biography; portrait; roles.

### 6.3 Book page (`/books/the-intelligence-multiplier/`)

masthead → book hero → endorsements → launch-updates card → footer.

**Book hero.** Cover left (larger than homepage band). Kicker as homepage. Title, then the longest pitch on the site (two–three sentences), then a short "inside the book" prose paragraph or contents link — this content is deliberately demoted below endorsements in prominence. Retailer buttons: featured retailer as primary button ("Pre-order — Publisher" or preferred channel), others (Amazon, Bookshop.org, Waterstones, etc.) as secondary buttons; wraps on mobile. Retailer list and URLs live in front matter or a data file.

**Endorsements.** `--paper-tint` band. One **lead** endorsement full-width at 26px Playfair italic with attribution, divider rule, then a responsive two-column grid of further quotes at 18px. Source: `_data/endorsements.yml`, each entry `quote`, `name`, `role`, `org`, optional `lead: true` (exactly one). The grid must handle 2–8 entries without template change.

**Launch-updates card.** White card: "Get launch updates" / "Publication news, events and a sample chapter, via Context Window." + signup form (dedicated Kit tag for book-driven subscribers recommended).

Housekeeping: the current redirect behaviour on this URL must be diagnosed and fixed (§9).

### 6.4 Writing archive (`/posts/`, tag pages, year pages)

Two columns: list left, sidebar right (sidebar below list on mobile).

**List.** Page title "Writing". Filter pills: All / Newsletter / Posts, driven by the category field. Entries are compact — metadata line (date · category), Playfair title, one-line summary (from `description` front matter, else truncated excerpt) — separated by 1px rules. No full excerpts. Existing pagination retained ("Older →" / "← Newer").

**Sidebar.** Topics: **all** tags, untruncated, with counts. Years: **all** years, untruncated, with counts. Set at 13px with tightened leading so the full lists sit comfortably. (The "Writing" tag currently has a zero count and is **retained deliberately** — George intends to populate it. It must keep its sidebar entry and its `/tags/writing/` page. Superseded 17 July 2026; v1.0 had called for it to be removed or suppressed.)

**Tag and year pages** reuse this template with the heading swapped ("Writing: Strategy", "Writing: 2025") at their existing URLs.

### 6.5 Post template

**Single column. No sidebar.** Centred measure of 65–70ch.

Order: metadata line (date · category label · reading time, computed at build) → Playfair headline → body → tag links ("Tagged: …" above a 1px rule) → prev/next → signup card → footer.

Body typography: 18px/1.75 sans; Playfair 500 subheadings; blockquotes per §5; links underlined with `--accent-underline`; images full column width, 4px radius, optional small-caption style in `--muted`.

**Prev/next** navigate **within the post's category** (newsletter readers page through newsletter issues; posts through posts), falling back to global order if the category has no neighbour.

**Signup card.** White card above the footer. Copy is conditional:
- `category: newsletter` → "Enjoyed this? It started life in Context Window." + one-line description.
- otherwise → neutral default, e.g. "I write about AI in media and publishing every week." + description.
Both strings live in `_config.yml` or a data file; the provenance line must never appear on non-newsletter posts.

## 7. Content model

**Category (new front matter field).** Every post gains `category:` with values `newsletter` or `post`. Display labels are config constants: `newsletter → "Newsletter"`, `post → "Posts"` (plural, for pills) / `"Post"` (singular, metadata line). Note: "Articles/Article" was flagged as an alternative label pair and can be swapped in config at any time. Tags are unchanged and remain the granular taxonomy; category is coarse and for display/filtering only. A migration pass over existing posts is required (implementation plan, stage 7) — proposed values reviewed as a diff before committing.

**Featured flag.** Optional `featured: true` pins a post into the homepage writing cards.

**Description.** Optional `description:` front matter provides the one-line summary for cards and archive entries; fall back to a truncated excerpt.

**Endorsements.** `_data/endorsements.yml` per §6.3.

**Config strings.** Subscriber count, signup copy variants, book kicker state (`new-book` / `out-now`), retailer list, category labels.

## 8. Responsive and accessibility floor

- Breakpoints at implementer's discretion; every template must work from 360px width up. Hero, book band and footer columns stack; nav collapses to a disclosure menu.
- Remove `maximum-scale=1.0` from the viewport meta — pinch-zoom must work.
- Visible keyboard focus styles on all interactive elements (2px `--accent` outline offset 2px, or equivalent).
- Semantic landmarks (`header`, `nav`, `main`, `footer`); skip-to-content link; single `h1` per page; alt text on portrait and cover.
- Colour contrast: all token pairings above meet WCAG AA at their specified sizes; verify `--muted` on `--paper` (4.6:1) is only used at 13px+ and `--footer-muted` on `--ink` for footer body only.
- No motion is required by this design; if any transitions are added (hover states), respect `prefers-reduced-motion`.

## 9. Housekeeping (in scope)

1. `og:locale` → `en_GB`.
2. Viewport meta: remove `maximum-scale=1.0`.
3. Diagnose and fix the redirect behaviour on `/books/the-intelligence-multiplier/`.
4. Retire the client-side writing-streak script; words and weeks computed at build (§5 footer).
5. Recommended: move the build to a GitHub Actions workflow with Jekyll 4.x (hosting and URLs unchanged). If done, verify plugin compatibility before merging.
6. Refresh `og-default.png` to the new visual identity once the design is live (deferred, low priority).

## 10. Open items (owner: George)

- Final hero statement copy and supporting line.
- Portrait selection and grade; book cover asset.
- Retailer list and pre-order URLs; featured retailer choice.
- Endorsement copy as it arrives; choice of lead quote.
- Confirm "Posts" vs "Articles" label (config constant; default "Posts").
- Kit form/tag IDs per placement.
- Subscriber count wording and update cadence.
