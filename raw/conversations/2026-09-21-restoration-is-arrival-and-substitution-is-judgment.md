# Conversation — restoration counts as arrival; substitution counts judgment

**Date:** 2026-09-21
**Participants:** user, assistant (Claude Fable 5.1, Claude Code session)
**Original language:** Korean

## Capture note

Machine-extracted from a Claude Code session opened with the question what is
next. It begins at the user's choice to take up the ALS restoration question
first, asked with a request to explain what ALS is, and ends at the user's
decision turn; the ingestion turn that followed is excluded because this record
was made inside it. The opening what-is-next exchange is excluded as a routine
read of `wiki/current-state.md`.

Boundary as in its predecessors: user and assistant messages verbatim, tool
invocations and their outputs, system reminders and invoked skill bodies
excluded. The first user message switched a terse-style session rule to a
lighter level; the invocation text is kept because the message continues in the
same line. The assistant's replies were written under that rule; they are
reproduced as written.

The user decisions here: restoration counts as arrival; the substitution
channel counts substitution of judgment. The user then qualifies both in the
same turn — some execution has a restoring side (voicing, reading in a learned
voice), some execution is substitution because it hands over the deliberation
whole (the translated greeting), and the split may be ambiguous — and proposes
a per-security ontology fixing how much execution and judgment each security
involves and how exposed each is. The proposal is the user's, put as *should*,
not decided. The example table in the assistant's second reply and its two
decision points are assistant proposals.

---

## Turn 1 — user

/caveman:caveman lite
ALS 복원 AI = 도착인가, 대체 = 실행인가 판단인가 먼저 해보자. ALS가 일단 뭐야?

---

## Turn 2 — assistant

**ALS = 루게릭병** (Amyotrophic Lateral Sclerosis, 근위축성 측삭경화증). 운동신경세포가 점진적으로 죽는 병. 근육 마비가 퍼지고, 결국 말하기·삼키기·호흡 근육까지 잃음. 인지·판단은 대부분 끝까지 온전함. 즉 "할 말은 있는데 입이 안 움직이는" 상태.

어제(2026-09-21) 사용자가 든 사례: ALS로 말을 잃은 사람이 턱·입 운동신경 신호를 읽는 AI 디코더로 다시 "말하게" 됨. 사용자 질문은 "이건 낭만이 **증가**하는 방향 아닌가?" 결정 아니라 질문으로 기록됨.

이게 왜 문제인가:
- 현재 AI wave의 connection coefficient는 social web의 1/10. **대체(substitution) 효과만 보고** 설정됨. 복원 효과는 한 번도 셈에 안 들어감.
- 페이지의 두 phase는 "도착 = 새 연결 방법 생김", "대체 = 실천을 기계가 가져감". ALS 사례는 둘 다 아님. 병이 뺏은 길을 **되돌려줌**.

어시스턴트 제안 3개, 전부 `llm-proposed`, 미채택:
1. 복원과 대체는 두 기술 아니라 **한 기술의 두 행동**. 같은 음성 생성이 본인 말 실어주면 복원, 편지를 대신 써주면 대체.
2. **실행 대체 ≠ 판단 대체**. 합성기가 내가 고른 말을 소리 내주면 실행만 넘긴 것, 선택은 남음. substitution 채널이 어느 쪽 재는지 명시 필요.
3. 전제 재서술: "기술이 낭만을 뺏는다"에서 "기술은 할 수 있는 것을 넓히고, 이미 할 수 있던 것을 대신할 때만 가치를 줄인다"로. [[reflection]]의 사유 정의(본인 판단의 여지)와 연결.

결정할 것 두 개:
- 복원을 도착(arrival)으로 셀 것인가. Yes면 AI coefficient 재설정 필요.
- substitution이 재는 것이 실행인가 판단인가. 이게 정해져야 측정 설계([[data-sources]])로 넘어감.

---

## Turn 3 — user

복원을 도착(arrival)으로 센다는게 무슨 의미를 갖는가?
substitution이 재는 단위의 후보인 실행과 판단에 대한 각각의 예시 필요.

---

## Turn 4 — assistant

**1. 복원을 도착으로 센다는 것의 의미**

모델 구조상 "도착(arrival)"은 하나의 기계적 정의. [[DEC-008-bearer-bond-is-perpetual]]의 증권에서 **issuance(발행)를 올리는 것**. 사람이 서로에게 기대는 새 방법이 생기면 새 관계(채권)가 발행되고, 실천(practice)이 늘고, 시장이 오름. 반대로 substitution은 call(상환)을 올림. 혼자 할 수 있게 되면 관계가 끝남.

복원을 도착으로 센다 = 다음 네 가지가 따라옴:

