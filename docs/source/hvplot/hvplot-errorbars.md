# エラーバーしたい（`hvplot.errorbars`）

```python
errors = data.hvplot.errorbars(
    x="X軸のカラム名",
    y="Y軸のカラム名",
    yerr1="Y軸のエラーのカラム名",
    color="black",
    line_width=1,
)

# 基本プロットを作成
lines = data.hvplot.line(...)

# プロットを重ねる
charts = (lines * errors)
charts
```

`hvplot.errorbars`でエラーバーを作成できます。
`y`に中心値、`yerr1`にエラーの大きさのカラム名を指定します。
エラーバーのみが描画されるため、
別に作成した基本プロット（`hvplot.line`や`hvplot.scatter`）の上に重ね書きする必要があります。

:::{seealso}

- [](../altair/altair-errorbars.md)
- [](../pandas/pandas-plot-errorbars.md)
- [](../plotly/plotly-errorbars.md)

:::

## 非対称エラーバーしたい

```python
errors = data.hvplot.errorbars(
    x="X軸のカラム名",
    y="Y軸のカラム名",
    yerr1="+方向のエラーの大きさ",
    yerr2="-方向のエラーの大きさ",
    color="black",
    line_width=1,
)
```

エラーの大きさが非対称な場合は、`yerr1`と`yerr2`にそれぞれ指定します。

## エラーを計算したい

```python
import hvplot.pandas

g = ["x"]
v = "y"
grouped = data.groupby(g)[v].agg(["mean", "std"]).reset_index()

mark = grouped.hvplot.scatter(x="x", y="mean")
errors = grouped.hvplot.errorbars(x="x", y="mean", yerr1="std")
mark * errors
```

データフレームを整理し、平均値と標準偏差を計算します。
``pd.DataFrame.agg``を使うと、``mean``と``std``を一度に取得できます。




## リファレンス

- [hvplot.errorbars](https://hvplot.holoviz.org/reference/tabular/errorbars.html)
- [hvPlot.errorbars - hvplot.holoviz.org](https://hvplot.holoviz.org/en/docs/latest/ref/api/manual/hvplot.hvPlot.errorbars.html#hvplot.hvPlot.errorbars)
