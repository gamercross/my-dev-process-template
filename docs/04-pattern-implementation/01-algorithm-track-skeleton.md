# 알고리즘 트랙 — 스켈레톤 방향

## "Make it work, make it right, make it fast"

코딩 커뮤니티에서 흔히 Kent Beck의 원칙으로 인용되는 3단계 진행 방식입니다. 4단계
(패턴 구현)는 이 중 **첫 단계("work")**만 담당합니다 — 3단계에서 고른 패러다임이
맞는 방향인지, 최적화 없이 무차별 대입(brute force)으로 먼저 정답을 만들어 확인합니다.

| 단계 | 목표 | 어느 워크플로우 단계 |
|---|---|---|
| Make it work | 작은 입력에서 정답만 나오면 됨. 효율은 무시 | **4단계 (여기)** |
| Make it right | 구조를 정리하고 가독성을 높임 | 5단계 |
| Make it fast | 3단계에서 고른 패러다임으로 실제 최적화 | 5단계 |

## 왜 브루트포스부터 시작하는가

브루트포스는 가능한 모든 경우를 체계적으로 시도하는 가장 단순한 전략입니다 — 비효율
적이지만 정확성이 검증하기 쉬워서, "이 문제를 제대로 이해했는가"부터 확인하기에
좋은 출발점입니다. 예외: 입력 크기가 너무 커서 브루트포스조차 못 돌리는 게 뻔하면
이 단계를 생략하고 바로 5단계 최적화로 갈 수 있습니다.

## 브루트포스를 나중까지 남겨두는 이유 — 차등 테스트(Differential Testing)

브루트포스 버전을 지우지 말고 **정답 오라클(oracle)**로 남겨두면, 5단계에서 최적화한
버전과 결과를 자동으로 비교하는 스트레스 테스트를 만들 수 있습니다: 무작위 입력
생성기로 여러 케이스를 만들고, 브루트포스와 최적화 버전의 출력이 일치하는지 확인하는
방식입니다.

## Two Sum 예시로 보는 흐름

[algorithm-track.md](../01-problem-save/algorithm-track.md)의 Two Sum 예시를 이 방식으로
진행하면:

```
4단계 (여기): 이중 루프 O(n^2) 브루트포스 — 모든 쌍을 확인. 정답만 확인, 느려도 됨.
5단계:        해시맵 O(n) 최적화 — 3단계에서 찾은 "기법 패턴"(해시맵) 적용.
              브루트포스와 결과 비교하는 테스트 추가.
```

## 출처
- "Make it work, make it right, make it fast" — Kent Beck 원칙으로 널리 인용됨
- [Why You Can't Optimize Your Initial Solutions in Coding Problems - AlgoCademy](https://algocademy.com/blog/why-you-cant-optimize-your-initial-solutions-in-coding-problems/)
- [Brute Force - 30 Days Coding](https://blogs.30dayscoding.com/blogs/dsa/problem-solving-and-competitive-programming/problem-solving-strategies/brute-force/) (차등 테스트 관행 포함)
