# ヒートマップしたい（`matplotlib.axes.Axes.imshow`）

```python
import numpy as np
import matplotlib.pyplot as plt

# データを準備する
x = np.linspace(0, 10, 100)  # 0から10までの100点を生成
y = np.linspace(0, 10, 100)  # 0から10までの100点を生成
X, Y = np.meshgrid(x, y)     # グリッドを作成
Z = np.sin(X) * np.cos(Y)    # ZはXとYの関数（例：sin(X)*cos(Y)）
data = Z  # 2次元配列

# Figureエリアを作成
fig, ax = plt.subplots()

# ヒートマップ
hm = ax.imshow(
    data,    # 2次元配列
    cmap="viridis",
    vmin=0,
    vmax=1,
)

# カラーバーを追加
fig.colorbar(hm, ax=ax)
plt.show()
```

`imshow`メソッドでヒートマップを作成できます。
2次元配列を渡すと、値の大きさに応じて色が変わるヒートマップが描画されます。
オプションでカラーマップを変更できます。

:::{note}

`imshow`はもともと画像を表示するためのメソッドですが、数値データを色で表現するヒートマップとしてもよく使われます。

:::
