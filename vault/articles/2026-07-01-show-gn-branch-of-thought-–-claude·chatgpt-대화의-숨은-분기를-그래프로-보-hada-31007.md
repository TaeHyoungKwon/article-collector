---
category: AI
collected_at: '2026-07-01T20:29:15+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31007
id: hada-31007
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/ijzereen
title: 'Show GN: Branch of Thought – Claude·ChatGPT 대화의 숨은 분기를 그래프로 보여주는 크롬 확장'
url: https://github.com/ijzereen/branch-of-thought
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Claude나 ChatGPT에서 메시지를 편집하면, 대화가 조용히 새로운 분기로 갈라집니다. 그런데 이전 대화는 작은 ‹ 2/3 › 화살표 뒤로 묻혀버려서, 돌아가고 싶은 분기를 자꾸 놓치게 되더군요. 그게 불편해서 직접 만들었습니다.

뭘 하는 거냐면, 사이드패널에 대화 전체를 분기 트리 그래프로 그려줍니다. 대화가 어디서 갈라졌는지 한눈에 보이고 현재 경로는 강조되며, 노드를 클릭하면 그 버전의 메시지 전문을 질문과 답변까지 함께 읽을 수 있습니다. 버려뒀던 분기로도 클릭 한 번에 바로 이동하고, 노드를 드래그해 배치를 바꾸거나 그래프를 HTML, PNG, SVG로 내보낼 수 있습니다.

만들면서 가장 까다로웠던 건 Claude와 ChatGPT가 대화를 저장하는 구조가 완전히 다르다는 점이었습니다. ChatGPT는 mapping 트리를 노출하는데 Claude는 그렇지 않아서, 둘을 같은 형태로 접어 넣는 정규화기를 하나 만들었습니다. 그 덕에 그 아래 로직은 전부 플랫폼 무관하게 동작하고, 두 번째 플랫폼을 붙이는 게 훨씬 수월했습니다.

MV3 기반이고, MAIN world에서 도는 content script가 브라우저가 이미 받아온 대화 데이터를 읽습니다. 그래서 전부 로컬에서 처리되고 서버나 분석, 텔레메트리가 없습니다. 노드 제목을 Claude Haiku로 한 줄 요약하는 옵션이 있는데, 이건 본인 API 키를 쓰고 메시지당 한 번만 요약해서 캐싱합니다.

제 첫 브라우저 확장이라 거친 부분이 많습니다. 웹스토어에는 올리지 않았고 앞으로도 안 올릴 예정이며, 압축 해제 상태로 직접 로드하는 방식입니다. 그래서 실행 전에 코드로 정확히 뭘 하는지 확인할 수 있습니다. MIT 라이선스이고 Claude와 ChatGPT를 모두 지원합니다.  
접근 방식이나 UX, 제가 놓친 엣지 케이스에 대한 피드백을 받고 싶습니다. 뭐든 편하게 물어봐 주세요.

## 원문
- [원문](https://github.com/ijzereen/branch-of-thought)
- [GeekNews 토론](https://news.hada.io/topic?id=31007)

## My Note
<!-- 한 줄 코멘트 남기기 -->
