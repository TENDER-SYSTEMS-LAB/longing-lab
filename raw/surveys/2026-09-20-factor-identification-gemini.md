엄밀한 계량경제학적 조건 분석과 상위 조건(스텝별 검증, 불확실한 정보 구체화, 감정 및 이모티콘 배제)에 따라 작성을 진행합니다.

---

## Section 1 — The identification frontier

33개 자산(3개 시장 × 11개 관행), 1,565개 주차 관측치 기준 식별 가능성 분석:

### 1. 최대 식별 가능 요인 수 및 성립 조건

* **최대 식별 가능 요인 수**: 이론적 상한은 단일 시점 단면 관측치 수인 $N=33$ 미만($K < 33$)입니다. 공분산 행렬의 식별 및 추정 안정성을 고려할 때 통계적 유의성을 지니는 최대 요인 수는 계절성 및 시차 변수를 제외할 때 **22개 내외**로 제한됩니다.
* **성립 조건**: 요인 로딩 행렬(Factor Loading Matrix) $\mathbf{\Lambda}$가 Full Column Rank($\text{rank}(\mathbf{\Lambda}) = K$)를 유지해야 하며, 특유 오차(Idiosyncratic Noise) 간의 횡단면 상관관계가 0에 수렴해야 합니다($\text{Cov}(\epsilon_i, \epsilon_j) = 0, i \neq j$).

### 2. 식별 원천별 구분

* **단일 시장 내 횡단면 식별 요인**: 동일 시장 내 11개 관행 간 차이에서 식별됩니다. 시장별로 최대 $11 - 1 = 10$개의 독립적 직교 요인을 식별할 수 있습니다.
* **교차 시장(Cross-market) 식별 요인**: 동일 관행의 3개 시장 간 시차(Arrival phase 시간차) 및 강도 차이에서 식별됩니다. 관행당 최대 $3 - 1 = 2$개의 시장 특화 요인을 식별할 수 있으며, 11개 관행에 대해 총 22개 요인이 식별 대상이 됩니다.
* **시계열 전용 식별 요인**: 33개 자산 전체에 동시 적용되는 시계열 변화(예: Numeraire 가치 변화, 전 지구적 기술 수용)입니다. 단일 공통 트렌드로만 식별되며, 완만하게 움직이는 다른 대역 외 변수와 식별 불가능(Confounded)합니다.

### 3. 바인딩 제약 조건 (Binding Constraint)

* **바인딩 제약**: **교차 시장 식별 제약**이 가장 결정적인 제약으로 작용합니다.
* **이유**: 관행 단위(11개)는 고정되어 있으며, 시장 수(3개)가 적어 시장 간 자유도가 제한적입니다. 특히 이력 후반부로 갈수록 기술 파동의 동기화로 인해 교차 시장 독립 변동성(Cross-market variation)이 소멸하므로, 식별 가능 집합의 크기를 결정짓는 주요 제약이 됩니다.

---

## Section 2 — What the three-market structure buys, exactly

### 1. 구조적 분리 가능 조건

* **성립 조건**: 미·일·한 3개국의 기술 파동 도달 시점 차이($\Delta t_{\text{arrival}} > 0$)로 인해 관행별 수익률 간 상호 correlation이 낮은 구간($r \approx 0.2$)에서 성립합니다. 이 시기에는 각 국의 고유 제도, 인프라 보급 시차로 인해 $\mathbf{\Lambda}_{\text{local}}$과 $\mathbf{\Lambda}_{\text{common}}$ 간의 직교성이 확보됩니다.

### 2. 수렴(Convergence) 시 식별 파괴

* **실패 조건**: 이력 후반부 상관계수가 $r \approx 0.9$로 상승함에 따라 시장 간 독립 변동성이 소멸합니다.
* **식별 파괴 시점**: 3개 시장 간 관행별 기술 대체율의 시차 및 편차가 통계적 오차 범위 내로 축소되는 시점(상관계수 $r \ge 0.85$ 도달 시)에 교차 시장 요인의 식별이 불가능해집니다.
* **결과**: 공통 요인(Common Factor)과 지역 요인(Local Factor) 간 다중공선성(Multicollinearity)이 극대화되어 행렬 $\mathbf{\Lambda}^T \mathbf{\Lambda}$의 역행렬 존재 조건이 무너지며, 지역 요인은 idiosyncratic noise와 구별되지 않고 흡수됩니다.

---

## Section 3 — The nine lines

초기 대장(Opening Ledger)이 지지하는 요인 라인 도출:

### 1. 초기/후반부 식별 가능 요인 수

