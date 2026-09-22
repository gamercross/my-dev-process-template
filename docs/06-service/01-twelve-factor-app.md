# 프로젝트 트랙 — 배포 방향 (Twelve-Factor App)

Heroku 공동창업자 Adam Wiggins가 수백만 개의 앱을 운영한 경험을 정리해 만든
**Twelve-Factor App** 방법론입니다. 개인 프로젝트라도 이 중 몇 가지만 지켜도 배포·운영
사고를 크게 줄입니다. 12개 전부를 외울 필요는 없고, 아래 5개가 개인 프로젝트에 가장
자주 문제가 됩니다.

## 개인 프로젝트에 우선 적용할 5가지

| 요소 | 규칙 | 이걸 어기면 생기는 문제 |
|---|---|---|
| Config | 설정(API 키, DB 주소 등)은 환경변수로, 코드에 하드코딩하지 않는다 | 키가 git에 커밋되어 유출 |
| Backing Services | DB·캐시 등은 "붙였다 뗄 수 있는 자원"으로 취급 (연결 정보만 설정으로) | 로컬↔배포 환경 전환 시 코드 수정 필요 |
| Build, Release, Run | 빌드(코드+의존성 묶기) / 릴리즈(빌드+설정 결합) / 실행 단계를 분리 | 배포 중 설정만 바꾸고 싶은데 재빌드해야 함 |
| Processes | 상태를 프로세스 안에 저장하지 않는다(stateless) | 재시작하면 데이터 유실, 여러 인스턴스로 못 늘림 |
| Logs | 로그는 표준출력으로 흘려보내고, 파일 관리는 실행 환경에 맡긴다 | 로그 파일이 무한히 쌓여 디스크 가득 참 |

## 이 저장소 자체에 적용하면

이 워크플로우 시스템(`.claude/skills/dev-workflow/`)은 배포되는 서비스가 아니라 로컬
도구라 12요소 대부분은 해당 없습니다. 그래도 **Config** 원칙은 유효합니다 — 나중에
GitHub 토큰이나 API 키가 필요한 기능을 추가하게 되면, SKILL.md나 저장소 파일에
하드코딩하지 말고 환경변수로 참조해야 합니다.

## 출처
- Wiggins, A., *The Twelve-Factor App* — [12factor.net](https://12factor.net/)
- [Twelve-Factor App methodology - Wikipedia](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology)
