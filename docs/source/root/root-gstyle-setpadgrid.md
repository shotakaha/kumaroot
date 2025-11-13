# 補助線を表示したい（`gStyle->SetPadGrid*`）

```cpp
#include <TStyle.h>

// X軸に補助線を表示
gStyle->SetPadGridx(1);

// Y軸に補助線を表示
gStyle->SetPadGridy(1);

// 両軸に補助線を表示
gStyle->SetPadGridx(1);
gStyle->SetPadGridy(1);
```

`gStyle->SetPadGridx`と`gStyle->SetPadGridy`メソッドで、
グラフやヒストグラムの背景に補助線（グリッドライン）を表示できます。

```python
from ROOT import gStyle

# X軸に補助線を表示
gStyle.SetPadGridx(1)

# Y軸に補助線を表示
gStyle.SetPadGridy(1)

# 両軸に補助線を表示
gStyle.SetPadGridx(1)
gStyle.SetPadGridy(1)
```

## グリッドラインを理解したい

グリッドラインは、グラフ上の値を読み取る際に参考となる補助線です。

### グリッドラインの役割

- **視認性の向上**: データポイントの座標値を視覚的に読み取りやすくする
- **精度の向上**: 軸との対応関係が明確になり、値の読み誤りを減らせる
- **比較を簡単に**: 複数のデータ系列を比較する際に、値の大小関係を判断しやすい

### 設定値

- `0`：グリッドラインを表示しない（デフォルト）
- `1`：グリッドラインを表示する

## 異なるグリッド設定を使いたい

### X軸のみに補助線を表示

```cpp
#include <TStyle.h>

gStyle->SetPadGridx(1);
gStyle->SetPadGridy(0);
```

X軸方向の値を読み取りやすくしたい場合に有効です。
例：時系列データ、周波数特性

### Y軸のみに補助線を表示

```cpp
#include <TStyle.h>

gStyle->SetPadGridx(0);
gStyle->SetPadGridy(1);
```

Y軸方向の値を読み取りやすくしたい場合に有効です。
例：大きさ比較、相対値の評価

### X軸とY軸の両方に補助線を表示

```cpp
#include <TStyle.h>

gStyle->SetPadGridx(1);
gStyle->SetPadGridy(1);
```

XY平面全体で座標値を読み取りたい場合に有効です。
例：散布図、2次元デーマップ

### グリッドラインを非表示にする

```cpp
#include <TStyle.h>

gStyle->SetPadGridx(0);
gStyle->SetPadGridy(0);
```

すべてのグリッドラインを非表示にします。

## 実用例

### 論文用（シンプルで見やすい）

```cpp
#include <TStyle.h>

// Y軸のみに補助線を表示
gStyle->SetPadGridx(0);
gStyle->SetPadGridy(1);
```

論文ではシンプルさが重視されるため、
必要最小限のY軸補助線のみを表示するのが一般的です。
これにより、値の読み取りが容易になります。

### プレゼンテーション用（見やすく強調）

```cpp
#include <TStyle.h>

// 両軸に補助線を表示
gStyle->SetPadGridx(1);
gStyle->SetPadGridy(1);
```

プレゼンテーションではグラフの見やすさが重要なため、
両軸に補助線を表示して、データポイントの座標を視覚的に把握しやすくします。

### データ分析用（詳細な読み取り）

```cpp
#include <TStyle.h>

// 両軸に補助線を表示
gStyle->SetPadGridx(1);
gStyle->SetPadGridy(1);

// 軸の目盛りも詳細に表示
gStyle->SetNdivisions(510, "X");
gStyle->SetNdivisions(510, "Y");
```

データ分析では精密な値の読み取りが必要なため、
両軸の補助線と詳細な目盛りを組み合わせます。

### 測定データの可視化

```cpp
#include <TStyle.h>

// Y軸のみに補助線を表示
gStyle->SetPadGridy(1);
```

測定結果のプロットでは、Y軸（測定値）の読み取りが重要なため、
Y軸補助線のみを表示します。

### 時系列グラフ

```cpp
#include <TStyle.h>

// X軸のみに補助線を表示
gStyle->SetPadGridx(1);
```

時系列データでは、X軸（時間）の読み取りが重要なため、
X軸補助線のみを表示します。

## グリッドラインのカスタマイズ

### グリッドラインのスタイルを変更

```cpp
#include <TStyle.h>
#include <TH1F.h>

TH1F *hist = new TH1F("hist", "Histogram", 100, 0, 10);
// ...データをFill...

// グリッドラインを表示
hist->GetPainter()->SetGridx();
hist->GetPainter()->SetGridy();

// グリッドラインのスタイルを変更（破線など）
gStyle->SetGridStyle(2);  // 2 = 破線
gStyle->SetGridColor(kGray);
gStyle->SetGridWidth(1);
```

### 個別のオブジェクトで設定

```cpp
#include <TStyle.h>
#include <TCanvas.h>
#include <TH1F.h>

TCanvas *c = new TCanvas();
TH1F *hist = new TH1F("hist", "Histogram", 100, 0, 10);

// キャンバス単位でグリッドを設定
c->SetGridx(1);
c->SetGridy(1);

hist->Draw();
c->Draw();
```

## 注意事項

- **グリッドラインの密度**: 目盛りが多すぎると、グリッドラインが煩雑になります。必要に応じて目盛り数を調整してください

- **グリッドラインと背景色**: グリッドラインが見えにくい場合は、背景色やグリッドラインの色を調整してください

- **印刷時の見え方**: スクリーン表示では見やすくても、印刷時にグリッドラインが目立ちすぎることがあります

## グリッドラインのスタイル設定

グリッドラインの外観をさらにカスタマイズする場合：

```cpp
#include <TStyle.h>

gStyle->SetPadGridx(1);
gStyle->SetPadGridy(1);

// グリッドラインのスタイル
gStyle->SetGridStyle(1);   // 1 = 実線、2 = 破線、3 = 点線
gStyle->SetGridColor(15);  // カラーコード（15 = グレー）
gStyle->SetGridWidth(1);   // 線の太さ
```

## リファレンス

- [ROOT TStyle::SetPadGridx Documentation](https://root.cern/doc/master/classTStyle.html#a7f76b3a7e0d8c3f0c2d5e1f8b4a9c7d6)
- [ROOT TStyle::SetPadGridy Documentation](https://root.cern/doc/master/classTStyle.html#a5e3b2d8f7c9a1b4e6f8d0c2a4e1b9f7)
- [ROOT TStyle Documentation](https://root.cern/doc/master/classTStyle.html)
