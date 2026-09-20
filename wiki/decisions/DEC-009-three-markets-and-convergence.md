---
status: confirmed
attribution: user-confirmed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-bearer-bond-issuance
  - SRC-2026-09-20-factor-identification-prompt
  - SRC-2026-09-20-institution-naming-prompt
  - SRC-2026-09-20-japanese-publisher-is-national
  - SRC-2026-09-20-identification-experiment-findings-v4
---

# DEC-009 — Three markets, and the convergence that erases them

## The decision

Asked whether naming Korean events would fix the world to one country, the user
answered with a market fact instead of a setting:

> 현실 금융시장에도 각 나라의 금융시장이 존재하고, 각 나라별 상황에 따라 다르게
> 반응하기도 하지만, 시장이 점점 "효율적"으로 변하면서 동조화된다. 이 내용을 우리
> 작품에 녹여볼 수 있지 않을까? 일본 한국 미국 정도로 좁혀서 보면 될 것 같다.

**Three markets — Japan, Korea, the United States.** The same practice is listed
separately in each, with its own float, its own fundamental, and its own events.
The same thing dies at different speeds in different places.

That is not decoration. It is true of the period the work covers: in the late
1990s the three countries were finding each other on different machines — pagers
and i-mode, bulletin boards and the alumni boom, dial-up services. [[technology-waves]]
owns the arrival dates; this page owns what having three of them does to the market.

## Convergence is not declared. It comes off the same driver.

```
global share of events = ψ(A(t))
```

Early, an event is mostly **local** — it moves one market and not the others, and
the three indices go their own ways. Late, the same platform arrives everywhere at
once, events are **common**, and the three move together.

No new authored curve. `A(t)` was already doing three jobs — making the yardstick
heavier, advancing substitution, and calling balances. This is the fourth: **it
makes the world resemble itself.**

## What this publishes

**`DISPERSION`** — the variance across the three markets' returns. It falls as the
world becomes one market.

**A local/common split in the weekly ledger.** [[attribution-ledger]] gains a line
separating how much of this week's move was this market's own and how much was
everyone's.

**A second invisible peak.** The first is the backing's. This one is *the last week
the three markets disagreed*. Nobody can identify it at the time; only the
dispersion chart shows it, years later.

Efficiency is the word finance uses for this, and it uses it approvingly. The
institute does not comment. It prints the dispersion.

## Index names carry who was counting

Real flagship indices are named after four different authorities: a country
(KOSPI), a newspaper (Nikkei), a ratings agency (S&P), an exchange's quotation
system (NASDAQ). The name records who held the right to measure in that market.

The user chose that each market's index is computed and published by **a different
fictional institution**, so the naming structure carries the same information.

| Market | Structure | Candidate, not adopted |
|---|---|---|
| Korea | state-issued acronym | `KOCPI` — Korea Composite Practice Index |
| Japan | a newspaper's average | `<evening paper>` Average |
| United States | a ratings house of two surnames | `<name> & <name>` |
| All three | the institute's own product | `LONGING COMPOSITE` |

Constituent counts follow each market's listed universe, and the counts differ —
which records that coverage was never the same in the three places.

**The naming carries the convergence story to its end.** As the markets move
together the local indices become redundant, and the institute's global composite
takes their place. What a government counted, what a newspaper counted, and what a
ratings house counted are absorbed into one international series. Nobody took
anything. The names simply stop being quoted. **A third invisible peak: the last
week a local index was cited.**

`romance` is deliberately absent from the candidate names. [[overview]] fixes the
subject as the conditions of human experience that modernization is removing, and
does not use romance as a category label.

## Consequences elsewhere

**It attacks the factor-identification problem directly.** The third review round's
sharpest objection was that eleven securities cannot identify which shocks are
common. Three markets carrying the same practices make local and common factors
**structurally separable**, which is what identification needs.
[[DEC-005-ledger-resolution-scales-with-universe]] ties ledger resolution to
universe size, and the user's position is that listing choice determines which
factors can exist; tripling the universe acts on both.

**One numeraire, not three.** Each market does not get its own STANDARD RETURN. The
basket is defined once, globally, and all three quote against it. Three currencies
would require an exchange rate between them, and convergence — the thing this
decision exists to show — would be hidden inside currency moves. It is also right
in the fiction: the yardstick measures what the tools hand back, and the tools are
global.

