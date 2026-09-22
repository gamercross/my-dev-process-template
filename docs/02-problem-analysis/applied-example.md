# 적용 예시: 이 워크플로우 시스템 자체의 요구사항

이 저장소(나만의 개발 워크플로우 시스템)를 만들 때 실제로 2단계 파이프라인 전체를
적용한 결과입니다. 새 프로젝트에서 템플릿을 어떻게 채우는지 참고용으로 남겨둡니다.

## 1. 수집 (Elicitation)

- 사용한 기법: **Document Analysis** (1단계 문제 저장 항목 + 대화 중 나온 원문제 정의를
  검토) → **Requirements Workshop** (혼자 하는 워크숍 — 이 대화 세션 자체가 요구사항을
  정리·확정하는 자리 역할)
- 수집된 원자료: "새 프로젝트마다 즉흥적으로 시작해서 배운 게 재사용 안 된다"는 원문제,
  그리고 알고리즘/프로젝트 두 트랙 모두에 적용하고 싶다는 조건

## 2. 초기 요구사항 (ISO 29148 5요소로 처음 뽑았던 버전)

| ID | 요구사항 | 근거 | 충족기준 | 우선순위(MoSCoW) |
|---|---|---|---|---|
| FR1 | 사용자가 새 문제/프로젝트를 시작하면, 시스템은 트랙에 맞는 저장 템플릿을 제공해야 한다 | 즉흥적 시작 방지 | 필수 필드 미기입 시 다음 단계 진행 불가 | Must |
| FR2 | 사용자가 패턴을 검색하면, 시스템은 태그/키워드로 일치하는 카탈로그 항목을 반환해야 한다 | 과거 패턴 재사용 안 됨 | 로컬 파일 기준 즉시 결과 표시 | Should |
| FR3 | 유지보수 단계 완료 시, 시스템은 회고 내용을 카탈로그/체크리스트에 추가하는 진입점을 제공해야 한다 | 원문제 핵심(피드백 루프) | 회고 후 1회 명령으로 카탈로그 항목 추가 가능 | Must |

## 3. EARS 문법으로 재작성

→ [02-specification-ears.md](02-specification-ears.md)의 "우리 프로젝트 요구사항을 EARS로
재작성" 참조. FR1의 암묵적 예외 케이스가 별도 요구사항(FR1-예외)으로 명시화됨.

## 4. 비기능 요구사항을 Planguage로 정량화

→ [03-quantification-planguage.md](03-quantification-planguage.md) 참조. Usability /
Supportability / Reliability 각각에 Scale·Meter·Goal 부여.

## 5. MoSCoW × Kano 재분류

→ [04-prioritization.md](04-prioritization.md) 참조. FR3가 "Must + Performance" 조합으로
드러나면서, 단순 구현보다 사용 편의성에 투자할 가치가 크다는 게 확인됨.

## 6. 추적 매트릭스 (RTM)

→ [05-traceability.md](05-traceability.md) 참조. FR1~FR3를 UC1/UC3/UC7과 연결.

## 결론 (2단계 확정)

- **Must**: FR1(EARS 예외 케이스 포함), FR3
- **Should**: FR2
- **Could**: 자동 반영(Excitement 항목, 여유 있을 때)
- **Won't (지금은)**: GUI, 웹앱화

이 확정된 요구사항을 가지고 [`docs/03-pattern-analysis/`](../03-pattern-analysis/README.md)로
진행했고, [ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)로 결정이
확정됐습니다.
