---
status: working
attribution: llm-synthesis
updated: 2026-09-07
sources:
  - SRC-2026-09-06-dataset-backtesting-research
---

# Datasets for Model Backtesting

The initial survey identifies 23 dataset families and six Kaggle access routes, with overlaps explicitly retained as mirrors or related benchmarks rather than independent evidence. The [full research notes](../../raw/surveys/2026-09-06-dataset-backtesting-research.md) contain publisher links, geographic and temporal coverage, available fields, access limitations, proposed experiments and provenance checks.

This extends [[data-sources]] from a candidate list into a test plan. It does not select a factor set or make an empirical claim about model performance. No dataset was downloaded or fitted; publisher documentation was inspected where accessible, and discovery-only resources are marked. Some live pages and a sample API request could not be retrieved.

## What can be validated

1. **Behavior:** whether practice, participation, time allocation and substitution models predict later observations.
2. **Observation layers:** whether attention forecasts behavior, and whether reporting volume or revisions create misleading shocks.
3. **Transferable mechanisms:** persistence, re-entry, contact structure, crowding and credibility updates in suitable external domains.

No dataset supplies observed LONGING security prices or its unobserved fundamental value. The unresolved [[Q-004-unit-of-account|security unit]] and valuation bridge prevent treating a simulation as an empirical price backtest. See [[academic-model-survey]] for the same distinction between fitting behavior and pricing a claim on it.

## Proposed collection priorities

These priorities are **llm-proposed**, not user-confirmed.

| Priority source | First useful test | Main limitation |
|---|---|---|
| Seattle Public Library monthly checkouts | Physical/digital substitution versus coexistence | Borrowing is not completed reading; availability and counting conventions matter |
| BLS American Time Use Survey | Time and social opportunity versus abstract modernization factors | Repeated cross-sections, not person-level transitions; rare activities are weakly measured |
| RIAA format history | Decline, persistence and revival | Revenue is not incidence; retail/wholesale, inflation and taxonomy must be reconciled |
| USPS correspondence reports | LETTER-adjacent behavior and cohort differences | Correspondence is not necessarily handwritten; report-series continuity needs checking |
| Wikimedia pageviews | Whether attention adds predictive value beyond behavior history | Language is not geography; attention is not practice or sentiment |

For a Korean-first study, Korea Media Panel, Korean Time Use Survey and KOBIS are the leading local routes, pending file and access checks. Other candidates cover postal infrastructure, libraries, payments, longitudinal households, values, contacts, ratings, retail transactions, churn, news, rumors, trader positions and historical release vintages.

## What the data may require us to calculate

Separate participation from duration, new adoption from repeat use and temporary exit, spending from price and volume, infrastructure from preference, and cohort replacement from within-person change. Each may be a denominator, observation correction or security-specific state rather than a new common factor. Conversely, if additional factors fail to improve later-period predictions or stable explanations, their extra complexity is unsupported for that use.

The survey proposes temporal holdouts, simple and seasonal baselines, incremental mechanism comparisons, parameter-stability checks and adverse cases such as revival. Factors may outnumber securities; identification depends on independent measurements and restrictions. Weekly interpolation does not create new evidence from annual observations. Exact ledger reconciliation remains necessary arithmetic, not evidence of causal truth. See [[factor-set-failure-profile-review]] and [[attribution-ledger]].

## Remaining collection gaps

- Direct handwritten-letter incidence, voluntary waiting valuations and willingness-to-pay evidence remain weak.
- CFTC positions need compatible price histories and pre-specified surprises before squeeze testing; positions alone do not observe consensus.
- Current survey microdata entitlements, specific file versions and exhibition reuse terms need checking at collection time.
- Kaggle mirror licenses and units can differ from publisher metadata. Prefer originals and preserve discrepancies.
- The survey does not establish whether LONGING will ship with real data, nor adopt a pricing specification.

## Related

- [[data-sources]]
- [[pricing-model]]
- [[academic-model-survey]]
- [[information-quality]]

## Sources

- [[SRC-2026-09-06-dataset-backtesting-research]] — [raw/surveys/2026-09-06-dataset-backtesting-research.md](../../raw/surveys/2026-09-06-dataset-backtesting-research.md); original LLM research synthesis, with documented availability distinguished from untested access and proposed LONGING applications
