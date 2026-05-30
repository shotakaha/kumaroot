# RNTupleしたい（`ROOT::RNTupleModel` / `ROOT::RNTupleWriter` / `ROOT::RNTupleReader`）

```cpp
void macro() {
    // Define schema
    auto model = ROOT::RNTupleModel::Create();
    // Define fields (= alternatives for TBranch)
    auto event_id = model->MakeField<int>("event_id");
    auto energy = model->MakeField<float>("energy");

    // Create RNTupleWriter
    auto writer = ROOT::RNTupleWriter::Recreate(
        std::move(model),
        "events",
        "output.root"
    );

    // Fill data
    for (int i = 0; i < 100; i++) {
        *event_id = i;
        *energy = 100.0f + i;
        writer->Fill();
    }

    // Commit and Close will be called automatically when writer goes out of scope
}
```

`RNTuple`は、ROOTのイベントデータI/Oシステムです。
25年以上の運用経験がある`TTree`の後継となるクラスです。
2018年ころから実験的な機能（`ROOT::Experimental`）として開発がはじまり、
ROOT 6.36で安定版としてリリースされました。

`TTree`が読み書き兼用の単一クラスであるのに対し、
`RNTuple`では、書き込み専用の`RNTupleWriter`と読み込み専用の`RNTupleReader`に分かれています。
これにより責務が明確となり、現代のストレージ技術に最適化できるようになっています。

:::{note}
C++の`std::tuple`やPythonの`tuple`（タプル）のように、`tuple`は「1組のデータ」を表す概念です。
そして、`Ntuple`は任意の`tuple`を格納できるデータ構造です。

素粒子実験の場合、
`tuple`は「1イベントのデータ」、
`Ntuple`は「ランの中のすべてのイベントのデータ」を
イメージするとわかりやすいと思います。

実は、このデータ構造の概念、PAWの時代から変わっていません。
PAWの`HBOOK NTuple`、ROOTの`TTree`と新しい`RNTuple`のどれも、
それぞれの世代の計算機環境に合わせて最適化された`Ntuple`の実装です。

:::

## スキーマを定義したい（`RNTupleModel::Create`）

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

## ファイルを作成したい（`RNTupleWriter::Recreate`）

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

## ファイルを読み込みたい（`RNTupleReader::Open`）

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

## 関連メソッド

- [TTree::Branch](./root-ttree-branch.md) - TTreeでのブランチ作成
- [TTree::Fill](./root-ttree-fill.md) - TTreeでのデータ追加
- [TTree::Write](./root-ttree-write.md) - TTreeでのファイル保存

## 参考リンク

- [ROOT RNTuple Documentation](https://root.cern/doc/master/namespacesROOT_1_1Experimental.html)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
- [ROOT Release Notes](https://root.cern/release-notes/)
