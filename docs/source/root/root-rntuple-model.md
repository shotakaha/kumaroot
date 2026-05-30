# スキーマを定義したい（`RNTupleModel::Create`）

```cpp
auto model = ROOT::RNTupleModel::Create();
auto event_id = model->MakeField<int>("event_id");
auto energy = model->MakeField<float>("energy");
```

`RNTupleModel::Create`でスキーマを定義します。
スキーマのフィールドは、`MakeField<T>()`で追加します。
`T`にフィールドのデータ型を指定し、引数にフィールド名を文字列で指定します。
戻り値のポインター名は任意ですが、フィールド名と同
じにするとわかりやすいです。

:::{note}
スキーマの作成は、`TTree::Branch`の設定に相当する作業です。
`TTree::Branch`では、文字列でフィールドの型と名前を指定していましたが、
`MakeField<T>()`ではテンプレートメソッドで型を明示することで、より安全にスキーマを定義できます。
:::
