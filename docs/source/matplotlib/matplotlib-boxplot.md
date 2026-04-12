# 箱ひげ図したい（`matplotlib.axes.Axes.boxplot`）

```python
import matplotlib.pyplot as plt
import numpy as np

# データを準備する
data = [np.random.normal(loc=0, scale=1, size=100) for _ in range(4)]  # 4つのグループのデータを生成

# キャンバスを作成
fig, ax = plt.subplots()

# 箱ひげ図を作成
ax.boxplot(data)

# グラフのタイトルと軸ラベルを設定
ax.set_title("箱ひげ図の例")
ax.set_xlabel("グループ")
ax.set_ylabel("値")
plt.show()
```

`Axes.boxplot`で箱ひげ図を作成できます。
データをリストのリスト（または2次元配列）で指定します。
オプションで箱のスタイルや色を変更できます。
