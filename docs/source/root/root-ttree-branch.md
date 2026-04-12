# ブランチを作成したい（`TTree::Branch`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Event data");
Int_t run = 0;
tree->Branch(
    "run",    // name
    &run,     // address
    "run/I"   // leaflist
);

run = 2025;
tree->Fill();
```

`TTree::Branch`メソッドで`TTree`にブランチを作成できます。
ブランチは変数を格納するための構造で、イベントごとに異なる値を保存できます。

`name`はブランチの名前を指定します。
`address`は変数のアドレスを指定します。
配列の場合は先頭アドレスでOKです。

:::{hint}

変数が実体の場合は`&`が必要です。
配列の場合は、変数が先頭アドレスを指すため`&`は不要です。

:::

`leaflist`は変数の型を指定する文字列で、`変数/型`の形式で記述します。
たとえば、`int`型の変数を保存する場合は`I`、`float`型の場合は`F`、`double`型の場合は`D`を使用します。
ブランチを作成した後、変数に値を設定して`Fill`メソッドを呼び出すことで、イベントデータを保存できます。

```python
import ROOT

tree = ROOT.TTree("tree", "Event data")
run = ROOT.ctypes.c_int()
tree.Branch("run", run, "run/I")

run.value = 2025
tree.Fill()
```

## 複数ブランチしたい（`TTree::Branch`）

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Event data");

Int_t run = 0;
Float_t energy = 0.0;
Int_t fadc[100];

tree->Branch("run", &run, "run/I");
tree->Branch("energy", &energy, "energy/F");
tree->Branch("fadc", fadc, "fadc[100]/I");
```

`TTree::Branch`を複数回呼び出すことで、複数のブランチを作成できます。
イベントごとに異なる値を保存するため、各ブランチに対応する変数が必要です。

固定長配列をブランチに追加する場合、`leaflist`に配列の長さを明示的に指定します。
第2引数は配列のアドレスのため、配列名をそのまま指定できます。

## 可変長配列したい（`TTree::Branch`）

```cpp
#include <TTree.h>
#include <vector>

// 可変長配列を保存するためのブランチ
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

イベントごとに異なるサイズの配列を保存したい場合、可変長配列を使用します。
`TTree::Branch`の使い方は固定長配列と同様です。
C++標準の`std::vector`を使用すると、
ROOTが自動的にサイズと型を判定してくれるため`leaflist`は不要です。

## 参考リンク

- [TTree - ROOT Documentation](https://root.cern/doc/master/classTTree.html)
