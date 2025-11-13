# 軸に時間を表示したい（`SetTimeDisplay` / `SetTimeFormat` / `SetTimeOffset`）

```cpp
#include <TStyle.h>
#include <TGraph.h>

TGraph *graph = new TGraph();
// ...データをFill...

// Unix epoch と ROOT epoch の差を設定
gStyle->SetTimeOffset(-788918400);

// グラフのX軸を時間表示に設定
graph->GetXaxis()->SetTimeDisplay(1);

// 時間のフォーマットを指定
graph->GetXaxis()->SetTimeFormat("%Y-%m-%d %H:%M:%S");

// タイムゾーンを GMT+0 に設定
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

`SetTimeDisplay`、`SetTimeFormat`、`SetTimeOffset`メソッドで、
グラフやヒストグラムの軸に時間情報を表示できます。

```python
from ROOT import gStyle, TGraph

graph = TGraph()
# ...データを充填...

# Unix epoch と ROOT epoch の差を設定
gStyle.SetTimeOffset(-788918400)

# グラフのX軸を時間表示に設定
graph.GetXaxis().SetTimeDisplay(1)

# 時間のフォーマットを指定
graph.GetXaxis().SetTimeFormat("%Y-%m-%d %H:%M:%S")

# タイムゾーンを GMT+0 に設定
graph.GetXaxis().SetTimeOffset(0, "gmt")
```

## Epoch時間を理解したい

Epoch時間とは、特定の基準時点から経過した秒数で時刻を表す方式です。

### Unix Epoch と ROOT Epoch の違い

**Unix Epoch**：

- 基準時点: 1970年1月1日00時00分00秒（UTC）
- コンピューターの標準時間形式として広く使われている
- Linux、Unix、Windows、macOSなど多くのOSで採用

**ROOT Epoch**：

- 基準時点: 1995年1月1日00時00分00秒（UTC）
- ROOT固有の時間形式
- 1995年から2038年までの期間に対応

### Epoch時間の計算

1970年から1995年までの時間差を計算します：

```python
# 1970年から1995年までは25年間
years = 1995 - 1970  # 25 years

# 25年間に含まれる日数
# 通常の年：365日、閏年：366日
days_per_year = 365
leap_years = 6  # 1972, 1976, 1980, 1984, 1988, 1992

# 総日数
total_days = years * days_per_year + leap_years  # 9131 days

# 秒数に変換
seconds_per_day = 24 * 60 * 60  # 86400 seconds
epoch_difference = total_days * seconds_per_day  # 788918400 seconds

# ROOT では負の値を使用（UnixのepochがROOTのepochより前）
root_offset = -788918400
```

## 時間表示の設定をしたい

### 基本的な時間表示設定

```cpp
#include <TStyle.h>
#include <TGraph.h>

TGraph *graph = new TGraph();
// ...データを充填...

// グローバル設定：Unix epoch と ROOT epoch の差
gStyle->SetTimeOffset(-788918400);

// グラフ個別設定：時間表示を有効化
graph->GetXaxis()->SetTimeDisplay(1);

// グラフ個別設定：タイムゾーンを GMT+0 に設定
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

### 時間フォーマットの指定

```cpp
#include <TStyle.h>
#include <TGraph.h>

TGraph *graph = new TGraph();
// ...データを充填...

// ISO 8601形式：年-月-日T時:分:秒
graph->GetXaxis()->SetTimeFormat("%Y-%m-%dT%H:%M:%S");

// または別の形式：年/月/日 時:分:秒
graph->GetXaxis()->SetTimeFormat("%Y/%m/%d %H:%M:%S");
```

## 異なる時間フォーマットを使いたい

### ISO 8601形式（推奨）

```cpp
#include <TStyle.h>

graph->GetXaxis()->SetTimeFormat("%Y-%m-%dT%H:%M:%S");
```

- `%Y` - 4桁の年（例：2025）
- `%m` - 2桁の月（01-12）
- `%d` - 2桁の日（01-31）
- `%H` - 2桁の時間（00-23）
- `%M` - 2桁の分（00-59）
- `%S` - 2桁の秒（00-59）

### 月日と時刻を2段に表示

```cpp
#include <TStyle.h>

// 長時間測定の場合、月日と時刻を分ける
graph->GetXaxis()->SetTimeFormat("#splitline{%m-%d}{%H:%M}");
```

