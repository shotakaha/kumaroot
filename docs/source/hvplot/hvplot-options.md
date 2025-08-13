# オプションしたい（`.opts`）

```python
bars = data.hvplot.bar(...)
errors = data.hvplot.errorbars(...)
markers = data.hvplot.scatter(...)

# 棒グラフ（orヒストグラム）にエラーバーとデータ点を重ね書き
charts = (bars * errors * markers)

charts.opts(
    width=800,
    height=400,
    padding=0.1,
    show_grid=True,
    title="グラフのタイトル",
    xlabel="X軸のタイトル",
    ylabel="Y軸のタイトル",
)
```

`.opts`でグラフのオプションを設定できます。
グラフエリアのサイズ（`width` / `height`）や、
余白（`padding`）、グリッド表示（`show_grid`）などを一括設定できます。

グラフ全体のタイトル（`title`）や
X軸（`xlabel`）、
Y軸（`ylabel`）
のタイトルも設定できます。

:::{note}

`.opts`の正確なメソッド名は`holoviews.core.options.Optionable.opts()`です。
`hvplot`はHoloViewsのラッパーライブラリとなっているため、どのグラフオブジェクトでも`.opts()`が利用できます。

:::

## オプションを確認したい

```python
import hv
hv.help(charts)
```

## サイズを変更したい

```python
charts.opts(
    width=800,    # グラフの幅
    height=400,   # グラフの高さ
    padding=0.1,  # 余白
    margin=10,    # 余白
    aspect="equal"    # アスペクト比
)
```

## タイトルしたい

```python
charts.opts(
    title="グラフのタイトル",
    xlabel="X軸のタイトル",
    ylabel="X軸のタイトル",
    title_format="{label}"
    fontsize=12,
    fontfamily="sans-serif",
)
```

```python
charts.opts(
    fontsize={"title": 18, "labels": 12, "ticks": 10, "legend": 11},
)
```

## 軸したい

```python
charts.opts(
    show_grid=True,  # 主グリッドを表示
    grid_line_alpha=0.8,  # 主グリッドの透明度
    minor_xticks=5,  # X軸の補助目盛り
    minor_yticks=5,  # Y軸の補助目盛り
    minor_grid_line_alpha=0.3,  # 補助グリッドの透明度
    xrotation=45,    # X軸ラベルの回転角度
    yrotation=0,     # Y軸ラベルの回転角度
    xlim=(0, 100),   # X軸の範囲
    ylim=(0, 50),   # Y軸の範囲
    logx=False,    # X軸の対数スケール
    logy=False,    # Y軸の対数スケール
)
```

## 凡例したい

```python
charts.opts(
    show_legent=True,         # 凡例を表示する
    legend_position="right",  # 表示位置
    legend_offset=(10, 10)    # 表示のオフセット
)
```

## ツールバーしたい

```python
charts.opts(
    tools=["hover", "pan", "wheel_zoom"],
    toolbar="above",
    active_tools=["pan"]
)
```

## 色したい

```python
charts.opts(
    color="blue",      # 基本色
    cmap="viridis",    # カラーマップ
    alpha=0.8,         # 透明度
    line_width=2,      # 線の太さ
    line_color="red",  # 線の色
    fill_color="lightblue",  # 塗りつぶし色
)
```

## カラーマップしたい

```python
# 色名
charts.opts(cmap=["red", "blue", "green"])

# HEX値
charts.opts(cmap=["#FF0000", "#0000FF", "#00FF00"])

# RGB値
charts.opts(cmap=[(1,0,0), (0,0,1), (0,1,0)])
```

`cmap`オプションに色名のリストを指定してカスタマイズできます。
色は色名、HEX値、RGB値を利用できます。

```python
import matplotlib.pyplot as plt
print(plt.colormaps())
```

HoloViewsはmatplotlibのカラーマップをサポートしています。
`plt.colormaps`で全カラーマップを確認できます。

プリセット値として、
単色系（`Blues`、`Greens`、`Reds`、`Purples`、`Oranges`、`Greys`）、
多色系（`viridis`、`plasma`、`inferno`、`magma`、`cividis`）、
発散値向き（`RdBu`、`RdYlBu`、`RdYlGn`、`Spectral`、`coolwarm`、`seismic`）、
カテゴリ向き（`Set1`、`Set2`、`Pastel1`、`Dark2`、`tab10`、`tab20`）
などがあります。

## リファレンス

- [Customization](https://hvplot.holoviz.org/user_guide/Customization.html)
