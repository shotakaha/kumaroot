# 散布図したい（``pd.DataFrame.plot.scatter``）

```python
data.plot(kind="scatter", x="X軸", y="Y軸", s="点の大きさ", c="点の色")
data.plot.scatter(x="X軸", y="Y軸", s="点の大きさ", c="点の色")
```

[pandas.DataFrame.plot.scatter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html)で散布図を作成できます。
``x``、``y``でX軸とY軸に使うカラム名を指定します。
``c``オプションで、点の色を変更できます。ヒートマップを作成したりできます。
``s``オプションで、点のサイズを変更できます。バブル図を作成できます。
オプションに[matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)のオプションも利用できます。

:::{seealso}

- [](../altair/altair-scatter.md)
- [](../hvplot/hvplot-scatter.md)
- [](../plotly/plotly-scatter.md)

:::
