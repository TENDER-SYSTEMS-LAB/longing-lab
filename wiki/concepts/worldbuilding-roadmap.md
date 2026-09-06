---
status: working
attribution: llm-proposed
updated: 2026-09-07
sources:
  - SRC-2026-09-06-worldbuilding-roadmap-and-handoff
  - SRC-2026-09-06-world-rules-letter-spec-request
  - SRC-2026-09-06-worldbuilding-roadmap-request
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-06-attribution-resolution-and-universe-scaling
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
  - SRC-2026-09-06-academic-model-recovered-excerpts
  - SRC-2026-09-06-factor-set-failure-profile-prompt-v2
  - SRC-2026-09-06-factor-set-failure-profile-chatgpt
  - SRC-2026-09-06-factor-set-failure-profile-glm
  - SRC-2026-09-06-academic-model-research-notes
  - SRC-2026-09-06-cross-domain-model-survey
  - SRC-2026-09-06-dataset-backtesting-research
---

# World-building Scope and Roadmap

The user originally asked to assess how far LONGING has been designed, establish how deeply to design its world, and use that boundary to plan the next work. The assessment below preserves that proposal. A subsequent request explicitly uses its consistency target and takes up stages 1 and 2 together; their drafts are now [[world-rules]] and [[letter-practice-dynamics]]. Completion gates, later sequence, sample scope, and the drafts' design choices remain **LLM proposals for discussion**. This page coordinates design pages; their detailed specifications remain there.

## Stage 1–2 draft checkpoint — 2026-09-06

The selected task boundary is to make numbers, reports, actions, and past records arise from the same world rules. The world draft supplies proposed jurisdiction, institutional powers, actor knowledge, audience persistence, and delivery. Existing [[Q-004-unit-of-account]] now compares concrete units and their consequences for price, indices, positions, arbitrage, and artistic meaning; [[Q-002-listing-lifecycle]] specifies separate practice, observation, coverage, and listing states. The LETTER draft answers what is calculated, what changes it, and how assumed strengths can be examined without real data.

The draft gate is reviewability, not adoption or an operating release. The shared city/cohort assumption, practice-episode convention, feedback loop, coefficient ranges, unit branch, observation windows, and medium await user selection. Deterministic arithmetic illustrates attention/practice divergence and changed-condition recovery; it does not select a natural-data generator or validate a full factor model. Stage 3 must settle the observation contract and chosen unit before producing value, price, settlement, and index rules. The original unit-review work item remains prepared but undispatched.

## Assessment — the premise is developed; the operating world is incomplete

LONGING has a developed artistic premise, institutional presentation, publication rhythm, and market architecture under review. Its parts do not yet form a specified, demonstrated cycle from a change in human practice to a published price, conflicting research, and a viewer encounter. Readiness is therefore better described by dependencies than by a completion percentage.

