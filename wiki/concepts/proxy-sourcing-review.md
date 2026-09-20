---
status: working
attribution: llm-synthesis
updated: 2026-09-20
sources:
  - SRC-2026-09-20-proxy-sourcing-prompt
  - SRC-2026-09-20-proxy-sourcing-chatgpt
  - SRC-2026-09-20-proxy-sourcing-claude
  - SRC-2026-09-20-proxy-sourcing-deepseek
  - SRC-2026-09-20-proxy-sourcing-gemini
  - SRC-2026-09-20-proxy-sourcing-glm
  - SRC-2026-09-20-proxy-sourcing-grok
  - SRC-2026-09-20-proxy-sourcing-qwen
  - SRC-2026-09-20-wdi-spine-retrieval
  - SRC-2026-09-20-wdi-internet-use
  - SRC-2026-09-20-wdi-mobile-subscriptions
  - SRC-2026-09-20-wdi-fixed-broadband
  - SRC-2026-09-20-wdi-spine-csv
---

# Proxy Sourcing Review

[[technology-waves]] rests on one claim about the world outside the fiction: that the driver behind the decline can be *measured where measurement exists and extrapolated beyond*, with the institute publishing the boundary. The sourcing round asked seven models whether the measurement half of that claim is true — whether a continuous, comparable series of communication-technology adoption in Japan, Korea and the United States from 1996 to 2026 can be assembled from published statistics, and on what terms. It was written as a sourcing and documentation task, with an invented figure named as the failure mode. Seven responses were collected: ChatGPT, Claude, DeepSeek, Gemini, GLM, Grok and Qwen. Kimi was not consulted.

**No series was downloaded, and no proxy is selected by this page.** What the round produced is an inventory of what is published, a map of where the definitions do not match, a list of breaks, a unanimous verdict on the one question asked, and one finding that changes a sentence on [[technology-waves]]. All reviewer proposals are `llm-proposed`; this comparison is `llm-synthesis`.

## Scope and source quality

The prompt asked each reviewer to state its training cut-off, mark every row `verified`, `probable` or `unknown`, and say when it could not check. Compliance varies more here than in the other two rounds, because the task rewards live retrieval.

- **ChatGPT** is the most rigorous: *first year* and *last year* report verified coverage only, never assumed inception; every post-cut-off item carries a dagger; licences are checked edition by edition; and it declines to certify the World Bank country-year extracts it could not retrieve. Its refusal to fill a cell is the round's model of the requested behaviour.
- **Claude** and **Grok** ran live checks on 20 September 2026, tag them, and refuse to reproduce historical values from memory. Claude supplies the last-measured publication dates for each country's generative-AI point; Grok opens licence pages and finds the Korean restriction below.
- **GLM** performed no live lookup, says so first, gives its cut-off as early 2025, and marks every row as needing re-verification. It is the most honest about its limits and the least current: it cannot attest to any Korean generative-AI survey, which the others verify exists.
- **DeepSeek** checks its rejections and cites secondary republishers (IndexMundi, IndexBox) for figures, which the prompt discouraged; its `verified` means *the series exists*, not *the coverage is confirmed*.
- **Gemini** claims its identifiers were *verified against active domain registries*, which is not a check that establishes coverage, and supplies several breaks with a specificity no other reviewer supports — an earthquake-year sample exclusion, a 2017 mode shift with an *upward step among the 60+*, a 2022 MVNO reclassification. Its normalisation invokes *historical national telecom transformation vectors* it does not define. Recorded, not carried.
- **Qwen** gives its cut-off as *2026*, assigns Japan's individual survey an age floor of 13+ and the US supplement 15+ (no other reviewer agrees), reports a 2017–2019 suspension of the US supplement that the others' wave lists contradict, and — the failure mode the prompt named — proposes static unique-subscriber divisors of 1.20, 1.15 and 1.08 *derived from periodic cross-checks* that it does not cite. Its inventory is not used here.

