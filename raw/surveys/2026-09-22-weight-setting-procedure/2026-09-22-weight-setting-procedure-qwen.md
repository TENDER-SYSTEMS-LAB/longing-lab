Training cut-off: January 2025. No claims regarding real practices after this date are relied upon in the design of this procedure.

## Section 1 — The unit of classification

The unit of classification is the **Canonical Step**. A Canonical Step is a discrete, necessary cognitive or physical action required to move the practice from initiation to completion, as defined by the security’s foundational prospectus. It is neither the entire practice (too coarse) nor a fleeting micro-moment (too fine and subjective). 

To ensure precision, a practice is decomposed into a finite list of Canonical Steps. No step may be added or removed without triggering the revision procedure. 

**Decomposition of the reference security, LETTER:**

| Canonical Step | Description |
| :--- | :--- |
| 1. Conception | Deciding to write, identifying the specific recipient, and establishing the core intent. |
| 2. Composition | Drafting the specific words, meaning, and emotional tone of the message. |
| 3. Physical Production | The physical acts of handwriting the text, addressing the envelope, and sealing it. |
| 4. Dispatch | Releasing the physical item to the delivery route (e.g., dropping in a mailbox). |

## Section 2 — The sorting rule

The test for classifying a Canonical Step relies on the nature of the options available during that step. 

**The Sorting Test:** 
A step is classified as **Judgment** if its essential function is to select among multiple live options to determine the *meaning, content, or consequential direction* of the practice. 
A step is classified as **Execution** if its essential function is the physical or mechanical realization of a meaning already determined, where the options are constrained to a single correct physical outcome (i.e., there is no meaningful choice about *what* is being done, only the physical mechanics of doing it).

**Application to the hard cases:**

