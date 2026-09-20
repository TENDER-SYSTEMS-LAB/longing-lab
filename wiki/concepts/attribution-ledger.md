---
status: working
attribution: jointly-developed
updated: 2026-09-21
sources:
  - SRC-2026-09-21-joint-shown-and-blocks-fitted-jointly
  - SRC-2026-09-20-joint-line-as-a-range
  - SRC-2026-09-20-hearts-cooling-line
  - SRC-2026-09-20-orthogonalisation-order
  - SRC-2026-09-06-attribution-resolution-and-universe-scaling
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
  - SRC-2026-09-05-pricing-model-v2-factor-framework
  - SRC-2026-09-05-pricing-model-v2-factor-review-prompt
  - SRC-2026-09-05-pricing-model-v2-factor-review-claude
  - SRC-2026-09-05-pricing-model-v2-factor-review-deepseek
  - SRC-2026-09-05-pricing-model-v2-factor-review-gemini
  - SRC-2026-09-05-pricing-model-v2-factor-review-glm
  - SRC-2026-09-05-pricing-model-v2-factor-review-grok
  - SRC-2026-09-05-pricing-model-v2-factor-review-qwen
  - SRC-2026-09-06-factor-set-failure-profile-prompt-v2
  - SRC-2026-09-06-factor-set-failure-profile-chatgpt
  - SRC-2026-09-06-factor-set-failure-profile-glm
  - SRC-2026-09-20-factor-identification-prompt
  - SRC-2026-09-20-round-decisions-and-deferrals
  - SRC-2026-09-20-identification-experiment-findings
---

# Attribution Ledger

The weekly attribution ledger is the object the audience actually reads. [[pricing-model]] and [[factor-architecture-review-consensus]] work out what the factor architecture is; this page is about what gets printed beside each security's price every week, because that printed breakdown is what makes the factor architecture a display decision and not only a modelling one.

## What the ledger is

Each week, for each security, the price move is decomposed into named lines whose sum is exactly the return. The institution does not print `+1.57%` and stay silent; it prints the breakdown beside it. Worked example, reproduced verbatim from the source:

```text
LETTER  Handwritten Letter          27.43 → 27.86      +1.57%
week ending 2026-09-04

  Latency Collapse                  −0.31%
  Functional Substitution           −0.44%
  Predictive Pre-selection           0.00%
  Dematerialization                 −0.18%
  Attentional Slack                 −0.22%
  Friction Premium                  +1.86%
  Status Coding                     +0.74%
  ──────────────────────────────────────────
  Factor contribution               +1.45%
  Security fundamentals             +0.09%
  Positioning                       +0.03%
  Interaction / residual             0.00%
  ──────────────────────────────────────────
  Total return                      +1.57%
```

Each line is one multiplication: the security's assigned exposure to a factor times that factor's move for the week.

## Why it is central

The ledger lines are not internal machinery reported for completeness — they are the vocabulary of causes the work speaks in. Choosing the factor count is therefore choosing how many lines appear on screen. The same week rendered with a five-factor set collapses four distinct human changes into one line; rendered with a twelve-factor set it separates them, but thereby claims an ability to distinguish them that has to be earned.

Making the lines sum exactly is always achievable — it is arithmetic, not evidence. The real risk the ledger carries is manufacturing certainty that does not exist in order to reach an exact sum: an institution that always balances its books can do so honestly or by quietly assigning false precision to categories it cannot actually separate.

## The three layers

The worked example already displays three layers below the factor lines: **factor contribution**, **security fundamentals**, and **positioning**, plus an **interaction / residual** line. A three-layer allocation rule for routing any given event into one of these — a cause spanning several securities goes to the factor layer, a cause confined to one security goes to the security-fundamentals layer, participant crowding goes to the positioning layer, and anything fitting none of them fires `Unexplained` — was proposed by the assistant in the 2026-09-06 session. **This is an LLM proposal, not yet confirmed by the user.** It is recorded here because it is the mechanism that would make the ledger's layer structure principled rather than ad hoc, but its status should not be read as settled.

## The resolution rule

