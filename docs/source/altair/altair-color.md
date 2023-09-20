# 配色を変えたい（``alt.Scale``）

```python
alt.Chart(data).mark_bar().encode(
    alt.X("x"),
    alt.Y("y"),
    alt.Color("color").scale(scheme="カラースキーム")
)
```

[altair.Scale](https://altair-viz.github.io/user_guide/generated/core/altair.Scale.html)を使って、スケール（軸の目盛り系？）を設定できます。
``scheme``オプションで、グラフの配色（カラーパレット）を変更できます。
指定できる値は[Color Schemes - Vega](https://vega.github.io/vega/docs/schemes/)を参照してください。

色覚多様性に配慮した配色は

1. ``accent``
2. ``category20``
3. ``category20b``
4. ``category20c``
5. ``set3``
