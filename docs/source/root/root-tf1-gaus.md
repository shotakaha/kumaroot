# ガウス分布でフィットしたい（`TF1::Fit` with `"gaus"`）

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <TCanvas.h>

// テスト用にガウス分布のヒストグラムを作成
TH1D *h = new TH1D("h", "Gaussian Distribution", 100, 0, 100);

TRandom3 random;
for (int i = 0; i < 10000; i++) {
    h->Fill(random.Gaus(50, 10));
}

// ガウス関数を定義してフィッティング
TF1 *gaussian = new TF1("gaussian", "gaus", 20, 80);
h->Fit(gaussian);

TCanvas *c = new TCanvas("c", "canvas", 800, 600);
h->Draw();
gaussian->Draw("same");
```

ガウス関数`"gaus"`を使用してヒストグラムをフィットします。
`"gaus"`はROOTが提供する組み込み関数で、3つのパラメーター（正規化、平均値、標準偏差）を持ちます。

```python
from ROOT import TH1D, TF1, TRandom3, TCanvas

# テスト用にガウス分布のヒストグラムを作成
h = TH1D("h", "Gaussian Distribution", 100, 0, 100)

random = TRandom3()
for i in range(10000):
    h.Fill(random.Gaus(50, 10))

# ガウス関数を定義してフィッティング
gaussian = TF1("gaussian", "gaus", 20, 80)
h.Fit(gaussian)

c = TCanvas("c", "canvas", 800, 600)
h.Draw()
gaussian.Draw("same")
```

## ガウス関数について

### パラメーター

ガウス関数`"gaus"`は以下の3つのパラメーターで定義されます：

| パラメーター | インデックス | 説明 | デフォルト値 |
|----------|------|------|---------|
| 正規化（Normalization） | [0] | ガウス曲線の高さ | ヒストグラムから自動設定 |
| 平均値（Mean） | [1] | 分布の中心 | ヒストグラムから自動設定 |
| 標準偏差（Sigma） | [2] | 分布の幅 | ヒストグラムから自動設定 |

ガウス関数の数式: $f(x) = p0 \cdot e^{-0.5 \cdot ((x-p1)/p2)^2}$

## ガウス関数でヒストグラムをフィットしたい（`Fit`）

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

// ガウス関数でフィット
TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);

// フィット結果を取得
Double_t mean = f->GetParameter(1);
Double_t sigma = f->GetParameter(2);

std::cout << "Mean: " << mean << std::endl;
std::cout << "Sigma: " << sigma << std::endl;
```

`Fit()`メソッドでヒストグラムをガウス関数でフィットし、パラメーターを自動的に決定します。

## パラメーターを手動で初期化してフィットしたい

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -10, 10);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(2, 1.5));
}

// ガウス関数を作成
TF1 *f = new TF1("f", "gaus", -10, 10);

// パラメーターを手動で初期化
f->SetParameter(0, 200);   // 正規化（ヒストグラムの最大値程度）
f->SetParameter(1, 2.0);   // 平均値
f->SetParameter(2, 1.0);   // 標準偏差

// フィット実行
h->Fit(f);

f->Draw();
```

初期パラメーター値がデータに近い場合、フィットが高速かつ正確になる傾向があります。

## パラメーターを固定してフィットしたい

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

// ガウス関数を作成
TF1 *f = new TF1("f", "gaus", -5, 5);

// 平均値を0に固定し、他のパラメーターのみフィット
f->FixParameter(1, 0.0);

h->Fit(f);
```

`FixParameter()`で特定のパラメーターを固定することで、他のパラメーターのみをフィットできます。

## フィット結果を取得したい

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <iostream>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);

// パラメーター値を取得
Double_t norm = f->GetParameter(0);
Double_t mean = f->GetParameter(1);
Double_t sigma = f->GetParameter(2);

// 誤差を取得
Double_t mean_err = f->GetParError(1);
Double_t sigma_err = f->GetParError(2);

std::cout << "Mean: " << mean << " +/- " << mean_err << std::endl;
std::cout << "Sigma: " << sigma << " +/- " << sigma_err << std::endl;

// カイ二乗値を取得
Double_t chi2 = f->GetChisquare();
Int_t ndf = f->GetNDF();
std::cout << "Chi2: " << chi2 << ", NDF: " << ndf << std::endl;
```

フィット後、パラメーター値、誤差、統計情報などを取得できます。

## 複数のガウス関数でフィットしたい

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "bimodal data", 100, -10, 10);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    if (random.Uniform() < 0.5) {
        h->Fill(random.Gaus(-3, 1));
    } else {
        h->Fill(random.Gaus(3, 1));
    }
}

// 2つのガウス関数の和
TF1 *f = new TF1("f",
    "gaus(0) + gaus(3)",
    -10, 10);

// 各ガウス関数のパラメーターを初期化
f->SetParameter(0, 250);   // 第1ガウスの正規化
f->SetParameter(1, -3);    // 第1ガウスの平均値
f->SetParameter(2, 1);     // 第1ガウスの標準偏差

f->SetParameter(3, 250);   // 第2ガウスの正規化
f->SetParameter(4, 3);     // 第2ガウスの平均値
f->SetParameter(5, 1);     // 第2ガウスの標準偏差

h->Fit(f);
f->Draw();
```

複数のガウス関数を組み合わせることで、複雑な分布をフィットできます。

## フィット結果を描画したい

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <TCanvas.h>

TH1D *h = new TH1D("h", "Gaussian Fit", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);

TCanvas *c = new TCanvas("c", "Fit Result", 600, 400);
h->Draw();
f->SetLineColor(2);
f->SetLineWidth(2);
f->Draw("same");

c->BuildLegend();
```

ヒストグラムとフィット曲線を重ねて描画できます。

## 関連メソッド

- [TF1](./root-tf1.md) - 関数を定義
- [TH1::Fit](./root-th1-fit.md) - ヒストグラムをフィット
- [GetParameter](./root-tf1-getparameter.md) - パラメーター値を取得
- [SetParameter](./root-tf1-setparameter.md) - パラメーター値を設定
- [FixParameter](./root-tf1-fixparameter.md) - パラメーターを固定

## 参考リンク

- [ROOT TF1 Documentation](https://root.cern/doc/master/classTF1.html)
- [ROOT TH1::Fit Documentation](https://root.cern/doc/master/classTH1.html#a7e7d8ff3b6b6b6b6b6b)
