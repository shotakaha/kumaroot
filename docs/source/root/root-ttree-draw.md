# ブランチの分布を確認したい（`TTree::Draw`）

```cpp
tree->Draw(
    "energy_deposit",  // varexp
    "parent_id==0",    // selection
    "HIST",            // option
    1000,              // nentries
    0                  // firstentry
);
```

`TTree::Draw`でブランチの分布をクイックチェックできます。
第一引数（`varexp`）に確認したいブランチ名を指定します。
第二引数（`selection`）にフィルター条件を指定できます。
第三引数（`option`）で描画オプションを指定できます。
第四引数（`nentries`）で描画するエントリー数を制限できます。
第五引数（`firstentry`）で描画開始エントリーを指定できます。

```cpp
tree->Draw(
    "energy_deposit:position_x",
    "parent_id==0",
    "COLZ");
```

`varexp`は`y:x`の形式で2次元プロットも可能です。

```python
import ROOT

# TTreeを作成・取得
tree = ROOT.TTree("tree", "Event data")

# 1次元プロット
tree.Draw(
    "energy_deposit",
    "parent_id==0",
    "HIST",
    1000,
    0
)

# 2次元プロット
tree.Draw(
    "energy_deposit:position_x",
    "parent_id==0",
    "COLZ"
)
```

## 1Dヒストグラムしたい（`TTree::Draw`)

```cpp
TH1D *h1 = new TH1D(
    "h1",
    "Energy Deposit;Energy [MeV];Entries",
    100, 0, 1000
);
tree->Draw(
    "energy_deposit >> h1",  // varexp with histogram definition
    "parent_id==0",
    "HIST",);
```

`varexp`にヒストグラムを含めることができます。
事前にTH1オブジェクトを作成することで、
タイトルやビン数などを制御できます。

## 2Dヒストグラムしたい（`TTree::Draw`）

```cpp
TH2D *h2 = new TH2D(
    "h2",
    "Energy Deposit vs Position;Position X [mm];Energy Deposit [MeV]",
    100, 0, 1000,
    100, -500, 500
);
tree->Draw(
    "energy_deposit:position_x >> h2",  // 2D histogram definition
    "parent_id==0",
    "COLZ",
)
```

2次元ヒストグラムも1次元ヒストグラムと同様に
`varexp`に含めることができます。

## 複数条件したい（`TTree::Draw`）

```cpp
tree->Draw(
    "energy_deposit",
    "parent_id==0 && energy_deposit>10",
);
```

`selection`に複数の条件を指定できます。
論理演算子（`&&`、`||`、`!`）を使用して条件を組み合わせることができます。

## リファレンス

- [TTree - ROOT Documentation](https://root.cern/doc/master/classTTree.html)
