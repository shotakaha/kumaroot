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
フィールドは`TTree::Branch`に相当する概念で、`MakeField<T>`で定義します。
`T`にフィールドのデータ型を指定し、引数にフィールド名を文字列で指定します。
戻り値のポインター名は任意ですが、フィールド名と同じにするとわかりやすいです。

## RNTupleを作成したい（`RNTupleWriter::Recreate`）

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

## データを読み込みたい（`RNTupleReader::Open`）

```cpp
#include <ROOT/RNTuple.hxx>

using RNTupleReader = ROOT::Experimental::RNTupleReader;

auto reader = RNTupleReader::Open("events", "data.root");
auto view = reader->GetView<int, float, float>({"event_id", "pt", "eta"});

for (auto entry : view) {
    int event_id = std::get<0>(entry);
    float pt = std::get<1>(entry);
    float eta = std::get<2>(entry);
    std::cout << "Event: " << event_id << ", pt: " << pt << ", eta: " << eta << std::endl;
}
```

`RNTupleReader::Open()`でNTupleから読み込みます。`GetView()`でフィールドを指定してアクセスできます。

## 複数のフィールドを定義したい（`MakeField`）

```cpp
#include <ROOT/RNTuple.hxx>

using RNTupleWriter = ROOT::Experimental::RNTupleWriter;

auto writer = RNTupleWriter::Recreate("events", "output.root");

auto run_number = writer->MakeField<int>("run");
auto event_number = writer->MakeField<int>("event");
auto energy = writer->MakeField<double>("energy");
auto charge = writer->MakeField<int>("charge");

for (int i = 0; i < 100; i++) {
    *run_number = 2025;
    *event_number = i;
    *energy = 100.0 + i;
    *charge = (i % 2 == 0) ? 1 : -1;
    writer->Fill();
}

writer->Commit();
```

各データ型に応じて`MakeField<T>()`でフィールドを定義します。複数のフィールドを定義して、`Fill()`で全フィールドを同時に記録します。

## 参考情報

### RNTupleの特徴

- **高速な読み書き**: 最適化されたバイナリ形式
- **デフォルト圧縮**: ディスク容量を効率的に利用
- **スケーラビリティ**: 大規模データセットに対応
- **モダン設計**: 並列処理に最適化

### 実験的ステータス

RNTupleはまだ実験的なクラスです。本番環境での使用は、ROOT開発チームの最新情報を確認してから判断してください。

## 関連メソッド

- [TTree::Branch](./root-ttree-branch.md) - TTreeでのブランチ作成
- [TTree::Fill](./root-ttree-fill.md) - TTreeでのデータ追加
- [TTree::Write](./root-ttree-write.md) - TTreeでのファイル保存

## 参考リンク

- [ROOT RNTuple Documentation](https://root.cern/doc/master/namespacesROOT_1_1Experimental.html)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
- [ROOT Release Notes](https://root.cern/release-notes/)
