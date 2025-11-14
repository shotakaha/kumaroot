# 1次元ヒストグラムを作りたい（`TH1`）

```cpp
#include <TH1D.h>

// ヒストグラムを作成
TH1D *h = new TH1D("h1", "Histogram;X axis;Y axis", 200, -2, 2);
```

`TH1`は1次元ヒストグラムの基本クラスです。
データを解析する際に、データの分布を視覚化して分析するために使用します。
データ型に応じた派生クラスを選択することで、メモリ使用量と精度のバランスを最適化できます。

```python
from ROOT import TH1D

# ヒストグラムを作成
h = TH1D("h1", "Histogram;X axis;Y axis", 200, -2, 2)
```

## コンストラクターのシグネチャ

```cpp
TH1D(const char* name,
     const char* title,
     Int_t nbinsx,
     Double_t xlow,
     Double_t xup);
```

### 引数の説明

**name** - ヒストグラムの名前

- オブジェクト識別用
- ROOTファイルでの保存
- 同じディレクトリ内では一意

**title** - ヒストグラムのタイトル

- TCanvasに描画するときにキャンバス内に表示
- `"タイトル;X軸;Y軸"`のようにセミコロン区切りの形式で軸ラベルも指定可能

**nbinsx** - X軸のビン数

- ビン幅は `(xup - xlow) / nbinsx` で計算
- `nbinsx`はヒストグラムのメモリ使用量に影響するため、適切な値を選択

**xlow** - X軸の最小値

- `xlow`より小さい値は`Undeflow`としてカウントされる

**xup** - X軸の最大値

- `xup`より大きい値は`Overflow`としてカウントされる

## データ型を選択したい

`TH1`には複数の派生クラスがあります。
入力するデータの特性に合わせて選択できます。

| クラス名 | データ型 | データ長 | 用途 |
|---|---|---|---|
| `TH1C` | `char` | 8bit 整数 | 非常に小さいカウント値（0-256） |
| `TH1S` | `short` | 16bit 整数 | 小〜中程度のカウント値（0-65536） |
| `TH1I` | `int` | 32bit 整数 | 整数値データ |
| `TH1F` | `float` | 32bit 浮動小数点 | 連続値データ（標準） |
| `TH1D` | `double` | 64bit 浮動小数点 | 高精度が必要な連続値データ |

**選択のガイドライン：**

- **整数値データ**: `TH1I`を使用
- **連続値データ**: `TH1F`（メモリ効率）または`TH1D`（高精度）を使用
- **データサイズが大きい場合**: `TH1F`でメモリ節約
- **高精度が必要な場合**: `TH1D`を使用

## タイトルしたい（`title`）

```cpp
#include <TH1D.h>

// タイトルのみ
TH1D *h1 = new TH1D(
    "h1",
    "Histogram Title",
    100, 0, 10
);
```

## 軸ラベルしたい（`title;x-axis;y-axis`）

```cpp
#include <TH1D.h>

// タイトルと軸ラベル
TH1D *h2 = new TH1D(
    "h2",
    "Title;X axis;Y axis",
    100, 0, 10
);

// セミコロン区切り：タイトル;X軸タイトル;Y軸タイトル
TH1D *h3 = new TH1D(
    "h3",
    "Gaussian Distribution;Value;Frequency",
    100, -5, 5
);
```

ヒストグラムを初期化するときに、タイトルと軸ラベルを指定できます。
セミコロン（`;`）で区切ることで、グラフのタイトル、X軸タイトル、Y軸タイトルを同時に指定できます。



## エラー（統計誤差）を管理したい

ヒストグラムの各ビンには、統計誤差（エラー）が関連付けられています。通常、エラーは自動的に計算されますが、明示的に設定することもできます。

### 重みとエラーの違い

| 項目 | 重み（Weight） | エラー（Error） |
|---|---|---|
| 指定方法 | `Fill`の第2引数 | `SetBinError`で個別設定、または`Sumw2`で追跡 |
| 役割 | データポイントの統計的重要度 | 各ビンの統計誤差（不確かさ） |
| フィッティング | 重みが統計的重要度として考慮される | エラーは重みとして使用される場合がある |
| 自動計算 | 指定しない場合は重み=1 | `Sumw2()`後は重みから自動計算、通常は√N |

## 実践例：ガウス分布のデータを解析したい

```cpp
#include <TH1D.h>
#include <TRandom.h>
#include <cstdio>

// ヒストグラムを作成
TH1D *h = new TH1D("gauss",
                   "Gaussian Distribution;Value;Frequency",
                   200, -5, 5);

// ガウス分布に従うデータを生成
for (Int_t i = 0; i < 100000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// 統計情報を表示
printf("Mean: %f\n", h->GetMean());
printf("RMS: %f\n", h->GetRMS());
printf("Entries: %lld\n", h->GetEntries());

// 統計ボックスを表示して描画
h->SetStats();
h->Draw();
```

このサンプルでは、平均0、標準偏差1のガウス分布に従う100000個のデータポイントをヒストグラムに入力し、その統計情報を表示しています。

## 関連メソッド

- [TH1::GetEntries](https://root.cern/doc/master/classTH1.html#a3e1dce4da0d3de6f9e5175c4a4da5589) - エントリー数を取得
- [TH1::GetBinContent](https://root.cern/doc/master/classTH1.html#a2f88d66e1e7fb2c6a872d50c4e5f5efb) - ビンの内容を取得
- [TH1::GetBinError](https://root.cern/doc/master/classTH1.html#a72e5df3acb63a960cdaebc3e18f47bfd) - ビンの誤差を取得
- [TH1::Integral](https://root.cern/doc/master/classTH1.html#ae49a9a1d996e4f8f30b2d12a09e6e034) - ヒストグラムの積分値を計算
- [TH1::Fit](https://root.cern/doc/master/classTH1.html#a5bc5a5f4f48285d8d41ce37d82e7a8ea) - 関数をフィットする

## 参考資料

- [ROOT Documentation - TH1](https://root.cern/doc/master/classTH1.html)
- [ROOT Documentation - TH1D](https://root.cern/doc/master/classTH1D.html)
