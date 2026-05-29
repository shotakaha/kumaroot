# イベントを記録したい（`TTree::Fill`）

```cpp
void macro() {
    TFile *file = TFile::Open("output.root", "recreate");
    TTree *tree = new TTree("events", "Event data");

    // ブランチ変数を定義する
    int run{0};  // イベント番号
    double energy{0.0};  // エネルギー
    int n_hits{0};  // ヒット数

    // ブランチを作成する
    tree->Branch("run", &run, "run/I");
    tree->Branch("energy", &energy, "energy/D");
    tree->Branch("n_hits", &n_hits, "n_hits/I");

    // イベントループ
    for (int i = 0; i < 1000; i++) {
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

`TTree::Fill`は、イベント（エントリー）を`TTree`に追加するメソッドです。

イベントループの中で、ブランチ変数に値を設定した後に`Fill()`を呼び出すことで、その値を1つのエントリーとして記録できます。
複数のブランチがある場合、すべてのブランチの値が同時に1つのエントリーとして記録されます。

## 参考リンク

- [ROOT TTree::Fill Documentation](https://root.cern/doc/master/classTTree.html#a51846c4bdfac85f6cf6ebe0b0edb5bb1)
