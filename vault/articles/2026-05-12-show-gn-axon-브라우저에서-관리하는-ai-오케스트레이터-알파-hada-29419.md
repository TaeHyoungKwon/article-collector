---
category: AI
collected_at: '2026-05-12T11:28:26+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29419
id: hada-29419
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.099
recommended_on: '2026-05-12'
source: geeknews
tags:
- AI
- Other
- github.com/dogsinatas29
title: 'Show GN: axon - 브라우저에서 관리하는 ai 오케스트레이터 알파'
url: https://github.com/dogsinatas29/SYNAPSE
---

## TL;DR
- 이 글은 로컬 LLM을 이용한 ai 오케스트레이터 'axon'의 개념 검증 영상과 기능을 소개한다.
- axon은 아키텍트, 시니어, 주니어 모델을 통해 코드 제안 및 검토 과정을 스레드 형태로 관리하며, 다양한 언어 지원을 제공한다.
- 이 시스템은 AI 개발 및 관리의 효율성을 높이고, 향후 인사 관리 및 결과물 버전업 작업도 진행될 예정이므로 관련 업계에 중요한 시사점을 제공한다.

## GeekNews 요약
<https://youtu.be/gmUdrVNKrPg?feature=shared>  
개념 검증 영상입니다.편집없이 작업했고 서버 사양이 사양인 만큼 인내심이필요합니다.  
로컬llm은 i7 하스웰 16gb 1050ti에 airllm을 이용해서 ollama를 구동하고 그위에 qwen과 llama3를 올렸습니다  
개발은 구글 안티그래비티로 작업하고있습니다  
이 영상은 api없이 로컬llm만으로 작업한 영상입니다.  
axon을 실행하면 아키텍트/시니어/주니어 모델을 결정하고 명세를 주입하면 아키텍트(tot)가 작업을 분리하고 주니어가 개별작업에 대한 코드를 제안(cot)합니다. 시니어는 이 코드를 리뷰하고(cot->tot) 승인 반려합니다.이 과정은 모두 스레드 형태의 로컬호스트 게시판에 등록되고 승인이 이뤄지면 실제 파일이 작성됩니다. 그 이전까지는 샌드박스 환경에서 이뤄지고요.  
설정 최초 과정에서 llm의 국가별 언어 강제가 있습니다. 영어 한글 그리고 일본어가 지원됩니다.

러스트와 파이선으로 검증은 했습니다  
이제 c c++ 테스트중입니다만 ir과 검증기의 한계로 아예 언어별 검증기를 분리하는 작업중입니다.

추후 ai들이 남는 시간에 노가리 떠는 게시판  
인사 게시판을 통한 시니어 주니어 고용 및 해고, 페르소나 주입  
그리고 axon이 만든 결과물을 버전업하기위한 브라운필드 작업이 진행될 예정입니다  
관심있으시면 방문해서 테스트라도 해주시면 감사하겠습니다

## 원문
- [원문](https://github.com/dogsinatas29/SYNAPSE)
- [GeekNews 토론](https://news.hada.io/topic?id=29419)

## My Note
<!-- 한 줄 코멘트 남기기 -->
