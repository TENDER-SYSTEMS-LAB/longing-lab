---
status: confirmed
attribution: user-confirmed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-order-constraint-retained
  - SRC-2026-09-20-joint-line-as-a-range
---

# DEC-012 — Each analyst carries their own order, inside the house constraint, until the record says otherwise

## The decision

[[DEC-010-declared-order-with-a-joint-line]] makes the attribution's order a published convention and its `Joint` line the range over every admissible order. When that range was decided the user asked whether each analyst might carry a different order. The assistant's reply ([[SRC-2026-09-20-joint-line-as-a-range]], Turn 6) argued for it — the analysts on [[analyst-system]] are already defined by what they are willing to count as value, and an order makes that arithmetic — and named the choice it left: whether an analyst's order is bound to the admissible set the house ledger uses, or exempt from it with the house ledger as the neutral reference. The user answered:

> 일단 그럼 순서 제약을 유지하자. 내가 나중에 기록보고 순서 제약을 해제 하던지 고려해볼게

**Three parts, `user-confirmed`, the first by the assistant's reading of a message that does not restate the proposal it accepts:**

1. **Analysts carry their own order.** An analyst's monthly research may declare its own sequence and read the month's weeks through it. The house ledger keeps the one published order of DEC-010 and its `Joint` range; an analyst's reading is a second layer, not a replacement.
2. **The house constraint holds for analysts.** Measured lines are removed before estimated lines and the reflexive line is last, for every analyst as for the house. An analyst chooses among the admissible orders — six over the three movable blocks on the current lines — so each analyst's attribution is a point inside the house `Joint` band, never outside it.
3. **The constraint is provisional.** The user will read the record — the generated history, its bands and its analysts' readings — and then consider lifting the constraint. What is revisable is the constraint on analysts' orders, not the decision that they carry one; what in the record would prompt the lifting is not stated.

## What this does and does not do

- **What it gives.** The `Joint` width becomes the room the analysts have to disagree in a given week; when the band collapses, as it does late in the generated history ([[identification-experiment]]), every admissible order returns the same numbers and the disagreement is arithmetically moot. This is the assistant's reading of the consequence, `llm-proposed`.
- **What it costs.** An order that puts the analyst's own valued line ahead of the schedule is not admissible, so the most romantic reading is expressible only within the estimated block; the SHORT analyst's natural order coincides with the house order. This is the cost the user accepted for now and the reason the choice is provisional.
- **What it does not decide.** Which order each analyst carries; whether the reading appears in the monthly report as a line-by-line ledger or only in prose; how a monthly reading is cut from weekly ledgers, since the house ledger is weekly and research is monthly ([[DEC-003-weekly-market-monthly-research]]); and the relation to scoring — an order cannot be tested from returns, so an analyst's order never enters a track record ([[analyst-system]], open scoring).

## Related

- [[DEC-010-declared-order-with-a-joint-line]]
- [[DEC-011-the-audience-ledger-reads-hearts-cooling]]
- [[DEC-003-weekly-market-monthly-research]]
- [[analyst-system]]
- [[attribution-ledger]]
- [[identification-experiment]]
- [[Q-003-calibrating-the-bias]]

## Sources

- [[SRC-2026-09-20-joint-line-as-a-range]] — [raw/conversations/2026-09-20-joint-line-as-a-range.md](../../raw/conversations/2026-09-20-joint-line-as-a-range.md); the question and the assistant's proposal it answers
- [[SRC-2026-09-20-order-constraint-retained]] — [raw/conversations/2026-09-20-order-constraint-retained.md](../../raw/conversations/2026-09-20-order-constraint-retained.md); the decision
