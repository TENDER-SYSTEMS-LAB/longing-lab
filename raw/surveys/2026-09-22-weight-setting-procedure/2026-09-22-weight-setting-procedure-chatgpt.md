## 1 — The unit of classification

I recommend a **versioned responsibility ledger**: first specify the finite responsibilities that constitute the practice, then classify them, then allocate a fixed budget across them. The resulting pair is approved only after independent reconstruction and cross-market checks.

The unit should be **a functional responsibility within a defined occasion of the practice**—not the whole occasion, an elapsed minute, a bodily movement, or every moment at which someone could choose otherwise.

A functional responsibility has an identifiable contribution: determining what is communicated, embodying an already-chosen message, authorizing its release, and so on. It can recur or be performed simultaneously with another responsibility without becoming a new unit each time. Task analysis provides a methodological precedent for separating physical and mental contributions and identifying how responsibilities are distributed between people and systems. It does not, by itself, supply the numerical weights proposed here. ([NASA][1])

My training cutoff is **December 2025**. The hard cases below are treated as stipulated cases, not as claims about subsequent technical capabilities or adoption.

### Define the boundary before decomposing

Each security needs a definition sheet specifying its starting boundary, completion boundary, included actors, required contributions, permissible variants, and exclusions.

For LETTER, I propose interpreting “released” as **entrusted to a delivery route addressed to the intended recipient**, rather than successfully received or read. This boundary interpretation requires the user’s approval before weighting. Otherwise, one analyst could count the carrier’s transportation work and another could stop at posting.

The earlier relationship, acquisition of literacy, manufacture of paper, and recipient’s eventual response are outside this boundary. Immediate preparation and handling necessary to produce and release the artifact are inside it.

### Proposed decomposition of LETTER

The table is a classification illustration, not an approved allocation. **No responsibility masses or security weights are assigned.**

| Parent responsibility  | Classification unit               | Required contribution                                                                                                                                                                 | Proposed label |
| ---------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Addressed intention    | Establish the addressed intention | Determine or adopt the particular recipient and the communicative purpose of this message.                                                                                            | Judgment       |
| Personal composition   | Determine content                 | Settle what thoughts, facts, questions, commitments, or omissions the message contains. Interpretation relevant to composing a reply belongs here.                                    | Judgment       |
| Personal composition   | Determine expression              | Settle wording, arrangement, tone, and any deliberately expressive visual choices. Revisions of these choices remain within this responsibility.                                      | Judgment       |
| Handwritten embodiment | Produce the handwritten artifact  | Prepare the immediate writing means and physically inscribe the chosen expression, including implementation of chosen corrections.                                                    | Execution      |
| Authorized release     | Authorize this message’s release  | Adopt the artifact as the message to release, including consequential decisions about destination, timing, privacy, or handling. This need not be a separate conscious review ritual. | Judgment       |
| Authorized release     | Prepare the authorized route      | Address, package, or otherwise prepare the artifact as the selected route requires, using already-settled release conditions.                                                         | Execution      |
| Authorized release     | Perform the release               | Place or hand the artifact into that route.                                                                                                                                           | Execution      |

These are responsibilities, not a mandatory chronological script. Someone may compose while handwriting. Someone may revise repeatedly. Someone may hand-deliver without packaging. Those variations do not automatically add units.

In particular, the table does **not** require proofreading, multiple drafts, an envelope, or a separately articulated decision to send. Optional procedures sit inside their parent responsibility; they are not silently promoted into defining requirements.

### The stopping rule

Every unit must have a card recording its input, contribution, completion criterion, unresolved choices, and exclusions.

Split a unit when it contains contributions that can be separately specified or assigned—for example, choosing wording and producing its physical trace. Stop splitting when further divisions merely repeat the same responsibility or describe implementation details.

Every proposed subdivision must identify where its contribution was previously counted. **Subdivision redistributes an existing parent’s budget; it cannot create additional budget.** This prevents handwriting from gaining weight merely because an analyst lists more strokes than decisions.

The decomposition is complete when every defining contribution has a home, no contribution is counted twice, and the agreed range of valid occasions can be described without inventing new responsibilities.

## 2 — The sorting rule

