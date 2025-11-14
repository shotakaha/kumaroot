# フィット結果を取得したい（`TF1::GetParameter`）

```cpp
// ガウス関数を作成
TF1 *f = new TF1("gaussian", "gaus", -5, 5);

// ヒストグラムをフィット
h->Fit(f);

// パラメーターを取得
Double_t norm = f->GetParameter(0);
Double_t mean = f->GetParameter(1);
Double_t sigma = f->GetParameter(2);
```

`TF1::GetParameter`メソッドで、
フィットして得られたパラメーター値を取得できます。

## フィット誤差したい（`TF1::GetParError`）

```cpp
Double_t mean_error = f->GetParError(1);
Double_t sigma_error = f->GetParError(2);

std::cout << "Mean:" << mean " +/- " << mean_error << std::endl;
std::cout << "Sigma:" << sigma " +/- " << sigma_error << std::endl;
```

`TF1::GetParError`メソッドで、
フィット誤差を取得できます。
