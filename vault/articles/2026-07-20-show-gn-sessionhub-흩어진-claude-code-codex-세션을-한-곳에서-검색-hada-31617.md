---
category: Dev Tools
collected_at: '2026-07-20T16:56:22+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31617
id: hada-31617
matched_keywords:
- Claude Code
- Codex
read: false
recommend_score: 4.693
recommended_on: '2026-07-21'
source: geeknews
tags:
- Dev Tools
- Other
- github.com/esc5221
title: 'Show GN: sessionhub - 흩어진 Claude Code, Codex 세션을 한 곳에서 검색'
url: https://github.com/esc5221/sessionhub
---

## TL;DR
- sessionhub는 여러 머신에 분산된 Claude Code와 Codex 세션을 통합하여 검색할 수 있는 도구이다.
- 사용자는 SSH를 통해 세션을 15분마다 중앙 서버에 모으며, 필요한 경우 검색으로 쉽게 접근할 수 있다.
- 이 도구는 과거 작업을 신속하게 검색할 수 있도록 도와주며, 개발자의 효율성을 높이는 데 기여한다.

## GeekNews 요약
sessionhub는 여러 머신에 흩어진 Claude Code · Codex 세션을 한 곳에 모아 검색하는 도구입니다.

데스크톱과 노트북을 오가고 가끔 서버에서도 개발하는데, "이거 전에 해봤는데" 싶은 작업이 어느 머신에 있었는지 자주 헷갈렸습니다. Claude Code랑 Codex 세션이 각 머신 `~/.claude/projects`, `~/.codex/sessions`에 JSONL로 쌓이긴 하는데, 파일은 다 있어도 검색이 안 되니 결국 여러 머신에 SSH로 접속해 일일이 뒤지게 되더라고요.

찾을 땐 키워드로 검색합니다. `sessionhub search "connection pool"` 로 찾고, `sessionhub raw <id>` 로 그때 대화를 봅니다.

요즘 제일 편하게 쓰는 건 에이전트 연동입니다. 설치하면 Claude Code랑 Codex에 스킬이 같이 깔려서, 작업하다 "예전에 이거 어떻게 했었지"가 필요한 순간에 에이전트가 관련 세션을 찾아 컨텍스트로 가져옵니다.

```
# Claude Code  
/sessionhub 저번에 커넥션 풀 터지던거 어떻게 고쳤더라  
  
# Codex  
$sessionhub 저번에 커넥션 풀 터지던거 어떻게 고쳤더라
```

동작은 단순합니다. 허브 한 대를 정해두면 나머지 머신의 세션이 15분마다 SSH로 모이고, 허브가 아닌 다른 머신에서 검색하면 허브가 대신 찾아줍니다. 무거운 로그를 여기저기 복사할 일이 없습니다.

용량도 가볍습니다. 제 로그를 뜯어보니 99.7%가 tool 호출·스트리밍 프레임·토큰 계산 같은 기계용 데이터고, 정작 다시 찾아보는 대화는 0.3% 정도뿐이더라고요. 그래서 대화만 뽑아 압축해 인덱스에 넣습니다. 제 경우 ~10GB 원문이 수백 MB로 줄었습니다. 원본 전체는 원래 있던 머신에 그대로 두니까, 필요하면 그때 열면 됩니다.

설치하면 `setup`이 허브 설정과 스킬 설치까지 안내합니다.

```
uv tool install git+https://github.com/esc5221/sessionhub  
sessionhub setup
```

---

요즘은 에이전트에 장기 메모리를 붙이는 시도가 많습니다. 지난 대화를 요약·추출해서 별도 메모리에 쌓아두고 다음 세션이 참고하게 하는 방식인데, 저도 이런 접근을 좋아하지만 두 가지가 늘 걸렸습니다. 요약하는 순간 원래 맥락이 조금씩 깎이고, 쌓인 메모리는 시간이 지나면 stale하게되어서 계속 손봐줘야하는게 번거로웠던거 같습니다

그래서 저는 요약을 따로 만들지 않고, 원본을 그대로 둔 채 필요할 때 그때 대화를 다시 꺼내 봅니다. memory-centric보다 compute-centric에 가까운 방식입니다.

이 문제(에이전트한테 과거 컨텍스트를 안 낡게, 손실 없이 주는 것)를 다르게 풀고 계신 분이나 더 나은 방법도 궁금하네요. 댓글로도 의견 많이 주시면 감사하겠습니다

- GitHub: <https://github.com/esc5221/sessionhub>

## 원문
- [원문](https://github.com/esc5221/sessionhub)
- [GeekNews 토론](https://news.hada.io/topic?id=31617)

## My Note
<!-- 한 줄 코멘트 남기기 -->