I would replace “the handed-over step contained more than one live option” with a more restrictive test:

**Does fulfilling this responsibility require settling a meaning, intention, interpretation, commitment, or consequential preference that remains unresolved by the practice’s definition and the upstream instructions?**

If yes, classify that responsibility as **judgment**. If those matters are already settled and the responsibility is to realize, transmit, recover, or check their faithful implementation, classify it as **execution**.

The distinction concerns the responsibility being performed, not whether its performer is a human, whether the algorithm is deterministic, or whether the work is difficult.

### What counts as a live option?

A live option must remain permissible after the supplied instructions are respected, and choosing it must settle something relevant to the communicative or relational act.

Alternative pen trajectories are not automatically alternative judgments. Competing guesses about which sentence a person already intended are not automatically alternative authorial choices. Conversely, choosing a more distant rather than intimate formulation can be judgment even when a system makes that choice instantaneously.

Each judgment classification therefore needs a **choice witness**: a description of alternatives that satisfy the upstream instructions but leave a consequential distinction unsettled.

Each execution classification needs a **specification witness**: an account of what has already been settled and how completion can be assessed without supplying a new communicative preference.

A consequential distinction should be specified before inspecting an interesting case. The ledger should recognize meaning, relational stance, disclosure, commitment, authorization, and deliberately expressive form. It should not classify accidental variation as judgment merely because an observer could later attach significance to it.

### Application to the hard cases

| Hard case                                                                                               | Classification                                                                                                                                                                 | Why                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Voicing a sentence the person has chosen                                                                | **Execution**, provided the system faithfully realizes the intended sentence and already-settled expressive requirements.                                                      | The system supplies the means of expression, not the message’s consequential choice. Recovering an intended sentence from uncertain signals is not, merely because recovery is uncertain, authorship of a new sentence. Under the stipulated mechanism, restoring that means belongs to arrival.      |
| Reading a chosen text aloud in a voice learned from another person                                      | **Execution for the rendering itself.** Selection of voice identity or consequential expressive treatment is a separately classified responsibility when it remains unsettled. | A learned voice does not make the rendering judgment by itself. But choosing to sound like a particular person, or choosing an emotionally consequential delivery, need not be mere implementation.                                                                                                   |
| Sending “how are you” and letting a system decide its translation                                       | **Judgment substituted for the delegated formulation**, with any faithful transmission classified separately as execution.                                                     | In the stipulated case, the intention to ask after someone does not settle how that intention should be expressed to this recipient. The system resolves that underdetermination. The sender’s broad intention and final approval do not retrospectively make the system’s wording choices execution. |
| Reading a system’s interpretation before the original message, with one’s decision consequently changed | **Judgment retained under system framing**, with any identifiable upstream interpretive selection also classified as judgment.                                                 | Explicit handover is not required for a system to select an interpretation or make some considerations salient. Nevertheless, a changed final decision alone does not establish that final decision authority was transferred.                                                                        |

The last case requires particular restraint. The ledger should distinguish the person’s final judgment from upstream selection of interpretations, evidence, or options. It must not count the same interpretive responsibility again merely because both person and system contribute to it.

Where the only known fact is “the interpretation was read first and the response changed,” the defensible classification is **judgment under framing; allocation of control unresolved**. This procedure cannot determine from that description how much judgment was substituted. Nor should that uncertainty change the security’s fixed judgment share.

More generally, “translation” is not a permanent judgment label attached to a technology. An explicitly prescribed conversion that leaves no relevant expressive choice unsettled would pass the execution test. That does not alter the classification of the stipulated translation case.

### Mixed units

An occasion can be both execution and judgment; so can a coarse description such as “write the sentence.” The preferred response is to separate its responsibilities analytically, even when they occur simultaneously.

A mixed parent’s division is then derived from its children’s approved responsibility budgets under Section 3. **The classification reviewers identify the responsibilities; the allocation reviewers propose their relative masses; the user ratifies them.**

A split is not set by averaging opposing labels. Disagreement between an execution label and a judgment label is not evidence that the unit is partly each.

Where a contribution genuinely cannot be separated, retain competing classifications and carry them into the uncertainty assessment. The fallback is an explicit boundary convention approved by the user, or withholding approval—not an automatic compromise fraction.

