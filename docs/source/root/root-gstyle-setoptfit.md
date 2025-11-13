# フィット結果を表示したい（`gStyle->SetOptFit`）

```cpp
#include <TStyle.h>

// デフォルト: フィット結果を非表示
gStyle->SetOptFit(0);

// フィット結果を詳細表示
gStyle->SetOptFit(1111111);

// フィット関数とパラメーターのみ表示
gStyle->SetOptFit(111);
```

`gStyle->SetOptFit`メソッドで、
ヒストグラムにフィットした関数のパラメーターや統計情報の表示を制御できます。

```python
from ROOT import gStyle

# フィット結果を表示
gStyle.SetOptFit(1111111)

# フィット関数とパラメーターのみ表示
gStyle.SetOptFit(111)
```

## ビット構造を理解したい

`SetOptFit`の引数は、7桁の整数で各ビットがフィット結果の異なる項目に対応しています。

**ビット構造（右から数えます）：**

| 位置 | ビット値 | 説明 |
|------|--------|------|
| 1桁目 | 0/1 | Chi square（$\chi^{2}$値） |
| 2桁目 | 0/1 | パラメーター値 |
| 3桁目 | 0/1 | パラメーターのエラー |
| 4桁目 | 0/1 | フィット関数の名前 |
| 5桁目 | 0/1 | 追加統計情報 |
| 6桁目 | 0/1 | 行列情報 |
| 7桁目 | 0/1 | 確率（Probability） |

各ビットの値

- `0`：非表示
- `1`：表示

### デフォルト値（0）の説明

```text
0000000 = フィット結果を非表示
```

フィット結果を表示する場合は、最低でも`1`を指定する必要があります。

## 異なる表示設定を使いたい

### 最小限の表示（$\chi^{2}$値とパラメーターのみ）

```cpp
#include <TStyle.h>

gStyle->SetOptFit(111);
```

- 1桁目`1`: χ²値表示
- 2桁目`1`: パラメーター値表示
- 3桁目`1`: パラメーターのエラー表示
- 4～7桁目`0`: その他は非表示

### 標準的な表示（もっともよく使用）

```cpp
#include <TStyle.h>

gStyle->SetOptFit(1111);
```

- 1～3桁目: χ²値、パラメーター、エラー表示
- 4桁目`1`: フィット関数の名前表示
- 5～7桁目`0`: その他は非表示

### 詳細な表示（全情報表示）

```cpp
#include <TStyle.h>

gStyle->SetOptFit(1111111);
```

- すべてのビットを`1`に設定
- χ²値、パラメーター、エラー、関数名、統計情報、行列情報、確率を表示

### シンプルな表示（関数名と$\chi^{2}$値のみ）

```cpp
#include <TStyle.h>

gStyle->SetOptFit(1001);
```

- 1桁目`1`: χ²値表示
- 2～3桁目`0`: パラメーター非表示
- 4桁目`1`: 関数名表示
- 5～7桁目`0`: その他は非表示

## 統計情報との組み合わせ

フィット結果の表示と統計情報の表示を組み合わせることが一般的です。

```cpp
#include <TStyle.h>

// 統計情報を表示（エントリー数、平均、標準偏差）
gStyle->SetOptStat(111110);

// フィット結果を表示（パラメーター、χ²値）
gStyle->SetOptFit(1111);
```

この設定により、ヒストグラムに統計情報とフィット結果の両方が表示されます。

## 実用例

### 論文用（見やすくシンプル）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(0);         // 統計情報非表示
gStyle->SetOptFit(1111);       // フィット情報を適度に表示
```

論文では通常、統計情報は表示せず、
フィット結果のパラメーターとχ²値のみを表示するのが一般的です。

### データ分析用（詳細な確認）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(111110);    // 統計情報を詳細に表示
gStyle->SetOptFit(1111111);    // フィット結果も詳細に表示
```

データ分析時には、統計情報とフィット結果の両方を詳細に確認できます。

### プレゼンテーション用（視認性重視）

```cpp
#include <TStyle.h>

gStyle->SetOptStat(11);        // エントリー数と平均のみ
gStyle->SetOptFit(111);        // χ²値とパラメーターのみ
```

プレゼンテーションでは、必要最小限の情報に絞って表示します。

## SetOptStatとの関係

`SetOptFit`と[SetOptStat](./root-gstyle-setoptstat.md)は異なる設定です。

- **SetOptStat**: ヒストグラムの統計情報（エントリー数、平均、標準偏差など）
- **SetOptFit**: フィットされた関数のパラメーターと統計情報

両方を組み合わせることで、完全な情報表示が可能になります。

## リファレンス

- [ROOT TStyle::SetOptFit Documentation](https://root.cern/doc/master/classTStyle.html#a7a4e47b73a249b5e3270eb90fa7a16ba)
- [ROOT TStyle::SetOptStat Documentation](https://root.cern/doc/master/classTStyle.html#af25d6cdc6a59bae7b1e37cc1c6ab42c9)
