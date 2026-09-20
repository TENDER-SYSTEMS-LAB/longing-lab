---
status: working
attribution: llm-proposed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-identification-experiment
  - SRC-2026-09-20-identification-experiment-findings
  - SRC-2026-09-20-factor-identification-prompt
  - SRC-2026-09-20-identification-experiment-v2
  - SRC-2026-09-20-identification-experiment-findings-v2
  - SRC-2026-09-20-wave-calibration-from-spine
  - SRC-2026-09-20-identification-experiment-findings-v3
  - SRC-2026-09-20-wave-calibration-from-national-series
  - SRC-2026-09-20-nia-internet-usage-survey-2025-record
---

# Identification Experiment

The executable check on [[factor-identification-review]]. Seven reviewers proposed the same procedure in that round's Section 7 — generate the panel this world produces, strip the lines the institute measures, and see what the listing can identify — and none ran it. On the user's instruction it was run on 2026-09-20 against the v3 harness of [[loop-simulation]], unmodified, with five seeds. Script and findings are registered; this page records what came out and what it does not establish.

**Nothing here selects a factor set, names a factor, or calibrates anything against the real world.** The harness's wave dates, loadings and coefficients are placeholders, so every number is a property of the generated world. All of it is `llm-proposed`.

## What the run does

Weekly log returns of the quote, 3 markets × 11 practices × 1,564 weeks. The numeraire line is removed exactly (the quote is `V·e^z / U`), then the declared arrival and substitution schedule is regressed out per security. The residual is what an estimator would have to explain. Early and late windows are the ones the harness's own convergence test uses.

## Five results

**The handover is real, and it runs through the interaction block.** Early, the residual's variance sits 45% in the practice contrasts, 35% in the practice × market interaction, and under 10% in each of the common and market blocks. Late, practice rises to 67% and interaction falls to 18%. GLM's handover shows, with a correction to its description: in this world a local shock is a practice-shaped loading on one market, which is interaction space, so what convergence drains is the interaction block rather than the two market contrasts, which were never large. This is the formal content of *a practice dying at three speeds is three cell effects, not a practice factor*.

**The count an estimator recovers depends on the window more than on the truth.** With the harness's event-factor count swept over 3, 6, 9 and 13, an eigenvalue-ratio estimator on the full panel collapses to one or two directions early whatever the truth, and late recovers eight of nine and nine of thirteen. **Thirteen is never recovered**; the late panel saturates near nine. The practice-average panel is the one that names factors late and is unstable early, as the round said. The market-demeaned panel over-counts small truths, which is a fact about the estimator, not the world.

**A fixed promotion threshold cannot work.** A random direction lowers held-out unexplained variance by about two percent by construction, so any fixed reduction threshold below about four percent promotes most planted nulls. Calibrated on the null's 95th percentile per window — the way Claude, GLM and ChatGPT specified — the held-out gate has power 0.89 early and 0.98 late against the generator's own factors. One gate of the battery; the others were not run.

**Two markets predict the third late and barely early.** Nine factors fit on two markets explain 23% of the third's residual early and 56% late. This is the transportability of the factor structure, and the mirror of the first result.

**The orthogonalisation order moves the schedule line — a lot, early.** Estimating the declared schedule line before versus after five factor components changes its weekly attribution by 1.45 times its own size early and 0.57 late, and nearly doubles the drift it carries early (−3.7 to −6.9 basis points a week). This gives the deferred order question a magnitude: in the early history the split between *substitution* and *factor* is mostly a convention, and the published order decides what the institute says caused the decline. See [[attribution-ledger]].

## What it does not establish

No factor names. No calibration: the [[proxy-sourcing-review]] spine retrieved the same day is not wired into the harness. One estimator, one gate, five seeds, two windows; rank tests, placebo on permuted arrival dates, stability and the post-publication check are not run. Positioning and reflexive lines are not stripped because the harness does not expose flows, so their content sits in the residual. The order experiment swaps two lines out of a six-line ordering.

## Second run — on the v4 world, two waves measured

