# 구현 방식 — TDD Red-Green-Refactor

Kent Beck이 *Test-Driven Development: By Example*(2002)에서 정식화한 순환입니다. 4단계
스켈레톤(브루트포스/Walking Skeleton)을 "제대로" 만드는 5단계의 기본 리듬으로 씁니다.

## 3단계 순환

| 단계 | 하는 일 |
|---|---|
| Red | 아직 통과 못 하는 테스트를 먼저 쓴다 — 이 코드가 뭘 해야 하는지 정의 |
| Green | 테스트를 통과시키는 **최소한의** 코드만 쓴다 — 구조나 최적화는 무시 |
| Refactor | 동작은 그대로 두고 구조·가독성만 개선 |

한 사이클은 보통 1~10분 정도로 짧게, 하루에도 여러 번 반복합니다.

## 이 워크플로우에 적용

- **알고리즘 트랙**: [4단계 브루트포스](../04-pattern-implementation/01-algorithm-track-skeleton.md)가
  이미 "Red(예제 입출력 테스트) → Green(브루트포스로 통과)"까지 온 상태입니다. 5단계는
  **Refactor 자리에 "최적화"를 넣은 변형**입니다 — 3단계에서 고른 패러다임으로 다시
  구현하고, 브루트포스와 결과가 같은지 테스트로 고정합니다.
- **프로젝트 트랙**: 새 기능 하나마다 이 3단계 순환을 그대로 적용. 2단계 EARS
  Unwanted-behavior 요구사항이 Red 단계의 테스트 후보가 됩니다.

## 출처
- Beck, K., *Test-Driven Development: By Example* (2002)
- [TDD: Red-Green-Refactor cycle for code that holds - KERN-IT](https://www.kern-it.be/en/definitions/tdd/)
- [Test Driven Development - Martin Fowler](https://www.martinfowler.com/bliki/TestDrivenDevelopment.html)
