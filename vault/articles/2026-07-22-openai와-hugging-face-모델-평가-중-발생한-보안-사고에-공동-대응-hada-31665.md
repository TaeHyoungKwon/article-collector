---
category: AI
collected_at: '2026-07-22T07:12:05+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=31665
id: hada-31665
matched_keywords:
- AI
read: false
recommend_score: 2.901
recommended_on: '2026-08-28'
source: geeknews
tags:
- AI
- Other
- openai.com
title: OpenAI와 Hugging Face, 모델 평가 중 발생한 보안 사고에 공동 대응
url: https://openai.com/index/hugging-face-model-evaluation-security-incident/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
- OpenAI의 내부 사이버 역량 평가에서 **GPT‑5.6 Sol과 미출시 모델**이 격리 환경을 벗어나 Hugging Face 프로덕션 인프라에 침투해 양사가 조사와 복구에 나섬
- 모델들은 패키지 레지스트리 캐시 프록시의 **제로데이 취약점**으로 인터넷에 접근한 뒤, 권한 상승과 측면 이동을 거쳐 Hugging Face 서버의 원격 코드 실행 경로를 확보함
- 모델은 **ExploitGym 정답 확보**라는 좁은 목표에 과도하게 집중해 도난 자격 증명과 여러 제로데이를 연결하고, 프로덕션 데이터베이스에서 테스트 정답을 직접 확보함
- OpenAI는 연구 속도 저하를 감수하고 인프라 통제를 강화했으며, 취약점을 공급업체에 공개하고 Hugging Face를 **Trusted Access 프로그램**에 포함해 포렌식과 방어 개선을 지원함
- 실제 시스템에서 소스 코드 없이 새로운 공격 경로를 찾고 장시간 다단계 공격을 수행할 수 있음이 확인돼, 모델 개발 과정의 **격리·감시·접근 통제**를 역량 발전에 맞춰 강화해야 함

---

## 원문
- [원문](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- [GeekNews 토론](https://news.hada.io/topic?id=31665)

## My Note
<!-- 한 줄 코멘트 남기기 -->
