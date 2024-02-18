# 見た目したい（``import matplotlib.pyplot as plt``）

```python
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
```

グラフの見た目を整えたい場合、[matplotlib](https://matplotlib.org)についても簡単に知っておく必要があります。
まず、公式ドキュメントの[The lifecycle of a plot](https://matplotlib.org/stable/tutorials/lifecycle.html)に目を通すのがよいと思います。
とくに[A note on the explicit vs implicit interfaces](https://matplotlib.org/stable/tutorials/lifecycle.html#a-note-on-the-explicit-vs-implicit-interfaces)は、ウェブに転がっている他のコードを読むのに役立つ情報だと思います。

## Explicit vs Implicit Interfaces

``Explicit interface``はオブジェクト指向的な使い方で、``axes.Axes``オブジェクトに対して設定する方法です。
``Implicit interface``はMATLAB的な使い方で、``pyplot``モジュールのグローバルなオブジェクト（？）に対して設定する方法です。

:::{note}

公式でも推奨しているように、MATLABユーザーでないかぎり、``explicit interface``を使うのがよいと思います。
また、意図せずに混合して使うのは避けた方がよいと思います。

:::

## Axes and Figure

``matplotlib``の用語として把握しておくべきなのは``Axes``と``Figure``です。
``Axes``は独立した図オブジェクト単体を指します。
``Figure``は最終的に保存する描画オブジェクトを指し、複数の``Axes``オブジェクトを含むことができます。

``Figure``オブジェクトの構成要素は
[Parts of a Figure](https://matplotlib.org/stable/users/explain/quick_start.html#parts-of-a-figure)の図と説明を参照してください。

:::{hint}

ROOTを使ってるひとは、
``Figure``オブジェクトは``TCanvas``オブジェクト相当、
``Axes``オブジェクトは``TCanvas::Divide``したエリア相当、
とイメージするとよいと思います。

:::

```python
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

fig, axes = plt.subplots(2, 3)
```

```python
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlob

fig = plt.Figure()
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)
```

## ImplicitからExplicitに変換したい

```python
# Current Figure を取得する
fig = plt.gcf()

# Current Axesを取得する
ax = plt.gca()
```

``plt.gcf``や``plt.gca``で``implicit interface``で使われているグローバルオブジェクトを``explicit interface``として使えるようにできます。
