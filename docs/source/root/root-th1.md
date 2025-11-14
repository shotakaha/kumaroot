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

各派生クラスのコンストラクターは以下のシグネチャを持ちます。

```cpp
TH1D(const char* name,
     const char* title,
     Int_t nbinsx,
     Double_t xlow,
     Double_t xup);
```

### 引数の説明

| 引数 | 型 | 説明 |
|---|---|---|
| `name` | `const char*` | ヒストグラムの名前（オブジェクト識別用、ROOTファイルでの保存に使用） |
| `title` | `const char*` | ヒストグラムのタイトル（セミコロン区切りで軸ラベルも指定可能） |
| `nbinsx` | `Int_t` | X軸のビン数（正の整数） |
| `xlow` | `Double_t` | X軸の最小値 |
| `xup` | `Double_t` | X軸の最大値 |

**注意事項：**

- `name`は同じディレクトリ内では一意である必要があります
- `title`でセミコロン区切りを使う場合: `"タイトル;X軸;Y軸"` 形式
- `nbinsx`はヒストグラムのメモリ使用量に影響するため、適切な値を選択してください
- ビン幅は `(xup - xlow) / nbinsx` で計算されます

### 異なるデータ型での使用例

```cpp
#include <TH1.h>

// TH1D（64bit浮動小数点、最も一般的）
TH1D *h1 = new TH1D("h1", "Histogram D", 100, 0.0, 10.0);

// TH1F（32bit浮動小数点、メモリ効率重視）
TH1F *h2 = new TH1F("h2", "Histogram F", 100, 0.0, 10.0);

// TH1I（32bit整数、整数データ向け）
TH1I *h3 = new TH1I("h3", "Histogram I", 100, 0, 10);

// TH1S（16bit整数、小規模データ向け）
TH1S *h4 = new TH1S("h4", "Histogram S", 100, 0, 10);
```



## クイックリファレンス

### C++

```cpp
#include <TH1D.h>
#include <TRandom.h>

// ヒストグラムを作成
TH1D *h = new TH1D("h1", "Histogram;X axis;Y axis", 200, -2, 2);

// データを入力
for (Int_t i = 0; i < 100000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}

// 統計情報を取得
Double_t mean = h->GetMean();
Double_t rms = h->GetRMS();

// 統計ボックスを表示
h->SetStats();

// ヒストグラムを描画
h->Draw();
```

### Python

```python
from ROOT import TH1D, TRandom, gRandom

# ヒストグラムを作成
h = TH1D("h1", "Histogram;X axis;Y axis", 200, -2, 2)

# データを入力
for i in range(100000):
    h.Fill(gRandom.Gaus(0, 1))

# 統計情報を取得
mean = h.GetMean()
rms = h.GetRMS()

# 統計ボックスを表示
h.SetStats()

# ヒストグラムを描画
h.Draw()
```

## ヒストグラムのデータ型を選択したい

`TH1`には複数の派生クラスがあり、データの特性に合わせて選択できます。

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

## タイトルと軸ラベルを指定したい（コンストラクターの第2引数）

ヒストグラムを初期化するときに、タイトルと軸ラベルを指定できます。

```cpp
#include <TH1D.h>

// タイトルのみ
TH1D *h1 = new TH1D("h1", "Histogram Title", 100, 0, 10);

// タイトルと軸ラベル
TH1D *h2 = new TH1D("h2", "Title;X axis;Y axis", 100, 0, 10);

// セミコロン区切り：タイトル;X軸タイトル;Y軸タイトル
TH1D *h3 = new TH1D("h3", "Gaussian Distribution;Value;Frequency", 100, -5, 5);
```

セミコロン（`;`）で区切ることで、グラフのタイトル、X軸タイトル、Y軸タイトルを同時に指定できます。

## データを入力したい（`Fill`）

ヒストグラムにデータを入力するには`Fill`メソッドを使用します。

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);

// 単一の値を入力
h->Fill(5.5);

// ループでデータを入力
for (Int_t i = 0; i < 1000; i++) {
    h->Fill(gRandom->Gaus(5, 1));
}

// 重み付きで入力
h->Fill(7.2, 2.5);  // 値7.2に重み2.5を追加
```

## 統計情報を取得したい

ヒストグラムから統計情報を取得するメソッドです。

### 平均値を取得したい（`GetMean`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t mean = h->GetMean();
printf("Mean: %f\n", mean);

// X軸の平均（デフォルト）
Double_t mean_x = h->GetMean(1);

// Y軸の平均（重み付けが必要な場合）
Double_t mean_y = h->GetMean(2);
```

`GetMean`でヒストグラムの平均値を取得します。引数でX軸またはY軸を指定できます。

### RMS（二乗平均平方根）を取得したい（`GetRMS`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

Double_t rms = h->GetRMS();
printf("RMS: %f\n", rms);

// X軸のRMS（デフォルト）
Double_t rms_x = h->GetRMS(1);

// Y軸のRMS
Double_t rms_y = h->GetRMS(2);
```

`GetRMS`でRoot Mean Square（二乗平均平方根）を取得します。これはデータの広がり（分散の平方根）を表します。

## 統計ボックスを表示したい（`SetStats`）

描画時に統計ボックス（統計情報を表示するボックス）を表示するには、`SetStats`メソッドを使用します。

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

// 統計ボックスを表示
h->SetStats();
// または
h->SetStats(1);

// 統計ボックスを非表示
h->SetStats(0);

h->Draw();
```

`SetStats(1)`で統計ボックスを表示し、`SetStats(0)`で非表示にします。統計ボックスには平均値、RMS、エントリー数などが表示されます。

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
