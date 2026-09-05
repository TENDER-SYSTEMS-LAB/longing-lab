# LONGING — Pricing Model v2: Factor Framework

**Date:** 2026-09-05  
**Status:** Working proposal  
**Purpose:** Reframe the macro/factor layer of LONGING's pricing engine before selecting the actual factor set.

---

## 1. Why this revision is necessary

The first pricing-model discussion produced a broad set of structural variables:

- Efficiency
- Automation
- Predictability
- Mediation
- Immediacy
- Digitization
- Optimization

The subsequent multi-model review converged on one criticism: these variables were too close to one another to function as independent pricing factors. If they all rise together as manifestations of the same underlying modernization process, then treating them as separate explanatory forces creates several problems:

1. unstable or arbitrary factor sensitivities;
2. double counting;
3. attribution that looks precise but is not causally meaningful;
4. securities moving together for effectively the same reason under different labels.

I agree with that criticism.

However, I do **not** think the correct conclusion is that LONGING should therefore have only one factor, or that the final pricing model should remain simple.

The better conclusion is:

> **LONGING should be allowed to become highly complex, but only after its complexity is decomposed into causally distinct mechanisms.**

The central aesthetic contrast of LONGING benefits from this.

The securities themselves concern subjective, fragile, romantic, difficult-to-measure human practices.  
The institution that prices them should be almost obsessively quantitative, systematic, auditable, and internally coherent.

The system should look as though it has spent an unreasonable amount of effort calculating the price of something that may resist calculation in the first place.

---

## 2. New design principle

The factor set should not be chosen by asking:

> How many factors should LONGING have?

Instead, it should be chosen by asking:

> **Does this factor explain a different causal story from the other factors?**

A factor deserves to exist only if it can pass most of the following tests.

### 2.1 Causal distinction

Can the factor change while another factor remains roughly unchanged?

If not, they may be two names for one underlying force.

### 2.2 Cross-sectional distinction

Does the factor affect different securities in meaningfully different ways?

For example, a factor that strongly affects handwritten letters but barely affects live performance may deserve to remain separate from one that affects both equally.

### 2.3 Event distinction

Can we point to real or fictional events that primarily move this factor rather than all factors at once?

If every plausible event raises five factors simultaneously, the decomposition is probably weak.

### 2.4 Temporal distinction

Does the factor operate on a different time scale?

A slow structural force and a fast cyclical premium may both matter even when they are related.

### 2.5 Sign distinction

Can some securities have positive exposure while others have negative exposure?

This is especially valuable because LONGING must be able to produce structural winners, not only decliners.

### 2.6 Attribution value

When a weekly price move is decomposed, does showing this factor separately make the explanation more meaningful?

If removing the factor barely changes the story, it probably does not deserve its own line.

### 2.7 Observability / estimability

Can the factor be inferred from a defensible set of observable indicators, modeled variables, or editorial assessments?

A factor may be latent, but it should not be a free artistic control knob.

---

## 3. Complexity should be hierarchical, not flat

The first model treated many visible indicators as though each were a pricing factor.

I now think the system should distinguish at least three levels:

```text
OBSERVABLE INDICATORS
        ↓
LATENT / STRUCTURAL FACTORS
        ↓
SECURITY-SPECIFIC EXPOSURES
        ↓
PRICE EFFECTS
```

For example:

```text
OBSERVABLE INDICATORS

Immediacy
Automation
Predictability
Digitization
Optimization
Platform Mediation
Delivery Latency
Recommendation Penetration
AI Substitution
Scheduling Density
etc.

        ↓

LATENT FACTORS

Time Compression
Human Substitution
Mediation
Uncertainty Compression
Physicality Displacement
Coordination Compression
Scarcity / Friction Premium
etc.

        ↓

SECURITY EXPOSURES

LTR — Handwritten Letter
WALK — Aimless Walking
VISIT — Unplanned Visit
FILM — Film Photography
LIVE — Live Performance
SOL — Solitude
...
```

