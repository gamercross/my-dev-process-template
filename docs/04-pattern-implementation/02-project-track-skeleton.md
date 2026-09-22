# 프로젝트 트랙 — 스켈레톤 방향

프로젝트 트랙의 스켈레톤 단계는 세 가지 표준 개념 중 상황에 맞는 걸 골라 씁니다. 셋을
헷갈리면 "일단 만들어보고 버리는 건지, 남기는 건지"를 기준으로 구분하세요.

## 1. Walking Skeleton — 기본으로 쓸 개념

Alistair Cockburn이 *Writing Effective Use Cases*(2000)에서 제안한 개념으로, **실제
기능의 가장 얇은 조각을 자동으로 빌드·배포·테스트까지 end-to-end로 돌려보는 것**입니다.
최종 아키텍처를 그대로 쓸 필요는 없지만, **주요 아키텍처 컴포넌트들은 실제로 연결**되어
있어야 합니다. 작게 시작해서 모든 통신 경로를 실제로 거쳐보면, 방향이 맞는지 초기에
확인할 수 있고 — 문제가 생겨도 아직 많이 투자하지 않은 시점이라 구조를 쉽게 바꿀 수
있습니다.

**이 저장소에서 이미 한 일**: [4단계에서 만든 `SKILL.md`](../../.claude/skills/dev-workflow/SKILL.md)가
정확히 Walking Skeleton입니다 — ADR-0001이 고른 "파일+스킬 하이브리드" 아키텍처를
최종 형태 그대로는 아니지만, "트리거 → 트랙 인식 → 파일 저장"이라는 핵심 경로를 실제로
연결해봤고, 버릴 코드가 아니라 5단계에서 그대로 자라날 골격입니다.

## 2. Tracer Bullet — Walking Skeleton과 헷갈리기 쉬운 개념

Andy Hunt와 Dave Thomas가 *The Pragmatic Programmer*(1999)에서 소개한 기법으로,
군대의 예광탄(밤에 궤적이 보이는 총알)에서 따온 이름입니다. **핵심 차이**: 일회용
프로토타입은 버려지는 코드지만, Tracer Bullet 코드는 **얇지만 완결된(lean but
complete)** 코드로, 최종 시스템의 골격 일부가 됩니다 — 이 점에서 Walking Skeleton과
거의 같은 개념이고, 실제로 업계에서도 상호 교환적으로 쓰이는 경우가 많습니다. 요구사항이
아직 흐릿하거나 낯선 기술을 쓸 때, 여러 번 쏘면서 목표에 맞춰가는 이미지로 쓰입니다.

## 3. Spike — Walking Skeleton과 절대 헷갈리면 안 되는 개념

Extreme Programming에서 나온 개념으로, **기술적 불확실성을 줄이기 위한 시간제한(timebox)
탐색**입니다. 가장 중요한 차이: **Spike 코드는 대부분 버려지는 게 정상**입니다. 문제
자체만 파고들고 다른 건 다 무시하고 만들며, 남겨서 자라나게 할 코드가 아닙니다.

## 언제 뭘 쓰는가

| 상황 | 개념 | 코드 운명 |
|---|---|---|
| 아키텍처 전체를 얇게 연결해서 확인하고 싶다 | Walking Skeleton | 남겨서 5단계에서 확장 |
| 요구사항이 흐릿해서 실제로 쏴보며 목표를 좁혀야 한다 | Tracer Bullet | 남겨서 확장 (Walking Skeleton과 사실상 동의어로 취급해도 무방) |
| 특정 기술/API가 우리 방식대로 동작하는지 그 자체가 불확실하다 | Spike | 확인 후 버림 |

## 이 저장소에 남은 Spike 성격의 미해결 사항

`SKILL.md`의 자연어 트리거("새 문제 시작"에 실제로 반응하는지)는 아직 실제 세션에서
확인 못 했습니다 — 이건 Walking Skeleton의 일부라기보다 **"Claude Code 스킬 트리거가
우리 기대대로 동작하는가"라는 기술적 불확실성**이므로, 5단계에서 짧게 시간을 정해두고
Spike처럼 확인한 뒤 결과만 기록하고 탐색 코드 자체는 남길 필요 없습니다.

## 출처
- Cockburn, A., *Writing Effective Use Cases* (2000) — [Walking Skeleton 정리, Medium](https://medium.com/@jorisvdaalsvoort/walking-skeletons-in-software-architecture-894168276e3f)
- [60. Start with a Walking Skeleton - 97 Things Every Software Architect Should Know](https://www.oreilly.com/library/view/97-things-every/9780596800611/ch60.html)
- Hunt, A., Thomas, D., *The Pragmatic Programmer* (1999) — [Tracer Bullets 정리](https://www.barbarianmeetscoding.com/notes/books/pragmatic-programmer/tracer-bullets/)
- [Spike (software development) - Wikipedia](https://en.wikipedia.org/wiki/Spike_(software_development))
- [Spike solution - extremeprogramming.org](http://www.extremeprogramming.org/rules/spike.html)
