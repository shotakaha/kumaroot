# エラーバーしたい（``hvplot.errorbars``）

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

``hvplot.errorbars``は、両端のエラーバーのみを描画するため、
``hvplot.scatter``と重ね書きして中心点を描画します。

:::{seealso}

- [](../altair/altair-errorbars.md)
- [](../pandas/pandas-plot-errorbars.md)
- [](../plotly/plotly-errorbars.md)

:::

## リファレンス

- [hvplot.errorbars](https://hvplot.holoviz.org/reference/tabular/errorbars.html)
