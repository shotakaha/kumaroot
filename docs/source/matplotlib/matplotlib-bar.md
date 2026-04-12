# 棒グラフしたい（`matplotlib.axes.Axes.bar`）

```python
import matplotlib.pyplot as plt
import numpy as np

# データを準備する
categories = ['A', 'B', 'C', 'D', 'E']  # カテゴリー
values = [10, 15, 7, 12, 20]  # 各カテゴリーの値

# キャンバスを作成
fig, ax = plt.subplots()

# 棒グラフを作成
bar = ax.bar(
    categories,  # X軸のカテゴリー
    values         # Y軸の値
)

# グラフのタイトルと軸ラベルを設定
ax.set_title("棒グラフの例")
ax.set_xlabel("カテゴリー")
ax.set_ylabel("値")
plt.show()
```

`Axes.bar`で棒グラフを作成できます。
X軸のカテゴリーとY軸の値を配列で指定します。
オプションで棒の色や幅を変更できます。

:::{hint}

棒グラフとヒストグラムは形が似ていますが、
棒グラフはカテゴリーごとの値を表すのに対し、
ヒストグラムは数値データの分布を表すために使用します。

:::

## 水平の棒グラフにしたい（`Axes.barh`）

```python
ax.barh(
    categories,  # Y軸のカテゴリー
    values         # X軸の値
)
```

`Axes.barh`で水平の棒グラフを作成できます。
