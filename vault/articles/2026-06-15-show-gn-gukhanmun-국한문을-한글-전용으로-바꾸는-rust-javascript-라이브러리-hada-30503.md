---
category: Other
collected_at: '2026-06-15T16:19:04+09:00'
geeknews_comments: 0
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30503
id: hada-30503
matched_keywords: []
read: false
recommend_score: 1.099
source: geeknews
tags:
- Other
- gukhanmun.org
title: 'Show GN: Gukhanmun: 국한문을 한글 전용으로 바꾸는 Rust/JavaScript 라이브러리'
url: https://gukhanmun.org/ko-KR/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
안녕하세요. 국한문을 한글 전용으로 바꾸는 라이브러리 Gukhanmun을 공개했습니다. 오래된 문헌, 국한문 자료, 옛 신문이나 공문서 같은 텍스트를 처리할 때 도움이 되면 좋겠습니다.

언뜻 생각하면 글자 하나씩 독음 대응표를 찾으면 그만일 것 같지만, 실제로 구현해보면 그런 방식으로는 제대로 된 결과를 내기 어렵다는 걸 금방 알 수 있습니다. 같은 한자라도 단어 첫머리에서는 두음법칙이 적용되고, 여러 글자가 모여 하나의 단어를 이루면 글자별 독음과 다른 발음이 나기도 합니다. 「庫間」은 “고간”이 아니라 “곳간”이고, 「標識」는 “표식”이 아니라 “표지”이며, 한자와 한글이 섞인 「汽車길」은 사이시옷이 붙어 “기찻길”입니다. 한자 숫자도 까다로운데, 「二〇一六年」은 “2016년”이 맞지만 「十一月」은 “11월”이고 「一千二百三十四」는 “1234”라, 같은 숫자 표기 안에서도 어떤 방식인지 판단해야 합니다.

예전에 비슷한 목적으로 Haskell 라이브러리 [Seonbi](https://github.com/dahlia/seonbi)를 만들었는데, 이번에는 범위를 한자 변환에 맞춰 Rust로 새로 짰습니다. 표준국어대사전을 내장해서 별도 사전 설치 없이 쓸 수 있고, 일반 텍스트와 HTML, Markdown을 처리합니다. 출력은 한글만 남기거나, 한자(漢字)처럼 괄호로 병기하거나, HTML 루비 마크업으로 내보낼 수 있습니다. 남한·북한 맞춤법 프리셋, 동음이의어가 있을 때 한자를 병기하는 옵션도 넣었습니다.

가장 신경 쓴 부분은 분할 알고리즘입니다. 왼쪽에서 오른쪽으로 가장 긴 항목을 고르는 방식은 「資本論理」를 「資本論」+「理」로 잘라 “자본**론이**”로 읽습니다. Gukhanmun은 래티스(lattice) 위에서 동적 계획법(Viterbi 알고리즘)을 돌려 「資本」+「論理」로 나눠 “자본논리”를 찾아냅니다.

처음부터 Rust로 만든 이유 중 하나는 여러 언어에서 갖다 쓰기 쉽게 하려는 것입니다. CLI는 [GitHub Releases](https://github.com/dahlia/gukhanmun/releases)에서, Rust 크레이트 [`gukhanmun`](https://crates.io/crates/gukhanmun)은 crates.io에서 받을 수 있고, JavaScript 쪽은 WebAssembly([`@gukhanmun/wasm`](https://www.npmjs.com/package/@gukhanmun/wasm))와 Node.js 네이티브 애드온([`@gukhanmun/napi`](https://www.npmjs.com/package/@gukhanmun/napi)) 두 가지로 npm과 JSR에 올려 두었습니다. 핵심 크레이트 [`gukhanmun-core`](https://crates.io/crates/gukhanmun-core)는 `no_std` + `alloc` 환경도 지원해서 임베디드에서도 쓸 수 있습니다.

- 문서 및 웹사이트: <https://gukhanmun.org/ko-KR/>
- 연습장: <https://gukhanmun.org/ko-KR/playground>
- GitHub 저장소: <https://github.com/dahlia/gukhanmun>

## 원문
- [원문](https://gukhanmun.org/ko-KR/)
- [GeekNews 토론](https://news.hada.io/topic?id=30503)

## My Note
<!-- 한 줄 코멘트 남기기 -->
