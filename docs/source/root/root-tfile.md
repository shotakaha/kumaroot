# ファイル操作したい（`TFile`）

```cpp
#include <TFile.h>

TFile* f = TFile::Open("source.root");
if (!f || f->IsZombie()) {
    std::cerr << "Error opening file: " << "source.root" << std::endl;
    return;
}

TTree* tree = (TTree*)f->Get("events");
f->Close();
```

`TFile`はROOTファイルを操作するためのクラスです。
`TFile::Open`は静的メソッドで、ファイルを読み取り専用で開きます。
`TFile`の`read`モードに相当します。

第一引数にはファイル名を指定します。
ファイル名は相対パスや絶対パスで指定できまが、
`~`を使用したホームディレクトリの指定はサポートされていません。
ファイルが正常に開けない場合は、`nullptr`を返すか、`IsZombie()`が`true`になります。

`TFile::Get`で、ファイル内のオブジェクトを名前で取得できます。
`TObject*`型のポインターが返されるため、適切な型にキャストする必要があります。
このサンプルでは`TTree*`型にキャストしています。

`TFile::Close`でファイルを閉じることができます。
マクロや関数のスコープを抜けるとファイルは自動的に閉じられますが、安全のため明示的に閉じる習慣をつけておくとよいです。

```python
import ROOT

# ファイルを開く
f = ROOT.TFile.Open("source.root")

# TTreeを取得
tree = f.Get("events")
tree.Print()

# ファイルを閉じる
f.Close()
```

## ファイルを作成したい（`TFile`）

```cpp
TFile* f = new TFile("output.root", "recreate");
if (!f || f->IsZombie()) {
    std::cerr << "Error creating file: output.root" << std::endl;
    return;
}
```

`recreate`モードを指定してファイルを新規作成できます。
同名のファイルが存在する場合は上書きされます。

## ファイルを上書き防止したい（`TFile`）

```cpp
TFile *f = new TFile("output.root", "create");
if (!f || f->IsZombie()) {
    std::cerr << "Error: File already exists. Use 'recreate' mode to overwrite." << std::endl;
    return;
}
```

`create`もしくは`new`モードを指定してファイルを作成できます。
同名のファイルが存在する場合はエラーになります。

## ファイルを追記したい（`TFile`）

```cpp
TFile* f = new TFile("output.root", "update");
if (!f || f->IsZombie()) {
    std::cerr << "Error opening file for update: output.root" << std::endl;
    return;
}
```

`update`モードを指定してファイルを開くと、既存のファイルに追記できます。
ファイルが存在しない場合は新規作成されます。

## 上書き確認したい（`TFile`）

```cpp
#include <TFile.h>
#include <filesystem>
#include <iostream>

std::string filename = "output.root";
if (std::filesystem::exists(filename)) {
    std::cout << "File " << filename << " already exists. Do you want to overwrite it? (y/n): ";
    char response;
    std::cin >> response;
    if (response != 'y' && response != 'Y') {
        std::cerr << "Aborted." << std::endl;
        return;
    }
}

TFile* f = new TFile(filename.c_str(), "recreate");
```

ファイルを作成するときに、同名のファイルが存在した場合にユーザーに上書き確認するサンプルです。
C++17以降の`std::filesystem`を使用して、ファイルの存在を確認しています。
ユーザーが上書きを拒否した場合は、処理を中断します。

:::{note}
`FileStat_t`と`TSystem::GetPathInfo`を使ってファイルの存在を確認する方法もありますが、C++17以降は`std::filesystem`を使う方が簡単なようです。
:::

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
