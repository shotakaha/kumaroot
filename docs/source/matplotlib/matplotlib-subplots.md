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

plt.show()
```

`pyplot.subplots`でキャンバスを作成できます。
返り値は`Figure`オブジェクトと`Axes`オブジェクトです。
`Axes`オブジェクトを使ってグラフを描画します。

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

)
```

`nrows`と`ncols`オプションで、キャンバスを複数に分割できます。
分割したキャンバスの戻り値は、行数と列数に応じた2次元配列になります。

## ループ処理したい（`ravel`）

```python
# データを準備する
# 次のカラムを持つpd.DataFrameを想定
# time | v1 | v2 | v3 | v4 | v5 | v6
data = pd.DataFrame(...)

# キャンバスを分割
fig, axs = plt.subplots(
    nrows=2,
    ncols=3,
    figsize=(8, 12),
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
分割したキャンバスの戻り値は2次元配列になっています。
このままでは、アクセスが面倒なので、`ravel`メソッドで1次元配列に変換しています。

上のサンプルでは、[pandasの散布図](../pandas/pandas-plot-scatter.md)と組み合わせたものにしてみました。

分割数が分からなくても、グラフが描けるようになっています。

## リファレンス

- [matplotlib.pyplot.subplots - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
