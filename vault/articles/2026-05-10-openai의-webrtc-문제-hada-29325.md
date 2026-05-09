---
category: AI
collected_at: '2026-05-10T00:39:03+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29325
id: hada-29325
matched_keywords:
- AI
read: false
recommend_score: 2.901
source: geeknews
tags:
- AI
- Other
- moq.dev
title: OpenAI의 WebRTC 문제
url: https://moq.dev/blog/webrtc-is-the-problem/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- **WebRTC**는 회의 통화처럼 낮은 지연을 우선해 네트워크가 나쁠 때 오디오 패킷을 적극적으로 버리지만, Voice AI에서는 느린 응답보다 음성 프롬프트 손상이 응답 품질을 더 크게 해칠 수 있음
- **TTS**는 실시간보다 빠르게 오디오를 만들 수 있어 클라이언트 버퍼링으로 짧은 네트워크 장애를 숨길 수 있지만, WebRTC는 도착 시간 기준 렌더링과 작은 지터 버퍼 때문에 패킷을 제때 보내도록 인위적으로 대기해야 함
- WebRTC는 임시 포트, ICE, DTLS, SCTP 등으로 연결 설정과 운영이 복잡하며, 단일 포트 다중화에서는 STUN, SRTP/SRTCP, DTLS, TURN 패킷을 각 연결로 라우팅하기 어려움
- OpenAI가 빠른 연결 설정을 요구해도 WebRTC는 시그널링과 미디어 서버 절차를 합쳐 최소 **8 RTT**가 들 수 있으며, P2P 지원 구조 때문에 서버가 고정 IP를 가져도 같은 절차를 거쳐야 함
- 대안으로 **WebSockets**와 **QUIC/WebTransport**가 제시되며, QUIC은 `CONNECTION_ID`, QUIC-LB, `preferred_address`를 통해 단일 포트, 주소 변경, 상태 없는 로드밸런싱, anycast와 unicast 조합을 더 단순하게 지원함

---

## 원문
- [원문](https://moq.dev/blog/webrtc-is-the-problem/)
- [GeekNews 토론](https://news.hada.io/topic?id=29325)

## My Note
<!-- 한 줄 코멘트 남기기 -->
