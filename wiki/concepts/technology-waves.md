---
status: working
attribution: user-confirmed
updated: 2026-09-21
sources:
  - SRC-2026-09-20-bearer-bond-issuance
  - SRC-2026-09-20-proxy-sourcing-prompt
  - SRC-2026-09-20-wdi-spine-retrieval
  - SRC-2026-09-20-wdi-internet-use
  - SRC-2026-09-20-wdi-mobile-subscriptions
  - SRC-2026-09-20-wdi-fixed-broadband
  - SRC-2026-09-20-wdi-spine-csv
  - SRC-2026-09-20-wave-calibration-from-spine
  - SRC-2026-09-20-loop-simulation-harness-v4
  - SRC-2026-09-20-wave-calibration-from-national-series
  - SRC-2026-09-20-national-series-retrieval
  - SRC-2026-09-20-loop-simulation-harness-v5
  - SRC-2026-09-20-no-korean-time-series
  - SRC-2026-09-21-ai-enablement-and-substitution
  - SRC-2026-09-21-restoration-is-arrival-and-substitution-is-judgment
---

# Technology Waves — arrival raises what substitution later takes

## The correction this page exists for

Every model in this project until 2026-09-20 had technology working in one
direction. `A(t)` rose, the substitution channel bit, practices were taken over,
and the index fell. The user rejected that as false to the record:

> 하지만 "밀레니엄, 《시월애》《동감》, 인터넷 동창 찾기 열풍. 새 세기에 대한 설렘" 과
> 같이 항상 새로운 기술이 낭만을 없에는 쪽으로만 작용하지는 않는다.

The internet around 1999 did not remove these practices. **It made them.** The
alumni-finding boom was a machine for restoring severed relationships. The two
films named are both about communication across time that should not be possible —
a mailbox and a radio. When a new device arrived, the first thing people did with
it was look for each other.

## The two phases

A technology wave produces two effects with opposite signs, and they are ordered.

| Phase | What it does to the instrument in [[DEC-008-bearer-bond-is-perpetual]] | Direction |
|---|---|---|
| **Arrival** (leads) | new modes of connection appear; people lean on each other in ways that were not available before — **issuance rises** | practices rise |
| **Substitution** (lags) | the same capability lets a person do alone what needed someone else — **calls rise** | practices fall |

Arrival comes first and substitution overtakes it. Every wave therefore contributes
a rise followed by a decline, and the aggregate is a sum of overlapping waves
rather than one curve.

**This replaces a scheduled fiction.** [[loop-simulation]] had a revival era placed
by hand, because a history needs at least one long advance to be a history rather
than a slope. The advance is now structural: it is what the early part of a wave
does. Nothing is scheduled.

**It also multiplies the invisible peak.** [[reserve-instruments]] records that
device as a single unobservable moment; each wave now has one — the week its
substitution effect overtakes its arrival effect. Nobody can see it happen. Only
a later chart shows it.

## The span is thirty years, 1996 to 2026

The user fixed the history at exactly thirty years. Within it the waves stack:
bulletin-board services and pagers, mobile telephony, broadband, the social web,
messaging, and finally AI.

This solves a sourcing problem the AI-only version had. Token volumes are
published only for the last few years and not as a continuous series; **internet,
mobile and broadband penetration have national statistics running from the late
1990s**. Twenty-six of the thirty years can rest on measured series, with the AI
segment attached from vendor disclosures at the end.

## The driver is measured where measurement exists

```
A(t) = measured proxy over the window where data exists
     = extrapolation of the same functional form beyond it
```

The institute **publishes the boundary**. On the methodology page and on the
numeraire's own chart, a vertical rule marks where measurement stops and the model
continues.

This is the strongest thing the decision buys. Until now the decline was not
hard-coded but the *rise* was drawn by hand, and that was the design's remaining
soft spot. Now the early history is a record of what the world actually did.
[[DEC-004-secular-decline-with-rallies]]'s sentence — *calculated against the
world's current direction, it keeps falling* — stops being a figure of speech.

The institute defends neither side of the rule. It only marks which part is
observation and which part is estimate.

## What remains open

- **Which proxies.** Penetration series exist for three countries with different
  definitions and base years; a normalisation rule is required and the institute
  must publish it. The 2026-09-20 sourcing round — [[proxy-sourcing-review]] —
  names the candidate spine (the ITU / World Bank triplet for internet use, mobile
  and fixed broadband, 1996 to about 2024) and finds that only four of the seven
  waves can be carried as measured series at all: dial-up, messaging and
  generative AI cannot. **The spine is now in hand** (2026-09-20): the three WDI
  series for the three countries, vintage 2026-07-13, retrieved and registered with
  their coverage — internet use 1996–2024 everywhere; mobile 1996–2024, Japan to
  2023; fixed broadband 1998–2024, Japan to 2023. The last fully measured common
  year is 2023. No proxy is selected, nothing is normalised, and the national
  satellite series are verified to exist but not collected. See
  [[SRC-2026-09-20-wdi-spine-retrieval]] and [[proxy-sourcing-review]].
