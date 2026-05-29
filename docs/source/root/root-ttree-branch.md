# ブランチを作成したい（`TTree::Branch`）

```cpp
#include <TFile.h>
#include <TTree.h>

void macro() {
    TFile* file = new TFile::Open("output.root", "RECREATE");
    TTree *tree = new TTree("events", "Event data");

    int run{0};          // イベント番号
    double energy{0.0};  // エネルギー
    int n_hits{0};       // ヒット数
    int fadc[100]{0};    // FADCの波形データ（最大100サンプル）

    // Branch("name", address, "leaflist")
    tree->Branch("run", &run, "run/I");
    tree->Branch("energy", &energy, "energy/D");
    tree->Branch("n_hits", &n_hits, "n_hits/I");
    tree->Branch("fadc", fadc, "fadc[100]/I");

    for (int i = 0; i < 1000; ++i) {
        run = i;
        energy = 1.0 + i * 0.01;
        n_hits = i % 10;
        // エントリーを記録する
        tree->Fill();
    }
    // ファイルに書き込む
    tree->Write();
    file->Close();
}
```

`TTree::Branch`は`TTree`にブランチを作成するメソッドです。
ブランチは変数を格納するための構造で、イベントごとに異なる値を保存できます。

第一引数（`name`）にはブランチの名前を指定します。
第二引数（`address`）には変数のアドレスを指定します。
配列を使う場合は先頭アドレスにします。

:::{hint}

変数が実体の場合は`&変数名`のように先頭に`&`をつけます。
配列の場合は、変数が先頭アドレスを指すため`&`は不要です。

:::

第三引数（`leaflist`）は変数名とその型を指定する文字列で、`変数/型`の形式で記述します。
たとえば、`int`型の変数を保存する場合は`I`、`float`型の場合は`F`、`double`型の場合は`D`を使用します。
固定長配列を使う場合は、`leaflist`に配列の長さを明示します。

ブランチを作成した後、変数に値を設定して`Fill`メソッドを呼び出すことで、イベントデータを保存できます。

```python
import ROOT
import numpy as np

def macro():

    with ROOT.TFile("output.root", "RECREATE") as f:
        tree = ROOT.TTree("events", "Event data")

        # ブランチ変数を定義する（arrayもしくはnumpy.array）
        run = np.zeros(1, dtype=np.int32)  # イベント番号
        energy = np.zeros(1, dtype=np.float64)  # エネルギー
        n_hits = np.zeros(1, dtype=np.int32)  # ヒット数
        fadc = np.zeros(100, dtype=np.int32)  # FADCの波形データ（最大100サンプル）

        # ブランチを作成する
        tree.Branch("run", run, "run/I")
        tree.Branch("energy", energy, "energy/D")
        tree.Branch("n_hits", n_hits, "n_hits/I")
        tree.Branch("fadc", fadc, "fadc[100]/I")

        # イベントループ
        for i in range(1000):
            run[0] = i
            energy[0] = 1.0 + i * 0.01
            n_hits[0] = i % 10
            tree.Fill()
        tree.Write()
```

## 可変長配列したい（`TTree::Branch`）

```cpp
TTree *tree = new TTree("events", "Event data");

int n_hits{0};
float hit_energy[100]{0}; // ヒットのエネルギー（最大100ヒット）

tree->Branch("n_hits", &n_hits, "n_hits/I");
tree->Branch("hit_energy", hit_energy, "hit_energy[n_hits]/F");
```

イベントごとに異なるサイズの配列を保存する場合、
可変長配列を使用します。
このとき、配列の長さの変数と配列の両方をブランチとして作成します。
配列を定義する際には、配列の最大サイズを指定する必要があります。

このサンプルでは
イベントごとの異なるヒットのエネルギーを記録するために、
イベントごとのヒット数（`n_hits`）と、
ヒットごとのエネルギー（`hit_energy`）のブランチを作成しています。

## 可変長配列したい（`std::vector`）

```cpp
void macro() {
    TFile* file = new TFile::Open("output_vector.root", "RECREATE");
    TTree *tree = new TTree("events", "Event data");

    std::vector<double> hit_energy;
    tree->Branch("hit_energy", &hit_energy);

    for (int event = 0; event < 1000; ++event) {
        // イベントループの先頭でベクター配列をクリアする
        hit_energy.clear();
        for (int h = 0; h < event + 1; ++h) {
            // ベクター配列にヒットのエネルギーを追加する
            hit_energy.push_back(0.5 * (h + 1));
        }
        tree->Fill();
    }
    tree->Write();
    file->Close();
}
```

C++標準の`std::vector`を使用して可変長配列を保存できます。
この場合、配列の最大サイズの指定は不要です。
ROOTが自動的にサイズと型を判定してくれるため`leaflist`は不要です。

## 参考リンク

- [TTree - ROOT Documentation](https://root.cern/doc/master/classTTree.html)
