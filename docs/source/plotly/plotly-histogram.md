# ヒストグラムしたい（`px.histogram`）

```python
import plotly.express as px

# データを準備する
data = pd.DataFrame(...)

# ヒストグラムを描く
fig = px.histogram(
    data,    # pd.DataFrame
    x="ヒストグラムに使うカラム名",
    nbins=10,  # ビンの数
    range_x=(0, 100)  # ビンの範囲
)
fig.show()
```

`px.histogram`でヒストグラムを作成できます。
`data`に`pd.DataFrame`、`x`にヒストグラムに使うカラム名を指定します。
`nbins`でビンの数を、`range_x`でビンの範囲を指定できます。

:::{seealso}

- [](../matplotlib/matplotlib-hist.md)
- [](../pandas/pandas-plot-hist.md)
- [](../altair/altair-histogram.md)
- [](../hvplot/hvplot-hist.md)

:::

## リファレンス

- [plotly.express.histogram](https://plotly.com/python-api-reference/generated/plotly.express.histogram.html)