Two Korean dates on which the reviewers disagree are settled by the one that cites official indicator documentation: the age floor of the Internet Usage Survey moved from 7+ to 6+ in 2002 and to 3+ in 2006 (ChatGPT, verified), not in 2013 as GLM and Qwen recall. Pew's two mode breaks are both real — the migration to the American Trends Panel in the mid-2010s (GLM) and the move from telephone to web and mail in 2023 (Grok, ChatGPT).

## The verdict, which is unanimous

**A single thirty-year series does not exist. A thirty-year chain can be assembled, wave by wave, and the waves are not equal.** Every reviewer answers the one question this way; they differ only in how many waves they let in.

| Wave | Can it be carried as a measured three-country series? | On what |
|---|---|---|
| Mobile telephony | Yes, 1996 to about 2024 | ITU / World Bank `IT.CEL.SETS.P2`, subscriptions per 100; national contract counts as satellites |
| Fixed broadband | Yes, from about 1998–2000 to about 2024 | ITU / World Bank `IT.NET.BBND.P2` at ≥256 kbit/s; OECD Broadband Portal as the second source |
| Internet use, any access | Yes, from 1996 to about 2024, with a recall-window caveat | ITU / World Bank `IT.NET.USER.ZS`; national surveys as satellites, not substitutes |
| Smartphones | National surveys only, from about 2010–11; good for timing, not for levels | MIC household survey; Korea Internet Usage Survey; Pew adults |
| Social web | Three national series, not one indicator: US from 2005, Japan and Korea from about 2011–12 | Pew; MIC media-use survey; Korea survey SNS item with a changing platform list |
| Dial-up and bulletin boards | No. Fragments only | Japan and Korea: company membership counts (Nifty-Serve, PC-VAN, Hitel, Chollian) in print-era white papers; US BBS: does not exist as a measured quantity |
| Messaging | No official series anywhere | Japan LINE and Korea KakaoTalk items inside national surveys; US has no dominant platform and no official series |
| Generative AI | Three or four non-comparable annual points per country from 2023; no volume series | Japan MIC white-paper item; Korea Internet Usage Survey item; Pew *ever used ChatGPT*; plus vendor and telemetry estimates below |

The ITU / World Bank triplet is the only spine that is continuous, public, three-country and definitionally aligned by a single compiler. All seven name it; Grok and ChatGPT would make internet use the spine and everything else a satellite. Its licence is CC BY 4.0 with attribution to ITU. Its history is silently revised whenever a country resubmits, ITU and OECD do not always print the same number for the same country-year, and the ITU DataHub migration of 2023 changed series names — so a download is a *vintage*, and the date must be recorded (Claude, Grok, ChatGPT).

**Whether the earliest and latest waves can be carried at all is the disagreement that matters.** Four reviewers say dial-up and messaging cannot be carried as measured series and generative AI only as a post-2022 survey layer. Qwen and DeepSeek go further: a series across all seven waves would be, in DeepSeek's word, *dishonest* unless every splice and gap is marked. The round therefore returns [[technology-waves]]'s wave stack to the design with a division drawn through it — four waves measured, three not.

## The inventory, condensed

The national series the seven agree exist. Start years are the reviewers' consensus and remain `probable` until a table is opened; ChatGPT's stricter rule — record only what was verified — is the one to apply at collection.

**Japan.** The Communications Usage Trend Survey (通信利用動向調査, MIC, on e-Stat) — households from 1990, individuals from 1997 or 2001, smartphone item from 2010, SNS items from the early 2010s, a generative-AI item from FY2023; the survey archive on e-Stat runs 1996 to 2025 (ChatGPT). TCA carrier contract counts, monthly from a January 1996 archive, quarterly from about 2013–14 (ChatGPT verified the endpoints; 2014–16 did not resolve on the current site). MIC quarterly contract statistics from about 2004, covering mobile, PHS, BWA and fixed broadband by technology with no speed floor. The MIC media-use survey (情報通信メディアの利用時間と情報行動に関する調査) from FY2012 for platform-level use, ages 13–69. Japan's generative-AI item is a commissioned web panel, three points, 9.1% → 26.7% → 58.8%, and the 2026 edition added 15–19-year-olds, so the 20+ rate is 52.2% against the headline (Claude, live).