- **The boundary is not one line.** This page says a vertical rule marks where
  measurement stops. The sourcing round's most consistent finding is that the
  boundary differs by technology and by country, that each observation carries
  its own reference, fieldwork, publication and revision dates, and that for
  generative AI the *no longer measured* line sits almost immediately after
  *first measured*. Either the chart carries one boundary per series or the
  methodology page states a rule for collapsing them into one published week.
  Undecided.
- **Wave membership and dating.** Which technologies count as waves, and when each
  arrives in each market, is unselected. **Two of the seven are now dated from
  measurement** (2026-09-20): mobile and broadband arrival weeks and widths come
  from logistic fits to the WDI spine under a published rule —
  [[SRC-2026-09-20-wave-calibration-from-spine]]. Measured, both waves arrive
  later than the placeholders in every market, Korea and Japan reach mobile
  together (1999.8, 1999.9) with the United States two and a half years behind,
  and broadband's cross-market spread halves. The other five keep placeholder
  dates; internet use was fitted as a check series and not wired, since it is
  not a dial-up series. The fits are `llm-proposed`; the harness with them is
  [[SRC-2026-09-20-loop-simulation-harness-v4]].
  **Two more waves are dated in two markets** later the same day —
  [[SRC-2026-09-20-wave-calibration-from-national-series]]: smartphones in Japan
  (MIC household ownership) and the United States (Pew adults), the social web in
  the United States (Pew, share of internet users, 2005–2015) and Japan (OECD
  `D1B_I`, individuals 16–74, from 2012, ceiling fixed at 100). All four dates
  are later than the placeholders; Japan's social-web date, 2014.8, dates a
  survey definition that includes LINE rather than the arrival of the social
  web. Korea keeps its placeholder in both: no smartphone series was reached,
  and its OECD social-networking series begins above half its ceiling, so it
  bounds the midpoint (at or before 2005) without containing it. The harness
  with them is [[SRC-2026-09-20-loop-simulation-harness-v5]]; mixing a
  placeholder with measured dates inside one wave is a recorded distortion.
  Dial-up, messaging and AI remain placeholders.
  **The Korean rates by year are not available** (user, 2026-09-20), so the
  smartphone and social-web waves cannot be measured in all three markets. What
  v5 showed — a guessed date sixteen years from a measured one inside a single
  wave, and the artificial local structure that follows — leads to a rule,
  `llm-proposed`: **a wave's dates are wired only when every market's date is
  measured**; a wave measured in some markets keeps its placeholder in all,
  and the measured dates are recorded beside it as what the placeholder must
  not contradict. Under that rule the working build is v4 — mobile and
  broadband measured, five waves on placeholders — and v5 is retained as the
  record of what mixing does. The Japanese and US smartphone and social-web
  dates stay on file in [[SRC-2026-09-20-wave-calibration-from-national-series]].
