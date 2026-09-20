---
status: confirmed
attribution: user-confirmed
updated: 2026-09-21
sources:
  - SRC-2026-09-21-joint-shown-and-blocks-fitted-jointly
  - SRC-2026-09-20-joint-line-as-a-range
  - SRC-2026-09-20-hearts-cooling-line
---

# DEC-013 — The `Joint` width is shown to the audience, and the ledger's blocks are fitted jointly

## The decision

[[DEC-010-declared-order-with-a-joint-line]] made the `Joint` line the range, per line, over every admissible order. Two things it left open were put to the user on 2026-09-21 in plain language ([[SRC-2026-09-21-joint-shown-and-blocks-fitted-jointly]]): whether the width is shown to the audience, and whether the lines inside a block — the waves of the declared schedule, the priced factors — are themselves ordered or fitted as one.

> 일단 Joint 폭을 독자에게 보여주자.

> 응 B로 가자. 둘 다 기록해줘

**Two parts, `user-confirmed`:**

1. **The `Joint` width is shown to the audience.** It is not an additive line — the five lines of [[DEC-011-the-audience-ledger-reads-hearts-cooling]] still sum to the week's return — but a width carried beside each line, the amount that line would move under another admissible order. The user's first sentence decides showing; that it sits *beside* each line rather than as a sixth row follows from the range not entering the sum, and the parenthesised `±` form the assistant printed is `llm-proposed`. Its published name and wording are not decided; the assistant's note was only that it must not be confused with `Unexplained`, which is *unknown*, where `Joint` is *what the convention decided*.
2. **Blocks are fitted jointly.** Order exists only between the ledger's blocks, never within one. The lines of a block — several waves in the schedule, several priced factors, and any lines positioning or the reflexive term come to carry — are estimated together on what the preceding blocks left, so no order arises among them and no within-block overlap is produced. The admissible orders are permutations of the *movable blocks* under DEC-010's constraint, six on the current lines, and their count grows with the number of blocks, not with the number of lines. `Joint` is therefore one width per block, which is one width per receipt line.

## What part 2 closes on DEC-010

- *The internal order of the estimated block* — priced factors, then positioning, then reflexive — is no longer an order among lines within a block. Priced factors, positioning and the reflexive term remain three blocks in the sequence DEC-010 declares, and the reflexive block stays last by construction; what is closed is any question of order *inside* each of them.
- *Whether the schedule is one line or one per wave* — it is one block, fitted jointly, however many waves [[technology-waves]] carries. The per-wave split is available inside the block as a joint estimate, not as an ordered residualisation.
- *The exact-sum requirement* — unchanged from the range decision: `Joint` is a width and does not enter the sum, so no finite-change allocation rule is required by it.

## What it costs

Within a block, the shared variance of two lines — two waves that arrive together, two factors that move together — is not split by any rule; it stays inside the block's joint estimate. Per-line widths inside a block are not published. The assistant's reading, `llm-proposed`, is that a per-line diagnostic can be run separately later without touching this decision.

## What this does not decide

- The published name and wording of the width on the audience receipt, alongside the receipt's other wording ([[DEC-011-the-audience-ledger-reads-hearts-cooling]]).
- Where the numeraire revision appears on the audience receipt.
- How a width is drawn — parentheses, a band, a bar — and whether it is shown when it is zero.
- Which lines each block contains at the current universe, which is [[factor-identification-review]]'s question, not this one's.

## Related

- [[DEC-010-declared-order-with-a-joint-line]]
- [[DEC-011-the-audience-ledger-reads-hearts-cooling]]
- [[DEC-012-analyst-orders-inside-the-house-constraint]]
- [[attribution-ledger]]
- [[technology-waves]]
- [[identification-experiment]]

## Sources

- [[SRC-2026-09-21-joint-shown-and-blocks-fitted-jointly]] — [raw/conversations/2026-09-21-joint-shown-and-blocks-fitted-jointly.md](../../raw/conversations/2026-09-21-joint-shown-and-blocks-fitted-jointly.md); both decisions
- [[SRC-2026-09-20-joint-line-as-a-range]] — [raw/conversations/2026-09-20-joint-line-as-a-range.md](../../raw/conversations/2026-09-20-joint-line-as-a-range.md); the range decision these two complete
- [[SRC-2026-09-20-hearts-cooling-line]] — [raw/conversations/2026-09-20-hearts-cooling-line.md](../../raw/conversations/2026-09-20-hearts-cooling-line.md); the proposals first put, unanswered there
