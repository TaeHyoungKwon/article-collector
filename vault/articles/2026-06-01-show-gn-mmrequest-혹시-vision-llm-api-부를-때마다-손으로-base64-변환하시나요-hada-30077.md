---
category: AI
collected_at: '2026-06-01T23:58:11+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30077
id: hada-30077
matched_keywords:
- AI
- LLM
read: false
recommend_score: -995.307
recommended_on: '2026-06-01'
source: geeknews
tags:
- AI
- Other
- mm-request.vercel.app
title: 'Show GN: MMRequest - 혹시 vision LLM API 부를 때마다 손으로 base64 변환하시나요 - 빡쳐서 만든 Chrome
  확장'
url: https://mm-request.vercel.app
---

## TL;DR
- 이 글은 vision 또는 audio LLM API 호출 시 이미지/오디오 파일의 base64 변환을 자동화하는 Chrome 확장인 MMRequest에 대해 다룹니다.
- 이 확장은 파일을 드래그하거나 붙여넣기를 통해 자동으로 base64 인코딩을 수행하고, Postman에서의 JSON 본문 처리 과정을 간소화합니다.
- 이러한 도구는 멀티모달 API 사용 시 반복적인 작업을 줄여주어 개발자들의 생산성을 향상시키는 데 기여할 수 있다.

## GeekNews 요약
**혹시 vision 또는 audio LLM API 부를 때마다, Postman에서 매번 이미지/오디오를 base64로 변환하시는 분 계신가요?**

네, 저도 그래서 자동으로 처리해주는 Chrome 확장을 만들었습니다.

vLLM 매일 쓰면서 GPT-4o · Claude · Whisper · TTS 같은 클라우드 API들도 Postman으로 자주 호출했습니다. 그런데 vision/audio 요청 한 번 보낼 때마다 같은 일을 반복해야 했어요 — 이미지를 어디 base64 인코더 사이트에 올리고, 300KB짜리 문자열을 복사해서, Postman 본문에 붙이고, 에디터가 버벅이는 걸 보다가, 이미지가 한 번 바뀌면 처음부터 다시. **Postman은 애초에 멀티모달 워크플로를 위해 만들어진 도구가 아니라서** 그냥 도구를 바꿔야겠다 싶었습니다. 같은 답답함 겪고 계신 분들 도움 됐으면 해서 공유합니다.

**MMRequest** — vision/audio LLM 워크플로 한 가지만 잘 풀어주는 Chrome 확장입니다.

- 이미지나 오디오 파일을 **드래그 / 붙여넣기 / 선택**하면 `{{base64Image}}` · `{{base64Audio}}` 변수로 자동 바인딩됩니다. 파일은 **브라우저 안 FileReader로만** 처리해서 외부 서버로 나가지 않습니다.
- JSON 본문에는 변수만 적어두면 되고, 실제 치환은 **Send 시점에 네트워크 경계에서만** 일어납니다. 컬렉션 파일 크기가 300KB가 아니라 **1KB로 유지**됩니다.
- 스트리밍 응답이 청크 단위로 쪼개져서 그대로 읽으면 보기 불편한데, **Stream 탭에서 청크들을 다시 합쳐서 한 화면에서** 보여줍니다. NDJSON · SSE · JSON array 모두 자동 감지.
- 응답 Pretty 뷰는 **필드 단위로 접을 수** 있어서, 응답에 base64가 다시 echoed back 되거나 `b64_json` 같은 긴 문자열이 들어와도 화면이 도배되지 않습니다.
- **OpenAI / Claude / Gemini / vLLM 본문 템플릿**이 사이드바에 내장되어 한 번 클릭으로 가져올 수 있습니다.
- **Postman Collection v2.1로 export 가능**. 받는 쪽은 MMRequest 없이도 Postman에서 그대로 실행됩니다.

**솔직한 disclaimer**

- v0.0.3 베타라 거친 부분 있을 수 있습니다.
- 로그인은 선택 사항이고, 안 해도 모든 기능 사용 가능합니다.

랜딩 페이지에 자세한 내용 + 비교표 + 사용 흐름 정리해뒀습니다 → <https://mm-request.vercel.app>

읽어보시고 같은 문제 겪고 계셨다면 한번 써보세요. **피드백 환영합니다.**

## 원문
- [원문](https://mm-request.vercel.app)
- [GeekNews 토론](https://news.hada.io/topic?id=30077)

## My Note
<!-- 한 줄 코멘트 남기기 -->
