---
status: confirmed
attribution: jointly-developed
updated: 2026-09-15
sources:
  - SRC-2026-09-15-numeraire-and-standard-return
  - SRC-2026-09-15-reserve-absorption-and-trust-instruments
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-06-world-rules-letter-spec-request
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
  - SRC-2026-09-05-qwen-critic-of-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-deepseek-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-grok-critic-of-model
  - SRC-2026-09-05-gemini-critic-of-model
---

# Q-004 — What is one unit of a LONGING security?

## Answered — see [[DEC-007-standard-return-numeraire]] (2026-09-15)

The question is closed, and not by selecting among U1, U2 and U3 below. Those asked what one unit of a *security* is. The backing layer had already replaced that with the denominator question in the section below it, and that is the question the user answered.

Prices are quoted against **STANDARD RETURN** (`SR`): a fixed basket of AI-mediated acts, valued by what the basket gives back. The numeraire is countable, so float and positioning survive, and it appreciates, so the decline needs no drift coefficient. Both constraints this page placed on any later answer are satisfied — the backing is not the numeraire, since the unit is the return flow rather than the stock of trust, and BEARER BOND and BLIND TRUST share the unit.

The connected sub-question below is also closed: float is **not** the index weight. The headline index is equal-weighted, so prevalence cannot feed both the fundamental and the weight, and float is a separate quantity — outstanding BEARER BONDs, estimated rather than counted because a bearer instrument has no register.

The separate review round this page requested was never dispatched and is now moot for the question as framed. Everything below is preserved as the record of how the question stood before it was answered; U1, U2 and U3 remain unadopted.

## Current branch and narrowed dependency (2026-09-07)

**User-confirmed:** for [[reflection|사유]], connect directional exposure first to its market price, with flexibility for a later state-linked structure. This is a choice of reference, not a completed unit, contract, currency, payout, or adoption of the three earlier branches below.

The user wants to simulate the aggregate Market rather than a securities trading system and excludes investor-persona profit/loss stories from the content. A completed borrowing, counterparty, and settlement system is therefore not a prerequisite to all further price design. Quote normalization and index weighting still need definitions; any selected amplification mechanism needs enough state and constraints to explain it. Concrete design depth and financial vocabulary remain open.

U1 assessment, U2 future-practice claims, and U3 support entitlements remain unadopted comparison branches. The abstract-condition definition also removes a universal requirement that every quoted unit count a practice. Earlier contract-specific gates remain relevant only if that branch is later chosen. The separate unit review was requested previously but has not been dispatched, and its brief would need this updated scope.

## The backing layer sharpens this question (2026-09-15)

LONGING now owns a backing layer: what a romantic good rests on, and where that backing goes. See [[reserve-instruments]] and [[DEC-006-reserve-function-absorbed]].

It does **not** answer this question, and the reason is exactly the failure the originating premise ran into. If the traded good and the thing backing it are made of the same substance, both sides of the ratio move together and the quote does not move at all. A price only exists once the two are separable and separately named. So the backing layer converts "what is one unit" from a weighting problem into a **denominator** problem: a LONGING price is a ratio between a romantic good and something else, and that something else is still unnamed.

Two constraints the backing layer adds to any answer chosen later:

- **The numeraire cannot itself be love, understanding, or trust.** Those are the backing. Pricing the backing in the backing yields a constant.
- **BEARER BOND and BLIND TRUST are denominated in the same unit as each other**, since the world's central comparison is between their risk and yield. Whatever the unit is, it has to survive that comparison.

An `llm-proposed` route not taken: price the decline in an appreciating numeraire — speed, certainty, immediacy — so romance did not get cheaper, the yardstick got heavier. Recorded as an alternative to the branches below, not adopted.

## The question

The original reviews asked what underlies a share price. LONGING still has no selected answer to the equivalent question; the 2026-09-06 design below now specifies alternatives and their consequences:

> What is one unit of `LTR`?

