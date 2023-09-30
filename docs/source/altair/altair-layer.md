# 重ね書きしたい（``alt.layer``）

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

``alt.layer``を使って、複数のグラフを重ね書きできます。
``alt.layer``は``+``演算子で代替できます。
サンプルでは、ヒストグラム（``mark_bar``）にエントリー数をテキスト（``mark_text``）表示しています。

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
