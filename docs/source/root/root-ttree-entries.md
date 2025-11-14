# イベント数を取得したい（`TTree::GetEntries`）

```cpp
#include <TTree.h>
#include <iostream>

// TTreeを開く
TTree *tree = (TTree *)file->Get("tree");

// エントリー数を取得
Long64_t nentries = tree->GetEntries();

std::cout << "エントリー数: " << nentries << std::endl;
```

`TTree::GetEntries`メソッドで、TTreeに格納されているエントリー（イベント）の総数を取得できます。
エントリー数はデータ解析に必要な基本情報で、ループ処理やプログレス表示に重要です。

```python
from ROOT import TFile, TTree

# ROOTファイルを開く
file = TFile("data.root")

# TTreeを取得
tree = file.Get("tree")

# エントリー数を取得
nentries = tree.GetEntries()

print(f"エントリー数: {nentries}")
```

## メソッドシグネチャ

```cpp
Long64_t GetEntries() const;
Long64_t GetEntries(const char *selection);
```

`TTree::GetEntries`は、TTreeに含まれるデータのエントリー数を返すメソッドです。
エントリーはTTreeの最小データ単位で、通常は1つのイベントに対応します。

### 引数の説明

**selection** - フィルター条件（オプション）

- セレクション文字列を指定することで、条件に合致するエントリー数のみを取得できます
- ROOTの`TCut`や`TEntryList`で指定できる条件構文が使用可能です
- 指定しない場合は全エントリー数が返されます

### 戻り値

- **Long64_t**: エントリー数（64ビット長整数）
- セレクション引数なしの場合：全エントリー数
- セレクション引数あり：条件に合致するエントリー数

## エントリーとは

**エントリー** - TTreeの最小データ単位

- 1行のデータに対応
- 通常は1つの物理イベントを表現
- ブランチの葉（リーフ）に格納される値の集合

## TTreeの階層構造

```text
TTree（木）
├── Branch1（枝）
│   ├── Leaf1（葉）
│   └── Leaf2（葉）
├── Branch2（枝）
│   └── Leaf3（葉）
└── エントリー1, 2, 3, ... N
```

各エントリーは、すべてのブランチに1つずつデータを保持します。

## エントリー数を取得したい

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void get_entries_basic() {
    // ROOTファイルを開く
    TFile *file = TFile::Open("data.root");

    // TTreeを取得
    TTree *tree = (TTree *)file->Get("mytree");

    // エントリー数を取得
    Long64_t nentries = tree->GetEntries();

    std::cout << "全エントリー数: " << nentries << std::endl;

    file->Close();
}
```

シンプルな用法で、TTreeの全エントリー数を取得できます。

```python
from ROOT import TFile

# ROOTファイルを開く
file = TFile("data.root")

# TTreeを取得
tree = file.Get("mytree")

# エントリー数を取得
nentries = tree.GetEntries()

print(f"全エントリー数: {nentries}")

file.Close()
```

## 単純な条件での取得

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void count_entries_with_selection() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    // 条件に合致するエントリー数を取得
    // x > 100 の条件を満たすエントリーの数
    Long64_t n_selected = tree->GetEntries("x > 100");

    std::cout << "x > 100 を満たすエントリー数: " << n_selected << std::endl;
    std::cout << "全エントリー数: " << tree->GetEntries() << std::endl;

    file->Close();
}
```

## 複合条件での取得

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void count_with_complex_selection() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    // 複数条件を AND / OR で組み合わせ
    Long64_t n_selected = tree->GetEntries("x > 100 && y < 50");

    std::cout << "(x > 100) AND (y < 50): " << n_selected << " entries" << std::endl;

    // OR 条件
    Long64_t n_or = tree->GetEntries("x < 0 || y > 200");

    std::cout << "(x < 0) OR (y > 200): " << n_or << " entries" << std::endl;

    file->Close();
}
```

### Python でセレクション条件を使用

```python
from ROOT import TFile