This preserves the rich Bloomberg-like surface without pretending that every visible indicator is an independent source of risk.

The interface can therefore be information-dense while the underlying model remains structurally intelligible.

---

## 4. Candidate factor families

The following are **working hypotheses**, not a final factor set.

The important point is not the names.  
The question is whether each can be demonstrated to represent a different causal mechanism.

---

### 4.1 Time Compression

**Question:** How much time between desire, action, and outcome is being removed?

Possible observables:

- average response latency;
- same-day / instant fulfillment penetration;
- synchronous communication share;
- on-demand availability;
- delivery speed;
- time-to-information;
- booking or coordination lead time.

Possible exposures:

- Handwritten Letter: strongly negative
- Waiting for a Reply: strongly negative
- Unplanned Visit: moderately negative
- Film Photography: moderately negative
- Live Performance: weak / near zero

This is not identical to digitization. A process can become digital while remaining slow.

---

### 4.2 Human Substitution

**Question:** To what degree can the human act itself be replaced while preserving the functional outcome?

Possible observables:

- automation penetration;
- AI-generated communication;
- recommendation systems;
- autonomous scheduling;
- synthetic media usage;
- machine-mediated decision share.

Possible exposures:

- Handwritten Letter: strongly negative
- Personal Recommendation: strongly negative
- Handmade Object: negative
- Solitude: potentially positive or neutral
- Live Performance: lower sensitivity

This differs from Time Compression because substitution can increase without making the process faster.

---

### 4.3 Mediation

**Question:** How much direct human-to-human or human-to-world contact is replaced by an intermediary layer?

Possible observables:

- platform-mediated transactions;
- algorithmic discovery share;
- digital intermediary penetration;
- remote interaction share;
- mediated communication share.

Potential distinction:

A human may still perform the act, but through a platform that changes the nature of the encounter.

Examples:

- discovering music through an algorithm versus through a friend;
- visiting someone after a calendar invitation versus arriving unannounced;
- seeing a landscape through a feed before encountering it physically.

Mediation may therefore deserve to remain separate from automation.

---

### 4.4 Uncertainty Compression

**Question:** How aggressively does the surrounding system remove chance, ambiguity, failure, and unpredictability?

Possible observables:

- route optimization;
- predictive recommendations;
- algorithmic ranking;
- scheduling precision;
- ETA accuracy;
- reservation penetration;
- risk scoring;
- pre-selection systems.

Possible exposures:

- Aimless Walking: strongly negative
- Serendipitous Discovery: strongly negative
- Unplanned Visit: strongly negative
- Handwritten Letter: weaker negative
- Live Performance: potentially mixed

This factor is conceptually important because LONGING is not only about slowness.  
Many romantic experiences depend on the possibility that something unplanned may happen.

---

### 4.5 Physicality Displacement

**Question:** How much of an experience's physical carrier is being replaced by a digital or dematerialized equivalent?

Possible observables:

- physical media share;
- paper correspondence share;
- cash usage;
- printed photo share;
- physical ticketing;
- in-person versus remote participation.

Possible exposures:

- Film Photography: strongly negative
- Physical Media: strongly negative
- Handwritten Letter: negative
- Aimless Walking: nearly zero
- Solitude: nearly zero

This could justify remaining separate because many non-physical practices are still exposed to Time Compression or Mediation.

---

### 4.6 Coordination Compression

**Question:** How much spontaneous or loosely coordinated social behavior is being replaced by explicit scheduling, optimization, and availability management?

Possible observables:

- calendar usage;
- reservation rates;
- scheduled versus unscheduled contact;
- invitation lead time;
- automated scheduling penetration;
- location-sharing / ETA coordination.

Possible exposures:

- Unplanned Visit: strongly negative
- Unplanned Phone Call: strongly negative
- Aimless Walking: weak
- Film Photography: minimal
- Live Performance: minimal

This may be an especially useful factor because it explains a class of practices that neither digitization nor time compression fully captures.