- **AI wave의 issuance 곡선이 바뀜.** 지금 AI coefficient는 social web의 1/10. 이 숫자는 "AI는 대체만 하고 거의 아무도 연결 안 함"이란 이 작품의 유일한 AI 주장. 복원을 세면 그 주장이 깨지고 coefficient 재설정 필요.
- **AI wave도 상승 구간을 가짐.** 지금 시뮬레이션은 2010년 이후 모든 상승이 short covering. "세기의 전환이 매수가 시장을 올린 마지막 순간"이라는 결론이 [[loop-simulation]]에 있음. 복원 도착이 들어가면 AI 시대에도 실제 매수로 오르는 구간이 생길 수 있음. 30년 역사의 모양이 바뀜.
- **보이지 않는 peak의 위치가 옮겨짐.** 각 wave는 substitution이 arrival을 추월하는 주가 하나 있음. AI의 도착 효과가 커지면 그 추월 시점이 늦춰짐.
- **"도착"의 정의 자체가 넓어짐.** 지금은 "없던 연결 방법이 생김". 복원은 "있었는데 뺏긴 방법이 돌아옴". 둘 다 issuance 상승이지만 원인이 다름. 세면 정의를 "새 방법 또는 회복된 방법"으로 고쳐야 하고, 다른 wave도 복원 사례 있는지 다시 봐야 함(예: 인터넷 동창 찾기도 사실 "끊긴 관계의 복원"이었음. 페이지가 이미 그렇게 서술함).

안 세면: coefficient 유지, AI = 순수 대체 wave, ALS 사례는 예외로 기록만.

**2. substitution 측정 단위: 실행 vs 판단, 예시**

기준: 한 행위(act)마다 "주된 단계를 누가 했나"와 "내용·결정을 누가 했나"는 다른 질문.

| 행위 | 실행 대체 (execution) | 판단 대체 (judgment) |
|---|---|---|
| 편지 | 내가 쓴 초고를 AI가 맞춤법·문장 다듬음. 손은 넘겼고 할 말은 내 것 | "그 사람한테 사과 편지 써줘"로 AI가 내용·톤·사과할지 말지까지 결정 |
| ALS 음성 | 내가 고른 문장을 디코더가 소리로 냄. 발성만 넘김 | 디코더가 상대 말을 듣고 "적절한 답"을 자동 제안, 나는 승인 버튼만 누름 |
| 만남 약속 | 내가 정한 날짜·장소를 앱이 캘린더에 넣고 알림 | 앱이 "이 사람과는 이번 주 만나지 마세요"라고 판단, 나는 따름 |
| 안부 연락 | 내가 "요즘 어때"라고 보내고 AI가 번역 | AI가 연락 끊긴 사람 목록에서 누구에게 언제 연락할지 정하고 문구까지 생성 |
| 선물 | 내가 고른 책을 AI가 주문·배송 처리 | AI가 상대 취향 분석해 선물 고름, 나는 결제만 |
| 상대 이해 | 상대 편지를 AI가 큰 글자로 읽어줌(시각장애) | AI가 상대 편지를 요약하고 "이 사람은 지금 화났음"이라고 해석해줌, 나는 원문 안 읽음 |

규칙: 왼쪽 열은 "이미 할 수 없던 것을 다시 하게 됨" 또는 "손만 넘김"이라 [[data-sources]] 제안대로면 substitution으로 안 세거나 낮게 셈. 오른쪽 열은 "내가 할 수 있던 결정을 시스템이 함"이라 사유(본인 판단의 여지)가 줄어드는 쪽. 마지막 버튼을 내가 눌렀다는 것만으로 판단이 남았다고 볼 수 없음. [[data-sources]] 제안이 그래서 매 행위 옆에 "내용·결정이 누구 것인가"를 별도 기록하자고 함.

**결정 지점 두 개:**
- substitution 채널이 재는 것을 **판단 대체로 한정**하면: ALS 디코더, 번역, 확대 읽기 전부 substitution 아님. AI coefficient 자동으로 올라감. 실행 대체는 "관계에 무해"로 처리.
- **실행 대체도 셈**하되 판단 유지 여부를 통제 변수로 두면: [[data-sources]] 제안 그대로. 측정은 복잡해지지만 "손 넘긴 것 = 낭만 상실"로 오독하는 것을 막음.

어느 쪽이든 아직 결정 아님. 둘 다 `llm-proposed`.

---

## Turn 5 — user

복원을 도착으로 세고, substitution은 판단 대체를 셈하자.
근데 이것이 실행인지 판단인지 애매한 것들이 있지는 않을까?
실행을 모두 복원으로 볼 수 는 없지만 실행중 발성을 대신해주거나 다른 사람의 목소리를 학습해서 글을 읽어주는 것 같은것은 복원의 측면도 있어.
"내가 "요즘 어때"라고 보내고 AI가 번역" 하는 것은 사실 어떻게 안부를 보낼까 고민하는 과정 자체를 통으로 넘기는거라서 이런 실행은 또 대체로 카운트 해야할것 같아.
뭔가 종목별로 온톨로지를 분석해서 각각이 실행과 판단이 얼마나 적용되고, 그것이 각각 얼마나 노출되어 있는지를 꼼꼼하게 결정해야할 것 같아.
