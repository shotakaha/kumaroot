# ノーマライズしたい（`TH1::Scale`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t integral = h->Integral();
h->Scale(1.0 / integral);  // 積分値が1になるように正規化
```

`TH1::Scale`メソッドで、ヒストグラムをスケーリング（拡大・縮小）できます。
`TH1::Integral`メソッドと組み合わせることで、ヒストグラムを正規化できます。

```python
from ROOT import TH1D

h = TH1D("h", "Data", 100, 0, 10)
# ...データを入力...

integral = h.Integral()
h.Scale(1.0 / integral)  # 積分値が1になるように正規化
```

## メソッドのシグネチャ

```cpp
void Scale(Double_t c1 = 1.0, Option_t* option = "");
```

### 引数と戻り値

**引数**:

- **c1** - スケーリング係数（デフォルト値は1.0）
- **option** - オプション文字列（通常は空）

**戻り値**:

- なし（`void`）

## ヒストグラム全体をスケーリングしたい（`Scale`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);

// データを入力
h->Fill(2.5);
h->Fill(5.0);
h->Fill(7.5);

// すべてのビンを2倍に拡大
h->Scale(2.0);

// または半分に縮小
h->Scale(0.5);

printf("After scaling, integral: %.1f\n", h->Integral());
```

`Scale(factor)`メソッドで、ヒストグラムのすべてのビン内容に係数を乗算できます。
これにより、ヒストグラムの全体的な大きさを変更できます。

## 積分値が1になるように正規化したい（`Integral` + `Scale`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Distribution", 100, 0, 10);

// データを入力
for (Int_t i = 0; i < 1000; i++) {
    h->Fill(gRandom->Gaus(5, 1));
}

// 積分値を計算
Double_t integral = h->Integral();

// 積分値が1になるように正規化
h->Scale(1.0 / integral);

printf("After normalization, integral: %.6f\n", h->Integral());
```

`Integral()`と`Scale()`を組み合わせることで、ヒストグラムを正規化できます。
正規化されたヒストグラムは、確率分布として解釈できます。

## 複数のヒストグラムを同じスケールで比較したい（`Scale`）

```cpp
#include <TH1D.h>

TH1D *h1 = new TH1D("h1", "Sample 1", 100, 0, 10);
TH1D *h2 = new TH1D("h2", "Sample 2", 100, 0, 10);

// データを入力
for (Int_t i = 0; i < 1000; i++) {
    h1->Fill(gRandom->Gaus(5, 1));
    h2->Fill(gRandom->Gaus(6, 1.5));
}

// 両方のヒストグラムを正規化
Double_t integral1 = h1->Integral();
Double_t integral2 = h2->Integral();

h1->Scale(1.0 / integral1);
h2->Scale(1.0 / integral2);

printf("h1 integral: %.6f, h2 integral: %.6f\n", h1->Integral(), h2->Integral());
```

複数のヒストグラムを比較する場合、各ヒストグラムを個別に正規化することで、
イベント数の違いに左右されない公平な比較ができます。

## 関連メソッド

- [`TH1::Integral`](./root-th1-integral.md) - ヒストグラムの積分値を計算
