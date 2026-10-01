---
status: confirmed
attribution: user-confirmed
updated: 2026-10-02
sources:
  - SRC-2026-10-02-no-listing-and-a-stopped-price
---

# DEC-015 — Nothing is listed, and a price that stops stays where it stopped

## The decision

After gap G3 lost its grounds ([[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]), the assistant proposed folding it into the open question of who lists a security ([[Q-002-listing-lifecycle]]). The user questioned listing itself ([[SRC-2026-10-02-no-listing-and-a-stopped-price]]):

> 실제 세계에서는 어떤 낭만적인 것들은 누군가가 상장하지 않는다. 그냥 존재했다 이전부터.
> 우리가 주식 시장을 대할 때도 대부분의 종목들은 이전부터 그냥 존재했다. 언젠가 어느시점엔가 상장했겠지만, 대부분의 경우 우리는 이를 무시한다.
>
> 따라서 상장이라는 개념을 꼭 세계관에 가져와야하나 싶다.

The assistant proposed one sentence to record: listing is not kept in the world; securities are there from the start; disappearance and return are handled through the BEARER BOND; the institution's side is handled as coverage. The user accepted it and added three things:

> 응 그렇게 기록해줘. 단, 관객의 경험으로 coverage가 사라진 종목도 그래프와 거래량을 확인할 수 있게는 해줘.
> 거래가 없어졌으니 가격이 0으로 변경되지는 않겠지만, 그래도 뭔가 가격이 0이 아닌 상태로 멈춰있는것도 철학적이고 감상 포인트가 있을 것 같아.
>
> 밑에 보조지표로 거래량이 표시될거니 자연스럽게 사람들은 거래가 줄어서 가격이 멈췄구나라고 생각할거임.

**`user-confirmed`:**

1. **Listing is not a concept of the world.** Nobody listed a romantic thing; it existed from before. A security is there when the record begins, as most securities in a stock market are simply there for the people who look at them.
2. **Disappearance and return are handled through the BEARER BOND.** The bond is issued by the person who leans ([[DEC-008-bearer-bond-is-perpetual]]). When trading in a security ends, its price stops. When someone leans again, a bond exists again. No committee admits or re-admits anything.
3. **The institution's side is coverage.** LONGING RESEARCH is a research house ([[DEC-002-research-house-form]]); what it does to a security is cover it or stop covering it.
4. **A security whose coverage has ended stays visible.** The audience can still open its graph and its trading volume.
5. **A price that stops does not become zero.** Trading has ended, so the price is not moved to zero. It stays stopped at a level that is not zero. The user's reason: a price resting at a level that is not zero is philosophical and something to contemplate.
6. **Volume is shown beneath the price as a secondary indicator.** The audience is expected to read from it, without being told, that the price stopped because trading dried up.

Part 5 amends the assistant's proposal, which had said a security with no outstanding bond has no price.

## Accepted inside the proposal, not separately stated by the user

These stood in the body of the answer the user accepted. The user's acceptance quoted the one sentence above, so they are recorded as the assistant's wording, `llm-proposed`, uncontested:

- **Gap G3 needs no separate answer.** Nobody inside the world agrees to the weights or publishes a method of setting prices. The execution and judgment weights sit in LONGING RESEARCH's own description of a security it covers. The price is formed apart from that description, by the market.
- **Gap G2 is not a rule of the world.** What may become a security is the user's criterion for choosing securities, outside the fiction.
- **The listing question is absorbed by gap G4**, how a security relates to its outstanding BEARER BONDs.
- **A price of 100 is set where the record begins**, as an index has a base date, instead of "at listing" as [[DEC-007-standard-return-numeraire]] words it.

## Why rejected — listing, the committee and re-admission

The listing and quotation states, the Methodology and Listings Committee, the four-release admission test, the thirteen-week delisting review and re-admission, all on [[Q-002-listing-lifecycle]], were `llm-proposed` trial specifications of 2026-09-06 and were never selected. They are now `rejected`. The reason is the user's: a listing is an event the people who look at a market ignore, and a romantic thing was never admitted by anyone. The separation of practice, observation and coverage on that page is not rejected by this decision.

## Not decided

- **What volume counts.** [[DEC-003-weekly-market-monthly-research]] rejected real-time pricing because it would need fabricated volume and a fabricated order book. A weekly volume therefore has to come from something the model already carries. The week's BEARER BOND issues and calls are a candidate, `llm-proposed`, not selected.
- **When a price stops.** Whether that is the week no bond is outstanding, the week nothing trades, or something else. This belongs to gap G4.
- **Whether a price can reach zero while it is still traded.** In [[loop-simulation]] easily substituted securities reach a numerical zero through the price formula. The user's statement covers a price that stops because trading ended; a zero produced by the formula is not addressed.
- **How coverage ending and a price stopping relate.** The user speaks of them together. Whether they are one event or two, and what ends coverage, is open.
- **What a return does.** How the price moves again when someone leans again, and whether coverage resumes.
- **The index.** What a stopped security does to an index it belongs to.
- **The `Coverage Discontinued` page.** [[system-grammar]] has the page end there. With part 4 the graph and volume stay reachable; the page's form is not redrawn.

## Related

- [[Q-002-listing-lifecycle]]
- [[DEC-008-bearer-bond-is-perpetual]]
- [[DEC-002-research-house-form]]
- [[DEC-003-weekly-market-monthly-research]]
- [[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]
- [[system-grammar]]
- [[current-state]]

## Sources

- [[SRC-2026-10-02-no-listing-and-a-stopped-price]] — [raw/conversations/2026-10-02-no-listing-and-a-stopped-price.md](../../raw/conversations/2026-10-02-no-listing-and-a-stopped-price.md); no listing, BEARER BOND and coverage, a stopped price that is not zero, volume beneath the price
