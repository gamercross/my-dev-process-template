# 2단계: 문제 분석

> 상태: ✅ 완료 — [ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)까지
> 확정됨. 전체 진행상황은 [`docs/00-overview/README.md`](../00-overview/README.md) 참고.

문제 저장 단계에서 받은 원문제를, 다섯 단계로 이루어진 파이프라인을 거쳐 실제로 다룰 수
있는 요구사항으로 만듭니다. 각 단계는 서로 다른 검증된 방법론을 씁니다.

```mermaid
flowchart LR
    P[원문제] --> C1[1 수집<br/>BABOK]
    C1 --> C2[2 명세<br/>EARS]
    C2 --> C3[3 정량화<br/>Planguage]
    C3 --> C4[4 우선순위<br/>MoSCoW × Kano]
    C4 --> C5[5 추적<br/>RTM]
    C5 --> R[다음: 3단계 패턴 분석]
```

| 단계 | 방법론 | 하는 일 |
|---|---|---|
| [1. 수집](01-elicitation.md) | BABOK | 9대 기법 중 실용적인 것들로 원자료를 모은다 |
| [2. 명세](02-specification-ears.md) | EARS | 기능 요구사항을 5가지 정해진 문형으로만 써서 모호함·암묵적 예외를 제거한다 |
| [3. 정량화](03-quantification-planguage.md) | Planguage | 비기능 요구사항(FURPS+)에 Scale/Meter/Goal을 부여해 "빠르다/편하다"를 숫자로 바꾼다 |
| [4. 우선순위](04-prioritization.md) | MoSCoW × Kano | 무엇을 지금 할지(MoSCoW)와 투자 대비 만족도(Kano)를 함께 본다 |
| [5. 추적](05-traceability.md) | RTM | 요구사항 5개 이상이면 출처→설계→구현→테스트 연결을 표로 관리한다 |

검증(품질 체크)은 `docs/catalog/checklist.md`를 참조 — 매번 이 체크리스트로 최종 점검합니다.

## 적용 범위 — 항상 5단계 전부 돌리지 않는다

이 파이프라인은 규모가 있는 **프로젝트 트랙**을 기준으로 만들어졌습니다. 등급별로
어디까지 적용할지는 [scope-tiers.md](../00-overview/scope-tiers.md)로 정합니다.

- **Full 등급 (프로젝트 트랙, 규모 있는 문제)**: 5단계 전부 적용
- **Xpress 등급 (알고리즘 트랙, 단순 문제)**: 보통 [1단계 템플릿](../01-problem-save/algorithm-track.md)의
  "입력 형식+제약조건" 필드만으로 충분 — 이 파이프라인은 생략하고 바로
  [3단계 패턴 분석](../03-pattern-analysis/README.md)으로 넘어간다
- **애매하면**: 수집(1)과 명세(2)만 가볍게 하고 정량화/우선순위/추적(3~5)은 생략

> 왜 이 규칙이 생겼는지는 [worklog.md](../00-overview/worklog.md)를 참고하세요.

## 새 프로젝트에 적용할 때: 빈 템플릿

```
### 1. 수집
- 사용한 기법: (문서분석/인터뷰/관찰/프로토타이핑/브레인스토밍/워크숍)
- 수집된 원자료:

### 2. 기능 요구사항 (EARS)
FR1 (패턴: Ubiquitous/Event-driven/State-driven/Unwanted/Optional):
  When/While/If <조건>, the 시스템은 shall <행동>.
  근거:
  충족기준:

### 3. 비기능 요구사항 (Planguage)
범주(FURPS):
  Scale:
  Meter:
  Goal:
  Stretch(선택):

### 4. 우선순위
| ID | MoSCoW | Kano |
|---|---|---|

### 5. 추적 (요구사항 5개 이상일 때만)
| ID | 출처 | 3단계 패턴 | 구현 위치 | 테스트 | 상태 |
|---|---|---|---|---|---|
```

## 적용 예시

이 저장소 자체의 요구사항(FR1~FR3)을 이 파이프라인 전체로 실제 적용한 결과:
→ [applied-example.md](applied-example.md)
