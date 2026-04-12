# TTreeしたい（`TTree`）

```cpp
#include <TTree.h>

// TTree::TTree(name, title)
TTree *tree = new TTree("mytree", "example tree");
```

`new TTree`でTTreeオブジェクトを作成します。

古いドキュメントやサンプルでは`TNtuple`が紹介されていることがありますが、現在は`TTree`を使用すればOKです。
`TTree`は`TNtuple`の機能を包含しており、より柔軟で強力です。

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
