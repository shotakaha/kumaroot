# キャンバスの表示を更新したい（`TCanvas::Update`）

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TGraph *g = new TGraph();

for (int i = 0; i < 100; i++) {
    g->SetPoint(i, i, i * i);
    if (i % 10 == 0) {
        g->Draw("AL");
        c->Update();  // キャンバスを更新して表示
    }
}
```

`TCanvas::Update`でキャンバスの表示を強制的に更新できます。
ループ処理中にリアルタイムで描画を反映させたい場合に使います。

```python
from ROOT import TCanvas, TGraph

c = TCanvas("c", "Canvas", 800, 600)
g = TGraph()

for i in range(100):
    g.SetPoint(i, i, i * i)
    if i % 10 == 0:
        g.Draw("AL")
        c.Update()
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

## 関連メソッド

- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TCanvas::Divide](./root-tcanvas-divide.md) - キャンバスを分割する
- [TCanvas::Print](./root-tcanvas-print.md) - 複数ページのPDFに保存する

## 参考資料

- [ROOT Documentation - TCanvas::Update](https://root.cern/doc/master/classTCanvas.html)
