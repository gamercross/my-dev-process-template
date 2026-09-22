# 엣지 케이스 테스트 설계 — 동등분할 + 경계값 분석

지금까지 "엣지 케이스를 나열한다"고만 해왔는데, **뭘 엣지 케이스로 쳐야 하는지**를
체계적으로 뽑는 표준 기법 두 가지가 있습니다. 둘 다 ISO/IEC/IEEE 29119(소프트웨어
테스트 국제표준)이 분류하는 명세 기반(specification-based) 기법입니다.

## 동등분할 (Equivalence Partitioning)

입력 범위를 "같은 방식으로 처리될 것"으로 기대되는 부분집합(equivalence class)으로
나눕니다. 예: `1 ≤ n ≤ 100`이면 세 구간(유효: 1~100, 무효: n<1, 무효: n>100) — 각
구간에서 대표값 하나씩만 테스트하면 됩니다.

## 경계값 분석 (Boundary Value Analysis)

동등분할이 나눈 **경계 지점**을 집중적으로 테스트합니다 — 실무 경험상 버그는 구간
가운데보다 경계에서 훨씬 자주 생깁니다. 위 예시라면 `n=0, 1, 2`(하한 경계 안팎)와
`n=99, 100, 101`(상한 경계 안팎)을 테스트합니다.

## 이 저장소의 규칙

2단계 [Planguage 정량화](../02-problem-analysis/03-quantification-planguage.md)에서
이미 제약조건에 숫자(`Scale`)를 넣어뒀다면, 그 숫자마다 동등분할 → 경계값 순으로
테스트 케이스를 뽑습니다:

```
1. 제약조건에서 구간 나누기 (동등분할)
2. 각 구간 경계값 ±1 테스트 (경계값 분석)
3. 2단계 EARS Unwanted-behavior 요구사항과 매칭되는지 확인
```

### Two Sum 예시

[algorithm-track.md](../01-problem-save/algorithm-track.md) 제약조건
`2 ≤ len(nums) ≤ 10^4`에 적용하면:
- 동등분할: len < 2(무효) / 2 ≤ len ≤ 10^4(유효) / len > 10^4(무효)
- 경계값: len = 1, 2, 3 / len = 9999, 10000, 10001

## 출처
- [Software Testing - Boundary Value Analysis vs Equivalence Partitioning - GeeksforGeeks](https://www.geeksforgeeks.org/software-testing/software-testing-boundary-value-analysis-vs-equivalence-partitioning/)
- ISO/IEC/IEEE 29119 (Software Testing) — 명세 기반 테스트 설계 기법 분류
- [Boundary Value Analysis & Equivalence Partitioning - SoftwareTestingHelp](https://www.softwaretestinghelp.com/what-is-boundary-value-analysis-and-equivalence-partitioning/)
