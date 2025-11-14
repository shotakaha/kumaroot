# 色見本を表示したい（`TCanvas::DrawColorTable`）

```cpp
#include <TCanvas.h>

// キャンバスを作成
TCanvas *c = new TCanvas("c", "Color Table", 800, 600);

// カラーテーブルを描画
c->DrawColorTable();
```

`TCanvas::DrawColorTable`メソッドでROOTで利用可能なすべての色を視覚的に確認できます。
各色の色番号と色名を表示した見本表をキャンバスに描画します。

```python
from ROOT import TCanvas

c = TCanvas("c", "Color Table", 800, 600)

# カラーテーブルを描画
c.DrawColorTable()
```

## メソッドのシグネチャ

```cpp
void DrawColorTable()
```

### 引数と戻り値

**引数**:

- なし

**戻り値**:

- なし

## 使用例

### カラーテーブルを表示したい

```cpp
#include <TCanvas.h>

TCanvas *c = new TCanvas("c", "ROOT Color Table", 800, 600);

// カラーテーブルを描画
c->DrawColorTable();
```

ROOTで使用可能なすべての色を一覧で表示します。
各色には色番号が振られており、プログラムで色を指定する際に使用できます。

### カラーテーブルを保存したい

```cpp
#include <TCanvas.h>

TCanvas *c = new TCanvas("c", "Color Table", 800, 600);

c->DrawColorTable();

// PNG形式で保存
c->SaveAs("color_table.png");

// PDF形式で保存
c->SaveAs("color_table.pdf");
```

カラーテーブルを画像ファイルとして保存できます。

### 対話モードで表示したい

```cpp
root> TCanvas c
root> c.DrawColorTable()
```

ROOT対話モードで実行する場合は、上記のように入力します。

## ROOTの色について

### 色の種類

ROOTは以下の色を提供しています：

| 色番号 | 色名 | 説明 |
|--------|------|------|
| 0 | White | 白 |
| 1 | Black | 黒 |
| 2 | Red | 赤 |
| 3 | Green | 緑 |
| 4 | Blue | 青 |
| 5 | Yellow | 黄 |
| 6 | Magenta | マゼンタ |
| 7 | Cyan | シアン |
| 8 | Orange | オレンジ |
| 9 | Spring | スプリング |
| 10 | Teal | ティール |
| 11+ | その他 | 拡張色 |

### プログラムで色を指定する

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Using Colors", 800, 600);

TH1D *h = new TH1D("h", "Histogram", 100, -5, 5);
h->FillRandom("gaus", 1000);

// 色番号で指定（例：赤=2）
h->SetLineColor(2);      // 線色を赤に
h->SetFillColor(3);      // 塗りつぶし色を緑に
h->SetMarkerColor(4);    // マーカー色を青に

h->Draw();
```

色番号を使って、ヒストグラムやグラフの色を指定できます。

### 色の効果的な組み合わせ

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Color Combinations", 1200, 400);

c->Divide(3, 1);

// パッド1：温色系
c->cd(1);
TH1D *h1 = new TH1D("h1", "Warm Colors", 50, -5, 5);
h1->FillRandom("gaus", 1000);
h1->SetLineColor(2);     // 赤
h1->SetFillColor(5);     // 黄
h1->Draw();

// パッド2：冷色系
c->cd(2);
TH1D *h2 = new TH1D("h2", "Cool Colors", 50, -5, 5);
h2->FillRandom("gaus", 1000);
h2->SetLineColor(4);     // 青
h2->SetFillColor(7);     // シアン
h2->Draw();

// パッド3：対比効果
c->cd(3);
TH1D *h3 = new TH1D("h3", "Contrast", 50, -5, 5);
h3->FillRandom("gaus", 1000);
h3->SetLineColor(1);     // 黒
h3->SetFillColor(5);     // 黄
h3->Draw();
```

色の組み合わせで視覚的な効果を高めることができます。

## カラーテーブルの活用

### 複数のデータを異なる色で表示

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Multi-colored Histograms", 800, 600);

