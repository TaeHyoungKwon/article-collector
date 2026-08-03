---
category: AI
collected_at: '2026-08-03T17:43:32+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32096
id: hada-32096
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- huggingface.co
title: 'Show GN: VODAM Motion API: 운동 영상을 업로드하면 PINN 기반으로 자세 분석/가이드 비교를 해주는 API'
url: https://huggingface.co/spaces/JuSeongvin/vodam-motion-api
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
운동/동작 영상을 업로드하면 PINN 기반 motion pipeline으로 분석 결과를 반환하는 Public API를 만들었습니다.

주요 기능은 두 가지입니다.

precision: 단일 영상을 분석해서 움직임 설명/운동 분석 결과를 반환  
compare: 사용자 영상을 가이드 영상과 비교해서 점수와 피드백 반환  
API 키는 vodam.ai 에서 신청해주시면 됩니다.

예시:

curl -N <https://api.vodam.ai/v1/motion/analyze/stream> ^  
-H "Authorization: Bearer %VODAM\_KEY%" ^  
-F "video=@user\_squat.mp4" ^  
-F "mode=compare" ^  
-F "exercise\_type=squat" ^  
-F "guide\_source=server"

분석 시간이 조금 걸릴 수 있어서, API는 중간 진행 상태를 streaming text로 출력합니다.

예시 출력:

[요청이 접수되었습니다.]  
[영상 업로드가 완료되었습니다.]  
[가이드 영상을 준비했습니다.]  
[분석이 시작되었습니다.]  
[분석이 완료되었습니다.]

[분석 결과]  
종합 점수: 82.4 / 100  
자세 점수: 82.4 / 100  
각도 점수: 82.4 / 100  
힘/흐름 점수: 82.4 / 100

기술적으로는 pose extraction, 3D skeleton postprocessing, PINN 기반 human motion representation, guide-vs-user scoring pipeline을 묶어서 API 형태로 제공하는 구조입니다.

현재는 운동/동작 분석 보조 도구이며, 의료 진단/재활 처방/생체 인식 목적은 아닙니다.

API 형태, 결과 포맷, 개발자 입장에서 더 필요한 기능에 대한 피드백을 받고 싶습니다.

## 원문
- [원문](https://huggingface.co/spaces/JuSeongvin/vodam-motion-api)
- [GeekNews 토론](https://news.hada.io/topic?id=32096)

## My Note
<!-- 한 줄 코멘트 남기기 -->