One letter? One person who writes letters? One annual practice instance? One hour of practice? One participant-year? One unit of attention?

Until that is answered, several things downstream are unstable: index weighting has no principled basis, "market capitalization" has no analogue, positioning and short interest have nothing to be a fraction *of*, and a short squeeze is an arbitrary force rather than a consequence of finite supply.

This question was not raised by the user. It surfaced in the 2026-09-05 reviews, where one review named it the single biggest weakness in the design and three others reached it independently from the index-weighting side. It is recorded here because it blocks [[index-architecture]] from publishing a composition.

## Why the reviews split on it

They agree the problem is real and disagree completely on whether to solve it or refuse it.

**Define the unit.** Qwen proposes a standardized **Practice Unit** per security — one non-institutional handwritten letter sent, one hour of non-utilitarian night walking, one unarranged in-person visit — and then `Practice Capitalization = Market Price × Modelled Practice Units`, capped at 10–15% per constituent, with divisor continuity. GLM's variant weights by **footprint** (practising population × frequency, re-measured annually with buffer bands, tagged `MODELED`), on the precedent of fundamental indexing.

This has a genuinely good property. As a practice becomes rare, price per unit may rise on scarcity while units outstanding fall — so the aggregate can decline even as the security rallies. *A thing can appreciate as an object of longing while the total value of the practice collapses.* GLM adds the quiet detail that annual re-measurement makes the weights lag the world by a year: the benchmark of human longing always updates one year behind the world that is killing it.

**Refuse the unit.** Claude, Kimi, and Grok argue the opposite, and their objections are specific rather than squeamish:

- **Double counting.** Prevalence would feed the fundamental *and* the weight, so the same decline is counted twice, in opposite directions.
- **Fabrication.** Credible long-horizon prevalence series do not exist for most of these securities, and constructing them means inventing numbers that look like measurements — the exact failure mode the work is trying to avoid.
- **It damps the signal.** Cap-weighting shrinks the weight of decliners, so a cap-weighted LONGING index would fall *less* than its average constituent. The opposite of what the work is showing, achieved by accident.

Their alternative is **equal weighting**, with an institutional position attached that is worth as much as the arithmetic: *a research institution that declines to rank human experiences by importance.* Kimi adds that LONGING is not an investable benchmark — no capital tracks it — so there is no reason for size to determine weight at all.

Gemini takes a third route: keep a size measure but make it **Total Attentional Float** — the total time and frequency people physically spend on the practice.

## The proposal that dissolves the disagreement

Claude's compromise is the only one that lets both answers coexist: an **equal-weighted headline index**, plus a **prevalence-weighted secondary index covering only the handful of securities where real public data genuinely exists** — postal volume, film sales, landline minutes — with its narrow coverage stated honestly.

The spread between the two then becomes the interesting output rather than a methodological embarrassment: is the decline concentrated in practices people have already abandoned, or is it broad-based across everything? The institution does not have to interpret it. It only has to print it.

## The connected sub-question

Positioning needs supply too. Several reviews note that "78% short interest" is meaningless without a float, and propose defining a notional supply per security so that positioning is a fraction in `[−1, +1]` and covering flow has something to exhaust. Whether that float should be the same quantity as the index weight, or a deliberately separate fiction, is unresolved.

## The user's instruction on how to resolve it

On 2026-09-06 the user directed that this question be put to the review models as its own round, in the way the pricing model and the factor architecture were:

> "1주가 대체 무엇이냐."에 대해서는 LLM들에게 의견을 구해봐도 좋을 것 같아.

This is an instruction about method, not about content. The user stated no position on the question itself, and none of the answers below has gained standing. What changes is that the question moves from a blocker being carried to a work item with a defined next action.

