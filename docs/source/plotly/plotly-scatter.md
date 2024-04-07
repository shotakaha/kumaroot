# 散布図したい（``px.scatter``）

```python
import plotly.express as px
fig = px.scatter(
    data,    # pd.DataFrame
    x="X軸のカラム名",
    y="Y軸のカラム名",
)
fig.show()
```

:::{seealso}

- [](../altair/altair-scatter.md)
- [](../hvplot/hvplot-scatter.md)
- [](../pandas/pandas-plot-scatter.md)

:::

## リファレンス

- [Scatter plots with Plotly Express](https://plotly.com/python/line-and-scatter/)
