# テキストファイルをTTreeに変換したい（`TTree::ReadFile`）

```cpp
#include <TTree.h>
#include <TFile.h>
#include <TString.h>

// TTreeオブジェクトを作成
TTree *tree = new TTree("tree", "tree from text file");

// テキストファイルを読み込み
tree->ReadFile("input.csv", "col1/I:col2/I:col3/D", ",");

// ヒストグラムを作成
tree->Draw("col1");
```

`TTree::ReadFile`メソッドで、テキスト形式のファイル（CSV、タブ区切り等）を直接TTreeオブジェクトに読み込むことができます。

```python
from ROOT import TTree, TFile

# TTreeオブジェクトを作成
tree = TTree("tree", "tree from text file")

# テキストファイルを読み込み
tree.ReadFile("input.csv", "col1/I:col2/I:col3/D", ",")

# ヒストグラムを作成
tree.Draw("col1")
```

## メソッドのシグネチャ

```cpp
Long64_t ReadFile(
    const char *filename,
    const char *branchDescriptor,
    char delimiter = ' '
)
```

`TTree::ReadFile`は、テキスト形式のデータファイルをROOTのTTreeオブジェクトに直接読み込む便利なメソッドです。

### 引数の説明

**filename** - 読み込むファイルパス

- テキスト形式のデータファイルを指定します
- 絶対パスまたは相対パスで指定可能です
- 複数ファイルを読み込む場合は`TString`を使って動的に指定することも可能です

**branchDescriptor** - ブランチ構造定義

- ブランチ名と型を指定します
- 複数のブランチは`:`（コロン）で区切ります
- 型は以下の形式で指定します：`branchname/type`

**delimiter** - 区切り文字

- データの区切り文字を指定します
- デフォルトは`" "`（スペース）です
- CSVファイルの場合は`","`を指定します
- タブ区切りの場合は`"\t"`を指定します

### データ型一覧

| 型コード | C++型 | 説明 |
|---------|------|------|
| `I` | `Int_t` | 32ビット整数 |
| `L` | `Long64_t` | 64ビット整数 |
| `F` | `Float_t` | 単精度浮動小数点数（デフォルト） |
| `D` | `Double_t` | 倍精度浮動小数点数 |
| `C` | `Char_t` | 文字 |
| `S` | `Short_t` | 16ビット短整数 |

### 戻り値

- **成功時**: 読み込んだデータ行数（Long64_t）
- **失敗時**: -1

## ファイル形式の要件

`TTree::ReadFile`で読み込むテキストファイルは以下の形式である必要があります。

- **1行目以降がデータ**: 各行が1つのイベントに対応
- **列の順序**: branchDescriptorで指定した順序と一致する必要があります
- **区切り文字**: 指定した区切り文字で各列が分離されている

### サンプルファイル形式

**CSV形式（カンマ区切り）**:

```csv
# コメント行はスキップされます
100,105,104,103,20.5
101,106,103,100,20.7
102,107,105,102,20.9
```

**スペース区切り形式**:

```text
100 105 104 103 20.5
101 106 103 100 20.7
102 107 105 102 20.9
```

**タブ区切り形式**:

```text
100 105 104 103 20.5
101 106 103 100 20.7
102 107 105 102 20.9
```

## 異なるファイル形式を読み込みたい

### CSV形式（カンマ区切り）

```cpp
#include <TTree.h>
#include <TFile.h>

TTree *tree = new TTree("tree", "CSV data");

// CSVファイルを読み込み（4つのInt型列と1つのDouble型列）
Long64_t nentries = tree->ReadFile("data.csv", "ch1/I:ch2/I:ch3/I:ch4/I:temp/D", ",");

std::cout << "読み込んだデータ行数: " << nentries << std::endl;

// データを確認
tree->Draw("ch1");
```

CSVファイルはスプレッドシートソフトで作成・編集しやすいため、実験データの保存に適しています。

### スペース区切り形式

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Space-separated data");

// スペース区切りファイルを読み込み（デフォルト）
Long64_t nentries = tree->ReadFile("data.txt", "x/D:y/D:z/D");

// データの統計情報を表示
tree->Print();
```

スペース区切りはテキストエディターで手動編集しやすく、シンプルなデータ形式です。

### タブ区切り形式

```cpp
#include <TTree.h>

TTree *tree = new TTree("tree", "Tab-separated data");

// タブ区切りファイルを読み込み
Long64_t nentries = tree->ReadFile("data.tsv", "time/D:value/D:error/D", "\t");

tree->Print();
```

タブ区切りはスペースを含むテキストを扱う場合に有効です。

## ROOTファイルに保存したい

```cpp
#include <TTree.h>
#include <TFile.h>
#include <TString.h>

// ファイル名を設定
TString input_filename = "data.csv";
TString output_filename = "output.root";

// TTreeを作成
TTree *tree = new TTree("data", "Data from CSV");

// CSVファイルを読み込み
Long64_t nentries = tree->ReadFile(
    input_filename.Data(),
    "ch1/I:ch2/I:ch3/I:ch4/I:temp/D",
    ","
);

std::cout << "読み込んだイベント数: " << nentries << std::endl;

// ROOTファイルを作成
TFile *outfile = new TFile(
    output_filename.Data(),
    "recreate"
);

// TTreeをファイルに書き込み
tree->Write();

// ファイルを閉じる
outfile->Close();

std::cout << "保存完了: " << output_filename << std::endl;
```

読み込んだTTreeをROOTファイルに保存することで、後の解析を高速化できます。

```python
from ROOT import TTree, TFile

# ファイル名を設定
input_filename = "data.csv"
output_filename = "output.root"

# TTreeを作成
tree = TTree("data", "Data from CSV")