Two constraints the round should be built to respect, both already in the repository. First, the review set has already split cleanly on this question — define the unit, refuse the unit, or run both indices side by side — so a round that simply re-collects those three positions adds nothing; the useful question is what each choice makes impossible downstream. Second, the question has since acquired a second dependant: [[arbitrage]] needs a finite thing to hold before a position can exist at all, which is an argument for the unit that did not exist when the reviews split.

## Evolution — three executable meanings to compare (2026-09-06)

**Previous state:** this page held names for possible practice units, a disagreement over weights, and the requested model-review round. **Transition:** the user asked for concrete world rules and LETTER dynamics and explicitly required consequences for price, indices, positions, arbitrage, and the work's meaning. **Current state:** the alternatives below are specified enough to expose their costs; all are `llm-proposed` and no selection or external review has occurred in this task. The separate review request remains outstanding.

Read [[world-rules]] for the common population and actor rules and [[letter-practice-dynamics]] for the qualifying-send boundary. A LETTER coverage page and a dated financial claim on LETTER need different identifiers. The former can persist after the latter matures.

### U1 — A quoted reference with no owned share

**Object:** an institutional assessment of LETTER practice in a named population over a rolling 52-week horizon. There are no issued shares. A published level of 100 at the reference date is an assessment baseline; one point is one hundredth of that baseline assessment, not one letter, person, hour, or currency unit. A concrete trial appraisal could use expected next-52-week qualifying sends: `F_t = 100 × E_house[L_(t,t+52)] / L_reference`, with `L_reference` fixed and positive. A different functional including persistence, effort, scarcity, or relational breadth would change what the quote measures and must be declared. This behavioral trial functional is an option, not the adopted value bridge.

`P_t` would be a separately published assessment of the same object under a stated belief-aggregation rule, on the same point scale. The next stage must explain that rule; calling it a market price does not create transactions. A quote of 27.43 under the simple behavioral functional expresses an assessed 27.43% of the reference annual send count. It is neither a payment nor the value of an individual letter. A viewer's LONG stance is a dated view, with no payout or obligation.

**Finite resources and positions:** fictional research participants can have finite time or conviction budgets for producing forecasts, but there is no owned asset or counterparty. A `61% LONG` statistic can mean share of recorded opinions. It cannot mean 61% of float, open interest, capital at risk, or short interest. No short squeeze is available until another instrument and funding rule are introduced.

**Index:** a fixed, equal-weighted set of normalized quote levels has a coherent meaning as breadth of institutional assessments. Practice volume can be shown separately. There is no market capitalization because there is no issued supply. Multiplying an assessment by current volume is allowed only as a separately named aggregate with an explanation of why volume enters both price and weight; it does not become market capitalization by naming it so.

**Arbitrage and meaning:** disagreeing with the house can lead to a contrary forecast and eventual evidence, but there is nothing to buy, sell, redeem, or settle. A gap between `P` and `F` is disagreement; closure is information-driven convergence, not an arbitrage payout. This branch makes the institution's act of pricing the central fiction. It preserves the viewer's distance but gives up a literal finite-position market. It is the recommended smaller publication rehearsal, not a way to claim that arbitrage has already been designed.

### U2 — A fully funded claim on a dated practice outcome

**Object and unit:** one `LETTER-[period]` claim pays an amount determined by the qualifying sends from the declared cohort during a fixed 52-week window. Let `L_T = sum(Q_t)` over that window, using the LETTER specification's dispatch boundary. The proposed bounded payout is:

```text
LONG payout g(L_T) = 100 × min(L_T / K, 1) fictional clearing credits
Complementary payout = 100 − g(L_T)
```

`K` is frozen at issue. The illustrative choice `K = 10,000 qualifying sends` means one claim pays 0.01 credit per eligible send, capped at 100 credits. Thus 4,000 sends produce 40 credits, 10,000 produce 100, and 12,000 still produce 100. **This is a contractual scale example, not a forecast, calibration, or proposed observed count. It fails the companion LETTER baseline:** about 416 sends/week would produce 21,632 over 52 unchanged weeks, reaching the 10,000 cap around week 25. All later changes would then leave this claim's payout unchanged. A trial `K = 40,000` places that unchanged-flow outcome at 54.08 credits and delays saturation, while scaling down the credit response per letter. It still has a ceiling and is not a selected threshold. No person is sold and no holder acquires a letter, a relationship, a vote over writers, or the right to require someone to practise.

