# National series retrieval record — smartphones and the social web, 2026-09-20

**Type:** document (retrieval record)
**Retrieved:** 2026-09-20, by the assistant in a Claude Code session, on the user's instruction to fetch the smartphone and social-web national series and date those waves under the same rule as mobile and broadband
**Attribution:** jointly-developed — the user asked for the series; the assistant chose where to get them and what to record

The sourcing round said smartphones and the social web exist only as national surveys, good for timing and not for levels. This record says which of those surveys the session could actually reach, what each measures, and what it could not reach. Nothing here is normalised or interpolated; the files are the responses as received, with one derived subset.

## Files registered

| File | What it is | Source and reuse |
|---|---|---|
| `2026-09-20-pew-mobile-phone-ownership-chart4746.csv` | Pew Research Center chart data, *Mobile phone ownership*, % of U.S. adults who own a cellphone / smartphone, dated survey points 2002–2025; smartphone from 2011-05-22 | `pewresearch.org/wp-json/prc-chart-builder/v1/charts/4746/data.csv`, from the Mobile Fact Sheet. Pew terms: reuse with attribution, restrictions on wholesale republication |
| `2026-09-20-pew-social-media-platforms-chart4749.csv` | Pew chart data, *Which social media platforms are most popular*, % of U.S. adults who ever use each named platform, 2012–2025 | chart 4749, Social Media Fact Sheet. Retrieved and registered; **not used for dating** — platform-specific, and Facebook is already at 54% at its first point |
| `2026-09-20-pew-social-media-use-over-time-2015.csv` | Twelve dated points, Feb 2005 – Jul 2015, **% of internet users** who use social networking sites, transcribed from the text of Pew's chart page *Social Media Use Over Time* (report dated 2015-06-10) | `pewresearch.org/internet/chart/social-media-use-over-time/`. The page exposes the series only as text; no data endpoint was found. The base is internet users, not adults |
| `2026-09-20-mic-r06-f00308-household-device-ownership.csv` | MIC, 令和6年版情報通信白書 data collection figure f00308, 情報通信機器の世帯保有率の推移: household ownership rates 1999–2023 by device; smartphone column from 2010 | `soumu.go.jp/johotsusintokei/whitepaper/ja/r06/csv/f00308.csv`, Shift-JIS as served, `@Date` 2024-07-05. Government of Japan Standard Terms of Use |
| `2026-09-20-mic-r06-f00310-internet-use-individuals.csv` | MIC white paper figure f00310, インターネット利用率（個人）の推移, 1997–2023 | same collection. A check series beside WDI's Japan internet line, not wired |
| `2026-09-20-oecd-ict-individuals-D1B_I-social-networking.csv` | The 828 rows for measure `D1B_I` — *Individuals using the internet for accessing social networking sites, last 3 months* — extracted from the OECD dataflow `OECD.STI.DEP:DSD_ICT_HH_IND@DF_IND(1.1)` for JPN, KOR, USA, all breakdowns | Full pull `sdmx.oecd.org/public/rest/data/OECD.STI.DEP,DSD_ICT_HH_IND@DF_IND,/KOR+JPN+USA.........`, CSV with labels, 16,080,855 bytes, SHA-256 `7405c284f28b309e7d233cba72b379f76589d93caf7e46c3d293589df1e151f7`, 36,937 rows; not committed for size, the subset is. OECD terms, CC BY 4.0 |

The total-population rows of `D1B_I` (ages 16–74, all sexes, all education, all income, all employment) are:

| country | years | first | last | status flag |
|---|---|---|---|---|
| JPN | 2012–2024 | 39.8 | 84.6 | D (definition differs) throughout |
| KOR | 2005–2024 | 37.9 | 66.1 | D to 2020, A from 2021 |
| USA | 2015, 2017, 2019, 2021, 2023 | 56.8 | 68.0 | D |

The OECD series is each country's own survey passed through — Japan's is MIC's SNS item, in which LINE counts as SNS; Korea's is the Internet Usage Survey item — so the D flag is the definitional mismatch the sourcing round described, in one file.

## What could not be reached

- **Korea, data.go.kr file dataset 15086936** (한국지능정보사회진흥원_인터넷이용실태조사 통계자료_20251231.xlsx, catalogue modified 2026-04-27). The page's download runs through a limit-check and a `fileDownload.do` call; reproducing it returned JSON metadata and then a zero-byte body. Not obtained.
- **Korea, MSIT postings.** The 2025 results release carries a `.hwp` attachment and the 2024 report a `.zip`; neither was parsed. The pages carry no time-series table in their text.
- **Korea, KOSIS.** A guessed table id returned the portal's error page; the API needs a key.
- **Korea, 지표누리.** No smartphone or SNS indicator was found by search or by probing neighbouring ids of the internet-use indicator.
- **Korea smartphone ownership, any source.** Not obtained. The OECD individuals dataflow carries no smartphone or mobile-device measure for Korea.
- **Japan SNS time series from MIC's own publications.** The 2024 and 2025 white-paper data collections (257 and 246 CSVs, all downloaded and their captions read) contain SNS snapshots by age and disaster-information items, not a usage-rate trend. The media-use survey (情報通信メディアの利用時間と情報行動に関する調査) publishes one Excel per year from 2012; those were not opened. The OECD `D1B_I` row for Japan stands in.
- **Pew, any-social-media as % of adults over time.** The fact sheet now carries platform series only; the 2005–2015 series is on the internet-user base.
- **ITU DataHub**: still 403.

## Definitions, as they bear on dating

- US smartphone: adults 18+, ownership, self-report, telephone to 2021 then web and mail. US social web: **internet users**, not adults, 2005–2015; the base was roughly 70–85% of adults over that span, so the population-based curve sits lower and its midpoint slightly later.
- Japan smartphone: **households** owning at least one, 6+ respondents, year-end reference. A household rate saturates earlier than an individual rate.
- Japan social web (OECD): individuals 16–74, last three months, LINE counted; begins in 2012 at 40%.
- Korea social web (OECD): individuals 16–74, last month in the national survey; begins in 2005 at 38%, plateaus near 66–69% and dips — the series does not contain its own midpoint.
