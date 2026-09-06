# Dataset research for LONGING backtesting

Research date: 2026-09-06. Attribution: LLM research synthesis; all priorities, mappings, and experiments below are proposals, not adopted design decisions. This is an original research note, not a verbatim export of the user conversation or a copy of the linked datasets.

## Scope and evidence boundary

The user requested diverse datasets, including but not limited to Kaggle, to test the mathematical model, discover omitted factors and necessary calculations, and detect overengineering. Exact fit is not required.

The current Wiki was read before research: index, current state, schema, pricing model, data sources, academic model survey, and index architecture. The architecture separates underlying practice, research value, market price, attention, discourse, and positioning. The final factor set and security unit remain unresolved. Consequently, no external dataset supplies ground-truth LONGING prices. We can test observable components and transferable mechanisms; a historical replay of authored prices is a simulation, not empirical price validation.

Evidence levels used here:

- **Documented:** publisher documentation or its official catalog describes the resource and access route. This does not mean a binary download was completed.
- **Discovery:** the resource exists in search/catalog results but its current files, schema, or access terms were not fully inspected.
- **Proposed:** a LONGING mapping or experiment inferred from those resources.

No dataset was downloaded or fitted in this task. A three-row Seattle API request failed because the shell environment could not resolve the host; web retrieval of its schema also failed. Some Kaggle pages returned an empty text body, and direct reads of PHEME, MovieLens, and IMLS encountered retrieval errors. Search-visible publisher records are identified below rather than treated as inspected rows. Account-gated access, current quotas, and exhibition reuse rights remain unverified unless explicitly stated. All 33 previously registered source hashes matched at the start.

## Recommended first collection

1. **Seattle library checkouts:** the most immediately useful monthly physical/digital substitution panel, with item-level heterogeneity.
2. **ATUS:** the strongest first source for whether available time, companions, work, and care obligations explain practices better than abstract modernization scores.
3. **RIAA format history:** a long-run decline/revival test, with revenue separated from units wherever compatible unit series can be obtained.
4. **USPS correspondence reports:** the closest initial LETTER anchor, subject to category and survey continuity checks.
5. **Wikimedia pageviews:** a separate attention channel to pair with suitable behavior series, never a substitute for them.

For a Korean-first analysis, prioritize Korea Media Panel plus Korean Time Use Survey and KOBIS. These are more culturally local but need additional file/codebook and access checks. US observations do not establish a Korean or global trend.

## A. Behavior and substitution datasets

### D01 — American Time Use Survey (ATUS), BLS

