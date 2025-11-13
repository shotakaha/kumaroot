# データフレームしたい（`RDataFrame`）

```cpp
#include "ROOT/RDataFrame.hxx"

// ROOTファイルの読み込み
ROOT::RDataFrame df(
    "treeName",
    {"file1.root", "file2.root", "file3.root"}
);

// 条件でフィルタリング
auto filtered_df = df.Filter("x > 0 && y < 100");

// ヒストグラムを作成
auto filtered_df = df.Histo1D(
    {"hist", "Distribution", 100, 0, 10},
    "x"
);
hist->Draw();
```

[RDataFrame](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)は、ROOTにおいて[pandas](../pandas/pandas-usage.md)のような使い勝手を目指した高レベルAPIです。
2017年ころに導入され、最新のROOTで推奨されているデータ分析フレームワークです。

## ファイルを読み込みたい

```cpp
#include "ROOT/RDataFrame.hxx"

ROOT::RDataFrame df("treeName", "ファイル名.root");
```

ROOTファイルのTTreeをRDataFrameで読み込みます。

```cpp
#include "ROOT/RDataFrame.hxx"

ROOT::RDataFrame df(
    "treeName",
    {"file1.root", "file2.root", "file3.root"}
);
```

複数のROOTファイルを同時に処理できます。
内部的にはTChainが使用されています。

---

```python
import ROOT
df = ROOT.RDataFrame(
    "treeName",
    "ファイル名.root",
)

df = ROOT.RDataFrame(
    "treeName",
    ["file1.root", "file2.root", "file3.root"],
)
```

## 背景情報

:::{note}

ROOTは1995年にリリースされたときから`TTree`というデータ構造を軸にしていました。
しかし、LHC Run4の開始に合わせて、`RDataFrame`や`RNTuple`といった
よりモダンなフレームワークへと置き換えるというロードマップを描いています。

RDataFrameは従来のTTreeに比べて：

- 直感的なAPI設計
- より効率的なメモリ管理
- 並列処理の容易さ

を特徴としています。

:::

## リファレンス

- [ROOT::RDataFrame Documentation](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
- [ROOT Data Analysis Framework Guide](https://root.cern/manual/data_analysis_with_rdataframe/)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
