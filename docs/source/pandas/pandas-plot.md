# グラフしたい（``pd.DataFrame.plot``）

```python
data.plot(
    data=データフレーム,
    x="x軸名",
    y="y軸名",
    kind="グラフの種類"
    )
```

[pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)を使って、データフレームからグラフを作成できます。
``kind``オプションで指定できるグラフの種類は``bar``、``hist``、``scatter``など全11種類あります。
それぞれの種類に対応した簡易メソッドもあります。

このメソッドは``matplotlib``のラッパー的なものなので、``matplotlib``のインストールが必要です。
巷では``matplotlib``を使ってグラフを作成するサンプルが多いですが、
さくっと確認したい場合は、このメソッドで十分だと思います。

## ヒストグラムしたい（``pd.DataFrame.plot.hist``）

```python
data.plot.hist(by=["カラム名"], bins=ビン数)
```

[pandas.DataFrame.plot.hist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html)でヒストグラムを描画できます。
``by``オプションにグループ化に使うカラム名を指定します。
``bins``オプションでビン数を変更できます。デフォルトは``10``になっています。
その他に[pandas.DataFrame.hist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html)と[matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist)のオプションも利用できます。

:::{note}

測定したデータをヒストグラムにして分布を確認することは、実験解析の一歩目です。
データがきちんと取得できたかを判断したり、
解析の条件をいろいろと考えたりするときに、
測定データの基本分布を理解しないまま進んではいけません。

:::

## 散布図したい（``pd.DataFrame.plot.scatter``）

```python
data.plot.scatter(x="x軸名", y="y軸名", s="サイズ", c="色")
```

[pandas.DataFrame.plot.scatter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html)で散布図を描画できます。
オプションに[matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)のオプションも利用できます。


