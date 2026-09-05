---
status: working
attribution: llm-synthesis
updated: 2026-09-06
sources:
  - SRC-2026-09-05-pricing-model-v2-factor-framework
  - SRC-2026-09-05-pricing-model-v2-factor-review-prompt
  - SRC-2026-09-05-pricing-model-v2-factor-review-claude
  - SRC-2026-09-05-pricing-model-v2-factor-review-deepseek
  - SRC-2026-09-05-pricing-model-v2-factor-review-gemini
  - SRC-2026-09-05-pricing-model-v2-factor-review-glm
  - SRC-2026-09-05-pricing-model-v2-factor-review-grok
  - SRC-2026-09-05-pricing-model-v2-factor-review-qwen
---

# Factor Architecture Review Consensus

The second pricing-model review round asks a narrower question than [[model-review-consensus]]: after accepting that the original seven modernization indicators were collinear, how can LONGING recover complexity without returning to seven names for one force?

The working framework rejects both a predetermined factor count and simplification as an end in itself. It proposes a large candidate pool, a hierarchy from observables to latent factors, and a promotion test based on causal, cross-sectional, event, temporal, sign, attribution, and observability distinctions. Six hash-verified model reviews — Claude, DeepSeek, Gemini, GLM, Grok, and Qwen — tested that proposal against one registered prompt. Qwen's original registration was a defective capture that ended mid-expression partway through the response; the user replaced it with the complete response on 2026-09-06. This is a capture correction, not a change to the evidence, and is recorded in `raw/sources.md` and in `wiki/log.md`. All six reviews are now verified and synthesized below.

**Nothing on this page is a user decision.** The framework is explicitly a working proposal; the reviews are `llm-proposed`; this page is a synthesis of where they agree and split.

## Consensus: the problem is classification, not factor count — with one dissent

Five of six verified reviews accept the framework's central move and then sharpen it: a distinct story is necessary but not sufficient. A live factor must also produce a distinguishable exposure vector across securities and own plausible events that can move it without moving its neighbors in the same way.

Qwen accepts the same collinearity diagnosis and the same layered architecture, but treats reduction, not classification, as the remedy. It collapses the nine candidates to five core factors — Friction Elimination, Agency Displacement, Material Decoupling, Social Revaluation, Attention Scarcity — and states this as a parsimony choice: fewer factors that are "causally sharper," rather than more factors that are more finely distinguished. This is not a return to the first review round's one-to-three macro factors; it is a middle position between that round's reduction and the other five reviews' larger candidate pools, and it still routes through the same observables → latent factors → security exposures hierarchy as the rest of the second round. The dissent is recorded here as a minority position, not folded into the majority finding below.

The five reviews that accept classification over reduction also agree that the nine candidates mix different kinds of objects. The stable hierarchy across the set is:

```text
OBSERVABLE INDICATORS
        ↓
STRUCTURAL / WORLD FACTORS
        ↓
SECURITY-SPECIFIC EXPOSURES AND FUNDAMENTALS
        ↓
VALUATION / NARRATIVE REGIMES
        ↓
POSITIONING AND WEEKLY PRICE
```

This is more than an organizational preference. It prevents one cause from entering the ledger twice — first as a change in the world and again as a response to the decline it already caused.

## Consensus: the candidate pool is too technology-centric

Every verified review, including Qwen, finds a missing demand side — Qwen's own diagnosis of the framework is that it "confused *technological enablers* with *economic consequences*," and that the candidate pool "leans heavily on technological displacement... but under-weights sociological revaluation." That convergence is real but partly prompt-induced: the registered review prompt (`SRC-2026-09-05-pricing-model-v2-factor-review-prompt`) directed reviewers to "actively search for missing causal dimensions" and itself named attention scarcity, economic scarcity of time, loneliness and social fragmentation, and geographic distance as dimensions to investigate — territory that overlaps what the reviews returned. What the reviews independently contribute is not the bare observation that something is missing, but the specific causal structure they propose and the claim that the demand side is what lets the index rally without any technological retreat. The names differ, but the omitted causal territory repeats:

