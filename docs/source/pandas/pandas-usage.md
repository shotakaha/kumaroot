# Pandasの使い方

```python
import pandas as pd
import matplotlib.pyplot as plt
```

`Pandas`は、Pythonでデータ分析をするためのライブラリです。
データの読み込み、整形、変換、集計、可視化など、データ分析に必要な機能が豊富に用意されています。
データフレーム（`pandas.DataFrame`）を中心に、
データを操作するためのさまざまなメソッドが提供されています。
データ分析の目的に応じて、適切なメソッドを選択して使うことが重要です。

また、Pandasは内部で`NumPy`を利用しています。
`NumPy`は、Pythonでの数値計算の基盤となるライブラリです。
`math`モジュールがスカラー値の計算に特化しているのに対して、
`NumPy`は多次元配列（`numpy.ndarray`）やベクトルの計算を効率的に行うことができます。

さらに、`SciPy`は、`NumPy`を基盤とした科学技術計算ライブラリです。
統計分析（`scipy.stats`）や
最適化（`scipy.optimize`）、
数値積分（`scipy.integrate`）、
信号処理（`scipy.signal`）など、
さまざまな分野に対応したモジュールが用意されています。
これらの計算を自分で実装することで理解を深めることもできますが、
SciPyの実装やAPIを活用することで効率的に高度な解析を行うことができます。

このドキュメントでは、`Pandas`を中心としたデータ分析の基本的な使い方を紹介します。
必要に応じて、`NumPy`や`SciPy`の機能も併せて紹介します。

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
pandas-sum
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
pandas-plot-box
pandas-plot-area
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
