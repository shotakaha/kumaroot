# ファイルを作成したい（`RNTupleWriter::Recreate`）

```cpp
auto writer = ROOT::RNTupleWriter::Recreate(
    std::move(model),
    "events",
    "output.root"
);
```

`RNTupleWriter::Recreate()`で`NTuple`を新規作成します。
第一引数（`model`）にスキーマ（`RNTupleModel`）を渡します。
`std::move(model)`で、スキーマの所有権を`NTupleWriter`に移しています。
第二引数は`RNTuple`の名前、第三引数は出力ファイル名です。

`RNTupleWriter`は内部で`TFile`を使っています。
スコープを抜けると自動的に`Commit()`と`Close()`が呼ばれます。

:::{note}

「所有権」は、そのオブジェクトを削除する権限のことです。
`std::move`は、C++のムーブセマンティクスを利用して、オブジェクトの所有権を移すための関数です。
これにより、スキーマをコピーすることなく、効率的に
`RNTupleModel`から`RNTupleWriter`へ所有権を移すことができます。
`RNTupleWriter`がスキーマの所有権を持っているため、`RNTupleWriter`の寿命が終わると、スキーマも自動的にクリーンアップされます。

:::

## データを書き込みたい（`RNTupleWriter::Fill`）

```cpp
for (int i = 0; i < 100; i++) {
    *event_id = i;
    *energy = 100.0f + i;
    writer->Fill();
}
```

`RNTupleWriter::Fill()`でデータを追加します。
`Fill()`を呼ぶと、現在のフィールドの値が`Ntuple`に追加されます。

このサンプルでは、
`event_id`に0から99までの整数（`int`）を、
`energy`に100.0から199.0までの浮動小数点数（`float`）をセットしています

:::{note}
`MakeField<T>()`で作成したフィールドは、ポインターとして値をセットできます。
ポインターなので、`*event_id`のように先頭に`*`をつけて値を代入します。
:::
