# 正規化したい（`TH1::Scale`）

```cpp
Double_t integral = h->Integral();
h->Scale(1.0 / integral);  // 積分値が1になるように正規化
```

`TH1::Scale`メソッドで、ヒストグラムをスケール（拡大・縮小）できます。
`TH1::Integral`メソッドと組み合わせることで、ヒストグラムを正規化できます。

```python
from ROOT import TH1D

h = TH1D("h", "Data", 100, 0, 10)
# ...データを入力...

integral = h.Integral()
h.Scale(1.0 / integral)  # 積分値が1になるように正規化
```

## 複数のヒストグラムを比較したい（`TH1::Scale`）

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

複数のヒストグラムを比較する場合、イベント数が異なる場合でも、それぞれ個別に正規化することで、
公平な比較ができます。
