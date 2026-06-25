---
category: AI
collected_at: '2026-06-25T13:56:39+09:00'
geeknews_comments: 2
geeknews_score: 2
geeknews_url: https://news.hada.io/topic?id=30817
id: hada-30817
matched_keywords:
- AI
read: false
recommend_score: 3.428
recommended_on: '2026-06-25'
source: geeknews
tags:
- AI
- Other
- github.com/airtaxi
title: 'Show GN: Windows 11 작업표시줄에 내 앱 UI를 올릴 수 있게 해주는 라이브러리를 만들었습니다.'
url: https://github.com/airtaxi/Deskband11Lib
---

## TL;DR
- Windows 11의 작업표시줄에 앱 UI를 통합할 수 있는 라이브러리 **Deskband11Lib**에 대해 설명한다.
- 이 라이브러리는 WinUI 3나 WPF 앱을 작업표시줄 위젯으로 구현할 수 있는 기능을 제공한다.
- 개발자들은 이 라이브러리를 통해 Windows 11의 작업표시줄에서도 자신만의 UI 경험을 유지할 수 있다.

## GeekNews 요약
최근 Windows 11 작업표시줄(taskbar) 안에 직접 앱 UI를 끼워 넣을 수 있는 라이브러리를 공개했습니다. 이름은 **Deskband11Lib**이고, NuGet으로 설치하면 WinUI 3이나 WPF 앱을 작업표시줄 위젯으로 만들 수 있습니다.

왜 만들게 됐는지, 어떻게 돌아가는지, 그리고 실제로 스토어에 등록한 PoC 위젯까지 이어서 설명드릴게요.

---

### 배경: Windows 11에서 사라진 데스크밴드

Windows 10까지는 작업표시줄에 작은 도구모음을 띄우는 **데스크밴드(Deskbands)** 기능이 있었습니다. Windows 11로 넘어오면서 이 기능이 통째로 없어졌죠. 미디어 컨트롤, 시스템 모니터, 빠른 실행 같은 "항상 떠 있는 작은 위젯"을 작업표시줄에 두고 싶은 입장에서는 꽤 아쉬운 변경이었습니다.

### 영감: zadjii의 Deskband11

