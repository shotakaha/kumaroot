# ヒストグラムしたい（``pandas.DataFrame.plot.hist``）

```python
data.plot(kind="hist", bins=ビン数, title="ヒストグラム")
data.plot(kind="hist", bins=ビン数, stacked=True, title="積み上げヒストグラム")
data.plot.hist(by=["カラム名"], bins=ビン数)
```

[pandas.DataFrame.plot.hist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html)を使って数値データをヒストグラムにできます。
``by``オプションにグループ化に使うカラム名を指定します。
``bins``オプションでビン数を変更できます。デフォルトは``10``になっています。
その他に[pandas.DataFrame.hist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html)と[matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist)のオプションも利用できます。

:::{note}

カラム内のデータが``str型``の場合、このメソッドは使えません（たぶん）。
あらかじめデータフレームを集計して、棒グラフ（``pandas.DataFrame.plot.bar``）を使う必要があります（たぶん）。

:::

:::{important}

ヒストグラムはいろんなことを教えてくれます。
実験で測定したデータは、まずヒストグラムにしてその分布を確認しましょう。

:::

## 統計情報を自動計算したい

```python
def hbar(data, x, bins, xmin, xmax, **kwargs):

    # x で指定したカラムのコピーを作成
    copied = data[[x]].copy()

    # Entries
    entries = len(copied)

    # Underflow
    q = f"{x} < {xmin}"
    uf = copied.query(q).count().iloc[0]

    # Overflow
    q = f"{x} > {xmax}"
    of = copied.query(q).count().iloc[0]

    # Valid
    q = f"{xmin} <= {x} <= {xmax}"
    v = copied.query(q)
    n = len(v)
    mean = v.mean().iloc[0]
    rms = v.std().iloc[0]

    stats = {
        "entries": int(entries),
        "underflow": int(uf),
        "overflow": int(of),
        "mean": mean,
        "rms": rms
        }
    plot = v.plot.hist(bins=bins, **kwargs)
    return plot, stats
```

ROOTの``TH1クラス``を真似してヒストグラムを作ってみました。