How many lines the ledger carries is a user decision: start near nine displayed factors, and let the number of ledger lines grow as the security universe grows. This makes factor count a function of universe size rather than a constant. See [[DEC-005-ledger-resolution-scales-with-universe]] for the decision itself, its rationale, and what remains open under it — principally, the promotion criterion that decides which candidate factor gets a line next is still `llm-proposed`, and the starting nine-factor set's membership is not decided.

## The user's later refinement of the promotion criterion

Later on 2026-09-06 the user stated that **factors may outnumber securities**, and that the ordering conclusion from the earlier session — which practices are listed determines which factors can exist — is the reason that is acceptable. This rejects the working ratio `K ≤ N/3` while endorsing the expressibility argument that the per-factor separability test above is an attempt to formalize. It does not confirm that test. Both positions are to be carried into the next review round as stated context. See [[DEC-005-ledger-resolution-scales-with-universe]] for the full quotation and reading.

## What `Unexplained` means here

In a real market, residual is what a model fails to explain about an *observed* price. In LONGING the price is generated by the model itself, so residual is structurally zero in that sense — there is no external observation for the model to fall short of. Nothing is "unexplained" the way a statistical residual is unexplained.

The real gap is different. Events are authored, and each one must be translated into factor moves. Some events have no word in the current factor vocabulary — `Unexplained` here names a vocabulary gap, not statistical noise.

**Worked example, including the assistant's own correction.** The initial illustration offered was the last large film-processing chain closing: cultural prestige unchanged, material preference unchanged, digital capability unchanged — what changed is whether the practice can be performed at all, described in the session as "infrastructure viability," which none of the six second-round candidate factor sets carries as a macro factor. This was first presented as a case for widening the factor vocabulary or accepting an `Unexplained` line.

On examination, the example was mis-framed. Infrastructure viability loads heavily on Film Photography, Physical Media, and Live Performance, and is near zero on Solitude or Waiting for a Reply — a factor supported on three of eleven constituents is a security-level effect, not a macro factor, for the same reason one second-round review left its own thinly supported factor unpriced (see [[factor-architecture-review-consensus]]). The ledger's three layers already have a home for this: a film-lab closure belongs in the **security-fundamentals** layer from the start, not in a new factor and not in `Unexplained`. The option initially presented as the lesser choice was in fact the architecturally correct one for that event. This correction is recorded because it is a concrete illustration of how easily an authored event gets mis-routed, and of why the routing rule matters.

## Open questions

- ~~Whether `Unexplained` is ever displayed to the viewer, or used only internally as a design instrument during construction.~~ Closed 2026-09-20: it is on the audience receipt as *unknown*. See [[DEC-011-the-audience-ledger-reads-hearts-cooling]].
- How a retracted or corrected report appears in a ledger week that has already been published — an exact-sum problem raised by the news-quality direction. See [[information-quality]].
- Whether the three-layer allocation rule survives user review, and in what form.
- Whether a per-factor separability test — a factor earns a ledger line when at least one security in the universe responds to it differently from every other factor — replaces the earlier working ratio of roughly one factor per three securities. Proposed by the assistant; not confirmed. See [[DEC-005-ledger-resolution-scales-with-universe]].
- Which nine (or so) factors form the starting ledger, which is not yet decided.
- ~~Whether "nine" counts priced factor lines or every line.~~ Closed 2026-09-20: the user said nine was an LLM proposal, not a designed number, and the count may grow as needed. See [[DEC-005-ledger-resolution-scales-with-universe]].
- ~~**The orthogonalisation order.**~~ Closed 2026-09-20 by [[DEC-010-declared-order-with-a-joint-line]]: declared and published, measured lines before estimated lines, with the order-dependent overlap carried as a `Joint` line. What remains open is how `Joint` is computed and whether it is displayed. The record of the question: the fourth round agrees the weekly split is a recursive residualisation in a declared order — numeraire, substitution, priced factors, positioning, reflexive, `Unexplained` is the order most reviewers assume — and that the order determines the split, cannot be tested from returns, and must be published. No order is chosen; the user deferred it on 2026-09-20 to a later discussion. The same day [[identification-experiment]] measured how much it matters in the generated world: swapping the schedule and factor lines shifts the schedule line's weekly attribution by 1.45 times its own size early and 0.57 late, and nearly doubles the early drift it carries.

