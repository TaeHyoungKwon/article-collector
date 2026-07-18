---
category: AI
collected_at: '2026-07-18T22:14:33+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31552
id: hada-31552
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/airtaxi
title: 'Show GN: 윈도우의 MSIX를 더블클릭 인스톨러 EXE로 만들어주는 도구를 만들어봤습니다.'
url: https://github.com/airtaxi/AT-Installer/blob/master/MSIX.ko.md
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
MSIX는 Windows의 최신 패키징 포맷입니다. 샌드박스 기반으로 동작해서 레지스트리나 파일 연결 같은 시스템 변경이 격리되고, 삭제하면 잔여물이 하나도 남지 않습니다. MSIXBundle로 x64, x86, ARM64를 하나의 파일에 담을 수도 있고요.

문제는 배포입니다.

MSIX를 스토어 밖에서 설치하려면 사용자가 개발자 모드를 켜고, PowerShell을 열고, 인증서를 신뢰해야 합니다. 개발자한테는 당연한 과정이지만, 일반 사용자한테는 전부 장벽입니다. Electron이나 Tauri로 앱을 만들어도 MSIX 패키징을 지원하지 않는 프레임워크가 많고요.

그래서 만들었습니다. \_\_MSIX Installer Generator\_\_는 MSIX 패키징부터 더블클릭 EXE 인스톨러 생성까지 한 번에 처리하는 도구입니다.

#### 어떻게 시작됐나

원래 이 프로젝트는 MSIX와는 관계가 없었습니다.

WinUI 3로 만든 앱을 스토어 밖에서 배포하려고, `.atp`라는 자체 패키지 포맷을 쓰는 인스톨러 프레임워크를 만들고 있었습니다. 7z로 압축해서 인스톨러에 넘기고, 레지스트리 등록이나 시작 메뉴 바로가기 생성을 인스톨러가 처리하는 구조였습니다. 단순한 EXE 패키징으로는 충분히 잘 동작했고요.

그러던 중에 문득 "MSIX를 쓰면 샌드박스까지 지원하는데, 이걸로 인스톨러를 만들면 어떨까?" 하는 생각이 떠올랐습니다. 기존 `.atp` 방식은 편리하긴 하지만, 결국 레지스트리에 직접 쓰고 AppData에 폴더를 만드는 전통적인 설치 방식이라 깔끔한 삭제가 보장되지 않습니다. MSIX를 쓰면 Windows가 알아서 샌드박스로 격리하고, 삭제할 때 잔여물이 하나도 남지 않잖아요.

그래서 MSIX 설치 지원을 추가하기 시작했는데, 하다 보니 인증서 생성, 매니페스트 작성, 패키징까지 전부 사용자가 직접 해야 한다는 게 문제였습니다. 프레임워크가 MSIX 패키징을 지원하지 않는 경우도 많고요. 결국 패키징까지 자동화하는 도구를 만들게 됐고, 지금은 MSIX 패키징부터 EXE 인스톨러 구성까지 한 번에 처리하는 형태가 됐습니다.

#### 어떤 문제를 풀고 싶었나

MSIX로 배포하려니 사용자 경험이 너무 안 좋았습니다.

- "개발자 모드를 켜세요" → 사용자가 당황
- "PowerShell을 관리자 권한으로 열어서 명령어를 입력하세요" → 더 당황
- "인증서를 신뢰하세요" → 제일 당황

인스톨러를 더블클릭하면 끝나는 전통적인 EXE 인스톨러의 간편함과 MSIX의 샌드박스 이점을 둘 다 가져가고 싶었습니다.

#### MSIX Installer Generator가 하는 일

크게 두 가지입니다.

**1. MSIX 패키징**

인증서 생성, 매니페스트 작성, 빌드 출력 패키징을 GUI에서 처리합니다. 프레임워크가 MSIX 패키징을 지원하지 않아도, 빌드 출력 폴더만 지정하면 됩니다. x64, ARM64 등 아키텍처별 폴더를 추가하면 PE 헤더를 읽어서 자동으로 감지하고, 단일 .msix 또는 다중 아키텍처 .msixbundle을 만들어 냅니다.

**2. EXE 인스톨러 구성**

만들어진 MSIX를 더블클릭 한 번에 설치되는 독립 실행형 EXE 인스톨러로 변환합니다. 사이드로딩에 필요한 모든 과정(인증서 설치, 의존성 처리 등)을 인스톨러가 알아서 처리합니다. 사용자 입장에서는 그냥 인스톨러를 다운로드하고 실행하면 끝입니다. PowerShell도, 개발자 모드도, 인증서 프롬프트도 나오지 않습니다.

#### CLI 도구도 있습니다

GUI 말고 CLI 도구(`aticmsixgen`)도 NuGet에 올려뒀습니다. CI나 AI 자동화 워크플로에서 명령줄로 MSIX 패키징과 EXE 구성을 전부 처리할 수 있습니다. NativeAOT로 빌드해서 런타임 의존성이 없는 단일 실행 파일입니다.

```
dotnet tool install --global aticmsixgen
```

인증서 생성, 매니페스트 작성, MSIX 패키징, EXE 구성까지 전부 CLI에서 됩니다.

#### 이런 분들께 잘 맞습니다

- MSIX로 배포하고 싶은데 사이드로딩 과정이 부담스러운 분
- Electron, Tauri, WPF 등 MSIX 패키징을 기본 지원하지 않는 프레임워크를 쓰는 분
- x64, ARM64 등 여러 아키텍처를 하나의 인스톨러로 배포하고 싶은 분
- CI에서 MSIX 패키징과 EXE 구성을 자동화하고 싶은 분

#### 링크

- GitHub: <https://github.com/airtaxi/AT-Installer>
- Microsoft Store: <https://apps.microsoft.com/detail/9P5GS17TCDQX>
- NuGet (CLI): <https://www.nuget.org/packages/aticmsixgen>

MIT 라이선스이고, 피드백이나 이슈는 GitHub에 남겨주시면 됩니다. 한국어로 남겨주셔도 괜찮습니다.

## 원문
- [원문](https://github.com/airtaxi/AT-Installer/blob/master/MSIX.ko.md)
- [GeekNews 토론](https://news.hada.io/topic?id=31552)

## My Note
<!-- 한 줄 코멘트 남기기 -->