## 3 — The counting rule

I recommend **constitutionally weighted functional coverage**: allocate a fixed responsibility budget according to the contributions’ importance to the identity of the defined practice, then total the budget assigned to each category.

This makes a necessary assumption explicit. There is no common physical unit supplied here that makes a minute of handwriting commensurable with a decision about what to disclose. The institution must adopt a meaning for “share.” Equal counting would also be a substantive convention, not the absence of one. The OECD/JRC handbook similarly notes that weighting embodies judgments and that equal weighting can unintentionally favor dimensions represented by more items. ([OECD][2])

Under this proposal, the pair describes **the institution’s allocation of the practice’s constitutive responsibilities**. It does not describe a fraction of elapsed time, mental effort, social benefit, or observed automation.

### How the responsibility budget is elicited

Use a total budget of **100 responsibility points** as a protocol convention. This is an allocation device, not a proposed weight for any security.

First allocate that budget among the parent responsibilities. Then distribute each parent’s budget among its children. Each reviewer submits a complete allocation, rather than independently scoring items and leaving their relative scale unspecified.

The precedent is the budget-allocation method, in which informed assessors distribute a fixed total and their allocations are recorded and combined. My proposed hierarchy, separation of classification from allocation, and approval tests are additional requirements for LONGING, not properties established for it by that precedent. ([OECD][2])

The allocation question should be fixed in the handbook:

**How much of this practice’s defining identity is carried by this responsibility, considered over its full stated scope, rather than by its duration, difficulty, prestige, or consequences in a particular occasion?**

Reviewers should receive parallel responsibility cards with comparably detailed descriptions. They should not see execution/judgment totals, existing coefficients, or generated historical readings while allocating. Hiding category totals does not make them ignorant of the responsibilities’ character; it removes a direct numerical target.

To make the allocation more than an unsupported impression, require comparisons between counterfactual definitions that relax different responsibilities while preserving the others. These are elicitation probes, not actual amendments to the security. The reviewer explains which relaxation changes the practice’s identity more, then checks whether the proposed budget is consistent with that explanation.

**Rankings are insufficient to determine ratios.** A reviewer who can defend an ordering but not the numerical distances must submit an admissible allocation range, not invented cardinal precision.

Likewise, finding every responsibility indispensable does not establish their relative shares. Indispensability may identify membership in the definition without identifying a numerical allocation among its members.

### How allocations become the pair

Once classification is resolved, assign every responsibility point exactly once to execution or judgment. Sum each category and divide by the total budget.

For mixed parents, use the allocations of the classified children. Repeated performance does not multiply a responsibility’s budget. Further subdivisions must conserve the parent allocation.

The proposed allocation is the arithmetic mean of the reviewers’ complete, admissible budget allocations, with equal influence for each market. This averaging occurs **only after classification disputes and the cross-market eligibility checks have been addressed**. It is a declared aggregation convention, not a claim that the mean discovers a naturally true weight.

An unresolved responsibility cannot be made to disappear by assigning the unexplained remainder to the other category.

### What this rule assumes—and distorts

| Counting basis                 | What it would assume                                                                 | Why I would not adopt it as the primary rule                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Equal count of listed steps    | Every listed step carries the same share.                                            | The answer depends on how finely different parts are described.                                                                    |
| Time                           | Duration measures the relevant composition of the practice.                          | The answer becomes conditional on speed, skill, capacity, and the selected occasion.                                               |
| Consequence of failure         | Greater potential loss means a larger share of the practice.                         | A consequential disclosure or release decision could dominate because of stakes rather than because of the practice’s composition. |
| Observed reasons for failure   | Frequent bottlenecks identify the underlying shares.                                 | The result depends on the circumstances and population in which failure was observed.                                              |
| Proposed responsibility budget | Constitutive importance can be explicitly allocated on a common institutional scale. | It depends on interpretive judgments about the practice’s identity and can overvalue culturally prestigious contributions.         |

Consequences still help identify whether an option is consequential enough to count as judgment. They do **not** automatically determine its responsibility mass.

I would also avoid presenting this as ordinary outcome-based swing weighting. In multi-criteria analysis, swing weights depend on defined changes across performance ranges; transferring that interpretation here would introduce a different quantity from responsibility composition. ([GOV.UK][3])

