---
status: confirmed
attribution: user-confirmed
updated: 2026-09-05
sources:
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

## Sources

- [[SRC-2026-09-05-price-formation-market-model]] — raw/conversations/2026-09-05-price-formation-market-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
