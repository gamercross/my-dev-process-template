# 세션 (실제로 채운 문제/프로젝트 항목)

이 폴더는 `docs/01-problem-save/`의 템플릿 파일(`algorithm-track.md`, `project-track.md`,
`learning-track.md`)을 실제로 채운 결과물이 쌓이는 곳입니다. 템플릿 원본은 건드리지 않고,
여기에 트랙별 하위 폴더를 만들어 항목을 모읍니다.

## 경로 규칙 (`.claude/skills/dev-workflow/SKILL.md` 참고)

```
docs/01-problem-save/sessions/<트랙파일명(확장자 제외)>/<YYYY-MM-DD>-<슬러그>.md
```

예: `docs/01-problem-save/sessions/algorithm-track/2026-09-20-two-sum.md`

트랙파일명은 `docs/01-problem-save/`에 있는 템플릿 파일 이름과 그대로 맞춥니다 —
새 트랙(`README.md`, `prd-template.md`가 아닌 새 `*.md` 파일)을 추가하면 이 폴더에도
같은 이름의 하위 폴더가 자연스럽게 생깁니다.

## 트래커 — 지금까지 진행한 모든 항목

새 항목을 저장하거나 게이트가 바뀔 때마다 이 표를 같이 갱신합니다. 개별 항목의
자세한 진행(게이트 로그, 회고)은 각 세션 파일에, 실제 코드/테스트는
[`implementations/`](../../../implementations/)에 있습니다.

| 문제/프로젝트 | 트랙 | 등급 | 사용한 패턴 | 게이트 | 테스트 | 세션 파일 |
|---|---|---|---|---|---|---|
| _(아직 없음 — 첫 항목을 저장하면 여기에 행이 생깁니다)_ | | | | | | |

전체 테스트를 한 번에 돌리려면: `python3 implementations/run_all_tests.py`

## 지금까지 나온 패턴/교훈이 남는 곳

- **패턴**: [`docs/catalog/patterns.md`](../../catalog/patterns.md) — 위 표의 "사용한 패턴" 열이 여기서 옵니다
- **체크리스트**: [`docs/catalog/checklist.md`](../../catalog/checklist.md) — 회고에서 나온 재발 방지 항목
- **과정 전체 기록**: [`docs/00-overview/worklog.md`](../../00-overview/worklog.md)
