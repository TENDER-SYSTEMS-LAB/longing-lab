## Section 1 — The identification frontier

Let the return panel be \(r_{i,m,t}\) for practice \(i=1,\dots,11\), market \(m=1,\dots,3\), week \(t=1,\dots,1565\). In a linear factor model \(r_t = Bf_t+\varepsilon_t\), with no restrictions on loadings \(B\), the common covariance has rank at most \(N=33\). So at most 33 common factors can be separated statistically, and labels are not identified without restrictions. With an intercept, the usual bound is \(N-1=32\).

Under the panel structure implied by the specification — practices and markets as distinct dimensions — the largest set of separately identifiable common factor lines is:

\[
1 \text{ global} + (11-1) \text{ practice contrasts} + (3-1) \text{ market contrasts} = 13.
\]

This holds if loadings are known or restricted: a global factor loads equally on all 33; a practice factor loads on the three market listings of one practice and zero elsewhere; a market factor loads on the eleven practices in one market and zero elsewhere. Practice-by-market interactions are unique to one security, so they are not common factors; they are idiosyncratic unless additional securities or known cross-loadings are introduced.

- **Cross-sectional variation within one market.** At most 11 factors, or 10 independent practice contrasts, can be identified from the eleven practices in a single market. Across three markets, this gives 33 security-specific dimensions, but only 11 are common across markets for the same practice.
- **Cross-market variation in the same practice.** With three markets, at most 2 independent market contrasts can be identified per practice, or 2 global market contrasts if the market effect is common across practices. A third market dimension is redundant with the global factor.
- **Time-series variation only.** \(T=1565\) permits many lags, trends, and slowly varying components. But any factor identified only by time-series variation is confounded with every other slow-moving line: numeraire revision, substitution exposure, positioning, reflexive component, and unexplained. Without exogenous timing or cross-sectional restrictions, these are not separately identified.

The binding constraint is **cross-market variation**. Three markets yield only two independent cross-market contrasts. This limits how many local factors can be separated from common factors. The cross-sectional within-market dimension is also limited, by 11 practices, but time-series length is not numerically binding; it is the source of confounding rather than the binding count.

## Section 2 — What the three-market structure buys, exactly

The claim that three markets make local and common factors structurally separable is true under these conditions:

1. Cross-market correlations are strictly less than 1.
2. Local factors have non-zero variance not shared by other markets.
3. Loadings are known or restricted so that a common factor loads equally across markets and a local factor loads on one market only.
4. The three market factors are not perfectly collinear with the global factor.
5. Estimation error is small relative to local variance.

With three markets, one can identify one common factor and two independent local contrasts. That is the structural gain: it allows a common component and two local deviations to be separated.

The claim fails as cross-market correlations approach 1. If markets have correlation \(\rho\), the variance of a cross-market difference is proportional to \(1-\rho\). At \(\rho=0.2\), local variation is large. At \(\rho=0.9\), local variation is roughly one tenth of common variation, and it can be swamped by noise. At \(\rho=1\), local factors are perfectly confounded with the common factor and cannot be separated.

Convergence therefore weakens and eventually destroys the identification that early divergence provides. The exact point of destruction is not determined by the specification. It depends on signal-to-noise and sample size. With \(T=1565\), a correlation of \(+0.9\) is statistically distinguishable from \(+1\), so local factors are not automatically unidentifiable. But they are weakly identified, and if the local variance is small relative to idiosyncratic noise, they will fail standard tests. The change occurs when the cross-market contrast is no longer statistically distinguishable from zero. From the given information alone, the exact week cannot be determined.

## Section 3 — The nine lines

The defensible number is not nine. Under the panel structure, the maximum separately identifiable common factor lines are **13 early** and **11 late** if convergence makes the two market contrasts unidentifiable.

The 13-line set is:

1. **Global common factor.** Loads positively on all 33 securities. Observable as common movement across every practice and market. Unidentifiable if numeraire revision absorbs all common movement.
2. **Ten practice contrasts.** For each practice except one, a factor loads positively on that practice’s three market listings and negatively on the cross-practice average. Observable as a spread between that practice and the other practices. Unidentifiable if all practices move together, or if substitution exposure absorbs the practice-specific variation.
3. **Two market contrasts.** For example, Japan versus United States and Korea versus United States. Each loads positively on all eleven practices in one market and negatively on the reference market. Observable as a spread between that market and the reference market. Unidentifiable when cross-market correlation approaches 1, as late in the history.

Early in the history, when cross-market correlation is near \(+0.2\), all 13 lines are defensible. Late, when correlation is near \(+0.9\), the two market contrasts are weakly identified or unidentifiable, leaving a maximum of 11 lines: one global plus ten practice contrasts.

Nine is a subset of this maximum, not a derived maximum. The design does not identify which nine practice contrasts to price. If the opening ledger has nine factor lines, the remaining identifiable lines must be declared but unpriced until they pass the promotion test. The number nine is not supported by the identification frontier as a maximum.

## Section 4 — The promotion schedule

A declared-but-unpriced factor is promoted to a priced line when it passes a test that can be run on the panel. The rule is:

