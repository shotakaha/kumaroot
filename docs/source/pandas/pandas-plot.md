# グラフしたい（``plot``）

```python
data.plot(data=データフレーム, x="x軸名", y="y軸名", kind="グラフの種類")
```

[pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)を使ってグラフを作成できます。
グラフ描画に``matplotlib``が必要なので、追加でインストールしてください。
グラフの種類は``kind``オプションで指定します。
また、それぞれの種類に対応した簡易メソッドもあります。

## 散布図したい（``plot.scatter``）

```python
data.plot.scatter(x="x軸名", y="y軸名", s="サイズ", c="色")
```

散布図を描く場合は[pandas.DataFrame.plot.scatter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html)を使います。
[matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)のオプションも指定できます。
