# キャンバスを保存したい（`TCanvas::SaveAs`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TH1D *h = new TH1D("h", "Histogram", 100, 0, 10);
h->FillRandom("gaus", 1000);
h->Draw();

// 各形式で保存
c->SaveAs("output.png");     // PNG形式
c->SaveAs("output.pdf");     // PDF形式
c->SaveAs("output.root");    // ROOT形式
c->SaveAs("output.eps");     // EPS形式
```

`TCanvas::SaveAs`メソッドでキャンバスをさまざまな形式で保存できます。
PNG、PDF、ROOT、EPS、SVGなど複数の出力形式に対応しています。

```python
from ROOT import TCanvas, TH1D

c = TCanvas("c", "Canvas", 800, 600)
h = TH1D("h", "Histogram", 100, 0, 10)
h.FillRandom("gaus", 1000)
h.Draw()

# 各形式で保存
c.SaveAs("output.png")
c.SaveAs("output.pdf")
c.SaveAs("output.root")
```

## メソッドのシグネチャ

```cpp
void SaveAs(const char *filename = "", Option_t *option = "")
```

### 引数と戻り値

**引数**:

- **filename** - 出力ファイルパスと名前。ファイル拡張子で形式が判定されます
- **option** - 出力オプション（形式によって異なります）

## ファイル形式について

キャンバスを保存できる主な形式：

| 拡張子 | 形式 | 説明 |
|--------|------|------|
| `.png` | PNG | ラスター画像（推奨） |
| `.pdf` | PDF | ポータブルドキュメント |
| `.root` | ROOT形式 | ROOT ファイル（編集可能） |
| `.eps` | EPS | PostScript形式 |
| `.svg` | SVG | ベクター画像 |
| `.jpg` | JPEG | ラスター画像 |
| `.gif` | GIF | アニメーション画像 |
| `.tex` | LaTeX | LaTeX コード |

## 使用例

### PNG形式で保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TH1D *h = new TH1D("h", "Data", 100, 0, 10);
h->FillRandom("gaus", 1000);
h->Draw();

// PNG形式で保存
c->SaveAs("histogram.png");
```

PNG形式はウェブでの使用やプレゼンテーション資料に適しています。
ファイルサイズは比較的小さく、ほとんどのアプリケーションで開くことができます。

### PDF形式で保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TH1D *h = new TH1D("h", "Data", 100, 0, 10);
h->FillRandom("gaus", 1000);
h->Draw();

// PDF形式で保存
c->SaveAs("histogram.pdf");
```

PDF形式は論文やレポートに最適です。
ベクター図形として保存されるため、拡大縮小しても品質が劣化しません。

### ROOT形式で保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TH1D *h = new TH1D("h", "Data", 100, 0, 10);
h->FillRandom("gaus", 1000);
h->Draw();

// ROOT形式で保存（編集可能）
c->SaveAs("canvas.root");
```

ROOT形式で保存することで、キャンバス全体をROOTファイルとして保存できます。
後でROOTを使って再度開き、さらに編集することが可能です。

### 高解像度で保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 1600, 1200);
TH1D *h = new TH1D("h", "Data", 100, 0, 10);
h->FillRandom("gaus", 1000);
h->Draw();

// キャンバスサイズを大きくしてから保存
c->SaveAs("histogram_high_res.png");
```

キャンバスのサイズを大きくしてから保存することで、高解像度の画像を得られます。
グラフのサイズを `new TCanvas(name, title, width, height)` で指定します。

## 出力オプション

形式によって異なるオプションが使用できます：

```cpp
// PNG形式のオプション例
c->SaveAs("histogram.png", "");

// PDF形式で複数ページ出力
c->SaveAs("histogram.pdf");

// PostScript形式の詳細オプション
c->SaveAs("histogram.eps", "");
```

詳細なオプションはROOT公式ドキュメントを参照してください。

## 関連メソッド

- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)
- [キャンバスを描画したい（`TCanvas::Draw`）](./root-tcanvas-draw.md)
- [キャンバスを印刷したい（`TCanvas::Print`）](./root-tcanvas-print.md)

## 参考資料

- [ROOT TCanvas::SaveAs Documentation](https://root.cern/doc/master/classROOT_1_1Math_1_1LorentzVector.html)
- [ROOT Graphics Output Formats](https://root.cern/doc/master/group__Graphics.html)
