# グラフィックススタイルを設定したい（`gROOT->SetStyle`）

```cpp
#include <TROOT.h>
#include <TStyle.h>

// デフォルトのプレーンスタイル（推奨）
gROOT->SetStyle("Plain");

// キャンバスのスタイルを適用
gROOT->ForceStyle();
```

`gROOT->SetStyle`メソッドで、ROOTの全体的なグラフィックススタイルを設定できます。
後に作成されるオブジェクトに自動的に適用されます。

```python
from ROOT import gROOT

# デフォルトのプレーンスタイル（推奨）
gROOT.SetStyle("Plain")

# キャンバスのスタイルを適用
gROOT.ForceStyle()
```

## ROOTのスタイルを理解したい

ROOTには複数の組み込みスタイルが提供されています。

### 利用可能なスタイル

| スタイル名 | 説明 | 背景色 | 用途 |
|-----------|------|------|------|
| `Plain` | シンプルで見やすい（デフォルト推奨） | 白 | 論文、プレゼンテーション、標準 |
| `Classic` | 古いROOTスタイル | 灰色 | 互換性が必要な場合のみ |
| `Modern` | モダンで洗練 | 白 | プレゼンテーション向け |
| `ATLAS` | ATLAS実験用 | 白 | 高エネルギー物理学向け |
| `CMS` | CMS実験用 | 白 | 高エネルギー物理学向け |
| `ROOT` | ROOT標準 | 灰色 | 古いバージョン互換 |

## 異なるスタイルを使いたい

### プレーンスタイル（推奨）

```cpp
#include <TROOT.h>

gROOT->SetStyle("Plain");
gROOT->ForceStyle();
```

シンプルで見やすく、論文やプレゼンテーションに最適です。
ROOT v5.30以降のデフォルト設定です。

### クラシックスタイル（互換性用）

```cpp
#include <TROOT.h>

gROOT->SetStyle("Classic");
gROOT->ForceStyle();
```

ROOT v5.30以前のスタイルです。
古いコードとの互換性が必要な場合のみ使用してください。

### モダンスタイル（プレゼンテーション向け）

```cpp
#include <TROOT.h>

gROOT->SetStyle("Modern");
gROOT->ForceStyle();
```

モダンで洗練された見た目です。
スクリーン表示やプレゼンテーション向けです。

### ATLAS実験スタイル

```cpp
#include <TROOT.h>

gROOT->SetStyle("ATLAS");
gROOT->ForceStyle();
```

ATLASコラボレーション推奨のスタイルです。
高エネルギー物理学の論文に適しています。

### CMS実験スタイル

```cpp
#include <TROOT.h>

gROOT->SetStyle("CMS");
gROOT->ForceStyle();
```

CMSコラボレーション推奨のスタイルです。
高エネルギー物理学の論文に適しています。

## スタイルを設定したい

### 基本的な設定方法

```cpp
#include <TROOT.h>

// スタイルを選択
gROOT->SetStyle("Plain");

// 現在のスタイルに設定を反映
gROOT->ForceStyle();
```

`SetStyle`で選択したスタイルは、その後に作成されるオブジェクトに自動的に適用されます。
既存のオブジェクトには`ForceStyle()`を使用して適用します。

### 複数のグラフをスタイル統一したい場合

```cpp
#include <TROOT.h>
#include <TGraph.h>
#include <TH1F.h>

// スタイルをスクリプト開始時に設定
gROOT->SetStyle("Plain");

// その後に作成するすべてのグラフに自動適用
TGraph *graph1 = new TGraph();
TH1F *hist1 = new TH1F("hist1", "Histogram 1", 100, 0, 10);

TGraph *graph2 = new TGraph();
TH1F *hist2 = new TH1F("hist2", "Histogram 2", 100, 0, 10);
```

複数のグラフ/ヒストグラムを作成する場合は、スクリプト開始時に`SetStyle`を呼ぶことで、すべてのオブジェクトに統一されたスタイルが適用されます。

## 利用可能なスタイル一覧を確認したい

```cpp
#include <TROOT.h>
#include <iostream>

// 利用可能なスタイル一覧を表示
std::cout << "Available styles:" << std::endl;
std::cout << "- Plain" << std::endl;
std::cout << "- Classic" << std::endl;
std::cout << "- Modern" << std::endl;
std::cout << "- ATLAS" << std::endl;
std::cout << "- CMS" << std::endl;
```

組み込みスタイルは上記の5種類が基本です。
システムやROOT設定によって追加スタイルが利用できる場合もあります。

## 実用例

### 論文用（標準的な設定）

```cpp
#include <TROOT.h>
#include <TStyle.h>

gROOT->SetStyle("Plain");
gROOT->ForceStyle();

// その他の細かい設定も可能
gStyle->SetOptStat(111110);      // 統計情報を表示
gStyle->SetOptFit(1111);         // フィット結果を表示
gStyle->SetPadGridy(1);          // Y軸補助線表示
```

論文掲載用には`Plain`スタイルが標準です。

### プレゼンテーション用（見やすく）

```cpp
#include <TROOT.h>
#include <TStyle.h>

gROOT->SetStyle("Modern");
gROOT->ForceStyle();

// さらに見やすくするための設定
gStyle->SetHistLineWidth(2);
gStyle->SetHistLineColor(2);      // 赤色
gStyle->SetOptStat(0);            // 統計情報非表示
```

プレゼンテーションではモダンスタイルで、見やすさを重視します。

### 高エネルギー物理学向け

```cpp
#include <TROOT.h>
#include <TStyle.h>

// ATLASまたはCMS実験規約に従う
gROOT->SetStyle("ATLAS");
gROOT->ForceStyle();

gStyle->SetOptStat(111110);
gStyle->SetOptFit(111);
```

国際学会投稿時の標準です。

### 古いコードとの互換性確保

```cpp
#include <TROOT.h>

// 古いバージョンのスタイルを使用
gROOT->SetStyle("Classic");
gROOT->ForceStyle();
```

レガシーコードとの互換性が必要な場合のみ使用します。

## 注意事項

- **タイミング**: `SetStyle`はスクリプト開始時に呼ぶことが重要です。呼び出し後に作成されるオブジェクトにのみ適用されます

- **既存オブジェクトへの適用**: すでに作成されたオブジェクトに適用する場合は`ForceStyle()`を使用してください

- **ROOT v5.30以降**: v5.30以降はデフォルトが`Plain`スタイルなので、明示的に呼び出す必要がありません

- **カスタムスタイル**: 組み込みスタイルをベースにカスタマイズすることも可能です（`TStyle`クラスのメソッドを使用）

- **ATLAS/CMSスタイル**: これらは実験グループの推奨設定です。所属実験の規約にしたがってください

## SetStyle() vs ForceStyle()

| メソッド | 説明 | タイミング |
|---------|------|----------|
| `SetStyle()` | スタイルを選択 | スクリプト開始時 |
| `ForceStyle()` | 現在のスタイルをすべてのオブジェクトに適用 | 既存オブジェクトに適用する場合 |

## リファレンス

- [ROOT gROOT::SetStyle Documentation](https://root.cern/doc/master/classTROOT.html#a0e0fe6d5f0e8c3d5b4a7e9f2d1c3e5a7)
- [ROOT TStyle Documentation](https://root.cern/doc/master/classTStyle.html)
- [ROOT Style Examples](https://root.cern/doc/master/group__Styles.html)
