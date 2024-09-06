# 描画パッケージを切り替えたい（``hvplot.extension``）

```python
import hvplot.pandas

hvplot.extension("bokeh")
hvplot.extension("matploblib")
hvplot.extension("plotly")

hvplot.extension("plotly", "matploblib")
```

``hvplot.extension``で描画ライブラリを変更できます。
デフォルトは``Bokeh``です。

Colaboratoryは`bokeh`バックエンドで表示できませんでしたが、
`matplotlib`に変更したらOKでした。

## リファレンス

- [Plotting Extensions - hvplot.holoviz.org](https://hvplot.holoviz.org/user_guide/Plotting_Extensions.html)