## What remains open

- **Which practices list in which market**, and the counts.
- **Named fictional institutions.** An evening paper and a ratings house must be
  invented, and a collision check against real companies is required. [[DEC-001-project-name-longing]]
  already carries an unperformed trademark and collision check; this triples it.
  The 2026-09-20 naming round — [[institution-naming-review]] — mapped what is
  occupied and produced uncleared candidates; **two reviewers independently reject
  the `KOCPI` placeholder above**, as one letter from KOSPI and as embedding `CPI`.
  The round also surfaced a decision this page did not make: whether the Japanese
  publisher is a national paper, as the Nikkei is, or a regional one. **Decided
  2026-09-20: a national paper.** `user-confirmed`. The index therefore carries
  national authority from the start, and its later absorption into the composite
  is a national institution ceding to an international one. Candidates with a
  regional qualifier — 東海, 北陸, 京浜 — are out; the surviving forms are those
  without a place name. The name itself is still unselected.
- **Symmetric research.** Using specific Korean events obliges comparable
  specificity for Japan and the United States. Not done.
- **Normalisation across three national statistical series** with different
  definitions and base years — and the institute must publish the rule it uses.
- **The dispersion measure's definition**, and whether the local/common ledger
  split is displayed to the audience or only computed.

## Evolution — the fourth round tests the separability claim

The 2026-09-20 factor identification round put the claim above — that three
markets make local and common factors structurally separable — to seven models
against this exact universe. Their answer, `llm-proposed` and recorded in
[[factor-identification-review]], is that the claim is half-true at every date.
The layout *names* local versus common permanently: thirteen directions, one
common, two market contrasts, ten practice contrasts. But it *estimates* market
factors only while the markets differ and practice factors only while they
align — a practice dying at three speeds in three markets is three
security-specific effects, not one practice factor. The two purchases are never
at full strength together, and the handover between them is the structural
event of the middle of the history, dated by a rank test rather than by the
specification. Convergence also has an asymmetry the decision did not state:
loadings on early, staggered waves survive it if they are time-invariant, while
loadings on waves that arrive coincidentally everywhere — smartphones,
messaging, AI — were never identified at all. And the correlation path is not
the right observable: `+0.2 → +0.9` can mean local shocks shrinking or global
variance growing, and only the absolute variance of the two market contrasts
distinguishes them. None of this reverses the decision; it says exactly what
the decision bought. A later run the same day — the placebo gate in
[[identification-experiment]] — adds a number to it: with mobile and broadband
dated from measurement, Korea and Japan arrive in the same season and the
United States within two years, and permuting the market labels of the declared
schedule costs no explanatory power. The stagger this page relies on is, for the
two measured waves, smaller than the placeholders assumed; the naming of local
versus common survives, the estimation from timing does not, for those waves.

## Related

- [[technology-waves]]
- [[DEC-008-bearer-bond-is-perpetual]]
- [[DEC-007-standard-return-numeraire]]
- [[DEC-005-ledger-resolution-scales-with-universe]]
- [[index-architecture]]
- [[attribution-ledger]]
- [[factor-identification-review]]
- [[institution-naming-review]]

## Sources

- [[SRC-2026-09-20-bearer-bond-issuance]] — [raw/conversations/2026-09-20-bearer-bond-issuance.md](../../raw/conversations/2026-09-20-bearer-bond-issuance.md)
- [[SRC-2026-09-20-factor-identification-prompt]] — [raw/documents/2026-09-20-factor-identification-prompt.md](../../raw/documents/2026-09-20-factor-identification-prompt.md); the evolution note draws on the seven responses synthesised in [[factor-identification-review]]
- [[SRC-2026-09-20-institution-naming-prompt]] — [raw/documents/2026-09-20-institution-naming-prompt.md](../../raw/documents/2026-09-20-institution-naming-prompt.md); the naming note draws on the seven responses synthesised in [[institution-naming-review]]
- [[SRC-2026-09-20-japanese-publisher-is-national]] — [raw/conversations/2026-09-20-japanese-publisher-is-national.md](../../raw/conversations/2026-09-20-japanese-publisher-is-national.md); the publisher is national
