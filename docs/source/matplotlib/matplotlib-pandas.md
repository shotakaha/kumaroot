# `pandas`したい

```python
import matplotlib.pyplot as plt
import pandas as pd

# データを準備する
# x: X方向の検出位置
# y: Y方向の検出位置
# adc: 検出された値
data = pd.DataFrame(
  [
    {"x": 1, "y": 2, "adc": 0.5},
    {"x": 2, "y": 3, "adc": 0.7},
    {"x": 3, "y": 1, "adc": 0.2},
    # ... (さらにデータが続く)
  ]
)

# レイアウトを定義する
panels = [
    ["profile", "hist_y"],
    ["hist_x", "."],
]

# キャンバスを作成する
fig, axs = plt.subplot_mosaic(
    mosaic=panels,
    layout="constrained",
    figsize=(8, 6),
)

# 散布図: プロファイル
data.plot.scatter(
    x="x",
    y="y",
    c="adc",
    ax=axs["profile"],
    s=10,
    cmap="viridis"
)
axs["profile"].set_title("Profile")
axs["profile"].set_xlabel("X")
axs["profile"].set_ylabel("Y")

# ヒストグラム: X方向の分布
data["x"].plot.hist(
    ax=axs["hist_x"],
    bins=20,
)
axs["hist_x"].set_title("X Distribution")
axs["hist_x"].set_xlabel("X")
axs["hist_x"].set_ylabel("Frequency")

# ヒストグラム: Y方向の分布
data["y"].plot.hist(
    ax=axs["hist_y"],
    bins=20,
)
axs["hist_y"].set_title("Y Distribution")
axs["hist_y"].set_xlabel("Y")
axs["hist_y"].set_ylabel("Frequency")

# キャンバスを保存する
fig.savefig("pandas_plot.png")
```

[pd.DataFrame.plot](../pandas/pandas-plot.md)で描画したグラフは、`ax`オプションで`matplotlib`のグラフと組み合わせることができます。

上のサンプルでは、
`subplot_mosaic`を使って、プロファイルとそれぞれの方向のヒストグラムを配置しています。

:::{note}

データ分析の入門書では、`pd.DataFrame.plot`だけで描画するサンプルを多く見かけます。
`ax`オプションを使って、`matplotlib`のグラフと組み合わせることで、より柔軟にレイアウトを調整できます。

:::
