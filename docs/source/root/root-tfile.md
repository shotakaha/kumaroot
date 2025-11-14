# ROOTファイルを操作したい（`TFile`）

```cpp
#include <TFile.h>

TFile *fin = new TFile("input.root", "read");
TH1D *h1 = (TH1D*)fin->Get("histogram_name");
fin->Close();
```

`TFile`はROOTファイル（`.root`）の読み込みと書き込みを行うクラスです。
オブジェクト（ヒストグラム、TTree、キャンバスなど）を保存・復元できます。

```python
import ROOT

fin = ROOT.TFile("input.root", "read")
h1 = fin.Get("histogram_name")
fin.Close()
```

## ファイルを読み込みたい（`TFile`）

```cpp
#include <TFile.h>

TFile *fin = new TFile("input.root", "read");
TH1D *h1 = (TH1D*)fin->Get("h1");
fin->Close();
```

ROOTファイルから名前を指定してオブジェクトを取得します。
キャストして正しい型を指定することが重要です。

```python
import ROOT

fin = ROOT.TFile("input.root", "read")
h1 = fin.Get("h1")
fin.Close()
```

## ファイルに書き込みたい（`TFile`）

```cpp
#include <TFile.h>

TFile *fout = new TFile("output.root", "recreate");
tree->Write();
hist->Write();
canvas->Write();
fout->Close();
```

`TFile`を作成してから、各オブジェクトの`Write()`メソッドを呼び出して保存します。
最後に`Close()`でファイルを閉じます。

```python
import ROOT

fout = ROOT.TFile("output.root", "recreate")
tree.Write()
hist.Write()
canvas.Write()
fout.Close()
```

## ファイルの有無を確認したい（`TFile`）

```cpp
#include <TFile.h>
#include <TSystem.h>

TString ifn = "input.root";
FileStat_t info;

if (gSystem->GetPathInfo(ifn.Data(), info) != 0) {
    printf("File '%s' does not exist.\n", ifn.Data());
} else {
    printf("File exists. Size: %lld bytes\n", info.fSize);
    TFile *fin = new TFile(ifn.Data(), "read");
}
```

`gSystem->GetPathInfo()`を使用してファイルの存在確認とメタ情報取得ができます。
戻り値が0の場合はファイルが存在します。

### FileStat_tの主要な要素

- **fSize** - ファイルサイズ（バイト）
- **fMtime** - 最終変更時刻（Unix timestamp）
- **fIsLink** - シンボリックリンクかどうか（`kTRUE`または`kFALSE`）
- **fDev** - デバイスID
- **fUid** - ユーザID
- **fGid** - グループID

## 複数のファイルに書き込みたい（`TFile`）

```cpp
#include <TFile.h>

TFile *fout1 = new TFile("output1.root", "recreate");
TFile *fout2 = new TFile("output2.root", "recreate");

// fout2が現在のディレクトリ
tree1->Write();  // fout2に書き込まれる

// fout1に切り替え
fout1->cd();
tree2->Write();  // fout1に書き込まれる

fout1->Close();
fout2->Close();
```

複数のTFileを開いている場合、`cd()`メソッドで対象ファイルを切り替えてから`Write()`を実行します。
ROOTの内部にはディレクトリ構造があり、`cd()`でそのディレクトリに移動します。

```python
import ROOT

fout1 = ROOT.TFile("output1.root", "recreate")
fout2 = ROOT.TFile("output2.root", "recreate")

tree1.Write()  # fout2に書き込まれる

fout1.cd()
tree2.Write()  # fout1に書き込まれる

fout1.Close()
fout2.Close()
```

## ファイルの上書き確認をしたい（`TFile`）

```cpp
#include <TFile.h>
#include <TSystem.h>
#include <cstdio>

TString ofn = "output.root";
FileStat_t info;

if (gSystem->GetPathInfo(ofn.Data(), info) == 0) {
    fprintf(stderr, "Error: File '%s' already exists.\n", ofn.Data());
    fprintf(stderr, "Overwrite? [y/n] > ");

    int readch = getchar();
    while (readch != '\n' && readch != EOF) readch = getchar();

    if (readch == 'y' || readch == 'Y') {
        fprintf(stderr, "Overwriting '%s'.\n", ofn.Data());
        TFile *fout = new TFile(ofn.Data(), "recreate");
    } else {
        fprintf(stderr, "Aborted.\n");
        return 1;
    }
} else {
    TFile *fout = new TFile(ofn.Data(), "recreate");
}
```

ファイルがすでに存在する場合、ユーザーに上書き確認を促します。

## メソッドシグネチャ

### TFileのコンストラクター

```cpp
TFile(const char *fname, Option_t *option = "", const char *ftitle = "", Int_t compress = 505)
```

### ファイルアクセスモード

| モード | 説明 |
|-------|------|
| `"read"` または `"r"` | 読み込みモード（ファイルが存在する必要があります） |
| `"update"` または `"u"` | 既存ファイルを更新モード |
| `"recreate"` または `"w"` | 新規作成（既存ファイルは上書き） |
| `"create"` または `"c"` | 新規作成（既存ファイルはエラー） |

### 主要なメソッド

- **`Get(const char *namecycle)`** - 名前を指定してオブジェクトを取得
- **`Write()`** - 現在のディレクトリに含まれるすべてのオブジェクトを書き込み
- **`Close()`** - ファイルを閉じる
- **`cd(const char *path = "")`** - ROOTのディレクトリを変更
- **`cd(Int_t slot)`** - スロット番号を指定してディレクトリを変更
- **`Flush()`** - バッファーをディスクに書き込み（ファイルは開いたまま）

## ファイルパスの指定方法

相対パスと絶対パスが使用できます。

**相対パス**:

```cpp
TFile *f = new TFile("data/input.root", "read");
```

**絶対パス**（推奨）:

```cpp
TFile *f = new TFile("/home/user/data/input.root", "read");
```

**ホームディレクトリの指定（非推奨）**:

```cpp
// ~ はサポートされていません
// 代わりに絶対パスを使用してください
```

## 関連するクラス

- [TTree](./root-ttree.md) - ROOT形式のデータツリー
- [TH1](./root-th1-fill.md) - ヒストグラムクラス
- [TCanvas](./root-tcanvas.md) - 描画キャンバス
- [RDataFrame](./root-rdataframe.md) - 現代的なデータ分析フレームワーク

## 参考資料

- [ROOT::TFile クラスリファレンス](https://root.cern/doc/master/classTFile.html)
- [ROOT ファイルフォーマット](https://root.cern/doc/master/classTFile.html)
- [TSystem クラスリファレンス](https://root.cern/doc/master/classTSystem.html)
