# ブランチを読み込みたい（`TTree::SetBranchAddress`）

```cpp
// Define branch variables
int run{0};
double energy{0.0};

// Associate branch variables with the TTree branches
tree->SetBranchAddress("run", &run);
tree->SetBranchAddress("energy", &energy);
```

`TTree::SetBranchAddress`は、既存のブランチを読み込むためのメソッドです。
ファイルか読み込んだ`TTree`にあるブランチと、マクロ内の変数を紐づけるために使用します。

第一引数（`name`）は、読み込むブランチの名前を指定します。
第二引数（`address`）は、ブランチのデータを格納する変数のアドレスを指定します。
ブランチのデータ型と変数の型が一致している必要があります。

ブランチを読み込んだ後、`TTree::GetEntry`でイベントを取得すると、ブランチのデータが指定した変数に格納されます。
