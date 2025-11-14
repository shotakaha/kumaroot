# 複数のキャンバスをPDFに保存したい（`TCanvas::Print`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

// ファイル名を設定
TString filename = "output.pdf";

// キャンバスを作成
TCanvas *c = new TCanvas("c", "Multi-page PDF", 800, 600);

// PDFファイルを開く（最初のページ）
c->Print(filename + "[", "pdf");

// 複数のヒストグラムを描画して保存
for (Int_t i = 0; i < 3; i++) {
    TH1D *h = new TH1D(Form("h%d", i), Form("Histogram %d", i), 100, -3, 3);
    h->FillRandom("gaus", 1000);
    h->Draw();

    // PDFにページを追加
    c->Print(filename, "pdf");
}

// PDFファイルを閉じる
c->Print(filename + "]", "pdf");
```

`TCanvas::Print`メソッドを使って、複数のページを1つのPDFファイルに保存できます。
PDF形式ではページ開始記号`[`と終了記号`]`を使うことで、複数のキャンバスを同じファイルに追記できます。

```python
from ROOT import TCanvas, TH1D

filename = "output.pdf"

c = TCanvas("c", "Multi-page PDF", 800, 600)

# PDFファイルを開く
c.Print(filename + "[", "pdf")

# 複数のページを追加
for i in range(3):
    h = TH1D(f"h{i}", f"Histogram {i}", 100, -3, 3)
    h.FillRandom("gaus", 1000)
    h.Draw()
    c.Print(filename, "pdf")

# PDFファイルを閉じる
c.Print(filename + "]", "pdf")
```

## メソッドのシグネチャ

```cpp
void Print(const char *filename = "", Option_t *option = "")
```

### 引数と戻り値

**引数**:

- **filename** - 出力ファイルパス。PDFマルチページの場合：
  - `filename + "["` - PDFファイルを開く（最初のページ）
  - `filename` - PDFにページを追加
  - `filename + "]"` - PDFファイルを閉じる

- **option** - 出力形式（`"pdf"`、`"ps"`など）

## PDFマルチページの基本パターン

### ページ開始・追加・終了の記号

| 記号 | 説明 | 使用例 |
|------|------|--------|
| `[` | PDFファイルを開く（最初のページは出力しない） | `filename + "["` |
| （通常） | 現在のキャンバスをページとして追加 | `filename` |
| `]` | PDFファイルを閉じる | `filename + "]"` |

### 記号の重要性

- `[` を使わないと、その時点でページが出力される
- `]` を使うことで、PDFファイルが確実に閉じられる
- 複数の `[` と `]` を使うと、エラーが発生する可能性がある

## 使用例

### 複数のヒストグラムを1つのPDFに保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c", "Analysis Results", 800, 600);

TString filename = "analysis.pdf";

// PDFファイルを開く
c->Print(filename + "[", "pdf");

// 複数のヒストグラムを描画して保存
for (Int_t i = 0; i < 5; i++) {
    TH1D *h = new TH1D(Form("h%d", i), Form("Dataset %d", i), 100, -5, 5);

    // ガウス分布でデータを埋める
    for (Int_t j = 0; j < 10000; j++) {
        h->Fill(gRandom->Gaus(0, 1));
    }

    h->Draw();
    c->Print(filename, "pdf");  // ページを追加
}

// PDFファイルを閉じる
c->Print(filename + "]", "pdf");
```

複数のヒストグラムを順番に描画し、各々をPDFの新しいページとして保存します。

### 複数のキャンバスから異なるオブジェクトを保存したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>
#include <TH2D.h>

TString filename = "mixed_objects.pdf";

// 1番目のキャンバス：ヒストグラム
TCanvas *c1 = new TCanvas("c1", "Canvas 1", 800, 600);
c1->Print(filename + "[", "pdf");

TH1D *h = new TH1D("h", "Histogram", 100, -3, 3);
h->FillRandom("gaus", 5000);
h->Draw();
c1->Print(filename, "pdf");

// 2番目のキャンバス：グラフ
TCanvas *c2 = new TCanvas("c2", "Canvas 2", 800, 600);
TGraph *g = new TGraph();
for (Int_t i = 0; i < 100; i++) {
    g->SetPoint(i, i, sin(i * 0.1));
}
g->Draw("AL");
c2->Print(filename, "pdf");

