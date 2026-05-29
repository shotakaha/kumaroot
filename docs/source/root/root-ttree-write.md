# ツリーを保存したい（`TTree::Write`）

```cpp
tree->Write();
```

`TTree::Write`メソッドでツリーをROOTファイルに保存できます。
保存先は直前に作成した`TFile`です。

:::{note}
`TTree`を作成すると、その所有権が`gDirectory`に追加されます。
`gDirectory`は通常、もっとも最近に作成した`TFile`を指しています。

:::

## 保存先を変更したい

```cpp
TFile *file1 = TFile::Open("file1.root", "recreate");

TFile *file2 = TFile::Open("file2.root", "recreate");

// この時点で gDirectory = file2 になっているため
// tree->Writeするとfile2に保存される

// file1をアクティブにする
file1->cd();
tree->Write();
```

## 参考リンク

- [ROOT TTree::Write Documentation](https://root.cern/doc/master/classTTree.html#a4ad09b008c6b8b67e94d5d4d32f606b7)
- [ROOT TFile Documentation](https://root.cern/doc/master/classTFile.html#a506dde3c02a0d9b8e86f2ceb32ec00d0)