- **The lag between arrival and substitution**, per wave. Unselected.
- ~~**Whether restoration counts as arrival, and whether substitution distinguishes
  execution from judgment.**~~ Decided 2026-09-21: restoration counts as arrival
  and the substitution channel counts substitution of judgment,
  [[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]. What remains
  is **the AI wave's reset connection coefficient**, and **the rule that sorts an
  act between execution and judgment** — the user names an ambiguous middle and
  proposes a per-security ontology to carry the rule, `user-originated`.
- **Named events.** Using specific cultural events puts real proper nouns into one
  market's event stream, which obliges comparable density in the other two.
  Unresearched.

## What the third simulation round added to this page

Each wave now carries a coefficient for how much of its arrival makes new ways to
reach a person rather than new ways to manage without one. It is the only place in
the design where the technologies are distinguished from each other, and it
separates the eras by character rather than by assertion: the social web and
mobile telephony score highest, and **AI is the outlier at a tenth of them**. That
single number is the only claim this work makes about AI — it substitutes heavily
and connects almost nobody.

The consequence shows in the market. Advances before 2000 run at 1.5–1.9× the
run's mean arrival intensity; every advance after 2010 runs below a third of it
and is short covering. **The century's turn is the last time buying itself lifted
this market.** See [[loop-simulation]].

## Evolution — the AI wave also restores (2026-09-21)

The user put a case to the assistant that the page's two phases had not named:
a person who lost speech to ALS, given it back by a decoder that reads the jaw
and mouth motor signals and says what they meant to say. The user's reading —
put as a question, not a decision — is that this runs in the direction of
**more** romance, not less:

> 루게릭병에 걸려서 말을 못하는 사람이 있었는데 인공지능을 사용해서 말을 하려고 할 때 …
> 이런건 낭만이 증가하는 방향이 아닐까?

That is an arrival-phase effect inside the AI wave, and it is a different kind
from the ones this page lists. The internet's arrival *made* new ways to reach a
person; this *restores* a way that illness had taken. Both put issuance up. The
page's coefficient for AI — a tenth of the social web's — was set from the
substitution half alone and has never counted this. The user has not decided
whether it should, and the coefficient is unchanged.

Three refinements from the assistant, all `llm-proposed`, none adopted:

- **Enablement and substitution are two actions of one technology, not two
  technologies.** The same speech-generating capability is restoration when it
  carries a person's own words and substitution when it writes the letter for
  them. Sorting technologies into good and bad is therefore the wrong
  classification; the same technology can sit in both places depending on who
  uses it for what, and can move from one to the other as it spreads — restoring
  at first, deciding what everyone says later.
- **Substitution of execution is not substitution of judgment.** Corrected by the
  assistant against its own first answer: less done by hand does not mean less
  decided by the person. A synthesiser that voices what one chose to say takes
  the execution and leaves the choice. The channel this page calls substitution
  would then need to say which it measures; the assistant proposes recording
  beside every substituted act whether the content and the consequential choice
  were the person's or the system's, as a check that keeps execution handed off
  from being read as agency lost.
- **The work's premise, restated.** From *technology takes romance* to: technology
  widens what a person can do, and reduces the value and room of an act only
  when it starts doing what the person already could. The assistant ties this to
  [[reflection]]'s definition of 사유 as room for one's own judgment — the
  measured object becomes the change in human agency, not the amount of
  technology in use. The conceptual sign rule *romance effect ≈ agency restored
  − agency displaced* was offered and then withdrawn as a measurement formula by
  the same assistant: the two sides are in different units.

How either action might be measured is on [[data-sources]].

## Evolution — restoration is arrival; substitution is of judgment (2026-09-21)

The user decided the question the same day
([[SRC-2026-09-21-restoration-is-arrival-and-substitution-is-judgment]],
[[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]): restoration
counts as arrival, so the arrival phase is *new or recovered* modes of
connection, and the substitution channel counts substitution of judgment, not
of execution. The AI coefficient above is therefore wrong by construction and
must be reset; its value is not set. The user's qualifications — some execution
restores (voicing a chosen sentence, reading in a learned voice), some execution
substitutes because it hands over the deliberation whole (letting AI translate a
greeting), the middle may be ambiguous — and the proposal of a per-security
ontology of execution and judgment are `user-originated`, not decided.

## Related

- [[DEC-008-bearer-bond-is-perpetual]]
- [[DEC-009-three-markets-and-convergence]]
- [[DEC-007-standard-return-numeraire]]
- [[DEC-004-secular-decline-with-rallies]]
- [[data-sources]]
- [[reflection]]
- [[loop-simulation]]
- [[proxy-sourcing-review]]

## Sources

- [[SRC-2026-09-21-restoration-is-arrival-and-substitution-is-judgment]] — [raw/conversations/2026-09-21-restoration-is-arrival-and-substitution-is-judgment.md](../../raw/conversations/2026-09-21-restoration-is-arrival-and-substitution-is-judgment.md); the decision, DEC-014
- [[SRC-2026-09-20-bearer-bond-issuance]] — [raw/conversations/2026-09-20-bearer-bond-issuance.md](../../raw/conversations/2026-09-20-bearer-bond-issuance.md)
- [[SRC-2026-09-20-proxy-sourcing-prompt]] — [raw/documents/2026-09-20-proxy-sourcing-prompt.md](../../raw/documents/2026-09-20-proxy-sourcing-prompt.md); the two open items above draw on the seven responses synthesised in [[proxy-sourcing-review]]
- [[SRC-2026-09-20-wdi-spine-retrieval]] — [raw/documents/2026-09-20-wdi-spine-retrieval.md](../../raw/documents/2026-09-20-wdi-spine-retrieval.md); the spine's coverage as retrieved, with the data files it describes
- [[SRC-2026-09-20-wave-calibration-from-spine]] — [raw/documents/2026-09-20-wave-calibration-from-spine.md](../../raw/documents/2026-09-20-wave-calibration-from-spine.md); the rule and fits that date two waves
- [[SRC-2026-09-20-wave-calibration-from-national-series]] — [raw/documents/2026-09-20-wave-calibration-from-national-series.md](../../raw/documents/2026-09-20-wave-calibration-from-national-series.md); two more waves, two markets each
- [[SRC-2026-09-20-national-series-retrieval]] — [raw/documents/2026-09-20-national-series-retrieval.md](../../raw/documents/2026-09-20-national-series-retrieval.md); what was reached and what was not
- [[SRC-2026-09-20-no-korean-time-series]] — [raw/conversations/2026-09-20-no-korean-time-series.md](../../raw/conversations/2026-09-20-no-korean-time-series.md); no Korean series to add, and the rule that follows
- [[SRC-2026-09-21-ai-enablement-and-substitution]] — [raw/conversations/2026-09-21-ai-enablement-and-substitution.md](../../raw/conversations/2026-09-21-ai-enablement-and-substitution.md); the ALS case is the user's, put as a question; the two-action split and the execution/judgment distinction are the assistant's
