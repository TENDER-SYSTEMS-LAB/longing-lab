# LONGING — Technology Diffusion Proxy Sourcing

**Audit date: 20 September 2026. Training cut-off: December 2025.** Publications, revisions and observations dated after that cut-off are marked **†**. They are outside what I can attest from training knowledge; statements about them below rely on the sources retrieved during this audit.

**Finding:** substantial historical material exists, but this audit does **not** establish an uninterrupted, like-for-like, measured 1996–2026 series covering all seven waves. The strongest candidates measure Internet use or telecommunications connections. Later waves introduce different populations, questions and units; generative-AI sources remain particularly heterogeneous.

There is also a calendar limitation: **1996–2026 contains 31 annual labels across a thirty-year interval, and the full 2026 calendar year has not yet occurred.**

## 1 — The inventory

### How to read the tables

**`verified`** means the named series or explicitly bounded published observations were verified—not that every intervening cell has been audited. **`probable`** means the source is a credible candidate, but its exact variable, historical coverage or definition remains unresolved. **`unknown`** means no sufficiently identified series was established.

“First year” and “last year” report **verified coverage**, not an assumed inception or final publication. **“Not established” is intentional.** Publication archives, chart-axis endpoints and a database’s global reference period are not proof of country-year observations.

### International series used in all three inventories

These exact identifiers resolve ambiguity between similarly named national statistics:

| ID      | Exact series name and source                                                                                                                                              | Publisher                          | Definition                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **W-I** | [Individuals using the Internet (% of population) — `IT.NET.USER.ZS`](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IT.NET.USER.ZS) | ITU; republished in World Bank WDI | Internet use from any location/device during the preceding three months, subject to country-source qualifications. |
| **W-M** | [Mobile cellular subscriptions (per 100 people) — `IT.CEL.SETS.P2`](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IT.CEL.SETS.P2)   | ITU; WDI                           | Voice-capable cellular subscriptions, not unique owners.                                                           |
| **W-B** | [Fixed broadband subscriptions (per 100 people) — `IT.NET.BBND.P2`](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IT.NET.BBND.P2)   | ITU; WDI                           | Qualifying fixed subscriptions divided by population; residential and organizational connections.                  |

The series names, identifiers and annual frequency are verified. Their metadata give global reference periods of **1990–2025 for W-I** and **1998–2025 for W-B**. Those are **not verified national coverage ranges**. Country pages were only partly accessible, and data/API retrieval failed repeatedly; consequently, the nine country-series extracts below remain `probable`, rather than certified complete histories. ([DataBank][1])

**Reuse and revision:** the WDI metadata specify **CC BY 4.0** and request attribution to ITU. The database reports an update on **13 July 2026†**. That is a database refresh date, **not a verified numerical-revision date for any particular country series**. Direct ITU products should not automatically be assumed to have identical reuse terms. ([DataBank][1])

### Japan

| Technology                            | Series name                                                          | Publisher                                                | First year                                            | Last year         | Frequency                                                  | Unit and definition                                                                                           | Status                                                                                        |
| ------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | ----------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Dial-up / BBS                         | No sufficiently identified national series                           | Not established                                          | —                                                     | —                 | —                                                          | A BBS account, dial-up subscription and Internet user would be different quantities                           | **unknown**                                                                                   |
| General Internet diffusion            | **W-I**, Japan                                                       | ITU / World Bank                                         | Not established                                       | Not established   | Annual                                                     | Individuals using Internet, subject to country notes                                                          | **probable** — country-year extract not audited                                               |
| General Internet diffusion            | **インターネット利用率**, MIC results reproduced by NICT                       | MIC; NICT republication                                  | 2020 checked; earlier history not established         | 2025              | Annual                                                     | Reported national individual-use rate; denominator must be tied to the selected MIC table                     | **verified** for the published 2020–2025 excerpt. ([NICT][2])                                 |
| Mobile telephony                      | **W-M**, Japan                                                       | ITU / World Bank                                         | Not established                                       | Not established   | Annual                                                     | Subscriptions per 100 people                                                                                  | **probable** — extract not audited                                                            |
| Mobile telephony                      | **携帯電話契約数 / 事業者別契約数**                                                | Telecommunications Carriers Association, TCA             | January 1996 archive                                  | June 2026†        | Monthly historical archive; current quarterly presentation | Operator-reported subscription counts, not individuals                                                        | **verified** endpoints and archive; uninterrupted retrieval not established. ([TCA][3])       |
| Fixed broadband                       | **W-B**, Japan                                                       | ITU / World Bank                                         | Not established                                       | Not established   | Annual                                                     | Fixed subscriptions per 100 people                                                                            | **probable** — extract not audited                                                            |
| Fixed broadband / access technology   | **問２ 自宅でインターネットを利用する世帯の接続回線**, 通信利用動向調査, household table 10          | MIC / e-Stat                                             | 2024 checked                                          | 2025              | Annual                                                     | Connection types among households using Internet at home; not automatically an all-household penetration rate | **probable** as a broadband series; table verified, category history unchecked. ([e-Stat][4]) |
| Smartphones                           | **問１ 情報通信機器の保有状況**, household table 7; smartphone category candidate | MIC / e-Stat                                             | Not established                                       | 2025 table exists | Annual survey                                              | Household equipment ownership; exact smartphone-category history not extracted                                | **probable**. ([e-Stat][5])                                                                   |
| Social web                            | Platform-use items in **情報通信メディアの利用時間と情報行動に関する調査**                   | MIC, Institute for Information and Communications Policy | Item history unverified; 2012 survey catalog verified | Not established   | Survey editions                                            | Exact platform questions, ages and denominators not verified                                                  | **probable — could not verify underlying tables**. ([e-Gov 데이터 포털][6])                        |
| Messaging                             | Messaging-platform items in the same MIC media-use survey            | MIC / IICP                                               | Not established                                       | Not established   | Survey editions                                            | A platform-specific rate would not establish all-messaging adoption                                           | **probable — could not verify underlying tables**. ([e-Gov 데이터 포털][7])                        |
| Generative AI                         | **生成AI計の利用経験**, NRC Daily Tracking report                            | Nippon Research Center, NRC                              | March 2023                                            | March 2026†       | Selected survey waves                                      | Experience using any listed generative-AI service; online respondents aged 20–69, weighted                    | **verified**, not a daily AI-adoption series. ([NRC][8])                                      |
| Generative AI, cross-country estimate | **AI Diffusion / AI User Share**, described in §4                    | Microsoft AI Economy Institute                           | H1 2025                                               | H2 2025           | Two half-year observations verified                        | Estimated users relative to working-age population                                                            | **verified** published estimates, not an industry census. ([Microsoft][9])                    |

