# 비기능 요구사항 정량화 — Gilb's Planguage

**FURPS+**(1단계/2단계 다른 문서에서 계속 나오는 약어)는 비기능 요구사항을 Functionality
/ Usability / Reliability / Performance / Supportability(+ 기타 제약) 5범주로 분류하는
모델입니다. FURPS+ 규칙("정성적 표현 금지, 측정 가능한 숫자로")은 원칙만 말해주고
"어떻게 숫자로 만드는가"는 안 알려줍니다. Tom Gilb의 **Planguage**는 "정량화할 수 없으면
통제할 수 없다(If you can't quantify it, you can't control it)"는 원칙 아래, FURPS+로
분류된 비기능 요구사항을 정확히 숫자로 못박는 표준 필드를 제공합니다.

## Planguage 핵심 필드

Planguage 원전은 Budget, Record, Trend, Fail, Survival 등 더 많은 필드를 정의하지만,
개인 프로젝트에는 과합니다. 이 저장소에서는 실용적으로 아래 6개만 씁니다.

| 필드 | 의미 |
|---|---|
| Scale | 측정 단위 (예: "초", "%", "MB") |
| Meter | 실제로 어떻게 측정할 것인가 (예: "stopwatch로 측정", "git log 커밋 시각 차이") |
| Past | 현재/과거 수준 (baseline) |
| Goal | 이번에 달성해야 하는 최소 기준 (이걸 못 채우면 요구사항 미충족) |
| Stretch | 더 바람직한 수준 |
| Wish | 이상적이지만 지금 당장은 무리인 수준 |

> 프로젝트가 커져서 여러 사람이 같은 요구사항을 다른 기준으로 해석하는 문제가 생기면,
> 그때 Budget(자원 한도)·Fail(이 아래로 떨어지면 실패)·Survival(생존 최소선) 필드를
> 추가로 도입한다.

## 우리 프로젝트 NFR을 Planguage로 재작성

기존 FURPS+ 표의 막연했던 항목들을 아래처럼 못박습니다.

### Usability — "각 단계 템플릿은 5분 이내 작성 가능"

```
Scale: 템플릿 1개 작성에 걸리는 시간(분)
Meter: 실제로 타이머를 켜고 템플릿을 채워보며 측정
Past: (아직 측정 안 함 — 최초 사용 시 기록)
Goal: 5분 이내
Stretch: 3분 이내
```

### Supportability — "새 트랙 추가 시 기존 구조 무변경으로 확장 가능"

```
Scale: 새 트랙 추가 시 수정해야 하는 기존 "핵심 로직" 파일 수(개) —
  .claude/skills/dev-workflow/SKILL.md와 implementations/ 아래 코드만
  해당. 트래커(sessions/README.md)·진행상황 표·worklog.md처럼 새 항목을
  저장할 때마다(트랙이 새로운지와 무관하게) 매번 갱신하는 기록용 파일은
  제외한다.
Meter: git diff --stat으로 새 트랙 추가 커밋에서 변경된 파일을 세고, 위
  기준으로 핵심 로직/기록용을 분류한다.
Goal: 핵심 로직 파일 0개 (신규 파일만 추가)
Stretch: 해당 없음 (0이 이미 최선)
```

> **실측(2026-09-22, 세 번째 트랙 `learning-track.md` 추가)**: 핵심 로직
> 파일(SKILL.md, `implementations/` 코드) **0개 수정** — Goal 달성.
> `docs/01-problem-save/sessions/README.md`(트래커) 등 기록용 파일은
> 예정대로 수정됨(신규 트랙 여부와 무관한 정상 동작). 위 "핵심 로직 파일만
> 센다"는 구분 자체가 이번 실측 과정에서 명확해졌다 — 원래 Scale은
> "기존 파일 수"라고만 적혀 있어서 기록용 파일까지 포함하면 이 Goal은
> 애초에 달성 불가능했다(항목을 저장할 때마다 트래커가 바뀌므로). 자세한
> 경위는 [worklog.md](../00-overview/worklog.md)의 2026-09-22 항목 참고.

### Reliability — "저장 데이터 유실 방지"

```
Scale: 데이터 유실 사고 건수
Meter: git log 이력 확인 (force-push, reset --hard 등 이력 파괴 행위 여부)
Goal: 0건
Wish: 모든 변경 이력이 영구 보존됨 (git 자체가 이미 이 조건을 만족)
```

## 이 저장소에서의 규칙

- 비기능 요구사항(FURPS+ 표)에는 최소한 `Scale`, `Meter`, `Goal` 세 필드를 반드시 채운다.
- "빠르다/편하다/견고하다" 같은 표현이 나오면 반드시 이 문서 형식으로 재작성한다.

## 출처
- Gilb, T., *Specifying Quality Requirements With Planguage*, [ModernAnalyst](https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/2926/Specifying-Quality-Requirements-With-Planguage.aspx)
- Gilb, T., *How to Quantify Quality: Finding Scales of Measure*, [ACCU Overload 13(70)](https://www.accu.org/journals/overload/13/70/gilb_299/)