## Evolution — the order is decided (2026-09-20)

[[DEC-010-declared-order-with-a-joint-line]] closes the order question. The split is a recursive orthogonalisation in a published sequence — numeraire, declared schedule, priced factors, positioning, reflexive, `Unexplained` — justified as *measured before estimated* rather than as a causal claim, and the ledger gains a line: `Joint`, the amount the split would move under the alternative order. This is the third distinction the page now draws. Exact accounting is the sum; causal recovery is what returns cannot give; and `Joint` is the size of the gap between them for the week, published rather than assigned. In the generated world it is large early and small late. ~~How `Joint` is computed for more than one swap~~ was decided later the same day: the range over every admissible order, per line the largest minus the smallest attribution across them, a width that does not enter the sum. Whether it is shown to the viewer was decided on 2026-09-21: it is, as a width beside each receipt line, and the ledger's blocks are fitted jointly so that order exists only between blocks — [[DEC-013-joint-shown-as-a-width-and-blocks-fitted-jointly]]. `Unexplained` is shown, by [[DEC-011-the-audience-ledger-reads-hearts-cooling]].

## Evolution — the audience receipt (2026-09-20)

[[DEC-011-the-audience-ledger-reads-hearts-cooling]] separates the ledger the engine keeps from the receipt the audience reads. The user's position is that the viewer need not know finance and that the work's purpose is recognition of romance leaving the age; the positioning line therefore stays in the engine, where every rally mechanism depends on it, and is published as *the share from hearts cooling* — romance valued less, as against romance diminished. The receipt has five audience lines over the engine's lines: technology, romance itself, hearts cooling, last week's report, unknown. `Unexplained` is displayed. The numeraire line's place on the receipt and the wording are open.

## Evolution — the width is shown and blocks are fitted jointly (2026-09-21)

[[DEC-013-joint-shown-as-a-width-and-blocks-fitted-jointly]] completes the `Joint` line. Its width is published beside each audience line, so the receipt carries, for every line, both the institute's number and how far the institute's own convention moved it. The ledger's lines are fitted in blocks: the schedule's waves together, the priced factors together, positioning, the reflexive term; order and overlap exist only between blocks. The line count the listing can carry, from round 4, is unaffected — it counts lines, and the joint fit changes how they are estimated, not how many there are. Wording, the numeraire revision's place on the receipt, and how a width is drawn remain open.

## Evolution — round 3 tests the ledger's causal language

The eight-response [[factor-set-failure-profile-review]] makes the existing arithmetic-versus-evidence distinction concrete. A fixed generator can sum more factor contributions than there are securities; uniquely recovering unrestricted unknown shocks from one cross-section is a different problem. Reviewer claims that twelve factors on eleven securities make exact accounting impossible are not adopted. The user's position that factors may outnumber securities remains current.

The useful review output is a set of contrasting events and stability tests: trust without proximity, scheduling without attention loss, supply without taste change, and crowding without changed belief. A missing common-factor name does not erase the existing fundamentals or positioning layers. Multiple legitimate effects of one event are not automatically double counting. Routing, interaction treatment, visibility of uncertainty, and line stability remain untested proposals, not confirmed mechanisms. The earlier lab-closure example's treatment in security fundamentals is preserved.

## Evolution — round 4 derives the line count from the listing

The seven-response [[factor-identification-review]] gives the ledger its first count that is not a preference. A listing of eleven practices in three markets names thirteen factor directions — one common, ten practice contrasts, two market contrasts — and the twenty remaining dimensions are single securities' own noise, which is the formal form of the *effect with ambitions* objection. Measured lines consume none of that capacity, which is how the user's position that factors may outnumber securities is read. Convergence moves the estimable lines from the market side to the practice side without changing what can be named. The promotion criterion becomes a gate battery with a post-publication check, because publication itself can create a factor once the reflexive line exists. `Unexplained` gains a mechanical role: if its cross-sectional covariance stops being near-diagonal, a line is missing and the promotion search runs. The exact-accounting-versus-causal-recovery distinction this page draws is kept and sharpened — a shared driver is not itself a double count, and exact weekly sums in a nonlinear model need a stated finite-change allocation rule. All of it `llm-proposed`; nothing on this page is adopted by it.

