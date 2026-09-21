---
status: working
attribution: user-originated
updated: 2026-09-07
sources:
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-06-world-rules-letter-spec-request
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-price-formation-market-model
---

# Arbitrage

A direction stated by the user on 2026-09-06:

> 차익거래를 해당 세계관에 추가하면 재미있겠다. 차익거래가 LONGING 세계관에서 어떻게 구현되는지 보는것도 재미있는 요소일 것 같아.

The interest is explicitly double. Arbitrage is wanted as a market mechanism, and *how it turns out to be implemented in this particular world* is itself named as part of the appeal. That framing makes it a world-building question before it is an equation, which is why it has its own page rather than a paragraph inside [[pricing-model]].

No mechanism was proposed in the session by either party. This page records the direction, the material already in the repository that it lands on, and the questions it opens. Nothing here is a specification.

## What the model already has

The corpus contains **limits to arbitrage** but not arbitrage. Claude's first-round proposal scales the mean-reversion coefficient down by crowding:

```text
κ = κ₀ × (1 − |crowding|) × evidence_arrival
```

Read plainly: a mispricing persists because nobody is left to take the other side, not because belief is intense. It is one of the two live candidates for replacing the rejected `κ(1−S)` gate — the other being the dual anchor — and it survives in [[pricing-model]] as an unresolved alternative.

That mechanism is entirely negative. It describes the *absence* of an arbitrageur without ever depicting one. At the time of that discussion, the repository did not specify who took the other side, what holding cost, or what closing meant. The later unit-dependent proposals and revised market scope are recorded below.

## What the work already advertises

The governing display of the whole system is a standing arbitrage advertisement:

```text
Fundamental Value     34.80
Market Price          21.42
Discount to Model    -38.4%
```

An institution that prints a 38.4% discount to its own fair value every week is, in the register of financial research, publishing a trade. The work has been showing the gap since the model's first draft without ever asking what it would mean for someone to act on it. That is the specific opening the user's direction points at.

## Questions this opens

These are questions raised in the Wiki from registered material, not proposals from the source session.

**Who is the counterparty?** The house publishes `F`. If the house also arbitrages toward `F`, the institution is trading against its own estimate and the circularity that sank the original consensus mechanism — analysts setting the anchor *and* the force acting on the anchor — returns in a new costume. If the arbitrageur is someone else, that participant has to exist in the fiction.

**What is bought?** Arbitrage needs something finite to hold. The repository has no unit: [[Q-004-unit-of-account]] is unresolved, and several reviews already note that positioning and short interest are meaningless without a float. Arbitrage is a second, independent reason the unit question blocks work downstream — and the user has separately asked for that question to be put to the review models.

**What makes it converge?** In a real market the arbitrageur is paid when price meets value. Here `F` is the research house's monthly opinion, not a settlement. Without a scheduled observable there is nothing for a position to be *right* about, which is the same gap two second-round reviews named when they proposed a quarterly print of realized incidence. Arbitrage may be a third argument for that print rather than a separate feature.

**Does an arbitrageur belong to this work's politics?** [[system-grammar]] holds that the system never understands emotion and that neither LONG nor SHORT is virtue. A participant who buys handwritten letters because they are cheap relative to model — not because they are loved — is the purest available expression of that rule. It is also the point at which the work's quiet bias could tip either way, which makes it material for [[Q-003-calibrating-the-bias]].

## Evolution — concrete unit-dependent branches

The world-rules/LETTER task now proposes specific holdings in [[Q-004-unit-of-account]] and separates market participants from research staff and viewers in [[world-rules]]. A funded future-practice claim can have finite collateral, an opposite claimant, a dated payoff, and a budget cost. A publication-only quotation has none of these holdings. Support certificates instead require a real in-world service promise and an explicit support-to-practice channel. These are alternatives, not adopted mechanisms.

For the proposed funded branch, the gap between house estimate and market quote is a risky convergence thesis: the house may be wrong and has no authority to make its estimate true. A strict arbitrage example needs executable inconsistent prices for identical or complementary payouts, with fees, collateral, settlement and timing specified. Merely printing `F > P` does not establish that opportunity. The earlier text records the gap in the original corpus; the new candidates make it reviewable without claiming an implemented market.

## Related

- [[pricing-model]]
- [[analyst-system]]
- [[attribution-ledger]]
- [[system-grammar]]
- [[Q-001-price-formation]]
- [[Q-003-calibrating-the-bias]]
- [[Q-004-unit-of-account]]

## Evolution — market scope without investor stories (2026-09-07)

The user now excludes investor personas' betting and profit/loss stories and selects the aggregate Market as the simulation scope. The earlier arbitrage questions about a named participant or a full contract system are conditional design questions, not universal gates for the work. No arbitrage mechanism has been chosen.

The user remains interested in convincing financial phenomena, explicitly reopening forced short covering for exploration. [[pricing-model]] preserves the assistant's aggregate exposure/maintenance candidate. It is neither an implemented arbitrage route nor a confirmed squeeze. [[Q-004-unit-of-account]] records the initial market-price reference for 사유 and the possible later state link. The distinction between a valuation gap and an executable riskless opportunity remains relevant if strict arbitrage is pursued.

## Sources

- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md); ChatGPT export, 2026-09-06–07; user turns support decisions, assistant synthesis and mechanisms retain proposal status

- [[SRC-2026-09-06-world-rules-letter-spec-request]] — [raw/documents/2026-09-06-world-rules-letter-spec-request.md](../../raw/documents/2026-09-06-world-rules-letter-spec-request.md); exact current design request; application choices and tests remain LLM proposals

- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md)
- [[SRC-2026-09-05-claude-critic-of-model]] — [raw/surveys/2026-09-05-critic-of-model/2026-09-05-claude-critic-of-model.md](../../raw/surveys/2026-09-05-critic-of-model/2026-09-05-claude-critic-of-model.md)
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md)
