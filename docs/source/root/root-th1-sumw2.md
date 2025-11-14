# 重み付きデータのエラーしたい（`TH1::Sumw2`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Weighted Data", 100, 0, 10);

// 重み付きデータのエラーを追跡開始
h->Sumw2();

// 重み付きデータを入力
for (Int_t i = 0; i < 1000; i++) {
    h->Fill(gRandom->Gaus(5, 1), gRandom->Uniform(0.5, 1.5));
}

// エラーを取得
Double_t error = h->GetBinError(10);
printf("Bin 10 Error: %f\n", error);
```

`TH1::Sumw2`メソッドで、
重み付きヒストグラムの各ビンのエラーを自動計算できます。
ヒストグラムにデータを追加する前に、呼び出す必要があります。
