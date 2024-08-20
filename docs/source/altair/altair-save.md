# 保存する（``Chart.save``）

```python
import altair as alt

chart = alt.Chart(...)

chart.save("test.json")
chart.save("test.html")
chart.save("test.html", embed_options={"renderer": "svg"})
chart.save("test.html", inline=True)

chart.save("test.png")
chart.save("test.svg")
chart.save("test.pdf")
```

PNGなどの画像形式に出力する場合は、``vl-convert``パッケージが必要です。

## リファレンス

- [Saving Altair Charts](https://altair-viz.github.io/user_guide/saving_charts.html)
