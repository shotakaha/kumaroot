# フォントしたい（`gStyle->SetTextFont` / `SetTitleFont` / `SetLabelFont` など）

```cpp
#include <TStyle.h>

// グラフのテキストフォント
gStyle->SetTextFont(62);

// グラフタイトルのフォント
gStyle->SetTitleFont(62, "xyz");

// 軸ラベルのフォント
gStyle->SetLabelFont(62, "xyz");

// 凡例のフォント
gStyle->SetLegendFont(62);

// 統計情報のフォント
gStyle->SetStatFont(62);
```

`SetXXXFont`メソッドで、グラフやヒストグラムのさまざまな要素のフォントを変更できます。

```python
from ROOT import gStyle

# グラフのテキストフォント
gStyle.SetTextFont(62)

# グラフタイトルのフォント
gStyle.SetTitleFont(62, "xyz")

# 軸ラベルのフォント
gStyle.SetLabelFont(62, "xyz")

# 凡例のフォント
gStyle.SetLegendFont(62)

# 統計情報のフォント
gStyle.SetStatFont(62)
```

## フォントコードを理解したい

ROOTのフォントは、フォントIDと精度（Precision）の組み合わせで指定されます。

### フォントコードの計算

```text
フォントコード = 10 × フォントID + 精度
```

**計算例**：

- フォントID=6、精度=2 → 10 × 6 + 2 = 62
- フォントID=1、精度=2 → 10 × 1 + 2 = 12
- フォントID=2、精度=1 → 10 × 2 + 1 = 21

### フォント ID の種類

| ID | X11フォント名 | TrueType | イタリック | 太さ |
|----|----|--------|--------|-----|
| 1 | times-medium-i-normal | Times New Roman | Yes | 4 |
| 2 | times-bold-r-normal | Times New Roman | No | 7 |
| 3 | times-bold-i-normal | Times New Roman | Yes | 7 |
| 4 | helvetica-medium-r-normal | Arial | No | 4 |
| 5 | helvetica-medium-o-normal | Arial | Yes | 4 |
| 6 | helvetica-bold-r-normal | Arial | No | 7 |
| 7 | helvetica-bold-o-normal | Arial | Yes | 7 |
| 8 | courier-medium-r-normal | Courier New | No | 4 |
| 9 | courier-medium-o-normal | Courier New | Yes | 4 |
| 10 | courier-bold-r-normal | Courier New | No | 7 |
| 11 | courier-bold-o-normal | Courier New | Yes | 7 |
| 12 | symbol-medium-r-normal | Symbol | No | 6 |
| 13 | times-medium-r-normal | Times New Roman | No | 4 |
| 14 | （カスタム） | Wingdings | No | 4 |

### 精度（Precision）の種類

| 精度値 | 説明 | 用途 |
|------|------|------|
| 0 | PDFの不精確なビットマップフォント | 古いシステム向け |
| 1 | ベクトルフォント（PostScript） | 高品質印刷 |
| 2 | TrueTypeフォント（デフォルト） | 汎用・標準 |

## 異なるフォント設定を使いたい

### ヘルベチカ系（Arial相当）を使用

```cpp
#include <TStyle.h>

// ID=6（Helvetica Bold）、精度=2（TrueType）
gStyle->SetTextFont(62);
gStyle->SetTitleFont(62, "xyz");
gStyle->SetLabelFont(62, "xyz");
gStyle->SetLegendFont(62);
gStyle->SetStatFont(62);
```

一般的で読みやすいフォントです。プレゼンテーションや論文に推奨されます。

### タイムズ系（Times New Roman相当）を使用

```cpp
#include <TStyle.h>

// ID=13（Times Medium）、精度=2（TrueType）
gStyle->SetTextFont(132);
gStyle->SetTitleFont(132, "xyz");
gStyle->SetLabelFont(132, "xyz");
gStyle->SetLegendFont(132);
gStyle->SetStatFont(132);
```

格調高く見えるフォントです。学位論文や学術論文に適しています。

### クーリエ系（Courier New相当）を使用

```cpp
#include <TStyle.h>

// ID=8（Courier Medium）、精度=2（TrueType）
gStyle->SetTextFont(82);
gStyle->SetTitleFont(82, "xyz");
gStyle->SetLabelFont(82, "xyz");
gStyle->SetLegendFont(82);
gStyle->SetStatFont(82);
```

等幅フォントで、コードやプログラム出力の表示に適しています。

### 太いヘルベチカ（強調用）

```cpp
#include <TStyle.h>

// ID=6（Helvetica Bold）、精度=1（PostScript）
gStyle->SetTextFont(61);
gStyle->SetTitleFont(61, "xyz");
```

