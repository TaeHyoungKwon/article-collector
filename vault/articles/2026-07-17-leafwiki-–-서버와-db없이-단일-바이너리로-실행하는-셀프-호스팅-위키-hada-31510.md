---
category: AI
collected_at: '2026-07-17T09:31:02+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31510
id: hada-31510
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- leafwiki.com
title: LeafWiki – 서버와 DB없이 단일 바이너리로 실행하는 셀프 호스팅 위키
url: https://leafwiki.com/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 런북, 홈랩 문서, 튜토리얼, 팀 노트를 **폴더 트리 구조**로 정리하는 사람들을 위한 도구
- 콘텐츠를 디스크에 `.md` 파일로 저장하고 **단일 Go 바이너리**로 동작해 웹서버/DB 없이 실행되며 리눅스/맥/윈도우/라즈베리 파이 지원
- 페이지는 항상 일반 파일로 저장되어 앱 없이도 읽기 가능하고, grep 검색 가능하며, 백업은 `cp -r`만으로 처리
  - 링크/태그/검색 인덱스 같은 메타데이터는 파일 옆의 경량 SQLite에 저장
- 라이브 프리뷰(Markdown 원문과 렌더링 결과를 **나란히 실시간 표시**) / 단축키 / 내부 링크 자동완성을 갖춘 내장 에디터 제공
  - **자동 저장**, `Ctrl+V` 이미지 붙여넣기 자동 업로드/링크, `[[wikilink]]` Obsidian 호환 자동완성
  - 표, 작업 목록, 각주, 콜아웃(`:::info`/`:::warning`), **Mermaid 다이어그램**, KaTeX 수식 지원
- admin/editor/viewer **역할 기반 권한** 제공. CSRF 보호/인증 레이트 리미팅 기본 활성화
- **트리 내비게이션**으로 전체 구조를 계속 볼수 있고, 태그 필터 전체 텍스트 검색(`Ctrl+Shift+F`), 빠른 이동(`Ctrl+Alt+P`) 지원
- **리비전 히스토리**로 모든 저장을 기록, 한 번의 클릭으로 이전 버전 복원 가능
- **백링크 추적**으로 페이지 이름 변경/이동 시 기존 링크 자동 갱신, 깨진 링크는 페이지별로 표시
- **세 가지 실행 모드** 지원 : 로그인 필요한 사설 위키 / 누구나 읽을 수 있는 퍼블릭 문서 사이트 / 인증 없는 로컬 노트패드
- Wiki.js나 Outline이 과하다고 느끼는 소규모 팀/홈랩용
- MIT 라이선스

## 원문
- [원문](https://leafwiki.com/)
- [GeekNews 토론](https://news.hada.io/topic?id=31510)

## My Note
<!-- 한 줄 코멘트 남기기 -->
