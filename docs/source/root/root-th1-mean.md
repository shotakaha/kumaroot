# 平均値したい（`TH1::GetMean`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t mean = h->GetMean();
printf("Mean: %f\n", mean);

// X軸の平均（デフォルト）
Double_t mean_x = h->GetMean(1);

// Y軸の平均（重み付けが必要な場合）
Double_t mean_y = h->GetMean(2);
```

`TH1::GetMean`メソッドで、ヒストグラムの平均値を取得できます。
引数でX軸またはY軸を指定できます。
