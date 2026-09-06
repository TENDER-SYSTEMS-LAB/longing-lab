# 2026-09-06 — Arbitrage, News Quality, and Next Work Items

Compiled record of a working session held after the ledger-resolution session of the same day. This is not a byte-exact export: the session began with the user asking for successive plain-language explanations of the pricing model (an ELI5 walkthrough for a fifteen-year-old, a follow-up on the symbols `K`, `N`, and `κ`, and a full enumeration of every formula in the corpus explained for a reader with no finance background). Those explanations restated material already in the Wiki and are not reproduced here. What is reproduced is the substantive turn at the end of the session, in which the user proposed two new mechanisms and set three work items.

The user's statements are reproduced verbatim in Korean. Everything attributed to the assistant is paraphrase.

---

## 1. The explanation pass (context only)

The user asked, in sequence:

> 지금까지 결정된 LONGING 작품에 사용할 가격 결정 모델을 15살에게 설명해줘.

> 이전 대화들에서 가격 결정 모델을 설명하는서 너가 K, N 과 같은 단어들도 등장했는데 그건 뭐야?

> 해당 작품에 등장하는 모든 수식을 하나하나 나열한 뒤 금융을 하나도 모르는 20살에게 설명해줘.

The assistant answered from the existing Wiki and raw corpus. The third answer enumerated every formula registered in the repository across the draft conversation, the seven first-round reviews, and the six second-round reviews, grouped by layer, each with its source and status.

No new claim about the model was made in this pass. Its relevance to the record is that the user's subsequent proposals were made immediately after seeing the whole formula set laid out at once, and two of the three work items are legible as responses to gaps visible only at that scale.

---

## 2. Arbitrage as a world-building element (user)

> 차익거래를 해당 세계관에 추가하면 재미있겠다. 차익거래가 LONGING 세계관에서 어떻게 구현되는지 보는것도 재미있는 요소일 것 같아.

Stated as an interest, not a specification. The user's framing is explicitly about the fiction — what arbitrage *is* inside a market whose securities are human practices — rather than about the pricing equation alone.

Note on what already exists: the corpus already contains a *limits to arbitrage* mechanism, proposed by Claude in the first review round, in which the mean-reversion coefficient is scaled down by crowding, `κ = κ₀ × (1 − |crowding|) × evidence_arrival`. That mechanism explains why mispricings persist. It does not depict an arbitrageur, and nothing in the corpus says who takes the other side of a LONGING trade, what a position costs to hold, or what it would mean to close one. The user's proposal is the affirmative case that mechanism presupposes.

---

## 3. News quality as a modelled layer (user)

> 뉴스는 한번에 공개되기도 하지만, 오보 되기도, 과대/과소 보도 되기도 하고, 큰 뉴스가 찌라시처럼 미리 시장에 돌아다니기도 한다. 이것도 모델에 추가하면 재미있을 것 같아.

Four distinct information behaviours are named:

1. Clean disclosure — an event becomes known at once.
2. Erroneous reporting (`오보`) — a report that later turns out to be false.
3. Over- and under-reporting — a report whose magnitude does not match the event.
4. Pre-circulation as rumour (`찌라시`) — a large event leaking into the market ahead of its formal disclosure.

Note on what already exists: the second and fourth items have no representation anywhere in the corpus. The third is partly reachable through the existing surprise framing. The event layer as recorded already holds two relevant rules — that only the surprise moves price, and that confidence should scale the *speed* at which an event is priced in rather than the size of the move, so a low-confidence event bleeds in over several weeks and can reverse if unconfirmed. That second rule is the nearest existing structure to what the user is describing, but it models uncertainty about an event that is nonetheless true. Nothing currently models a report that is simply wrong.

---

## 4. Q-004 to be put to the review models (user)

> "1주가 대체 무엇이냐."에 대해서는 LLM들에게 의견을 구해봐도 좋을 것 같아.

An instruction about method rather than content: the unresolved unit-of-account question should be sent out as its own review round, in the way the pricing model and the factor architecture were. The user did not state a position on the question itself.

---

## 5. Factors may outnumber securities (user)

> "DEC-005로 확정된 것: 9개 근처에서 시작, 종목 늘면 줄 수도 늘린다. 어떤 9개인지는 미정." 이라고 했어. 근데 나는 종목보다 팩터가 더 많아도 될 것 같아. 그래서 너가 정리해준것처럼 "어떤 실천을 상장하느냐가 어떤 팩터가 존재할 수 있는지를 결정"하는 방식이어야해. 다음 모델링에서 LLM들에게 의견을 구할 때 참고해줘.

Two things, stated together.

First, a position on the identification constraint: the user is willing to have more factors than securities. This is a direct rejection of the working ratio proposed by Claude in the second round, `K ≤ N/3`, under which eleven securities support roughly four factors and forty-five support roughly fifteen. The user does not dispute the reasoning recorded against raising the security count; the position is that the factor count should not be capped by the constituent count.

Second, an endorsement of the ordering conclusion reached in the previous session, quoted back to the assistant: which practices are listed determines which factors can exist, rather than the reverse. The user attaches this as the *reason* the first position is acceptable — the constraint that matters is whether the listed universe can express a factor, not how the two counts compare numerically.

Third, an instruction: carry both into the next review round as stated context.

---

## 6. Check the academic literature (user)

> 그리고 우리가 모델링하려고 하는것이 이전에 학술적인 연구등으로 이미 정의가 되어지고 있는것들이 있는지 확인하고 참고해보는 것도 다음 할일로 정리해야해.

A work item: determine whether what LONGING is modelling has already been defined in academic research, and consult that work. The existing `prior-art` page covers comparable *artworks* only; nothing in the repository has surveyed scholarship.

---

## 7. Recording instruction (user)

> 이 내용도 wiki에 추가되면 좋을 것 같아.

---

## Status of the material in this record

Stated by the user as directions or positions:

- Arbitrage should be represented in the work; how it is implemented in this world is itself of interest.
- News quality — misreporting, over- and under-reporting, and pre-circulating rumour — should be added to the model.
- The unit-of-account question should be put to the review models.
- Factors may outnumber securities; listing choice determines which factors can exist; both are to be carried into the next review round.
- Academic prior art is to be checked as a next work item.

None of these is a specified mechanism. No mechanism for arbitrage or for news quality was proposed by either party in this session, and the user stated no position on the unit-of-account question itself.

Proposed by the assistant and not confirmed by the user: nothing in this session. The assistant's contribution was the explanation pass and the observation of where each proposal does and does not overlap existing material.
