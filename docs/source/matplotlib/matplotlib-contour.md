# 等高線したい（`matplotlib.axes.Axes.contour`）

```python
import numpy as np
import matplotlib.pyplot as plt

# データを準備する
x = np.linspace(0, 10, 100)  # 0から10までの100点を生成
y = np.linspace(0, 10, 100)  # 0から10までの100点を生成
X, Y = np.meshgrid(x, y)     # グリッドを作成
Z = np.sin(X) * np.cos(Y)    # ZはXとYの関数（例：sin(X)*cos(Y)）
data = Z  # 2次元配列

# キャンバスを作成
fig, ax = plt.subplots()

# 等高線を作成
contour = ax.contour(
    X, Y, data,  # X、Y、Zの値を指定
    levels=10,   # 等高線のレベル数
    cmap="viridis",  # カラーマップ
)

# カラーバーを追加
fig.colorbar(contour, ax=ax)
plt.show()
```

`Axes.contour`で等高線を作成できます。
X、Y、Zの値を指定し、オプションで等高線のレベル数やカラーマップを変更できます。
