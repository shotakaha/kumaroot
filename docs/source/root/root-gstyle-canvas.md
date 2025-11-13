# キャンバスを設定したい（`gStyle->SetCanvasDef*`）

```cpp
#include <TStyle.h>

// キャンバスのサイズを設定（幅×高さ）
gStyle->SetCanvasDefW(700);  // 幅：700ピクセル
gStyle->SetCanvasDefH(500);  // 高さ：500ピクセル

// キャンバスの表示位置を設定
gStyle->SetCanvasDefX(10);   // X座標：10ピクセル
gStyle->SetCanvasDefY(10);   // Y座標：10ピクセル
```

`gStyle->SetCanvasDefW`、`gStyle->SetCanvasDefH`、`gStyle->SetCanvasDefX`、`gStyle->SetCanvasDefY`メソッドで、
新規に作成されるキャンバスのデフォルトサイズと表示位置を設定できます。

```python
from ROOT import gStyle

# キャンバスのサイズを設定
gStyle.SetCanvasDefW(700)  # 幅：700ピクセル
gStyle.SetCanvasDefH(500)  # 高さ：500ピクセル

# キャンバスの表示位置を設定
gStyle.SetCanvasDefX(10)   # X座標：10ピクセル
gStyle.SetCanvasDefY(10)   # Y座標：10ピクセル
```

## キャンバスのサイズを理解したい

キャンバスのサイズは、グラフやヒストグラムを表示するための領域を決定します。

### メソッドの説明

| メソッド | 説明 | デフォルト値 |
|---------|------|----------|
| `SetCanvasDefW()` | キャンバスの幅（ピクセル） | 700 |
| `SetCanvasDefH()` | キャンバスの高さ（ピクセル） | 500 |
| `SetCanvasDefX()` | キャンバスのX座標（画面左上からのオフセット） | 10 |
| `SetCanvasDefY()` | キャンバスのY座標（画面左上からのオフセット） | 10 |

### キャンバスサイズの選択

- **小さいサイズ（400×300）**: 複数のプロットを並べて表示する場合
- **標準サイズ（700×500）**: 単一のグラフ/ヒストグラム表示に推奨
- **大きいサイズ（1000×800）**: 詳細な解析やプレゼンテーション用

## 異なるキャンバスサイズを使いたい

### 小さいサイズ（4個のプロットを2×2で表示）

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(400);
gStyle->SetCanvasDefH(300);
gStyle->SetCanvasDefX(50);
gStyle->SetCanvasDefY(50);
```

複数のプロットを並べて表示する場合に有効です。

### 標準サイズ（単一プロット用）

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(700);
gStyle->SetCanvasDefH(500);
gStyle->SetCanvasDefX(10);
gStyle->SetCanvasDefY(10);
```

ROOTのデフォルト設定と同じく、単一のグラフ/ヒストグラムの表示に最適です。

### 大きいサイズ（高解像度ディスプレイ用）

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(1000);
gStyle->SetCanvasDefH(800);
gStyle->SetCanvasDefX(100);
gStyle->SetCanvasDefY(100);
```

高解像度ディスプレイや詳細な解析に適しています。

### ワイドフォーマット（16:9比率）

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(960);
gStyle->SetCanvasDefH(540);
gStyle->SetCanvasDefX(10);
gStyle->SetCanvasDefY(10);
```

プレゼンテーション用のワイドスクリーン比率です。

## キャンバスの表示位置を設定したい

キャンバスの表示位置は、ウィンドウがスクリーンのどこに表示されるかを制御します。

```cpp
#include <TStyle.h>

// 画面左上に配置
gStyle->SetCanvasDefX(0);
gStyle->SetCanvasDefY(0);

// 画面中央に配置（フルHDの場合）
gStyle->SetCanvasDefX(640);
gStyle->SetCanvasDefY(360);
```

複数のキャンバスを開く場合は、位置をずらすことで重なりを避けられます。

## 実用例

### 論文用（標準的な大きさ）

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(700);
gStyle->SetCanvasDefH(500);
gStyle->SetCanvasDefX(10);
gStyle->SetCanvasDefY(10);
```

単一のプロットを論文に掲載する場合の標準設定です。

### プレゼンテーション用（大きく見やすく）

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(1000);
gStyle->SetCanvasDefH(750);
gStyle->SetCanvasDefX(50);
gStyle->SetCanvasDefY(50);
```

スクリーンでの表示を想定した大きめのサイズです。

### データ分析用（複数プロット並列表示）

```cpp
#include <TStyle.h>

// 4つのプロットを2×2で表示
gStyle->SetCanvasDefW(500);
gStyle->SetCanvasDefH(400);
gStyle->SetCanvasDefX(10);
gStyle->SetCanvasDefY(10);
```

複数のプロットを比較しながら解析する場合に適しています。

### 高解像度ディスプレイ向け

```cpp
#include <TStyle.h>

gStyle->SetCanvasDefW(1400);
gStyle->SetCanvasDefH(1050);
gStyle->SetCanvasDefX(200);
gStyle->SetCanvasDefY(200);
```

4Kやそれ以上の解像度を持つディスプレイで詳細な表示が可能です。

## 注意事項

- **表示位置の範囲**: キャンバスの表示位置はスクリーンのサイズを超えないよう設定してください
- **複数キャンバス**: 複数のキャンバスを開く場合は、位置をずらして重なりを避けてください
- **既存キャンバスへの影響**: `gStyle` での設定は、その後に作成されるキャンバスに適用されます
- **インタラクティブ設定**: ウィンドウは後からマウスでリサイズ・移動できます

## 現在の設定を確認したい

```cpp
#include <TStyle.h>

int width = gStyle->GetCanvasDefW();
int height = gStyle->GetCanvasDefH();
int x_pos = gStyle->GetCanvasDefX();
int y_pos = gStyle->GetCanvasDefY();
```

`Get*` メソッドで現在の設定値を確認できます。

## リファレンス

- [ROOT TStyle::SetCanvasDefW Documentation](https://root.cern/doc/master/classTStyle.html#a9c3a8e3d8f7b6c5a4e3d2c1b0a9f8e7)
- [ROOT TStyle::SetCanvasDefH Documentation](https://root.cern/doc/master/classTStyle.html#a8b7a6e5f4d3c2b1a0f9e8d7c6b5a4e3)
- [ROOT TStyle::SetCanvasDefX Documentation](https://root.cern/doc/master/classTStyle.html#a7f8e7d6c5b4a3f2e1d0c9b8a7e6f5d4)
- [ROOT TStyle::SetCanvasDefY Documentation](https://root.cern/doc/master/classTStyle.html#a6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1)
