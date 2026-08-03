---
category: Other
collected_at: '2026-08-03T22:32:28+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32105
id: hada-32105
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- research.jfrog.com
title: 환각으로 생성된 SQLite 취약점에 Critical CVE가 발급됨
url: https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 새 GitHub 저장소가 공개한 SQLite 취약점 6건은 NVD와 CISA ADP에서 중요 취약점으로 분류됐지만, 검증 결과 **존재하지 않는 코드와 동작**에 근거한 것으로 확인됨
- 공식 SQLite 버전을 Docker에서 빌드해 AddressSanitizer로 검사하자 모든 PoC가 정상 실행되거나 구문·JSON 파싱 단계에서 실패해, 보고된 **use-after-free**가 재현되지 않음
- 같은 계정의 권고문 55건을 감사한 결과 **54건은 완전히 조작**됐고, 나머지 1건도 실제 버그에 검증되지 않은 CVE 메타데이터를 결합한 사례였음
- MITRE 공개 제출 양식은 실질적인 신원 확인이 없고 PoC나 버그 재현도 요구하지 않아, 그럴듯한 허위 권고문이 **GHSA·하위 데이터베이스·기업 스캐너**까지 전파될 수 있음
- 출처가 새롭거나 검증되지 않은 CVE는 공식 공급자 권고, 수정 커밋, CPE·버전 정보, 실제 코드 존재 여부를 확인하고 **격리된 환경에서 PoC를 직접 재현**해야 함

---

## 원문
- [원문](https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/)
- [GeekNews 토론](https://news.hada.io/topic?id=32105)

## My Note
<!-- 한 줄 코멘트 남기기 -->