| Area | Recorded progress | Remaining boundary before a coherent prototype |
|---|---|---|
| Artistic premise and form | LONGING is named; human practices are processed through financial research. The research-house direction was accepted provisionally. | Define the world's geographical, population, and temporal scope and what the institution claims to measure. See [[overview]], [[system-grammar]], [[DEC-002-research-house-form]], [[data-sources]]. |
| Time and long-term behavior | Weekly prices and monthly formal research are confirmed. Secular decline with rallies is confirmed; decline must emerge from conditions. | Specify state transitions and demonstrate that changed conditions can produce recovery without rewriting the engine. See [[DEC-003-weekly-market-monthly-research]], [[DEC-004-secular-decline-with-rallies]]. |
| Securities and indices | Practices/situations, candidate securities, and six condition-based sub-indices exist in the design. | Unit, currency/quote meaning, eligible universe, weighting, listing, delisting, and return from disappearance remain open. See [[index-architecture]], [[Q-002-listing-lifecycle]], [[Q-004-unit-of-account]]. |
| Practice dynamics | The user requires separate starts and discontinuation, and feedback. Academic applications have been explained. | Select computed states, directional causes, feedback paths, and assumed effect ranges. No generator or calibrated model is selected. See [[academic-model-survey]], [[pricing-model]]. |
| Market and information | Fundamental Value versus Market Price, analyst targets, events, positioning, and attribution have working architectures. The user wants arbitrage and imperfect news represented. | Choose the valuation bridge and mechanisms; define actors, finite resources, what they know, how beliefs can be wrong, and what corrects them. See [[arbitrage]], [[information-quality]], [[Q-001-price-formation]]. |
| Factor architecture | Three review rounds exist; the third compares failures of six fixed sets in eight accepted responses. Ledger resolution has a confirmed growth rule. | No factor set, exposure matrix result, or simulation has been selected or established. Displayed lines and internal factors are separate questions. See [[factor-set-failure-profile-review]], [[attribution-ledger]]. |
| People and viewer experience | Four analyst philosophies, disagreement, positions, and archive gestures are developed as working material. | Connect actual reports, scorecards, positions, corrections, and archive pages over time. Several emotional/archival devices remain proposals. See [[analyst-system]], [[Q-003-calibrating-the-bias]]. |
| Research and production | Six detailed model cards, a 120-entry discovery catalog, and 23 dataset families provide research coverage. | The surveys are not implementation or validation. Data has not been downloaded or fitted in the recorded work; delivery context, platform, and operating workflow remain open. See [[dataset-backtesting-survey]], [[current-state]]. |

## Proposed target depth — a world that can operate and retain consequences

Design every rule needed to produce the work's visible claims and actions, then demonstrate those rules across a publication cycle and its exceptions. The first release need not explain every aspect of the imagined society.

| Depth | What is designed | Proposed treatment |
|---|---|---|
| Premise and surface | Theme, tone, names, institution, interface vocabulary | Preserve the developed foundation; resolve only contradictions that affect the next layers. |
| Operating rules | Entities, units, resources, institutional authority, states, causation, information, time, and audience permissions | Specify all rules used by the first release, including their unknowns and limits. This is the immediate design target. |
| Lived consequences | Recurring publications, changing positions, wrong forecasts, corrections, disappearance, revival, and persistent traces | Demonstrate a representative slice in depth. A world becomes convincing when its previous actions constrain its next actions. |
| Extended background | Full institutional genealogy, exhaustive biographies, comprehensive economics and history | Expand when it changes a rule, report, conflict, or encounter the work actually needs. It is not a general prerequisite. |

The design boundary is **causal and institutional consistency across the audience's encounter**. A fictional world can meet it without empirical calibration. A claim that the model measures real human behavior requires separate evidence. Model transparency can appear in ordinary methodology, source labels, and revision records while the interface retains its dry research register.

## What must be specified, and where to stop

| Domain | Required design depth for the proposed first slice | Completion question |
|---|---|---|
| World and institution | Whose practices, where, in what time; relation to the real world; who publishes quotes, grants coverage, lists securities, and corrects records | Can the institution explain its jurisdiction and responsibility without treating one population's decline as universal? A funding model is needed only if incentives depend on it. |
| Security ontology | The practice's inclusion/exclusion boundary; behavior versus memory/attention; unit and quoted quantity; what holding a position means, if any holding exists | Can one describe exactly what changes when someone starts, stops, holds, or closes, without confusing a price with a participant count? |
| Human practice | Starts, continuation, cessation, possible re-entry; time, effort, infrastructure, relationships, and substitution where relevant | Can the same net decline arise from different starts/stops and produce different research? Can a feedback path be traced back to its cause? |
| Actors and market | Practitioners, analysts, publishers, and any modeled market participants; their aims, information, constraints, and channels of influence | If arbitrage is implemented, who holds what, against whom, at what cost, and why can the gap persist or close? Role rules matter before full biographies. |
| Knowledge and error | Underlying event versus report versus belief; access delays, surprise, false reports, over/under-reporting, leaks, and corrections | Can price move on a false report while the underlying practice remains unchanged, with a later correction that preserves what was known earlier? |
| Value and price | Practice state, institutional valuation, forecasts, price, and index weighting, with distinct meanings and update rules | Can every displayed movement be reconstructed, while the institution's valuation and analysts can still be wrong? Exact accounting alone does not prove the causal model. |
| Institutional memory | Publication dates, forecast evaluation, listing changes, discontinued coverage, archival traces, and revival procedure | Does a disappearance have a defined state and visible aftermath? Does revival follow a rule, including what one returning practitioner can and cannot do? |
| Viewer and delivery | Entry point, reading path, position recording, return visit, medium, persistence, and what viewer actions affect | Can a viewer take a position and return to its consequences? Practice feedback does not by itself authorize audience votes to affect price. |

