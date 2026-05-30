# ファイル操作したい（`TFile`）

```cpp
#include <TFile.h>

void macro() {
    TFile *file = TFile::Open("output.root", "recreate");
    if (!file || file->IsZombie()) {
        std::cerr << "Error creating file: output.root" << std::endl;
        return;
    }
    // ファイル操作のコード
    TTree *tree = file->Get<TTree>("tree");

    // ファイルを閉じる
    file->Close();
}
```

`TFile`はROOTファイルを操作するためのクラスです。
`TFile::Open`はファイルを開くための静的メソッドです。

第一引数（`name`）にはファイル名を指定します。
ファイルが正常に開けない場合は`nullptr`を返すか、`IsZombie()`が`true`になります。

:::{note}

`TFile::Open`は、リモートにあるファイルや、ROOTの仮想ファイルシステムを利用したファイルアクセスもサポートしています。

ローカルにあるファイルを開くだけであれば
`new TFile`でも問題ありません。

:::

`TFile::Get`で、ファイル内のオブジェクトを名前で取得できます。
`TObject*`型のポインターが返されるため、適切な型にキャストする必要があります。
このサンプルでは`TTree*`型にキャストしています。

`TFile::Close`でファイルを閉じることができます。
マクロや関数のスコープを抜けるとファイルは自動的に閉じられますが、安全のため明示的に閉じる習慣をつけておくとよいです。

```python
import ROOT

# ファイルを開く
f = ROOT.TFile.Open("source.root")

# TTreeを取得
tree = f.Get("events")
tree.Print()

# ファイルを閉じる
f.Close()
```

```{toctree}
---
maxdepth: 1
---
root-tfile-open
root-tfile-get
root-tfile-cd
```

## リファレンス

- [TFile - ROOT Documentation](https://root.cern/doc/master/classTFile.html)
- [TSystem - ROOT Documentation](https://root.cern/doc/master/classTSystem.html)
