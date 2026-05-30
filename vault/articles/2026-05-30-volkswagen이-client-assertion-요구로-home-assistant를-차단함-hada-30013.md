---
category: Other
collected_at: '2026-05-30T11:39:00+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=30013
id: hada-30013
matched_keywords: []
read: false
recommend_score: 0.901
source: geeknews
tags:
- Other
- github.com/robinostlund
title: Volkswagen이 client assertion 요구로 Home Assistant를 차단함
url: https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **Issue #967**은 아직 Open 상태이며, 관련 항목으로 [#971](https://github.com/robinostlund/homeassistant-volkswagencarnet/pull/971)과 최신 릴리스 `v5.4.7`이 표시되지만, 제공된 논의만으로 최종 해결 여부는 확인되지 않음
- 최초 보고는 Home Assistant의 **homeassistant-volkswagencarnet** 인증이 만료된 뒤 이메일과 비밀번호로 재로그인이 불가능해졌고, Android 앱과 브라우저 로그인은 계속 동작한다는 내용임
- 재현 절차는 이메일과 비밀번호 입력이며, 오류 메시지는 `Anmeldung bei Volkswagen Connect nicht möglich. Bitte überprüfe deine Zugangsdaten und stelle sicher, dass der Dienst verfügbar ist.`로 나타남
- 한 참여자는 이것이 버그가 아니라 Volkswagen이 **API를 영구 비활성화**한 결과라고 봤고, 이후 다른 참여자는 공식 유료 API와 무료 비공식 API가 있으며 후자가 더 이상 동작하지 않는다고 정리함
- 일부 사용자는 웹 로그인은 가능하지만 API와 앱이 동작하지 않거나 앱 응답이 매우 느리다고 보고했고, 다른 사용자는 Android 앱 로그인은 가능하지만 Home Assistant 재시작 뒤 같은 문제가 생겼다고 보고함
- [CarConnectivity-plugin-mqtt](https://github.com/tillsteinbach/CarConnectivity-plugin-mqtt)가 동작한다는 보고가 있었지만, 같은 API를 쓰므로 기존 설정은 토큰 만료 전까지만 유지되고 신규 사용자는 동작하지 않을 수 있다는 반론이 나옴
- 다른 사용자는 CarConnectivity-plugin-mqtt를 처음 써도 새 인증 토큰으로 데이터를 가져왔다고 보고해, 해당 대안의 지속 가능성은 논의 안에서 확정되지 않음
- Skoda EV Facebook 포럼에 관련 변경이 공유됐고, 공식 발표를 보지 못했다는 참여자는 이 변경이 **VAG 브랜드 전체**에 영향을 줄 가능성이 있다고 봄
- 대안으로 Smartcar와 Tibber가 거론됐으며, Smartcar는 차량 데이터 흐름과 GDPR 적용 여부가 논의됐고 한 사용자는 Smartcar로 “일단 동작”하게 만들었다며 [wbyoung/smartcar#110의 댓글](https://github.com/wbyoung/smartcar/issues/110#issuecomment-4579464041)을 공유함
- Tibber는 Home Assistant의 기본 Tibber 통합으로 동작한다는 보고가 있었지만, Tibber가 엔터프라이즈 API 접근 비용을 내는 구조라면 비결제 신규 사용자가 몰리는 상황을 오래 허용하지 않을 수 있다는 우려가 제기됨
- 한 참여자는 Skoda 공지가 돈을 요구한다기보다 API 사용자가 Volkswagen에 등록해야 한다는 의미라고 해석하며 프로젝트 등록 여부를 물었고, 유지관리자는 Volkswagen 차량을 더 이상 보유하지 않아 직접 진행하지 않았다고 답함
- 유지관리자는 등록이 사용자별 키를 요구할 가능성이 있다고 봤고, 조사와 프로젝트 유지관리를 도와줄 사람이 필요하다고 요청해 해결 방향은 커뮤니티 지원에 의존하는 상태로 남음

## 원문
- [원문](https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967)
- [GeekNews 토론](https://news.hada.io/topic?id=30013)

## My Note
<!-- 한 줄 코멘트 남기기 -->
