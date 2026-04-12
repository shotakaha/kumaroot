# Altairの使い方

[Altair](https://altair-viz.github.io/)はPythonでグラフを描くためのライブラリのひとつです。
`Pandas`で作成したデータフレームも描画できます。

データフレームを`alt.Chart`オブジェクトに変換して、プロットの種類（`.mark_*`）やデータ点（`.encode`）、タイトルなどを設定（`.properties`）するという構成になっています。
`matplotlib`に比べて作業が抽象化されていて、宣言的に記述できるのが特徴です。

`Altair`本体にもデータを集計する機能がありますが、基本は`Pandas`で前処理は完了させておくのがよいと思います。

:::{note}

`Altair`は、[Vega-Lite](https://vega.github.io/vega-lite/)というJavaScriptでグラフを描くためのパッケージを、Pythonでも使えるようにしたものです。

:::

```{toctree}
---
maxdepth: 1
---
altair-install
altair-mark
altair-encode
altair-histogram
altair-heatmap
altair-pie
altair-layer
altair-hconcat
altair-vconcat
altair-datetime
altair-color
altair-errorbars
altair-scatter
altair-save
```
