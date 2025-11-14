# エラーを追加したい（`TH1::SetBinContent` / `TH1::SetBinError`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Custom Error", 100, 0, 10);

// ビンの内容を設定
h->SetBinContent(10, 50);

// ビンのエラーを明示的に設定
h->SetBinError(10, 5);  // ビン10のエラー=5

// エラーを取得
Double_t error = h->GetBinError(10);  // 5が返される
```

`TH1::SetBinContent`と
`TH1::SetBinError`を組み合わせて、
任意のビンの値とエラーのデータを追加できます。
