# TChainしたい

```cpp
TChain *chain=new TChain("tree", "tree title");
// 第1引数: 読み込むTTreeの名前; 読み込むTTreeの名前と一致してないと怒られる
// 第2引数: TChainのタイトルや説明。空欄でもOK
```

``TChain``クラスで、同じ構造の ``TTree``を複数連結（＝chain）して、
ひとつの ``TTree`` として扱うことができます。
``TTree`` を継承したクラスなので、連結した後は ``TTree``と同じように使えます。

## 複数のTTreeを読み込みたい（``TChain::Add``）

```cpp
// TChain::Add("ファイル名")
chain->Add("../anadata/CALIB_RUN10.root");
chain->Add("../anadata/CALIB_RUN11.root");
chain->Add("../anadata/CALIB_RUN12.root");
```

``TChain::Add``で、複数のファイル名を連結できます。
ファイル名はワイルドカード（``*.root``）で指定できます。

## サンプルコード : ループで読み込む

```cpp
TChain *chain=new TChain("chain", "chain_title");
const Int_t fNFile=11;
Int_t iFile;
for (iFile=0; iFile<fNFile; ++iFile) {
    chain->Add(Form("../anadata/CALIB_RUN%d.root", iFile+10));
}
```

## サンプルコード : ワイルドカード指定

```cpp
TChain *ch = new TChain("upk");
ch->Add("upk_run*.root")
```

## 読み込んだTTreeの数を知りたい（``TChain::GetNtrees``）

```cpp
chain->GetNtrees()
```

## 読み込んだTTreeのリストを取得したい（``GetListOfFiles``）

```cpp
TObjArray *fileElements = fBsd->GetListOfFiles();
TIter next(fileElements);
TChainElement *chEl = 0;
while (( chEl=(TChainElement*)next() )) {
    fprintf(stdout, "[%s]\tListOfFiles\t'%s'\n", __FUNCTION__, chEl->GetTitle() );
}
```

ROOTマニュアルに載ってた
