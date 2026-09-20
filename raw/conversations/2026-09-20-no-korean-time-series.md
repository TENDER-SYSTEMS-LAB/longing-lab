# Conversation — No Korean time series to add

**Date:** 2026-09-20
**Participants:** user, assistant (Claude Fable 5.1, Claude Code session)
**Original language:** Korean

## Capture note

Machine-extracted from the same Claude Code session as the day's other records,
registered separately because a registered original is never edited. It begins
at the assistant's report on the 2025 microdata the user had fetched and ends
at the user's reply; the ingestion turn that followed is excluded because this
record was made inside it.

Boundary as in its predecessors: user and assistant messages verbatim, tool
invocations and their outputs, system reminders and invoked skill bodies
excluded.

The user statement here: the published rates by year that would date the
Korean smartphone and social-web waves are not available to add. It is a
statement about availability, not a design decision; the assistant's response
to it — which build is the working one, and a rule for when a wave may be
wired — is `llm-proposed`.

---

## Turn 1 — assistant

커밋 `65b9231`. 워킹트리 클린.

**저장**: `raw/documents/2026-09-20-nia-internet-usage-survey-2025-microdata.xlsx`(31.8MB, `user-originated`), 라이선스 스크린샷, 기록 문서. 등록 완료.

**파일 내용 — 시계열이 아님.** 2025년 한 해의 응답자 단위 마이크로데이터(가구 22,691·가구원 50,750, 가중치 `WT1`/`WT2`). 연도별 비율표가 아니라서 규칙상 파동 날짜 측정 불가(중점이 관측 안에 있어야 함).

**대신 2025년 한 점은 산출** (가중치 `WT2`, 만 3세 이상):
| 항목 | 3세+ | 16~74세 |
|---|---|---|
| 스마트폰 보유 | 96.8% | 99.8% |
| 최근 1개월 스마트폰 인터넷 이용 | 92.9% | — |
| 최근 1개월 SNS 이용 | 61.3% | 68.1% |
| 최근 1개월 인스턴트 메신저 이용 | 92.4% | — |

16~74세 SNS 68.1%는 OECD passthrough 2024년 66.1%와 맞음 — 같은 조사 항목.

**라이선스**: 이 파일은 **2유형**(출처표시·상업적 이용금지). 오늘 본 것만 세 종류(2025 발표문 1유형, 2024 보고서 4유형, 마이크로데이터 2유형). 게시물마다 다름 — 파일별 확인 규칙 재확인.

**아직 필요한 것 — 연도별 비율 시계열.** 한국 스마트폰·소셜웹 날짜를 측정하려면 이것 하나면 됨:
1. https://kosis.kr → 검색 `인터넷이용실태조사`
2. 통계표 중 「스마트폰 보유율」(또는 「휴대형 정보통신기기 보유율」), 「SNS 이용률」, 「인스턴트메신저 이용률」
3. 시점 「전체」 선택 → 「다운로드」 → xlsx 또는 csv
4. `raw/inbox/`에 넣어주면 같은 규칙으로 적합 → v6 빌드·재실행 → v5의 한국 placeholder 왜곡 제거.

로그인 불필요. 파일 3개면 됨. 세 항목이 한 표에 같이 있으면 그 하나로 충분.

---

## Turn 2 — user

시계열 데이터가 없어서 추가를 못해.
