# 複数のキャンバスをPDFに保存したい（`TCanvas::Print`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Multi-page PDF", 800, 600);
TString filename = "output.pdf";

c->Print(filename + "[");  // PDFを開く

for (Int_t i = 0; i < 3; i++) {
    TH1D *h = new TH1D(Form("h%d", i), Form("Histogram %d", i), 100, -3, 3);
    h->FillRandom("gaus", 1000);
    h->Draw();
    c->Print(filename);  // ページを追加
    delete h;
}

c->Print(filename + "]");  // PDFを閉じる
```

`TCanvas::Print`で複数ページのPDFを1ファイルにまとめて保存できます。
`[` で開始し、`]` で閉じるのが基本パターンです。

```python
from ROOT import TCanvas, TH1D

c = TCanvas("c", "Multi-page PDF", 800, 600)
filename = "output.pdf"

c.Print(filename + "[")

for i in range(3):
    h = TH1D(f"h{i}", f"Histogram {i}", 100, -3, 3)
    h.FillRandom("gaus", 1000)
    h.Draw()
    c.Print(filename)

c.Print(filename + "]")
```

## 異なるオブジェクトを1つのPDFに保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TGraph.h>

TString filename = "report.pdf";

TCanvas *c1 = new TCanvas("c1", "Canvas 1", 800, 600);
c1->Print(filename + "[");

// 1ページ目：1次元ヒストグラム
TH1D *h = new TH1D("h", "Histogram", 100, -3, 3);
h->FillRandom("gaus", 5000);
h->Draw();
c1->Print(filename);

// 2ページ目：グラフ
TCanvas *c2 = new TCanvas("c2", "Canvas 2", 800, 600);
TGraph *g = new TGraph();
for (Int_t i = 0; i < 100; i++) g->SetPoint(i, i, sin(i * 0.1));
g->Draw("AL");
c2->Print(filename);

// 3ページ目：2次元ヒストグラム
TCanvas *c3 = new TCanvas("c3", "Canvas 3", 800, 600);
TH2D *h2 = new TH2D("h2", "2D Histogram", 50, -3, 3, 50, -3, 3);
for (Int_t i = 0; i < 10000; i++) h2->Fill(gRandom->Gaus(), gRandom->Gaus());
h2->Draw("colz");
c3->Print(filename + "]");  // 最後のページで閉じる
```

異なるキャンバスの内容を順番にページとして追加できます。
最後の `Print` で `]` を付けてPDFを閉じます。

## 大量のページをループで生成したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TString filename = "large.pdf";

c->Print(filename + "[");

for (Int_t page = 0; page < 100; page++) {
    TH1D *h = new TH1D(Form("h%d", page), Form("Page %d", page), 100, -5, 5);
    h->Fill(gRandom->Gaus(-5 + page * 0.1, 1));
    h->Draw();
    c->Print(filename);
    delete h;  // メモリを解放してから次のページへ
}

c->Print(filename + "]");
```

ループ内で `delete h` してメモリを解放しておくと、大量ページでもメモリ不足になりません。

## 関連メソッド

- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - 1枚の画像として保存する
- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TH1::Draw](./root-th1-draw.md) - ヒストグラムを描画する

## 参考資料

- [ROOT Documentation - TCanvas::Print](https://root.cern/doc/master/classTCanvas.html)
