# 散布図したい（`matplotlib.pyplot.scatter`）

```python
import numpy as np
import matplotlib.pyplot as plt

# データを準備する
xdata = data["x"]
ydata = data["y"]
sizes = data["sizes"]
colors = data["colors"]

# Figureエリアを作成
fig, ax = plt.subplots()

# 散布図
sc = ax.scatter(
    x=xdata,
    y=ydata,
    s=sizez,
    c=colors,
    cmap="viridis",
    vmin=0,
    vmax=10,
    label="凡例に使う名前",
)

# axesの設定
ax.set(
    xlim=(0, 8),
    xticks=np.arange(1, 8),
    ylim=(0, 8),
    ytics=np.arange(1, 8),
)
ax.grid(True)

fig.colorbar(sc, ax=ax)
ax.legend()

plt.show()
```

[Axes.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html)で散布図を作成できます。
X軸（``x``）、Y軸（``y``）、マーカーの大きさ（``s``）や色（``c``）の値は、
あらかじめデータフレームで整えておくとよいです。

カラーマップの上限と下限はそれぞれ``vmin``と``vmax``で設定できます。
``cmap``オプションで設定できる配色パターン名は[colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html)を参照してください。

:::{seealso}

- [](../altair/altair-scatter.md)
- [](../hvplot/hvplot-scatter.md)
- [](../pandas/pandas-plot-scatter.md)
- [](../plotly/plotly-scatter.md)

:::

## リファレンス

- [matplotlib.pyplot.scatter - matplotlib.org](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
- [matplotlib.axes.Axes.scatter - matplotlib.org](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html)
- [scatter(x,y) - matplotlib.org](https://matplotlib.org/stable/plot_types/basic/scatter_plot.html)
- [colormap reference - matplotlib.org](https://matplotlib.org/stable/gallery/color/colormap_reference.html)