---

### 4.7 Friction / Inconvenience Premium

**Question:** Does the market currently punish or reward practices that require effort, patience, skill, inconvenience, or commitment?

This may behave differently from structural factors.

It could be cyclical or mean-reverting rather than permanently trending.

Examples:

- periods of renewed interest in analog practice;
- nostalgia cycles;
- slow-living movements;
- fatigue with automation;
- premiumization of handmade goods.

Potentially positive exposures:

- Handmade Object
- Vinyl
- Film Photography
- Live Performance
- Long-form correspondence

This factor could help produce long rallies inside a secular decline without hard-coding reversals.

---

### 4.8 Scarcity Revaluation

**Question:** When a practice becomes rarer, does rarity itself increase the value assigned to each remaining instance?

This is dangerous because scarcity may already affect fundamentals.  
It should remain separate only if we can distinguish:

- **declining prevalence** from
- **the market's changing willingness to pay for rarity**.

That distinction could create one of LONGING's most interesting paradoxes:

> A practice can become rarer and therefore more valuable per unit, while its total presence in society continues to collapse.

This factor requires careful treatment to avoid double counting.

---

### 4.9 Social Legibility / Status

**Question:** Does the practice gain or lose value because it becomes socially legible as tasteful, meaningful, authentic, inefficient, old-fashioned, or elite?

Examples:

- vinyl as cultural status;
- film photography as aesthetic identity;
- handwritten letters as ceremonial objects;
- handmade goods as premium signals.

This introduces a factor that is explicitly psychological and social rather than technological.

That is desirable.

A financial market is not only a machine for translating objective fundamentals.  
It also prices stories, status, expectations, fear, fashion, and collective belief.

LONGING should not remove that ambiguity.  
It should quantify it.

---

## 5. Structural factors and belief factors must remain distinct

Not everything that moves price should be called a macro factor.

A useful separation is:

```text
WORLD / STRUCTURAL FACTORS
    What is changing in the environment?

PRACTICE FUNDAMENTALS
    What is happening to this specific practice?

BELIEF / NARRATIVE
    What does the market think those changes mean?

POSITIONING
    How much of that belief has already been acted upon?

EVENT SURPRISE
    What changed relative to expectation?
```

This distinction matters because the same objective development can produce opposite interpretations.

Example:

> An AI service launches that generates handwritten-style letters.

Possible structural interpretation:

- Human Substitution rises.

Possible analyst interpretations:

- Bear: proof that the human act is becoming unnecessary.
- Bull: proof that demand for the form of handwritten correspondence remains culturally strong.

The Event Desk should classify the event and its relevance.  
The market and analysts should determine interpretation.

---

## 6. Subjectivity should be modeled, not removed

LONGING should not try to escape subjectivity.

That would weaken the work.

Real financial markets use highly mathematical language while depending on inputs such as:

- expected growth;
- terminal value;
- risk premium;
- management quality;
- future demand;
- competitive durability;
- narrative credibility.

These are not purely objective facts.

LONGING can intensify that contradiction.

Example:

```text
LTR — HANDWRITTEN LETTER

Cultural Attachment          76.4
Replacement Resistance       18.6
Expected 5Y Persistence      42.8
Scarcity Premium             24.1

Duration                     11.7y

β Time Compression           -0.84
β Human Substitution         -1.31
β Uncertainty Compression    -0.42

Research Fair Value          34.82
```

The number may be calculated to two decimal places.

The viewer can still ask:

> Who decided Cultural Attachment was 76.4?

That question is not a flaw.  
It is part of the work.

The institution's job is therefore not to eliminate subjective judgment, but to make its transformation into numbers systematic, documented, and auditable.

---

## 7. Complexity requirement

The final pricing model does **not** need to be simple.

It may eventually include:

