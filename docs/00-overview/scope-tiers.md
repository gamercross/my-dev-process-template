# 규모 판단 — 이 워크플로우를 얼마나 밟을지 먼저 정한다

지금까지 "각 단계를 어떻게 통과하는가"만 정해뒀고, **"애초에 7단계 전부를 밟을 가치가
있는 일인가"**는 기준이 없었습니다 (전체 시스템 점검에서 발견). Robert Cooper 본인이
Stage-Gate를 만든 뒤 겪은 문제이기도 합니다 — 원래 하나의 무거운 프로세스만 있었더니,
정작 개발 자원 대부분을 차지하는 **작은 개선·수정 프로젝트들이 그 프로세스를 그냥
무시하고 우회**해버렸습니다. 그래서 Cooper는 프로젝트 규모별로 축소판을 공식화했습니다.

## Cooper의 3단계 규모 (Stage-Gate Full / Xpress / Lite)

| 등급 | 원래 용도 | 이 저장소 매핑 |
|---|---|---|
| **Full** (7단계, 여러 게이트) | 크고 위험도 높은 프로젝트 | 프로젝트 트랙, 규모 있는 작업 — 이 워크플로우 시스템 자체가 이 등급 |
| **Xpress** (3단계급, 중간 위험도) | 개선·수정·확장 | 알고리즘 트랙 단순 문제 — 이미 만든 ["2단계 적용 범위"](../02-problem-analysis/README.md) 규칙이 사실 이 등급이었음 |
| **Lite** (2단계급, 작은 프로젝트) | 단순 고객 요청 수준의 작은 일 | 아래 "Lite 등급" 참고 |

## 여기에 추가하는 네 번째 등급 — 즉시 처리 (Two-Minute Rule)

David Allen의 GTD(*Getting Things Done*)에는 **2분 규칙**이 있습니다: 2~5분 안에
끝낼 수 있는 일은 어딘가에 기록하고 나중에 처리하려 하지 말고, **그 자리에서 바로
끝내라**는 원칙입니다 — 기록하고 되돌아오는 데 드는 비용이 그냥 하는 것보다 더 큽니다.
이 저장소에도 그대로 적용됩니다: 1단계 템플릿 하나 채우는 데도 시간이 드는데, 오타
수정처럼 그보다 짧게 끝나는 일까지 저장·기록하려 들면 오버헤드가 일 자체보다 커집니다.

## 등급 결정 기준

```
이 작업, 전체가 2~5분 안에 끝나는가?
  예 → 즉시 처리. 아무 단계도 밟지 않는다. (GTD Two-Minute Rule)
  아니오 ↓

알고리즘 문제이고 표준 패턴(3단계 카탈로그)으로 바로 풀리는가?
  예 → Xpress. 1 → (2 Skip) → 3 → 4 → 5 → 6 → 7
  아니오 ↓

작은 버그 수정/한 파일짜리 스크립트 수준인가?
  예 → Lite. 1단계(간단 기록) → 7단계(짧은 회고)만. 2~6단계는 전부 생략.
  아니오 → Full. 7단계 전부, docs/00-overview/gates.md의 DoR/DoD 그대로 적용.
```

## 등급별로 뭐가 달라지는가

| 등급 | 1단계 | 2단계 | 3단계 | 4~6단계 | 7단계 |
|---|---|---|---|---|---|
| 즉시 처리 | — | — | — | — | — |
| Lite | 간단히(제목+한 줄) | 생략 | 생략 | 생략 | 짧게(배운 게 있을 때만) |
| Xpress | 전체 템플릿 | Skip (이미 규정됨) | 카탈로그 검색 | 진행 | 진행 |
| Full | 전체 템플릿 | 5단계 파이프라인 전체 | ADR까지 | 진행 | 5 Whys + Blameless |

## 게이트 로그에 등급을 남긴다

[`docs/00-overview/gates.md`](gates.md)의 "게이트 로그" 블록 맨 위에 등급을 한 줄
추가합니다:

```
등급: Full / Xpress / Lite / 즉시처리
```

## 출처
- Cooper, R. G. — Stage-Gate Full/Xpress/Lite 등급 구분,
  [ResearchGate 그림 자료](https://www.researchgate.net/figure/Illustration-of-the-SGS-Stage-Gate-Xpress-and-Stage-Gate-Lite-adapted-from-Cooper_fig1_368399853)
- Allen, D., *Getting Things Done* — Two-Minute Rule,
  [The Two-Minute Rule - gettingthingsdone.com](https://gettingthingsdone.com/2020/05/the-two-minute-rule-2/)
