# 折れ線したい（`matplotlib.axes.Axes.plot`）

```python
import numpy as np
import matplotlib.pyplot as plt

# データを準備する
x = np.linspace(0, 10, 100)  # 0から10までの100点を生成
y = np.sin(x)                # Y軸の値
data = list(zip(x, y))       # データをタプルのリストとして準備

# キャンバスを作成
fig, ax = plt.subplots()

# 折れ線グラフを作成
lines =ax.plot(
    x, y,  # X軸とY軸の値を指定
    label="sin(x)",  # 凡例に使う名前
)

# グラフのタイトルと軸ラベルを設定
ax.set_title("折れ線グラフの例")
ax.set_xlabel("X軸")
ax.set_ylabel("Y軸")
ax.legend()  # 凡例を表示
plt.show()
```

`Axes.plot`で折れ線グラフを作成できます。
X軸とY軸の値を配列で指定します。
オプションで線のスタイルや色を変更できます。
