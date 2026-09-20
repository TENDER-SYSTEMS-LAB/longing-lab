## Section 1 — The identification frontier

### Assumptions made explicit

The specification is silent on several econometric details. The following assumptions are therefore stated rather than inferred:

1. **Weekly attribution is treated as approximately linear** over short horizons:
   \[
   r_{m,p,t}=\alpha_{m,p}+\sum_k \beta_{m,p,k}F_{k,t}+\varepsilon_{m,p,t},
   \]
   where \(m\in\{J,K,U\}\), \(p\in\{1,\dots,11\}\), and \(t=1,\dots,1565\).

2. A factor is **separately identified** only if its loading pattern across the 33 securities and its time series can be recovered up to scale and sign from the listed universe plus any declared observed proxies, without relying on reviewer preference.

3. The standing non-priced attribution lines — numeraire revision, substitution exposure, positioning, reflexivity — are either observed through proxies or are not separately identifiable. Where their loading vectors are needed, they are treated as observable covariates. If no proxy exists, those lines are themselves confounded.

4. Idiosyncratic shocks are not perfectly correlated across securities. If they are, the effective number of independent securities is lower.

5. No specific volatilities, correlations, or factor variances are assumed beyond the stated qualitative early/late correlation regime.

---

### Statistical ceiling versus design-identified factors

With 33 securities and 1,565 weekly observations, the raw time-series dimension is not the scarce resource. A sample covariance matrix can have rank up to 33. In a purely statistical factor model,

\[
R_t = B F_t + \varepsilon_t,
\]

