---
category: Dev Tools
collected_at: '2026-05-13T11:14:12+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=29456
id: hada-29456
matched_keywords:
- Claude Code
read: false
recommend_score: -996.614
recommended_on: '2026-05-13'
source: geeknews
tags:
- Dev Tools
- Other
- macwelt.de
title: 새로운 Mac 스틸러가 Claude에서 Apple 지원으로 위장하고 있습니다
url: https://www.macwelt.de/article/3135791/neuer-mac-stealer-tarnt-sich-als-apple-support-auf-claude.html
---

## TL;DR
- 새로운 Mac 스틸러는 Claude 채팅창에서 Apple 지원을 사칭하여 맥 사용자를 타겟으로 하고 있다.
- 공격자는 가짜 채팅을 통해 사용자가 악성 터미널 명령어를 실행하도록 유도하여 정보를 탈취한다.
- 이는 사용자에게 보안 의식을 강화할 필요성을 시사하며, 최신 macOS 업데이트와 보안 대책 유지의 중요성을 강조한다.

## GeekNews 요약
보안 연구원들과 'Bleeping Computer'는 최근 맥 사용자를 겨냥한 새로운 공격 방식을 발견했습니다. 공격자들은 공유된 클로드(Claude) 채팅창 내에서 애플 지원팀(Apple Support)을 사칭하며, 맥에 '클로드 코드(Claude Code)' 소프트웨어를 설치하는 방법을 안내하며 접근합니다.

#### 공격 방식 및 특징

- **터미널 명령 유도:** 가짜 채팅을 통해 사용자가 터미널 명령어를 복사하여 실행하도록 유도합니다. 이 명령어를 실행하면 '클로드 코드' 환경이 구축되는 것처럼 보이지만, 실제로는 백그라운드에서 악성코드를 다운로드하여 셸 스크립트에 기록합니다.
- **지역 선별:** 일부 변종은 감염된 컴퓨터에 러시아어 또는 구소련 독립국가연합(CIS) 지역 키보드가 설정되어 있는지 확인합니다. 해당 지역일 경우 악성코드는 스스로 종료됩니다.
- **휘발성 설치:** 이 악성코드는 주로 메모리(RAM) 내에서 실행되므로 영구 저장 장치에 명확한 흔적을 거의 남기지 않습니다.
- **데이터 탈취:** 설치된 소프트웨어는 로그인 정보, 쿠키, macOS 키체인 콘텐츠 등을 수집하여 공격자의 서버로 전송합니다. 보안 전문가 Berk Albayrak은 이를 'MacSync'의 변종으로 식별했습니다.

#### 대응 및 예방

이와 유사한 공격은 2025년 12월 ChatGPT와 Grok을 통해서도 발생한 바 있습니다. 애플은 최신 보안 대책을 지속적으로 강화하고 있습니다.

- **시스템 경고:** macOS 26.4 버전부터는 외부에서 복사한 명령어를 터미널에 붙여넣을 때 시스템 차원의 경고 메시지가 표시됩니다.
- **최신 업데이트 유지:** macOS를 항상 최신 버전으로 업데이트하고, 타사 백신 소프트웨어를 최신 상태로 유지하는 것이 권장됩니다.

## 원문
- [원문](https://www.macwelt.de/article/3135791/neuer-mac-stealer-tarnt-sich-als-apple-support-auf-claude.html)
- [GeekNews 토론](https://news.hada.io/topic?id=29456)

## My Note
<!-- 한 줄 코멘트 남기기 -->