1. **Execution with a restoring side (voicing a chosen sentence / reading in a learned voice):** The meaning was determined in a prior step. The voicing or reading is the physical realization of that determined meaning. Therefore, this is classified as **Execution**. (The fact that it restores a lost capacity affects its *exposure* to execution restoration, but not its fundamental weight).
2. **Execution handing over deliberation whole (sending "how are you" for system translation):** The user inputs a placeholder, but the system selects the consequential meaning, tone, and phrasing in the target context. Because the system is selecting among live options to determine the final content, this step is classified as **Judgment**.
3. **Judgment kept but narrowed (system interpretation read before original):** The person still makes the final choice among the remaining live options. Because the consequential choice is still exercised by the person, the step remains classified as **Judgment**. (The narrowing affects the *exposure* to judgment substitution, not the step's inherent weight).

**Handling partial overlap:**
A Canonical Step is never split into fractions. If a step inherently fuses physical doing and meaning-making (e.g., choosing a specific physical paper that alters the message's aesthetic meaning), it is assigned to the category of its **primary bottleneck**. If the physical constraint limits or dictates the meaning, it is Judgment. If the meaning is fixed and the physical act is merely the medium, it is Execution. 

## Section 3 — The counting rule

Classified units are aggregated into a pair summing to one using **Proportional Baseline Median Duration**. 

For each Canonical Step, the procedure measures the median time a competent practitioner spends on that step in the baseline year (1996). The execution share is the sum of the baseline median durations of all Execution steps, divided by the total baseline median duration of all steps. The judgment share is the remainder.

*Illustrative calculation for LETTER:*
* Conception (Judgment): 2 minutes
* Composition (Judgment): 10 minutes
* Physical Production (Execution): 3 minutes
* Dispatch (Execution): 1 minute
* Total time: 16 minutes. 
* Judgment share: 12 / 16 = 0.75. Execution share: 4 / 16 = 0.25. *(Numbers are illustrative).*

**Assumptions and Distortions:**
This rule assumes that the time spent on a step is a valid proxy for its "share" or weight in the practice. The primary distortion is that it ignores cognitive intensity and consequence. A one-second judgment (the decision to write the letter at all) may be more defining to the practice than ten minutes of physical handwriting, but the time-weighting rule will assign the handwriting a higher share. 

## Section 4 — Who sets it, and how disagreement is resolved

The user is presented with a **Decomposition and Classification Matrix** (the list of Canonical Steps, their baseline durations, and their sorted labels), rather than just a final pair. The user reviews the logic of the decomposition and the sorting before the math is finalized.

**Disagreement Resolution:**
If two analysts disagree on the label of a specific Canonical Step, they do not average their views. The procedure uses **Blind Adjudication**:
1. A third, independent analyst classifies the step without seeing the previous labels.
2. If two out of three analysts agree, that label stands.
3. If all three analysts choose a different label (a three-way split), the step is deemed ambiguous. The fallback is to redefine the step by splitting it into two distinct sub-steps, or to assign it to the category of its primary bottleneck via a majority vote of the Security Custodian.

**Tolerance:**
The final mathematical pair must be exact to two decimal places. However, the user may apply a **User Override** to adjust a weight by up to ±0.05 for philosophical or structural reasons. If overridden, both the mathematical sum and the user-adjusted pair are recorded, and the user-adjusted pair becomes the official weight.

## Section 5 — Cross-market consistency

The procedure initially yields **one pair per market** (Japan, Korea, United States). This is because local practitioners may decompose the practice or measure baseline durations slightly differently based on local cultural norms.

**Detecting Disagreement:**
Condition (b) states that a security's weights revising due to cross-market disagreement is a ground for revision. The procedure detects this by calculating the variance of the execution and judgment shares across the three markets. 
If the absolute difference between the highest and lowest market share for either execution or judgment exceeds a tolerance of **±0.10**, condition (b) is triggered. This variance indicates that the markets are no longer pricing the same underlying practice, necessitating a revision to harmonize the weights into a single universal pair, or to formally split the security into three distinct market-specific securities.

## Section 6 — The revision procedure

Revisions are strictly limited to conditions (a) and (b). 

**The Revision Record:**
When initiated, the record must contain:
1. The specific condition triggered ((a) definition change or (b) cross-market variance > 0.10).
2. The evidence (a redlined prospectus document for (a); a statistical variance report for (b)).
3. The old pair and the proposed new pair.
4. The effective date of the revision.

**Initiation and Evidence:**
* Condition (a) is initiated by the **Security Custodian**. Evidence is a formal amendment to the security's definition (a step added or removed).
* Condition (b) is initiated by the **Market Harmonization Committee**. Evidence is the quarterly variance report showing the cross-market tolerance breach.

**Effect on past readings:**
Past readings are **never restated**. The old pair remains the historical truth for the era in which it was active. A "revision breakpoint" is logged in the time series. Future exposures are calculated using the new pair from the effective date forward. Tuning the new pair to make the historical price record look better is explicitly rejected.

## Section 7 — Failure modes

The ways this procedure could produce a confident wrong pair, ranked from hardest to detect to easiest to detect:

1. **The Baseline Time Distortion (Hardest to detect):** The procedure relies on 1996 median times, but the time spent does not actually correlate with the true "weight" or importance of the practice (as noted in Section 3). Because the math is internally consistent, this error is hidden behind a veneer of precision and is detectable only through deep philosophical debate about the nature of the practice.
2. **The Step Granularity Trap (Medium to detect):** The analysts define the Canonical Steps too finely or too coarsely to force a desired weight (e.g., splitting "Composition" into five sub-steps to inflate the Judgment share). Detectable by reviewing the decomposition logic, but requires deep domain knowledge to catch.
3. **The Hard Case Misclassification (Medium to detect):** Misapplying the sorting rule to the hard cases (e.g., treating "narrowed judgment" as execution because the option space was altered). Detectable by stress-testing the hard cases against the sorting test, but requires careful logical review.
4. **The Cross-Market Illusion (Easiest to detect):** The procedure forces a single universal pair to satisfy condition (b), but the practice actually means something fundamentally different in Japan than in the US. The math will show low variance, but the pair is conceptually wrong for one market. Easily detected when local practitioners complain that the security no longer reflects their local practice.

## Objections

I object to Fixed Point 2 on the grounds that in many modern practices, the boundary between execution and judgment is practically porous; the "doing" inherently shapes the "choice" (e.g., an algorithmic curation system that physically executes the delivery of a message inherently shapes the consequential choice of *who* receives it by filtering the audience). However, recognizing that this point is fixed and not open in this round, the procedure is designed to strictly enforce the separation, treating any handover of the physical doing that alters the consequential choice as a handover of judgment, as instructed.