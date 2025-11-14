# カイ二乗値したい（`TF1::GetChiSquare`）

```cpp
// ガウス関数を作成
TF1 *f = new TF1("gaussian", "gaus", -5, 5);

// ヒストグラムをフィット
h->Fit(f);

// カイ二乗値を取得
Double_t chi2 = f->GetChisquare();
Int_t ndf = f->GetNDF();
std::cout << "Chi2: " << chi2 << ", NDF: " << ndf << std::endl;
```

`TF1::GetChiSquare`メソッドでカイ二乗値を取得できます。
フィットを評価できます。