The same day the mobile and broadband dates were replaced by logistic fits to the WDI spine ([[SRC-2026-09-20-wave-calibration-from-spine]]) and the run repeated on the v4 harness with the script's harness path made an argument — [[SRC-2026-09-20-identification-experiment-findings-v2]]. The sixteen design tests pass on v4. **Every one of the five readings holds.** The variance shares move by a few points and keep their shape; the early panel still collapses to one or two directions and the late panel still saturates near eight or nine, never thirteen; the calibrated gate's power stays above 0.9; two markets still explain the third only late. One number strengthened: the early order sensitivity rose from 1.45 to **1.85** times the schedule line's own size, because measured waves arrive later and closer together across markets, so in the early window less of the decline is the schedule's on its own and more of what the schedule line claims depends on whether the factor lines were removed first. The *placeholder* qualifier is weakened, not removed: five of seven waves are still guessed.

## Third run — on the v5 world, with the measured and the guessed side by side

Smartphone and social-web dates for Japan and the United States were then fitted from national series — [[SRC-2026-09-20-wave-calibration-from-national-series]] — with Korea left on placeholders, and the run repeated: [[SRC-2026-09-20-identification-experiment-findings-v3]]. Sixteen tests pass. The five readings hold in conclusion, but the early market and common blocks grow (0.10 → 0.14, 0.09 → 0.16), the estimator over-counts a truth of three early, cross-market transportability rises early and falls late, and the largest melt-up moves to 1998. All of it follows from one row: Korea's placeholder social-web date sits sixteen years before Japan's measured one, which itself dates a late survey definition. The v5 numbers are read as partly an artefact of mixing placeholders with measurements inside a wave; **v4 remains the cleaner comparison.** The early order sensitivity is 1.88.

## What it makes possible next

- Obtain a Korean smartphone series and a Korean social-web series that contains its own midpoint, so the two newly dated waves are measured in all three markets and the mix goes away; the data.go.kr file, MSIT's attachments and KOSIS all refused the session. The user then fetched the data.go.kr file by hand; it is 2025 microdata, one year, and gives a point (smartphone ownership 96.8%, SNS 61.3%) but not a series — [[SRC-2026-09-20-nia-internet-usage-survey-2025-record]]. The series still has to come from KOSIS or the annual reports.
- Run the rest of the gate battery, and the placebo on permuted arrival labels.
- Use the order-sensitivity number when the deferred orthogonalisation decision is taken up.

## Related

- [[factor-identification-review]]
- [[loop-simulation]]
- [[attribution-ledger]]
- [[DEC-005-ledger-resolution-scales-with-universe]]
- [[DEC-009-three-markets-and-convergence]]
- [[proxy-sourcing-review]]

## Sources

- [[SRC-2026-09-20-identification-experiment]] — [raw/documents/2026-09-20-identification-experiment.py](../../raw/documents/2026-09-20-identification-experiment.py); the script
- [[SRC-2026-09-20-identification-experiment-findings]] — [raw/documents/2026-09-20-identification-experiment-findings.md](../../raw/documents/2026-09-20-identification-experiment-findings.md); the tables and their reading
- [[SRC-2026-09-20-factor-identification-prompt]] — [raw/documents/2026-09-20-factor-identification-prompt.md](../../raw/documents/2026-09-20-factor-identification-prompt.md); Section 7, the procedure as asked for
- [[SRC-2026-09-20-identification-experiment-v2]] — [raw/documents/2026-09-20-identification-experiment-v2.py](../../raw/documents/2026-09-20-identification-experiment-v2.py); the script with the harness path as an argument
- [[SRC-2026-09-20-identification-experiment-findings-v2]] — [raw/documents/2026-09-20-identification-experiment-findings-v2.md](../../raw/documents/2026-09-20-identification-experiment-findings-v2.md); the five readings on v4 beside v3
- [[SRC-2026-09-20-wave-calibration-from-spine]] — [raw/documents/2026-09-20-wave-calibration-from-spine.md](../../raw/documents/2026-09-20-wave-calibration-from-spine.md); how the two dates were measured
- [[SRC-2026-09-20-identification-experiment-findings-v3]] — [raw/documents/2026-09-20-identification-experiment-findings-v3.md](../../raw/documents/2026-09-20-identification-experiment-findings-v3.md); the third run, on v5
- [[SRC-2026-09-20-wave-calibration-from-national-series]] — [raw/documents/2026-09-20-wave-calibration-from-national-series.md](../../raw/documents/2026-09-20-wave-calibration-from-national-series.md); the two further waves