* **초기 (1996 ~ 상관계수 상승 전)**: 최대 **11개 ~ 14개** 요인 식별 가능.
* **후반부 (상관계수 $r \ge 0.85$ 이후)**: **5개 ~ 6개** 요인으로 축소.
* **9개 라인 도출 유효성**: 초기 환경에서는 9개 라인 설정이 계통적으로 방어 가능하나, 후반부에는 9개 유지 불가.

### 2. 요인 라인 구성 (초기 9개 기준)

1. **Global Substitution Trend**
* **구분 관측치**: 33개 자산 전체의 공통 하락 트렌드.
* **자산 및 부호**: 33개 자산 전체 (-).
* **식별 불가 조건**: Numeraire 가치 상승률과 기술 대체 속도가 완전히 일치할 때.


2. **US Arrival Lead Factor**
* **구분 관측치**: 미국 시장 선행 기술 파동 자산의 선행 변동성.
* **자산 및 부호**: US 11개 자산 (+), JP/KR 시차 반영 (0 내지 -).
* **식별 불가 조건**: US, JP, KR 간 기술 도입 시차가 0에 수렴할 때.


3. **Asia Adoption Lag Factor**
* **구분 관측치**: 한·일 시장 내 인프라 적응 시차로 인한 수명 연장 변동.
* **자산 및 부호**: JP/KR 자산 (+), US 자산 (0).
* **식별 불가 조건**: 한·일 시장의 기술 수용 속도가 미국과 동기화될 때.


4. **Synchronous Physicality Factor**
* **구분 관측치**: 물성/실체성을 갖는 관행(편지, LP, 필름)의 집단 변동.
* **자산 및 부호**: 물성 기반 관행 5개 (+), 비물성 관행 6개 (-).
* **식별 불가 조건**: 디지털 대체재의 물성 재현 기술이 완벽히 가동될 때.


5. **Asynchronous Spontaneity Factor**
* **구분 관측치**: 약속 없는 방문, 무작위 통화 등 즉흥성 기반 관행 변동.
* **자산 및 부호**: 즉흥성 관행 3개 (+), 계획성 관행 8개 (-).
* **식별 불가 조건**: 통신 인프라 점유율 변동과 완벽히 동기화될 때.


6. **Solitude / Reflection Factor**
* **구분 관측치**: 혼자만의 시간, 고독, 방랑 등 비연결성 관행 변동.
* **자산 및 부호**: 고독/성찰 관행 3개 (+), 타인 상호작용 관행 8개 (-).
* **식별 불가 조건**: AI 매개 대화형 서비스 도입으로 비연결 개념이 모호해질 때.


7. **Local Japan Float Decay Rate**
* **구분 관측치**: 일본 시장 특화 유동주의(Float) 소멸 지연.
* **자산 및 부호**: JP 11개 자산 (+), 타 시장 (0).
* **식별 불가 조건**: JP 시장 내 유동주의 상환율이 타 시장과 동일해질 때.


8. **Local Korea Mobile Shift Speed**
* **구분 관측치**: 한국 시장 특화 모바일 급증/대체 속도.
* **자산 및 부호**: KR 11개 자산 (-), 타 시장 (0).
* **식별 불가 조건**: 한국의 모바일 전환율 변동성이 글로벌 평균에 흡수될 때.


9. **Reflexive Liquidity Premium**
* **구분 관측치**: 대장 공표 및 연구소 리포트 발간 직후 발생하는 가격 되돌림/재귀적 변동.
* **자산 및 부호**: 전체 33개 자산 (주차별 유동성에 따라 +, - 전환).
* **식별 불가 조건**: 시장 참가자들의 거래 반응이 완전 무작위화(Random Walk)될 때.



---

## Section 4 — The promotion schedule

선언되었으나 미가격화된 요인(Declared-but-unpriced factor)을 가격화 라인(Priced line)으로 승격하기 위한 검증 가능 규칙:

### 승격 검증 시험 (Test Specification)

요인 Candidate $F_k$에 대해 지난 $T_{window} = 52$주(1년) 데이터를 바탕으로 다음 조건을 동시에 충족할 때 승격합니다.

1. **잔차 직교성 및 유의성 검정**: 기존 $K$개 요인으로 회귀분석한 잔차 $\mathbf{e}_t$에 대해, Candidate $F_k$의 회귀 계수 $b_k$가 통계적으로 유의해야 함.

$$t\text{-statistic}(b_k) > 2.58 \quad (p < 0.01)$$


2. **자산 최소 로딩 제약**: 최소 3개 이상의 자산에서 해당 요인에 대한 로딩 $\vert{}\lambda_{i, k}\vert{} > 0.35$를 유지해야 함 (단일/쌍 자산 특유 효과 배제).
3. **분산 설명력(Incremental $R^2$) 제약**: $F_k$ 추가 시 대장 전체 설명력 상승분 $\Delta R^2 \ge 0.05$ (최소 5% 이상 추가 설명).

