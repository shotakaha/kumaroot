# TTreeを描画したい（`TTree::Draw`）

```cpp
tree->Draw(
    "energy_deposit",  // varexp
    "parent_id==0",    // selection
    "HIST",            // option
    1000,              // nentries
    0                  // firstentry
);
```

`TTree::Draw`でTTreeの変数を描画できます。
`varexp`に描画したい軸を設定します。
`selection`にフィルター条件を設定できます。

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

## リダイレクトしたい（`TTree::Draw`)

```cpp
tree->Draw(
    "energy_deposit >> h1(100, 0, 1000)",  // varexp with histogram definition
    "parent_id==0",
    "HIST",);
```

`varexp`にヒストグラム定義を含めることで、描画結果を新しいヒストグラムオブジェクトにリダイレクトできます。
この例では、`energy_deposit`のヒストグラムが`h1`という名前で作成されます。

```cpp
tree->Draw(
    "energy_deposit:position_x >> h2(100, 0, 1000, 100, -500, 500)",  // 2D histogram definition
    "parent_id==0",
    "COLZ",
)
```

2次元プロットも同様にヒストグラム定義を含めることができます。

## 複数条件したい（`TTree::Draw`）

```cpp
tree->Draw(
    "energy_deposit",
    "parent_id==0 && energy_deposit>10",
);
```

`selection`に複数の条件を指定することもできます。
論理演算子（&&、||、!）を使用して条件を組み合わせることができます。

## リファレンス

- [TTree - ROOT Documentation](https://root.cern/doc/master/classTTree.html)