**Documented.** US repeated cross-sectional diaries; the official catalog lists annual files from 2003 and currently includes 2025. The 2024 file page was inspected: CSV inside ZIP, with Respondent, Activity, Activity Summary, Who, Roster, and CPS-related files. Activity data include timing and location; Who records companions. Access is public download. [Catalog](https://www.bls.gov/tus/data.htm), [2024 files](https://www.bls.gov/tus/data/datafiles-2024.htm).

**Proposed use:** annual weighted participation and minutes for socializing, reading, walking, and relevant leisure activities; test available time and social circumstances as candidate explanatory variables. Diary records are not a multi-year person panel. Being alone is not loneliness; leisure is not necessarily unstructured time; walking is not necessarily aimless. Freeze activity-code mappings, account for weights/design and coding changes, and do not manufacture weekly population estimates from sparse diaries.

### D02 — Korean Time Use Survey

**Partly documented.** Official 2024 release describes a five-year survey begun in 1999, covering residents aged 10+ in 12,750 sampled households. It says microdata would be provided through MDIS; this survey did not verify whether the 2024 downloadable microdata are now available. [Official 2024 release](https://sri.kostat.go.kr/boardDownload.es?bid=220&list_no=437764&seq=9), [MDIS access portal](https://mdis.kostat.go.kr/).

**Proposed use:** Korean time-budget and cohort comparisons. Obtain the accessible waves and codebooks before selecting comparable activities. Five-year waves support structural comparisons, not a monthly/weekly historical price backtest. Age, period, and cohort effects cannot all be freely identified from their arithmetic relationship.

### D03 — Korea Media Panel Survey, KISDI

**Documented portal; files uninspected.** The publisher provides questionnaire/raw-data and item-download sections and indicators including telephone use and device use; the series has a 2010 report. [Data portal](https://stat.kisdi.re.kr/main.html), [2010 publisher record](https://library.kisdi.re.kr/%24/10230/contents/3934581?articleId=520705&checkinId=737361).

**Proposed use:** test within-person shifts among media, whether old and new channels coexist, and differences across generations. Request comparable waves, stable person IDs, weights and questionnaires; verify exact format and login terms. A fall in recorded calls cannot establish a fall in unplanned calls, and media diary time is not total human connection.

### D04 — USPS Household Diary Study / Household Mail Survey

**Documented reports, not open respondent microdata.** The current survey is called Household Mail Survey, formerly Household Diary Study. An accessible FY2011 report separates correspondence and discusses household differences. [Current survey](https://about.usps.com/what/performance/household-mail-survey/), [FY2011 report](https://about.usps.com/studying-americans-mail-use/household-diary/2011/report-htmL/usps-hds-fy11.html).

**Proposed use:** construct an annual LETTER-adjacent correspondence series, preserving household/population denominators and category definitions. Personal correspondence is closer than all mail, but still not verified handwritten letters. Historical report extraction and continuity across survey changes are collection work, not completed here. Compare cohort composition and substitution explanations before imposing an exponential decline.

### D05 — Universal Postal Union Postal Statistics

**Documented.** Country postal statistics cover letter post and infrastructure; the 2023 publication presents country data over a five-year window. [Statistics entry](https://www.upu.int/en/universal-postal-union/activities/research-publications/postal-statistics), [2023 publication](https://www.upu.int/en/publications/statistics/postal-statistics-2023).

**Proposed use:** country-year letter-post rates and postal-access measures for infrastructure-versus-demand hypotheses. Public reports are available; bulk machine-readable access and the usable historical country intersection need confirmation. Do not call designated-operator letter post handwritten correspondence or assume all countries use identical reporting coverage. Missing reporting is not zero demand.

### D06 — RIAA US format revenue history

**Documented.** Current official database covers format evolution since 1973 and explicitly describes wholesale revenue. It defines vinyl, CD, downloads, and streaming categories, including category changes in 2025. [Official database](https://www.riaa.com/u-s-sales-database/).

**Proposed use:** compare physical formats, downloads and streaming; test substitution, coexistence and revival. Obtain compatible historical shipment-unit tables separately before decomposing revenue into units and average revenue per unit. Preserve retail/wholesale basis, inflation treatment and taxonomy versions. Aggregate revenue is neither listening incidence nor a transaction-price series. This is a valuable adverse case for a model that predicts every physical practice must disappear.

### D07 — Seattle Public Library Checkouts by Title

**Documented catalog; rows uninspected.** Monthly title-level counts of physical and electronic checkouts begin April 2005. The city catalog exposes CSV/JSON/XML routes and dataset ID `tmmm-ytt6`. [Official government catalog](https://catalog.data.gov/dataset/checkouts-by-title), [City dataset](https://cos-data.seattle.gov/d/tmmm-ytt6).

**Proposed use:** monthly format totals, physical share, title persistence, and matched-work substitution. Normalize title/edition identifiers; distinguish supply availability from demand; inspect renewal/counting conventions for this exact dataset. Checkouts are not completed reading. A separate physical transaction dataset, `5src-czff`, excludes renewals and traces 2005–2016 data to George Legrady's artwork; do not transfer that schema or counting rule automatically to the combined monthly table. [Separate physical dataset documentation](https://dev.socrata.com/foundry/data.seattle.gov/5src-czff/embed).

### D08 — IMLS Public Libraries Survey

**Publisher-catalog documented; direct page returned 403.** Annual library records and public-use files; the catalog lists CSV, SAS, SPSS and documentation, with historical files including 1992. [Publisher catalog](https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls), [1992 government record](https://catalog.data.gov/dataset/public-library-survey-pls-1992).

**Proposed use:** infrastructure, opening hours, collections, visits and circulation where present in a common-year codebook. Test whether access conditions explain apparent cultural decline. Maintain library IDs and service-area population; handle mergers, imputation and fiscal-year differences. Library-level counts cannot identify individual abandonment or establish that opening hours caused demand changes.

### D09 — KOBIS cinema records

**Documented service; authenticated response untested.** Official service lists daily and weekly box-office operations. [Official API service](https://kobis.or.kr/kobisopenapi/webservice), [Daily interface](https://m.kobis.or.kr/kobisopenapi/homepg/main/apiMainDailyResult.do).

**Proposed use:** attendance/revenue and release-related shocks as a Korean example of embodied cultural consumption. Obtain API credentials under provider terms and confirm fields/date coverage. A ranked box-office response must not be summed as the entire market without checking coverage; use total-market tables for that target. Screen availability, releases, ticket prices, holidays and pandemic closures can masquerade as structural preference change.

### D10 — Bank of Canada Methods-of-Payment Survey

**Documented aggregate reports.** Survey waves include 2009, 2013, 2017 and 2021–2024. Reports distinguish payment counts and value, and describe cash persistence. Public microdata were not verified. [Publisher survey](https://www.bankofcanada.ca/banknotes/bank-notes-research-reports/methods-of-payment-survey/), [2023 report](https://www.bankofcanada.ca/2024/07/staff-discussion-paper-2024-8/).

**Proposed use:** CASH/physical exchange as a substitution-with-residual-use test. Separate adoption, transaction share and spending share. Merchant acceptance and transaction size may matter as much as convenience. Cash use does not directly measure delight in physical exchange.

## B. Individual persistence, social structure, and valuation proxies

### D11 — Understanding Society / UK Household Longitudinal Study

**Documented.** UK household panel begun in 2009; UK Data Service announced Wave 15 in January 2026. End-user-licence access is a route, not a verified entitlement for this project. [Series description](https://ukdataservice.ac.uk/help/data-types/longitudinal-data-studies/), [Wave 15 release](https://ukdataservice.ac.uk/2026/01/27/understanding-society-wave-15-data-now-available-from-the-uk-data-service/).

**Proposed use:** distinguish within-person change from changing population composition using harmonized social-participation or leisure items where repeated. Inspect module timing, attrition, weights, and access conditions. Not every question is asked each year. A panel can improve identification but cannot remove unobserved confounding by itself.

### D12 — World Values Survey

**Documented download portal.** Cross-national wave datasets, questionnaires and country documentation; Wave 7 is labeled 2017–2022. [Official documentation](https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation).

**Proposed use:** cultural attachment, social values and institutional context as slow covariates, choosing only repeated documented items. Wave comparisons are not a person panel or continuous time series. Expressed values are neither willingness to pay nor observed practice. Translation and measurement equivalence matter before country pooling.

### D13 — SocioPatterns high-school temporal contacts

**Documented schema and download links.** France: four days in 2011 and seven days in 2012; contact records at 20-second resolution with anonymous pair IDs and class metadata. CC BY-NC-SA terms are stated. [Publisher dataset](https://sociopatterns.org/datasets/high-school-dynamic-contact-networks/).

**Proposed use:** compare a constant encounter-rate model with time-varying contact and network models. Test repeated versus new contacts and schedule-driven clustering. Contacts are not necessarily conversation, friendship or unplanned encounters. Short school observations cannot calibrate decades of social decline. Research reuse and exhibition use must respect the noncommercial/share-alike terms.

### D14 — MovieLens 32M

**Discovery with publisher documentation.** A versioned rating/tag dataset from a recommendation service; publisher README identifies five-star ratings and free-text tagging. Direct README retrieval failed, so exact file dates, counts and permissions need inspection. [Publisher listing](https://www.grouplens.org/datasets/movielens/), [README](https://files.grouplens.org/datasets/movielens/ml-32m-README.html).

**Proposed use:** rating dispersion, taste persistence and popularity concentration as limited preference proxies. Timestamped ratings are not view timestamps, ticket sales, willingness to pay or analyst forecasts. No randomized recommendation exposure was verified, so recommendation effects or serendipity cannot be recovered from ratings alone.

### D15 — UCI Online Retail II

**Documented fields, license and file.** UK gift retailer transactions, December 2009–December 2011; 1,067,371 records and a 43.5 MB XLSX. Invoice, item, quantity, time, unit price, customer and country are documented; cancellations and missing data are present. CC BY 4.0. [Original UCI dataset](https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii).

**Proposed use:** repeat purchase, inactive intervals, reactivation and heterogeneous demand. Gift merchandise is not gifting intent, and wholesalers complicate household interpretation. Absence after the last observation is right-censoring, not permanent abandonment. Preserve returns instead of indiscriminately deleting negative quantities. Useful for checking whether an adoption-only model omits repeat use and exits.

### D16 — Kaggle KKBox Churn Prediction Challenge

**Discovery.** Original competition exists; its current data page returned no readable body. The published survival-model paper identifies KKBox as the donor. Current binary access, data version, fields, historical interval and competition-use terms remain unverified. [Competition](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge), [Research using the competition](https://jmlr.csail.mit.edu/papers/volume20/18-424/18-424.pdf).

**Proposed use:** a later persistence/exit benchmark if transaction and activity histories can be obtained. Distinguish payment expiry, cancellation, inactivity, churn definition and return. Renewal records after a prediction cutoff must not become predictors. Stopping one service is not abandoning music. UCI is the easier documented fallback for a first repeat-use experiment.

## C. Attention, reporting and financial-mechanism benchmarks

### D17 — Wikimedia pageviews

**Documented API.** Official pageview endpoints cover data from July 1, 2015. [API reference](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/reference/page-views.html).

**Proposed use:** aggregate chosen pages to week/month; test attention decay and revival, then whether lagged attention improves behavior forecasts. Fix language/project, page mappings, agent/access filters and redirects; document extraction time. English-language traffic is not US-only traffic. Pageviews measure attention, not positive sentiment or actual practice.

### D18 — Google Trends

**Documented export.** Google supports CSV export; values are sampled, normalized relative search interest on a 0–100 scale, with low-volume and statistical-noise limitations. [Export guide](https://support.google.com/trends/answer/4365538?hl=en), [Data FAQ](https://support.google.com/trends/answer/4365533?hl=en).

**Proposed use:** geographically matched attention series alongside behavior. Freeze terms/topics, region, category, interval, request date and normalization strategy. Zero need not mean no searches. Scaling against a future peak can leak information into historical model preprocessing. Historical API access is not required for a small manual pilot and no API-alpha entitlement is claimed here.

### D19 — GDELT Events, Mentions and GKG

**Documented download/query routes.** GDELT 2.0 updates every 15 minutes and separates events, mentions and the knowledge graph. [Publisher data guide](https://gdeltproject.org/data.html).

**Proposed use:** test reporting bursts, repeated coverage and event-routing robustness. Deduplicate shared stories and normalize against changing source/language coverage. Mentions are observations of reporting, not independent world shocks. GDELT is not a truth-label dataset and its event ontology may miss subtle cultural changes. Use a bounded period/topic instead of downloading the entire archive.

### D20 — PHEME rumours and non-rumours

**Discovery from publisher repository.** Figshare lists the dataset and a 25.5 MB download, but direct retrieval failed. [Deposited dataset](https://figshare.com/articles/dataset/PHEME_dataset_of_rumours_and_non-rumours/4010619).

**Proposed use:** event-held-out tests for rumor/report classification and time-limited evidence handling, after verifying the exact version and labels. A rumor is unverified at the time, not automatically false; the deposit title does not establish truth labels for every record. Do not expose later corrections or complete conversation trees to an early-time predictor. Historic platform terms and availability must be checked before reuse.

### D21 — CFTC Commitments of Traders

**Documented.** Weekly positions; Legacy history begins January 1986 and Disaggregated/TFF histories June 2006. Official API and annual text/Excel downloads exist. Categories distinguish commercial, managed-money and other positions. [Official guide](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm), [Historical files](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm).

**Proposed use:** test whether crowded positioning adds predictive information for asymmetric responses, using a separately sourced, contract-matched price series and pre-specified surprises. COT alone cannot establish a squeeze or consensus belief. Preserve report publication time, not only position date; distinguish gross/net positions and open interest; define contract rolls. No compatible price-plus-surprise panel was secured in this task, so this is not yet an executable squeeze backtest.

### D22 — ALFRED data vintages

**Documented.** Retrieves economic releases as they were available on a historical date; vintage-date documentation identifies release/revision dates. [ALFRED](https://alfred.stlouisfed.org/), [Vintage API documentation](https://fred.stlouisfed.org/docs/api/fred/series_vintagedates.html).

**Proposed use:** a separate sandbox for research forecast → first release → revision → credibility updates. Use the model's own pre-release forecasts as expectations unless contemporaneous consensus data are separately obtained. A revision is not a forecast surprise. This tests information timing and accounting mechanics; it does not validate a LONGING value-to-price coefficient. Series availability and API-key conditions depend on collection route.

### D23 — Kaggle Web Traffic Time Series Forecasting

**Documented competition description.** Approximately 145,000 Wikipedia article traffic series; a static competition benchmark rather than current behavior measurement. [Original competition](https://www.kaggle.com/competitions/web-traffic-time-series-forecasting), [Rules](https://www.kaggle.com/c/web-traffic-time-series-forecasting/rules).

**Proposed use:** compare simple seasonal forecasts with decay/event models across many attention series. Check download access, exact date spans and rules before collection. It overlaps D17's measurement family and is not independent evidence confirming an attention mechanism. Chronological validation is required even when convenient competition train/test files exist.

## Kaggle routes and provenance traps

Kaggle is useful for discovery and convenient copies; original publishers usually provide clearer weights, codebooks, revisions and reuse terms.

| Kaggle resource | Relationship and collection decision |
|---|---|
| [ATUS](https://www.kaggle.com/datasets/bls/american-time-use-survey) | Card lists 2003–2015 microdata; prefer the documented current BLS files for full longitudinal coverage. A mirror is not a second study. |
| [Music Sales Data](https://www.kaggle.com/datasets/thedevastator/music-sales-data/versions/2) | Card attributes data to RIAA. Audit units, revenue basis and category versions against the original before merging. |
| [Seattle checkouts](https://www.kaggle.com/datasets/city-of-seattle/seattle-checkouts-by-title) | Convenient snapshot; prefer the city catalog and record its exact extraction date. |
| [Online Retail II mirror](https://www.kaggle.com/datasets/sanlian/online-retail-dataset) | Card points to UCI but labels the copy CC0, whereas current UCI says CC BY 4.0. Use the original and its attribution terms; mirror metadata does not remove them. |
| [KKBox](https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge) | Potentially valuable original industry benchmark; access/terms audit still needed. |
| [Web Traffic](https://www.kaggle.com/competitions/web-traffic-time-series-forecasting) | Useful fixed benchmark for the attention layer. |

Generic loneliness or social-media/happiness CSVs were not promoted to the shortlist when sampling, collection dates and provenance could not be verified. For example, the [Social Media Usage and Emotional Well-Being card](https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being) was discoverable but its provenance was not established in this session. This is not a claim that it is synthetic; it is a reason not to use it as calibration evidence yet.

Art-auction or collectible sale prices are attractive analogies for contested value, but no sufficiently documented open longitudinal transaction panel was verified in this pass. Asking prices, catalog records and aggregate sales reports would not close that gap. Direct willingness-to-pay, expected waiting value, handwritten-practice incidence, analyst consensus and cultural short positions remain especially weakly observed.

## What missing quantities these datasets can expose

All items below are hypotheses to assess, not newly adopted common factors.

| Candidate quantity | Where to test | Why it could change the model |
|---|---|---|
| Available time and care/work constraints | ATUS, Korean Time Use | Practices may fall because opportunity disappears, rather than preferences changing. |
| Infrastructure/access | IMLS, UPU, KOBIS | A closed venue or absent supply suppresses participation without extinguishing demand. |
| Entry, repeat use, temporary exit and return | Media Panel, UKHLS, UCI, KKBox | Cumulative adoption cannot describe active practice or revival alone. |
| Cohort composition | Time-use surveys, panels, USPS | Population replacement can look like individuals abandoning a practice. |
| Coexistence/complementarity | Seattle, RIAA, Media Panel | Digital adoption need not subtract one-for-one from physical use. |
| Price, inflation and product mix | RIAA, UCI, KOBIS | Higher spending may reflect higher prices rather than more participation. |
| Network contact opportunities | SocioPatterns | Encounter frequency depends on schedules and network structure, not one universal friction rate. |
| Reporting intensity and measurement revision | GDELT, PHEME, ALFRED | More reports can create apparent shocks even when the underlying state barely changes. |

No listed field should become a priced common factor solely because it is measurable. It may belong in the observation model, a denominator, a control, a security-specific state, or uncertainty estimates.

## Proposed backtesting protocol

### Pilot 1: physical/digital substitution, Seattle

After inspecting the schema, build monthly physical and digital counts, total counts, and physical share. Retain item/format detail to examine heterogeneity. Start with a complete pre-pandemic interval selected from verified coverage; keep later periods as temporal holdouts and report closure/reopening periods separately.

Compare (a) last-year same-month baseline, (b) seasonal trend plus measured access/supply controls where obtainable, and (c) a constrained substitution/coexistence model. Score count forecasts with MAE or Poisson deviance as appropriate and share forecasts with absolute error. Inspect residual seasonality and parameter stability. Do not infer substitution causality solely because two aggregate trends have opposite slopes.

### Pilot 2: time opportunity, ATUS

Pre-register a small interpretable activity mapping; estimate weighted participation and conditional duration separately by year and broad demographic groups. Compare a trend/composition baseline with a model adding work, care and companion measures. Use design-aware uncertainty and later-year holdouts, not randomly shuffled episodes. Repeated cross-sections cannot estimate each person's transition probability.

### Pilot 3: decline and revival, RIAA

Construct a version-consistent format-year panel. Fit simple trend/decay, substitution-only and substitution-with-coexistence alternatives. Hold out multiple historical periods rather than choosing a single famous revival retrospectively. Use volume only where verified; report revenue separately. If all models fit historical decline but fail recovery, the missing state may be re-entry, supply, price or cohort demand—not another technology score.

### Pilot 4: attention adds information, Wikimedia plus behavior

Choose attention topics before examining correlations. Aggregate at the behavior source's native frequency, using lagged attention and matched geography when available. Compare behavior-only forecasts with behavior-plus-attention. If attention adds no stable out-of-sample improvement, keep it as contextual evidence instead of a price driver. Language coverage mismatch remains a limitation even after rescaling.

### Pilot 5: information and positioning mechanics

Use PHEME/GDELT for evidence handling, ALFRED for publication/revision timing, and COT only after securing compatible prices and surprise proxies. Evaluate these as separate modules. Do not concatenate unrelated countries, dates and outcomes into one panel and call it a historical LONGING market.

### Common controls against overengineering

- Freeze targets, candidate mappings and temporal splits before fitting. Tune preprocessing and hyperparameters inside training folds only.
- Use rolling-origin tests and leave-one-series/group-out transfer tests where the data support them. Compare against naïve/seasonal forecasts and a small regularized model.
- Add one mechanism at a time; remove it again to measure its incremental contribution. Choose a simpler model when performance differences are small relative to uncertainty and its explanations are more stable.
- Report forecast error, uncertainty coverage, coefficient sign stability, sensitivity to normalization, and whether event attribution changes arbitrarily when correlated indicators are swapped.
- Let factors outnumber securities if the measurement structure and restrictions justify it. More rows from diaries or weekly interpolation do not automatically provide independent variation for every latent factor. Inspect effective rank and weak identification; do not use factor count alone as the verdict.
- Keep exact ledger reconciliation as a numerical consistency test, separate from causal recovery and predictive accuracy. Synthetic known-truth shocks can test implementation and recovery under assumptions; they cannot validate those assumptions in the real world.
- Preserve a level's native frequency. Carry the last known annual observation as stale information with an age flag if needed; interpolated weeks are modeled values, not additional observations. Current revised archives permit retrospective validation only unless publication vintages are reconstructed.
- Include contrary cases and stable practices. A model that makes every series decline despite held-out growth fails the empirical test even if the artwork retains its authored secular-bear premise.

## Minimal collection contract

Before any fit, record dataset/version, publisher URL, retrieval date, license, file checksum, unit, geography/population, observation date, publication date, revision/vintage, sampling weights, missing-value codes, classification changes and transformation history. Never replace a registered raw source. Keep future binary dataset storage and derived tables distinct from these research notes.

For every candidate output, label **OBSERVED**, **MODELED** or **EDITORIAL**. For each proposed coefficient record its units, estimation window, uncertainty and target. No parameter value, factor architecture, security unit or empirical backtest result was adopted or produced by this survey.
