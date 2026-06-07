# デフォルトの色を変更したい（`gROOT->GetColor->SetRGB`）

```cpp
// 色番号3を緑に変更
gROOT->GetColor(kGreen)->SetRGB(0.00, 0.70, 0.00);
```

`SetRGB` メソッドで、デフォルト色をカスタマイズできます。
ROOTのデフォルト配色は、蛍光が強すぎて見えにくい色があるので、変更することをオススメします。

```python
from ROOT import gROOT

# 色番号3を緑に変更
gROOT.GetColor(kGreen).SetRGB(0.00, 0.70, 0.00)
```

## デフォルト配色一覧

| `TColor` | 番号 | PAW互換値 | デフォルト色 | RGB値（10進） |
| --- | --- | --- | --- | --- |
| `kBlack` | 1 | 1 | 黒 | (0, 0, 0) |
| `kRed` | 632 | 2 | 赤 | (255, 0, 0) |
| `kGreen` | 416 | 3 | 緑（蛍光） | (0, 255, 0) |
| `kBlue` | 600 | 4 | 青 | (0, 0, 255) |
| `kYellow` | 400 | 5 | 黄（蛍光） | (255, 255, 0) |
| `kMagenta` | 616 | 6 | マゼンタ | (255, 0, 255) |
| `kCyan` | 432 | 7 | シアン（蛍光） | (0, 255, 255) |
| `kWhite` | 0 | 10 | 白 | (255, 255, 255) |
| `kGray` | 920 | - | 灰色 | (128, 128, 128) |
| `kOrange` | 800 | - | オレンジ | (255, 127, 0) |
| `kSpring` | 820 | - | 黄緑 | (255, 127, 127) |
| `kTeal` | 840 | - | 青緑 | (0, 127, 127) |
| `kAzure` | 860 | - | 水色 | (127, 127, 255) |
| `kViolet` | 880 | - | 紫 | (127, 0, 127) |
| `kPink` | 900 | - | ピンク | (255, 127, 255) |

## 色覚多様性したい

```cpp
// Use Okabe-Ito color palette for better visibility
void setup_colors() {
  const struct {
    Color_t index;
    float r, g, b;
  } kOverrides[] = {
    {kBlack, 0/255.f, 0/255.f, 0/255.f},       // Black
    {kOrange, 230/255.f, 159/255.f, 0/255.f},    // Orange
    {kCyan, 86/255.f, 180/255.f, 233/255.f},     // Sky Blue
    {kGreen, 0/255.f, 158/255.f, 115/255.f},    // Bluish Green
    {kYellow, 240/255.f, 228/255.f, 66/255.f},    // Yellow
    {kBlue, 0/255.f, 114/255.f, 178/255.f},      // Blue
    {kRed, 213/255.f, 94/255.f, 0/255.f},       // Vermillion
    {kMagenta, 204/255.f, 121/255.f, 167/255.f},   // Reddish Purple
  };

  for (const auto& c : kOverrides) {
    TColor* color = gROOT->GetColor(c.index);
    if (color) color->SetRGB(c.r, c.g, c.b);
  }
}
```

Okabe-Itoカラーパレットを参考にして、
色覚多様性に配慮した配色に変更するサンプルです。

## 落ち着いた配色にしたい

```cpp
#include <TROOT.h>

gROOT->GetColor(kGreen)->SetRGB(0.00, 0.70, 0.00);    // Green
gROOT->GetColor(kOrange)->SetRGB(1.00, 0.50, 0.00);    // Orange
gROOT->GetColor(kAzure)->SetRGB(0.15, 0.29, 0.56);    // China Blue
gROOT->GetColor(kTeal)->SetRGB(0.22, 0.37, 0.04);    // Leaf Green
gROOT->GetColor(kViolet)->SetRGB(0.50, 0.30, 0.70);    // Purple
```

蛍光が強い色を落ち着いた色に変更します。
論文や報告書に向いています。

```python
from ROOT import gROOT

gROOT.GetColor(kGreen).SetRGB(0.00, 0.70, 0.00)    # Green
gROOT.GetColor(kOrange).SetRGB(1.00, 0.50, 0.00)    # Orange
gROOT.GetColor(kAzure).SetRGB(0.15, 0.29, 0.56)    # China Blue
gROOT.GetColor(kTeal).SetRGB(0.22, 0.37, 0.04)    # Leaf Green
gROOT.GetColor(kViolet).SetRGB(0.50, 0.30, 0.70)    # Purple
```

## 鮮やかな配色にしたい

```cpp
#include <TROOT.h>

gROOT->GetColor(kRed)->SetRGB(0.95, 0.20, 0.20);    // Coral Red
gROOT->GetColor(kGreen)->SetRGB(0.20, 0.80, 0.20);    // Emerald Green
gROOT->GetColor(kBlue)->SetRGB(0.20, 0.40, 0.95);    // Vibrant Blue
gROOT->GetColor(kYellow)->SetRGB(0.95, 0.60, 0.10);    // Gold
gROOT->GetColor(kMagenta)->SetRGB(0.90, 0.20, 0.80);    // Hot Pink
```

より鮮やかで視認性の高い配色です。
プレゼンテーションやスライドに向いています。

```python
from ROOT import gROOT

gROOT.GetColor(kRed).SetRGB(0.95, 0.20, 0.20)    # Coral Red
gROOT.GetColor(kGreen).SetRGB(0.20, 0.80, 0.20)    # Emerald Green
gROOT.GetColor(kBlue).SetRGB(0.20, 0.40, 0.95)    # Vibrant Blue
gROOT.GetColor(kYellow).SetRGB(0.95, 0.60, 0.10)    # Gold
gROOT.GetColor(kMagenta).SetRGB(0.90, 0.20, 0.80)    # Hot Pink
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
