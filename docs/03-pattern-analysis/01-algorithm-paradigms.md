# 알고리즘 트랙 — 후보 패턴 도출

문제를 어떤 알고리즘으로 풀지 막막할 때, 임의로 아무 자료구조나 떠올리기보다 **표준
알고리즘 설계 패러다임 4가지**를 체크리스트처럼 훑으면 후보를 빠르게 좁힐 수 있습니다.
CLRS(Cormen/Leiserson/Rivest/Stein)를 비롯한 알고리즘 교재들이 공통으로 쓰는 분류입니다.

## 4대 알고리즘 설계 패러다임

| 패러다임 | 핵심 아이디어 | 적합한 문제 특징 |
|---|---|---|
| Divide and Conquer (분할정복) | 문제를 독립적인 부분문제로 쪼개 각각 풀고 결합 | 부분문제가 서로 독립적일 때. 대용량 데이터에 특히 효율적 |
| Dynamic Programming (동적계획법) | 부분문제를 재귀적으로 풀되 결과를 저장해 중복 계산 제거 | 부분문제가 겹치고(overlapping subproblems), 최적 부분구조(optimal substructure)를 가질 때 |
| Greedy (탐욕법) | 매 단계에서 지역적으로 최선인 선택을 함 | 지역 최적해가 전역 최적해로 이어짐이 증명 가능할 때. 빠르고 단순하지만 항상 전역 최적은 아님 |
| Backtracking (백트래킹) | 제약조건을 만족하는 해를 탐색하며, 막히면 되돌아감 | 제약 충족 문제(constraint satisfaction), 조합 탐색 |

## 사용 절차

1. **[문제 분석](../02-problem-analysis/README.md) 산출물(태그, 제약조건)을 놓고 4개 중
   후보를 1~2개로 좁힌다.** 예: "부분문제가 겹치는가?"에 예라고 답했으면 DP 후보.
2. `docs/catalog/patterns.md`에서 같은 태그의 과거 항목을 검색한다 (구체적 구현 아이디어).
3. 후보가 여전히 2개 이상이면 [03-tradeoff-evaluation-atam.md](03-tradeoff-evaluation-atam.md)의
   시나리오 비교 방식을 간소화해서 적용한다 (시간복잡도 vs 구현 난이도 vs 코드 길이).
4. 선택 근거를 한 줄 기록 — 7단계 회고에서 "왜 이걸 골랐는지" 복기 가능하게.

## 주의: 4대 패러다임에 안 맞는 문제도 많다

[algorithm-track.md](../01-problem-save/algorithm-track.md)의 Two Sum 예시를 4개 패러다임에
대입해보면 어디에도 깔끔히 안 들어맞습니다 — 정답은 해시맵으로 한 번 순회하며 짝을
찾는 것인데, 이건 "설계 패러다임"이라기보다 자주 반복되는 **구현 기법(technique
pattern)**에 가깝습니다. CLRS의 4대 패러다임은 "문제를 어떤 전략으로 접근할지"를
말해주지만, 코딩테스트에 자주 나오는 두 포인터(Two Pointers)/슬라이딩 윈도우(Sliding
Window)/Fast-Slow Pointer 같은 **구체적 구현 기법**은 다루지 않습니다.

그래서 이 저장소에서는 후보 도출 시 두 계층을 모두 확인합니다.

| 계층 | 역할 | 카탈로그 |
|---|---|---|
| 설계 패러다임 (이 문서) | "어떤 전략으로 문제에 접근할까" | Divide and Conquer / DP / Greedy / Backtracking |
| 구현 기법 패턴 | "어떤 구체적 트릭으로 구현할까" | Two Pointers, Sliding Window, Fast & Slow Pointers 등 (Educative *Grokking Coding Interview Patterns* 계열 카탈로그 참고) |

`algorithm-track.md`의 "태그" 필드(예: "해시맵, 투포인터후보")는 대부분 구현 기법 패턴
쪽 태그입니다. 두 계층 중 하나라도 후보가 안 잡히면 다른 계층에서 다시 찾아봅니다.

## 출처
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (CLRS) — 표준 알고리즘
  패러다임 분류의 근거 교재
- [What Are the 4 Types of Algorithms? - DesignGurus](https://www.designgurus.io/answers/detail/what-are-the-4-types-of-algorithm)
- Haq, F., *14 Patterns to Ace Any Coding Interview Question*, Educative/*Grokking Coding
  Interview Patterns* — [DEV Community 정리](https://dev.to/fahimulhaq/14-patterns-to-ace-any-coding-interview-question-d9g)
