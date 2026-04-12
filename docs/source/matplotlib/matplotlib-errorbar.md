# エラーバーしたい（`matplotlib.axes.Axes.errorbar`）

```python
import matplotlib.pyplot as plt
import numpy as np

# データを準備する
x = np.linspace(0, 10, 10)  # X軸の値
y = np.sin(x)                # Y軸の値
y_error = 0.1 * np.abs(y)    # Y軸のエラー（例：値の10%）

# キャンバスを作成
fig, ax = plt.subplots()

# エラーバー付きの散布図を作成
errors = ax.errorbar(
    x=x,
    y=y,
    yerr=y_error,
    fmt='o',  # マーカーのスタイル
    ecolor='red',  # エラーバーの色
    capsize=5,  # エラーバーのキャップのサイズ
)

# グラフのタイトルと軸ラベルを設定
ax.set_title("エラーバー付きの散布図")
ax.set_xlabel("X軸")
ax.set_ylabel("Y軸")

plt.show()
```

`Axes.errorbar`で、エラーバー付きの図を作成できます。
`xerr`と`yerr`オプションでそれぞれの方向のエラーを設定できます。
各点ごとにエラーが異なる場合は、あらかじめデータフレームで計算しておくとよいでしょう。

:::{seealso}

- [](../pandas/pandas-plot-errorbars.md)
- [](../altair/altair-errorbars.md)
- [](../plotly/plotly-errorbars.md)
- [](../hvplot/hvplot-errorbars.md)

:::

## 非対称エラーしたい（`xerr` / `yerr`）

```python
ax.errorbar(
    x=x,
    y=y,
    xerr=[0.1 * np.abs(x), 0.2 * np.abs(x)],  # X軸の非対称エラー
    yerr=[0.1 * np.abs(y), 0.2 * np.abs(y)],  # Y軸の非対称エラー
    fmt='o',
    ecolor='red',
    capsize=5,
)
```

`xerr`と`yerr`オプションで、非対称エラーを設定できます。
エラーの大きさは、リストやタプルで指定します。
たとえば、`xerr=[0.1 * np.abs(x), 0.2 * np.abs(x)]`のように、X軸のエラーの下限を値の10%、上限を値の20%に設定できます。

## リファレンス

- [matplotlib.pyplot.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)
- [matplotlib.axes.Axes.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)
- [Errorbar limit selection](https://matplotlib.org/stable/gallery/lines_bars_and_markers/errorbar_limits_simple.html)