The principal limitation is therefore irreducibly constitutional: evidence can constrain the responsibility map and expose inconsistent allocations, but it cannot supply an institution-independent answer to every comparison of constitutive importance. Where a numerical distinction cannot be defended, the user must either adopt an explicit convention or leave the pair unapproved.

## 4 — Who sets it, and how disagreement is resolved

The user should receive **one proposed pair, its complete derivation, and the remaining admissible range**—not a naked percentage, and not an invitation to adjust a slider until the result feels right.

The approval packet should contain the definition sheet, responsibility tree, unit cards, independent classifications, independent budget allocations, disagreement record, cross-market comparison, reconstruction results, and proposed pair.

### Separate the roles

Use two independent classification reviewers for each initial assessment, including relevant practice and language competence. A methodology reviewer checks boundaries, duplicated responsibilities, and application of the sorting rule.

Budget allocation should occur in a separate pass, preferably with additional reviewers who have not participated in the classification dispute. Practitioner and accessibility evidence should be included where the boundary questions require it.

An independent reconstruction team must then repeat the substantive procedure without seeing the first team’s pair or allocations. Copying an approved ledger and obtaining the same sum demonstrates arithmetic reproducibility, not independent reconstruction.

The published assessment record should identify assessor selection, independence, materials, and the agreement procedure. Reliability-reporting guidance supports documenting these design choices rather than reporting an agreement result without its conditions. ([PubMed][4])

### Resolve a disputed label at its source

When two reviewers disagree, require each to write the other classification’s strongest case. Then identify the disagreement’s level.

| Disagreement                                                                     | Resolution                                                                                |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| They assumed different upstream instructions.                                    | Restate the instructions and repeat the test.                                             |
| They identified different responsibilities inside the same phrase.               | Split or clarify the unit while conserving its parent budget.                             |
| They disagree about whether an alternative changes meaning or relational stance. | Require concrete alternatives and native-language or practice evidence.                   |
| They agree on the facts but disagree about the security’s intended boundary.     | Put the boundary choice to the user explicitly.                                           |
| They agree on classification but not responsibility mass.                        | Retain the competing allocations; resolve through the counting procedure, not relabeling. |
| Available evidence does not discriminate.                                        | Preserve the ambiguity and test its numerical effect. Do not manufacture consensus.       |

The user can accept the proposed allocation or issue a reasoned ruling on a boundary or allocation convention. A substantive change must then pass reconstruction again. User authority settles the institution’s definition; it does not convert dissent into empirical agreement.

### Tolerance and approval gate

I propose an **absolute reconstruction tolerance of 0.02 in either share—two percentage points**. This is a protocol acceptance threshold, not an assertion that any security already meets it.

Approval requires independently reconstructed pairs and the admissible alternatives retained after review to fit within a total span no wider than that tolerance. The range is a **sensitivity envelope**, not a statistical confidence interval. Its extremes must come from coherent allocations that respect all budget constraints.

Aggregate agreement alone is insufficient. On the aligned responsibility map, compare execution allocations and judgment allocations unit by unit. Add their absolute differences and divide by two. Require this total reassigned responsibility mass also to remain within 0.02. This prevents opposite disagreements from canceling into an apparently identical pair.

Alignment must follow demonstrated equivalence of responsibilities, not convenient matching of labels. Purely descriptive split-and-merge operations must reproduce the pair exactly.

Publish the pair to two decimal places and retain the full allocation record internally. Extra stored digits are bookkeeping, not extra evidential precision.

If the gate fails, the result is **not yet approved**. The fallback is further evidence, an explicit constitutional ruling, or withholding listing. The tolerance should not be relaxed merely because the reviewers have already spent substantial time.

## 5 — Cross-market consistency

The procedure should yield **one pair for one security definition across Japan, Korea, and the United States**.

Local assessments are independent tests of that common definition, not automatic entitlements to different coefficients. This requires testing conceptual equivalence, not merely translating an English form. The International Test Commission distinguishes linguistic translation from the broader work of establishing that a construct and its interpretation remain comparable across populations. 

