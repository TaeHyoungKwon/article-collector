---
category: Other
collected_at: '2026-06-09T13:43:21+09:00'
geeknews_comments: 0
geeknews_score: 3
geeknews_url: https://news.hada.io/topic?id=30317
id: hada-30317
matched_keywords: []
read: false
recommend_score: 1.386
source: geeknews
tags:
- Other
- github.com/promet99
title: 'Show GN: korean-bank-tx-crawler – 국내 개인은행 거래내역을 파이썬 3줄로 가져오기'
url: https://github.com/promet99/korean_bank_tx_crawler/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
국내 은행은 개인용 API가 없어서 거래내역 자동화가 필요할 때마다 매번 손으로 엑셀 내보내기를 하고 있었습니다.

코드 3줄로 거래내역을 가져오는 파이썬 라이브러리입니다.  
개인 통장을 동아리 통장이나 모임 통장 등으로 쓰신다면 유용하실 겁니다.

현재 KB국민은행, 우리은행을 지원합니다. 사용하실 계좌에 인터넷뱅킹으로 빠른조회 서비스 등록이 필요합니다.

```
from simple_bank_korea import get_transactions  
  
txs = get_transactions(  
    bank_name='woori',  
    bank_num='1002360090945',  
    birthday='990429',  
    password='1234',  
    days=30,       # optional, default 30  
    headless=True  # optional, default True  
)  
  
for tx in txs:  
    print(tx['date'], tx['amount'], tx['transaction_by'], tx['balance'])
```

결과:

```
[  
    {'date': datetime(2026, 6, 9, 13, 28, 15), 'amount': -10000, 'balance': 0, 'transaction_by': '김철수'},  
    {'date': datetime(2026, 6, 9, 13, 27,  6), 'amount':  10000, 'balance': 10000, 'transaction_by': '홍길동'}  
]
```

amount는 입금 양수, 출금 음수입니다.

사용하려면:

```
pip install korean_bank_tx_crawler
```

> beomi님의 [simple\_bank\_korea](https://github.com/beomi/simple_bank_korea) 라이브러리를 포크해서 만들었습니다.

## 원문
- [원문](https://github.com/promet99/korean_bank_tx_crawler/)
- [GeekNews 토론](https://news.hada.io/topic?id=30317)

## My Note
<!-- 한 줄 코멘트 남기기 -->
