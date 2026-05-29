# ディレクトリ操作したい（`TFile::cd` / `TFile::mkdir`）

```cpp
TFile *f = TFile::Open("output.root", "recreate");
f->mkdir("subdir");  // "subdir"ディレクトリを作成
f->cd("subdir");  // "subdir"ディレクトリに移動
tree->Write();  // "subdir"に書き込まれる
f->Close();
```

ROOTファイルの中に、ディレクトリ構造を作成できます。
`TFile::mkdir`でディレクトリを作成できます。
`TFile::cd`で、ファイル内のディレクトリを変更できます。

現在アクティブなディレクトリは`gDirectory`というグローバルポインターで参照できます。
`TFile::cd`でディレクトリを変更すると、`gDirectory`も変更されます。
`TTree::Write`などの書き込み操作は、現在の`gDirectory`に対して行われます。