Prepare the responsibility cards jointly across the languages. Native-language reviewers should assess functionally matched cases, and bilingual reviewers should check whether distinctions such as faithful rendering, interpretive selection, consequential expression, and authorization survive translation.

Each market produces its own provisional decomposition, classifications, allocation, and uncertainty record before reconciliation. It must also pass an independent within-market reconstruction.

The comparison then asks whether reviewers identified the same responsibilities, interpreted their boundaries equivalently, and allocated their importance consistently. Differences in strokes, conventions, available tools, or ordinary speeds do not automatically imply different responsibility shares under the proposed counting rule.

### Detecting condition (b)

Because the published pair is common, disagreement cannot be detected simply by comparing the published coefficients. Maintain **independent diagnostic re-estimates by market**.

Condition (b) is satisfied when a same-definition cross-market difference exceeding the stated tolerance persists after each market passes its internal reconstruction check, and an independent repeat reproduces the discrepancy. A lone outlier or an internally unstable assessment is grounds for investigation, not sufficient evidence of a stable market disagreement.

The first response is to locate the cause: translation, different occasion assumptions, different practice boundaries, or genuinely different judgments about constitutive importance.

Do not average incompatible interpretations merely to obtain a common pair. Reconcile them through a reasoned common ruling, or conclude that the intended common definition has not been established. Where the actual responsibilities differ, a definition change may be necessary.

Unit-level disagreement with identical aggregate pairs remains an audit warning. **It does not, by itself, satisfy condition (b)** if the security’s execution and judgment weights do not disagree.

## 6 — The revision procedure

Any analyst, market reviewer, auditor, reader, or the user may submit a revision request. Only the user authorizes a revised pair.

A request must establish an eligible trigger **before a replacement pair is selected**.

| Permitted trigger                                           | Evidence required                                                                                                                                                               | What does not qualify                                                                                                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **(a) A defining step is added or removed**                 | An approved before-and-after definition, a responsibility-level semantic difference, and an explanation of which occasions now qualify or cease to qualify.                     | Renaming a responsibility, describing it more finely, changing an example, or changing one’s preferred allocation while the practice remains unchanged. |
| **(b) The same security’s weights disagree across markets** | Same-version local assessments, their underlying ledgers, successful internal reconstruction checks, and a reproduced cross-market discrepancy beyond the registered tolerance. | Differences in generated readings, technology adoption, narrative fit, or a single unsupported estimate.                                                |

A subdivision is not an added step unless it represents an actual addition to the practice’s definition. This distinction prevents analysts from using a more elaborate task description as a pretext for revising a coefficient.

Once a trigger is accepted, reopen the affected responsibilities and their budget relationships. Recheck the full allocation for conservation, duplication, and cross-market consistency. Responsibilities outside the substantive change should retain their prior rationale unless the revision identifies a specific dependency.

Weight-setting reviewers should remain insulated from generated readings during this work. Outcomes are not evidence in the approval packet.

### Required revision record

| Record component      | Required contents                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Identity              | Security identifier, old and new definition versions, old and new weight-record versions.                                           |
| Trigger               | Condition (a) or (b), initiator, supporting evidence, and the user’s eligibility decision.                                          |
| Substantive change    | Changed responsibilities, labels, boundaries, or allocation judgments, with old-to-new mappings.                                    |
| Numerical derivation  | Complete old and new allocations, resulting pairs, retained alternatives, and explanation of every changed contribution.            |
| Review                | Independent assessments, disagreements, rulings, reconstruction tests, and cross-market checks.                                     |
| Timing                | Approval date, publication date, and the definition period to which each version applies.                                           |
| Publication treatment | Which existing readings retain their original basis, which are superseded, and which appear in a separately identified restatement. |

### Already-published readings

Published records should be immutable and carry their exact definition and weight versions.

For **condition (a)**, old readings remain readings of the old definition. A newly added or removed responsibility must not be silently projected backward as though it had always belonged to that security. Any retrospective presentation using the new definition must be explicitly distinguished from the original record.

For **condition (b)**, the institution may publish a corrected edition for the unchanged definition’s applicable span. That edition should be identified as a methodological restatement, preserve the original edition, and isolate the weight revision from unrelated input revisions. It should not silently splice the replacement coefficient into the record at the administrative approval date.

