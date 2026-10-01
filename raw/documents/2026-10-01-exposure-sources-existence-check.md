# Exposure sources existence check — 2026-10-01

**Type:** document (retrieval record)
**Retrieved:** 2026-10-01, by the assistant in a Claude Code session, on the user's instruction "5번 존재 확인부터 진행해" (work item 5 in `wiki/current-state.md`: narrow the exposure sources, starting by checking existence)
**Method:** web search, one or more queries per item; most verdicts rest on search-result titles and snippets, and one page (the Google Books Ngram corpus list) was opened directly. No dataset was downloaded. "Not found" means not found by these searches, not proven absent.
**Scope:** the ten series flagged as suspect in `wiki/concepts/exposure-sources-review.md` (Provenance warnings), plus twenty-six sources the review ranks as fewest-step or names across many files. The rest of the pool (roughly a hundred further rows across the twelve surveys) is unchecked.

Verdicts: **exists** — the holder publishes a series or document matching the claim; **exists, narrower** — something real stands behind the claim but with a shorter span, fewer markets or a different measure than claimed; **point only** — a single figure or study, not a series; **not found**.

## A. The ten suspect series

| # | Claimed (file) | Verdict | What was found |
|---|---|---|---|
| A1 | Japanese Google Books corpus, ~37/90 cells (GLM) | **not found** — does not exist | The Ngram Viewer's corpus list has English variants, Chinese (Simplified), French, German, Hebrew, Spanish, Russian, Italian. No Japanese or Korean corpus. https://books.google.com/ngrams/info |
| A2 | NHIS annual assistive-technology module 1996–2026 (Qwen) | **exists, narrower** | NHIS Assistive Device Supplement (1990) and the NHIS on Disability (NHIS-D), fielded 1994 and 1995 only. Not annual. https://archive.cdc.gov/www_cdc_gov/nchs/nhis/nhis_disability.htm |
| A3 | ASHA registry reporting a percentage of non-verbal patients restored to communication, 2000–2026 (Gemini v2) | **exists, narrower** | ASHA NOMS: a voluntary registry developed in 1997 that scores Functional Communication Measures at admission and discharge. No published annual "percentage restored" was found. https://www.asha.org/noms/ |
| A4 | Tobii Dynavox and Prentke Romich unit reports, US/JP/KR, 1996– (Qwen v2; Gemini) | **exists, narrower** | Tobii Dynavox annual reports exist from its 2021 listing. The 2022 report gives "more than 45,000" devices sold; 78% of 2023 revenue came from North America; no Japan or Korea split. DynaVox Inc. filed with the SEC 2010–2013. PRC-Saltillo is private. https://downloads.tobiidynavox.com/Web/Investor+Relations/Meetings/AGM_2024/Tobii_Dynavox_Annual_Report_2023_EN.pdf |
| A5 | Inmate digital messaging volumes from the Japanese and Korean justice ministries (Qwen v2) | **Japan not found; Korea exists, narrower** | Japan: no electronic-mail channel for detainees found; letters go by post. Korea: the Corrections Headquarters ran an "internet letter" service from 2005 to October 2023. Messages typed online were delivered to inmates on paper. Press reports give 4,302,265 internet letters in 2022, 48.2% of 8,940,940 letters received. Whether an annual series is published was not established. https://www.khan.co.kr/article/202311151716001 ; https://www.lawtimes.co.kr/news/articleView.html?idxno=197016 |
| A6 | ALS Association registry of AAC prescriptions 1996–2026 (Qwen) | **not found** | ALSA publishes guidance on communication options, not a registry. The nearest data is a one-off survey: OHSU 2021, 216 respondents, 54.6% owned a speech-generating device. https://www.ohsu.edu/sites/default/files/2023-01/REKNEW-A-Recent-Survey-of-Augmentative-and-Alternative-Communication-Use-and-Service-Delivery-Experiences-of-People-With-Amyotrophic-Lateral-Sclerosis-in-the-United-States.pdf |
| A7 | "NIPA Korean Language IT Usage Reports" on predictive word completion, 2010–2026 (Qwen) | **not found** | NIPA exists; no such report was found. |
| A8 | AI-generation transparency reports from Meta, LINE and Kakao giving message volumes (Qwen) | **not found** as described | Meta's Transparency Center reports counts of AI-labelled content (e.g. on Threads), not generated personal messages. Kakao's transparency report covers government data requests. https://transparency.meta.com/governance/tracking-impact/labeling-ai-content ; https://privacy.kakao.com/transparency |
| A9 | "National AAC & AT Utilization Database", 1996–2026 (Gemini v2) | **not found** | Nearest real sources: NATADS/CATADA (state AT programme activity, FY2013 onward; B7 below) and CMS DME aggregate tables. |
| A10 | A Japanese postal statistic separating handwritten correspondence (Gemini) | **not found** | Japan Post publishes New Year card volumes (B13). The Ministry of Internal Affairs ran a 2019 postal-use questionnaire covering frequency, not production method. https://www.soumu.go.jp/main_content/000602251.pdf |

## B. Core sources the review ranks high

