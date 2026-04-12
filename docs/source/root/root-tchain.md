# TChainしたい（`TChain`）

```cpp
TChain *chain = new TChain(
    "tree",        // name: 読み込むTTreeの名前
    "tree title",  // title: TChainのタイトルや説明。空欄でもOK
);
```

`TChain`クラスは、同じ構造の`TTree`を複数連結して、
ひとつの`TTree`に変換できます。
連結後の`TChain`は、通常の`TTree`と同じように使用できます。

## TTreeを追加したい（`TChain::Add`）

```cpp
// TChain::Add("ファイル名")
chain->Add("../anadata/CALIB_RUN10.root");
chain->Add("../anadata/CALIB_RUN11.root");
chain->Add("../anadata/CALIB_RUN12.root");
```

`TChain::Add`で、ファイルパスを指定して`TTree`を連結できます。
ファイルパスはワイルドカード（`*.root`）でも指定できます。

## イベント数を知りたい（`TChain::GetEntries`）

```cpp
Long64_t nentries = chain->GetEntries();
```

`TChain::GetEntries`で、連結したすべてのイベント数を取得できます。

## ブランチを取得したい（`TChain::SetBranchAddress`）

```cpp
Float_t energy_deposit;
chain->SetBranchAddress("energy_deposit", &energy_deposit);
```

`TChain::SetBranchAddress`で、ブランチを取得できます。
連結したすべての`TTree`のブランチにアクセスできます。

## ループ処理したい（`TChain::GetEntry`）

```cpp
Long64_t nentries = chain->GetEntries();
for (Long64_t i = 0; i < nentries; ++i) {
    chain->GetEntry(i);
    // energy_depositを使用した処理
}
```

`TChain::GetEntry`で、イベントごとにデータを取得できます。
連結したすべての`TTree`のイベントを順番に処理できます。

## ファイル数を知りたい（`TChain::GetNfiles`）

```cpp
Int_t nfiles = chain->GetNfiles();
```

`TChain::GetNfiles`で、連結したファイルの数を取得できます。

## TTreeの数を知りたい（`TChain::GetNtrees`）

```cpp
Int_t ntrees = chain->GetNtrees();
```

`TChain::GetNtrees`で、連結した`TTree`の数を取得できます。
