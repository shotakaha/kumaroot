# キャンバスを割付したい（`matplotlib.pyplot.subplot_mosaic`）

```python
import matplotlib.pyplot as plt

# キャンバスの割付を設定する
# +-------+---+
# |   A   |   |
# |-------| B |
# | C | D |   |
# +---+---+---+
# |     E     |
# +-----------+

# 結合するキャンバスは同じ名前にする
panels = [
    ["A", "A", "B"],
    ["C", "D", "B"],
    ["E", "E", "E"],
]

# キャンバスを作成する
# fig: matplotlib.figure.Figure
# axs: dict[str, matplotlib.axes.Axes]
fig, axs = plt.subplot_mosaic(
    mosaic=panels,    # 割付を指定
    layout="constrained",  # レイアウト調整
    figsize=(8, 6),   # 縦長のキャンバスを作成
)

# 割付した名前を使ってAxesオブジェクトを取り出す
axs["A"].set_title("Panel A")
axs["B"].set_title("Panel B")
axs["C"].set_title("Panel C")
axs["D"].set_title("Panel D")
axs["E"].set_title("Panel E")

# キャンバスを保存
fig.savefig("subplot_mosaic.png", dpi=300)  # 解像度を上げて保存
```

`pyplot.subplot_mosaic`を使って、複雑に分割したキャンバスを作成できます。
戻り値は、辞書型となっていて、Axesオブジェクトキーで取得できます。

:::{note}

``mosaic``はモザイク処理ではなく、タイルのことを指しているのだと思います。

:::

## 論文したい

```python
# +----------------+------+
# |      main      |      |
# |----------------+ cbar |
# |  sub1  | sub2  |      |
# +----------------+------+

import matplotlib.pyplot as plt
import numpy as np

# レイアウトを設定する
# セマンティクスを考慮して、名前をつけるとわかりやすい
# main: メインのグラフ
# cbar: カラーバー
# sub1, sub2: サブのグラフ
panels = [
    ["main", "main", "cbar"],
    ["sub1", "sub2", "cbar"],
]

# キャンバスを作成する
fig, axs = plt.subplot_mosaic(
    panels,
    figsize=(10, 6),
    layout="constrained",
    gridspec_kw={"width_ratios": [1, 1, 0.05]},  # 列の幅を指定
)

# main: メインのグラフを描く
axs["main"].plot(x, y)
axs["main"].set_title("Main Result")
axs["main"].set_xlabel("X-axis")
axs["main"].set_ylabel("Y-axis")

# sub1: サブのグラフを描く
axs["sub1"].scatter(x, y1, s=10)
axs["sub1"].set_title("Sub Plot 1")
axs["sub1"].set_xlabel("X-axis")
axs["sub1"].set_ylabel("Y-axis")

# sub2: サブのグラフを描く
axs["sub2"].scatter(x, y2, s=10)
axs["sub2"].set_title("Sub Plot 2")
axs["sub2"].set_xlabel("X-axis")
axs["sub2"].set_ylabel("Y-axis")

# cbar: カラーバーを描く
sm = plt.cm.ScalarMappable(cmap="viridis")
sm.set_array([])  # カラーバーの範囲を設定
fig.colorbar(
    sm,
    cax=axs["cbar"],
    orientation="vertical",
    label="Colorbar"
)

# キャンバスを保存する
fig.savefig("subplot_mosaic_paper.png", dpi=300)
```

論文などで利用することを想定したサンプルです。
メインのグラフとサブのグラフを分割して、カラーバーを配置しています。
`gridspec_kw`オプションで、列の幅を指定しています。

## ダッシュボードしたい

```python
# +----------------+----------------+
# |     panel1     |     panel2     |
# |----------------+----------------|
# |     panel3     |     panel4     |
# +----------------+----------------+

import matplotlib.pyplot as plt
import numpy as np

# レイアウトを設定する
panels = [
    ["panel1", "panel2"],
    ["panel3", "panel4"],
]

# キャンバスを作成する
fig, axs = plt.subplot_mosaic(
    panels,
    figsize=(12, 8),
    layout="constrained",
)

# panel1: グラフを描く
axs["panel1"].plot(x, y)
axs["panel1"].set_title("Panel 1")
axs["panel1"].set_xlabel("X-axis")
axs["panel1"].set_ylabel("Y-axis")

# panel2: グラフを描く
axs["panel2"].scatter(x, y1, s=10)
axs["panel2"].set_title("Panel 2")
axs["panel2"].set_xlabel("X-axis")
axs["panel2"].set_ylabel("Y-axis")

# panel3: グラフを描く
axs["panel3"].scatter(x, y2, s=10)
axs["panel3"].set_title("Panel 3")
axs["panel3"].set_xlabel("X-axis")
axs["panel3"].set_ylabel("Y-axis")

# panel4: グラフを描く
axs["panel4"].scatter(x, y3, s=10)
axs["panel4"].set_title("Panel 4")
axs["panel4"].set_xlabel("X-axis")
axs["panel4"].set_ylabel("Y-axis")

# キャンバスを保存する
fig.savefig("subplot_mosaic_dashboard.png", dpi=300)
```

ダッシュボードなどで利用することを想定したサンプルです。
4つのグラフを分割して配置しています。

:::{note}

リアルタイムで更新するダッシュボードを作る場合は、`matplotlib.animation`モジュールと組み合わせて利用します。

:::
