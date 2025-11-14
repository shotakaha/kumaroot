# キャンバスを作成したい（`TCanvas`）

```cpp
#include <TCanvas.h>

// キャンバスを作成
TCanvas *c = new TCanvas("c1", "Canvas Title", 800, 600);
c->Draw();
```

`TCanvas`はROOTで図形やグラフを描画するための描画領域（キャンバス）を提供するクラスです。
ヒストグラムやグラフなどのオブジェクトはTCanvas上に描画されます。

```{note}
ROOTの対話モードで`h->Draw()`を実行した場合、キャンバスが存在しなければ自動的に生成されます。
ただし、マクロやスクリプトではキャンバスを明示的に作成することが推奨されます。
```

```python
from ROOT import TCanvas

# キャンバスを作成
c = TCanvas("c1", "Canvas Title", 800, 600)
c.Draw()
```

## コンストラクターのシグネチャ

```cpp
// デフォルトコンストラクター
TCanvas();

// 基本的なコンストラクター
TCanvas(const char *name,
        const char *title = "",
        Int_t ww = 0,
        Int_t wh = 0);

// 詳細なコンストラクター（位置とサイズを指定）
TCanvas(const char *name,
        const char *title,
        Int_t wtopx,
        Int_t wtopy,
        Int_t ww,
        Int_t wh);
```

## コンストラクターのパラメーター

### 基本的なコンストラクター

**name** - キャンバスの識別名

- オブジェクト識別用
- ROOTファイルでの保存
- 同じディレクトリ内では一意

**title** - キャンバスのタイトル

- ウィンドウのタイトルバーに表示

**ww** - キャンバスの幅（ピクセル）

- デフォルト値：0（自動決定）
- 0の場合は約700ピクセル

**wh** - キャンバスの高さ（ピクセル）

- デフォルト値：0（自動決定）
- 0の場合は約600ピクセル

### 詳細なコンストラクター（位置とサイズ指定）

**wtopx** - ウィンドウの左端のX座標

**wtopy** - ウィンドウの上端のY座標

**ww** - キャンバスの幅（ピクセル）

**wh** - キャンバスの高さ（ピクセル）

## キャンバスを作成したい

```cpp
#include <TCanvas.h>

// パターン1：デフォルトサイズ
TCanvas *c1 = new TCanvas("c1", "My Canvas");

// パターン2：サイズ指定
TCanvas *c2 = new TCanvas("c2", "Large Canvas", 1024, 768);

// パターン3：位置とサイズを指定
TCanvas *c3 = new TCanvas("c3", "Positioned Canvas", 100, 50, 800, 600);
// X座標100、Y座標50の位置に、幅800、高さ600のキャンバスを作成

c1->Draw();
c2->Draw();
c3->Draw();
```

## グラフやヒストグラムを描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

// キャンバスを作成
TCanvas *c = new TCanvas("c", "Histogram Canvas", 800, 600);

// ヒストグラムを作成
TH1D *h = new TH1D("h", "Gaussian Distribution", 100, -3, 3);

// データを入力
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// キャンバスに描画
h->Draw();

// キャンバスを保存
c->SaveAs("histogram.png");
```

## キャンバスを分割したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c", "Divided Canvas", 1200, 800);

// キャンバスを2×2に分割
c->Divide(2, 2);

// 各領域に異なるヒストグラムを描画
for (int i = 1; i <= 4; i++) {
    c->cd(i);  // i番目の領域を選択
    TH1D *h = new TH1D(Form("h%d", i), Form("Histogram %d", i), 100, -3, 3);
    for (int j = 0; j < 10000; j++) {
        h->Fill(gRandom->Gaus(0, 1));
    }
    h->Draw();
}
```

`Divide(nx, ny)`でキャンバスをnx×nyの領域に分割できます。
`cd(i)`で描画対象の領域を選択します。

## キャンバスをファイルに保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);

TH1D *h = new TH1D("h", "Histogram", 100, -3, 3);
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}
h->Draw();

// 異なるフォーマットで保存
c->SaveAs("output.png");   // PNG形式
c->SaveAs("output.pdf");   // PDF形式
c->SaveAs("output.eps");   // EPS形式
c->SaveAs("output.gif");   // GIF形式
c->SaveAs("output.root");  // ROOT形式
```

`SaveAs()`メソッドでキャンバスをさまざまなフォーマットで保存できます。
ファイル名の拡張子で出力形式が決定されます。

## キャンバスの表示を更新したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TGraph *g = new TGraph();

// グラフに点を追加して随時更新
for (int i = 0; i < 100; i++) {
    g->SetPoint(i, i, i * i);
    if (i % 10 == 0) {
        g->Draw("AL");
        c->Update();  // キャンバスを更新して表示
    }
}
```

`Update()`メソッドでキャンバスの表示を更新できます。

## 関連メソッド

- [TCanvas::Divide](./root-tcanvas-divide.md) - キャンバスを分割する
- [TCanvas::Draw](./root-tcanvas-draw.md) - グラフを描画する
- [TCanvas::SaveAs](./root-tcanvas-pdf.md) - ファイルに保存する
- [TCanvas::cd](./root-tcanvas-cd.md) - 領域を選択する
- [TLegend](./root-tlegend.md) - 凡例を追加する

## 参考資料

- [ROOT Documentation - TCanvas](https://root.cern/doc/master/classTCanvas.html)
