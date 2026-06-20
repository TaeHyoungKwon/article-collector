---
category: Other
collected_at: '2026-06-20T09:51:17+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30653
id: hada-30653
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- jvm-weekly.com
title: 'Project Valhalla 설명: 10년 작업이 JDK 28에 도착하는 방식'
url: https://www.jvm-weekly.com/p/project-valhalla-explained-how-a
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Oracle 엔지니어 Lois Foltan이 **JEP 401: Value Classes and Objects**의 OpenJDK 메인 저장소 통합과 JDK 28 타깃을 확인하며, Valhalla가 실제 JDK preview로 들어가는 단계에 도달함
- 핵심 목표는 Java 객체를 “클래스처럼 코딩하고 int처럼 동작”하게 만들어 **객체 헤더·힙 할당·GC·포인터 간접 참조** 비용을 줄이는 것임
- JDK 28의 value class는 아직 **null 가능한 참조 타입**이며, non-null 타입·전문화 제네릭·128비트 인코딩은 포함되지 않고 `--enable-preview`가 필요함
- JVM은 value object를 **스칼라화**하거나 필드·배열에 **힙 평탄화**할 수 있지만, erased generic이나 `Object` 같은 상위 타입에서는 힙 객체로 materialize될 수 있음
- Java 개발자는 identity와 value의 차이를 코드 설계에 반영해야 하며, `==`, `synchronized`, primitive wrapper, 배열 성능, 향후 제네릭 전문화까지 영향이 이어짐

---

## 원문
- [원문](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a)
- [GeekNews 토론](https://news.hada.io/topic?id=30653)

## My Note
<!-- 한 줄 코멘트 남기기 -->
