# 軸を対数スケール表示したい（`TCanvas::SetLogy`、`SetLogx`）

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Log Scale Canvas", 800, 600);

TH1D *h = new TH1D("h", "Distribution", 100, 0.1, 1000);
h->FillRandom("expo", 1000);

// Y軸を対数スケールに設定
c->SetLogy();

h->Draw();
```

`TCanvas::SetLogy`メソッドでY軸を対数スケール表示に変更できます。
大きく異なる値の範囲を視覚的に比較する場合に便利です。

```python
from ROOT import TCanvas, TH1D

c = TCanvas("c", "Log Scale Canvas", 800, 600)

h = TH1D("h", "Distribution", 100, 0.1, 1000)
h.FillRandom("expo", 1000)

# Y軸を対数スケールに設定
c.SetLogy()

h.Draw()
```

## メソッドのシグネチャ

```cpp
void SetLogy(Int_t value = 1)
void SetLogx(Int_t value = 1)
void SetLogz(Int_t value = 1)
```

### 引数と戻り値

**引数**:

- **value** - 対数スケールのON/OFF（1=ON、0=OFF）

**戻り値**:

- なし

```{note}
## TCanvas::SetLogy vs gStyle::SetOptLogy

本ドキュメント（**TCanvas::SetLogy**）と `gStyle::SetOptLogy` は異なる設定メソッドです：

| 機能 | TCanvas::SetLogy | gStyle::SetOptLogy |
|-----|-----------------|-------------------|
| 設定対象 | **特定のキャンバス** | **グローバルスタイル** |
| 影響範囲 | そのキャンバスのみ | 以降に作成されるすべてのオブジェクト |
| 使用例 | `canvas->SetLogy()` | `gStyle->SetOptLogy(1)` |
| 適用タイミング | 即座に適用 | 次のオブジェクト作成時に適用 |

**使い分けの目安**：
- **TCanvas::SetLogy**: 特定のキャンバスだけを対数スケールにしたい場合
- **gStyle::SetOptLogy**: プログラム全体で統一的に対数スケールを使いたい場合

詳細は [gStyle::SetOptLogy](./root-gstyle-setoptlog.md) を参照してください。
```

## 対数スケール設定メソッド

| メソッド | 説明 |
|---------|------|
| `SetLogy()` | Y軸を対数スケール表示 |
| `SetLogx()` | X軸を対数スケール表示 |
| `SetLogz()` | Z軸を対数スケール表示（3D図の場合） |

## 使用例

### Y軸を対数スケール表示したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Y-axis Log Scale", 800, 600);

TH1D *h = new TH1D("h", "Exponential Distribution", 100, 0, 10);

// 指数分布に従うデータを生成
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Exp(1));
}

// Y軸を対数スケールに設定
c->SetLogy();

h->Draw();
```

指数関数的に減少するデータを視覚的に比較しやすくなります。

### X軸を対数スケール表示したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "X-axis Log Scale", 800, 600);

TGraph *g = new TGraph();

// X軸が指数的に増加するデータを生成
for (int i = 0; i < 50; i++) {
    double x = pow(10, i * 0.1);  // 10^0 から 10^5 まで
    double y = sin(log10(x));
    g->SetPoint(i, x, y);
}

// X軸を対数スケールに設定
c->SetLogx();

g->Draw("AL");
```

X軸の値が非常に広い範囲をカバーする場合に有効です。

### 両軸を対数スケール表示したい

```cpp
#include <TCanvas.h>
#include <TH2D.h>

TCanvas *c = new TCanvas("c", "Both Axes Log Scale", 800, 600);

TH2D *h2 = new TH2D("h2", "Power-law Distribution", 50, 0.1, 1000, 50, 0.1, 1000);

// べき乗則に従うデータを生成
for (int i = 0; i < 10000; i++) {
    double x = pow(10, gRandom->Uniform(0, 3));
    double y = pow(10, gRandom->Uniform(0, 3));
    h2->Fill(x, y);
}

// 両軸を対数スケールに設定
c->SetLogx();
c->SetLogy();

h2->Draw("colz");
```

べき乗則やスケーリング則を分析する場合に活用できます。

### キャンバスを分割して一部だけ対数スケールにしたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Mixed Log Scales", 1200, 500);

// キャンバスを2つに分割
c->Divide(2, 1);

// パッド1：通常のスケール
c->cd(1);
TH1D *h1 = new TH1D("h1", "Linear Scale", 100, 0, 10);
h1->FillRandom("gaus", 5000);
h1->Draw();

// パッド2：対数スケール
c->cd(2);
TH1D *h2 = new TH1D("h2", "Log Scale", 100, 0.1, 1000);
h2->FillRandom("expo", 5000);
gPad->SetLogy();  // 現在のパッドのY軸を対数スケール
h2->Draw();
```

