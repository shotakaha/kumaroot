# ヒストグラムを描画したい（`TH1::Draw`）

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 10000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);
h->Draw();
```

`TH1::Draw`メソッドで、ヒストグラムをキャンバスに描画できます。
描画スタイル、色、線種などをカスタマイズして、データを効果的に可視化できます。

```python
from ROOT import TH1D, TCanvas, TRandom3

h = TH1D("h", "Histogram", 100, -5, 5)

random = TRandom3()
for i in range(10000):
    h.Fill(random.Gaus(0, 1))

c = TCanvas("c", "canvas", 600, 400)
h.Draw()
```

## メソッドシグネチャ

```cpp
virtual void Draw(Option_t *option = "")
```

### 引数と戻り値

**引数**:

- **option** - 描画オプション（文字列）
  - `"HIST"` - ヒストグラムのアウトラインのみ
  - `"E"` - 統計誤差（エラーバー）を表示
  - `"E1"` - 誤差バーのスタイル1（角度あり）
  - `"E2"` - 誤差バーのスタイル2（矩形バー）
  - `"BAR"` - 棒グラフスタイル
  - `"BAR1"` - 棒グラフスタイル1
  - `"BAR2"` - 棒グラフスタイル2
  - `"BAR3"` - 棒グラフスタイル3（立体）
  - `"BAR4"` - 棒グラフスタイル4
  - `"SAME"` - 前の描画の上に重ねて描画
  - `"C"` - スムーズな曲線（スプライン）
  - `"L"` - 直線で接続
  - `"*"` - マーカーで表示

**戻り値**:

- なし

## 基本的な描画

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Basic Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

// キャンバスを作成
TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// ヒストグラムを描画
h->Draw();
```

もっとも基本的な描画方法です。デフォルトスタイルでヒストグラムが描画されます。

## 描画スタイルの選択

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 800, 600);
c->Divide(2, 2);

// 標準スタイル
c->cd(1);
h->Draw();

// アウトラインのみ
c->cd(2);
h->Draw("HIST");

// 誤差バー付き
c->cd(3);
h->Draw("E");

// スムーズな曲線
c->cd(4);
h->Draw("C");
```

異なる描画オプションを使用して、ヒストグラムの見た目を変更できます。

## 誤差バー付きで描画したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Histogram with Errors", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// 誤差バーを表示
h->Draw("E");
```

`"E"`オプションで統計誤差（ビンの内容の平方根）をエラーバーで表示できます。

## 複数のヒストグラムを重ねて描画したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h1 = new TH1D("h1", "Distribution 1", 100, -5, 5);
TH1D *h2 = new TH1D("h2", "Distribution 2", 100, -5, 5);

TRandom3 random;

// ヒストグラム1に正規分布（平均0、標準偏差1）
for (int i = 0; i < 5000; i++) {
    h1->Fill(random.Gaus(0, 1));
}

// ヒストグラム2に正規分布（平均1、標準偏差1.5）
for (int i = 0; i < 5000; i++) {
    h2->Fill(random.Gaus(1, 1.5));
}

// 色を設定
h1->SetLineColor(2);  // 赤
h2->SetLineColor(4);  // 青

TCanvas *c = new TCanvas("c", "Overlaid Histograms", 600, 400);

// 最初のヒストグラムを描画
h1->Draw();

// 2番目のヒストグラムを重ねて描画
h2->Draw("SAME");

// 凡例を追加
c->BuildLegend();
```

`"SAME"`オプションで複数のヒストグラムを重ねて描画できます。
異なる色や線種を使用して区別をつけることが重要です。

## 棒グラフとして描画したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Bar Chart", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// 棒グラフとして描画
h->Draw("BAR");
```

`"BAR"`オプションで棒グラフスタイルで描画できます。
カテゴリカルデータやビンの内容を強調したい場合に有効です。

## 複数パネル表示したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h1 = new TH1D("h1", "Dataset 1", 100, -5, 5);
TH1D *h2 = new TH1D("h2", "Dataset 2", 100, -5, 5);
TH1D *h3 = new TH1D("h3", "Dataset 3", 100, -5, 5);
TH1D *h4 = new TH1D("h4", "Dataset 4", 100, -5, 5);

TRandom3 random;

for (int i = 0; i < 5000; i++) {
    h1->Fill(random.Gaus(0, 1));
    h2->Fill(random.Gaus(1, 1));
    h3->Fill(random.Gaus(-1, 1));
    h4->Fill(random.Gaus(0, 1.5));
}

// 2行2列のキャンバスを作成
TCanvas *c = new TCanvas("c", "Multi-panel Display", 800, 600);
c->Divide(2, 2);

// パネル1
c->cd(1);
h1->Draw();

