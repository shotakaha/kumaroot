# イベントを処理したい（`TTree::GetEntry`）

```cpp
#include <TTree.h>
#include <TFile.h>
#include <iostream>

TFile *file = TFile::Open("data.root");
TTree *tree = (TTree *)file->Get("tree");

Float_t x;
tree->SetBranchAddress("x", &x);

// エントリー0を取得
tree->GetEntry(0);
std::cout << "Entry 0: x = " << x << std::endl;
```

`TTree::GetEntry`メソッドで指定したエントリーのデータをメモリに読み込みます。
ブランチに設定されたアドレスの変数にデータが格納されます。

```python
from ROOT import TFile

file = TFile("data.root")
tree = file.Get("tree")

x = 0
tree.SetBranchAddress("x", x)

# エントリー0を取得
tree.GetEntry(0)
print(f"Entry 0: x = {x}")
```

## メソッドのシグネチャ

```cpp
Int_t GetEntry(Long64_t entry)
```

### 引数と戻り値

**引数**:

- **entry** - 取得するエントリー番号（0から開始）

**戻り値**:

- **Int_t**: 読み込んだバイト数。エラーの場合は負の値

## 単一のエントリーを取得したい（`GetEntry`）

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

TFile *file = TFile::Open("data.root");
TTree *tree = (TTree *)file->Get("tree");

Int_t event_id;
Float_t energy;
tree->SetBranchAddress("event_id", &event_id);
tree->SetBranchAddress("energy", &energy);

// エントリー5を取得
tree->GetEntry(5);

std::cout << "Event ID: " << event_id << ", Energy: " << energy << std::endl;

file->Close();
```

特定のエントリーをメモリに読み込み、ブランチのデータにアクセスできます。

## ループですべてのエントリーを処理したい（`GetEntry`）

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

TFile *file = TFile::Open("data.root");
TTree *tree = (TTree *)file->Get("tree");

Long64_t nentries = tree->GetEntries();

Float_t x, y;
tree->SetBranchAddress("x", &x);
tree->SetBranchAddress("y", &y);

for (Long64_t i = 0; i < nentries; i++) {
    tree->GetEntry(i);

    if (x > 100) {
        std::cout << "Entry " << i << ": x=" << x << ", y=" << y << std::endl;
    }
}

file->Close();
```

データ解析の基本となるエントリーループで、各エントリーのデータを順番に処理できます。

## 特定の条件のエントリーのみ処理したい（`GetEntry` + セレクション）

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

TFile *file = TFile::Open("data.root");
TTree *tree = (TTree *)file->Get("tree");

Float_t pt, eta;
tree->SetBranchAddress("pt", &pt);
tree->SetBranchAddress("eta", &eta);

Long64_t nentries = tree->GetEntries();

for (Long64_t i = 0; i < nentries; i++) {
    tree->GetEntry(i);

    // 条件を満たすエントリーのみ処理
    if (pt > 20.0 && std::abs(eta) < 2.5) {
        std::cout << "Entry " << i << ": pt=" << pt << ", eta=" << eta << std::endl;
    }
}

file->Close();
```

条件フィルタリングを適用して、特定の条件を満たすエントリーのみを処理できます。

## 概念的な理解

### GetEntryの動作

`GetEntry(i)`を呼び出すと：

1. ファイルからエントリーiのデータを読み込む
2. `SetBranchAddress`で設定されたメモリアドレスに値を格納
3. 他のエントリーのデータは上書きされる

### ブランチアドレスの重要性

```cpp
Float_t x = 0;
tree->SetBranchAddress("x", &x);  // 重要：&xはアドレス
tree->GetEntry(0);                // xの値が更新される
```

ブランチアドレスを設定しないと、`GetEntry`で読み込んだデータにアクセスできません。

## 関連メソッド

- [SetBranchAddress](./root-ttree-setbranchaddress.md) - ブランチアドレスを設定
- [GetEntries](./root-ttree-getentries.md) - エントリー数を取得
- [Branch](./root-ttree-branch.md) - ブランチを作成
- [Fill](./root-ttree-fill.md) - イベントを追加

## 参考リンク

- [ROOT TTree::GetEntry Documentation](https://root.cern/doc/master/classTTree.html#ae98bf44a21a61c0d9a9bb8f4d64d412d)
- [ROOT TTree Documentation](https://root.cern/doc/master/classTTree.html)