**Japan source locations, reuse and revision status**

**MIC / e-Stat:** the [Communications Usage Trend Survey archive](https://www.e-stat.go.jp/stat-search/files?toukei=00200356) contains survey editions from **1996 through 2025**. This does not establish every variable over that span. The 2025 edition was published/updated **29 May 2026†**; its last numerical revision is not separately identified. e-Stat permits commercial reuse and adaptation with attribution and disclosure of processing; its terms are compatible with CC BY 4.0, subject to exclusions. ([e-Stat][10])

**TCA:** [current database](https://www.tca.or.jp/database/) and [historical archive](https://www.tca.or.jp/database/index_archive.html). The latest reference period verified was June 2026†; no numerical-revision date was identified. TCA’s posted copyright terms require permission outside permitted quotation/private-use exceptions; this is **not an identified open-data licence**. ([TCA][11])

**MIC media-use survey:** official government catalog records for the [2012 edition](https://data.e-gov.go.jp/data/dataset/soumu_20160325_0043) and [2013 edition](https://data.e-gov.go.jp/data/dataset/soumu_20160325_0044) were accessible, but the underlying MIC landing page was not. Catalogue updates dated **16 June 2023** do not establish numerical revisions. Exact reuse terms for the underlying files remain unverified. ([e-Gov 데이터 포털][6])

**NRC:** [March 2026 generative-AI report](https://www.nrc.co.jp/report/260410.html), published **10 April 2026†**. No numerical-revision history was found. The page requests contact concerning quotation/reproduction and requires source credit; no open-data licence was established. ([NRC][8])

### Republic of Korea

| Technology                            | Series name                                                                            | Publisher                      | First year                                           | Last year                   | Frequency                                  | Unit and definition                                                              | Status                                                                                           |
| ------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------- | --------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Dial-up / BBS                         | No sufficiently identified national series                                             | Not established                | —                                                    | —                           | —                                          | Service subscriptions and unique users would require separate accounting         | **unknown**                                                                                      |
| General Internet diffusion            | **W-I**, Korea, Rep.                                                                   | ITU / World Bank               | Not established                                      | Not established             | Annual                                     | International Internet-use series                                                | **probable** — extract not audited                                                               |
| General Internet diffusion            | **인터넷이용률**, 인터넷이용실태조사                                                                  | MSIT / NIA; e-Nara Index       | 2000 documented; earlier inception not established   | 2025                        | Annual since 2008; previously twice yearly | Currently population aged 3+ using wired/wireless Internet in the previous month | **verified**, with documented breaks. ([지표누리][12])                                               |
| Mobile telephony                      | **W-M**, Korea, Rep.                                                                   | ITU / World Bank               | Not established                                      | Not established             | Annual                                     | Subscriptions per 100 people                                                     | **probable** — extract not audited                                                               |
| Mobile telephony                      | **유·무선통신서비스 가입 현황 및 무선데이터 트래픽 통계**                                                     | MSIT; ITSTAT distribution      | May 2025 edition checked; earlier history unverified | June 2026† catalogue entry  | Monthly                                    | Subscription categories; exact inclusion of non-handset connections not checked  | **probable** as a continuous, consistently classified series. ([MSIT][13])                       |
| Fixed broadband                       | **W-B**, Korea, Rep.                                                                   | ITU / World Bank               | Not established                                      | Not established             | Annual                                     | Fixed subscriptions per 100 people                                               | **probable** — extract not audited                                                               |
| Fixed broadband                       | **과학기술정보통신부_유선통신서비스 통계**, 초고속인터넷 component                                             | MSIT / data.go.kr / ITSTAT     | December 2017                                        | November 2024               | Monthly                                    | National fixed-service subscription statistics, including high-speed Internet    | **verified** catalogue coverage; earlier/later files not established here. ([데이터.go.kr][14])     |
| Social web                            | SNS-use items in **인터넷이용실태조사**; exact historical table label unchecked                 | MSIT / NIA                     | Not established                                      | 2025 parent survey verified | Annual survey                              | Exact age base and reference window unresolved                                   | **probable**                                                                                     |
| Smartphones                           | Smartphone ownership items in the same survey; exact historical table label unchecked  | MSIT / NIA                     | Not established                                      | 2025 parent survey verified | Annual survey                              | Personal versus household denominator requires table-level verification          | **probable**                                                                                     |
| Messaging                             | Instant-messenger-use items in the same survey; exact historical table label unchecked | MSIT / NIA                     | Not established                                      | 2025 parent survey verified | Annual survey                              | Exact reference window and eligible population unresolved                        | **probable**                                                                                     |
| Generative AI                         | Generative-AI experience reported in **인터넷이용실태조사**; exact table label unchecked        | MSIT / NIA                     | 2023 published comparison                            | 2025                        | Annual observations                        | Experience rate; full question, recall window and age denominator not verified   | **probable** as a harmonizable series; three published annual figures verified. ([KDI EIEC][15]) |
| Generative AI, cross-country estimate | **AI Diffusion / AI User Share**, §4                                                   | Microsoft AI Economy Institute | H1 2025                                              | H2 2025                     | Two half-year observations verified        | Estimated users / working-age population                                         | **verified** published estimates. ([Microsoft][9])                                               |

For the three unresolved survey-item rows, the **parent publication is verified, not the requested variable history**. I have not assigned a guessed start year or treated a familiar Korean label as a verified historical series identifier.

**Korea source locations, reuse and revision status**

**Internet Usage Survey:** [official Internet-use indicator and archive](https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1346). The 2025 results were announced **31 March 2026†**; the indicator page shows an update on **27 April 2026†**. Neither establishes when each historical number was last revised. ([Korea][16])

Licensing is **edition-specific**. The [2024 full-report posting](https://www.msit.go.kr/bbs/view.do?bbsSeqNo=79&mId=99&mPid=74&nttSeqNo=3173673&sCode=user) displays **KOGL Type 4: attribution, non-commercial, no derivatives**. The [2025-results release](https://www.msit.go.kr/bbs/view.do?bbsSeqNo=94&mId=113&nttSeqNo=3187098) displays **KOGL Type 1: attribution**. A single blanket licence for the entire survey history would therefore be inaccurate. The last correction notice found for the 2024 report is **8 September 2025**. ([MSIT][17])

**Fixed-service dataset:** [data.go.kr record](https://www.data.go.kr/data/15070091/fileData.do?recommendDataYn=Y), **KOGL Type 1**. Catalogue modification: **31 July 2025**; numerical-revision date unknown. ([데이터.go.kr][14])

**Monthly telecommunications release:** the May 2025 edition was posted **18 July 2025** and displays **KOGL Type 4**. That licence should not be silently transferred to a different ITSTAT edition or file. Numerical revision history remains unverified. ([MSIT][13])

### United States

| Technology                            | Series name                                                                | Publisher                      | First year      | Last year       | Frequency                                           | Unit and definition                                                                   | Status                                                                |
| ------------------------------------- | -------------------------------------------------------------------------- | ------------------------------ | --------------- | --------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Dial-up / BBS                         | No sufficiently verified continuous series in this audit                   | Not established                | —               | —               | —                                                   | NTIA/Census connection-type files remain a retrieval lead, not a certified BBS series | **unknown**                                                           |
| General Internet diffusion            | **W-I**, United States                                                     | ITU / World Bank               | Not established | Not established | Annual                                              | International Internet-use series                                                     | **probable** — extract not audited                                    |
| General Internet diffusion            | **Internet use**                                                           | Pew Research Center            | 2000            | 2025            | Survey observations, pooled by available year; gaps | Percentage of adults saying they use Internet                                         | **verified**. ([Pew Research Center][18])                             |
| Mobile telephony                      | **W-M**, United States                                                     | ITU / World Bank               | Not established | Not established | Annual                                              | Subscriptions per 100 people                                                          | **probable** — extract not audited                                    |
| Mobile ownership                      | **Mobile phone ownership — cellphone**                                     | Pew                            | 2002            | 2025            | Irregular survey waves                              | Percentage of adults owning a cellphone                                               | **verified**. ([Pew Research Center][19])                             |
| Fixed broadband                       | **W-B**, United States                                                     | ITU / World Bank               | Not established | Not established | Annual                                              | Fixed subscriptions per 100 people                                                    | **probable** — extract not audited                                    |
| Home broadband adoption               | **Home broadband use**                                                     | Pew                            | 2000            | 2025            | Irregular survey observations                       | Percentage of adults with home broadband; not operator subscriptions                  | **verified**. ([Pew Research Center][18])                             |
| Social web                            | **Facebook**, platform-use time series in *Social Media Fact Sheet*        | Pew                            | 2012            | 2025            | Irregular survey waves                              | Percentage of adults reporting platform use; not all-social-web adoption              | **verified**, narrow proxy. ([Pew Research Center][20])               |
| Smartphones                           | **Mobile phone ownership — smartphone**                                    | Pew                            | 2011            | 2025            | Irregular survey waves                              | Percentage of adults owning a smartphone                                              | **verified**. ([Pew Research Center][19])                             |
| Messaging                             | **WhatsApp**, platform-use time series                                     | Pew                            | 2018            | 2025            | Published years: 2018, 2019, 2021, 2023–2025        | Percentage of adults using this platform, not any messaging service                   | **verified**, narrow proxy with gaps. ([Pew Research Center][20])     |
| Generative AI                         | **Ever used ChatGPT**, reported in *34% of U.S. adults have used ChatGPT…* | Pew                            | 2023            | 2025            | Repeated survey waves                               | Adults aged 18+; lifetime experience with one named product                           | **verified**, not industry-wide adoption. ([Pew Research Center][21]) |
| Generative AI, cross-country estimate | **AI Diffusion / AI User Share**, §4                                       | Microsoft AI Economy Institute | H1 2025         | H2 2025         | Two half-year observations verified                 | Estimated users / working-age population                                              | **verified** published estimates. ([Microsoft][9])                    |

**US source locations, reuse and revision status**

Pew provides the [Internet/broadband](https://www.pewresearch.org/internet/fact-sheet/internet-broadband/), [mobile](https://www.pewresearch.org/internet/fact-sheet/mobile/) and [social-media](https://www.pewresearch.org/internet/fact-sheet/social-media/) tables, with downloadable data. The verified fact-sheet editions are dated **20 November 2025**. These are publication/update dates; I found no complete numerical-revision ledger. The ChatGPT report was updated **25 June 2025**, using fieldwork conducted **24 February–2 March 2025**. ([Pew Research Center][18])

[Pew’s terms](https://www.pewresearch.org/about/terms-and-conditions/) permit substantial reuse, including modification, subject to attribution, notices and other restrictions. They prohibit implied endorsement and place limits on wholesale republication and unauthorized scraping. They are **not simply a non-commercial-only licence**. ([Pew Research Center][22])

**National versus international versions:** both have been retained above rather than substituted for one another. I verified important definitional differences, but **did not verify matched-vintage numerical discrepancies between their complete country-year extracts**.

## 2 — Definitions that do not match

### Dial-up and bulletin-board services

No harmonized three-country definition was verified. At least four possible quantities must remain separate: people using a service, registered accounts, paid subscriptions, and connections using a particular access technology.

Consequently, **general Internet penetration is not a measured dial-up/BBS series**. Nor can dial-up users be recovered by subtracting broadband subscriptions from Internet users: those operands count different things.

### General Internet use: one month, three months, one year

This is the clearest verified mismatch:

| Source                                   | Verified question or reference window              | Population/denominator issue                                                |
| ---------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| ITU/WDI                                  | Internet use during the preceding **three months** | Country-source qualifications remain relevant                               |
| Korea’s national Internet-use indicator  | Use during the preceding **one month**             | Currently ages **3+**; historical age scope changed                         |
| Japan’s 2025 MIC household-member tables | Experience during the preceding **one year**       | Separate tables exist for **all respondents** and **excluding nonresponse** |
| Pew US Internet-use series               | Whether adults say they use Internet               | Adult population; not established here as the same three-month question     |

These are not equivalent prevalence measures. Japan’s two denominator versions are themselves a warning against selecting a figure solely because its headline says “Internet use.” ([DataBank][1])

### Mobile telephony: subscriptions versus people

ITU’s subscription definition includes postpaid accounts and prepaid accounts active within the preceding three months. It excludes specified categories such as data-only mobile-broadband subscriptions, paging and telemetry. Multiple qualifying subscriptions held by one person remain multiple subscriptions; **a result above 100 per 100 people is not an error**. ([DataBank][23])

Japan’s TCA series is an operator-subscription count. Pew measures adult ownership. The exact inclusion rules for the Korean monthly categories were not extracted. These cannot be made into equivalent ownership rates merely by dividing all three by population. TCA also explicitly states that smartphones are included in cellphone totals but that it does not compile the requested smartphone breakdown. ([TCA][11])

### Fixed broadband: speed, technology and denominator

The WDI long definition uses a **256 kbit/s downstream threshold**, includes residential and organizational subscriptions, and includes satellite and terrestrial fixed wireless while excluding mobile-cellular access. However, another paragraph on the same metadata page excludes technologies classified as wireless broadband. **That internal wording inconsistency needs ITU clarification; it is not a verified dated definition change.** ([DataBank][24])

Japan’s household connection-type table, Korea’s administrative line counts, and Pew’s adult home-broadband rate measure different objects. In particular, Japan’s table is explicitly about households already using Internet at home; its connection-type percentages should not automatically be treated as percentages of all households. ([e-Stat][5])

A country’s contemporary policy definition of “adequate broadband” must not be substituted retrospectively for the statistical threshold without creating a separately documented series.

### Social web

The verified US series is platform-specific. The Japanese and Korean candidate histories still require exact questionnaires and denominators. I did not establish a common “any social network” definition across all three.

Adding platform percentages would double-count people using more than one platform. A changing list of surveyed platforms can also change measured coverage without any individual changing behavior. Pew’s platform inventory itself expands over time. ([Pew Research Center][20])

### Smartphones

**Household possession, individual ownership, use of a smartphone to access Internet, and smartphone-associated subscriptions are four different variables.** Japan’s household equipment table and Pew’s adult ownership series belong to different categories; the Korean candidate requires table-level verification. A household ownership percentage cannot be converted to an individual ownership percentage from household size alone. ([e-Stat][5])

### Messaging platforms

The verified US WhatsApp series is not a measure of all instant messaging. The Japanese and Korean candidate sources require verification of whether they count a named app, any messenger, SMS, or particular activities.

A common scale cannot resolve a different service universe. The required numerator is the **union of eligible users**, not the sum of app-specific user percentages.

### Generative AI

Japan’s NRC measure concerns experience with listed services among ages **20–69**; it also publishes a separate “currently using” measure. Pew concerns **ever using ChatGPT among adults 18+**. Korea publishes an experience rate, but I could not verify its complete age and recall specifications. Microsoft supplies a calibrated working-age-population estimate. These should not be presented as four implementations of the same question. ([NRC][8])

**Base years:** these prevalence rates and subscription densities do not inherently have an index base year. Setting a year to 100 would be a subsequent transformation, not a property of the published statistic.

## 3 — Breaks, revisions and discontinuities

The following were verified. This is **not an exhaustive audit of every questionnaire and statistical vintage since 1996**.

| Year/date                             | Source                                  | What changed or remains unresolved                                                                                                                                                                                                                                    |
| ------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2002; 2006**                        | Korea Internet Usage Survey             | Minimum age changed from 7+ to 6+ in 2002, then to 3+ in 2006.                                                                                                                                                                                                        |
| **2004**                              | Korea Internet-use indicator            | Criterion changed from average monthly use to use within the preceding month.                                                                                                                                                                                         |
| **2008**                              | Korea survey                            | Renamed from 정보화실태조사 to 인터넷이용실태조사; twice-yearly collection became annual.                                                                                                                                                                                             |
| **2006, 2008, 2009, 2014**            | Korea survey                            | Documented sample-size changes: 10,000, 17,000, 30,000 and 25,000 households respectively. These are survey-design changes, not automatically discontinuities of known magnitude.                                                                                     |
| **October 2013**                      | TCA archive                             | PHS and BWA reporting changed to quarterly. This notice must **not** be misread as establishing the same change date for cellphone reporting.                                                                                                                         |
| **2015–2018**                         | Pew home broadband                      | Question wording changed. Pew specifically identifies July 2015 and January 2018 as directly comparable observations.                                                                                                                                                 |
| **2023; 2024**                        | Pew technology fact sheets              | Telephone surveys gave way to web/mail in 2023; the later protocol included telephone as well. These are marked mode changes, not invisible joins.                                                                                                                    |
| **8 April, 8 July, 8 September 2025** | Korea 2024 Internet Usage Survey report | Posted corrections concern demographic/sample tables, education/learning material, and later typographical corrections. The notices do not justify assuming that all headline rates changed.                                                                          |
| **June 2026†**                        | Anthropic Economic Index                | New continuous sampling replaced the earlier seven-day sampling approach; product scope and classification procedures also changed.                                                                                                                                   |
| **Retrieval on 20 September 2026†**   | OpenAI Signals                          | The download page identifies v2.0, while the rendered dictionary retrieved during this audit displayed v1.1. This is a **retrieval/version inconsistency**, not proof that the underlying dataset is wrong. Version-specific historical revisions were not certified. |

Sources for the Korean historical changes: official indicator documentation. ([지표누리][12]) TCA: archive notice. ([TCA][3]) Pew: fact-sheet notes. ([Pew Research Center][18]) Korean corrections: original report posting. ([msit.go.kr][17]) AI changes: publisher documentation and retrieved dictionary image. ([Anthropic][25])

Two additional qualifications matter. **TCA’s current navigation did not resolve 2014–2016 during this audit**; that is an access/continuity-verification gap, not evidence that measurements ceased. And the WDI database refresh date does not reveal which historical country values changed. ([TCA][11])

## 4 — The gap after the last measurement: generative AI

**I did not find a verified public, continuous, industry-wide series of national generative-AI usage volumes for Japan, Korea and the US.** This is a statement about what was established here, not a claim that no unpublished industry data exist.

The closest verified sources fall into different categories.

### Vendor disclosures: actual published totals, but snapshots

OpenAI’s **15 September 2025** publication, [*How people are using ChatGPT*](https://openai.com/index/how-people-are-using-chatgpt/), states **700 million weekly active users**. That is an actual publisher disclosure, not an estimate invented for this audit. But the page does not supply an uninterrupted national series or identify the exact reporting week for that headline total. Its numerical-revision history and a dedicated open licence for that disclosure were not established. ([OpenAI][26])

A sequence of such announcements remains a sequence of announcements unless the underlying reporting definitions, dates and missing periods are supplied.

### OpenAI Signals: downloadable longitudinal vendor data

[OpenAI Signals](https://openai.com/signals/data/) reports coverage from **July 2024 through June 2026†**, with an HTML update dated **6 August 2026†**. The [download page](https://openai.com/signals/data-download/) offers data under **CC BY 4.0**. Published outputs include usage composition and country rankings based on messages per capita—not a complete table of absolute, deduplicated national AI users or industry-wide message totals. Institutional usage is outside the stated consumer-plan scope. ([OpenAI][27])

**Status:** verified dataset publication; exact country-file coverage and the conflicting dictionary version were not fully audited.

### Anthropic Economic Index: continuous sampling does not mean an industry total

The **26 June 2026†** [*Anthropic Economic Index report: Cadences*](https://www.anthropic.com/research/economic-index-june-2026-report) introduces continuous sampling and more granular activity patterns. It describes usage within Anthropic products, not all generative AI. Reported task distributions and relative activity are not interchangeable with population adoption or total national usage volume. An applicable dataset reuse licence and numerical-revision date were not verified here. ([Anthropic][25])

**Status:** verified publisher report and sampling change; not a verified three-country industry-volume series.

### Microsoft: the closest verified common three-country adoption estimate

The **January 2026†** report [*Global AI Adoption in 2025 — A Widening Digital Divide*](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/Microsoft-AI-Diffusion-Report-2025-H2.pdf) publishes **H1 and H2 2025** estimates for all three countries.

Its **AI Diffusion / AI User Share** measure uses Microsoft telemetry with adjustments for factors including device/operating-system coverage and Internet penetration. It is therefore a **calibrated estimate**, not a direct census of every vendor’s users. I found no open-data licence or numerical-revision history for the report. ([Microsoft][9])

### National surveys: adoption experience, not volume

NRC, MSIT/NIA and Pew provide the national observations inventoried above. They are useful evidence of reported experience, but none of those three verified publications supplies a comparable series of total prompts, tokens, sessions or inference-hours.

**The “last measured week” cannot yet be one universal date.** Each input needs at least four dates: reference period, fieldwork period where applicable, publication date, and revision date. For example, Pew’s June 2025 ChatGPT article reports February–March fieldwork, not June usage. ([Pew Research Center][21])

An annual observation does not create 52 measured weekly observations. Interpolation would need a separate label; extrapolation begins beyond an observation’s reference coverage, not automatically beyond its publication date. Interior missing years also remain missing even before the latest observation.

## 5 — A normalisation proposal

**Proposed rule: match the measured quantity first; scale second. Unmatched quantities remain separate or missing.** This is a data-normalisation rule, not a proposal for index behavior.

### A. Fix the observation record

For each value, retain:

```text
country
technology_definition_id
source_series_id
reference_start / reference_end
population_universe
unit
question_and_recall_window
survey_or_administrative_method
estimate_flag
release_date / revision_date / retrieval_date
source_version_or_file_hash
value
```

Freeze a particular source vintage. A later revised figure must create a new vintage rather than silently replacing a published historical record.

### B. Connections: use subscription density, not ownership probability

For a consistently defined administrative count:

$$
D_{c,t}=100\frac{C_{c,t}}{P_{c,t}},
$$

where \(C\) is the qualifying connection count and \(P\) is the specified population denominator from one documented population vintage.

Use the same inclusion rules and reference-date convention across countries. **Do not cap the result at 100.** Do not relabel it as the percentage of people who adopted the technology.

When numerator and denominator are unavailable separately, retain the published per-100 series; do not pretend it has been recalculated using a common population vintage.

### C. Individuals: harmonize questions and, where possible, age

For an explicitly matched individual-use question, a reproducible age-standardized option is:

$$
A_{c,t}=100\sum_{a=1}^{5}0.2\,p_{c,t,a},
$$

with five age bands: **20–29, 30–39, 40–49, 50–59, 60–69**.

Here \(p_{c,t,a}\) is the survey-weighted proportion satisfying the **same technology definition and recall window** in each age band. Require, for example, “used during the preceding three months” consistently; do not convert lifetime experience into three-month use.

If a required age band or matching question cannot be recovered from published tables or authorized microdata, the result is **NA**. Do not split a 50–64 age bin by assumption. The aggregate sources verified above do **not currently supply everything needed to execute this harmonization**.

This rule assumes meaningful equivalence of translated questions and survey coverage. It deliberately removes differences in age composition and therefore no longer represents each country’s actual population-average adoption.

### D. Annualization and gaps

For administrative end-of-year series, use the December observation only when it exists and matches the definition. For surveys, retain the actual fieldwork window; an observation assigned to a year remains a survey estimate for that window, not a calendar-year average.

Missing values remain **NA**. Pre-launch years are not automatically observed zeroes. No interpolation, smoothing, extrapolation or substitution from another source is implicit in this rule.

### E. When only within-country change is defensible

Within an unchanged-definition segment, an optional relative scale is:

$$
R_{c,t}=100\frac{x_{c,t}}{x_{c,b}},
$$

where \(b\) is the earliest verified year in that segment with \(x_{c,b}>0\). Publish \(b\) explicitly.

This permits a statement about **relative change within that segment**. It does not permit country-level adoption rankings when countries have different baselines or definitions. Equal index values can correspond to very different adoption levels.

**Still invalid after normalization:** subscriptions versus persons; households versus individuals; platform-specific versus all-platform adoption; lifetime versus recent use; estimated vendor coverage versus an industry census; and precise point-in-time comparisons between surveys conducted in different periods. Arithmetic scaling cannot repair those differences.

## 6 — What cannot be sourced

| Missing evidence                                                                                      | Classification reached in this audit                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A continuous, harmonized 1996–2026 BBS/dial-up adoption series for all three countries                | **Not found.** Whether suitable national components were unpublished or collected under other definitions remains unresolved.                                                                                                                                                                                              |
| Complete WDI country-year extracts, source flags and revision histories                               | **Published infrastructure, but not successfully retrieved/audited here.** Metadata availability did not establish complete measured annual coverage.                                                                                                                                                                      |
| Historical Japanese smartphone, social-platform and messaging items with stable definitions           | **Published survey archives exist; exact variable histories were not verified.** Direct MIC access was unsuccessful.                                                                                                                                                                                                       |
| Full Korean SNS, messenger, smartphone and generative-AI question/denominator histories               | **Published survey material exists, but the necessary tables were not successfully inspected.**                                                                                                                                                                                                                            |
| NTIA/Census connection-type histories and FCC administrative broadband histories                      | **Published-source leads, not completed verification.** The [NTIA dataset page](https://www.ntia.gov/page/download-ntia-internet-use-survey-datasets) and [FCC report page](https://www.fcc.gov/internet-access-services-reports) could not be adequately inspected; coverage and reuse terms are therefore not certified. |
| Public, deduplicated national usage volumes across all generative-AI vendors                          | **No verified publication found.** Vendor totals cannot be added into this quantity without overlap and coverage information.                                                                                                                                                                                              |
| Full-calendar-year 2026 observations                                                                  | **Not yet measurable as a completed year on 20 September 2026.**                                                                                                                                                                                                                                                           |
| One observed weekly transition date from measurement to extrapolation for the entire proposed history | **Not established as a measured quantity.** It depends on the chosen sources’ reference periods and on how interior gaps are handled.                                                                                                                                                                                      |

I have not treated inaccessible tables as nonexistent, nor treated potentially purchasable commercial data as verified alternatives.

## 7 — Refusals and confidence

**No requested sourcing question was declined.** I did not manufacture historical values, fill gaps, certify unseen table definitions, or label vendor estimates as industry measurements.

**Overall judgment:** **a defensible thirty-year historical panel of diffusion proxies is plausible, but the continuous three-country series specified here has not been established.** A narrower connectivity history built around Internet use and telecommunications subscriptions is the strongest candidate, conditional on a successful country-year extraction, estimate-flag audit and definition reconciliation. The evidence does not support certifying an uninterrupted, comparable, fully measured seven-wave series through 2026.

Confidence is **high** in the named verified publications and the documented definitional mismatches; **moderate** in the feasibility of assembling a narrower long-run connectivity panel; and **low** in any claim that all required years and waves can already be joined without missing values or changes of meaning.

What this audit found is a set of usable sources and specific verification leads. What remains insufficient is **observation-level coverage, consistent definitions, and a completed 2026 measurement—not merely a choice of normalization formula.**

[1]: https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IT.NET.USER.ZS "Glossary | DataBank"
[2]: https://www.nict.go.jp/info-barrierfree/relate/statistics/elder_net.html "高齢者のインターネット利用率 | :情報通信研究機構 (NICT)"
[3]: https://www.tca.or.jp/database/index_archive.html "https://www.tca.or.jp/database/index_archive.html"
[4]: https://www.e-stat.go.jp/stat-search/files?layout=datalist&lid=000001459471&page=1&utm_source=chatgpt.com "ファイル | 統計データを探す"
[5]: https://www.e-stat.go.jp/stat-search/files?cycle=0&layout=datalist&page=1&tclass1=000001243777&tclass2val=0&toukei=00200356&tstat=000001243701 "通信利用動向調査 令和7年通信利用動向調査 世帯全体編 | ファイル | 統計データを探す | 政府統計の総合窓口"
[6]: https://data.e-gov.go.jp/data/dataset/soumu_20160325_0043?utm_source=chatgpt.com "情報通信メディアの利用時間と情報行動に関する調査_平成24年"
[7]: https://data.e-gov.go.jp/data/dataset/soumu_20160325_0044?utm_source=chatgpt.com "情報通信メディアの利用時間と情報行動に関する調査_平成25年"
[8]: https://www.nrc.co.jp/report/260410.html "https://www.nrc.co.jp/report/260410.html"
[9]: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/Microsoft-AI-Diffusion-Report-2025-H2.pdf "https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/Microsoft-AI-Diffusion-Report-2025-H2.pdf"
[10]: https://www.e-stat.go.jp/stat-search/files?toukei=00200356 "https://www.e-stat.go.jp/stat-search/files?toukei=00200356"
[11]: https://www.tca.or.jp/database/ "https://www.tca.or.jp/database/"
[12]: https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1346 "https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1346"
[13]: https://www.msit.go.kr/bbs/view.do?bbsSeqNo=79&mId=99&mPid=74&nttSeqNo=3173685&pageIndex=&sCode=user&searchOpt=ALL&searchTxt=&utm_source=chatgpt.com "통계정보 | 상세화면"
[14]: https://www.data.go.kr/data/15070091/fileData.do?recommendDataYn=Y "https://www.data.go.kr/data/15070091/fileData.do?recommendDataYn=Y"
[15]: https://eiec.kdi.re.kr/policy/materialView.do?num=264952&utm_source=chatgpt.com "과기정통부, 「2024 인터넷이용실태조사」 결과 발표"
[16]: https://www.korea.kr/briefing/pressReleaseView.do?newsId=156751949 "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156751949"
[17]: https://www.msit.go.kr/bbs/view.do?bbsSeqNo=79&mId=99&mPid=74&nttSeqNo=3173673&sCode=user&utm_source=chatgpt.com "2024 인터넷이용실태조사 결과"
[18]: https://www.pewresearch.org/internet/fact-sheet/internet-broadband/ "Demographics of Internet and Home Broadband Usage in the United States | Pew Research Center"
[19]: https://www.pewresearch.org/internet/fact-sheet/mobile/?utm_source=chatgpt.com "Mobile Fact Sheet - Pew Research Center"
[20]: https://www.pewresearch.org/internet/fact-sheet/social-media/ "https://www.pewresearch.org/internet/fact-sheet/social-media/"
[21]: https://www.pewresearch.org/short-reads/2025/06/25/34-of-us-adults-have-used-chatgpt-about-double-the-share-in-2023/ "https://www.pewresearch.org/short-reads/2025/06/25/34-of-us-adults-have-used-chatgpt-about-double-the-share-in-2023/"
[22]: https://www.pewresearch.org/about/terms-and-conditions/ "https://www.pewresearch.org/about/terms-and-conditions/"
[23]: https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IT.CEL.SETS.P2 "Glossary | DataBank"
[24]: https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IT.NET.BBND.P2 "Glossary | DataBank"
[25]: https://www.anthropic.com/research/economic-index-june-2026-report "https://www.anthropic.com/research/economic-index-june-2026-report"
[26]: https://openai.com/index/how-people-are-using-chatgpt/ "https://openai.com/index/how-people-are-using-chatgpt/"
[27]: https://openai.com/signals/data/ "https://openai.com/signals/data/"
