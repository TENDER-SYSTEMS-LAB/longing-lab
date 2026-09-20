# WDI spine retrieval record — 2026-09-20

**Type:** document (retrieval record)
**Retrieved:** 2026-09-20T08:07:50Z, by the assistant in a Claude Code session, on the user's instruction "spine 먼저 하자"
**Source vintage:** World Bank World Development Indicators, API response field `lastupdated` = **2026-07-13** for all three indicators
**Licence:** WDI is CC BY 4.0; the indicator metadata names the originator as the ITU World Telecommunication/ICT Indicators Database and asks that ITU be cited

This record documents what was retrieved, from where, with what coverage, and what was verified on the national portals in the same session. It does not select a proxy, apply a normalisation, or interpolate anything. The files it describes are registered as separate originals in `raw/sources.md`.

## Files

| File | What it is |
|---|---|
| `2026-09-20-wdi-IT.NET.USER.ZS.json` | Raw API response, byte-for-byte: Individuals using the Internet (% of population), JPN, KOR, USA, 1990–2026 requested |
| `2026-09-20-wdi-IT.CEL.SETS.P2.json` | Raw API response: Mobile cellular subscriptions (per 100 people) |
| `2026-09-20-wdi-IT.NET.BBND.P2.json` | Raw API response: Fixed broadband subscriptions (per 100 people) |
| `2026-09-20-wdi-spine.csv` | Tidy derivation of the three responses: one row per country × indicator × year, 324 rows, with the vintage and retrieval timestamp on every row |

Request URL pattern: `https://api.worldbank.org/v2/country/JPN;KOR;USA/indicator/<code>?format=json&per_page=1000&date=1990:2026`. Indicator metadata from `https://api.worldbank.org/v2/indicator/<code>?format=json`. The API returned no `obs_status` flags on any cell; estimates are therefore not distinguishable from reported values in this vintage, and the ITU DataHub itself (which carries estimate flags) returned HTTP 403 to the session.

## Coverage, as retrieved

*First* and *last* are the first and last years with a non-null value. *Gaps* are null cells inside 1996–2024.

| Indicator | Country | First | Last | Gaps 1996–2024 |
|---|---|---|---|---|
| `IT.NET.USER.ZS` internet use, % of population | JPN | 1990 | 2024 | none |
| | KOR | 1990 | 2024 | none |
| | USA | 1990 | 2024 | none |
| `IT.CEL.SETS.P2` mobile subscriptions per 100 | JPN | 1990 | **2023** | 2024 |
| | KOR | 1990 | 2024 | none |
| | USA | 1990 | 2024 | none |
| `IT.NET.BBND.P2` fixed broadband per 100 | JPN | 1998 | **2023** | 1996, 1997, 2024 |
| | KOR | 1998 | 2024 | 1996, 1997 |
| | USA | 1998 | 2024 | 1996, 1997 |

Nothing for 2025 or 2026 in any series. The last fully measured common year across all nine series is **2023**; 2024 is complete for seven of nine. The fixed-broadband series begins in 1998 everywhere, which is the indicator's own start, not a country gap.

Anchor values as retrieved (not rounded beyond the source):

| Indicator | Country | 1996 | 2000 | 2005 | 2010 | 2015 | 2020 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|
| internet use % | JPN | 4.37 | 29.99 | 66.92 | 78.21 | 91.06 | 90.22 | 85.01 | 85.54 |
| | KOR | 1.62 | 44.7 | 73.5 | 83.7 | 89.90 | 96.51 | 97.42 | 97.90 |
| | USA | 16.4 | 43.08 | 67.97 | 71.69 | 74.55 | 90.34 | 93.53 | 94.69 |
| mobile /100 | JPN | 21.40 | 52.57 | 75.43 | 96.18 | 126.15 | 154.43 | 178.43 | — |
| | KOR | 6.97 | 57.34 | 80.13 | 104.10 | 115.60 | 135.97 | 162.11 | 172.52 |
| | USA | 16.37 | 38.89 | 68.88 | 91.66 | 101.83 | 103.86 | 112.41 | 113.19 |
| fixed bb /100 | JPN | — | 0.67 | 18.22 | 26.60 | 30.54 | 34.84 | 38.63 | — |
| | KOR | — | 8.28 | 25.48 | 35.26 | 39.28 | 43.05 | 46.57 | 47.80 |
| | USA | — | 2.51 | 17.30 | 27.17 | 31.34 | 35.72 | 38.09 | 38.86 |

