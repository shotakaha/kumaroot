# デフォルトの色を変更したい（`gROOT->GetColor->SetRGB`）

```cpp
#include <TROOT.h>

// 色番号3を緑に変更
gROOT->GetColor(3)->SetRGB(0.00, 0.70, 0.00);
```

`SetRGB` メソッドで、デフォルト色をカスタマイズできます。
ROOTのデフォルト配色は、蛍光が強すぎて見えにくい色があるので、変更することをオススメします。

```python
from ROOT import gROOT

# 色番号3を緑に変更
gROOT.GetColor(3).SetRGB(0.00, 0.70, 0.00)
```

## デフォルト配色一覧

| 色番号 | デフォルト色 | RGB値（10進） |
|--------|-----------|-----------|
| 1 | 黒 | (0, 0, 0) |
| 2 | 赤 | (255, 0, 0) |
| 3 | 緑（蛍光） | (0, 255, 0) |
| 4 | 青 | (0, 0, 255) |
| 5 | 黄（蛍光） | (255, 255, 0) |
| 6 | マゼンタ | (255, 0, 255) |
| 7 | シアン（蛍光） | (0, 255, 255) |
| 8 | Dull Green | (56, 94, 11) |
| 9 | Dull Navy | (128, 0, 0) |
| 10 | 白 | (255, 255, 255) |

## 落ち着いた配色にしたい

```cpp
#include <TROOT.h>

gROOT->GetColor(3)->SetRGB(0.00, 0.70, 0.00);    // Green
gROOT->GetColor(5)->SetRGB(1.00, 0.50, 0.00);    // Orange
gROOT->GetColor(7)->SetRGB(0.15, 0.29, 0.56);    // China Blue
gROOT->GetColor(8)->SetRGB(0.22, 0.37, 0.04);    // Leaf Green
gROOT->GetColor(9)->SetRGB(0.50, 0.30, 0.70);    // Purple
```

蛍光が強い色を落ち着いた色に変更します。
論文や報告書に向いています。

```python
from ROOT import gROOT

gROOT.GetColor(3).SetRGB(0.00, 0.70, 0.00)    # Green
gROOT.GetColor(5).SetRGB(1.00, 0.50, 0.00)    # Orange
gROOT.GetColor(7).SetRGB(0.15, 0.29, 0.56)    # China Blue
gROOT.GetColor(8).SetRGB(0.22, 0.37, 0.04)    # Leaf Green
gROOT.GetColor(9).SetRGB(0.50, 0.30, 0.70)    # Purple
```

## 鮮やかな配色にしたい

```cpp
#include <TROOT.h>

gROOT->GetColor(2)->SetRGB(0.95, 0.20, 0.20);    // Coral Red
gROOT->GetColor(3)->SetRGB(0.20, 0.80, 0.20);    // Emerald Green
gROOT->GetColor(4)->SetRGB(0.20, 0.40, 0.95);    // Vibrant Blue
gROOT->GetColor(5)->SetRGB(0.95, 0.60, 0.10);    // Gold
gROOT->GetColor(6)->SetRGB(0.90, 0.20, 0.80);    // Hot Pink
```

より鮮やかで視認性の高い配色です。
プレゼンテーションやスライドに向いています。

```python
from ROOT import gROOT

gROOT.GetColor(2).SetRGB(0.95, 0.20, 0.20)    # Coral Red
gROOT.GetColor(3).SetRGB(0.20, 0.80, 0.20)    # Emerald Green
gROOT.GetColor(4).SetRGB(0.20, 0.40, 0.95)    # Vibrant Blue
gROOT.GetColor(5).SetRGB(0.95, 0.60, 0.10)    # Gold
gROOT.GetColor(6).SetRGB(0.90, 0.20, 0.80)    # Hot Pink
```

## RGB値の変換方法

RGB値は0～255（10進数）で表されますが、ROOTでは0～1の範囲で指定します。

### 変換式

```text
ROOTの値 = RGB値（10進数）/ 255
```

### 例

- RGB(255, 0, 0) → SetRGB(1.0, 0.0, 0.0)
- RGB(178, 34, 34) → SetRGB(0.70, 0.13, 0.13)

## リファレンス

- [The Rainbow Color Map - ROOT公式ブログ](https://root.cern/blog/rainbow-color-map/)
- [ROOT Color Guide](https://root.cern/doc/master/classTColor.html)
