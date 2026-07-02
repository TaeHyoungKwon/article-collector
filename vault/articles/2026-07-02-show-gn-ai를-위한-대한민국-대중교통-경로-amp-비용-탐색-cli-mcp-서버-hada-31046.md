---
category: AI
collected_at: '2026-07-02T19:11:59+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31046
id: hada-31046
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/GyeongHoKim
title: 'Show GN: AI를 위한, 대한민국 대중교통 경로 &amp; 비용 탐색 CLI, MCP 서버'
url: https://github.com/GyeongHoKim/naeryeo
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
대중교통 경로 & 비용을 알려주는 CLI 및 MCP 서버입니다

<https://github.com/GyeongHoKim/naeryeo>

homebrew, scoop, npm으로 설치가 가능합니다.  
사용예시 다음과 같습니다.

```
# API 키를 OS 키체인에 등록  
naeryeo setup  
# 경로 출력  
naeryeo route --from "강남역" --to "홍대입구역"  
# MCP 서버 활성화  
naeryeo mcp  
# API 키 삭제  
naeryeo logout
```

지원하는 설치방법은 2가지 입니다.

1. skills + cli
2. mcp 서버

청년매입임대 주택 2차 신청할때 정보 수집을 AI한테 시키려니 회사에서 해당 주택까지 출퇴근 거리나 비용을 계산하는 MCP 서버가 없다는걸 깨달았습니다.  
국내에서 호출할 수 있는 api 중 odsay는 경로 묻는게 되는데 kakao는 안되고, odsay는 지오코딩이 안되는데 kakao는 되더라고요. 그래서 두 개를 적당히 섞었습니다.

## 원문
- [원문](https://github.com/GyeongHoKim/naeryeo)
- [GeekNews 토론](https://news.hada.io/topic?id=31046)

## My Note
<!-- 한 줄 코멘트 남기기 -->
