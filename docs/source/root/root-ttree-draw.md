# TTreeを描画したい（``TTree::Draw``）

```cpp
// TTree::Draw("varexp", "selection");
tree->Draw("energy_deposit", "parent_id==0");
```

``TTree::Draw``で、TTreeの変数を描画できます。
第1引数（``varexp``）に、描画したい軸を設定します。
第2引数（``selection``）に、フィルターを設定します。
