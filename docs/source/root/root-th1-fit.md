# ヒストグラムをフィットしたい（`TH1::Fit`）

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);
```

`TH1::Fit`メソッドで、ヒストグラムを数学関数でフィットできます。
フィット関数は`TF1`で作成し、ヒストグラムのデータに対して最小二乗法による最適化を行います。

```python
from ROOT import TH1D, TF1, TRandom3

h = TH1D("h", "data", 100, -5, 5)

random = TRandom3()
for i in range(5000):
    h.Fill(random.Gaus(0, 1))

f = TF1("f", "gaus", -5, 5)
h.Fit(f)
```

## メソッドシグネチャ

```cpp
TFitResultPtr Fit(TF1 *f1,
                  Option_t *option = "",
                  Option_t *goption = "",
                  Axis_t xmin = 0,
                  Axis_t xmax = 0)
```

### 引数と戻り値

**引数**:

- **f1** - フィット関数（`TF1`オブジェクト）
- **option** - フィットオプション（文字列）
  - `"Q"` - 静粛モード（出力なし）
  - `"S"` - 統計情報を出力
  - `"V"` - 冗長モード（詳細情報を出力）
  - `"+"` - 前のフィット結果に追加
  - `"N"` - パラメーターの制約を無視
  - `"R"` - 指定範囲でのみフィット
- **goption** - グラフィック描画オプション（`Draw`に渡される）
- **xmin, xmax** - フィット範囲（指定しない場合はヒストグラム全体）

**戻り値**:

- **TFitResultPtr** - フィット結果オブジェクト（パラメーター値、誤差、カイ二乗値などを含む）

## 基本的なフィット

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <iostream>

TH1D *h = new TH1D("h", "Histogram", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

// ガウス関数でフィット
TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);

// フィット結果を表示
std::cout << "フィット完了" << std::endl;
```

基本的な用法で、ヒストグラムをガウス関数でフィットできます。
`Fit()`メソッドはパラメーターを自動的に初期化してフィットを実行します。

## ガウス関数でフィットしたい

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

// ガウス関数でフィット
TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);

// フィット結果を取得
Double_t mean = f->GetParameter(1);
Double_t sigma = f->GetParameter(2);

std::cout << "Mean: " << mean << std::endl;
std::cout << "Sigma: " << sigma << std::endl;
```

`"gaus"`は組み込み関数で、3つのパラメーター（正規化、平均値、標準偏差）を持ちます。
フィット後、`GetParameter()`でパラメーター値を取得できます。

### Python での実装

```python
from ROOT import TH1D, TF1, TRandom3

h = TH1D("h", "data", 100, -5, 5)

random = TRandom3()
for i in range(5000):
    h.Fill(random.Gaus(0, 1))

f = TF1("f", "gaus", -5, 5)
h.Fit(f)

mean = f.GetParameter(1)
sigma = f.GetParameter(2)

print(f"Mean: {mean}")
print(f"Sigma: {sigma}")
```

## カスタム関数でフィットしたい

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <iostream>
#include <cmath>

// カスタム関数
Double_t myFunc(Double_t *x, Double_t *par) {
    return par[0] * exp(-0.5 * pow((x[0] - par[1]) / par[2], 2));
}

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

// カスタム関数でフィット
TF1 *f = new TF1("f", myFunc, -5, 5, 3);
h->Fit(f);
```

関数ポインターまたはラムダ式でカスタム関数を定義し、フィットに使用できます。

## パラメーター初期化によるフィット最適化

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
```

初期パラメーター値がデータに近い場合、フィットが高速かつ正確になる傾向があります。
ヒストグラムのピーク位置や幅から推定して初期値を設定することが重要です。

## パラメーター制約によるフィット

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

// フィット実行
h->Fit(f);
```

`FixParameter()`で特定のパラメーターを固定することで、他のパラメーターのみをフィットできます。
物理知識から特定のパラメーター値がわかっている場合に有効です。

## フィット結果の解析

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
TFitResultPtr res = h->Fit(f);

// フィット結果から値を取得
if (res) {
    // パラメーター値と誤差
    Double_t norm = f->GetParameter(0);
    Double_t mean = f->GetParameter(1);
    Double_t sigma = f->GetParameter(2);

    Double_t mean_err = f->GetParError(1);
    Double_t sigma_err = f->GetParError(2);

    // 統計情報
    Double_t chi2 = f->GetChisquare();
    Int_t ndf = f->GetNDF();
    Double_t prob = f->GetProb();

    std::cout << "Mean: " << mean << " +/- " << mean_err << std::endl;
    std::cout << "Sigma: " << sigma << " +/- " << sigma_err << std::endl;
    std::cout << "Chi2/NDF: " << chi2 / ndf << std::endl;
    std::cout << "Probability: " << prob << std::endl;
}
```

フィット後、パラメーター値、誤差、カイ二乗値などの統計情報を取得できます。
これらの値は結果の品質を判定するために重要です。

## 指定範囲でのフィット

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TF1 *f = new TF1("f", "gaus", -5, 5);

// 特定の範囲でのみフィット
h->Fit(f, "", "", -2, 2);
```

`Fit()`の最後の2つの引数で、フィット範囲を指定できます。
ヒストグラムの一部のみをフィットしたい場合に有効です。

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

// パラメーターを初期化
f->SetParameter(0, 250);   // 第1ガウスの正規化
f->SetParameter(1, -3);    // 第1ガウスの平均値
f->SetParameter(2, 1);     // 第1ガウスの標準偏差

f->SetParameter(3, 250);   // 第2ガウスの正規化
f->SetParameter(4, 3);     // 第2ガウスの平均値
f->SetParameter(5, 1);     // 第2ガウスの標準偏差

h->Fit(f);
```

複数のガウス関数を組み合わせることで、複雑な分布（双峰分布など）をフィットできます。
各ガウス関数は3つのパラメーターを持つため、パラメーターのインデックスに注意が必要です。

## フィット結果の可視化

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

ヒストグラムとフィット曲線を重ねて描画することで、フィットの品質を視覚的に確認できます。

## フィットオプションの活用

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>

TH1D *h = new TH1D("h", "data", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TF1 *f = new TF1("f", "gaus", -5, 5);

// 詳細情報を出力
h->Fit(f, "V");

// 静粛モード
// h->Fit(f, "Q");

// 指定範囲でフィット
// h->Fit(f, "R", "", -2, 2);
```

`Fit()`メソッドのオプション引数を活用することで、フィットの動作や出力をカスタマイズできます。

## 関連メソッド

- [TF1](./root-tf1.md) - 関数を定義
- [TF1::SetParameter](./root-tf1-setparameter.md) - パラメーター値を設定
- [TF1::GetParameter](./root-tf1-getparameter.md) - パラメーター値を取得
- [TF1::FixParameter](./root-tf1-fixparameter.md) - パラメーターを固定
- [TF1::SetLineColor](./root-tf1-setlinecolor.md) - 線の色を設定
- [TH1::Draw](./root-th1-draw.md) - ヒストグラムを描画
- [ガウス関数でフィットしたい](./root-tf1-gaus.md) - ガウス関数の詳細

## 参考リンク

- [ROOT TH1::Fit Documentation](https://root.cern/doc/master/classTH1.html#a7e7d8c9b6b6b6b6b6b)
- [ROOT TF1 Documentation](https://root.cern/doc/master/classTF1.html)
- [ROOT TFitResult Documentation](https://root.cern/doc/master/classTFitResult.html)
