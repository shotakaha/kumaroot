# TTreeをRNTupleに変換したい（`RNTupleImporter`）

```cpp
void macro() {
    // Define importer
    auto importer = ROOT::RNTupleImporter::Create(
        "source.root",
        "events",
        "target.root"
    );
    importer->Import();
}
```

`RNTupleImporter`は、既存の`TTree`を`RNTuple`に変換するためのクラスです。
`RNTupleImporter::Create()`でインポーターを作成し、`Import()`で変換を実行します。
第一引数は入力ファイル名、第二引数は`TTree`の名前、第三引数は出力ファイル名です。

:::{note}
すべてのブランチを、自動的に対応するフィールドに変換します。
`TTree`の構造が複雑な場合や、特殊なデータ型を使用している場合は、専用の変換マクロを作成する必要があります。
:::
