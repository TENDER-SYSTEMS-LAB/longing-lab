---
status: confirmed
attribution: user-confirmed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-orthogonalisation-order
  - SRC-2026-09-20-round-decisions-and-deferrals
  - SRC-2026-09-20-identification-experiment-findings-v4
---

# DEC-010 — The attribution's order is declared, measured lines first, and the overlap is published as its own line

## The decision

The weekly attribution is a recursive orthogonalisation: each line is estimated on what the lines before it left. Lines that move together share variance, and the order decides which line is credited with the shared part. The fourth round ([[factor-identification-review]]) established that the order determines the split, cannot be tested from returns, and must be published; the user deferred choosing it on 2026-09-20 ([[SRC-2026-09-20-round-decisions-and-deferrals]]) and took it up the same day.

Asked whether the order could be found in the world, the user answered that it could not:

> 실제 세계에서는 거의 랜덤하게 동작하지 않을까? 닭이먼저냐 달걀이 먼저냐의 문제인것 같아.

The assistant's reading, which the user accepted, separates two things the question runs together. In the world, within a week, the numeraire, substitution and factor lines are simultaneous, and returns cannot order them — the chicken-and-egg is real, and it is what the fourth round proved. The reflexive line is the one place the design already breaks the circle, by construction: it is the coefficient on the *lagged published* attribution, so it is never simultaneous with the rest. In the ledger, however, the order is not random. It is a convention the institute chooses and publishes, as a Cholesky ordering in a macro VAR or the market-first convention of a factor model is.

Offered three conventions — a declared order, an order-free average over all orders (Shapley), and a declared order that also publishes the overlap as its own line, as the interaction term of a Brinson attribution does — the user chose the third with the assistant's recommended sequence:

> 응 그걸로 가자. 결정 기록해줘

**Three parts, all `user-confirmed`:**

1. **The order is declared and published.** The institute states the sequence in which lines are removed. It is a convention, not a causal claim, and it is part of the published specification.
2. **Measured lines are removed before estimated lines.** The numeraire and the declared technology schedule are external, measured series; priced factors, positioning and the reflexive line are estimated from the market. The justification is not that measured causes come first but that *what is certain is removed first*, so the estimated lines are fitted on what measurement cannot explain.
3. **The order-dependent overlap is published as its own line.** Beside the ordered lines the ledger carries a `Joint` line: the amount by which the split would move under the alternative order. The undecidable part of the week is shown as undecidable, not assigned to either side.

The resulting sequence, with the first two positions fixed by part 2 and the rest carried over from the order the fourth round's reviewers assumed:

```
numeraire  →  substitution (declared schedule)  →  priced factors  →  positioning  →  reflexive  →  Unexplained
                                      +  Joint  (the overlap the order decided)
```

## Why the third convention

The institute's bias is the work's subject ([[Q-003-calibrating-the-bias]]), so the order is itself a statement: the published sequence is the institute's official answer to *what caused the decline*. A Shapley average would remove the statement along with the arbitrariness. Publishing the overlap keeps the statement and shows its cost. In the generated world that cost is already measured and already has the right shape: swapping the schedule and factor lines moves the schedule line by 1.85 times its own size early and 0.57 late on the v4 build ([[identification-experiment]]), so `Joint` is large in the early history, when the split between *substitution* and *factor* is mostly convention, and shrinks as the markets converge. The size of the chicken-and-egg becomes a published series.

## What this does not decide

- **Where the `Joint` line sits in the display**, whether it is a ledger line the viewer sees or an internal diagnostic like `Unexplained`. The same question is open for `Unexplained` on [[attribution-ledger]].
- **How `Joint` is computed** when more than two lines can be swapped. The experiment swapped two of six; the assistant's example was that single swap. Whether `Joint` is one alternative order, the range over all orders, or something between is unspecified. `llm-proposed` territory.
- **The internal order of the estimated block** — priced factors, then positioning, then reflexive — is inherited from the reviewers' assumed order, not chosen on its own grounds. The reflexive line is last by construction because it is lagged; the factor-before-positioning position has no argument recorded.
- **Whether the schedule is one line or one per wave.** [[technology-waves]] carries several waves; part 2 says the measured block goes first, not how the block is ordered inside itself.
- The exact-sum requirement: adding `Joint` to a ledger that must sum to the week's return needs the finite-change allocation rule [[attribution-ledger]] already lists as unstated.

## Related

- [[attribution-ledger]]
- [[factor-identification-review]]
- [[identification-experiment]]
- [[DEC-005-ledger-resolution-scales-with-universe]]
- [[DEC-007-standard-return-numeraire]]
- [[technology-waves]]
- [[Q-003-calibrating-the-bias]]

## Sources

- [[SRC-2026-09-20-orthogonalisation-order]] — [raw/conversations/2026-09-20-orthogonalisation-order.md](../../raw/conversations/2026-09-20-orthogonalisation-order.md)
- [[SRC-2026-09-20-round-decisions-and-deferrals]] — [raw/conversations/2026-09-20-round-decisions-and-deferrals.md](../../raw/conversations/2026-09-20-round-decisions-and-deferrals.md); the deferral this decision closes
- [[SRC-2026-09-20-identification-experiment-findings-v4]] — [raw/documents/2026-09-20-identification-experiment-findings-v4.md](../../raw/documents/2026-09-20-identification-experiment-findings-v4.md); the order-sensitivity figures
