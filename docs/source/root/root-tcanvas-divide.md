# キャンバスを分割したい（`TCanvas::Divide`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Divided Canvas", 1200, 800);

// 2列×3行に分割（6つの領域）
c->Divide(2, 3);

// 5番目の領域に描画
c->cd(5);
```

`TCanvas::Divide`でキャンバスを複数の領域に分割できます。
`TCanvas::cd`で描画対象の領域を選択します。

```python
from ROOT import TCanvas

c = TCanvas("c", "Divided Canvas", 1200, 800)

c.Divide(2, 3)
c.cd(5)
```

## 複数のヒストグラムを描画したい（`TCanvas::cd`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c", "Divided Canvas", 1200, 800);
c->Divide(2, 2);

for (int i = 1; i <= 4; i++) {
    c->cd(i);
    TH1D *h = new TH1D(Form("h%d", i), Form("Histogram %d", i), 100, -3, 3);
    for (int j = 0; j < 10000; j++) h->Fill(gRandom->Gaus(0, 1));
    h->Draw();
}
```

領域番号は左上が1で、左から右、上から下の順に増加します。
`Divide(2, 2)`の場合の領域番号は以下のとおりです。

```text
1  2
3  4
```

0を指定するとメインキャンバスが選択されます。

## マージンを調整したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 1200, 800);

// X・Yマージンを5%に設定（デフォルトは1%）
c->Divide(2, 3, 0.05, 0.05);

for (int i = 1; i <= 6; i++) {
    c->cd(i);
    TH1D *h = new TH1D(Form("h%d", i), Form("Histo %d", i), 50, -3, 3);
    h->FillRandom("gaus", 1000);
    h->Draw();
}
```

## グラフを描画したい（`TCanvas::cd`）

```cpp
#include <TCanvas.h>
#include <TGraph.h>
#include <TMath.h>

TCanvas *c = new TCanvas("c", "Canvas", 1200, 800);
c->Divide(1, 2);

c->cd(1);
TGraph *g1 = new TGraph();
for (int i = 0; i < 10; i++) g1->SetPoint(i, i, i * i);
g1->SetTitle("Upper Area");
g1->Draw("APL");

c->cd(2);
TGraph *g2 = new TGraph();
for (int i = 0; i < 10; i++) g2->SetPoint(i, i, TMath::Sqrt(i));
g2->SetTitle("Lower Area");
g2->Draw("APL");
```

## メインキャンバスに戻したい

```cpp
#include <TCanvas.h>

TCanvas *c = new TCanvas("c", "Canvas", 1200, 800);
c->Divide(2, 2);

for (int i = 1; i <= 4; i++) {
    c->cd(i);
    // ... 描画処理 ...
}

// メインキャンバスに戻す
c->cd(0);
```

`cd(0)`でメインキャンバスに戻ります。

## 関連メソッド

- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - 分割されたキャンバスを保存する

## 参考資料

- [ROOT Documentation - TCanvas::Divide](https://root.cern/doc/master/classTCanvas.html#a3be10e7ba1175f4fa9b1e17d3a3a0a85)
- [ROOT Documentation - TCanvas::cd](https://root.cern/doc/master/classTCanvas.html#abed08c1fdb30e5a73d9e3d09e31cb8eb)
