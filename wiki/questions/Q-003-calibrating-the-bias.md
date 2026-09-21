---
status: working
attribution: jointly-developed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-requisition-cap-decision
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
---

# Q-003 — How far can the bias go before the work argues?

## The question

Two of the work's stated principles pull against each other.

One: **LONGING does not claim romance is right.** The system provides numbers and reports; the meeting point of conflicting views appears as a price; feeling occurs in the viewer, not in the system.

Two, from the user immediately afterward: **the work should be faintly biased toward romance.** The user liked the neutrality principle and still wanted a quiet tilt — and proposed a way to get it: give the analysts who publish SHORT on romantic securities a subtly machine-like or villainous persona. They asked, in the same breath, whether that was too obvious.

## Where it stands

The persona approach was set aside as too legible. A machine-versus-human reading resolves the work in one move — human good, machine bad — and the SHORT desk stops being an argument and becomes a costume. Explicitly rejected: robot characterization, codenames like `A-17`. Adrian Kessler is instead an entirely normal, highly competent professional whose model simply has no field for certain things. *He does not dislike letters; he believes their value cannot be demonstrated.* The stated aim: more frightening, and more contemporary, than a villain.

The bias was relocated into structure — the asymmetries listed in [[system-grammar]], of which the sharpest is that the most mechanical analyst is usually right and the most human one is usually wrong, and that his accuracy is exactly what drives the index down. *He is usually right.* That is what makes it sad, without a word of argument.

The user's closing response was "좋은 정리 감사해" ("thanks, good summary"). That is acknowledgment, not an explicit decision — so this is recorded as a `working` direction and not as `user-confirmed`. Under the repository's attribution rule, an LLM proposal does not become a user decision until the user confirms it.

## What remains open

- **How much asymmetry is too much.** Every listed asymmetry is individually subtle; their sum may not be. There is no rule yet for how many are used at once, or how often.
- **Whether the LONG desk's sentences may become the work's own.** The device where a LONG report's line reappears years later as an epigraph puts the institution's voice behind one side. Powerful, and the closest thing to advocacy in the current design.
- **The self-attack.** *Consumers romanticize behaviors they no longer practice* is a SHORT line aimed at the whole project, kept deliberately. How prominently it is placed decides whether the work genuinely doubts itself or only performs doubt.
- **Restated as the working formulation:** LONGING does not claim romance is right; it keeps asking whether its disappearance is really progress. How faint can the asking be and still be heard?

## The question moved into the model (2026-09-05)

The bias stopped being only a matter of tone once the market got a mechanism. On 2026-09-05 the user stated that LONGING should trend downward because they believe romance genuinely is disappearing ([[DEC-004-secular-decline-with-rallies]]) — which is the most direct expression of the tilt so far, and simultaneously the place where it is most at risk of becoming an argument.

The constraint the user attached in the same breath is the answer to this page's question, restated as engineering: **the decline must not be hard-coded.** Not `weekly_drift = -0.3%`, but structural forces that rise while most securities hold negative exposure to them. The distinction is between *"낭만은 반드시 죽는다"* and *"현재 세계의 방향으로 계산해보니 계속 떨어지고 있다"* — the first argues, the second asks.

The seven reviews of the market model turned that into checkable tests, which is more than this page had before:

- **Publish the drift parameter**, with its rationale. A hidden thumb on the scale is manipulation; a disclosed assumption in a published methodology is what an index provider does.
- **Keep structural winners** — one review puts it at 15–25% of the universe with positive or near-zero exposure. A universe where everything declines is a tautology, and a viewer decodes it immediately.
- **Publish a neutral-drift companion index** at zero drift beside the headline, inviting the audience to subtract the thesis and see what remains.
- **The model must be able to disagree with its author.** The sharpest form: film photography and vinyl genuinely revived in reality, so if `FILM` cannot stage a multi-year bull market inside the model, the model is rigged. The 2026-09-20 requisition cap in [[DEC-007-standard-return-numeraire]] keeps this possible after the tipping point; the cap is to be published like the drift parameter above, and its condition — the whole chart still falls — is the first stated bound on how far the bias may go.
- **A measurable version of the bias.** If returns decompose into a flow effect and a re-rating effect, then a market compressing multiples further than practice decline justifies is charging a *despair premium* — something the viewer discovers in an attribution table rather than being told.

And one device that goes further than anything previously on this page: let the institution **revise its own fundamental model downward** at the annual review, in dry language, with a changelog, once its estimates have been persistently wrong. A research desk quietly marking down its model of human value on schedule is the thesis executed as a maintenance procedure — the strongest available form of "structural rather than stated", and also the closest the work has come to letting the bias be visible in the machinery instead of the prose.

None of these is decided. They are recorded because they convert this question from a matter of taste into a set of parameters that can be argued about.

## Related

- [[system-grammar]]
- [[analyst-system]]
- [[pricing-model]]
- [[model-review-consensus]]
- [[DEC-004-secular-decline-with-rallies]]
- [[overview]]

## Evolution — authored history and an unexplained surface (2026-09-07)

The user explicitly locates the bias in the fictional historical data: the selected human conditions diminish over time. This is no longer merely acknowledgment of an assistant's structural-bias proposal. The price model must still allow recovery under different conditions; [[DEC-004-secular-decline-with-rallies]] owns that constraint.

Internal definitions are explicit in GitHub, while the artwork leaves their interpretation to indicators, securities, and reports. This selects the location of ambiguity without selecting a numeric degree of bias or a public explanatory methodology. The earlier neutral-drift companion, fixed winner percentage, epigraphs, and disclosure devices remain proposals.

HOLD/SHORT's better cumulative forecasting record is now a stated artistic direction. It does not equate prediction success, accurate understanding of the underlying condition, and moral rightness; precise scoring remains open in [[analyst-system]].

## Sources

- [[SRC-2026-09-20-requisition-cap-decision]] — [raw/conversations/2026-09-20-requisition-cap-decision.md](../../raw/conversations/2026-09-20-requisition-cap-decision.md); the cap, and the condition that bounds it
- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md); ChatGPT export, 2026-09-06–07; user turns support decisions, assistant synthesis and mechanisms retain proposal status

- [[SRC-2026-09-04-longing-concept-brainstorm]] — [raw/conversations/2026-09-04-longing-concept-brainstorm.md](../../raw/conversations/2026-09-04-longing-concept-brainstorm.md)
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md)
- [[SRC-2026-09-05-claude-critic-of-model]] — [raw/surveys/2026-09-05-critic-of-model/2026-09-05-claude-critic-of-model.md](../../raw/surveys/2026-09-05-critic-of-model/2026-09-05-claude-critic-of-model.md)
- [[SRC-2026-09-05-glm-critic-of-model]] — [raw/surveys/2026-09-05-critic-of-model/2026-09-05-glm-critic-of-model.md](../../raw/surveys/2026-09-05-critic-of-model/2026-09-05-glm-critic-of-model.md)
