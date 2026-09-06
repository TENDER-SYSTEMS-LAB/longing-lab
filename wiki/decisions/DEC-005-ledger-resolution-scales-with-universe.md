---
status: confirmed
attribution: user-confirmed
updated: 2026-09-07
sources:
  - SRC-2026-09-06-attribution-resolution-and-universe-scaling
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
---

# DEC-005 — Ledger resolution scales with the security universe

## The decision

Asked how many lines the weekly attribution ledger should carry, the user answered:

> 9개 안팍으로 가되, 종목수가 늘어날걸 고려해서, 종목이 늘어나면 줄 수가 늘어나도록 해야겠다. 노출되는 Factor가 늘어나니까.

Read as: start near nine displayed factors, and let the number of ledger lines grow as the security universe grows.

This is a **rule, not a set selection**. The user did not pick which nine factors open the ledger. The user fixed how the count behaves as the work grows: factor count becomes a function of universe size, not a constant chosen once and left alone.

## Why it matters

Three consequences follow from stating this as a rule rather than a fixed number.

**It converts a single choice into a promotion schedule.** The unresolved question "which factor set" stops being a one-time selection among the six second-round candidate sets (see [[factor-architecture-review-consensus]]) and becomes an ongoing schedule: start near nine, add a line when the universe supports one more.

**It generalizes a device one review applied narrowly.** In the second review round, Claude declared Coordination Compression a real factor but left it unpriced, on the stated ground that its support in the eleven-security universe was essentially two constituents — "a factor supported on two constituents is not a macro factor; it is a security-specific effect with ambitions." That was one review's treatment of one of its own factors. This decision takes the same device — a factor can exist as declared-but-unpriced until the universe can support it — and makes it standing policy for the whole ledger, not a one-off exception.

**It turns a deliberately separated question into a roadmap input.** The third review round put security-universe expansion explicitly out of scope, to keep the factor-set question and the universe question separable while that round runs (see `raw/sources.md`, note on the third review round). This decision does not reopen that separation for the third round's purposes; it settles a different question — how ledger resolution behaves over time — in a way that makes universe size a direct input to future factor-count decisions rather than a blocker sitting outside the process.

## What remains open under it

- **The promotion criterion is not settled.** The assistant proposed, in the same session, that a factor earns a ledger line when at least one security in the universe responds to it differently from every other factor — a replacement for the earlier working ratio of roughly one factor per three securities. This is `llm-proposed`. The user agreed with the direction of raising the security count to raise the factor ceiling, but did not confirm this specific criterion.
- **Which nine factors form the starting set is not decided.** The rule fixes the target count and its growth behavior, not membership. Membership remains exactly as open as it was left by [[factor-architecture-review-consensus]].
- **The three-layer allocation rule and the treatment of `Unexplained`** that this resolution rule interacts with are both `llm-proposed`, not confirmed. See [[attribution-ledger]].

## A later user position that bears on the promotion criterion

Later on 2026-09-06, after the decision was recorded, the user read this page's summary back and added a position:

> 근데 나는 종목보다 팩터가 더 많아도 될 것 같아. 그래서 너가 정리해준것처럼 "어떤 실천을 상장하느냐가 어떤 팩터가 존재할 수 있는지를 결정"하는 방식이어야해. 다음 모델링에서 LLM들에게 의견을 구할 때 참고해줘.

Two things, and an instruction.

**Factors may outnumber securities.** This rejects the working ratio `K ≤ N/3` proposed by Claude in the second review round, under which eleven securities support roughly four factors and forty-five support roughly fifteen. The user does not dispute the argument recorded against simply raising the security count — that thirty more slow analog practices leave effective rank where it was. The position is that the factor count should not be capped by the constituent count in the first place.

**Listing choice determines which factors can exist.** The user quotes back the ordering conclusion reached in the earlier session and attaches it as the reason the first position is acceptable. The binding constraint is not the ratio of two counts; it is whether the listed universe can express a given factor at all — which is the same object the `llm-proposed` per-factor separability test above is trying to measure. The user endorsed the ordering, not that test.

**Both are to be carried into the next review round as stated context.**

This does not change the decision. DEC-005 fixes how ledger resolution behaves as the work grows, and it remains exactly that. What the position does is settle the direction of the still-open promotion criterion: whatever criterion is adopted must be a test of expressibility against the listed universe, not an arithmetic cap on factor count. Recorded as `user-originated` and `working` — a stated direction, not a specified mechanism.

## Status

Confirmed. The user stated the rule directly in response to a direct question, in the same exchange that also stated related positions (that unattributable events should not occur, and that factors should be abstract but numerous) which are recorded separately as `user-originated` and `working` because they are stated directions rather than specified mechanisms — see [[attribution-ledger]].

## Related

- [[attribution-ledger]]
- [[pricing-model]]
- [[factor-architecture-review-consensus]]
- [[Q-001-price-formation]]

## Sources

- [[SRC-2026-09-06-attribution-resolution-and-universe-scaling]] — [raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md](../../raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md)
- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md)
