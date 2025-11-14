# ブランチを作成したい（`TTree::Branch`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Event data");
Int_t run = 0;
tree->Branch("run", &run, "run/I");

run = 2025;
tree->Fill();
```

`TTree::Branch`メソッドでツリーにブランチを作成し、変数をツリーに関連付けることで、複雑なデータ構造を設定できます。

```python
import ROOT

tree = ROOT.TTree("tree", "Event data")
run = ROOT.ctypes.c_int()
tree.Branch("run", run, "run/I")

run.value = 2025
tree.Fill()
```

## メソッドのシグネチャ

```cpp
TBranch* Branch(const char* name,
                Long_t address,
                const char* leaflist,
                Int_t bufsize = 32000)
```

### 引数と戻り値

**引数**:

- **name** - ブランチ名を指定します。変数名とのひも付けは`address`で行います
- **address** - 変数のアドレスを指定します。変数が実体の場合は`&`が先頭に必要です。配列の場合はそのまま指定します
- **leaflist** - 変数の型を指定します。`変数/型`形式で記述（`int`は`I`、`float`は`F`、`double`は`D`など）
- **bufsize** - バッファサイズ（デフォルト値は32000）

**戻り値**:

- 作成されたTBranchオブジェクトへのポインター

## 単一の値をブランチに追加したい（`Branch`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Event data");
Int_t run = 0;
Float_t energy = 0.0;
tree->Branch("run", &run, "run/I");
tree->Branch("energy", &energy, "energy/F");

for (int evt = 0; evt < 100; evt++) {
    run = 2025;
    energy = 100.5 + evt * 0.1;
    tree->Fill();
}
```

単一の変数をブランチとして追加する場合、変数の型を指定して`Branch()`を呼び出します。
複数のブランチを定義する場合、各変数ごとに`Branch()`を呼び出します。

## 配列をブランチに追加したい（`Branch`）

```cpp
#include <TTree.h>

Int_t val[100];
TTree *tree = new TTree("tree", "array branch");
tree->Branch("val", val, "val[100]/I");

for (int i = 0; i < 100; i++) {
    val[i] = i;
    tree->Fill();
}
```

固定長配列をブランチに追加する場合、`leaflist`に配列の長さを明示的に指定します。
第2引数は配列のアドレスのため、配列名をそのまま指定できます。

## 可変長配列をブランチに追加したい（`Branch`）

```cpp
#include <TTree.h>

Int_t fN = 0;
Int_t val[100];
TTree *tree = new TTree("tree", "variable-length array");
tree->Branch("nch", &fN, "nch/I");
tree->Branch("val", val, "val[nch]/I");

for (int evt = 0; evt < 100; evt++) {
    fN = 10 + evt % 20;
    for (int i = 0; i < fN; i++) {
        val[i] = i;
    }
    tree->Fill();
}
```

可変長配列を使う場合、配列のサイズを保存するブランチと配列データ用ブランチの両方が必要です。
重要なのは、`leaflist`に配列名ではなく、サイズを格納するブランチ名（ここでは`nch`）を指定することです。

## 可変長文字列をブランチに追加したい（`Branch`）

```cpp
#include <TTree.h>
#include <cstring>

const Int_t NMAX_MOJI = 100;
char moji[NMAX_MOJI];
Int_t nmoji = 0;
TTree *tree = new TTree("tree", "variable-length string");
tree->Branch("nmoji", &nmoji, "nmoji/I");
tree->Branch("moji", moji, "moji[nmoji]/C");

strcpy(moji, "Hello ROOT");
nmoji = strlen(moji);
tree->Fill();
```

文字列をブランチに追加する場合、文字数を管理するブランチと、文字配列用ブランチの両方が必要です。
`leaflist`の型指定に`C`を使用します。

## std::vectorをブランチに追加したい（`Branch`）

```cpp
#include <TTree.h>
#include <vector>

std::vector<Double_t> vec;
TTree *tree = new TTree("tree", "vector branch");
tree->Branch("vec", &vec);

for (int evt = 0; evt < 100; evt++) {
    vec.clear();
    for (int i = 0; i < 10; i++) {
        vec.push_back(i * 0.1);
    }
    tree->Fill();
}
```

`std::vector`をブランチに追加する場合、第2引数にベクトルのアドレスを指定し、第3引数は省略します。
ROOTが自動的にベクトルのサイズと型を判定します。ベクトルは通常、ブランチの最後に配置することが推奨されます。

## 関連メソッド

- [Fill](./root-ttree-fill.md) - イベントを追加
- [Write](./root-ttree-write.md) - ツリーをファイルに保存
- [GetBranch](./root-ttree-getbranch.md) - ブランチを取得

## 参考リンク

- [ROOT TTree::Branch Documentation](https://root.cern/doc/master/classTTree.html#a9e1c8fb17a98a71c34ef78b86f8f1f4a)