複数のパッドで異なるスケール設定ができます。

### 特定のパッドで対数スケールを設定したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Specific Pad Log Scale", 1200, 600);

// キャンバスを3つに分割
c->Divide(3, 1);

// パッド1：通常のスケール
c->cd(1);
TH1D *h1 = new TH1D("h1", "Pad 1", 50, -5, 5);
h1->FillRandom("gaus", 1000);
h1->Draw();

// パッド2：Y軸対数スケール
c->cd(2);
TH1D *h2 = new TH1D("h2", "Pad 2", 50, 0, 10);
h2->FillRandom("expo", 1000);
gPad->SetLogy();
h2->Draw();

// パッド3：XY両軸対数スケール
c->cd(3);
TH1D *h3 = new TH1D("h3", "Pad 3", 50, 0.1, 100);
h3->FillRandom("pareto", 1000);
gPad->SetLogx();
gPad->SetLogy();
h3->Draw();
```

キャンバス内の複数のパッドで異なるスケール設定を適用できます。

### 対数スケールのON/OFFを切り替えたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Toggle Log Scale", 800, 600);

TH1D *h = new TH1D("h", "Data", 100, 0.1, 1000);
h->FillRandom("expo", 5000);

// 最初は通常スケール
h->Draw();

// ... 後で対数スケールに変更
c->SetLogy(1);
c->Update();

// ... さらに後で通常スケールに戻す
c->SetLogy(0);
c->Update();
```

SetLogy(1)で対数スケール有効、SetLogy(0)で無効にできます。

### gPad を使って現在のパッドに設定したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Using gPad", 1200, 600);

c->Divide(2, 1);

// パッド1
c->cd(1);
TH1D *h1 = new TH1D("h1", "Histogram 1", 50, -5, 5);
h1->FillRandom("gaus", 1000);
h1->Draw();
gPad->SetLogy();  // 現在のパッド（パッド1）に対数スケールを設定

// パッド2
c->cd(2);
TH1D *h2 = new TH1D("h2", "Histogram 2", 50, 0, 10);
h2->FillRandom("expo", 1000);
h2->Draw();
gPad->SetLogy();  // 現在のパッド（パッド2）に対数スケールを設定
```

`gPad`は「current pad」（現在のパッド）へのポインターです。

## 対数スケールが有効な用途

| 用途 | 説明 |
|------|------|
| 指数関数的分布 | 指数減少データを可視化 |
| べき乗則データ | スケーリング則の分析 |
| 広い値域の比較 | 10倍以上離れた値を比較 |
| 小さい値の詳細表示 | 小さい値の変化を顕著に表示 |
| 周波数スペクトラム | 音響や振動解析 |

## 注意事項

### 負の値を含む場合

```cpp
// ❌ エラー：負の値は対数スケールで表示できない
TH1D *h = new TH1D("h", "Data with Negative", 50, -10, 10);
h->FillRandom("gaus", 1000);
c->SetLogy();  // 負の値があるとエラー
h->Draw();

// ✅ 解決策：負の値を除外またはシフト
TH1D *h = new TH1D("h", "Data without Negative", 50, 0.1, 10);
h->FillRandom("expo", 1000);
c->SetLogy();
h->Draw();
```

対数スケールでは負の値や0は表示できません。

### 0を含む場合

```cpp
// ❌ 注意：0を含むとスケールが正しく設定されない
TH1D *h = new TH1D("h", "Data with Zero", 50, 0, 10);
// ...

// ✅ 小さい正の値を最小値に設定
TH1D *h = new TH1D("h", "Data Starting from Small Value", 50, 0.1, 10);
```

最小値を小さい正の数に設定します。

## 関連メソッド

- [グラフを描画したい（`TCanvas::Draw`）](./root-tcanvas-draw.md)
- [キャンバスを分割したい（`TCanvas::Divide`）](./root-tcanvas-divide.md)
- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)

## 参考資料

- [ROOT TCanvas::SetLogy Documentation](https://root.cern/doc/master/classTCanvas.html)
- [ROOT Graphics Documentation](https://root.cern/doc/master/group__Graphics.html)
- [ROOT Axis Documentation](https://root.cern/doc/master/classROOT_1_1Math_1_1LorentzVector.html)
