# キャンバスしたい（``matplotlib.pyplot.figure``）

```python
import matplotlib.pyplot as plt

fig = plt.figure()
fig = plt.figure()
ax2 = fig.add_subplot(2, 3, 1)
ax4 = fig.add_subplot(nrows=2, ncols=3, index=4)
ax6 = fig.add_subplot(pos=236)
```

[matplotlib.pyplot.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)で``Figure``オブジェクトを作成し、
[matplotlib.pyplot.add_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)で``Axes``オブジェクトを追加します。
位置引数として``（行の数, 列の数, 場所）``の``tuple``を指定したり、それをまとめて``pos``で指定したりできます。
