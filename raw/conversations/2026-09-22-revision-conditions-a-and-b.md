# Conversation — revision conditions are (a) and (b); two round prompts requested

**Date:** 2026-09-22
**Participants:** user, assistant (Claude Fable 5.1, Claude Code session)
**Original language:** Korean

## Capture note

Machine-extracted from the same Claude Code session as
`2026-09-21-weights-sum-to-one-and-conditional-revision.md`, registered
separately because a registered original is never edited. It begins at the
assistant's reply to that record's last turn — the ingestion report and three
next items — and ends at the user's answer; the ingestion turn that followed,
in which the two prompts were drafted, is excluded because this record was made
inside it. The prompts are registered as documents of their own.

Boundary as in its predecessors: user and assistant messages verbatim, tool
invocations and their outputs, system reminders and invoked skill bodies
excluded. The assistant's reply was written under a terse-style session rule
and is reproduced as written; its wiki links are as printed. The user's
message arrived after midnight and carries this record's date.

The user decision here: a security's weights may be revised under the
assistant's conditions (a) — the security's own definition changes — and (b) —
the same security's weights disagree across the three markets; condition (c),
a residual threshold in the generated record, is rejected. The user also
requests drafts of the two round prompts and states they will run each prompt
themselves and bring the responses into the wiki as before. The three
candidate conditions and the note on (c)'s circularity are the assistant's.

---

## Turn 1 — assistant

기록 완료, 커밋 `4b95965`. [DEC-014](wiki/decisions/DEC-014-restoration-is-arrival-and-substitution-is-judgment.md) 두 번째 evolution.

- **결정(`user-confirmed`)**: 비중 = 합 1인 한 쌍. 개정 가능하되 사전에 정한 조건 충족 시에만.
- **사용자가 정한 절차(결과 미정)**: 비중 설정 절차 → LLM 의견 수집 후 사용자 최종 판단. 노출 출처 → 넓게 수집 후 양·질로 추림.
- current-state next steps에 작업 항목 4, 5로 등록.

**다음에 필요한 것, 의존성 없는 순서:**

1. **개정 조건 후보.** 조건 없이는 "개정 가능"이 "맘대로"와 구분 안 됨. 후보 셋: (a) 종목 정의 자체가 바뀔 때(실천의 단계가 추가·삭제), (b) 다른 시장에서 같은 종목의 비중이 어긋날 때(DEC-009 세 시장), (c) 생성된 기록에서 비중이 설명 못 하는 잔차가 임계 이상일 때. (c)는 데이터 순환 위험 있음 — 비중을 결과에 맞추는 것. 이건 사용자 결정.
2. **LLM 라운드 프롬프트 초안** (작업 4). 필요한 것: 질문 문안, 고정 컨텍스트(DEC-014 전체, 합 1 규칙, 개정 조건 결정 여부), 응답 형식. 지금 쓸 수 있음. 어느 모델 셋에 돌릴지는 이전 라운드 관행(7모델) 따르면 됨.
3. **노출 출처 브레인스토밍 프롬프트 초안** (작업 5). 2번과 별개 라운드로 돌려야 함 — 하나에 섞으면 응답 질 떨어짐. 필요한 것: 종목 하나를 예시로 고정(LETTER), 실행 복원 노출·판단 대체 노출 각각에 "어떤 데이터가 시대별로 존재하는가"만 묻기, 양·질 평가는 수집 후.

2와 3은 서로 독립, 1은 사용자 답이 필요. 초안 둘 다 지금 쓸까, 아니면 1번 먼저 정할까.

---

## Turn 2 — user

1. 개정 조건은 (a)랑 (b)로 가고 (c)는 빼자
2. LLM 라운드 프롬프트 초안 작성해줘.
3. 노출 출처 브레인스토밍 프롬프트 초안 작성해줘.


각 프롬프트는 내가 직접 돌려서 지금까지 해오던대로 wiki에 넣어줄게/
