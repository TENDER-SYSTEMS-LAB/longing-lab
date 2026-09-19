---
status: confirmed
attribution: user-confirmed
updated: 2026-09-19
sources:
  - SRC-2026-09-19-market-texture-findings
  - SRC-2026-09-07-artwork-brainstorm-v2
  - SRC-2026-09-05-price-formation-market-model
---

# DEC-003 — Weekly market, monthly research

## The decision

The user set the market's clock directly, rejecting the monthly evaluation cycle that had just been proposed:

> 그리고 월별은 너무 길어. 위클리로 가자. 월별로 애널리스트의 리서치 보고서가 나오고, 그거에 따라 시장 가격이 결정되는거지.

Two cycles, not one:

- **Weekly** — the market closes, prices are struck, indices are recalculated.
- **Monthly** — the analysts publish formal research: rating, target price, conviction, thesis. That research sets the anchor the weekly market moves toward.

In the same message the user added a requirement that follows from it: *"너의 모델은 이벤트를 감지할 무언가는 필요하네."* If prices move weekly and research only lands monthly, something has to supply the information in between. That is the Event Desk.

## The full cadence that follows

```text
CONTINUOUS   Event monitoring
WEEKLY       Market close, index calculation, market movers, Weekly Brief
MONTHLY      Full analyst research, rating and target review, valuation anchor reset
QUARTERLY    Index constituent review, listing and delisting review
ANNUALLY     THE STATE OF LONGING
```

Only the weekly and monthly layers are the user's decision. The quarterly and annual layers were proposed in the same conversation and are recorded as `working` on [[pricing-model]], not as decided.

## Why weekly and not real-time

Real-time pricing was considered and set aside for a reason that is as much about honesty as about aesthetics: a price that ticks by 0.01 every second has to be propped up with fabricated volume and a fabricated order book. A **weekly close** does not. It reads as a research institution observing a week's worth of the world and reweighing its market at a stated moment — `FRIDAY 17:00 UTC`.

```text
LTR     28.41    -1.82% W/W
WTG     34.92    +0.41% W/W
NTW     41.17    -0.22% W/W
CLL     19.81    -3.91% W/W
```

More institutional, less toy — and it keeps [[DEC-002-research-house-form]]'s register intact.

## Why the two cycles are separated

The separation removes the need for anyone to re-score securities by hand each week, and it creates the gap the work runs on. The monthly report is the considered judgment; the weekly print is the market's answer to it. Between them sits room for the market to be moving one way while the research says another — which is exactly the situation the analysts exist to argue about.

It also fixes the publication burden. Weekly output is a flash note, not a report:

```text
EVENT RESPONSE

LTR
Adrian Kessler

Replacement risk increased.
Estimate revised.

Target 18.50 → 17.20
Rating SHORT maintained.
```

Monthly output is the twelve-page initiating-or-maintaining-coverage document. One review flagged the operational arithmetic that this cadence still has to answer: four analysts across a large universe every month is an unshippable number of reports, and the realistic fix is that coverage should be sparse and uneven, with some securities carrying `NO COVERAGE` — which is also how real sell-side coverage looks. That refinement is recorded on [[analyst-system]], not decided here.

## Status

Confirmed. Stated by the user as an instruction, not a suggestion, and it overrode a proposal already on the table.

## Related

- [[pricing-model]]
- [[analyst-system]]
- [[DEC-002-research-house-form]]
- [[Q-001-price-formation]]

## Evolution — cadence within a fictional archive (2026-09-07)

The new conversation retains weekly prices and monthly formal research in its opening user brief. Its final user turn places weekly and monthly outlook/target records throughout the fictional history. This extends the cadence into an accumulated past rather than deciding how long future live operation must continue.

The assistant proposed weekly short/event or target-update records alongside monthly full research as a reconciliation. Exact weekly analyst obligations, coverage density, forecast horizons, and report length remain unselected; the samples and extended cadence above are not newly confirmed. [[analyst-system]] owns the historical record and scoring questions.

## Evolution — the week is the tick, so the candle is a month (2026-09-19)

A consequence of this decision that nothing had stated, found by drawing the
market rather than describing it. See [[loop-simulation]].

If prices strike weekly, **there is no intra-week high or low**. A weekly
candlestick therefore cannot be drawn on any LONGING surface: its wicks would be
data the world does not have, and inventing them is the failure mode the work is
built to avoid. The smallest honest candle is the **month** — four weekly strikes
supplying open, high, low and close — and any moving average on such a chart is
in months.

A weekly chart is still available as a line, which is what a weekly close is.
This constrains the terminal's chart furniture and nothing else: no cadence,
analyst obligation, or publication rule changes.

The same decision's other half was also found missing in the first build. This
page records that something must supply information between monthly research
notes; the first simulation had no event layer at all, and the resulting market
had no texture — smooth enough that a viewer would read it as drawn. The event
layer is now built, and [[information-quality]]'s distinction between events that
are true of the practice and events that merely move the quote is carried in it.
Neither the arrival process nor the true-event share is selected.

## Sources

- [[SRC-2026-09-19-market-texture-findings]] — [raw/documents/2026-09-19-market-texture-findings.md](../../raw/documents/2026-09-19-market-texture-findings.md); the candle-unit consequence and the missing event layer
- [[SRC-2026-09-07-artwork-brainstorm-v2]] — [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](../../raw/conversations/2026-09-07-artwork-brainstorm-v2.md); ChatGPT export, 2026-09-06–07; user turns support decisions, assistant synthesis and mechanisms retain proposal status

- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md)