**Funding and counterparty:** each newly matched LONG/complement pair requires 100 credits in a separate clearing trust. If the LONG price is `P`, its buyer contributes `P` and the complementary claimant contributes `100 − P`. Credits cannot be created by recording a stance. Each participant has an initial finite budget; no borrowing, leverage, or uncovered issuance is assumed. Transfer of an existing claim exchanges credits between participants without adding collateral. New pairs require new collateral. At maturity the trust distributes exactly the 100 credits per pair and retires it. The counterparty is another funded claimant, backed by that escrow; the writer and the research house owe no payout.

For example, at `P = 27.43`, the LONG side spends 27.43 and the complementary side spends 72.57. If the eligible outcome is 4,000 sends under the illustrative threshold, payouts are 40 and 60; gains before any costs are +12.57 and −12.57. The opposite loss occurs for a sufficiently low outcome. Full funding bounds the payout obligations; it does not remove outcome risk.

**Quote and institutional value:** `P` is credits per LONG claim at the weekly close. `F = E_house[g(L_T)]` is the house's estimate of that payout under its information. The institution's expectation, analyst price targets, and participant bids are different records. A reader can believe a letter has exceptional human value while expecting the claim to lose money. Conversely, a concentrated increase in letters from a small group can raise expected payout while the practice reaches fewer people.

The weekly price-formation rule remains to be specified. It must use funded, feasible positions and preserve the directed role of monthly research in the anchor. It cannot derive a fabricated transaction from a target-price average. No matching algorithm, participant population, budget distribution, or transaction volume has been adopted here.

**Positioning denominator:** each outstanding pair has one LONG claim and one complementary claim, so total claims on both sides are mechanically balanced. “The whole market is net 78% short” is not a meaningful consequence of this construction. Crowding can instead describe concentration by participant group, how much uncommitted capital remains on each side, or the distribution of directional portfolios. State the numerator and denominator. Closing may require a willing transferee; full collateral does not guarantee an exit price. The fully paid complementary claim is bearish exposure, not a borrowed short. It has no forced margin call or buy-in, so the earlier squeeze story is not inherited automatically. Voluntary belief reversal and thin offered inventory may reprice a claim; forced covering needs a separately designed obligation and cannot be asserted from this contract alone.

**Index:** issued claim count is demand for risk exposure, not the size of human practice. `P × outstanding claims` would be the market value of outstanding contingent exposure, not the cultural capitalization of LETTER. Prefer an equal-weighted research composite of normalized prices, with an independent behavior series. A dated claim becomes less forward-looking as it matures; a rolling headline needs a declared maturity/roll policy and continuity adjustment. Show roll effects and membership changes separately. Do not label a constructed rolling quote series an investable portfolio return without specifying the required holdings and funding. Zero-price and unavailable-quote handling are additional methodology choices. The same maturity issue applies to analyst targets: a fresh twelve-month target on an already issued 52-week claim extends beyond its life. Specify a shorter valid horizon, a future vintage, or a constant-maturity target and score that same object.

**Arbitrage:** buying because `P < F` is a risky forecast trade. It can lose because the house is wrong, the eligible release differs from underlying behavior, the cap binds differently, or exit liquidity is absent. The outcome is not contractually `F`.