# CSVファイルを読み込み
nentries = tree.ReadFile(
    input_filename,
    "ch1/I:ch2/I:ch3/I:ch4/I:temp/D",
    ","
)

print(f"読み込んだイベント数: {nentries}")

# ROOTファイルを作成
outfile = TFile(output_filename, "recreate")

# TTreeをファイルに書き込み
tree.Write()

# ファイルを閉じる
outfile.Close()

print(f"保存完了: {output_filename}")
```

## 実用例

### シンプルな測定データの変換（C++マクロ）

```cpp
// convert_data.C
#include <TTree.h>
#include <TFile.h>
#include <TString.h>
#include <iostream>

void convert_data() {
    // ステップ1: ファイル名を設定
    TString input_file = "measurement.csv";
    TString output_file = "measurement.root";

    // ステップ2: TTreeを作成
    TTree *tree = new TTree("measurements", "Laboratory measurement data");

    // ステップ3: CSVファイルを読み込み
    // 4つのセンサーからの値と温度を読み込み
    Long64_t nentries = tree->ReadFile(
        input_file.Data(),
        "sensor1/I:sensor2/I:sensor3/I:sensor4/I:temperature/D",
        ","
    );

    if (nentries < 0) {
        std::cout << "ファイルの読み込みに失敗しました" << std::endl;
        return;
    }

    std::cout << "読み込んだデータ: " << nentries << " イベント" << std::endl;

    // ステップ4: データの確認
    tree->Print();

    // ステップ5: ROOTファイルに保存
    TFile *outfile = new TFile(output_file.Data(), "recreate");
    tree->Write();

    // ステップ6: ファイルを閉じる
    outfile->Close();

    std::cout << "完了: " << output_file << std::endl;
}
```

マクロとして実行します。

```console
$ root -l -b -q convert_data.C
```

### 複数ファイルを順次読み込む

```cpp
#include <TTree.h>
#include <TFile.h>
#include <TString.h>
#include <iostream>

void convert_multiple_files() {
    // 読み込むファイルの個数
    const int nfiles = 10;

    // TTreeを作成（複数ファイルのデータを統合）
    TTree *tree = new TTree("data", "Combined data from multiple files");

    Long64_t total_entries = 0;

    // 各ファイルを順次読み込み
    for (int i = 1; i <= nfiles; i++) {
        // ファイル名を動的に生成
        TString filename;
        filename.Form("data_%03d.csv", i);

        std::cout << "読み込み中: " << filename << std::endl;

        // ファイルを読み込み
        Long64_t nentries = tree->ReadFile(
            filename.Data(),
            "time/D:value/D:error/D",
            ","
        );

        if (nentries < 0) {
            std::cout << "  警告: ファイル読み込み失敗" << std::endl;
            continue;
        }

        total_entries += nentries;
        std::cout << "  " << nentries << " イベント読み込み済み" << std::endl;
    }

    std::cout << "合計: " << total_entries << " イベント" << std::endl;

    // ROOTファイルに保存
    TFile *outfile = new TFile("combined_data.root", "recreate");
    tree->Write();
    outfile->Close();
}
```

### データの検証と解析

```cpp
#include <TTree.h>
#include <TFile.h>
#include <TString.h>
#include <iostream>

void analyze_data() {
    // TTreeを作成
    TTree *tree = new TTree("data", "Data analysis");

    // データを読み込み
    Long64_t nentries = tree->ReadFile("sensor_data.csv",
                                       "sensor1/F:sensor2/F:sensor3/F",
                                       ",");

    std::cout << "読み込んだイベント数: " << nentries << std::endl;

    // ブランチの情報を表示
    std::cout << "\nブランチ情報:" << std::endl;
    tree->Print();

    // 統計情報を計算
    std::cout << "\n統計情報:" << std::endl;
    tree->Draw("sensor1");  // ヒストグラムを表示
    tree->Draw("sensor1 >> h1(100, 0, 1000)", "", "HIST");  // カスタムヒストグラム

    // クエリ結果を取得
    tree->Draw("sensor1:sensor2", "sensor3>500", "COLZ");  // 2次元プロット
}
```

## 注意事項

- **コメント行**: `#`で始まる行はスキップされます
- **空行**: 空行はスキップされます
- **型の指定**: 型を指定しない場合はデフォルトの`Float_t`（/F）になります
- **戻り値の確認**: ReadFileの戻り値が−1の場合は読み込み失敗を示すため、エラーチェックが推奨されます
- **大規模ファイル**: 非常に大きなテキストファイルの場合、ROOTファイル形式での保存が推奨されます。テキスト解析より高速にアクセスできます
- **文字エンコーディング**: UTF-8等のマルチバイト文字を含むファイルは読み込みに失敗する可能性があります
- **データ型の一致**: ファイル内のデータ型がbranchDescriptorで指定した型と一致していることを確認してください
- **学生実験での活用**: 実験機器がテキスト形式でデータを出力する場合、このメソッドで素早くROOT解析フォーマットに変換できます

## ワークフロー

1. **データ取得**: 実験機器などからテキスト形式でデータを取得
2. **ファイル保存**: テキストファイルとして保存（CSV推奨）
3. **TTree読み込み**: ReadFileでテキストをTTreeに変換
4. **ROOT形式保存**: TFileに書き込んで保存
5. **解析**: 保存したROOTファイルを後の解析で高速にアクセス

## リファレンス

- [ROOT TTree::ReadFile Documentation](https://root.cern/doc/master/classTTree.html#a5c8f2e1b6f4e3d2c1a0f9e8d7c6b5a4)
- [ROOT TString Documentation](https://root.cern/doc/master/classTString.html)
- [ROOT TFile Documentation](https://root.cern/doc/master/classTFile.html)
