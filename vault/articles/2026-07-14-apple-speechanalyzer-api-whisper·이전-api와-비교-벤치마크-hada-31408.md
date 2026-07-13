---
category: Other
collected_at: '2026-07-14T06:58:45+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31408
id: hada-31408
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- get-inscribe.com
title: Apple SpeechAnalyzer API, Whisper·이전 API와 비교 벤치마크
url: https://get-inscribe.com/blog/apple-speech-api-benchmark.html
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- Apple M2 Pro에서 5,559개 LibriSpeech 음성을 동일한 프로덕션 코드로 처리한 결과, **SpeechAnalyzer**가 깨끗한 음성 2.12%, 잡음이 많은 음성 4.56%의 단어 오류율(WER)로 테스트한 모든 엔진보다 정확했음
- 기존 **SFSpeechRecognizer**의 WER는 각각 9.02%와 16.25%였으며, 새 API는 같은 음성에서 오류를 3.5~4배 줄이면서 구두점과 대소문자까지 적용함
- SpeechAnalyzer는 **Whisper Small보다 정확하면서 약 3배 빨랐지만**, 약 30개 로케일과 OS 26 이상 Apple 플랫폼으로 지원 범위가 제한됨
- 모든 엔진이 M2 Pro에서 실시간보다 **약 12~40배 빠르게** 작동해 1시간 분량을 1.5~5분에 처리했으나, 개발 작업이 병행된 환경이라 엔진별 정밀 속도는 공개되지 않았음
- 현재 iPhone이나 Mac에서 영어를 온디바이스로 전사한다면 SpeechAnalyzer가 우선 선택지가 될 수 있으며, **Inscribe**도 지원 언어에는 SpeechAnalyzer를, 나머지에는 Whisper를 쓰도록 기본 설정을 변경함

---

## 원문
- [원문](https://get-inscribe.com/blog/apple-speech-api-benchmark.html)
- [GeekNews 토론](https://news.hada.io/topic?id=31408)

## My Note
<!-- 한 줄 코멘트 남기기 -->
