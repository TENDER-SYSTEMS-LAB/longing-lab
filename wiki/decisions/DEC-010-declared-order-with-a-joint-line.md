---
status: confirmed
attribution: user-confirmed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-joint-line-as-a-range
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
- ~~**How `Joint` is computed** when more than two lines can be swapped.~~ Closed 2026-09-20 below: the range over every admissible order. What the range still needs is a statement of *what is permuted* — whether a block of several lines (the waves of the schedule, the priced factors) is fitted jointly so that only blocks are ordered; that is the assistant's proposal and remains `llm-proposed`.
- **The internal order of the estimated block** — priced factors, then positioning, then reflexive — is inherited from the reviewers' assumed order, not chosen on its own grounds. That positioning belongs to the estimated block at all is settled by [[DEC-007-standard-return-numeraire]]'s `MODELED` tag, noted on [[DEC-011-the-audience-ledger-reads-hearts-cooling]]. The reflexive line is last by construction because it is lagged; the factor-before-positioning position has no argument recorded.
- **Whether the schedule is one line or one per wave.** [[technology-waves]] carries several waves; part 2 says the measured block goes first, not how the block is ordered inside itself.
- The exact-sum requirement: adding `Joint` to a ledger that must sum to the week's return needs the finite-change allocation rule [[attribution-ledger]] already lists as unstated.

## Evolution — `Joint` is the range over every admissible order (2026-09-20)

Asked, in plain language, what the line is, and told that the experiment had measured one swap of six lines, the user chose the computation:

> 순서 조합 전부 돌려 범위로 내자. 결정 기록해줘.

**`Joint` is computed by running every order combination and publishing the range**, `user-confirmed`. Per line, it is the largest minus the smallest attribution that line receives across the orders. The assistant's reading, recorded as such, is that *every combination* means every order that respects the constraints parts 1–3 already fix — measured lines before estimated lines, the reflexive line last by construction — since the user was answering a summary of that proposal ([[SRC-2026-09-20-hearts-cooling-line]], option b) and a sweep that also permuted the measured block would contradict the decision it extends. Under those constraints, with the schedule, the priced factors and positioning as the three movable blocks, six orders are run; the count grows with the blocks, not with the lines, only if blocks are fitted jointly, which is still a proposal.

Because the range is a width and not a share, it is not additive: the declared lines still sum to the week's return and `Joint` does not enter the sum, so the finite-change allocation rule noted above is not required by this line. The 1.85 / 0.57 single-swap figures on [[identification-experiment]] become a lower bound on the early and late widths, not the width itself.

Still open after this: whether `Joint` is shown to the audience, and how; the joint fit of blocks; and a question the user attached to the decision — whether each analyst may carry a different order — which the assistant answered with a proposal, that the house ledger keeps one order and each analyst's monthly research declares its own reading as a point inside, or exempt from, the house band. Taken up the same day as [[DEC-012-analyst-orders-inside-the-house-constraint]]: analysts carry their own order inside this decision's constraint, provisionally.

## Related

- [[attribution-ledger]]
- [[factor-identification-review]]
- [[identification-experiment]]
- [[DEC-005-ledger-resolution-scales-with-universe]]
- [[DEC-007-standard-return-numeraire]]
- [[technology-waves]]
- [[Q-003-calibrating-the-bias]]
- [[DEC-011-the-audience-ledger-reads-hearts-cooling]]

## Sources

- [[SRC-2026-09-20-joint-line-as-a-range]] — [raw/conversations/2026-09-20-joint-line-as-a-range.md](../../raw/conversations/2026-09-20-joint-line-as-a-range.md); `Joint` computed as the range over every admissible order
- [[SRC-2026-09-20-orthogonalisation-order]] — [raw/conversations/2026-09-20-orthogonalisation-order.md](../../raw/conversations/2026-09-20-orthogonalisation-order.md)
- [[SRC-2026-09-20-round-decisions-and-deferrals]] — [raw/conversations/2026-09-20-round-decisions-and-deferrals.md](../../raw/conversations/2026-09-20-round-decisions-and-deferrals.md); the deferral this decision closes
- [[SRC-2026-09-20-identification-experiment-findings-v4]] — [raw/documents/2026-09-20-identification-experiment-findings-v4.md](../../raw/documents/2026-09-20-identification-experiment-findings-v4.md); the order-sensitivity figures
