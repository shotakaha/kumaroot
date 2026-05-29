# キャンバスしたい（`TCanvas`）

```cpp
TCanvas *c1 = new TCanvas(
    "c1",         // name
    "My Canvas",  // title
    1200,         // ww: default 800
    800           // wh: default 600
);
```

`TCanvas`はキャンバスを管理するクラスです。
アクティブな描画領域は`gPad`というグローバルポインターで参照できます。
ヒストグラムやグラフは`gPad`に描画されます。

第一引数（`name`）にオブジェクト名、
第二引数（`title`）にウィンドウのタイトルを指定できます。

キャンバス作成時に、キャンバスのサイズを変更できます。
幅（`ww`）と高さ（`wh`）を調整できます。
デフォルトは幅800ピクセル、高さ600ピクセルです。

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

## バッチモードしたい（`gROOT::SetBatch`）

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
- [TH1::Draw](./root-th1-draw.md) - ヒストグラムを描画する
- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - ファイルに保存する
- [TCanvas::Update](./root-tcanvas-update.md) - キャンバスを更新する
- [TLegend](./root-tlegend.md) - 凡例を追加する

## 参考資料

- [ROOT Documentation - TCanvas](https://root.cern/doc/master/classTCanvas.html)
