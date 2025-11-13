# 対数スケールにしたい（`gStyle->SetOptLog*`）

```cpp
#include <TStyle.h>

// X軸を対数スケールに設定
gStyle->SetOptLogx(1);

// Y軸を対数スケールに設定
gStyle->SetOptLogy(1);

// Z軸を対数スケールに設定（3次元グラフ用）
gStyle->SetOptLogz(1);
```

`gStyle->SetOptLogx`、`gStyle->SetOptLogy`、`gStyle->SetOptLogz`メソッドで、
グラフやヒストグラムの軸を対数スケール（対数目盛）に変更できます。

```python
from ROOT import gStyle

# X軸を対数スケールに設定
gStyle.SetOptLogx(1)

# Y軸を対数スケールに設定
gStyle.SetOptLogy(1)

# Z軸を対数スケールに設定
gStyle.SetOptLogz(1)
```

## 対数スケールを理解したい

対数スケールは、広い範囲のデータを見やすく表示するときに有効です。

### 線形スケール vs 対数スケール

**線形スケール**:

- 軸の目盛り間隔が均等
- 1から10までと100から1000までが同じ距離
- データが指数関数的に増減する場合、小さい値の詳細が見えにくい

**対数スケール**：

- 軸の目盛り間隔が指数関数的
- 1から10までと10から100までが同じ距離
- 広い範囲のデータを均衡よく表示できる

**設定値**:

- `0`：線形スケール（デフォルト）
- `1`：対数スケール

## 異なる軸設定を使いたい

### X軸のみ対数スケール

```cpp
#include <TStyle.h>

gStyle->SetOptLogx(1);
gStyle->SetOptLogy(0);
```

X軸が指数関数的に変化するデータに有効です。
例：周波数応答、べき乗則分布

### Y軸のみ対数スケール

```cpp
#include <TStyle.h>

gStyle->SetOptLogx(0);
gStyle->SetOptLogy(1);
```

Y軸が指数関数的に変化するデータに有効です。
例：指数減衰、確率分布

### X軸とY軸の両方を対数スケール

```cpp
#include <TStyle.h>

gStyle->SetOptLogx(1);
gStyle->SetOptLogy(1);
```

X軸とY軸の両方が広い範囲で変化するデータに有効です。
例：べき乗則（パワーロー）に従うデータ

### 3次元プロット用（Z軸も対数スケール）

```cpp
#include <TStyle.h>

gStyle->SetOptLogx(1);
gStyle->SetOptLogy(1);
gStyle->SetOptLogz(1);
```

3次元ヒストグラムやプロットで、全軸を対数スケールに設定します。

### 線形スケールに戻す

```cpp
#include <TStyle.h>

gStyle->SetOptLogx(0);
gStyle->SetOptLogy(0);
gStyle->SetOptLogz(0);
```

すべての軸を線形スケールに戻します。

## 実用例

### 指数減衰データの可視化

```cpp
#include <TStyle.h>

// Y軸を対数スケールにして、指数減衰を直線で表示
gStyle->SetOptLogx(0);
gStyle->SetOptLogy(1);
```

指数関数 $y = Ae^{-\lambda x}$ は、Y軸を対数スケールにすると直線として表示されます。
これにより、減衰率$\lambda$を視覚的に読み取りやすくなります。

### べき乗則データの解析

```cpp
#include <TStyle.h>

// X軸とY軸の両方を対数スケールに設定
gStyle->SetOptLogx(1);
gStyle->SetOptLogy(1);
```

べき乗則 $y = Ax^{\alpha}$ は、両軸を対数スケールにすると直線として表示されます。
天体物理学や天文学でよく見られるデータ分布の解析に有効です。

### 周波数応答特性の測定

```cpp
#include <TStyle.h>

// X軸を対数スケール、Y軸を線形スケール
gStyle->SetOptLogx(1);
gStyle->SetOptLogy(0);
```

電子工学や音響学の周波数応答（bodeプロット）では、
X軸を対数スケールにして周波数の詳細な変化を表示します。

### 粒子検出器のエネルギースペクトル

```cpp
#include <TStyle.h>

// Y軸を対数スケール
gStyle->SetOptLogy(1);
```

高エネルギー物理学の実験では、
エネルギースペクトルのカウント数が指数的に減少するため、
Y軸を対数スケールにして全範囲を表示します。

## 注意事項

- **ゼロや負の値**: 対数スケールではゼロや負の値は表示できません。データに負の値が含まれる場合は線形スケールを使用してください

- **グリッドライン**: 対数スケールでは、主目盛りと副目盛りの間隔が異なります

- **データの確認**: 対数スケールの使用前に、データの範囲と分布を確認してください

## 個別のオブジェクトで設定したい

`gStyle`で設定した対数スケール設定は、その後に作成されるオブジェクトに適用されます。
すでに作成されたオブジェクトに対して適用する場合は、オブジェクトのメソッドを直接使用してください。

```cpp
#include <TStyle.h>
#include <TH1F.h>

TH1F *hist = new TH1F("hist", "Histogram", 100, 0, 10);
// ...データを充填...

// このヒストグラムのY軸だけを対数スケールに設定
hist->GetYaxis()->SetLogscale(1);

// X軸を対数スケールに設定
hist->GetXaxis()->SetLogscale(1);
```

## リファレンス

- [ROOT TStyle::SetOptLogx Documentation](https://root.cern/doc/master/classTStyle.html#af6c5a12b7f1d43895dd1ca9a7f49de4c)
- [ROOT TStyle::SetOptLogy Documentation](https://root.cern/doc/master/classTStyle.html#a847b2b69c05b4be3e3b7c8d05c9f0e89)
- [ROOT TStyle::SetOptLogz Documentation](https://root.cern/doc/master/classTStyle.html#a3bef5f9e5e5c6d7e8f9a0b1c2d3e4f50)
- [ROOT Axis Documentation](https://root.cern/doc/master/classTAxis.html)
