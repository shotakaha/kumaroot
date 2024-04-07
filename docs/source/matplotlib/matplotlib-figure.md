# キャンバスしたい（``matplotlib.pyplot.figure``）

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax2 = fig.add_subplot(2, 3, 1)    # index=2
ax4 = fig.add_subplot(nrows=2, ncols=3, index=4)
ax6 = fig.add_subplot(pos=236)    # index=6
```

[plot.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)で``Figure``オブジェクトを作成し、
[plot.add_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)で分割キャンバス（``Axes``オブジェクト）を追加します。

位置引数に``（行の数, 列の数, 場所）``の``tuple``を指定したり、それをまとめて``pos``で指定したりできます。

:::{seealso}

- [](./matplotlib-subplots.md)
- [](./matplotlib-subplot_mosaic.md)

個人的には``figure``より``subplots``を使う方法がオススメです。
``figure``のオプションは``subplots``でも使えます。

:::

## サイズを変更したい（``figsize``）

```python
fig = plt.figure(figsize=(4, 3))
```

``figsize``でキャンバス全体のサイズを変更できます。
単位はインチです。
デフォルトは``figsize=[6.4, 4,8]``です。

:::{note}

単位はインチですが、実際の大きさは気にせず、
アスペクト比を指定するくらいの気持ちで使っています。

解像度が不足している場合は、``dpi``オプションで変更すればよいと思います。
デフォルトは``dpi=100``です。

:::

## レイアウトしたい（``layout``）

```python
fig = plt.figure(layout="constrained")
fig = plt.figure(layout="compressed")
fig = plt.figure(layout="tight")
fig = plt.figure(layout="none")
```

``layout``オプションで、キャンバス内のレイアウトをよしなに設定できます。
デフォルトは``layout=None``です。

ひとつのキャンバスに複数の図を描くと、タイトルや軸タイトルが重なってしまうことがあります。
そのようなときは``layout="constrained"``オプションをつけるとよいです。
余白の大きさをもっと詰めたい場合は、好みに応じて``compressed``、``tight``を選択してください。

## リファレンス

- [matplotlib.pyplot.figure - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
- [matplotlib.pyplot.add_subplot - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
