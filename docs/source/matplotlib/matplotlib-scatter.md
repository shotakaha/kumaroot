# 散布図したい（`matplotlib.axes.Axes.scatter`）

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
    s=sizes,
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
    yticks=np.arange(1, 8),
)
ax.grid(True)

fig.colorbar(sc, ax=ax)
ax.legend()

plt.show()
```

`Axes.scatter`で散布図を作成できます。
X軸（`x`）とY軸（`y`）の値を配列で指定します。
オプションでマーカーの大きさ（`s`）や色（`c`）を変更できます。

カラーマップの上限と下限はそれぞれ``vmin``と``vmax``で設定できます。
``cmap``オプションで設定できる配色パターン名は[colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html)を参照してください。

:::{seealso}

- [](../pandas/pandas-plot-scatter.md)
- [](../altair/altair-scatter.md)
- [](../plotly/plotly-scatter.md)
- [](../hvplot/hvplot-scatter.md)

:::

## マーカーしたい（`s`）

```python
sc = ax.scatter(
    x=xdata,
    y=ydata,
    s=sizes,
    marker="o",
)
```

`marker`オプションで、マーカーの種類を変更できます。
マーカーの大きさは`s`オプションで変更できます。

たとえば、y軸の値に応じてマーカーの大きさを変えたい場合、
あらかじめ`sizes=math.sqrt(ydata)`のようにマーカーの大きさを計算しておき、
`s=sizes`と指定します。

:::{note}

上記のように、マーカーの大きさ（＝円の面積）で大小を分かりやすく表現することはよくあります。
円の面積は半径の2乗に比例するので、マーカーの大きさは**値の平方根に比例**させる必要があります。
値に比例させてしまうと、視覚的に得られる印象が実際の値より大きくなってしまい、誤解を招く可能性があります。

:::

## カラーマップしたい（`cmap`）

```python
import matplotlib.pyplot as plt

# キャンバスを作成
fig, ax = plt.subplots()

# 散布図を作成
sc = ax.scatter(
    x=xdata,
    y=ydata,
    c=colors,
    cmap="viridis",
    vmin=0,
    vmax=10,
)
```

`cmap`オプションで、マーカーの色のカラーマップを変更できます。
z軸の値を色で表現したい場合は、`c`オプションでz軸の値を指定し、`cmap`オプションでカラーマップを指定します。
カラーマップの上限値と下限値はそれぞれ``vmin``と``vmax``で設定できます。

## リファレンス

- [matplotlib.pyplot.scatter - matplotlib.org](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
- [matplotlib.axes.Axes.scatter - matplotlib.org](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html)
- [scatter(x,y) - matplotlib.org](https://matplotlib.org/stable/plot_types/basic/scatter_plot.html)
- [colormap reference - matplotlib.org](https://matplotlib.org/stable/gallery/color/colormap_reference.html)
