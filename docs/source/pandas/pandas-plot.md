# グラフしたい（``pandas.DataFrame.plot``）

```python
data.plot()
data.plot(
    title="グラフのタイトル",
    xlabel="X軸のタイトル",
    ylabel="Y軸のタイトル"
)
```

[pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)を使って、データフレームからグラフを作成できます。
デフォルトで、数値データのみのカラムがすべて折れ線グラフで表示されます。

このメソッドは``matplotlib``のラッパー的なものなので、``matplotlib``のインストールが必要です。
巷では``matplotlib``を使ってグラフを作成するサンプルが多いですが、
さくっと確認したい場合は、このメソッドで十分だと思います。

## グラフの種類を変更したい

```python
data.plot(kind="hist")
data.plot(kind="scatter", x="xカラム", y="yカラム")
```

``kind``オプションでグラフの種類を変更できます。
指定できるグラフの種類は``bar``、``hist``、``scatter``など全11種類あります。
散布図（``scatter``）など、一部のグラフ種類ではX軸、Y軸の指定が必要です。

## ヒストグラムしたい（``pd.DataFrame.plot.hist``）

```python
data.plot(kind="hist", bins=ビン数)
data.plot.hist(by=["カラム名"], bins=ビン数)
```

[pandas.DataFrame.plot.hist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html)でヒストグラムを作成できます。
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
data.plot(kind="scatter", x="X軸", y="Y軸", s="点の大きさ", c="点の色")
data.plot.scatter(x="X軸", y="Y軸", s="点の大きさ", c="点の色")
```

[pandas.DataFrame.plot.scatter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html)で散布図を描画できます。
オプションに[matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)のオプションも利用できます。

## その他のグラフ

実際に使う時ができたら追記します。

1. [pandas.DataFrame.plot.area](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.area.html): 面グラフ
1. [pandas.DataFrame.plot.bar](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html): 棒グラフ。重みのついたヒストグラムとしても使えるはず。
1. [pandas.DataFrame.plot.barh](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.barh.html): 棒グラフ（横）
1. [pandas.DataFrame.plot.box](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.box.html): 箱ひげ図。
1. [pandas.DataFrame.plot.hexbin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hexbin.html): マス目が六角形の図。ヒートマップを作るとカッコ良さそう。六角形にするのに見た目以外の意味はあるのだろうか？
1. [pandas.DataFrame.plot.density](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.density.html): ガウシアンを仮定したKDE分布関数
1. [pandas.DataFrame.plot.kde](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.kde.html): 上とどう違うんだろう？
1. [pandas.DataFrame.plot.line](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.line.html): 折れ線グラフ
1. [pandas.DataFrame.plot.pie](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.pie.html): 円グラフ
