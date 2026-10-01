# Conversation — weights first; securities later, after ontology deliberation

**Date:** 2026-10-01
**Participants:** user, assistant (Claude Opus 5.5, Claude Code session)
**Original language:** Korean

## Capture note

Recorded inside the Claude Code session that produced
`raw/documents/2026-10-01-exposure-sources-existence-check.md`. The record
starts with the user's question, which arrived while the assistant was running
the existence check. It continues with the assistant's report and answer and
ends with the user's decision. The session's earlier turns (what to do next,
the instruction to begin the existence check) and the turn that made this
record are excluded.

Boundary as in earlier records: user and assistant messages verbatim; tool
invocations, their outputs and system reminders excluded. The assistant's reply
was written under a terse-style session rule and is reproduced as written,
including its wiki links.

The user decision here: commit the existence check, decide the weight-setting
procedure (work item 4) first, and decide the securities later. The user says
choosing securities needs deliberation about the ontology, because securities
carry a very important part of the work, and so they must be chosen with great
care. The argument for more securities than LETTER, the two cautions and the
candidate practices (CALLING, face-to-face conversation, shopping in person,
wayfinding) are the assistant's. None of them is adopted.

---

## Turn 1 — user

LETTER 말고도 다른 여러 종목들을 만들어야 시대별 노출도를 확인할 수 있지 않을까?

---

## Turn 2 — assistant

36개 항목의 존재 확인을 마치고 위키에 기록했습니다. 대상은 의심 시계열 10개와 상위 출처 26개입니다. 아직 커밋하지 않았습니다.

**존재 확인 결과**
- **존재하지 않음:** GLM이 셈한 일본어 Google Books 코퍼스는 없습니다. Ngram Viewer에 일본어·한국어 코퍼스가 아예 없습니다.
- **찾지 못함 (4개):**
  - ALS Association AAC 레지스트리
  - "NIPA" 자동완성 보고서
  - Meta·LINE·Kakao의 AI 생성 메시지 투명성 보고서
  - "National AAC & AT Utilization Database"
- **실재하지만 주장보다 좁음:**
  - NHIS 보조기기 문항은 1990년과 1994–95년에만 조사됐습니다. 매년이 아닙니다.
  - ASHA NOMS에는 "회복 비율"이 공표되지 않습니다.
  - Tobii Dynavox 보고서는 2021년 상장 이후분만 있고, 한국·일본 분리가 없습니다.
  - 손글씨를 구분하는 일본 우편 통계는 없습니다.
- **기존 경고 정정:** 한국 수용자 인터넷 서신은 실재했습니다. 2005–2023년 운영됐고, 2022년 430만 건으로 수신 편지의 48.2%였습니다. 온라인으로 타이핑하고 종이로 받는 편지라 LETTER에 특이한 사례입니다.
- **시작 연도 충돌 해결:** Medicare SGD 보장은 1996년이 아니라 2001년부터입니다.
- **상위 출처는 대부분 존재합니다.** 예외:
  - 연하카드 협회(GCA)의 65억 장, Smart Reply의 10%는 시계열이 아니라 단발 수치입니다.
  - 손말이음센터와 NIA 보조기기 보급사업은 전국 연도별 건수를 찾지 못했습니다.
- **남은 일:** 풀의 나머지 약 100행은 미확인입니다. 양·질 채점도 시작하지 않았습니다.

변경 파일:
- [raw/documents/2026-10-01-exposure-sources-existence-check.md](raw/documents/2026-10-01-exposure-sources-existence-check.md) (신규, 등록함)
- [exposure-sources-review.md](wiki/concepts/exposure-sources-review.md)
- current-state, index, log

---

**LETTER 외 종목 질문: 맞는 방향이라고 봅니다.** 이유는 세 가지입니다.

1. **LETTER는 측정이 가장 어려운 종목입니다.** 이번 확인에서 실재가 확인된 출처는 말하기, 통화, 타이핑을 회복시킵니다. 손글씨는 아닙니다. 예를 들어 중계 서비스 분량은 CALLING의 execution 회복을 바로 보여주지만, LETTER에서는 3–5단계 추론이 필요합니다. 데이터가 직접 닿는 종목이 있어야 노출도에 실측 근거가 생깁니다.
2. **한 종목으로는 시대 효과와 종목 효과를 분리할 수 없습니다.** 같은 시대의 같은 기술이 여러 종목을 함께 움직이는지 봐야 공통 성분이 보입니다. DEC-005(팩터 수는 종목 수에 비례)와도 같은 방향입니다.
3. **판단 대체 쪽 데이터도 다른 종목에 더 맞습니다.** Smart Reply, AI 사용량 데이터는 이메일과 메시지를 관측합니다. 손편지가 아닙니다.

**주의할 점 두 가지:**
- **편향:** 데이터가 있는 실천만 골라 종목을 만들면, 종목 구성 자체가 측정 가능성 쪽으로 쏠립니다. 작품의 주제는 사라지는 것, 즉 기록되지 않는 것인데 반대 방향입니다.
- **선행 조건:** 종목을 정의하면 가중치 쌍도 정해야 합니다. 그래서 4번(가중치 설정 절차)의 결정이 먼저 필요합니다.

**추천 방법:** 후보 실천 목록을 먼저 뽑고, 각 후보에 대해 "어떤 데이터가 닿는가"를 지금 확인한 출처로 매핑합니다. 후보 예시는 CALLING, 대면 대화, 직접 장보기, 길 찾기 등입니다. 정의는 아직 하지 않고, 그 표를 보고 종목을 결정하시면 됩니다.

이 방향을 결정으로 기록할지, 후보 매핑 표부터 만들지 정해 주세요. 지금 변경분을 커밋할까요?

---

## Turn 3 — user

커밋하고 4번 가중치의 결정을 먼저하고 종목은 나중에 결정하자.
종목은 온톨로지에 대한 고민이 필요해보여. 작품에서 아주 중요한 부분을 담담하고 있기 때문에 종목은 아주 신중하고 고심해서 결정해야해.
