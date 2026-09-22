# 기능 요구사항 명세 — EARS 문법

기존에 쓰던 ISO 29148의 5요소(`[조건][주체][행동][대상][제약]`)는 "요구사항에 뭐가 들어가야
하는가"를 말해주지만, "문장을 정확히 어떻게 쓰는가"까지는 규정하지 않습니다. **EARS(Easy
Approach to Requirements Syntax)**는 롤스로이스에서 항공엔진 제어 요구사항을 분석하며
만든 문법으로, 자연어 요구사항의 모호함을 줄이기 위해 5가지 정해진 문장 패턴만 씁니다.

## EARS 5가지 패턴

| 패턴 | 문형 | 언제 쓰는가 |
|---|---|---|
| Ubiquitous (상시) | `The <system> shall <response>` | 항상 성립해야 하는 규칙 |
| Event-driven (이벤트 기반) | `When <trigger>, the <system> shall <response>` | 특정 사건이 트리거일 때 |
| State-driven (상태 기반) | `While <state>, the <system> shall <response>` | 특정 상태 동안 계속 성립 |
| Unwanted behavior (예외/금지) | `If <unwanted condition>, then the <system> shall <response>` | 에러/예외 처리 |
| Optional feature (선택 기능) | `Where <feature is included>, the <system> shall <response>` | 특정 기능이 있을 때만 |

복합 조건은 `While <precondition>, When <trigger>, the <system> shall <response>` 형태로
조합 가능합니다.

## 우리 프로젝트 요구사항을 EARS로 재작성

기존 FR1~FR3([applied-example.md](applied-example.md) 참고)를 EARS 문형으로 다시 쓰면:

```
FR1 (Event-driven): When 사용자가 새 문제/프로젝트를 시작하면,
                     the 시스템은 shall 트랙(알고리즘/실무)에 맞는 저장 템플릿을 제공한다.

FR2 (Event-driven): When 사용자가 패턴을 검색하면,
                     the 시스템은 shall 태그/키워드로 일치하는 카탈로그 항목을 반환한다.

FR3 (Event-driven): When 유지보수 단계가 완료되면,
                     the 시스템은 shall 회고 내용을 카탈로그/체크리스트에 추가하는
                     진입점을 제공한다.

FR1-예외 (Unwanted behavior): If 필수 필드가 비어 있으면,
                     then the 시스템은 shall 다음 단계로 진행을 막는다.
```

EARS로 다시 쓰니 원래는 암묵적이었던 "FR1의 예외 케이스"가 별도 요구사항으로 명시적으로
드러납니다 — 이게 EARS를 쓰는 실질적 이득입니다.

## 이 저장소에서의 규칙

1. 새 요구사항은 항상 5가지 패턴 중 하나로 작성한다.
2. 조건/트리거가 여러 개 겹치면 패턴을 조합하되, 한 문장에는 `shall` 이후 행동 하나만
   남긴다 (기존 IEEE 830 규칙과 동일 원칙).
3. `docs/catalog/checklist.md`에 "EARS 패턴을 따르는가?"를 검증 항목으로 추가한다.

## 출처
- [Easy Approach to Requirements Syntax - Wikipedia](https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax)
- Mavin, A., Wilkinson, P. et al., *Easy Approach to Requirements Syntax (EARS)*, IEEE RE'09.
  [원문 PDF](https://ccy05327.github.io/SDD/08-PDF/Easy%20Approach%20to%20Requirements%20Syntax%20(EARS).pdf)