## Proposed roadmap and completion gates

These are dependency stages, not calendar estimates. The medium, initial breadth, and operating capacity are not settled enough to assign credible dates. A paper or static rehearsal can expose problems before executable implementation.

| Stage | Work and deliverable | Completion gate / dependency |
|---|---|---|
| 1. Define the world contract | A short design brief covering world scope, institutional authority, price/unit meaning, actor roles, audience permissions, a provisional delivery context, and the first/return visit. Draft security cards alongside the unit question. Prepare the already requested unit review around downstream consequences rather than repeating existing options. | The possible meanings of a security, price, holding, and disappearance are explicit and their consequences comparable. Adopted choices require user decisions; a trial can proceed with clearly labeled provisional assumptions. |
| 2. Specify practice dynamics | Use `LETTER` as a proposed reference case. Answer the three pending questions in order: what is computed; what increases/decreases it; how effect strengths are set without real data. Produce a state/causal map and a parameter table with units, ranges, delays, bounds, and assumptions. | Starts and stops are distinct; at least one explicit feedback path exists; overlap, substitution, and complementarity are not forced into an exclusive 100% split. Natural-looking data generation remains a later task. |
| 3. Connect institution, information, and price | Specify a mechanism linking practice state, observations, institutional estimates, analyst forecasts, positioning, and prices. Develop imperfect reporting and arbitrage using stage 1's meanings. Draft lifecycle and correction rules. | One ordinary event and one false-report/correction sequence can be traced through the system. Valuation, forecast, and price are not defined solely by each other. A held position has a meaning and constraints before a squeeze/arbitrage rule uses it. |
| 4. Choose and challenge the factor/universe design | Select contrasting practices to expose different mechanisms; compare relevant A–F failure hypotheses against the causal map. Specify exposures, routing, the displayed ledger, and provisional index construction. Deliberately seek events the current vocabulary cannot explain. | Distinguish forward accounting from recovering causes. Legitimate multiple effects are not automatically double counting. Resolve each diagnostic failure through a rule, exposure, factor, or an explicit scope boundary; do not rename every failure away. No factor-to-security count cap is imposed. |
| 5. Rehearse a connected release | Produce one reference security in full plus a few contrasting securities with sufficient specification to challenge it. Proposed sample: 12 consecutive weekly closes crossing three monthly publication points, with charts, attribution, opposed research, corrections, a lifecycle vignette, and a recorded viewer position. | All artifacts refer to the same events and state history. A long-horizon replay or separate scenario covers disappearance/revival and forecast evaluation beyond the sample. Twelve-month targets cannot acquire completed track records within twelve weeks; their scores remain pending until their horizons mature. The sample demonstrates the system, not empirical accuracy. |
| 6. Test the encounter and establish operation | Test the provisional delivery context through the first navigable experience built from those artifacts. Check the first visit and return visit, publication effort, source status, versioning, and preservation of old reports. | A viewer can encounter disagreement and loss through ordinary research material; LONG and SHORT can each be coherent and wrong. Repeated publication is feasible at the proposed coverage breadth. Expand the universe and integrations when these gates hold. |

