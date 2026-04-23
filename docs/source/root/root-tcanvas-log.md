# 対数スケールにしたい（`TCanvas::SetLogy`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Log Scale Canvas", 800, 600);

TH1D *h = new TH1D("h", "Distribution", 100, 0.1, 1000);
h->FillRandom("expo", 1000);

c->SetLogy();
h->Draw();
```

`TCanvas::SetLogy`メソッドでY軸を対数スケール表示に変更できます。
それぞれの軸に対して、`SetLogx`（X軸）や`SetLogz`（Z軸）も同様に使用できます。
大きく異なる値の範囲を視覚的に比較する場合に便利です。

```python
from ROOT import TCanvas, TH1D

c = TCanvas("c", "Log Scale Canvas", 800, 600)

h = TH1D("h", "Distribution", 100, 0.1, 1000)
h.FillRandom("expo", 1000)

c.SetLogy()
h.Draw()
```

```{seealso}

- [](./root-gstyle-setoptlog.md)

`TCanvas::SetLogy`と
`gStyle->SetOptLogy`は異なる設定メソッドです。

`TCanvas::SetLogy`は特定のキャンバスに対して対数スケールを設定するのに対し、
`gStyle->SetOptLogy(1)`はグローバルスタイルを変更して、以降に作成されるすべてのオブジェクトに対数スケールを適用します。

```

## 対数スケールをトグルしたい

```cpp
c->SetLogy(1);  // 対数スケール有効
c->Update();

c->SetLogy(0);  // 通常スケールに戻す
c->Update();
```

`SetLogy(1)`で対数スケール有効、`SetLogy(0)`で無効にできます。
`Update`でキャンバス表示の更新が必要です。

## 両対数したい

```cpp
#include <TCanvas.h>
#include <TH2D.h>

TCanvas *c = new TCanvas("c", "Both Axes Log Scale", 800, 600);

TH2D *h2 = new TH2D("h2", "Power-law Distribution", 50, 0.1, 1000, 50, 0.1, 1000);

for (int i = 0; i < 10000; i++) {
    double x = pow(10, gRandom->Uniform(0, 3));
    double y = pow(10, gRandom->Uniform(0, 3));
    h2->Fill(x, y);
}

c->SetLogx();
c->SetLogy();
h2->Draw("colz");
```

べき乗則やスケーリング則を分析する場合に活用できます。

## キャンバスを分割して一部だけ対数スケールにしたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Mixed Log Scales", 1200, 500);

c->Divide(2, 1);

// パッド1：通常のスケール
c->cd(1);
TH1D *h1 = new TH1D("h1", "Linear Scale", 100, 0, 10);
h1->FillRandom("gaus", 5000);
h1->Draw();

// パッド2：対数スケール
c->cd(2);
TH1D *h2 = new TH1D("h2", "Log Scale", 100, 0.1, 1000);
h2->FillRandom("expo", 5000);
gPad->SetLogy();
h2->Draw();
```

`gPad`は「current pad」（現在のパッド）へのポインターです。
複数のパッドで異なるスケール設定ができます。

## 関連メソッド

- [ヒストグラムを描画したい（`TH1::Draw`）](./root-th1-draw.md)
- [キャンバスを分割したい（`TCanvas::Divide`）](./root-tcanvas-divide.md)
- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)

## 参考資料

- [ROOT TCanvas Documentation](https://root.cern/doc/master/classTCanvas.html)
- [ROOT Graphics Documentation](https://root.cern/doc/master/group__Graphics.html)
