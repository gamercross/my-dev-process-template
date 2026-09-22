# 나만의 개발 워크플로우 시스템

새 프로그램/문제를 시작할 때마다 즉흥적으로 접근해서, 배운 게 다음 프로젝트에
재사용되지 않는 문제를 풀기 위한 개인 개발 워크플로우입니다. **7단계로 진행하고,
마지막 단계(유지보수)의 회고가 다시 앞 단계의 참조 자료로 쌓입니다** — 이 피드백
루프가 이 시스템의 핵심입니다.

> 🌱 **이 브랜치(`template`)는 빈 상태로 시작하는 버전입니다.** 규칙·템플릿·
> 스킬은 다 갖춰져 있지만, 특정 문제를 실제로 풀었던 기록은 없습니다 — 당신
> 것으로 채워 나가면 됩니다. 처음 시작한다면 **[GETTING_STARTED.md](GETTING_STARTED.md)**부터
> 읽으세요.

```mermaid
flowchart LR
    S1[1 문제 저장] --> S2[2 문제 분석] --> S3[3 패턴 분석]
    S3 --> S4[4 패턴 구현] --> S5[5 구현] --> S6[6 서비스] --> S7[7 유지보수]
    S7 -. 배운 것 반영 .-> S1

    style S7 fill:#2b2b40,stroke:#888,color:#fff
```

> 모든 일이 7단계를 다 밟지는 않습니다 — 규모에 따라 일부를 건너뜁니다. 등급별
> 분기가 포함된 상세 다이어그램은 [docs/00-overview/README.md](docs/00-overview/README.md)에 있습니다.

## 새 일이 생기면 (퀵스타트)

1. **규모부터 정한다** → [docs/00-overview/scope-tiers.md](docs/00-overview/scope-tiers.md)
   — 2~5분짜리면 그냥 바로 처리, 아니면 Full/Xpress/Lite 중 하나
2. **Claude Code에서 `dev-workflow` 스킬을 트리거**한다 ("새 문제 시작" 등) —
   [`.claude/skills/dev-workflow/SKILL.md`](.claude/skills/dev-workflow/SKILL.md)가
   트랙 선택부터 저장까지 안내함. 스킬 없이 수동으로 하려면
   [docs/01-problem-save/](docs/01-problem-save/README.md) 템플릿을 직접 채운다
3. 단계를 넘어갈 때마다 → [docs/00-overview/gates.md](docs/00-overview/gates.md)의
   DoR/DoD로 확인

**지금까지 진행한 모든 문제/프로젝트를 한눈에 보려면 →
[docs/01-problem-save/sessions/README.md](docs/01-problem-save/sessions/README.md)**
(트래커 표: 문제별 트랙/등급/패턴/게이트 상태/테스트 개수 — 이 브랜치는 아직
비어 있습니다). 전체 테스트를 한 번에 돌리려면
`python3 implementations/run_all_tests.py`.

## 단계 안내

| 단계 | 하는 일 | 핵심 개념 |
|---|---|---|
| [00. 개요](docs/00-overview/README.md) | 원문제, 전체 그림, 진행상황, 유즈케이스 | — |
| [01. 문제 저장](docs/01-problem-save/README.md) | 새 문제/프로젝트를 표준 형식으로 기록 | ICPC 규격 / GitHub Issue Template / PRD |
| [02. 문제 분석](docs/02-problem-analysis/README.md) | 요구사항을 명확하고 측정 가능하게 다듬기 | BABOK / EARS / Planguage / MoSCoW×Kano / RTM |
| [03. 패턴 분석](docs/03-pattern-analysis/README.md) | 어떤 방식으로 풀지 후보를 좁히고 결정 | CLRS 패러다임 / 아키텍처 5대 스타일 / ATAM / ADR |
| [04. 패턴 구현](docs/04-pattern-implementation/README.md) | 최소 골격으로 방향이 맞는지 검증 | Walking Skeleton / Tracer Bullet / Spike |
| [05. 구현](docs/05-implementation/README.md) | 완성 코드와 테스트 작성 | TDD Red-Green-Refactor / 경계값 분석 |
| [06. 서비스](docs/06-service/README.md) | 실제로 쓸 수 있는 형태로 내보내기 | Twelve-Factor App |
| [07. 유지보수](docs/07-maintenance/README.md) | 회고해서 다음 프로젝트에 반영 | 5 Whys / Blameless Postmortem |
| [catalog/](docs/catalog/) | 패턴·체크리스트가 계속 쌓이는 공용 저장소 | — |
| [worklog.md](docs/00-overview/worklog.md) | 지금 이 모양이 된 과정(왜 이렇게 바뀌었는지) | — |

## 폴더 구조

```
.claude/skills/dev-workflow/   Claude Code 스킬 — 새 문제 저장 / 패턴 검색 / 회고 반영
docs/
  00-overview/                 개요 + gates.md(게이트 규정) + scope-tiers.md(규모 판단)
                                + worklog.md(작업 로그)
  01-problem-save/             1단계 템플릿(트랙별 + PRD) + sessions/(실제 저장된 항목)
  02-problem-analysis/         2단계 방법론 + 적용 범위(경량화 규칙) + 적용 예시
  03-pattern-analysis/         3단계 방법론 + adr/(Architecture Decision Record)
  04-pattern-implementation/   4단계 방법론 + 다이어그램 선택 가이드
  05-implementation/           5단계 방법론
  06-service/                  6단계 방법론
  07-maintenance/              7단계 방법론
  catalog/                     patterns.md + checklist.md — 7단계 회고에서 계속 누적
implementations/                5단계 실제 코드 — <트랙파일명>/<세션 슬러그>/ 구조,
                                sessions/와 같은 이름 규칙
```
