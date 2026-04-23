# ヒストグラムを描画したい（`TH1::Draw`）

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);

TH1D *h = new TH1D("h", "Histogram", 100, -5, 5);
TRandom3 rng;
for (int i = 0; i < 10000; i++) h->Fill(rng.Gaus(0, 1));

h->Draw();
c->SaveAs("output.png");
```

`TH1::Draw`でヒストグラムをキャンバスに描画できます。
引数に描画オプションを指定することで表示スタイルを変えられます。

```python
from ROOT import TH1D, TCanvas, TRandom3

c = TCanvas("c", "Canvas", 800, 600)

h = TH1D("h", "Histogram", 100, -5, 5)
rng = TRandom3()
for i in range(10000):
    h.Fill(rng.Gaus(0, 1))

h.Draw()
c.SaveAs("output.png")
```

## 描画オプション

| オプション | 説明 |
| --------- | ---- |
| （デフォルト） | バーグラフ |
| `"HIST"` | アウトラインのみ |
| `"E"` | エラーバー付き |
| `"E1"` | エラーバー付き（端に横線あり） |
| `"E2"` | エラーを矩形で表示 |
| `"C"` | スプライン曲線 |
| `"L"` | 折れ線 |
| `"P"` | マーカー |
| `"BAR"` | 棒グラフ |
| `"SAME"` | 前の描画に重ねる |
| `"COLZ"` | カラーマップ（TH2向け） |

## エラーバー付きで描画したい

```cpp
h->Draw("E");
```

統計誤差（ビン内容の平方根）をエラーバーで表示します。
測定データを扱うときに使いましょう。

```python
h.Draw("E")
```

## 複数のヒストグラムを重ねて描画したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);

TH1D *h1 = new TH1D("h1", "Signal", 100, -5, 5);
TH1D *h2 = new TH1D("h2", "Background", 100, -5, 5);

TRandom3 rng;
for (int i = 0; i < 5000; i++) {
    h1->Fill(rng.Gaus(0, 1));
    h2->Fill(rng.Gaus(1, 1.5));
}

h1->SetLineColor(kRed);
h2->SetLineColor(kBlue);

h1->Draw();
h2->Draw("SAME");

c->BuildLegend();
```

`"SAME"`オプションで2本目以降を重ねて描画できます。
色を変えておくと見分けやすくなります。

## 描画スタイルを比較したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
c->Divide(2, 2);

TH1D *h = new TH1D("h", "Data", 100, -5, 5);
TRandom3 rng;
for (int i = 0; i < 5000; i++) h->Fill(rng.Gaus(0, 1));

c->cd(1); h->Draw();        // デフォルト
c->cd(2); h->Draw("HIST");  // アウトラインのみ
c->cd(3); h->Draw("E");     // エラーバー
c->cd(4); h->Draw("C");     // スプライン曲線
```

## ログスケールで描画したい

```cpp
TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
c->SetLogy();
h->Draw();
```

`SetLogy()`でY軸をログスケールにできます。
`SetLogx()`でX軸も同様に設定できます。

## 関連メソッド

- [TH1::Fill](./root-th1-fill.md) - データを入力する
- [TH1::Fit](./root-th1-fit.md) - フィットする
- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - ファイルに保存する
- [TCanvas::Divide](./root-tcanvas-divide.md) - キャンバスを分割する
- [TCanvas::SetLog](./root-tcanvas-log.md) - ログスケールに設定する

## 参考資料

- [ROOT Documentation - TH1::Draw](https://root.cern/doc/master/classTH1.html)
- [ROOT Drawing Options](https://root.cern/doc/master/classTH1.html#a90c3bd37049675c14c0e06a24e18b53f)
