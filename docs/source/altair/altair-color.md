# 配色を変えたい

```python
alt.Chart(data).mark_bar().encode(
    alt.X("x"),
    alt.Y("y"),
    alt.Color("color").scale(scheme="カラースキーム")
)
```

``scheme``オプションを使って、グラフの配色（カラーパレット）を変更できます。
指定できる値は[VegaのColor Scheme](https://vega.github.io/vega/docs/schemes/)を参照してください。

色覚多様性に配慮した配色は
``accent``
``category20``
``category20b``
``category20c``
``set3``
