# 積分値したい（`TH1::Integral`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

// 全体の積分値を計算
Double_t integral = h->Integral();
std::cout << "Integral: " << integral << std::endl;
```

`TH1::Integral`メソッドで、ヒストグラムのビン内容の合計（積分値）を計算できます。

```python
from ROOT import TH1D

h = TH1D("h", "Data", 100, 0, 10)
# ...データを入力...

integral = h.Integral()
print(f"Integral: {integral}")
```

## 範囲を指定したい（`TH1::Integral`）

```cpp
// ビン20からビン50までの積分値
Double_t partial_integral = h->Integral(20, 50);
```

`Integral(bin1, bin2)`メソッドで、指定されたビン範囲の積分値を計算できます。
これはヒストグラムの特定の領域だけのイベント数を数える場合に便利です。
