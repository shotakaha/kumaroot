# 初期パラメーターを固定したい（`TF1::FixParameter`）

```cpp
// ガウス関数を作成
TF1 *f = new TF1("gaussian", "gaus", -5, 5);

// 平均値を0に固定
f->FixParameter(1, 0.0);
```

`TF1::FixParameter`メソッドで、特定のパラメーターを固定することで、他のパラメーターのみフィットできます。
