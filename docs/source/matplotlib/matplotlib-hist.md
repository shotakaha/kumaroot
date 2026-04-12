# ヒストグラムしたい（`matplotlib.axes.Axes.hist`）

```python
import matplotlib.pyplot as plt
import numpy as np

# データを準備する
data = np.random.normal(loc=0, scale=1, size=1000)  # 平均0、標準偏差1の正規分布から1000点を生成

# キャンバスを作成
fig, ax = plt.subplots()

# ヒストグラムを作成
ax.hist(
    data,       # データ
    bins=30,    # ビンの数
    range=(-5, 5),  # 範囲
    color='blue',   # 色
    alpha=0.7,      # 透明度
)

# グラフのタイトルと軸ラベルを設定
ax.set_title("ヒストグラム")
ax.set_xlabel("値")
ax.set_ylabel("頻度")

plt.show()
```

`Axes.hist`でヒストグラムを作成できます。
データを配列で指定し、オプションでビンの数や範囲を変更できます。

## 重みをつけたい（`weights`）

```python
ax.hist(
    data,
    bins=30,
    range=(-5, 5),
    color='blue',
    alpha=0.7,
    weights=np.ones_like(data) / len(data)  # 重みを設定
)
```

`weights`オプションで、各データポイントに重みをつけることができます。
たとえば、`np.ones_like(data) / len(data)`のように設定すると、ヒストグラムが正規化され、面積が1になるようになります。

## ログ表示したい（`log`）

```python
ax.hist(
    data,
    bins=30,
    range=(-5, 5),
    color='blue',
    alpha=0.7,
    log=True,  # Y軸をログ表示
)
```

`log=True`オプションで、Y軸をログ表示にできます。
頻度の値が大きく異なる場合に、ログ表示にすることで全体の傾向を見やすくできます。

## 正規化したい（`density`）

```python
ax.hist(
    data,
    bins=30,
    range=(-5, 5),
    color='blue',
    alpha=0.7,
    density=True,  # 正規化
)
```

`density=True`オプションで、ヒストグラムを正規化できます。
正規化すると、ヒストグラムの面積が1になるように調整されます。

## 累積したい（`cumulative`）

```python
ax.hist(
    data,
    bins=30,
    range=(-5, 5),
    color='blue',
    alpha=0.7,
    cumulative=True,  # 累積
)
```

`cumulative=True`オプションで、ヒストグラムを累積できます。
累積ヒストグラムは、各ビンの値がそれまでのビンの値の合計になるように調整されます。

## 重ね書きしたい（`histtype`）

```python
ax.hist(
    [data1, data2],  # 複数のデータセット
    bins=30,
    range=(-5, 5),
    color=['blue', 'orange'],
    alpha=0.7,
    histtype='step',  # 重ね書き
)
```

`data`を複数のデータセットにすることで同時描画できます。
`histtype='step'`オプションで境界線のみを描画することで、視覚的に分かりやすくできます。

`alpha`オプションで透明度を調整することで、複数のヒストグラムを重ねて表示することもできます。

## 積み上げたい（`stacked`）

```python
ax.hist(
    [data1, data2],  # 複数のデータセット
    bins=30,
    range=(-5, 5),
    color=['blue', 'orange'],
    alpha=0.7,
    stacked=True,  # 積み上げ
)
```

`stacked=True`オプションで、複数のヒストグラムを積み上げて表示できます。
複数のデータセットをリストで指定し、色や透明度を調整することで、各データセットの寄与を視覚的にわかりすく表示できます。
