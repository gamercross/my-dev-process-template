# 시작하기 (다른 사람이 이 시스템을 쓰는 법)

이 문서는 이 저장소를 만든 사람이 아니라, **처음 받아서 써보려는 사람**을 위한
안내입니다. 지금 보고 있는 `template` 브랜치는 규칙·템플릿·Claude Code 스킬은
다 갖췄지만, 특정 문제를 실제로 풀었던 기록(세션 파일, 트래커, 카탈로그
누적 항목)은 비어 있는 **빈 상태**입니다.

## 필요한 것

- [Claude Code](https://claude.com/claude-code) (또는 `.claude/skills/`의 스킬
  파일을 읽어서 실행할 수 있는 호환 도구)
- Git
- 문서가 전부 **한국어**입니다 — 영어로 번역해서 쓰고 싶으면 `docs/`를 통째로
  번역하거나, Claude에게 "이 문서 영어로 요약해서 설명해줘"라고 요청하며
  진행해도 됩니다(구조 자체는 언어와 무관합니다).

## 1. 받기

```bash
git clone <이 저장소 URL> my-dev-process
cd my-dev-process
git checkout template
```

본인만의 기록을 계속 쌓고 싶다면, 이 시점에 원격을 본인 것으로 바꾸는 걸
권장합니다(예: GitHub에서 새 저장소를 만들고 `git remote set-url origin
<새 URL>`) — 원본 저장소에 직접 푸시할 권한이 없을 수도 있고, 어차피 이제부터는
완전히 독립적인 기록이 되는 게 맞습니다.

## 2. Claude Code로 열기

이 폴더에서 Claude Code를 실행하면 `.claude/skills/dev-workflow/SKILL.md`가
자동으로 스킬 목록에 뜹니다 — 별도 설치나 등록이 필요 없습니다. 목록에 안
뜨면 Claude Code 버전이 스킬 기능을 지원하는지 확인하세요.

## 3. 첫 항목 저장해보기

자연어로 트리거합니다: "새 문제 시작해줘" 또는 "이 프로젝트 저장해줘" 같은
요청이면 스킬이 반응합니다. 자연어 트리거가 안 먹히면(세션마다 다를 수
있습니다) `dev-workflow` 스킬을 직접 지정해서 실행하도록 요청하세요.

**처음이라면 작은 것부터 추천합니다**: 간단한 알고리즘 문제(LeetCode 아무거나)나
아주 작은 스크립트 하나로 1→7단계를 한 번 완주해 보면서 전체 흐름(등급 판단 →
저장 → 패턴 검색 → 게이트 → 구현 → 실측 → 회고)이 몸에 익습니다. 그다음에
진짜 프로젝트(Full 등급)로 넘어가면 PRD/EARS/RTM/ADR 같은 무거운 절차까지
자연스럽게 이어집니다.

## 4. 알아두면 좋은 파일들

| 파일 | 역할 |
|---|---|
| [`docs/00-overview/README.md`](docs/00-overview/README.md) | 전체 그림, 진행상황 |
| [`docs/00-overview/scope-tiers.md`](docs/00-overview/scope-tiers.md) | 새 일이 생기면 제일 먼저 볼 문서 — 등급(Full/Xpress/Lite/즉시처리) 판단 |
| [`docs/00-overview/gates.md`](docs/00-overview/gates.md) | 단계를 넘어갈 때 확인하는 기준 |
| [`.claude/skills/dev-workflow/SKILL.md`](.claude/skills/dev-workflow/SKILL.md) | AI가 실제로 따르는 실행 절차 |
| [`docs/01-problem-save/sessions/README.md`](docs/01-problem-save/sessions/README.md) | 지금까지 진행한 모든 항목 트래커 (지금은 비어 있음) |
| [`docs/catalog/patterns.md`](docs/catalog/patterns.md), [`checklist.md`](docs/catalog/checklist.md) | 회고에서 쌓이는 재사용 지식 (지금은 비어 있음) |
| [`docs/00-overview/worklog.md`](docs/00-overview/worklog.md) | 여러분의 시행착오를 기록하는 곳 |

## 5. 본인 것으로 바꾸기

- **새 트랙이 필요하면** `docs/01-problem-save/`에 템플릿 파일 하나만
  추가하세요(`README.md`, `prd-template.md` 제외). 스킬 로직을 고칠 필요가
  없습니다 — [ADR-0001](docs/03-pattern-analysis/adr/0001-storage-and-interface.md)의
  설계 제약이자, `main` 브랜치에서 실제로 검증된 방식입니다.
- **규칙 자체가 안 맞으면** `docs/00-overview/gates.md`, `scope-tiers.md`,
  `SKILL.md`를 바로 고치세요 — 이 시스템도 스스로 계속 고쳐가며 만들어진
  것입니다. 뭘 왜 고쳤는지는 `worklog.md`에 남기는 습관을 들이면, 나중에
  "왜 이렇게 바꿨더라"를 다시 안 물어봐도 됩니다.

## 원본과의 관계

이 저장소의 원본(`main` 브랜치)에는 실제로 여러 문제/프로젝트를 1→7단계로
풀어본 기록이 남아 있습니다 — 방식이 실제로 검증된 예시가 궁금하면 그쪽
`worklog.md`와 `docs/01-problem-save/sessions/`를 참고하세요. 이 `template`
브랜치는 그 검증된 틀만 가져오고 개인 기록은 뺀 버전입니다.