file = TFile("data.root")
tree = file.Get("tree")

# 単純条件
n_selected = tree.GetEntries("x > 100")
print(f"x > 100 のエントリー数: {n_selected}")

# 複合条件
n_and = tree.GetEntries("x > 100 && y < 50")
print(f"(x > 100) AND (y < 50): {n_and}")

n_or = tree.GetEntries("x < 0 || y > 200")
print(f"(x < 0) OR (y > 200): {n_or}")

file.Close()
```

## ループ処理したい

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void loop_over_entries() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    // エントリー数を取得
    Long64_t nentries = tree->GetEntries();

    // ブランチを設定
    Float_t x, y;
    tree->SetBranchAddress("x", &x);
    tree->SetBranchAddress("y", &y);

    // すべてのエントリーをループ
    for (Long64_t i = 0; i < nentries; i++) {
        tree->GetEntry(i);

        // ここでデータ処理
        if (x > 100) {
            std::cout << "Entry " << i << ": x=" << x << ", y=" << y << std::endl;
        }
    }

    file->Close();
}
```

データ解析の基本となるエントリーループで、GetEntriesを活用します。

## プログレス表示付きループ

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>
#include <cmath>

void loop_with_progress() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    Long64_t nentries = tree->GetEntries();

    Float_t x;
    tree->SetBranchAddress("x", &x);

    // プログレス表示用の間隔
    Long64_t progress_step = std::max(1LL, nentries / 100);

    std::cout << "処理開始: " << nentries << " エントリー" << std::endl;

    for (Long64_t i = 0; i < nentries; i++) {
        tree->GetEntry(i);

        // データ処理
        // ...

        // プログレス表示（100回に1回、または最後）
        if (i % progress_step == 0 || i == nentries - 1) {
            int percent = (100 * (i + 1)) / nentries;
            std::cout << "\r進捗: " << percent << "% (" << (i + 1)
                      << "/" << nentries << ")" << std::flush;
        }
    }

    std::cout << "\n処理完了" << std::endl;
    file->Close();
}
```

### Python でのエントリーループ

```python
from ROOT import TFile

file = TFile("data.root")
tree = file.Get("tree")

nentries = tree.GetEntries()

# ブランチを設定
x_val = 0
y_val = 0
tree.SetBranchAddress("x", x_val)
tree.SetBranchAddress("y", y_val)

print(f"処理開始: {nentries} エントリー")

for i in range(nentries):
    tree.GetEntry(i)

    # ここでデータ処理
    if x_val > 100:
        print(f"Entry {i}: x={x_val}, y={y_val}")

    # プログレス表示
    if (i + 1) % 1000 == 0:
        print(f"進捗: {i + 1}/{nentries}")

print("処理完了")
file.Close()
```

## エントリー数の統計情報を取得したい

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void tree_statistics() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    // 基本統計
    Long64_t total_entries = tree->GetEntries();
    Long64_t loaded_entries = tree->GetLoadedEntries();

    std::cout << "全エントリー数: " << total_entries << std::endl;
    std::cout << "ロード済みエントリー数: " << loaded_entries << std::endl;

    // セレクション条件によるカウント
    Long64_t selected_entries = tree->GetEntries("quality > 0.8");

    std::cout << "品質良好なエントリー: " << selected_entries << std::endl;
    std::cout << "品質不良なエントリー: " << (total_entries - selected_entries) << std::endl;

    // 割合を計算
    double percent = (100.0 * selected_entries) / total_entries;
    std::cout << "品質良好な割合: " << percent << "%" << std::endl;

    // ブランチごとの情報
    TIter next(tree->GetListOfBranches());
    TBranch *branch;
    while ((branch = (TBranch *)next())) {
        std::cout << "ブランチ: " << branch->GetName()
                  << ", 最大エントリー: " << branch->GetEntries() << std::endl;
    }

    file->Close();
}
```

## メモリ効率的にエントリー数を確認したい

