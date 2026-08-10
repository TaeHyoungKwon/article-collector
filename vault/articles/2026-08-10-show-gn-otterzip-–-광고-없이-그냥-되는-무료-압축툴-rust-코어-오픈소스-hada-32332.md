---
category: Other
collected_at: '2026-08-10T11:38:06+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=32332
id: hada-32332
matched_keywords: []
read: false
recommend_score: 1.307
source: geeknews
tags:
- Other
- lumibearstudio.github.io
title: 'Show GN: OtterZip – 광고 없이 그냥 되는 무료 압축툴 (Rust 코어, 오픈소스)'
url: https://lumibearstudio.github.io/otterzip-web/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
압축 하나 풀려고 프로그램 켰더니 광고에 결제 유도에... 그게 싫어서  
"조용히 그냥 되는" 압축툴을 만들었습니다. OtterZip입니다.

맥에서 Keka를 쓰다가 "이 심플한 동작이 윈도우엔 왜 없지" 싶었고, 그 방식을  
많이 참고했습니다. 컨셉은 "앱을 안 여는 것"에 가깝습니다  
— 파일 우클릭하면 압축, 압축파일 우클릭하면 풀기. 파일이나 폴더를 앱에 드래그해 넣어도 자동으로 압축/해제됩니다.  
최대한 손이 덜 가는 시나리오를 목표로 했습니다.

- 광고·계정·추적·번들 전부 없음
- ZIP / 7z / RAR / TAR 등 풀기, ZIP·7z·tar.gz 만들기, 암호(AES-256)·분할도 지원
- 엔진은 Rust, UI는 C#/WinUI 네이티브 (창 속 웹뷰 아님) · 다크모드 · 10개 언어
- 무료 + 오픈소스(GPL-3.0) — 소스가 열려 있어 "추적 없다"는 것도 직접 확인 가능합니다. 스토어 버전만 "후원용"으로 유료지만 앱은 완전히 동일합니다

가장 신경 쓴 부분은 속도입니다.  
무거운 코덱은 다들 쓰는 C 라이브러리(libdeflate·zstd·liblzma)를 그대로 붙이고, 그 위에 Rust로 병렬 추출·스마트 저장을 얹었습니다.  
반디집 같은 빠른 툴들과 비교해도 체감상 밀리지 않습니다. 이상한 아카이브를 열 때 경로 탈출·압축폭탄 같은 위험을 막는 쪽에도 공을 들였습니다.

알려진 이슈 하나는 미리 밝혀둡니다.  
재부팅 직후 첫 우클릭에서 메뉴가 안 뜰 때가 있습니다(한 번 더 우클릭하면 나옵니다).  
MSIX 패키지형 셸 확장의 콜드스타트문제인데, NanaZip 같은 패키지 앱도 똑같이 겪는 걸 보면 패키지 앱 공통의 벽인 듯합니다. 아직 완전히 잡지는 못했습니다.  
혹시 이쪽 경험이 있어 해결 힌트를 주신다면 정말 감사하겠습니다.

써보시다 "이건 안 열리는데?" 싶은 파일이 있으면 GitHub 이슈로 남겨주세요.  
하나하나 챙겨보겠습니다.

· 무료 다운로드 <https://lumibearstudio.github.io/otterzip-web/>  
· 소스 <https://github.com/LumiBearStudio/OtterZip>

## 원문
- [원문](https://lumibearstudio.github.io/otterzip-web/)
- [GeekNews 토론](https://news.hada.io/topic?id=32332)

## My Note
<!-- 한 줄 코멘트 남기기 -->
