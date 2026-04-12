
# 散布図したい（`.mark_circle`）

```python
import altair as alt
import pandas as pd

# データを準備する
data = pd.DataFrame(...)

# 散布図を描く
alt.Chart(data).mark_circle().encode(
    x="X軸のカラム名",
    y="Y軸のカラム名",
)
```

`mark_circle`で散布図を作成できます。
`x`、`y`でX軸とY軸に使うカラム名を指定します。

:::{seealso}

- [](../matplotlib/matplotlib-scatter.md)
- [](../pandas/pandas-plot-scatter.md)
- [](../plotly/plotly-scatter.md)
- [](../hvplot/hvplot-scatter.md)

:::

## リファレンス


- [Scatter Plot with Tooltips](https://altair-viz.github.io/gallery/scatter_tooltips.html)
- [Multifeature Scatter Plot](https://altair-viz.github.io/gallery/multifeature_scatter_plot.html)
- [Scatter Plot with Rolling Mean](https://altair-viz.github.io/gallery/scatter_with_rolling_mean.html)
- [Scatter Plot with Shaded Area](https://altair-viz.github.io/gallery/scatter_with_shaded_area.html)
- [Scatter Plot with Labels](https://altair-viz.github.io/gallery/scatter_with_labels.html)