얼마 전 GitHub에서 [zadjii/Deskband11](https://github.com/zadjii/Deskband11)를 봤는데, 핵심 접근이 정말 멋있었습니다.

> 작업표시줄 위에 투명한 WinUI 3 창을 하나 얹고, 그 창을 작업표시줄의 자식 HWND로 `SetParent`한 다음, 콘텐츠 크기에 맞춰 클립 영역을 잡아서 마치 작업표시줄의 일부처럼 보이게 만드는 것.

결국 "작업표시줄 위에 떠 있는 창일 뿐"인데, 이 발상이 너무 영리했습니다. 다만 원본 프로젝트는 스스로 "해커톤급 코드"라고 밝히고 있었고, 실제 제품에 가져다 쓰기에는 부족한 점들이 있었습니다.

### 그래서 라이브러리로 만들었습니다

아까운 아이디어라서, `dotnet add package` 한 줄로 누구나 쓸 수 있게 라이브러리로 다시 짰습니다.

- GitHub: <https://github.com/airtaxi/Deskband11Lib>
- NuGet: `Deskband11Lib.WinUI` / `Deskband11Lib.Wpf`

#### 사용법은 간단합니다

WinUI 3 창을 하나 만들고 `TaskbarContentHost`에 넘겨주면 끝입니다.

```
var window = new MainWindow();  
var host = new TaskbarContentHost(window, rootElement, new TaskbarContentHostOptions  
{  
    PreferredWidth = 360,  
    PreferredHeight = 48  
});  
  
await host.AttachWhenLayoutReadyAsync();  
window.Activate();
```

WPF도 API가 거의 같습니다. 작업표시줄 정렬(좌측/중앙) 감지, 시작 버튼 및 알림 영역과의 겹침 방지, Explorer 재시작 시 복구, 레이아웃 변경 애니메이션까지 라이브러리가 알아서 처리합니다.

---

### 작동하게 만드는 데 시간이 꽤 들었습니다

원본 코드를 그대로 돌려보니 실행은 됐는데, 창의 위치와 크기가 엉뚱하게 잡히더라고요. 원본이 해커톤 때 짠 코드라, Windows 11이 업데이트되면서 작업표시줄 구현이 바뀌어서 그런 건지 아니면 원래 코드 자체가 어긋나 있는 건지 처음에는 판단이 안 섰습니다. 둘 다 원인일 수 있어서 작업표시줄 쪽을 하나씩 뜯어보면서 현재 빌드에서 실제로 어떻게 잡히는지 직접 확인하는 수밖에 없었습니다. 게다가 원본은 시작 버튼이 중앙에 오는 경우나 위젯 버튼 같은 요소를 전혀 고려하지 않고 있어서, 라이브러리화하면서 새로 신경 써야 했습니다.

그래서 원본에서는 UI Automation 사용 방식과 창 크기/위치를 잡는 Win32 API 정도만 참고하고, 빈 공간을 계산하는 로직 자체는 처음부터 다시 짰습니다. 시작 버튼, 작업표시줄 앱 버튼 그룹, 위젯 버튼, 알림 영역 위치를 읽어와 남는 공간을 구해야 하는데, 작업표시줄 정렬이 좌측인지 중앙인지에 따라 여유 공간이 생기는 자리가 달라지기도 해서 이런 부분을 새로 고려해야하기도 했고요.

---

### 실제로 앱 하나 만들어서 스토어에 올렸습니다: BarPlay

라이브러리가 진짜 쓸만한지 확인하고 싶어서, 이걸로 앱 하나를 만들어 Microsoft Store에 등록했습니다. 이름은 **[BarPlay](https://github.com/airtaxi/BarPlay)** 입니다.

작업표시줄에 지금 재생 중인 미디어의 썸네일, 제목, 컨트롤을 띄워주는 위젯입니다. Spotify, 브라우저, YouTube PWA 앱 등 Windows 시스템 미디어 컨트롤(SMTC)을 지원하는 앱이면 모두 동작합니다. NativeAOT로 컴파일해서 시작 속도와 리소스 사용량을 최소화했습니다.

[Microsoft Store 앱 링크](https://apps.microsoft.com/detail/9N841L4XR28R)

주변 지인들에게 먼저 소개해 봤는데 반응이 꽤 좋았습니다.

---

### 어디에 쓸 수 있을까

WinUI 3나 WPF로 만드는 콘텐츠를 별도 창을 열지 않고도 항상 보이는 자리에 둘 수 있습니다. 타이머, 미디어 재생 컨트롤(BarPlay처럼), 빌드 상태나 CI 알림, 시스템 모니터, 퀵런처나 계정 전환, 알림 표시기 같은 용도를 생각해 볼 수 있겠네요.

본인 앱의 컨트롤과 스타일을 그대로 가져가면서 작업표시줄에 올릴 수 있어서, 데스크밴드가 사라진 Windows 11에서 이런 경험을 구현할 수 있는 거의 유일한 .NET 라이브러리라고 생각합니다.

---

### 링크 모음

- [Deskband11Lib (라이브러리)](https://github.com/airtaxi/Deskband11Lib)
- [NuGet (WinUI)](https://www.nuget.org/packages/Deskband11Lib.WinUI)
- [NuGet (WPF)](https://www.nuget.org/packages/Deskband11Lib.Wpf)
- [BarPlay (Proof of Concept, Store)](https://apps.microsoft.com/detail/9N841L4XR28R)
- [BarPlay (소스코드)](https://github.com/airtaxi/BarPlay)
- [원본 영감 (zadjii/Deskband11)](https://github.com/zadjii/Deskband11)

MIT 라이선스이고, 샘플 프로젝트(`Deskband11Lib.WinUI.Sample`, `Deskband11Lib.Wpf.Sample`)를 복사해서 시작하실 수 있습니다. 피드백, 이슈, PR 모두 환영합니다. 재미있는 작업표시줄 위젯이 만들어지면 알려주세요.

## 원문
- [원문](https://github.com/airtaxi/Deskband11Lib)
- [GeekNews 토론](https://news.hada.io/topic?id=30817)

## My Note
<!-- 한 줄 코멘트 남기기 -->