1. **Rank test.** Apply a panel factor-number test — for example, Bai–Ng information criteria or the Onatski eigenvalue test — to the residual covariance after including all currently priced factors. The candidate factor is promoted only if the null of no additional common factor is rejected at a pre-specified size.
2. **Risk-premium test.** Estimate a Fama–MacBeth cross-sectional regression of weekly returns on exposures to existing priced factors plus the candidate. Test whether the candidate’s price of risk is zero. Use Newey–West standard errors and control the false discovery rate across candidates.
3. **Incremental explanatory power.** Require the candidate to reduce out-of-sample unexplained variance in a holdout period by a pre-specified amount.
4. **Collinearity check.** Require the candidate’s return series to have a variance inflation factor below a pre-specified threshold against all existing priced lines.

A factor that fails any of these remains declared but unpriced. The rule is mechanical: promotion occurs when the test rejects the null, not when a reviewer prefers the factor.

## Section 5 — What this universe cannot identify

The following factors plausibly operate in this world but cannot be separated from the listed universe, no matter how the model is specified. For each, the confound and the listing change that would separate it are given.

| Unidentifiable factor | Confounded with | Listing change that would separate it |
|---|---|---|
| Global technology-wave arrival | Numeraire revision | Add a security exposed to the technology wave but not to the AI-mediated numeraire |
| Substitution exposure | Practice-specific decline | List multiple sub-practices within each practice with different substitution elasticities |
| Market-specific technology arrival late in history | Global technology wave | Add markets whose technology arrival dates differ from the existing three |
| Positioning | Reflexive component | List a security with observable positioning data or a practice immune to reflexivity |
| Float redemption | Attention decay | List practices with different redemption rules or observable redemption events |
| Practice-by-market interaction | Idiosyncratic noise | List multiple securities per practice-market cell |
| Cross-practice common factors, e.g. analog nostalgia | Practice main effects | List more practices that share the latent factor, or provide known cross-loadings |
| Arrival phase vs substitution phase of the same wave | Each other, when timing overlaps | List practices with different lags between arrival and substitution |
| Global risk appetite | Numeraire | Add a non-practice security sensitive to risk appetite but not numeraire |
| Demographic change | Slow practice decline | List practices with different demographic exposure across markets |

This section is the direct consequence of the second position: listing determines which factors can exist. The current 33-security universe cannot identify any factor that requires within-practice variation, within-market-practice variation, or a fourth market. It also cannot identify a factor that is only a slow time-series trend, because every such trend is confounded with numeraire, substitution, positioning, reflexive, and unexplained.

## Section 6 — Double counting

The numeraire, substitution channel, and float all derive from the same underlying capability series. Double counting occurs wherever a proposed factor line would count the same movement twice.

- **Numeraire revision and global factor.** A global factor that loads on all securities will absorb numeraire revision. Prevent by quoting in the frozen-yardstick companion index or by orthogonalizing the global factor against the numeraire line.
- **Substitution exposure and practice factors.** A practice factor that declines because of substitution is partly the substitution line. Prevent by residualizing practice factors on substitution exposure before pricing.
- **Float changes and attention or redemption factors.** Float is a balance that grows by issuance and falls by redemption. A factor line called “attention” or “redemption” will double count float changes. Prevent by modeling float growth as an exposure, not as a factor return.
- **Positioning or reflexive component and sentiment factors.** Any proposed sentiment or reflexivity factor will overlap the existing positioning and reflexive lines. Prevent by orthogonalizing the candidate against both.
- **Unexplained and residual factors.** A factor that is only residual noise will double count the unexplained line. Prevent by requiring incremental explanatory power over the existing priced lines and unexplained residual.

## Section 7 — What would settle it

A Monte Carlo simulation can discriminate between candidate factor sets using data this world can generate. The procedure is:

1. Specify a true factor structure — for example, 13 common factors plus idiosyncratic noise — and a convergence path for cross-market correlation from \(+0.2\) to \(+0.9\).
2. Generate many panels of 33 securities over 1565 weeks under that structure.
3. Estimate each candidate factor set using maximum likelihood factor analysis with the known loading restrictions.
4. For each candidate set, compute the Bai–Ng information criterion, out-of-sample forecast error on the last 565 weeks, and a Diebold–Mariano test against competing sets.
5. Repeat across the correlation path and record when each candidate set fails to recover the true factors.

The candidate set that recovers the true number of factors and minimizes out-of-sample forecast error across the correlation path is the one supported by the data. This test can actually be run. It does not require preference or judgement beyond the pre-specified significance levels.

## Section 8 — Refusals

I declined to propose a preferred factor set, rank the earlier sets, or make a recommendation. I did not invent specific volatilities, correlations, or sample sizes that were not given. I did not answer whether the work’s premise is good, whether romance is declining, or whether the subject is well chosen.

The specification is silent on loadings, event data, and the exact convergence path, so several answers are conditional. The framing is not wrong, but the author’s second position — that listing determines which factors can exist — is a premise, not an identification result. The identification analysis can state what the listed universe can separate; it cannot state what the universe should list.