複数日にわたるデータでは、日付と時刻を分けて表示すると見やすくなります。

### 日付のみを表示

```cpp
#include <TStyle.h>

graph->GetXaxis()->SetTimeFormat("%Y-%m-%d");
```

長期間のデータで、時間の詳細が不要な場合に使用します。

### 時刻のみを表示

```cpp
#include <TStyle.h>

graph->GetXaxis()->SetTimeFormat("%H:%M:%S");
```

短時間の測定データで、日付の詳細が不要な場合に使用します。

## タイムゾーンを設定したい

```cpp
#include <TStyle.h>

// GMT+0（世界標準時）
graph->GetXaxis()->SetTimeOffset(0, "gmt");

// ローカルタイム
graph->GetXaxis()->SetTimeOffset(0, "local");
```

タイムゾーンの設定がないと、軸の時間がずれることがあります。
通常は `"gmt"` を使用して、世界標準時に統一することが推奨されます。

## 実用例

### 短時間測定データ（時刻のみ）

```cpp
#include <TStyle.h>
#include <TGraph.h>

gStyle->SetTimeOffset(-788918400);

TGraph *graph = new TGraph();
// ...データを充填...

graph->GetXaxis()->SetTimeDisplay(1);
graph->GetXaxis()->SetTimeFormat("%H:%M:%S");
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

1時間以内の測定では、時刻だけで十分です。

### 1日間の測定データ（時刻と時間帯）

```cpp
#include <TStyle.h>
#include <TGraph.h>

gStyle->SetTimeOffset(-788918400);

TGraph *graph = new TGraph();
// ...データを充填...

graph->GetXaxis()->SetTimeDisplay(1);
graph->GetXaxis()->SetTimeFormat("%H:%M");
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

日中の測定では、時間と分で十分な場合が多いです。

### 複数日の測定データ（日付と時刻を2段に）

```cpp
#include <TStyle.h>
#include <TGraph.h>

gStyle->SetTimeOffset(-788918400);

TGraph *graph = new TGraph();
// ...データを充填...

graph->GetXaxis()->SetTimeDisplay(1);
graph->GetXaxis()->SetTimeFormat("#splitline{%m-%d}{%H:%M}");
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

複数日にわたるデータでは、月日と時刻を分けて表示すると見やすくなります。

### 長期観測データ（日付のみ）

```cpp
#include <TStyle.h>
#include <TGraph.h>

gStyle->SetTimeOffset(-788918400);

TGraph *graph = new TGraph();
// ...データを充填...

graph->GetXaxis()->SetTimeDisplay(1);
graph->GetXaxis()->SetTimeFormat("%Y-%m-%d");
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

数ヶ月以上の観測データでは、日付のみで十分です。

## 時間データの準備

Unixtimestampを ROOTの時間形式に変換する場合：

```cpp
#include <ctime>
#include <TGraph.h>
#include <TStyle.h>

// Unix timestamp (秒単位)
time_t unix_time = std::time(nullptr);

// ROOT epoch への変換
double root_time = unix_time + 788918400;

// グラフに設定
gStyle->SetTimeOffset(-788918400);
TGraph *graph = new TGraph();
graph->SetPoint(0, root_time, value);

graph->GetXaxis()->SetTimeDisplay(1);
graph->GetXaxis()->SetTimeFormat("%Y-%m-%d %H:%M:%S");
```

## 注意事項

- **タイムゾーン設定**: タイムゾーンを指定しないと、軸の時間がずれます。通常は `"gmt"` を使用します

- **データの時間形式**: あらかじめデータを ROOT epoch に変換しておく必要があります

- **フォーマット文字列**: `strftime` 関数の標準フォーマットに準じています

- **`#splitline`の使用**: 2行表示が必要な場合は `#splitline{上段}{下段}` の構文を使用します

## リファレンス

- [ROOT TAxis::SetTimeDisplay Documentation](https://root.cern/doc/master/classTAxis.html#aa1c42d68dac4ed7d96f2b48a7f1a0c4b)
- [ROOT TAxis::SetTimeFormat Documentation](https://root.cern/doc/master/classTAxis.html#a8b5b5e3c3e3c3e3c3e3c3e3c3e3c3e3)
- [ROOT TAxis::SetTimeOffset Documentation](https://root.cern/doc/master/classTAxis.html#ab5c5e3c3e3c3e3c3e3c3e3c3e3c3e3c)
