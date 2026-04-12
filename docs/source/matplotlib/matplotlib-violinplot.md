# バイオリン図したい（`matplotlib.axes.Axes.violinplot`）

```python
import matplotlib.pyplot as plt
import numpy as np

# データを準備する
data = [np.random.normal(loc=0, scale=1, size=100) for _ in range(4)]  # 4つのグループのデータを生成

# キャンバスを作成
fig, ax = plt.subplots()

# バイオリン図を作成
ax.violinplot(data)

# グラフのタイトルと軸ラベルを設定
ax.set_title("バイオリン図の例")
ax.set_xlabel("グループ")
ax.set_ylabel("値")
plt.show()
```

`Axes.violinplot`でバイオリン図を作成できます。
データをリストのリスト（または2次元配列）で指定します。
オプションでバイオリンのスタイルや色を変更できます。

:::{hint}

バイオリン図は、箱ひげ図と密度プロットを組み合わせたもので、データの分布を視覚化するのに役立ちます。

:::
