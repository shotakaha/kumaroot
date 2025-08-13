# 散布図したい（`hvplot.scatter`）

```python
import hvplot.pandas
data.hvplot.scatter(
    x="X軸のカラム名",
    y="Y軸のカラム名",
    )
```

`hvplot.scatter`で散布図を作成できます。
X軸とY軸に散布図に利用するカラム名を指定します。
Y軸は複数のカラム名をリストで指定できます。

:::{seealso}

- [](../altair/altair-scatter.md)
- [](../pandas/pandas-plot-scatter.md)
- [](../plotly/plotly-scatter.md)

:::

## マーカーしたい

```python
data.hvplot.scatter(x=..., y=..., marker="circle", s=50)
```

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
