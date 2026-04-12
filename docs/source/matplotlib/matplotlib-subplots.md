# キャンバスしたい（`matplotlib.pyplot.subplots`）

```python
import matplotlib.pyplot as plt

# キャンバスを作成
fig, ax = plt.subplots()

sc1 = ax.scatter(x=xdata, y=ydata)
sc2 = ax.scatter(x=xdata, y=ydata2)

# グラフのタイトルと軸ラベルを設定
ax.set_title("散布図の例")
ax.set_xlabel("X軸")
ax.set_ylabel("Y軸")

# 凡例を追加
ax.legend(
    [sc1, sc2],    # 凡例の対象
    ["データ1", "データ2"]  # 凡例のラベル
)

# キャンバスを保存
fig.savefig("scatter.png")

# グラフを表示
plt.show()
```

`pyplot.subplots`でキャンバスを作成できます。
返り値は`Figure`オブジェクトと`Axes`オブジェクトです。
`Axes`オブジェクトを使ってグラフを描画します。

```python
# MATLAB-style
plt.figure(figsize=(6, 4))
plt.scatter(x=xdata, y=ydata)
plt.title("散布図の例")
plt.xlabel("X軸")
plt.ylabel("Y軸")
plt.savefig("scatter.png")
plt.show()
```

## キャンバスサイズしたい（`figsize`）

```python
fig, ax = plt.subplots(
    figsize=(8, 6)  # 幅8インチ、高さ6インチのキャンバスを作成
)
```

`figsize`オプションで、キャンバスのサイズをインチ単位で指定できます。

## 複数に分割したい（`nrows` / `ncols`）

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(
    figsize=(8, 12),
    nrows=2,
    ncols=3,
    # squeezed=False,  # 2行3列のキャンバスを作成
)
```

`nrows`と`ncols`オプションで、キャンバスを複数に分割できます。
このときの`axs`は、行数（`nrows`）と列数（`ncols`）の
2次元配列（`ndarray`）になっています。

:::{caution}

`nrows=1`または`ncols=1`のとき、`axs`は1次元配列になります。
`squeezed=False`オプションで分割数が1のときも2次元配列になります。
後述するループ処理では、分割数に依存しないように、`squeezed=False`を指定することをオススメします。

:::

## ループ処理したい（`ravel`）

```python
# データを準備する
# 次のカラムを持つpd.DataFrameを想定
# time | v1 | v2 | v3 | v4 | v5 | v6
data = pd.DataFrame(...)

# キャンバスを分割
# fig: matplotlib.figure.Figure
# axs: np.ndarray[matplotlib.axes.Axes]
fig, axs = plt.subplots(
    nrows=2,
    ncols=3,
    figsize=(8, 12),
    squeezed=False,
)

# 2次元配列のキャンバスを1次元配列に変換
canvas = axs.ravel()

# 反復処理でグラフを描く
for i, ax in enumerate(canvas):
    data.plot.scatter(
        x="time",
        y=f"v{i+1}",
        ax=ax
    )

# キャンバスを保存
fig.savefig("waveforms.png")
```

複数のグラフをループ処理で描くサンプルです。
分割したキャンバスの戻り値は2次元配列（`np.ndarray[matplotlib.axes.Axes]`）になっています。
`squeeze=False`オプションを指定し、分割数に依らず2次元配列に変換しています。

2次元配列のままでもループ処理できますが、`ravel`（`np.ndarray.ravel`メソッド）で1次元配列に変換しておくと、アクセスが楽になります。
上のサンプルでは、[pandasの散布図](../pandas/pandas-plot-scatter.md)と組み合わせたものにしてみました。

:::{note}

同様のことは`flatten`（`np.ndarray.flatten`メソッド）でもできます。

```python
# iterator: ループ処理の中でアクセスできる
for i, ax in enumerate(axs.flatten()):
    data.plot.scatter(
        x="time",
        y=f"v{i+1}",
        ax=ax
    )
```

`flatten`はイテレーターを返すので、
`canvas = axs.ravel()`を
`canvas = axs.flatten()`
に置き換えただけではループ処理でアクセスできません。
ものすごい大量のグラフを描く時は`flatten`の方がメモリ効率がよいかもしれません。
通常は`ravel`で十分です。

:::

## リファレンス

- [matplotlib.pyplot.subplots - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