大規模ファイルでは、メモリを効率的に使用することが重要です。

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void efficient_entry_count() {
    // ファイルをREADモードで開く
    TFile *file = TFile::Open("large_data.root", "READ");

    // TTreeを取得（データはまだロードされていない）
    TTree *tree = (TTree *)file->Get("tree");

    // エントリー数を取得（メモリをほとんど使わない）
    Long64_t nentries = tree->GetEntries();

    std::cout << "エントリー数: " << nentries << std::endl;
    std::cout << "メモリ使用量: " << tree->GetTotBytes() / (1024.0 * 1024.0)
              << " MB" << std::endl;
    std::cout << "圧縮率: " << (100.0 * tree->GetZipBytes()) / tree->GetTotBytes()
              << "%" << std::endl;

    file->Close();
}
```

## 実用例

### 複数ファイルのエントリー数を集計

```cpp
#include <TFile.h>
#include <TTree.h>
#include <TString.h>
#include <iostream>

void count_multiple_files() {
    const int nfiles = 10;
    Long64_t total_entries = 0;

    for (int i = 0; i < nfiles; i++) {
        TString filename;
        filename.Form("data_%03d.root", i);

        TFile *file = TFile::Open(filename.Data());
        if (!file || file->IsZombie()) {
            std::cerr << "ファイルを開けません: " << filename << std::endl;
            continue;
        }

        TTree *tree = (TTree *)file->Get("tree");
        if (!tree) {
            std::cerr << "TTreeが見つかりません: " << filename << std::endl;
            file->Close();
            continue;
        }

        Long64_t entries = tree->GetEntries();
        std::cout << filename << ": " << entries << " エントリー" << std::endl;

        total_entries += entries;
        file->Close();
    }

    std::cout << "\n合計: " << total_entries << " エントリー" << std::endl;
}
```

### エントリー数に基づくデータ分割

```cpp
#include <TFile.h>
#include <TTree.h>
#include <iostream>

void split_data_by_entries() {
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("tree");

    Long64_t nentries = tree->GetEntries();
    Long64_t chunk_size = 10000;

    // データを複数のチャンクに分割
    Long64_t nchunks = (nentries + chunk_size - 1) / chunk_size;

    std::cout << "全エントリー数: " << nentries << std::endl;
    std::cout << "チャンクサイズ: " << chunk_size << std::endl;
    std::cout << "チャンク数: " << nchunks << std::endl;

    for (Long64_t chunk = 0; chunk < nchunks; chunk++) {
        Long64_t start = chunk * chunk_size;
        Long64_t end = (chunk + 1) * chunk_size;
        if (end > nentries) end = nentries;

        std::cout << "チャンク " << chunk << ": " << start << " - " << (end - 1)
                  << " (" << (end - start) << " エントリー)" << std::endl;
    }

    file->Close();
}
```

## 注意事項

- **長整数型**: GetEntriesは`Long64_t`（64ビット長整数）を返します。大規模なTTreeに対応しているため、通常の`int`型では値が溢れる可能性があります

- **セレクション処理時間**: セレクション条件付きGetEntriesは全エントリーをスキャンするため、大規模TTreeでは時間がかかる可能性があります

- **キャッシング**: `GetLoadedEntries()`はメモリにロードされたエントリー数を返すため、ファイルから読み込まれたエントリー数と異なる場合があります

- **ブランチの非同期化**: マルティプル・バリエーション・キーによって一部のブランチが同期していない場合があります

- **エントリーサイズの確認**: 各エントリーのメモリサイズは`GetTotBytes()`で確認できます

## リファレンス

- [ROOT TTree::GetEntries Documentation](https://root.cern/doc/master/classTTree.html#a7c15435dc3d3e5626a1d8f20a5b2d78)
- [ROOT TTree Documentation](https://root.cern/doc/master/classTTree.html)
- [ROOT TFile Documentation](https://root.cern/doc/master/classTFile.html)
