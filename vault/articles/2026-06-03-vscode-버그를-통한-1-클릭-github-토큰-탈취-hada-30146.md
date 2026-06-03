---
category: Other
collected_at: '2026-06-03T19:36:07+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30146
id: hada-30146
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- blog.ammaraskar.com
title: VSCode 버그를 통한 1-클릭 GitHub 토큰 탈취
url: https://blog.ammaraskar.com/github-token-stealing/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **github.dev**는 github.com에서 전달받은 OAuth 토큰으로 브라우저 VSCode에서 파일 열람, PR, 커밋을 수행하며, 이 토큰이 특정 저장소로 제한되지 않아 사용자가 접근 가능한 저장소 전체를 읽고 쓸 수 있음
- VSCode webview는 `vscode-webview://...` iframe으로 격리하지만, 키보드 단축키 UX를 위해 webview의 `keydown`을 `did-keydown` 메시지로 메인 창에 전달하면서 **신뢰되지 않은 스크립트**가 사용자 키 입력처럼 이벤트를 보낼 수 있음
- 임의 텍스트 입력은 HTML `<input>` 때문에 통하지 않지만, 기본 단축키 `Ctrl`+`Shift`+`A`와 추천 확장 설치 알림, **local workspace extensions** 및 커스텀 키바인딩을 조합해 확장 설치 명령을 실행할 수 있음
- PoC는 **Jupyter notebook**의 마크다운 셀에서 JavaScript를 실행해 추천 확장 설치를 수락하고, 새 키바인딩으로 선택한 확장을 설치한 뒤 GitHub API 토큰과 비공개 저장소 목록을 표시함
- 데스크톱 VSCode도 같은 취약점이 있지만 공격자는 저장소 복제와 notebook 열기를 유도해야 하며, github.dev 사용자는 사이트 데이터를 지워 초기 확인 대화상자가 다시 나오게 하는 방어가 필요함

---

## 원문
- [원문](https://blog.ammaraskar.com/github-token-stealing/)
- [GeekNews 토론](https://news.hada.io/topic?id=30146)

## My Note
<!-- 한 줄 코멘트 남기기 -->
