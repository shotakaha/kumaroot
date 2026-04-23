# キャンバスを保存したい（`TCanvas::SaveAs`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TH1D *h = new TH1D("h", "Histogram", 100, 0, 10);
h->FillRandom("gaus", 1000);
h->Draw();

c->SaveAs("output.png");   // PNG形式
c->SaveAs("output.pdf");   // PDF形式
c->SaveAs("output.root");  // ROOT形式
```

`TCanvas::SaveAs`でキャンバスをさまざまな形式で保存できます。
拡張子で保存形式が自動的に判定されます。

```python
from ROOT import TCanvas, TH1D

c = TCanvas("c", "Canvas", 800, 600)
h = TH1D("h", "Histogram", 100, 0, 10)
h.FillRandom("gaus", 1000)
h.Draw()

c.SaveAs("output.png")
c.SaveAs("output.pdf")
c.SaveAs("output.root")
```

## 保存形式について

| 拡張子 | 形式 | 用途 |
|--------|------|------|
| `.png` | PNG | ウェブ・プレゼンテーション |
| `.pdf` | PDF | 論文・レポート（拡大しても劣化しない） |
| `.root` | ROOT形式 | 後から再編集したい場合 |
| `.eps` | EPS | PostScript形式 |
| `.svg` | SVG | ベクター画像 |
| `.jpg` | JPEG | ラスター画像 |
| `.tex` | LaTeX | LaTeXコード |

## 関連メソッド

- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TCanvas::Print](./root-tcanvas-print.md) - キャンバスを印刷する

## 参考資料

- [ROOT Documentation - TCanvas::SaveAs](https://root.cern/doc/master/classTCanvas.html)