- **available time and attention** — whether anyone has an unhurried hour or an unclaimed mind, independent of what technology can do;
- **social and spatial conditions** — proximity, durable ties, trust, third places, housing and the cost of unscheduled encounter;
- **valuation regimes** — whether patience, inconvenience, materiality, authenticity, and social legibility are currently rewarded or punished;
- **practice infrastructure and cohort transmission** — whether labs, venues, shops, skills, and a next generation of practitioners still exist.

These additions matter because they create bull markets without reversing technology. A four-day week can raise slow practices while automation continues; dense public space can revive unplanned encounter without disabling calendars; synthetic-media saturation can revalue live performance or chemical photography; a patience or authenticity regime can lift the whole market or one exposed group.

This territory list is a union across reviews, not a unanimous set. Qwen adds only one demand-side factor, Attention Scarcity, and explicitly considers and rejects two others: institutional trust, on the grounds that its effect is already mediated through Social Revaluation and would risk collinearity with it, and demographic shift, on the grounds that it is too slow-moving and is already priced into the secular drift of the other factors.

## Candidate dispositions

The reviews agree more strongly about where candidates do **not** belong than about the final names.

| Candidate family | Verified-review result |
|---|---|
| Time Compression | Retained as a distinct structural speed or latency mechanism by five of six. Qwen merges it into Friction Elimination, alongside Uncertainty Compression and Coordination Compression, on the grounds that time delay is one form of friction and separating it creates false precision. |
| Human Substitution | Retained by all six as the question of who performs the act. Qwen renames it Agency Displacement, sharpening "substitution" (the outcome) into "displacement" (the mechanism). |
| Uncertainty Compression | Retained by five, sometimes renamed predictive pre-selection (Claude) or uncertainty suppression (GLM). Qwen merges it into Friction Elimination, treating uncertainty removal as part of the same systemic optimization as removing time delay. |
| Physicality Displacement | Retained by all six in some form, usually sharpened toward dematerialization, embodiment, or permanence. Qwen renames it Material Decoupling. |
| Mediation | The split widens to three positions plus Qwen's: delete and decompose it; retain it as relational intermediation; or narrow it to extraction, surveillance, and control of terms. Qwen dissolves it entirely, routing its algorithmic half into Agency Displacement and its platform/digital half into Material Decoupling, and treats it as not a standalone causal force. |
| Coordination Compression | Five of six now merge, demote, or delay it — Claude and DeepSeek delete it as reducible to latency plus intermediation, Gemini and Grok demote it to an indicator inside an encounter-erosion factor, and Qwen merges it into Friction Elimination as a scheduling/friction-reduction tool. Only GLM retains it, as Coordination Formalization. Its current support may be too concentrated in unplanned calls and visits for a market-wide factor. |
| Friction / Inconvenience Premium | Preserved by five as a cyclical taste, patience, or valuation regime rather than a simple structural pressure. Qwen is the exception: it demotes this candidate to a security-level fundamental, holding that the market's reaction to it is already captured by Social Revaluation and that it is a characteristic of specific securities rather than a macro factor. |
| Scarcity Revaluation | Five of six now demote, delete, or absorb it as a macro force — four treat it as a security-level nonlinear response to prevalence (Grok names that transform Rarity Elasticity) on the grounds that pricing it as a factor double-counts the decline that produced the rarity, and Qwen absorbs it into Social Revaluation as an input to status rather than a separate mechanism. Only GLM retains it as a factor, F8. This remains the clearest unresolved classification dispute. |
| Social Legibility / Status | Retained by all six as a cultural or narrative revaluation channel, though some combine it with friction or authenticity. Qwen renames it Social Revaluation and widens it to absorb Scarcity Revaluation as well. |

## The identification disciplines

The reviews propose complementary checks rather than one final method:

