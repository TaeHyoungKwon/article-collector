---
category: Other
collected_at: '2026-07-19T10:06:07+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31572
id: hada-31572
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- alexalejandre.com
title: Lone Lisp를 만든 Matheus Moreira 인터뷰
url: https://alexalejandre.com/interviews/interview-with-matheus-moreira/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Lone Lisp**는 `libc` 없이 Linux 시스템 호출 위에서 직접 실행되는 Lisp로, Matheus Moreira가 freestanding C만으로 온전한 언어와 사용자 공간 프로그램을 만들 수 있는지 확인하려 시작함
- 안정적인 **Linux 사용자 공간 ABI**를 직접 이용해 `errno`, 로케일, 암묵적 파일 버퍼링 같은 C 라이브러리의 전역 상태와 레거시 API를 제거하고 런타임·메모리 할당기·테스트 도구를 직접 구현함
- **FEXPR와 적절한 꼬리 호출 최적화**를 비롯해 생성기, 구분된 연속체, 재개 가능한 오류 처리를 지원하며 벡터·테이블·연속체도 같은 함수 호출 방식으로 다룸
- 시작은 빠르지만 임시 벤치마크에서 Python보다 **10~100배 느린** 리스트 수준 인터프리터이며, C 인터프리터를 부트스트랩 기준으로 남기고 장기적으로 Lone 자체에 JIT 컴파일러를 구현할 계획임
- Moreira는 Claude를 코드 검토와 프로젝트 관리에 활용하되 Lone 코드는 직접 작성·검토하며, 정적 사이트 생성기·셸·유틸리티를 만들어 **전통적인 Linux 사용자 공간을 재구축**하려 함

---

## 원문
- [원문](https://alexalejandre.com/interviews/interview-with-matheus-moreira/)
- [GeekNews 토론](https://news.hada.io/topic?id=31572)

## My Note
<!-- 한 줄 코멘트 남기기 -->
