# RNTupleしたい

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

```{toctree}
---
maxdepth: 1
---
root-rntuple-model
root-rntuple-writer
root-rntuple-reader
root-rntuple-importer
```

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

## リファレンス

- [RNTuple Introduction](https://root.cern.ch/doc/master/group__NTuple.html)
- [ROOT::RNTuple Class Reference](https://root.cern.ch/doc/master/classROOT_1_1RNTuple.html)
- [ROOT::RNTupleReader Class Reference](https://root.cern.ch/doc/master/classROOT_1_1RNTupleReader.html)
- [ROOT::RNTupleWriter Class Reference](https://root.cern.ch/doc/master/classROOT_1_1RNTupleWriter.html)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
