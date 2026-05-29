# イベント数を取得したい（`TTree::GetEntries`）

```cpp
long long n_entries = tree->GetEntries();
std::cout << "エントリー数: " << n_entries << std::endl;
```

`TTree::GetEntries`メソッドで、TTreeのイベント数を取得できます。
第一引数（`selection`）でフィルター条件を指定できます。
大規模なデータ解析に対応しているため、戻り値は`Long64_t`型となっています。
`Long64_t`型もしくは`long long`型で受け取ることができます。

イベント数はデータ解析に必要な基本情報です。
TTreeを使ったデータ解析ではループ処理に利用します。

```python
n_entries = tree.GetEntries()
print(f"エントリー数: {n_entries}")
```

## リファレンス

- [ROOT TTree::GetEntries Documentation](https://root.cern/doc/master/classTTree.html#a7c15435dc3d3e5626a1d8f20a5b2d78)
- [ROOT TTree Documentation](https://root.cern/doc/master/classTTree.html)
- [ROOT TFile Documentation](https://root.cern/doc/master/classTFile.html)