より目立つフォントが必要な場合に使用します。

## 各要素のフォントを個別に設定したい

```cpp
#include <TStyle.h>

// タイトル：太いヘルベチカ
gStyle->SetTitleFont(62, "xyz");

// 軸ラベル：通常ヘルベチカ
gStyle->SetLabelFont(42, "xyz");

// 統計情報：小さいヘルベチカ
gStyle->SetStatFont(42);

// 凡例：通常ヘルベチカ
gStyle->SetLegendFont(42);

// テキスト（デフォルト）：太いヘルベチカ
gStyle->SetTextFont(62);
```

各要素で異なるフォントを使用する場合の設定例です。

## フォント設定の確認をしたい

```cpp
#include <TStyle.h>

int text_font = gStyle->GetTextFont();
int title_font = gStyle->GetTitleFont();
int label_font = gStyle->GetLabelFont();
int legend_font = gStyle->GetLegendFont();
int stat_font = gStyle->GetStatFont();

// フォント ID と精度を計算
int font_id = text_font / 10;
int precision = text_font % 10;
```

`Get*Font()`メソッドで現在のフォント設定を確認できます。
フォントIDと精度を計算して分析することも可能です。

## 実用例

### 論文用（格調高く）

```cpp
#include <TStyle.h>

// Times フォント（精度2 = TrueType）で統一
gStyle->SetTextFont(132);
gStyle->SetTitleFont(132, "xyz");
gStyle->SetLabelFont(132, "xyz");
gStyle->SetLegendFont(132);
gStyle->SetStatFont(132);
```

学位論文や学術論文に適した設定です。

### プレゼンテーション用（見やすく）

```cpp
#include <TStyle.h>

// Helvetica フォント（太め）で統一
gStyle->SetTextFont(62);
gStyle->SetTitleFont(62, "xyz");
gStyle->SetLabelFont(62, "xyz");
gStyle->SetLegendFont(62);
gStyle->SetStatFont(62);
```

スクリーン表示を想定した読みやすいフォント設定です。

### 国際学会用（汎用性重視）

```cpp
#include <TStyle.h>

// Helvetica フォント（標準）で統一
gStyle->SetTextFont(42);
gStyle->SetTitleFont(42, "xyz");
gStyle->SetLabelFont(42, "xyz");
gStyle->SetLegendFont(42);
gStyle->SetStatFont(42);
```

多くの環境で対応でき、汎用性の高い設定です。

### データ分析用（多階層フォント）

```cpp
#include <TStyle.h>

// タイトルを太く
gStyle->SetTitleFont(62, "xyz");

// ラベルと統計情報は標準
gStyle->SetLabelFont(42, "xyz");
gStyle->SetStatFont(42);
gStyle->SetLegendFont(42);
gStyle->SetTextFont(42);
```

タイトルを強調しながら、その他は読みやすく統一した設定です。

## 注意事項

- **フォントの可用性**: TrueTypeフォント（精度2）は多くのシステムで利用可能ですが、PostScriptフォント（精度1）はシステムによって異なる場合があります

- **和文フォント**: ROOTは日本語フォントの設定に対応していません。日本語テキストを使用する場合は、別途対応が必要です

- **印刷時の確認**: スクリーン表示では見えなくても、印刷時にフォントが変わることがあります。必要に応じてPDF出力で確認してください

- **複数のグラフ**: 複数のグラフを統一した見た目にするには、同じフォント設定を使用してください

## SetXXXFont メソッド一覧

| メソッド | 対象 | 引数 |
|---------|------|------|
| `SetTextFont()` | テキスト要素（デフォルト） | フォントコード |
| `SetTitleFont()` | グラフ/ヒストグラムのタイトル | フォントコード、軸指定（"x"、"y"、"z"、"xyz"） |
| `SetLabelFont()` | 軸ラベル | フォントコード、軸指定 |
| `SetLegendFont()` | 凡例 | フォントコード |
| `SetStatFont()` | 統計情報ボックス | フォントコード |

## リファレンス

- [ROOT TStyle::SetTextFont Documentation](https://root.cern/doc/master/classTStyle.html#a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6)
- [ROOT TStyle::SetTitleFont Documentation](https://root.cern/doc/master/classTStyle.html#a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7)
- [ROOT TStyle::SetLabelFont Documentation](https://root.cern/doc/master/classTStyle.html#a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8)
- [ROOT TStyle::SetLegendFont Documentation](https://root.cern/doc/master/classTStyle.html#a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9)
- [ROOT TStyle::SetStatFont Documentation](https://root.cern/doc/master/classTStyle.html#a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9da)
