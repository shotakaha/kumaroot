# 円グラフしたい（`matplotlib.axes.Axes.pie`）

```python
import matplotlib.pyplot as plt

# データを準備する
labels = ["A", "B", "C", "D"]  # ラベル
sizes = [15, 30, 45, 10]        # 各セクションのサイズ
colors = ["red", "green", "blue", "yellow"]  # 色

# キャンバスを作成
fig, ax = plt.subplots()

# 円グラフを作成
ax.pie(
    sizes,       # 各セクションのサイズ
    labels=labels,  # ラベル
    colors=colors,  # 色
    autopct="%1.1f%%",  # パーセンテージを表示
    startangle=90,  # 開始角度
)

# グラフのタイトルを設定
ax.set_title("円グラフの例")
plt.show()
```

`Axes.pie`で円グラフを作成できます。
データを配列で指定し、オプションでラベルや色、パーセンテージの表示方法を変更できます。
