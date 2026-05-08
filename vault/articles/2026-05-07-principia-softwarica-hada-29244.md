---
collected_at: '2026-05-07T09:08:47+09:00'
geeknews_comments: 1
geeknews_score: 1
geeknews_url: https://news.hada.io/topic?id=29244
id: hada-29244
matched_keywords: []
read: false
recommend_score: 0.0
source: geeknews
tags:
- principia-softwarica.org
title: Principia Softwarica
url: https://principia-softwarica.org/
---

## TL;DR
- (요약 대기 중)

## GeekNews 요약
Principia Softwarica
는
Plan 9 from Bell Labs
의 커널, 셸, 윈도 시스템, 컴파일러, 링커, 에디터, 브라우저, 디버거 소스 코드를 책으로 풀어 컴퓨터 내부 동작을 이해하도록 돕는 시리즈임
각 책은 소스 코드와 문서를 함께 담은
리터레이트 프로그램(literate program)
에서 만들어지며, 실제 코드와 책이 같은 문서에서 자동 생성됨
전체 시리즈는
205,081 LOC
,
82,014 LOE
,
6,312쪽
규모이고, 목표는 코드 한 줄마다 설명 한 줄을 대응시키는 LOE/LOC 1.0 달성임
Plan 9는 전체 시스템이
183K LOC
로 작고, 일관된 C 스타일과 “모든 것이 파일”, 프로세스별 네임스페이스, 네트워크 투명성 같은 아이디어를 균일하게 적용해 전체 운영체제를 설명 가능한 대상으로 만듦
프로젝트 소스는
github.com/aryx/principia-softwarica
에 공개되어 있으며,
Getting Started
는 Docker 또는 소스에서 Plan 9를 빌드하고 실행하는 방법을 제공함
프로젝트 개요
Principia Softwarica
는 프로그래머가 사용하는 핵심 시스템 프로그램의 전체 소스 코드를 자세히 풀어 컴퓨터 내부 동작을 이해하도록 돕는 책 시리즈임
모든 프로그램은 Unix의 후속으로 설계된 운영체제인
Plan 9 from Bell Labs
에서 가져왔으며, 코드가 작고 우아하다는 점을 핵심 전제로 삼음
다루는 프로그램에는
커널
, 셸, 윈도 시스템, 컴파일러, 링커, 에디터, 웹 브라우저, 디버거가 포함되며, 각 프로그램은 별도 책으로 구성됨
책은 구현을 해설하는 문서이면서 구현 그 자체이기도 함
각 프로그램은 소스 코드와 문서를 함께 담은
리터레이트 프로그램(literate program)
에서 나오며, 실제 코드와 책이 모두 이 문서에서 자동 생성됨
리터레이트 프로그래밍에 대한 별도 설명은
more about literate programming
에 있음
프로젝트 소스는
github.com/aryx/principia-softwarica
에 공개되어 있음
왜 필요한가
교육의 빈틈
터미널 창에서
ls
를 입력하면 무슨 일이 일어나는지에 대한 답은 셸, C 라이브러리, 커널, 그래픽 스택, 윈도 시스템을 모두 거침
Keith Adams는 Facebook 동료였고 이후 Slack Chief Architect가 되었으며, 이 질문을 인터뷰 질문으로 사용했음. 전체 추적은
The Journey of
ls
에 있음
오늘날 “풀스택”은 보통 React, Node, 클라우드를 뜻하지만, 실제 하부 스택에는
컴파일러
, 링커, 커널, 시스템 호출이 있음
시스템 프로그램의 개념을 설명하는 훌륭한 교과서는 있지만, 실제 소스 코드를 보여주는 자료는 거의 없으며 Principia Softwarica가 이 간극을 메우려 함
AI 시대의 중요성
AI 코딩 도구는 Principia Softwarica가 설명하는
grep
,
sed
,
diff
,
awk
,
gcc
,
ld
같은 프로그램을 하루에 수백 번 실행함
코딩 업무에서 코드 작성이 20%이고 이해가 80%라면, AI가 20%를 맡을수록 코드가 실제로 무엇을 하는지 하드웨어까지 내려가 이해하는 80%가 더 중요해짐
기계가 딥러닝을 거쳤으니 인간도 깊게 배워야 한다는 문제의식이 깔려 있음
책과 범위
전체 시리즈는
205,081 LOC
,
82,014 LOE
,
6,312쪽
규모이며, 전체 LOE/LOC 비율은
0.40
임
LOC는 코드 줄 수, LOE는 설명 줄 수, Pages는 조판된 페이지 수를 뜻함
목표는 모든 책에서
LOE/LOC 1.0
을 달성해 코드 한 줄마다 설명 한 줄을 대응시키는 것임
녹색은 0.75 이상으로 목표에 가까움
노란색은 0.50 이상으로 진행 중임
주황색은 0.25 이상으로 아직 상당한 집필이 남아 있음
빨간색은 0.25 미만으로 아직 대부분 코드이고 설명이 적음
핵심 시스템
Kernel
:
9pi
, 35,528 LOC, 11,601 LOE, 1,083쪽
Core libraries
:
libc
,
libthread
,
libbio
,
libflate
,
libregexp
, 20,490 LOC, 7,396 LOE, 641쪽
Shell
:
rc
, 6,534 LOC, 4,245 LOE, 249쪽
개발 툴체인
C compiler
:
5c
,
libcc
, 18,700 LOC, 5,654 LOE, 569쪽
Assembler
:
5a
, 3,570 LOC, 4,987 LOE, 179쪽
Linker
:
5l
, 7,528 LOC, 6,142 LOE, 308쪽
개발자 도구
Editor
:
ed
, 1,597 LOC, 1,102 LOE, 46쪽
Build system
:
mk
, 4,356 LOC, 4,959 LOE, 210쪽
Debuggers
:
db
,
acid
,
strace
,
libmach
, 14,895 LOC, 5,741 LOE, 465쪽
Profilers
:
time prof tprof kprof stats iostats
, 3,921 LOC, 2,532 LOE, 149쪽
그래픽
Graphics stack
:
libdraw
,
libmemdraw
,
libmemlayer
,
libimg
, 18,528 LOC, 5,753 LOE, 562쪽
Windowing system
:
rio
,
libframe
,
libcomplete
,
libplumb
, 8,825 LOC, 7,696 LOE, 362쪽
GUI toolkit
:
libpanel
, 3,749 LOC, 2,986 LOE, 170쪽
네트워킹과 기타 프로그램
Network stack
:
libip
,
lib9p
, 19,769 LOC, 3,884 LOE, 578쪽
Web browser
:
mothra
,
webfs
,
hget webcookies uhtml resize
,
tcs
, 12,949 LOC, 4,482 LOE, 384쪽
CLI utilities
:
cat
,
ls
,
grep
,
sed
,
diff
,
tar
,
gzip
,
bc dc hoc
,
awk
, 23,921 LOC, 2,082 LOE, 509쪽
Emulator
:
5i
, 3,176 LOC, 3,215 LOE, 143쪽
Plan 9를 선택한 이유
Plan 9는 전체 운영체제를 현실적으로 이해할 수 있을 만큼 작고, 일관된 C 스타일로 작성되어 있으며, 몇 가지 강력한 아이디어를 균일하게 적용함
모든 것이 파일임
프로세스별 네임스페이스를 사용함
네트워크 투명성을 제공함
macOS나 Windows만큼 화려하지는 않지만, 본질적으로 같은 핵심 서비스를 제공함
프로세스와 메모리를 관리하는 커널
윈도 시스템
셸
컴파일러
네트워킹
그래픽 애플리케이션
전체 Plan 9 시스템은 커널, 컴파일러, 셸, 윈도 시스템 등을 모두 포함해
183K LOC
이며,
vim 350K LOC
보다 거의 2배 작음
400쪽짜리 책 한 권이 약 12K LOC를 다룬다고 보면, Principia Softwarica는 Plan 9 전체를 약 15권으로 다룰 수 있음
gdb
같은 단일 프로그램은 10배 많은 책이 필요함
gcc
는 100배 많은 책이 필요함
Wayland는 X11의 현대적 대체물이고 Clang은 GCC의 현대적 대체물이지만, “깨끗한 재작성”만으로 프로그램이 작아지지는 않음
처음부터 단순성을 목표로 설계한 Plan 9 접근이 모든 줄을 책으로 설명할 수 있게 만듦
배운 내용을 다른 시스템에 적용하는 방식
Plan 9를 직접 사용할 필요는 없으며, 작고 우아한 운영체제 하나를 이해하면 Linux, macOS, Windows에 대한 직관을 얻을 수 있음
커널, 컴파일러, 링커, 셸, 에디터, 디버거, GUI 툴킷, 네트워크 스택은 모두 같은 근본 문제를 풀며, 코드가 5천 줄이든 50만 줄이든 문제의 본질은 같음
Plan 9의 C 컴파일러를 읽으면 GCC를 탐색할 때 필요한 어휘를 얻을 수 있음
Plan 9의 링커를 한 번에 이해하면 LLD의 재배치 처리가 압도적이지 않고 읽을 수 있는 대상이 됨
acid
가 심볼 테이블을 읽고 스택을 걷는 방식을 보면 GDB에서 무엇을 봐야 하는지 배울 수 있음
작은 구현은 큰 코드베이스에서
본질적 복잡성
과 우발적 복잡성을 구분하는 작업 모델을 제공함
Plan 9의 아이디어는 이미 널리 퍼져 있음
UTF-8은 Thompson과 Pike가 Plan 9를 위해 만들었음
/proc
는 Plan 9에서 왔음
Docker와 컨테이너의 기반인 Linux namespaces는 Plan 9에서 왔음
Go는 Pike와 Thompson이 만들었고, goroutine은 Plan 9의 libthread에서 영감을 받음
9P 프로토콜은 WSL2에서 사용됨
Principia Softwarica가 설명하는
grep
,
sed
,
awk
,
diff
,
cc
,
ld
는 프로그래머가 매일 쓰는 도구이며, 같은 개념이 Plan 9에서는 훨씬 더 명확하게 표현됨
plan9port
는 Plan 9 사용자 영역의
grep
,
sed
,
awk
를 Linux와 macOS로 가져옴
goken9cc
는 Linux, macOS, Windows에서 Plan 9 C 툴체인을 사용해 해당 플랫폼용 네이티브 바이너리를 만들 수 있게 함
소스 코드와 실행
github.com/aryx/principia-softwarica
— Principia Softwarica에서 사용하는 Plan 9 코드와 리터레이트 프로그램
Getting Started
— Docker 또는 소스에서 Plan 9를 빌드하고 실행하는 방법
The Journey of
ls
— 간단한 명령이 시스템의 각 계층을 통과하는 추적과 책들이 서로 연결되는 방식
OCaml 포트와 보조 도구
여러 권의 책을 쓴 뒤 일부 프로그램이 정적 타입 함수형 언어인
OCaml
로 포팅됨
원래 동기는 C 코드를 더 잘 이해하기 위한 것이었음
프로그램을 다른 언어로 옮기면 어떤 부분이 본질적이고 어떤 부분이 부수적인지 드러남
포트의 버그는 원본에 숨어 있던 미묘한 부분을 드러냄
OCaml 포트는 별도 프로젝트인
XIX
로 발전했으며, OCaml 버전 도구를 다루는 자체 웹사이트와 리터레이트 프로그래밍 책 시리즈를 가짐
syncweb
— 모든 책을 만드는 데 사용되는 리터레이트 프로그래밍 도구이며 Noweb의 후손임
goken9cc
— Linux, macOS, Windows에서 Plan 9를 빌드하기 위한 C 크로스 컴파일러이며 Kencc의 후손임
관련 작업과 차이
Project Oberon
은 전체 운영체제를 컴파일러와 윈도 시스템을 포함한 전체 소스 코드와 함께 제시한다는 점에서 Principia Softwarica와 가장 정신적으로 가까움
Oberon은 Oberon 프로그램만 실행할 수 있어 Smalltalk처럼 아름답지만 고립된 자기완결 세계임
Plan 9과 Unix는 어떤 언어로 작성된 프로그램도 컴파일하고 실행할 수 있는 범용 시스템임
Oberon에는 네트워킹이 없고 커스텀 하드웨어에서 실행됨
Principia Softwarica는 실제 운영체제 위에서 컴파일러, 링커, 셸, 디버거, 그래픽, 네트워킹까지 더 넓은 범위를 다룸
The Elements of Computing Systems
는 Nand2Tetris로도 알려져 있으며, NAND 게이트에서 Tetris까지 컴퓨터를 구축함
교육적으로 훌륭하지만 하드웨어와 소프트웨어가 강의를 위해 만들어진 장난감 CPU, 장난감 OS, 장난감 언어임
Principia Softwarica는 실제 하드웨어에서 동작하는 실제 코드와 실제 운영체제를 설명하는 반대 접근을 택함
Computer Systems: A Programmer's Perspective
는 CS:APP로 알려져 있으며, 메모리 배치, 링킹, 가상 메모리, 동시성 같은 시스템 프로그래밍 개념을 설명하는 훌륭한 교과서임
CS:APP는 개념에서 멈추며 실제 커널, 실제 링커, 실제 컴파일러의 소스 코드를 보여주지는 않음
Principia Softwarica는 그 소스 코드를 줄 단위로 설명해 CS:APP를 보완함
진행 이력과 저자
2026년 3월 Principia Softwarica 웹사이트가 공개됨
2025년에 QEMU와 Raspberry Pi에서 다시 빌드 및 실행되도록 재개되었고, Dockerfile과 CI가 추가됨
2019년부터 2024년까지는
Semgrep
작업으로 중단 기간이 있었음
2017년에 커널이 Raspberry Pi로 포팅되었고 Shell 및 Graphics 책 작업이 진행됨
2016년에 Build System 책이 완료되었고 첫 Libcore 및 Compiler 리터레이트 프로그램이 만들어짐
2015년에 Assembler와 Linker 책이 완료되었고 Knuth를 만남
2014년에 Plan 9을 포크하고 macOS에서 크로스 컴파일했으며 첫 리터레이트 프로그램을 만들며 프로젝트가 시작됨
Principia Softwarica는 Yoann Padioleau가 작성했으며, 코드는 Ken Thompson, Rob Pike, Dave Presotto, Phil Winterbottom, Tom Duff, Andrew Hume, Russ Cox의 코드를 포함함
Principia Mathematica가 수학의 기초를 다루는 것처럼, Principia Softwarica의 목표는
기초 시스템 프로그램
을 다루는 것임

## 원문
- [원문](https://principia-softwarica.org/)
- [GeekNews 토론](https://news.hada.io/topic?id=29244)

## My Note
<!-- 한 줄 코멘트 남기기 -->
