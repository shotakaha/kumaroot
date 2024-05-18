# 重ね書きしたい（``alt.layer``）

```python
hbars = alt.Chart(data).mark_bar().encode(x="time", y="events")
marks = alt.Chart(data).mark_point().encode(x="time", y="temperature")
hbars + marks
```

`+`演算子を使って、同じX軸を持つ``alt.Chart``オブジェクトをひとつのレイヤーに重ね書きできます。
サンプルでは、時系列データのイベント数（``hbars``）と気温（``marks``）を表示しています。

## テキストを重ねたい

```python
base = alt.Chart(data).encode(
    alt.X("x").title("X軸"),
    alt.Y("y").title("Y軸"),
)

mark = base.mark_bar()

text = base.mark_text().encode(
    alt.Text("y")
)

# mark + text
alt.layer(
    mark,
    text
)
```

``+``演算子は``alt.layer``のエイリアスです。
このサンプルでは、あるデータのヒストグラム（``mark``）に、その時のエントリー数（``text``）を重ねて表示しています。

## 2軸グラフしたい

```python
base = alt.Chart(data).encode(
    alt.X("time").title("測定時刻")
)

mark1 = base.mark_bar().encode(
    alt.Y("event_rate").title("イベントレート [Hz]").scale(domain=[0, 5]),
)

mark2 = base.mark_point().encode(
    alt.Y("tmpC").title("気温 [℃]").scale(domain=[20, 30]),
)

alt.layer(
    mark1,
    mark2,
).resolve_scale(
    y="independent",
)
```

``resolve_scale``を使って、[2軸グラフ](https://altair-viz.github.io/gallery/layered_chart_with_dual_axis.html)を作成できます。
サンプルではイベントレートと気温の時間変化を同じグラフに表示しています。
それぞれの軸の長さは``alt.Scale``で調整できます。

## リファレンス

- [Layered and Multi-View Charts](https://altair-viz.github.io/user_guide/compound_charts.html)
- [Bar Chart with Line on Dual Axis](https://altair-viz.github.io/gallery/bar_and_line_with_dual_axis.html)
- [Layered chart with Dual-Axis](https://altair-viz.github.io/gallery/layered_chart_with_dual_axis.html)