**Korea.** The Internet Usage Survey (인터넷이용실태조사, MSIT / NIA, national approved statistic 120005) from 1999 or 2000, ages 3+, use within the last month, with a publisher chain KRNIC → NIDA → KISA → NIA; the 2025 wave was published 31 March 2026 (Claude, live). MSIT monthly wireless and wired subscription statistics from the late 1990s, with IoT lines split from handsets from about 2014 and MVNO from about 2011. The KISDI Korea Media Panel from 2010. Korea's generative-AI item runs 33.3% (2024) → 44.5% (2025) on the ages-3+ survey — but two other official Korean surveys give 38.9% and 78.1% for 2025 on different universes, so *publishing one number labelled Korea gen-AI adoption 2025 would be a fabrication of comparability* (Grok).

**United States.** The NTIA / Census CPS Computer and Internet Use Supplement, irregular — 1994, 1997, 1998, 2000, 2001, 2003, 2007, 2009–2013, 2015, 2017, 2019, 2021, 2023 — households and persons aged 3+. The ACS internet questions from 2013, no standard 2020 release. FCC Form 477 from December 1999 to about 2021–22, connections over 200 kbps in one direction, replaced by the Broadband Data Collection in 2022, which measures availability rather than subscriptions. CTIA's wireless survey from 1985, whose *connections* include tablets, watches and machine lines. Pew fact sheets from 2000 (internet, home broadband), 2005 (social media), 2011 (smartphone), adults 18+, with the 2023 mode break. Pew's *ever used ChatGPT*: 18% → 23% → 34% → 44% across four annual waves to early 2026 (Claude, live).

**Generative AI beyond the surveys.** Microsoft's AI Diffusion Report is the only cross-country estimate: share of the population aged 15–64, modelled from Microsoft telemetry on PCs and tablets, adjusted for device share and internet penetration, at H1 2025, H2 2025 and Q1 2026 (Claude; ChatGPT verified two points). OpenAI Signals publishes downloadable data under CC BY 4.0 from July 2024 to June 2026, but as usage composition and per-capita message rankings, not deduplicated national user counts (ChatGPT). The Anthropic Economic Index gives relative indices for one vendor. OpenAI's weekly-active-user announcements are global and irregular. Similarweb and Sensor Tower cover all three countries behind paywalls with unstable definitions. The Census Bureau's Business Trends and Outlook Survey is the only high-frequency official AI series anywhere, and it measures firms.

## Definitions that do not match

The prompt called this the point of the exercise. The mismatches the seven agree on:

- **Subscriptions are not people.** Every supply-side series counts lines. Japan's include embedded communication modules and, historically, PHS and a separate BWA line that double-counts holders of both; Korea's include IoT lines until they were split out; CTIA's *connections* include every data device. Prepaid is negligible in Japan and Korea and substantial in the US, so ITU's active-within-three-months rule bites mainly there. A value above 100 per 100 is not an error and must not be capped or relabelled as adoption (ChatGPT).
- **Broadband has three speed floors and one of them keeps moving.** ITU and OECD use ≥256 kbit/s and have not changed it. The FCC collection floor is 200 kbps in one direction, and on top of it the policy benchmark moved to 4/1, 25/3 (2015) and 100/20 Mbps (2024), so a US *broadband adoption* number is a different object from the ITU number. Japan and Korea define broadband by technology — FTTH, DSL, cable — with no speed floor at all.
- **The recall window is four different windows.** Japan: used in the past twelve months. Korea: the past month. ITU: the past three months, which matches none of its national inputs before the late-2010s harmonisation. Pew: *at least occasionally*. NTIA: current use, reported by a household proxy.
- **The age floor is 6+, 3+ and 18+**, with OECD at 16–74 and Japan's NRC generative-AI panel at 20–69. Standardising across them shifts rates by several points (Gemini's 5–12% is an assertion, not a measurement).
- **Household, individual and adult are three bases.** Japan publishes household smartphone ownership near 90%, individual near 80%, and an operator institute's share of mobile owners at 97–98%; these cannot be plotted as one line (Grok). A household rate cannot be converted to an individual rate from household size alone (ChatGPT).
- **Social web and messaging are not one quantity.** Japan's SNS category includes LINE; Korea reports messenger and SNS separately, so a 65% SNS rate and a 98% KakaoTalk rate are answers to different questions; Pew's *any social media* depends on a platform list that grows. Adding platform percentages double-counts.
- **Generative AI has no shared question.** Ever-use, experience, use in the last three months, weekly, a named product, or *any AI service* including appliances are all in circulation. MIC's own US comparator, 68.8%, sits far above Pew's for the same period, which shows how much the mode and wording matter (Claude).
- **The population denominator itself revises** after each census — Japan 2015 and 2020, Korea 2015 and 2020, US 2010 and 2020 — which moves every per-100 series without any change in subscriptions (Grok).

