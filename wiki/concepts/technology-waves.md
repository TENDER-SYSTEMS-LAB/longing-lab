---
status: working
attribution: user-confirmed
updated: 2026-09-20
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
- **The lag between arrival and substitution**, per wave. Unselected.
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

## Related

- [[DEC-008-bearer-bond-is-perpetual]]
- [[DEC-009-three-markets-and-convergence]]
- [[DEC-007-standard-return-numeraire]]
- [[DEC-004-secular-decline-with-rallies]]
- [[data-sources]]
- [[loop-simulation]]
- [[proxy-sourcing-review]]

## Sources

- [[SRC-2026-09-20-bearer-bond-issuance]] — [raw/conversations/2026-09-20-bearer-bond-issuance.md](../../raw/conversations/2026-09-20-bearer-bond-issuance.md)
- [[SRC-2026-09-20-proxy-sourcing-prompt]] — [raw/documents/2026-09-20-proxy-sourcing-prompt.md](../../raw/documents/2026-09-20-proxy-sourcing-prompt.md); the two open items above draw on the seven responses synthesised in [[proxy-sourcing-review]]
- [[SRC-2026-09-20-wdi-spine-retrieval]] — [raw/documents/2026-09-20-wdi-spine-retrieval.md](../../raw/documents/2026-09-20-wdi-spine-retrieval.md); the spine's coverage as retrieved, with the data files it describes
- [[SRC-2026-09-20-wave-calibration-from-spine]] — [raw/documents/2026-09-20-wave-calibration-from-spine.md](../../raw/documents/2026-09-20-wave-calibration-from-spine.md); the rule and fits that date two waves
