# エラーバーしたい（``matplotlib.pyplot.errorbar``）

```python
import matplotlib.pyplot as plt

x_data = data["x"]
y_data = data["y"]
y_error = data["y_error"]

fig, ax = plt.subplots()
ax.errorbar(
    x=x_data,
    y=y_data,
    yerr=y_error,
    )

plt.show()
```

[Axes.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)で、エラーバー付の散布図を作成できます。
エラーの大きさ``xerr``、``yerr``オプションで設定できます。
大きさはあらかじめデータフレームで計算しておくとよいでしょう。

:::{seealso}

- [](../pandas/pandas-plot-errorbars.md)
- [](../altair/altair-errorbars.md)
- [](../plotly/plotly-errorbars.md)
- [](../hvplot/hvplot-errorbars.md)

:::

## リファレンス

- [matplotlib.pyplot.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)
- [matplotlib.axes.Axes.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)
- [Errorbar limit selection](https://matplotlib.org/stable/gallery/lines_bars_and_markers/errorbar_limits_simple.html)
