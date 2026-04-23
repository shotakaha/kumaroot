# キャンバスを作成したい（`TCanvas`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c1", "My Canvas", 800, 600);

TH1D *h = new TH1D("h", "Gaussian;x;Entries", 100, -3, 3);
for (int i = 0; i < 10000; i++) h->Fill(gRandom->Gaus(0, 1));
h->Draw();

c->SaveAs("output.png");
```

`TCanvas`はROOTの描画領域を提供するクラスです。
ヒストグラムやグラフは`TCanvas`上に描画されます。

```python
from ROOT import TCanvas, TH1D, TRandom3

c = TCanvas("c1", "My Canvas", 800, 600)

h = TH1D("h", "Gaussian;x;Entries", 100, -3, 3)
rng = TRandom3()
for i in range(10000):
    h.Fill(rng.Gaus(0, 1))
h.Draw()

c.SaveAs("output.png")
```

## キャンバスのサイズを変えたい

```cpp
#include <TCanvas.h>

// TCanvas(name, title, width, height)
TCanvas *c = new TCanvas("c1", "My Canvas", 1200, 800);
```

引数はそれぞれ、識別名・タイトル・幅（ピクセル）・高さ（ピクセル）です。
引数なしで作成した場合はデフォルトサイズになります。

## バッチモードで使いたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TROOT.h>

gROOT->SetBatch(true);  // ウィンドウを表示しない

TCanvas *c = new TCanvas("c1", "My Canvas", 800, 600);
// ... 描画処理 ...
c->SaveAs("output.png");
```

マクロやスクリプトでファイルに書き出すだけの場合は、
`gROOT->SetBatch(true)`でウィンドウ表示を抑制できます。

```python
from ROOT import TCanvas, gROOT

gROOT.SetBatch(True)

c = TCanvas("c1", "My Canvas", 800, 600)
```

## 関連メソッド

- [TCanvas::Divide](./root-tcanvas-divide.md) - キャンバスを分割する
- [TCanvas::Draw](./root-tcanvas-draw.md) - キャンバスの内容を再描画する
- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - ファイルに保存する
- [TCanvas::Update](./root-tcanvas-update.md) - キャンバスを更新する
- [TLegend](./root-tlegend.md) - 凡例を追加する

## 参考資料

- [ROOT Documentation - TCanvas](https://root.cern/doc/master/classTCanvas.html)
