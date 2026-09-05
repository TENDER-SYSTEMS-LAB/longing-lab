---
status: working
attribution: jointly-developed
updated: 2026-09-05
sources:
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
---

# Data Sources

Whether LONGING's numbers rest on real-world data, and if so which. The user opened the question directly: *"실제 데이터를 보여주는 방식을 사용해볼까? 예를 들어 Reddit이나 X, Instagram, Threads 등에서 긁어오는거야."* No source has been secured yet; this page records the layering that was agreed, what each candidate is actually good for, and the honesty rules that survived review.

## The distinction that reorders everything

Social platforms measure **what people say**, not what they do. Priced on mention volume alone, `LETTER` would track people who talk about handwritten letters rather than people who write them. So the layers are kept apart and never blended into one score:

| Layer | Measures | Examples |
|---|---|---|
| **BEHAVIOR** | what people actually did | postal volume, call minutes, cinema admissions, film sales |
| **ATTENTION** | what people looked for | Google Trends, Naver search trends, Wikipedia pageviews |
| **DISCOURSE** | what people talked about | Threads, X, Reddit, Instagram |

The ranking that follows is `A` observed behavior (public and institutional statistics), `B` revealed attention (search), `C` expressed interest (social platforms), `D` in-work participation (viewer LONG/HOLD/SHORT). Trust descends down the list, and `D` is kept furthest from price — consistent with the existing rule that participant votes must never be the price ([[analyst-system]]).

Separating the layers is not only methodological hygiene. It produces the paradox the work is about:

```text
LTR — HANDWRITTEN LETTER

BEHAVIOR   Postal correspondence volume   -8.4% YoY
ATTENTION  Search interest               +12.8% YoY
DISCOURSE  Social mentions               +31.4% YoY
           Positive sentiment              78.2%

BEHAVIOR / SENTIMENT GAP                   +42.8
```

People talk about letters more and write fewer of them. The gap between the two is a candidate indicator for the whole work, and it turns Adrian Kessler's line — *consumers romanticize behaviors they no longer practice* — into something the data can confirm or refute rather than assert.

## Candidate sources, as assessed

**Public statistics — the priority.** For `LETTER`, Korea Post publishes monthly letter-post acceptance and delivery volumes, with annual national statistics on KOSIS. Far stronger than counting hashtags. It also carries the naming discipline the work needs: ordinary letter post includes bills and business mail, so the series must be labelled `DOMESTIC LETTER-POST VOLUME` and never `HANDWRITTEN LETTERS SENT`. That dry honesty suits LONGING better than a flattering label would.

**Google Trends — wanted, gated.** Closer to revealed behavior than any survey, because it counts what people typed. The official Trends API was in alpha with access limited to selected testers; an application text was drafted in the conversation describing LONGING as a research-oriented interactive web project studying long-term change in cultural behavior, explicitly distinguishing observed behavior, revealed attention, and public discourse, and disclaiming any individual profiling or ad targeting.

**Threads — the most attractive social source.** Its official API offers keyword search over public posts, and its text-first nature suits exploring the work's concepts in natural language.

**X — best search, worst cost.** Strong operators, seven-day and full-archive search, but pay-per-use pricing makes it a later addition rather than a first one.

**Reddit — qualitative, not quantitative.** People narrate their own experience at length there, which makes it evidence for analyst research rather than an input to a mention count. Unapproved scraping is off the table; the official API's terms and rate limits apply.

**Instagram — visual archive only.** The official API is built around professional accounts and hashtag-scoped media, not open collection. Cultural visibility signal, yes; price input, no.

## The rule the reviews added

Two reviews of the pricing model raise the same hazard from opposite ends: never fabricate a statistic that looks like a measurement, and never present a constructed indicator as an observed fact. A number like `Immediacy 138.4` is defensible as an index level with a published base date and construction; it is indefensible as an empirical claim about the world.

The operational form of that rule is a **provenance tag on every displayed number** — `OBSERVED`, `MODELED`, or `EDITORIAL`. It also has a bonus: a handful of securities genuinely do have public data (postal volumes, film sales, vinyl revenue, cinema attendance), so those can be tagged `OBSERVED` and the system acquires real anchors exactly where the world supplies them, with no pretence about the rest.

## If nothing can be obtained

The fallback is not to fake data but to publish an internal valuation model and be cold about its status — see [[pricing-model]]. The architecture is designed so data can arrive later without discarding it: each factor becomes a slot that public statistics plug into.

```text
Presence = Editorial Assessment
                ↓ later
Presence = Postal Data 60% + Survey 20% + Editorial Model 20%
```

## Open

- No data source has been secured. The Google Trends application has not been submitted or approved on the record.
- Whether the work ships on real data at all, or on the internal model, is undecided — and the choice changes what LONGING is: an authored fiction, a data visualization, or something between. See [[Q-001-price-formation]].
- Korean-only sources (Korea Post, Naver) versus global coverage is unaddressed, and it bears on whose disappearance the work is measuring.

## Related

- [[pricing-model]]
- [[Q-001-price-formation]]
- [[Q-004-unit-of-account]]

## Sources

- [[SRC-2026-09-05-price-formation-market-model]] — raw/conversations/2026-09-05-price-formation-market-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md

The platform capabilities and statistical series described above reach this repository only through the source conversation, which cited them from web search during the discussion. They are secondary citations and have not been independently verified here.
