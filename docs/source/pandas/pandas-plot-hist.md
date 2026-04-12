# ヒストグラムしたい（`pandas.DataFrame.plot.hist`）

```python
import pandas as pd

# データを準備する
data = pd.DataFrame(...)

# ヒストグラムを描く
data.plot.hist(
  bins=ビン数,
  range=(ヒストグラムの下限値, ヒストグラムの上限値),
  title="ヒストグラム",
  xlabel="X軸のタイトル",
  ylabel="Y軸のタイトル"
)
```

`pd.DataFrame.plot.hist`でヒストグラムを作成できます。
オプションでビン数やヒストグラムの範囲、タイトルや軸のタイトルを変更できます。

`bins`オプションでビン数を変更できます。デフォルトは``10``になっています。
`range`オプションでヒストグラムの範囲を変更できます。
デフォルトは、データの最小値と最大値が自動的に設定されます。

:::{important}

データ分析するときは、まずヒストグラムを作ってデータの分布を確認しましょう。
ヒストグラムは、データの分布を視覚的に理解するための基本的なツールです。
データの分布を理解することで、適切な統計手法を選択したり、データの特徴を把握したりできます。

:::

:::{caution}

ヒストグラムは、連続的な数値データをビンに分割して、その頻度を表示するグラフです。
カラム内のデータに文字列（`str`）が含まれている場合、このメソッドは使えません（たぶん）。

カテゴリカルデータをヒストグラムで表現したい場合は、あらかじめデータフレームを集計して、棒グラフ（``pandas.DataFrame.plot.bar``）を使う必要があります。

:::

:::{seealso}

- [](../altair/altair-histogram.md)
- [](../hvplot/hvplot-hist.md)
- [](../plotly/plotly-histogram.md)

:::

## ビニングしたい（`bins` / `range`）

```python
# 任意のビニング
bins = [0, 10, 30, 50, 70, 80]

data.plot.hist(
    bins=bins,
    range=(0, 100),
)
```

`bins`オプションでビン数を変更できます。デフォルトは`10`になっています。
リストを指定すれば、任意の間隔でビニングできます。

`range`オプションでヒストグラムの範囲を変更できます。
デフォルトは、データの最小値と最大値が自動的に設定されます。

:::{caution}

`range`はヒストグラムに使用するデータの範囲を制限するオプションです。
範囲外のデータは集計対象から除除されます。

アンダーフローやオーバーフローとして集計されないので注意してください。

:::

## 累積したい（`cumulative`）

```python
data.plot.hist(
    cumulative=True,
    bins=ビン数,
    range=(xmin, xmax)
)

# matplotlibで設定する場合
fig, ax = plt.subplots()
ax.hist(
    data,
    bins=ビン数,
    range=(xmin, xmax),
    cumulative=True
)
```

`cumulative=True`オプションで、累積ヒストグラムを作成できます。

## 規格化したい（`density`）

```python
data.plot.hist(
    density=True,
    bins=ビン数,
    range=(xmin, xmax)
)
```

`density=True`オプションで、ヒストグラムを規格化できます。
規格化すると、ヒストグラムの面積が1になるように調整されます。

## ログ表示したい（`log`）

```python
data.plot.hist(
    log=True,
    bins=ビン数,
    range=(xmin, xmax)
)
```

`log=True`オプションで、Y軸をログ表示にできます。
頻度の値が大きく異なる場合に、ログ表示にすることで全体の傾向を見やすくできます。

## グループ化したい（`by`）

```python
data.plot.hist(
    by="グループ化したいカラム名",
    bins=ビン数,
    range=(xmin, xmax)
)

# data.groupbyした場合
grouped = data.groupby("グループ化したいカラム名")
grouped.plot.hist(
    bins=ビン数,
    range=(xmin, xmax)
)
```

`by`オプションで、指定したカラムの値ごとにグループ化してヒストグラムを作成できます。
グループ化されたヒストグラムは、同じグラフ内に重ねて表示されます。
グループごとに色分けされるので、グループごとの分布の違いを視覚的に比較できます。

:::{note}

`by`オプションは、内部的には`groupby`してからヒストグラムを作成しているだけなので、あらかじめ`groupby`してからヒストグラムを作成することもできます。

:::

## 積み上げたい（`stacked`）

```python
data.plot.hist(
    by="グループ化したいカラム名",
    bins=ビン数,
    range=(xmin, xmax),
    stacked=True
)
```

`stacked=True`オプションで、グループ化したヒストグラムを積み上げて表示できます。

## 統計情報を自動計算したい

```python
def hbar(
    data: pd.DataFrame,
    header: str,
    *,
    bins: int = 50,
    xmin: float = 0,
    xmax: float = 100,
    ax: plt.Axes | None = None,
    **kwargs
) -> tuple[plt.Axes, dict]:
    """
    ROOTのTH1風ヒストグラム関数
    """
    # データを抽出
    d = data[header]

    # Axesを作成
    if ax is None:
        fig, ax = plt.subplots()

    # underflow data: d < xmin
    uf = (d < xmin).sum()

    # overflow data: d > xmax
    of = (d > xmax).sum()

    # valid data: within the range
    valid = d[(d >= xmin) & (d <= xmax)]

    # histogram
    h = ax.hist(
      valid,
      bins=bins,
      range=(xmin, xmax),
      **kwargs
    )

    # statistics: ROOT-like
    total_entries = int(len(d))
    valid_entries = int(len(valid))
    underflow = int(uf)
    overflow = int(of)
    mean = float(valid.mean()) if valid_entries > 0 else np.nan
    stddev = float(valid.std()) if valid_entries > 0 else np.nan

    stats = {
      "total_entries": total_entries,
      "valid_entries": valid_entries,
      "underflow": underflow,
      "overflow": overflow,
      "mean": mean,
      "rms": stddev,
      "xmin": xmin,
      "xmax": xmax,
      "bins": bins,
    }

    return ax, stats
```

ROOTの`TH1クラス`を真似してヒストグラムを作ってみました。
ヒストグラムの統計情報を自動的に計算して、辞書で返す関数です。
この関数を使うと、ヒストグラムの統計情報を簡単に取得できます。

```python
# Usage
ax, stats = hbar(
    data,
    header="ヒストグラムにしたいカラム名",
    bins=ビン数,
    xmin=ヒストグラムの下限値,
    xmax=ヒストグラムの上限値,
    color="blue",
    alpha=0.7,
    title="ヒストグラム",
    xlabel="X軸のタイトル",
    ylabel="Y軸のタイトル",
)

# 統計情報を表示
print(stats)

# 統計情報を凡例に追加
ax.legend([
    f"Entries: {stats['total_entries']}",
    f"Valid Entries: {stats['valid_entries']}",
    f"Underflow: {stats['underflow']}",
    f"Overflow: {stats['overflow']}",
    f"Mean: {stats['mean']:.2f}",
    f"RMS: {stats['rms']:.2f}",
])

# グラフを表示
plt.show()
```

## リファレンス

- [pandas.DataFrame.plot.hist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html)
- [matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
- [matplotlib.axes.Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)
- [TH1 Class Reference - ROOT Documentation](https://root.cern/doc/master/classTH1.html)
