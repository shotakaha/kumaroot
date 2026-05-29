# オブジェクトを取得したい（`TFile::Get`）

```cpp
TFile *source = TFile::Open("source.root");

TH1D *hist = (TH1D *)source->Get("hist_name");
```

`TFile::Get`は、`TFile`内のオブジェクトを名前で取得するためのメソッドです。
返されるのは`TObject*`型のポインターであるため、適切な型にキャストする必要があります。
このサンプルでは、`TH1D*`型にキャストしています。