with \(R_t\) a \(33 \times 1\) vector, one can write up to 33 orthogonal return components. But this is not identification in the economic sense. Without restrictions, factor models suffer from rotational indeterminacy: for any nonsingular matrix \(H\), \(BHF_t'\) and \(H^{-1}F_t\) produce the same fit. Naming factors requires exclusion restrictions, observed proxies, timing restrictions, or cross-sectional structure.

The relevant bound is therefore not the raw 33-dimensional covariance rank, but the number of economically distinct loading patterns that the listing structure can support.

---

### Listing-only maximum: 13 contemporaneous group factors

The listing has a natural two-way structure: 3 markets × 11 practices. If returns are decomposed additively into a universal component, market components, and practice components,

\[
r_{m,p,t}=a_t+u_{m,t}+v_{p,t}+\varepsilon_{m,p,t},
\]

with normalizations such as \(\sum_m u_{m,t}=0\) and \(\sum_p v_{p,t}=0\), then the number of independent group-level components is:

\[
1 \;+\; (3-1) \;+\; (11-1) \;=\; 13.
\]

These are:

- one all-universe component;
- two independent country-relative components;
- ten independent practice-relative components.

Under the conditions below, **13 is the maximum number of contemporaneous group factors that the listing structure alone can separately identify**.

Conditions for this maximum:

- one security per market-practice cell;
- additive separability of market and practice effects;
- no persistent market-by-practice interaction, or such interactions are not treated as factors unless shared across multiple securities;
- idiosyncratic errors not perfectly correlated;
- factor loadings are either known, stable, or change according to pre-specified event windows;
- normalization restrictions are imposed to remove the indeterminacy between universal, country, and practice effects.

If market-by-practice interactions are allowed to be arbitrary, there are 33 cell-specific shocks, but with only one security per cell those interactions are not separately distinguishable from idiosyncratic noise unless they are shared across multiple securities through a declared loading structure.

---

### Factors identified by cross-sectional variation within one market

Within a single market there are 11 securities. A factor identified purely from cross-sectional variation inside that market is a loading vector in an 11-dimensional practice space.

Maximum:

- At most 11 mutually independent loading patterns can exist in one market.
- If one dimension is absorbed by the market-wide component, at most **10 relative practice-loading patterns** remain.

But this is a loading-space bound, not a guarantee that all 10 correspond to meaningful economic factors. Each additional within-market factor requires a distinct pattern of loadings across the 11 practices and sufficient dispersion in those loadings.

A factor that loads only on one security inside one market is not identified as a factor under a multi-constituent definition. It is an idiosyncratic or security-specific effect.

---

### Factors identified by cross-market variation in the same practice

For each practice there are three securities: Japan, Korea, United States.

A three-security triplet can support:

- one common practice component loading on all three markets;
- two market-contrast components.

However, if the market-contrast components are allowed to be different for every practice, they become practice-specific local effects, often supported by only one or two effective constituents. Under the earlier round’s objection that a factor supported by too few constituents is not a macro factor, those are not separately defensible as factors unless they are shared across practices.

If the country contrasts are constrained to be common across all 11 practices, then the cross-market structure supplies:

- **two independent country-relative factors** overall;
- plus the practice-common components.

Thus the three-market structure is powerful for separating country-wide from practice-wide effects, but only because each country effect is supported by 11 securities and each practice effect is supported by three securities.

---

### Factors identified only by time-series variation

The 1,565 weekly observations are ample for estimating a given time series precisely if the loading pattern is known. But time-series length alone does not separate factors that move together slowly.

A factor that loads similarly across all securities and evolves slowly — for example, a broad cultural drift, a general preference shift, or a slow technology capability trend — is confounded with any other slow factor that has a similar loading pattern. Identification then requires:

- non-overlapping event timing;
- external proxies;
- exclusion restrictions;
- or observable exposure measures.

This is a standard limitation of latent factor models: temporal precision does not solve rotational or economic-label indeterminacy.

---

### Binding constraint

The binding constraint for the central claim of this design — that three markets separate local and common factors — is **cross-market variation**, not time-series length.

Reason:

- There are only three markets.
- Therefore only two independent country contrasts exist.
- Those contrasts are what separate country-specific effects from common practice effects.
- As markets converge, the country-contrast variance shrinks.
- When that variance becomes too small relative to noise, local factors are no longer separately attributable week by week.

The within-market cross-section of 11 practices is a secondary bound on the number of practice-loading patterns. The time series is long enough that it is not the primary binding constraint, although slow-moving factors remain confounded with one another.

---

## Section 2 — What the three-market structure buys, exactly

### The claim

The design claims that three markets make local and common factors structurally separable.

This claim is true only under specific conditions. It is not automatically true for all periods.

---

### Conditions under which the claim is true

The three-market structure separates local and common factors if all of the following hold:

1. **Common factors load across markets for the same practice.**  
   For example, a global decline in handwritten letters must affect the Japanese, Korean, and US letter securities in a related way.

2. **Country factors load across practices within a market.**  
   A Japan-specific shock must affect many or all Japanese practice securities, not just one security.

3. **Loading vectors are linearly independent.**  
   The country loading pattern must not be a scalar multiple of the global loading pattern.

4. **Idiosyncratic shocks are not perfectly correlated.**  
   If Japan letters, Korea letters, and US letters move together for unrelated security-specific reasons, the common practice component is contaminated.

5. **There is nonzero variance in both common and local components.**  
   If the common component has zero variance, it cannot be identified. If the local component has zero variance, it cannot be identified.

6. **Factor loadings are stable or change according to known regimes.**  
   If loadings drift unpredictably, early identification does not transfer to later periods.

7. **Technology-wave arrival dates are not perfectly synchronized across markets for the factors being identified.**  
   Staggered arrival dates create event-timing restrictions. Simultaneous arrival removes them.

Under those conditions, the three-market panel can distinguish:

- a shock common to a practice across all markets;
- a shock common to all practices in one market;
- a shock specific to one market-practice cell, which is treated as idiosyncratic unless shared.

---

### Simple correlation interpretation

For a given practice \(p\), suppose the three market returns have a common component and local components. In a simplified equal-loading case,

\[
r_{m,p,t}=g_{p,t}+c_{m,p,t}+\varepsilon_{m,p,t}.
\]

If local and idiosyncratic components are uncorrelated across markets, the same-practice cross-market correlation is roughly:

\[
\rho_p \approx
\frac{\operatorname{Var}(g_p)}
{\operatorname{Var}(g_p)+\operatorname{Var}(c_p)+\operatorname{Var}(\varepsilon_p)}.
\]

The exact expression depends on loadings and variances, but the qualitative meaning is robust:

- When \(\rho_p\) is low, local variance dominates.
- When \(\rho_p\) is high, common variance dominates.
- When \(\rho_p = 0\), the common component is absent or unidentifiable.
- When \(\rho_p = 1\), local components are absent or unidentifiable.

The stated history moves from roughly \(+0.2\) early to roughly \(+0.9\) late.

That means:

- Early, country-local variation is abundant; common practice factors are weaker but not necessarily absent.
- Late, common practice variation is abundant; country-local variation is weak.

---

### Conditions under which the claim fails

The three-market separability claim fails in several distinct ways.

#### 1. Correlation approaches one

If same-practice cross-market correlation approaches 1, country contrasts have vanishing variance. The loading vectors may still be formally independent, but the weekly signal in the country contrasts becomes too small to attribute reliably.

In the limit \(\rho_p=1\), local factors are not identified.

At \(\rho_p \approx 0.9\), local factors are not mathematically annihilated if local variance remains positive, but they may be practically unidentifiable for weekly attribution if the local signal is small relative to idiosyncratic noise.

#### 2. Correlation approaches zero

If same-practice cross-market correlation approaches 0, the common practice component has little variance. A global practice factor is then weakly identified.

Early in the history, this is the risk for common practice factors.

#### 3. Loadings converge

If country factors and global factors come to have the same loading pattern, they become collinear. This can happen even if local variance is not literally zero.

Example: if late-stage technology waves affect all markets identically and all practices similarly, a “US technology arrival” factor and a “global technology arrival” factor may no longer be distinguishable.

#### 4. Arrival dates coincide

Early staggered technology arrivals create difference-in-differences identification. A wave arriving in Japan but not yet in Korea or the US can be identified through the Japanese exposed securities relative to non-arriving markets.

If arrival dates converge, that timing restriction disappears. Late simultaneous AI-mediated substitution, for example, may be inseparable from the numeraire revision or from a global substitution exposure.

#### 5. Market-practice interactions are not shared

A shock that affects only Japanese handwritten letters is supported by one security. It is not identifiable as a factor unless it is linked to a broader loading structure, such as a Japan-letters-plus-Korea-letters pattern or a Japan-material-culture pattern.

---

### Does convergence destroy early identification?

Plainly: **convergence can destroy the identification of local factors that early divergence provides.**

It destroys local-factor identification when the country-contrast variance becomes zero or falls below the minimum detectable signal for the attribution window.

It does not necessarily destroy common-factor identification. In fact, convergence usually strengthens common-factor identification.

The prompt does not provide enough information to give a calendar date. The change occurs when an operational condition is met, not when a particular year arrives.

An operational definition:

- Compute rolling same-practice cross-market correlations or eigenvalues of the country-demeaned covariance matrix.
- Test whether the country-contrast eigenvalues are statistically distinguishable from idiosyncratic noise.
- The local-factor line becomes undefensible when those eigenvalues fail the test for a pre-specified consecutive window.

Without volatilities, noise levels, and estimation windows, the date cannot be determined from the given specification.

---

## Section 3 — The nine lines

### Counting convention

The ledger description separates:

- numeraire revision;
- substitution exposure;
- priced factor lines;
- positioning;
- reflexivity;
- unexplained.

This section treats “the nine lines” as **nine priced factor lines**, because the four standing lines are separately named. If the intended count includes the four standing lines, then the number of priced factor lines is five, and the same rank logic applies with a smaller priced-factor subspace.

---

### Derivation of nine priced factor slots

The listing-only additive basis has rank:

\[
1 + (3-1) + (11-1) = 13.
\]

The four standing non-priced attribution lines — numeraire revision, substitution exposure, positioning, reflexivity — each require a loading vector across the 33 securities. If those four loading vectors are linearly independent and lie within the 13-dimensional listing basis, they occupy four independent directions.

The residual priced-factor subspace then has dimension:

\[
13 - 4 = 9.
\]

Thus, **nine priced factor slots is the largest opening set that can be defended from the listing structure alone**, under the following conditions:

1. The additive market-practice basis is the relevant identification space.
2. The four standing lines have four linearly independent loading vectors.
3. No priced factor line is collinear with a standing line.
4. Factor loadings are stable enough to be estimated, or their changes are governed by known event windows.
5. Each priced factor has a loading pattern that is not supported by only one security.

If the standing lines are not linearly independent, the number of priced slots rises. If they require more than four directions, or if some priced factors are collinear with them, the number falls.

In general:

\[
K_{\text{priced}} = 13 - \operatorname{rank}(X_{\text{standing}})
\]

within the listing basis, capped between 0 and 13.

---

### Important limitation

The specification does not determine which practices load positively or negatively on the practice-residual factors. That depends on the estimated residual covariance matrix and on the measured loading vectors for numeraire, substitution, positioning, and reflexivity.

Therefore the non-preference-derived answer is a set of **factor slots**, not a set of named economic factors. Economic labels require additional exposure restrictions.

Factor sign is also not identified by the data alone. A sign convention must be imposed for ledger presentation.

---

### The nine defensible slots

A canonical representation of the nine priced slots is:

- two country-relative factors;
- seven residual practice-common factors.

This representation is not an economic labeling. It is the rank decomposition left after the standing lines occupy four directions in the 13-dimensional listing basis.

| Line | What it is | Observable that distinguishes it | Securities loading and sign convention | What makes it unidentifiable |
|---|---|---|---|---|
| **C1: first country-relative factor** | A country-loading pattern orthogonal to the universal direction and to the standing lines. In a contrast representation, Japan versus the other two markets. | A residualized Japan-minus-rest return spread after removing numeraire, substitution, positioning, reflexivity, and the global direction. Co-movement of the 11 Japanese securities relative to the other 22. | Positive loadings on the 11 Japanese securities; negative loadings on Korean and US securities using weights that make the vector orthogonal to the global direction and standing lines. Sign convention: Japan positive. | Japan-rest spread has zero or negligible variance; Japan loadings become proportional to global loadings; late convergence reduces country-contrast signal below detection; collinearity with a standing line. |
| **C2: second country-relative factor** | The remaining independent country-loading pattern, for example Korea versus US after orthogonalizing against C1 and the global direction. | A residualized Korea-US spread after removing C1, standing lines, and the global direction. Co-movement of Korean securities relative to US securities. | Positive loadings on Korean securities; negative loadings on US securities; zero or orthogonal weight on Japan depending on contrast convention. Sign convention: Korea positive. | Korea-US spread has zero or negligible variance; Korea and US become indistinguishable after global and standing-line removal; collinearity with C1 or standing lines. |
| **P1: first residual practice-common factor** | The largest remaining orthogonal co-movement across practices after removing C1, C2, and the standing lines. | The first eigenvalue/eigenvector of the residual practice covariance matrix, after partialling out standing lines and country contrasts. | All three market listings of each practice \(p\) load with weight \(v_{p1}\), or proportionally if market-specific practice loadings are allowed. Specific practices and signs are determined by the estimated eigenvector. Sign convention: largest absolute loading positive. | Eigenvalue not statistically distinguishable from idiosyncratic noise; eigenvector unstable; same-practice cross-market correlation too low; loading vector lies in span of standing lines. |
| **P2: second residual practice-common factor** | The second largest remaining orthogonal practice co-movement. | Second residual eigenvalue, orthogonal to P1 and all prior lines. | Same structure as P1, with weights \(v_{p2}\). Specific practices and signs come from the second eigenvector. | Eigenvalue too close to P1 or noise; rotational indeterminacy between P1 and P2; collinearity with standing lines. |
| **P3: third residual practice-common factor** | The third remaining orthogonal practice co-movement. | Third residual eigenvalue, orthogonal to P1, P2, standing lines, and country contrasts. | Same structure, weights \(v_{p3}\). | Same failure modes: weak eigenvalue, unstable eigenvector, collinearity. |
| **P4: fourth residual practice-common factor** | The fourth remaining orthogonal practice co-movement. | Fourth residual eigenvalue, orthogonal to earlier residual components. | Same structure, weights \(v_{p4}\). | Same failure modes. |
| **P5: fifth residual practice-common factor** | The fifth remaining orthogonal practice co-movement. | Fifth residual eigenvalue, orthogonal to earlier residual components. | Same structure, weights \(v_{p5}\). | Same failure modes. |
| **P6: sixth residual practice-common factor** | The sixth remaining orthogonal practice co-movement. | Sixth residual eigenvalue, orthogonal to earlier residual components. | Same structure, weights \(v_{p6}\). | Same failure modes. |
| **P7: seventh residual practice-common factor** | The seventh remaining orthogonal practice co-movement. | Seventh residual eigenvalue, orthogonal to earlier residual components. | Same structure, weights \(v_{p7}\). | Same failure modes. |

The specific securities loading positively or negatively on P1 through P7 cannot be determined from the given specification. They would be determined by:

- the measured numeraire loading vector;
- the measured substitution exposure vector;
- the measured positioning vector;
- the measured reflexivity vector;
- the residual covariance matrix of practice-common returns.

Any named assignment beyond that is an additional restriction, not a consequence of identification.

---

### If the four standing lines are counted inside the nine

If “nine factor lines” means nine total non-unexplained attribution lines, then four of those are:

1. **Numeraire revision** — identified by the difference between the standard-return quote and the frozen-yardstick companion.
2. **Substitution exposure** — identified by measured exposure to redemption or capability substitution.
3. **Positioning** — identified by observable position or crowding measures, if available.
4. **Reflexivity** — identified by observable feedback from prices to fundamentals, if available.

That leaves five priced factor slots. The same residual-rank construction applies, taking the first five residual components instead of seven.

The specification does not determine whether the intended count is nine priced lines or nine total lines. The rank logic is the same; only the count of priced slots changes.

---

### Early and late defensibility

The nine slots exist as a rank allocation, but the number of slots that are reliably populated changes over the history.

#### Early regime: weak cross-market correlation

When same-practice cross-market correlation is low:

- country-relative factors C1 and C2 have stronger signal;
- practice-common factors P1 through P7 may have weak common signal because the three listings of each practice do not move together tightly.

A conservative early statement:

- The structurally defensible country-relative slots are the two independent country contrasts.
- The practice-common slots are not guaranteed to be populated unless their residual eigenvalues pass significance tests.
- If no global standing line absorbs the universal direction, three country components may be representable, but only two independent contrasts remain once a universal component is included.

#### Late regime: high cross-market correlation

When same-practice cross-market correlation is high:

- practice-common factors P1 through P7 become more defensible;
- country-relative factors C1 and C2 become weak because country contrasts have low variance.

A conservative late statement:

- The structurally defensible practice-common slots can rise toward seven, subject to residual eigenvalue tests.
- The country-relative slots may become unpopulatable for weekly attribution if country-contrast variance falls below the detection threshold.

#### When the change occurs

The change occurs when rolling rank or eigenvalue tests cross pre-specified thresholds:

- country-demeaned eigenvalues fall below the minimum detectable signal;
- practice-common eigenvalues rise above it;
- or vice versa.

No calendar date can be derived from the prompt. The date is data-dependent.

---

### If the defensible number is not nine

Nine is defensible only as a maximum number of priced factor slots under the rank assumptions above.

The defensible number is lower if:

- the standing lines are not linearly independent;
- some residual eigenvalues are statistically indistinguishable from noise;
- some candidate factors are collinear with standing lines;
- country-contrast variance or practice-common variance is too weak in a given regime;
- factor loadings are unstable and no regime structure is supplied.

The defensible number is not fixed by preference. It is determined by the rank of the loading matrix that the listed universe can support.

---

## Section 4 — The promotion schedule

A declared-but-unpriced factor is promoted to a priced line only when a mechanical test is passed. The test must be runnable on the current universe.

Let the existing priced factors be \(F_E\) with loading matrix \(B_E\). Let the candidate factor be \(c\), with candidate loading vector \(b_c\) or proxy series \(f_{c,t}\).

Promotion occurs if and only if all gates below pass.

---

### Gate 1: Expression gate

The candidate must be expressible by the listed universe.

Test:

\[
\operatorname{rank}([B_E, b_c]) = \operatorname{rank}(B_E) + 1.
\]

If \(b_c\) lies in the span of existing loading vectors, the candidate is not a new factor. It is a recomputation of existing lines.

A statistical version tests the null hypothesis that \(b_c\) is linearly dependent on \(B_E\). Promotion requires rejection under a pre-specified significance rule.

---

### Gate 2: Signal gate

The candidate factor must have nonzero signal.

Test:

- The candidate proxy or estimated factor has nonzero variance.
- The candidate’s cross-sectional loading dispersion is nonzero.
- The eigenvalue associated with the candidate direction in the residual covariance matrix is statistically larger than idiosyncratic noise.

This can be run as a bootstrap or permutation eigenvalue test because the cross-section is small and fixed.

---

### Gate 3: Incremental attribution gate

The candidate must explain returns beyond existing lines.

Restricted model:

\[
R_t = B_E F_{E,t} + \varepsilon_t.
\]

Unrestricted model:

\[
R_t = B_E F_{E,t} + b_c f_{c,t} + \varepsilon_t.
\]

Test the null:

\[
H_0: b_c = 0
\]

or, if the factor series is estimated jointly,

\[
H_0: \text{candidate contributes zero incremental fit}.
\]

A Wald, likelihood-ratio, or generalized least squares restriction test can be used with heteroskedasticity and autocorrelation robust errors.

Promotion requires rejection at a threshold fixed in advance.

---

### Gate 4: Non-double-count gate

The candidate must not be a recomputation of numeraire revision, substitution exposure, positioning, reflexivity, or existing priced factors.

Test:

- Residualize \(b_c\) against all standing lines and existing priced factors.
- Compute the multiple correlation between the candidate factor series and existing factor series.
- Compute variance inflation factors or condition numbers for the augmented loading matrix.

Promotion requires the residualized loading vector to retain rank and the candidate’s correlation with existing lines to remain below thresholds fixed in advance.

---

### Gate 5: Stability or regime gate

The candidate loading pattern must be stable enough to estimate, or its instability must be governed by a known regime rule.

Test:

- Estimate loadings over rolling windows.
- Test whether loading estimates remain inside pre-specified confidence bands.
- If the factor is event-driven, test whether its activity concentrates in declared event windows.

If loadings drift without structure, the factor is not separately attributable.

---

### Gate 6: Replication gate

The candidate must be replicable, at least approximately, by a portfolio or attribution combination of listed securities.

Test:

- Construct the listed portfolio implied by \(b_c\).
- Measure tracking error between the candidate factor series and the portfolio return.
- Require tracking error below a threshold fixed in advance.

If the factor cannot be expressed through listed securities, it is not a factor for this ledger.

---

### Rule form

A candidate is promoted when:

\[
\text{Promote}(c)=
\text{Gate 1}
\land
\text{Gate 2}
\land
\text{Gate 3}
\land
\text{Gate 4}
\land
\text{Gate 5}
\land
\text{Gate 6}.
\]

Demotion follows the same rule in reverse: if any gate fails for a pre-specified consecutive window, the factor returns to declared-but-unpriced status.

The numerical thresholds are not derivable from the prompt. They must be fixed ex ante to keep the rule mechanical.

---

## Section 5 — What this universe cannot identify

This section follows from the position that listing determines which factors can exist. A factor is identifiable only if some listed security varies in the dimension required to express it. If the relevant dimension is not listed, the factor either becomes part of another factor or falls into `Unexplained`.

The listing changes below are stated as counterfactual identification conditions, not as proposals.

---

| Unidentifiable factor | Confounded with | Listing change that would separate it |
|---|---|---|
| **Pure AI capability improvement**, distinct from the standard-return numeraire and from substitution. | Numeraire revision and substitution exposure, because all three derive from the same capability series. | Listing the constituents of the AI basket separately, or listing AI-complementary claims whose value rises when human practices fall, would create securities with opposite exposure to the same capability series. |
| **Aggregate desire for communication or social contact**, separate from the form of communication. | Practice factors and substitution exposure, because the listed securities are specific communication forms rather than communication as a whole. | Listing additional communication modes or a composite contact-practice index would allow total communication demand to be separated from substitution among forms. |
| **Generational cohort preference shifts**. | Time-series technology-wave effects and country factors, because cohorts are not separately listed. | Listing cohort-segmented claims for the same practices would separate age-cohort preference changes from period-level technology shocks. |
| **Demographic aging, household structure, or population density effects**. | Country factors and slow substitution trends, because demographics move slowly and are correlated with technology adoption by market. | Listing demographic-linked claims or securities whose payoffs vary with age structure independently of practice exposure would separate demographics from country and substitution effects. |
| **Platform-specific shocks**, such as a dominant app, device, or intermediary changing its rules. | Practice factors and country factors, because the listing is at practice level, not platform level. | Listing platform-level securities or practice variants segmented by platform would identify platform shocks directly. |
| **Regulatory or privacy-policy shocks**. | Country factors and technology-arrival timing, because policy changes usually occur at country level and can coincide with technology waves. | Listing policy-event claims or additional regulatory regimes would allow policy shocks to be separated from country and wave effects. |
| **Income or wealth distribution effects**. | Float factors and positioning, because float measures attention balances but does not distinguish who holds the attention. | Listing income-segmented or wealth-segmented claims on the same practices would separate distribution effects from aggregate float or positioning. |
| **Supply-side constraints**, such as film stock shortages, paper availability, or craft material costs. | Practice-specific idiosyncratic shocks, because input markets are not listed. | Listing input or commodity claims related to the physical practices would separate supply constraints from demand-side practice factors. |
| **Health, loneliness, or mental-health epidemiology**. | Practice demand factors and reflexivity, because wellbeing effects influence practice demand but are not separately listed. | Listing health- or wellbeing-linked claims would separate epidemiological shifts from practice-preference and reflexivity effects. |
| **Urban form, night safety, transport, or weather effects**. | The aimless night walk security, country factors, and seasonal patterns, because the relevant environment is not separately listed. | Listing urban-mobility, safety, weather, or regional claims would separate environmental exposure from the practice itself. |
| **Reflexivity separate from positioning**, if reflexivity means price changes altering fundamentals. | Positioning, momentum, and lagged practice shocks, unless there is an observable feedback channel. | Listing claims on float issuance and redemption, or instruments that separate speculative positioning from fundamental float, would allow reflexivity to be identified as feedback rather than as positioning. |

The common feature is that the existing universe lists practices by country, but it does not list the underlying economic, demographic, technological, or institutional claimants that might drive those practices.

Therefore many plausible forces can move returns, but they cannot be separately priced unless their exposure is expressed through listed securities.

---

## Section 6 — Double counting

The numeraire, substitution channel, and float all derive from the same underlying capability series. This creates several double-counting hazards.

---

### 1. Numeraire revision versus an AI-progress factor

A factor labeled “AI progress” or “tool improvement” would count the same movement twice if the numeraire revision line already captures the appreciation of the AI-mediated basket.

Prevention:

- The numeraire revision line is assigned the denominator effect.
- Any AI-progress factor must be defined only as residual variation orthogonal to the numeraire revision line.
- If no orthogonal residual exists, the factor is not a separate line.

---

### 2. Substitution exposure versus substitution-themed factors

A factor labeled “substitution risk,” “digital substitution,” or “practice erosion” double counts if its loading vector is proportional to the substitution exposure line.

Prevention:

- Substitution exposure is assigned the measured exposure to redemption or capability substitution.
- A separate substitution-themed factor must have a loading vector orthogonal to the substitution exposure vector.
- If it merely scales substitution exposure, it is not promoted.

---

### 3. Float factor versus substitution-driven redemption

Float falls when holders redeem because they can manage alone. That redemption is part of the substitution channel.

A float factor that loads on declining float would double count substitution if it does not distinguish expected redemption from unexpected float variation.

Prevention:

- Define the float factor using unexpected float changes, residualized against substitution exposure.
- Alternatively, define it as a level or turnover effect after subtracting the substitution-implied redemption path.

---

### 4. Positioning versus float

Positioning and float both relate to outstanding balances. If positioning is measured by changes in float or by crowded exposure to float, it can double count float.

Prevention:

- Float is the fundamental attention balance.
- Positioning is the deviation of market positioning from the float-weighted or fundamental benchmark.
- The positioning loading vector must be orthogonal to the float loading vector.

---

### 5. Reflexivity versus positioning or momentum

Reflexivity means price movements affect fundamentals. Positioning means existing positions affect prices. Both can create return autocorrelation.

If reflexivity is measured only by lagged returns, it can double count positioning or momentum.

Prevention:

- Reflexivity must be identified through a feedback channel from price to float, issuance, redemption, or participation.
- Positioning must be identified through holdings or exposure deviations.
- The two lines must be orthogonalized, and reflexivity must survive residualization against positioning.

---

### 6. Country arrival factors versus global wave factors

Early in the history, a technology wave arriving in one market but not another can be identified as a country-timing factor. Late, when arrival is simultaneous, the same movement can be counted once as a country factor and once as a global wave factor.

Prevention:

- Country arrival factors are active only during declared market-specific arrival windows.
- Once the wave is simultaneous across markets, the country-timing version must be collapsed into the global wave factor or dropped.
- The loading matrix must not allow the same wave exposure to appear in both country and global lines.

---

### 7. Practice factors versus substitution or float vectors

A practice-common factor may load heavily on practices with high substitution exposure or large float balances. If its loading vector is spanned by substitution and float, it is not separate.

Prevention:

- Residualize practice-factor loading vectors against substitution and float vectors.
- Require the residual loading vector to pass the rank and signal gates.

---

### General prevention rule

No factor line is admissible if its loading vector lies in the span of previously assigned lines.

The ledger’s design matrix must maintain full column rank:

\[
\operatorname{rank}([X_{\text{standing}}, B_{\text{priced}}])
=
\operatorname{rank}(X_{\text{standing}})
+
\operatorname{rank}(B_{\text{priced}}).
\]

If rank fails, the candidate line is a double count.

---

## Section 7 — What would settle it

A discriminable test can be built from data this world can generate.

The procedure below can be run on historical world data if the generative process is observable, or on simulated data if the world’s laws can be replicated.

---

### Step 1: Declare candidate factor sets

Each candidate set must specify:

- factor names or slots;
- loading restrictions;
- zero restrictions;
- sign conventions;
- timing restrictions;
- which standing lines are included;
- which factors are country-relative, practice-common, or characteristic-based.

Candidate sets are not ranked qualitatively. They are tested.

---

### Step 2: Estimate a constrained state-space model

For each candidate set, write:

\[
R_t = B F_t + \varepsilon_t,
\]

with factor dynamics specified as needed. Estimate by maximum likelihood using a Kalman filter or equivalent state-space method.

Normalize factors to fix scale and sign. Use the same normalization across candidates.

---

### Step 3: Run rank tests

Estimate the number of common components in:

1. the full 33-security panel;
2. the country-demeaned panel;
3. the practice-demeaned panel;
4. the residual panel after standing lines.

Because the cross-section is small and fixed, standard large-\(N\) factor criteria are not sufficient by themselves. Use bootstrap or permutation eigenvalue tests calibrated to the 33-security panel.

This tests whether the claimed number of factor slots is compatible with the covariance structure.

---

### Step 4: Run overidentification tests

Where a candidate set imposes restrictions, test them.

Examples:

- A Japan country factor should not load on Korean or US securities.
- A global practice factor should load on the same practice across markets with proportional loadings.
- A technology-arrival factor should be active only in declared arrival windows.
- A substitution factor should not explain residual variation orthogonal to substitution exposure.

Wald or Hansen-style overidentification tests can be used where enough restrictions exist.

---

### Step 5: Use staggered arrival events as difference-in-differences tests

The early history contains staggered technology arrivals across markets.

For each declared arrival:

- identify exposed practices;
- identify non-exposed practices;
- identify arriving market and non-arriving markets;
- estimate the differential response of exposed securities in the arriving market.

A candidate set is consistent if the attributed arrival factor captures this differential response and the residuals show no systematic arrival effect.

Placebo tests can be run on non-arriving markets and non-exposed practices.

---

### Step 6: Test convergence breakdown

Estimate rolling country-contrast eigenvalues and practice-common eigenvalues.

The test should identify:

- when country factors lose signal;
- when practice-common factors gain signal;
- whether the transition is smooth or regime-like.

This determines the empirical date at which early identification stops supporting local factors.

---

### Step 7: Compare out-of-sample attribution

For each candidate set:

- estimate factors over a training window;
- produce one-step-ahead attributed forecasts or density forecasts;
- evaluate log predictive likelihood, root mean squared attribution error, and unexplained variance.

A candidate set is retained if it passes overidentification and produces no systematic out-of-sample failure. Non-nested comparisons can use Vuong-style tests or penalized likelihood criteria, but the procedure must be pre-specified.

---

### Step 8: Simulation recovery

If the world can be simulated:

1. Generate data from a known factor structure.
2. Estimate each candidate set.
3. Test whether the true factors are recovered up to scale and sign.
4. Test whether false factors are rejected.
5. Measure power and false-positive rates.

This settles which candidate sets are recoverable under the design.

---

## Section 8 — Refusals

The following were declined:

1. **No ranking of the six earlier sets is provided.**  
   The round forbids ranking, defense, or attack of earlier sets.

2. **No preferred factor set is offered.**  
   The output gives identification conditions, rank bounds, and factor slots, not a favored economic labeling.

3. **No specific volatilities, correlations, or thresholds were invented.**  
   Where quantities are missing from the specification, the answer states what would determine them.

4. **No calendar date was assigned to the breakdown of local-factor identification.**  
   The breakdown is determined by a testable signal-to-noise condition, not by the given narrative alone.

5. **No new securities, markets, or span changes were proposed as actions.**  
   Section 5 describes counterfactual listing changes only as identification conditions, because the required output asks what change to the listing would separate each unidentifiable factor.

6. **No named assignment of practices to P1 through P7 was made.**  
   That assignment is not determined by the given specification. It would be determined by the measured standing-line loading vectors and the residual covariance matrix.

One framing limitation is noted here, as permitted: the phrase “maximum number of factors” is not answerable as a single number unless the type of factor is defined. A purely statistical component count, a listing-only group-factor count, and a priced economic factor count are different objects. The answer above separates them. The binding result is that the listed three-market structure supports at most 13 contemporaneous group directions, and, after four independent standing lines, at most nine priced factor slots within that listing basis. Factors beyond those slots may be declared, but they are not separately identified until the listed universe expresses them.