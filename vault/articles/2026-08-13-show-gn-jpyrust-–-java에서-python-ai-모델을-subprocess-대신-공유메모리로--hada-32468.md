---
category: AI
collected_at: '2026-08-13T21:44:01+09:00'
geeknews_comments: 0
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=32468
id: hada-32468
matched_keywords:
- AI
read: false
recommend_score: 2.693
source: geeknews
tags:
- AI
- Other
- github.com/farmer0010
title: 'Show GN: JPyRust – Java에서 Python AI 모델을 subprocess 대신 공유메모리로 호출해봤습니다. (390배
  향상된 속...'
url: https://github.com/farmer0010/JPyRust
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Java 백엔드에서 Python으로 만든 AI 모델을 호출해야 하는 일이 있어서 관련 방법을 찾아보다가 궁금한 부분이 생겨서 직접 한번 만들어 보게 되었습니다!

Java에서 Python을 사용할 수 있게 해주는 라이브러리는 이미 여러 가지가 있어서 처음에는 그냥 있는 라이브러리를 사용하면 되지 않을까 생각했습니다. 그런데 교육기관에서 시스템 콜부터 운영체제 아래쪽을 공부하다 보니 Java에서 다른 프로세스를 실행하고 데이터를 주고받는 게 실제로 어떤 흐름으로 이루어지는지 궁금해졌습니다.

그래서 그냥 라이브러리를 가져다 쓰는 것보다는 Java에서 시작해서 JNI를 거치고, Rust를 통해 Python 프로세스까지 연결되는 과정을 직접 만들어보면 어떨까 싶어서 시작하게 됐습니다.

마침 이걸 실제로 필요로 했던 프로젝트도 있었습니다. 교육 재단에서 진행했던 사물함 대여 프로젝트에서 사물함 반납을 카메라 이미지로 처리하는 기능을 붙이면서 Java 서버에서 Python AI 모델을 호출해야 했습니다. 처음에는 subprocess로 Python을 실행하는 방식으로 처리했는데, 반납 요청이 들어올 때마다 프로세스를 새로 띄우고 모델까지 다시 로딩하다 보니 AI 추론 자체보다 Python 실행이나 모델 로딩에 걸리는 시간이 더 크게 느껴졌습니다.

그래서 Python 워커를 하나 띄워놓고 계속 대기시키는 방식으로 바꿔봤고, Java와 Python 사이의 연결은 Rust로 JNI를 만들어서 처리했습니다. 이미지처럼 크기가 있는 데이터는 소켓이나 파일로 넘기는 대신 공유 메모리(SHMEM)를 사용했습니다.

그리고 실제로 얼마나 차이가 나는지 궁금해서 YOLOv8n을 기준으로 간단하게 테스트해봤는데 생각보다 차이가 컸습니다.

subprocess 방식: 평균 약 2,330ms  
JPyRust: 평균 약 6ms

약 390배 정도 차이가 났습니다.

레포에 `LatencyBenchmark.java`를 넣어놔서 같은 테스트를 직접 돌려볼 수도 있습니다.

물론 이게 AI 추론 자체가 390배 빨라졌다는 의미는 아닙니다. subprocess 방식에서는 요청마다 Python 인터프리터를 실행하고 라이브러리를 import한 다음 모델까지 다시 로딩하기 때문에 여기서 시간이 많이 걸립니다. 반대로 JPyRust는 Python 워커와 모델을 미리 띄워놓고 요청이 들어오면 이미지 데이터만 전달하는 방식이라 이 부분에서 차이가 크게 났습니다.

현재는 Windows / macOS / Linux에서 사용할 수 있도록 만들어봤고, Python 환경도 실행 환경에 맞춰 자동으로 구성하도록 해놨습니다.

아직 제대로 검증하지 못한 부분도 있습니다. 동시 요청이 많이 들어왔을 때 워커를 어떤 방식으로 운영하는 게 좋을지, 워커가 죽었을 때 자동으로 복구하는 부분이나 여러 AI 모델을 동시에 사용하는 경우까지는 아직 충분히 테스트하지 못했습니다.

이번 프로젝트를 만들면서 Java에서 Python을 호출하는 것도 결국 그 아래에서는 프로세스와 메모리, IPC 같은 것들이 연결되어 있다는 게 재미있어서 조금 더 내려가 보면서 만들어봤습니다. 아직 공부하면서 만든 프로젝트라 부족한 부분도 많습니다.

코드는 GitHub에 올려뒀습니다.

Java에서 Python AI 모델을 연결해보신 분들이 있다면 보통 어떤 방식을 사용하시는지, 제가 생각하지 못한 부분이 있는지도 궁금합니다.

사용해보시거나 개선할 부분이 보인다면 편하게 피드백 부탁드립니다.

## 원문
- [원문](https://github.com/farmer0010/JPyRust)
- [GeekNews 토론](https://news.hada.io/topic?id=32468)

## My Note
<!-- 한 줄 코멘트 남기기 -->
