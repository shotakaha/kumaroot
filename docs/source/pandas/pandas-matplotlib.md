# 詳細設定したい（``import matplotlib.pyplot as plt``）

```python
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを用意する（ここでは省略）
# data: pd.DataFrame

# matplotlib.pyplotで FigureとAxesオブジェクトを作成する
fig, axs = plt.subplots()

# pandasでプロットを作成する
data.plot(
    kind="scatter",
    x="X軸のカラム名",
    y="Y軸のカラム名",
    ax=axs  # 描画先のAxesオブジェクトを指定する
    )
```

グラフの詳細設定したい場合は、[matplotlib.pyplot.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html)を使います。

[pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)の``ax``オプションで、``matplotlib``の``Axes``オブジェクトを指定できます。

:::{seealso}

``matplotlib``の使い方は、まず、公式ドキュメントの[The lifecycle of a plot](https://matplotlib.org/stable/tutorials/lifecycle.html)に目を通すのがよいと思います。
とくに[A note on the explicit vs implicit interfaces](https://matplotlib.org/stable/tutorials/lifecycle.html#a-note-on-the-explicit-vs-implicit-interfaces)は、ウェブに転がっている他のコードを読むのに役立つ情報だと思います。

:::