One thing visible in the raw values and expected from the sourcing round: Japan's internet-use series falls from 91.06 (2015) to 85.01 (2023). The sourcing round (Grok) warned that the WDI Japan internet line is jumpy relative to MIC's survey and that this is a reconciliation problem, not a real collapse in use. Recorded here; not adjusted.

## Definitions, from the indicator metadata

- **Internet use**: individuals who used the Internet from any location in the last three months, any device. National sources differ in recall window and age floor; WDI passes them through.
- **Mobile subscriptions**: postpaid subscriptions plus prepaid accounts active in the last three months, voice-capable; excludes data cards, USB modems, public mobile data, trunked radio, paging and telemetry. Multiple subscriptions per person count separately.
- **Fixed broadband**: fixed subscriptions at downstream speeds ≥256 kbit/s, including cable, DSL, fibre, other wired, satellite and terrestrial fixed wireless, excluding mobile-cellular data. The metadata's wording on wireless broadband is internally inconsistent in one paragraph, as the sourcing round (ChatGPT) noted.

## National portals verified in the same session

Checked by fetching each page on 2026-09-20; what follows is what the page text shows, not an audit of the underlying tables.

**Japan — e-Stat, 通信利用動向調査 archive** (`e-stat.go.jp/stat-search/files?toukei=00200356`, HTTP 200). Editions listed from 平成8年 (1996) through 令和7年 (2025); the page lists 29 edition labels and the 2019 edition's label was not captured by the pattern used, so the count is 29 or 30. The 令和7年 (2025) edition's publication/update date is **2026-05-29**; the 令和6年 edition's is 2025-05-30. The filter-by-survey-month list runs back to 1996. About 2,266 files in the archive.

**Korea — 지표누리, 인터넷 이용률** (`index.go.kr … idx_cd=1346`, HTTP 200). The indicator page states: internet use rate is the share of persons aged **3 and over** who used the Internet within the **last one month**; the survey population moved from 7+ to **6+ in 2002** and to **3+ in 2006**; the underlying survey is 인터넷이용실태조사, national approved statistic no. 120005; year selector runs 2000–2023. This confirms the dates the sourcing synthesis adopted from ChatGPT over GLM's and Qwen's recalled 2013.

**Korea — licences, edition by edition.** The MSIT posting of the 2025 survey results (`nttSeqNo=3187098`, HTTP 200) displays **공공누리 제1유형** (attribution). The MSIT posting of the 2024 full report (`nttSeqNo=3173673`, HTTP 200) displays **공공누리 제4유형** (attribution, no commercial use, no derivatives), and the page carries a 정정 (correction) notice. The data.go.kr fixed-service dataset page (`data/15070091`, HTTP 200) shows a KOGL link and modification dates 2020-10-22 and 2025-07-31; its type marker was not in the page text as fetched. The sourcing round's finding stands: the Korean licence must be read per file.

**United States — NTIA dataset page** (`ntia.gov/page/download-ntia-internet-use-survey-datasets`, HTTP 200). The page is script-rendered; the fetched text names July 2011, July 2013 and July 2015 waves and nothing else. The wave list in the sourcing synthesis is not re-verified by this fetch.

**ITU DataHub** (`datahub.itu.int`): HTTP **403** to the session. The WDI republication is the accessible route; the DataHub's estimate flags and any post-2024 points were not obtained.

## What this record does not do

No interpolation, no smoothing, no normalisation, no capping, no selection among the three indicators as *the* driver, no substitution of a national series for a WDI cell, and no claim about 2025 or 2026. The measurement edge these files establish is 2023 for all nine series together and 2024 for seven of them.
