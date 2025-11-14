# TTreeを描画したい（`TTree::Draw`）

```cpp
#include <TFile.h>
#include <TTree.h>

TFile* file = new TFile("data.root");
TTree* tree = (TTree*)file->Get("tree");

// 基本的な描画
tree->Draw("energy_deposit");

// フィルター条件付き描画
tree->Draw("energy_deposit", "parent_id==0");
```

`TTree::Draw`でTTreeの変数を描画できます。第1引数（`varexp`）に描画したい軸を設定し、第2引数（`selection`）にフィルター条件を設定します。

```python
import ROOT

file = ROOT.TFile("data.root")
tree = file.Get("tree")

# 基本的な描画
tree.Draw("energy_deposit")

# フィルター条件付き描画
tree.Draw("energy_deposit", "parent_id==0")
```

## メソッドのシグネチャ

```cpp
Long64_t Draw(const char* varexp, const char* selection = "",
              Option_t* option = "", Long64_t nentries = kMaxEntries,
              Long64_t firstentry = 0)
```

### 引数と戻り値

**引数**:

- **varexp** - 描画する変数。形式: `"variable"`（1D）、`"y:x"`（2D）、`"z:y:x"`（3D）
- **selection** - フィルター条件（オプション、デフォルト: なし）
- **option** - 描画オプション（オプション、デフォルト: 空文字列）
- **nentries** - 処理するエントリ数（デフォルト: 全エントリ）
- **firstentry** - 開始エントリ番号（デフォルト: 0）

**戻り値**:

- 描画されたエントリ数（条件を満たしたエントリ数）

## 1次元ヒストグラムを描画したい（`Draw`）

```cpp
#include <TFile.h>
#include <TTree.h>

TFile* file = new TFile("data.root");
TTree* tree = (TTree*)file->Get("tree");

tree->Draw("energy_deposit");
```

`Draw`メソッドで、単一の変数をヒストグラムとして描画できます。

## 2次元プロットを作成したい（`Draw`）

```cpp
#include <TFile.h>
#include <TTree.h>

TFile* file = new TFile("data.root");
TTree* tree = (TTree*)file->Get("tree");

tree->Draw("energy_deposit:position_x");
```

`Draw`メソッドで2つの変数の関係を散布図として可視化できます。横軸に`position_x`、縦軸に`energy_deposit`がプロットされます。

## フィルター条件付きで描画したい（`Draw`）

```cpp
#include <TFile.h>
#include <TTree.h>

TFile* file = new TFile("data.root");
TTree* tree = (TTree*)file->Get("tree");

tree->Draw("energy_deposit", "parent_id==0");

// 複数条件を指定
tree->Draw("energy_deposit", "parent_id==0 && energy_deposit>10");
```

`Draw`メソッドの第2引数に条件を指定することで、特定の条件を満たすデータのみを描画できます。論理演算子で複数条件を結合することも可能です。

## 描画結果から統計情報を取得したい（`Draw`）

```cpp
#include <TFile.h>
#include <TTree.h>

TFile* file = new TFile("data.root");
TTree* tree = (TTree*)file->Get("tree");

Long64_t n = tree->Draw("energy_deposit", "parent_id==0");
std::cout << "Matched entries: " << n << std::endl;
```

`Draw`メソッドの戻り値でフィルター条件に合致したエントリ数を取得できます。

## 関連メソッド

- `TTree::Scan`: データを表形式で表示
- `TTree::GetEntries`: 総エントリ数を取得
- `TTree::GetLeaf`: リーフ（葉）オブジェクトを取得

## 参考資料

- [ROOT Documentation - TTree::Draw](https://root.cern/doc/master/classTTree.html#a73450649dc6e54b5b94516c91e3db4a)
