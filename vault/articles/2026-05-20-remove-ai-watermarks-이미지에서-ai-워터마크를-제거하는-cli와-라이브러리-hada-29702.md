---
category: AI
collected_at: '2026-05-20T13:42:31+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29702
id: hada-29702
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- github.com/wiltodelta
title: Remove-AI-Watermarks - 이미지에서 AI 워터마크를 제거하는 CLI와 라이브러리
url: https://github.com/wiltodelta/remove-ai-watermarks
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Remove-AI-Watermarks**는 Google Gemini(Nano Banana), ChatGPT/DALL-E, Stable Diffusion, Adobe Firefly, Midjourney 등에서 생성된 이미지의 보이는 워터마크, 보이지 않는 워터마크, AI 생성 메타데이터를 한 번에 처리하는 CLI와 Python 라이브러리임
- **보이는 워터마크 제거**는 Gemini/Nano Banana의 sparkle 로고를 대상으로 하며, 알려진 알파 맵을 이용한 역 알파 블렌딩과 그래디언트 마스크 인페인팅으로 처리되고 이미지당 약 0.05초이며 GPU가 필요 없음
- **보이지 않는 워터마크 제거**는 SynthID, StableSignature, TreeRing 같은 픽셀·주파수 영역 패턴을 확산 기반 재생성으로 약화시키는 방식이며, 기본 프로필은 SDXL과 약 1024px 네이티브 파이프라인을 사용함
- 메타데이터 정리는 **EXIF**, PNG text chunks, XMP `DigitalSourceType`, C2PA Content Credentials를 대상으로 하며, Instagram, Facebook, X(Twitter)의 “Made with AI” 라벨을 유발하는 AI 관련 필드를 제거하고 Author, Copyright, Title 같은 표준 메타데이터는 보존함
- 지원 범위는 Google Gemini/Nano Banana/Gemini 3 Pro의 sparkle 로고·SynthID·C2PA/EXIF, OpenAI DALL-E 3/ChatGPT의 C2PA, Stable Diffusion의 PNG text chunks와 스테가노그래픽 워터마크, Adobe Firefly의 Content Credentials, Midjourney의 EXIF/XMP 등을 포함함
- **Smart Face Protection**은 확산 처리 전에 YOLO로 사람을 감지해 얼굴을 추출하고, 처리 후 원본 얼굴을 부드러운 타원 마스크로 다시 블렌딩해 얼굴 특징 왜곡을 줄이는 기능임
- **Analog Humanizer**는 선택적으로 필름 그레인과 색수차를 추가해 출력이 화면을 촬영한 사진처럼 보이게 만들며, AI 이미지 분류기를 우회하기 위한 기능으로 설명됨
- 설치는 `pipx install git+https://github.com/wiltodelta/remove-ai-watermarks.git` 또는 `uv tool install git+https://github.com/wiltodelta/remove-ai-watermarks.git`가 권장되며, 기본 설치는 보이는 워터마크 제거와 메타데이터 제거를 포함함
- 요구사항은 **Python 3.10+** 이며, 보이는 워터마크 제거와 메타데이터 처리는 CPU만으로 가능하고, 보이지 않는 워터마크 제거는 CUDA 또는 MPS GPU가 권장되지만 CPU에서도 느리게 동작함
- 보이지 않는 워터마크 제거는 첫 실행 시 약 **2GB** 모델을 자동 다운로드하고, 장치는 CUDA(Linux/Windows) > MPS(macOS) > CPU 순서로 자동 감지되며 `--device`로 지정 가능함
- CLI는 `remove-ai-watermarks all image.png -o clean.png`, 디렉터리 일괄 처리는 `remove-ai-watermarks batch ./images/ --mode all`처럼 사용하며, `visible`, `invisible`, `metadata` 하위 명령도 제공함
- Python API는 `GeminiEngine`으로 워터마크 감지와 제거를 수행하고, `has_ai_metadata`, `remove_ai_metadata`로 이미지의 AI 메타데이터 확인과 제거를 처리할 수 있음
- 로드맵에는 SynthID-Image v2 자동 회귀 테스트, AVIF/HEIF/JPEG-XL 내부 EXIF/XMP 제거 한계, 별도 패키지로 계획된 비디오 파이프라인이 포함되며, Nightshade/Glaze/PhotoGuard 제거는 예술가 보호를 공격하는 범위로 간주해 지원하지 않음
- 법적 섹션은 AI 생성 출처 표시가 여러 관할권에서 규제되고 있으며, 출처 정보를 속일 의도로 제거하는 행위가 법률·DMCA·플랫폼 약관을 위반할 수 있고 사용자가 준수 책임을 진다고 명시함
- 위협 모델은 이미 배포된 AI 이미지가 자동 감지 시스템과 “Made with AI” 라벨에 대응하도록 돕는 데 초점이 있으며, 원본 파일이 생성자 계정이나 Google 시스템을 거쳤다면 서버 측 기록까지 익명화하지는 못한다고 경고함

## 원문
- [원문](https://github.com/wiltodelta/remove-ai-watermarks)
- [GeekNews 토론](https://news.hada.io/topic?id=29702)

## My Note
<!-- 한 줄 코멘트 남기기 -->
