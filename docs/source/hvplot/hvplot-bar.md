# 棒グラフしたい（`hvplot.bar`）

```python
import hvplot.pandas

data.hvplot.bar(x="離散値", y="連続値")
data.hvplot.bar(y="連続値")
```

`hvplot.bar`で棒グラフを作成できます。
X軸に離散値（カテゴリカルな値）、
Y軸に連続値（数値）を指定します。
X軸を省略すると、データフレームのインデックスが使われます。

## ヒストグラムしたい

```python
data["離散値"].value_counts(sort=False).hvplot.bar()
```

[pd.DataFrame.sort_values](../pandas/pandas-sort_values.md)と組み合わせて、
離散値（カテゴリカルな値）を持つカラムの頻度を
比較的簡単に可視化できます。

## 積み上げグラフしたい

```python
g = ["カラム1", "カラム2"]
data.groupby(g).count().hvplot.bar()
data.groupby(g).count().hvplot.bar(stacked=True)
```

マルチインデックを持つデータフレームも棒グラフにできます。
``stacked=True``で積み上げグラフにできます。

## 色を変更したい（``color``）

```python
data.hvplot(color="色名")
data.hvplot(color="カラム名")
data.groupby(g).count().hvplot.bar(color=["色1", "色2"])
```

``color``で棒グラフの色を変更できます。
色名はカラーコードで設定します。

また、データフレームのカラム名の値を設定したり、
マルチインデックスの数だけリストで指定したりできます。

## リファレンス

- [Bar - hvplot.holoviz.org](https://hvplot.holoviz.org/reference/tabular/bar.html)
- [Barh - hvplot.holoviz.org](https://hvplot.holoviz.org/reference/tabular/barh.html)
