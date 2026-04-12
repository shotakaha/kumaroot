# ヒストグラムしたい（`pandas.DataFrame.plot.hist`）

```python
import pandas as pd

# データを準備する
data = pd.DataFrame(...)

# ヒストグラムを描く
data.plot.hist(
  bins=ビン数,
  xmin=ヒストグラムの下限値,
  xmax=ヒストグラムの上限値,
  title="ヒストグラム",
  xlabel="X軸のタイトル",
  ylabel="Y軸のタイトル"
)
```

`pd.DataFrame.plot.hist`でヒストグラムを作成できます。
オプションでビン数やヒストグラムの範囲、タイトルや軸のタイトルを変更できます。

`bins`オプションでビン数を変更できます。デフォルトは``10``になっています。
`xmin`、`xmax`オプションでヒストグラムの下限値と上限値を変更できます。
設定しない場合は、データの最小値と最大値が自動的に設定されます。

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

## ビニングしたい（`bins` / `xmin` / `xmax`）

```python
# 任意のビニング
bins = [0, 10, 30, 50, 70, 80]

data.plot.hist(
    bins=bins,
    xmin=0,
    xmax=100
)
```

`bins`オプションでビン数を変更できます。デフォルトは`10`になっています。
リストを指定すれば、任意の間隔でビニングできます。

`xmin`、`xmax`オプションでヒストグラムの下限値と上限値を変更できます。
設定しない場合は、データの最小値と最大値が自動的に設定されます。

`xmin`を下回るビンはアンダーフロー、`xmax`を上回るビンはオーバーフロー
として、ヒストグラムの外側に表示されます。

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
