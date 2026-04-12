# キャンバスしたい（`matplotlib.figure.Figure`）

```python
import matplotlib.pyplot as plt

fig = plt.figure(
  figsize=(6, 4),
  dpi=150,
  layout="constrained",
  facecolor="white",
)
```

`figure.Figure`（=`pyplot.figure`）でキャンバスを作成できます。
`figure`は、グラフ全体を表すオブジェクトで、複数のグラフを描くときの土台になります。

:::{hint}

不正確な部分がありますが、`matplotlib`の構成要素は以下のようになっています。

```tree
Figure: キャンバス全体
|-- Axes: グラフ領域
    |-- Axis: 軸
    |   |-- Tick: 目盛り
    |   |   |-- Line2D: 目盛り線
    |   |   |-- Line2D: グリッド線
    |   |   |-- Text: 目盛りラベル
    |   |-- Label: 軸ラベル
    |-- Line2D: 線
    |-- PathCollection: 散布図の点
    |-- Patch: 図形
    |-- Text: テキスト
    |   |-- Title: タイトル
    |-- Legend: 凡例
```

`Figure`と`Axes`の関係を理解することが重要です。

:::

## 分割したい（`add_subplot`）

```python
# キャンバスを作成
fig = plt.figure(figsize=(8, 6))

ax1 = fig.add_subplot(2, 3, 1)    # index=1
ax4 = fig.add_subplot(nrows=2, ncols=3, index=4)
ax6 = fig.add_subplot(pos=236)    # index=6
```

`add_subplot`メソッドで、キャンバスを分割して複数のグラフを描くことができます。

位置引数には`(行の数, 列の数, 場所)`を`tuple`で指定したり、
それをまとめて`pos`で指定したりできます。

:::{seealso}

- [](./matplotlib-subplots.md)
- [](./matplotlib-subplot_mosaic.md)

個人的には`figure`より`subplots`を使う方法がオススメです。
`figure`のオプションは`subplots`でも使えます。

:::

## 保存したい（`savefig`）

```python
fig.savefig("figure.png")
```

`savefig`メソッドでキャンパスを保存できます。

:::{note}

`plt.savefig`メソッドも存在します。
`plt.savefig`はMATLAB風のAPIで、現在アクティブなFigureを保存します。
`fig.savefig`はオブジェクト指向APIで、よりPythonicです。

:::

## サイズを変更したい（``figsize``）

```python
fig = plt.figure(figsize=(4, 3))
```

`figsize`オプションでキャンバス全体のサイズを変更できます。
単位はインチです。
デフォルトは``figsize=(6.4, 4.8)``です。

:::{note}

単位はインチですが、実際の大きさは気にせず、
アスペクト比を指定するくらいの気持ちで使っています。

解像度が不足している場合は、``dpi``オプションで変更すればよいと思います。
デフォルトは``dpi=100``です。

:::

## レイアウトしたい（`layout`）

```python
fig = plt.figure(layout="constrained")  # 自動で重なりを回避（recommended）
fig = plt.figure(layout="compressed")  # constrainedより詰める
fig = plt.figure(layout="tight")    # さらに詰める
fig = plt.figure(layout="none")    # 自動調整なし
```

`layout`オプションで、キャンバス内のレイアウトをよしなに設定できます。
デフォルトは`layout=None`です。

ひとつのキャンバスに複数の図を描くと、タイトルや軸タイトルが重なってしまうことがあります。
そのようなときは`layout="constrained"`オプションをつけるとよいです。
余白の大きさをもっと詰めたい場合は、好みに応じて`compressed`、`tight`を選択してください。

## 解像度したい（`dpi`）

```python
fig = plt.figure(dpi=200)
```

`dpi`オプションで画像の解像度を変更できます。
論文や資料用には200〜300、
画面表示用には100（デフォルト）が目安です。

## 背景色したい（`facecolor` / `edgecolor`）

```python
fig = plt.figure(facecolor="lightgray")
```

`facecolor`オプションで、キャンバス全体の背景色を変更できます。

## フレームしたい（`frameon`）

```python
fig = plt.figure(frameon=false)
```

`frameon`オプションで、キャンバスの枠線を変更できます。
`frameon=false`で枠を非表示にできます。





## リファレンス

- [matplotlib.pyplot.figure - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
- [matplotlib.pyplot.add_subplot - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
