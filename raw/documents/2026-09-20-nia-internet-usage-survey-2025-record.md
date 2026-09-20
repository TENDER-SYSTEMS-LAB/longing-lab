# Korea Internet Usage Survey 2025 — microdata received, one point measured

**Type:** document (retrieval and derivation record)
**Received:** 2026-09-20, from the user, downloaded by hand from data.go.kr dataset 15086936 (한국지능정보사회진흥원_인터넷이용실태조사 통계자료_20251231.xlsx, 31,817,915 bytes) after the session's own attempts returned zero bytes
**Licence, as the page showed it to the user:** 공공누리 **제2유형** — 출처표시, 상업적 이용금지 (attribution, no commercial use). Screenshot registered beside the file.
**Attribution:** jointly-developed — the user fetched the file and the licence; the assistant read it and derived the figures below

## What the file is

Four sheets: a household codebook (348 rows), a person codebook (2,572 rows), household microdata (22,691 households × 41 variables) and person microdata (50,750 persons × 362 variables), with survey weights `WT1` (household) and `WT2` (person). It is the **2025 wave only** — respondent-level records for one year, not a table of rates over years. It therefore supplies one measured point per item, not a series, and cannot date a wave under the calibration rule, which needs the midpoint to lie inside the observations.

The sample matches what the sourcing round's Claude response reported for the 2025 survey (22,671 households, 50,750 persons; the household count here is 22,691 rows).

## Weighted estimates derived from it

Person weight `WT2`, all persons aged 3 and over unless stated; weighted population 50,995,677.

| item | variable | definition | persons 3+ | persons 16–74 |
|---|---|---|---|---|
| smartphone ownership | `Y15_1_1`–`Y15_1_9` = 2 (휴대형 정보통신기기 보유현황, 스마트폰) | owns a smartphone | **96.8%** | 99.8% |
| used the internet on a smartphone in the last month | `Y10` = 1 | 최근 스마트폰 이용시기 1개월 이내 | 92.9% | — |
| SNS use in the last month | `Y19_1` = 1 | 최근 SNS 이용시기 1개월 이내 | **61.3%** | **68.1%** |
| instant-messenger use in the last month | `Y17_1` = 1 | 최근 인스턴트메신저 이용시기 1개월 이내 | 92.4% | — |

The 16–74 SNS figure, 68.1% for 2025, sits beside the OECD `D1B_I` value for Korea 2024 (66.1%) and 2023 (66.8%), which is the same survey item passed through; the three agree to within survey movement. The smartphone figure confirms that a Korean smartphone series, whenever it is obtained, will be near its ceiling by 2025.

## Licence note

This is the third KOGL type seen on this survey's postings in one day: Type 1 on the 2025 results release, Type 4 on the 2024 report, Type 2 on this microdata file. The licence attaches to the posting, not the survey. For an index the institute publishes, the rule from the sourcing round stands — read it per file.

## What it does not give

A time series. Dating the Korean smartphone and social-web waves needs the published rates by year — 스마트폰 보유율, SNS 이용률, 인스턴트메신저 이용률 — from KOSIS (statistic 120005) or from the annual reports. One point does not contain a midpoint.
