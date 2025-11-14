# イベントを追加したい（`TTree::Fill`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Event data");
Int_t value = 0;
tree->Branch("value", &value, "value/I");

// 単一のイベントを追加
tree->Fill();

// ループでイベントを追加
for (int i = 0; i < 100; i++) {
    value = i;
    tree->Fill();
}
```

`TTree::Fill`メソッドでブランチに設定した変数の現在値をイベントレコードとして追加します。
ブランチが複数ある場合、すべてのブランチの値が同時に1つのエントリとして記録されます。

```python
import ROOT

tree = ROOT.TTree("tree", "Event data")
value = ROOT.std.vector('int')()
tree.Branch("value", value)

# 単一のイベントを追加
tree.Fill()

# ループでイベントを追加
for i in range(100):
    value.clear()
    value.push_back(i)
    tree.Fill()
```

## メソッドのシグネチャ

```cpp
Int_t Fill()
```

### 引数と戻り値

**戻り値**:

- ツリーに追加されたエントリ数（通常は正の値）

## 単一のイベントを追加したい（`Fill`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "simple event");
Int_t count = 0;
tree->Branch("count", &count, "count/I");

count = 42;
tree->Fill();
```

ブランチに値を設定してから`Fill()`を呼び出します。
1回の呼び出しで1つのイベントレコードが追加されます。

## 複数のブランチにデータを追加したい（`Fill`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "multi-branch event");
Int_t run = 0;
Float_t energy = 0.0;
tree->Branch("run", &run, "run/I");
tree->Branch("energy", &energy, "energy/F");

// イベントループ
for (int evt = 0; evt < 1000; evt++) {
    run = 2025;
    energy = 100.5 + evt * 0.1;
    tree->Fill();
}
```

複数のブランチを定義すると、`Fill()`は全ブランチの現在値を同時に記録します。
各ブランチのデータが1つのエントリとして関連付けられ、あとでデータ分析時に対応するデータにアクセスできます。

## 関連メソッド

- [Branch](./root-ttree-branch.md) - ブランチを作成
- [Write](./root-ttree-write.md) - ツリーをファイルに保存
- [GetEntries](./root-ttree-getentries.md) - ツリーのエントリ数を取得

## 参考リンク

- [ROOT TTree::Fill Documentation](https://root.cern/doc/master/classTTree.html#a51846c4bdfac85f6cf6ebe0b0edb5bb1)
