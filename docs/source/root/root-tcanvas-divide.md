# キャンバスを分割したい（`TCanvas::Divide`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

// キャンバスを作成
TCanvas *c = new TCanvas("c", "Divided Canvas", 1200, 800);

// キャンバスを2×3に分割（6つの領域）
c->Divide(2, 3);

// 5番目の領域に描画する場合
c->cd(5);
```

`TCanvas::Divide`メソッドでキャンバスを複数の領域に分割できます。
`TCanvas::cd`メソッドで描画対象の領域を選択します。
これにより、複数のグラフやヒストグラムを1つのキャンバスに同時に表示できます。

```python
from ROOT import TCanvas, TH1D, TRandom, gRandom

# キャンバスを作成
c = TCanvas("c", "Divided Canvas", 1200, 800)

# キャンバスを2×3に分割
c.Divide(2, 3)

# 5番目の領域に描画
c.cd(5)
```

## メソッドのシグネチャ

```cpp
// キャンバスを分割
void Divide(Int_t nx = 1,
            Int_t ny = 1,
            Float_t xmargin = 0.01,
            Float_t ymargin = 0.01,
            Int_t color = 0);

// 領域を選択
TPad *cd(Int_t subpadnumber = 0);
```

## パラメーターの説明

### Divide()

**nx** - X方向の分割数

- デフォルト値：1
- 例：nx=2, ny=3の場合、2×3 = 6つの領域に分割

**ny** - Y方向の分割数

- デフォルト値：1

**xmargin** - 領域間のX方向マージン

- デフォルト値：0.01（1%）
- 0.0～1.0の範囲で指定

**ymargin** - 領域間のY方向マージン

- デフォルト値：0.01（1%）
- 0.0～1.0の範囲で指定

**color** - 背景色

- デフォルト値：0（白）

### cd()

**subpadnumber** - 領域番号

- 1から始まる番号で領域を指定
- 0の場合はメインキャンバスを選択
- 左上が1、右方向に増加

## 基本的な使い方

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

## マージンを調整したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas with Custom Margins", 1000, 800);

// 2×3に分割、マージンを調整
c->Divide(2, 3, 0.05, 0.05);  // X、Yマージンを5%に設定

for (int i = 1; i <= 6; i++) {
    c->cd(i);
    TH1D *h = new TH1D(Form("h%d", i), Form("Histo %d", i), 50, -3, 3);
    h->FillRandom("gaus", 1000);
    h->Draw();
}
```

マージンを大きくすると領域同士の間隔が広がります。

## 領域のサイズが異なるグリッド

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Uneven Division", 1200, 800);

// 均等な2×2グリッドを作成
c->Divide(2, 2);

// 領域1：メインプロット
c->cd(1);
TH1D *h1 = new TH1D("h1", "Main Plot", 100, -3, 3);
h1->FillRandom("gaus", 5000);
h1->Draw();

// 領域2～4：補助プロット
for (int i = 2; i <= 4; i++) {
    c->cd(i);
    TH1D *h = new TH1D(Form("h%d", i), Form("Sub %d", i), 50, -3, 3);
    h->FillRandom("gaus", 1000);
    h->Draw();
}
```

## 領域を選択した後の操作

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Canvas", 1000, 600);
c->Divide(1, 2);  // 1×2に分割

// 上の領域
c->cd(1);
TGraph *g1 = new TGraph();
for (int i = 0; i < 10; i++) {
    g1->SetPoint(i, i, i * i);
}
g1->SetTitle("Upper Area");
g1->Draw("APL");

// 下の領域
c->cd(2);
TGraph *g2 = new TGraph();
for (int i = 0; i < 10; i++) {
    g2->SetPoint(i, i, sqrt(i));
}
g2->SetTitle("Lower Area");
g2->Draw("APL");
```

## メインキャンバスに戻したい

```cpp
#include <TCanvas.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
c->Divide(2, 2);

// 各領域に描画
for (int i = 1; i <= 4; i++) {
    c->cd(i);
    // ... 描画処理 ...
}

// メインキャンバスに戻す
c->cd(0);
// メインキャンバス上のタイトルなどを追加
c->SetTitle("Main Title");
```

## 注意点

- **領域番号は1から始まる** - 0はメインキャンバスを示す
- **左上から右方向に番号が増加** - 2×3の場合：

```text
1 2
3 4
5 6
```

- **Divide()は複数回呼び出せない** - すでに分割済みのキャンバスに再度Divide()を呼び出すと前の分割は上書きされる
- **マージンの合計が1.0を超えないようにする** - 領域が重なる可能性がある

## 関連メソッド

- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TCanvas::SaveAs](./root-tcanvas-pdf.md) - 分割されたキャンバスを保存
- [TPad](./root-tpad.md) - 領域（パッド）の詳細設定

## 参考資料

- [ROOT Documentation - TCanvas::Divide](https://root.cern/doc/master/classTCanvas.html#a3be10e7ba1175f4fa9b1e17d3a3a0a85)
- [ROOT Documentation - TCanvas::cd](https://root.cern/doc/master/classTCanvas.html#abed08c1fdb30e5a73d9e3d09e31cb8eb)
