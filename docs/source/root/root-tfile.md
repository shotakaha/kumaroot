# ファイル操作したい（`TFile`）

```cpp
#include <TFile.h>

// ファイルを開く
TFile *fin = new TFile(
    "input.root",  // fname
    "read",        // option: read | update | recreate | create
    "Input ROOT file",  // ftitle (optional)
    505            // compress (optional)
);

// オブジェクトを取得
TH1D *h1 = (TH1D*)fin->Get("histogram_name");

// ファイルを閉じる
fin->Close();
```

`TFile`クラスで、ROOTファイルの読み書きができます。
ファイルを開いてオブジェクトを取得し、最後にファイルを閉じるのが基本的な流れです。

`fname`はファイル名を指定します。
ファイル名は相対パスや絶対パスで指定できます。
ただし、`~`を使用したホームディレクトリの指定はサポートされていません。

`option`はファイルアクセスモードを指定します。
読み込み専用（`read` / `r`）、
更新・追記（`update` / `u`）、
新規作成（存在する場合はエラー）（`create` / `c`）
新規作成（存在する場合は上書き）（`recreate`）
のいずれかを指定します。
デフォルトは`read`です。

`ftitle`はファイルのタイトル説明を設定できます。
`compress`は圧縮レベルを指定できます。デフォルトは505です。

```python
import ROOT

# ファイルを開く
fin = ROOT.TFile("input.root", "read")

# オブジェクトを取得
h1 = fin.Get("histogram_name")

# ファイルを閉じる
fin.Close()
```

## ファイルに保存したい（`TFile`）

```cpp
#include <TFile.h>

TFile *fout = new TFile(
    "output.root",
    "recreate"
);

// オブジェクトをファイルに書き込む
tree->Write();
hist->Write();
canvas->Write();

fout->Close();
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
オブジェクトの名前を指定して、正しい型にキャストすることが重要です。

:::{note}

`auto`を使用して型推論することもできますが、明示的な型指定の方が安全です。

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

## リファレンス

- [TFile - ROOT Documentation](https://root.cern/doc/master/classTFile.html)
- [TSystem - ROOT Documentation](https://root.cern/doc/master/classTSystem.html)