Strictly offsetting trades exist only where contractual equivalence exists. Under the designed complete-set rule, a matched LONG and complement can be surrendered together for their 100 credits of collateral. If independently offered executable prices sum below 100, buying both and surrendering the pair leaves a positive credit difference before costs. Conversely, a participant able to fund and sell a newly created pair for more than 100 can retain the difference. Both examples need simultaneous feasible execution, identical settlement terms, sufficient inventory/collateral, and costs below the difference. A single matching rule that enforces `P + P_complement = 100` prevents this opportunity. A second venue quoting the identical claim could supply another equivalent-payout comparison, but no second venue has been adopted. The work must decide whether it wants a visible constrained relative-value trader, an occasional strict arbitrage opportunity, or both.

**Settlement gate:** a real statistical truth and a contract's administratively eligible outcome are different. Choose who publishes `L_T`, which observation/estimate qualifies, how late reports are handled, when a release becomes final for payout, and what happens if evidence never arrives. A private author-known true count may be useful in a test; giving it to the clearing trust would eliminate precisely the observation problem the fictional institution is meant to face. No settlement is operational before these choices are made.

**Choice of outcome within U2:** cumulative sends reward both participation and intensity, and may be dominated by a few prolific writers. Qualifying practitioner-weeks (each sender counted at most once per week) limit that concentration but ignore additional letters and still differ from ongoing latent episodes. Mean ongoing practitioners would include weeks with no dispatch and require a stronger observational claim about intention. A 52-week terminal continuation count emphasizes persistence at one boundary and can miss substantial activity earlier. The recommendation is to use cumulative sends for the first contract comparison because it matches the operational flow already defined, while publishing breadth alongside it. The user still needs to select what the financial claim should reward.

**Meaning and recommendation:** U2 makes it possible to profit from forecasting a practice's future without loving it and to lose money while correctly recognizing its human importance. It supplies finite fictional resources and counterparties while the artwork remains a research house with a stance-only audience. Recommend this as the full-world direction if finite positions and arbitrage are central. Its costs are substantial: a bounded outcome, expiry/roll mechanics, settlement authority, and the narrowing of price toward measurable activity. The saturation example demonstrates why the threshold cannot be an invisible tuning knob. In this trial market participants are separate from cohort practitioners and cannot commission, finance, or direct dispatches to alter payout; relaxing that boundary would introduce a market-to-practice incentive or manipulation loop, beyond the selected task's practice-feedback requirement.

### U3 — A transferable entitlement to finite support capacity

**Object and unit:** one dated certificate grants one person-hour at a designated writing room, a stated paper/material allowance, and dispatch of one qualifying physical message during that period. It is a claim on an enabling service supplied by a fictional independent capacity provider. It is not a claim on the recipient, the writer's inner experience, or proof that a letter will actually be sent. The provider commits, for example, 1,000 person-hours for one month; this round number is a capacity fixture, not measured demand.

**Conservation and counterparty:** each dated entitlement is in exactly one state: available/unallocated, held, reserved for redemption, redeemed, or expired. The total of those states equals the issued service capacity; transferred certificates change holder, not total supply. A new month's capacity is a new issue. Provider receipts and the service obligations are tracked separately from available market participants' credits. The provider is responsible for the service; holders retain the option not to use it. A failure to deliver needs a specified replacement/refund rule before a functioning quote can be published.

**Price, value, and positioning:** `P` is credits per service entitlement and `F` is an institutional estimate of that entitlement's service value. A holder may buy to redeem, to transfer later, or to keep capacity available for someone else. Owned supply and outstanding unused capacity give a real float. Ordinary SHORT would require a borrow/return arrangement or a separately funded claim against the service price; neither comes for free from a SHORT label. No leverage or borrowing is assumed in this branch.

**Index:** `P × unredeemed issued units` measures the market value of remaining service entitlements. It can fall as capacity is consumed even when practice is healthy, so it is a poor unqualified extinction indicator. Equal weights across services avoid a large writing-room program dominating the index, but cannot make an hour of one practice's support identical to another's. A scarcity premium can raise an entitlement's price while fewer people can access the enabling service. That is a concrete institutional conflict rather than a rule that rarity itself makes every letter valuable.

