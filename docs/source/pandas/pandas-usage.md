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

## ファイル操作したい

```{toctree}
---
maxdepth: 1
---
pandas-read_csv
pandas-to_csv
pandas-to_json
```

## 前処理したい

```{toctree}
---
maxdepth: 1
---
pandas-dataframe
pandas-concat
pandas-to_datetime
pandas-replace
pandas-rename
pandas-sort_values
```

## 抽出したい

```{toctree}
---
maxdepth: 1
---
pandas-loc
pandas-query
pandas-drop
pandas-isna
pandas-duplicated
```

## 集計したい

```{toctree}
---
maxdepth: 1
---
pandas-astype
pandas-categorical
pandas-unique
pandas-groupby
pandas-crosstab
pandas-mean
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
