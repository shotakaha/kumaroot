# TTreeしたい（`TTree`）

```cpp
#include <TTree.h>

void macro() {
    TTree *tree = new TTree(
        "events",       // name
        "event data"  // title
    );
}
```

`TTree`はROOTのデータ構造の中核となるクラスです。
イベントごとにデータを効率的に管理できるのが特徴で、物理実験のデータ保存・解析に広く使用されています。
`TTree`の列をブランチと呼び、行をエントリーと呼びます。

第一引数（`name`）はTTreeの識別子です。
マクロ内や`TFile`内で一意となる名前を指定します。

第二引数（`title`）はTTreeを説明する文字列です。
文字数の上限は255文字で、TTreeの内容を簡潔に説明するために使用されます。

```python
from ROOT import TTree

def macro():
    tree = TTree("events", "event data")
```

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
