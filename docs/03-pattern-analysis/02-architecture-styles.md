# 프로젝트 트랙 — 후보 아키텍처 도출

프로젝트가 "어떤 구조로 만들지" 막막할 때 참고하는 표준 카탈로그. Mark Richards의
*Software Architecture Patterns* (O'Reilly)가 정리한 5대 아키텍처 스타일을 기본 후보군으로
씁니다. 각 스타일은 트레이드오프 스코어카드(품질속성별 강약점)를 함께 제공합니다.

## 5대 아키텍처 스타일

| 스타일 | 핵심 아이디어 | 적합한 상황 |
|---|---|---|
| Layered (계층형) | 계층별로 책임을 나누고, 각 계층은 바로 아래 계층에만 의존 | 가장 흔하고 익숙함. 단순한 CRUD/개인 프로젝트에 기본값 |
| Event-Driven (이벤트 기반) | 분리된 단일 목적 컴포넌트들이 이벤트에 반응, 비동기·분산 | 높은 확장성이 필요할 때, 컴포넌트 간 결합을 낮추고 싶을 때 |
| Microkernel (마이크로커널) | 핵심 기능 + 플러그인 형태의 확장 기능 | 제품화되어 배포되는 애플리케이션, 확장 기능을 자주 추가/제거할 때 |
| Microservices (마이크로서비스) | 독립적으로 배포·확장 가능한 서비스 단위로 분리 | 서비스별로 독립적 확장성이 필요할 때. 개인 프로젝트에는 대개 과함 |
| Space-Based (공간 기반) | 인메모리 데이터 기반의 극한 확장성 설계 | 매우 높은 트래픽/확장성이 필요한 특수 상황 |

## 사용 절차

1. [문제 분석](../02-problem-analysis/README.md) 산출물(FURPS+ 비기능 요구사항, 특히
   Supportability/Performance)을 놓고 5개 중 후보를 1~2개로 좁힌다.
2. 개인 프로젝트/작은 사이드 프로젝트는 기본적으로 **Layered**에서 시작하고, 명확한
   근거(요구사항)가 없으면 Event-Driven 이상으로 넘어가지 않는다 — 과잉 엔지니어링 방지
   (2단계 Kano 모델에서 "Basic" 항목에 과투자하지 말라는 원칙과 동일한 맥락).
3. 후보가 2개 이상 남으면 [03-tradeoff-evaluation-atam.md](03-tradeoff-evaluation-atam.md)로
   품질속성 시나리오 비교를 한다.
4. 결정은 [adr/](adr/README.md)에 ADR로 남긴다.

## 참고: 이 워크플로우 시스템 자체는?

[ADR-0001](adr/0001-storage-and-interface.md)에서 이미 다뤘듯, 이 프로젝트는 5대 스타일
중 어디에도 깔끔히 들어맞지 않는 "정적 파일 + 외부 툴(Claude Code) 인터페이스" 하이브리드였습니다.
표준 카탈로그가 항상 정답을 주는 건 아니고, **후보를 빠르게 좁히는 출발점**으로 쓰는 것임을
보여주는 사례입니다.

## 출처
- Richards, M., *Software Architecture Patterns*, O'Reilly. [개요](https://marabesi.com/software-architecture/software-architecture-patterns.html)
