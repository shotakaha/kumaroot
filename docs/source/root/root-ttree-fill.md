# イベントを記録したい（`TTree::Fill`）

```cpp
tree->Fill();
```

`TTree::Fill`メソッドでブランチに設定した変数の現在の値を記録できます。
通常は1イベントごとに呼び出します。
複数のブランチがある場合、すべてのブランチの値が同時に1つのエントリーとして記録されます。

## 参考リンク

- [ROOT TTree::Fill Documentation](https://root.cern/doc/master/classTTree.html#a51846c4bdfac85f6cf6ebe0b0edb5bb1)
