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

## マーカーしたい（`marker`）

```python
fig = px.scatter(
    data,
    x=...,
    y=...,
    marker="circle",
    size=50
)
fig.show()
```

`marker`オプションで、マーカーの形を指定できます。
指定できるマーカーの形は[Marker reference](https://plotly.com/python/marker-style/)を参照してください。
`marker`オプションでマーカーの形を指定した場合、マーカーの大きさは`size`オプションで指定できます

## カラーマップしたい（`color` / `color_continuous_scale`）

```python
fig = px.scatter(
    data,
    x=...,
    y=...,
    color="色に使うカラム名",
    color_continuous_scale="Viridis",
)
fig.show()
```

`color`オプションで、マーカー色に使うカラム名を指定できます。
`color_continuous_scale`オプションで、カラーマップのパターンを指定できます。
指定できるカラーマップのパターンは[colormap reference](https://plotly.com/python/builtin-colorscales/)を参照してください。

## リファレンス

- [plotly.express.scatter](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html)
- [Scatter plots with Plotly Express](https://plotly.com/python/line-and-scatter/)
- [Marker style](https://plotly.com/python/marker-style/)
- [Built-in color scales](https://plotly.com/python/builtin-colorscales/)