| # | Source | Verdict | What was found |
|---|---|---|---|
| B1 | FCC TRS Fund minutes by service (US) | **exists** | The fund administrator (Rolka Loube) files annual reports with demand in minutes for six relay services, e.g. DA-21-556, DA-23-407, DA-26-516. First year of the minute series not established here. https://docs.fcc.gov/public/attachments/DA-26-516A1.pdf |
| B2 | Medicare speech-generating-device claims (US) | **exists**; the start-year conflict is resolved to **2001** | NCD 50.1: SGDs covered as DME effective 1 January 2001. Public aggregate tables by HCPCS exist (CMS DMEPOS); the first public year was not established here. https://www.cms.gov/medicare-coverage-database/view/ncd.aspx?ncdid=274&ncdver=2 |
| B3 | 電話リレーサービス (JP) | **exists**, from FY2021 | The Nippon Foundation Telephone Relay Service publishes annual business reports with monthly users, call counts and call time (FY2024 report). https://www.nftrs.or.jp/information/files/results/bpieb_R6houkoku.pdf |
| B4 | 손말이음센터 relay (KR) | **exists** (service since 2005); annual counts **not found** | https://107.relaycall.or.kr/user/center/intro |
| B5 | 補装具費支給, 重度障害者用意思伝達装置 (JP) | **exists, narrower** | 福祉行政報告例 on e-Stat carries 補装具 purchase and repair decisions (145,872 purchases in FY2021). The device-type breakdown is indicated but not opened. https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00450046&tstat=000001034573 |
| B6 | NIA 정보통신보조기기 보급사업 (KR) | **exists**; national annual counts **not found** | Local counts only (Seoul: 829, 840 and 659 recipients, 2023–2025). A press report says recipients over 12 years were about 2% of those eligible. https://news.seoul.go.kr/gov/archives/528004 ; https://www.mediatoday.co.kr/news/articleView.html?idxno=306008 |
| B7 | NATADS / CATADA (US) | **exists**, FY2013 onward | State AT programmes' annual progress reports: device loan, reuse, state financing. https://catada.info/ |
| B8 | USPS Household Diary Study | **exists** | Annual reports with a personal-correspondence table (Table 3.10) split into personal letters and holiday and non-holiday cards. Reports FY2010–FY2024 found. https://www.prc.gov/sites/default/files/uspsreports/USPS_HDS_FY13.pdf |
| B9 | Korea Post letter-post volumes | **exists**, 2006–2020 on data.go.kr | National approved postal statistics (21 kinds). The file covers 2006–2020; earlier years not established here. https://www.data.go.kr/data/15090572/fileData.do |
| B10 | 디지털정보격차 실태조사 (KR) | **exists** | Annual from 2002 for disabled, low-income, elderly and farming and fishing households; the gap index from 2004. https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=81623&bcIdx=27832&parentSeq=27832 |
| B11 | Greeting Card Association volume estimate (US) | **point only** | "About 6.5 billion cards a year", repeated from about 2012. It is not a series. https://www.greetingcard.org/wp-content/uploads/2019/09/Greeting-Card-Facts-09.25.19.pdf |
| B12 | Moonpig gift attach rate (UK) | **exists**, short series | 17.3% (FY24), 17.7% (FY25), 17.9% (FY26). UK market, outside the three. https://www.moonpig.group/media/t2lbafil/moonpig-group-plc-fy26-half-year-results-announcement.pdf |
| B13 | 年賀郵便 volumes (JP) | **exists** | Japan Post press releases each New Year. 491 million delivered on 1 January 2025; about 363 million reported for 2026. https://www.post.japanpost.jp/notification/pressrelease/2025/00_honsha/0101_01_01.pdf |
| B14 | Gmail Smart Reply share | **point only** | About 10% of Inbox mobile replies (Kannan et al., KDD 2016). https://arxiv.org/abs/1606.04870 |
| B15 | Anthropic Economic Index | **exists**, from 2025 | Directive automation rose from 27% to 39%; country-level data from the September 2025 release. https://www.anthropic.com/research/anthropic-economic-index-september-2025-report |
| B16 | OpenAI / NBER "How People Use ChatGPT" | **exists**, point study | NBER w34255: messages from May 2024 to June 2025; writing is dominated by editing, summarising and translating user text. https://www.nber.org/papers/w34255 |
| B17 | Liang et al., LLM-assisted writing across society | **exists**, 2022–2024 | About 18% of financial consumer complaints, 24% of corporate press releases and 14% of UN press releases LLM-assisted by late 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12745980/ |
| B18 | CoAuthor | **exists**, single dataset | 63 writers, 1,445 sessions with GPT-3 (CHI 2022). https://coauthor.stanford.edu |
| B19 | Willett et al. 2021, handwriting BCI | **exists**, single study | Nature 593:249–254. https://www.nature.com/articles/s41586-021-03506-2 |
| B20 | OHSU 2021 ALS AAC survey | **exists**, single survey | See A6. |
| B21 | Osaka 2024 AAC survey (Grok) | **not found** as named | Nearby: a nationwide survey of 780 Japanese ALS patients (J Neurol 2020), and a 2025 survey on ICT accessibility features among ALS patients. https://link.springer.com/article/10.1007/s00415-020-09903-3 |

## Not checked

The remaining rows of the twelve surveys were not checked, including the Japanese and Korean disability surveys, 通信利用動向調査, ITU indicators, patent classes, time-use surveys, card software vendors and e-card vendors. Most are national statistics or known products and the review did not flag them. Checking existence alone does not decide quantity or quality.
