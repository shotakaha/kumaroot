# キャンバスを分割したい（``matplotlib.pyplot.subplots``）

```python
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, figsize=(4, 4))

data.plot.scatter(x="time", y="v1", ax=axs, c="blue")
data.plot.scatter(x="time", y="v2", ax=axs, c="red")
```

[plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)でキャンバスを作成できます。

## 複数に分割したい

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 3, figsize=(8, 12))
canvas = axs.ravel()  # 1次元配列に変換

data.plot.scatter(x="time", y="v1", ax=canvas[0])
data.plot.scatter(x="time", y="v2", ax=canvas[1])
data.plot.scatter(x="time", y="v3", ax=canvas[2])
data.plot.scatter(x="time", y="v4", ax=canvas[3])
data.plot.scatter(x="time", y="v5", ax=canvas[4])
data.plot.scatter(x="time", y="v6", ax=canvas[5])

fig.savefig("ファイルに保存.png")
```

[plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)の引数を指定してキャンパスを分割できます。

上のサンプルは[pandasの散布図](../pandas/pandas-plot-scatter.md)と組み合わせたものにしてみました。
**2x3**の6分割にし、6種類の散布図をそれぞれのキャンパスに描いています。

``axs``は**2x3**の2次元配列になっていますが、
``axs.ravel``を使って1次元配列に変換しています。
順番にループ処理して描画する場合は1次元配列に変換しておくと便利です。

:::{note}

``axs``を2次元配列のまま使ったサンプルです。

```python
data.plot.scatter(x="time", y="v1", ax=axs[0][0])
data.plot.scatter(x="time", y="v2", ax=axs[0][1])
data.plot.scatter(x="time", y="v3", ax=axs[0][2])
data.plot.scatter(x="time", y="v4", ax=axs[1][0])
data.plot.scatter(x="time", y="v5", ax=axs[1][1])
data.plot.scatter(x="time", y="v6", ax=axs[1][2])
```

:::



## リファレンス

- [matplotlib.pyplot.subplots - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