Stages 1 and 2 should inform each other: an impossible unit may be revealed by a concrete practice, and a world contract may change what the equation must compute. Existing [[current-state|resume questions]] remain active inside this broader frame. Model clarification precedes choosing an equation. The unit-review preparation can run alongside that clarification; it does not require selecting a factor set first.

The small reference slice is a **production and comprehension sample**, not a ceiling on the final universe or evidence that a many-factor architecture can be inferred from three securities. Factor and universe design can iterate before the reference case is polished. The user allows factors to outnumber securities; the ledger's initial display near nine lines and its growth rule do not select internal model dimensionality or membership.

## Proposed scenario checks before expanding

- **Ordinary decline:** a worsening condition changes starts/stops and practice persistence through specified channels; a negative return is not inserted solely to enforce the theme.
- **Counterfactual recovery:** enabling conditions improve and the same rules can sustain recovery. No numeric recovery target is claimed in advance.
- **Attention without practice:** publicity grows while continuation weakens; behavior, attention, and discourse can diverge.
- **Information failure:** a rumor or false report changes belief, later disclosure corrects it, and the archive retains the earlier information state.
- **Divergent securities:** the same event has different effects on a relational practice and a solitary or infrastructure-dependent practice, for explicit reasons.
- **Scarcity and disappearance:** price, practice prevalence, and total index contribution can diverge according to the chosen unit/weighting convention; cessation and revival follow the lifecycle rule.
- **Disagreement and accountability:** an analyst changes stance or is wrong for a reason supported by their method; scoring is not merely a comparison with a price the same analyst dictated.
- **Unexplained events:** design-stage failures remain visible long enough to challenge the factor vocabulary. Exact ledger totals do not close the investigation.

For a fictional-data trial, inspect consistency, bounds, reproducibility, response to changed assumptions, and whether the intended distinctions survive across a stated parameter range. Do not call that a real-world backtest. If observed data is later used, pursue the component-level tests mapped in [[dataset-backtesting-survey]] with source-specific limits.

## The original immediate-next-work brief

Prepare **one provisional world contract and one `LETTER` state specification** together. Resolve or expose these questions concretely:

1. Who and where are represented, and what is the institution publishing a price *of*?
2. Which quantities describe the practice independently of price, and how do starting, stopping, and returning differ?
3. What conditions alter those quantities, and through which feedback paths?
4. What can the institution, analysts, market actors, and viewer know or do differently?
5. Which assumptions need a user choice or the requested unit review, and which can be tested provisionally in the first connected sample?

The outcome is a reviewable specification with explicit unresolved branches, not a new list of models. Further literature or dataset work should answer a named gap in this specification. No review services were contacted, simulation run, or implementation undertaken by this roadmap task.

## Evolution

The originating roadmap task's assessment and next-session handoff are now preserved in [[SRC-2026-09-06-worldbuilding-roadmap-and-handoff]]. After the assessment, the user said they would continue in a new session and requested an instruction prompt. The assistant supplied a brief pairing the world contract with the LETTER specification and preserving the three application questions, current constraints, and proposal/decision boundary. This records preparation of a handoff; it does not by itself adopt the brief's detailed recommendations. The separate user-issued request, [[SRC-2026-09-06-world-rules-letter-spec-request]], provides the subsequent task's scope authorization. The two records are one lineage, not independent validation. This retrospective ingestion preserves the stage 1–2 checkpoint above rather than resetting work to the earlier assessment.

The subsequent world-rules/LETTER request selects the first two stages as current work and restates the consistency target. The checkpoint above records draft progress; it does not promote assistant recommendations into user decisions or claim the later publication sample has been built.

