# 統計情報を表示したい（`gStyle->SetOptStat`）

```cpp
#include <TStyle.h>

// デフォルト: エントリー数、平均、標準偏差のみ表示
gStyle->SetOptStat(111110);

// 詳細な統計情報を表示
gStyle->SetOptStat(1111111);

// シンプルな統計情報のみ表示
gStyle->SetOptStat(100);
```

`gStyle->SetOptStat`メソッドで、
ヒストグラムに表示される統計情報の種類と表示方法を制御できます。

```python
from ROOT import gStyle

# 詳細な統計情報を表示
gStyle.SetOptStat(1111111)

# シンプルな統計情報のみ表示
gStyle.SetOptStat(100)
```

## ビット構造を理解したい

`SetOptStat`の引数は、7桁の整数で各ビットが異なる統計量に対応しています。

**ビット構造（右から数えます）：**

| 位置 | ビット値 | 統計量 | 説明 |
|------|--------|------|------|
| 1桁目 | 0/1/2 | Entries（エントリー数） | ヒストグラムの総サンプル数 |
| 2桁目 | 0/1/2 | Mean（平均値） | データの平均値 |
| 3桁目 | 0/1/2 | StdDev（標準偏差） | データの標準偏差 |
| 4桁目 | 0/1/2 | Underflow（アンダーフロー） | 下限値より小さいデータ数 |
| 5桁目 | 0/1/2 | Overflow（オーバーフロー） | 上限値より大きいデータ数 |
| 6桁目 | 0/1/2 | Integral（積分値） | ヒストグラムの全面積 |
| 7桁目 | 0/1/2 | Skewness（歪度） | 分布の非対称性を示す統計量 |

各ビットの値

- `0`：非表示
- `1`：表示
- `2`：エラー付きで表示（標準偏差を表示）

:::{note}

Kurtosis（尖度）も計算されますが、SetOptStatの第1桁では直接制御できません。

:::

### デフォルト値（111110）の説明

```text
111110 =
  Entries(1)
+ Mean(1)
+ StdDev(1)
+ Underflow(1)
+ Overflow(1)
+ Integral(0)
```

デフォルトでは以下の情報が表示されます。

- `1桁目 1`: Entries（エントリー数）表示
- `2桁目 1`: Mean（平均値）表示
- `3桁目 1`: Std Dev（標準偏差）表示
- `4桁目 1`: Underflow（アンダーフロー）表示
- `5桁目 1`: Overflow（オーバーフロー）表示
- `6桁目 0`: Integral（積分値）非表示
- `7桁目 0`: Skewness（歪度）非表示

## 異なる表示設定を使いたい

### シンプルな表示（3項目のみ）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(100);
```

- `1桁目 1`: Entries表示
- `2桁目 0`: Mean非表示
- `3桁目 0`: StdDev非表示
- 4～7桁目: その他非表示

エントリー数のみを表示するもっともシンプルな設定です。

### 基本的な表示（平均と標準偏差を含む）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(110);
```

- `1桁目 0`: Entries非表示
- `2桁目 1`: Mean表示
- `3桁目 1`: StdDev表示
- 4～7桁目: その他非表示

平均値と標準偏差の統計量を表示します。

### 標準的な表示（デフォルト構成）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(111110);
```

- `1～5桁目 1`: Entries、Mean、StdDev、Underflow、Overflow表示
- `6桁目 0`: Integral非表示
- `7桁目 0`: Skewness非表示

デフォルト設定と同じく、主要な統計情報を表示します。

### 詳細な表示（全情報表示）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(1111111);
```

- すべてのビットを`1`に設定
- Entries、Mean、StdDev、Underflow、Overflow、Integral、Skewnessを表示

利用可能なすべての統計情報を表示します。

### エラー付き表示（標準偏差を強調）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(112111);
```

- `1桁目 1`: Entries表示
- `2桁目 1`: Mean表示
- `3桁目 2`: StdDev「エラー付きで表示」
- `4～5桁目 1`: Underflow、Overflow表示
- `6～7桁目 0`: その他非表示

3桁目に`2`を指定することで、標準偏差をエラーバー風に強調表示できます。

## 実用例

### 論文用（見やすくシンプル）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(110);         // 平均と標準偏差のみ
gStyle->SetOptFit(1111);         // フィット情報も表示
```

論文では通常、エントリー数などの詳細情報は不要で、
平均値と標準偏差、フィット結果のみを表示するのが一般的です。

### プレゼンテーション用（視認性重視）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(111110);      // 主要な統計情報を表示
gStyle->SetOptFit(111);          // フィット結果も適度に表示
```

プレゼンテーションでは視認性を重視し、
主要な統計情報とフィット結果を適度に表示します。

### データ分析用（詳細な確認）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(1111111);     // すべての統計情報を表示
gStyle->SetOptFit(1111111);      // フィット結果も詳細に表示
```

データ分析時には、統計情報とフィット結果の両方を詳細に確認できます。

### 統計情報非表示

```cpp
#include <TStyle.h>

gStyle->SetOptStat(0);           // 統計情報を一切表示しない
```

ヒストグラムの形状だけに注目したい場合に使用します。

## SetOptFitとの関係

`SetOptStat`と[SetOptFit](./root-gstyle-setoptfit.md)は異なる設定です。

- **SetOptStat**: ヒストグラムの統計情報（エントリー数、平均、標準偏差など）
- **SetOptFit**: フィットされた関数のパラメーターと統計情報

両方を組み合わせることで、完全な情報表示が可能になります。

```cpp
#include <TStyle.h>

// 統計情報とフィット結果の両方を表示
gStyle->SetOptStat(111110);      // 統計情報
gStyle->SetOptFit(1111);         // フィット結果
```

## リファレンス

- [ROOT TStyle::SetOptStat Documentation](https://root.cern/doc/master/classTStyle.html#af25d6cdc6a59bae7b1e37cc1c6ab42c9)
- [ROOT TStyle::SetOptFit Documentation](https://root.cern/doc/master/classTStyle.html#a7a4e47b73a249b5e3270eb90fa7a16ba)