- **Event signature:** each factor must own a class of primary events that does not automatically move its neighbors.
- **Exposure rank:** a factor's exposure vector must not be reproducible from the other exposure vectors. Claude adds a practical limit: with only eleven reference securities, the model cannot identify a large factor set; expand the universe or keep some factors declared but unpriced.
- **Observable separation:** indicators may feed several factors, but the routing and allocation rule must be published. A visible dashboard can stay rich without treating every visible series as a priced factor.
- **Temporal separation:** slow structural pressures, cyclical valuation regimes, and fast positioning cannot be interchangeable lines in one flat sum.
- **Pre-registration:** exposures, thresholds, regime switches, editorial rubrics, and revision dates must be versioned before the price path is seen.
- **Falsification:** film photography must be able to revive, at least one structural winner must emerge, collinearity and attribution must stay bounded, and the model must sometimes contradict the artist's prior.

The strongest new warning is that universe selection can hard-code the conclusion even when no equation contains negative drift. If every constituent was chosen because it appears to be disappearing, aggregate decline is partly embedded before the model begins. Claude and Grok independently propose the same remedy: expand the universe from eleven examples to roughly 40–60 practices, including practices in genuine secular expansion, before pricing a large factor set. Both treat this as blocking rather than optional — Claude states it as a rule (roughly K ≤ N/3: eleven securities support about four factors, forty-five support about fifteen) and calls it the single most important point in its review; Grok says nothing else in its specification is defensible until the universe is expanded. Gemini notes the eleven-security limit without proposing a target; DeepSeek, GLM, and Qwen are silent on it and Qwen's own specification works directly with the eleven-security reference set. Two of six reviews converging on the same numeric target, both treating it as a precondition, is stronger than a single-review proposal, though short of the six-review unanimity this page reserves for full consensus.

## Attribution: exact arithmetic is agreed, method is not

All six reviews preserve the exact weekly ledger and reject unexplained narrative patching. They differ on how to reach exactness:

- Shapley allocation of nonlinear interactions;
- orthogonalized or principal-component attribution while preserving causal factors upstream;
- explicit interaction and residual lines with hard limits;
- delayed-impact pipelines that carry one event across several weeks;
- confidence as shrinkage, uncertainty, or pacing rather than an ungrounded multiplier.

The shared requirement is reconstructability: the published lines, including any residual, must sum to the return and allow the price path to be replayed. Persistent large residuals, post-hoc exposure changes, or a factor that never diverges from the common modernization component are failure conditions.

## What changed from the first review round

The first seven-model review concluded that the credible V1 path was reduction: collapse the original macro layer to one to three factors and remove excess machinery. The subsequent framework accepts the diagnosis of collinearity but disputes reduction as the design goal. The second review round largely supports that reframing, five of six: complexity may return when it is hierarchical, identified, falsifiable, and supported by a sufficiently heterogeneous security universe. Qwen dissents toward reduction, collapsing the nine candidates to five core factors on parsimony grounds rather than adopting classification as the remedy — see the dissent recorded above.

This is an **evolution of the working proposal**, not a reversal of any confirmed decision. The final factor set remains open.

## Open decisions

- Which factors are priced in the first implemented model, and which remain research indicators.
- Whether Mediation survives as a narrow extraction/intermediation factor.
- Whether Coordination becomes a factor after the security universe expands.
- Whether Scarcity is always a security-level transform or can ever be a market-wide factor.
- Whether time and attention remain separate, and whether spatial proximity, tie density, trust, and encounter habitat are one factor or several.
- How many constituents are required before the exposure matrix can support the chosen factor count.
- Whether exact attribution uses Shapley values, an orthogonalized reporting basis, bounded residuals, or a documented combination.
- Whether the factor set lands near Qwen's five, near the larger sets the other five reviews propose, or between them. This is open, not resolved — the second round has not converged on a count.

## Related

- [[pricing-model]]
- [[model-review-consensus]]
- [[index-architecture]]
- [[data-sources]]
- [[Q-001-price-formation]]
- [[Q-003-calibrating-the-bias]]

## Sources

- [[SRC-2026-09-05-pricing-model-v2-factor-framework]] — raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-prompt]] — raw/documents/2026-09-05-pricing-model-v2-factor-review-prompt.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-claude]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-deepseek]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-gemini]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-glm]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-grok]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-qwen]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md