---

## Section 5 — What this universe cannot identify

현재 상장 자산(33개) 구조상 **절대 식별 불가능한 요인** 및 상장 변경 대안:

1. **Intra-Individual Isolation vs. Social Apathy**
* **내용**: 개인의 자발적 고독 선호 증가와 사회적 무관심/고립화 현상 간의 구분.
* **혼동 원인**: 고독, 성찰, 무작위 밤산책 자산의 하락/상승 패턴이 두 요인에서 동일하게 나타남.
* **상장 변경 대안**: 집단적 고독 관행(예: 조용한 시위, 묵언 공간 이용) 자산 추가 상장.


2. **AI Numeraire Value Shift vs. Global Utility Collapse**
* **내용**: Numeraire(STANDARD RETURN) 자산 자체의 가치 상승과 인간 관행 전체의 본질적 효용 감소.
* **혼동 원인**: 모든 자산이 STANDARD RETURN 기준으로 표기되므로, 전체 관행의 일괄 가격 하락이 Numeraire의 절상 때문인지 효용 소멸 때문인지 단면/시계열로 구분 불가.
* **상장 변경 대안**: 고정 기준 지수(Frozen Yardstick Index)의 하위 교환 자산 직접 상장.


3. **Hardware Infrastructure Substitution vs. Software Protocol Shift**
* **내용**: 물리적 기기 변경(예: 유선→무선) 효과와 소프트웨어 프로토콜 변화(예: 음성→문자) 효과의 분리.
* **혼동 원인**: 동일 관행(예: Planned call) 내에서 두 변화가 시기적으로 중첩되어 발생함.
* **상장 변경 대안**: 매체별(통화형, 메시지형) 기술 종속 자산 분리 상장.



---

## Section 6 — Double counting

중복 계상(Double counting) 발생 지점 및 방지책:

1. **Numeraire Appreciation vs. Substitution Exposure**
* **중복 지점**: Numeraire의 가치 상승(시간 절약 효율 증가)이 Substitution 라인의 기술 대체율 변동과 동일한 하락 압력으로 중복 계산됨.
* **방지책**: Substitution 요인 산출 시 Numeraire 가치 변동률을 사전에 편편회귀(Partial Regression)하여 직교화(Orthogonalization)된 잔차만을 Substitution 라인에 반영.


2. **Float Redemption vs. Positioning Line**
* **중복 지점**: 관행의 유동주의(Float) 조기 상환(Redemption) 변동이 거래 포지셔닝(Positioning) 변화로 중복 집계됨.
* **방지책**: Float 변동을 순수 발행/상환 Balance 수량으로 고정하고, Positioning 라인에는 순수 가격 변동에 따른 롱/숏 유동성 잔고 변동만 분리 집계.



---

## Section 7 — What would settle it

후보 요인 집합 간 우위를 판별하기 위한 실행 가능한 추정 및 시뮬레이션 절차:

### 절차 명세 (Estimation Procedure)

1. **Out-of-Sample Rolling Cross-Sectional Regression**
* 1,565개 주차 데이터를 26주 단위 Rolling Window로 분할합니다.
* 각 후보 요인 집합(5요인 ~ 12요인)에 대해 Fama-MacBeth 회귀분석을 수행합니다.


2. **Penalized Structural Equation Modeling (LASSO / Elastic Net)**
* 요인 로딩 행렬에 $L_1$ 규제(Penalty)를 적용하여 다음 목적함수를 최적화합니다.

$$\min_{\mathbf{\Lambda}, \mathbf{F}} \sum_{t=1}^{T} \Vert{}\mathbf{R}_t - \mathbf{\Lambda} \mathbf{F}_t\Vert{}^2 + \lambda \sum_{j=1}^{K} \Vert{}\lambda_j\Vert{}_1$$




3. **판정 기준 (Decision Metric)**
* Out-of-sample 예측 오차(Root Mean Squared Error, RMSE)를 최소화하고, Akaike Information Criterion(AIC) 및 Bayesian Information Criterion(BIC) 점수가 가장 낮게 유지되는 요인 개수 및 조합을 적정 집합으로 결정합니다.



---

## Section 8 — Refusals

* **거부 사항**: 특정한 요인 집합을 최종 세트로 "선택"하거나 "추천"하는 작업, 이전 라운드의 6개 후보 세트에 대한 순위 매기기.
* **이유**: 상기 요청은 본 라운드의 목적("선호가 아닌 식별 가능성에 따른 한계 규명") 및 가이드라인 제약 조건에 직접적으로 위배되므로 거부합니다.