# キャンバスを分割したい（`TCanvas::Divide`）

```cpp
c->Divide(
    1,  // nx: 列数
    1,  // ny: 行数
    0.01,  // xmargin: Xマージン（0.0-1.0）
    0.01   // ymargin: Yマージン（0.0-1.0）
    0,     // color: パッドの背景色（オプション）
)
```

`TCanvas::Divide`でキャンパスを複数のパッド領域（`TPad`）に分割できます。

第一引数（`nx`）と第二引数（`ny`）で列数と行数を指定します。
第三引数（`xmargin`）と第四引数（`ymargin`）でパッド間のマージンを変更できます。
第五引数（`color`）でパッド領域の背景色を変更できます。

```cpp
// +---+---+
// | 1 | 2 |
// +---+---+
// | 3 | 4 |
// +---+---+
// | 5 | 6 |
// +---+---+

c->Divide(2, 3);

// 5番目のパッドを選択
c->cd(5);

// 全体を選択
c->cd(0);
```

上記のサンプルは、キャンバスを2列3行に分割しています。
`TCanvas::cd`で描画対象のパッドを選択できます。
このサンプルでは5番目のパッドが選択しています。
`cd(0)`でキャンバス全体を選択できます。

## マージンを調整したい（`TPad::SetLeftMargin`）

```cpp
gPad->SetLeftMargin(0.15);  // 左マージンを15%に設定（default: 0.10）
gPad->SetBottomMargin(0.12); // 下マージンを12%に設定（default: 0.10）
gPad->SetRightMargin(0.05); // 右マージンを5%に設定（default: 0.05）
gPad->SetTopMargin(0.05);   // 上マージンを5%に設定（default: 0.05）
```

`TPad::SetLeftMargin`や`TPad::SetBottomMargin`などのメソッドで、
キャンバスの余白を調整できます。
マージンは領域の端から描画領域までのスペースで、デフォルトは0.01（1%）です。
軸ラベルが切れないように左と下のマージンを広めに設定するとよいです。

## 描画領域を切り替えたい（`TCanvas::cd`）

```cpp
#include <TCanvas.h>
#include <TGraph.h>
#include <TMath.h>

TCanvas *c = new TCanvas("c", "Canvas", 1200, 800);
c->Divide(1, 2);

c->cd(1);
TGraph *g1 = new TGraph();
for (int i = 0; i < 10; i++) g1->SetPoint(i, i, i * i);
g1->SetTitle("Upper Area");
g1->Draw("APL");

c->cd(2);
TGraph *g2 = new TGraph();
for (int i = 0; i < 10; i++) g2->SetPoint(i, i, TMath::Sqrt(i));
g2->SetTitle("Lower Area");
g2->Draw("APL");
```

`TCanvas::cd`で描画領域を切り替えて、
複数のヒストグラムやグラフを同じキャンバスに描画できます。

```cpp
// 2列×2行に分割
c->Divide(2, 2);
// +---+---+
// | 1 | 2 |
// +---+---+
// | 3 | 4 |
// +---+---+

// 2列x3行の分割
c->Divide(2, 3);
// +---+---+
// | 1 | 2 |
// +---+---+
// | 3 | 4 |
// +---+---+
// | 5 | 6 |
// +---+---+
```

領域番号は左上が1で、左から右、上から下の順に増加します。

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c", "Divided Canvas", 1200, 800);
c->Divide(2, 2);

for (int i = 1; i <= 4; i++) {
    c->cd(i);
    TH1D *h = new TH1D(Form("h%d", i), Form("Histogram %d", i), 100, -3, 3);
    for (int j = 0; j < 10000; j++) h->Fill(gRandom->Gaus(0, 1));
    h->Draw();
}
```

ループ処理と組み合わせて、複数のヒストグラムを効率的に描画できます。

```cpp
c->cd(0);
```

0を指定するとメインキャンバスが選択されます。

## 関連メソッド

- [TCanvas](./root-tcanvas.md) - キャンバスの基本
- [TCanvas::SaveAs](./root-tcanvas-saveas.md) - 分割されたキャンバスを保存する

## 参考資料

- [ROOT Documentation - TCanvas::Divide](https://root.cern/doc/master/classTCanvas.html#a3be10e7ba1175f4fa9b1e17d3a3a0a85)
- [ROOT Documentation - TCanvas::cd](https://root.cern/doc/master/classTCanvas.html#abed08c1fdb30e5a73d9e3d09e31cb8eb)
