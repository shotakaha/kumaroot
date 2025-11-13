# 統計量したい（`RDataFrame::Stats`）

```cpp
#include "ROOT/RDataFrame.hxx"
#include <iostream>

// 統計情報をまとめて取得
auto stats = df.Stats("x");
auto result = stats.GetValue();

std::cout << "Count: " << result.GetN() << std::endl;
std::cout << "Mean: " << result.GetMean() << std::endl;
std::cout << "StdDev: " << result.GetStdDev() << std::endl;
std::cout << "Min: " << result.GetMin() << std::endl;
std::cout << "Max: " << result.GetMax() << std::endl;
```

`Stats` メソッドで、指定したカラムの平均、標準偏差、最大値、最小値などを一度に計算できます。

すべての統計メソッドは**遅延実行**されるため、
`GetValue()` メソッドを呼ぶまで計算が実行されません

`Filter()` と組み合わせて、条件に合ったデータのみに対して統計量を計算できます。

```python
# 統計情報をまとめて取得
stats = df.Stats("x")
result = stats.GetValue()

print(f"Count: {result.GetN()}")
print(f"Mean: {result.GetMean()}")
print(f"StdDev: {result.GetStdDev()}")
print(f"Min: {result.GetMin()}")
print(f"Max: {result.GetMax()}")
```

## 平均値したい（`RDataFrame::Mean`）

```cpp
// 平均値を計算
auto mean_x = df.Mean("x");
std::cout << mean_x.GetValue() << std::endl;
```

```python
# 平均値を計算
mean_x = df.Mean("x")
print(mean_x.GetValue())
```

## 最大値したい（`RDataFrame::Max`）

```cpp
// 最大値
auto max_x = df.Max("x");
std::cout << max_x.GetValue() << std::endl;
```

```python
# 最大値
max_x = df.Max("x")
print(max_x.GetValue())
```

## 最小値したい（`RDataFrame::Min`）

```cpp
// 最小値
auto min_x = df.Min("x");
std::cout << min_x.GetValue() << std::endl;
```

```python
# 最小値
min_x = df.Min("x")
print(min_x.GetValue())
```

## 合計したい（`RDataFrame::Sum`）

```cpp
// 合計値
auto sum_x = df.Sum("x");
std::cout << sum_x.GetValue() << std::endl;
```

カラムのすべての値の合計を計算します。

```python
# 合計値
sum_x = df.Sum("x")
print(sum_x.GetValue())
```

## エントリ数を数えたい（`RDataFrame::Count`）

```cpp
// フィルタリング後のエントリ数
auto count = df.Filter("x > 0").Count();
std::cout << count.GetValue() << std::endl;
```

フィルタリング後のデータ件数を取得します。

```python
# フィルタリング後のエントリ数
count = df.Filter("x > 0").Count()
print(count.GetValue())
```

## 標準偏差したい（`RDataFrame::StdDev`）

```cpp
// 標準偏差（不偏推定量）
auto std_x = df.StdDev("x");
std::cout << std_x.GetValue() << std::endl;
```

データのばらつきを表す標準偏差を計算します。

```python
# 標準偏差
std_x = df.StdDev("x")
print(std_x.GetValue())
```

## 統計量メソッド一覧

| メソッド | 説明 | 戻り値 |
|---------|------|--------|
| `Count()` | エントリ数 | uint64_t |
| `Sum(col)` | 合計値 | カラムと同じ型 |
| `Mean(col)` | 平均値 | double |
| `Max(col)` | 最大値 | カラムと同じ型 |
| `Min(col)` | 最小値 | カラムと同じ型 |
| `StdDev(col)` | 標準偏差（不偏推定量） | double |
| `Stats(col)` | 複数統計情報 | TStatistic オブジェクト |

## リファレンス

- [ROOT::RDataFrame Documentation](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