// 3番目のキャンバス：2次元ヒストグラム
TCanvas *c3 = new TCanvas("c3", "Canvas 3", 800, 600);
TH2D *h2 = new TH2D("h2", "2D Histogram", 50, -3, 3, 50, -3, 3);
for (Int_t i = 0; i < 10000; i++) {
    h2->Fill(gRandom->Gaus(), gRandom->Gaus());
}
h2->Draw("colz");
c3->Print(filename, "pdf");

// PDFファイルを閉じる
c3->Print(filename + "]", "pdf");
```

異なるキャンバスや異なるオブジェクト（ヒストグラム、グラフ、2次元ヒストグラムなど）を同じPDFに保存できます。

### ループで大量のページを生成したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TString filename = "large_pdf.pdf";
TCanvas *c = new TCanvas("c", "Large PDF", 800, 600);

c->Print(filename + "[", "pdf");

// 100ページ分のヒストグラムを生成
for (Int_t page = 0; page < 100; page++) {
    TH1D *h = new TH1D(Form("h%d", page),
                       Form("Page %d - Distribution", page),
                       100, -5, 5);

    // 異なる平均値でデータを生成
    Double_t mean = -5 + page * 0.1;
    for (Int_t i = 0; i < 5000; i++) {
        h->Fill(gRandom->Gaus(mean, 1));
    }

    h->Draw();
    c->Print(filename, "pdf");

    // メモリ管理：前のヒストグラムを削除
    delete h;
}

c->Print(filename + "]", "pdf");

std::cout << "PDF file created: " << filename << std::endl;
```

ループを使って大量のページを効率的に生成できます。
メモリ管理を適切に行うことで、スムーズな処理が実現します。

### PostScript形式で複数ページを保存したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TString filename = "output.ps";
TCanvas *c = new TCanvas("c", "PostScript Output", 800, 600);

// PostScript形式で開始
c->Print(filename + "[", "ps");

// 複数のページを追加
for (Int_t i = 0; i < 3; i++) {
    TH1D *h = new TH1D(Form("h%d", i), Form("Page %d", i), 100, 0, 10);
    h->FillRandom("gaus", 1000);
    h->Draw();
    c->Print(filename, "ps");
}

// PostScript形式で終了
c->Print(filename + "]", "ps");
```

PDFと同様に、PostScript形式でも複数ページの出力がサポートされています。

## トラブルシューティング

### PDFが開けない、または破損している場合

```cpp
// 最初と最後の記号が正確に対応していることを確認
c->Print("output.pdf" + "[", "pdf");   // OK: 開始
// ... 処理 ...
c->Print("output.pdf" + "]", "pdf");   // OK: 終了

// ❌ 間違い: 記号が逆
// c->Print("output.pdf" + "]", "pdf");
// c->Print("output.pdf" + "[", "pdf");
```

### 複数のファイルに分割したい場合

```cpp
// 複数のPDFファイルを作成する場合
for (Int_t file = 0; file < 3; file++) {
    TString filename;
    filename.Form("output_%d.pdf", file);

    TCanvas *c = new TCanvas(Form("c%d", file), "", 800, 600);
    c->Print(filename + "[", "pdf");

    for (Int_t page = 0; page < 10; page++) {
        TH1D *h = new TH1D(Form("h%d", page), "", 100, 0, 10);
        h->FillRandom("gaus", 1000);
        h->Draw();
        c->Print(filename, "pdf");
    }

    c->Print(filename + "]", "pdf");
}
```

## 関連メソッド

- [キャンバスを保存したい（`TCanvas::SaveAs`）](./root-tcanvas-saveas.md)
- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)
- [キャンバスを描画したい（`TCanvas::Draw`）](./root-tcanvas-draw.md)

## 参考資料

- [ROOT TCanvas::Print Documentation](https://root.cern/doc/master/classTCanvas.html#a7267521c1e8006e2d4e9b0b8f8ef3d5)
- [ROOT Graphics and Postscript Interface](https://root.cern/doc/master/group__Graphics.html)
