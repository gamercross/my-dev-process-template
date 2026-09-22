# PRD 템플릿 (문제 저장 + 문제 분석 확장판)

프로젝트 트랙에서 규모가 커지면 `project-track.md`만으로는 부족할 수 있습니다. 이때 PRD로
확장합니다. 두 가지 검증된 스타일 중 상황에 맞게 고릅니다.

## 언제 PRD로 확장하는가

"규모가 커지면"을 감으로 판단하지 않고 [scope-tiers.md](../00-overview/scope-tiers.md)
등급으로 정합니다:

- **Full 등급 + 프로젝트 트랙**만 PRD 대상. Xpress/Lite/즉시처리는 절대 안 씀
  (`project-track.md`로 충분하거나 그마저 생략)
- Full 등급 중에서도 **개인 프로젝트/빠른 검증**이면 경량형, **이해관계자가 여럿이거나
  장기 프로젝트**면 상세형 — 아래 "선택 기준" 참고

## 경량형 — Google 원페이지 스타일 (기본 권장)

```
Feature Overview:
Business Justification:
Technical Architecture:
Security & Compliance:
Testing Strategy:
```

개인 프로젝트나 빠른 검증에는 이 정도로 충분합니다.

## 상세형 — Atlassian 스타일 (팀/이해관계자가 많을 때)

경량형 항목 + 아래 추가:

```
Participants(관련자):
Status(현재 상태):
Background & Strategic Fit(왜 하는가, 전체 목표와의 연관성):
User Stories:
UX 설계:
Scoping(범위):
```

## 선택 기준

- 개인 프로젝트, 빠른 검증 → 경량형
- 협업, 이해관계자 다수, 장기 프로젝트 → 상세형으로 확장
