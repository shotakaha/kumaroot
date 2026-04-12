# TTreeしたい（`TTree`）

```cpp
#include <TTree.h>

// TTree::TTree(name, title)
TTree *tree = new TTree(
    "mytree",       // name
    "example tree"  // title
);
```

`TTree`はROOTでイベントデータを管理するためのクラスです。
`TTree::TTree`コンストラクターで`TTree`オブジェクトを作成できます。
`name`はTTreeの識別子で、プログラム内でTTreeを参照する際に使用します。
`title`はTTreeの説明やタイトルを設定するための文字列です。

`TTree`は高エネルギー物理実験のデータ保存・解析に広く使用されている形式です。
イベントごとにデータを効率的に保存し、あとから高速にアクセスできるように設計されています。

:::{note}

古いドキュメントやサンプルでは`TNtuple`が紹介されていることがありますが、現在は`TTree`を使用すればOKです。

:::

:::{hint}

さらに歴史をさかのぼると、Fortranで書かれたHBOOKの時代から`Ntuple`という概念が存在していました。
ROOTの`TNtuple`はその名残で、単純な構造のTreeを提供していました。
`TTree`は`TNtuple`の機能を内包をしており、より柔軟で高機能なデータ構造を提供しています。

ROOT6.34以降では、
`TTree`の機能がさらに強化され、
`RDataFrame`などの新しいデータ分析フレームワークも登場しています。

:::

```python
from ROOT import TTree

# Pythonでの作成
tree = TTree("mytree", "example tree")
```

## ファイルに保存したい（`TTree::Write`）

```cpp
#include <TFile.h>

// TTreeを作成
// ...（前のコードと同様）

// TTreeをファイルに保存
TFile *file = new TFile("tree.root", "RECREATE");
tree->Write();  // TTreeをファイルに書き込む
file->Close();  // ファイルを閉じる
```

`TTree`は`TFile`に保存できます。
`TTree::Write`メソッドでTTreeを書き込みます。
複数の`TTree`を作成した場合は、`TTree`ごとに`Write`することで、同じファイルに保存できます。

## ファイルから読み込みたい

```cpp
#include <TFile.h>
#include <TTree.h>

// ファイルからTTreeを読み込む
TFile *file = new TFile("tree.root", "READ");
TTree *tree = (TTree*)file->Get("mytree");  // "mytree"はTTreeの名前
```

`TFile::Get`メソッドで、ファイルからTTreeを読み込むことができます。
読み込んだTTreeは、元のTTreeと同じ名前でアクセスできます。

## リファレンス

- [TTree - ROOT Documentation](https://root.cern.ch/doc/master/classTTree.html)
- [TFile - ROOT Documentation](https://root.cern.ch/doc/master/classTFile.html)
