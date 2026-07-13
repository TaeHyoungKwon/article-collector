---
category: Other
collected_at: '2026-07-14T00:08:23+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31401
id: hada-31401
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- n2c.bini59.dev
title: 'Show GN: Notion 일정을 구글/애플 캘린더에서 구독하기 — 오픈소스 iCal 브릿지'
url: https://n2c.bini59.dev
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Notion으로 일정을 관리하는데 이걸 애플 캘린더에서 보고 싶었습니다. 그런데, Notion Calendar는 외부 캘린더가 구독할 수 있는 .ics 내보내기를 지원하지 않더라고요. 상용 서비스는 유료고.. 그래서 하나 만들어봤습니다.

Notion 데이터베이스를 표준 iCal(.ics) 피드로 뽑아주는 브릿지입니다. 캘린더 앱이 이 URL을  
구독하면 Notion 일정이 그대로 올라옵니다.

아래 기능을 제공합니다:

- Notion DB를 연결하여 캘린더를 설정.
- 어떤 속성을 제목·시작일·종료일·설명·장소에 붙일지 지정.
- 설명은 속성 값, 페이지 본문을 인식하도록 하였습니다.
- 필터 기능을 지원합니다(select/status/checkbox/relation). 필터를 지정하면 지정한 필터의 항목만 가져오도록 합니다.
- 캘린더 구독을 하기 때문에, URL이 유출되면 캘린더가 유출됩니다. URL 유출시 재설정 기능을 사용해주세요.

주의점:

- 모바일에서 연결하려 하면 Notion 앱이 인증을 가로채는 문제가 있어, 최초 셋업은 데스크톱을 추천합니다.

<https://github.com/bini59/318_notion_calander>  
notion을 등록하는 것에 거부감이 있으시면, 위 깃허브에서 레포를 받아 사용하실 수 있습니다.  
배포 방법은 README를 참조하시면 되겠습니다.

## 원문
- [원문](https://n2c.bini59.dev)
- [GeekNews 토론](https://news.hada.io/topic?id=31401)

## My Note
<!-- 한 줄 코멘트 남기기 -->
