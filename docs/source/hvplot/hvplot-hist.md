# ヒストグラムしたい（``hvplot.hist``）

```python
import pandas as pd
import hvplot.pandas

# data : pd.DataFrame
data.hvplot.hist(
    y = "energy_deposit",
    xlabel="Energy Deposit [MeV]")
```

``hvplot.hist``でヒストグラムを作成できます。
``y``に連続値をとるカラムを指定します。

:::{hint}

離散値（カテゴリカル）なカラムを指定したい場合は、
``hvplot.bar``を使います。

:::

Altairと比べて直感的に記述できるため、とても簡単です。

:::{seealso}

- [](../altair/altair-histogram.md)
- [](../pandas/pandas-plot-hist.md)
- [](../plotly/plotly-histogram.md)

:::

## 引数

公式のAPIドキュメントが見つからなかったため、ベタ書きしておきます。

```python
data.hvplot.hist(
    y: str | list,    # カラム名 / 連続値
    by: str | list,   # カラム名 / グループ化
    bins: int,        # ビン数
    bin_range: tuple = None,   # ビンの範囲
    normed: bool = False,      # 規格化
    cumulative: bool = False,  # 累積
    alpha: float = 1.0         # 透過度
)
```

## タイトルしたい（``title``）

```python
data.hvplot.hist(title="タイトル")
data.hvplot.hist(fontsize={"title": "15pt"})
```

## 軸したい（``xlabel`` / ``ylabel`` / ``clabel``）

```python

data.hvplot.hist(xlabel="x軸のタイトル")
data.hvplot.hist(xaxis="bottom")
data.hvplot.hist(xaxis="top")
data.hvplot.hist(ylabel="y軸のタイトル")
data.hvplot.hist(yaxis="left")
data.hvplot.hist(yaxis="right")
data.hvplot.hist(clabel="z軸のタイトル")
data.hvplot.hist(xticks=5, xformatter="%.3f")
data.hvplot.hist(yticks=5, yformatter="%.3f")
data.hvplot.hist(rot=45)
data.hvplot.hist(shared_axis=True)
```

``xlabel``、``ylabel``、``clabel``で軸のタイトルを変更できます。
``xaxis``、``yaxis``で軸を表示する位置を変更できます。
``xticks``、``yticks``で軸目盛りの間隔を変更できます。
また、``xformatter``、``yformatter``で目盛り表示のフォーマットを変更できます。

## 凡例したい（``legend``）

```python
data.hvplot.hist(legend=True)
data.hvplot.hist(legend="top")
data.hvplot.hist(legend="bottom")
data.hvplot.hist(legend="left")
data.hvplot.hist(legend="right")
```

凡例の表示／非表示を変更できます。
また、表示位置を変更できます。

## 対数したい

```python
data.hvplot.hist(logx=True)    # 片対数（x軸）
data.hvplot.hist(logy=True)    # 片対数（y軸）
data.hvplot.hist(logz=True)    # 片対数（z軸）
data.hvplot.hist(loglog=True)  # 両対数（x軸とy軸）
```

``logx``、``logy``、``logz``で片対数グラフに変更できます。
また、``loglog``で両対数グラフにできます。


## キャンバスしたい

```python
data.hvplot.hist(width=700, height=300)
data.hvplot.hist(max_width=700, max_height=700)
data.hvplot.hist(min_width=300, min_height=300)
data.hvplot.hist(responsive=True)
data.hvplot.hist(frame_width=500, frame_height=500)
data.hvplot.hist(padding=0.1)
data.hvplot.hist(grid=True)
data.hvplot.hist(bgcolor=None)
```

## 範囲したい

```python
data.hvplot.hist(xlim=(0, 500))
data.hvplot.hist(ylim=(0, 500))
data.hvplot.hist(clim=(0, 500))
```

x軸、y軸、z軸（＝カラーバー）の範囲を変更できます。

## カラーバーしたい

```python
data.hvplot.hist(colorbar=True)
data.hvplot.hist(cnorm="linear")
data.hvplot.hist(cnorm="log")
data.hvplot.hist(cnorm="eq_hist")
```

## フォントしたい（``fontsize`` / ``fontscale``）

```python
data.hvplot.hist(fontsize=15)
data.hvplot.hist(fontsize={"title": "15pt", "ylabel": "5pt", "ticks": 20})
data.hvplot.hist(fontscale=1.5)
```

``fontsize``でフォントサイズを変更できます。
辞書を使って、要素ごとにサイズを変更できます。
``fontscale``ですべてのフォントサイズをスケールできます。

## リファレンス

- [Hist](https://hvplot.holoviz.org/reference/tabular/hist.html)
