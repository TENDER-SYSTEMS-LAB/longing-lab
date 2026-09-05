---
status: unknown
attribution: llm-proposed
updated: 2026-09-05
sources:
  - SRC-2026-09-05-qwen-critic-of-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-deepseek-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-grok-critic-of-model
  - SRC-2026-09-05-gemini-critic-of-model
---

# Q-004 — What is one unit of a LONGING security?

## The question

An equity price is not a number floating in space. It is the price of a share, and a share is a claim on something. LONGING has no answer to the equivalent question:

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

## Why it matters

This is the question that decides whether LONGING's indices are *constructed* or merely *asserted*. It also decides how much fiction the work has to manufacture: a practice-unit universe requires inventing a plausible number for every security, and every one of those numbers is a place where the artist's hand can be found.

## Related

- [[index-architecture]]
- [[pricing-model]]
- [[model-review-consensus]]
- [[data-sources]]
- [[Q-001-price-formation]]
- [[Q-002-listing-lifecycle]]

## Sources

- [[SRC-2026-09-05-qwen-critic-of-model]] — raw/surveys/2026-09-05-qwen-critic-of-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
- [[SRC-2026-09-05-deepseek-critic-of-model]] — raw/surveys/2026-09-05-deepseek-critic-of-model.md
- [[SRC-2026-09-05-kimi-critic-of-model]] — raw/surveys/2026-09-05-kimi-critic-of-model.md
- [[SRC-2026-09-05-grok-critic-of-model]] — raw/surveys/2026-09-05-grok-critic-of-model.md
- [[SRC-2026-09-05-gemini-critic-of-model]] — raw/surveys/2026-09-05-gemini-critic-of-model.md
