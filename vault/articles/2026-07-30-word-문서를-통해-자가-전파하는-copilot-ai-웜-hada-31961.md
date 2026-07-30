---
category: AI
collected_at: '2026-07-30T07:33:20+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31961
id: hada-31961
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-07-30'
source: geeknews
tags:
- AI
- Other
- enklypesalt.com
title: Word 문서를 통해 자가 전파하는 Copilot AI 웜
url: https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/
---

## TL;DR
- 이 글은 Word 문서를 통한 자가 전파하는 Copilot AI 웜의 작동 원리를 다룬다.
- 교차 도메인 프롬프트 주입 방식으로 공격 문서 없이도 일상적인 업무 흐름을 통해 악성 코드가 전파될 수 있다.
- 사용자는 외부 문서와 Couilot 결과의 출처를 확인하고 메타데이터를 보존하는 것이 중요함을 인식해야 한다.

## GeekNews 요약
- 외부 Word 문서에 숨긴 **교차 도메인 프롬프트 주입(XPIA)** 이 Copilot의 작성·편집 결과를 조작하고 새 문서로 복제돼, 원본 공격 문서 없이도 일상적인 업무 흐름을 따라 전파될 수 있음
- 흰색·소형 글꼴로 감춘 명령도 Copilot이 서식을 제거한 뒤 읽으며, 실험에서는 재무 수치를 바꾸고 전체 공격 프롬프트를 결과 문서 하단에 숨겨 **새 공격 매개체**로 만들었음
- 공격자는 피해자의 Microsoft 365 테넌트에 접근할 필요가 없으며, SharePoint·Teams·Outlook으로 문서를 공유한 뒤 사용자가 첨부하거나 **Work IQ**가 OneDrive의 관련 자료로 선택하게 만들면 됨
- Microsoft가 특정 페이로드 차단과 모델 업그레이드를 배포했지만, 변형된 프롬프트로 **GPT-5.6**에서도 전체 공격 체인이 재현됐고 144일간의 조정 후에도 취약점 유형 전체를 막지 못했음
- 감염 문서는 정상적인 내부·협력사 자료처럼 유통돼 출처 추적과 탐지가 어려우므로, 외부 문서와 Copilot 결과를 검토하고 원본 출처와 모델 편집 내역을 **메타데이터로 보존**해야 함

---

## 원문
- [원문](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)
- [GeekNews 토론](https://news.hada.io/topic?id=31961)

## My Note
<!-- 한 줄 코멘트 남기기 -->