Earlier source proposals put price formation first, then listing lifecycle, one complete `LETTER`, indices, screens, and universe expansion. Subsequent reviews exposed the unit, causal identification, and information gaps; the user added arbitrage, news quality, factor-count directions, starts/stops, and feedback. The present request widens the planning question to the depth of the world itself. This proposal places a world contract around the existing single-security and model-application work; it does not supersede a confirmed work order, because no such order is recorded.

## Sources

- [[SRC-2026-09-06-worldbuilding-roadmap-and-handoff]] — [raw/conversations/2026-09-06-worldbuilding-roadmap-and-handoff.md](../../raw/conversations/2026-09-06-worldbuilding-roadmap-and-handoff.md); selected original assessment, user handoff request, assistant-written prompt, and ingestion request; earlier state preserved without replacing subsequent drafts

- [[SRC-2026-09-06-world-rules-letter-spec-request]] — [raw/documents/2026-09-06-world-rules-letter-spec-request.md](../../raw/documents/2026-09-06-world-rules-letter-spec-request.md); exact subsequent request taking up stages 1 and 2, with explicit design constraints

- [[SRC-2026-09-06-worldbuilding-roadmap-request]] — [raw/documents/2026-09-06-worldbuilding-roadmap-request.md](../../raw/documents/2026-09-06-worldbuilding-roadmap-request.md); exact initiating request, not approval of this proposal
- [[SRC-2026-09-04-longing-concept-brainstorm]] — [raw/conversations/2026-09-04-longing-concept-brainstorm.md](../../raw/conversations/2026-09-04-longing-concept-brainstorm.md); artistic premise, institution, audience, and lifecycle questions; foundational single-source dependence remains
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md); market architecture, cadence, and original next-work proposal
- [[SRC-2026-09-06-attribution-resolution-and-universe-scaling]] — [raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md](../../raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md); ledger growth and design-stage diagnostic intent; compiled record with quoted user statements
- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md); user directions on arbitrage, reports, factor count, and separate unit review
- [[SRC-2026-09-06-academic-model-recovered-excerpts]] — [raw/conversations/2026-09-06-academic-model-recovered-excerpts.md](../../raw/conversations/2026-09-06-academic-model-recovered-excerpts.md); original selected user positions on starts/stops, feedback, unavailable real data, and application clarification
- [[SRC-2026-09-06-factor-set-failure-profile-prompt-v2]] — [raw/documents/2026-09-06-factor-set-failure-profile-prompt-v2.md](../../raw/documents/2026-09-06-factor-set-failure-profile-prompt-v2.md); fixed-set test framing
- [[SRC-2026-09-06-factor-set-failure-profile-chatgpt]] — [raw/surveys/2026-09-06-factor-set-failure-profile-chatgpt.md](../../raw/surveys/2026-09-06-factor-set-failure-profile-chatgpt.md); v1 review; accounting/identification cautions, with wider review provenance in [[factor-set-failure-profile-review]]
- [[SRC-2026-09-06-factor-set-failure-profile-glm]] — [raw/surveys/2026-09-06-factor-set-failure-profile-glm.md](../../raw/surveys/2026-09-06-factor-set-failure-profile-glm.md); v2 review; conditional failure hypotheses, not test results
- [[SRC-2026-09-06-academic-model-research-notes]] — [raw/surveys/2026-09-06-academic-model-research-notes.md](../../raw/surveys/2026-09-06-academic-model-research-notes.md); six model cards and unadopted applications
- [[SRC-2026-09-06-cross-domain-model-survey]] — [raw/surveys/2026-09-06-cross-domain-model-survey.md](../../raw/surveys/2026-09-06-cross-domain-model-survey.md); discovery breadth, not an implemented model
- [[SRC-2026-09-06-dataset-backtesting-research]] — [raw/surveys/2026-09-06-dataset-backtesting-research.md](../../raw/surveys/2026-09-06-dataset-backtesting-research.md); data candidates and proposed component tests
