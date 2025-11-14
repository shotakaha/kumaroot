# RMSしたい（`TH1::GetRMS`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t rms = h->GetRMS();
printf("RMS: %f\n", rms);

// X軸のRMS（デフォルト）
Double_t rms_x = h->GetRMS(1);

// Y軸のRMS
Double_t rms_y = h->GetRMS(2);
```

`GetRMS`でRoot Mean Square（二乗平均平方根）を取得します。
これはデータの広がり（分散の平方根）を表します。
