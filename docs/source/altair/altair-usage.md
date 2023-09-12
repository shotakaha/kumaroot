# Altairの使い方

[Altair](https://altair-viz.github.io/)は``Pandas`` で作成したデータフレームを描画するパッケージのひとつです。
[Vega](https://vega.github.io/vega/)と[Vega-Lite](https://vega.github.io/vega-lite/)という（たぶん）JavaScriptベースの描画パッケージを、Pythonでも使えるようにしたものです。

データフレームを読み込んだ``alt.Chart``オブジェクトに対して、``.mark_*``でプロットの種類、``.encode``でデータ点、``.properties``でプロットのタイトルなどを設定するという感じで作業が抽象化されています。

Altairにもデータを集計する機能がありますが、基本は``Pandas``で前処理は完了させておくのがよいと思います。

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
altair-datetime
altair-color
```
