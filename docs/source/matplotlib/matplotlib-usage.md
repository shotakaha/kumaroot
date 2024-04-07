# Matplotlibの使い方

```{toctree}
---
maxdepth: 1
---
matplotlib-install
matplotlib-import
matplotlib-figure
matplotlib-subplots
matplotlib-subplot_mosaic
matplotlib-scatter
matplotlib-errorbar
```

## Explicit vs Implicit Interfaces

``Explicit interface``はオブジェクト指向的な使い方（``OO-style``）で、``axes.Axes``オブジェクトに対して設定する方法です。
``Implicit interface``はMATLAB的な使い方（``pyplot-style``）で、``pyplot``モジュールのグローバルなオブジェクト（？）に対して設定する方法です。

:::{note}

公式で推奨しているように、MATLABユーザーでないかぎり、``OO-style``を使えばよいと思います。
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
# OO-styleの基本形
import matplotlib.pyplot as plt

# データオブジェクト（辞書型 or データフレーム）
# sample_data: dict | pd.DataFrame

fig, ax = plt.subplots()
ax.scatter(
    data=sample_data,
    x="X軸のカラム名",
    y="Y軸のカラム名",
    c="マーカーの色のカラム名",
    marker="マーカーの種類")
ax.set_title("散布図のタイトル")
ax_set_xlabel("X軸のタイトル")
ax_set_ylabel("Y軸のタイトル")
```

OO-styleの基本的な形として、
[matplotlib.pyplot.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)で描画オブジェクト（``Figure``オブジェクトと``Axes``オブジェクト）を作成し、
[matplotlib.axes.Axes.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)を使ってグラフを作成&詳細設定します。

:::{hint}

``pandas.DataFrame``などのデータフレームからグラフを作成する場合に、
X軸とY軸の値を``numpy.array``などに変換しているサンプルを見かけますが、
``data``オプションでデータフレームを指定し、
X軸とY軸にカラム名を指定すればよいと思います。

:::


## ImplicitからExplicitに変換したい

```python
# Current Figure を取得する
fig = plt.gcf()

# Current Axesを取得する
ax = plt.gca()
```

``plt.gcf``や``plt.gca``で``implicit interface``で使われているグローバルオブジェクトを``explicit interface``として使えるようにできます。
