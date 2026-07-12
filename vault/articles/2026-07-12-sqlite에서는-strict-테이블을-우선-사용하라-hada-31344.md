---
category: Other
collected_at: '2026-07-12T15:34:08+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31344
id: hada-31344
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- evanhahn.com
title: SQLite에서는 STRICT 테이블을 우선 사용하라
url: https://evanhahn.com/prefer-strict-tables-in-sqlite/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 테이블 정의 끝에 **`STRICT`** 를 추가하면 정수 열에 임의의 텍스트가 들어가는 타입 오류를 조기에 차단해 **데이터 무결성**을 높일 수 있음
- 삽입·갱신 시 타입을 검사하면서도 `'123'`처럼 손실 없이 변환 가능한 값은 허용하며, 열 타입은 **`INT`, `INTEGER`, `REAL`, `TEXT`, `BLOB`, `ANY`** 로 제한됨
- 여러 타입을 담아야 하는 열에는 **`ANY`** 를 지정할 수 있어 엄격한 검증과 유연한 저장을 한 테이블 안에서 함께 적용 가능함
- 기존 테이블을 곧바로 STRICT로 바꿀 수는 없어 **새 테이블 생성과 데이터 복사**가 필요하며, 잘못된 기존 데이터는 정리하거나 형 변환해야 함
- STRICT 테이블은 **SQLite 3.37.0 이상**에서만 지원되며 이론적인 검사 비용은 있지만, 비공식 실험에서는 뚜렷한 성능·파일 크기 차이가 확인되지 않았음

---

## 원문
- [원문](https://evanhahn.com/prefer-strict-tables-in-sqlite/)
- [GeekNews 토론](https://news.hada.io/topic?id=31344)

## My Note
<!-- 한 줄 코멘트 남기기 -->
