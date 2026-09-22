# 우선순위 결정 — MoSCoW + Kano 병행

MoSCoW(Must/Should/Could/Won't)는 "지금 당장 필요한가"를 정하지만, "이걸 넣으면 얼마나
만족도가 올라가는가"는 구분하지 못합니다. 노리아키 카노(Noriaki Kano)의 **Kano 모델**을
같이 쓰면 이 둘을 분리해서 볼 수 있습니다.

## Kano 3범주

| 범주 | 설명 | 없으면? | 많으면? |
|---|---|---|---|
| Basic (기본/당연) | 없으면 불만족, 있어도 만족도가 크게 안 오름 | 강한 불만족 | 만족도 정체 |
| Performance (성능) | 투입량에 비례해서 만족도가 선형으로 오름 | 불만족 | 만족도 비례 상승 |
| Excitement (감동/기쁨) | 기대 안 했는데 있으면 감동, 없어도 불만 없음 | 무반응 | 만족도 급상승 |

같은 항목이라도 시간이 지나면 Excitement → Performance → Basic으로 내려갑니다 (예:
스마트폰 지문인식은 한때 Excitement였지만 지금은 Basic).

## MoSCoW × Kano 매트릭스로 우리 요구사항 재분류

| ID | MoSCoW | Kano | 해석 |
|---|---|---|---|
| FR1 (저장 템플릿 제공) | Must | Basic | 없으면 워크플로우 자체가 성립 안 함. 완벽히 잘 만들어도 "당연한 것"이라 감동은 없음 |
| FR3 (회고→카탈로그 반영 진입점) | Must | Performance | 잘 만들수록(쉬울수록) 실제로 더 자주 쓰게 되고 원문제 해결도가 비례해서 올라감 — 투자 가치가 높은 항목 |
| FR2 (패턴 검색) | Should | Performance | 검색이 빠르고 정확할수록 워크플로우 효율이 비례 상승 |
| (자동 반영, Could 항목) | Could | Excitement | 지금 없어도 불만 없지만, 나중에 생기면 "오, 이거 좋은데"가 될 요소 |

## 실무 판단 규칙

- **Must + Basic** 조합: 최소 기능만 빠르게 구현하고 더 이상 투자하지 않는다 (과잉 엔지니어링 방지)
- **Must/Should + Performance** 조합: 여기에 실제 개선 노력을 집중한다 — 투자 대비 만족도 상승이 가장 큼
- **Could + Excitement** 조합: 여유 있을 때만, 나중에 추가

이 프로젝트에서는 **FR3(회고 피드백 루프)가 Performance 항목**이라는 게 중요한 발견입니다
— 즉 "일단 되게만 만들기"가 아니라 "쓰기 쉽게 계속 다듬는 것"이 원문제 해결에 직접
비례한다는 뜻입니다.

## 출처
- [The Kano Model: Prioritizing Features That Delight - Product School](https://productschool.com/blog/product-fundamentals/kano-model)
- [Understanding the Kano Model: A Complete Guide - Edstellar](https://www.edstellar.com/blog/kano-model)
