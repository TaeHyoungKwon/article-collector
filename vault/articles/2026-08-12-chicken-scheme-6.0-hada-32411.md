---
category: Other
collected_at: '2026-08-12T01:37:49+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32411
id: hada-32411
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- code.call-cc.org
title: Chicken Scheme 6.0
url: https://code.call-cc.org/releases/6.0.0/NEWS
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 핵심 시스템에 **R7RS small 전체 모듈**을 포함하고 문자열 내부 표현을 UTF-8로 전환해 완전한 Unicode 문자열을 지원함
- 기존 `(chicken blob)`을 R7RS 호환 **`(chicken bytevector)`** 로 교체했으며, blob 읽기 문법과 여러 u8vector 전용 입출력 절차를 제거함
- 프로세스 API가 PID 대신 **process-object**를 반환하고 파일 잠금이 `flock(2)` 기반으로 바뀌어 기존 코드의 수정이 필요한 호환성 변경이 다수 포함됨
- FFI는 문자열과 심볼을 복사하지 않고 C 코드에 직접 전달하며, **복소수·C struct·union**을 인자와 반환값으로 직접 사용할 수 있음
- 컴파일러의 **클로저 재사용·공유 최적화**와 `configure` 기반 빌드가 추가됐으며, Windows 빌드에는 POSIX 셸과 기본 명령줄 도구가 필요하고 `zig cc`도 지원함

---

## 원문
- [원문](https://code.call-cc.org/releases/6.0.0/NEWS)
- [GeekNews 토론](https://news.hada.io/topic?id=32411)

## My Note
<!-- 한 줄 코멘트 남기기 -->
