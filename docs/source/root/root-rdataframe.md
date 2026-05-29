# データフレームしたい（`RDataFrame`）

```cpp
// イベント数を指定してRDataFrameを作成
auto df = ROOT::RDataFrame(100)
    .Define("x", "gRandom->Gaus(0, 1)")
    .Define("y", "gRandom->Gaus(0, 1)");
df.Describe();
```

`RDataFrame`は、ROOTにおいて[pandas](../pandas/pandas-usage.md)のような宣言的なデータフレーム操作を提供するクラスです。

`TTree`の上に構築された解析専用の高レベルAPIで、従来の`TTree`のイベントループをベースとしたコードよりも簡潔で効率的なデータ分析が可能になります。

## ファイルから読み込みたい

```cpp
auto df = ROOT::RDataFrame("events", "source.root");
```

`RDataFrame`はROOTファイルの`TTree`を直接読み込むことができます。
第一引数（`name`）には`TTree`の名前、
第二引数（`files`）にはファイル名を指定します。

```cpp
auto df = ROOT::RDataFrame(
    "events",
    {"file1.root", "file2.root", "file3.root"}
);
```

複数のファイルを同時に読み込むことができます。

:::{notes}
`TTree`のブランチ構造を自動的にに認識して、データフレームの列として扱います。
`TTree::SetBranchAddress`でブランチを設定する必要はありません。

:::

## `TTree`を読み込みたい

```cpp
TFile *source_file = TFile::Open("source.root");
TTree *tree = source_file->Get<TTree>("events");

auto df = ROOT::RDataFrame(tree);
```

`RDataFrame`は、すでに読み込んだ`TTree`を引数にして作成することもできます。
この方法は、`TTree`を読み込む際に特別な設定が必要な場合に便利です。

## リファレンス

- [ROOT::RDataFrame Documentation](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
- [ROOT Data Analysis Framework Guide](https://root.cern/manual/data_analysis_with_rdataframe/)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
