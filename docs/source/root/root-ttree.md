# TTreeしたい（`TTree`）

```cpp
#include <TFile.h>
#include <TTree.h>

void macro() {
    TFile *file = TFile::Open("output.root", "recreate");
    TTree *tree = new TTree("events", "Event Data");

    tree->Branch("run", &run, "run/I");
    tree->Branch("energy", &energy, "energy/D");

    for (int i = 0; i < 1000; ++i) {
        run = i;
        energy = 1.0 + i * 0.01;
        tree->Fill();
    }
    tree->Write();
    file->Close();
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

```{toctree}
---
maxdepth: 1
---
root-ttree-branch
root-ttree-setbranchaddress
root-ttree-print
root-ttree-draw
root-ttree-entries
root-ttree-entry
root-ttree-fill
root-ttree-readfile
root-ttree-write
```

## リファレンス

- [TTree - ROOT Documentation](https://root.cern.ch/doc/master/classTTree.html)
- [TFile - ROOT Documentation](https://root.cern.ch/doc/master/classTFile.html)
