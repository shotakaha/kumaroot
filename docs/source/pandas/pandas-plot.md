# グラフしたい（``pandas.DataFrame.plot``）

```python
import pandas
import matplotlib.pyplot as plt
import japanize_matplotlib

fig, axs = plt.subplots()
data.plot(ax=axs)
fig.savefig("ファイル名")
```

[pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)を使って、データフレームからグラフを作成できます。
デフォルトで、数値データのみのカラムがすべて折れ線グラフで表示されます。

このメソッドは``matplotlib``のラッパー的なものなので、``matplotlib``のインポートが必要です。
また、日本語を表示したい場合は``japanize_matplotlib``をインポートするとよいです。

:::{note}

検索すると``matplotlib``（``matplotlib.pyplot``）を使ってグラフを作成する記事が多くヒットします。
せっかくPandasを使っているので、ここではできるだけPandasを使った方法を試してみようと思います。

:::

## 種類を変更したい（``kind``）

```python
data.plot(kind="hist")
data.plot(kind="scatter", x="x軸のカラム名", y="Y軸のカラム名")
```

``kind``オプションでグラフの種類を変更できます。
指定できるグラフの種類はヒストグラム（``hist``）、散布図（``scatter``）、棒グラフ（``bar``）、箱ひげ図（``box``）など全11種類あります。

散布図（``scatter``）など、一部のグラフ種類ではX軸、Y軸の指定が必要です。

## タイトルしたい（``title`` / ``xlabel`` / ``ylabel``）

```python
data.plot(
    title="グラフのタイトル",
    xlabel="X軸のタイトル",
    ylabel="Y軸のタイトル",
    )
```

``title``、``xlabel``、``ylabel``オプションで、グラフのタイトルや軸タイトルを表示できます。
``japanize_matplotlib``をインポートするだけで、日本語フォントを扱えるようになります。

:::{important}

軸タイトルは単位も含めて設定しておくとよいです。

:::

## サブプロットしたい（``subplots``）

```python
data.plot(subplots=True)

data.plot(
    subplots=True,
    figsize=(横サイズ, 縦サイズ),
    layout=(行数, 列数),
    )
```

``subplots=True``オプションで、複数のカラムのデータをそれぞれのサブプロットに表示できます。
``figsize``オプションで図の全体サイズを変更できます。横サイズ／縦サイズの単位は``inch``です（``dpi=72``）。
``layout``オプションでサブプロットの行数と列数を変更できます。デフォルトは縦配置です。
サブプロットの詳細は[matplotlib.pyplot.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)も参照してください。

## 目盛りしたい（``grid``）

```python
data.plot(grid=True)

data.plot(
    grid=True,
    xticks=range(0, 1000, 50),
    yticks=range(-5, 15, 1)
    )
```

``grid=True``オプションで、目盛り（補助目盛り）を表示できます。
``xticks``、``yticks``オプションで目盛り間隔を変更できます。
目盛りの詳細は[matplotlib.pyplot.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)も参照してください。

## 表示範囲したい（``xlim`` / ``ylim``）

```python
data.plot(
    xlim=(x軸の下限値, x軸の上限値),
    ylim=(y軸の下限値, y軸の上限値)
    )
```

``xlim``、``ylim``オプションで、X軸とY軸それぞれの下限値と上限値を変更できます。

## 対数グラフしたい（``logx`` / ``logy`` / ``loglog``）

```python
data.plot(logx=True)
data.plot(logy=True)
data.plot(loglog=True)
```

``logx=True``、``logy=true``、``loglog=True``オプションで片対数グラフや両対数グラフに変更できます。
``loglog=True``は``logx=True, logy=True``と同等です。

## 詳細設定したい（``ax``）

```python
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを用意する（ここでは省略）
# data: pd.DataFrame

# matplotlib.pyplotで FigureとAxesオブジェクトを作成する
fig, axs = plt.subplots()

# pandasでプロットを作成する
data.plot(
    kind="scatter",
    x="X軸のカラム名",
    y="Y軸のカラム名",
    ax=axs  # 描画先のAxesオブジェクトを指定する
    )
```

``ax``オプションで``matplotlib``の``Axes``オブジェクトを指定できます。
グラフをより詳細に設定したい場合は、[matplotlib.pyplot.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html)に対して変更を加えます。

:::{seealso}

``matplotlib``の使い方は、まず、公式ドキュメントの[The lifecycle of a plot](https://matplotlib.org/stable/tutorials/lifecycle.html)に目を通すのがよいと思います。
とくに[A note on the explicit vs implicit interfaces](https://matplotlib.org/stable/tutorials/lifecycle.html#a-note-on-the-explicit-vs-implicit-interfaces)は、ウェブに転がっている他のコードを読むのに役立つ情報だと思います。

:::

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
