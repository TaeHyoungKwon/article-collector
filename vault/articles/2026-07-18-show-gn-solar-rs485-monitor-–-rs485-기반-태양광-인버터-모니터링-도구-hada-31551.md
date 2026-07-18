---
category: Other
collected_at: '2026-07-18T21:13:32+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31551
id: hada-31551
matched_keywords: []
read: false
recommend_score: 0.693
source: geeknews
tags:
- Other
- github.com/call518
title: 'Show GN: Solar-RS485-Monitor – RS485 기반 태양광 인버터 모니터링 도구'
url: https://github.com/call518/Solar-RS485-Monitor
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
집에 설치한 태양광 인버터의 실시간 발전량과 누적 발전량을 직접 확인하기 위해 만든 오픈소스 프로젝트입니다.

Raspberry Pi와 USB-RS485 어댑터를 이용해 인버터 데이터를 수집하고, 전압·전류·출력·역률·주파수·누적 발전량·고장 코드 등을 파싱합니다.

수집한 데이터는 필요에 따라 다음 대상으로 저장하거나 시각화할 수 있습니다.

- SQLite
- Google Sheets
- ThingSpeak
- MariaDB
- OpenSearch / Elasticsearch
- Supabase
- Streamlit 대시보드
- Telegram 장애 알림

현재 InoElectric IEPVS-3.5-G1/G2 인버터를 기준으로 직접 연결하고 동작을 검증했습니다. 다른 인버터는 요청 프레임과 응답 파싱 규칙을 해당 모델에 맞게 수정해야 합니다.

제조사 클라우드에 의존하지 않고 태양광 발전 데이터를 직접 수집·저장·활용하는 방법을 정리한 프로젝트이며, 비슷한 환경에서 태양광 인버터를 직접 모니터링하려는 분들에게 참고가 되었으면 합니다.

## 원문
- [원문](https://github.com/call518/Solar-RS485-Monitor)
- [GeekNews 토론](https://news.hada.io/topic?id=31551)

## My Note
<!-- 한 줄 코멘트 남기기 -->
