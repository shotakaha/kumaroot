# ファイル操作したい（`TFile`）

```cpp
#include <TFile.h>

TString source_filename = "source.root";
TString source_treename = "events";

TFile* source_file = TFile::Open(source_filename);
if (!source_file || source_file->IsZombie()) {
    std::cerr << "Error opening file: " << source_filename << std::endl;
    return;
}

TTree* source_tree = (TTree*)source_file->Get(source_treename);
source_file->Close();
```

`TFile`はROOTファイルを操作するためのクラスです。
`TFile::Open`は静的メソッドで、ファイルを読み取り専用で開きます。
第一引数にファイル名を指定します。
ファイル名は相対パスや絶対パスで指定できます。
ただし、`~`を使用したホームディレクトリの指定はサポートされていません。
ファイルが正常に開けない場合は、`nullptr`を返すか、`IsZombie()`が`true`になります。

`TFile::Get`で、ファイル内のオブジェクトを名前で取得できます。
`TObject*`型のポインターが返されるため、適切な型にキャストする必要があります。
このサンプルでは`TTree*`型にキャストしています。

`TFile::Close`でファイルを閉じることができます。
マクロや関数のスコープを抜けるとファイルは自動的に閉じられますが、安全のため明示的に閉じる習慣をつけておくとよいです。

```python
import ROOT

# ファイルを開く
source_file = ROOT.TFile.Open("source.root")

# TTreeを取得
source_tree = source_file.Get("events")
source_tree.Print()

# ファイルを閉じる
source_file.Close()
```

## ファイルに保存したい（`TFile`）

```cpp
#include <TFile.h>

TString target_filename = "target.root";

TFile* target_file = new TFile(target_filename, "recreate");

// オブジェクトをファイルに書き込む
tree->Write();
hist->Write();
canvas->Write();

target_file->Close();
```

`TFile`を`recreate`モードで作成してから、各オブジェクトの`Write()`メソッドを呼び出して保存します。
最後に`Close()`でファイルを閉じます。

ファイルに追記する場合は`update`モードを使用します。

## オブジェクトを取得したい（`TFile::Get`）

```cpp
#include <TFile.h>
TFile *fin = new TFile("input.root", "read");
TH1D *h1 = (TH1D*)fin->Get("histogram_name");
fin->Close();
```

`TFile::Get`で、ファイルからオブジェクトを取得できます。
`TObject*`型のポインターが返されるため、適切な型にキャストする必要があります。
このサンプルでは、`TH1D*`型にキャストしています。

:::{note}

`auto`キーワードで型推論に任せることもできますが、
この場合は型指定を明示したほうが安全です。

:::

## ディレクトリを変更したい（`TFile::cd`）

```cpp
#include <TFile.h>
TFile *fout = new TFile("output.root", "recreate");
fout->cd("subdir");  // "subdir"ディレクトリに移動
tree->Write();  // "subdir"に書き込まれる
fout->Close();
```

`TFile::cd`で、ファイル内のディレクトリを変更できます。
ROOTファイルにはディレクトリ構造を持たせることができます。
`cd()`でそのディレクトリに移動してから`Write()`を呼び出すことで、指定したディレクトリにオブジェクトを保存できます。

## 上書き確認したい（`TFile`）

```cpp
#include <TFile.h>
#include <TSystem.h>
#include <cstdio>

TString ofn = "output.root";
FileStat_t info;
if (gSystem->GetPathInfo(ofn, info) == 0) {
    printf("File %s already exists. Do you want to overwrite it? (y/n): ", ofn.Data());
    char response;
    std::cin >> response;
    if (response != 'y' && response != 'Y') {
        printf("Aborting file write.\n");
        return;
    }
}

TFile *fout = new TFile(ofn, "recreate");
// ...オブジェクトの書き込み...
fout->Close();
```

ファイルが存在する場合に、ユーザーに上書き確認を促すサンプルです。
`TSystem::GetPathInfo`でファイルの存在を確認しています。

## イベント取得したい

```cpp
#include <TFile.h>
#include <TTree.h>

// イベント数
// 実際はコマンド引数などで指定できるようにする
Int_t n = 1000;

// 保存するファイルを作成
TFile *fout = new TFile::Open(
    "tree.root",
    "recreate"
);

TTree *tree = new TTree("tree", "Event data");
// TTreeをファイルに関連付ける
tree->SetDirectory(fout);
// 指定したイベント数ごとに自動的にフラッシュ
ttree->SetAutoFlush(10000);

// ブランチを追加
Int_t ch1, ch2, ch3, ch4;
Double_t temp;
tree->Branch("ch1", &ch1, "ch1/I");
tree->Branch("ch2", &ch2, "ch2/I");
tree->Branch("ch3", &ch3, "ch3/I");
tree->Branch("ch4", &ch4, "ch4/I");
tree->Branch("temp", &temp, "temp/D");

for (Int_t i = 0; i < n; i++) {
    // データ取得
    ch1 = ...;  // チャンネル1の値
    ch2 = ...;  // チャンネル2の値
    ch3 = ...;  // チャンネル3の値
    ch4 = ...;  // チャンネル4の値
    temp = ...; // 温度の値

    // イベントをTTreeに保存
    tree->Fill();

    // 定期的に自動保存
    if (i % 10000 == 0) {
        tree->AutoSave("SaveSelf");        printf("Saved %d events...\n", i);
    }

}

// 最終的にファイルに書き込む
tree->Write();

// ファイルを閉じる
fout->Close();
```

`TFile`と`TTree`を組み合わせて、実験データをROOT形式で保存できます。
`TFile`でファイルを開いて、`TTree`にイベントデータを保存するのが一般的な使い方です。

`TTree::SetAutoFlush`で、指定したイベント数ごとに自動的にファイルにフラッシュするように設定できます。
これにより、大量のイベントを保存する際のメモリ使用量を抑えることができます。

`TTree::AutoSave`で、定期的にファイルに保存できます。
DAQが途中でクラッシュした場合でも、保存されたデータを復旧することができるようになります。

:::{caution}

`TTree:Write`は、ファイルに書き込む際にTTreeの内容を完全に保存します。
イベントごとに呼び出してはいけません。
イベント数が多い場合は、`AutoSave`や`AutoFlush`を活用して、定期的にファイルに書き出すようにします。

:::

## リファレンス

- [TFile - ROOT Documentation](https://root.cern/doc/master/classTFile.html)
- [TSystem - ROOT Documentation](https://root.cern/doc/master/classTSystem.html)