- multiple structural factors;
- factor interactions;
- nonlinear sensitivities;
- duration;
- regime dependence;
- analyst forecast distributions;
- narrative re-rating;
- crowding;
- liquidity;
- periodic observable prints;
- surprise;
- model credibility;
- revisions;
- eventually reflexivity or leverage if justified.

But complexity should enter only when each component has a distinct function.

A good rule is:

> **Every parameter must buy the model a behavior it could not explain without that parameter.**

If two parameters always explain the same movement, one should probably disappear or become an observable feeding the other.

---

## 8. Auditability is more important than simplicity

The strongest design principle for Pricing Model v2 is:

> **LONGING's price engine does not need to be simple. It needs to be auditable.**

A weekly return should be decomposable.

Example:

```text
LTR — WEEKLY RETURN                         +13.84%

Fundamental Revision                         +2.14%
Time Compression                             -1.82%
Human Substitution                           -3.11%
Uncertainty Compression                      +0.46%
Narrative Re-rating                          +4.31%
Short Covering                               +9.72%
Interaction / Residual                       +2.14%
                                             -------
TOTAL                                        +13.84%
```

Ideally, even the residual should eventually be explainable or deliberately bounded.

The model should never produce a number merely because the work "needs" the chart to move.

---

## 9. Tests the final factor set should pass

Before accepting a factor set, we should test it against a small universe of very different securities.

Suggested reference set:

- Handwritten Letter
- Waiting for a Reply
- Unplanned Phone Call
- Unplanned Visit
- Aimless Walking
- Film Photography
- Physical Media
- Serendipitous Discovery
- Handmade Object
- Live Performance
- Solitude

For each proposed factor, ask:

1. What exactly does the factor measure?
2. What real-world change causes it to move?
3. Which observables estimate it?
4. Which securities have large positive exposure?
5. Which have large negative exposure?
6. Which should have near-zero exposure?
7. Can it move independently from the other factors?
8. What historical or hypothetical event isolates it?
9. Is it structural, cyclical, or mixed?
10. Does it double count something already present in fundamentals?
11. Does it help explain a price pattern we otherwise cannot produce?
12. Can its contribution be shown in a weekly attribution ledger?

If a factor cannot answer these questions, it should probably remain an indicator rather than a pricing factor.

---

## 10. Current preferred direction

My current preference is **not** to decide that LONGING has one, two, three, or seven factors.

Instead:

1. Build a large candidate pool.
2. Separate visible indicators from latent pricing factors.
3. Require a distinct causal story for every factor.
4. Test factors across heterogeneous securities.
5. merge factors that remain empirically or conceptually inseparable.
6. preserve multiple factors when they create genuinely different exposures, event responses, or time behavior.
7. allow the system to become complex again after the decomposition is defensible.

The first candidate pool should include at minimum:

- Time Compression
- Human Substitution
- Mediation
- Uncertainty Compression
- Physicality Displacement
- Coordination Compression
- Friction / Inconvenience Premium
- Scarcity Revaluation
- Social Legibility / Status

I do **not** assume all nine should survive.

Several may collapse together.  
Others may need to be split further.  
More important factors may be missing entirely.

That is precisely the question that should now be put to other models.

---

## 11. Separate open question: LONGING's currency

The idea of giving LONGING its own currency is promising, but it should be treated as a separate **Monetary System** design problem rather than folded prematurely into the factor model.

Questions such as issuance, numéraire, inflation, exchange rates, and whether changes in the currency can be separated from changes in the securities are substantial enough to deserve a dedicated review.

For the current factor discussion, the currency question should remain explicitly out of scope so that the critique stays focused.

---

## 12. Working thesis

The desired end state is not a minimalist simulation.

It is a research market that feels uncomfortably serious.

The calculations should be rigorous enough that a viewer could, in principle, audit why `LTR` moved by `+13.84%`.

Yet the object being priced remains something like:

- waiting for a reply;
- receiving a handwritten letter;
- walking without a destination;
- arriving without an appointment;
- discovering something by accident.

That contradiction is not an implementation detail.

It is the work.