**Arbitrage and feedback:** identical transferable entitlements with the same provider, date, and terms could be bought and sold across two venues if an executable price difference exceeds costs. Different rooms, hours, delivery quality, or availability are not identical claims. A price–model gap remains a risky service-demand judgment. Redemption changes access conditions and may affect LETTER starts or continuation; sales proceeds might fund future capacity only through an explicit provider budget rule. These mechanisms add a market-to-practice loop and alter the work's scope. They are separate from audience voting and from the practice feedback required in [[letter-practice-dynamics]].

**Meaning:** U3 asks which conditions people fund or reserve so a practice can remain possible. It creates an allocation institution with distributional consequences. This is a valid alternative, but it shifts attention from research about disappearance toward who controls support. It is not recommended as the first branch unless that change is desired.

### Selection rule and unresolved work

Do not combine the unit of one branch, the capitalization of another, and the squeeze of a third without explicitly designing the connecting contracts. U1 needs an appraisal rule; U2 needs an outcome, a prospectus, settlement, budgets, and maturity treatment; U3 needs enforceable capacity and redemption rules. None resolves whether scarcity belongs in a human-value estimate by itself. Keep the behavior series available independently of price under every branch.

The requested next review can use these concrete branches to ask what each makes impossible, especially the narrowed meaning of value in U2 and the intervention authority in U3. The current task prepares that decision; it does not select a financial mechanism by implication or dispatch another model-review round.

## Why it matters

This is the question that decides whether LONGING's indices are *constructed* or merely *asserted*. It also decides how much fiction the work has to manufacture: a practice-unit universe requires inventing a plausible number for every security, and every one of those numbers is a place where the artist's hand can be found.

## Related

- [[world-rules]]
- [[letter-practice-dynamics]]
- [[index-architecture]]
- [[pricing-model]]
- [[arbitrage]]
- [[model-review-consensus]]
- [[data-sources]]
- [[Q-001-price-formation]]
- [[Q-002-listing-lifecycle]]

## Sources

- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md); ChatGPT export, 2026-09-06–07; user turns support decisions, assistant synthesis and mechanisms retain proposal status

- [[SRC-2026-09-06-world-rules-letter-spec-request]] — [raw/documents/2026-09-06-world-rules-letter-spec-request.md](../../raw/documents/2026-09-06-world-rules-letter-spec-request.md); exact request for concrete unit alternatives and downstream consequences; U1–U3 are new LLM proposals, not adopted mechanisms
- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md)
- [[SRC-2026-09-05-qwen-critic-of-model]] — [raw/surveys/2026-09-05-qwen-critic-of-model.md](../../raw/surveys/2026-09-05-qwen-critic-of-model.md)
- [[SRC-2026-09-05-claude-critic-of-model]] — [raw/surveys/2026-09-05-claude-critic-of-model.md](../../raw/surveys/2026-09-05-claude-critic-of-model.md)
- [[SRC-2026-09-05-glm-critic-of-model]] — [raw/surveys/2026-09-05-glm-critic-of-model.md](../../raw/surveys/2026-09-05-glm-critic-of-model.md)
- [[SRC-2026-09-05-deepseek-critic-of-model]] — [raw/surveys/2026-09-05-deepseek-critic-of-model.md](../../raw/surveys/2026-09-05-deepseek-critic-of-model.md)
- [[SRC-2026-09-05-kimi-critic-of-model]] — [raw/surveys/2026-09-05-kimi-critic-of-model.md](../../raw/surveys/2026-09-05-kimi-critic-of-model.md)
- [[SRC-2026-09-05-grok-critic-of-model]] — [raw/surveys/2026-09-05-grok-critic-of-model.md](../../raw/surveys/2026-09-05-grok-critic-of-model.md)
- [[SRC-2026-09-05-gemini-critic-of-model]] — [raw/surveys/2026-09-05-gemini-critic-of-model.md](../../raw/surveys/2026-09-05-gemini-critic-of-model.md)
