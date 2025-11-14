# 初期パラメーターを設定したい（`TF1::SetParameter`）

```cpp
// ガウス関数を作成
TF1 *f = new TF1("gaussian", "gaus", -10, 10);

f->SetParameter(0, 200);    // 正規化係数
f->SetParameter(1, 2.0);    // 平均値
f->SetParameter(2, 1.0);    // 標準偏差
```

`TF1::SetParameter`メソッドで、
パラメーターの初期値を手動で設定できます。
初期値がデータに近い場合、フィットが高速かつ正確になる傾向があります。
