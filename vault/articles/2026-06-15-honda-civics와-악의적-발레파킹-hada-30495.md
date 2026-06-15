---
category: AI
collected_at: '2026-06-15T09:49:00+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30495
id: hada-30495
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- juniperspring.org
title: Honda Civics와 악의적 발레파킹
url: https://juniperspring.org/posts/honda-evil-valet/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 2021년형 Honda Civic **헤드유닛**은 USB 업데이트 경로에서 공개 AOSP 테스트 키로 서명된 업데이트를 받아들일 수 있어, 물리 접근자가 임의 코드를 실행할 수 있음
- Honda의 업데이트는 Android recovery를 통해 적용되며, `recovery` 바이너리가 수정됐어도 **`verify_file` 서명 검증 로직**은 기본 AOSP와 일치함
- 공개 AOSP 테스트 키로 서명하고 USB 드라이브 형식을 맞추면 `su`와 `setuid` 없이도 원하는 코드를 설치할 수 있으며, 이를 **EvilValet** 공격으로 부름
- 새 도구 **ota-builder** 는 헤드유닛이 받아들이는 업데이트 파일 준비를 쉽게 하며, **apk-rebuilder** 는 업데이트 파일을 역공학에 필요한 출력 트리로 변환함
- 프로젝트는 조사 작업 대부분을 마쳤지만 저장소는 중단되지 않았으며, 버전 정보·툴체인·커스텀 테마·AIDL 매핑 개선에 기여가 필요함

---

## 원문
- [원문](https://juniperspring.org/posts/honda-evil-valet/)
- [GeekNews 토론](https://news.hada.io/topic?id=30495)

## My Note
<!-- 한 줄 코멘트 남기기 -->
