# 2次元ヒストグラムしたい（`TH2`）

```cpp
#include <TH2D.h>

// 2次元ヒストグラムを作成
TH2D *h = new TH2D("h2d", "2D Histogram;X axis;Y axis", 100, -1, 1, 100, -5, 5);
```

`TH2`は2次元ヒストグラムの基本クラスです。
2つの変数の相関関係を可視化する際に、データの分布を両軸で同時に解析するために使用します。
[TH1](./root-th1.md)と同じように、データ型に応じた派生クラスを選択することで、メモリ使用量と精度のバランスを最適化できます。

```python
from ROOT import TH2D

# 2次元ヒストグラムを作成
h = TH2D("h2d", "2D Histogram;X axis;Y axis", 100, -1, 1, 100, -5, 5)
```

## コンストラクターのシグネチャ

```cpp
TH2D(const char* name,
     const char* title,
     Int_t nbinsx,
     Double_t xlow,
     Double_t xup,
     Int_t nbinsy,
     Double_t ylow,
     Double_t yup);
```

### 引数の説明

**name** - ヒストグラムの名前

- オブジェクト識別用
- ROOTファイルでの保存
- 同じディレクトリ内では一意

**title** - ヒストグラムのタイトル

- TCanvasに描画するときに表示
- `"タイトル;X軸;Y軸"`のようにセミコロン区切りの形式で軸ラベルも指定可能

**nbinsx** - X軸のビン数

- ビン幅は `(xup - xlow) / nbinsx` で計算

**xlow、xup** - X軸の範囲

- `xlow`より小さい値は`Underflow`としてカウント
- `xup`より大きい値は`Overflow`としてカウント

**nbinsy** - Y軸のビン数

- ビン幅は `(yup - ylow) / nbinsy` で計算

**ylow、yup** - Y軸の範囲

- `ylow`より小さい値は`Underflow`としてカウント
- `yup`より大きい値は`Overflow`としてカウント

## データ型を選択したい

`TH2`には複数の派生クラスがあります。
入力するデータの特性に合わせて選択できます。

| クラス名 | データ型 | データ長 | 用途 |
|---|---|---|---|
| `TH2C` | `char` | 8bit 整数 | 非常に小さいカウント値（0-256） |
| `TH2S` | `short` | 16bit 整数 | 小〜中程度のカウント値（0-65536） |
| `TH2I` | `int` | 32bit 整数 | 整数値データ |
| `TH2F` | `float` | 32bit 浮動小数点 | 連続値データ（標準） |
| `TH2D` | `double` | 64bit 浮動小数点 | 高精度が必要な連続値データ |

**選択のガイドライン：**

- **整数値データ**: `TH2I`を使用
- **連続値データ**: `TH2F`（メモリ効率）または`TH2D`（高精度）を使用
- **データサイズが大きい場合**: `TH2F`でメモリ節約
- **高精度が必要な場合**: `TH2D`を使用

## タイトルと軸ラベルしたい

```cpp
#include <TH2D.h>

// タイトルと軸ラベル
TH2D *h = new TH2D(
    "h",
    "Title;X axis;Y axis",
    100, 0, 10,
    100, 0, 20
);

// セミコロン区切り：タイトル;X軸タイトル;Y軸タイトル
TH2D *h2 = new TH2D(
    "h2",
    "Energy Distribution;Kinetic Energy (GeV);Angle (deg)",
    100, 0, 100,
    50, 0, 180
);
```

ヒストグラムを初期化するときに、タイトルと軸ラベルを指定できます。
セミコロン（`;`）で区切ることで、グラフのタイトル、X軸タイトル、Y軸タイトルを同時に指定できます。

## 実践例：相関関係を解析したい

```cpp
#include <TH2D.h>
#include <TRandom.h>
#include <cstdio>

// 2次元ヒストグラムを作成
TH2D *h = new TH2D("correlation",
                   "X vs Y Correlation;X Value;Y Value",
                   100, -3, 3,
                   100, -3, 3);

// 相関のあるデータを生成
for (Int_t i = 0; i < 10000; i++) {
    double x = gRandom->Gaus(0, 1);
    double y = 2 * x + gRandom->Gaus(0, 0.5);
    h->Fill(x, y);
}

// カラーマップで描画
h->Draw("COLZ");
```

このサンプルでは、y=2xの関係を持つ相関データを生成し、その相関関係を2次元ヒストグラムで可視化しています。

## 描画オプション

2次元ヒストグラムの描画時には、異なる表示方法を指定できます。

| オプション | 説明 |
|---|---|
| `"COLZ"` | カラーマップで表示（デフォルト、推奨） |
| `"CONT"` | 等高線で表示 |
| `"LEGO"` | 3D立体図で表示 |
| `"SURF"` | 3D曲面で表示 |
| `"BOX"` | ボックスで表示 |
| `"SCATTER"` | 散布図で表示 |

```cpp
#include <TH2D.h>

TH2D *h = new TH2D("h", "2D Histogram", 50, -5, 5, 50, -5, 5);

// ... データを入力 ...

// 異なる表示方法
h->Draw("COLZ");      // カラーマップ
h->Draw("CONT");      // 等高線
h->Draw("LEGO");      // 3D立体図
```

## 関連メソッド

- [TH1](./root-th1.md) - 1次元ヒストグラム
- [TH3](./root-th3.md) - 3次元ヒストグラム
- [TProfile](./root-tprofile.md) - プロファイルヒストグラム

## 参考資料

- [ROOT Documentation - TH2](https://root.cern/doc/master/classTH2.html)
- [ROOT Documentation - TH2D](https://root.cern/doc/master/classTH2D.html)