A transcription or arithmetic error that misreports the already-approved pair can receive an erratum without changing that pair. That is correction of publication, not revision of the approved weights.

There is a harder limit under the stipulated rules: a substantively defective approved pair that agrees across all markets, with no definition change, has no eligible revision trigger. The institution should record the defect and suspend further use if necessary—not fabricate a definition change or market disagreement.

## 7 — Failure modes

The ranking below concerns **difficulty of detection after publication**, not probability or severity.

| Rank    | Failure mode                                                                                          | Why it can produce a confident wrong pair                                                                                                                      | Principal safeguard                                                                                    |
| ------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Hardest | **The allocation measures the wrong construct.**                                                      | Reviewers consistently allocate nostalgia, prestige, effort, or moral importance while calling it responsibility composition. Excellent agreement can survive. | Fixed allocation question, comparative rationales, and explicit limits on interpretation.              |
| Next    | **A shared cultural, historical, or capacity assumption defines the reference practice incorrectly.** | Every reviewer can agree because the same excluded kind of occasion never enters the evidence packet.                                                          | Independently assembled practice evidence, boundary cases, and cross-market challenge.                 |
| Next    | **Outcome expectations enter ostensibly independent reasoning.**                                      | A preferred pair can be justified afterward through plausible decomposition or budget choices.                                                                 | Outcome insulation, dated submissions, and preservation of first-pass records.                         |
| Next    | **Interacting responsibilities are treated as independently allocable.**                              | A contribution may exist only through the combination of expression and embodiment, yet receive apparently precise separate masses.                            | Interaction cases, alternative decompositions, and explicit conventions for inseparable contributions. |
| Next    | **Consensus is manufactured through correlated reviewers or reconciliation pressure.**                | Repeated outputs from one model or tightly shared training materials can be mistaken for independent confirmation.                                             | Independent recruitment and reconstruction; retain pre-reconciliation disagreement.                    |
| Next    | **Unresolved judgment is hidden inside “implementation.”**                                            | Translation, framing, defaults, and expressive delivery can be labeled execution because no explicit decision handover occurred.                               | Choice witnesses and a separate record of upstream interpretive selections.                            |
| Next    | **Every implementation alternative is inflated into judgment.**                                       | Motor variation and uncertainty about an already-chosen intention are confused with authorial choice.                                                          | Specification witnesses and the requirement that a consequential preference remain unsettled.          |
| Next    | **Segmentation changes the answer or duplicates responsibility.**                                     | More detailed descriptions receive more weight; authorization or interpretation is counted repeatedly.                                                         | Conserved parent budgets and exact split-and-merge tests.                                              |
| Next    | **Opposing disagreements cancel in the final pair.**                                                  | Reviewers reach the same totals through incompatible classifications or allocations.                                                                           | Unit-by-unit responsibility-mass comparison, not aggregate agreement alone.                            |
| Easiest | **Arithmetic, rounding, or version-control errors.**                                                  | The published pair differs from the approved ledger, or readings cite the wrong definition.                                                                    | Exact budget reconciliation, version identifiers, and publication checks.                              |

The procedure can establish that a pair follows a disclosed definition and allocation convention, survives specified challenges, and can be independently reconstructed within tolerance. It cannot establish that constitutive importance has a unique natural numerical scale.

**The defensible claim is therefore a reproducible, carefully justified institutional assignment—not an objectively discovered percentage disguised by decimal precision.**

[1]: https://www.nasa.gov/reference/3-0-systems-engineering-processes-vol-2/ "3.0 Systems Engineering Processes - NASA"
[2]: https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf "Handbook on Constructing Composite Indicators: Methodology and User Guide (EN)"
[3]: https://www.gov.uk/government/publications/green-book-supplementary-guidance-multi-criteria-decision-analysis/use-of-multi-criteria-decision-analysis-in-options-appraisal-of-economic-cases "Use of Multi-Criteria Decision Analysis in options appraisal of economic cases - GOV.UK"
[4]: https://pubmed.ncbi.nlm.nih.gov/21130355/?utm_source=chatgpt.com "Guidelines for Reporting Reliability and Agreement Studies (GRRAS ..."
