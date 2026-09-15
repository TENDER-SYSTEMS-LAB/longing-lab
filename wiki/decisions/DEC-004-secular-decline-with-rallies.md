---
status: confirmed
attribution: user-confirmed
updated: 2026-09-15
sources:
  - SRC-2026-09-15-reserve-absorption-and-trust-instruments
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
---

# DEC-004 — LONGING is a secular bear market, inverted

## The decision

The user stated the market's long-run shape and the reason for it:

> 기본적으로 사람들이 "그래도 시장은 우상향이야" 라는 잠재적인 믿음이 있는것이 있지. 그런데 낭만은 실제로 사라져가고 있다고 난 생각해. 그래서 LONGING 세계관에서는 우하향 하는걸로 그려져야 할거 같아.

And, in the same message, the inversion that gives the shape its texture:

> 단, 우리 세상에서도 완만한 상승이나 지수적인 상승이후에도 가격조정이라 급락과 같은걸로 시장이 떨어지는데, 이걸 LONGING 세계관에서는 완만한 가격상승, 급등 등으로 표현하는 것도 재미있을 것 같아.

So: **a long decline, punctuated by sharp rallies.** Real markets are believed to rise over time and are interrupted by crashes; LONGING declines over time and is interrupted by melt-ups. The mirror is exact, and it is deliberate.

## The constraint attached to it

The decision came with a design rule that matters more than the shape itself, stated plainly in the conversation: **the decline must not be a hard-coded drift.**

```text
weekly_drift = -0.3%     ← rejected
```

Instead the structural forces of the world rise — automation, immediacy, mediation, predictability — most securities hold negative exposure to them, and the decline is what falls out. The difference is the difference between two sentences:

> "낭만은 반드시 죽는다."

and

> "현재 세계의 방향으로 계산해보니 계속 떨어지고 있다."

The second leaves the work asking rather than arguing, which is the point of [[Q-003-calibrating-the-bias]]. It also means that if the world's direction genuinely changed, the model would have to produce a bull market. That possibility must exist.

## What the market's psychology becomes

Real markets carry an unspoken belief that things rise in the long run. LONGING's participants carry the opposite one — *longing declines over time* — nobody declares it, and everybody acts on it. So a rally is met with suspicion rather than hope: not "is this the turn?" but "how long will this one last?" Priced through, it becomes a **bearish asymmetry** — good news is discounted, bad news is over-absorbed.

The market history can then carry named rallies, the way real markets carry named crashes:

```text
2007–2009   THE ANALOG REBOUND
2019–2020   PHYSICAL MEDIA RALLY
2027        THE LETTER REPRICING
```

Each looked at the time like the end of the structural decline. Seen years later on the chart, each was a rebound inside it — or, in some case not yet written, was not. The research house cannot tell which in advance either.

The emotional consequence the user identified: on a normal financial chart the eye expects the top right, so here the eye slowly learns to expect the bottom right, and the moment worth clicking becomes the sudden spike. *What happened then?* Each of those spikes is a small story about something briefly coming back.

## How the reviews say to keep it honest

All seven reviews accepted an emergent secular decline as reasonable, and several supplied concrete tests for whether it looks manipulated. Recorded here because they constrain how the decision gets implemented, though none is itself decided:

- **Publish the drift parameter** with its rationale, as an index provider publishes rules.
- **Keep structural winners in the universe** — 15–25% of securities with positive or near-zero rate sensitivity, such as solitude, handmade objects, live performance. A universe where everything declines is a tautology a viewer decodes in thirty seconds.
- **Publish a neutral-drift companion index** at zero drift beside the headline, so the audience can subtract the thesis and see what remains.
- **The model must be able to disagree with the artist.** The sharpest form of this test: film photography and vinyl genuinely revived in the real world, so if `FILM` cannot stage a multi-year bull market inside the model, the model is rigged.

Three rally engines at three speeds were identified, none requiring special-case logic: weeks — crowded-short squeezes in illiquid names; months — the macro factors decelerating; years — a genuine revival, incidence beating expectations quarter after quarter.

## Status

Confirmed as direction. The user stated both the decline and the inversion as their own view of the world, and the no-hard-coded-drift constraint was accepted in the same exchange. The mechanism that delivers it is not decided — see [[pricing-model]].

## Related

- [[pricing-model]]
- [[model-review-consensus]]
- [[index-architecture]]
- [[Q-003-calibrating-the-bias]]
- [[overview]]

## Evolution — the bias belongs to the chosen history (2026-09-07)

The user now explicitly chooses fictional historical data biased toward human conditions diminishing, with the market model producing prices from that history. The final turn reaffirms sideways periods, short rises, and sharp moves; prices do not fall linearly. The opening brief retains the requirement that changed conditions permit maintenance and recovery under the same rules.

Together these specify an authored declining history without requiring an engine that falls under every input. This is **user-confirmed direction**, not adoption of any factor set, drift coefficient, synthetic generator, or price equation. The named rally dates above remain illustrative history, not the chosen historical span.

The user also wants HOLD/SHORT reports to have the stronger accumulated win record in that market history. [[analyst-system]] owns this outcome direction and the unresolved definition of a win; it is not a fixed ranking for the proposed named analysts.

## Evolution — the decline acquires a structural cause, and nobody argues it (2026-09-15)

This decision already required that the decline **emerge** rather than be imposed, and left open what structural forces would deliver it. The 2026-09-15 conversation supplies a candidate cause and one further constraint.

**The cause.** Trust between people leaves for AI, and the total falls at the same time, because unilateral trust creates no new trust the way bilateral trust did. [[reserve-instruments]] owns the mechanism; [[DEC-006-reserve-function-absorbed]] owns the decision to hold it inside LONGING. This is the kind of structural force this decision asked for: securities hold negative exposure to it and the drift falls out, rather than being written in.

**The constraint.** The user stated that nobody in the world argues the decline:

> 세계관의 흐름상 낭만이 줄어들 뿐이야. 사람들이 그걸 대세로 주장하지도 않아. 그냥 세상의 흐름이 그렇게 되는거야. 실제 금융 시장이 움직이는것처럼.

This is stronger than the existing *the system never argues*. It removes the advocate from inside the fiction as well: no character, analyst, or institution asserts the trend. Each participant acts correctly on their own facts and the aggregate does what nobody chose — the ordinary behaviour of a market.

Two `llm-proposed` consequences follow and are recorded, not adopted. First, the market should not crash: volume thins, the spread widens, and quotes remain with nothing filling — the way a market actually dies. Second, the peak is invisible in its own moment and legible only later on a chart, which delivers loss without any sentence mourning it.

None of this selects a factor, a coefficient, a drift value, a curve, or a historical span. The no-hard-coded-drift rule and the requirement that the model be able to disagree with its author are unchanged and now bind the new cause as well: if transfer-to-AI becomes a modelled force, it must be publishable, testable, and capable of reversing.

## Sources

- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md); ChatGPT export, 2026-09-06–07; user turns support decisions, assistant synthesis and mechanisms retain proposal status

- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md)
- [[SRC-2026-09-05-claude-critic-of-model]] — [raw/surveys/2026-09-05-claude-critic-of-model.md](../../raw/surveys/2026-09-05-claude-critic-of-model.md)
- [[SRC-2026-09-05-glm-critic-of-model]] — [raw/surveys/2026-09-05-glm-critic-of-model.md](../../raw/surveys/2026-09-05-glm-critic-of-model.md)