// 複数のヒストグラムを異なる色で表示
TH1D *h1 = new TH1D("h1", "Data 1", 50, -5, 5);
h1->FillRandom("gaus", 5000);
h1->SetLineColor(2);     // 赤
h1->Draw();

TH1D *h2 = new TH1D("h2", "Data 2", 50, -5, 5);
h2->FillRandom("gaus", 5000);
h2->SetLineColor(4);     // 青
h2->Draw("SAME");

TH1D *h3 = new TH1D("h3", "Data 3", 50, -5, 5);
h3->FillRandom("gaus", 5000);
h3->SetLineColor(3);     // 緑
h3->Draw("SAME");

// 凡例を追加
TLegend *leg = new TLegend(0.7, 0.7, 0.9, 0.9);
leg->AddEntry(h1, "Data 1 (Red)", "l");
leg->AddEntry(h2, "Data 2 (Blue)", "l");
leg->AddEntry(h3, "Data 3 (Green)", "l");
leg->Draw();
```

複数のデータセットを異なる色で視覚的に区別できます。

### グリッドに色を適用

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Colored Grid", 800, 600);

TGraph *g = new TGraph();

for (int i = 0; i < 50; i++) {
    double x = i * 0.2;
    double y = sin(x);
    g->SetPoint(i, x, y);
}

// グラフを青で描画
g->SetLineColor(4);
g->SetMarkerColor(4);
g->SetMarkerStyle(20);
g->Draw("APL");

// グリッドラインを灰色で表示
c->SetGridx();
c->SetGridy();
```

グリッドに色を付けてグラフを見やすくできます。

## 色の選択ガイドライン

### データ表示における色の使い分け

| 用途 | 推奨色 | 理由 |
|------|--------|------|
| メインデータ | 2（赤）または4（青） | 視認性が高い |
| 比較データ1 | 3（緑） | 赤との区別がしやすい |
| 比較データ2 | 6（マゼンタ） | 複数データの区別に有効 |
| 背景 | 0（白）または15（灰色） | コントラストが取りやすい |
| グリッド | 13-18（淡色） | データを見やすくする |

### プレゼンテーション用色選択

```cpp
// 推奨：背景色を明るくしてコントラストを高める
gStyle->SetCanvasColor(0);  // 白背景

// 避けるべき：背景色が濃いと見えにくい
// gStyle->SetCanvasColor(1);  // 黒背景
```

プレゼンテーション資料では背景色とのコントラストが重要です。

## カラーテーブルの関連機能

### カラーパレットの変更

```cpp
#include <TCanvas.h>
#include <TStyle.h>

// ROOTのカラーパレットを変更
gStyle->SetPalette(1);  // カラーパレット1を設定

// キャンバスを作成して描画
TCanvas *c = new TCanvas("c", "Alternative Palette", 800, 600);
c->DrawColorTable();
```

異なるカラーパレットを選択することで、さまざまな色配列が利用できます。

### カスタムカラーの定義

```cpp
#include <TCanvas.h>
#include <TROOT.h>

TCanvas *c = new TCanvas("c", "Custom Colors", 800, 600);

// カスタムカラーを定義（RGB値で指定）
Int_t customColor = TColor::GetColor(255, 128, 0);  // オレンジ

// ヒストグラムにカスタムカラーを適用
TH1D *h = new TH1D("h", "Custom Color", 100, -5, 5);
h->FillRandom("gaus", 1000);
h->SetLineColor(customColor);
h->Draw();
```

RGB値を使ってカスタムカラーを定義し、より細かい色調整が可能です。

## 関連メソッド

- [グラフを描画したい（`TCanvas::Draw`）](./root-tcanvas-draw.md)
- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)
- [キャンバスを保存したい（`TCanvas::SaveAs`）](./root-tcanvas-saveas.md)

## 参考資料

- [ROOT TCanvas::DrawColorTable Documentation](https://root.cern/doc/master/classTCanvas.html)
- [ROOT Color Palette Documentation](https://root.cern/doc/master/classTColor.html)
- [ROOT Graphics Documentation](https://root.cern/doc/master/group__Graphics.html)
