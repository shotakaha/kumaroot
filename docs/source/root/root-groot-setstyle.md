# グラフィックススタイルを設定したい（`TROOT::SetStyle`）

```cpp
#include <TROOT.h>
#include <TStyle.h>

// デフォルトのプレーンスタイル（推奨）
gROOT->SetStyle("Plain");

// キャンバスのスタイルを適用
gROOT->ForceStyle();
```

`gROOT->SetStyle`で、ROOTの全体的なグラフィックススタイルを変更できます。
デフォルトは`"Plain"`です。

```python
from ROOT import gROOT

# デフォルトのプレーンスタイル（推奨）
gROOT.SetStyle("Plain")

# キャンバスのスタイルを適用
gROOT.ForceStyle()
```

## 組み込みスタイルを一覧したい（`TROOT::GetListOfStyles`）

```cpp
gROOT->GetListOfStyles()->Print();
// Collection name='Styles', class='TList', size=9
// OBJ: TStyle	Plain	Plain Style (no colors/fill areas)
// OBJ: TStyle	Bold	Bold Style
// OBJ: TStyle	Video	Style for video presentation histograms
// OBJ: TStyle	Pub	Style for Publications
// OBJ: TStyle	Classic	Classic Style
// OBJ: TStyle	Default	Equivalent to Classic
// OBJ: TStyle	Modern	Modern Style
// OBJ: TStyle	ATLAS	ATLAS Style
// OBJ: TStyle	BELLE2	Belle II Style
```

`gROOT->GetListOfStyles()`で、利用可能な組み込みスタイルの一覧を確認できます。

| スタイル名 | 背景色 | 説明 |
| --- | --- | --- |
| `Default` | 灰色 | `Classic`に相当 |
| `Classic` | 灰色 | 古いROOTスタイル |
| `Modern` | 白 | モダンで洗練されたスタイル |
| `Plain` | 白 | シンプルで見やすい（推奨） |
| `Video` | 灰色 | ビデオプレゼンテーション用スタイル |
| `Pub` | 灰色 | 論文用スタイル |
| `Bold` | 灰色 | 太字スタイル |
| `ATLAS` | 白 | ATLAS実験用スタイル |
| `BELLE2` | 白 | Belle II実験用スタイル |

`Plain`は、パッドの背景が白色で、シンプルで見やすいスタイルです。
ROOT v5.30以降のデフォルト設定です。
個人利用であればデフォルトの`Plain`スタイルで十分です。
`ATLAS`と`BELLE2`は、白黒にしたい場合に使うとよいかもしれません。

`Default`や`Classic`は、パッドの背景が灰色のスタイルです。
ROOT v5.30以前の古いスタイルなので、現在は使う理由はありません。
また、`Video`や`Pub`、`Bold`などは、
説明にあるような用途に最適化されたスタイルとは言い難いです。
こちらも、わざわざ使う必要はないと思います。

## リファレンス

- [ROOT gROOT::SetStyle Documentation](https://root.cern/doc/master/classTROOT.html#a0e0fe6d5f0e8c3d5b4a7e9f2d1c3e5a7)
- [ROOT TStyle Documentation](https://root.cern/doc/master/classTStyle.html)
- [ROOT Style Examples](https://root.cern/doc/master/group__Styles.html)
