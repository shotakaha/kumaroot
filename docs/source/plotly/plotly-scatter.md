# 散布図したい（`px.scatter`）

```python
import plotly.express as px

# データを準備する
data = pd.DataFrame(...)

# 散布図を描く
fig = px.scatter(
    data,    # pd.DataFrame
    x="X軸のカラム名",
    y="Y軸のカラム名",
)
fig.show()
```

`px.scatter`で散布図を作成できます。
`data`に`pd.DataFrame`、
`x`、`y`にX軸とY軸に使うカラム名を指定します。


:::{seealso}

- [](../matplotlib/matplotlib-scatter.md)
- [](../pandas/pandas-plot-scatter.md)
- [](../altair/altair-scatter.md)
- [](../hvplot/hvplot-scatter.md)

:::

## リファレンス

- [Scatter plots with Plotly Express](https://plotly.com/python/line-and-scatter/)
