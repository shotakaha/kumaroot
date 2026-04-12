# 散布図したい（`hvplot.scatter`）

```python
import hvplot.pandas

# データを準備する
data = pd.DataFrame(...)

# 散布図を描く
data.hvplot.scatter(
    x="X軸のカラム名",
    y="Y軸のカラム名",
)
```

`hvplot.scatter`で散布図を作成できます。
X軸とY軸に散布図に利用するカラム名を指定します。
Y軸は複数のカラム名をリストで指定できます。

:::{seealso}

- [](../matplotlib/matplotlib-scatter.md)
- [](../pandas/pandas-plot-scatter.md)
- [](../altair/altair-scatter.md)
- [](../plotly/plotly-scatter.md)

:::

## マーカーしたい（`marker`）

```python
data.hvplot.scatter(
    x=...,
    y=...,
    marker="circle",
    s=50
)
```

`marker`オプションで、マーカーの形を指定できます。
指定できるマーカーの形は[Marker reference](https://hvplot.holoviz.org/reference/markers.html)を参照してください。
`marker`オプションでマーカーの形を指定した場合、マーカーの大きさは`s`オプションで指定できます。

## カラーマップしたい（`c` / `cmap`）

```python
data.hvplot.scatter(
    x=...,
    y=...,
    c="色に使うカラム名",
    cmap="viridis",
)
```

`c`オプションで、マーカー色に使うカラム名を指定できます。
`cmap`オプションで、カラーマップのパターンを指定できます。
指定できるカラーマップのパターンは[colormap reference](https://hvplot.holoviz.org/reference/colormaps.html)を参照してください。

## 重ね書きしたい

```python
import hvplot.pandas

names = ["X軸", "Y軸1", "Y軸2"]
data[names].hvplot.scatter(x="X軸", grid=True)
```

共通のX軸に対して、複数のY軸の値を描画したい（＝重ね書きしたい）場合、
データフレームのカラム名を絞り込むのが一番簡単だと思います。
`x="X軸"`を指定しない場合は、インデックスが適用されます。

## リファレンス

- [Scatter - hvplot.holoviz.org](https://hvplot.holoviz.org/reference/tabular/scatter.html)
- [hvPlot.scatter - hvplot.holoviz.org](https://hvplot.holoviz.org/en/docs/latest/ref/api/manual/hvplot.hvPlot.scatter.html)
