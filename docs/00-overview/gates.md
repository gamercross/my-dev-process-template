# 게이트 규정 — 단계를 잘 넘어가고 있는지 확인하는 방법

7단계를 그냥 순서대로 밟는 것과, **각 단계를 제대로 마쳤는지 확인하고 넘어가는 것**은
다릅니다. 이 문서는 두 표준 개념을 결합해 "다음 단계로 넘어가도 되는가"를 명확한
규정으로 만듭니다.

> **먼저 [scope-tiers.md](scope-tiers.md)로 이 일이 7단계를 다 밟을 가치가 있는지부터
> 정하세요.** 아래 DoR/DoD 표는 Full 등급 기준입니다 — Xpress/Lite/즉시처리 등급이면
> 일부 단계를 건너뜁니다.

## 쓰는 두 가지 표준 개념

1. **DoR/DoD (스크럼)** — 각 단계마다 "시작하려면 뭐가 갖춰져 있어야 하는가"(Definition
   of Ready, 진입기준)와 "끝났다고 부르려면 뭐가 갖춰져 있어야 하는가"(Definition of
   Done, 완료기준)를 미리 정해둡니다. DoR은 다음 단계로 들어가는 조건, DoD는 지금
   단계에서 나가는 조건입니다.
2. **Stage-Gate (Robert G. Cooper)** — 제품 개발에서 단계 사이마다 "게이트"를 두고,
   미리 정한 기준으로 **Go / Kill / Hold / Recycle** 넷 중 하나를 결정하는 방법론입니다.
   - **Go**: DoD를 충족했다 → 다음 단계로
   - **Recycle**: DoD를 못 채웠다 → 지금 단계로 돌아가 보완
   - **Hold**: 외부 사정(우선순위 변경 등)으로 일시 중단
   - **Kill**: 원문제 정의 자체가 잘못됐다고 판명 → [0단계](README.md#원문제-정의)로

즉 "느낌상 다음으로 넘어가도 될 것 같다"가 아니라, **정해둔 체크리스트를 다 채웠는지로만
판단**합니다.

## 단계별 DoR / DoD

| 단계 | 진입기준 (DoR) | 완료기준 (DoD) |
|---|---|---|
| 0. 원문제 정의 | — (시작점) | 시나리오·원하는 결과·적용 대상 3요소가 문장으로 명시됨 |
| 1. 문제 저장 | 0단계 완료 | 트랙 선택됨, 템플릿 필수 필드 전부 채움(IEEE 830: 문장당 동작 하나, 정성적 표현 없음), 태그 부여됨. **Full 등급 프로젝트 트랙이면** [PRD 확장 여부](../01-problem-save/prd-template.md)도 결정하고, 확장했다면 PRD 섹션(경량형 5개/상세형 11개)도 전부 채움 |
| 2. 문제 분석 | 1단계 항목 저장 완료 | [`catalog/checklist.md`](../catalog/checklist.md)의 "2단계 파이프라인 체크리스트" 4개 항목 모두 체크 |
| 3. 패턴 분석 | 2단계 요구사항 확정 | [`catalog/checklist.md`](../catalog/checklist.md)의 "3단계 파이프라인 체크리스트" 4개 항목 모두 체크 |
| 4. 패턴 구현 | 3단계 결정(패턴/ADR) 확정 | [Walking Skeleton](../04-pattern-implementation/02-project-track-skeleton.md) 기준으로 주요 컴포넌트가 실제로 연결됨(스모크 테스트 통과) — 또는 알고리즘 트랙은 브루트포스가 정답을 냄 |
| 5. 구현 | 4단계 스켈레톤 검증 완료 | 단위 테스트 통과. **Full 등급(2단계 수행함)**: EARS Unwanted-behavior 요구사항 전부 커버. **Xpress/Lite(2단계 Skip)**: [동등분할·경계값 분석](../05-implementation/02-boundary-value-equivalence.md) + 브루트포스 대비 차등 테스트로 대체 |
| 6. 서비스 | 5단계 구현·테스트 통과 | **프로젝트 트랙**: 2단계 Planguage Goal을 실측해서 달성 여부가 기록됨 (미달이어도 "기록됨"이면 조건 충족 — 미달 자체가 7단계 입력이 됨). **알고리즘 트랙**: 제출/채점 결과 + 성능(런타임/메모리)이 기록됨 |
| 7. 유지보수 | 6단계 실측 완료 | 회고 작성 + 5 Whys로 근본원인 도달 + `catalog/patterns.md` 또는 `checklist.md` 갱신 + git 커밋 |

DoD 열은 앞 단계가 이미 만들어둔 체크리스트를 그대로 가리킵니다 — **게이트 규정은
새로운 기준을 만드는 게 아니라, 이미 흩어져 있던 기준들을 "언제 확인하는가"의 순서로
모아놓은 것**입니다.

> 이 게이트 규정 전체가 실제로 작동하는지("적는 것"뿐 아니라 "꺼내 쓰는 것"까지)는
> [`catalog/patterns.md`](../catalog/patterns.md)에 실제 검증 사례로 남아있습니다.
> 과정은 [worklog.md](worklog.md)의 "핵심 피드백 루프 실증" 참고.

## 새 문제/프로젝트용 게이트 로그 템플릿

위 표는 **이 워크플로우 시스템 자체(메타 프로젝트)**의 기록입니다. 앞으로 저장하는
개별 문제/프로젝트(예: `sessions/algorithm-track/...`)는 자기 것을 따로 남겨야
하는데, 지금까지는 그 자리가 없었습니다 — 전체 점검에서 발견한 빈틈입니다.

**규칙: 1단계 세션 파일(`docs/01-problem-save/sessions/<트랙>/<날짜>-<슬러그>.md`)
맨 아래에 아래 블록을 그대로 붙여서 채운다.**

```
## 게이트 로그

등급: (Full / Xpress / Lite / 즉시처리 — [scope-tiers.md](scope-tiers.md) 참고)

| 게이트 | 결정 | 근거 |
|---|---|---|
| 1 → 2 | | |
| 2 → 3 | | |
| 3 → 4 | | |
| 4 → 5 | | |
| 5 → 6 | | |
| 6 → 7 | | |
```

- 등급이 Xpress/Lite/즉시처리면 해당 안 되는 게이트 행은 지운다 (표시만 안 할 뿐,
  거짓 Go로 채우지 않는다)
- 결정 칸은 항상 Go / Recycle / Hold / Kill 중 하나
- [2단계 "적용 범위"](../02-problem-analysis/README.md)에 따라 단계 자체를 생략하는
  경우(알고리즘 트랙 단순 문제가 2단계를 건너뛰는 경우 등)는 **Skip**으로 쓰고 근거에
  왜 생략했는지 남긴다 — Cooper의 4개 결정에는 없는 예외지만, 이 저장소의 2단계 경량화
  규칙과 맞물려서 필요함
- 아직 안 온 게이트는 행 자체를 비워두거나 지운다 (거짓으로 채우지 않는다)

## 게이트 통과 기록 (이 프로젝트 자체)

| 게이트 | 결정 | 근거 |
|---|---|---|
| 0 → 1 | Go | 원문제 정의 문장 확정 |
| 1 → 2 | Go | 템플릿 3종 작성 완료 |
| 2 → 3 | Go | 5단계 파이프라인 체크리스트 충족, [applied-example.md](../02-problem-analysis/applied-example.md) 참고 |
| 3 → 4 | Go | [ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md) Accepted |
| 4 → 5 | Go | 트랙 자동 인식 스모크 테스트 통과 ([04단계 README](../04-pattern-implementation/README.md)) |
| 5 → 6 | Go | 5·6·7단계 방법론(TDD, Twelve-Factor, 5 Whys+Blameless) 전부 문서화 완료 |
| 6 → 7 | Go | 위와 동일 — 시스템 자체는 실사용으로 검증할 일만 남음 |

이 표는 이 워크플로우 시스템 자체(메타 프로젝트)를 만드는 과정의 기록이라
지우지 않고 남겨뒀습니다. 실제로 이 시스템을 써서 무언가를 풀어본 기록은
`sessions/README.md` 트래커에 새로 쌓입니다.

## 출처
- [What Is the Difference Between DoD and DoR? - Scrum.org](https://www.scrum.org/resources/blog/what-difference-between-definition-done-dod-and-definition-ready-dor)
- Cooper, R. G., *The Stage-Gate® System* — [Toolshero 정리](https://www.toolshero.com/innovation/stage-gate-process/)
