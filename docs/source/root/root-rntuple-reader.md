# ファイルを読み込みたい（`RNTupleReader::Open`）

```cpp
auto reader = ROOT::RNTupleReader::Open("events", "output.root");
```

`RNTupleReader::Open()`で`NTuple`を読み込みます。
第一引数は`RNTuple`の名前、第二引数は入力ファイル名です。

## データを読み込みたい（`RNTupleReader::GetView`）

```cpp
void macro() {
    // Open RNTupleReader
    auto reader = ROOT::RNTupleReader::Open("output.root");

    // Get field views
    auto view_event_id = reader->GetView<int>("event_id");
    auto view_energy = reader->GetView<float>("energy");

    // Loop over entries
    for (auto entryIndex : *reader) {
        int event_id = view_event_id[entryIndex];
        float energy = view_energy[entryIndex];

        // Process data...
        std::cout << "Event ID: " << event_id << ", Energy: " << energy << std::endl;
    }
}
```

`RNTupleReader::GetView<T>()`はカラム単位の遅延ロードをするためのメソッドです。
`T`にフィールドのデータ型を指定し、引数にフィールド名を文字列で指定します。
戻り値は、指定したフィールドのビュー（`RNTupleView<T>`）です。

イベントループは、`RNTupleReader`自体をイテレーターとして呼び出します。
ループ内で、`view_event_id[entryIndex]`のように、ビューからエントリーごとに値を取得できます。

:::{note}
`GetView`しなかったカラムは、アクセスの対象外となります。
これは`TTree::SetBranchStatus`のような機能に相当します。
:::
