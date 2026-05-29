# イベントを取得したい（`TTree::GetEntry`）

```cpp
// 100番目のイベント情報を取得
tree->GetEntry(100);
```

`TTree::GetEntry`メソッドで $i$ 番目のイベントを取得できます。
イベントはブランチに設定されたアドレスの変数に格納されます。

```cpp
void macro() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    Int_t event_id;
    Float_t energy;
    tree->SetBranchAddress("event_id", &event_id);
    tree->SetBranchAddress("energy", &energy);

    long long n_entries = tree->GetEntries();
    std::cout << "エントリー数: " << n_entries << std::endl;

    for (long long i = 0; i < n_entries; ++i) {
        tree->GetEntry(i);
        // エントリーiのデータにアクセス
        std::cout << "Entry " << i << ": event_id=" << event_id << ", energy=" << energy << std::endl;
    }
    file->Close();
}
```

$i$ 番目のイベントを単一で取得することもできますが、
通常は全イベント数（`TTree::GetEntries`）に対するループの中で、イベント情報を取得・選択して利用します。

## 参考リンク

- [ROOT TTree::GetEntry Documentation](https://root.cern/doc/master/classTTree.html#ae98bf44a21a61c0d9a9bb8f4d64d412d)
- [ROOT TTree Documentation](https://root.cern/doc/master/classTTree.html)
