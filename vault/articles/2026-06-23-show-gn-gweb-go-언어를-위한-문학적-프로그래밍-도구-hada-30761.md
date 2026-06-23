---
category: Other
collected_at: '2026-06-23T21:15:22+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30761
id: hada-30761
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/sjnam
title: 'Show GN: GWEB: Go 언어를 위한 문학적 프로그래밍 도구'
url: https://github.com/sjnam/gweb
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
**GWEB**은 Go 언어를 위한 문학적 프로그래밍(Literate Programming) 시스템입니다. 도널드 커누스(Donald Knuth)의 CWEB 구조를 긴밀하게 모델링하여 개발되었습니다.  
개발자는 하나의 `.w` 소스 파일에 TeX 문서(설명)와 Go 코드를 병행하여 작성합니다. 이 파일은 기계와 사람을 위한 두 가지 결과물로 변환됩니다.

#### 핵심 도구와 기능

GWEB 시스템은 크게 두 가지 핵심 명령어로 작동합니다.

- **gtangle**: 문서 설명을 제외하고 Go 코드 섹션만 모아 컴파일 가능한 .go 파일을 생성합니다. 출력 시 자동으로 gofmt 스타일로 포맷팅됩니다.
- **gweave**: 사람이 읽기 좋은 아름다운 조판 문서(.tex ➡️ PDF)를 생성합니다. 예약어는 굵게, 식별자는 이탤릭으로 표현되며 교차 참조 인덱스가 자동 생성됩니다.

#### 주요 특징 및 장점

- **직관적인 포맷**: `//line` 지시어를 기본으로 지원하여 컴파일 에러나 패닉 발생 시 `.go` 파일이 아닌 원본 `.w` 파일의 줄 위치를 정확히 안내합니다.
- **Self-Hosting 시스템**: GWEB 자체도 문학적 프로그래밍 방식으로 개발되었습니다. `lit/` 폴더 안의 `.w` 파일들이 GWEB의 실제 소스 원본입니다.
- **에디터 지원**: VS Code, Vim, Emacs 사용자를 위한 구문 강조(Syntax Highlighting) 설정 기능을 함께 제공합니다.

GWEB을 사용하면 복잡한 Go 프로젝트의 설계 의도와 알고리즘을 한 편의 책을 쓰듯 우아하게 기록하고 관리할 수 있습니다.

## 원문
- [원문](https://github.com/sjnam/gweb)
- [GeekNews 토론](https://news.hada.io/topic?id=30761)

## My Note
<!-- 한 줄 코멘트 남기기 -->
