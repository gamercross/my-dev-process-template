# 트레이드오프 평가 — ATAM (간소화 버전)

후보가 2개 이상 남았을 때, "그냥 감으로" 고르지 않기 위한 평가 방법. **ATAM(Architecture
Tradeoff Analysis Method)**은 카네기멜론대 SEI(Software Engineering Institute)가 개발한
아키텍처 평가 방법론으로, 후보 아키텍처들을 **품질속성 시나리오**에 대입해 트레이드오프와
리스크를 드러냅니다. 원래는 팀 단위의 무거운 워크숍 절차지만, 개인 프로젝트에는 핵심
아이디어만 축약해서 씁니다.

## 원래 ATAM의 핵심 개념

- **품질속성 시나리오(Quality Attribute Scenario)**: "자극(stimulus) → 시스템이 어떻게
  반응해야 하는가 → 반응을 측정하는 방법"의 형태로 요구사항을 구체화한 것
- 여러 후보 아키텍처를 같은 시나리오 집합에 대입해 비교 → **트레이드오프 지점**(한
  속성을 얻으려면 다른 속성을 희생해야 하는 지점)과 **민감점(sensitivity point)**,
  **리스크**를 식별

## 개인 프로젝트용 축약 절차

1. 2단계에서 만든 **Planguage 비기능 요구사항**([03-quantification-planguage.md](../02-problem-analysis/03-quantification-planguage.md))을
   그대로 시나리오로 재사용한다 — 이미 Scale/Meter/Goal이 있으므로 새로 안 만들어도 됨.
2. 후보 패턴/아키텍처마다 각 시나리오를 만족하는지 O/△/X로 채점한다.
3. 트레이드오프(한 후보가 어떤 시나리오에서 이기고 어떤 시나리오에서 지는지)를 표로 남긴다.
4. 이 표를 ADR의 "Considered Alternatives"/"Consequences" 섹션 근거 자료로 그대로 인용한다.

## 축약 평가표 템플릿

| 시나리오 (Planguage 기준) | 후보 A | 후보 B | 비고(트레이드오프) |
|---|---|---|---|
| (예: Usability - 5분 이내 작성) | O | △ | A가 더 단순하지만 B가 확장성은 나음 |
| (예: Supportability - 신규 확장 시 기존 파일 무변경) | O | O | 동일 |

## 언제 이 단계를 생략해도 되는가

후보가 1개뿐이거나(비교할 대상이 없음), Kano 분류상 해당 요구사항이 **Basic**이면
(2단계 [04-prioritization.md](../02-problem-analysis/04-prioritization.md) 참고) 과도한
평가는 시간 낭비입니다 — 가장 단순한 후보를 바로 선택하고 ADR에 "대안 비교 생략, 이유:
요구사항이 Basic 수준" 이라고만 남깁니다.

## 출처
- [Architecture Tradeoff Analysis Method - GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/architecture-tradeoff-analysis-method-atam/)
- [Architecture tradeoff analysis method - Wikipedia](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)
- Kazman, R., Klein, M., Clements, P., *ATAM: Method for Architecture Evaluation*, SEI/CMU
