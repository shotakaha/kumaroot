# ヒストグラムの見た目を変更したい（`gStyle->SetHist*`）

```cpp
#include <TStyle.h>

gStyle->SetHistLineWidth(2);      // 線幅
gStyle->SetHistLineColor(1);      // 線の色
gStyle->SetHistLineStyle(1);      // 線のスタイル
gStyle->SetHistFillStyle(0);      // 塗りつぶしスタイル
gStyle->SetHistFillColor(1);      // 塗りつぶしの色
```

`gStyle->SetHist*`系のメソッドで、ヒストグラムのデフォルト表示属性を変更できます。
`SetHistLine*`で線の幅、色、スタイル、
`SetHistFill*`で塗りつぶしをカスタマイズできます。

```python
from ROOT import gStyle

gStyle.SetHistLineWidth(2)        # 線幅
gStyle.SetHistLineColor(1)        # 線の色
gStyle.SetHistLineStyle(1)        # 線のスタイル
gStyle.SetHistFillStyle(0)        # 塗りつぶしスタイル
gStyle.SetHistFillColor(1)        # 塗りつぶしの色
```

:::{note}

`gStyle` で設定した値は、その後に作成されるヒストグラムに適用されます。
`.rootrc`で設定し、全体に読み込ませるとよいです。

すでに作成されたヒストグラムに適用するには、
各ヒストグラムオブジェクトの
`SetLineWidth()`、
`SetLineColor()`
などのメソッドを使用してください

:::

## 線の幅を変更したい（``SetHistLineWidth``）

```cpp
gStyle->SetHistLineWidth(2);      // デフォルト: 1
```

`gStyle->SetHistLineWidth`メソッドで、
ヒストグラムの外枠線の太さを変更できます。
デフォルトは`1`です。
やや太い`2`がオススメです。
`3`以上は太くなりすぎて、複数ヒストグラムの重ね描き時は見えにくくなる可能性があります。

## 線の色を変更したい（``SetHistLineColor``）

```cpp
gStyle->SetHistLineColor(1);      // 黒
gStyle->SetHistLineColor(2);      // 赤
gStyle->SetHistLineColor(3);      // 緑
gStyle->SetHistLineColor(4);      // 青
gStyle->SetHistLineColor(5);      // 黄
gStyle->SetHistLineColor(6);      // マゼンタ
gStyle->SetHistLineColor(7);      // シアン
```

`gStyle->SetHistLineColor`メソッドで
ヒストグラムの外枠線の色を変更できます。

## 線のスタイルを変更したい（``SetHistLineStyle``）

```cpp
gStyle->SetHistLineStyle(1);      // 実線（デフォルト）
gStyle->SetHistLineStyle(2);      // 破線
gStyle->SetHistLineStyle(3);      // 点線
gStyle->SetHistLineStyle(4);      // 一点鎖線
```

`gStyle->SetHistLineStyle`メソッドで、
ヒストグラムの外枠線のスタイルを変更できます。

## 塗りつぶしスタイルを変更したい（``SetHistFillStyle``）

```cpp
gStyle->SetHistFillStyle(0);      // 塗りつぶしなし
gStyle->SetHistFillStyle(1001);   // 単色で塗りつぶし
gStyle->SetHistFillStyle(3001);   // 網目模様（水平線）
gStyle->SetHistFillStyle(3004);   // ハッチング（斜線+45°）
gStyle->SetHistFillStyle(3005);   // ハッチング（逆斜線-45°）
```

`gStyle->SetHistFillStyle`メソッドでヒストグラムの内部の塗りつぶし方法を指定します。

## 塗りつぶしの色を変更したい（``SetHistFillColor``）

```cpp
gStyle->SetHistFillColor(2);      // 赤で塗りつぶし
```

`gStyle->SetHistFillColor`メソッドで、
ヒストグラムの内部の塗りつぶし色を指定します。
`SetHistLineColor` と同じカラーコードを使用します。

## 実用例

### 落ち着いた配色にしたい

```cpp
#include <TStyle.h>

gStyle->SetHistLineWidth(2);
gStyle->SetHistLineColor(1);      // 黒
gStyle->SetHistLineStyle(1);      // 実線
gStyle->SetHistFillStyle(0);      // 塗りつぶしなし
```

### 視認性を重視したい

```cpp
#include <TStyle.h>

gStyle->SetHistLineWidth(3);
gStyle->SetHistLineColor(4);      // 青
gStyle->SetHistLineStyle(1);      // 実線
gStyle->SetHistFillStyle(1001);   // 単色塗りつぶし
gStyle->SetHistFillColor(4);      // 青で塗りつぶし
```

### 複数のヒストグラムを重ねたい

```cpp
#include <TStyle.h>

gStyle->SetHistLineWidth(2);
gStyle->SetHistFillStyle(0);      // 塗りつぶしなし（背景が透ける）
// 各ヒストグラムで異なる色を指定
```

複数のヒストグラムを重ね描きする場合、
線幅が太すぎるとヒストグラムが見えにくくなる可能性があります。

## リファレンス

- [ROOT TStyle Documentation](https://root.cern/doc/master/classTStyle.html)
