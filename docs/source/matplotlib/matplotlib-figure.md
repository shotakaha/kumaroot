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

:::

## リファレンス

- [matplotlib.pyplot.figure - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
- [matplotlib.pyplot.add_subplot - matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
