---
status: working
attribution: llm-synthesis
updated: 2026-09-15
sources:
  - SRC-2026-09-14-typographic-voice
  - SRC-2026-09-14-design-principles-draft
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-05-price-formation-market-model
---

# Design and Typographic Application

How LONGING applies the institution's typographic rule and reads the unconfirmed institutional design draft against its own surfaces. The shared rule is owned by TENDER SYSTEMS; only the local reading below belongs to this repository.

## What is inherited, and what is proposed here

**Inherited and user-confirmed (institutional).** Typeface identifies the speaker. The user stated it directly, in their own words:

> "누가 말하고 있는가에 따라 서체가 달라지는 것이 중요한것 같아.
> 시스템이 만들어내고 말하는 글꼴과 사람이 쓴글을 달라야해."

| Speaker | Typeface | Where it appears |
|---|---|---|
| The system | Inconsolata | Prices, dates, codes, status values, metadata, general interface text, system-generated sentences |
| The machine, more directly | Departure Mono | Terminals, dashboards, monitoring surfaces, logs, live status |
| A person | Source Serif | Reports, essays, interpretation, commentary — long text a human wrote |

Inconsolata is the base voice. Departure Mono was considered as a replacement for it and deliberately was not adopted as one; it carries the narrower role above. The canonical record is institutional: [DEC-006 — Typeface Identifies the Speaker](https://github.com/TENDER-SYSTEMS-LAB/tender-systems/blob/main/wiki/decisions/DEC-006-typographic-voice.md).

**Unconfirmed at institutional level.** The ten TENDER SYSTEMS design principles, the three-layer scheme (institutional principles → per-work principles → implementation guide), and the conflict ordering are draft v0.1 in [Design Principles](https://github.com/TENDER-SYSTEMS-LAB/tender-systems/blob/main/wiki/concepts/design-principles.md). The user asked for an abstract layer that each work specialises; the draft answering that request ends with no user reply. What the user originated is the *layering intent*, not the ten principles.

**Proposed here (`llm-proposed`).** Every surface assignment, counter-example, and question below is this repository's reading, produced on 2026-09-15 by comparing the institutional sources against LONGING's existing pages. None of it is a user decision, and the request to ingest the institutional material did not ratify it.

## What the rule does not say

- **Length and hierarchy do not identify a speaker.** A heading, a caption, and a paragraph do not automatically differ. A machine reading, a system record, and a human interpretation do.
- **Prose is not proof of a person.** A long report set in Source Serif is not thereby human-written. In LONGING, *every* word on the surface is authored fiction, and several of the longest documents in the work are explicitly system output. The typeface marks who is speaking **inside the fiction**; it certifies nothing about who actually wrote the bytes.
- **Departure Mono is not a theme.** It marks a surface that is behaving mechanically right now. It is not permission to render the whole research house as a retro terminal — which is also what [[DEC-002-research-house-form]] already says about the Bloomberg reference: borrow the attitude, not the palette.
- **The works need not look alike.** Draft principle 8 proposes consistency of reasoning rather than uniform appearance; LONGING's density is its own, and a difference from OTHER GOODS or THE RESERVE is legitimate when it follows from role.

## Speaker classification on LONGING surfaces

`llm-proposed`. Project facts cited are existing repository material; the assignment of each to a voice is new.

| LONGING surface | Speaker | Proposed typeface | Existing evidence |
|---|---|---|---|
| Index and sub-index levels, price and change lines, the Fundamental Value / Market Price pair | The system | Inconsolata | [[index-architecture]], [[pricing-model]] |
| Ratings, target prices, conviction figures, consensus and rating distribution, high/low spread | The system | Inconsolata | [[analyst-system]] |
| `Position recorded.`, the viewer's accumulated positions list, aggregate participation percentages | The system | Inconsolata | [[DEC-002-research-house-form]], [[analyst-system]] |
| `NO COVERAGE`, coverage initiation and coverage drop notices, `UNCLASSIFIED` codings | The system | Inconsolata | [[analyst-system]], [[letter-practice-dynamics]] |
| Weekly attribution-ledger lines, including the `Unexplained` residual | The system | Inconsolata | [[attribution-ledger]] |
| Market terminal header, status and last-update lines, weekly strike state, listing-state logs | The machine | Departure Mono | [[DEC-002-research-house-form]], [[DEC-003-weekly-market-monthly-research]] |
| Monthly research bodies — argument, thesis, risk discussion, rebuttal prose | A person (in the fiction) | Source Serif | [[analyst-system]] |

### Worked examples, and the three that break the easy reading

**A price line is the system talking.** `LETTER 31.82 ▲8.4%` is a published number with no argument attached. So is a whole page of them. Under [[DEC-002-research-house-form]] the institution *publishes a number and does not explain it* — the explanation is the analysts' job. Number in Inconsolata, argument in Source Serif, and the page shows the division without captioning it.

**A report body is a person talking.** Eleanor Vale's *"The market continues to price waiting exclusively as a cost. We disagree."* and Adrian Kessler's *"Sentimental attachment should not be confused with intrinsic value."* are interpretation, argued by a named analyst who exists in the fiction as a person. Source Serif. Mina Seo's HOLD note on LETTER is the same case.

**But: a report by a person is not automatically a human voice.** Julian Hart's quantitative output is described in [[analyst-system]] as *almost no prose* — signal, momentum, usage, scarcity, sentiment, replacement risk, a model output, a twelve-month target, a confidence figure. The named analyst is the publisher; the speaker is his model. That output stays in the system voice, and the joke the page already makes — that the least human-sounding desk may be the most accurate long-range judge of romance — survives the typography instead of being erased by it.

**But: a note filed under an analyst is not automatically their writing.** The flash notes between coverage updates — `No rating change. Target unchanged.` — are system records of an absence of new judgment. Inconsolata. If a flash note grows into four lines of revised reasoning, it has changed speaker, and the typeface should change with it rather than with the file it is stored in.

**But: one document holds more than one speaker.** A report is a system-issued header (`LN-001 / ANALYST REPORT 024`, date, rating, target), a human body, and a system-issued data block (current price, 30-day change, position). Three voices in one page is the intended behaviour of the rule, not a failure of it. The institutional source shows exactly this layout.

### Cases deliberately left open

- **Event-detector headlines.** [[current-state]] requires an event detector to supply information between monthly reports. Whether an event arrives as a system record (Inconsolata) or as a report written by a fictional journalist (Source Serif) depends on a news-authorship model that does not exist: [[information-quality]] states that misreporting, over- and under-reporting, and pre-disclosure leakage have no representation anywhere in the corpus. Until a speaker is decided for the event layer, treat headlines as system output and leave the question recorded rather than answered.
- **LETTER.** LETTER is classified exactly like any other security here — a price line is system voice, a report about it is its author's voice. Nothing on this page adds, implies, or fixes any LETTER behaviour; the practice trial in [[letter-practice-dynamics]] and the unit branches in [[Q-004-unit-of-account]] remain unadopted and open.
- **Korean text.** 사유 and the other internally defined Korean terms have no assigned typeface, because the institution has not chosen a Korean auxiliary face at all. The one early suggestion on record belongs to a superseded typeface direction. Do not assume Korean will be set in any of the three faces.

## What this page does not decide

Weights, sizes, spacing, line length, palette, screen layout, per-work density, the "Source Serif 4" version, and licensing all remain unresolved upstream and are not settled here. The claim in the source that Departure Mono renders cleanly at multiples of 11px is the source assistant's report of a third-party guide; it was not verified, and it is a reason to *ask* whether Departure Mono suits LONGING's dense tables, not a specification. No font was obtained, installed, licensed, or rendered in this ingestion, and no product code was touched.

A theoretical limit is never a licence for a broken screen. Draft principle 3 distinguishes a system's inherent limit from a flawed implementation, and draft principle 5 distinguishes open interpretation from missing information: if the viewer cannot tell what their position did, that is a defect, not ambiguity in the work's favour.

## Local design questions

`llm-proposed`, derived from draft v0.1 against LONGING's existing design. None is answered here.

1. **Does a weekly market have a live surface at all?** Departure Mono marks monitoring and live status, but [[DEC-003-weekly-market-monthly-research]] rejected real-time pricing precisely because it would require fabricated volume and a fabricated order book. What is genuinely live in LONGING — the strike moment, the event feed, nothing?
2. **Which speaker owns an event?** See above. The answer decides whether the event layer is a record or a report, and it interacts with the unmodelled news-quality layer.
3. **How is the Fundamental Value / Market Price gap shown without claiming to have captured its subject?** Draft principle 3 warns against the system's assigned value standing in for the thing named. The gap is [[pricing-model]]'s most informative output and also its largest claim.
4. **What does the terminal register promise?** Draft principle 6 warns against institutional appearance implying authority that does not exist. LONGING publishes prices, targets, and positions for human experiences; the work is fiction and offers no financial claim, product, or advice. Where does that boundary need to be legible on the surface?
5. **Where does density stop being information?** Draft principle 7 permits dense screens and forbids decorative procedure. The research terminal is deliberately dense with no onboarding; the test is whether a given column earns its place or only looks institutional.
6. **Does the unresolved Korean face block anything here?** The internal definitions are Korean, the artwork's surface language is undecided, and no Korean typeface exists in the rule. This is an institutional gap that LONGING should raise rather than solve locally.

## Related

- [[DEC-002-research-house-form]]
- [[DEC-003-weekly-market-monthly-research]]
- [[analyst-system]]
- [[attribution-ledger]]
- [[index-architecture]]
- [[information-quality]]
- [[system-grammar]]
- [[Q-004-unit-of-account]]
- [[current-state]]

## Sources

- [[SRC-2026-09-14-typographic-voice]] — [raw/conversations/2026-09-14-typographic-voice.md](../../raw/conversations/2026-09-14-typographic-voice.md); derivative import of the institutional original, byte-identical and registered under the same source ID. The user's acceptances are quoted from their own messages; candidate comparisons, the density table, the English formulation, and all glyph and licensing claims are the source assistant's unverified proposals
- [[SRC-2026-09-14-design-principles-draft]] — [raw/conversations/2026-09-14-design-principles-draft.md](../../raw/conversations/2026-09-14-design-principles-draft.md); derivative import, byte-identical. Only the request for an abstract layer is the user's; the ten principles, the three-layer table, and the conflict ordering are an unanswered draft
- [[SRC-2026-09-04-longing-concept-brainstorm]] — [raw/conversations/2026-09-04-longing-concept-brainstorm.md](../../raw/conversations/2026-09-04-longing-concept-brainstorm.md)
- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md)
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md)

Both 2026-09-14 sources are external ChatGPT sessions with no access to this repository. Their LONGING examples — including the sample terminal, ledger, and report layouts — are that assistant's inventions and are used here as illustrations of the rule, never as evidence about LONGING's design.
