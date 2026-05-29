# リアルタイム更新したい（`TCanvas::Modified` / `TCanvas::Update`）

```cpp
#include <TCanvas.h>
#include <TGraph.h>

void macro() {
    TCanvas *c = new TCanvas("c", "Real-time Monitor", 800, 600);
    TGraph *g = new TGraph();

    for (int i = 0; i < 100; i++) {
        g->SetPoint(i, i, i * i);
        if (i % 10 == 0) {
            g->Draw("AL");
            c->Modified();  // Mark canvas as changed
            c->Update();  // Flush to screen
        }
        gSystem->ProcessEvents();  // Handle GUI events
    }
}
```

キャンバスをリアルタイムで更新したい場合は、
`TCanvas::Modified` -> `TCanvas::Update`の2ステップが必要です。

`TCanvas::Modified`はキャンバスが変更されたことをマークします。
`TCanvas::Update`は変更を画面に反映させます。

`gSystem->ProcessEvents`は、
マウスやキーボード操作などのGUIイベントを処理するためのメソッドです。
イベントループで毎回呼ぶことで、描画中もウィンドウが応答するようになります。

```python
from ROOT import TCanvas, TGraph, gSystem

def macro():
    c = TCanvas("c", "Real-time Monitor", 800, 600)
    g = TGraph()

    for i in range(100):
        g.SetPoint(i, i, i * i)
        if i % 10 == 0:
            g.Draw("AL")
            c.Modified()  # Mark canvas as changed
            c.Update()  # Flush to screen
        gSystem.ProcessEvents()  # Handle GUI events
```

## グラフを段階的に描画したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>
#include <TSystem.h>
#include <TMath.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TGraph *g = new TGraph();

for (int i = 0; i < 100; i++) {
    g->SetPoint(i, i * 0.1, TMath::Sin(i * 0.1));
    if (i % 10 == 0) {
        g->Draw("AL");
        c->Update();
        gSystem->Sleep(100);  // 100ミリ秒待機
    }
}
g->Draw("AL");
c->Update();
```

`gSystem->Sleep()`と組み合わせることで、グラフが描かれていく様子を確認できます。

## ヒストグラムを動的に更新したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TH1D *h = new TH1D("h", "Distribution", 100, -3, 3);
h->Draw();

for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
    if (i % 1000 == 0) c->Update();  // 1000個ごとに更新
}
c->Update();
```

`Update`の呼び出しが多すぎると処理が遅くなります。適切な間隔で呼ぶことが大切です。

## アニメーションを作りたい

```cpp
#include <TCanvas.h>
#include <TGraph.h>
#include <TSystem.h>
#include <TMath.h>

TCanvas *c = new TCanvas("c", "Animation", 800, 600);
TGraph *g = new TGraph();

for (int frame = 0; frame < 100; frame++) {
    g->Clear();
    for (int i = 0; i < 50; i++) {
        double x = i * 0.1;
        g->SetPoint(i, x, TMath::Sin(x + frame * 0.1));
    }
    g->SetTitle(Form("Frame %d", frame));
    g->Draw("AL");
    c->Update();
    gSystem->Sleep(16);  // 約60fps
}
```

## サンプリング表示したい

```cpp
void macro() {
    // Non-blocking: DAQ keeps running, display updates periodically
    auto t_last = std::chrono::steady_clock::now();

    while (running) {
        // Acquire new data and fill histogram
        // DAQ is never blocked
        h1->Fill(get_next_sample());

        auto now = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - t_last).count();

        if (elapsed >= 500) {  // Update every 500 ms
            h1->Draw();
            c->Modified();
            c->Update();
            gSystem->ProcessEvents();  // Handle GUI events
            t_last = now;
        }
    }
}
```

イベントレートが高い場合は、表示する頻度を制限するとよいです。
このとき`gSystem->Sleep`を使うと、データ取得もブロックされてしまうため、
`std::chrono`などのタイマーを使って、経過時間ベースで更新するとよいです。

## 関連メソッド

- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TCanvas::Divide](./root-tcanvas-divide.md) - キャンバスを分割する
- [TCanvas::Print](./root-tcanvas-print.md) - 複数ページのPDFに保存する

## 参考資料

- [ROOT Documentation - TCanvas::Update](https://root.cern/doc/master/classTCanvas.html)
