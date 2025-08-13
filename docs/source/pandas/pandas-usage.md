# Pandasの使い方

```python
import pandas as pd
import matplotlib.pyplot as plt
```

```{toctree}
---
maxdepth: 1
---
pandas-install
pandas-import
```

## データフレームを作成したい

```{toctree}
---
maxdepth: 1
---
pandas-dataframe
pandas-from_dict
pandas-from_list
pandas-from_numpy
pandas-from_records
pandas-copy
```

## データを読み込みたい

```{toctree}
---
maxdepth: 1
---
pandas-read_csv
```

## データを保存したい

```{toctree}
---
maxdepth: 1
---
pandas-to_csv
pandas-to_json
```

## データを確認したい

```{toctree}
---
maxdepth: 1
---
pandas-head
pandas-tail
pandas-info
pandas-describe
pandas-shape
pandas-columns
pandas-dtypes
pandas-isna
pandas-duplicated
pandas-unique
```

## データを選択したい

```{toctree}
---
maxdepth: 1
---
pandas-loc
pandas-query
pandas-sample
```

## データを整形したい

```{toctree}
---
maxdepth: 1
---
pandas-replace
pandas-astype
pandas-categorical
pandas-to_datetime
pandas-rename
pandas-drop
pandas-dropna
pandas-fillna
pandas-drop_duplicates
```

## データを変換したい

```{toctree}
---
maxdepth: 1
---
pandas-groupby
pandas-pivot_table
pandas-merge
pandas-concat
pandas-apply
pandas-sort_values
```

## 集計したい

```{toctree}
---
maxdepth: 1
---
pansas-sum
pandas-mean
pandas-var
pandas-std
pandas-skew
pandas-kurt
pandas-count
pandas-value_counts
pandas-crosstab
```

## 度数分布したい

```{toctree}
---
maxdepth: 1
---
pandas-cut
```

## フィットしたい

フィットには[SciPy](https://scipy.org/)や[NumPy](https://numpy.org/ja/)を使います。

```{toctree}
---
maxdepth: 1
---
pandas-fit-curve_fit
pandas-fit-gaussian
pandas-fit-erfc
pandas-fit-poisson
pandas-interpolate-spline
pandas-lmfit
```

## 可視化したい

データの可視化にはデフォルトで[matplotlib](https://matplotlib.org/)を使います。

```{toctree}
---
maxdepth: 1
---
pandas-plot
pandas-plot-hist
pandas-plot-scatter
pandas-plot-errorbars
```

``pandas.DataFrame``と連携できる可視化ツールもいろいろあります。
これまで使ったことがあるツールは、
[](../matplotlib/matplotlib-usage.md)、
[](../altair/altair-usage.md)、
[](../plotly/plotly-usage.md)、
[](../hvplot/hvplot-usage.md)
にそれぞれ整理しました。

## リファレンス

- [Pandas公式ドキュメント](https://pandas.pydata.org/docs/)
- [note.nkmk.me](https://note.nkmk.me/pandas/)
