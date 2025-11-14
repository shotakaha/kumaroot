# グラフを描画したい（`TCanvas::Draw`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);

TH1D *h = new TH1D("h", "Histogram", 100, -3, 3);
h->FillRandom("gaus", 1000);

// キャンバスに描画
h->Draw();
```

`TCanvas::Draw`メソッドでオブジェクト（ヒストグラム、グラフなど）をキャンバスに描画できます。
描画オプションで表示スタイルをカスタマイズできます。

```python
from ROOT import TCanvas, TH1D

c = TCanvas("c", "Canvas", 800, 600)

h = TH1D("h", "Histogram", 100, -3, 3)
h.FillRandom("gaus", 1000)

# キャンバスに描画
h.Draw()
```

## メソッドのシグネチャ

```cpp
void Draw(Option_t *option = "")
```

### 引数と戻り値

**引数**:

- **option** - 描画オプション（オブジェクトの種類によって異なります）

**戻り値**:

- なし

## ヒストグラムの描画オプション

ヒストグラムの描画ではさまざまなオプションが使用できます：

| オプション | 説明 |
|-----------|------|
| （デフォルト） | バーグラフ |
| `"E"` | エラーバー付き |
| `"E1"` | エラーバー付き（点線） |
| `"E2"` | エラーバーのみ |
| `"E3"` | エラーフィルエリア |
| `"E4"` | 拡張エラーバー |
| `"C"` | 曲線接続 |
| `"L"` | 折れ線グラフ |
| `"*"` | 点描画 |
| `"P"` | マーカー付き |
| `"B"` | バーグラフ |
| `"HIST"` | ステップヒストグラム |

## 使用例

### ヒストグラムを描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Histogram", 800, 600);

TH1D *h = new TH1D("h", "Distribution", 100, -5, 5);

// データを追加
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// ヒストグラムを描画
h->Draw();
```

基本的なバーグラフ形式でヒストグラムを描画します。

### エラーバー付きで描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Histogram with Error Bars", 800, 600);

TH1D *h = new TH1D("h", "Data with Errors", 50, -5, 5);

// データを追加
for (int i = 0; i < 5000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// エラーバー付きで描画
h->Draw("E");
```

統計的なエラーバーを表示します。

### 曲線で描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Smooth Histogram", 800, 600);

TH1D *h = new TH1D("h", "Distribution", 50, -5, 5);

// データを追加
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// 曲線で描画
h->Draw("C");
```

ヒストグラムの値を曲線で接続して表示します。

### 複数のヒストグラムを重ねて描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Overlaid Histograms", 800, 600);

// 最初のヒストグラム
TH1D *h1 = new TH1D("h1", "Dataset 1", 50, -5, 5);
for (int i = 0; i < 5000; i++) {
    h1->Fill(gRandom->Gaus(0, 1));
}
h1->SetLineColor(2);  // 赤色
h1->Draw();

// 2番目のヒストグラム
TH1D *h2 = new TH1D("h2", "Dataset 2", 50, -5, 5);
for (int i = 0; i < 5000; i++) {
    h2->Fill(gRandom->Gaus(0.5, 1.2));
}
h2->SetLineColor(4);  // 青色
h2->Draw("SAME");  // SAME オプションで重ねる

// 凡例を追加
TLegend *leg = new TLegend(0.7, 0.7, 0.9, 0.9);
leg->AddEntry(h1, "Dataset 1", "l");
leg->AddEntry(h2, "Dataset 2", "l");
leg->Draw();
```

複数のヒストグラムを同時に表示して比較できます。

### グラフを描画したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Graph", 800, 600);

TGraph *g = new TGraph();

// グラフのポイントを追加
for (int i = 0; i < 50; i++) {
    double x = i * 0.1;
    double y = sin(x);
    g->SetPoint(i, x, y);
}

// グラフを描画
g->Draw("AL");
```

グラフを直線で描画します。`"AL"`オプションで軸とポイントを結ぶ線を表示します。

### マーカー付きでグラフを描画したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Graph with Markers", 800, 600);

TGraph *g = new TGraph();

// グラフのポイントを追加
for (int i = 0; i < 20; i++) {
    double x = i;
    double y = i * i;
    g->SetPoint(i, x, y);
}

// マーカーと線で描画
g->Draw("ALP");  // A: 軸, L: 線, P: マーカー
```

各ポイントにマーカーを表示します。

### 2次元ヒストグラムを描画したい

```cpp
#include <TCanvas.h>
#include <TH2D.h>

TCanvas *c = new TCanvas("c", "2D Histogram", 800, 600);

TH2D *h2 = new TH2D("h2", "2D Distribution", 50, -5, 5, 50, -5, 5);

// 2次元データを追加
for (int i = 0; i < 10000; i++) {
    h2->Fill(gRandom->Gaus(), gRandom->Gaus());
}

// カラーマップで描画
h2->Draw("colz");
```

2次元ヒストグラムをカラーマップで表示します。

### ステップヒストグラムで描画したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Step Histogram", 800, 600);

TH1D *h = new TH1D("h", "Data", 50, 0, 10);

// データを追加
for (int i = 0; i < 1000; i++) {
    h->Fill(gRandom->Uniform(0, 10));
}

// ステップヒストグラムで描画
h->Draw("HIST");
```

ヒストグラムをステップ形式で描画します。

## 描画オプションの組み合わせ

複数のオプションを組み合わせることで、より複雑な描画ができます：

| オプション | 説明 |
|-----------|------|
| `"SAME"` | 前の描画に追加（同じパッドに重ねる） |
| `"SAMES"` | 統計ボックスを再描画（SAME使用時） |
| `"+"` | 軸の統計ボックスをリセット |
| `"S"` | 統計ボックスを表示 |

## 描画後のカスタマイズ

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Customized", 800, 600);

TH1D *h = new TH1D("h", "Data", 100, -5, 5);
h->FillRandom("gaus", 5000);

h->Draw();

// 描画後にプロパティを変更
h->SetLineColor(2);      // 線色を赤に
h->SetLineWidth(2);      // 線幅を変更
h->SetFillColor(5);      // 塗りつぶし色を変更
h->SetFillStyle(3004);   // 塗りつぶしパターンを変更

c->Modified();  // 変更を反映
c->Update();    // 再描画
```

描画後にオブジェクトのプロパティを変更して、再度Updateする必要があります。

## Draw vs SaveAs vs Print

| メソッド | 目的 | 用途 |
|---------|------|------|
| `Draw()` | キャンバスに描画 | リアルタイム表示 |
| `SaveAs()` | ファイルに保存（単一形式） | 画像ファイルとして保存 |
| `Print()` | ファイルに出力（複数形式対応） | PDF/PSマルチページ対応 |

## 関連メソッド

- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)
- [キャンバスを保存したい（`TCanvas::SaveAs`）](./root-tcanvas-saveas.md)
- [複数のキャンバスをPDFに保存したい（`TCanvas::Print`）](./root-tcanvas-print.md)
- [キャンバスを更新したい（`TCanvas::Update`）](./root-tcanvas-update.md)
- [キャンバスを分割したい（`TCanvas::Divide`）](./root-tcanvas-divide.md)

## 参考資料

- [ROOT TH1::Draw Documentation](https://root.cern/doc/master/classROOT_1_1Math_1_1LorentzVector.html)
- [ROOT Histogram Drawing Options](https://root.cern/doc/master/group__HistDrawFunc.html)
- [ROOT Graphics Documentation](https://root.cern/doc/master/group__Graphics.html)
