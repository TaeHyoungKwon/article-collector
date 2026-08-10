---
category: Other
collected_at: '2026-08-10T20:01:55+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32355
id: hada-32355
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- fzakaria.com
title: 'nixpkgs-multiverse: 지금까지 존재한 모든 패키지 버전'
url: https://fzakaria.com/2026/08/09/nixpkgs-multiverse-every-version-that-ever-existed
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **nixpkgs-multiverse**는 과거 Nixpkgs 커밋을 일일이 찾아 고정하지 않아도, 하나의 flake 입력에서 지금까지 존재한 모든 패키지 버전에 접근하게 해줌
- 일반 flake 입력은 사용 여부와 관계없이 즉시 가져오지만, 이 프로젝트는 `builtins.fetchTree`와 `narHash`로 실제 참조한 **리비전만 지연 로딩**함
- 2017~2026년 Hydra에서 빌드·캐시된 **1,393개 리비전**과 289,521개 `(속성, 버전)` 쌍을 5.18MB JSON 인덱스로 관리함
- 사용하지 않는 `nixpkgs` 입력 5개는 평가 전에 26초를 소비한 반면, 1,393개 리비전을 제공하는 nixpkgs-multiverse의 **JSON 파싱은 0.20초**가 걸림
- 약 200줄의 Nix와 5MB 규모 JSON만으로 버전·릴리스·날짜·커밋별 Nixpkgs를 한 셸이나 빌드 환경에서 조합하며, 패키지를 직접 빌드·미러링·호스팅하지 않음

---

## 원문
- [원문](https://fzakaria.com/2026/08/09/nixpkgs-multiverse-every-version-that-ever-existed)
- [GeekNews 토론](https://news.hada.io/topic?id=32355)

## My Note
<!-- 한 줄 코멘트 남기기 -->
