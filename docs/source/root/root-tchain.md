# TChainしたい（`TChain`）

```cpp
TChain *chain = new TChain(
    "events",      // name
    "Event data",  // title
);
```

`TChain`は、同じ構造の`TTree`を複数連結して、ひとつの`TTree`として扱えるようにするクラスです。

第一引数（`name`）には、連結する`TTree`の名前を指定します。
連結するすべての`TTree`は、同じ名前でなければなりません。
第二引数（`title`）は、`TChain`のタイトルや説明を指定します。
空欄でも問題ありません。

`TChain`クラスは`TTree`クラスを継承しているため、`TTree`と同じように`GetEntry`や`SetBranchAddress`などのメソッドを使用できます。

:::{note}

`TChain`は読み取り専用です。
`Tree::Branch`や`Tree::Fill`などの書き込み用のメソッドは使用できません。

:::

## TTreeを追加したい（`TChain::Add`）

```cpp
// TChain::Add("ファイル名")
chain->Add("../anadata/CALIB_RUN10.root");
chain->Add("../anadata/CALIB_RUN11.root");
chain->Add("../anadata/CALIB_RUN12.root");
```

`TChain::Add`はファイルを連結するメソッドです。
第一引数にファイルパスを指定してします。
ファイルパスはワイルドカード（`*.root`）で指定できます。

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
