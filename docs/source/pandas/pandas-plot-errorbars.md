# エラーバーしたい（`pandas.DataFrame.plot`）

```python
import pandas as pd
import matplotlib.pyplot as plt

# データを準備する
data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [2, 3, 5, 7, 11],
    "xerr": [0.1, 0.2, 0.1, 0.3, 0.2],
    "yerr": [0.2, 0.3, 0.2, 0.4, 0.3],
});

# 散布図を描く
# ax: matplotlib.axes.Axes
ax = data.plot.scatter(
    x="x",
    y="y",
)

# エラーバーを描く
ax.errorbar(
    x=data["x"],
    y=data["y"],
    xerr=data["xerr"],
    yerr=data["yerr"],
    fmt='o',  # マーカーのスタイル
    capsize=3,
)

# グラフのタイトルと軸ラベルを設定
ax.set_title("エラーバー付きの散布図")
ax.set_xlabel("X軸")
ax.set_ylabel("Y軸")

# グラフを表示
plt.show()
```

`pd.DataFrame.plot`単体ではエラーバーを描くことができません。
そのため`pd.DataFrame.plot.scatter`で散布図を描いた後に、`Axes.errorbar`でエラーバーを描きます。

:::{seealso}

- [](../altair/altair-errorbars.md)
- [](../hvplot/hvplot-errorbars.md)
- [](../plotly/plotly-errorbars.md)
- [](../matplotlib/matplotlib-errorbar.md)

:::
