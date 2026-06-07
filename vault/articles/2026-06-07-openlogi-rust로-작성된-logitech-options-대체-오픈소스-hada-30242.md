---
category: Other
collected_at: '2026-06-07T09:31:01+09:00'
geeknews_comments: 1
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30242
id: hada-30242
matched_keywords: []
read: false
recommend_score: 1.307
source: geeknews
tags:
- Other
- github.com/AprilNEA
title: OpenLogi - Rust로 작성된 Logitech Options+ 대체 오픈소스
url: https://github.com/AprilNEA/OpenLogi
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- 계정/클라우드/텔레메트리 없이 Logitech 마우스의 **버튼/DPI/SmartShift**를 제어하는 도구로, 공식 Logi Options+ 설치 필요 없음
- **HID++** 프로토콜로 Logi Bolt 리시버, Bluetooth 직접 연결, 유선 연결을 통해 마우스와 직접 통신
- 설정은 클라우드가 아닌 일반 **TOML 파일**에 저장하며, 유일한 네트워크 호출은 "장치 이미지 가져오기" 및 "옵트인 업데이트 확인(기본은 Off)"
- **GUI**로 클릭 가능한 인터랙티브 마우스 다이어그램, 39종 내장 액션과 커스텀 단축키 녹화, DPI 프리셋, SmartShift 패널(휠 모드/민감도) 제공
- 앱 포커스에 따라 자동 전환되는 **앱별 프로파일 오버레이**와 페어링 장치를 실시간 전환하는 디바이스 캐러셀 지원
- **CLI** 도 제공: 헤드리스 인벤토리 조회(`list`), 에셋 동기화, 장치 진단 서브커맨드 내장
- 버튼 입력은 OS 이벤트 탭으로 재매핑 되며, DPI/SmartShift 변경은 HID++로 장치에 직접 기록
- 현재 **macOS** 지원, Linux/Windows는 개발 예정이며 Unifying 리시버는 미지원
- 활발히 개발 중인 상태로 아직 안정 버전 아님. 기능과 설정이 변경될 수 있음
- Apache-2.0 / MIT 이중 라이선스

## 원문
- [원문](https://github.com/AprilNEA/OpenLogi)
- [GeekNews 토론](https://news.hada.io/topic?id=30242)

## My Note
<!-- 한 줄 코멘트 남기기 -->
