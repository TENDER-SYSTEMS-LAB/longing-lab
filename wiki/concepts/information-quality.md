---
status: working
attribution: user-originated
updated: 2026-09-07
sources:
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-claude-critic-of-model
---

# Information Quality

A direction stated by the user on 2026-09-06:

> 뉴스는 한번에 공개되기도 하지만, 오보 되기도, 과대/과소 보도 되기도 하고, 큰 뉴스가 찌라시처럼 미리 시장에 돌아다니기도 한다. 이것도 모델에 추가하면 재미있을 것 같아.

The existing design treats an event as a fact that arrives. The user's position is that news is also a *report about* a fact, and that reports fail in specific, patterned ways. Four behaviours are named:

1. **Clean disclosure** — the event becomes known at once.
2. **Erroneous reporting** (`오보`) — a report that later turns out to be false.
3. **Over- and under-reporting** — a report whose magnitude does not match the event.
4. **Pre-circulation as rumour** (`찌라시`) — a large event leaking into the market before its formal disclosure.

No mechanism was proposed in the session by either party. This page records the direction and maps it against what the event layer already holds.

## What the event layer already has

Recorded in [[pricing-model]] and surviving all seven first-round reviews:

- The Event Desk classifies **relevance only** — which conditions and which securities an event touches, at what magnitude and confidence. It never publishes a direction. Direction is left to the analysts, who disagree.
- **One event writes to exactly one layer**, so the same news is not counted twice through the betas.
- **Only the surprise moves price.** The anticipated part is already in the fundamental and already in the price.
- Confidence should scale **the speed at which an event is priced in, not the size of the move**: high confidence prices in within the week, low confidence bleeds in over several weeks **and can reverse if unconfirmed**.

That last rule is the nearest existing structure to what the user is describing, and it is not the same thing. It models *uncertainty about an event that is nonetheless true*. Nothing currently models a report that is simply wrong. GLM's treatment goes furthest in the corpus — provisional events carry half weight and decay unless confirmed within N weeks, and **revisions are themselves events** — but a revision there corrects a magnitude; it does not retract a fact.

Mapped against the four behaviours: item 1 is the current default, item 3 is partly reachable through the existing surprise and confidence framing, and items 2 and 4 have no representation anywhere in the repository.

## What each addition would touch

Raised in the Wiki from registered material, not proposed in the source session.

**Misreporting collides with the ledger's exact sum.** [[attribution-ledger]] requires that the printed lines sum exactly to the return. A false report that moves price in week 1 and is retracted in week 3 produces two real moves with one cause, and the cause was never true. Whether the retraction is a fresh event, a reversal of the original line, or a restatement of the earlier week's ledger is a display decision before it is a modelling one — and restating a published week is exactly the kind of institutional behaviour the form is built to depict.

**Misreporting is the cheapest available source of surprise.** The largest structural gap two second-round reviews identified is that nothing in the drafted system can surprise anyone, and their fix was a quarterly print of realized incidence. A retracted report is a second, independent way for the market to have been wrong about something — and unlike the print, it needs no new observable.

**Pre-circulation is a positioning mechanism, not an event mechanism.** A rumour that leaks before disclosure moves the crowd before the news, which means the formal disclosure then lands on an already-crowded book. That is precisely the configuration the asymmetric squeeze amplifier exists to price: the shock that agrees with positioning does nothing, because the position is already taken. Modelling the leak may therefore require no new price machinery at all — only a timing structure over an event that already exists.

**It gives credibility something to be scored on.** GLM's credibility weight `w` updates on lagged forecast errors, so the research house can accumulate a recorded losing streak. A press layer that can be wrong extends that to a second institution: the work would then hold two fallible authorities — the model and the reporting — and the gap between them is legible without commentary.

**It touches the work's honesty rules.** [[data-sources]] holds that the system must not fabricate numbers that look like measurements. A report that is wrong is not a fabricated measurement; it is a depicted institution behaving as institutions do. But the boundary between the two is thin enough to be worth stating before the mechanism is built.

## Open

- Whether misreporting is a property of the event, of a separately modelled press layer, or of the Event Desk itself.
- How a retraction appears in a ledger that has already been published.
- Whether rumour is modelled as an early partial event or purely as a positioning drift ahead of a scheduled disclosure.
- Whether the reporting layer can be wrong about *direction*, given that the Event Desk deliberately publishes none.

## Related

- [[pricing-model]]
- [[attribution-ledger]]
- [[analyst-system]]
- [[data-sources]]
- [[arbitrage]]
- [[Q-001-price-formation]]

## Evolution — information inside authored history (2026-09-07)

The new fictional-history direction makes the gap between author-known data and contemporaneous knowledge central to research records. The opening user brief retains the distinctions among underlying state, observed reports, institutional estimates, analyst forecasts, and market price. The final assistant synthesis proposes timestamped information availability and preserved release vintages so a past report cannot silently know a later correction.

It also proposes separating information arrival, publication, price response, and performance evaluation when reports influence prices. These production controls support the desired historical record but were not individually confirmed by the user. No lag, error, rumour, correction, or forecast-generation rule is selected. See [[analyst-system]] and [[data-sources]].

## Sources

- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md); ChatGPT export, 2026-09-06–07; user turns support decisions, assistant synthesis and mechanisms retain proposal status

- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md)
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md)
- [[SRC-2026-09-05-glm-critic-of-model]] — [raw/surveys/2026-09-05-glm-critic-of-model.md](../../raw/surveys/2026-09-05-glm-critic-of-model.md)
- [[SRC-2026-09-05-claude-critic-of-model]] — [raw/surveys/2026-09-05-claude-critic-of-model.md](../../raw/surveys/2026-09-05-claude-critic-of-model.md)
