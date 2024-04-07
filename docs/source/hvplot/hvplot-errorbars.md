# エラーバーしたい（``hvplot.errorbars``）

```python
import hvplot.pandas
data.hvplot.scatter(x="Xの値", y="Yの値") * data.hvplot.errorbars(y="Yの値", yerr1="Yの誤差)
```

ベースとなる図にエラーバー付きの図を重ね書きします。

:::{seealso}

- [](../altair/altair-errorbars.md)
- [](../pandas/pandas-plot-errorbars.md)
- [](../plotly/plotly-errorbars.md)

:::

## リファレンス

- [hvplot.errorbars](https://hvplot.holoviz.org/reference/tabular/errorbars.html)