// パネル2
c->cd(2);
h2->Draw();

// パネル3
c->cd(3);
h3->Draw();

// パネル4
c->cd(4);
h4->Draw();
```

`Divide()`メソッドで複数のパネルを持つキャンバスを作成できます。
異なるデータセットや分析結果を比較したい場合に有効です。

## 描画スタイルをカスタマイズしたい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Customized Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// 描画スタイルをカスタマイズ
h->SetLineColor(2);      // 線の色（赤）
h->SetLineWidth(2);      // 線幅
h->SetLineStyle(1);      // 線種（実線）
h->SetFillColor(38);     // 塗りつぶし色（青灰色）
h->SetFillStyle(3003);   // 塗りつぶしパターン
h->SetMarkerColor(1);    // マーカー色（黒）
h->SetMarkerSize(0.8);   // マーカーサイズ
h->SetMarkerStyle(20);   // マーカー種（○）

h->Draw("E");
```

色、線幅、線種、塗りつぶしなど、さまざまなスタイル属性をカスタマイズできます。

## タイトルと軸ラベルを設定したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Distribution of Random Values", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// 軸ラベルを設定
h->GetXaxis()->SetTitle("Value");
h->GetXaxis()->SetTitleSize(0.05);
h->GetXaxis()->SetLabelSize(0.04);

h->GetYaxis()->SetTitle("Frequency");
h->GetYaxis()->SetTitleSize(0.05);
h->GetYaxis()->SetLabelSize(0.04);

h->Draw();
```

軸のタイトル、ラベルサイズ、フォントなどを調整して、可読性を向上させることができます。

## ログスケール表示したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// Y軸をログスケールに設定
c->SetLogy();

// ログスケールで描画
h->Draw();
```

`SetLogy()`でY軸をログスケールに設定できます。
広いダイナミックレンジを持つデータの可視化に有効です。

## 統計情報ボックスを表示したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TStyle.h>

TH1D *h = new TH1D("h", "Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// 統計情報の表示を有効化
gStyle->SetOptStat(1111);  // 平均、RMS、オーバーフロー、アンダーフロー

h->Draw();
```

`SetOptStat()`で統計情報ボックスの表示内容をコントロールできます。
数値は異なる統計情報の表示を制御します。

## 範囲を制限して描画したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Full Data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// X軸の表示範囲を制限
h->GetXaxis()->SetRangeUser(-2, 2);

// Y軸の表示範囲を制限
h->GetYaxis()->SetRangeUser(0, 500);

h->Draw();
```

軸の`SetRangeUser()`メソッドで表示範囲を制限できます。
特定の領域に焦点を当てたい場合に有効です。

## スムーズな曲線で描画したい

```cpp
#include <TH1D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "Smooth Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "canvas", 600, 400);

// スムーズな曲線で描画
h->Draw("C");
```

`"C"`オプションでスプライン補間によるスムーズな曲線で描画できます。
ノイズの多いデータの傾向を視覚化する場合に有効です。

## 2次元ヒストグラムを描画したい

```cpp
#include <TH2D.h>
#include <TCanvas.h>
#include <TRandom3.h>

TH2D *h2 = new TH2D("h2", "2D Histogram", 50, -5, 5, 50, -5, 5);

TRandom3 random;
for (int i = 0; i < 10000; i++) {
    h2->Fill(random.Gaus(0, 1), random.Gaus(0, 1));
}

TCanvas *c = new TCanvas("c", "2D Histogram", 600, 600);

// 2次元ヒストグラムを描画
h2->Draw("COLZ");
```

2次元ヒストグラムは`"COLZ"`オプションでカラーマップで描画できます。
2つの変数の相関を可視化する場合に有効です。

## 関連メソッド

- [SetLineColor](./root-tf1-setlinecolor.md) - 線の色を設定
- [SetFillColor](./root-th1-setfillcolor.md) - 塗りつぶし色を設定
- [GetXaxis](./root-th1-getxaxis.md) - X軸を取得
- [GetYaxis](./root-th1-getyaxis.md) - Y軸を取得
- [Fit](./root-th1-fit.md) - ヒストグラムをフィット
- [Fill](./root-th1-fill.md) - ヒストグラムにデータを入力

## 参考リンク

- [ROOT TH1::Draw Documentation](https://root.cern/doc/master/classTH1.html#a7e7d8ff3b6b6b6b6b6b)
- [ROOT TH1 Documentation](https://root.cern/doc/master/classTH1.html)
- [ROOT TCanvas Documentation](https://root.cern/doc/master/classTCanvas.html)
- [ROOT Drawing Options](https://root.cern/doc/master/classTH1.html#a90c3bd37049675c14c0e06a24e18b53f)
