# 積分値を計算したい（`TH1::Integral`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t integral = h->Integral();
printf("Integral: %f\n", integral);
```

`TH1::Integral`メソッドで、ヒストグラムのビン内容の合計（積分値）を計算できます。

```python
from ROOT import TH1D

h = TH1D("h", "Data", 100, 0, 10)
# ...データを入力...

integral = h.Integral()
print(f"Integral: {integral}")
```

## メソッドのシグネチャ

```cpp
Double_t Integral(
    Int_t bin1 = 1,
    Int_t bin2 = −1,
    Option_t* option = ""
);
```

### 引数と戻り値

**引数**:

- **bin1** - 開始ビン番号（デフォルト値は1）
- **bin2** - 終了ビン番号（デフォルト値は−1、最後のビンまで）
- **option** - オプション文字列（通常は空）

**戻り値**:

- 指定されたビン範囲の内容の合計（`Double_t`型）

## 全体の積分値を計算したい（`Integral`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Distribution", 100, 0, 10);

// データを入力
h->Fill(2.5);
h->Fill(5.0);
h->Fill(7.5);

// 全体の積分値を計算
Double_t integral = h->Integral();

printf("Total integral: %.1f\n", integral);
```

`Integral()`メソッドで、ヒストグラムのすべてのビン内容の合計を計算できます。
これはヒストグラムに入力されたイベント数の合計と同じです。

## ビン範囲を指定して積分値を計算したい（`Integral`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Energy", 100, 0, 10);

// データを入力
for (Int_t i = 0; i < 1000; i++) {
    h->Fill(gRandom->Uniform(0, 10));
}

// 全体の積分値
Double_t total_integral = h->Integral();

// ビン20からビン50までの積分値
Double_t partial_integral = h->Integral(20, 50);

printf("Total: %.1f, Partial (bin 20-50): %.1f\n", total_integral, partial_integral);
```

`Integral(bin1, bin2)`メソッドで、指定されたビン範囲の積分値を計算できます。
これはヒストグラムの特定の領域だけのイベント数を数える場合に便利です。
