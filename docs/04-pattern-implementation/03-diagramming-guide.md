# 패턴을 다이어그램으로 구상하는 법 — 어떤 걸 고를지

패턴 구현(4단계)에서 코드를 짜기 전에 구조를 그려보고 싶을 때, "뭘 그릴지" 고르는
기준은 하나입니다: **어떤 질문에 답하고 싶은가.** 다이어그램 종류마다 답하는 질문이
다르고, 질문에 안 맞는 다이어그램을 고르면 오히려 헷갈립니다.

## 핵심 기준: 질문 → 다이어그램

| 답하고 싶은 질문 | 다이어그램 | 표준/출처 |
|---|---|---|
| 로직이 어떤 순서로 갈라지는가 (분기·반복) | **순서도 (Flowchart)** | ISO 5807 |
| 무엇으로 이루어져 있는가 (정적 구조) | **구조 다이어그램** (클래스/컴포넌트) | UML Structure Diagrams |
| 컴포넌트들이 어떤 순서로 상호작용하는가 (동적 흐름) | **행동 다이어그램** (시퀀스/액티비티) | UML Behavior Diagrams |
| 같은 아키텍처를 청중마다 어느 줌 레벨로 보여줄까 | **C4 모델** (Context/Container/Component/Code) | Simon Brown |

UML은 이 표의 2·3번을 "정적 구조(What) vs 동적 행동(How)"로 크게 나눕니다 —
구조 다이어그램부터 시스템을 정의하고, 그 위에 행동 다이어그램으로 상호작용을
덧붙이는 순서를 권장합니다.

## 알고리즘 트랙

- **순서도 (ISO 5807)**: 분기·반복이 있는 로직(예: 이중 루프 브루트포스 vs 해시맵
  탐색)을 그릴 때 기본값. `if 조건 → 분기`, `while 반복 → 루프` 기호가 표준화돼 있어서
  다른 사람도 바로 읽을 수 있습니다.
- **재귀 트리 / 호출 그래프**: [3단계](../03-pattern-analysis/01-algorithm-paradigms.md)의
  분할정복·백트래킹처럼 재귀 구조인 패턴은 순서도보다 재귀 트리가 훨씬 직관적입니다
  (표준 규격은 아니지만 알고리즘 교재에서 관례적으로 씀).

## 프로젝트 트랙

**질문이 "청중마다 얼마나 자세히 보여줄까"라면 C4 모델부터 고릅니다.** Simon Brown이
제안한 4단계 줌 레벨:

| 레벨 | 보여주는 것 | 이 저장소에 적용하면 |
|---|---|---|
| Context | 전체 시스템이 외부와 어떻게 연결되는가 | "사용자 ↔ dev-workflow 시스템 ↔ GitHub" |
| Container | 배포/실행 단위 | `docs/`(파일 저장소) + `.claude/skills/dev-workflow/`(스킬) — [ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md)의 하이브리드가 정확히 이 레벨 |
| Component | 컨테이너 내부 구성 요소 | SKILL.md의 명령 1/2/3 |
| Code | 클래스/함수 수준 | 실제 구현 코드가 생기면 (UML 클래스 다이어그램과 동일 레벨) |

**질문이 "이게 뭘로 이루어져 있나(구조)" vs "어떻게 동작하나(행동)"라면 UML 분류를
씁니다**:
- 구조: 클래스/컴포넌트 다이어그램
- 행동: 시퀀스(시간순 상호작용)/액티비티(작업 흐름)/상태(State Machine)

## 이미 이 저장소에서 쓴 다이어그램을 이 기준으로 분류하면

| 위치 | 실제로는 |
|---|---|
| [00-overview 전체 방향 다이어그램](../00-overview/README.md) | Activity Diagram(작업 흐름)에 가까움 — mermaid flowchart 문법으로 그림 |
| [00-overview 유즈케이스 다이어그램](../00-overview/README.md) | UML Use Case Diagram (행동) |
| [03-pattern-analysis 파이프라인 다이어그램](../03-pattern-analysis/README.md) | Activity Diagram |

즉 지금까지는 "행동(어떻게 흘러가는가)" 계열만 썼고, **"구조(무엇으로 이루어져
있는가)" 계열(클래스/컴포넌트/C4 Container)은 아직 하나도 안 그렸습니다** — 이게
4~5단계에서 실제 코드/스킬 구조를 잡을 때 다음으로 채울 빈틈입니다.

## 결정 절차

```
1. "로직 분기/반복을 보여주고 싶다" → 순서도 (알고리즘 트랙)
2. "재귀/분할정복 구조를 보여주고 싶다" → 재귀 트리
3. "청중마다 다른 확대 수준으로 보여주고 싶다" → C4 (프로젝트 트랙)
4. "정적 구조(뭐로 이루어졌나)를 보여주고 싶다" → UML 구조 다이어그램(클래스/컴포넌트)
5. "동적 흐름(어떻게 상호작용하나)을 보여주고 싶다" → UML 행동 다이어그램(시퀀스/액티비티/상태)
```

## 출처
- [ISO 5807:1985 - Information processing, flowchart symbols](https://www.iso.org/standard/11955.html)
- [Home - C4 model, Simon Brown](https://c4model.com/)
- [UML - Behavioral Diagram vs Structural Diagram - Visual Paradigm](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/behavior-vs-structural-diagram/)