## Breaks the round could source

Consolidated from the seven, keeping only breaks at least one reviewer sourced or that are standard in the series:

| When | Series | What changed |
|---|---|---|
| 2001, 2004 | Japan, all MIC series | Publisher MPT → MPHPT → MIC |
| 2002, 2006 | Korea Internet Usage Survey | Age floor 7+ → 6+ → 3+ (verified) |
| 2004 | Korea internet-use indicator | Criterion changed from average monthly use to use within the preceding month |
| 2008 | Korea survey | Renamed from 정보화실태조사; twice-yearly became annual |
| 2005, 2008, 2014 | FCC Form 477 | Threshold removed; tract-level, speed tiers and mobile added; further revision |
| 2010, 2015, 2024 | FCC | Broadband benchmark raised |
| about 2011, 2019 | Korea mobile lines | MVNO added; 5G added; IoT split from handsets about 2014 |
| 2013 | US | ACS internet questions begin; CPS supplement goes biennial |
| October 2013 | TCA | PHS and BWA reporting moved to quarterly (not cellphone reporting — ChatGPT's caution) |
| mid-2010s | Pew | Migration to the American Trends Panel |
| 2019 | Japan CUTS | Survey design change produced an anomalous jump; MIC advises caution across this year |
| 2020 | ACS | No standard one-year release |
| 2021–23 | Japan | PHS wound down and drops out of the counts |
| 2022 | FCC | Form 477 replaced by the Broadband Data Collection |
| 2023 | ITU | DataHub migration; series names and identifiers changed |
| 2023, 2024 | Pew | Telephone → web and mail → mixed |
| 2026 | Japan MIC generative-AI item | 15–19-year-olds added to the sample |

## The finding that changes a sentence

[[technology-waves]] says the institute marks *a vertical rule* where measurement stops and the model continues. The round's most consistent finding is that **the boundary is not one week and not one line.** Claude: *it is a different date for each technology and country; it is not one week.* ChatGPT: the last measured week *cannot yet be one universal date* — each input carries at least four dates (reference period, fieldwork, publication, revision), an annual observation does not create fifty-two weekly ones, extrapolation begins after the observation's reference coverage rather than its publication date, and interior gaps stay gaps even before the latest point. GLM: for generative AI, the *no longer measured* line sits almost immediately after *first measured*. Grok: after end-2024 or the 2025 survey, the series stops.

As of 20 September 2026 the last measured points Claude could verify are: Japan, the FY2025 survey published 24 July 2026; Korea, the 2025 survey published 31 March 2026; the US, Pew's early-2026 wave published 17 June 2026; Microsoft, Q1 2026. The ITU spine's last fully measured common year is 2024. And 1996–2026 is thirty-one annual labels over a thirty-year interval whose last year is not yet complete (ChatGPT).

The design consequence is not resolved here: either the chart carries one boundary per series, or the institute's methodology page states a rule for collapsing many boundaries into one published week. Recorded as open on [[technology-waves]].

## Normalisation — where the seven agree, and the choice they leave

The prompt asked for a rule precise enough to replicate. Seven rules came back, and on their principles they agree:

- **One spine per technology, never spliced.** Pick the ITU / OECD series where one exists, otherwise the national official survey, otherwise Pew; publish second sources beside it and never blend them in (Claude, GLM, Grok).
- **Date every observation at its true reference date**, not the label year — year-end for ITU, end of August for Japan's survey, fieldwork midpoint for Korea and Pew (Claude, ChatGPT).
- **Freeze one vintage and record the download date** (all).
- **No interpolation without a flag; no imputation; a missing year stays missing; pre-launch years are not zeroes** (Claude, GLM, Grok, ChatGPT). Anything finer than annual is a constructed value and must say so.
- **At a break, chain-link only with an overlap year; otherwise insert a gap marker** (GLM, DeepSeek).
- **Keep the observation record**: ChatGPT's schema — country, definition id, series id, reference start and end, population universe, unit, question and recall window, method, estimate flag, release, revision and retrieval dates, file hash, value — is the minimum that lets two people get the same numbers.

Where they differ is the scaling step, and the difference is a design choice rather than a fact:

| Rule | What it does | Who |
|---|---|---|
| Own-ceiling timing scale | Unbounded series divided by their own plateau, `D = min(1, x/S)`, with `S` the mean of the first three consecutive annual points changing under 2% | Claude |
| Declared ceilings | Fixed per-technology ceilings — mobile 130, others 100 — with age-band and adult-to-population conversions from UN population shares | GLM |
| Subscription density, uncapped | `100·C/P` with one population vintage; never capped, never relabelled as adoption; an age-standardised individual rate over five bands 20–69 where microdata allow, else NA | ChatGPT |
| First observation = 0, last = 1 | Within-country intensity index per technology; ITU internet use alone as the cross-country spine | Grok |
| Within-country z-score | Standard deviations from the country's own mean, cross-country levels explicitly forbidden | DeepSeek |

And on what survives any rule, the seven agree exactly: **within-country time paths are valid; cross-country timing is valid** — the dates a country crossed 10%, 50% and 90%, and the time from 10% to 90% (Claude); **cross-country levels at a point in time are valid only on the ITU / OECD indicators in harmonised years; cross-country social, messaging and generative-AI comparisons are invalid under every rule**, because arithmetic cannot repair a different question.

## What cannot be sourced, and why

- **BBS users in the US** — does not exist as a measured quantity.
- **PC-communication membership in Japan and Korea** — published as company counts in print-era white papers; not survey-based; not accessible to any reviewer.
- **A continuous dial-up series** — fragments from the FCC, MIC and company filings; nothing harmonised; the US pre-2000 record cannot be made annual honestly (GLM).
- **The social web before about 2005, and before about 2011 in Japan and Korea** — essentially unmeasured; platform MAUs by country are mostly unpublished; Meta reports the US with Canada; X stopped reporting after 2022.
- **US messaging** — no official series.
- **Generative-AI usage volumes by country** — sessions, tokens, MAU — held by vendors, unpublished; a sequence of announcements is not a series.
- **Anything at weekly frequency for persons** — does not exist in official statistics.
- **Unique mobile users, one person one count** — does not exist continuously anywhere.
- **The full ITU micro-history without a paid extract** — published but thinner on the public DataHub (Grok).
- **A complete 2026** — not yet measurable.

## Licences are not uniform, and one matters

World Bank WDI is CC BY 4.0 with attribution to ITU; OECD is CC BY 4.0 since 2024; US federal series are public domain; Japan's government statistics fall under Standard Terms of Use compatible with CC BY; Pew permits reuse with attribution and restrictions on wholesale republication; CTIA is proprietary; TCA's tables carry a copyright notice and are not an open-data licence (ChatGPT). **Korea's licence is edition-specific**: the 2024 Internet Usage Survey report is posted under KOGL Type 4 — attribution, no commercial use, no derivatives — while the 2025 results release is Type 1, attribution only (ChatGPT verified both; Grok flagged Type 4). For an index the institute publishes, that is a check to run per file, not a licence to assume.

## Refusals

Every reviewer but Qwen declined to reproduce historical values from memory; the compliant ones put almost no numbers in their tables at all, which is what the prompt asked. All declined to say what the index should do with the series. GLM and ChatGPT declined to certify any table they had not opened. None assessed the premise.

## Evolution — the spine was collected the same day

On the user's instruction the assistant retrieved the three WDI series for the three countries on 2026-09-20 — vintage 2026-07-13 — and registered the raw responses, a tidy CSV and a retrieval record, [[SRC-2026-09-20-wdi-spine-retrieval]]. Coverage matches what the round expected with two specifics the round could not give: Japan's mobile and fixed-broadband series end in 2023 in this vintage while every other series reaches 2024, and the API returns no estimate flags, so estimated and reported cells are indistinguishable here (the ITU DataHub, which carries the flags, returned 403). Japan's internet-use line falls from 91 in 2015 to 85 in 2023 in the raw data — the reconciliation problem Grok predicted, recorded and not adjusted. Portal checks in the same session confirmed the Korean age-floor dates (2002, 2006), the one-month window, the e-Stat edition run 1996–2025, and the per-posting Korean licence (Type 1 for the 2025 release, Type 4 for the 2024 report). Nothing is normalised and no proxy is selected.

## Related

- [[technology-waves]]
- [[data-sources]]
- [[DEC-007-standard-return-numeraire]]
- [[DEC-009-three-markets-and-convergence]]
- [[loop-simulation]]
- [[dataset-backtesting-survey]]
- [[factor-identification-review]]

## Sources

- [[SRC-2026-09-20-proxy-sourcing-prompt]] — [raw/documents/2026-09-20-proxy-sourcing-prompt.md](../../raw/documents/2026-09-20-proxy-sourcing-prompt.md)
- [[SRC-2026-09-20-proxy-sourcing-chatgpt]] — [raw/surveys/2026-09-20-proxy-sourcing-chatgpt.md](../../raw/surveys/2026-09-20-proxy-sourcing-chatgpt.md)
- [[SRC-2026-09-20-proxy-sourcing-claude]] — [raw/surveys/2026-09-20-proxy-sourcing-claude.md](../../raw/surveys/2026-09-20-proxy-sourcing-claude.md)
- [[SRC-2026-09-20-proxy-sourcing-deepseek]] — [raw/surveys/2026-09-20-proxy-sourcing-deepseek.md](../../raw/surveys/2026-09-20-proxy-sourcing-deepseek.md)
- [[SRC-2026-09-20-proxy-sourcing-gemini]] — [raw/surveys/2026-09-20-proxy-sourcing-gemini.md](../../raw/surveys/2026-09-20-proxy-sourcing-gemini.md)
- [[SRC-2026-09-20-proxy-sourcing-glm]] — [raw/surveys/2026-09-20-proxy-sourcing-glm.md](../../raw/surveys/2026-09-20-proxy-sourcing-glm.md)
- [[SRC-2026-09-20-proxy-sourcing-grok]] — [raw/surveys/2026-09-20-proxy-sourcing-grok.md](../../raw/surveys/2026-09-20-proxy-sourcing-grok.md)
- [[SRC-2026-09-20-proxy-sourcing-qwen]] — [raw/surveys/2026-09-20-proxy-sourcing-qwen.md](../../raw/surveys/2026-09-20-proxy-sourcing-qwen.md)
- [[SRC-2026-09-20-wdi-spine-retrieval]] — [raw/documents/2026-09-20-wdi-spine-retrieval.md](../../raw/documents/2026-09-20-wdi-spine-retrieval.md); the spine as retrieved
