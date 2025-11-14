# ツリーを保存したい（`TTree::Write`）

```cpp
#include <TTree.h>
#include <TFile.h>

TFile *file = new TFile("output.root", "recreate");

TTree *tree = new TTree("tree", "Event data");
Int_t run = 0;
tree->Branch("run", &run, "run/I");

run = 2025;
tree->Fill();

tree->Write();
file->Close();
```

`TTree::Write`メソッドでツリーをROOTファイルに保存します。
ツリーを保存するには、`TFile`を作成してからツリーを書き込む必要があります。

```python
import ROOT

file = ROOT.TFile("output.root", "recreate")

tree = ROOT.TTree("tree", "Event data")
run = ROOT.ctypes.c_int()
tree.Branch("run", run, "run/I")

run.value = 2025
tree.Fill()

tree.Write()
file.Close()
```

## メソッドのシグネチャ

```cpp
Int_t Write(const char* name = nullptr,
            Int_t option = 0,
            Int_t bufsize = 0)
```

### 引数と戻り値

**引数**:

- **name** - オブジェクト名（nullptrの場合は元の名前を使用）
- **option** - 書き込みオプション（0=デフォルト、1=上書き）
- **bufsize** - バッファサイズ

**戻り値**:

- 書き込んだバイト数

## ツリーをROOTファイルに保存したい（`Write`）

```cpp
#include <TTree.h>
#include <TFile.h>

TFile *file = new TFile("data.root", "recreate");

TTree *tree = new TTree("tree", "analysis data");
Int_t event_id = 0;
Float_t energy = 0.0;
tree->Branch("event_id", &event_id, "event_id/I");
tree->Branch("energy", &energy, "energy/F");

for (int i = 0; i < 1000; i++) {
    event_id = i;
    energy = 10.0 + i * 0.1;
    tree->Fill();
}

tree->Write();
file->Close();
```

基本的な保存方法です。`TFile`を"recreate"モードで作成し、データを入力したあとに`Write()`を呼び出します。
最後に`Close()`でファイルを閉じます。

## 既存のツリーに追加で保存したい（`Write`）

```cpp
#include <TTree.h>
#include <TFile.h>

TFile *file = new TFile("data.root", "update");

TTree *tree = new TTree("tree2", "additional data");
Int_t value = 0;
tree->Branch("value", &value, "value/I");

for (int i = 0; i < 100; i++) {
    value = i * 2;
    tree->Fill();
}

tree->Write();
file->Close();
```

既存のファイルに新しいツリーを追加する場合、`TFile`を"update"モードで開きます。
新しいツリーが既存のツリーと同じ名前の場合、オプション引数で上書きを指定できます。

## 複数のツリーを保存したい（`Write`）

```cpp
#include <TTree.h>
#include <TFile.h>

TFile *file = new TFile("multidata.root", "recreate");

// 1つ目のツリー
TTree *tree1 = new TTree("tree1", "first dataset");
Int_t val1 = 0;
tree1->Branch("val1", &val1, "val1/I");

for (int i = 0; i < 100; i++) {
    val1 = i;
    tree1->Fill();
}
tree1->Write();

// 2つ目のツリー
TTree *tree2 = new TTree("tree2", "second dataset");
Int_t val2 = 0;
tree2->Branch("val2", &val2, "val2/I");

for (int i = 0; i < 100; i++) {
    val2 = i * 2;
    tree2->Fill();
}
tree2->Write();

file->Close();
```

1つのROOTファイルに複数のツリーを保存する場合、各ツリーに対して`Write()`を呼び出します。
各ツリーは異なる名前で識別されます。

## 関連メソッド

- [Branch](./root-ttree-branch.md) - ブランチを作成
- [Fill](./root-ttree-fill.md) - イベントを追加
- [TFile](./root-tfile.md) - ROOTファイルの操作

## 参考リンク

- [ROOT TTree::Write Documentation](https://root.cern/doc/master/classTTree.html#a4ad09b008c6b8b67e94d5d4d32f606b7)
- [ROOT TFile Documentation](https://root.cern/doc/master/classTFile.html#a506dde3c02a0d9b8e86f2ceb32ec00d0)
