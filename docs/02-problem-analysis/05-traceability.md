# 요구사항 추적 — Requirements Traceability Matrix (RTM)

BABOK은 요구사항이 "출처 → 명세 → 설계 → 구현 → 테스트"까지 끊기지 않고 연결되는지
확인하는 걸 Trace Requirements라고 부릅니다. 소규모 프로젝트에는 표 하나(RTM)로 충분합니다.

## RTM 템플릿

| 요구사항 ID | 출처 (UC/Volere Originator) | 3단계 패턴 | 4~5단계 구현 위치 | 테스트/충족기준 | 상태 |
|---|---|---|---|---|---|
| FR1 | UC1 | 파일+스킬 하이브리드 ([ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)) | [SKILL.md 명령 1](../../.claude/skills/dev-workflow/SKILL.md) | 필수 필드 미기입 시 진행 불가 | 구현완료 |
| FR2 | UC3 | 파일+스킬 하이브리드 ([ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)) | (템플릿 브랜치에는 예시 구현이 빠져 있음) | 0.5초 이내 결과 표시 | 패턴선정 |
| FR3 | UC7 | 파일+스킬 하이브리드 ([ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)) | [SKILL.md 명령 3](../../.claude/skills/dev-workflow/SKILL.md) | 회고 후 1회 명령으로 카탈로그 항목 추가 | 구현완료 |

> 이 표는 이 워크플로우 시스템 자체(메타 프로젝트)의 RTM입니다. FR2는
> 원래 별도 CLI 도구로 구현·실측(0.5초 목표에 34ms 실측)까지 갔었지만, 그
> 도구는 `main` 브랜치의 실제 사용 예시였을 뿐이라 이 템플릿 브랜치에서는
> 뺐습니다 — 여러분이 비슷한 요구사항을 만들면 이 행을 본인 구현 위치로
> 채우세요. RTM은 "한 번 쓰고 끝"이 아니라 각 단계가 끝날 때마다 갱신해야
> 추적표로서 의미가 있습니다.

## 이 표를 언제 채우는가

- **출처/충족기준**: 2단계(문제 분석)에서 채움
- **3단계 패턴** 열: 3단계 완료 시 채움
- **구현 위치** 열: 5단계 완료 시 실제 파일 경로/커밋 링크로 채움
- **상태** 열: 분석완료 → 패턴선정 → 구현완료 → 서비스적용 → 회고완료로 갱신

## 이 저장소에서의 규칙

- RTM은 프로젝트당 하나, `applied-example.md`처럼 해당 프로젝트 폴더에 둔다.
- 요구사항이 나중에 바뀌면(예: FR2가 취소됨) RTM에서 바로 확인 가능해야 한다 — 즉 요구사항
  변경 시 RTM 갱신을 빼먹지 않는다.
- 작은 개인 프로젝트에 과도한 RTM은 오히려 오버헤드이므로, **요구사항이 5개를 넘어가는
  프로젝트에만 RTM을 쓴다** (BABOK도 "요구사항이 적을 때만" 이 방식을 권장).

## 출처
- IIBA BABOK Guide, [5.1 Trace Requirements](https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/5-requirements-life-cycle-management/5-1-trace-requirements/)
- [An Introduction to Requirements Traceability - Modern Analyst](https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/1722/An-Introduction-to-Requirements-Traceability.aspx)
