# 平均値したい（`TH1::GetMean`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t mean = h->GetMean();
printf("Mean: %f\n", mean);
```

`TH1::GetMean`メソッドで、ヒストグラムの平均値を取得できます。

```python
from ROOT import TH1D

h = TH1D("h", "Data", 100, 0, 10)
# ...データを入力...

mean = h.GetMean()
print(f"Mean: {mean}")
```

## メソッドのシグネチャ

```cpp
Double_t GetMean(Int_t axis = 1);
Double_t GetMeanError(Int_t axis = 1);
```

### 引数と戻り値

**引数**:

- **axis** - 軸番号（デフォルト値は1）
  - 1: X軸の平均値
  - 2: Y軸の平均値（2次元ヒストグラムで使用）
  - 3: Z軸の平均値（3次元ヒストグラムで使用）

**戻り値**:

- 指定された軸の平均値（`Double_t`型）

## X軸の平均値を取得したい（`GetMean`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Energy", 100, 0, 10);

// データを入力
h->Fill(2.5);
h->Fill(5.0);
h->Fill(7.5);

// X軸の平均値を取得
Double_t mean = h->GetMean();    // デフォルトはaxis=1
Double_t mean = h->GetMean(1);   // 明示的に指定

printf("Mean: %.3f\n", mean);
```

`GetMean`メソッドで、ヒストグラムに入力されたデータの平均値を計算できます。

## 平均値の誤差を一緒に取得したい（`GetMeanError`）

```cpp
#include <TH1D.h>
#include <cstdio>

TH1D *h = new TH1D("h", "Measurements", 100, 0, 100);

// データを入力
for (Int_t i = 0; i < 1000; i++) {
    h->Fill(gRandom->Gaus(50, 10));
}

Double_t mean = h->GetMean();
Double_t mean_error = h->GetMeanError();

printf("Mean: %.3f ± %.3f\n", mean, mean_error);
```

`GetMeanError`メソッドで、平均値の統計的な誤差を取得できます。
これはヒストグラムのエントリー数から計算される、平均値の信頼区間を表します。

## 2次元ヒストグラムのY軸平均値を取得したい（`GetMean`）

```cpp
#include <TH2D.h>

TH2D *h2 = new TH2D("h2", "2D Data", 50, 0, 10, 50, 0, 10);

// データを入力
h2->Fill(2.0, 3.0);
h2->Fill(5.0, 7.0);
h2->Fill(8.0, 6.0);

// X軸とY軸の平均値を取得
Double_t mean_x = h2->GetMean(1);
Double_t mean_y = h2->GetMean(2);

printf("Mean X: %.2f, Mean Y: %.2f\n", mean_x, mean_y);
```

2次元ヒストグラムでは、引数で軸を指定することで、各軸の平均値を個別に取得できます。