## Related

- [[factor-set-failure-profile-review]]
- [[factor-identification-review]]

- [[pricing-model]]
- [[information-quality]]
- [[arbitrage]]
- [[factor-architecture-review-consensus]]
- [[index-architecture]]
- [[Q-001-price-formation]]
- [[Q-004-unit-of-account]]
- [[DEC-005-ledger-resolution-scales-with-universe]]
- [[DEC-010-declared-order-with-a-joint-line]]
- [[DEC-013-joint-shown-as-a-width-and-blocks-fitted-jointly]]
- [[DEC-011-the-audience-ledger-reads-hearts-cooling]]

## Sources

- [[SRC-2026-09-06-attribution-resolution-and-universe-scaling]] — [raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md](../../raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md)
- [[SRC-2026-09-20-factor-identification-prompt]] — [raw/documents/2026-09-20-factor-identification-prompt.md](../../raw/documents/2026-09-20-factor-identification-prompt.md); the evolution note draws on the seven responses synthesised in [[factor-identification-review]]
- [[SRC-2026-09-20-round-decisions-and-deferrals]] — [raw/conversations/2026-09-20-round-decisions-and-deferrals.md](../../raw/conversations/2026-09-20-round-decisions-and-deferrals.md); nine closed as moot, the order deferred
- [[SRC-2026-09-20-orthogonalisation-order]] — [raw/conversations/2026-09-20-orthogonalisation-order.md](../../raw/conversations/2026-09-20-orthogonalisation-order.md); the order decided, the `Joint` line added
- [[SRC-2026-09-20-joint-line-as-a-range]] — [raw/conversations/2026-09-20-joint-line-as-a-range.md](../../raw/conversations/2026-09-20-joint-line-as-a-range.md); `Joint` computed as the range over every admissible order
- [[SRC-2026-09-21-joint-shown-and-blocks-fitted-jointly]] — [raw/conversations/2026-09-21-joint-shown-and-blocks-fitted-jointly.md](../../raw/conversations/2026-09-21-joint-shown-and-blocks-fitted-jointly.md); the width shown, blocks fitted jointly
- [[SRC-2026-09-20-hearts-cooling-line]] — [raw/conversations/2026-09-20-hearts-cooling-line.md](../../raw/conversations/2026-09-20-hearts-cooling-line.md); the audience receipt and the hearts-cooling line
- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-framework]] — [raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md](../../raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-prompt]] — [raw/documents/2026-09-05-pricing-model-v2-factor-review-prompt.md](../../raw/documents/2026-09-05-pricing-model-v2-factor-review-prompt.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-claude]] — [raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md](../../raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-deepseek]] — [raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md](../../raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-gemini]] — [raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md](../../raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-glm]] — [raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md](../../raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-grok]] — [raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md](../../raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md)
- [[SRC-2026-09-05-pricing-model-v2-factor-review-qwen]] — [raw/surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md](../../raw/surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md)
- [[SRC-2026-09-06-factor-set-failure-profile-prompt-v2]] — [raw/documents/2026-09-06-factor-set-failure-profile-prompt-v2.md](../../raw/documents/2026-09-06-factor-set-failure-profile-prompt-v2.md)
- [[SRC-2026-09-06-factor-set-failure-profile-chatgpt]] — [raw/surveys/2026-09-06-factor-set-failure-profile-chatgpt.md](../../raw/surveys/2026-09-06-factor-set-failure-profile-chatgpt.md)
- [[SRC-2026-09-06-factor-set-failure-profile-glm]] — [raw/surveys/2026-09-06-factor-set-failure-profile-glm.md](../../raw/surveys/2026-09-06-factor-set-failure-profile-glm.md)
